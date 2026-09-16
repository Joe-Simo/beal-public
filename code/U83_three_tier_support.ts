export {};

type Cycles = number[];
const units10 = [1, 3, 7, 9] as const;
const orders17 = [1, 2, 4, 8, 16] as const;

function mod(a: number, n: number): number {
  const r = a % n;
  return r < 0 ? r + n : r;
}

function powMod(base: number, exponent: number, modulus: number): number {
  let b = mod(base, modulus);
  let e = exponent;
  let out = 1;
  while (e > 0) {
    if ((e & 1) !== 0) out = (out * b) % modulus;
    b = (b * b) % modulus;
    e >>= 1;
  }
  return out;
}

function order17(h: number): number {
  for (const r of orders17) if (powMod(h, r, 17) === 1) return r;
  throw new Error(`No order for ${h}`);
}

function cycleLengths(a: number, t: number): Cycles {
  const seen = Array<boolean>(10).fill(false);
  const out: number[] = [];
  for (let start = 0; start < 10; start += 1) {
    if (seen[start]) continue;
    let j = start;
    let n = 0;
    while (!seen[j]) {
      seen[j] = true;
      n += 1;
      j = mod(a * j + t, 10);
    }
    out.push(n);
  }
  return out.sort((u, v) => u - v);
}

function key(xs: Cycles): string { return xs.join(","); }
function isClean(cycles: Cycles, r: number): boolean { return cycles.every((d) => d % r !== 0); }

const cycleHistogram = new Map<string, number>();
const rows: Array<{a:number;t:number;h:number;r:number;cycle:string;category:string}> = [];
const counts = new Map<string, number>([["strong",0],["semi",0],["weak",0],["uncontrolled",0]]);

for (const a of units10) {
  for (let t = 0; t < 10; t += 1) {
    const cycles = cycleLengths(a, t);
    cycleHistogram.set(key(cycles), (cycleHistogram.get(key(cycles)) ?? 0) + 1);
    for (let h = 1; h < 17; h += 1) {
      const r = order17(h);
      const strong = isClean(cycles, r) || (r === 1 && key(cycles) === "10");
      const semi = !strong && ((r === 1 && key(cycles) === "5,5") || (r === 2 && key(cycles) === "10"));
      const weak = !strong && !semi && r === 1 && (t & 1) === 1;
      const category = strong ? "strong" : semi ? "semi" : weak ? "weak" : "uncontrolled";
      counts.set(category, (counts.get(category) ?? 0) + 1);
      rows.push({a,t,h,r,cycle:key(cycles),category});
    }
  }
}

const expectedHistogram = new Map<string, number>([
  ["1,1,1,1,1,1,1,1,1,1", 1], ["10", 4], ["5,5", 4],
  ["2,2,2,2,2", 6], ["1,1,4,4", 10], ["2,4,4", 10], ["1,1,2,2,2,2", 5],
]);
for (const [k, v] of expectedHistogram) if (cycleHistogram.get(k) !== v) throw new Error(`cycle histogram mismatch ${k}`);
if (rows.length !== 640) throw new Error(`Expected 640 Frobenius pairs, got ${rows.length}`);

for (const [k, v] of new Map<string, number>([["strong",529],["semi",8],["weak",16],["uncontrolled",87]])) {
  if (counts.get(k) !== v) throw new Error(`category count mismatch ${k}`);
}

const semiRows = rows.filter((r) => r.category === "semi");
if (semiRows.filter((r) => r.r === 1 && r.cycle === "5,5").length !== 4) throw new Error("semi 5,5 count");
if (semiRows.filter((r) => r.r === 2 && r.cycle === "10").length !== 4) throw new Error("semi 10 count");
const weakRows = rows.filter((r) => r.category === "weak");
if (!weakRows.every((r) => r.r === 1 && (r.t & 1) === 1 && r.cycle !== "10")) throw new Error("weak structural condition");

const controlled = (counts.get("strong") ?? 0) + (counts.get("semi") ?? 0) + (counts.get("weak") ?? 0);
if (controlled !== 553) throw new Error("controlled count");

const b4Numerator = -1100n;
const b9Numerator = 658767450n;
if (b4Numerator !== -4n * 25n * 11n) throw new Error("B4 numerator factorization");
if (b9Numerator !== 2n * 3n * 25n * 11n * 59n * 67n * 101n) throw new Error("B9 numerator factorization");

console.log(JSON.stringify({
  checkpoint: "U83",
  cycleTypes: Object.fromEntries([...cycleHistogram.entries()].sort()),
  categoryCounts: Object.fromEntries(counts),
  strongDensity: "529/640",
  semiDensity: "1/80",
  weakDensity: "1/40",
  controlledUnionDensity: "553/640",
  uncontrolledDensity: "87/640",
  b4Numerator: b4Numerator.toString(),
  b9Numerator: b9Numerator.toString(),
  fullBealSolved: false,
}, null, 2));
