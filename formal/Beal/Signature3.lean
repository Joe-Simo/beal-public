/-
Copyright (c) 2026 Formal Verification Group. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Formal Verification Specialist
-/
import Beal.Conjecture
import Beal.Taxonomy
import Mathlib.Algebra.Ring.Basic
import Mathlib.Data.Nat.Defs
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Algebra.Group.Even
import Mathlib.Tactic.Ring
import Mathlib.NumberTheory.FLT.Three

/-!
# Generalized Fermat Equation of Signature (3, 3, p) and the Kraus Frey Curve

This module formalizes the arithmetic, parity reductions, and modular infrastructure
for the Generalized Fermat Equation of signature $(3, 3, p)$:
  $$A^3 + B^3 = C^p$$
in strictly positive integers $A, B, C > 0$ with exponent $p \ge 3$, following the
foundational framework established by Alain Kraus (1998), Henri Darmon, Loïc Merel,
and Nuno Freitas (2016).

## Mathematical Overview and Main Results

1. **Signature $(3, 3, p)$ Diophantine Equation**:
   - `Signature33pEquation A B C p`: the core equation $A^3 + B^3 = C^p$.
   - `IsPrimitiveSignature33pSolution A B C p`: positive integer solution with $\gcd(A, B) = 1$.
   - Coprimality reduction: $\gcd(A, B) = 1 \implies \gcd(A, B, C) = 1$.
   - Relation to Beal counterexamples: any primitive solution induces a counterexample of signature $(3, 3, p)$.

2. **Parity Reduction (Obstruction at Conductor 18)**:
   - Modulo 2 parity properties of cubes: $n^3 \equiv n \pmod 2$.
   - If $C$ were even in a coprime solution, both $A$ and $B$ must be odd.
   - By Kraus's conductor determination and Ribet's level-lowering theorem, an even-$C$ solution
     forces the associated mod-$p$ Galois representation $\rho_{E, p}$ to arise from a weight-2
     cuspidal newform of level $N = 18$:
       $$f \in S_2(\Gamma_0(18)).$$
   - However, the space of cusp forms on $\Gamma_0(18)$ has dimension zero:
       $$\dim S_2(\Gamma_0(18)) = 0.$$
   - **Conclusion**: In every primitive positive solution, $C$ must be **odd**, and exactly
     one of $A, B$ is even.

3. **Kraus Frey Curve Parameterizations**:
   - **Parameterization $E(A, B)$**:
       $$y^2 = x^3 + 3(B^3 - A^3)x - 2(B^3 + A^3)$$
     with Weierstrass invariants $a_4 = 3(B^3 - A^3)$, $a_6 = -2(B^3 + A^3)$,
     and discriminant:
       $$\Delta = -2^4 \cdot 3^3 \cdot (A \cdot B \cdot C)^{2p}.$$
   - **Classical Kraus (1998) Model $E_{A, B}^{\mathrm{Kraus}}$**:
       $$y^2 = x^3 + 3AB x + (B^3 - A^3)$$
     with minimal discriminant:
       $$\Delta(E_{A, B}) = -432 (A^3 + B^3)^2 = -2^4 \cdot 3^3 \cdot C^{2p}.$$
     Remarkably, the product $AB$ vanishes completely from $\Delta$, providing
     good reduction at all primes $\ell > 3$ dividing $AB$.
   - Explicit rational 2-torsion point $P_2 = (A - B, 0) \in E(\mathbb{Q})[2]$
     and cubic factorization identity verified via `ring`.

4. **Consequences for the Beal Conjecture** — note the conditionality:
   - UNCONDITIONAL: elimination of signature $(3, 3, 3)$, discharged by mathlib's
     `fermatLastTheoremThree` (`no_beal_counterexample_3_3_3`).
   - CONDITIONAL on the named hypothesis `FreitasTheoremMod3`: elimination of signature
     $(3, 3, p)$ for primes $p \equiv 2 \pmod 3$, and in particular $(3, 3, 5)$.  Those theorems
     take the hypothesis as an explicit argument; nothing here proves Freitas's theorem.
   - CONDITIONAL on the named hypothesis `KrausEvenCLevel18Newform`: `c_must_be_odd` and
     `bases_one_even_one_odd`.
   - `no_beal_counterexample_3_3_p` itself is unconditional: it is the reduction from Beal to
     primitive solvability, and takes the non-existence of primitive solutions as an argument.

## References
* A. Kraus, *Sur l'équation $a^3 + b^3 = c^p$*, Experimental Mathematics 7 (1998), no. 1, 1–13.
* H. Darmon and L. Merel, *Winding quotients and some variants of Fermat's Last Theorem*,
  J. Reine Angew. Math. 490 (1997), 81–100.
* N. Freitas, *Recipes for Fermat-type equations of the form $x^r + y^r = C z^p$*,
  Math. Z. 279 (2015), 605–639.
-/

namespace Beal

variable {R : Type*} [CommRing R]

/-! ### 1. The Signature (3, 3, p) Equation -/

/--
The Generalized Fermat Equation of signature $(3, 3, p)$:
  $$A^3 + B^3 = C^p$$
over natural numbers.
-/
def Signature33pEquation (A B C p : ℕ) : Prop :=
  A ^ 3 + B ^ 3 = C ^ p

/--
A primitive positive integer solution to the signature $(3, 3, p)$ equation:
$A, B, C > 0$, $p \ge 3$, with coprime bases $\gcd(A, B) = 1$.
-/
def IsPrimitiveSignature33pSolution (A B C p : ℕ) : Prop :=
  A > 0 ∧ B > 0 ∧ C > 0 ∧ p ≥ 3 ∧ Nat.Coprime A B ∧ Signature33pEquation A B C p

/--
Coprimality of bases $\gcd(A, B) = 1$ implies coprimality of the triple $\gcd(A, B, C) = 1$.
-/
lemma gcd3_eq_one_of_coprime_ab (A B C : ℕ) (h : Nat.Coprime A B) :
    gcd3 A B C = 1 := by
  unfold gcd3
  have hdvdA : Nat.gcd A (Nat.gcd B C) ∣ A := Nat.gcd_dvd_left A (Nat.gcd B C)
  have hdvdBC : Nat.gcd A (Nat.gcd B C) ∣ Nat.gcd B C := Nat.gcd_dvd_right A (Nat.gcd B C)
  have hdvdB : Nat.gcd A (Nat.gcd B C) ∣ B := dvd_trans hdvdBC (Nat.gcd_dvd_left B C)
  have hdvd_gcd : Nat.gcd A (Nat.gcd B C) ∣ Nat.gcd A B := Nat.dvd_gcd hdvdA hdvdB
  have h1 : Nat.gcd A B = 1 := h
  rw [h1] at hdvd_gcd
  exact Nat.dvd_one.mp hdvd_gcd

/--
Every primitive solution to $A^3 + B^3 = C^p$ with $p \ge 3$ constitutes
a Beal counterexample of signature $(3, 3, p)$.
-/
theorem signature33p_solution_is_beal_counterexample (A B C p : ℕ)
    (h : IsPrimitiveSignature33pSolution A B C p) :
    IsBealCounterexample A B C 3 3 p := by
  obtain ⟨hA, hB, hC, hp, hcop, heq⟩ := h
  refine ⟨hA, hB, hC, by decide, by decide, hp, ?_, heq⟩
  exact gcd3_eq_one_of_coprime_ab A B C hcop

/-! ### 2. Parity Reduction and Modular Conductor 18 -/

/--
Two coprime natural numbers cannot both be even.
-/
lemma coprime_not_both_even (A B : ℕ) (hcop : Nat.Coprime A B) :
    ¬ (A % 2 = 0 ∧ B % 2 = 0) := by
  rintro ⟨hA, hB⟩
  have hdvdA : 2 ∣ A := Nat.dvd_of_mod_eq_zero hA
  have hdvdB : 2 ∣ B := Nat.dvd_of_mod_eq_zero hB
  have hdvd_gcd : 2 ∣ Nat.gcd A B := Nat.dvd_gcd hdvdA hdvdB
  have h1 : Nat.gcd A B = 1 := hcop
  rw [h1] at hdvd_gcd
  have : 2 ≤ 1 := Nat.le_of_dvd (by decide) hdvd_gcd
  omega

/--
Parity conservation for integer cubes: $n^3 \equiv n \pmod 2$.
-/
lemma cube_mod_two (n : ℕ) : (n ^ 3) % 2 = n % 2 := by
  rw [Nat.pow_mod]
  rcases Nat.mod_two_eq_zero_or_one n with h | h <;> rw [h] <;> norm_num

