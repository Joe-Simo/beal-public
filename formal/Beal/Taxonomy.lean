/-
Copyright (c) 2026 Formal Verification Group. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Formal Verification Specialist
-/
import Beal.Conjecture
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# Signature Taxonomy and Curvature Classification for Generalized Fermat Equations

This module formalizes the **geometric and curvature taxonomy** of Generalized Fermat
Equations of signature $(p, q, r)$:
  $$A^p + B^q = C^r$$
with particular focus on the domain of the **Beal Conjecture** ($p, q, r \ge 3$).

## Background and Darmon–Granville Theory

The arithmetic behavior of generalized Fermat equations is governed by the Euler characteristic
(or orbifold Euler characteristic) of the associated stack / curve:
  $$\chi(p, q, r) = \frac{1}{p} + \frac{1}{q} + \frac{1}{r} - 1.$$

Clearing denominators, we define the integer curvature invariant:
  $$E(p, q, r) = q r + p r + p q - p q r.$$

Notice that for $p, q, r > 0$:
  $$\chi(p, q, r) = \frac{E(p, q, r)}{p q r}$$
and hence $\operatorname{sign}(\chi) = \operatorname{sign}(E)$.

Three geometric regimes arise:
1. **Spherical ($\chi > 0, E > 0$)**: Finitely many exception signatures; can admit infinitely
   many primitive integer solutions (e.g., $(2, 2, r)$ Pythagorean triples, $(2, 3, 3), (2, 3, 4), (2, 3, 5)$).
2. **Parabolic / Euclidean ($\chi = 0, E = 0$)**: Exactly three signature classes up to permutation:
   $(3, 3, 3)$, $(2, 4, 4)$, and $(2, 3, 6)$, corresponding to curves of genus 1.
3. **Hyperbolic ($\chi < 0, E < 0$)**: The orbifold has negative curvature and genus $g > 1$.
   By the landmark theorem of **Darmon and Granville (1995)**, any hyperbolic generalized
   Fermat equation has at most **finitely many** primitive integer solutions.

## Main Results Formalized Here:
- Definition of the curvature invariant $E(p, q, r)$ and classification into `SignatureCurvature`.
- **Classification of Parabolic Signatures**: $(3, 3, 3)$ is the *unique* parabolic signature in the Beal domain $p, q, r \ge 3$.
- **Universal Hyperbolicity of Non-Cubic Beal Signatures**: For all $p, q, r \ge 3$ with $(p, q, r) \ne (3, 3, 3)$,
  $E(p, q, r) < 0$ and $\chi(p, q, r) \le -1/12$.
- **Darmon–Granville Finiteness Framing**: Connection between hyperbolicity and the Beal conjecture.
-/

namespace Beal

/--
The integer curvature invariant $E(p, q, r) = qr + pr + pq - pqr$,
corresponding to the numerator of $\chi(p, q, r) = 1/p + 1/q + 1/r - 1$.
-/
def curvatureNumerator (p q r : ℕ) : ℤ :=
  (q * r : ℤ) + (p * r : ℤ) + (p * q : ℤ) - (p * q * r : ℤ)

/--
Geometric curvature classification of a signature $(p, q, r)$.
-/
inductive SignatureCurvature where
  | Spherical   -- χ > 0 (E > 0)
  | Parabolic   -- χ = 0 (E = 0)
  | Hyperbolic  -- χ < 0 (E < 0)
  deriving DecidableEq, Repr

/--
Compute the curvature type of a signature $(p, q, r)$ from its integer invariant $E(p, q, r)$.
-/
def signatureCurvature (p q r : ℕ) : SignatureCurvature :=
  let E := curvatureNumerator p q r
  if E > 0 then SignatureCurvature.Spherical
  else if E = 0 then SignatureCurvature.Parabolic
  else SignatureCurvature.Hyperbolic

/--
Predicate specifying that a signature $(p, q, r)$ is strictly hyperbolic ($E < 0$).
-/
def IsHyperbolicSignature (p q r : ℕ) : Prop :=
  curvatureNumerator p q r < 0

/--
Predicate specifying that a signature $(p, q, r)$ lies in the Beal conjecture domain ($p, q, r \ge 3$).
-/
def IsBealSignature (p q r : ℕ) : Prop :=
  p ≥ 3 ∧ q ≥ 3 ∧ r ≥ 3

/-! ### 1. Parabolic Signatures (χ = 0) -/

/--
The cubic signature $(3, 3, 3)$ has zero curvature ($E = 0$): this is the classical Fermat cubic.
-/
theorem curvature_3_3_3 : curvatureNumerator 3 3 3 = 0 := by
  unfold curvatureNumerator
  decide

/--
The signature $(2, 4, 4)$ has zero curvature ($E = 0$).
-/
theorem curvature_2_4_4 : curvatureNumerator 2 4 4 = 0 := by
  unfold curvatureNumerator
  decide

/--
The signature $(2, 3, 6)$ has zero curvature ($E = 0$).
-/
theorem curvature_2_3_6 : curvatureNumerator 2 3 6 = 0 := by
  unfold curvatureNumerator
  decide

