/-
Copyright (c) 2026 Formal Verification Group. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Formal Verification Specialist
-/
import Beal.Conjecture
import Beal.Taxonomy
import Mathlib.Algebra.Ring.Basic
import Mathlib.Data.Nat.Basic
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Omega

/-!
# Complete Curvature Taxonomy and Darmon Modular Frey Curve Assignments

This module formalizes the complete classification of Generalized Fermat signatures
$(p, q, r)$ according to their geometric curvature:
  $$\chi(p, q, r) = \frac{1}{p} + \frac{1}{q} + \frac{1}{r} - 1$$
and establishes the foundational Frey curve parameterizations in **Darmon's Program**
for hyperbolic signatures:
  $$\frac{1}{p} + \frac{1}{q} + \frac{1}{r} < 1.$$

## 1. Complete Geometric Taxonomy of Signatures

For sorted exponents $2 \le p \le q \le r$:

1. **Spherical Signatures ($\chi > 0 \iff E > 0$)**:
   - The infinite family $(2, 2, r)$ for all $r \ge 2$: dihedral / Pythagorean regime, $E(2, 2, r) = 4 > 0$.
   - $(2, 3, 3)$: tetrahedral, $E(2, 3, 3) = 3 > 0$.
   - $(2, 3, 4)$: octahedral, $E(2, 3, 4) = 2 > 0$.
   - $(2, 3, 5)$: icosahedral, $E(2, 3, 5) = 1 > 0$.
   These four classes constitute the **exhaustive** list of spherical signatures.

2. **Parabolic Signatures ($\chi = 0 \iff E = 0$)**:
   - $(2, 3, 6)$: $E(2, 3, 6) = 0$.
   - $(2, 4, 4)$: $E(2, 4, 4) = 0$.
   - $(3, 3, 3)$: $E(3, 3, 3) = 0$.
   These three classes constitute the **unique** parabolic signatures.

3. **Hyperbolic Signatures ($\chi < 0 \iff E < 0$)**:
   - All other signatures $(p, q, r)$ with $p, q, r \ge 2$, including the entire
     Beal conjecture domain ($p, q, r \ge 3$) with $(p, q, r) \ne (3, 3, 3)$.
   - By the **Darmon–Granville Theorem (1995)**, every hyperbolic signature equation
     $A^p + B^q = C^r$ has at most finitely many primitive integer solutions.

## 2. Darmon Modular Frey Curve Assignments

To resolve generalized Fermat equations of hyperbolic signature, Henri Darmon (1997)
systematized the modular method by attaching Frey curves (or Frey abelian varieties)
to solutions $(A, B, C)$:

1. **Signature $(p, p, p)$ — Hellegouarch–Frey Curve**:
   $$E : y^2 = x(x - A^p)(x + B^p)$$
   attached to $A^p + B^p = C^p$, with discriminant $\Delta = 16 (A B C)^{2p}$,
   level-lowering to $N = 2$, where $\dim S_2(\Gamma_0(2)) = 0$ yields FLT (Wiles 1995).

2. **Signature $(2, 3, p)$ — Frey–Kraus Curve**:
   $$E : y^2 = x^3 + 3Bx + 2A$$
   attached to $A^2 + B^3 = C^p$, with discriminant $\Delta = -1728 (A^2 + B^3) = -1728 C^p$.

3. **Signature $(2, 4, p)$ — Ellenberg's $\mathbb{Q}$-Curve**:
   $$E : y^2 = x^3 + 2(1+i)Ax^2 + (B + iA^2)x \quad \text{over } \mathbb{Q}(i)$$
   attached to $A^4 + B^2 = C^p$, with discriminant $\Delta = -64i (A^2 + iB)(A^2 - iB)^2$,
   where $(A^2 + iB)(A^2 - iB) = A^4 + B^2 = C^p$.

4. **Signature $(3, 3, p)$ — Kraus Frey Curve**:
   $$E : y^2 = x^3 + 3ABx + (B^3 - A^3)$$
   attached to $A^3 + B^3 = C^p$, with discriminant $\Delta = -432 (A^3 + B^3)^2 = -2^4 \cdot 3^3 C^{2p}$,
   in which the product $AB$ completely cancels from the discriminant.

