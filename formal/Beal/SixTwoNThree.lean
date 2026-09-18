/-
# Signature `(6, 2n, 3)` (U151): assembly relative to two named hypotheses

* `BennettSkinnerThree` (as in `EvenEvenThree.lean`), used only when the `2n` side is `3`-free and `n ≥ 4`.
* `Mordell27`: the rational points of `Y² = X³ + 27` are `O` and `(−3, 0)`
  (PARI/GP: conductor 144, torsion ℤ/2, 2-descent rank bound 0 — see `code/U151_mordell27.gp`).

The elliptic-curve step: if `s ≠ 0` and `3 v² = s⁶ − ε t³` then `(3T, 9V)` with `T = −ε t/s²`,
`V = v/s³` lies on the curve, so `V = 0`, so `v = 0`.
-/
import Beal.GaussianPow
import Beal.EvenEvenThree

open Zsqrtd

local notation "ℤ[i]" => GaussianInt

namespace Beal

/-- Named hypothesis: `Y² = X³ + 27` has only the rational points `O` and `(−3, 0)`. -/
def Mordell27 : Prop := ∀ X Y : ℚ, Y ^ 2 = X ^ 3 + 27 → X = -3 ∧ Y = 0

/-- **Curve step.** `3 v² = s⁶ − ε t³` with `s ≠ 0`, `ε = ±1` forces `v = 0`. -/
lemma curve_step (hM : Mordell27) {s t v : ℤ} (hs : s ≠ 0) {ε : ℤ} (hε : ε = 1 ∨ ε = -1)
    (h : 3 * v ^ 2 = s ^ 6 - ε * t ^ 3) : v = 0 := by
  have hsq : (s : ℚ) ≠ 0 := by exact_mod_cast hs
  set T : ℚ := -ε * t / (s : ℚ) ^ 2 with hT
  set V : ℚ := v / (s : ℚ) ^ 3 with hV
  have hε2 : (ε : ℚ) ^ 2 = 1 := by rcases hε with rfl | rfl <;> norm_num
  have hε3 : (ε : ℚ) ^ 3 = ε := by rcases hε with rfl | rfl <;> norm_num
  have hq : (3 : ℚ) * (v : ℚ) ^ 2 = (s : ℚ) ^ 6 - ε * (t : ℚ) ^ 3 := by exact_mod_cast h
  have hcurve : (9 * V) ^ 2 = (3 * T) ^ 3 + 27 := by
    rw [hT, hV]
    field_simp
    have : (-(ε : ℚ) * t) ^ 3 = -ε * t ^ 3 := by
      have : (-(ε : ℚ) * t) ^ 3 = -(ε ^ 3) * t ^ 3 := by ring
      rw [this, hε3]
    nlinarith [hq, this]
  obtain ⟨_, hY⟩ := hM _ _ hcurve
  have : (V : ℚ) = 0 := by linarith
  rw [hV] at this
  have hv : (v : ℚ) = 0 := by
    rcases div_eq_zero_iff.mp this with h0 | h0
    · exact h0
    · exact absurd h0 (pow_ne_zero 3 hsq)
  exact_mod_cast hv

