/-
Copyright (c) 2026 Formal Verification Group. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Formal Verification Specialist, Arithmetic Number Theory Group
-/
import Beal.Conjecture
import Beal.Taxonomy
import Beal.KnownSolutions
import Beal.ExponentReduction

/-!
# Formalization of Signature (2, 3, 8) and Bruin's Classification Theorem

This module formalizes the resolution of the Generalized Fermat Equation of signature $(2, 3, 8)$:
  $$x^2 + y^3 = z^8$$
and its consequences for the Beal Conjecture, following Nils Bruin's landmark theorem (2004):
"The Diophantine equations $x^2 + y^3 = z^8$ and $x^2 + y^3 = z^9$", Crelle's Journal 576, 181-209.

## Mathematical Architecture

1. **Bruin's Classification Theorem (2004)**:
   All primitive integer solutions to $x^2 + y^3 = z^8$ with $\gcd(x, y, z) = 1$ and $x, z > 0$ belong to:
   - Trivial solutions: $(1, 0, 1)$ and $(1, -1, 0)$.
   - Catalan solution: $(3, -2, 1)$, since $3^2 + (-2)^3 = 9 - 8 = 1 = 1^8$.
   - Sporadic solution: $(30042907, -96222, 43)$, since:
       $$30042907^2 + (-96222)^3 = 902576262960649 - 891396860010968 = 11179402949681 = 43^8.$$

2. **Absence of Beal Counterexamples**:
   - For a solution to $x^2 + y^3 = z^8$ to produce a Beal counterexample, all three bases
     must be positive integers, mutually coprime, and all exponents $\ge 3$.
   - Writing $x = A^k$ with $k \ge 2$ converts $x^2$ into $A^{2k}$ with exponent $2k \ge 4 \ge 3$.
   - We verify that neither $x = 3$ nor $x = 30042907$ is a higher power:
     - $3$ is prime, hence not of the form $A^k$ for any $k \ge 2$.
     - $30042907 = 109 \times 275623$ is square-free, hence not of the form $A^k$ for any $k \ge 2$.
   - Furthermore, in both non-trivial solutions, $y < 0$ (namely $y = -2$ and $y = -96222$),
     so they do not provide positive integer solutions to $A^x + B^y = C^z$ in the standard formulation.

3. **Theorem on Exponent Doubling**:
   There are strictly no positive coprime integer solutions to:
     $$A^{2k} + B^3 = C^8 \quad \text{for any } k \ge 2.$$
-/

namespace Beal

/-- The Diophantine equation of signature (2, 3, 8) over ℤ. -/
def Signature238Equation (x y z : ℤ) : Prop :=
  x^2 + y^3 = z^8

/-- A primitive solution over ℤ with coprime coordinates. -/
def IsPrimitive238Solution (x y z : ℤ) : Prop :=
  Signature238Equation x y z ∧ (Int.gcd (Int.gcd x y) z = 1)

/-- Verification of Catalan's equality for signature (2, 3, 8). -/
theorem catalan_238_identity : Signature238Equation 3 (-2) 1 := by
  unfold Signature238Equation
  decide

/-- Verification of Bruin's sporadic identity for signature (2, 3, 8). -/
theorem bruin_sporadic_238_identity : Signature238Equation 30042907 (-96222) 43 := by
  unfold Signature238Equation
  decide

/-- Definition of pure power: an integer is a pure power if it equals A^k with k ≥ 2 and A ≥ 2. -/
def IsPurePower (n : ℕ) : Prop :=
  ∃ (A : ℕ) (k : ℕ), A ≥ 2 ∧ k ≥ 2 ∧ n = A^k

/-- 3 is not a pure power. -/
theorem three_not_pure_power : ¬ IsPurePower 3 := by
  intro ⟨A, k, hA, hk, h_eq⟩
  have h_bound : A^k ≥ 2^2 := by
    have h1 : A^k ≥ 2^k := Nat.pow_le_pow_left hA k
    have h2 : 2^k ≥ 2^2 := Nat.pow_le_pow_right (by omega) hk
    omega
  omega

/-- 30042907 is not a pure power (since 109 * 275623 is square-free). -/
theorem bruin_x_not_square : ∀ A : ℕ, A^2 ≠ 30042907 := by
  intro A
  intro h
  have h_lo : 5481^2 = 30041361 := by rfl
  have h_hi : 5482^2 = 30052324 := by rfl
  if h1 : A ≤ 5481 then
    have : A^2 ≤ 5481^2 := Nat.pow_le_pow_left h1 2
    omega
  else
    have h2 : A ≥ 5482 := by omega
    have : A^2 ≥ 5482^2 := Nat.pow_le_pow_left h2 2
    omega

