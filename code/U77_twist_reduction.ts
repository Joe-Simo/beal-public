/** U77 exact certificates. This is not a rank or global-point computation. */
export {};
const check: (ok: boolean, message: string) => asserts ok = (ok, message) => {
  if (!ok) throw new Error(message);
};
const primes = [1021,1361,1531] as const;
const mod=(a:number,p:number):number=>((a%p)+p)%p;
function pow(a:number,e:number,p:number):number {
  check(Number.isSafeInteger(e)&&e>=0&&p<2000,'Power domain');
  let b=mod(a,p),out=1;
  while(e>0){if(e%2===1)out=out*b%p;b=b*b%p;e=Math.floor(e/2);}
  return out;
}
function inverse(a:number,n:number):number {
  let r=n,s=mod(a,n),x=0,y=1;
  while(s!==0){const q=Math.floor(r/s);[r,s]=[s,r-q*s];[x,y]=[y,x-q*y];}
  check(r===1,'Not a unit');return mod(x,n);
}
function isPrime(n:number):boolean {
  if(n<2)return false;
  for(let j=2;j*j<=n;j++)if(n%j===0)return false;return true;
}
function primitiveRoot(q:number):number {
  let n=q-1;const factors:number[]=[];
  for(let p=2;p*p<=n;p++)if(n%p===0){factors.push(p);while(n%p===0)n/=p;}
  if(n>1)factors.push(n);
  for(let g=2;g<q;g++)if(factors.every(p=>pow(g,(q-1)/p,q)!==1))return g;
  throw new Error('Primitive root not found');
}
function determinant(input: readonly (readonly bigint[])[]):bigint {
  const a=input.map(r=>[...r]),n=a.length;
  check(n>0&&a.every(r=>r.length===n),'Determinant domain');
  let old=1n,sign=1n;
  for(let k=0;k<n-1;k++){
    let p=k;while(p<n&&a[p]![k]===0n)p++;
    if(p===n)return 0n;
    if(p!==k){[a[p],a[k]]=[a[k]!,a[p]!];sign=-sign;}
    const pivot=a[k]![k]!;
    for(let i=k+1;i<n;i++)for(let j=k+1;j<n;j++){
      const num=pivot*a[i]![j]!-a[i]![k]!*a[k]![j]!;
      check(num%old===0n,'Inexact Bareiss division');a[i]![j]=num/old;
    }
    for(let i=k+1;i<n;i++)a[i]![k]=0n;
    old=pivot;
  }
  return sign*a[n-1]![n-1]!;
}
function gcd(a:bigint,b:bigint):bigint {while(b!==0n)[a,b]=[b,a%b];return a<0n?-a:a;}
function jacobiNorm(counts:readonly number[],sgn:number):bigint {
  const cols:bigint[][]=[];
  for(let k=0;k<16;k++){
    const c=Array<bigint>(33).fill(0n);
    for(let j=0;j<17;j++)c[j+k]=BigInt(sgn*counts[j]!+(j===0?1:0));
    for(let j=32;j>=16;j--)for(let r=0;r<16;r++)c[j-16+r]=c[j-16+r]!-c[j]!;
    cols.push(c.slice(0,16));
  }
  return determinant(Array.from({length:16},(_,j)=>cols.map(c=>c[j]!)));
}
function reductionRecords(){
  return primes.map(q=>{
    check(isPrime(q)&&q%85===1,'Bad reduction prime');
    const g=primitiveRoot(q),zeta=pow(g,(q-1)/5,q),ph=mod(1+zeta+inverse(zeta,q),q);
    const delta=mod(3-ph,q),eps=mod(zeta*zeta-pow(zeta,3,q),q);
    check(eps*eps%q===mod(-delta,q),'Twist constant');
    const sign=pow(delta,(q-1)/2,q)===1?1:-1;
    check(sign===(q%4===1?1:-1),'Twist character sign');
    const root=pow(g,(q-1)/17,q),lookup=new Map<number,number>();
    for(let j=0;j<17;j++)lookup.set(pow(root,j,q),j);
    const d=(1+zeta)%q,counts=Array<number>(17).fill(0);
    for(let t=1;t<q;t++)if(t!==d){
      const v=t*mod(d-t,q)%q,e=lookup.get(pow(v,(q-1)/17,q));
      check(e!==undefined,'Character undefined');counts[e]=counts[e]!+1;
    }
    check(counts.reduce((a,b)=>a+b,0)===q-2,'Wrong character domain');
    const order=jacobiNorm(counts,sign);check(order>0n,'Nonpositive order');
    let count=1;
    for(let t=0;t<q;t++){
      const f=mod(ph+2-4*delta*pow(t,17,q),q);
      count+=1+(f===0?0:pow(f,(q-1)/2,q)===1?1:-1);
    }
    check(count===q+1+sign*(16*counts[0]!-counts.slice(1).reduce((a,b)=>a+b,0)),'Point count sign');
    return {q,generator:g,zeta,phi:ph,delta,quadratic_character_delta:sign,
      character_counts:counts,curve_points:count,jacobian_order:order.toString()};
  });
}
// All exact integer ring calculations here take place in Z[zeta_5].
type Cyclo=readonly bigint[];
const one=[1n,0n,0n,0n],zz=[0n,1n,0n,0n];
const add=(a:Cyclo,b:Cyclo):bigint[]=>a.map((v,i)=>v+b[i]!);
const scale=(a:Cyclo,k:bigint):bigint[]=>a.map(v=>v*k);
function mul(a:Cyclo,b:Cyclo):bigint[]{
  check(a.length===4&&b.length===4,'Cyclotomic rank');
  const c=Array<bigint>(7).fill(0n);
  for(let i=0;i<4;i++)for(let j=0;j<4;j++)c[i+j]=c[i+j]!+a[i]!*b[j]!;
  for(let j=6;j>=4;j--)for(let r=0;r<4;r++)c[j-4+r]=c[j-4+r]!-c[j]!;
  return c.slice(0,4);
}
function power(a:Cyclo,n:number):bigint[]{let out=one;for(let j=0;j<n;j++)out=mul(out,a);return out;}
const equal=(a:Cyclo,b:Cyclo):boolean=>a.join(',')===b.join(',');
const zero=[0n,0n,0n,0n];
const phi=add(add(one,zz),power(zz,4)),eps=add(power(zz,2),scale(power(zz,3),-1n));
const delta=add(scale(one,3n),scale(phi,-1n));
check(equal(add(add(power(phi,2),scale(phi,-1n)),scale(one,-1n)),zero),'phi relation');
check(equal(add(power(eps,2),delta),zero),'epsilon relation');
check(equal(add(mul(delta,power(phi,2)),scale(add(phi,scale(one,2n)),-1n)),zero),'Integral model');
check(equal(add(add(one,zz),mul(power(zz,3),phi)),zero),'d normalization');
const conjEps=add(power(zz,8),scale(power(zz,12),-1n));
check(equal(add(conjEps,eps),zero),'Kappa sign');
// Cleared-denominator degree-two identity: three exact s-values suffice.
for(const s of [-1n,0n,1n]){
  const r17=mul(add(one,scale(zz,s)),add(one,scale(power(zz,4),s)));
  const v=add(add(scale(power(eps,2),(1n-s)**2n),scale(power(phi,2),-((1n+s)**2n))),scale(r17,4n));
  check(equal(v,zero),'Normalized curve identity');
}
// Degree at most five in x and two in lambda, in the same exact ring.
for(let x=0n;x<=5n;x++)for(const l of [-1n,0n,1n]){
  const P=scale(one,(x-1n)**5n),Q=power(add(scale(one,x),scale(zz,-1n)),5);
  const diff=add(scale(add(P,scale(Q,l)),1n-l),scale(add(P,scale(Q,-l)),-(1n+l)));
  check(equal(diff,scale(add(Q,scale(P,-1n)),2n*l)),'Orbit distinction identity');
}
for(let s=-2n;s<=2n;s++)for(let h=-2n;h<=2n;h++){
  check(s*(1n+h*s)**2n-h*s*(1n+s)**2n===s*(1n-h)*(1n-h*s*s),'u distinction identity');
}
function orbitExample(){
  const q=41,zeta=10,iroot=9,c5=16*iroot%q,ord=q**5-1;
  check(pow(c5,(q-1)/5,q)!==1,'The quintic must be irreducible');
  const exp=inverse(17,ord),ph=mod(1+zeta+inverse(zeta,q),q),ep=mod(zeta*zeta-pow(zeta,3,q),q);
  type Vec=readonly number[];
  const o=[1,0,0,0,0],c=[0,1,0,0,0];
  const sc=(a:Vec,n:number):number[]=>a.map(v=>mod(v*n,q));
  const ad=(a:Vec,b:Vec):number[]=>a.map((v,i)=>mod(v+b[i]!,q));
  function m(a:Vec,b:Vec):number[]{
    const t=Array<number>(9).fill(0);
    for(let i=0;i<5;i++)for(let j=0;j<5;j++)t[i+j]=mod(t[i+j]!+a[i]!*b[j]!,q);
    for(let j=8;j>=5;j--)t[j-5]=mod(t[j-5]!+c5*t[j]!,q);
    return t.slice(0,5);
  }
  function pw(a:Vec,n:number):number[]{let b=[...a],out=o;
    while(n>0){if(n%2===1)out=m(out,b);b=m(b,b);n=Math.floor(n/2);}return out;}
  const inv=(a:Vec):number[]=>{check(a.some(v=>v!==0),'Zero field inverse');return pw(a,ord-1);};
  const orbits=[1,-1].map(sign=>{
    const taus=Array.from({length:5},(_,j)=>ad(o,sc(c,sign*pow(zeta,j,q))));
    const roots=taus.map(t=>pw(t,exp));
    check(roots.every((r,j)=>pw(r,17).join(',')===taus[j]!.join(',')),'Finite common roots');
    const us:number[][]=[],vs:number[][]=[],xs:number[][]=[];
    for(let j=0;j<5;j++){
      const u=m(m(roots[(j+1)%5]!,roots[(j+4)%5]!),inv(pw(roots[j]!,2)));
      const s=sc(c,sign*pow(zeta,j,q)),v=sc(m(ad(o,sc(s,-1)),inv(ad(o,s))),ep);
      check(ad(pw(v,2),sc(pw(u,17),4)).join(',')===sc(o,ph*ph).join(','),'Finite curve identity');
      const xx=m(taus[(j+1)%5]!,inv(taus[j]!));
      check(xx.join(',')===sc(ad(sc(o,1+zeta),sc(v,pow(zeta,3,q))),inverse(2,q)).join(','),'Finite coordinate map');
      us.push(u);vs.push(v);xs.push(xx);
    }
    check(new Set(us.map(v=>v.join(','))).size===5&&vs.every(v=>v.some(a=>a!==0)),'Finite reduced divisor');
    let vand=o;
    for(let j=0;j<5;j++)for(let k=0;k<j;k++)vand=m(vand,ad(us[j]!,sc(us[k]!,-1)));
    const vn=pw(vand,(q**5-1)/(q-1));
    check(vn[0]!==0&&vn.slice(1).every(v=>v===0),'Vandermonde norm');
    let cs=[o];
    for(const xx of xs){
      const next=Array.from({length:cs.length+1},()=>[0,0,0,0,0]);
      for(let j=0;j<cs.length;j++){next[j]=ad(next[j]!,sc(m(cs[j]!,xx),-1));next[j+1]=ad(next[j+1]!,cs[j]!);}cs=next;
    }
    check(cs.every(v=>v.slice(1).every(a=>a===0)),'Orbit polynomial not rational');
    return {sign,theta_roots:roots,u_values:us,v_values:vs,x_polynomial:cs.map(v=>v[0]!),vandermonde_norm:vn[0]!};
  });
  check(orbits[0]!.x_polynomial.join(',')!==orbits[1]!.x_polynomial.join(','),'Orbits not separated');
  return {q,zeta,i:iroot,c5,X:1,Y:1,scope:'one finite-field example, not a global solution',orbits};
}
const records=reductionRecords();const orders=records.map(r=>BigInt(r.jacobian_order));
check(gcd(gcd(orders[0]!,orders[1]!),orders[2]!)===1n,'Torsion gcd');
primes.forEach((p,i)=>check(orders.some((n,j)=>j!==i&&n%BigInt(p)!==0n),'Residue-characteristic torsion not covered'));
// Norm(a*b)=400 for a=-4(3-phi),b=phi+2; degree-17 binomial discriminant.
check(equal(mul(delta,add(phi,scale(one,2n))),scale(one,5n)), 'Coefficient norm identity');
const summary={symbolic_identities_verified:true,twist:'(3-phi)w^2=phi^2-4u^17, phi^2-phi-1=0',
  integral_model:'v^2=phi+2-4(3-phi)u^17',base_field_degree:2,genus:8,torsion_order:1,
  rank_upper_bound_computed:false,rank_positive_is_necessary_for_weighted_solution:true,
  known_smaller_field_subgroup_saturation_excluded_as_target:true,full_Beal_solved:false};
console.log(JSON.stringify({checkpoint:'U77',summary,reduction_records:records,
  character_signs:{eta:-1,kappa:-1,eta_kappa:1},
  model_discriminant_norm_factorization:{'2':64,'5':32,'17':34},finite_orbit_example:orbitExample()},null,2));
