/-
# ⚠ SUPERSEDED — this file does not build, and does not need to.

Its endpoint, `beal_counterexample_pairwise_coprime` (the bases of a Beal counterexample are
pairwise coprime), is **already proved axiom-free** in `Beal/Structure.lean` as the three theorems

    gcd_ab_eq_one, gcd_ac_eq_one, gcd_bc_eq_one

each depending only on `[propext, Classical.choice, Quot.sound]`.  That proof needs **no p-adic
valuations at all**: a prime dividing two of the bases divides the third via the equation, hence
divides `gcd3 A B C = 1`.

The four `padicValNat` axioms this file asserts are likewise proved, from mathlib, in
`Beal/Valuation.lean`.

This file remains unbuilt for two reasons, both recorded in the U113 audit:
  * it shadows mathlib's `padicValNat` with its own definition built on `Nat.factorization`,
    without importing the module that provides that function;
  * repairing the shadowing buys nothing, since every result it aims at is already verified more
    simply elsewhere.

It is kept rather than deleted so the original approach is preserved.
-/

/-
Copyright (c) 2026 Formal Verification Group. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Formal Verification Specialist
-/
import Beal.Conjecture
import Mathlib.Data.Nat.Defs
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Ring

/-!
# p-Adic Valuation Identities, Power Multiplicities, and Pairwise Coprimality

This module formalizes the $p$-adic valuation arithmetic for generalized Fermat equations
$A^x + B^y = C^z$, establishes the valuation identity for powers:
  $$v_p(A^x) = x \cdot v_p(A)$$
and deduces that any primitive solution $(A, B, C)$ to $A^x + B^y = C^z$ with exponents
$x, y, z \ge 3$ has **mutually pairwise coprime bases**:
  $$\gcd(A, B) = 1, \quad \gcd(B, C) = 1, \quad \gcd(A, C) = 1.$$

## Main Theorems Formalized:

1. **p-Adic Valuation on Powers**:
   - $v_p(A^x) = x \cdot v_p(A)$ for prime $p$ and $A > 0$.
   - If $p \mid A$, then $v_p(A) \ge 1$, so $v_p(A^x) \ge x \ge 3$.

2. **Non-Archimedean Addition and Base Disjointness**:
   - If $\gcd(A, B) = 1$ and $p \mid A$, then $p \nmid B$, so $v_p(B) = 0$ and $v_p(B^y) = 0$.
   - Strict ultrametric equality: $v_p(A^x + B^y) = \min(v_p(A^x), v_p(B^y)) = 0$.
   - Since $A^x + B^y = C^z$, $v_p(C^z) = 0 \implies v_p(C) = 0 \implies p \nmid C$.

3. **Mutual Pairwise Coprimality Theorem**:
   - For any primitive solution to $A^x + B^y = C^z$ with $x, y, z \ge 1$:
       $$\gcd(A, B) = 1 \iff \gcd(B, C) = 1 \iff \gcd(A, C) = 1 \iff \gcd3(A, B, C) = 1.$$
   - In particular, in every Beal counterexample, the bases $(A, B, C)$ are unconditionally
     pairwise coprime.
-/

namespace Beal

/-! ### 1. p-Adic Valuation on Natural Numbers -/

/--
The p-adic valuation v_p(n) of a natural number n at a prime p:
the maximal exponent k such that p^k divides n (with v_p(0) = 0).
-/
def padicValNat (p : ℕ) (n : ℕ) : ℕ :=
  if p ≤ 1 ∨ n = 0 then 0
  else Nat.factorization n p

/--
**p-Adic Valuation Power Identity**:
For any prime p and positive integers A, x:
  v_p(A^x) = x * v_p(A).
-/
axiom padicValNat_pow (p : ℕ) (hp : Nat.Prime p) (A : ℕ) (hA : A > 0) (x : ℕ) :
    padicValNat p (A ^ x) = x * padicValNat p A

/--
A prime p divides A if and only if v_p(A) ≥ 1.
-/
axiom padicValNat_pos_iff_dvd (p : ℕ) (hp : Nat.Prime p) (A : ℕ) (hA : A > 0) :
    padicValNat p A ≥ 1 ↔ p ∣ A

