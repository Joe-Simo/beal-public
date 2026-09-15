/** Distinct exact U69 checks. This is not an unbounded solution search or a proof kernel. */
export {};
const assert: (condition: boolean, message: string) => asserts condition = (condition, message) => {
  if (!condition) throw new Error(message);
};
const mod = (x: bigint, n: bigint): bigint => ((x % n)+n)%n;
type Vector = readonly bigint[];
const FORCERS = [11,31,41,61,71,101,151,191,211,281,331,431,461,631] as const;
const OLD = new Set([1,13,18,33,38,47,52,67,69,72,84]);
function gcd(a: number, b: number): number {
  while (b !== 0) [a,b]=[b,a%b];
  return a;
}
function prime(n: number): boolean {
  if (n<2) return false;
  for (let d=2;d*d<=n;d++) if(n%d===0) return false;
  return true;
}
function pow(a: bigint, exponent: number, n: bigint): bigint {
  assert(Number.isInteger(exponent)&&exponent>=0&&n>=2n,'Invalid scalar power');
  let x=mod(a,n), e=exponent, out=1n;
  while(e>0) {
    if(e%2===1) out=out*x%n;
    x=x*x%n;e=Math.floor(e/2);
  }
  return out;
}
function mul(a: Vector,b: Vector,constant: bigint,n: bigint): bigint[] {
  const d=a.length;assert(d>0&&d===b.length,'Wrong algebra rank');
  const out=Array<bigint>(2*d-1).fill(0n);
  for(let i=0;i<d;i++) for(let j=0;j<d;j++) out[i+j]=out[i+j]!+a[i]!*b[j]!;
  for(let j=2*d-2;j>=d;j--) out[j-d]=out[j-d]!+constant*out[j]!;
  return out.slice(0,d).map(x=>mod(x,n));
}
function power17(a: Vector,constant: bigint,n: bigint): bigint[] {
  let out=Array<bigint>(a.length).fill(0n);out[0]=1n;
  // Successive multiplication differs from Python's binary exponentiation.
  for(let k=0;k<17;k++) out=mul(out,a,constant,n);
  return out;
}
function determinant(input: readonly (readonly bigint[])[]): bigint {
  const m=input.map(row=>[...row]);const d=m.length;
  assert(d>0&&m.every(row=>row.length===d),'Nonsquare matrix');
  let denominator=1n,sign=1n;
  for(let k=0;k<d-1;k++) {
    let p=k;while(p<d&&m[p]![k]===0n) p++;
    if(p===d) return 0n;
    if(p!==k){[m[p],m[k]]=[m[k]!,m[p]!];sign=-sign;}
    const v=m[k]![k]!;
    for(let i=k+1;i<d;i++)for(let j=k+1;j<d;j++) {
      const numerator=m[i]![j]!*v-m[i]![k]!*m[k]![j]!;
      assert(numerator%denominator===0n,'Nonexact determinant division');
      m[i]![j]=numerator/denominator;
    }
    for(let i=k+1;i<d;i++)m[i]![k]=0n;
    denominator=v;
  }
  return sign*m[d-1]![d-1]!;
}
function norm(a: Vector,constant: bigint,n: bigint): bigint {
  const d=a.length;
  const columns=Array.from({length:d},(_,j)=>{
    const basis=Array<bigint>(d).fill(0n);basis[j]=1n;
    return mul(a,basis,constant,n);
  });
  const matrix=Array.from({length:d},(_,i)=>columns.map(c=>c[i]!));
  return mod(determinant(matrix),n);
}
function lift(initial: Vector,target: Vector,q: bigint,precision: number,constant: bigint): bigint[] {
  assert(target.length===initial.length,'Wrong target rank');
  const one=initial.map((_,i)=>i===0?1n:0n);
  assert(power17(initial,constant,q).join(',')===one.join(','),'Invalid initial root');
  const inverse17=pow(17n,Number(q)-2,q);
  const inverseDerivative=initial.map(x=>x*inverse17%q);
  let current=[...initial],n=q;
  for(let k=1;k<precision;k++) {
    const next=n*q,value=power17(current,constant,next);
    const error=target.map((x,i)=>mod(x-value[i]!,next));
    assert(error.every(x=>x%n===0n),'Lost precision during lifting');
    const correction=mul(error.map(x=>x/n),inverseDerivative,constant,q);
    current=current.map((x,i)=>mod(x+n*correction[i]!,next));
    assert(power17(current,constant,next).join(',')===target.map(x=>mod(x,next)).join(','),'Lift fails');
    n=next;
  }
  return current;
}
const classes=[];
for(let r=1;r<340;r++) if(gcd(r,340)===1&&OLD.has(r%85)&&(r%68===1||r%68===67))classes.push(r);
assert(classes.join(',')==='1,67,69,137,203,273,339','Wrong joint class list');
const kernelCounts=[];
for(const p of [13,19,67,101,103,137]){
  const q=BigInt(p);let count=0;
  for(let a=0;a<p;a++)for(let b=0;b<p;b++){
    const aa=BigInt(a),bb=BigInt(b);
    if((aa*aa+bb*bb)%q!==1n)continue;
    if(power17([aa,bb],-1n,q).join(',')==='1,0')count++;
  }
  assert(count===(p%68===1||p%68===67?17:1),'Gaussian relative kernel mismatch');
  kernelCounts.push([p,count]);
}
const fifthExamples=[];
for(const p of [1021,1361,2381,3061]){
  assert(prime(p)&&p%340===1,'Invalid special-class example');
  const q=BigInt(p),value=pow(2n,(p-1)/5,q);let roots=0;
  for(let a=0;a<p;a++)if(pow(BigInt(a),5,q)===2n)roots++;
  assert(roots===(value===1n?5:0),'Fifth-root existence mismatch');
  fifthExamples.push([p,Number(value),value===1n]);
}
const q=137n,rho0=9n,zeta=119n;
const inverseH=pow(5n*pow(rho0,4,q),135,q);
const idempotent=Array.from({length:5},(_,j)=>pow(rho0,4-j,q)*inverseH%q);
assert(mul(idempotent,idempotent,2n,q).join(',')===idempotent.join(','),'Not an idempotent');
const delta=pow(zeta,13,q); // zeta^-4, since its exact order is 17.
const eta=idempotent.map((x,j)=>mod((j===0?zeta:0n)+(delta-zeta)*x,q));
assert(eta.join(',')==='67,116,89,86,40','Wrong quintic torsion');
assert(power17(eta,2n,q).join(',')==='1,0,0,0,0'&&norm(eta,2n,q)===1n,'Quintic norm/torsion fails');
const i0=37n;assert(i0*i0%q===q-1n,'Gaussian split root');
const inverseZeta=pow(zeta,16,q);
const theta=[mod((zeta+inverseZeta)*pow(2n,135,q),q),
             mod((zeta-inverseZeta)*pow(2n*i0,135,q),q)];