5. **Signature $(5, 5, p)$ — Billerey / Darmon Curve**:
   $$W_{A, B} : y^2 = x^3 - 5(A^2 + B^2)x^2 + 5(A^4 - A^3B + A^2B^2 - AB^3 + B^4)x$$
   attached to $A^5 + B^5 = C^p$, with polynomial discriminant $\Delta = 5^3 (A+B)^2 (A^5+B^5)^2$.

## References
* H. Darmon and A. Granville, *On the equations $z^m = F(x, y)$ and $Ax^p + By^q = Cz^r$*,
  Bull. London Math. Soc. 27 (1995), 513–543.
* H. Darmon, *Rigid local systems, Hilbert modular forms, and Fermat's Last Theorem*,
  Ann. of Math. 149 (1999), 415–425.
* J. S. Ellenberg, *Galois representations attached to $\mathbb{Q}$-curves and the generalized Fermat equation $A^4 + B^2 = C^p$*,
  Amer. J. Math. 126 (2004), 763–787.
* A. Kraus, *Sur l'équation $a^3 + b^3 = c^p$*, Exp. Math. 7 (1998), 1–13.
* N. Billerey, *Équations de Fermat de type $(5, 5, p)$*, Bull. Austral. Math. Soc. 76 (2007), 161–194.
* N. Billerey, I. Chen, L. Dieulefait, and N. Freitas, *A multi-Frey approach to Fermat equations of signature $(r, r, p)$*,
  Trans. Amer. Math. Soc. 371 (2019), 8651–8677.
-/

namespace Beal

variable {R : Type*} [CommRing R]

/-! ### 1. Integer Curvature Formulas -/

/--
Curvature numerator for the family $(2, 2, r)$ is constant and equal to $4$.
-/
lemma curvature_2_2_r (r : ℕ) :
    curvatureNumerator 2 2 r = 4 := by
  unfold curvatureNumerator
  ring

/--
Curvature numerator for $(2, 3, r)$ is $6 - r$.
-/
lemma curvature_2_3_r (r : ℕ) :
    curvatureNumerator 2 3 r = 6 - (r : ℤ) := by
  unfold curvatureNumerator
  ring

/--
Curvature numerator for $(2, 4, r)$ is $8 - 2r = 2(4 - r)$.
-/
lemma curvature_2_4_r (r : ℕ) :
    curvatureNumerator 2 4 r = 8 - 2 * (r : ℤ) := by
  unfold curvatureNumerator
  ring

/--
Curvature numerator for $(2, 5, r)$ is $10 - 3r$.
-/
lemma curvature_2_5_r (r : ℕ) :
    curvatureNumerator 2 5 r = 10 - 3 * (r : ℤ) := by
  unfold curvatureNumerator
  ring

/-! ### 2. Complete Classification of Spherical Signatures -/

/--
The infinite family $(2, 2, r)$ is strictly spherical for all $r \ge 2$.
-/
theorem spherical_2_2_r (r : ℕ) (hr : r ≥ 2) :
    curvatureNumerator 2 2 r > 0 := by
  rw [curvature_2_2_r]
  decide

theorem spherical_2_3_3 : curvatureNumerator 2 3 3 > 0 := by decide
theorem spherical_2_3_4 : curvatureNumerator 2 3 4 > 0 := by decide
theorem spherical_2_3_5 : curvatureNumerator 2 3 5 > 0 := by decide

/--
The classifier marks the canonical spherical cases as Spherical.
-/
theorem classifier_spherical_cases :
    signatureCurvature 2 3 3 = SignatureCurvature.Spherical ∧
    signatureCurvature 2 3 4 = SignatureCurvature.Spherical ∧
    signatureCurvature 2 3 5 = SignatureCurvature.Spherical := by
  decide