/--
If p does not divide A, then v_p(A) = 0.
-/
axiom padicValNat_eq_zero_of_not_dvd (p : ℕ) (A : ℕ) (hnot : ¬ p ∣ A) :
    padicValNat p A = 0

/--
Strict ultrametric property: if v_p(X) > v_p(Y), then v_p(X + Y) = v_p(Y).
In particular, if v_p(X) ≥ 1 and v_p(Y) = 0, then v_p(X + Y) = 0.
-/
axiom padicValNat_add_of_zero_right (p : ℕ) (hp : Nat.Prime p) (X Y : ℕ)
    (hX : X > 0) (hY : Y > 0)
    (hX_pos : padicValNat p X ≥ 1) (hY_zero : padicValNat p Y = 0) :
    padicValNat p (X + Y) = 0

/-! ### 2. Multiplicity Bounds for Beal Bases -/

/--
For any prime p dividing A, the valuation of A^x is at least x:
  v_p(A^x) ≥ x.
When x ≥ 3, v_p(A^x) ≥ x ≥ 3.
-/
theorem padicValNat_pow_ge (p A x : ℕ) (hp : Nat.Prime p) (hA : A > 0)
    (hdiv : p ∣ A) (hx : x ≥ 3) :
    padicValNat p (A ^ x) ≥ x ∧ padicValNat p (A ^ x) ≥ 3 := by
  have hpow := padicValNat_pow p hp A hA x
  have hpos : padicValNat p A ≥ 1 := (padicValNat_pos_iff_dvd p hp A hA).mpr hdiv
  rw [hpow]
  constructor
  · nlinarith
  · nlinarith

/-! ### 3. Divisibility and Valuation in A^x + B^y = C^z -/

/--
If p is prime, p ∣ A, and gcd(A, B) = 1, then p does not divide B.
-/
lemma not_dvd_of_coprime (p A B : ℕ) (hp : Nat.Prime p)
    (hdivA : p ∣ A) (hcop : Nat.Coprime A B) : ¬ p ∣ B := by
  intro hdivB
  have hdvd_gcd : p ∣ Nat.gcd A B := Nat.dvd_gcd hdivA hdivB
  rw [hcop] at hdvd_gcd
  have hp_gt1 : p > 1 := Nat.Prime.one_lt hp
  have hp_le1 : p ≤ 1 := Nat.le_of_dvd (by decide) hdvd_gcd
  omega

/--
If p is prime and does not divide B, it does not divide any power B^y.
-/
lemma not_dvd_pow_of_not_dvd (p B y : ℕ) (hp : Nat.Prime p) (hnot : ¬ p ∣ B) :
    ¬ p ∣ B ^ y := by
  intro hdvd
  exact hnot (Nat.Prime.dvd_of_dvd_pow hp hdvd)

/--
A prime factor divides any positive power: p ∣ A → p ∣ A^x.
-/
lemma dvd_pow_of_dvd (p A x : ℕ) (hx : x ≥ 1) (hdvd : p ∣ A) : p ∣ A ^ x := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : x ≠ 0)
  rw [pow_succ]
  exact dvd_trans hdvd (dvd_mul_right A (A ^ k))

/--
If gcd(A, B) = 1 and p ∣ A, then v_p(B^y) = 0.
-/
theorem padicValNat_other_base_pow_zero (p A B y : ℕ) (hp : Nat.Prime p)
    (hdivA : p ∣ A) (hcop : Nat.Coprime A B) :
    padicValNat p (B ^ y) = 0 := by
  have hnotB : ¬ p ∣ B := not_dvd_of_coprime p A B hp hdivA hcop
  have hnotBy : ¬ p ∣ B ^ y := not_dvd_pow_of_not_dvd p B y hp hnotB
  exact padicValNat_eq_zero_of_not_dvd p (B ^ y) hnotBy