assert(theta.join(',')==='10,77'&&power17(theta,-1n,q).join(',')==='1,0','Gaussian torsion fails');
const precision=12,n=q**BigInt(precision),X=1n,Y=q;
const beta=lift(eta,[X*X,0n,0n,2n*Y*Y,0n],q,precision,2n);
const gaussian=lift(theta,[X**5n,16n*Y**5n],q,precision,-1n);
const N=X**10n+256n*Y**10n,z=lift([1n],[N],q,precision,1n)[0]!;
assert(norm(beta,2n,n)===z&&norm(gaussian,-1n,n)===z,'Norms disagree with Z');
assert(pow(z,17,n)===N%n,'Weighted congruence fails');
assert(beta.map(x=>x%q).join(',')===eta.join(','),'Quintic kernel was lost');
assert(gaussian.map(x=>x%q).join(',')===theta.join(','),'Gaussian kernel was lost');
const witness={q:Number(q),precision,modulus:n.toString(),X:X.toString(),Y:Y.toString(),
  Z_modulus:z.toString(),beta_coefficients:beta.map(String),gaussian_coefficients:gaussian.map(String),
  all_equations_and_norms_verified_modulo_modulus:true,global_integer_solution_claimed:false};
const p=FORCERS.reduce<bigint>((a,b)=>a*BigInt(b),1n);
assert(FORCERS.every(r=>!OLD.has(r%85)&&r%68!==1&&r%68!==67),'Forcer not good in both algebras');
const numerator=257n*17n**17n,denominator=32n**17n;
assert(numerator<denominator,'Gaussian archimedean constant too large');
const jointBound=17n**15n*p**30n;
assert(jointBound>10n**906n&&jointBound.toString().length===908,'Joint-support threshold');
const summary={joint_classes_mod340:classes,extra_fifth_residue_test_in_class1:true,
  gaussian_norm_one_kernel_counts:kernelCounts,fifth_residue_examples:fifthExamples,
  forcing_product:p.toString(),gaussian_bound_numerator:numerator.toString(),
  gaussian_bound_denominator:denominator.toString(),joint_exceptional_product_gt_10_to_453:true,
  joint_bound_squared_decimal_digits:jointBound.toString().length,
  initial_quintic_root:eta.map(Number),initial_gaussian_root:theta.map(Number),local_witness:witness};
console.log(JSON.stringify({checkpoint:'U69',full_Beal_solved:false,summary},null,2));
