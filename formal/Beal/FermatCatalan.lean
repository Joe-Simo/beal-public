/-
# The known Fermat–Catalan solutions, and why each fails Beal

There are exactly ten known primitive (coprime) solutions of `a^p + b^q = c^r` with
`1/p + 1/q + 1/r < 1`.  **Every one of them has `2` among its exponents.**

Beal's conjecture is therefore equivalent to the assertion that `2` is an *obligatory* exponent
for every non-trivial primitive solution in the hyperbolic regime.

This file verifies each identity in exact arithmetic and confirms that each fails
`IsBealCounterexample` **for the same reason**: an exponent equal to 2.

No `sorry`, no custom axioms.
-/
import Beal.Conjecture
import Mathlib.Tactic.NormNum

namespace Beal

/-- Each known solution, as an exact identity. -/
theorem fc1  : 1 ^ 7 + 2 ^ 3 = 3 ^ 2 := by norm_num
theorem fc2  : 2 ^ 5 + 7 ^ 2 = 3 ^ 4 := by norm_num
theorem fc3  : 7 ^ 3 + 13 ^ 2 = 2 ^ 9 := by norm_num
theorem fc4  : 2 ^ 7 + 17 ^ 3 = 71 ^ 2 := by norm_num
theorem fc5  : 3 ^ 5 + 11 ^ 4 = 122 ^ 2 := by norm_num
theorem fc6  : 17 ^ 7 + 76271 ^ 3 = 21063928 ^ 2 := by norm_num
theorem fc7  : 1414 ^ 3 + 2213459 ^ 2 = 65 ^ 7 := by norm_num
/-- Note: the value `15312283` here.  An external survey gave `1531228`, which is **false**. -/
theorem fc8  : 9262 ^ 3 + 15312283 ^ 2 = 113 ^ 7 := by norm_num
theorem fc9  : 43 ^ 8 + 96222 ^ 3 = 30042907 ^ 2 := by norm_num
theorem fc10 : 33 ^ 8 + 1549034 ^ 2 = 15613 ^ 3 := by norm_num

/-- **The general reason every known solution fails Beal.**
A tuple with any exponent equal to `2` is not a Beal counterexample, because the definition
demands all three exponents be at least `3`. -/
theorem not_counterexample_of_exponent_two {A B C x y z : ℕ}
    (h2 : x = 2 ∨ y = 2 ∨ z = 2) : ¬ IsBealCounterexample A B C x y z := by
  rintro ⟨_, _, _, hx, hy, hz, _, _⟩
  rcases h2 with h | h | h <;> omega

/-- Every one of the ten known solutions fails Beal, each because of an exponent `2`. -/
theorem fc_all_fail_beal {A B C : ℕ} :
    (¬ IsBealCounterexample A B C 7 3 2) ∧
    (¬ IsBealCounterexample A B C 5 2 4) ∧
    (¬ IsBealCounterexample A B C 3 2 9) ∧
    (¬ IsBealCounterexample A B C 7 3 2) ∧
    (¬ IsBealCounterexample A B C 5 4 2) ∧
    (¬ IsBealCounterexample A B C 7 3 2) ∧
    (¬ IsBealCounterexample A B C 3 2 7) ∧
    (¬ IsBealCounterexample A B C 3 2 7) ∧
    (¬ IsBealCounterexample A B C 8 3 2) ∧
    (¬ IsBealCounterexample A B C 8 2 3) :=
  ⟨not_counterexample_of_exponent_two (Or.inr (Or.inr rfl)),
   not_counterexample_of_exponent_two (Or.inr (Or.inl rfl)),
   not_counterexample_of_exponent_two (Or.inr (Or.inl rfl)),
   not_counterexample_of_exponent_two (Or.inr (Or.inr rfl)),
   not_counterexample_of_exponent_two (Or.inr (Or.inr rfl)),
   not_counterexample_of_exponent_two (Or.inr (Or.inr rfl)),
   not_counterexample_of_exponent_two (Or.inr (Or.inl rfl)),
   not_counterexample_of_exponent_two (Or.inr (Or.inl rfl)),
   not_counterexample_of_exponent_two (Or.inr (Or.inr rfl)),
   not_counterexample_of_exponent_two (Or.inr (Or.inl rfl))⟩

end Beal
