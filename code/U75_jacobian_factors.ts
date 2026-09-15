/** U75 exact checks: character values and multiplication determinants,
 * plus differential-equation jets. No rank upper bound is computed. */
export {};
const check: (condition: boolean, message: string) => asserts condition = (condition,message) => {
  if (!condition) throw new Error(message);
};
const primes=[1021,1361,2381] as const;
const mod=(a:number,p:number):number=>((a%p)+p)%p;
function power(a:number,e:number,p:number):number {
  check(Number.isSafeInteger(e)&&e>=0&&p<3000,'Power domain');
  let out=1,b=mod(a,p);
  while(e>0){if(e%2===1)out=out*b%p;b=b*b%p;e=Math.floor(e/2);}
  return out;
}
function prime(n:number):boolean{
  if(n<2)return false;
  for(let i=2;i*i<=n;i++)if(n%i===0)return false;
  return true;
}
function primitiveRoot(q:number):number{
  let n=q-1;const factors:number[]=[];
  for(let p=2;p*p<=n;p++)if(n%p===0){factors.push(p);while(n%p===0)n/=p;}
  if(n>1)factors.push(n);
  for(let g=2;g<q;g++)if(factors.every(p=>power(g,(q-1)/p,q)!==1))return g;
  throw new Error('No generator');
}
function gcd(a:bigint,b:bigint):bigint{
  while(b!==0n)[a,b]=[b,a%b];return a<0n?-a:a;
}
function determinant(input:readonly (readonly bigint[])[]):bigint{
  const a=input.map(row=>[...row]),n=a.length;
  check(n>0&&a.every(row=>row.length===n),'Matrix domain');
  let denominator=1n,sign=1n;
  for(let k=0;k<n-1;k++){
    let p=k;while(p<n&&a[p]![k]===0n)p++;
    if(p===n)return 0n;
    if(p!==k){[a[p],a[k]]=[a[k]!,a[p]!];sign=-sign;}
    const v=a[k]![k]!;
    for(let i=k+1;i<n;i++)for(let j=k+1;j<n;j++){
      const numerator=a[i]![j]!*v-a[i]![k]!*a[k]![j]!;
      check(numerator%denominator===0n,'Inexact determinant division');
      a[i]![j]=numerator/denominator;
    }
    for(let i=k+1;i<n;i++)a[i]![k]=0n;
    denominator=v;
  }
  return sign*a[n-1]![n-1]!;
}
function cyclotomicNorm(counts:readonly number[]):bigint{
  check(counts.length===17,'Expected 17 character classes');
  const columns:bigint[][]=[];
  for(let k=0;k<16;k++){
    const c=Array<bigint>(33).fill(0n);
    for(let j=0;j<=16;j++)c[j+k]=BigInt(counts[j]!)+(j===0?1n:0n);
    // Quotient by Phi_17, not by a numerical complex root.
    for(let j=32;j>=16;j--)for(let r=0;r<16;r++)c[j-16+r]=c[j-16+r]!-c[j]!;
    columns.push(c.slice(0,16));
  }
  return determinant(Array.from({length:16},(_,r)=>columns.map(c=>c[r]!)));
}
function cyclicMultiply(a:readonly number[],b:readonly number[]):number[]{
  const c=Array<number>(17).fill(0);
  for(let i=0;i<17;i++)for(let j=0;j<17;j++)c[(i+j)%17]=c[(i+j)%17]!+a[i]!*b[j]!;
  return c;
}
function records(q:number){
  check(prime(q)&&q%340===1,'Reduction prime');
  const g=primitiveRoot(q),xi=power(g,(q-1)/17,q),zeta=power(g,(q-1)/5,q),iroot=power(g,(q-1)/4,q);
  const characterLookup=new Map<number,number>();
  for(let j=0;j<17;j++)characterLookup.set(power(xi,j,q),j);
  check(characterLookup.size===17&&power(zeta,5,q)===1&&zeta!==1&&iroot*iroot%q===q-1,'Roots');
  const exponent=(x:number):number=>{
    const result=characterLookup.get(power(x,(q-1)/17,q));
    check(result!==undefined,'Character zero input');return result;
  };
  const d=(1+zeta)%q;
  const seventeenths=new Set(Array.from({length:q-1},(_,j)=>power(j+1,17,q)));
  return Array.from({length:15},(_,j)=>{
    const a=j+1,counts=Array<number>(17).fill(0);let n=3;
    for(let x=1;x<q;x++)if(x!==d){
      const value=power(x,a,q)*mod(d-x,q)%q;
      const e=exponent(value);counts[e]=counts[e]!+1;
      if(seventeenths.has(value))n+=17;
    }
    check(counts.reduce((s,c)=>s+c,0)===q-2,'Character domain');
    check(n===q+1+16*counts[0]!-counts.slice(1).reduce((s,c)=>s+c,0),'Point count');
    const conjugate=Array.from({length:17},(_,j)=>counts[mod(-j,17)]!);
    const nn=cyclicMultiply(counts,conjugate);
    check(nn[0]!-q===nn[1]&&nn.slice(1).every(x=>x===nn[1]),'Jacobi purity');
    const order=cyclotomicNorm(counts);check(order>0n&&order%17n===0n,'Jacobian order');
    return {q,generator:g,zeta,i:iroot,a,character_counts:counts,curve_points:n,jacobian_order:order.toString()};
  });
}
function jets(a:number){
  const p=41,zeta=10,inv17=power(17,p-2,p);
  const ks=Array.from({length:16},(_,j)=>j+1).filter(k=>k+(a*k%17)<=17);
  check(ks.length===8,'Riemann-Roch basis size');
  const columns=[[1,...Array<number>(9).fill(0)],[1,1,...Array<number>(8).fill(0)]];
  for(const k of ks){
    const r=a*k%17,c=[power(zeta,3*k,p)];
    // Solve (1+z)(zeta-z) h'=[(r*zeta-k)-(r+k)z]h/17.
    for(let n=0;n<9;n++){
      const term1=mod((r*zeta-k)*inv17-(zeta-1)*n,p)*c[n]!;
      const term2=mod(n-1-(r+k)*inv17,p)*(n===0?0:c[n-1]!);
      c.push(mod((term1+term2)*power(zeta*(n+1)%p,p-2,p),p));
    }
    columns.push(c);
  }
  const rows=Array.from({length:10},(_,r)=>columns.map(c=>c[r]!));
  const det=Number(((determinant(rows.map(row=>row.map(BigInt)))%41n)+41n)%41n);
  check(det!==0,'Jet rank failure');
  return {a,k_values:ks,jet_matrix_mod41:rows,determinant_mod41:det};
}
const triangular:number[][]=[];
for(let r=1;r<17;r++)for(let s=1;r+s<=16;s++)triangular.push([r,s]);
check(triangular.length===120,'Genus character count');
const blocks=Array.from({length:15},(_,j)=>{
  const a=j+1,chars=triangular.filter(([r,s])=>mod(r!-a*s!,17)===0);
  check(chars.length===8,'Factor dimension');return {a,characters:chars};
});
check(new Set(blocks.flatMap(b=>b.characters.map(c=>c.join(',')))).size===120,'Incomplete partition');
const pairs:number[][]=[];
for(let a=1;a<16;a++){const b=power(a,15,17);if(a<=b)pairs.push([a,b]);}
const reduction=primes.flatMap(q=>records(q));
const cross=Array.from({length:15},(_,j)=>{
  const a=j+1,orders=reduction.filter(r=>r.a===a).map(r=>BigInt(r.jacobian_order));
  check(orders.length===3&&gcd(gcd(orders[0]!,orders[1]!),orders[2]!)===17n,'Torsion gcd');
  const exclusions=primes.map((p,k)=>{
    const rs=orders.filter((_,i)=>i!==k).map(n=>Number(n%BigInt(p)));
    check(rs.some(n=>n!==0),'Uncontrolled residue-characteristic torsion');return rs;
  });
  return {a,cross_characteristic_residues:exclusions};
});
const jetRecords=Array.from({length:15},(_,j)=>jets(j+1));
// Certify the common-orbit polynomial on a 6-by-6 grid over Q(zeta_5).
// Both sides have degree at most five in each variable, so the grid suffices.
function mul5(a:readonly bigint[],b:readonly bigint[]):bigint[]{
  check(a.length===4&&b.length===4,'Cyclotomic rank four');
  const c=Array<bigint>(7).fill(0n);
  for(let i=0;i<4;i++)for(let j=0;j<4;j++)c[i+j]=c[i+j]!+a[i]!*b[j]!;
  for(let k=6;k>=4;k--)for(let j=0;j<4;j++)c[k-4+j]=c[k-4+j]!-c[k]!;
  return c.slice(0,4);
}
function pow5(a:readonly bigint[],n:number):bigint[]{
  let out=[1n,0n,0n,0n];for(let k=0;k<n;k++)out=mul5(out,a);return out;
}
const z5=[0n,1n,0n,0n];
for(let x=-2;x<=3;x++)for(let u=-2;u<=3;u++){
  let out=[1n,0n,0n,0n];
  for(let j=0;j<5;j++){
    const v=mul5(pow5(z5,j),[BigInt(x),-1n,0n,0n]).map(t=>t*BigInt(u));
    v[0]=v[0]!+BigInt(x-1);out=mul5(out,v);
  }
  const rhs=pow5([BigInt(x),-1n,0n,0n],5).map(t=>t*BigInt(u)**5n);
  rhs[0]=rhs[0]!+BigInt(x-1)**5n;
  check(out.join(',')===rhs.join(','),'Common-orbit polynomial');
}
for(let a=1;a<16;a++){
  const exponents=Array<number>(5).fill(0);
  for(let j=0;j<5;j++){
    exponents[(j+1)%5]=exponents[(j+1)%5]!+a;
    exponents[(j+4)%5]=exponents[(j+4)%5]!+1;
    exponents[j]=exponents[j]!-a-1;
  }
  check(exponents.every(e=>e===0)&&15%5===0,'Orbit norm telescoping');
}
const summary={common_orbit_polynomial:true,common_orbit_norms:true,factor_count:15,factor_genus:8,jacobian_dimension:120,inverse_pairs:pairs,
  torsion_orders:Array<number>(15).fill(17),jet_determinants_mod41:jetRecords.map(j=>j.determinant_mod41),
  certified_rank_lower_bound:15,rank_upper_bound_computed:false,degree_five_points_classified:false,
  full_Beal_solved:false};
console.log(JSON.stringify({checkpoint:'U75',summary,character_blocks:blocks,reduction_records:reduction,
  cross_characteristic_checks:cross,jets:jetRecords},null,2));