/--
The three canonical Euclidean signatures are recognized as parabolic by the computable classifier.
-/
theorem classifier_parabolic_cases :
    signatureCurvature 3 3 3 = SignatureCurvature.Parabolic ∧
    signatureCurvature 2 4 4 = SignatureCurvature.Parabolic ∧
    signatureCurvature 2 3 6 = SignatureCurvature.Parabolic := by
  decide

/-! ### 2. Classification in the Beal Domain ($p, q, r \ge 3$) -/

/--
Explicit formula for $E(3, 3, r)$ showing linear dependence on $r$:
$$E(3, 3, r) = 3(3 - r).$$
-/
lemma curvature_3_3_r (r : ℕ) :
    curvatureNumerator 3 3 r = 3 * (3 - (r : ℤ)) := by
  unfold curvatureNumerator
  ring

/--
If two exponents are 3, the curvature numerator is strictly negative for all $r \ge 4$.
-/
theorem curvature_3_3_r_neg (r : ℕ) (hr : r ≥ 4) :
    curvatureNumerator 3 3 r < 0 := by
  rw [curvature_3_3_r]
  have : (r : ℤ) ≥ 4 := by omega
  nlinarith

/--
**Uniqueness of Parabolic Signature in Beal Domain**:
Among all exponents $p, q, r \ge 3$, the cubic signature $(3, 3, 3)$ is the
**unique** signature with zero curvature ($E = 0$).
-/
theorem beal_parabolic_unique (p q r : ℕ) (hp : p ≥ 3) (hq : q ≥ 3) (hr : r ≥ 3)
    (h_ord : p ≤ q ∧ q ≤ r) :
    curvatureNumerator p q r = 0 ↔ (p = 3 ∧ q = 3 ∧ r = 3) := by
  obtain ⟨hpq, hqr⟩ := h_ord
  constructor
  · intro hE
    unfold curvatureNumerator at hE
    have hP : (3 : ℤ) ≤ (p : ℤ) := by exact_mod_cast hp
    have hQ : (3 : ℤ) ≤ (q : ℤ) := by exact_mod_cast hq
    have hR : (3 : ℤ) ≤ (r : ℤ) := by exact_mod_cast hr
    have hPQ : (p : ℤ) ≤ (q : ℤ) := by exact_mod_cast hpq
    have hQR : (q : ℤ) ≤ (r : ℤ) := by exact_mod_cast hqr
    -- pqr = qr + pr + pq <= 3qr, so p <= 3
    have hp3 : (p : ℤ) = 3 := by nlinarith [mul_pos (by linarith : (0:ℤ) < q) (by linarith : (0:ℤ) < r)]
    rw [hp3] at hE
    -- now 2qr = 3q + 3r <= 6r, so q <= 3
    have hq3 : (q : ℤ) = 3 := by nlinarith
    rw [hq3] at hE
    have hr3 : (r : ℤ) = 3 := by linarith
    exact ⟨by exact_mod_cast hp3, by exact_mod_cast hq3, by exact_mod_cast hr3⟩
  · rintro ⟨rfl, rfl, rfl⟩
    unfold curvatureNumerator
    norm_num

/--
**Curvature Upper Bound in the Beal Domain**:
The maximal curvature in the Beal domain among non-cubic signatures occurs at $(3, 3, 4)$,
where $E(3, 3, 4) = -3$.
For all sorted triples $3 \le p \le q \le r$ not all 3, $E(p, q, r) \le -3$.
-/
theorem curvature_upper_bound_beal (p q r : ℕ)
    (h_beal : IsBealSignature p q r)
    (h_not_all_3 : ¬(p = 3 ∧ q = 3 ∧ r = 3))
    (h_ord : p ≤ q ∧ q ≤ r) :
    curvatureNumerator p q r ≤ -3 := by
  obtain ⟨hpq, hqr⟩ := h_ord
  obtain ⟨hp, hq, hr⟩ := h_beal
  unfold curvatureNumerator
  have hP : (3 : ℤ) ≤ (p : ℤ) := by exact_mod_cast hp
  have hQ : (3 : ℤ) ≤ (q : ℤ) := by exact_mod_cast hq
  have hR : (3 : ℤ) ≤ (r : ℤ) := by exact_mod_cast hr
  have hPQ : (p : ℤ) ≤ (q : ℤ) := by exact_mod_cast hpq
  have hQR : (q : ℤ) ≤ (r : ℤ) := by exact_mod_cast hqr
  have hQpos : (0 : ℤ) < (q : ℤ) := by linarith
  have hRpos : (0 : ℤ) < (r : ℤ) := by linarith
  rcases Nat.lt_or_ge 3 p with hp4 | hp3
  · -- p ≥ 4 :  E ≤ 3qr - pqr = qr(3-p) ≤ -qr ≤ -9
    have h4 : (4 : ℤ) ≤ (p : ℤ) := by exact_mod_cast hp4
    have e1 : (p : ℤ) * r ≤ (q : ℤ) * r := by nlinarith
    have e2 : (p : ℤ) * q ≤ (q : ℤ) * r := by nlinarith
    have e3 : (4 : ℤ) * ((q : ℤ) * r) ≤ (p : ℤ) * q * r := by
      have hqr : (0 : ℤ) ≤ (q : ℤ) * r := by positivity
      calc (4 : ℤ) * ((q : ℤ) * r) ≤ (p : ℤ) * ((q : ℤ) * r) :=
            mul_le_mul_of_nonneg_right h4 hqr
        _ = (p : ℤ) * q * r := by ring
    have e4 : (9 : ℤ) ≤ (q : ℤ) * r := by nlinarith
    linarith
  · have hp3' : p = 3 := by omega
    subst hp3'
    rcases Nat.lt_or_ge 3 q with hq4 | hq3
    · -- p = 3, q ≥ 4 :  E = 3q + 3r - 2qr ≤ 3r + 3r - 8r = -2r ≤ -8
      have h4 : (4 : ℤ) ≤ (q : ℤ) := by exact_mod_cast hq4
      have e1 : (8 : ℤ) * r ≤ 2 * ((q : ℤ) * r) := by nlinarith
      push_cast
      linarith
    · have hq3' : q = 3 := by omega
      subst hq3'
      -- p = q = 3, r ≥ 4 :  E = 9 - 3r ≤ -3
      have hr4 : (4 : ℤ) ≤ (r : ℤ) := by
        rcases Nat.lt_or_ge 3 r with h | h
        · exact_mod_cast h
        · exact absurd ⟨rfl, rfl, by omega⟩ h_not_all_3
      push_cast
      linarith

