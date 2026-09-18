/-
# The Gaussian `z`-th power step for odd `z` (U144, generalising `GaussianCube`)

`a² + b² = c^z`, `z` odd, `a, b` coprime, `c` odd  ⟹  `a + bi = (u + vi)^z` in `ℤ[i]`.
The unit is absorbed via `ε = (ε^z)^z`, valid because `ε⁴ = 1` and `z² ≡ 1 (mod 4)`.
-/
import Beal.GaussianCube

open Zsqrtd

local notation "ℤ[i]" => GaussianInt

namespace Beal

noncomputable local instance : GCDMonoid ℤ[i] := UniqueFactorizationMonoid.toGCDMonoid ℤ[i]

/-- For a unit `ε` of `ℤ[i]` and odd `z`, `(ε ^ z) ^ z = ε`. -/
lemma unit_pow_odd_sq {ε : ℤ[i]} (h : IsUnit ε) {z : ℕ} (hz : Odd z) : (ε ^ z) ^ z = ε := by
  have h4 := unit_pow_four h
  obtain ⟨k, hk⟩ := hz
  -- z² = 4k² + 4k + 1
  have : (ε ^ z) ^ z = ε ^ (4 * (k * k + k)) * ε := by
    rw [← pow_mul, hk]; ring_nf
  rw [this, pow_mul, h4, one_pow, one_mul]

