/-
# Signature `(4, 2n, 5)` (U154): assembly relative to two rank-0 curves

Only the exponent-4 side is used. With `(A², Bⁿ)` the coordinates of `w⁵ ∈ ℤ[i]` (kernel theorem
`even_even_odd_reduction`), `A² = u·Q`, `Q = u⁴ − 10u²v² + 5v⁴`, and `gcd(u, Q) ∣ 5`. Four branches:
* `5 ∤ u`, `u = s²`, `Q = t²`  → point `(v/s², t/s⁴)` on `C1 : W² = 5V⁴ − 10V² + 1`  (hyp. `Quartic400g2`);
* `5 ∤ u`, `u = −s²`, `Q = −t²` → impossible mod 16 (opposite parity of `s, v`);
* `5 ∣ u`, `u = 5s²`, `Q' = t²`  → point `(5s²/v, 5t/v²)` on `C3 : W² = 5(U⁴ − 10U² + 5)` (hyp. `Quartic400b2`);
* `5 ∣ u`, `u = −5s²`, `Q' = −t²` → impossible mod 16.
`C1`, `C3` have Jacobians LMFDB 400.g2 and 400.b2, both rank 0 with torsion ℤ/2, so each quartic has
exactly the two visible rational points; that is the content of the two named hypotheses.
-/
import Beal.GaussianPow
import Beal.EvenEvenThree
import Beal.SixTwoNThree

open Zsqrtd

local notation "ℤ[i]" => GaussianInt

namespace Beal

/-- Named hypothesis (LMFDB 400.g2, rank 0, torsion ℤ/2, so `C1(ℚ) = {(0, ±1)}`); only the
consequence used is stated: every rational point of `C1` has `V = 0`. -/
def Quartic400g2 : Prop := ∀ V W : ℚ, W ^ 2 = 5 * V ^ 4 - 10 * V ^ 2 + 1 → V = 0

/-- Named hypothesis (LMFDB 400.b2, rank 0, torsion ℤ/2, so `C3(ℚ) = {(0, ±5)}`); only the
consequence used is stated: every rational point of `C3` has `U = 0`. -/
def Quartic400b2 : Prop := ∀ U W : ℚ, W ^ 2 = 5 * (U ^ 4 - 10 * U ^ 2 + 5) → U = 0

/-! ### Two congruence obstructions, decided in `ZMod 16` -/

lemma sq_zmod16 : ∀ w : ZMod 16, w ^ 2 ∈ ({0, 1, 4, 9} : Finset (ZMod 16)) := by decide

lemma obsA1 : ∀ j l : ZMod 16,
    -((j + j) ^ 8 - 10 * (j + j) ^ 4 * (2 * l + 1) ^ 2 + 5 * (2 * l + 1) ^ 4) ∉
      ({0, 1, 4, 9} : Finset (ZMod 16)) := by decide
lemma obsA2 : ∀ j l : ZMod 16,
    -((2 * j + 1) ^ 8 - 10 * (2 * j + 1) ^ 4 * (l + l) ^ 2 + 5 * (l + l) ^ 4) ∉
      ({0, 1, 4, 9} : Finset (ZMod 16)) := by decide
lemma obsB1 : ∀ j l : ZMod 16,
    -(125 * (j + j) ^ 8 - 50 * (j + j) ^ 4 * (2 * l + 1) ^ 2 + (2 * l + 1) ^ 4) ∉
      ({0, 1, 4, 9} : Finset (ZMod 16)) := by decide
lemma obsB2 : ∀ j l : ZMod 16,
    -(125 * (2 * j + 1) ^ 8 - 50 * (2 * j + 1) ^ 4 * (l + l) ^ 2 + (l + l) ^ 4) ∉
      ({0, 1, 4, 9} : Finset (ZMod 16)) := by decide

