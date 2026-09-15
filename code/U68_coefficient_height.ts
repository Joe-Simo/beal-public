/** Distinct finite checks for U68; not a proof-assistant or an unbounded search. */
export {};
const assert: (condition: boolean, message: string) => asserts condition = (condition, message) => {
  if (!condition) throw new Error(message);
};
const FORCERS = [11,31,41,61,71,101,151,191,211,281,331,431,461,631] as const;
const EXCEPTIONAL = [1,13,18,33,38,47,52,67,69,72,84] as const;
type Vector = readonly bigint[];
const mod = (x: bigint, q: bigint): bigint => ((x % q)+q)%q;
function power(x: bigint, n: number, q: bigint): bigint {
  assert(Number.isInteger(n) && n >= 0 && q >= 2n, 'Invalid power domain');
  let out = 1n; let base = mod(x,q); let e = n;
  while (e > 0) {
    if (e%2 === 1) out = out*base%q;
    base = base*base%q; e = Math.floor(e/2);
  }
  return out;
}
function binomial(n: number, k: number): bigint {
  let out = 1n;
  for (let j=1; j<=k; j++) out = out*BigInt(n-j+1)/BigInt(j);
  return out;
}
function gcd(a: number, b: number): number {
  while (b !== 0) [a,b] = [b,a%b];
  return a;
}
function prime(n: number): boolean {
  if (n<2) return false;
  for (let d=2; d*d<=n; d++) if (n%d===0) return false;
  return true;
}
function multiply(a: Vector, b: Vector, q: bigint): bigint[] {
  assert(a.length===5 && b.length===5, 'Wrong quotient rank');
  const c = Array<bigint>(9).fill(0n);
  for (let i=0;i<5;i++) for (let j=0;j<5;j++) c[i+j]=c[i+j]!+a[i]!*b[j]!;
  for (let i=8;i>=5;i--) c[i-5]=c[i-5]!+2n*c[i]!;
  return c.slice(0,5).map(x=>mod(x,q));
}
function ringPower(a: Vector, n: number, q: bigint): bigint[] {
  let out=[1n,0n,0n,0n,0n]; let base=[...a]; let e=n;
  while (e>0) {
    if (e%2===1) out=multiply(out,base,q);
    base=multiply(base,base,q); e=Math.floor(e/2);
  }
  return out;
}
function forms(a: bigint, b: bigint, q: bigint): readonly [bigint,bigint] {
  const ap=[1n], bp=[1n];
  for(let i=1;i<=16;i++) { ap.push(ap[i-1]!*a%q); bp.push(bp[i-1]!*b%q); }
  let g=0n; let h=0n;
  for(let j=0;j<=8;j++) {
    const sign=j%2===0?1n:-1n;
    g+=sign*binomial(17,2*j)*ap[16-2*j]!*bp[2*j]!;
    h+=sign*binomial(17,2*j+1)*ap[16-2*j]!*bp[2*j]!;
  }
  return [mod(g,q),mod(h,q)];
}
function fullFifthImageScan(p: number, kind: number) {
  const q=BigInt(p);
  const cases = [[1n,16n,1n,1n],[17n**4n,16n,17n,1n],
                 [1n,16n*17n**4n,1n,17n]] as const;
  const spec=cases[kind-1]; assert(spec!==undefined,'Missing Gaussian case');
  const [ca,cb,dg,dh]=spec;
  const fifth=new Set<bigint>();
  for(let a=0;a<p;a++) fifth.add(power(BigInt(a),5,q));
  const gImage=new Set([...fifth].map(x=>x*dg%q));
  const hImage=new Set([...fifth].map(x=>x*dh%q));
  const survivors: [number,number][]=[]; let domain=0;
  // Unlike Python, enumerate every pair of fifth-power images, without rescaling.
  for(const fa of fifth) for(const fb of fifth) {
    if(fa===0n && fb===0n) continue;
    domain++;
    const [g,h]=forms(ca*fa%q,cb*fb%q,q);
    if(gImage.has(g)&&hImage.has(h)) survivors.push([Number(fa),Number(fb)]);
  }
  return {q:p,case:kind,domain,survivors};
}
function determinant(input: readonly (readonly bigint[])[]): bigint {
  const m=input.map(row=>[...row]); const n=m.length;
  assert(m.every(row=>row.length===n),'Nonsquare matrix');
  let denominator=1n; let sign=1n;
  for(let k=0;k<n-1;k++) {
    let pivot=k;
    while(pivot<n && m[pivot]![k]===0n) pivot++;
    if(pivot===n) return 0n;
    if(pivot!==k) { [m[pivot],m[k]]=[m[k]!,m[pivot]!]; sign=-sign; }
    const value=m[k]![k]!;
    for(let i=k+1;i<n;i++) for(let j=k+1;j<n;j++) {
      const numerator=m[i]![j]!*value-m[i]![k]!*m[k]![j]!;
      assert(numerator%denominator===0n,'Inexact Bareiss division');
      m[i]![j]=numerator/denominator;
    }
    for(let i=k+1;i<n;i++) m[i]![k]=0n;
    denominator=value;
  }
  return sign*m[n-1]![n-1]!;
}
function squareRootFloor(n: bigint): bigint {
  assert(n>=0n,'Negative square root');
  if(n<2n) return n;
  let x=1n<<BigInt(Math.ceil(n.toString(2).length/2));
  while(true) { const y=(x+n/x)/2n; if(y>=x) return x; x=y; }
}
const coefficientMaps=[new Map<number,bigint>(),new Map<number,bigint>()];
for(let k=0;k<=17;k++) {
  const r=(4*k)%5;
  if(r===1||r===2) coefficientMaps[r-1]!.set(k,binomial(17,k)*2n**BigInt(Math.floor(4*k/5)));
}
assert(JSON.stringify([...coefficientMaps[0]!].map(([k,v])=>[k,v.toString()]))===
  JSON.stringify([[4,'19040'],[9,'3111680'],[14,'1392640']]),'rho coefficient one');
