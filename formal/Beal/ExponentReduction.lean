/-
# Exponent Reduction for the Beal Conjecture

Every signature-by-signature attack on Beal tacitly restricts the exponents to
`{4} ∪ {odd primes}`.  The project's own discipline forbids restricting the exponent range
without proving the restriction covers every case.  This file supplies that proof.

No `sorry`, no custom `axiom`s.  The only imports are mathlib.
-/
import Beal.Conjecture
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.NumberTheory.FLT.Four
import Mathlib.Tactic.PushNeg
import Mathlib.Tactic.NormNum.Basic

namespace Beal

/-- The exponents that survive reduction: `4`, or an odd prime. -/
def Reduced (e : ℕ) : Prop := e = 4 ∨ (Nat.Prime e ∧ Odd e)

/-- Every exponent `e ≥ 3` factors as `e' * m` with `e'` reduced and `m ≥ 1`. -/
theorem exists_reduced_factor {e : ℕ} (he : 3 ≤ e) :
    ∃ e' m : ℕ, e = e' * m ∧ 0 < m ∧ Reduced e' := by
  by_cases hodd : ∃ p : ℕ, p.Prime ∧ Odd p ∧ p ∣ e
  · obtain ⟨p, hp, hpodd, hpdvd⟩ := hodd
    obtain ⟨m, hm⟩ := hpdvd
    refine ⟨p, m, hm, ?_, Or.inr ⟨hp, hpodd⟩⟩
    rcases Nat.eq_zero_or_pos m with rfl | h
    · simp [hm] at he
    · exact h
  · -- no odd prime divides `e`, so `e` is a power of two; `e ≥ 3` forces `4 ∣ e`
    push_neg at hodd
    have h2 : (4 : ℕ) ∣ e := by
      have he1 : e ≠ 1 := by omega
      -- the least prime factor of `e` cannot be odd, so it is 2
      have hmf : Nat.minFac e = 2 := by
        by_contra hne
        have hp : (Nat.minFac e).Prime := Nat.minFac_prime he1
        exact hodd _ hp (hp.odd_of_ne_two hne) (Nat.minFac_dvd e)
      have h2e : 2 ∣ e := hmf ▸ Nat.minFac_dvd e
      obtain ⟨t, ht⟩ := h2e
      have ht1 : t ≠ 1 := by omega
      -- `t` cannot be odd either, else its least prime factor is an odd prime dividing `e`
      have h2t : 2 ∣ t := by
        by_contra hnt
        have hp : (Nat.minFac t).Prime := Nat.minFac_prime ht1
        have hdvd : Nat.minFac t ∣ t := Nat.minFac_dvd t
        have hne2 : Nat.minFac t ≠ 2 := fun h => hnt (h ▸ hdvd)
        exact hodd _ hp (hp.odd_of_ne_two hne2) (hdvd.trans ⟨2, by omega⟩)
      obtain ⟨u, hu⟩ := h2t
      exact ⟨u, by omega⟩
    obtain ⟨m, hm⟩ := h2
    refine ⟨4, m, hm, ?_, Or.inl rfl⟩
    rcases Nat.eq_zero_or_pos m with rfl | h
    · simp [hm] at he
    · exact h

/-- **Primitivity is preserved by taking powers of the bases.**
This is the step that must not be waved through: a prime dividing `A ^ a` divides `A`. -/
theorem gcd_pow_eq_one {A B C a b c : ℕ}
    (h : gcd3 A B C = 1) :
    gcd3 (A ^ a) (B ^ b) (C ^ c) = 1 := by
  unfold gcd3 at h ⊢
  rw [Nat.eq_one_iff_not_exists_prime_dvd]
  rintro q hq hdvd
  have hqA : q ∣ A ^ a := hdvd.trans (Nat.gcd_dvd_left _ _)
  have hBC : q ∣ Nat.gcd (B ^ b) (C ^ c) := hdvd.trans (Nat.gcd_dvd_right _ _)
  have h1 : q ∣ A := hq.dvd_of_dvd_pow hqA
  have h2 : q ∣ B := hq.dvd_of_dvd_pow (hBC.trans (Nat.gcd_dvd_left _ _))
  have h3 : q ∣ C := hq.dvd_of_dvd_pow (hBC.trans (Nat.gcd_dvd_right _ _))
  have hg : q ∣ Nat.gcd A (Nat.gcd B C) := Nat.dvd_gcd h1 (Nat.dvd_gcd h2 h3)
  rw [h] at hg
  exact hq.one_lt.ne' (Nat.dvd_one.mp hg)

