/** Exact U71 verifier. Certificates are inputs, not trusted conclusions. */
import certificate from '../references/U71/certificate.json';
const assert: (ok: boolean, message: string) => asserts ok = (ok, message) => {
  if (!ok) throw new Error(message);
};
type Vector = readonly bigint[];
const mod = (a: bigint, n: bigint): bigint => ((a % n) + n) % n;
function determinant(input: readonly (readonly bigint[])[]): bigint {
  const a = input.map(row => [...row]); const n = a.length;
  assert(n > 0 && a.every(row => row.length === n), 'Non-square matrix');
  let sign = 1n; let denominator = 1n;
  for (let k = 0; k < n - 1; k++) {
    let pivot = k;
    while (pivot < n && a[pivot]![k] === 0n) pivot++;
    if (pivot === n) return 0n;
    if (pivot !== k) { [a[k], a[pivot]] = [a[pivot]!, a[k]!]; sign = -sign; }
    const value = a[k]![k]!;
    for (let i = k + 1; i < n; i++) for (let j = k + 1; j < n; j++) {
      const numerator = a[i]![j]! * value - a[i]![k]! * a[k]![j]!;
      assert(numerator % denominator === 0n, 'Inexact determinant division');
      a[i]![j] = numerator / denominator;
    }
    for (let i = k + 1; i < n; i++) a[i]![k] = 0n;
    denominator = value;
  }
  return sign * a[n - 1]![n - 1]!;
}
function normNumerator(a: Vector): bigint {
  assert(a.length === 10, 'Wrong rank');
  const matrix = Array.from({length: 10}, () => Array<bigint>(10).fill(0n));
  for (let j = 0; j < 10; j++) for (let k = 0; k < 10; k++) {
    matrix[(j + k) % 10]![j] = a[k]! * (j + k >= 10 ? -4n : 1n);
  }
  return determinant(matrix);
}
function integral(v: Vector): boolean {
  return v.length === 10 && v.slice(0, 3).every(a => a % 4n === 0n)
    && (v[3]! - 2n * v[8]!) % 4n === 0n
    && (v[4]! - 2n * v[9]!) % 4n === 0n
    && v.slice(5, 8).every(a => a % 2n === 0n);
}
function inverse(a: bigint, q: bigint): bigint {
  let r = q; let s = mod(a, q); let x = 0n; let y = 1n;
  while (s !== 0n) { const c = r / s; [r, s] = [s, r-c*s]; [x, y] = [y, x-c*y]; }
  assert(r === 1n, 'Nonunit'); return mod(x, q);
}
function multiply(a: Vector, b: Vector, modulus: bigint): bigint[] {
  assert(a.length === 10 && b.length === 10 && modulus >= 2n, 'Ring domain');
  const result = Array<bigint>(10).fill(0n);
  for (let i = 0; i < 10; i++) for (let j = 0; j < 10; j++) {
    const k = (i+j)%10;
    result[k] = result[k]! + a[i]!*b[j]!*(i+j >= 10 ? -4n : 1n);
  }
  return result.map(x => mod(x, modulus));
}
function ringPower(a: Vector, exponent: number, modulus: bigint): bigint[] {
  assert(Number.isSafeInteger(exponent) && exponent >= 0, 'Exponent domain');
  let out = [1n, ...Array<bigint>(9).fill(0n)]; let b = [...a]; let e = exponent;
  while (e > 0) {
    if (e % 2 === 1) out = multiply(out, b, modulus);
    b = multiply(b, b, modulus); e = Math.floor(e/2);
  }
  return out;
}
function scalarPower(x: bigint, e: number, q: bigint): bigint {
  let b = mod(x,q); let out = 1n;
  while(e > 0) { if(e%2 === 1) out = out*b%q; b = b*b%q; e = Math.floor(e/2); }
  return out;
}
// Prime-field operations have p<=519. Every product is reduced immediately,
// so these integer operations are strictly below 2^53 and exactly represented.
const fm = (a: number, p: number): number => ((a%p)+p)%p;
const trim = (a: readonly number[]): number[] => {
  const b = [...a]; while(b.length && b[b.length-1] === 0) b.pop(); return b;
};
function polySubtract(a: readonly number[], b: readonly number[], p: number): number[] {
  return trim(Array.from({length: Math.max(a.length,b.length)}, (_,i) => fm((a[i]??0)-(b[i]??0),p)));
}
function polyRemainder(a: readonly number[], b: readonly number[], p: number): number[] {
  const out = trim(a.map(x => fm(x,p))); assert(b.length>0, 'Zero polynomial divisor');
  const inv = Number(inverse(BigInt(b[b.length-1]!),BigInt(p)));
  while(out.length >= b.length) {
    const shift = out.length-b.length; const scale = fm(out[out.length-1]!*inv,p);
    for(let j=0;j<b.length;j++) out[shift+j] = fm(out[shift+j]!-scale*b[j]!,p);
    while(out.length && out[out.length-1] === 0) out.pop();
  }
  return out;
}
function polyMultiply(a: readonly number[], b: readonly number[], p: number): number[] {
  if(!a.length || !b.length) return [];
  const c = Array<number>(a.length+b.length-1).fill(0);
  for(let i=0;i<a.length;i++) for(let j=0;j<b.length;j++) c[i+j] = fm(c[i+j]!+a[i]!*b[j]!,p);
  return trim(c);
}
function polyGcd(a: readonly number[], b: readonly number[], p: number): number[] {
  let c = trim(a); let d = trim(b);
  while(d.length) [c,d] = [d,polyRemainder(c,d,p)];
  if(!c.length) return [];
  const inv = Number(inverse(BigInt(c[c.length-1]!),BigInt(p)));
  return c.map(x=>fm(x*inv,p));
}
function polyPower(a: readonly number[], e: number, f: readonly number[], p: number): number[] {
  let b = polyRemainder(a,f,p); let out=[1];
  while(e>0) { if(e%2===1) out=polyRemainder(polyMultiply(out,b,p),f,p);
    b=polyRemainder(polyMultiply(b,b,p),f,p);e=Math.floor(e/2); }
  return out;
}
function prime(n: number): boolean {
  if(n<2) return false;
  for(let i=2;i*i<=n;i++) if(n%i===0) return false;
  return true;
}
const rows = certificate.rows.map(row => {
  const p=row[0], f=row[1], v=row[2];
  assert(typeof p==='number' && prime(p) && Array.isArray(f) && Array.isArray(v), 'Malformed row');
  return {p,f:f.map(Number),v:v.map(BigInt)};
});
assert(rows.length === 89, 'Wrong certificate count');
for(const {p,f,v} of rows) {
  assert(p!==2 && p!==5 && p**(f.length-1)<520 && integral(v), 'Ideal domain or integrality');
  assert(normNumerator(v) === BigInt(p)**BigInt(f.length-1)*4n**10n, 'Wrong norm');
  assert(polyRemainder(v.map(Number),f,p).length === 0, 'Generator not in claimed prime');
}
// Independently certify completeness, without a polynomial factorizer: for
// every possible residue degree, x^(p^d)-x detects exactly the dividing degrees.
for(let p=3;p<520;p++) {
  if(p===5 || !prime(p)) continue;
  const f=certificate.polynomial.map(a=>fm(a,p)); const present=rows.filter(row=>row.p===p);
  for(let d=1;p**d<520;d++) {
    const actual=polyGcd(f,polySubtract(polyPower([0,1],p**d,f,p),[0,1],p),p);
    let expected=[1];
    for(const row of present) if(d%(row.f.length-1)===0) expected=polyMultiply(expected,row.f,p);
    assert(actual.join(',')===expected.join(','),`Incomplete ideal inventory at ${p}, degree ${d}`);
  }
}
for(const row of certificate.ramified) {
  const p=row[0], v=row[1]; assert(typeof p==='number' && Array.isArray(v),'Malformed ramified row');
  const n=v.map(BigInt); assert(integral(n) && normNumerator(n)===BigInt(p)*4n**10n,'Ramified norm');
}
const basisDet=determinant(certificate.basis4.map(row=>row.map(BigInt)));
assert(basisDet*128n===4n**10n,'Wrong order determinant');
const disc=-(10n**10n)*(4n**9n)*basisDet**2n/(4n**20n);
assert(disc===-160000000000n,'Wrong order discriminant');
assert(14863564800n < 520n*28629151n,'Minkowski threshold');
const unitLogs=certificate.units.map(v=> {
  const n=v.map(BigInt); assert(integral(n) && normNumerator(n)===4n**10n,'Not an integral unit');
  const b=n.map(a=>mod(a*inverse(4n,289n),289n)); const out=ringPower(b,17**4-1,289n);
  out[0]=mod(out[0]!-1n,289n);assert(out.every(a=>a%17n===0n),'Invalid Fermat quotient');
  return out.map(a=>Number(a/17n));
});
assert(JSON.stringify(unitLogs)===JSON.stringify(certificate.unit_logs),'Wrong unit logarithms');
const columns=[...unitLogs, [1,...Array<number>(9).fill(0)], [...Array<number>(9).fill(0),1]];
const minor=certificate.rank_rows.map(i=>columns.map(c=>BigInt(c[i]!)));
assert(determinant(minor)===-28765n && mod(determinant(minor),17n)===16n,'Log independence failed');
assert(ringPower([0n,1n,...Array<bigint>(8).fill(0n)],17**4,17n).join(',')==='0,1,0,0,0,0,0,0,0,0','Frobenius failed');
function choose(n: number,k: number): bigint { let out=1n;
  for(let j=1;j<=k;j++) out=out*BigInt(n-j+1)/BigInt(j);return out; }