/-- Helper: on a `3`-free side with exponent `3`, the parameter splits as `u = s³`,
`u² − 3v² = ε t³` and the curve step kills `v`. -/
lemma side_three (hM : Mordell27) {u v c : ℤ} (huv : IsCoprime u v) (h3 : ¬ (3 : ℤ) ∣ u)
    (hv : v ≠ 0) (hc : c ≠ 0)
    (h : u * (u ^ 2 - 3 * v ^ 2) = c ^ 3 ∨ u * (u ^ 2 - 3 * v ^ 2) = -(c ^ 3)) : False := by
  set w := u ^ 2 - 3 * v ^ 2 with hw
  have hcop : IsCoprime u w := isCoprime_u_cofactor huv h3
  have hodd : Odd 3 := by decide
  obtain ⟨c', hc', hprod⟩ : ∃ c' : ℤ, c' ≠ 0 ∧ u * w = c' ^ 3 := by
    rcases h with h | h
    · exact ⟨c, hc, h⟩
    · exact ⟨-c, neg_ne_zero.mpr hc, by rw [hodd.neg_pow, h]⟩
  have hu0 : u ≠ 0 := by
    intro h0; apply hc'; rw [h0, zero_mul] at hprod; exact pow_eq_zero_iff (by omega) |>.mp hprod.symm
  obtain ⟨s, hs⟩ := int_factor_pow hcop hprod
  obtain ⟨t, ht⟩ := int_factor_pow hcop.symm (by rw [mul_comm]; exact hprod)
  have hu2 : u ^ 2 = s ^ 6 := by rcases hs with hs | hs <;> rw [hs] <;> ring
  have hs0 : s ≠ 0 := by
    intro h0; apply hu0; rcases hs with hs | hs <;> rw [hs, h0] <;> simp
  -- `3 v² = s⁶ − ε t³`
  obtain ⟨ε, hε, heq⟩ : ∃ ε : ℤ, (ε = 1 ∨ ε = -1) ∧ 3 * v ^ 2 = s ^ 6 - ε * t ^ 3 := by
    rcases ht with ht | ht
    · exact ⟨1, Or.inl rfl, by linear_combination hw + hu2 - ht⟩
    · exact ⟨-1, Or.inr rfl, by linear_combination hw + hu2 - ht⟩
  exact hv (curve_step hM hs0 hε heq)

/-- **Main theorem.** No Beal counterexample of signature `(6, 2n, 3)` with `n ≥ 3`, relative to
Bennett–Skinner (odd `n ≥ 5`, `3`-free `Im` side), BCDY `(4, 2n, 3)` (even `n`) and `Mordell27`. -/
theorem no_counterexample_six_two_n_three (hBS : BennettSkinnerThree) (hBCDY : BCDYFourTwoNThree)
    (hM : Mordell27) {A B C n : ℕ} (hn : 3 ≤ n) (h : IsBealCounterexample A B C 6 (2 * n) 3) :
    False := by
  have h' : IsBealCounterexample A B C (2 * 3) (2 * n) 3 := h
  obtain ⟨w, hw, hcop⟩ := even_even_odd_reduction (by decide) h'
  have hab : Nat.Coprime A B := gcd_ab_eq_one h
  obtain ⟨hA, hB, hC, _, _, _, _, heq⟩ := h
  have hA0 : (A : ℤ) ≠ 0 := by exact_mod_cast hA.ne'
  have hB0 : (B : ℤ) ≠ 0 := by exact_mod_cast hB.ne'
  have hre : (A : ℤ) ^ 3 = w.re * (w.re ^ 2 - 3 * w.im ^ 2) := by
    have := congrArg Zsqrtd.re hw
    simp only [pow_succ, pow_zero, one_mul, Zsqrtd.mul_re, Zsqrtd.mul_im] at this
    linear_combination -this
  have him : (B : ℤ) ^ n = w.im * (3 * w.re ^ 2 - w.im ^ 2) := by
    have := congrArg Zsqrtd.im hw
    simp only [pow_succ, pow_zero, one_mul, Zsqrtd.mul_re, Zsqrtd.mul_im] at this
    linear_combination -this
  have hu0 : w.re ≠ 0 := by
    intro h0; apply pow_ne_zero 3 hA0; rw [hre, h0]; ring
  have hv0 : w.im ≠ 0 := by
    intro h0; apply pow_ne_zero n hB0; rw [him, h0]; ring
  by_cases h3u : (3 : ℤ) ∣ w.re
  · -- `3 ∤ v`: work on the `Im` side, exponent `n`
    have h3v : ¬ (3 : ℤ) ∣ w.im := by
      intro hd
      have := Int.isCoprime_iff_gcd_eq_one.mp hcop
      have hg := Int.dvd_gcd h3u hd
      rw [this] at hg
      exact absurd (Int.eq_one_of_dvd_one (by norm_num) hg) (by norm_num)
    have himv : w.im * (w.im ^ 2 - 3 * w.re ^ 2) = -((B : ℤ) ^ n) := by rw [him]; ring
    rcases Nat.even_or_odd n with ⟨k, hk⟩ | hnodd
    · -- even `n = 2k`, `k ≥ 2`: signature `(4, 6, 3)` after `B^{2n} = (B^k)^4`; BCDY
      refine hBCDY (B ^ k) A C 3 (by norm_num) (by positivity) hA hC (hab.symm.pow_left k) ?_
      have e : (B ^ k) ^ 4 = B ^ (2 * n) := by rw [← pow_mul]; congr 1; omega
      rw [e, add_comm]; exact heq
    · rcases Nat.lt_or_ge n 5 with hlt | hge
      · -- `n = 3`: the curve on the `Im` side
        have hn3 : n = 3 := by obtain ⟨j, hj⟩ := hnodd; omega
        subst hn3
        exact side_three hM hcop.symm h3v hu0 hB0 (Or.inr himv)
      · -- odd `n ≥ 5`: Bennett–Skinner on the `Im` side
        exact side_odd hBS hge hnodd hcop.symm h3v hu0 hB0 (Or.inr himv)
  · -- `3 ∤ u`: the curve on the `Re` side (exponent 3)
    exact side_three hM hcop h3u hv0 hA0 (Or.inl hre.symm)