/-- **Exponent Reduction Theorem.**
If a Beal counterexample exists at all, then one exists whose three exponents each lie in
`{4} ∪ {odd primes}`.  Hence it suffices to refute those signatures. -/
theorem reduction {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    ∃ A' B' C' x' y' z' : ℕ,
      IsBealCounterexample A' B' C' x' y' z' ∧ Reduced x' ∧ Reduced y' ∧ Reduced z' := by
  obtain ⟨hA, hB, hC, hx, hy, hz, hgcd, heq⟩ := h
  obtain ⟨x', mx, hxe, hmx, hxr⟩ := exists_reduced_factor hx
  obtain ⟨y', my, hye, hmy, hyr⟩ := exists_reduced_factor hy
  obtain ⟨z', mz, hze, hmz, hzr⟩ := exists_reduced_factor hz
  refine ⟨A ^ mx, B ^ my, C ^ mz, x', y', z', ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩,
    hxr, hyr, hzr⟩
  · exact Nat.pos_pow_of_pos _ hA
  · exact Nat.pos_pow_of_pos _ hB
  · exact Nat.pos_pow_of_pos _ hC
  · rcases hxr with rfl | ⟨hp, hodd⟩
    · norm_num
    · have h2 := hp.two_le
      rw [Nat.odd_iff] at hodd
      omega
  · rcases hyr with rfl | ⟨hp, hodd⟩
    · norm_num
    · have h2 := hp.two_le
      rw [Nat.odd_iff] at hodd
      omega
  · rcases hzr with rfl | ⟨hp, hodd⟩
    · norm_num
    · have h2 := hp.two_le
      rw [Nat.odd_iff] at hodd
      omega
  · exact gcd_pow_eq_one hgcd
  · rw [← pow_mul, ← pow_mul, ← pow_mul, mul_comm mx x', mul_comm my y', mul_comm mz z',
      ← hxe, ← hye, ← hze]
    exact heq



/-! ## Kernel-verified consequences of mathlib's Fermat's Last Theorem for exponent 4 -/

section DiagonalFour

/-- **Beal holds for every diagonal signature `(n,n,n)` with `4 ∣ n`.**
Any such counterexample would give `(A^m)^4 + (B^m)^4 = (C^m)^4`, contradicting
mathlib's `fermatLastTheoremFour`.  This closes an infinite family of signatures. -/
theorem no_counterexample_diagonal_of_four_dvd {n : ℕ} (hn : 4 ∣ n)
    {A B C : ℕ} (h : IsBealCounterexample A B C n n n) : False := by
  obtain ⟨hA, hB, hC, hx, _, _, _, heq⟩ := h
  obtain ⟨m, hm⟩ := hn
  have hm0 : m ≠ 0 := by rintro rfl; omega
  have hA' : A ^ m ≠ 0 := pow_ne_zero _ (by omega)
  have hB' : B ^ m ≠ 0 := pow_ne_zero _ (by omega)
  have hC' : C ^ m ≠ 0 := pow_ne_zero _ (by omega)
  refine fermatLastTheoremFour (A ^ m) (B ^ m) (C ^ m) hA' hB' hC' ?_
  rw [← pow_mul, ← pow_mul, ← pow_mul, mul_comm m 4, ← hm]
  exact heq

/-- Concrete instance: no Beal counterexample of signature `(4,4,4)`. -/
theorem no_counterexample_4_4_4 {A B C : ℕ} (h : IsBealCounterexample A B C 4 4 4) : False :=
  no_counterexample_diagonal_of_four_dvd ⟨1, by norm_num⟩ h

/-- Concrete instance: no Beal counterexample of signature `(8,8,8)`. -/
theorem no_counterexample_8_8_8 {A B C : ℕ} (h : IsBealCounterexample A B C 8 8 8) : False :=
  no_counterexample_diagonal_of_four_dvd ⟨2, by norm_num⟩ h

end DiagonalFour

end Beal
