/-
Copyright (c) 2026 Formal Verification Group. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Formal Verification Specialist
-/
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Nat.Prime.Basic

/-!
# The Beal Conjecture in Lean 4

This module formalizes the mathematical statement of the **Beal Conjecture**,
its primitive formulation, its prime-factor formulation, and the derivation of
Fermat's Last Theorem as an immediate corollary.

## Statement

The Beal Conjecture asserts that if:
  $$A^x + B^y = C^z$$
where $A, B, C, x, y, z$ are positive integers and $x, y, z \ge 3$,
then $A, B, C$ must share a common prime factor, or equivalently:
  $$\gcd(A, B, C) > 1.$$

## References

* R. Daniel Mauldin, *A Generalization of Fermat's Last Theorem: The Beal Conjecture and Prize Problem*,
  Notices of the AMS, December 1997, Vol. 44, No. 11, pp. 1436–1437.
-/

namespace Beal

/--
The greatest common divisor of three natural numbers `A, B, C`,
defined associatively as `gcd(A, gcd(B, C))`.
-/
def gcd3 (A B C : ℕ) : ℕ :=
  Nat.gcd A (Nat.gcd B C)

/--
A triple of natural numbers `(A, B, C)` is primitive if `gcd(A, B, C) = 1`.
-/
def IsPrimitiveTriple (A B C : ℕ) : Prop :=
  gcd3 A B C = 1

/--
A tuple `(A, B, C, x, y, z)` forms a **Beal counterexample** if:
1. `A, B, C` are strictly positive integers (`> 0`).
2. The exponents `x, y, z` satisfy `x ≥ 3`, `y ≥ 3`, `z ≥ 3`.
3. The bases are mutually coprime: `gcd(A, B, C) = 1`.
4. The Diophantine equation holds: `A^x + B^y = C^z`.
-/
def IsBealCounterexample (A B C x y z : ℕ) : Prop :=
  A > 0 ∧ B > 0 ∧ C > 0 ∧
  x ≥ 3 ∧ y ≥ 3 ∧ z ≥ 3 ∧
  gcd3 A B C = 1 ∧
  A ^ x + B ^ y = C ^ z

/--
**The Beal Conjecture (Primitive Formulation)**:
For any strictly positive integers `A, B, C` and exponents `x, y, z ≥ 3`,
if `A^x + B^y = C^z`, then `gcd(A, B, C) > 1`.
-/
def BealConjecture : Prop :=
  ∀ (A B C x y z : ℕ),
    A > 0 → B > 0 → C > 0 →
    x ≥ 3 → y ≥ 3 → z ≥ 3 →
    A ^ x + B ^ y = C ^ z →
    gcd3 A B C > 1

/--
**The Beal Conjecture (Prime Divisor Formulation)**:
Every positive integer solution to `A^x + B^y = C^z` with `x, y, z ≥ 3`
admits a common prime divisor `p` dividing `A`, `B`, and `C`.
-/
def BealConjecturePrimeForm : Prop :=
  ∀ (A B C x y z : ℕ),
    A > 0 → B > 0 → C > 0 →
    x ≥ 3 → y ≥ 3 → z ≥ 3 →
    A ^ x + B ^ y = C ^ z →
    ∃ p : ℕ, Nat.Prime p ∧ p ∣ A ∧ p ∣ B ∧ p ∣ C

/--
The Beal Conjecture is logically equivalent to the nonexistence of any Beal counterexample.
-/
theorem beal_iff_no_counterexample :
    BealConjecture ↔ ¬ ∃ (A B C x y z : ℕ), IsBealCounterexample A B C x y z := by
  constructor
  · intro h ⟨A, B, C, x, y, z, hA, hB, hC, hx, hy, hz, hprim, heq⟩
    have hg := h A B C x y z hA hB hC hx hy hz heq
    rw [hprim] at hg
    exact Nat.lt_irrefl 1 hg
  · intro h A B C x y z hA hB hC hx hy hz heq
    by_contra! hle
    have hgcd_pos : gcd3 A B C > 0 := by
      unfold gcd3
      have hC_pos : Nat.gcd B C > 0 := Nat.gcd_pos_of_pos_right B hC
      exact Nat.gcd_pos_of_pos_right A hC_pos
    have hgcd1 : gcd3 A B C = 1 := by
      omega
    have hce : IsBealCounterexample A B C x y z :=
      ⟨hA, hB, hC, hx, hy, hz, hgcd1, heq⟩
    exact h ⟨A, B, C, x, y, z, hce⟩

