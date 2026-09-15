/** Independent exact checks of U61 residue exclusions and elliptic reductions. */
type Pair = readonly [bigint, bigint];
type Point = readonly [Pair, Pair] | null;
const assert: (condition: boolean, message: string) => asserts condition = (condition, message) => {
  if (!condition) throw new Error(message);
};
const mod = (a: bigint, n: bigint): bigint => ((a % n) + n) % n;
function inverse(a: bigint, modulus: bigint): bigint {
  let r = modulus; let s = mod(a, modulus); let t = 0n; let u = 1n;
  while (s !== 0n) {
    const q = r / s;
    [r, s] = [s, r - q * s];
    [t, u] = [u, t - q * u];
  }
  if (r !== 1n) throw new Error('Nonunit inverse');
  return mod(t, modulus);
}
function power(a: bigint, n: bigint, modulus: bigint): bigint {
  let b = mod(a, modulus); let out = 1n;
  while (n > 0n) {
    if ((n & 1n) !== 0n) out = out * b % modulus;
    b = b * b % modulus; n >>= 1n;
  }
  return out;
}
class Field {
  readonly zero: Pair = [0n, 0n];
  readonly one: Pair = [1n, 0n];
  readonly pi: Pair = [0n, 1n];
  readonly elements: Pair[] = [];
  constructor(readonly p: bigint) {
    assert(power(17n, (p - 1n) / 2n, p) === p - 1n, '17 must be a nonsquare');
    for (let a = 0n; a < p; ++a) for (let b = 0n; b < p; ++b) this.elements.push([a, b]);
  }
  constant(a: bigint): Pair { return [mod(a, this.p), 0n]; }
  add(a: Pair, b: Pair): Pair { return [mod(a[0] + b[0], this.p), mod(a[1] + b[1], this.p)]; }
  neg(a: Pair): Pair { return [mod(-a[0], this.p), mod(-a[1], this.p)]; }
  sub(a: Pair, b: Pair): Pair { return this.add(a, this.neg(b)); }
  mul(a: Pair, b: Pair): Pair {
    return [mod(a[0] * b[0] + 17n * a[1] * b[1], this.p), mod(a[0] * b[1] + a[1] * b[0], this.p)];
  }
  div(a: Pair, b: Pair): Pair {
    const n = inverse(b[0] * b[0] - 17n * b[1] * b[1], this.p);
    return this.mul(a, [mod(b[0] * n, this.p), mod(-b[1] * n, this.p)]);
  }
  eq(a: Pair, b: Pair): boolean { return a[0] === b[0] && a[1] === b[1]; }
}
function ellipticAudit(p: bigint) {
  const f = new Field(p); const c = (a: bigint): Pair => f.constant(a);
  const a = f.sub(c(4n), f.pi);
  const b = f.add(c(-8n), f.div(f.mul(c(33n), f.pi), c(17n)));
  const base: Point = [f.sub(f.div(c(17n), c(4n)), f.pi),
    f.add(c(-16n), f.div(f.mul(c(31n), f.pi), c(8n)))];
  const rhs = (x: Pair): Pair => f.mul(x, f.add(f.mul(x, f.add(x, a)), b));
  const onCurve = (point: Point): boolean => point === null || f.eq(f.mul(point[1], point[1]), rhs(point[0]));
  const add = (p1: Point, p2: Point): Point => {
    if (p1 === null) return p2;
    if (p2 === null) return p1;
    const [x, y] = p1; const [u, v] = p2;
    if (f.eq(x, u) && f.eq(f.add(y, v), f.zero)) return null;
    const slope = f.eq(x, u)
      ? f.div(f.add(f.add(f.mul(c(3n), f.mul(x, x)), f.mul(c(2n), f.mul(a, x))), b), f.mul(c(2n), y))
      : f.div(f.sub(v, y), f.sub(u, x));
    const xx = f.sub(f.sub(f.sub(f.mul(slope, slope), a), x), u);
    const yy = f.sub(f.mul(slope, f.sub(x, xx)), y);
    const out: Point = [xx, yy]; assert(onCurve(out), 'Addition must preserve curve');
    return out;
  };
  for (const x of f.elements) {
    if (!f.eq(x, f.zero)) assert(f.eq(f.div(x, x), f.one), 'Field inverse identity');
  }
  assert(onCurve(base), 'P lies on E');
  assert(add([f.zero, f.zero], [f.zero, f.zero]) === null, 'T has order two');
  const discriminant = f.mul(c(16n), f.mul(f.mul(b, b), f.sub(f.mul(a, a), f.mul(c(4n), b))));
  assert(!f.eq(discriminant, f.zero), 'Good reduction');
  const points: Point[] = [null];
  for (const x of f.elements) for (const y of f.elements) {
    if (onCurve([x, y])) points.push([x, y]);
  }
  let q: Point = null; let order = 0;
  do { q = add(q, base); ++order; } while (q !== null && order <= points.length);
  assert(q === null && points.length % order === 0, 'P order divides group size');
  const rationalResidues: {point: Point; u: Pair}[] = [];
  if (p === 3n || p === 5n) {
    const a4 = f.sub(c(1n), f.div(f.mul(c(4n), f.pi), c(17n)));
    const d4 = f.sub(c(6n), f.pi); const twoB4 = f.sub(c(13n), f.mul(c(3n), f.pi));
    for (const point of points) {
      let u: Pair = c(2n);
      if (point !== null) {
        const xx = f.add(point[0], f.div(f.sub(f.pi, c(5n)), c(2n)));
        const denominator = f.sub(f.mul(xx, xx), f.mul(c(4n), a4));
        assert(!f.eq(denominator, f.zero), 'Inverse map has no finite pole over the residue field');
        const numerator = f.add(f.add(f.mul(c(2n), point[1]), f.mul(d4, xx)), twoB4);
        u = f.add(c(2n), f.div(numerator, denominator));
      }
      if (u[1] === 0n) rationalResidues.push({point, u});
    }
    assert(rationalResidues.length === 2, 'Exactly two rational-coordinate disks');
    assert(rationalResidues.every(row => f.eq(row.u, c(2n))), 'Both disks map to u=2');
  }
  return {p, extensionDegree: 2, fieldPolynomial: 'pi^2-17', points: points.length,
    orderP: order, reducedP: base, rationalCoordinateResidues: rationalResidues};
}
function localAudit(modulus: bigint, root: bigint) {
  const a = mod(-34n * (4n - root), modulus);
  const eps = mod(4n + root, modulus);
  const b = mod(17n * root * power(inverse(eps, modulus), 3n, modulus), modulus);
  const squares = new Set<bigint>();
  for (let i = 0n; i < modulus; ++i) squares.add(i * i % modulus);
  const classes: {sign: bigint; e: bigint; f: bigint; gamma: bigint; pairs: bigint}[] = [];
  for (const sign of [1n, -1n]) for (const e of [0n, 1n]) for (const f of [0n, 1n]) {
    const gamma = mod(sign * eps ** e * root ** f, modulus);
    const bOverGamma = mod(b * inverse(gamma, modulus), modulus); let pairs = 0n;
    for (let u = 0n; u < modulus; ++u) for (let v = 0n; v < modulus; ++v) {
      if ((u % 2n !== 0n || v % 2n !== 0n)
        && squares.has(mod(gamma * u ** 4n + a * u * u * v * v + bOverGamma * v ** 4n, modulus))) ++pairs;
    }
    classes.push({sign, e, f, gamma, pairs});
  }
  return {modulus, root, aDual: a, bDual: b, classes};
}
const elliptic = [3n, 5n, 7n].map(ellipticAudit);
assert(elliptic[0]?.points === 8 && elliptic[0]?.orderP === 8, 'F9 check');
assert(elliptic[1]?.points === 22 && elliptic[1]?.orderP === 22, 'F25 check');
assert(elliptic[2]?.points === 60 && elliptic[2]?.orderP === 20, 'F49 check');
const local = [localAudit(16n, 7n), localAudit(64n, 41n)];
const localSets = local.map(row => new Set(row.classes.filter(c => c.pairs > 0n)
  .map(c => `${c.sign},${c.e},${c.f}`)));
const first = localSets[0]; const second = localSets[1];
assert(first !== undefined && second !== undefined, 'Both split places tested');
const intersection = [...first].filter(c => second.has(c)).sort();
assert(intersection.join(';') === '1,0,0;1,1,1', 'Partner image upper bound is {1,eps*pi}');
console.log(JSON.stringify({status: 'completed', arithmetic: 'bigint', elliptic, twoAdic: local},
  (_key: string, value: unknown) => typeof value === 'bigint' ? value.toString() : value, 2));
