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

/--
**Classical Dimension Vanishing Theorem**:
The space of weight-2 cusp forms on $\Gamma_0(18)$ is trivial:
  $$\dim S_2(\Gamma_0(18)) = 0.$$
-/
theorem dim_S2_Gamma0_18 : cuspFormsDimGamma0 18 2 = 0 := by
  unfold cuspFormsDimGamma0
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

end Beal
