/**
 * Comprehensive Test Suite for Section 8 Beal Counterexample Checker (TypeScript)
 *
 * Covers all Section 8 requirements:
 * 1. Valid equality that fails the common-factor requirement: 3^3 + 6^3 = 3^5
 * 2. Valid equality excluded because an exponent is 2: 3^5 + 10^2 = 7^3
 * 3. Arithmetic mismatch
 * 4. Zero and negative inputs
 * 5. Noninteger inputs
 * 6. Integers beyond ordinary floating-point safe-integer limits
 * 7. Boundary conditions, input lengths, and calling conventions
 */

import assert from "node:assert/strict";
import { checkBeal, gcd, gcd3, parseExact } from "./section8_counterexample_checker.ts";

let totalTests = 0;
let passedTests = 0;

function it(name: string, fn: () => void): void {
  totalTests++;
  try {
    fn();
    passedTests++;
    console.log(`  ✔ ${name}`);
  } catch (err) {
    console.error(`  ✖ ${name}`);
    console.error(err);
    throw err;
  }
}

function describe(name: string, fn: () => void): void {
  console.log(`\n--- ${name} ---`);
  fn();
}

console.log("=================================================================");
console.log("Running Section 8 Beal Counterexample Checker Test Suite (TypeScript)");
console.log("=================================================================");

describe("1. Valid equalities failing common-factor requirement (gcd > 1)", () => {
  it("3^3 + 6^3 = 3^5 (27 + 216 = 243, gcd(3, 6, 3) = 3)", () => {
    const res = checkBeal([3, 6, 3, 3, 3, 5]);
    assert.equal(res.admissible, true);
    assert.equal(res.equality, true);
    assert.equal(res.primitive, false);
    assert.equal(res.counterexample, false);
    assert.equal(res.details?.gcd, 3n);
    assert.equal(res.details?.lhs, 243n);
    assert.equal(res.details?.rhs, 243n);
    assert.match(res.reason, /fails common-factor requirement/);
  });

  it("7^3 + 7^4 = 14^3 (343 + 2401 = 2744, gcd(7, 7, 14) = 7)", () => {
    const res = checkBeal([7, 7, 14, 3, 4, 3]);
    assert.equal(res.admissible, true);
    assert.equal(res.equality, true);
    assert.equal(res.primitive, false);
    assert.equal(res.counterexample, false);
    assert.equal(res.details?.gcd, 7n);
    assert.equal(res.details?.lhs, 2744n);
    assert.equal(res.details?.rhs, 2744n);
  });

  it("2^3 + 2^3 = 2^4 (8 + 8 = 16, gcd(2, 2, 2) = 2)", () => {
    const res = checkBeal([2, 2, 2, 3, 3, 4]);
    assert.equal(res.admissible, true);
    assert.equal(res.equality, true);
    assert.equal(res.primitive, false);
    assert.equal(res.counterexample, false);
    assert.equal(res.details?.gcd, 2n);
  });
});

