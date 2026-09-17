/**
 * Section 8: Beal Conjecture Exact Counterexample Checker (TypeScript)
 *
 * REQUIRE EXACT, REPRODUCIBLE COMPUTATION.
 * Before relying on a search, validate a small transparent counterexample checker.
 *
 * Requirements:
 * 1. Checks all six inputs: bases (A, B, C) and exponents (x, y, z).
 * 2. Positivity: all bases and exponents must be strictly positive integers (> 0).
 * 3. Exponent restrictions: exponents must satisfy x >= 3, y >= 3, z >= 3.
 * 4. Exact equality: verifies A^x + B^y === C^z over arbitrary-precision BigInt.
 * 5. Greatest common divisor: calculates gcd(A, B, C) = gcd(gcd(A, B), C).
 *    A counterexample requires gcd(A, B, C) === 1n (primitive).
 *    If gcd(A, B, C) > 1n, the equality satisfies the Beal conjecture and is NOT a counterexample.
 * 6. Rejects non-integers, unsafe IEEE-754 floating-point numbers, zeros, negatives, and malformed inputs.
 */

import { fileURLToPath } from "node:url";

export interface BealCheckDetails {
  inputs?: readonly [bigint, bigint, bigint, bigint, bigint, bigint];
  a?: bigint;
  b?: bigint;
  c?: bigint;
  x?: bigint;
  y?: bigint;
  z?: bigint;
  lhs?: bigint;
  rhs?: bigint;
  gcd?: bigint;
}

export interface BealCheckResult {
  /** True if all 6 inputs are exact integers, strictly positive (>0), and exponents >= 3 */
  admissible: boolean;
  /** True if exact arithmetic equality A^x + B^y === C^z holds */
  equality: boolean;
  /** True if gcd(A, B, C) === 1 */
  primitive: boolean;
  /** True if admissible && equality && primitive (a genuine Beal counterexample) */
  counterexample: boolean;
  /** Comprehensive diagnostic message explaining the outcome */
  reason: string;
  /** Computed intermediate values and parsed representations */
  details?: BealCheckDetails;
}

export interface BealInputObject {
  a?: unknown;
  b?: unknown;
  c?: unknown;
  x?: unknown;
  y?: unknown;
  z?: unknown;
  A?: unknown;
  B?: unknown;
  C?: unknown;
  X?: unknown;
  Y?: unknown;
  Z?: unknown;
}

/**
 * Parses an unknown value into an exact BigInt integer.
 *
 * - bigint: returned directly.
 * - number: only accepted if Number.isSafeInteger(n). Rejects floats (1.5),
 *   NaN, Infinity, and numbers >= 2^53 (e.g. 9007199254740992) where binary64 precision is lost.
 * - string: only accepted if matching strictly /^[+-]?\d+$/. Decimals ("1.2") and text are rejected.
 * - all other types (boolean, null, undefined, object, symbol, function): rejected.
 */
export function parseExact(x: unknown): bigint | null {
  if (typeof x === "bigint") {
    return x;
  }
  if (typeof x === "number") {
    if (Number.isSafeInteger(x)) {
      return BigInt(x);
    }
    return null;
  }
  if (typeof x === "string") {
    const trimmed = x.trim();
    if (/^[+-]?\d+$/.test(trimmed)) {
      try {
        return BigInt(trimmed);
      } catch {
        return null;
      }
    }
    return null;
  }
  return null;
}

/**
 * Computes the greatest common divisor of two BigInt integers using Euclidean algorithm.
 */
export function gcd(x: bigint, y: bigint): bigint {
  let a = x < 0n ? -x : x;
  let b = y < 0n ? -y : y;
  while (b !== 0n) {
    const t = b;
    b = a % b;
    a = t;
  }
  return a;
}

/**
 * Computes the greatest common divisor of three BigInt integers.
 */
export function gcd3(a: bigint, b: bigint, c: bigint): bigint {
  return gcd(gcd(a, b), c);
}

