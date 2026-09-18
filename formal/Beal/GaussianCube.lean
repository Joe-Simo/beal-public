/-
# The Gaussian cube step (U136): discharging `GaussianCubeStep`

`a² + b² = c³` with `a, b` coprime and `c` odd forces `a + bi = (u + vi)³` in `ℤ[i]`.
Proof: `α = a + bi` and `star α` are coprime (a common divisor divides `2` and the odd `c³`, so its
norm divides `gcd(4, c⁶) = 1`), their product is the cube `c³`, so `α` is a unit times a cube in the
UFD `ℤ[i]`; every unit of `ℤ[i]` is itself a cube (`ε⁴ = 1`), so `α` is a cube.
-/
import Beal.EvenEvenThree
import Mathlib.NumberTheory.Zsqrtd.GaussianInt
import Mathlib.RingTheory.UniqueFactorizationDomain.GCDMonoid
import Mathlib.Algebra.EuclideanDomain.Basic

open Zsqrtd

local notation "ℤ[i]" => GaussianInt

namespace Beal

noncomputable local instance : GCDMonoid ℤ[i] := UniqueFactorizationMonoid.toGCDMonoid ℤ[i]

/-- Norm divisibility follows from divisibility. -/
lemma norm_dvd_of_dvd {x y : ℤ[i]} (h : x ∣ y) : Zsqrtd.norm x ∣ Zsqrtd.norm y := by
  obtain ⟨k, rfl⟩ := h; rw [Zsqrtd.norm_mul]; exact dvd_mul_right _ _