/-- `t² = −(s⁸ − 10s⁴v² + 5v⁴)` is impossible for `s + v` odd. -/
lemma no_sq_A {s v t : ℤ} (hpar : Odd (s + v)) :
    t ^ 2 ≠ -(s ^ 8 - 10 * s ^ 4 * v ^ 2 + 5 * v ^ 4) := by
  intro h
  have h16 := congrArg (Int.cast : ℤ → ZMod 16) h
  push_cast at h16
  have hsq := sq_zmod16 (t : ZMod 16)
  rw [h16] at hsq
  rcases Int.even_or_odd s with ⟨j, hj⟩ | ⟨j, hj⟩
  · have hv : Odd v := by
      rcases Int.even_or_odd v with hv | hv
      · exact absurd hpar (by rw [Int.not_odd_iff_even]; exact Even.add ⟨j, hj⟩ hv)
      · exact hv
    obtain ⟨l, hl⟩ := hv
    subst hj hl; push_cast at hsq
    exact obsA1 (j : ZMod 16) (l : ZMod 16) hsq
  · have hv : Even v := by
      rcases Int.even_or_odd v with hv | hv
      · exact hv
      · exact absurd hpar (by rw [Int.not_odd_iff_even]; exact Odd.add_odd ⟨j, hj⟩ hv)
    obtain ⟨l, hl⟩ := hv
    subst hj hl; push_cast at hsq
    exact obsA2 (j : ZMod 16) (l : ZMod 16) hsq

/-- `t² = −(125s⁸ − 50s⁴v² + v⁴)` is impossible for `s + v` odd. -/
lemma no_sq_B {s v t : ℤ} (hpar : Odd (s + v)) :
    t ^ 2 ≠ -(125 * s ^ 8 - 50 * s ^ 4 * v ^ 2 + v ^ 4) := by
  intro h
  have h16 := congrArg (Int.cast : ℤ → ZMod 16) h
  push_cast at h16
  have hsq := sq_zmod16 (t : ZMod 16)
  rw [h16] at hsq
  rcases Int.even_or_odd s with ⟨j, hj⟩ | ⟨j, hj⟩
  · have hv : Odd v := by
      rcases Int.even_or_odd v with hv | hv
      · exact absurd hpar (by rw [Int.not_odd_iff_even]; exact Even.add ⟨j, hj⟩ hv)
      · exact hv
    obtain ⟨l, hl⟩ := hv
    subst hj hl; push_cast at hsq
    exact obsB1 (j : ZMod 16) (l : ZMod 16) hsq
  · have hv : Even v := by
      rcases Int.even_or_odd v with hv | hv
      · exact hv
      · exact absurd hpar (by rw [Int.not_odd_iff_even]; exact Odd.add_odd ⟨j, hj⟩ hv)
    obtain ⟨l, hl⟩ := hv
    subst hj hl; push_cast at hsq
    exact obsB2 (j : ZMod 16) (l : ZMod 16) hsq

lemma zmod2_re : ∀ j l : ZMod 2,
    (2 * j + 1) * ((2 * j + 1) ^ 4 - 10 * (2 * j + 1) ^ 2 * (2 * l + 1) ^ 2 + 5 * (2 * l + 1) ^ 4) = 0 := by
  decide
lemma zmod2_im : ∀ j l : ZMod 2,
    (2 * l + 1) * (5 * (2 * j + 1) ^ 4 - 10 * (2 * j + 1) ^ 2 * (2 * l + 1) ^ 2 + (2 * l + 1) ^ 4) = 0 := by
  decide

/-! ### The exponent-4 side -/