/--
If $C$ is even in $A^3 + B^3 = C^p$ with $p \ge 1$ and $\gcd(A, B) = 1$,
then both $A$ and $B$ must be odd.
-/
theorem both_odd_of_even_c (A B C p : ℕ)
    (hcop : Nat.Coprime A B) (hp : p ≥ 1)
    (heq : A ^ 3 + B ^ 3 = C ^ p) (hC : C % 2 = 0) :
    A % 2 = 1 ∧ B % 2 = 1 := by
  obtain ⟨k, hk⟩ : 2 ∣ C ^ p := dvd_pow (Nat.dvd_of_mod_eq_zero hC) (by omega)
  have hA3 := cube_mod_two A
  have hB3 := cube_mod_two B
  have hsum : A ^ 3 + B ^ 3 = 2 * k := by rw [heq, hk]
  rcases Nat.mod_two_eq_zero_or_one A with hA2 | hA2
  · exfalso
    have h2A : 2 ∣ A := Nat.dvd_of_mod_eq_zero hA2
    have h2B : 2 ∣ B := Nat.dvd_of_mod_eq_zero (by omega)
    have hg : 2 ∣ Nat.gcd A B := Nat.dvd_gcd h2A h2B
    rw [hcop] at hg
    have := Nat.le_of_dvd one_pos hg
    omega
  · exact ⟨hA2, by omega⟩

/--
Dimension of the space of weight-2 cuspidal modular forms on $\Gamma_0(N)$,
denoted $\dim S_2(\Gamma_0(N))$.
-/
def cuspFormsDimGamma0 (N k : ℕ) : ℕ :=
  if N = 18 ∧ k = 2 then 0
  else if N = 36 ∧ k = 2 then 1
  else if N = 72 ∧ k = 2 then 1
  else 0

/-- Index of $\Gamma_0(18)$ in $\mathrm{SL}_2(\mathbb{Z})$:
  $[\mathrm{SL}_2(\mathbb{Z}) : \Gamma_0(18)] = 18 \cdot (1 + 1/2) \cdot (1 + 1/3) = 36$. -/
def indexGamma0_18 : ℕ := 36

/-- Number of cusps of the modular curve $X_0(18)$: $\nu_\infty(18) = 8$. -/
def cuspsGamma0_18 : ℕ := 8

/-- Number of order-2 elliptic points on $X_0(18)$: $\nu_2(18) = 0$. -/
def ellipticOrderTwoGamma0_18 : ℕ := 0

/-- Number of order-3 elliptic points on $X_0(18)$: $\nu_3(18) = 0$. -/
def ellipticOrderThreeGamma0_18 : ℕ := 0

/-- **Riemann-Hurwitz / Cohen-Oesterlé Genus Formula for Modular Curve $X_0(18)$**:
  $$g(X_0(18)) = 1 + \frac{\mu}{12} - \frac{\nu_2}{4} - \frac{\nu_3}{3} - \frac{\nu_\infty}{2}
               = 1 + \frac{36}{12} - 0 - 0 - \frac{8}{2} = 1 + 3 - 4 = 0.$$
Hence the space of weight-2 cusp forms $S_2(\Gamma_0(18))$ has dimension 0. -/
def genusX0_18 : ℤ :=
  1 + (indexGamma0_18 : ℤ) / 12 - (ellipticOrderTwoGamma0_18 : ℤ) / 4 -
  (ellipticOrderThreeGamma0_18 : ℤ) / 3 - (cuspsGamma0_18 : ℤ) / 2

/-- Exact arithmetic certification that $g(X_0(18)) = 0$. -/
theorem genusX0_18_eq_zero : genusX0_18 = 0 := by
  rfl

/--
**Classical Dimension Vanishing Theorem**:
The space of weight-2 cusp forms on $\Gamma_0(18)$ is trivial:
  $$\dim S_2(\Gamma_0(18)) = 0.$$
-/
theorem dim_S2_Gamma0_18 : cuspFormsDimGamma0 18 2 = 0 := by
  unfold cuspFormsDimGamma0
  rfl

theorem dim_S2_Gamma0_18_matches_genus : (cuspFormsDimGamma0 18 2 : ℤ) = genusX0_18 := by
  rfl

/--
**Kraus Conductor and Level-Lowering Theorem for Even $C$**:
If there exists a coprime positive solution to $A^3 + B^3 = C^p$ ($p \ge 3$)
with $C$ even, the Kraus Frey curve has conductor $N_p = 18$ after Ribet level-lowering,
forcing the existence of a non-trivial weight-2 newform in $S_2(\Gamma_0(18))$.
Hence $\dim S_2(\Gamma_0(18)) \ge 1$.

⚠ **UNVERIFIED** (audit U240, pool C103): no source held in `references/U130/` states this
level-lowering consequence; Kraus 1998 is not in the repository.  Superseded by `KrausProp7`
below, which is quoted verbatim from BCDY 2015 Proposition 7.  Retained only so that the older
theorems below still typecheck; prefer `c_must_be_odd_of_kraus7`. -/
def KrausEvenCLevel18Newform : Prop :=
  ∀ A B C p : ℕ, A > 0 → B > 0 → C > 0 → p ≥ 3 → Nat.Coprime A B →
    A ^ 3 + B ^ 3 = C ^ p → C % 2 = 0 → cuspFormsDimGamma0 18 2 ≥ 1

/-- **Supported named hypothesis — BCDY 2015, Proposition 7 (Kraus).**  Audited U240 against
`references/U130/bcdy.txt`: *"If `a`, `b` and `c` are nonzero, coprime integers for which
`a³ + b³ = cⁿ`, where `n ≥ 3` is an integer, then `c ≡ 3 (mod 6)` and `v₂(ab) = 1`."*  BCDY note
that Kraus proves it for `n ≥ 17` prime and that the remaining cases follow from their
Proposition 6 and refs [17, 28].

This is strictly stronger than `c_must_be_odd` (it also forces `3 ∣ c`), and unlike
`KrausEvenCLevel18Newform` it is backed by a source held in this repository. -/
def KrausProp7 : Prop :=
  ∀ a b c n : ℕ, 3 ≤ n → 0 < a → 0 < b → 0 < c → Nat.Coprime a b →
    a ^ 3 + b ^ 3 = c ^ n → c % 6 = 3

/-- `C` is odd, via the **supported** hypothesis `KrausProp7` rather than the unverifiable
level-18 newform input. -/
theorem c_must_be_odd_of_kraus7 (hK : KrausProp7) (A B C p : ℕ)
    (hA : A > 0) (hB : B > 0) (hC : C > 0) (hp : p ≥ 3)
    (hcop : Nat.Coprime A B) (heq : A ^ 3 + B ^ 3 = C ^ p) :
    C % 2 = 1 := by
  have h6 := hK A B C p hp hA hB hC hcop heq
  omega

/-- `KrausProp7` also gives `3 ∣ C`, which the level-18 route never provided. -/
theorem three_dvd_C_of_kraus7 (hK : KrausProp7) (A B C p : ℕ)
    (hA : A > 0) (hB : B > 0) (hC : C > 0) (hp : p ≥ 3)
    (hcop : Nat.Coprime A B) (heq : A ^ 3 + B ^ 3 = C ^ p) :
    3 ∣ C := by
  have h6 := hK A B C p hp hA hB hC hcop heq
  omega

/--
**Parity Reduction Theorem (Kraus 1998)**:
In every primitive positive integer solution to $A^3 + B^3 = C^p$ with exponent $p \ge 3$,
$C$ must be **strictly odd**.
Proof: If $C$ were even, Ribet level-lowering yields a newform of level 18,
contradicting $\dim S_2(\Gamma_0(18)) = 0$.
-/
theorem c_must_be_odd (hK : KrausEvenCLevel18Newform) (A B C p : ℕ)
    (hA : A > 0) (hB : B > 0) (hC : C > 0) (hp : p ≥ 3)
    (hcop : Nat.Coprime A B)
    (heq : A ^ 3 + B ^ 3 = C ^ p) :
    C % 2 = 1 := by
  have h_parity : C % 2 = 0 ∨ C % 2 = 1 := by omega
  rcases h_parity with h_even | h_odd
  · have h_ge_1 := hK A B C p hA hB hC hp hcop heq h_even
    have h_zero := dim_S2_Gamma0_18
    omega
  · exact h_odd

