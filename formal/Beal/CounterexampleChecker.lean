/-
Copyright (c) 2026 Formal Verification Group. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Formal Verification Specialist
-/
import Beal.Conjecture

/-!
# Section 8: Beal Counterexample Checker Logic in Lean 4

This module formalizes the exact algorithmic verification logic specified in
Section 8 and implemented in `code/section8_counterexample_checker.py` and
`code/section8_counterexample_checker.ts`.

## Requirements Verified:
1. Validates all six inputs: bases (A, B, C) and exponents (x, y, z).
2. Positivity: all bases and exponents must be strictly positive integers (> 0).
3. Exponent restrictions: exponents must satisfy x ≥ 3, y ≥ 3, z ≥ 3.
4. Exact equality: verifies A^x + B^y = C^z over arbitrary-precision integers.
5. Greatest common divisor: calculates gcd(A, B, C) = gcd(gcd(A, B), C).
   A counterexample requires gcd(A, B, C) = 1 (primitive).
   If gcd(A, B, C) > 1, the equality satisfies the Beal conjecture and is NOT a counterexample.
6. Rejects zero, negative, and out-of-bounds inputs.

## Formal Properties:
- **Soundness**: Any candidate accepted as a counterexample satisfies `IsBealCounterexample`.
- **Completeness**: Any mathematical counterexample is classified as a counterexample by the checker.
- **Decidable Test Suite**: All canonical boundary test cases are proven via `decide` / `rfl`.
-/

namespace Beal

/--
Detailed structured result returned by the Section 8 Beal counterexample checker.
-/
structure BealCheckResult where
  admissible : Bool
  equality : Bool
  primitive : Bool
  counterexample : Bool
  reason : String
  a : Option ℤ := none
  b : Option ℤ := none
  c : Option ℤ := none
  x : Option ℤ := none
  y : Option ℤ := none
  z : Option ℤ := none
  lhs : Option ℤ := none
  rhs : Option ℤ := none
  gcd : Option ℕ := none
  deriving Repr, DecidableEq

/--
Computable Section 8 counterexample checker taking natural number inputs.
-/
def checkBealNat (A B C x y z : ℕ) : BealCheckResult :=
  if A = 0 || B = 0 || C = 0 then
    { admissible := false, equality := false, primitive := false, counterexample := false,
      reason := "Positivity violation: bases must be strictly positive (> 0)",
      a := some (A : ℤ), b := some (B : ℤ), c := some (C : ℤ),
      x := some (x : ℤ), y := some (y : ℤ), z := some (z : ℤ) }
  else if x = 0 || y = 0 || z = 0 then
    { admissible := false, equality := false, primitive := false, counterexample := false,
      reason := "Positivity violation: exponents must be strictly positive (> 0)",
      a := some (A : ℤ), b := some (B : ℤ), c := some (C : ℤ),
      x := some (x : ℤ), y := some (y : ℤ), z := some (z : ℤ) }
  else
    let g := gcd3 A B C
    let isPrim := (g == 1)
    let lhsVal := A ^ x + B ^ y
    let rhsVal := C ^ z
    let isEq := (lhsVal == rhsVal)
    if x < 3 || y < 3 || z < 3 then
      { admissible := false, equality := isEq, primitive := isPrim, counterexample := false,
        reason := "Exponent restriction violated (x, y, z must all be ≥ 3)",
        a := some (A : ℤ), b := some (B : ℤ), c := some (C : ℤ),
        x := some (x : ℤ), y := some (y : ℤ), z := some (z : ℤ),
        lhs := some (lhsVal : ℤ), rhs := some (rhsVal : ℤ), gcd := some g }
    else
      let isCe := isEq && isPrim
      let msg :=
        if isCe then
          "Genuine Beal counterexample verified"
        else if isEq then
          "Valid equality, but fails common-factor requirement: gcd > 1 (satisfies Beal conjecture)"
        else
          "Arithmetic mismatch"
      { admissible := true, equality := isEq, primitive := isPrim, counterexample := isCe,
        reason := msg,
        a := some (A : ℤ), b := some (B : ℤ), c := some (C : ℤ),
        x := some (x : ℤ), y := some (y : ℤ), z := some (z : ℤ),
        lhs := some (lhsVal : ℤ), rhs := some (rhsVal : ℤ), gcd := some g }

/--
Section 8 counterexample checker taking general integer inputs (rejecting negatives and zeros).
-/
def checkBealInt (A B C x y z : ℤ) : BealCheckResult :=
  if A ≤ 0 || B ≤ 0 || C ≤ 0 then
    { admissible := false, equality := false, primitive := false, counterexample := false,
      reason := "Positivity violation: bases must be strictly positive integers (> 0)",
      a := some A, b := some B, c := some C, x := some x, y := some y, z := some z }
  else if x ≤ 0 || y ≤ 0 || z ≤ 0 then
    { admissible := false, equality := false, primitive := false, counterexample := false,
      reason := "Positivity violation: exponents must be strictly positive integers (> 0)",
      a := some A, b := some B, c := some C, x := some x, y := some y, z := some z }
  else
    checkBealNat A.toNat B.toNat C.toNat x.toNat y.toNat z.toNat

/-! ### Soundness and Completeness Theorems -/