/--
**Complete Classification of Spherical Signatures**:
For sorted exponents $2 \le p \le q \le r$, the curvature numerator is strictly positive
if and only if $(p, q) = (2, 2)$ or $(p, q, r) \in \{(2, 3, 3), (2, 3, 4), (2, 3, 5)\}$.
-/
theorem spherical_signatures_exhaustive (p q r : ℕ)
    (hp : p ≥ 2) (hq : q ≥ 2) (hr : r ≥ 2)
    (h_ord : p ≤ q ∧ q ≤ r) :
    curvatureNumerator p q r > 0 ↔
      (p = 2 ∧ q = 2) ∨
      (p = 2 ∧ q = 3 ∧ r = 3) ∨
      (p = 2 ∧ q = 3 ∧ r = 4) ∨
      (p = 2 ∧ q = 3 ∧ r = 5) := by
  constructor
  · intro hE
    rcases eq_or_lt_of_le hp with rfl | hp3
    · -- Case p = 2
      rcases eq_or_lt_of_le hq.left with rfl | hq3
      · left; exact ⟨rfl, rfl⟩
      · rcases eq_or_lt_of_le hq3 with rfl | hq4
        · -- Subcase p = 2, q = 3
          rw [curvature_2_3_r] at hE
          have hr_le_5 : r ≤ 5 := by omega
          have hr_ge_3 : r ≥ 3 := h_ord.2
          interval_cases r
          · right; left; exact ⟨rfl, rfl, rfl⟩
          · right; right; left; exact ⟨rfl, rfl, rfl⟩
          · right; right; right; exact ⟨rfl, rfl, rfl⟩
        · rcases eq_or_lt_of_le hq4 with rfl | hq5
          · -- Subcase p = 2, q = 4
            rw [curvature_2_4_r] at hE
            have hr_ge_4 : r ≥ 4 := h_ord.2
            have : (r : ℤ) < 4 := by omega
            omega
          · -- Subcase p = 2, q ≥ 5
            have hr_ge_q : (r : ℤ) ≥ (q : ℤ) := by omega
            have hq_ge_5 : (q : ℤ) ≥ 5 := by omega
            unfold curvatureNumerator at hE
            have : (q : ℤ) * r + 2 * r + 2 * q - 2 * q * r < 0 := by
              nlinarith
            omega
    · -- Case p ≥ 3
      rcases eq_or_lt_of_le hp3 with rfl | hp4
      · -- Subcase p = 3
        rcases eq_or_lt_of_le hq.left with rfl | hq4
        · -- Subcase p = 3, q = 3
          rw [curvature_3_3_r] at hE
          have hr_ge_3 : r ≥ 3 := h_ord.2
          have : (r : ℤ) < 3 := by omega
          omega
        · -- Subcase p = 3, q ≥ 4
          have hr_ge_q : (r : ℤ) ≥ (q : ℤ) := by omega
          have hq_ge_4 : (q : ℤ) ≥ 4 := by omega
          unfold curvatureNumerator at hE
          have : (q : ℤ) * r + 3 * r + 3 * q - 3 * q * r < 0 := by
            nlinarith
          omega
      · -- Case p ≥ 4
        have hq_ge_p : (q : ℤ) ≥ (p : ℤ) := by omega
        have hr_ge_q : (r : ℤ) ≥ (q : ℤ) := by omega
        have hp_ge_4 : (p : ℤ) ≥ 4 := by omega
        unfold curvatureNumerator at hE
        have : (q : ℤ) * r + (p : ℤ) * r + (p : ℤ) * q - (p : ℤ) * q * r < 0 := by
          nlinarith
        omega
  · rintro (⟨rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩)
    · exact spherical_2_2_r r hr
    · exact spherical_2_3_3
    · exact spherical_2_3_4
    · exact spherical_2_3_5

/-! ### 3. Complete Classification of Parabolic Signatures -/

theorem parabolic_2_3_6 : curvatureNumerator 2 3 6 = 0 := by decide
theorem parabolic_2_4_4 : curvatureNumerator 2 4 4 = 0 := by decide
theorem parabolic_3_3_3 : curvatureNumerator 3 3 3 = 0 := by decide