assert(JSON.stringify([...coefficientMaps[1]!].map(([k,v])=>[k,v.toString()]))===
  JSON.stringify([[3,'2720'],[8,'1555840'],[13,'2437120']]),'rho coefficient two');
const resultant=determinant([[14n,143n,4n,0n],[0n,14n,143n,4n],
                             [4n,143n,14n,0n],[0n,4n,143n,14n]]);
assert(resultant===-2012500n,'Sparsity resultant');
const classes: number[]=[];
for(let a=1;a<85;a++) {
  if(gcd(a,85)!==1) continue;
  const degrees=a%5===1?[1,5]:a%5===4?[1,2]:[1,4];
  if(degrees.some(d=>power(BigInt(a),d,17n)===1n)) classes.push(a);
}
assert(JSON.stringify(classes)===JSON.stringify(EXCEPTIONAL),'Exceptional classification');
const q11=[1,2,3].map(kind=>fullFifthImageScan(11,kind));
assert(q11[0]!.survivors.length===0 && q11[1]!.survivors.length===0,'Cases I/II survive');
assert(q11[2]!.survivors.length===2 && q11[2]!.survivors.every(v=>v[1]===0),'Case III');
const scans=FORCERS.map(q=> {
  assert(prime(q) && q%5===1 && q%17!==1,'Forcing prime domain');
  const row=fullFifthImageScan(q,3);
  assert(row.survivors.length===(q-1)/5,'Wrong full-scale survivor count');
  assert(row.survivors.every(([a,b])=>a!==0 && b===0),'A nonaxis pair survived');
  assert(!classes.includes(q%85),'Forcing prime was exceptional');
  return row;
});
const eta=ringPower([1n,1n,0n,0n,0n],1680,13n);
let test=[1n,0n,0n,0n,0n];
for(let k=0;k<17;k++) test=multiply(test,eta,13n);
assert(test.join(',')==='1,0,0,0,0' && eta.slice(1).some(x=>x!==0n),'Bad-prime negative control');
const binomialValuations: number[]=[];
for(let j=1;j<=17;j++) {
  let n=binomial(17,j); let v=0;
  while(n%17n===0n) { n/=17n;v++; }
  binomialValuations.push(v);
}
assert(binomialValuations.slice(0,16).every(v=>v===1)&&binomialValuations[16]===0,'17-adic leading term');
const p=FORCERS.reduce<bigint>((x,q)=>x*BigInt(q),1n);
const d=17n*p*p; const bound=d**17n; const lower=squareRootFloor(bound)+1n;
assert((lower-1n)**2n<=bound && lower**2n>bound,'Integer root certificate');
assert(bound>10n**1028n && lower.toString().length===515,'Height threshold');
assert(17n**15n*p**32n>10n**966n,'Exceptional support threshold');
const summary={exceptional_classes_mod85:classes,forced_product:p.toString(),
  coefficient_divisor:d.toString(),integer_lower_bound:lower.toString(),lower_bound_digits:515,
  base_gt_10_to_514:true,exceptional_part_gt_10_to_483:true,sparsity_resultant:Number(resultant),
  q13_nontrivial_kernel:eta.map(Number),q11_case_nonempty:q11.map(x=>x.survivors.length>0),
  forcing_primes:FORCERS};
console.log(JSON.stringify({checkpoint:'U68',full_Beal_solved:false,summary,
  fifth_power_domain:'all distinct fifth-power image pairs, excluding only (0,0)',
  forcing_scans:scans,q11_cases:q11,binomial_17_valuations:binomialValuations},null,2));
