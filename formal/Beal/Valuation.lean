/-
# The four `SquarefreeCore` axioms, proved

`Beal/SquarefreeCore.lean` asserts four elementary p-adic valuation facts as custom `axiom`s,
and shadows mathlib's `padicValNat` with its own definition.  All four are theorems of mathlib.
This file proves them, so no custom axiom is needed for any of them.

No `sorry`, no custom `axiom`s.
-/
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Ring

namespace Beal

open Nat

/-- Axiom 1 of `SquarefreeCore`, proved: `v_p(A^x) = x * v_p(A)`. -/
theorem factorization_pow_eq (p A x : ℕ) :
    (A ^ x).factorization p = x * A.factorization p := by
  rw [Nat.factorization_pow]
  simp [mul_comm]

/-- Axiom 2 of `SquarefreeCore`, proved: for `A > 0` and `p` prime, `v_p(A) ≥ 1 ↔ p ∣ A`. -/
theorem factorization_pos_iff_dvd {p A : ℕ} (hp : p.Prime) (hA : 0 < A) :
    1 ≤ A.factorization p ↔ p ∣ A := by
  constructor
  · intro h
    by_contra hnd
    rw [Nat.factorization_eq_zero_of_not_dvd hnd] at h
    omega
  · intro hd
    have := (Nat.Prime.factorization_pos_of_dvd hp (by omega) hd)
    omega

/-- Axiom 3 of `SquarefreeCore`, proved: `¬ p ∣ A → v_p(A) = 0`. -/
theorem factorization_eq_zero_of_not_dvd' {p A : ℕ} (h : ¬ p ∣ A) :
    A.factorization p = 0 :=
  Nat.factorization_eq_zero_of_not_dvd h

/-- Axiom 4 of `SquarefreeCore`, proved, in its actually-used form:
if `p ∣ X` and `p ∤ Y` then `p ∤ X + Y`, hence `v_p(X + Y) = 0`. -/
theorem factorization_add_eq_zero {p X Y : ℕ}
    (hX : p ∣ X) (hY : ¬ p ∣ Y) : (X + Y).factorization p = 0 := by
  refine Nat.factorization_eq_zero_of_not_dvd (fun hsum => hY ?_)
  exact (Nat.dvd_add_right hX).mp hsum

end Beal