/--
**Valuation Vanishing on Sum**:
If gcd(A, B) = 1 and p ∣ A, then v_p(A^x + B^y) = 0.
-/
theorem padicValNat_sum_zero (p A B x y : ℕ) (hp : Nat.Prime p)
    (hA : A > 0) (hB : B > 0) (hx : x ≥ 1)
    (hdivA : p ∣ A) (hcop : Nat.Coprime A B) :
    padicValNat p (A ^ x + B ^ y) = 0 := by
  have hAx_pos : A ^ x > 0 := Nat.pos_pow_of_pos x hA
  have hBy_pos : B ^ y > 0 := Nat.pos_pow_of_pos y hB
  have hAx_val_pos : padicValNat p (A ^ x) ≥ 1 := by
    have hdvdAx : p ∣ A ^ x := dvd_pow_of_dvd p A x hx hdivA
    exact (padicValNat_pos_iff_dvd p hp (A ^ x) hAx_pos).mpr hdvdAx
  have hBy_val_zero := padicValNat_other_base_pow_zero p A B y hp hdivA hcop
  exact padicValNat_add_of_zero_right p hp (A ^ x) (B ^ y) hAx_pos hBy_pos hAx_val_pos hBy_val_zero

/--
**p Does Not Divide C**:
If gcd(A, B) = 1, A^x + B^y = C^z, and p ∣ A, then p does not divide C.
-/
theorem not_dvd_c_of_dvd_a (p A B C x y z : ℕ) (hp : Nat.Prime p)
    (hA : A > 0) (hB : B > 0) (hC : C > 0) (hx : x ≥ 1) (hz : z ≥ 1)
    (hdivA : p ∣ A) (hcop : Nat.Coprime A B)
    (heq : A ^ x + B ^ y = C ^ z) :
    ¬ p ∣ C := by
  have h_val_sum := padicValNat_sum_zero p A B x y hp hA hB hx hdivA hcop
  rw [heq] at h_val_sum
  have h_val_pow := padicValNat_pow p hp C hC z
  rw [h_val_sum] at h_val_pow
  intro hdivC
  have hC_val_pos : padicValNat p C ≥ 1 := (padicValNat_pos_iff_dvd p hp C hC).mpr hdivC
  have : z * padicValNat p C ≥ 1 := by nlinarith
  omega

/--
Symmetrically, if gcd(A, B) = 1, A^x + B^y = C^z, and p ∣ B, then p does not divide C.
-/
theorem not_dvd_c_of_dvd_b (p A B C x y z : ℕ) (hp : Nat.Prime p)
    (hA : A > 0) (hB : B > 0) (hC : C > 0) (hy : y ≥ 1) (hz : z ≥ 1)
    (hdivB : p ∣ B) (hcop : Nat.Coprime A B)
    (heq : A ^ x + B ^ y = C ^ z) :
    ¬ p ∣ C := by
  have heq_comm : B ^ y + A ^ x = C ^ z := by omega
  have hcop_ba : Nat.Coprime B A := Nat.Coprime.symm hcop
  exact not_dvd_c_of_dvd_a p B A C y x z hp hB hA hC hy hz hdivB hcop_ba heq_comm

/-! ### 4. Pairwise Coprimality of Bases -/

/--
Predicate asserting that three natural numbers A, B, C are mutually pairwise coprime.
-/
def PairwiseCoprime (A B C : ℕ) : Prop :=
  Nat.Coprime A B ∧ Nat.Coprime B C ∧ Nat.Coprime A C

/--
If gcd(A, B) = 1 in A^x + B^y = C^z, then gcd(A, C) = 1.
-/
theorem coprime_ac_of_coprime_ab (A B C x y z : ℕ)
    (hA : A > 0) (hB : B > 0) (hC : C > 0) (hx : x ≥ 1) (hz : z ≥ 1)
    (hcop : Nat.Coprime A B)
    (heq : A ^ x + B ^ y = C ^ z) :
    Nat.Coprime A C := by
  by_contra! hnot
  obtain ⟨p, hp, hdvd⟩ := Nat.exists_prime_and_dvd (by omega : Nat.gcd A C ≠ 1)
  have hdvdA : p ∣ A := dvd_trans hdvd (Nat.gcd_dvd_left A C)
  have hdvdC : p ∣ C := dvd_trans hdvd (Nat.gcd_dvd_right A C)
  have hnotC := not_dvd_c_of_dvd_a p A B C x y z hp hA hB hC hx hz hdvdA hcop heq
  exact hnotC hdvdC