/--
**Strict Hyperbolicity of Non-Cubic Beal Signatures**:
Every signature $(p, q, r)$ with $p, q, r \ge 3$ other than $(3, 3, 3)$
is strictly hyperbolic ($E < 0$).
-/
theorem beal_non_cubic_is_hyperbolic (p q r : ℕ)
    (h_beal : IsBealSignature p q r)
    (h_not_all_3 : ¬(p = 3 ∧ q = 3 ∧ r = 3))
    (h_ord : p ≤ q ∧ q ≤ r) :
    IsHyperbolicSignature p q r := by
  have h := curvature_upper_bound_beal p q r h_beal h_not_all_3 h_ord
  unfold IsHyperbolicSignature
  linarith

/-! ### 3. Canonical Signature Classification Table -/

theorem classify_3_3_4 : signatureCurvature 3 3 4 = SignatureCurvature.Hyperbolic := by decide
theorem classify_3_4_5 : signatureCurvature 3 4 5 = SignatureCurvature.Hyperbolic := by decide
theorem classify_4_4_4 : signatureCurvature 4 4 4 = SignatureCurvature.Hyperbolic := by decide
theorem classify_5_5_5 : signatureCurvature 5 5 5 = SignatureCurvature.Hyperbolic := by decide
theorem classify_2_3_7 : signatureCurvature 2 3 7 = SignatureCurvature.Hyperbolic := by decide
theorem classify_2_3_5 : signatureCurvature 2 3 5 = SignatureCurvature.Spherical  := by decide



/-! ## A sharp curvature bound: every Beal signature has `|χ| ≥ 1/12` -/

/-- **Sharp curvature bound.**  For `p, q, r ≥ 3` not all equal to 3,
`11pqr ≥ 12(qr + pr + pq)`, which is exactly `|χ| ≥ 1/12` for
`χ = 1/p + 1/q + 1/r - 1`.

Equality holds precisely at the permutations of `(3,3,4)`.  This strictly strengthens
`curvature_upper_bound_beal`, whose bound `E ≤ -3` is weak once `pqr` is large. -/
theorem curvature_sharp_bound (p q r : ℕ) (hp : p ≥ 3) (hq : q ≥ 3) (hr : r ≥ 3)
    (h_not_all_3 : ¬(p = 3 ∧ q = 3 ∧ r = 3)) :
    12 * (q * r + p * r + p * q) ≤ 11 * (p * q * r) := by
  -- at least one exponent is ≥ 4; handle by symmetry
  have key : ∀ a b c : ℕ, 3 ≤ a → 3 ≤ b → 4 ≤ c →
      12 * (b * c + a * c + a * b) ≤ 11 * (a * b * c) := by
    intro a b c ha hb hc
    nlinarith [Nat.mul_le_mul ha hb, Nat.mul_le_mul hb hc, Nat.mul_le_mul ha hc,
               Nat.mul_le_mul (Nat.mul_le_mul ha hb) hc]
  rcases Nat.lt_or_ge 3 r with h | h
  · exact key p q r hp hq h
  · rcases Nat.lt_or_ge 3 q with h2 | h2
    · have := key p r q hp hr h2; linarith [this]
    · rcases Nat.lt_or_ge 3 p with h3 | h3
      · have := key q r p hq hr h3; linarith [this]
      · exact absurd ⟨by omega, by omega, by omega⟩ h_not_all_3