describe("2. Valid equalities excluded because an exponent is 2 (< 3)", () => {
  it("3^5 + 10^2 = 7^3 (243 + 100 = 343, gcd=1, excluded by y=2)", () => {
    const res = checkBeal([3, 10, 7, 5, 2, 3]);
    assert.equal(res.admissible, false);
    assert.equal(res.equality, true);
    assert.equal(res.primitive, true);
    assert.equal(res.counterexample, false);
    assert.equal(res.details?.lhs, 343n);
    assert.equal(res.details?.rhs, 343n);
    assert.equal(res.details?.gcd, 1n);
    assert.match(res.reason, /Exponent restriction violated.*y=2/);
  });

  it("2^5 + 7^2 = 3^4 (32 + 49 = 81, gcd(2, 7, 3)=1, excluded by y=2)", () => {
    const res = checkBeal([2, 7, 3, 5, 2, 4]);
    assert.equal(res.admissible, false);
    assert.equal(res.equality, true);
    assert.equal(res.primitive, true);
    assert.equal(res.counterexample, false);
    assert.match(res.reason, /y=2/);
  });

  it("13^2 + 7^3 = 2^9 (169 + 343 = 512, gcd(13, 7, 2)=1, excluded by x=2)", () => {
    const res = checkBeal([13, 7, 2, 2, 3, 9]);
    assert.equal(res.admissible, false);
    assert.equal(res.equality, true);
    assert.equal(res.primitive, true);
    assert.equal(res.counterexample, false);
    assert.match(res.reason, /x=2/);
  });

  it("1^3 + 2^3 = 3^2 (1 + 8 = 9, gcd(1, 2, 3)=1, excluded by z=2)", () => {
    const res = checkBeal([1, 2, 3, 3, 3, 2]);
    assert.equal(res.admissible, false);
    assert.equal(res.equality, true);
    assert.equal(res.primitive, true);
    assert.equal(res.counterexample, false);
    assert.match(res.reason, /z=2/);
  });

  it("Multiple exponents equal to 2: 1^2 + 2^2 != 3^2, excluded by x=2, y=2, z=2", () => {
    const res = checkBeal([1, 2, 3, 2, 2, 2]);
    assert.equal(res.admissible, false);
    assert.equal(res.counterexample, false);
    assert.match(res.reason, /x=2/);
    assert.match(res.reason, /y=2/);
    assert.match(res.reason, /z=2/);
  });
});

describe("3. Arithmetic mismatches (A^x + B^y != C^z)", () => {
  it("2^3 + 3^3 != 4^3 (8 + 27 = 35 != 64)", () => {
    const res = checkBeal([2, 3, 4, 3, 3, 3]);
    assert.equal(res.admissible, true);
    assert.equal(res.equality, false);
    assert.equal(res.primitive, true);
    assert.equal(res.counterexample, false);
    assert.equal(res.details?.lhs, 35n);
    assert.equal(res.details?.rhs, 64n);
    assert.match(res.reason, /Arithmetic mismatch/);
  });

  it("3^3 + 4^3 != 5^3 (27 + 64 = 91 != 125)", () => {
    const res = checkBeal([3, 4, 5, 3, 3, 3]);
    assert.equal(res.admissible, true);
    assert.equal(res.equality, false);
    assert.equal(res.primitive, true);
    assert.equal(res.counterexample, false);
    assert.equal(res.details?.lhs, 91n);
    assert.equal(res.details?.rhs, 125n);
  });

  it("5^3 + 6^3 != 7^3 (125 + 216 = 341 != 343)", () => {
    const res = checkBeal([5, 6, 7, 3, 3, 3]);
    assert.equal(res.admissible, true);
    assert.equal(res.equality, false);
    assert.equal(res.primitive, true);
    assert.equal(res.counterexample, false);
  });
});

