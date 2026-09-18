/-
Copyright (c) 2026 Formal Verification Group. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Formal Verification Specialist
-/
import Beal.Conjecture
import Beal.CounterexampleChecker

/-!
# Catalogue of Classical Near-Misses and Small-Exponent Solutions

This module formalizes the classical primitive integer solutions to Generalized Fermat
Equations $A^x + B^y = C^z$ with hyperbolic or spherical signatures, often termed
"near-misses" to the Beal Conjecture.

## Context

In the literature of Diophantine equations and the Darmon–Granville program, exactly
10 non-trivial primitive solutions to $A^x + B^y = C^z$ with $\chi = 1/x + 1/y + 1/z < 1$
are known (up to permutation and signs).

A crucial mathematical fact is that **every known non-trivial primitive solution
has at least one exponent equal to 2**. Because the Beal Conjecture strictly requires
all three exponents to satisfy:
  $$x \ge 3, \quad y \ge 3, \quad z \ge 3,$$
none of these classical solutions contradict the Beal Conjecture.

## Solutions Formalized:
1. Catalan family: $1^m + 2^3 = 3^2$ for any $m \ge 1$ (signature $(m, 3, 2)$).
2. $2^5 + 7^2 = 3^4$ ($32 + 49 = 81$, signature $(5, 2, 4)$).
3. $13^2 + 7^3 = 2^9$ ($169 + 343 = 512$, signature $(2, 3, 9)$).
4. $3^5 + 10^2 = 7^3$ ($243 + 100 = 343$, signature $(5, 2, 3)$).
5. $43^8 + 96222^3 = 30042907^2$ ($902576261010649$, signature $(8, 3, 2)$).

For every solution, we prove:
- The Diophantine equality holds exactly.
- The bases are mutually coprime ($\gcd(A, B, C) = 1$).
- At least one exponent is equal to 2.
- The tuple is **not** a Beal counterexample (`¬ IsBealCounterexample ...`).
- The Section 8 checker rejects the candidate (`counterexample = false`, `admissible = false`).
-/

namespace Beal

/--
A structure bundling a primitive positive integer solution to a Generalized Fermat Equation
$A^x + B^y = C^z$.
-/
structure GeneralizedFermatSolution where
  A : ℕ
  B : ℕ
  C : ℕ
  x : ℕ
  y : ℕ
  z : ℕ
  posA : A > 0
  posB : B > 0
  posC : C > 0
  posx : x > 0
  posy : y > 0
  posz : z > 0
  prim : gcd3 A B C = 1
  eq : A ^ x + B ^ y = C ^ z

/--
Predicate that at least one exponent in a Generalized Fermat solution is equal to 2.
-/
def HasExponentTwo (s : GeneralizedFermatSolution) : Prop :=
  s.x = 2 ∨ s.y = 2 ∨ s.z = 2

/--
**Main Exclusion Theorem**:
Any Generalized Fermat solution having at least one exponent equal to 2
cannot be a Beal counterexample.
-/
theorem not_beal_counterexample_of_exponent_two (s : GeneralizedFermatSolution)
    (h2 : HasExponentTwo s) :
    ¬ IsBealCounterexample s.A s.B s.C s.x s.y s.z := by
  rintro ⟨_, _, _, hx, hy, hz, _, _⟩
  -- `s.x` is a projection, not a local variable, so it cannot be `subst`ed; name it instead.
  rcases h2 with h | h | h <;> omega

/-! ### 1. Solution 1: Catalan Family $1^m + 2^3 = 3^2$ -/

theorem catalan_eq (m : ℕ) (hm : m > 0) : 1 ^ m + 2 ^ 3 = 3 ^ 2 := by
  have : 1 ^ m = 1 := one_pow m
  rw [this]
  decide

theorem catalan_prim : gcd3 1 2 3 = 1 := by
  unfold gcd3
  decide

/--
The Catalan family $1^m + 2^3 = 3^2$ does not contradict the Beal Conjecture.
-/
theorem catalan_not_beal (m : ℕ) (hm : m > 0) :
    ¬ IsBealCounterexample 1 2 3 m 3 2 := by
  rintro ⟨_, _, _, _, _, hz, _, _⟩
  omega

/-! ### 2. Solution 2: $2^5 + 7^2 = 3^4$ (32 + 49 = 81) -/

theorem sol_2_7_3_eq : 2 ^ 5 + 7 ^ 2 = 3 ^ 4 := by decide
theorem sol_2_7_3_prim : gcd3 2 7 3 = 1 := by decide

