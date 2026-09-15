/** Exact U73 arithmetic. Digit lifting and real cyclotomic trace recurrence. */
export {};
const assert: (ok: boolean, message: string) => asserts ok = (ok, message) => {
  if (!ok) throw new Error(message);
};
type Vector = readonly bigint[];
const mod = (a: bigint, n: bigint): bigint => ((a % n) + n) % n;
function scalarPower(a: bigint, e: number, n: bigint): bigint {
  assert(Number.isSafeInteger(e) && e >= 0, 'Invalid exponent');
  let out = 1n; let b = mod(a, n);
  while (e) { if (e % 2) out = out*b % n; b = b*b % n; e = Math.floor(e/2); }
  return out;
}
function inverse(a: bigint, n: bigint): bigint {
  let r = n; let s = mod(a, n); let x = 0n; let y = 1n;
  while (s !== 0n) { const q = r/s; [r,s] = [s,r-q*s]; [x,y] = [y,x-q*y]; }
  assert(r === 1n, 'Attempt to invert a nonunit'); return mod(x,n);
}
function multiply(a: Vector, b: Vector, n: bigint): bigint[] {
  assert(a.length === b.length && (a.length === 10 || a.length === 20), 'Wrong ring rank');
  const d = a.length/10; const out = Array<bigint>(a.length).fill(0n);
  for (let i=0;i<a.length;i++) for (let j=0;j<b.length;j++) {
    if (a[i]===0n || b[j]===0n) continue;
    const ci=Math.floor(i/d), cj=Math.floor(j/d), pp=i%d+j%d;
    const index=((ci+cj)%10)*d;
    const coefficient=a[i]!*b[j]!*(ci+cj>=10?-256n:1n);
    // phi^2=phi+1. In rank ten there is no phi coordinate.
    if (pp===2) { out[index]=out[index]!+coefficient; out[index+1]=out[index+1]!+coefficient; }
    else out[index+pp]=out[index+pp]!+coefficient;
  }
  return out.map(x=>mod(x,n));
}
function power(a: Vector, e: number, n: bigint): bigint[] {
  let b=[...a]; let out=[1n,...Array<bigint>(a.length-1).fill(0n)];
  while(e) { if(e%2)out=multiply(out,b,n); b=multiply(b,b,n); e=Math.floor(e/2); }
  return out;
}
function add(a: Vector, b: Vector, n: bigint, factor=1n): bigint[] {
  assert(a.length===b.length,'Addition rank mismatch');
  return a.map((x,i)=>mod(x+factor*b[i]!,n));
}
function embed(a: Vector): bigint[] { return a.flatMap(x=>[x,0n]); }
function conjugatePhi(a: Vector,n: bigint): bigint[] {
  assert(a.length===20,'Not a quadratic vector');
  return Array.from({length:10},(_,j)=>[mod(a[2*j]!+a[2*j+1]!,n),mod(-a[2*j+1]!,n)]).flat();
}
function valuation(x: bigint): number {
  assert(x!==0n,'Zero valuation needs a precision bound'); let v=0;
  while(x%17n===0n){x/=17n;v++;} return v;
}
function rootByDigits(a: bigint,y: bigint,precision: number): bigint[] {
  const x=a**17n; let theta=[a,...Array<bigint>(9).fill(0n)];
  const derivativeInverse=inverse(scalarPower(a,16,17n),17n);
  for(let k=2;k<=precision;k++) {
    const digit=17n**BigInt(k), m=digit*17n;
    const image=power(theta,17,m), target=[mod(x,m),mod(y,m),...Array<bigint>(8).fill(0n)];
    const error=add(target,image,m,-1n);
    assert(error.every(z=>z%digit===0n),'Root did not reach the claimed precision');
    theta=theta.map((z,j)=>mod(z+(digit/17n)*mod(error[j]!/digit*derivativeInverse,17n),digit));
    assert(power(theta,17,m).join(',')===target.join(','),'Incorrect lifted digit');
  }
  return theta;
}
function inverseLinear(x: bigint,y: bigint,n: bigint): bigint[] {
  const a=mod(y*inverse(x,n),n); const d=mod(1n+256n*scalarPower(a,10,n),n);
  const scale=inverse(x*d,n);
  return Array.from({length:10},(_,j)=>mod(scale*scalarPower(-a,j,n),n));
}
// S_j=zeta^j+zeta^-j, in the independent basis (1,phi). No rank-40 algebra.
function traces(n: bigint): bigint[][] {
  const s:bigint[][]=[[2n,0n],[-1n,1n]];
  for(let k=2;k<=9;k++) {
    const prev=s[k-1]!, before=s[k-2]!;
    // (-1+phi)*(a+b*phi) = -a+b + a*phi.
    s.push([mod(-prev[0]!+prev[1]!-before[0]!,n), mod(prev[0]!-before[1]!,n)]);
  }
  assert(s[5]!.join(',')==='2,0','Trace recurrence is not periodic');
  return s;
}
function pairNorm(theta: Vector,n: bigint): bigint[] {
  const tr=traces(n), out=Array<bigint>(20).fill(0n);
  for(let i=0;i<10;i++) for(let j=i;j<10;j++) {
    const k=(i+j)%10, weight=theta[i]!*theta[j]!*(i+j>=10?-256n:1n);
    const z=i===j?[1n,0n]:tr[j-i]!;
    out[2*k]=out[2*k]!+weight*z[0]!;
    out[2*k+1]=out[2*k+1]!+weight*z[1]!;
  }
  return out.map(x=>mod(x,n));
}
function example(scalarRoot: number,y: bigint,precision: number) {
  const a=BigInt(scalarRoot),x=a**17n,n=17n**BigInt(precision);
  const theta=rootByDigits(a,y,precision), tauInverse=inverseLinear(x,y,n);
  const thetaInverse=multiply(power(theta,16,n),tauInverse,n);
  assert(multiply(theta,thetaInverse,n).join(',')==='1,0,0,0,0,0,0,0,0,0','Root inverse');
  const U=multiply(pairNorm(theta,n),embed(multiply(thetaInverse,thetaInverse,n)),n);
  const V=multiply([x,-y,...Array<bigint>(8).fill(0n)],tauInverse,n);
  const thetaBar=theta.map((z,j)=>mod(j%2?-z:z,n));
  const R=multiply(thetaBar,thetaInverse,n);
  assert(power(R,17,n).join(',')===V.join(','),'Missing seventeenth-power condition');
  const Vbar=V.map((z,j)=>mod(j%2?-z:z,n));
  assert(multiply(V,Vbar,n).join(',')==='1,0,0,0,0,0,0,0,0,0','Norm-one condition');
  const lhs=multiply([3n,-1n,...Array<bigint>(18).fill(0n)],power(embed(V),2,n),n);
  const rhs=add(power(U,17,n).map(z=>4n*z),[1n,1n,...Array<bigint>(18).fill(0n)],n,-1n);
  assert(lhs.join(',')===rhs.join(','),'Curve identity');
  const one=[1n,...Array<bigint>(9).fill(0n)];
  const recovery=multiply([0n,y,...Array<bigint>(8).fill(0n)],add(one,V,n),n);
  assert(recovery.join(',')===add(one,V,n,-1n).map(z=>mod(x*z,n)).join(','),'Recovery identity');
  const difference=add(U,conjugatePhi(U,n),n,-1n),e=valuation(y);
  assert(Math.min(...difference.filter(z=>z!==0n).map(valuation))===e-1,'Quadratic non-descent valuation');
  const lead=mod(y/17n*inverse(x,n),n);
  const expected=[0n,0n,-lead,2n*lead,...Array<bigint>(16).fill(0n)];
  assert(difference.every((z,j)=>mod(z-expected[j]!,17n**BigInt(e))===0n),'Incorrect leading quadratic part');
  return {scalar_root:scalarRoot,X:x.toString(),Y:y.toString(),precision,modulus:n.toString(),
    theta:theta.map(String),U_in_c_phi_basis:U.map(String),V_in_c_basis:V.map(String),R_in_c_basis:R.map(String),
    difference_valuation:e-1,curve_residual_zero:true,power_condition_R17_equals_V:true,recovery_identity_zero:true,
    scope:'local example only; no positive-integer W solution asserted'};
}
function choose(n: number,k: number): bigint {
  let out=1n;for(let i=1;i<=k;i++)out=out*BigInt(n-i+1)/BigInt(i);return out;
}
for(let j=0;j<16;j++) assert(choose(17,j+1)%17n===0n,'Eisenstein coefficient');
assert(choose(17,1)===17n,'Eisenstein constant');
const group=Array.from({length:16},(_,k)=>Number(scalarPower(3n,k,17n)));
assert(new Set(group).size===16,'Generator of cyclotomic Galois group');
const subgroups:number[][]=[];
for(const size of [1,2,4,8,16]) {
  const gen=group[16/size % 16]!;
  const h=Array.from({length:size},(_,j)=>Number(scalarPower(BigInt(gen),j,17n))).sort((a,b)=>a-b);
  assert(new Set(h).size===size,'Wrong subgroup order');
  if(size>1)assert(h.includes(16),'Proper subfield might be nonreal');
  subgroups.push(h);
}
const type=Array.from({length:8},(_,j)=>j+1);
const stabilizer=group.filter(g=>type.map(j=>g*j%17).sort((a,b)=>a-b).join(',')===type.join(',')).sort((a,b)=>a-b);
assert(stabilizer.join(',')==='1','CM type unexpectedly imprimitive');
const genus=(18-2)/2;
const coverGenus=(17*(2*genus-2)+17*16+2)/2;
assert(genus===8&&coverGenus===256&&2*coverGenus-2===-2*17+34*16,'Riemann-Hurwitz arithmetic');
const summary={genus,power_condition_cover_genus:coverGenus,cm_degree:16,cm_type_exponents:type,
  cm_stabilizer:stabilizer,subgroup_orders:subgroups.map(g=>g.length),all_nontrivial_subgroups_contain_minus_one:true,
  mobius_polynomial_degree:10,image_field_degree_over_Q:20,image_field_degree_over_Q_sqrt5:10,
  global_point_classification_performed:false,full_Beal_solved:false};
const examples=[example(1,17n**2n,12),example(1,17n**3n,12),example(2,3n*17n**2n,12)];
console.log(JSON.stringify({checkpoint:'U73',summary,cyclic_subgroups:subgroups,local_examples:examples},null,2));