/-- Every unit of `ℤ[i]` satisfies `ε ^ 4 = 1`. -/
lemma unit_pow_four {ε : ℤ[i]} (h : IsUnit ε) : ε ^ 4 = 1 := by
  have hn : ε.norm = 1 := (Zsqrtd.norm_eq_one_iff' (by norm_num) ε).mpr h
  rw [Zsqrtd.norm_def] at hn
  have hn' : ε.re * ε.re + ε.im * ε.im = 1 := by linarith
  have h1 : ε.re = 0 ∨ ε.re = 1 ∨ ε.re = -1 := by
    have hl : -1 ≤ ε.re := by
      by_contra hc; push_neg at hc
      have : ε.re ≤ -2 := by omega
      nlinarith [sq_nonneg ε.im]
    have hr : ε.re ≤ 1 := by
      by_contra hc; push_neg at hc
      have : 2 ≤ ε.re := by omega
      nlinarith [sq_nonneg ε.im]
    omega
  have h2 : ε.im = 0 ∨ ε.im = 1 ∨ ε.im = -1 := by
    have hl : -1 ≤ ε.im := by
      by_contra hc; push_neg at hc
      have : ε.im ≤ -2 := by omega
      nlinarith [sq_nonneg ε.re]
    have hr : ε.im ≤ 1 := by
      by_contra hc; push_neg at hc
      have : 2 ≤ ε.im := by omega
      nlinarith [sq_nonneg ε.re]
    omega
  have e4 : ε ^ 4 = ε * ε * ε * ε := by ring
  rw [e4]
  ext
  · simp only [Zsqrtd.mul_re, Zsqrtd.mul_im, Zsqrtd.one_re]
    rcases h1 with h1 | h1 | h1 <;> rcases h2 with h2 | h2 | h2 <;> simp [h1, h2] at hn' ⊢
  · simp only [Zsqrtd.mul_re, Zsqrtd.mul_im, Zsqrtd.one_im]
    rcases h1 with h1 | h1 | h1 <;> rcases h2 with h2 | h2 | h2 <;> simp [h1, h2] at hn' ⊢

/-- **`GaussianCubeStep` holds.** -/
theorem gaussianCubeStep : GaussianCubeStep := by
  intro a b c hab hc h
  set α : ℤ[i] := ⟨a, b⟩ with hα
  have hc3 : ((c : ℤ[i])) ^ 3 = ((c ^ 3 : ℤ) : ℤ[i]) := by push_cast; rfl
  -- the product with the conjugate is `c ^ 3`
  have hprod : α * star α = (c : ℤ[i]) ^ 3 := by
    rw [hc3]; ext
    · simp only [hα, Zsqrtd.add_re, Zsqrtd.add_im, Zsqrtd.sub_re, Zsqrtd.sub_im, Zsqrtd.mul_re, Zsqrtd.mul_im, Zsqrtd.star_re, Zsqrtd.star_im, Zsqrtd.intCast_re, Zsqrtd.intCast_im]
      nlinarith [h]
    · simp only [hα, Zsqrtd.add_re, Zsqrtd.add_im, Zsqrtd.sub_re, Zsqrtd.sub_im, Zsqrtd.mul_re, Zsqrtd.mul_im, Zsqrtd.star_re, Zsqrtd.star_im, Zsqrtd.intCast_re, Zsqrtd.intCast_im]
      ring
  -- any common divisor of `α` and `star α` is a unit
  have hunit : ∀ g : ℤ[i], g ∣ α → g ∣ star α → IsUnit g := by
    intro g h1 h2
    have h2a : g ∣ ((2 * a : ℤ) : ℤ[i]) := by
      have : α + star α = ((2 * a : ℤ) : ℤ[i]) := by
        ext <;> simp only [hα, Zsqrtd.add_re, Zsqrtd.add_im, Zsqrtd.sub_re, Zsqrtd.sub_im, Zsqrtd.mul_re, Zsqrtd.mul_im, Zsqrtd.star_re, Zsqrtd.star_im, Zsqrtd.intCast_re, Zsqrtd.intCast_im] <;> ring
      rw [← this]; exact dvd_add h1 h2
    have h2b : g ∣ ((2 * b : ℤ) : ℤ[i]) := by
      have : (α - star α) * ⟨0, -1⟩ = ((2 * b : ℤ) : ℤ[i]) := by
        ext <;> simp only [hα, Zsqrtd.add_re, Zsqrtd.add_im, Zsqrtd.sub_re, Zsqrtd.sub_im, Zsqrtd.mul_re, Zsqrtd.mul_im, Zsqrtd.star_re, Zsqrtd.star_im, Zsqrtd.intCast_re, Zsqrtd.intCast_im] <;> ring
      rw [← this]; exact (dvd_sub h1 h2).mul_right _
    have h2' : g ∣ ((2 : ℤ) : ℤ[i]) := by
      obtain ⟨m, n, hmn⟩ := hab
      have : ((2 : ℤ) : ℤ[i]) = (m : ℤ[i]) * ((2 * a : ℤ) : ℤ[i]) + (n : ℤ[i]) * ((2 * b : ℤ) : ℤ[i]) := by
        have := congrArg (fun t : ℤ => ((2 * t : ℤ) : ℤ[i])) hmn
        push_cast at this ⊢; linear_combination -this
      rw [this]; exact dvd_add (h2a.mul_left _) (h2b.mul_left _)
    have hgc : g ∣ ((c ^ 3 : ℤ) : ℤ[i]) := by rw [← hc3, ← hprod]; exact h1.mul_right _
    have n2 : g.norm ∣ 4 := by
      have := norm_dvd_of_dvd h2'
      have h4 : ((2 : ℤ) : ℤ[i]).norm = 4 := by
        rw [Zsqrtd.norm_def, Zsqrtd.intCast_re, Zsqrtd.intCast_im]; norm_num
      rwa [h4] at this
    have nc : g.norm ∣ c ^ 6 := by
      have := norm_dvd_of_dvd hgc
      have h6 : ((c ^ 3 : ℤ) : ℤ[i]).norm = c ^ 6 := by
        rw [Zsqrtd.norm_def, Zsqrtd.intCast_re, Zsqrtd.intCast_im]; ring
      rwa [h6] at this
    -- `gcd (4, c^6) = 1` since `c` is odd
    have hodd : ¬ (2 : ℤ) ∣ c ^ 6 := fun hd => hc (Int.prime_two.dvd_of_dvd_pow hd)
    have hcop : IsCoprime (4 : ℤ) (c ^ 6) := by
      have h2c : IsCoprime (2 : ℤ) (c ^ 6) := (Int.prime_two.irreducible.coprime_iff_not_dvd).mpr hodd
      have := h2c.mul_left h2c
      norm_num at this; exact this
    have hu : IsUnit g.norm := hcop.isUnit_of_dvd' n2 nc
    have hnorm : g.norm = 1 := by
      have h0 := GaussianInt.norm_nonneg g
      rcases Int.isUnit_iff.mp hu with h | h <;> omega
    exact (Zsqrtd.norm_eq_one_iff' (by norm_num) g).mp hnorm
  -- hence `gcd α (star α)` is a unit and `α` is associated to a cube
  have hgcd : IsUnit (gcd α (star α)) := hunit _ (gcd_dvd_left _ _) (gcd_dvd_right _ _)
  obtain ⟨δ, hδ⟩ := exists_associated_pow_of_mul_eq_pow hgcd hprod
  obtain ⟨ε, hε⟩ := hδ            -- δ ^ 3 * ε = α
  -- absorb the unit: `ε = (ε⁻¹) ^ 3` because `ε ^ 4 = 1`
  have hε4 : (ε : ℤ[i]) ^ 4 = 1 := unit_pow_four ε.isUnit
  set w : ℤ[i] := δ * (ε⁻¹ : ℤ[i]ˣ) with hw
  have hcube : w ^ 3 = α := by
    rw [← hε, hw, mul_pow]
    have hinv : ((ε⁻¹ : ℤ[i]ˣ) : ℤ[i]) ^ 3 = (ε : ℤ[i]) := by
      calc ((ε⁻¹ : ℤ[i]ˣ) : ℤ[i]) ^ 3 = ((ε⁻¹ : ℤ[i]ˣ) : ℤ[i]) ^ 3 * (ε : ℤ[i]) ^ 4 := by rw [hε4, mul_one]
        _ = (((ε⁻¹ : ℤ[i]ˣ) : ℤ[i]) * (ε : ℤ[i])) ^ 3 * (ε : ℤ[i]) := by ring
        _ = (ε : ℤ[i]) := by rw [Units.inv_mul]; ring
    rw [hinv]
  have hre : a = w.re * (w.re ^ 2 - 3 * w.im ^ 2) := by
    have := congrArg Zsqrtd.re hcube
    simp only [hα, pow_succ, pow_zero, one_mul, Zsqrtd.mul_re, Zsqrtd.mul_im] at this
    linear_combination -this
  have him : b = w.im * (3 * w.re ^ 2 - w.im ^ 2) := by
    have := congrArg Zsqrtd.im hcube
    simp only [hα, pow_succ, pow_zero, one_mul, Zsqrtd.mul_re, Zsqrtd.mul_im] at this
    linear_combination -this
  refine ⟨w.re, w.im, ?_, hre, him⟩
  rw [hre, him] at hab
  exact hab.of_mul_left_left.of_mul_right_left

/-- **Corollary.** `(2m, 2n, 3)`, `m, n ≥ 4`, needs only the two published theorems. -/
theorem no_counterexample_even_even_three' (hBS : BennettSkinnerThree) (hBCDY : BCDYFourTwoNThree)
    {A B C m n : ℕ} (hm : 4 ≤ m) (hn : 4 ≤ n)
    (h : IsBealCounterexample A B C (2 * m) (2 * n) 3) : False :=
  no_counterexample_even_even_three gaussianCubeStep hBS hBCDY hm hn h

end Beal