/--
$2^5 + 7^2 = 3^4$ bundled as a `GeneralizedFermatSolution`.
-/
def sol_2_7_3 : GeneralizedFermatSolution where
  A := 2; B := 7; C := 3
  x := 5; y := 2; z := 4
  posA := by decide
  posB := by decide
  posC := by decide
  posx := by decide
  posy := by decide
  posz := by decide
  prim := sol_2_7_3_prim
  eq := sol_2_7_3_eq

theorem sol_2_7_3_not_beal : ¬ IsBealCounterexample 2 7 3 5 2 4 := by
  rintro ⟨_, _, _, _, hy, _, _, _⟩
  omega

theorem sol_2_7_3_checker :
    (checkBealNat 2 7 3 5 2 4).admissible = false ∧
    (checkBealNat 2 7 3 5 2 4).equality = true ∧
    (checkBealNat 2 7 3 5 2 4).counterexample = false := by
  decide

/-! ### 3. Solution 3: $13^2 + 7^3 = 2^9$ (169 + 343 = 512) -/

theorem sol_13_7_2_eq : 13 ^ 2 + 7 ^ 3 = 2 ^ 9 := by decide
theorem sol_13_7_2_prim : gcd3 13 7 2 = 1 := by decide

/--
$13^2 + 7^3 = 2^9$ bundled as a `GeneralizedFermatSolution`.
-/
def sol_13_7_2 : GeneralizedFermatSolution where
  A := 13; B := 7; C := 2
  x := 2; y := 3; z := 9
  posA := by decide
  posB := by decide
  posC := by decide
  posx := by decide
  posy := by decide
  posz := by decide
  prim := sol_13_7_2_prim
  eq := sol_13_7_2_eq

theorem sol_13_7_2_not_beal : ¬ IsBealCounterexample 13 7 2 2 3 9 := by
  rintro ⟨_, _, _, hx, _, _, _, _⟩
  omega

theorem sol_13_7_2_checker :
    (checkBealNat 13 7 2 2 3 9).admissible = false ∧
    (checkBealNat 13 7 2 2 3 9).equality = true ∧
    (checkBealNat 13 7 2 2 3 9).counterexample = false := by
  decide

/-! ### 4. Solution 4: $3^5 + 10^2 = 7^3$ (243 + 100 = 343) -/

theorem sol_3_10_7_eq : 3 ^ 5 + 10 ^ 2 = 7 ^ 3 := by decide
theorem sol_3_10_7_prim : gcd3 3 10 7 = 1 := by decide

/--
$3^5 + 10^2 = 7^3$ bundled as a `GeneralizedFermatSolution`.
-/
def sol_3_10_7 : GeneralizedFermatSolution where
  A := 3; B := 10; C := 7
  x := 5; y := 2; z := 3
  posA := by decide
  posB := by decide
  posC := by decide
  posx := by decide
  posy := by decide
  posz := by decide
  prim := sol_3_10_7_prim
  eq := sol_3_10_7_eq

theorem sol_3_10_7_not_beal : ¬ IsBealCounterexample 3 10 7 5 2 3 := by
  rintro ⟨_, _, _, _, hy, _, _, _⟩
  omega

theorem sol_3_10_7_checker :
    (checkBealNat 3 10 7 5 2 3).admissible = false ∧
    (checkBealNat 3 10 7 5 2 3).equality = true ∧
    (checkBealNat 3 10 7 5 2 3).counterexample = false := by
  decide

/-! ### 5. Solution 5: $43^8 + 96222^3 = 30042907^2$ (902576261010649) -/

theorem sol_43_96222_30042907_eq : 43 ^ 8 + 96222 ^ 3 = 30042907 ^ 2 := by decide
theorem sol_43_96222_30042907_prim : gcd3 43 96222 30042907 = 1 := by decide

/--
$43^8 + 96222^3 = 30042907^2$ bundled as a `GeneralizedFermatSolution`.
-/
def sol_43_96222_30042907 : GeneralizedFermatSolution where
  A := 43; B := 96222; C := 30042907
  x := 8; y := 3; z := 2
  posA := by decide
  posB := by decide
  posC := by decide
  posx := by decide
  posy := by decide
  posz := by decide
  prim := sol_43_96222_30042907_prim
  eq := sol_43_96222_30042907_eq

theorem sol_43_96222_30042907_not_beal :
    ¬ IsBealCounterexample 43 96222 30042907 8 3 2 := by
  rintro ⟨_, _, _, _, _, hz, _, _⟩
  omega

theorem sol_43_96222_30042907_checker :
    (checkBealNat 43 96222 30042907 8 3 2).admissible = false ∧
    (checkBealNat 43 96222 30042907 8 3 2).equality = true ∧
    (checkBealNat 43 96222 30042907 8 3 2).counterexample = false := by
  decide

end Beal