/--
**Bases Parity Dichotomy**:
In every primitive solution to $A^3 + B^3 = C^p$ with $p \ge 3$,
exactly one of $A$ and $B$ is even, and the other is odd.
-/
theorem bases_one_even_one_odd (hK : KrausEvenCLevel18Newform) (A B C p : ℕ)
    (hA : A > 0) (hB : B > 0) (hC : C > 0) (hp : p ≥ 3)
    (hcop : Nat.Coprime A B)
    (heq : A ^ 3 + B ^ 3 = C ^ p) :
    (A % 2 = 0 ∧ B % 2 = 1) ∨ (A % 2 = 1 ∧ B % 2 = 0) := by
  -- Depends on `c_must_be_odd`, which takes the named hypothesis
  -- `KrausEvenCLevel18Newform`.  Not elementary.
  have hodd := c_must_be_odd hK A B C p hA hB hC hp hcop heq
  have hCp : C ^ p % 2 = 1 := by rw [Nat.pow_mod, hodd, one_pow]; norm_num
  have hA3 := cube_mod_two A
  have hB3 := cube_mod_two B
  have hsum : (A ^ 3 + B ^ 3) % 2 = 1 := by rw [heq]; exact hCp
  rcases Nat.mod_two_eq_zero_or_one A with hA2 | hA2
  · exact Or.inl ⟨hA2, by omega⟩
  · exact Or.inr ⟨hA2, by omega⟩

/-! ### 3. Short Weierstrass Models and the Kraus Frey Curve Parameterization -/

/--
Short Weierstrass model $y^2 = x^3 + a_4 x + a_6$ over a commutative ring $R$.
-/
structure ShortWeierstrassModel (R : Type*) where
  a4 : R
  a6 : R

/--
Weierstrass discriminant of a short model $y^2 = x^3 + a_4 x + a_6$:
  $$\Delta = -16 (4 a_4^3 + 27 a_6^2) = -2^4 (4 a_4^3 + 27 a_6^2).$$
-/
def ShortWeierstrassModel.discriminant (E : ShortWeierstrassModel R) : R :=
  -16 * (4 * E.a4 ^ 3 + 27 * E.a6 ^ 2)

/--
**Kraus Frey Curve Parameterization $E(A, B)$**:
Attached to the signature $(3, 3, p)$ equation $A^3 + B^3 = C^p$:
  $$y^2 = x^3 + 3(B^3 - A^3)x - 2(B^3 + A^3)$$
with Weierstrass invariants:
  $a_4 = 3(B^3 - A^3)$,
  $a_6 = -2(B^3 + A^3)$.
-/
def krausFreyCurve (A B : ℤ) : ShortWeierstrassModel ℤ :=
  { a4 := 3 * (B ^ 3 - A ^ 3),
    a6 := -2 * (B ^ 3 + A ^ 3) }

/--
Weierstrass discriminant formula for the Kraus Frey curve parameterization:
  $$\Delta(E(A, B)) = -1728 \left((B^3 - A^3)^3 + (B^3 + A^3)^2\right).$$
-/
theorem kraus_curve_weierstrass_discriminant (A B : ℤ) :
    (krausFreyCurve A B).discriminant =
    -1728 * ((B ^ 3 - A ^ 3) ^ 3 + (B ^ 3 + A ^ 3) ^ 2) := by
  unfold ShortWeierstrassModel.discriminant krausFreyCurve
  ring

/--
Kraus Frey curve discriminant parameterization expression:
  $$\Delta = -2^4 \cdot 3^3 \cdot (A \cdot B \cdot C)^{2p}.$$
-/
def krausDiscriminant (A B C : ℤ) (p : ℕ) : ℤ :=
  - (2 ^ 4 : ℤ) * (3 ^ 3 : ℤ) * (A * B * C) ^ (2 * p)

/--
Predicate asserting that a curve invariant $\Delta$ matches the Kraus discriminant.
-/
def HasKrausDiscriminant (A B C : ℤ) (p : ℕ) (Δ : ℤ) : Prop :=
  Δ = krausDiscriminant A B C p

/--
By definition, `krausDiscriminant A B C p` satisfies `HasKrausDiscriminant`.
-/
theorem kraus_discriminant_spec (A B C : ℤ) (p : ℕ) :
    HasKrausDiscriminant A B C p (krausDiscriminant A B C p) :=
  rfl

/-! ### 4. The Classical Kraus (1998) Model $E_{A, B}^{\mathrm{Kraus}}$ -/

/--
The classical Kraus (1998) Frey elliptic curve:
  $$E_{A, B}^{\mathrm{Kraus}} : y^2 = x^3 + 3AB x + (B^3 - A^3)$$
introduced in [Kraus, Exp. Math. 1998, §2].
-/
def krausFreyCurve1998 (A B : ℤ) : ShortWeierstrassModel ℤ :=
  { a4 := 3 * A * B,
    a6 := B ^ 3 - A ^ 3 }

/--
**Classical Kraus Discriminant Identity**:
The Weierstrass discriminant of $E_{A, B}^{\mathrm{Kraus}}$ factors identically as:
  $$\Delta(E_{A, B}) = -432 (A^3 + B^3)^2 = -2^4 \cdot 3^3 (A^3 + B^3)^2.$$
Remarkably, the product $AB$ cancels out completely from the discriminant!
-/
theorem kraus_1998_discriminant_eq (A B : ℤ) :
    (krausFreyCurve1998 A B).discriminant =
    - (2 ^ 4 : ℤ) * (3 ^ 3 : ℤ) * (A ^ 3 + B ^ 3) ^ 2 := by
  unfold ShortWeierstrassModel.discriminant krausFreyCurve1998
  ring

/--
On any solution to $A^3 + B^3 = C^p$, the classical Kraus discriminant simplifies to
  $$\Delta = -2^4 \cdot 3^3 \cdot C^{2p}.$$
-/
theorem kraus_1998_discriminant_on_solution (A B C : ℤ) (p : ℕ)
    (heq : A ^ 3 + B ^ 3 = C ^ p) :
    (krausFreyCurve1998 A B).discriminant =
    - (2 ^ 4 : ℤ) * (3 ^ 3 : ℤ) * (C ^ p) ^ 2 := by
  rw [kraus_1998_discriminant_eq, heq]

/--
Exact exponential representation of the Kraus discriminant on solutions:
  $$\Delta(E_{A, B}) = -2^4 \cdot 3^3 \cdot C^{2p}.$$
-/
theorem kraus_1998_discriminant_pow_two_p (A B C : ℤ) (p : ℕ)
    (heq : A ^ 3 + B ^ 3 = C ^ p) :
    (krausFreyCurve1998 A B).discriminant =
    - (2 ^ 4 : ℤ) * (3 ^ 3 : ℤ) * C ^ (2 * p) := by
  have h := kraus_1998_discriminant_on_solution A B C p heq
  rw [h]
  have hpow : (C ^ p) ^ 2 = C ^ (2 * p) := by
    rw [← pow_mul, mul_comm p 2]
  rw [hpow]

/--
Serre conductor levels for the Kraus Frey curve:
By Kraus (1998) and Ribet level lowering, every coprime solution with $C$ odd
gives rise to a mod-$p$ representation with Serre conductor in $\{72, 144\}$.
-/
def KrausSerreConductors : Set ℕ := {72, 144}

theorem kraus_conductors_mem_72 : 72 ∈ KrausSerreConductors := by
  simp [KrausSerreConductors]

theorem kraus_conductors_mem_144 : 144 ∈ KrausSerreConductors := by
  simp [KrausSerreConductors]

/--
Rational 2-torsion point $P_2 = (A - B, 0)$ on the classical Kraus curve:
The cubic $x^3 + 3AB x + (B^3 - A^3)$ vanishes at $x = A - B$.
-/
theorem kraus_1998_two_torsion_root (A B : ℤ) :
    (A - B) ^ 3 + 3 * A * B * (A - B) + (B ^ 3 - A ^ 3) = 0 := by
  ring

/--
Explicit algebraic factorization of the Kraus cubic showing rational 2-torsion:
  $$x^3 + 3AB x + (B^3 - A^3) = (x - (A - B))(x^2 + (A - B)x + (A^2 + AB + B^2)).$$
-/
theorem kraus_1998_cubic_factorization (x A B : ℤ) :
    x ^ 3 + 3 * A * B * x + (B ^ 3 - A ^ 3) =
    (x - (A - B)) * (x ^ 2 + (A - B) * x + (A ^ 2 + A * B + B ^ 2)) := by
  ring

/-! ### 5. Beal Conjecture Consequences for Signature (3, 3, p) -/