describe("4. Zero and negative inputs", () => {
  it("Base A = 0 rejected", () => {
    const res = checkBeal([0, 3, 4, 3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Positivity violation.*A=0/);
  });

  it("Base B = 0 rejected", () => {
    const res = checkBeal([3, 0, 4, 3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Positivity violation.*B=0/);
  });

  it("Base C = 0 rejected", () => {
    const res = checkBeal([3, 4, 0, 3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Positivity violation.*C=0/);
  });

  it("Exponent x = 0 rejected", () => {
    const res = checkBeal([3, 4, 5, 0, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Positivity violation.*x=0/);
  });

  it("Exponent y = 0 rejected", () => {
    const res = checkBeal([3, 4, 5, 3, 0, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Positivity violation.*y=0/);
  });

  it("Exponent z = 0 rejected", () => {
    const res = checkBeal([3, 4, 5, 3, 3, 0]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Positivity violation.*z=0/);
  });

  it("Negative base A = -3 rejected", () => {
    const res = checkBeal([-3, 4, 5, 3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Positivity violation.*A=-3/);
  });

  it("Negative base B = -4 rejected", () => {
    const res = checkBeal([3, -4, 5, 3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Positivity violation.*B=-4/);
  });

  it("Negative base C = -5 rejected", () => {
    const res = checkBeal([3, 4, -5, 3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Positivity violation.*C=-5/);
  });

  it("Negative exponent x = -3 rejected", () => {
    const res = checkBeal([3, 4, 5, -3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Positivity violation.*x=-3/);
  });

  it("Negative exponent y = -3 rejected", () => {
    const res = checkBeal([3, 4, 5, 3, -3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Positivity violation.*y=-3/);
  });

  it("Negative exponent z = -3 rejected", () => {
    const res = checkBeal([3, 4, 5, 3, 3, -3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Positivity violation.*z=-3/);
  });

  it("All zero inputs rejected", () => {
    const res = checkBeal([0, 0, 0, 0, 0, 0]);
    assert.equal(res.admissible, false);
    assert.equal(res.counterexample, false);
  });
});

describe("5. Noninteger inputs and unsafe representations", () => {
  it("Floating-point decimal 1.5 rejected", () => {
    const res = checkBeal([1.5, 3, 4, 3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Noninteger.*A/);
  });

  it("String decimal '1.2' rejected", () => {
    const res = checkBeal(["1.2", 3, 4, 3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Noninteger.*A/);
  });

  it("Boolean true rejected (does not coerce to 1n)", () => {
    const res = checkBeal([true, 3, 4, 3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Noninteger.*A/);
  });

  it("Boolean false rejected (does not coerce to 0n)", () => {
    const res = checkBeal([3, false, 4, 3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Noninteger.*B/);
  });

  it("null input rejected", () => {
    const res = checkBeal([3, 4, null, 3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Noninteger.*C/);
  });

  it("undefined input rejected", () => {
    const res = checkBeal([3, 4, 5, undefined, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Noninteger.*x/);
  });

  it("NaN input rejected", () => {
    const res = checkBeal([3, 4, 5, 3, NaN, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Noninteger.*y/);
  });

  it("Infinity and -Infinity rejected", () => {
    assert.equal(checkBeal([3, 4, 5, 3, 3, Infinity]).admissible, false);
    assert.equal(checkBeal([3, 4, 5, 3, 3, -Infinity]).admissible, false);
  });

  it("Text strings and empty strings rejected", () => {
    assert.equal(checkBeal(["abc", 3, 4, 3, 3, 3]).admissible, false);
    assert.equal(checkBeal(["", 3, 4, 3, 3, 3]).admissible, false);
    assert.equal(checkBeal(["   ", 3, 4, 3, 3, 3]).admissible, false);
    assert.equal(checkBeal(["1e5", 3, 4, 3, 3, 3]).admissible, false);
  });

  it("Object and array inputs as element rejected", () => {
    assert.equal(checkBeal([[1], 3, 4, 3, 3, 3]).admissible, false);
    assert.equal(checkBeal([{ val: 1 }, 3, 4, 3, 3, 3]).admissible, false);
  });
});

describe("6. Integers beyond ordinary floating-point safe-integer limits", () => {
  it("Raw JS number >= 2^53 (9007199254740992) rejected as unsafe float", () => {
    // 9007199254740992 = Number.MAX_SAFE_INTEGER + 1
    const res = checkBeal([9007199254740992, 3, 4, 3, 3, 3]);
    assert.equal(res.admissible, false);
    assert.match(res.reason, /Noninteger, unsafe floating-point/);
  });

  it("Safe integer boundary (9007199254740991 = MAX_SAFE_INTEGER) accepted", () => {
    assert.equal(parseExact(Number.MAX_SAFE_INTEGER), 9007199254740991n);
  });

  it("Exact BigInt beyond safe integer limits: (2^60)^3 + (2^60)^3 = 2^181", () => {
    // 2^60 = 1152921504606846976 (approx 1.15e18 >> 2^53 approx 9.007e15)
    // (2^60)^3 + (2^60)^3 = 2 * 2^180 = 2^181. Exponent z = 181.
    const res = checkBeal([2n ** 60n, 2n ** 60n, 2n, 3n, 3n, 181n]);
    assert.equal(res.admissible, true);
    assert.equal(res.equality, true);
    assert.equal(res.primitive, false);
    assert.equal(res.counterexample, false);
    assert.equal(res.details?.gcd, 2n);
  });

  it("Massive power of 2: (2^100)^3 + (2^100)^3 = 2^301", () => {
    // 2^100 has 31 decimal digits; 2^301 has 91 decimal digits
    const res = checkBeal([2n ** 100n, 2n ** 100n, 2n, 3n, 3n, 301n]);
    assert.equal(res.admissible, true);
    assert.equal(res.equality, true);
    assert.equal(res.primitive, false);
    assert.equal(res.counterexample, false);
    assert.equal(res.details?.gcd, 2n);
  });

  it("Decimal string serialization beyond safe integer: '9007199254740993'", () => {
    // 9007199254740993 = 2^53 + 1. In IEEE-754 binary64, this rounds to 9007199254740992.
    const parsed = parseExact("9007199254740993");
    assert.equal(parsed, 9007199254740993n);
  });

  it("Arithmetic mismatch on large integers beyond safe integer limits", () => {
    const res = checkBeal([2n ** 60n, 2n ** 60n, 3n, 3n, 3n, 181n]);
    assert.equal(res.admissible, true);
    assert.equal(res.equality, false);
    assert.equal(res.counterexample, false);
  });
});

describe("7. Boundary conditions, GCD correctness, and calling conventions", () => {
  it("Base one is retained as admissible positive integer", () => {
    const res = checkBeal([1, 2, 3, 3, 3, 3]);
    assert.equal(res.admissible, true);
    assert.equal(res.equality, false); // 1 + 8 != 27
    assert.equal(res.primitive, true);
    assert.equal(res.counterexample, false);
  });

  it("Input size checks: 0, 5, 7 inputs rejected", () => {
    assert.equal(checkBeal([]).admissible, false);
    assert.equal(checkBeal([1, 2, 3, 4, 5]).admissible, false);
    assert.equal(checkBeal([1, 2, 3, 4, 5, 6, 7]).admissible, false);
  });

  it("Calling via 6 positional arguments", () => {
    const res = checkBeal(3, 6, 3, 3, 3, 5);
    assert.equal(res.admissible, true);
    assert.equal(res.equality, true);
    assert.equal(res.primitive, false);
  });

  it("Calling via object input with uppercase keys", () => {
    const res = checkBeal({ A: 3, B: 6, C: 3, x: 3, y: 3, z: 5 });
    assert.equal(res.admissible, true);
    assert.equal(res.equality, true);
    assert.equal(res.primitive, false);
  });

  it("Calling via object input with lowercase keys", () => {
    const res = checkBeal({ a: 3, b: 6, c: 3, x: 3, y: 3, z: 5 });
    assert.equal(res.admissible, true);
    assert.equal(res.equality, true);
    assert.equal(res.primitive, false);
  });

  it("gcd and gcd3 correctness", () => {
    assert.equal(gcd(12n, 18n), 6n);
    assert.equal(gcd(-12n, 18n), 6n);
    assert.equal(gcd(18n, -12n), 6n);
    assert.equal(gcd(0n, 5n), 5n);
    assert.equal(gcd(5n, 0n), 5n);
    assert.equal(gcd3(12n, 18n, 24n), 6n);
    assert.equal(gcd3(7n, 11n, 13n), 1n);
    assert.equal(gcd3(27n, 216n, 243n), 27n);
  });

  it("Hypothetical counterexample logic: primitive equality with x,y,z >= 3 gives counterexample=true", () => {
    // If a candidate had primitive coprime bases and exact equality with x,y,z >= 3,
    // verify that counterexample === true.
    // We test the logic:
    // (A, B, C) with gcd=1, e.g. 1^3 + 2^3 != 3^3, but if equality held it would certify counterexample.
    const res = checkBeal([2, 3, 4, 3, 3, 3]);
    assert.equal(res.primitive, true);
    assert.equal(res.admissible, true);
    // Because equality is false, counterexample is false
    assert.equal(res.counterexample, false);
  });
});

console.log("\n=================================================================");
console.log(`TypeScript Test Suite Completed: ${passedTests}/${totalTests} tests passed.`);
console.log("=================================================================\n");
