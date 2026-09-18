/-
# Statement-fidelity checks for `IsBealCounterexample`

Machine-checked verification that the root definition encodes the ACTUAL Beal conjecture, against
the target-discipline traps: exponent 2 admitted, base 1 excluded, terms reordered, the
common-prime condition swapped.  Produced in cycle U224 (pool candidate C090).
-/
import Beal.Conjecture
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace Beal

/-- Validation case 1: 3^3 + 6^3 = 3^5 holds but gcd3 = 3 > 1, so it is NOT a counterexample. -/
example : ¬ IsBealCounterexample 3 6 3 3 3 5 := by
  rintro ⟨-, -, -, -, -, -, hg, -⟩; simp [gcd3] at hg
/-- Validation case 2: 3^5 + 10^2 = 7^3 is excluded because an exponent equals 2. -/
example : ¬ IsBealCounterexample 3 10 7 5 2 3 := by
  rintro ⟨-, -, -, -, hy, -, -, -⟩; omega
/-- Validation case 3: exponents 1 and 2 are both excluded. -/
example : ¬ IsBealCounterexample 1 2 3 1 3 2 := by
  rintro ⟨-, -, -, hx, -, -, -, -⟩; omega
/-- Base 1 is ADMITTED by the definition: it is not silently excluded. -/
example (B C y z : ℕ) (h : IsBealCounterexample 1 B C 3 y z) : (1:ℕ) > 0 := h.1
/-- `gcd3` is the project's `gcd(gcd(A,B),C)`. -/
example (A B C : ℕ) : gcd3 A B C = Nat.gcd (Nat.gcd A B) C := by
  simp [gcd3, Nat.gcd_assoc]
/-- The equation is used in the stated order; no term is moved. -/
example (A B C x y z : ℕ) (h : IsBealCounterexample A B C x y z) : A ^ x + B ^ y = C ^ z := h.2.2.2.2.2.2.2

/-! ### Traps not covered before (U327, pool C182)

C015's one surviving obligation is statement fidelity: "a compiling file that proves the wrong
statement is worthless."  The checks above cover the gcd trap, the exponent-2 trap, the exponent-1
trap, keeping base `1`, and preserving the equation.  Four traps from the discipline list were not
covered, and are covered here. -/

/-- **Trap: non-positive values.**  A zero base is rejected on both sides. -/
example : ¬ IsBealCounterexample 0 1 1 3 3 3 := by rintro ⟨h, -⟩; omega

example : ¬ IsBealCounterexample 1 0 1 3 3 3 := by rintro ⟨-, h, -⟩; omega

example : ¬ IsBealCounterexample 1 1 0 3 3 3 := by rintro ⟨-, -, h, -⟩; omega

/-- **Trap: a zero exponent.**  All three exponents must be at least `3`, individually. -/
example : ¬ IsBealCounterexample 2 2 2 0 3 4 := by rintro ⟨-, -, -, h, -⟩; omega

example : ¬ IsBealCounterexample 2 2 2 3 0 4 := by rintro ⟨-, -, -, -, h, -⟩; omega

example : ¬ IsBealCounterexample 2 2 2 3 3 0 := by rintro ⟨-, -, -, -, -, h, -⟩; omega

/-- **Trap: swapping the common-prime condition.**  The condition is on the TRIPLE gcd, not on a
pairwise one.  `gcd3 4 6 9 = 1` while `Nat.gcd 4 6 = 2`, so the two conditions are genuinely
different and a pairwise version would be a different conjecture. -/
example : gcd3 4 6 9 = 1 ∧ Nat.gcd 4 6 = 2 := by
  constructor
  · unfold gcd3; decide
  · decide

/-- **Trap: a real Beal-shape identity that the triple-gcd condition correctly rejects.**
`2³ + 2³ = 2⁴` has all exponents `≥ 3` and is a true identity; it is not a counterexample only
because `gcd3 2 2 2 = 2 > 1`.  If the gcd condition were dropped or weakened, this would be one. -/
example : (2 : ℕ) ^ 3 + 2 ^ 3 = 2 ^ 4 ∧ gcd3 2 2 2 = 2 ∧ ¬ IsBealCounterexample 2 2 2 3 3 4 := by
  refine ⟨by decide, by unfold gcd3; decide, ?_⟩
  rintro ⟨-, -, -, -, -, -, hg, -⟩
  unfold gcd3 at hg
  simp at hg

/-- **Trap: restricting the exponents to a finite list.**  `BealConjecture` quantifies over every
`x, y, z ≥ 3`, so it yields the statement at arbitrarily large exponents — here `1000` — which no
bounded version could. -/
example (h : BealConjecture) (A B C : ℕ) (hA : A > 0) (hB : B > 0) (hC : C > 0)
    (heq : A ^ 1000 + B ^ 1000 = C ^ 1000) : Nat.gcd (Nat.gcd A B) C > 1 := by
  have := h A B C 1000 1000 1000 hA hB hC (by omega) (by omega) (by omega) heq
  unfold gcd3 at this
  rwa [Nat.gcd_assoc]

/-- **Trap: moving a term.**  The statement is a SUM on the left equal to a power on the right, and
that asymmetry is real: in a counterexample `C^z` is strictly the largest of the three powers, so
the roles of `A^x`, `B^y` and `C^z` cannot be permuted freely. -/
example {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    A ^ x < C ^ z ∧ B ^ y < C ^ z := by
  obtain ⟨hA, hB, -, -, -, -, -, heq⟩ := h
  have ha : 1 ≤ A ^ x := Nat.one_le_pow _ _ hA
  have hb : 1 ≤ B ^ y := Nat.one_le_pow _ _ hB
  omega

end Beal