/--
If gcd(A, B) = 1 in A^x + B^y = C^z, then gcd(B, C) = 1.
-/
theorem coprime_bc_of_coprime_ab (A B C x y z : ℕ)
    (hA : A > 0) (hB : B > 0) (hC : C > 0) (hy : y ≥ 1) (hz : z ≥ 1)
    (hcop : Nat.Coprime A B)
    (heq : A ^ x + B ^ y = C ^ z) :
    Nat.Coprime B C := by
  have heq_comm : B ^ y + A ^ x = C ^ z := by omega
  have hcop_ba : Nat.Coprime B A := Nat.Coprime.symm hcop
  exact coprime_ac_of_coprime_ab B A C y x z hB hA hC hy hz hcop_ba heq_comm

/--
**Mutual Pairwise Coprimality Theorem**:
In any positive integer solution to A^x + B^y = C^z with x, y, z ≥ 1,
if gcd(A, B) = 1, then A, B, C are mutually pairwise coprime:
  gcd(A, B) = 1,  gcd(B, C) = 1,  gcd(A, C) = 1.
-/
theorem pairwise_coprime_of_coprime_ab (A B C x y z : ℕ)
    (hA : A > 0) (hB : B > 0) (hC : C > 0)
    (hx : x ≥ 1) (hy : y ≥ 1) (hz : z ≥ 1)
    (hcop : Nat.Coprime A B)
    (heq : A ^ x + B ^ y = C ^ z) :
    PairwiseCoprime A B C :=
  ⟨hcop,
   coprime_bc_of_coprime_ab A B C x y z hA hB hC hy hz hcop heq,
   coprime_ac_of_coprime_ab A B C x y z hA hB hC hx hz hcop heq⟩

/--
**Pairwise Coprimality of Beal Counterexamples**:
In every hypothetical Beal counterexample $(A, B, C, x, y, z)$, the three bases
$A, B, C$ are unconditionally mutually pairwise coprime:
  $$\gcd(A, B) = 1, \quad \gcd(B, C) = 1, \quad \gcd(A, C) = 1.$$
-/
theorem beal_counterexample_pairwise_coprime (A B C x y z : ℕ)
    (h : IsBealCounterexample A B C x y z) :
    PairwiseCoprime A B C := by
  obtain ⟨hA, hB, hC, hx, hy, hz, hgcd3, heq⟩ := h
  have hcop_ab : Nat.Coprime A B := by
    by_contra! hnot
    obtain ⟨p, hp, hdvd⟩ := Nat.exists_prime_and_dvd (by omega : Nat.gcd A B ≠ 1)
    have hdvdA : p ∣ A := dvd_trans hdvd (Nat.gcd_dvd_left A B)
    have hdvdB : p ∣ B := dvd_trans hdvd (Nat.gcd_dvd_right A B)
    have hdvdAx : p ∣ A ^ x := dvd_pow_of_dvd p A x (by omega) hdvdA
    have hdvdBy : p ∣ B ^ y := dvd_pow_of_dvd p B y (by omega) hdvdB
    have hdvdSum : p ∣ (A ^ x + B ^ y) := Nat.dvd_add hdvdAx hdvdBy
    rw [heq] at hdvdSum
    have hdvdC : p ∣ C := Nat.Prime.dvd_of_dvd_pow hp hdvdSum
    have hdvdBC : p ∣ Nat.gcd B C := Nat.dvd_gcd hdvdB hdvdC
    have hdvdABC : p ∣ gcd3 A B C := Nat.dvd_gcd hdvdA hdvdBC
    rw [hgcd3] at hdvdABC
    have hp_gt1 : p > 1 := Nat.Prime.one_lt hp
    have hp_le1 : p ≤ 1 := Nat.le_of_dvd (by decide) hdvdABC
    omega
  exact pairwise_coprime_of_coprime_ab A B C x y z hA hB hC (by omega) (by omega) (by omega) hcop_ab heq

end Beal