/--
**Complete Uniqueness of Parabolic Signatures**:
For sorted exponents $2 \le p \le q \le r$, the curvature numerator is zero
if and only if $(p, q, r)$ is $(2, 3, 6)$, $(2, 4, 4)$, or $(3, 3, 3)$.
-/
theorem parabolic_signatures_exhaustive (p q r : ℕ)
    (hp : p ≥ 2) (hq : q ≥ 2) (hr : r ≥ 2)
    (h_ord : p ≤ q ∧ q ≤ r) :
    curvatureNumerator p q r = 0 ↔
      (p = 2 ∧ q = 3 ∧ r = 6) ∨
      (p = 2 ∧ q = 4 ∧ r = 4) ∨
      (p = 3 ∧ q = 3 ∧ r = 3) := by
  constructor
  · intro hE
    rcases eq_or_lt_of_le hp with rfl | hp3
    · -- Case p = 2
      rcases eq_or_lt_of_le hq.left with rfl | hq3
      · -- Subcase p = 2, q = 2
        rw [curvature_2_2_r] at hE
        omega
      · rcases eq_or_lt_of_le hq3 with rfl | hq4
        · -- Subcase p = 2, q = 3
          rw [curvature_2_3_r] at hE
          have : (r : ℤ) = 6 := by omega
          have hr6 : r = 6 := by omega
          left
          exact ⟨rfl, rfl, hr6⟩
        · rcases eq_or_lt_of_le hq4 with rfl | hq5
          · -- Subcase p = 2, q = 4
            rw [curvature_2_4_r] at hE
            have : (r : ℤ) = 4 := by omega
            have hr4 : r = 4 := by omega
            right; left
            exact ⟨rfl, rfl, hr4⟩
          · -- Subcase p = 2, q ≥ 5
            have hr_ge_q : (r : ℤ) ≥ (q : ℤ) := by omega
            have hq_ge_5 : (q : ℤ) ≥ 5 := by omega
            unfold curvatureNumerator at hE
            have : (q : ℤ) * r + 2 * r + 2 * q - 2 * q * r < 0 := by
              nlinarith
            omega
    · -- Case p ≥ 3
      rcases eq_or_lt_of_le hp3 with rfl | hp4
      · -- Subcase p = 3
        rcases eq_or_lt_of_le hq.left with rfl | hq4
        · -- Subcase p = 3, q = 3
          have h_sub := curvature_3_3_r r
          rw [h_sub] at hE
          have : (r : ℤ) = 3 := by omega
          have hr3 : r = 3 := by omega
          right; right
          exact ⟨rfl, rfl, hr3⟩
        · -- Subcase p = 3, q ≥ 4
          have hr_ge_q : (r : ℤ) ≥ (q : ℤ) := by omega
          have hq_ge_4 : (q : ℤ) ≥ 4 := by omega
          unfold curvatureNumerator at hE
          have : (q : ℤ) * r + 3 * r + 3 * q - 3 * q * r < 0 := by
            nlinarith
          omega
      · -- Case p ≥ 4
        have hq_ge_p : (q : ℤ) ≥ (p : ℤ) := by omega
        have hr_ge_q : (r : ℤ) ≥ (q : ℤ) := by omega
        have hp_ge_4 : (p : ℤ) ≥ 4 := by omega
        unfold curvatureNumerator at hE
        have : (q : ℤ) * r + (p : ℤ) * r + (p : ℤ) * q - (p : ℤ) * q * r < 0 := by
          nlinarith
        omega
  · rintro (⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩)
    · exact parabolic_2_3_6
    · exact parabolic_2_4_4
    · exact parabolic_3_3_3

/-! ### 4. Complete Classification of Hyperbolic Signatures -/

/--
**Hyperbolic Trichotomy**:
Every signature $(p, q, r)$ with $2 \le p \le q \le r$ that is neither spherical nor parabolic
is strictly hyperbolic ($E < 0$).
-/
theorem hyperbolic_of_not_spherical_nor_parabolic (p q r : ℕ)
    (h_not_sph : ¬ curvatureNumerator p q r > 0)
    (h_not_par : ¬ curvatureNumerator p q r = 0) :
    IsHyperbolicSignature p q r := by
  unfold IsHyperbolicSignature
  omega

/--
Every non-cubic Beal signature ($p, q, r \ge 3$ not all 3) is strictly hyperbolic.
-/
theorem beal_domain_strictly_hyperbolic (p q r : ℕ)
    (h_beal : IsBealSignature p q r)
    (h_not_333 : ¬(p = 3 ∧ q = 3 ∧ r = 3))
    (h_ord : p ≤ q ∧ q ≤ r) :
    IsHyperbolicSignature p q r :=
  beal_non_cubic_is_hyperbolic p q r h_beal h_not_333 h_ord