/**
 * Validates a potential Beal counterexample.
 *
 * Can be called with:
 * - An array/tuple of 6 elements: checkBeal([A, B, C, x, y, z])
 * - 6 positional arguments: checkBeal(A, B, C, x, y, z)
 * - An object: checkBeal({ A, B, C, x, y, z })
 */
export function checkBeal(
  arg1: readonly unknown[] | BealInputObject | unknown,
  ...rest: unknown[]
): BealCheckResult {
  let rawInputs: readonly unknown[];

  if (Array.isArray(arg1)) {
    if (rest.length > 0) {
      return {
        admissible: false,
        equality: false,
        primitive: false,
        counterexample: false,
        reason: "Invalid input format: array argument followed by extra positional arguments",
      };
    }
    rawInputs = arg1;
  } else if (
    typeof arg1 === "object" &&
    arg1 !== null &&
    rest.length === 0 &&
    !(arg1 instanceof Set) &&
    !(arg1 instanceof Map)
  ) {
    const obj = arg1 as BealInputObject;
    const a = obj.A ?? obj.a;
    const b = obj.B ?? obj.b;
    const c = obj.C ?? obj.c;
    const x = obj.x ?? obj.X;
    const y = obj.y ?? obj.Y;
    const z = obj.z ?? obj.Z;
    rawInputs = [a, b, c, x, y, z];
  } else {
    rawInputs = [arg1, ...rest];
  }

  // Check 1: Exactly six inputs required
  if (rawInputs.length !== 6) {
    return {
      admissible: false,
      equality: false,
      primitive: false,
      counterexample: false,
      reason: `Input size mismatch: expected exactly 6 inputs (A, B, C, x, y, z), got ${rawInputs.length}`,
    };
  }

  // Check 2: Exact integer validation (no floats, no unsafe integers, no booleans)
  const a = parseExact(rawInputs[0]);
  const b = parseExact(rawInputs[1]);
  const c = parseExact(rawInputs[2]);
  const x = parseExact(rawInputs[3]);
  const y = parseExact(rawInputs[4]);
  const z = parseExact(rawInputs[5]);

  const names = ["A", "B", "C", "x", "y", "z"];
  const parsed = [a, b, c, x, y, z];
  const invalidIndices: number[] = [];
  for (let i = 0; i < 6; i++) {
    if (parsed[i] === null) {
      invalidIndices.push(i);
    }
  }

  if (invalidIndices.length > 0) {
    const badNames = invalidIndices.map((i) => names[i]).join(", ");
    return {
      admissible: false,
      equality: false,
      primitive: false,
      counterexample: false,
      reason: `Noninteger, unsafe floating-point, or unparseable input at: ${badNames}`,
    };
  }

  const [A, B, C, X, Y, Z] = [a!, b!, c!, x!, y!, z!];

  // Check 3: Positivity checks
  if (A <= 0n || B <= 0n || C <= 0n) {
    const nonPosBases: string[] = [];
    if (A <= 0n) nonPosBases.push(`A=${A}`);
    if (B <= 0n) nonPosBases.push(`B=${B}`);
    if (C <= 0n) nonPosBases.push(`C=${C}`);
    return {
      admissible: false,
      equality: false,
      primitive: false,
      counterexample: false,
      reason: `Positivity violation: bases must be strictly positive integers (> 0): ${nonPosBases.join(", ")}`,
      details: { a: A, b: B, c: C, x: X, y: Y, z: Z },
    };
  }

  if (X <= 0n || Y <= 0n || Z <= 0n) {
    const nonPosExp: string[] = [];
    if (X <= 0n) nonPosExp.push(`x=${X}`);
    if (Y <= 0n) nonPosExp.push(`y=${Y}`);
    if (Z <= 0n) nonPosExp.push(`z=${Z}`);
    return {
      admissible: false,
      equality: false,
      primitive: false,
      counterexample: false,
      reason: `Positivity violation: exponents must be strictly positive integers (> 0): ${nonPosExp.join(", ")}`,
      details: { a: A, b: B, c: C, x: X, y: Y, z: Z },
    };
  }

  // Check 4: Greatest common divisor of the three bases
  const commonDivisor = gcd3(A, B, C);
  const primitive = commonDivisor === 1n;

  // Check 5: Exact equality check (A^x + B^y === C^z)
  let lhs: bigint | undefined;
  let rhs: bigint | undefined;
  let equality = false;
  try {
    lhs = A ** X + B ** Y;
    rhs = C ** Z;
    equality = lhs === rhs;
  } catch (err) {
    return {
      admissible: false,
      equality: false,
      primitive,
      counterexample: false,
      reason: `Exponentiation calculation overflow or error: ${err instanceof Error ? err.message : String(err)}`,
      details: { a: A, b: B, c: C, x: X, y: Y, z: Z, gcd: commonDivisor },
    };
  }

  // Check 6: Exponent restrictions (x, y, z >= 3)
  const exponentsAdmissible = X >= 3n && Y >= 3n && Z >= 3n;
  if (!exponentsAdmissible) {
    const smallExp: string[] = [];
    if (X < 3n) smallExp.push(`x=${X}`);
    if (Y < 3n) smallExp.push(`y=${Y}`);
    if (Z < 3n) smallExp.push(`z=${Z}`);
    return {
      admissible: false,
      equality,
      primitive,
      counterexample: false,
      reason: `Exponent restriction violated (x, y, z must all be >= 3): ${smallExp.join(", ")}`,
      details: {
        inputs: [A, B, C, X, Y, Z],
        a: A,
        b: B,
        c: C,
        x: X,
        y: Y,
        z: Z,
        lhs,
        rhs,
        gcd: commonDivisor,
      },
    };
  }

  // All structural and domain conditions passed: admissible is true
  const counterexample = equality && primitive;

  let reason: string;
  if (counterexample) {
    reason = `Genuine Beal counterexample verified: ${A}^${X} + ${B}^${Y} === ${C}^${Z} with gcd(${A}, ${B}, ${C}) === 1`;
  } else if (equality && !primitive) {
    reason = `Valid equality (${A}^${X} + ${B}^${Y} === ${C}^${Z}), but fails common-factor requirement: gcd(${A}, ${B}, ${C}) === ${commonDivisor} > 1 (satisfies Beal conjecture)`;
  } else if (!equality) {
    reason = `Arithmetic mismatch: ${A}^${X} + ${B}^${Y} === ${lhs} !== ${rhs} === ${C}^${Z}`;
  } else {
    reason = "Conditions not satisfied";
  }

  return {
    admissible: true,
    equality,
    primitive,
    counterexample,
    reason,
    details: {
      inputs: [A, B, C, X, Y, Z],
      a: A,
      b: B,
      c: C,
      x: X,
      y: Y,
      z: Z,
      lhs,
      rhs,
      gcd: commonDivisor,
    },
  };
}