end Beal

namespace Beal

/-- Swapping the two summands of a counterexample. -/
theorem swap_counterexample {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    IsBealCounterexample B A C y x z := by
  obtain ⟨hA, hB, hC, hx, hy, hz, hg, heq⟩ := h
  refine ⟨hB, hA, hC, hy, hx, hz, ?_, by rw [add_comm]; exact heq⟩
  unfold gcd3 at hg ⊢
  rw [← Nat.gcd_assoc, Nat.gcd_comm B A, Nat.gcd_assoc]; exact hg

/-- **All of `(2m, 2n, 3)`, `m, n ≥ 2`**, relative to the three named hypotheses. -/
theorem no_counterexample_even_even_three_all (hBS : BennettSkinnerThree)
    (hBCDY : BCDYFourTwoNThree) (hM : Mordell27) {A B C m n : ℕ} (hm : 2 ≤ m) (hn : 2 ≤ n)
    (h : IsBealCounterexample A B C (2 * m) (2 * n) 3) : False := by
  have hab : Nat.Coprime A B := gcd_ab_eq_one h
  rcases Nat.lt_or_ge m 4 with hm4 | hm4
  · rcases Nat.lt_or_ge n 4 with hn4 | hn4
    · -- both in {2, 3}
      interval_cases m <;> interval_cases n
      · obtain ⟨hA, hB, hC, _, _, _, _, heq⟩ := h
        exact hBCDY A B C 2 le_rfl hA hB hC hab (by simpa using heq)
      · obtain ⟨hA, hB, hC, _, _, _, _, heq⟩ := h
        exact hBCDY A B C 3 (by norm_num) hA hB hC hab (by simpa using heq)
      · obtain ⟨hA, hB, hC, _, _, _, _, heq⟩ := h
        exact hBCDY B A C 3 (by norm_num) hB hA hC hab.symm (by rw [add_comm]; simpa using heq)
      · exact no_counterexample_six_two_n_three hBS hBCDY hM le_rfl h
    · -- m ∈ {2,3}, n ≥ 4
      interval_cases m
      · obtain ⟨hA, hB, hC, _, _, _, _, heq⟩ := h
        exact hBCDY A B C n (by omega) hA hB hC hab (by simpa using heq)
      · exact no_counterexample_six_two_n_three hBS hBCDY hM (by omega) h
  · rcases Nat.lt_or_ge n 4 with hn4 | hn4
    · -- m ≥ 4, n ∈ {2,3}: swap
      have h' := swap_counterexample h
      interval_cases n
      · obtain ⟨hB, hA, hC, _, _, _, _, heq⟩ := h'
        exact hBCDY B A C m (by omega) hB hA hC hab.symm (by simpa using heq)
      · exact no_counterexample_six_two_n_three hBS hBCDY hM (by omega) h'
    · exact no_counterexample_even_even_three' hBS hBCDY hm4 hn4 h

end Beal