/-- **Gaussian odd-power step.** -/
theorem gaussian_odd_pow_step {z : ℕ} (hz : Odd z) {a b c : ℤ} (hab : IsCoprime a b)
    (hc : ¬ (2 : ℤ) ∣ c) (h : a ^ 2 + b ^ 2 = c ^ z) :
    ∃ w : ℤ[i], w ^ z = ⟨a, b⟩ ∧ IsCoprime w.re w.im := by
  have hz0 : z ≠ 0 := by rintro rfl; exact (by decide : ¬ Odd 0) hz
  set α : ℤ[i] := ⟨a, b⟩ with hα
  have hcz : ((c : ℤ[i])) ^ z = ((c ^ z : ℤ) : ℤ[i]) := by push_cast; rfl
  have hprod : α * star α = (c : ℤ[i]) ^ z := by
    rw [hcz]; ext
    · simp only [hα, Zsqrtd.mul_re, Zsqrtd.star_re, Zsqrtd.star_im, Zsqrtd.intCast_re]; nlinarith [h]
    · simp only [hα, Zsqrtd.mul_im, Zsqrtd.star_re, Zsqrtd.star_im, Zsqrtd.intCast_im]; ring
  have hunit : ∀ g : ℤ[i], g ∣ α → g ∣ star α → IsUnit g := by
    intro g h1 h2
    have h2a : g ∣ ((2 * a : ℤ) : ℤ[i]) := by
      have : α + star α = ((2 * a : ℤ) : ℤ[i]) := by
        ext <;> simp only [hα, Zsqrtd.add_re, Zsqrtd.add_im, Zsqrtd.star_re, Zsqrtd.star_im,
          Zsqrtd.intCast_re, Zsqrtd.intCast_im] <;> ring
      rw [← this]; exact dvd_add h1 h2
    have h2b : g ∣ ((2 * b : ℤ) : ℤ[i]) := by
      have : (α - star α) * ⟨0, -1⟩ = ((2 * b : ℤ) : ℤ[i]) := by
        ext <;> simp only [hα, Zsqrtd.sub_re, Zsqrtd.sub_im, Zsqrtd.mul_re, Zsqrtd.mul_im,
          Zsqrtd.star_re, Zsqrtd.star_im, Zsqrtd.intCast_re, Zsqrtd.intCast_im] <;> ring
      rw [← this]; exact (dvd_sub h1 h2).mul_right _
    have h2' : g ∣ ((2 : ℤ) : ℤ[i]) := by
      obtain ⟨m, n, hmn⟩ := hab
      have : ((2 : ℤ) : ℤ[i]) = (m : ℤ[i]) * ((2 * a : ℤ) : ℤ[i]) + (n : ℤ[i]) * ((2 * b : ℤ) : ℤ[i]) := by
        have := congrArg (fun t : ℤ => ((2 * t : ℤ) : ℤ[i])) hmn
        push_cast at this ⊢; linear_combination -this
      rw [this]; exact dvd_add (h2a.mul_left _) (h2b.mul_left _)
    have hgc : g ∣ ((c ^ z : ℤ) : ℤ[i]) := by rw [← hcz, ← hprod]; exact h1.mul_right _
    have n2 : g.norm ∣ 4 := by
      have := norm_dvd_of_dvd h2'
      have h4 : ((2 : ℤ) : ℤ[i]).norm = 4 := by
        rw [Zsqrtd.norm_def, Zsqrtd.intCast_re, Zsqrtd.intCast_im]; norm_num
      rwa [h4] at this
    have nc : g.norm ∣ (c ^ z) ^ 2 := by
      have := norm_dvd_of_dvd hgc
      have h6 : ((c ^ z : ℤ) : ℤ[i]).norm = (c ^ z) ^ 2 := by
        rw [Zsqrtd.norm_def, Zsqrtd.intCast_re, Zsqrtd.intCast_im]; ring
      rwa [h6] at this
    have hodd : ¬ (2 : ℤ) ∣ (c ^ z) ^ 2 := fun hd =>
      hc (Int.prime_two.dvd_of_dvd_pow (Int.prime_two.dvd_of_dvd_pow hd))
    have hcop : IsCoprime (4 : ℤ) ((c ^ z) ^ 2) := by
      have h2c : IsCoprime (2 : ℤ) ((c ^ z) ^ 2) :=
        (Int.prime_two.irreducible.coprime_iff_not_dvd).mpr hodd
      have := h2c.mul_left h2c
      norm_num at this; exact this
    have hu : IsUnit g.norm := hcop.isUnit_of_dvd' n2 nc
    have hnorm : g.norm = 1 := by
      have h0 := GaussianInt.norm_nonneg g
      rcases Int.isUnit_iff.mp hu with h | h <;> omega
    exact (Zsqrtd.norm_eq_one_iff' (by norm_num) g).mp hnorm
  have hgcd : IsUnit (gcd α (star α)) := hunit _ (gcd_dvd_left _ _) (gcd_dvd_right _ _)
  obtain ⟨δ, hδ⟩ := exists_associated_pow_of_mul_eq_pow hgcd hprod
  obtain ⟨ε, hε⟩ := hδ            -- δ ^ z * ε = α
  set w : ℤ[i] := δ * (ε : ℤ[i]) ^ z with hw
  have hcube : w ^ z = α := by
    rw [← hε, hw, mul_pow, unit_pow_odd_sq ε.isUnit hz]
  refine ⟨w, hcube, ?_⟩
  -- coprimality of `re w, im w` from that of `a, b`: a common divisor of `w.re, w.im` divides `w`,
  -- hence `w ^ z = α`, hence `a` and `b`.
  have hwd : ∀ d : ℤ, d ∣ w.re → d ∣ w.im → d ∣ a ∧ d ∣ b := by
    intro d h1 h2
    have hd : (d : ℤ[i]) ∣ w := by
      obtain ⟨e1, he1⟩ := h1; obtain ⟨e2, he2⟩ := h2
      refine ⟨⟨e1, e2⟩, ?_⟩
      ext <;> simp only [Zsqrtd.mul_re, Zsqrtd.mul_im, Zsqrtd.intCast_re, Zsqrtd.intCast_im] <;>
        [rw [he1]; rw [he2]] <;> ring
    have hdα : (d : ℤ[i]) ∣ α := by
      rw [← hcube]; exact hd.trans (dvd_pow_self w hz0)
    obtain ⟨⟨e1, e2⟩, he⟩ := hdα
    have hre := congrArg Zsqrtd.re he
    have him := congrArg Zsqrtd.im he
    simp only [hα, Zsqrtd.mul_re, Zsqrtd.mul_im, Zsqrtd.intCast_re, Zsqrtd.intCast_im] at hre him
    exact ⟨⟨e1, by linarith⟩, ⟨e2, by linarith⟩⟩
  -- turn 'every common divisor divides a and b' into `IsCoprime` via Bezout in ℤ
  rw [Int.isCoprime_iff_gcd_eq_one]
  have hg := hwd _ (Int.gcd_dvd_left) (Int.gcd_dvd_right)
  have := Int.dvd_gcd hg.1 hg.2
  rw [Int.isCoprime_iff_gcd_eq_one.mp hab] at this
  exact Nat.eq_one_of_dvd_one (by exact_mod_cast this) |> fun h => by
    have : (Int.gcd w.re w.im : ℤ) = 1 := by exact_mod_cast h
    exact_mod_cast this

end Beal

namespace Beal

/-- **C045, machine-checked.** A Beal counterexample of signature `(2m, 2n, z)` with `z` odd is a
`z`-th power in `ℤ[i]`: `(A^m, B^n)` are the coordinates of `w ^ z` with `gcd(re w, im w) = 1`. -/
theorem even_even_odd_reduction {A B C m n z : ℕ} (hz : Odd z)
    (h : IsBealCounterexample A B C (2 * m) (2 * n) z) :
    ∃ w : GaussianInt, w ^ z = ⟨(A : ℤ) ^ m, (B : ℤ) ^ n⟩ ∧ IsCoprime w.re w.im := by
  have hab : Nat.Coprime A B := gcd_ab_eq_one h
  have hCodd : C % 2 = 1 := by
    have := not_both_exponents_even_of_even_C (h := h)
    by_contra hc
    exact this (by omega) ⟨by omega, by omega⟩
  obtain ⟨_, _, _, _, _, _, _, heq⟩ := h
  have hsq : ((A : ℤ) ^ m) ^ 2 + ((B : ℤ) ^ n) ^ 2 = (C : ℤ) ^ z := by
    have : A ^ (2 * m) + B ^ (2 * n) = C ^ z := heq
    rw [← pow_mul, ← pow_mul, mul_comm m 2, mul_comm n 2]
    exact_mod_cast this
  have hcop : IsCoprime ((A : ℤ) ^ m) ((B : ℤ) ^ n) := (Nat.isCoprime_iff_coprime.mpr hab).pow
  have hC2 : ¬ (2 : ℤ) ∣ (C : ℤ) := by
    intro hd; have := Int.natCast_dvd_natCast.mp hd; omega
  exact gaussian_odd_pow_step hz hcop hC2 hsq

end Beal
