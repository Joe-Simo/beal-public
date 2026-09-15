/** Exact checks for U60. Finite certificates, not a proof of Beal's conjecture. */
type Pair = readonly [bigint, bigint];
type Ring = readonly [bigint, bigint]; // w^2 = ring[0] + ring[1]*w
const gaussian: Ring = [-1n, 0n];
const quadratic: Ring = [1n, 1n];

function requireTrue(ok: boolean, message: string): asserts ok {
  if (!ok) throw new Error(message);
}
function mod(x: bigint, m: bigint): bigint {
  requireTrue(m > 0n, "Modulus must be positive");
  return ((x % m) + m) % m;
}
function mul(x: Pair, y: Pair, ring: Ring, m: bigint): Pair {
  const [a, b] = x;
  const [c, d] = y;
  return [mod(a*c + ring[0]*b*d, m), mod(a*d + b*c + ring[1]*b*d, m)];
}
function power(x: Pair, exponent: bigint, ring: Ring, m: bigint): Pair {
  requireTrue(exponent >= 0n, "Exponent must be nonnegative");
  let n = exponent;
  let base = x;
  let out: Pair = [1n, 0n];
  while (n > 0n) {
    if (n % 2n === 1n) out = mul(out, base, ring, m);
    base = mul(base, base, ring, m);
    n /= 2n;
  }
  return out;
}
function h(m: bigint, n: bigint, modulus: bigint): Pair {
  return [mod(m**4n + 30n*m*m*n*n + n**4n, modulus), mod(-16n*m*m*n*n, modulus)];
}
function key(x: Pair): string { return `${x[0]},${x[1]}`; }
function equal(x: Pair, y: Pair): boolean { return x[0] === y[0] && x[1] === y[1]; }
function gcd(x: bigint, y: bigint): bigint {
  let a = x < 0n ? -x : x;
  let b = y < 0n ? -y : y;
  while (b !== 0n) [a, b] = [b, a % b];
  return a;
}
function parseExact(x: unknown): bigint | null {
  if (typeof x === "bigint") return x;
  if (typeof x === "string" && /^[+-]?\d+$/.test(x)) return BigInt(x);
  if (typeof x === "number" && Number.isSafeInteger(x)) return BigInt(x);
  return null;
}
function checkBeal(input: readonly unknown[]): { admissible: boolean; equality: boolean; primitive: boolean; counterexample: boolean } {
  const invalid = { admissible: false, equality: false, primitive: false, counterexample: false };
  if (input.length !== 6) return invalid;
  const a=parseExact(input[0]), b=parseExact(input[1]), c=parseExact(input[2]);
  const x=parseExact(input[3]), y=parseExact(input[4]), z=parseExact(input[5]);
  if (a===null || b===null || c===null || x===null || y===null || z===null) return invalid;
  if (a<=0n || b<=0n || c<=0n || x<3n || y<3n || z<3n) return invalid;
  const equality = a**x + b**y === c**z;
  const primitive = gcd(gcd(a,b),c) === 1n;
  return { admissible: true, equality, primitive, counterexample: equality && primitive };
}

// Focused specification and boundary tests, not research discoveries.
requireTrue(equal(mul([0n,1n],[0n,1n],gaussian,289n),[288n,0n]), "Gaussian relation");
requireTrue(equal(mul([0n,1n],[0n,1n],quadratic,289n),[1n,1n]), "Quadratic relation");
requireTrue(equal(power([0n,1n],17n,quadratic,10000n),[987n,1597n]), "Fibonacci basis check");
requireTrue(equal(power([0n,0n],0n,quadratic,289n),[1n,0n]), "Polynomial x^0 convention");
const nonprimitive = checkBeal([3,6,3,3,3,5]);
requireTrue(nonprimitive.equality && !nonprimitive.counterexample, "Nonprimitive equality");
requireTrue(!checkBeal([3,10,7,5,2,3]).admissible, "Exponent two excluded");
requireTrue(!checkBeal([2,3,4,3,3,3]).equality, "Arithmetic mismatch");
for (const bad of [0,-1,1.5,"1.2",true,9007199254740992]) {
  requireTrue(!checkBeal([bad,3,4,3,3,3]).admissible, "Invalid/unsafe integer rejected");
}
requireTrue(checkBeal([2n**60n,2n**60n,2n,3n,3n,181n]).equality, "Beyond binary64 exactness");
requireTrue(parseExact("9007199254740993")===9007199254740993n, "Decimal serialization");
requireTrue(checkBeal([1,2,3,3,3,3]).admissible, "Base one retained");