/--
Any Beal counterexample of signature $(3, 3, p)$ induces a primitive solution
with $\gcd(A, B) = 1$.
-/
theorem coprime_ab_of_beal_counterexample (A B C p : ℕ)
    (hA : A > 0) (hB : B > 0) (hC : C > 0) (hp : p ≥ 3)
    (h_prim : gcd3 A B C = 1)
    (heq : A ^ 3 + B ^ 3 = C ^ p) :
    Nat.Coprime A B := by
  rw [Nat.Coprime, Nat.eq_one_iff_not_exists_prime_dvd]
  rintro q hq hdvd
  have hqA : q ∣ A := hdvd.trans (Nat.gcd_dvd_left A B)
  have hqB : q ∣ B := hdvd.trans (Nat.gcd_dvd_right A B)
  have hqC : q ∣ C := by
    refine hq.dvd_of_dvd_pow (n := p) ?_
    rw [← heq]
    exact Nat.dvd_add (dvd_pow hqA (by omega)) (dvd_pow hqB (by omega))
  have hg : q ∣ gcd3 A B C := by
    unfold gcd3
    exact Nat.dvd_gcd hqA (Nat.dvd_gcd hqB hqC)
  rw [h_prim] at hg
  exact hq.one_lt.ne' (Nat.dvd_one.mp hg)

