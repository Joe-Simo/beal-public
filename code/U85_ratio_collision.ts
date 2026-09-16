export {};

function binomial2(n: number): number { return n * (n - 1) / 2; }
function gcd(a: number, b: number): number {
  let x = Math.abs(a), y = Math.abs(b);
  while (y !== 0) [x, y] = [y, x % y];
  return x;
}

const conjugates = 10;
const orderedRatios = conjugates * (conjugates - 1);
const residueValues = 17;
if (orderedRatios !== 90) throw new Error('ordered ratio count');

const q = Math.floor(orderedRatios / residueValues);
const r = orderedRatios % residueValues;
const minimumCollisionPairs = r * binomial2(q + 1) + (residueValues - r) * binomial2(q);
if (q !== 5 || r !== 5 || minimumCollisionPairs !== 195) throw new Error('balanced collision count');

const valuationMultiplier = 2 * minimumCollisionPairs;
if (valuationMultiplier !== 390) throw new Error('valuation multiplier');

const comparisonPairs = binomial2(orderedRatios);
const squaredDifferenceFactors = 2 * comparisonPairs;
const thetaMagnitudeExponent = 2 * squaredDifferenceFactors;
if (comparisonPairs !== 4005 || squaredDifferenceFactors !== 8010 || thetaMagnitudeExponent !== 16020) {
  throw new Error('height exponents');
}

const raisedYExponent = 17 * valuationMultiplier;
const raisedTwoExponent = 17 * squaredDifferenceFactors;
const common = gcd(raisedYExponent, thetaMagnitudeExponent);
if (raisedYExponent !== 6630 || raisedTwoExponent !== 136170 || common !== 30) throw new Error('raised exponents');
if (raisedYExponent / common !== 221 || thetaMagnitudeExponent / common !== 534 || raisedTwoExponent / common !== 4539) {
  throw new Error('simplified exponents');
}

console.log(JSON.stringify({
  checkpoint: 'U85',
  conjugates,
  orderedRatios,
  seventeenthRootValues: residueValues,
  balancedOccupancies: {low:q, high:q+1, highBins:r, lowBins:residueValues-r},
  minimumCollisionPairs,
  valuationMultiplier,
  comparisonPairs,
  squaredDifferenceFactors,
  thetaMagnitudeExponent,
  simplifiedHeightInequality: 'Y_*^221 <= 2^4539 * H^534',
  fullBealSolved: false,
}, null, 2));