/--
**Soundness**:
If `checkBealNat` accepts `(A, B, C, x, y, z)` as a counterexample,
then the tuple is mathematically a genuine `IsBealCounterexample`.
-/
theorem checkBealNat_sound (A B C x y z : ℕ)
    (hce : (checkBealNat A B C x y z).counterexample = true) :
    IsBealCounterexample A B C x y z := by
  unfold checkBealNat at hce
  split_ifs at hce with h_bases h_exps h_small_exps
  · contradiction
  · contradiction
  · contradiction
  · -- Both branches of inner if
    simp only [Bool.and_eq_true, beq_iff_eq] at hce
    have h_pos_bases : A > 0 ∧ B > 0 ∧ C > 0 := by
      push_neg at h_bases
      omega
    have h_exp_ge : x ≥ 3 ∧ y ≥ 3 ∧ z ≥ 3 := by
      push_neg at h_small_exps
      omega
    exact ⟨h_pos_bases.1, h_pos_bases.2.1, h_pos_bases.2.2,
           h_exp_ge.1, h_exp_ge.2.1, h_exp_ge.2.2,
           hce.2, hce.1⟩

/--
**Completeness**:
If `(A, B, C, x, y, z)` is mathematically a genuine `IsBealCounterexample`,
then `checkBealNat` returns `counterexample = true`.
-/
theorem checkBealNat_complete (A B C x y z : ℕ)
    (h : IsBealCounterexample A B C x y z) :
    (checkBealNat A B C x y z).counterexample = true := by
  rcases h with ⟨hA, hB, hC, hx, hy, hz, hprim, heq⟩
  unfold checkBealNat
  have h_bases : ¬(A = 0 || B = 0 || C = 0) := by
    simp [hA.ne', hB.ne', hC.ne']
  have h_exps : ¬(x = 0 || y = 0 || z = 0) := by
    have : x > 0 := by omega
    have : y > 0 := by omega
    have : z > 0 := by omega
    simp [this.ne']
  have h_small : ¬(x < 3 || y < 3 || z < 3) := by
    simp [hx, hy, hz]
  simp [h_bases, h_exps, h_small, hprim, heq]

/-! ### Verified Section 8 Test Suite (Proof-by-Reflection / Decision) -/

/--
**Test Case 1**:
Valid equality that fails common-factor requirement:
$3^3 + 6^3 = 3^5$ ($27 + 216 = 243$, $\gcd(3, 6, 3) = 3 > 1$).
Result: equality holds, but counterexample is rejected.
-/
theorem test_case_01_nonprimitive_3_6_3 :
    (checkBealNat 3 6 3 3 3 5).admissible = true ∧
    (checkBealNat 3 6 3 3 3 5).equality = true ∧
    (checkBealNat 3 6 3 3 3 5).primitive = false ∧
    (checkBealNat 3 6 3 3 3 5).counterexample = false ∧
    (checkBealNat 3 6 3 3 3 5).gcd = some 3 := by
  decide

/--
**Test Case 2**:
Valid equality excluded because an exponent is 2:
$3^5 + 10^2 = 7^3$ ($243 + 100 = 343$, exponent $y = 2 < 3$).
Result: admissible is false, counterexample is rejected.
-/
theorem test_case_02_excluded_exponent_two :
    (checkBealNat 3 10 7 5 2 3).admissible = false ∧
    (checkBealNat 3 10 7 5 2 3).equality = true ∧
    (checkBealNat 3 10 7 5 2 3).counterexample = false := by
  decide

/--
**Test Case 3**:
Arithmetic mismatch:
$3^3 + 4^3 = 27 + 64 = 91 \ne 125 = 5^3$.
Result: equality is false, counterexample is rejected.
-/
theorem test_case_03_arithmetic_mismatch :
    (checkBealNat 3 4 5 3 3 3).equality = false ∧
    (checkBealNat 3 4 5 3 3 3).counterexample = false := by
  decide

/--
**Test Case 4**:
Valid higher-degree equality failing common-factor requirement:
$7^3 + 7^4 = 343 + 2401 = 2744 = 14^3$, $\gcd(7, 7, 14) = 7 > 1$.
Result: equality holds, but counterexample is rejected.
-/
theorem test_case_04_nonprimitive_7_7_14 :
    (checkBealNat 7 7 14 3 4 3).admissible = true ∧
    (checkBealNat 7 7 14 3 4 3).equality = true ∧
    (checkBealNat 7 7 14 3 4 3).primitive = false ∧
    (checkBealNat 7 7 14 3 4 3).counterexample = false ∧
    (checkBealNat 7 7 14 3 4 3).gcd = some 7 := by
  decide

/--
**Test Case 5**:
Negative base input rejected immediately by `checkBealInt`.
-/
theorem test_case_05_negative_input_rejected :
    (checkBealInt (-3) 6 3 3 3 5).admissible = false ∧
    (checkBealInt (-3) 6 3 3 3 5).counterexample = false := by
  decide

/--
**Test Case 6**:
Zero base input rejected immediately.
-/
theorem test_case_06_zero_input_rejected :
    (checkBealNat 0 6 3 3 3 5).admissible = false ∧
    (checkBealNat 0 6 3 3 3 5).counterexample = false := by
  decide

end Beal