/**
 * Self-verification routine when executed directly.
 */
function runSelfVerification(): void {
  function requireTrue(condition: boolean, msg: string): asserts condition {
    if (!condition) {
      throw new Error(`Self-verification failed: ${msg}`);
    }
  }

  // 1. Valid equality that fails common-factor requirement: 3^3 + 6^3 = 3^5
  const nonprimitive = checkBeal([3, 6, 3, 3, 3, 5]);
  requireTrue(
    nonprimitive.admissible &&
      nonprimitive.equality &&
      !nonprimitive.primitive &&
      !nonprimitive.counterexample &&
      nonprimitive.details?.gcd === 3n,
    "3^3 + 6^3 = 3^5 must be admissible equality failing common-factor requirement"
  );

  // 2. Valid equality excluded because an exponent is 2: 3^5 + 10^2 = 7^3
  const expTwo = checkBeal([3, 10, 7, 5, 2, 3]);
  requireTrue(
    !expTwo.admissible &&
      expTwo.equality &&
      expTwo.primitive &&
      !expTwo.counterexample,
    "3^5 + 10^2 = 7^3 must be excluded because exponent y=2 < 3"
  );

  // 3. Arithmetic mismatch: 2^3 + 3^3 != 4^3
  const mismatch = checkBeal([2, 3, 4, 3, 3, 3]);
  requireTrue(
    mismatch.admissible &&
      !mismatch.equality &&
      mismatch.primitive &&
      !mismatch.counterexample,
    "2^3 + 3^3 != 4^3 must fail exact equality"
  );

  // 4. Zero and negative inputs
  for (const bad of [0, -1, -100]) {
    requireTrue(!checkBeal([bad, 3, 4, 3, 3, 3]).admissible, `Base A=${bad} rejected`);
    requireTrue(!checkBeal([3, bad, 4, 3, 3, 3]).admissible, `Base B=${bad} rejected`);
    requireTrue(!checkBeal([3, 4, bad, 3, 3, 3]).admissible, `Base C=${bad} rejected`);
    requireTrue(!checkBeal([3, 4, 5, bad, 3, 3]).admissible, `Exponent x=${bad} rejected`);
    requireTrue(!checkBeal([3, 4, 5, 3, bad, 3]).admissible, `Exponent y=${bad} rejected`);
    requireTrue(!checkBeal([3, 4, 5, 3, 3, bad]).admissible, `Exponent z=${bad} rejected`);
  }

  // 5. Noninteger inputs
  for (const bad of [1.5, "1.2", true, false, null, undefined, NaN, Infinity, -Infinity, "foo"]) {
    requireTrue(!checkBeal([bad, 3, 4, 3, 3, 3]).admissible, `Noninteger ${String(bad)} rejected`);
  }

  // 6. Integers beyond ordinary floating-point safe-integer limits
  // (a) Raw number >= 2^53 rejected as unsafe float
  requireTrue(!checkBeal([9007199254740992, 3, 4, 3, 3, 3]).admissible, "Unsafe raw float rejected");
  // (b) Exact BigInt beyond safe integers evaluated exactly: (2^60)^3 + (2^60)^3 = 2^181
  const bigCheck = checkBeal([2n ** 60n, 2n ** 60n, 2n, 3n, 3n, 181n]);
  requireTrue(
    bigCheck.admissible &&
      bigCheck.equality &&
      !bigCheck.primitive &&
      !bigCheck.counterexample,
    "Beyond binary64 safe integer equality verified exactly"
  );
  // (c) Decimal string serialization beyond safe integer limit
  requireTrue(parseExact("9007199254740993") === 9007199254740993n, "String beyond safe int parsed exactly");

  // 7. Base one retained
  requireTrue(checkBeal([1, 2, 3, 3, 3, 3]).admissible, "Base 1 retained as positive integer");

  console.log(
    JSON.stringify(
      {
        status: "verified",
        section: 8,
        implementation: "TypeScript (BigInt)",
        checksPassed: [
          "nonprimitive_equality_3^3+6^3=3^5",
          "exponent_two_excluded_3^5+10^2=7^3",
          "arithmetic_mismatch_2^3+3^3!=4^3",
          "zero_and_negative_inputs_rejected",
          "noninteger_inputs_rejected",
          "unsafe_floating_point_rejected",
          "beyond_safe_integer_exact_computation",
          "decimal_string_serialization",
          "base_one_retained",
        ],
      },
      null,
      2
    )
  );
}

// Execute self-verification if run directly
if (typeof process !== "undefined" && process.argv && process.argv[1]) {
  try {
    const currentFile = fileURLToPath(import.meta.url);
    const invokedFile = process.argv[1];
    if (
      invokedFile === currentFile ||
      invokedFile.endsWith("/section8_counterexample_checker.ts") ||
      invokedFile.endsWith("\\section8_counterexample_checker.ts")
    ) {
      runSelfVerification();
    }
  } catch {
    // If URL parsing fails, ignore
  }
}