/--
A common prime factor exists if and only if the greatest common divisor is strictly greater than 1.
-/
lemma gcd3_gt_one_iff_exists_prime (A B C : ℕ) (hA : A > 0) :
    gcd3 A B C > 1 ↔ ∃ p : ℕ, Nat.Prime p ∧ p ∣ A ∧ p ∣ B ∧ p ∣ C := by
  constructor
  · intro hg
    obtain ⟨p, hp, hdvd⟩ := Nat.exists_prime_and_dvd (by omega : gcd3 A B C ≠ 1)
    have hdvdA : p ∣ A := dvd_trans hdvd (Nat.gcd_dvd_left A (Nat.gcd B C))
    have hdvdBC : p ∣ Nat.gcd B C := dvd_trans hdvd (Nat.gcd_dvd_right A (Nat.gcd B C))
    have hdvdB : p ∣ B := dvd_trans hdvdBC (Nat.gcd_dvd_left B C)
    have hdvdC : p ∣ C := dvd_trans hdvdBC (Nat.gcd_dvd_right B C)
    exact ⟨p, hp, hdvdA, hdvdB, hdvdC⟩
  · intro ⟨p, hp, hdA, hdB, hdC⟩
    have hdBC : p ∣ Nat.gcd B C := Nat.dvd_gcd hdB hdC
    have hdABC : p ∣ gcd3 A B C := Nat.dvd_gcd hdA hdBC
    have hp_pos : p > 1 := Nat.Prime.one_lt hp
    exact lt_of_lt_of_le hp_pos (Nat.le_of_dvd (by
      unfold gcd3
      have hBC_pos : Nat.gcd B C > 0 := by
        obtain ⟨k, rfl⟩ := hdC
        have : C > 0 := by omega
        exact Nat.gcd_pos_of_pos_right B (by omega)
      exact Nat.gcd_pos_of_pos_left (Nat.gcd B C) hA) hdABC)

/--
Equivalence between the primitive Beal Conjecture and its prime-divisor formulation.
-/
theorem beal_iff_prime_form :
    BealConjecture ↔ BealConjecturePrimeForm := by
  constructor
  · intro h A B C x y z hA hB hC hx hy hz heq
    have hg := h A B C x y z hA hB hC hx hy hz heq
    exact (gcd3_gt_one_iff_exists_prime A B C hA).mp hg
  · intro h A B C x y z hA hB hC hx hy hz heq
    have ⟨p, hp, hdA, hdB, hdC⟩ := h A B C x y z hA hB hC hx hy hz heq
    exact (gcd3_gt_one_iff_exists_prime A B C hA).mpr ⟨p, hp, hdA, hdB, hdC⟩

/--
**Fermat's Last Theorem as a direct corollary of the Beal Conjecture**:
If the Beal Conjecture is true, then for any exponent `n ≥ 3`,
there are no positive integers `A, B, C` with `gcd(A, B, C) = 1` such that `A^n + B^n = C^n`.
-/
theorem flt_of_beal (h : BealConjecture) (n : ℕ) (hn : n ≥ 3)
    (A B C : ℕ) (hA : A > 0) (hB : B > 0) (hC : C > 0)
    (h_prim : gcd3 A B C = 1) :
    A ^ n + B ^ n ≠ C ^ n := by
  intro heq
  have hg := h A B C n n n hA hB hC hn hn hn heq
  rw [h_prim] at hg
  exact Nat.lt_irrefl 1 hg

end Beal
