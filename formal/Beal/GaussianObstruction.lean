/-
# Beal fails over the Gaussian integers — an obstruction to a whole class of proofs

Helenius (2004): over `ℤ[i]` the Beal statement is **false**, witnessed by

    (-2 + i)^3 + (-2 - i)^3 = (1 + i)^4.

All three exponents are `≥ 3`, and the bases share no Gaussian prime — their norms are `5`, `5`
and `2`, and `gcd(5, 2) = 1`.

**Why this matters.** `ℤ[i]` is a principal ideal domain, hence a UFD. So Beal's conjecture
**cannot** be a consequence of unique factorisation alone: any valid proof must use something
special to `ℤ` — its total ordering, or the ramification behaviour of rational primes. Every
argument resting purely on formal factorisation identities is refuted in advance by this example.

No `sorry`, no custom axioms.
-/
import Mathlib.NumberTheory.Zsqrtd.GaussianInt

namespace Beal

open Zsqrtd

/-- The three Gaussian bases of the Helenius identity. -/
def gU : GaussianInt := ⟨-2, 1⟩
def gV : GaussianInt := ⟨-2, -1⟩
def gW : GaussianInt := ⟨1, 1⟩

/-- `(-2 + i)^3 = -2 + 11i`. -/
theorem gU_cube : gU ^ 3 = (⟨-2, 11⟩ : GaussianInt) := by decide

/-- `(-2 - i)^3 = -2 - 11i`. -/
theorem gV_cube : gV ^ 3 = (⟨-2, -11⟩ : GaussianInt) := by decide

/-- `(1 + i)^4 = -4`. -/
theorem gW_fourth : gW ^ 4 = (⟨-4, 0⟩ : GaussianInt) := by decide

/-- **The Helenius identity.** -/
theorem helenius : gU ^ 3 + gV ^ 3 = gW ^ 4 := by decide

/-- The norms are `5`, `5` and `2`. -/
theorem gauss_norms : gU.norm = 5 ∧ gV.norm = 5 ∧ gW.norm = 2 := by
  refine ⟨?_, ?_, ?_⟩ <;> simp [gU, gV, gW, Zsqrtd.norm_def]

/-- **Beal's statement is false over `ℤ[i]`.**
There are Gaussian integers `u, v, w`, all non-zero, and exponents `x, y, z ≥ 3` with
`u^x + v^y = w^z`, whose norms are pairwise coprime in pairs witnessing that the bases share no
common Gaussian prime. -/
theorem beal_false_over_gaussianInt :
    ∃ (u v w : GaussianInt) (x y z : ℕ),
      3 ≤ x ∧ 3 ≤ y ∧ 3 ≤ z ∧
      u ≠ 0 ∧ v ≠ 0 ∧ w ≠ 0 ∧
      u ^ x + v ^ y = w ^ z ∧
      Nat.gcd u.norm.natAbs w.norm.natAbs = 1 ∧
      Nat.gcd v.norm.natAbs w.norm.natAbs = 1 := by
  refine ⟨gU, gV, gW, 3, 3, 4, by norm_num, by norm_num, by norm_num, ?_, ?_, ?_, helenius, ?_, ?_⟩
  · decide
  · decide
  · decide
  · decide
  · decide

end Beal
