/** U72: exact determinant and digit-lift checks, distinct from the Python series. */
export {};
const assert: (ok: boolean, message: string) => asserts ok = (ok, message) => {
  if (!ok) throw new Error(message);
};
type Vector = readonly bigint[];
const PRIMES = [11,31,41,61,71,101,151,191,211,281,331,431,461,631] as const;
const H = [2n,0n,0n,0n,0n,2n,0n,0n,0n,0n];
const C = [256n,0n,0n,0n,0n,0n,0n,0n,0n,0n];
const one = [1n,...Array<bigint>(9).fill(0n)];
const mod = (a: bigint, n: bigint): bigint => ((a%n)+n)%n;
function multiply(a: Vector, b: Vector, lower: Vector, modulus: bigint|null): bigint[] {
  assert(a.length===10 && b.length===10 && lower.length===10, 'Wrong algebra rank');
  const out = Array<bigint>(19).fill(0n);
  for(let i=0;i<10;i++) for(let j=0;j<10;j++) out[i+j]=out[i+j]!+a[i]!*b[j]!;
  for(let k=18;k>=10;k--) for(let j=0;j<10;j++) out[k-10+j]=out[k-10+j]!-out[k]!*lower[j]!;
  return out.slice(0,10).map(a=>modulus===null?a:mod(a,modulus));
}
function power(a: Vector, exponent: number, lower: Vector, modulus: bigint|null): bigint[] {
  assert(Number.isSafeInteger(exponent)&&exponent>=0, 'Invalid exponent');
  let out=[...one], base=[...a], e=exponent;
  while(e>0) { if(e%2===1) out=multiply(out,base,lower,modulus);
    base=multiply(base,base,lower,modulus); e=Math.floor(e/2); }
  return out;
}
function scalarPower(a: bigint, e: number, p: bigint): bigint {
  let base=mod(a,p), out=1n;
  while(e>0) { if(e%2===1)out=out*base%p;base=base*base%p;e=Math.floor(e/2); }
  return out;
}
function inverse(a: bigint, p: bigint): bigint {
  let r=p,s=mod(a,p),x=0n,y=1n;
  while(s!==0n){const q=r/s;[r,s]=[s,r-q*s];[x,y]=[y,x-q*y];}
  assert(r===1n,'Inverting a nonunit');return mod(x,p);
}
function valuation(a: bigint, p: bigint): number {
  assert(a!==0n, 'Zero residue does not certify a valuation');
  let v=0; while(a%p===0n){a/=p;v++;} return v;
}
function determinant(input: readonly Vector[]): bigint {
  const a=input.map(row=>[...row]); const n=a.length;
  assert(n>0&&a.every(row=>row.length===n), 'Non-square determinant');
  let sign=1n, previous=1n;
  for(let k=0;k<n-1;k++) {
    let pivot=k;while(pivot<n&&a[pivot]![k]===0n)pivot++;
    if(pivot===n)return 0n;
    if(pivot!==k){[a[k],a[pivot]]=[a[pivot]!,a[k]!];sign=-sign;}
    const d=a[k]![k]!;
    for(let i=k+1;i<n;i++)for(let j=k+1;j<n;j++){
      const value=a[i]![j]!*d-a[i]![k]!*a[k]![j]!;
      assert(value%previous===0n, 'Inexact determinant step');a[i]![j]=value/previous;
    }
    for(let i=k+1;i<n;i++)a[i]![k]=0n;previous=d;
  }
  return sign*a[n-1]![n-1]!;
}
function normH(a: Vector): bigint {
  const cols=Array.from({length:10},(_,j)=>multiply(a,one.map((_,i)=>i===j?1n:0n),H,null));
  return determinant(Array.from({length:10},(_,i)=>cols.map(col=>col[i]!)));
}
function prime(n: number): boolean {
  if(n<2)return false;for(let d=2;d*d<=n;d++)if(n%d===0)return false;return true;
}
function binomial(n: number,k: number): bigint {
  let a=1n;for(let j=1;j<=k;j++)a=a*BigInt(n-j+1)/BigInt(j);return a;
}
const addScalar=(a: Vector,k: bigint):bigint[]=>a.map((v,i)=>i===0?v+k:v);
const isZero=(a: Vector):boolean=>a.every(x=>x===0n);
const ig=[1n,0n,0n,0n,0n,1n,0n,0n,0n,0n];
const rg=[0n,0n,1n,0n,0n,0n,0n,1n,0n,0n];
const cg=[0n,0n,0n,-2n,0n,0n,0n,0n,-1n,0n];
assert(isZero(addScalar(power(ig,2,H,null),1n)), 'i relation');
assert(isZero(addScalar(power(rg,5,H,null),-2n)), 'rho relation');
assert(isZero(multiply(ig,power(rg,4,H,null),H,null).map((a,i)=>a-cg[i]!)), 'c relation');
assert(isZero(addScalar(power(cg,10,H,null),256n)), 'c polynomial');
assert(isZero(power(cg,4,H,null).map((a,i)=>a-8n*rg[i]!)), 'rho recovery');
assert(isZero(power(cg,5,H,null).map((a,i)=>a-16n*ig[i]!)), 'i recovery');
const cols=Array.from({length:10},(_,j)=>power(cg,j,H,null));
const det=determinant(Array.from({length:10},(_,i)=>cols.map(col=>col[i]!)));
const index=det<0n?-det:det;
assert(index===2n**34n,'Order index');
const dh=[0n,0n,0n,0n,10n,0n,0n,0n,0n,10n];
const discH=-normH(dh),discC=-(10n**10n)*(256n**9n);
assert(discH===-160000000000n&&discC===discH*index*index,'Discriminant identity');
const numerators=[1n];
for(let j=1;j<=9;j++){
  const a=numerators[j-1]!*(1n-17n*BigInt(j-1));
  assert(a%BigInt(j)===0n,'Leading numerator recurrence');numerators.push(a/BigInt(j));
}
assert(numerators[9]===658767450n, 'Ninth binomial numerator');
const qRows=PRIMES.map(q=>{
  assert(prime(q)&&q%5===1,'Forcing prime');
  const degree=q%4===1?5:10,residue=Number(scalarPower(BigInt(q),degree,17n));
  assert(residue!==1,'Power map has torsion');
  const cResidue=[0n,1n,...Array<bigint>(8).fill(0n)];let image=[...cResidue];
  for(let step=0;step<degree;step++)image=power(image,q,C,BigInt(q));
  assert(image.join(',')===cResidue.join(','),'Frobenius-degree certificate');
  const vals=numerators.map(a=>valuation(a,BigInt(q)));
  assert(vals.every((v,j)=>v===Number(q===11&&j>=3)+Number(q===101&&j>=7)),'Leading q valuation');
  return [q,degree,residue,vals];
});
function liftExample(p: number,e: number,precision: number,scalar: number,yUnit: number){
  const q=BigInt(p),m=q**BigInt(precision),a=BigInt(scalar),v=BigInt(yUnit);
  const target=[scalarPower(a,17,m),v*q**BigInt(e),...Array<bigint>(8).fill(0n)];
  let root=[a,...Array<bigint>(9).fill(0n)];
  if(p===17){
    root[1]=mod(v*q**BigInt(e-1)*inverse(a**16n,m),m);
    for(let k=e+1;k<precision;k++){
      const prev=q**BigInt(k),next=prev*q, image=power(root,17,C,next);
      const residual=target.map((a,j)=>mod(a-image[j]!,next));
      assert(residual.every(a=>a%prev===0n),'Wrong 17-adic starting precision');
      root=root.map((a,j)=>mod(a+q**BigInt(k-1)*(residual[j]!/prev),next));
    }
  }else{
    const inv=inverse(17n*scalarPower(a,16,q),q);
    for(let k=1;k<precision;k++){
      const prev=q**BigInt(k),next=prev*q,image=power(root,17,C,next);
      const residual=target.map((a,j)=>mod(a-image[j]!,next));
      assert(residual.every(a=>a%prev===0n),'Wrong ordinary Hensel precision');
      root=root.map((a,j)=>mod(a+prev*mod(inv*(residual[j]!/prev),q),next));
    }
  }
  assert(power(root,17,C,m).join(',')===target.map(a=>mod(a,m)).join(','),'Failed local root');
  const known=precision-(p===17?1:0),knownMod=q**BigInt(known);
  root=root.map(a=>mod(a,knownMod));
  const vals=root.map(a=>valuation(a,q));assert(Math.max(...vals)<known,'Uncertified valuation');
  return {p,e,power_precision:precision,root_precision:known,scalar_root:scalar,y_unit:yUnit,
    root:root.map(String),valuations:vals,power_residual_zero:true};
}
const examples17=[2,3,4].map(e=>liftExample(17,e,9*(e-1)+10,1,1));
examples17.push(liftExample(17,2,22,2,3));
for(const row of examples17)assert(row.valuations.every((v,j)=>v===j*(row.e-1)),'17 coefficient profile');
const examplesGood=PRIMES.map(q=>liftExample(q,1,12,2,1));
for(const row of examplesGood)assert(row.valuations.every((v,j)=>v===j+Number(row.p===11&&j>=3)+Number(row.p===101&&j>=7)),'Good-prime profile');
const examples2=[[1,1],[3,2],[5,7],[11,4]].map(([X,Y])=>{
  assert(X!==undefined&&Y!==undefined,'Missing test value');
  const n=12,target=[BigInt(X),BigInt(Y),...Array<bigint>(8).fill(0n)];
  let root=target.map(a=>a%2n);
  assert(power(root,17,C,2n).join(',')===root.join(','),'Mod-two initial root');
  for(let k=1;k<n;k++){
    const prev=2n**BigInt(k),next=2n*prev,image=power(root,17,C,next);
    const residual=target.map((a,j)=>mod(a-image[j]!,next));
    assert(residual.every(a=>a%prev===0n),'2-adic lifting precision');
    root=root.map((a,j)=>a+residual[j]!);
  }
  assert(power(root,17,C,2n**BigInt(n)).join(',')===target.join(','),'Root closure example');
  return {X,Y,precision:n,root:root.map(String)};
});
function fullForcingScan(p: number,kind: number){
  const spec=([[1n,16n,1n,1n],[17n**4n,16n,17n,1n],[1n,16n*17n**4n,1n,17n]] as const)[kind-1];
  assert(spec!==undefined,'Unknown Gaussian case');const [ca,cb,dg,dh]=spec,q=BigInt(p);
  const fifth=new Set(Array.from({length:p},(_,i)=>scalarPower(BigInt(i),5,q)));
  const gSet=new Set([...fifth].map(a=>a*dg%q)),hSet=new Set([...fifth].map(a=>a*dh%q));
  const survivors:[number,number][]=[];
  for(const A of fifth)for(const B of fifth){
    if(A===0n&&B===0n)continue;
    const a=ca*A%q,b=cb*B%q,ap=[1n],bp=[1n];
    for(let j=1;j<=16;j++){ap.push(ap[j-1]!*a%q);bp.push(bp[j-1]!*b%q);}
    let g=0n,h=0n;
    for(let j=0;j<=8;j++){const sign=j%2===0?1n:-1n;
      g+=sign*binomial(17,2*j)*ap[16-2*j]!*bp[2*j]!;
      h+=sign*binomial(17,2*j+1)*ap[16-2*j]!*bp[2*j]!;}
    if(gSet.has(mod(g,q))&&hSet.has(mod(h,q)))survivors.push([Number(A),Number(B)]);
  }
  return {p,kind,survivors};
}
assert(fullForcingScan(11,1).survivors.length===0&&fullForcingScan(11,2).survivors.length===0,'Gaussian cases I/II');
const forcing=PRIMES.map(p=>{
  const row=fullForcingScan(p,3);assert(row.survivors.length===(p-1)/5,'Gaussian count');
  assert(row.survivors.every(([a,b])=>a!==0&&b===0),'Nonaxis forcing survivor');return row;
});
const P=PRIMES.reduce<bigint>((a,p)=>a*BigInt(p),1n),D=11n*101n*(17n*P)**9n;
const numerator=16n**153n*D**85n;
assert(numerator>243n*10n**24050n&&numerator<243n*10n**24055n,'Height threshold');
const summary={power_order_index:String(index),field_discriminant:String(discH),
  power_order_discriminant:String(discC),ninth_binomial:[String(numerators[9]),String(17n**9n)],
  forcing_prime_rows:qRows,forced_product:String(P),ninth_coefficient_divisor:String(D),
  base_bound_decimal_exponent:4810,full_support_17_profiles:examples17.map(row=>row.valuations),
  all_local_examples_pass:true,full_Beal_solved:false};
console.log(JSON.stringify({checkpoint:'U72',summary,forcing_scans:forcing,
  examples17,examples_good:examplesGood,examples2},null,2));