const fifth=new Set(Array.from({length:11},(_,a)=>Number(scalarPower(BigInt(a),5,11n))));
const gaussianCounts:number[]=[];
for(const [ca,cb,dg,dh] of [[1n,16n,1n,1n],[17n**4n,16n,17n,1n],[1n,16n*17n**4n,1n,17n]]) {
  assert(ca!==undefined&&cb!==undefined&&dg!==undefined&&dh!==undefined,'Missing Gaussian case');
  let count=0;
  for(let A=0;A<11;A++) for(let B=0;B<11;B++) {
    if(A===0&&B===0)continue;
    const a=ca*scalarPower(BigInt(A),5,11n)%11n,b=cb*scalarPower(BigInt(B),5,11n)%11n;
    let g=0n,h=0n;
    for(let j=0;j<=8;j++) { const sign=j%2===0?1n:-1n;
      g+=sign*choose(17,2*j)*a**BigInt(16-2*j)*b**BigInt(2*j);
      h+=sign*choose(17,2*j+1)*a**BigInt(16-2*j)*b**BigInt(2*j); }
    if(fifth.has(Number(mod(g*inverse(dg,11n),11n)))&&fifth.has(Number(mod(h*inverse(dh,11n),11n)))) {
      count++;assert(B===0&&A!==0,'Unexpected nonaxis survivor'); }
  }
  gaussianCounts.push(count);
}
assert(gaussianCounts.join(',')==='0,0,10','Incorrect Gaussian elimination');
// Full interpolation grid: both sides have degree <=10 in each variable.
for(let X=-5;X<=5;X++)for(let Y=-5;Y<=5;Y++) {
  const v=[4n*BigInt(X),...Array<bigint>(8).fill(0n),2n*BigInt(Y)];
  assert(normNumerator(v)===(BigInt(X)**10n+256n*BigInt(Y)**10n)*4n**10n,'Master norm identity');
}
const precision=9,modulus=17n**BigInt(precision);
const target=[1n,...Array<bigint>(8).fill(0n),mod(17n**2n*inverse(2n,modulus),modulus)];
let delta=[1n,...Array<bigint>(8).fill(0n),mod(17n*inverse(2n,modulus),modulus)];
for(let k=3;k<precision;k++) {
  const m=17n**BigInt(k+1),p=17n**BigInt(k), image=ringPower(delta,17,m);
  const errors=target.map((a,i)=>mod(a-image[i]!,m));assert(errors.every(a=>a%p===0n),'Insufficient lifting precision');
  delta=delta.map((a,i)=>mod(a+17n**BigInt(k-1)*(errors[i]!/p),m));
}
assert(ringPower(delta,17,modulus).join(',')===target.join(','),'17-adic survivor failure');
const summary={order_discriminant:Number(disc),minkowski_upper:'14863564800/28629151',
  unramified_prime_ideals_certified:89,ramified_prime_ideals_certified:3,unit_norms:[1,1,1,1],
  unit_logs:unitLogs,minor_determinant:-28765,minor_mod17:16,gaussian_case_counts:gaussianCounts,
  common_norm_identities:true,local_e17_equals2_survives:true,full_Beal_solved:false};
console.log(JSON.stringify({checkpoint:'U71',summary,local_17_root:delta.map(a=>a.toString())},null,2));