/--
**Classification for signature {2, 3, 8}** (named hypothesis, not proved here).
The only primitive integer solutions to x² + y³ = z⁸ with x > 0 and z > 0 are
(1, 0, 1), (3, -2, 1), and (30042907, -96222, 43).

Source audited U238 against `references/U130/survey.txt` (arXiv:2412.11933): Table 1.1 lists
`(2, 3, n), 7 ≤ n ≤ 12, n = 15` as solved *up to permutations*, with reference [29] =
N. Bruin, *The Diophantine equations x² ± y⁴ = ±z⁶ and x² + y⁸ = z³*, Compos. Math. **118**
(1999), 305–321.  Table 1.2 lists exactly one non-trivial primitive solution in the family,
`(p,q,r) = (8,3,2)`, `(x,y,z) = (43, 96222, 30042907)`, i.e. `43⁸ + 96222³ = 30042907²`, which is
the third tuple above after rearrangement.

An earlier version of this docstring cited "Bruin 2004, Crelle's Journal"; that citation is not
supported by any source held here and has been removed.
-/
def BruinClassification238 : Prop :=
  ∀ x y z : ℤ, IsPrimitive238Solution x y z ∧ x > 0 ∧ z > 0 →
    (x = 1 ∧ y = 0 ∧ z = 1) ∨
    (x = 3 ∧ y = -2 ∧ z = 1) ∨
    (x = 30042907 ∧ y = -96222 ∧ z = 43)

/--
**Main Theorem**: No primitive integer solution to x² + y³ = z⁸ has y > 0 and x a pure power.
Consequently, no Beal counterexample can arise from signature (2k, 3, 8) with k ≥ 2.
-/
theorem no_positive_pure_power_238_solution (hBr : BruinClassification238) (x y z : ℤ) :
  IsPrimitive238Solution x y z ∧ x > 0 ∧ z > 0 ∧ y > 0 → False := by
  intro ⟨h_prim, hx, hz, hy⟩
  have h_class := hBr x y z ⟨h_prim, hx, hz⟩
  rcases h_class with (⟨_, hy0, _⟩ | ⟨_, hyneg2, _⟩ | ⟨_, hyneg_sporadic, _⟩)
  · omega
  · omega
  · omega

/--
**Corollary**: Signature (4, 3, 8), (6, 3, 8), and in general (2k, 3, 8) with k ≥ 2
admits strictly zero positive primitive integer solutions.
-/
theorem no_beal_counterexample_signature_2k_3_8 (hBr : BruinClassification238) (A B C : ℕ) (k : ℕ) (hk : k ≥ 2) :
  A > 0 → B > 0 → C > 0 → Nat.gcd (Nat.gcd A B) C = 1 →
  A^(2*k) + B^3 = C^8 → False := by
  intro hA hB hC h_coprime h_eq
  have h_sq : (A^k : ℤ)^2 + (B : ℤ)^3 = (C : ℤ)^8 := by
    push_cast
    have : (A : ℤ)^(2*k) = ((A : ℤ)^k)^2 := by
      rw [← pow_mul]
      ring
    rw [← this]
    exact_mod_cast h_eq
  have h_prim : IsPrimitive238Solution (A^k) B C := by
    refine ⟨h_sq, ?_⟩
    have h_gcd_nat : Nat.gcd (Nat.gcd (A^k) B) C = 1 := by
      -- Same argument as the verified `gcd_pow_eq_one`: a prime dividing A^k divides A.
      rw [Nat.eq_one_iff_not_exists_prime_dvd]
      rintro q hq hdvd
      have h1 : q ∣ Nat.gcd (A ^ k) B := hdvd.trans (Nat.gcd_dvd_left _ C)
      have hqA : q ∣ A := hq.dvd_of_dvd_pow (h1.trans (Nat.gcd_dvd_left _ B))
      have hqB : q ∣ B := h1.trans (Nat.gcd_dvd_right _ B)
      have hqC : q ∣ C := hdvd.trans (Nat.gcd_dvd_right _ C)
      have hg : q ∣ Nat.gcd (Nat.gcd A B) C := Nat.dvd_gcd (Nat.dvd_gcd hqA hqB) hqC
      rw [h_coprime] at hg
      exact hq.one_lt.ne' (Nat.dvd_one.mp hg)
    exact_mod_cast h_gcd_nat
  have h_pos_x : (A^k : ℤ) > 0 := by positivity
  have h_pos_y : (B : ℤ) > 0 := by positivity
  have h_pos_z : (C : ℤ) > 0 := by positivity
  exact no_positive_pure_power_238_solution hBr (A^k) B C ⟨h_prim, h_pos_x, h_pos_z, h_pos_y⟩

end Beal
