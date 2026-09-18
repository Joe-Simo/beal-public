/-
# A machine-checked instance of the fixed-three-bases sieve (C080)

`3^x + 5^y = 7^z` has no solution in natural exponents at all: modulo 8 the left side is in
`{0, 2, 4, 6}` and the right side in `{1, 7}`. This is the single-modulus case of the covering sieve,
proved in the kernel as an exemplar of the certificates in `research/pool/evidence/`.
-/
import Beal.Conjecture
import Mathlib.Tactic.NormNum.Basic

namespace Beal

lemma three_pow_mod8 (k : ℕ) : 3 ^ k % 8 = 1 ∨ 3 ^ k % 8 = 3 := by
  induction k with
  | zero => left; norm_num
  | succ n ih => rw [pow_succ, Nat.mul_mod]; rcases ih with h | h <;> rw [h] <;> norm_num

lemma five_pow_mod8 (k : ℕ) : 5 ^ k % 8 = 1 ∨ 5 ^ k % 8 = 5 := by
  induction k with
  | zero => left; norm_num
  | succ n ih => rw [pow_succ, Nat.mul_mod]; rcases ih with h | h <;> rw [h] <;> norm_num

lemma seven_pow_mod8 (k : ℕ) : 7 ^ k % 8 = 1 ∨ 7 ^ k % 8 = 7 := by
  induction k with
  | zero => left; norm_num
  | succ n ih => rw [pow_succ, Nat.mul_mod]; rcases ih with h | h <;> rw [h] <;> norm_num

/-- No exponents at all satisfy `3^x + 5^y = 7^z`. -/
theorem no_solution_bases_3_5_7 (x y z : ℕ) : 3 ^ x + 5 ^ y ≠ 7 ^ z := by
  intro h
  have h8 : (3 ^ x + 5 ^ y) % 8 = 7 ^ z % 8 := by rw [h]
  rcases three_pow_mod8 x with a | a <;> rcases five_pow_mod8 y with b | b <;>
    rcases seven_pow_mod8 z with c | c <;> omega

/-- In particular there is no Beal counterexample with bases `(3, 5, 7)`, whatever the signature. -/
theorem no_counterexample_bases_3_5_7 (x y z : ℕ) : ¬ IsBealCounterexample 3 5 7 x y z := by
  rintro ⟨_, _, _, _, _, _, _, heq⟩
  exact no_solution_bases_3_5_7 x y z heq

end Beal