// Complete residue domain: all 289 alpha residues and all 288 primitive Gaussian residues.
const alphaImages = new Set<string>();
for (let a=0n;a<17n;a++) for (let b=0n;b<17n;b++) alphaImages.add(key(power([a,b],17n,quadratic,289n)));
requireTrue(alphaImages.size===289, "All alpha images, including zero-coordinate cases");
const survivors: string[][] = [];
for (let r=0n;r<17n;r++) for (let s=0n;s<17n;s++) {
  if (r===0n && s===0n) continue;
  const [m,n]=power([r,s],17n,gaussian,289n);
  const compatible=alphaImages.has(key(h(m,n,289n)));
  requireTrue(compatible===(r===0n || s===0n), "Mod289 survivor classification");
  if (compatible) survivors.push([r.toString(),s.toString()]);
}
requireTrue(survivors.length===32, "Exactly the 32 nonzero axis residues survive");

// Polynomial Bezout certificate over F_17; coefficients are in increasing degree order.
function polyMul(a: readonly bigint[], b: readonly bigint[]): bigint[] {
  const c = new Array<bigint>(a.length+b.length-1).fill(0n);
  for (let i=0;i<a.length;i++) for (let j=0;j<b.length;j++) c[i+j]=(c[i+j]??0n)+(a[i]??0n)*(b[j]??0n);
  return c;
}
const R=[1n,4n,-1n,3n,-1n,4n,1n];
const U=[-1n,-4n,-1n,1n,1n,-1n,1n,1n];
const V=[-2n,-8n,1n,-2n,-5n,-1n];
const T=[-1n,0n,0n,0n,0n,0n,0n,0n,1n];
const ur=polyMul(U,R), vt=polyMul(V,T);
for (let i=0;i<Math.max(ur.length,vt.length);i++) requireTrue(mod((ur[i]??0n)+(vt[i]??0n),17n)===(i===0?1n:0n), "Bezout coefficient identity");

const p16coeff=[17n,136n,1360n,7140n,30940n,99008n,252824n,510510n,826540n,1069640n,1101464n,891072n,554540n,256360n,82960n,16779n,1597n];
function p16(a: bigint,b: bigint): bigint {
  return p16coeff.reduce((out,c,j)=>out+c*a**BigInt(16-j)*b**BigInt(j),0n);
}
const rootCounts: {q: string; finiteRoots: string[]; infinityIsRoot: boolean}[]=[];
for (const q of [67n,103n,409n,883n]) {
  const roots: string[]=[];
  for (let a=0n;a<q;a++) if (mod(p16(a,1n),q)===0n) roots.push(a.toString());
  requireTrue(roots.length===(q===103n?0:16), "Unrestricted projective root count");
  const infinityIsRoot=mod(p16(1n,0n),q)===0n;
  requireTrue(!infinityIsRoot,"Point at infinity checked");
  rootCounts.push({q:q.toString(),finiteRoots:roots,infinityIsRoot});
}
// A=57 is permitted by A=1 mod8, and b=8. b^2/A need not be a square.
const parameter=mod(64n*47n,103n); // 57*47 = 1 mod103
requireTrue(mod(57n*47n,103n)===1n,"Inverse witness");
requireTrue(mod(parameter**51n,103n)===102n,"Normalization counterexample");

console.log(JSON.stringify({status:"completed",arithmetic:"bigint",alphaImageSize:alphaImages.size,gaussianInputs:288,survivorCount:survivors.length,survivors,bezoutVerified:true,rootCounts,normalizationCounterexample:{A:"57",b:"8",q:"103",parameter:parameter.toString()},fullBealSolved:false},null,2));