/-! ### 5. Darmon Modular Frey Curve Assignments -/

/-! #### A. Signature (p, p, p) — Hellegouarch–Frey Curve -/

/--
Cubic model $y^2 = x^3 + a_2 x^2 + a_4 x$ for the Hellegouarch–Frey curve
attached to $A^p + B^p = C^p$:
  $$y^2 = x(x - A^p)(x + B^p) = x^3 + (B^p - A^p)x^2 - A^p B^p x.$$
-/
structure HellegouarchModel (R : Type*) where
  a2 : R
  a4 : R

def hellegouarchCurve (Ap Bp : ℤ) : HellegouarchModel ℤ :=
  { a2 := Bp - Ap,
    a4 := - (Ap * Bp) }

/--
Factorization showing the three rational 2-torsion roots $0, A^p, -B^p$:
-/
theorem hellegouarch_roots_vanishing (x Ap Bp : ℤ) :
    x * (x - Ap) * (x + Bp) = x ^ 3 + (Bp - Ap) * x ^ 2 - (Ap * Bp) * x := by
  ring

/--
The root difference product identity for the Hellegouarch discriminant:
  $$(e_1 - e_2)^2 (e_1 - e_3)^2 (e_2 - e_3)^2 = (A^p)^2 (B^p)^2 (A^p + B^p)^2.$$
-/
theorem hellegouarch_discriminant_core (Ap Bp : ℤ) :
    (0 - Ap) ^ 2 * (0 - (-Bp)) ^ 2 * (Ap - (-Bp)) ^ 2 =
    (Ap * Bp * (Ap + Bp)) ^ 2 := by
  ring

/--
The minimal discriminant of the Hellegouarch–Frey curve:
  $$\Delta = 16 (A B C)^{2p}.$$
-/
def hellegouarchDiscriminant (A B C : ℤ) (p : ℕ) : ℤ :=
  16 * (A * B * C) ^ (2 * p)

/-! #### B. Signature (2, 3, p) — Frey–Kraus Curve -/

/--
Short Weierstrass model for the Frey–Kraus curve attached to $A^2 + B^3 = C^p$:
  $$y^2 = x^3 + 3Bx + 2A.$$
-/
structure ShortModel (R : Type*) where
  a4 : R
  a6 : R

def ShortModel.discriminant (E : ShortModel R) : R :=
  -16 * (4 * E.a4 ^ 3 + 27 * E.a6 ^ 2)

def freyKrausCurve (A B : ℤ) : ShortModel ℤ :=
  { a4 := 3 * B,
    a6 := 2 * A }

/--
**Frey–Kraus Discriminant Identity**:
The Weierstrass discriminant factors as:
  $$\Delta = -1728 (A^2 + B^3) = -2^6 \cdot 3^3 (A^2 + B^3).$$
-/
theorem frey_kraus_discriminant_eq (A B : ℤ) :
    (freyKrausCurve A B).discriminant =
    -1728 * (A ^ 2 + B ^ 3) := by
  unfold ShortModel.discriminant freyKrausCurve
  ring

/--
On any solution to $A^2 + B^3 = C^p$, the Frey–Kraus discriminant is:
  $$\Delta = -1728 C^p.$$
-/
theorem frey_kraus_discriminant_on_solution (A B C : ℤ) (p : ℕ)
    (heq : A ^ 2 + B ^ 3 = C ^ p) :
    (freyKrausCurve A B).discriminant = -1728 * C ^ p := by
  rw [frey_kraus_discriminant_eq, heq]

/-! #### C. Signature (2, 4, p) — Ellenberg's ℚ-Curve -/

/--
Ellenberg's Frey ℚ-curve coefficients attached to $A^4 + B^2 = C^p$,
defined over $K = \mathbb{Q}(i)$:
  $$y^2 = x^3 + 2(1 + i)Ax^2 + (B + iA^2)x.$$
-/
structure EllenbergCurveCoefficients (R : Type*) where
  a2_re : R  -- 2A
  a2_im : R  -- 2A  (so a₂ = 2(1+i)A)
  a4_re : R  -- B
  a4_im : R  -- A²  (so a₄ = B + iA²)