/-- **Core.** If `u·(u⁴ − 10u²v² + 5v⁴) = c²` with `gcd(u,v) = 1`, `u + v` odd, `c ≠ 0`, then `v = 0`. -/
theorem re_fifth_not_square (h1 : Quartic400g2) (h3 : Quartic400b2)
    {u v c : ℤ} (huv : IsCoprime u v) (hpar : Odd (u + v)) (hc : c ≠ 0)
    (h : u * (u ^ 4 - 10 * u ^ 2 * v ^ 2 + 5 * v ^ 4) = c ^ 2) : v = 0 := by
  by_contra hv
  obtain ⟨Q, hQ⟩ : ∃ Q : ℤ, Q = u ^ 4 - 10 * u ^ 2 * v ^ 2 + 5 * v ^ 4 := ⟨_, rfl⟩
  rw [← hQ] at h
  have hu0 : u ≠ 0 := by
    intro h0; apply hc; rw [h0, zero_mul] at h; exact pow_eq_zero_iff two_ne_zero |>.mp h.symm
  have hQ0 : Q ≠ 0 := by
    intro h0; apply hc; rw [h0, mul_zero] at h; exact pow_eq_zero_iff two_ne_zero |>.mp h.symm
  have hpos : 0 < u * Q := by rw [h]; positivity
  by_cases h5 : (5 : ℤ) ∣ u
  · -- `u = 5u'`, `Q = 5Q'`, `u'·Q' = (c/5)²`
    obtain ⟨u', rfl⟩ := h5
    obtain ⟨Q', hQ'def⟩ : ∃ Q' : ℤ, Q' = 125 * u' ^ 4 - 50 * u' ^ 2 * v ^ 2 + v ^ 4 := ⟨_, rfl⟩
    have hQ' : Q = 5 * Q' := by rw [hQ, hQ'def]; ring
    have h25 : (25 : ℤ) ∣ c ^ 2 := ⟨u' * Q', by rw [← h, hQ']; ring⟩
    have h5c : (5 : ℤ) ∣ c := by
      have : (5 : ℤ) ∣ c ^ 2 := (Dvd.intro _ (by norm_num : (5 : ℤ) * 5 = 25)).trans h25
      exact (Int.prime_iff_natAbs_prime.mpr Nat.prime_five : Prime (5 : ℤ)).dvd_of_dvd_pow this
    obtain ⟨c', rfl⟩ := h5c
    have hprod : u' * Q' = c' ^ 2 := by
      have h25' : (25 : ℤ) * (u' * Q') = 25 * c' ^ 2 := by
        rw [hQ'] at h; linear_combination h
      exact mul_left_cancel₀ (by norm_num) h25'
    have hc' : c' ≠ 0 := by rintro rfl; simp at hc
    -- `gcd(u', Q') = 1` since `Q' ≡ v⁴ (mod u')` and `gcd(u', v) = 1`
    have huv' : IsCoprime u' v := huv.of_mul_left_right
    have hcop : IsCoprime u' Q' := by
      have h1' : IsCoprime u' (v ^ 4) := huv'.pow_right
      have h2' : IsCoprime u' (v ^ 4 + u' * (125 * u' ^ 3 - 50 * u' * v ^ 2)) :=
        h1'.add_mul_left_right _
      have : v ^ 4 + u' * (125 * u' ^ 3 - 50 * u' * v ^ 2) = Q' := by rw [hQ'def]; ring
      rwa [this] at h2'
    obtain ⟨s, hs⟩ := int_factor_pow hcop hprod
    obtain ⟨t, ht⟩ := int_factor_pow hcop.symm (by rw [mul_comm]; exact hprod)
    have hpar' : Odd (u' + v) := by
      -- `5u' + v` odd ⟹ `u' + v` odd
      rcases Int.even_or_odd u' with ⟨j, hj⟩ | hu'
      · have : Even (5 * u') := ⟨5 * j, by rw [hj]; ring⟩
        have hv' : Odd v := by
          rcases Int.even_or_odd v with hv' | hv'
          · exact absurd hpar (by rw [Int.not_odd_iff_even]; exact this.add hv')
          · exact hv'
        exact Even.add_odd ⟨j, hj⟩ hv'
      · have : Odd (5 * u') := by obtain ⟨j, hj⟩ := hu'; exact ⟨5 * j + 2, by rw [hj]; ring⟩
        have hv' : Even v := by
          rcases Int.even_or_odd v with hv' | hv'
          · exact hv'
          · exact absurd hpar (by rw [Int.not_odd_iff_even]; exact Odd.add_odd this hv')
        exact Odd.add_even hu' hv'
    rcases hs with hs | hs <;> rcases ht with ht | ht
    · -- `u' = s²`, `Q' = t²`: point on `C3`
      have hs0 : s ≠ 0 := by rintro rfl; simp at hs; exact hu0 (by rw [hs]; ring)
      have hvq : (v : ℚ) ≠ 0 := by exact_mod_cast hv
      have hkey : (5 * (t : ℚ) / (v : ℚ) ^ 2) ^ 2 =
          5 * ((5 * (s : ℚ) ^ 2 / v) ^ 4 - 10 * (5 * (s : ℚ) ^ 2 / v) ^ 2 + 5) := by
        have hQ'q : (125 : ℚ) * (s : ℚ) ^ 8 - 50 * (s : ℚ) ^ 4 * (v : ℚ) ^ 2 + (v : ℚ) ^ 4 = (t : ℚ) ^ 2 := by
          rw [hs] at hQ'def
          exact_mod_cast (by linear_combination ht - hQ'def : (125 : ℤ) * s ^ 8 - 50 * s ^ 4 * v ^ 2 + v ^ 4 = t ^ 2)
        rw [div_pow, mul_pow, div_pow, div_pow, ← hQ'q]
        field_simp
        ring
      have := h3 _ _ hkey
      rcases div_eq_zero_iff.mp this with h0 | h0
      · exact hs0 (by
          have : (s : ℚ) ^ 2 = 0 := by linarith
          exact_mod_cast pow_eq_zero_iff two_ne_zero |>.mp this)
      · exact hvq h0
    · -- `u' = s²`, `Q' = −t²`: product negative
      exfalso
      have : u' * Q' = -(s ^ 2 * t ^ 2) := by rw [hs, ht]; ring
      rw [this] at hprod
      have : (0 : ℤ) < c' ^ 2 := by positivity
      nlinarith [sq_nonneg (s * t)]
    · exfalso
      have : u' * Q' = -(s ^ 2 * t ^ 2) := by rw [hs, ht]; ring
      rw [this] at hprod
      have : (0 : ℤ) < c' ^ 2 := by positivity
      nlinarith [sq_nonneg (s * t)]
    · -- `u' = −s²`, `Q' = −t²`: mod 16
      have hpar2 : Odd (s + v) := by
        -- `u' = −s²` has the parity of `s`
        rcases Int.even_or_odd s with ⟨j, hj⟩ | ⟨j, hj⟩
        · have : Even u' := ⟨-(2 * j * j), by rw [hs, hj]; ring⟩
          have hv' : Odd v := by
            rcases Int.even_or_odd v with hv' | hv'
            · exact absurd hpar' (by rw [Int.not_odd_iff_even]; exact this.add hv')
            · exact hv'
          exact Even.add_odd ⟨j, hj⟩ hv'
        · have : Odd u' := ⟨-(2 * j * j + 2 * j + 1), by rw [hs, hj]; ring⟩
          have hv' : Even v := by
            rcases Int.even_or_odd v with hv' | hv'
            · exact hv'
            · exact absurd hpar' (by rw [Int.not_odd_iff_even]; exact Odd.add_odd this hv')
          exact Odd.add_even ⟨j, hj⟩ hv'
      apply no_sq_B hpar2 (t := t)
      rw [hs] at hQ'def
      linear_combination ht - hQ'def
  · -- `5 ∤ u`: `gcd(u, Q) = 1`
    have hcop : IsCoprime u Q := by
      have hp5 : Prime (5 : ℤ) := Int.prime_iff_natAbs_prime.mpr Nat.prime_five
      have h5' : IsCoprime u 5 := ((hp5.irreducible.coprime_iff_not_dvd).mpr h5).symm
      have h1' : IsCoprime u (5 * v ^ 4) := h5'.mul_right huv.pow_right
      have h2' : IsCoprime u (5 * v ^ 4 + u * (u ^ 3 - 10 * u * v ^ 2)) := h1'.add_mul_left_right _
      have : 5 * v ^ 4 + u * (u ^ 3 - 10 * u * v ^ 2) = Q := by rw [hQ]; ring
      rwa [this] at h2'
    obtain ⟨s, hs⟩ := int_factor_pow hcop h
    obtain ⟨t, ht⟩ := int_factor_pow hcop.symm (by rw [mul_comm]; exact h)
    rcases hs with hs | hs <;> rcases ht with ht | ht
    · -- `u = s²`, `Q = t²`: point on `C1`
      have hs0 : s ≠ 0 := by rintro rfl; simp at hs; exact hu0 hs
      have hsq : (s : ℚ) ≠ 0 := by exact_mod_cast hs0
      have hkey : ((t : ℚ) / (s : ℚ) ^ 4) ^ 2 =
          5 * ((v : ℚ) / (s : ℚ) ^ 2) ^ 4 - 10 * ((v : ℚ) / (s : ℚ) ^ 2) ^ 2 + 1 := by
        have hQq : (s : ℚ) ^ 8 - 10 * (s : ℚ) ^ 4 * (v : ℚ) ^ 2 + 5 * (v : ℚ) ^ 4 = (t : ℚ) ^ 2 := by
          rw [hs] at hQ
          exact_mod_cast (by linear_combination ht - hQ : (s : ℤ) ^ 8 - 10 * s ^ 4 * v ^ 2 + 5 * v ^ 4 = t ^ 2)
        rw [div_pow, div_pow, div_pow, ← hQq]
        field_simp
        ring
      have := h1 _ _ hkey
      rcases div_eq_zero_iff.mp this with h0 | h0
      · exact hv (by exact_mod_cast h0)
      · exact hsq (pow_eq_zero_iff two_ne_zero |>.mp h0)
    · exfalso
      have : u * Q = -(s ^ 2 * t ^ 2) := by rw [hs, ht]; ring
      rw [this] at hpos; nlinarith [sq_nonneg (s * t)]
    · exfalso
      have : u * Q = -(s ^ 2 * t ^ 2) := by rw [hs, ht]; ring
      rw [this] at hpos; nlinarith [sq_nonneg (s * t)]
    · -- `u = −s²`, `Q = −t²`: mod 16
      have hpar2 : Odd (s + v) := by
        rcases Int.even_or_odd s with ⟨j, hj⟩ | ⟨j, hj⟩
        · have : Even u := ⟨-(2 * j * j), by rw [hs, hj]; ring⟩
          have hv' : Odd v := by
            rcases Int.even_or_odd v with hv' | hv'
            · exact absurd hpar (by rw [Int.not_odd_iff_even]; exact this.add hv')
            · exact hv'
          exact Even.add_odd ⟨j, hj⟩ hv'
        · have : Odd u := ⟨-(2 * j * j + 2 * j + 1), by rw [hs, hj]; ring⟩
          have hv' : Even v := by
            rcases Int.even_or_odd v with hv' | hv'
            · exact hv'
            · exact absurd hpar (by rw [Int.not_odd_iff_even]; exact Odd.add_odd this hv')
          exact Odd.add_even ⟨j, hj⟩ hv'
      apply no_sq_A hpar2 (t := t)
      rw [hs] at hQ
      linear_combination ht - hQ

/-- **Main theorem.** No Beal counterexample of signature `(4, 2n, 5)`, `n ≥ 2`. -/
theorem no_counterexample_four_two_n_five (h1 : Quartic400g2) (h3 : Quartic400b2)
    {A B C n : ℕ} (hn : 2 ≤ n) (h : IsBealCounterexample A B C 4 (2 * n) 5) : False := by
  have h' : IsBealCounterexample A B C (2 * 2) (2 * n) 5 := h
  obtain ⟨w, hw, hcop⟩ := even_even_odd_reduction (by decide) h'
  have hab : Nat.Coprime A B := gcd_ab_eq_one h
  obtain ⟨hA, hB, hC, _, _, _, _, _⟩ := h
  have hA0 : (A : ℤ) ≠ 0 := by exact_mod_cast hA.ne'
  have hB0 : (B : ℤ) ≠ 0 := by exact_mod_cast hB.ne'
  have hre : (A : ℤ) ^ 2 = w.re * (w.re ^ 4 - 10 * w.re ^ 2 * w.im ^ 2 + 5 * w.im ^ 4) := by
    have := congrArg Zsqrtd.re hw
    simp only [pow_succ, pow_zero, one_mul, Zsqrtd.mul_re, Zsqrtd.mul_im] at this
    linear_combination -this
  have him : (B : ℤ) ^ n = w.im * (5 * w.re ^ 4 - 10 * w.re ^ 2 * w.im ^ 2 + w.im ^ 4) := by
    have := congrArg Zsqrtd.im hw
    simp only [pow_succ, pow_zero, one_mul, Zsqrtd.mul_re, Zsqrtd.mul_im] at this
    linear_combination -this
  have hv0 : w.im ≠ 0 := by
    intro h0; apply pow_ne_zero n hB0; rw [him, h0]; ring
  -- opposite parity of `u, v`
  have hpar : Odd (w.re + w.im) := by
    rcases Int.even_or_odd w.re with ⟨j, hj⟩ | hu <;> rcases Int.even_or_odd w.im with ⟨l, hl⟩ | hv
    · -- both even contradicts coprimality
      exfalso
      have := Int.isCoprime_iff_gcd_eq_one.mp hcop
      have h2 : (2 : ℤ) ∣ Int.gcd w.re w.im := Int.dvd_gcd ⟨j, by omega⟩ ⟨l, by omega⟩
      rw [this] at h2; norm_num at h2
    · exact Even.add_odd ⟨j, hj⟩ hv
    · exact Odd.add_even hu ⟨l, hl⟩
    · -- both odd: then `A²` and `Bⁿ` are both even, contradicting `gcd(A, B) = 1`
      exfalso
      obtain ⟨j, hj⟩ := hu; obtain ⟨l, hl⟩ := hv
      have hA' : 2 ∣ A := by
        have h2 := congrArg (Int.cast : ℤ → ZMod 2) hre
        rw [hj, hl] at h2; push_cast at h2
        have : (A : ZMod 2) ^ 2 = 0 := by rw [h2]; exact zmod2_re (j : ZMod 2) (l : ZMod 2)
        have h0 : (A : ZMod 2) = 0 := pow_eq_zero_iff two_ne_zero |>.mp this
        exact (ZMod.natCast_zmod_eq_zero_iff_dvd A 2).mp h0
      have hB' : 2 ∣ B := by
        have h2 := congrArg (Int.cast : ℤ → ZMod 2) him
        rw [hj, hl] at h2; push_cast at h2
        have : (B : ZMod 2) ^ n = 0 := by rw [h2]; exact zmod2_im (j : ZMod 2) (l : ZMod 2)
        have h0 : (B : ZMod 2) = 0 := pow_eq_zero_iff (by omega) |>.mp this
        exact (ZMod.natCast_zmod_eq_zero_iff_dvd B 2).mp h0
      have := Nat.dvd_gcd hA' hB'
      rw [hab] at this; omega
  exact hv0 (re_fifth_not_square h1 h3 hcop hpar hA0 hre.symm)

end Beal

namespace Beal

/-- Symmetric form: no Beal counterexample of signature `(2m, 4, 5)`, `m ≥ 2`. -/
theorem no_counterexample_two_m_four_five (h1 : Quartic400g2) (h3 : Quartic400b2)
    {A B C m : ℕ} (hm : 2 ≤ m) (h : IsBealCounterexample A B C (2 * m) 4 5) : False :=
  no_counterexample_four_two_n_five h1 h3 hm (swap_counterexample h)

end Beal
