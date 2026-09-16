/**
 * U81 exact finite certificates for the clean-prime density theorem.
 *
 * This enumerates the 40 affine permutations j -> a*j+t on Z/10Z,
 * counts their cycle types, combines them with the possible orders in
 * (Z/17Z)^*, and checks the finite prime set inherited from U72.
 * It does not prove Chebotarev, the Galois-group identification, or Beal.
 */
export {};

type CycleKey = string;

const units10 = [1, 3, 7, 9] as const;
const residues = Array.from({ length: 10 }, (_, i) => i);

function mod(a: number, n: number): number {
  const r = a % n;
  return r < 0 ? r + n : r;
}

function cycleLengths(a: number, t: number): number[] {
  const seen = Array<boolean>(10).fill(false);
  const out: number[] = [];
  for (const start of residues) {
    if (seen[start]) continue;
    let j = start;
    let length = 0;
    while (!seen[j]) {
      seen[j] = true;
      length += 1;
      j = mod(a * j + t, 10);
    }
    out.push(length);
  }
  return out.sort((x, y) => x - y);
}

function key(xs: number[]): CycleKey {
  return xs.join(",");
}

function powMod(base: number, exponent: number, modulus: number): number {
  let b = mod(base, modulus);
  let e = exponent;
  let out = 1;
  while (e > 0) {
    if (e & 1) out = (out * b) % modulus;
    b = (b * b) % modulus;
    e >>= 1;
  }
  return out;
}

function multiplicativeOrder17(q: number): number {
  if (q % 17 === 0) throw new Error("17 has no order modulo 17");
  for (const d of [1, 2, 4, 8, 16]) {
    if (powMod(q, d, 17) === 1) return d;
  }
  throw new Error(`No order found for ${q}`);
}

const allCycles: number[][] = [];
const cycleCounts = new Map<CycleKey, number>();
for (const a of units10) {
  for (let t = 0; t < 10; t += 1) {
    const cycles = cycleLengths(a, t);
    allCycles.push(cycles);
    const k = key(cycles);
    cycleCounts.set(k, (cycleCounts.get(k) ?? 0) + 1);
  }
}

const expectedCycleCounts = new Map<CycleKey, number>([
  ["1,1,1,1,1,1,1,1,1,1", 1],
  ["10", 4],
  ["5,5", 4],
  ["2,2,2,2,2", 6],
  ["1,1,4,4", 10],
  ["2,4,4", 10],
  ["1,1,2,2,2,2", 5],
]);

if (cycleCounts.size !== expectedCycleCounts.size) throw new Error("Unexpected cycle-type count");
for (const [k, v] of expectedCycleCounts) {
  if (cycleCounts.get(k) !== v) throw new Error(`Cycle count mismatch for ${k}`);
}
if (allCycles.length !== 40) throw new Error("Affine group must have 40 elements");

function cleanGroupElements(order: number): number {
  return allCycles.filter((cycles) => cycles.every((f) => f % order !== 0)).length;
}

const cleanByOrder = new Map<number, number>([
  [1, cleanGroupElements(1)],
  [2, cleanGroupElements(2)],
  [4, cleanGroupElements(4)],
  [8, cleanGroupElements(8)],
  [16, cleanGroupElements(16)],
]);

const expectedClean = new Map<number, number>([
  [1, 0],
  [2, 5],
  [4, 20],
  [8, 40],
  [16, 40],
]);
for (const [order, count] of expectedClean) {
  if (cleanByOrder.get(order) !== count) throw new Error(`Clean-count mismatch for order ${order}`);
}

const numerator = 1 * 0 + 1 * 5 + 2 * 20 + 4 * 40 + 8 * 40;
const denominator = 16 * 40;
if (numerator !== 525 || denominator !== 640) throw new Error("Density numerator/denominator mismatch");
if (numerator * 128 !== denominator * 105) throw new Error("Density reduction mismatch");

const forced = [11, 31, 41, 61, 71, 101, 151, 191, 211, 281, 331, 431, 461, 631] as const;
const forcedRows = forced.map((q) => {
  if (q % 5 !== 1) throw new Error(`${q} is not 1 mod 5`);
  const d = q % 4 === 1 ? 5 : 10;
  const residue = powMod(q, d, 17);
  if (residue === 1) throw new Error(`${q} fails the clean sufficient test`);
  return { q, qMod17: q % 17, order17: multiplicativeOrder17(q), degreeBound: d, qPowDegreeMod17: residue };
});

const forcedProduct = forced.reduce((acc, q) => acc * BigInt(q), 1n);
if (forcedProduct !== 433992707035920672833426144791n) throw new Error("Forced product mismatch");

const b9Numerator = 658767450n;
if (b9Numerator !== 2n * 3n * 5n * 5n * 11n * 59n * 67n * 101n) {
  throw new Error("B9 numerator factorization mismatch");
}

console.log(JSON.stringify({
  checkpoint: "U81",
  affineGroupOrder: allCycles.length,
  cycleTypes: Object.fromEntries([...cycleCounts.entries()].sort()),
  cleanGroupElementsByCyclotomicOrder: Object.fromEntries(cleanByOrder),
  cleanPrimeDensity: "105/128",
  forcedPrimeRows: forcedRows,
  forcedProduct: forcedProduct.toString(),
  b9Numerator: b9Numerator.toString(),
  fullBealSolved: false,
}, null, 2));
