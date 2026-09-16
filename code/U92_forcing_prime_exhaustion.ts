export {};

/**
 * U92 exact finite certificate for the U72 Gaussian case-III forcing-prime sieve.
 *
 * For q ≡ 1 (mod 5), a nonzero B passing the two fifth-power tests means q is
 * not forced into Y by this particular finite-field criterion.  The script
 * exhausts all such primes below 10^7, records an explicit nonzero witness for
 * every non-forcing prime, and exhausts every residue B at the fourteen
 * forcing primes.  The companion written proof uses a genus-1576 Kummer cover
 * and Hasse-Weil above 9,936,802, so the finite scan overlaps the theoretical
 * range.  This does not solve the weighted equation or Beal's conjecture.
 */

const LIMIT = 10_000_000;
const WITNESS_LIMIT = 1000;
const K = 16 * 17 ** 4;

// G(v), H(v), ascending coefficient order.
const G = [1, -136, 2380, -12376, 24310, -19448, 6188, -680, 17] as const;
const H = [17, -680, 6188, -19448, 24310, -12376, 2380, -136, 1] as const;
const expectedForcing = [11, 31, 41, 61, 71, 101, 151, 191, 211, 281, 331, 431, 461, 631] as const;

function mod(a: number, p: number): number {
  const r = a % p;
  return r < 0 ? r + p : r;
}

// Every intermediate product is < 10^14, safely below Number.MAX_SAFE_INTEGER.
function mulMod(a: number, b: number, p: number): number {
  return (a * b) % p;
}

function powMod(a: number, exponent: number, p: number): number {
  let base = mod(a, p);
  let e = exponent;
  let out = 1;
  while (e > 0) {
    if (e & 1) out = mulMod(out, base, p);
    base = mulMod(base, base, p);
    e = Math.floor(e / 2);
  }
  return out;
}

function inverseMod(a: number, p: number): number {
  return powMod(a, p - 2, p);
}

function evaluatePolynomial(coefficients: readonly number[], x: number, p: number): number {
  let out = 0;
  for (let i = coefficients.length - 1; i >= 0; i -= 1) {
    out = mod(mulMod(out, x, p) + coefficients[i]!, p);
  }
  return out;
}

function fifthPowerOfBase(B: number, p: number): number {
  const square = mulMod(B, B, p);
  return mulMod(mulMod(square, square, p), B, p);
}

function isFifthPower(value: number, p: number, exponent: number): boolean {
  return value === 0 || powMod(value, exponent, p) === 1;
}

function survives(p: number, B: number): boolean {
  if (p % 5 !== 1 || p === 17 || B < 0 || B >= p) throw new Error("invalid finite-field input");
  const fifthExponent = (p - 1) / 5;
  const b = mulMod(K % p, fifthPowerOfBase(B, p), p);
  const v = mulMod(b, b, p);
  const g = evaluatePolynomial(G, v, p);
  if (!isFifthPower(g, p, fifthExponent)) return false;
  const h = mulMod(evaluatePolynomial(H, v, p), inverseMod(17, p), p);
  return isFifthPower(h, p, fifthExponent);
}

// Exact sieve of Eratosthenes to 10^7.
const composite = new Uint8Array(LIMIT);
const primes: number[] = [];
for (let i = 2; i < LIMIT; i += 1) {
  if (composite[i]) continue;
  primes.push(i);
  if (i * i < LIMIT) {
    for (let j = i * i; j < LIMIT; j += i) composite[j] = 1;
  }
}

const forcing: number[] = [];
let relevantPrimeCount = 0;
let largestFirstWitness = 0;
let largestFirstWitnessPrime = 0;

for (const p of primes) {
  if (p % 5 !== 1) continue;
  relevantPrimeCount += 1;
  let witness = 0;
  const bound = Math.min(WITNESS_LIMIT, p - 1);
  for (let B = 1; B <= bound; B += 1) {
    if (survives(p, B)) {
      witness = B;
      break;
    }
  }
  if (witness === 0) {
    forcing.push(p);
  } else if (witness > largestFirstWitness) {
    largestFirstWitness = witness;
    largestFirstWitnessPrime = p;
  }
}

if (relevantPrimeCount !== 166_104) throw new Error("unexpected prime count");
if (JSON.stringify(forcing) !== JSON.stringify(expectedForcing)) throw new Error("forcing list mismatch");
if (largestFirstWitness !== 370 || largestFirstWitnessPrime !== 2_344_241) {
  throw new Error("witness maximum mismatch");
}

// At the fourteen candidate forcing primes, do not rely on the B≤1000 cutoff:
// exhaust every residue and prove the only survivor is B=0.
const exactForcingSurvivors: Record<string, number[]> = {};
for (const p of forcing) {
  const rows: number[] = [];
  for (let B = 0; B < p; B += 1) {
    if (survives(p, B)) rows.push(B);
  }
  if (rows.length !== 1 || rows[0] !== 0) throw new Error(`unexpected survivor at ${p}`);
  exactForcingSurvivors[String(p)] = rows;
}

// Companion Hasse-Weil proof: genus g=1576, at most 850 rational points
// above all branch fibres.  We need q+1-3152 sqrt(q)>850.  For q>849
// this follows from (q-849)^2 > 3152^2 q.
let hasseThreshold = 850;
while ((hasseThreshold - 849) ** 2 <= 3152 ** 2 * hasseThreshold) hasseThreshold += 1;
if (hasseThreshold !== 9_936_802) throw new Error("Hasse threshold mismatch");
if (hasseThreshold >= LIMIT) throw new Error("finite/theoretical ranges do not overlap");

console.log(JSON.stringify({
  checkpoint: "U92",
  finiteScan: {
    limitExclusive: LIMIT,
    qCongruent1Mod5Count: relevantPrimeCount,
    witnessSearchBound: WITNESS_LIMIT,
    forcingPrimes: forcing,
    exactForcingSurvivors,
    largestFirstWitness,
    largestFirstWitnessPrime,
  },
  theoreticalOverlap: {
    genus: 1576,
    branchPointCap: 850,
    hasseWeilCoefficient: 3152,
    allPrimesAtLeast: hasseThreshold,
  },
  fullBealSolved: false,
}, null, 2));
