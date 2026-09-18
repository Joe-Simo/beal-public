/-
# What remains (U139): the residual shape of a Beal counterexample

A kernel-checked account of what is proved and what is left. If any counterexample exists, one
exists whose exponents lie in `{4} ∪ {odd primes}` and which avoids every family closed
unconditionally in this repository. Nothing here depends on external hypotheses.
-/
import Beal.Structure
import Beal.Necessary

namespace Beal

/-- The residual shape: exponents reduced to `{4} ∪ {odd primes}`, and the two reduced signatures
closed unconditionally here excluded — `(4,4,4)` (mathlib `not_fermat_42`) and `(3,3,3)` (mathlib FLT₃) —
together with the elementary structural facts. Nothing else is claimed. -/
def ResidualShape (A B C x y z : ℕ) : Prop :=
  IsBealCounterexample A B C x y z ∧
  Reduced x ∧ Reduced y ∧ Reduced z ∧
  -- `(4,4,4)` is closed by Fermat (mathlib `not_fermat_42`)
  ¬ (x = 4 ∧ y = 4 ∧ z = 4) ∧
  -- `(3,3,3)` is closed by mathlib's FLT₃
  ¬ (x = 3 ∧ y = 3 ∧ z = 3) ∧
  -- exactly one base is even
  ((A % 2 = 0 ∧ B % 2 = 1 ∧ C % 2 = 1) ∨ (A % 2 = 1 ∧ B % 2 = 0 ∧ C % 2 = 1) ∨
    (A % 2 = 1 ∧ B % 2 = 1 ∧ C % 2 = 0)) ∧
  -- if `C` is even then `x, y` are not both `4` (in fact not both even)
  (C % 2 = 0 → ¬ (x = 4 ∧ y = 4)) ∧
  -- no cancellation: `C^z` lies strictly above each term and within a factor 2 of the larger
  (A ^ x < C ^ z ∧ B ^ y < C ^ z ∧ C ^ z ≤ 2 * max (A ^ x) (B ^ y)) ∧
  -- the bases are pairwise coprime and distinct
  Nat.gcd A B = 1 ∧ Nat.gcd A C = 1 ∧ Nat.gcd B C = 1 ∧ A ≠ B

/-- **What remains.** Any Beal counterexample yields one of residual shape. -/
theorem residual_of_counterexample {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    ∃ A' B' C' x' y' z' : ℕ, ResidualShape A' B' C' x' y' z' := by
  obtain ⟨A', B', C', x', y', z', h', hx, hy, hz⟩ := reduction h
  refine ⟨A', B', C', x', y', z', h', hx, hy, hz, ?_, ?_, exactly_one_even h', ?_,
    no_cancellation h', gcd_ab_eq_one h', gcd_ac_eq_one h', gcd_bc_eq_one h', fun hAB => not_eq_bases (hAB ▸ h')⟩
  · rintro ⟨rfl, rfl, rfl⟩
    exact no_counterexample_of_four_four_even (by norm_num) (by norm_num) (by norm_num) h'
  · rintro ⟨rfl, rfl, rfl⟩
    exact no_counterexample_of_three_dvd_all (by norm_num) (by norm_num) (by norm_num) h'
  · rintro hC ⟨rfl, rfl⟩
    exact not_both_exponents_even_of_even_C h' hC ⟨by norm_num, by norm_num⟩

/-- Contrapositive form: to prove Beal it suffices to refute every residual shape. -/
theorem beal_of_no_residual (hres : ∀ A B C x y z : ℕ, ¬ ResidualShape A B C x y z) :
    ∀ A B C x y z : ℕ, ¬ IsBealCounterexample A B C x y z := by
  intro A B C x y z h
  obtain ⟨A', B', C', x', y', z', hr⟩ := residual_of_counterexample h
  exact hres _ _ _ _ _ _ hr

end Beal
