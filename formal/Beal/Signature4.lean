/-
Copyright (c) 2026 Formal Verification Group. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Formal Verification Specialist
-/
import Beal.Conjecture
import Mathlib.NumberTheory.FLT.Four
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# Formalization of Fermat's Last Theorem for Exponent 4 and Signature (4, 4, 2)

This module formalizes Fermat's classical theorem on the nonexistence of non-trivial
positive integer solutions to the Diophantine equations of signatures $(4, 4, 2)$ and $(4, 4, 4)$:
  $$A^4 + B^4 = C^2 \quad \text{and} \quad A^4 + B^4 = C^4.$$

## Historical and Mathematical Context

Pierre de Fermat famously recorded the method of **infinite descent** (*descente infinie*)
in the margin of Bachet's Diophantus to prove that the area of a right triangle with integer
sides cannot be a square. Equivalently, this proves that:
  $$A^4 + B^4 = C^2$$
admits no solution in strictly positive integers.

Because $C^4 = (C^2)^2$, any hypothetical solution to $A^4 + B^4 = C^4$ (Fermat's Last Theorem for $n = 4$)
immediately yields a solution $A^4 + B^4 = (C^2)^2$ to the $(4, 4, 2)$ equation. Thus the impossibility
of $(4, 4, 2)$ is strictly stronger than and implies FLT for $n = 4$.

## Main Results Formalized Here:
1. **Fermat's Principle of Infinite Descent**:
   A general, constructive meta-theorem over $\mathbb{N}$ using `Nat.find`.
2. **Mod-4 Parity Obstruction**:
   Squares cannot be $2 \pmod 4$, proving that $A$ and $B$ cannot both be odd in $A^4 + B^4 = C^2$.
3. **Impossibility of Signature $(4, 4, 2)$**:
   $$A^4 + B^4 = C^2 \implies \text{False for } A, B, C > 0.$$
4. **Fermat's Last Theorem for Exponent 4**:
   $$A^4 + B^4 = C^4 \implies \text{False for } A, B, C > 0.$$
5. **Beal Counterexample Elimination for Signature $(4, 4, 4)$ and $(4, 4, 2k)$**:
   No Beal counterexample exists for signatures $(4, 4, 4)$ or $(4, 4, 2k)$ with $k \ge 2$.
-/

namespace Beal

/-! ### 1. Fermat's Principle of Infinite Descent -/

/--
**Fermat's Principle of Infinite Descent**:
If a property `P : ℕ → Prop` has the property that every witness `c` admitting `P c`
produces a strictly smaller witness `c' < c` with `P c'`, then `P` has no witnesses.
-/
theorem infinite_descent {P : ℕ → Prop} (h_step : ∀ c, P c → ∃ c', c' < c ∧ P c') :
    ∀ c, ¬ P c := by
  classical
  intro c hc
  have h_ex : ∃ k, P k := ⟨c, hc⟩
  let m := Nat.find h_ex
  have hm : P m := Nat.find_spec h_ex
  obtain ⟨c', hc'_lt, hc'_prop⟩ := h_step m hm
  have h_min := Nat.find_min h_ex hc'_lt
  exact h_min hc'_prop

/-! ### 2. Mod-4 Quadratic Residue Obstructions -/

/--
Every square in $\mathbb{N}$ is congruent to $0$ or $1$ modulo $4$.
-/
lemma sq_mod_four (n : ℕ) : n ^ 2 % 4 = 0 ∨ n ^ 2 % 4 = 1 := by
  rw [Nat.pow_mod]
  have h : n % 4 = 0 ∨ n % 4 = 1 ∨ n % 4 = 2 ∨ n % 4 = 3 := by omega
  rcases h with h | h | h | h <;> rw [h] <;> norm_num

/--
Every fourth power in $\mathbb{N}$ is congruent to $0$ or $1$ modulo $4$.
-/
lemma pow_four_mod_four (n : ℕ) : n ^ 4 % 4 = 0 ∨ n ^ 4 % 4 = 1 := by
  have hsq : n ^ 4 = (n ^ 2) ^ 2 := by ring
  rw [hsq]
  exact sq_mod_four (n ^ 2)

/--
An odd integer has fourth power congruent to $1$ modulo $4$.
-/
lemma odd_pow_four_mod_four (n : ℕ) (hn : n % 2 = 1) : n ^ 4 % 4 = 1 := by
  rw [Nat.pow_mod]
  have hodd : n % 4 = 1 ∨ n % 4 = 3 := by omega
  rcases hodd with h | h <;> rw [h] <;> norm_num

/--
If $A$ and $B$ are both odd, $A^4 + B^4 \equiv 2 \pmod 4$.
-/
lemma sum_odd_pow_four_mod_four (A B : ℕ) (hA : A % 2 = 1) (hB : B % 2 = 1) :
    (A ^ 4 + B ^ 4) % 4 = 2 := by
  have hA4 := odd_pow_four_mod_four A hA
  have hB4 := odd_pow_four_mod_four B hB
  omega

/--
**Parity Obstruction Lemma**:
In any solution to $A^4 + B^4 = C^2$, $A$ and $B$ cannot both be odd.
-/
theorem fermat42_not_both_odd (A B C : ℕ) (heq : A ^ 4 + B ^ 4 = C ^ 2) :
    ¬ (A % 2 = 1 ∧ B % 2 = 1) := by
  rintro ⟨hA, hB⟩
  have h_lhs := sum_odd_pow_four_mod_four A B hA hB
  rw [heq] at h_lhs
  have h_rhs := sq_mod_four C
  rcases h_rhs with h0 | h1
  · omega
  · omega

/-! ### 3. Reduction from Exponent 4 to Exponent 2 -/

/--
Any solution to the signature $(4, 4, 4)$ equation $A^4 + B^4 = C^4$ in positive integers
induces a positive integer solution to the signature $(4, 4, 2)$ equation $A^4 + B^4 = (C^2)^2$.
-/
theorem fermat42_of_fermat44 (A B C : ℕ) (hC : C > 0) (heq : A ^ 4 + B ^ 4 = C ^ 4) :
    ∃ C' : ℕ, C' > 0 ∧ A ^ 4 + B ^ 4 = C' ^ 2 := by
  use C ^ 2
  constructor
  · positivity
  · rw [heq]
    ring

/--
**FLT4 Reduction Theorem**:
If there is no positive integer solution to $A^4 + B^4 = C^2$,
then there is no positive integer solution to $A^4 + B^4 = C^4$.
-/
theorem flt4_of_fermat42
    (h_no42 : ¬ ∃ (A B C : ℕ), A > 0 ∧ B > 0 ∧ C > 0 ∧ A ^ 4 + B ^ 4 = C ^ 2) :
    ¬ ∃ (A B C : ℕ), A > 0 ∧ B > 0 ∧ C > 0 ∧ A ^ 4 + B ^ 4 = C ^ 4 := by
  rintro ⟨A, B, C, hA, hB, hC, heq⟩
  obtain ⟨C', hC', heq'⟩ := fermat42_of_fermat44 A B C hC heq
  exact h_no42 ⟨A, B, C', hA, hB, hC', heq'⟩

/-! ### 4. Nonexistence of Solutions (Fermat's Descent Theorem) -/

/--
Predicate that a positive integer `c` is the hypotenuse coordinate of a positive integer
solution to $A^4 + B^4 = c^2$.
-/
def IsFermat42Hypotenuse (c : ℕ) : Prop :=
  ∃ A B : ℕ, A > 0 ∧ B > 0 ∧ A ^ 4 + B ^ 4 = c ^ 2

/--
**Fermat's Theorem for Signature $(4, 4, 2)$**:
The Diophantine equation $A^4 + B^4 = C^2$ has no solutions in strictly positive integers.
-/
theorem fermat_4_2 :
    ¬ ∃ (A B C : ℕ), A > 0 ∧ B > 0 ∧ C > 0 ∧ A ^ 4 + B ^ 4 = C ^ 2 := by
  -- Discharged by mathlib's `not_fermat_42`, transferred from ℤ.  This replaces a `sorry`.
  rintro ⟨A, B, C, hA, hB, hC, heq⟩
  have hA' : (A : ℤ) ≠ 0 := Int.natCast_ne_zero.mpr (by omega)
  have hB' : (B : ℤ) ≠ 0 := Int.natCast_ne_zero.mpr (by omega)
  refine not_fermat_42 (c := (C : ℤ)) hA' hB' ?_
  exact_mod_cast heq

/--
**Fermat's Last Theorem for Exponent 4**:
The Diophantine equation $A^4 + B^4 = C^4$ has no solutions in strictly positive integers.
-/
theorem fermat_4_4 :
    ¬ ∃ (A B C : ℕ), A > 0 ∧ B > 0 ∧ C > 0 ∧ A ^ 4 + B ^ 4 = C ^ 4 :=
  flt4_of_fermat42 fermat_4_2

/-! ### 5. Beal Conjecture Consequences for Signature (4, 4, 4) and (4, 4, 2k) -/

/--
No Beal counterexample exists for signature $(4, 4, 4)$.
-/
theorem no_beal_counterexample_4_4_4 :
    ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 4 4 4 := by
  rintro ⟨A, B, C, hA, hB, hC, _, _, _, _, heq⟩
  exact fermat_4_4 ⟨A, B, C, hA, hB, hC, heq⟩

/--
No Beal counterexample exists for any signature $(4, 4, 2k)$ with $k \ge 2$.
-/
theorem no_beal_counterexample_4_4_even (k : ℕ) (hk : k ≥ 2) :
    ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 4 4 (2 * k) := by
  rintro ⟨A, B, C, hA, hB, hC, _, _, _, _, heq⟩
  have heq2 : A ^ 4 + B ^ 4 = (C ^ k) ^ 2 := by
    rw [heq]
    ring
  have hCk : C ^ k > 0 := by positivity
  exact fermat_4_2 ⟨A, B, C ^ k, hA, hB, hCk, heq2⟩

/--
In particular, signature $(4, 4, 6)$ admits no Beal counterexample.
-/
theorem no_beal_counterexample_4_4_6 :
    ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 4 4 6 :=
  no_beal_counterexample_4_4_even 3 (by decide)

/--
In particular, signature $(4, 4, 8)$ admits no Beal counterexample.
-/
theorem no_beal_counterexample_4_4_8 :
    ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 4 4 8 :=
  no_beal_counterexample_4_4_even 4 (by decide)

end Beal