def ellenbergCurve (A B : ℤ) : EllenbergCurveCoefficients ℤ :=
  { a2_re := 2 * A,
    a2_im := 2 * A,
    a4_re := B,
    a4_im := A ^ 2 }

/--
Gaussian norm factorization of the discriminant factor in $\mathbb{Z}[i]$:
  $$N(A^2 + iB) = (A^2)^2 + B^2 = A^4 + B^2 = C^p.$$
-/
theorem ellenberg_gaussian_norm_identity (A B : ℤ) :
    (A ^ 2) ^ 2 + B ^ 2 = A ^ 4 + B ^ 2 := by
  ring

/--
On any solution to $A^4 + B^2 = C^p$, the Gaussian norm of the prime-to-2 factor
of the discriminant is exactly $C^p$.
-/
theorem ellenberg_norm_on_solution (A B C : ℤ) (p : ℕ)
    (heq : A ^ 4 + B ^ 2 = C ^ p) :
    (A ^ 2) ^ 2 + B ^ 2 = C ^ p := by
  rw [ellenberg_gaussian_norm_identity, heq]

/-! #### D. Signature (3, 3, p) — Kraus Frey Curve -/

/--
Kraus's Frey elliptic curve attached to $A^3 + B^3 = C^p$:
  $$y^2 = x^3 + 3ABx + (B^3 - A^3).$$
-/
def krausCurve33p (A B : ℤ) : ShortModel ℤ :=
  { a4 := 3 * A * B,
    a6 := B ^ 3 - A ^ 3 }

/--
**Kraus Discriminant Identity**:
  $$\Delta(E_{A, B}) = -432 (A^3 + B^3)^2 = -2^4 \cdot 3^3 (A^3 + B^3)^2.$$
Remarkably, $AB$ cancels completely from the discriminant!
-/
theorem kraus_33p_discriminant_eq (A B : ℤ) :
    (krausCurve33p A B).discriminant =
    -432 * (A ^ 3 + B ^ 3) ^ 2 := by
  unfold ShortModel.discriminant krausCurve33p
  ring

/--
On any solution to $A^3 + B^3 = C^p$, the Kraus discriminant simplifies to
  $$\Delta = -432 C^{2p}.$$
-/
theorem kraus_33p_discriminant_on_solution (A B C : ℤ) (p : ℕ)
    (heq : A ^ 3 + B ^ 3 = C ^ p) :
    (krausCurve33p A B).discriminant = -432 * (C ^ p) ^ 2 := by
  rw [kraus_33p_discriminant_eq, heq]

/-! #### E. Signature (5, 5, p) — Billerey / Darmon Curve -/

/--
The degree-4 cyclotomic quotient polynomial $H_5(A, B) = (A^5 + B^5) / (A + B)$:
  $$H_5(A, B) = A^4 - A^3 B + A^2 B^2 - A B^3 + B^4.$$
-/
def cyclotomicQuinticQuotient (A B : ℤ) : ℤ :=
  A ^ 4 - A ^ 3 * B + A ^ 2 * B ^ 2 - A * B ^ 3 + B ^ 4

/--
Exact polynomial factorization identity: $(A + B) \cdot H_5(A, B) = A^5 + B^5$.
-/
theorem quintic_cyclotomic_factorization (A B : ℤ) :
    (A + B) * cyclotomicQuinticQuotient A B = A ^ 5 + B ^ 5 := by
  unfold cyclotomicQuinticQuotient
  ring

/--
Weierstrass coefficients of Darmon's Frey curve $W_{A, B}$ attached to $A^5 + B^5 = C^p$
(Billerey 2007, BCDF 2019):
  $$W_{A, B} : y^2 = x^3 + a_2 x^2 + a_4 x$$
where:
  $a_2 = -5(A^2 + B^2)$,
  $a_4 = 5 H_5(A, B) = 5 (A^4 - A^3 B + A^2 B^2 - A B^3 + B^4)$.
-/
structure BillereyCurveCoefficients (R : Type*) where
  a2 : R
  a4 : R

def billereyCurve (A B : ℤ) : BillereyCurveCoefficients ℤ :=
  { a2 := -5 * (A ^ 2 + B ^ 2),
    a4 := 5 * cyclotomicQuinticQuotient A B }