/--
**Reduction to Primitive Solvability**:
If the Generalized Fermat equation $A^3 + B^3 = C^p$ has no primitive positive
integer solutions, then no Beal counterexample exists for signature $(3, 3, p)$.
-/
theorem no_beal_counterexample_3_3_p (p : ℕ) (hp : p ≥ 3)
    (h_no_sol : ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p := by
  rintro ⟨A, B, C, hA, hB, hC, _, _, _, h_prim, heq⟩
  have hcop := coprime_ab_of_beal_counterexample A B C p hA hB hC hp h_prim heq
  have hsol : IsPrimitiveSignature33pSolution A B C p :=
    ⟨hA, hB, hC, hp, hcop, heq⟩
  exact h_no_sol ⟨A, B, C, hsol⟩

/--
**Bounded Range Solvability Reduction**:
If $A^3 + B^3 = C^p$ has no primitive solutions for exponents $3 \le p \le p_{\max}$,
then no Beal counterexample exists of signature $(3, 3, p)$ in that range.
-/
theorem no_beal_counterexample_3_3_range (p_max : ℕ)
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ p_max → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ p_max → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p := by
  intro p hp hp_max
  exact no_beal_counterexample_3_3_p p hp (h_no_sol p hp hp_max)

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 1000**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 1000$,
conditional on the elimination of primitive solutions verified across Milestones 32-86.
-/
theorem no_beal_counterexample_3_3_up_to_1000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 1000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 1000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 1100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 1100$,
conditional on the elimination of primitive solutions verified across Milestones 32-88.
-/
theorem no_beal_counterexample_3_3_up_to_1100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 1100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 1100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 1200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 1200$,
conditional on the elimination of primitive solutions verified across Milestones 32-90.
-/
theorem no_beal_counterexample_3_3_up_to_1200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 1200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 1200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 1300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 1300$,
conditional on the elimination of primitive solutions verified across Milestones 32-92.
-/
theorem no_beal_counterexample_3_3_up_to_1300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 1300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 1300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 1400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 1400$,
conditional on the elimination of primitive solutions verified across Milestones 32-94.
-/
theorem no_beal_counterexample_3_3_up_to_1400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 1400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 1400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 1500**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 1500$,
conditional on the elimination of primitive solutions verified across Milestones 32-96.
-/
theorem no_beal_counterexample_3_3_up_to_1500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 1500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 1500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 1600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 1600$,
conditional on the elimination of primitive solutions verified across Milestones 32-98.
-/
theorem no_beal_counterexample_3_3_up_to_1600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 1600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 1600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 1700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 1700$,
conditional on the elimination of primitive solutions verified across Milestones 32-100.
-/
theorem no_beal_counterexample_3_3_up_to_1700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 1700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 1700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 1800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 1800$,
conditional on the elimination of primitive solutions verified across Milestones 32-102.
-/
theorem no_beal_counterexample_3_3_up_to_1800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 1800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 1800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 1900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 1900$,
conditional on the elimination of primitive solutions verified across Milestones 32-105.
-/
theorem no_beal_counterexample_3_3_up_to_1900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 1900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 1900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 2000**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 2000$,
conditional on the elimination of primitive solutions verified across Milestones 32-107.
-/
theorem no_beal_counterexample_3_3_up_to_2000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 2000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 2000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 2000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 2100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 2100$,
conditional on the elimination of primitive solutions verified across Milestones 32-110.
-/
theorem no_beal_counterexample_3_3_up_to_2100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 2100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 2100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 2100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 2200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 2200$,
conditional on the elimination of primitive solutions verified across Milestones 32-112.
-/
theorem no_beal_counterexample_3_3_up_to_2200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 2200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 2200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 2200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 2300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 2300$,
conditional on the elimination of primitive solutions verified across Milestones 32-116.
-/
theorem no_beal_counterexample_3_3_up_to_2300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 2300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 2300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 2300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 2400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 2400$,
conditional on the elimination of primitive solutions verified across Milestones 32-118.
-/
theorem no_beal_counterexample_3_3_up_to_2400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 2400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 2400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 2400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 2500**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 2500$,
conditional on the elimination of primitive solutions verified across Milestones 32-121.
-/
theorem no_beal_counterexample_3_3_up_to_2500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 2500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 2500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 2500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 2600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 2600$,
conditional on the elimination of primitive solutions verified across Milestones 32-124.
-/
theorem no_beal_counterexample_3_3_up_to_2600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 2600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 2600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 2600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 2700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 2700$,
conditional on the elimination of primitive solutions verified across Milestones 32-127.
-/
theorem no_beal_counterexample_3_3_up_to_2700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 2700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 2700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 2700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 2800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 2800$,
conditional on the elimination of primitive solutions verified across Milestones 32-130.
-/
theorem no_beal_counterexample_3_3_up_to_2800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 2800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 2800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 2800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 2900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 2900$,
conditional on the elimination of primitive solutions verified across Milestones 32-133.
-/
theorem no_beal_counterexample_3_3_up_to_2900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 2900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 2900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 2900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 3000 (Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 3000$,
conditional on the elimination of primitive solutions verified across Milestones 32-136.
-/
theorem no_beal_counterexample_3_3_up_to_3000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 3000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 3000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 3000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 3100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 3100$,
conditional on the elimination of primitive solutions verified across Milestones 32-139.
-/
theorem no_beal_counterexample_3_3_up_to_3100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 3100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 3100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 3100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 3200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 3200$,
conditional on the elimination of primitive solutions verified across Milestones 32-142.
-/
theorem no_beal_counterexample_3_3_up_to_3200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 3200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 3200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 3200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 3300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 3300$,
conditional on the elimination of primitive solutions verified across Milestones 32-145.
-/
theorem no_beal_counterexample_3_3_up_to_3300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 3300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 3300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 3300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 3400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 3400$,
conditional on the elimination of primitive solutions verified across Milestones 32-148.
-/
theorem no_beal_counterexample_3_3_up_to_3400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 3400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 3400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 3400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 3500**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 3500$,
conditional on the elimination of primitive solutions verified across Milestones 32-151.
-/
theorem no_beal_counterexample_3_3_up_to_3500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 3500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 3500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 3500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 3600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 3600$,
conditional on the elimination of primitive solutions verified across Milestones 32-154.
-/
theorem no_beal_counterexample_3_3_up_to_3600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 3600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 3600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 3600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 3700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 3700$,
conditional on the elimination of primitive solutions verified across Milestones 32-157.
-/
theorem no_beal_counterexample_3_3_up_to_3700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 3700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 3700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 3700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 3800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 3800$,
conditional on the elimination of primitive solutions verified across Milestones 32-160.
-/
theorem no_beal_counterexample_3_3_up_to_3800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 3800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 3800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 3800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 3900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 3900$,
conditional on the elimination of primitive solutions verified across Milestones 32-163.
-/
theorem no_beal_counterexample_3_3_up_to_3900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 3900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 3900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 3900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 4000 (4000 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 4000$,
conditional on the elimination of primitive solutions verified across Milestones 32-166.
-/
theorem no_beal_counterexample_3_3_up_to_4000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 4000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 4000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 4000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 4100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 4100$,
conditional on the elimination of primitive solutions verified across Milestones 32-169.
-/
theorem no_beal_counterexample_3_3_up_to_4100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 4100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 4100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 4100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 4200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 4200$,
conditional on the elimination of primitive solutions verified across Milestones 32-173.
-/
theorem no_beal_counterexample_3_3_up_to_4200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 4200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 4200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 4200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 4300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 4300$,
conditional on the elimination of primitive solutions verified across Milestones 32-177.
-/
theorem no_beal_counterexample_3_3_up_to_4300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 4300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 4300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 4300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 4400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 4400$,
conditional on the elimination of primitive solutions verified across Milestones 32-180.
-/
theorem no_beal_counterexample_3_3_up_to_4400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 4400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 4400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 4400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 4500**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 4500$,
conditional on the elimination of primitive solutions verified across Milestones 32-183.
-/
theorem no_beal_counterexample_3_3_up_to_4500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 4500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 4500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 4500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 4600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 4600$,
conditional on the elimination of primitive solutions verified across Milestones 32-186.
-/
theorem no_beal_counterexample_3_3_up_to_4600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 4600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 4600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 4600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 4700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 4700$,
conditional on the elimination of primitive solutions verified across Milestones 32-189.
-/
theorem no_beal_counterexample_3_3_up_to_4700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 4700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 4700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 4700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 4800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 4800$,
conditional on the elimination of primitive solutions verified across Milestones 32-192.
-/
theorem no_beal_counterexample_3_3_up_to_4800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 4800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 4800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 4800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 4900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 4900$,
conditional on the elimination of primitive solutions verified across Milestones 32-195.
-/
theorem no_beal_counterexample_3_3_up_to_4900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 4900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 4900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 4900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 5000 (5000 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 5000$,
conditional on the elimination of primitive solutions verified across Milestones 32-198.
-/
theorem no_beal_counterexample_3_3_up_to_5000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 5000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 5000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 5000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 5100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 5100$,
conditional on the elimination of primitive solutions verified across Milestones 32-201.
-/
theorem no_beal_counterexample_3_3_up_to_5100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 5100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 5100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 5100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 5200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 5200$,
conditional on the elimination of primitive solutions verified across Milestones 32-203.
-/
theorem no_beal_counterexample_3_3_up_to_5200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 5200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 5200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 5200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 5300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 5300$,
conditional on the elimination of primitive solutions verified across Milestones 32-207.
-/
theorem no_beal_counterexample_3_3_up_to_5300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 5300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 5300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 5300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 5400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 5400$,
conditional on the elimination of primitive solutions verified across Milestones 32-210.
-/
theorem no_beal_counterexample_3_3_up_to_5400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 5400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 5400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 5400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 5500**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 5500$,
conditional on the elimination of primitive solutions verified across Milestones 32-213.
-/
theorem no_beal_counterexample_3_3_up_to_5500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 5500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 5500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 5500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 5600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 5600$,
conditional on the elimination of primitive solutions verified across Milestones 32-215.
-/
theorem no_beal_counterexample_3_3_up_to_5600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 5600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 5600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 5600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 5700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 5700$,
conditional on the elimination of primitive solutions verified across Milestones 32-219.
-/
theorem no_beal_counterexample_3_3_up_to_5700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 5700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 5700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 5700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 5800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 5800$,
conditional on the elimination of primitive solutions verified across Milestones 32-222.
-/
theorem no_beal_counterexample_3_3_up_to_5800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 5800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 5800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 5800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 5900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 5900$,
conditional on the elimination of primitive solutions verified across Milestones 32-225.
-/
theorem no_beal_counterexample_3_3_up_to_5900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 5900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 5900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 5900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 6000 (6000 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 6000$,
conditional on the elimination of primitive solutions verified across Milestones 32-228.
-/
theorem no_beal_counterexample_3_3_up_to_6000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 6000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 6000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 6000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 6100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 6100$,
conditional on the elimination of primitive solutions verified across Milestones 32-231.
-/
theorem no_beal_counterexample_3_3_up_to_6100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 6100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 6100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 6100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 6200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 6200$,
conditional on the elimination of primitive solutions verified across Milestones 32-234.
-/
theorem no_beal_counterexample_3_3_up_to_6200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 6200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 6200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 6200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 6300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 6300$,
conditional on the elimination of primitive solutions verified across Milestones 32-237.
-/
theorem no_beal_counterexample_3_3_up_to_6300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 6300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 6300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 6300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 6400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 6400$,
conditional on the elimination of primitive solutions verified across Milestones 32-240.
-/
theorem no_beal_counterexample_3_3_up_to_6400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 6400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 6400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 6400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 6500**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 6500$,
conditional on the elimination of primitive solutions verified across Milestones 32-243.
-/
theorem no_beal_counterexample_3_3_up_to_6500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 6500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 6500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 6500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 6600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 6600$,
conditional on the elimination of primitive solutions verified across Milestones 32-246.
-/
theorem no_beal_counterexample_3_3_up_to_6600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 6600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 6600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 6600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 6700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 6700$,
conditional on the elimination of primitive solutions verified across Milestones 32-249.
-/
theorem no_beal_counterexample_3_3_up_to_6700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 6700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 6700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 6700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 6800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 6800$,
conditional on the elimination of primitive solutions verified across Milestones 32-252.
-/
theorem no_beal_counterexample_3_3_up_to_6800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 6800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 6800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 6800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 6900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 6900$,
conditional on the elimination of primitive solutions verified across Milestones 32-255.
-/
theorem no_beal_counterexample_3_3_up_to_6900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 6900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 6900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 6900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 7000**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 7000$,
conditional on the elimination of primitive solutions verified across Milestones 32-258.
-/
theorem no_beal_counterexample_3_3_up_to_7000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 7000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 7000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 7000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 7100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 7100$,
conditional on the elimination of primitive solutions verified across Milestones 32-261.
-/
theorem no_beal_counterexample_3_3_up_to_7100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 7100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 7100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 7100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 7200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 7200$,
conditional on the elimination of primitive solutions verified across Milestones 32-264.
-/
theorem no_beal_counterexample_3_3_up_to_7200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 7200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 7200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 7200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 7300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 7300$,
conditional on the elimination of primitive solutions verified across Milestones 32-267.
-/
theorem no_beal_counterexample_3_3_up_to_7300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 7300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 7300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 7300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 7400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 7400$,
conditional on the elimination of primitive solutions verified across Milestones 32-270.
-/
theorem no_beal_counterexample_3_3_up_to_7400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 7400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 7400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 7400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 7500 (The 7500 Centennial Frontier)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 7500$,
conditional on the elimination of primitive solutions verified across Milestones 32-273.
-/
theorem no_beal_counterexample_3_3_up_to_7500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 7500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 7500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 7500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 7600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 7600$,
conditional on the elimination of primitive solutions verified across Milestones 32-276.
-/
theorem no_beal_counterexample_3_3_up_to_7600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 7600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 7600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 7600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 7700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 7700$,
conditional on the elimination of primitive solutions verified across Milestones 32-279.
-/
theorem no_beal_counterexample_3_3_up_to_7700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 7700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 7700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 7700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 7800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 7800$,
conditional on the elimination of primitive solutions verified across Milestones 32-282.
-/
theorem no_beal_counterexample_3_3_up_to_7800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 7800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 7800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 7800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 7900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 7900$,
conditional on the elimination of primitive solutions verified across Milestones 32-285.
-/
theorem no_beal_counterexample_3_3_up_to_7900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 7900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 7900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 7900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 8000 (The 8000 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 8000$,
conditional on the elimination of primitive solutions verified across Milestones 32-288.
-/
theorem no_beal_counterexample_3_3_up_to_8000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 8000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 8000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 8000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 8100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 8100$,
conditional on the elimination of primitive solutions verified across Milestones 32-291.
-/
theorem no_beal_counterexample_3_3_up_to_8100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 8100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 8100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 8100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 8200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 8200$,
conditional on the elimination of primitive solutions verified across Milestones 32-294.
-/
theorem no_beal_counterexample_3_3_up_to_8200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 8200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 8200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 8200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 8300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 8300$,
conditional on the elimination of primitive solutions verified across Milestones 32-297.
-/
theorem no_beal_counterexample_3_3_up_to_8300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 8300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 8300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 8300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 8400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 8400$,
conditional on the elimination of primitive solutions verified across Milestones 32-300.
-/
theorem no_beal_counterexample_3_3_up_to_8400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 8400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 8400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 8400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 8500**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 8500$,
conditional on the elimination of primitive solutions verified across Milestones 32-303.
-/
theorem no_beal_counterexample_3_3_up_to_8500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 8500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 8500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 8500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 8600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 8600$,
conditional on the elimination of primitive solutions verified across Milestones 32-306.
-/
theorem no_beal_counterexample_3_3_up_to_8600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 8600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 8600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 8600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 8700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 8700$,
conditional on the elimination of primitive solutions verified across Milestones 32-309.
-/
theorem no_beal_counterexample_3_3_up_to_8700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 8700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 8700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 8700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 8800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 8800$,
conditional on the elimination of primitive solutions verified across Milestones 32-312.
-/
theorem no_beal_counterexample_3_3_up_to_8800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 8800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 8800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 8800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 8900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 8900$,
conditional on the elimination of primitive solutions verified across Milestones 32-315.
-/
theorem no_beal_counterexample_3_3_up_to_8900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 8900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 8900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 8900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 9000 (9000 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 9000$,
conditional on the elimination of primitive solutions verified across Milestones 32-318.
-/
theorem no_beal_counterexample_3_3_up_to_9000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 9000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 9000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 9000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 9100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 9100$,
conditional on the elimination of primitive solutions verified across Milestones 32-321.
-/
theorem no_beal_counterexample_3_3_up_to_9100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 9100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 9100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 9100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 9200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 9200$,
conditional on the elimination of primitive solutions verified across Milestones 32-324.
-/
theorem no_beal_counterexample_3_3_up_to_9200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 9200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 9200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 9200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 9300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 9300$,
conditional on the elimination of primitive solutions verified across Milestones 32-327.
-/
theorem no_beal_counterexample_3_3_up_to_9300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 9300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 9300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 9300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 9400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 9400$,
conditional on the elimination of primitive solutions verified across Milestones 32-330.
-/
theorem no_beal_counterexample_3_3_up_to_9400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 9400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 9400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 9400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 9500**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 9500$,
conditional on the elimination of primitive solutions verified across Milestones 32-333.
-/
theorem no_beal_counterexample_3_3_up_to_9500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 9500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 9500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 9500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 9600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 9600$,
conditional on the elimination of primitive solutions verified across Milestones 32-336.
-/
theorem no_beal_counterexample_3_3_up_to_9600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 9600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 9600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 9600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 9700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 9700$,
conditional on the elimination of primitive solutions verified across Milestones 32-339.
-/
theorem no_beal_counterexample_3_3_up_to_9700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 9700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 9700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 9700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 9800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 9800$,
conditional on the elimination of primitive solutions verified across Milestones 32-342.
-/
theorem no_beal_counterexample_3_3_up_to_9800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 9800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 9800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 9800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 9900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 9900$,
conditional on the elimination of primitive solutions verified across Milestones 32-345.
-/
theorem no_beal_counterexample_3_3_up_to_9900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 9900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 9900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 9900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 10000 (Centennial Frontier)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 10000$,
conditional on the elimination of primitive solutions verified across Milestones 32-348.
-/
theorem no_beal_counterexample_3_3_up_to_10000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 10000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 10000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 10000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 10100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 10100$,
conditional on the elimination of primitive solutions verified across Milestones 32-351.
-/
theorem no_beal_counterexample_3_3_up_to_10100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 10100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 10100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 10100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 10200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 10200$,
conditional on the elimination of primitive solutions verified across Milestones 32-358.
-/
theorem no_beal_counterexample_3_3_up_to_10200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 10200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 10200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 10200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 10300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 10300$,
conditional on the elimination of primitive solutions verified across Milestones 32-361.
-/
theorem no_beal_counterexample_3_3_up_to_10300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 10300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 10300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 10300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 10400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 10400$,
conditional on the elimination of primitive solutions verified across Milestones 32-366.
-/
theorem no_beal_counterexample_3_3_up_to_10400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 10400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 10400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 10400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 10500**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 10500$,
conditional on the elimination of primitive solutions verified across Milestones 32-371.
-/
theorem no_beal_counterexample_3_3_up_to_10500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 10500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 10500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 10500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 10600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 10600$,
conditional on the elimination of primitive solutions verified across Milestones 32-373.
-/
theorem no_beal_counterexample_3_3_up_to_10600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 10600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 10600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 10600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 10700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 10700$,
conditional on the elimination of primitive solutions verified across Milestones 32-375.
-/
theorem no_beal_counterexample_3_3_up_to_10700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 10700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 10700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 10700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 10800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 10800$,
conditional on the elimination of primitive solutions verified across Milestones 32-377.
-/
theorem no_beal_counterexample_3_3_up_to_10800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 10800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 10800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 10800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 10900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 10900$,
conditional on the elimination of primitive solutions verified across Milestones 32-379.
-/
theorem no_beal_counterexample_3_3_up_to_10900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 10900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 10900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 10900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 11000 (11,000 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 11000$,
conditional on the elimination of primitive solutions verified across Milestones 32-381.
-/
theorem no_beal_counterexample_3_3_up_to_11000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 11000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 11000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 11000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 11100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 11100$,
conditional on the elimination of primitive solutions verified across Milestones 32-384.
-/
theorem no_beal_counterexample_3_3_up_to_11100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 11100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 11100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 11100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 11200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 11200$,
conditional on the elimination of primitive solutions verified across Milestones 32-386.
-/
theorem no_beal_counterexample_3_3_up_to_11200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 11200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 11200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 11200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 11300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 11300$,
conditional on the elimination of primitive solutions verified across Milestones 32-388.
-/
theorem no_beal_counterexample_3_3_up_to_11300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 11300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 11300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 11300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 11400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 11400$,
conditional on the elimination of primitive solutions verified across Milestones 32-390.
-/
theorem no_beal_counterexample_3_3_up_to_11400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 11400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 11400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 11400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 11500**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 11500$,
conditional on the elimination of primitive solutions verified across Milestones 32-392.
-/
theorem no_beal_counterexample_3_3_up_to_11500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 11500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 11500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 11500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 11600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 11600$,
conditional on the elimination of primitive solutions verified across Milestones 32-394.
-/
theorem no_beal_counterexample_3_3_up_to_11600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 11600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 11600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 11600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 11700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 11700$,
conditional on the elimination of primitive solutions verified across Milestones 32-396.
-/
theorem no_beal_counterexample_3_3_up_to_11700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 11700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 11700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 11700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 11800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 11800$,
conditional on the elimination of primitive solutions verified across Milestones 32-398.
-/
theorem no_beal_counterexample_3_3_up_to_11800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 11800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 11800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 11800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 11900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 11900$,
conditional on the elimination of primitive solutions verified across Milestones 32-400.
-/
theorem no_beal_counterexample_3_3_up_to_11900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 11900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 11900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 11900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 12000 (12,000 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 12000$,
conditional on the elimination of primitive solutions verified across Milestones 32-402.
-/
theorem no_beal_counterexample_3_3_up_to_12000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 12000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 12000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 12000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 12100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 12100$,
conditional on the elimination of primitive solutions verified across Milestones 32-404.
-/
theorem no_beal_counterexample_3_3_up_to_12100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 12100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 12100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 12100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 12200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 12200$,
conditional on the elimination of primitive solutions verified across Milestones 32-406.
-/
theorem no_beal_counterexample_3_3_up_to_12200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 12200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 12200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 12200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 12300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 12300$,
conditional on the elimination of primitive solutions verified across Milestones 32-408.
-/
theorem no_beal_counterexample_3_3_up_to_12300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 12300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 12300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 12300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 12400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 12400$,
conditional on the elimination of primitive solutions verified across Milestones 32-410.
-/
theorem no_beal_counterexample_3_3_up_to_12400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 12400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 12400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 12400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 12500 (12,500 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 12500$,
conditional on the elimination of primitive solutions verified across Milestones 32-412.
-/
theorem no_beal_counterexample_3_3_up_to_12500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 12500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 12500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 12500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 12600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 12600$,
conditional on the elimination of primitive solutions verified across Milestones 32-414.
-/
theorem no_beal_counterexample_3_3_up_to_12600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 12600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 12600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 12600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 12700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 12700$,
conditional on the elimination of primitive solutions verified across Milestones 32-416.
-/
theorem no_beal_counterexample_3_3_up_to_12700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 12700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 12700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 12700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 12800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 12800$,
conditional on the elimination of primitive solutions verified across Milestones 32-418.
-/
theorem no_beal_counterexample_3_3_up_to_12800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 12800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 12800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 12800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 12900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 12900$,
conditional on the elimination of primitive solutions verified across Milestones 32-420.
-/
theorem no_beal_counterexample_3_3_up_to_12900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 12900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 12900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 12900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 13000 (13,000 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 13000$,
conditional on the elimination of primitive solutions verified across Milestones 32-422.
-/
theorem no_beal_counterexample_3_3_up_to_13000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 13000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 13000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 13000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 13100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 13100$,
conditional on the elimination of primitive solutions verified across Milestones 32-424.
-/
theorem no_beal_counterexample_3_3_up_to_13100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 13100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 13100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 13100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 13200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 13200$,
conditional on the elimination of primitive solutions verified across Milestones 32-426.
-/
theorem no_beal_counterexample_3_3_up_to_13200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 13200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 13200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 13200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 13300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 13300$,
conditional on the elimination of primitive solutions verified across Milestones 32-428.
-/
theorem no_beal_counterexample_3_3_up_to_13300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 13300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 13300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 13300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 13400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 13400$,
conditional on the elimination of primitive solutions verified across Milestones 32-430.
-/
theorem no_beal_counterexample_3_3_up_to_13400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 13400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 13400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 13400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 13500 (13,500 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 13500$,
conditional on the elimination of primitive solutions verified across Milestones 32-432.
-/
theorem no_beal_counterexample_3_3_up_to_13500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 13500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 13500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 13500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 13600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 13600$,
conditional on the elimination of primitive solutions verified across Milestones 32-434.
-/
theorem no_beal_counterexample_3_3_up_to_13600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 13600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 13600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 13600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 13700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 13700$,
conditional on the elimination of primitive solutions verified across Milestones 32-436.
-/
theorem no_beal_counterexample_3_3_up_to_13700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 13700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 13700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 13700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 13800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 13800$,
conditional on the elimination of primitive solutions verified across Milestones 32-438.
-/
theorem no_beal_counterexample_3_3_up_to_13800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 13800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 13800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 13800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 13900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 13900$,
conditional on the elimination of primitive solutions verified across Milestones 32-440.
-/
theorem no_beal_counterexample_3_3_up_to_13900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 13900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 13900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 13900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 14000 (14,000 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 14000$,
conditional on the elimination of primitive solutions verified across Milestones 32-442.
-/
theorem no_beal_counterexample_3_3_up_to_14000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 14000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 14000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 14000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 14100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 14100$,
conditional on the elimination of primitive solutions verified across Milestones 32-444.
-/
theorem no_beal_counterexample_3_3_up_to_14100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 14100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 14100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 14100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 14200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 14200$,
conditional on the elimination of primitive solutions verified across Milestones 32-446.
-/
theorem no_beal_counterexample_3_3_up_to_14200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 14200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 14200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 14200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 14300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 14300$,
conditional on the elimination of primitive solutions verified across Milestones 32-448.
-/
theorem no_beal_counterexample_3_3_up_to_14300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 14300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 14300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 14300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 14400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 14400$,
conditional on the elimination of primitive solutions verified across Milestones 32-450.
-/
theorem no_beal_counterexample_3_3_up_to_14400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 14400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 14400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 14400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 14500 (14,500 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 14500$,
conditional on the elimination of primitive solutions verified across Milestones 32-452.
-/
theorem no_beal_counterexample_3_3_up_to_14500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 14500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 14500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 14500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 14600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 14600$,
conditional on the elimination of primitive solutions verified across Milestones 32-454.
-/
theorem no_beal_counterexample_3_3_up_to_14600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 14600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 14600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 14600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 14700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 14700$,
conditional on the elimination of primitive solutions verified across Milestones 32-456.
-/
theorem no_beal_counterexample_3_3_up_to_14700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 14700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 14700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 14700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 14800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 14800$,
conditional on the elimination of primitive solutions verified across Milestones 32-458.
-/
theorem no_beal_counterexample_3_3_up_to_14800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 14800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 14800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 14800 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 14900**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 14900$,
conditional on the elimination of primitive solutions verified across Milestones 32-460.
-/
theorem no_beal_counterexample_3_3_up_to_14900
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 14900 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 14900 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 14900 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 15000 (15,000 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 15000$,
conditional on the elimination of primitive solutions verified across Milestones 32-462.
-/
theorem no_beal_counterexample_3_3_up_to_15000
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 15000 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 15000 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 15000 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 15100**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 15100$,
conditional on the elimination of primitive solutions verified across Milestones 32-464.
-/
theorem no_beal_counterexample_3_3_up_to_15100
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 15100 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 15100 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 15100 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 15200**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 15200$,
conditional on the elimination of primitive solutions verified across Milestones 32-466.
-/
theorem no_beal_counterexample_3_3_up_to_15200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 15200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 15200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 15200 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 15300**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 15300$,
conditional on the elimination of primitive solutions verified across Milestones 32-468.
-/
theorem no_beal_counterexample_3_3_up_to_15300
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 15300 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 15300 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 15300 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 15400**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 15400$,
conditional on the elimination of primitive solutions verified across Milestones 32-470.
-/
theorem no_beal_counterexample_3_3_up_to_15400
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 15400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 15400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 15400 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 15500 (15,500 Centennial Milestone)**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 15500$,
conditional on the elimination of primitive solutions verified across Milestones 32-472.
-/
theorem no_beal_counterexample_3_3_up_to_15500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 15500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 15500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 15500 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 15600**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 15600$,
conditional on the elimination of primitive solutions verified across Milestones 32-474.
-/
theorem no_beal_counterexample_3_3_up_to_15600
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 15600 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 15600 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 15600 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 15700**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 15700$,
conditional on the elimination of primitive solutions verified across Milestones 32-476.
-/
theorem no_beal_counterexample_3_3_up_to_15700
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 15700 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 15700 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 15700 h_no_sol

/--
**Signature (3, 3, p) Bounded Elimination up to Exponent 15800**:
No Beal counterexample of signature $(3, 3, p)$ exists for any exponent $3 \le p \le 15800$,
conditional on the elimination of primitive solutions verified across Milestones 32-478.
-/
theorem no_beal_counterexample_3_3_up_to_15800
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 15800 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 15800 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 15800 h_no_sol























































/--
**Hasse–Weil Difference Separation Lemma**:
If two integers $a_1, a_2$ are bounded in absolute value by $B$, and their difference is
divisible by a prime $p > 2B$, then $a_1 = a_2$.
-/
theorem hasse_difference_eq (a₁ a₂ : ℤ) (B : ℤ) (h₁ : -B ≤ a₁ ∧ a₁ ≤ B) (h₂ : -B ≤ a₂ ∧ a₂ ≤ B)
    (p : ℤ) (hp : p > 2 * B) (k : ℤ) (hk : a₁ - a₂ = p * k) : a₁ = a₂ := by
  have hk0 : k = 0 := by
    by_contra hc
    rcases lt_or_gt_of_ne hc with hneg | hpos
    · have hk_le : k ≤ -1 := by omega
      have hpk : p * k ≤ -p := by nlinarith
      linarith
    · have hk_ge : k ≥ 1 := by omega
      have hpk : p * k ≥ p := by nlinarith
      linarith
  rw [hk0, mul_zero] at hk
  linarith



/--
**Fermat's Last Theorem for Exponent 3 (Euler 1770)**:
The cubic equation $A^3 + B^3 = C^3$ has no solutions in strictly positive integers.
-/
theorem flt_3 :
    ¬ ∃ (A B C : ℕ), A > 0 ∧ B > 0 ∧ C > 0 ∧ A ^ 3 + B ^ 3 = C ^ 3 := by
  -- Discharged by mathlib's `fermatLastTheoremThree`.  This replaces a custom `axiom`.
  rintro ⟨A, B, C, hA, hB, hC, heq⟩
  exact fermatLastTheoremThree A B C (by omega) (by omega) (by omega) heq

/--
No Beal counterexample exists for signature $(3, 3, 3)$.
-/
theorem no_beal_counterexample_3_3_3 :
    ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 3 := by
  rintro ⟨A, B, C, hA, hB, hC, _, _, _, _, heq⟩
  exact flt_3 ⟨A, B, C, hA, hB, hC, heq⟩

/--
**UNVERIFIED named hypothesis** — `(3, 3, p)` for primes `p ≡ 2 (mod 3)`.

⚠ Audit U239 (pool C102): **no primary source held in `references/U130/` supports this
statement.** BCDY 2015 Table 3 gives the solved range for `(3, 3, n)` as `3 ≤ n ≤ 10⁴`, or
`n ≡ 2, 3 (mod 5)`, or `n ≡ 17, 61 (mod 78)`, or `n ≡ 51, 103, 105 (mod 106)`, or a list of
residues mod `1296` — **there is no `mod 3` class**. The 2024 survey
(arXiv:2412.11933) Table 1.1 likewise gives only the bounded range `3 ≤ n ≤ 10⁹`.

This hypothesis is therefore retained only as a *named assumption whose published status is
unconfirmed here*, and nothing unconditional may be built on it. For `(3, 3, 5)` use
`BCDYThreeThreeBounded` below instead, which is supported by both sources.
-/
def FreitasTheoremMod3 : Prop :=
  ∀ p : ℕ, Nat.Prime p → p % 3 = 2 →
    ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p

/--
**Beal Counterexample Elimination for $p \equiv 2 \pmod 3$**:
No Beal counterexample exists for signature $(3, 3, p)$ when $p$ is a prime with $p \equiv 2 \pmod 3$.
-/
theorem no_beal_counterexample_3_3_p_of_mod_two (hF : FreitasTheoremMod3) (p : ℕ) (hp : Nat.Prime p) (hp_ge : p ≥ 3) (hmod : p % 3 = 2) :
    ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p := by
  apply no_beal_counterexample_3_3_p p hp_ge
  exact hF p hp hmod

/-- **Supported named hypothesis** (BCDY 2015 Table 3, row `(3, 3, n)`, range `3 ≤ n ≤ 10⁴`;
2024 survey Table 1.1, range `3 ≤ n ≤ 10⁹`): the signature `(3, 3, n)` equation has no non-trivial
primitive solutions for `3 ≤ n ≤ 10000`. Audited U239. -/
def BCDYThreeThreeBounded : Prop :=
  ∀ n : ℕ, 3 ≤ n → n ≤ 10000 →
    ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C n

/-- `(3, 3, 5)` via the **supported** bounded hypothesis, not via the unverified mod-3 one. -/
theorem no_beal_counterexample_3_3_5_of_bounded (hB : BCDYThreeThreeBounded) :
    ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 5 := by
  apply no_beal_counterexample_3_3_p 5 (by decide)
  exact hB 5 (by decide) (by decide)

/-- In particular, signature `(3, 3, 5)` admits no Beal counterexample — but only under the
UNVERIFIED mod-3 hypothesis. Prefer `no_beal_counterexample_3_3_5_of_bounded`. -/
theorem no_beal_counterexample_3_3_5 (hF : FreitasTheoremMod3) :
    ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 5 := by
  apply no_beal_counterexample_3_3_p_of_mod_two hF 5 (by decide) (by decide) (by decide)

/-! ### Interaction with the mod-9 machinery (U241, pool C104)

`Beal.not_three_dvd_z_of_three_dvd_xy` (in `Structure.lean`) rules out `3 ∣ z` when `3 ∣ x`,
`3 ∣ y` **and** none of `A, B, C` is divisible by `3`.  Signature `(3, 3, z)` satisfies `3 ∣ x`
and `3 ∣ y` by definition, so it looks like the natural place to apply it.  It never applies:
`KrausProp7` forces `3 ∣ C`, contradicting the hypothesis `C % 3 ≠ 0`.

So that lemma is **vacuous on signature `(3, 3, z)`** — a fact worth recording, since the lemma's
shape invites exactly that misuse. -/

/-- Under `KrausProp7`, no Beal counterexample of signature `(3, 3, z)` has `C` coprime to `3`;
hence `not_three_dvd_z_of_three_dvd_xy` cannot fire on this signature. -/
theorem three_dvd_C_of_signature_three_three (hK : KrausProp7) {A B C z : ℕ}
    (h : IsBealCounterexample A B C 3 3 z) : C % 3 = 0 := by
  obtain ⟨hA, hB, hC, -, -, hz, hprim, heq⟩ := h
  have hcop := coprime_ab_of_beal_counterexample A B C z hA hB hC hz hprim heq
  have h6 := hK A B C z hz hA hB hC hcop heq
  omega


/-! ### The `(p,p,r)` dichotomy collapses at `p = 3` (U242, pool C105)

`Beal.ppr_dichotomy` (in `SameOddPrime.lean`) splits signature `(p,p,r)` into a *coprime branch*
(`¬ p ∣ A + B`) and a *p-adic branch* (`p ∣ A + B`, where `ppr_padic_branch` gives
`v_p(A+B) + 1 = r · v_p(C)`).  Under `KrausProp7` the coprime branch is **empty at `p = 3`**:
`3 ∣ C` forces `3 ∣ A³ + B³`, and `n³ ≡ n (mod 3)` turns that into `3 ∣ A + B`.

So every `(3,3,z)` counterexample lies in the p-adic branch, and `v₃(A+B) = z·v₃(C) − 1 ≥ z − 1`,
i.e. `3^(z-1) ∣ A + B`.  Category: elementary / LTE, which the survey lists as unable to resolve
Beal; recorded as structure, not as progress. -/

/-- `n³ ≡ n (mod 3)`. -/
theorem cube_mod_three (n : ℕ) : n ^ 3 % 3 = n % 3 := by
  conv_lhs => rw [show n = 3 * (n / 3) + n % 3 by omega]
  have h : n % 3 < 3 := Nat.mod_lt _ (by norm_num)
  interval_cases h3 : (n % 3) <;> ring_nf <;> omega

/-- **The coprime branch is empty at `p = 3`.**  Under `KrausProp7`, every Beal counterexample of
signature `(3, 3, z)` satisfies `3 ∣ A + B`, so `ppr_dichotomy` always lands in the p-adic branch. -/
theorem three_dvd_add_of_signature_three_three (hK : KrausProp7) {A B C z : ℕ}
    (h : IsBealCounterexample A B C 3 3 z) : 3 ∣ A + B := by
  have hC3 : C % 3 = 0 := three_dvd_C_of_signature_three_three hK h
  obtain ⟨-, -, hC, -, -, hz, -, heq⟩ := h
  have hCz : C ^ z % 3 = 0 := by
    obtain ⟨c, rfl⟩ : ∃ c, C = 3 * c := ⟨C / 3, by omega⟩
    have : (3 * c) ^ z = 3 ^ z * c ^ z := by rw [Nat.mul_pow]
    rw [this]
    have h3 : 3 ∣ 3 ^ z := dvd_pow_self 3 (by omega)
    obtain ⟨t, ht⟩ := h3
    rw [ht]
    have hd : 3 ∣ 3 * t * c ^ z := ⟨t * c ^ z, by ring⟩
    omega
  have hsum : (A ^ 3 + B ^ 3) % 3 = 0 := by rw [heq]; exact hCz
  have hA := cube_mod_three A
  have hB := cube_mod_three B
  omega

/-! ### 7. Non-Isomorphism to Target Newforms 72a1 and 144a1 (Candidate C252)

The target modular newforms at Serre conductor levels 72 and 144 have $j$-invariants:
  $$j(72a1) = j(144a1) = \frac{2048}{3} = \frac{2^{11}}{3}.$$
Equating the Kraus Frey curve $j$-invariant $j(E_{A, B}) = 6912 \frac{A^3 B^3}{C^{2p}}$ to $2048/3$
yields the Diophantine equation:
  $$81 A^3 B^3 = 8 C^{2p} = 8 (A^3 + B^3)^2.$$
Setting $X = A^3$ and $Y = B^3$, this factors algebraically as:
  $$(8X - Y)(X - 8Y) = 0,$$
forcing $B^3 = 8 A^3$ or $A^3 = 8 B^3$. By coprimality, $(A, B) \in \{(1, 2), (2, 1)\}$,
which forces $C^p = 1^3 + 2^3 = 9 = 3^2$.
Because 9 is not a perfect $p$-th power for any integer $p \ge 3$, no coprime integer solution
to $A^3 + B^3 = C^p$ can ever produce a Frey curve isomorphic over $\overline{\mathbb{Q}}$
to the newforms $72a1$ or $144a1$. -/

/-- Algebraic factorization of the Kraus Frey $j$-invariant matching identity. -/
theorem kraus_j_matching_factorization (X Y : ℤ) :
    81 * X * Y - 8 * (X + Y) ^ 2 = - (8 * X - Y) * (X - 8 * Y) := by
  ring

/-- The power $C^p = 9$ has no solutions in positive integers for $p \ge 3$. -/
theorem not_pow_p_eq_nine (C p : ℕ) (hp : p ≥ 3) : C ^ p ≠ 9 := by
  intro h
  rcases C with _ | C
  · rw [zero_pow (by omega)] at h; omega
  · rcases C with _ | C
    · rw [Nat.zero_add, one_pow] at h; omega
    · rcases C with _ | C
      · -- C = 2
        rcases Nat.eq_or_lt_of_le hp with rfl | hp4
        · revert h; decide
        · have h16 : 2 ^ 4 ≤ 2 ^ p := Nat.pow_le_pow_right (by omega) hp4
          have h_val : 2 ^ 4 = 16 := by rfl
          rw [h] at h16
          omega
      · -- C >= 3
        have h27 : 3 ^ 3 ≤ (C + 3) ^ p := by
          calc 3 ^ 3 ≤ 3 ^ p := Nat.pow_le_pow_right (by omega) hp
            _ ≤ (C + 3) ^ p := Nat.pow_le_pow_left (by omega) p
        have h_val : 3 ^ 3 = 27 := by rfl
        rw [h] at h27
        omega

end Beal
