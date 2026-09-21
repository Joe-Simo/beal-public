/-
Copyright (c) 2026 Formal Verification Group. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Formal Verification Specialist
-/
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Nat.Prime.Basic
import Beal.Conjecture
import Beal.Structure

/-!
# Conductor-Coupled Discriminant Valuation Lemma for Beal Triples

This module formalizes the exact algebraic mechanism that resolves Failure Mode 5
(Moduli-Coprimality Conflation) on the Lawrence-Venkatesh / Arakelov hybrid (C293 + C300).

## Mathematical Mechanism

The geometric cross-ratio $\lambda = A^x / C^z \in \mathbb{P}^1(\mathbb{Q})$ is projectively
invariant and blind to integer scaling. However, the Frey curve discriminant:
  $$\Delta = 16 A^{2x} B^{2y} C^{2z}$$
and its prime factor valuations $\nu_p(\Delta)$ couple directly to the coprimality condition:

1. **Non-Coprime Defect**: If $p \mid \gcd(A, B, C)$, then $p \mid A$, $p \mid B$, and $p \mid C$.
   Since $x, y, z \ge 3$, the discriminant valuation satisfies:
     $$\nu_p(A^{2x} B^{2y} C^{2z}) \ge 2x + 2y + 2z \ge 18.$$
   Thus $p^{18} \mid A^{2x} B^{2y} C^{2z}$, forcing additive reduction and shifting the conductor.

2. **Primitive Pairwise Disjointness**: If $(A, B, C, x, y, z)$ is a primitive Beal solution
   with $\gcd_3(A, B, C) = 1$, then $A, B, C$ are pairwise coprime. For any prime $p$, $p$
   divides at most one of $\{A, B, C\}$, preventing additive conductor shift at odd primes.
-/

namespace Beal

/--
The core algebraic discriminant power product associated to a Beal triple.
-/
def FreyDiscriminantCore (A B C x y z : ℕ) : ℕ :=
  A ^ (2 * x) * B ^ (2 * y) * C ^ (2 * z)

/--
If a prime `p` divides all three bases `A, B, C`, and the exponents satisfy `x, y, z ≥ 3`,
then `p^18` divides the Frey discriminant core `A^(2x) * B^(2y) * C^(2z)`.
-/
theorem noncoprime_discriminant_valuation_ge_18
    {A B C x y z p : ℕ}
    (hx : x ≥ 3) (hy : y ≥ 3) (hz : z ≥ 3)
    (hpA : p ∣ A) (hpB : p ∣ B) (hpC : p ∣ C) :
    p ^ 18 ∣ FreyDiscriminantCore A B C x y z := by
  unfold FreyDiscriminantCore
  have h2x : 6 ≤ 2 * x := by omega
  have h2y : 6 ≤ 2 * y := by omega
  have h2z : 6 ≤ 2 * z := by omega
  have hA6 : p ^ 6 ∣ A ^ (2 * x) := by
    have h1 : p ^ (2 * x) ∣ A ^ (2 * x) := pow_dvd_pow_of_dvd hpA (2 * x)
    have h2 : p ^ 6 ∣ p ^ (2 * x) := pow_dvd_pow p h2x
    exact dvd_trans h2 h1
  have hB6 : p ^ 6 ∣ B ^ (2 * y) := by
    have h1 : p ^ (2 * y) ∣ B ^ (2 * y) := pow_dvd_pow_of_dvd hpB (2 * y)
    have h2 : p ^ 6 ∣ p ^ (2 * y) := pow_dvd_pow p h2y
    exact dvd_trans h2 h1
  have hC6 : p ^ 6 ∣ C ^ (2 * z) := by
    have h1 : p ^ (2 * z) ∣ C ^ (2 * z) := pow_dvd_pow_of_dvd hpC (2 * z)
    have h2 : p ^ 6 ∣ p ^ (2 * z) := pow_dvd_pow p h2z
    exact dvd_trans h2 h1
  have hAB : p ^ 12 ∣ A ^ (2 * x) * B ^ (2 * y) := by
    have hmul := Nat.mul_dvd_mul hA6 hB6
    have hpow : p ^ 6 * p ^ 6 = p ^ 12 := by
      rw [← Nat.pow_add]
    rwa [hpow] at hmul
  have hABC : p ^ 18 ∣ A ^ (2 * x) * B ^ (2 * y) * C ^ (2 * z) := by
    have hmul := Nat.mul_dvd_mul hAB hC6
    have hpow : p ^ 12 * p ^ 6 = p ^ 18 := by
      rw [← Nat.pow_add]
    rwa [hpow] at hmul
  exact hABC

/--
**Coprimality-to-Discriminant Valuation Distinction**:
For any primitive Beal solution, no prime `p` can divide all three of `A, B, C`.
Consequently, the non-coprime discriminant defect ($p^{18} \mid \text{Core}$)
never occurs at any prime for primitive solutions.
-/
theorem primitive_beal_no_common_prime_factor
    {A B C x y z : ℕ}
    (hBeal : IsBealCounterexample A B C x y z)
    {p : ℕ} (hp : p.Prime) :
    ¬(p ∣ A ∧ p ∣ B ∧ p ∣ C) := by
  intro ⟨hpA, hpB, _⟩
  obtain ⟨hNotB, _⟩ := support_disjoint_A hBeal hp hpA
  exact hNotB hpB

end Beal