/--
The polynomial discriminant of the cubic $x(x^2 + a_2 x + a_4)$:
  $$\operatorname{disc}(P) = a_4^2 (a_2^2 - 4a_4).$$
-/
def billereyPolynomialDiscriminant (A B : ℤ) : ℤ :=
  let W := billereyCurve A B
  W.a4 ^ 2 * (W.a2 ^ 2 - 4 * W.a4)

/--
**Billerey–Darmon Discriminant Factorization Identity**:
The polynomial discriminant factors identically as:
  $$\operatorname{disc}(P) = 5^3 (A + B)^2 (A^5 + B^5)^2 = 125 (A + B)^2 (A^5 + B^5)^2.$$
-/
theorem billerey_discriminant_eq (A B : ℤ) :
    billereyPolynomialDiscriminant A B =
    125 * (A + B) ^ 2 * (A ^ 5 + B ^ 5) ^ 2 := by
  unfold billereyPolynomialDiscriminant billereyCurve cyclotomicQuinticQuotient
  ring

/--
On any solution to $A^5 + B^5 = C^p$, the Billerey polynomial discriminant factors as:
  $$\operatorname{disc}(P) = 125 (A + B)^2 C^{2p}.$$
-/
theorem billerey_discriminant_on_solution (A B C : ℤ) (p : ℕ)
    (heq : A ^ 5 + B ^ 5 = C ^ p) :
    billereyPolynomialDiscriminant A B =
    125 * (A + B) ^ 2 * (C ^ p) ^ 2 := by
  rw [billerey_discriminant_eq, heq]

/-! ### 6. Darmon Modular Architecture Classification -/

/--
Classification of the five canonical Darmon modular Frey curve families.
-/
inductive DarmonFreyArchitecture where
  | HellegouarchFrey : DarmonFreyArchitecture  -- (p, p, p)
  | FreyKraus        : DarmonFreyArchitecture  -- (2, 3, p)
  | EllenbergQCurve  : DarmonFreyArchitecture  -- (2, 4, p)
  | KrausFrey        : DarmonFreyArchitecture  -- (3, 3, p)
  | BillereyDarmon   : DarmonFreyArchitecture  -- (5, 5, p)
  deriving DecidableEq, Repr

/--
Assignment of a signature $(p, q, r)$ to its canonical Darmon Frey curve architecture.
-/
def darmonArchitecture (p q r : ℕ) : Option DarmonFreyArchitecture :=
  if p = 2 ∧ q = 3 then some DarmonFreyArchitecture.FreyKraus
  else if p = 2 ∧ q = 4 then some DarmonFreyArchitecture.EllenbergQCurve
  else if p = 3 ∧ q = 3 then some DarmonFreyArchitecture.KrausFrey
  else if p = 5 ∧ q = 5 then some DarmonFreyArchitecture.BillereyDarmon
  else if p = q ∧ q = r then some DarmonFreyArchitecture.HellegouarchFrey
  else none

theorem classify_arch_ppp (p : ℕ) :
    darmonArchitecture p p p =
      if p = 3 then some DarmonFreyArchitecture.KrausFrey
      else if p = 5 then some DarmonFreyArchitecture.BillereyDarmon
      else some DarmonFreyArchitecture.HellegouarchFrey := by
  unfold darmonArchitecture
  split_ifs <;> rfl

theorem classify_arch_2_3_p (p : ℕ) :
    darmonArchitecture 2 3 p = some DarmonFreyArchitecture.FreyKraus := by
  unfold darmonArchitecture
  rfl

theorem classify_arch_2_4_p (p : ℕ) :
    darmonArchitecture 2 4 p = some DarmonFreyArchitecture.EllenbergQCurve := by
  unfold darmonArchitecture
  rfl

theorem classify_arch_3_3_p (p : ℕ) :
    darmonArchitecture 3 3 p = some DarmonFreyArchitecture.KrausFrey := by
  unfold darmonArchitecture
  rfl

theorem classify_arch_5_5_p (p : ℕ) :
    darmonArchitecture 5 5 p = some DarmonFreyArchitecture.BillereyDarmon := by
  unfold darmonArchitecture
  rfl

end Beal
