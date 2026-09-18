/-
# Fixed-base closure of `{3, 4, r}` via rank-0 Mordell curves (U191/U192)

Named hypothesis `MordellXIntegral k`: every rational point of `y² = x³ + k` has integral `x`.
For a rank-0 curve this is Nagell–Lutz (all rational points are torsion, hence integral); the rank-0
facts are PARI 2-descent upper bounds saved in `references/U130/mordell_fixed_base_ranks.txt`.

Kernel content: the scaling `(X, Y) = (−A / n^{2j}, B² / n^{3j})` and the contradiction
`n^{2j} ∣ A` with `gcd(A, n) = 1`, `n ≥ 2`, `j ≥ 1` — valid for every `r = 6j + e` at once.
-/
import Beal.Structure
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

namespace Beal

/-- Every rational point of `y² = x³ + k` has an integral `x`-coordinate. -/
def MordellXIntegral (k : ℤ) : Prop := ∀ X Y : ℚ, Y ^ 2 = X ^ 3 + k → ∃ a : ℤ, X = a

/-- **Fixed-base step.** `A³ + Y² = n^{6j+e}` with `gcd(A, n) = 1`, `n ≥ 2`, `j ≥ 1` is impossible
when `y² = x³ + nᵉ` has only `x`-integral rational points.  (`Y` is any integer: take `Y = B²`.) -/
theorem fixed_base_cube_plus_square {A n j e : ℕ} {Y : ℤ} (hM : MordellXIntegral ((n : ℤ) ^ e))
    (hn : 2 ≤ n) (hj : 1 ≤ j) (hcop : Nat.Coprime A n)
    (h : (A : ℤ) ^ 3 + Y ^ 2 = (n : ℤ) ^ (6 * j + e)) : False := by
  have hnq : (n : ℚ) ≠ 0 := by exact_mod_cast (by omega : n ≠ 0)
  have hq : (A : ℚ) ^ 3 + (Y : ℚ) ^ 2 = (n : ℚ) ^ (6 * j + e) := by exact_mod_cast h
  have hpoint : ((Y : ℚ) / (n : ℚ) ^ (3 * j)) ^ 2 =
      (-(A : ℚ) / (n : ℚ) ^ (2 * j)) ^ 3 + (((n : ℤ) ^ e : ℤ) : ℚ) := by
    have e1 : ((n : ℚ) ^ (3 * j)) ^ 2 = (n : ℚ) ^ (6 * j) := by rw [← pow_mul]; congr 1; ring
    have e2 : ((n : ℚ) ^ (2 * j)) ^ 3 = (n : ℚ) ^ (6 * j) := by rw [← pow_mul]; congr 1; ring
    have e3 : (n : ℚ) ^ (6 * j + e) = (n : ℚ) ^ (6 * j) * (n : ℚ) ^ e := pow_add _ _ _
    have h6 : (n : ℚ) ^ (6 * j) ≠ 0 := pow_ne_zero _ hnq
    rw [div_pow, div_pow, e1, e2]
    push_cast
    field_simp
    rw [e3] at hq
    linear_combination hq
  obtain ⟨a, ha⟩ := hM _ _ hpoint
  -- `-A = a * n^{2j}` in ℤ, so `n ∣ A`
  have hdiv : (-(A : ℚ)) = (a : ℚ) * (n : ℚ) ^ (2 * j) := by
    have h2 : (n : ℚ) ^ (2 * j) ≠ 0 := pow_ne_zero _ hnq
    field_simp at ha; linarith
  have hdivZ : (-(A : ℤ)) = a * (n : ℤ) ^ (2 * j) := by exact_mod_cast hdiv
  have hnA : (n : ℤ) ∣ (A : ℤ) := by
    have : (n : ℤ) ∣ (n : ℤ) ^ (2 * j) := dvd_pow_self _ (by omega)
    have h1 : (n : ℤ) ∣ -(A : ℤ) := hdivZ ▸ Dvd.dvd.mul_left this a
    exact (dvd_neg).mp h1
  have hnA' : n ∣ A := by exact_mod_cast hnA
  have := Nat.dvd_gcd hnA' (dvd_refl n)
  rw [hcop] at this
  have : n = 1 := Nat.dvd_one.mp this
  omega

/-- Beal form: no counterexample `A³ + B⁴ = n^r` with `r = 6j + e`, `j ≥ 1`, under the hypothesis. -/
theorem no_counterexample_three_four_fixed_base {A B n j e : ℕ}
    (hM : MordellXIntegral ((n : ℤ) ^ e)) (hj : 1 ≤ j)
    (h : IsBealCounterexample A B n 3 4 (6 * j + e)) : False := by
  have hcop : Nat.Coprime A n := gcd_ac_eq_one h
  obtain ⟨hA, hB, hn, _, _, _, _, heq⟩ := h
  have hn2 : 2 ≤ n := by
    rcases Nat.lt_or_ge n 2 with hlt | hge
    · exfalso
      have h1 : n = 1 := by omega
      rw [h1, one_pow] at heq
      have hA3 : 1 ≤ A ^ 3 := Nat.one_le_pow _ _ hA
      have hB4 : 1 ≤ B ^ 4 := Nat.one_le_pow _ _ hB
      omega
    · exact hge
  refine fixed_base_cube_plus_square (Y := (B : ℤ) ^ 2) hM hn2 hj hcop ?_
  have : ((A : ℤ) ^ 3 + (B : ℤ) ^ 4) = (n : ℤ) ^ (6 * j + e) := by exact_mod_cast heq
  linear_combination this

/-- **General fixed-base step.** `Y² = X³ + σ·n^{6j+e}` with `σ = ±1`, `n ∤ X`-coprimality in the form
`n ∣ X → False`, `n ≥ 2`, `j ≥ 1` is impossible when `y² = x³ + σ·nᵉ` has only `x`-integral points. -/
theorem fixed_base_general {n j e : ℕ} {X Y σ : ℤ} (hσ : σ = 1 ∨ σ = -1)
    (hM : MordellXIntegral (σ * (n : ℤ) ^ e)) (hn : 2 ≤ n) (hj : 1 ≤ j)
    (hndvd : ¬ (n : ℤ) ∣ X) (h : Y ^ 2 = X ^ 3 + σ * (n : ℤ) ^ (6 * j + e)) : False := by
  have hnq : (n : ℚ) ≠ 0 := by exact_mod_cast (by omega : n ≠ 0)
  have hq : (Y : ℚ) ^ 2 = (X : ℚ) ^ 3 + (σ : ℚ) * (n : ℚ) ^ (6 * j + e) := by exact_mod_cast h
  have hpoint : ((Y : ℚ) / (n : ℚ) ^ (3 * j)) ^ 2 =
      ((X : ℚ) / (n : ℚ) ^ (2 * j)) ^ 3 + ((σ * (n : ℤ) ^ e : ℤ) : ℚ) := by
    have e1 : ((n : ℚ) ^ (3 * j)) ^ 2 = (n : ℚ) ^ (6 * j) := by rw [← pow_mul]; congr 1; ring
    have e2 : ((n : ℚ) ^ (2 * j)) ^ 3 = (n : ℚ) ^ (6 * j) := by rw [← pow_mul]; congr 1; ring
    have e3 : (n : ℚ) ^ (6 * j + e) = (n : ℚ) ^ (6 * j) * (n : ℚ) ^ e := pow_add _ _ _
    have h6 : (n : ℚ) ^ (6 * j) ≠ 0 := pow_ne_zero _ hnq
    rw [div_pow, div_pow, e1, e2]
    push_cast
    field_simp
    rw [e3] at hq
    linear_combination hq
  obtain ⟨a, ha⟩ := hM _ _ hpoint
  have hdiv : (X : ℚ) = (a : ℚ) * (n : ℚ) ^ (2 * j) := by
    have h2 : (n : ℚ) ^ (2 * j) ≠ 0 := pow_ne_zero _ hnq
    field_simp at ha; linarith
  have hdivZ : X = a * (n : ℤ) ^ (2 * j) := by exact_mod_cast hdiv
  exact hndvd (hdivZ ▸ Dvd.dvd.mul_left (dvd_pow_self _ (by omega)) a)

/-- A base coprime to `n ≥ 2` is not divisible by `n`. -/
lemma not_dvd_of_coprime {A n : ℕ} (hn : 2 ≤ n) (hcop : Nat.Coprime A n) : ¬ (n : ℤ) ∣ (A : ℤ) := by
  intro hd
  have hd' : n ∣ A := by exact_mod_cast hd
  have := Nat.dvd_gcd hd' (dvd_refl n)
  rw [hcop] at this
  have : n = 1 := Nat.dvd_one.mp this
  omega

/-- Sibling arrangement `A³ + n^r = C⁴` (`r = 6j+e`, `j ≥ 1`): point `(A, C²)` on `y² = x³ + n^r`. -/
theorem no_counterexample_three_r_four_fixed_base {A n C j e : ℕ}
    (hM : MordellXIntegral ((1 : ℤ) * (n : ℤ) ^ e)) (hn : 2 ≤ n) (hj : 1 ≤ j)
    (h : IsBealCounterexample A n C 3 (6 * j + e) 4) : False := by
  have hcop : Nat.Coprime A n := gcd_ab_eq_one h
  obtain ⟨_, _, _, _, _, _, _, heq⟩ := h
  refine fixed_base_general (X := (A : ℤ)) (Y := (C : ℤ) ^ 2) (Or.inl rfl) hM hn hj
    (not_dvd_of_coprime hn hcop) ?_
  have : ((A : ℤ) ^ 3 + (n : ℤ) ^ (6 * j + e)) = (C : ℤ) ^ 4 := by exact_mod_cast heq
  linear_combination -this

/-- Sibling arrangement `A⁴ + n^r = C³` (`r = 6j+e`, `j ≥ 1`): point `(C, A²)` on `y² = x³ − n^r`. -/
theorem no_counterexample_four_r_three_fixed_base {A n C j e : ℕ}
    (hM : MordellXIntegral ((-1 : ℤ) * (n : ℤ) ^ e)) (hn : 2 ≤ n) (hj : 1 ≤ j)
    (h : IsBealCounterexample A n C 4 (6 * j + e) 3) : False := by
  have hcop : Nat.Coprime n C := gcd_bc_eq_one h
  obtain ⟨_, _, _, _, _, _, _, heq⟩ := h
  refine fixed_base_general (X := (C : ℤ)) (Y := (A : ℤ) ^ 2) (Or.inr rfl) hM hn hj
    (not_dvd_of_coprime hn hcop.symm) ?_
  have : ((A : ℤ) ^ 4 + (n : ℤ) ^ (6 * j + e)) = (C : ℤ) ^ 3 := by exact_mod_cast heq
  linear_combination this

end Beal

namespace Beal

/-- Every positive rational point of `x³ + y³ = k` has an integral `x`. (For a rank-0 curve: all
points are torsion and the PARI check in `references/U130/fixed_base_333.txt` finds no positive
torsion point with a non-trivial denominator.) -/
def CubicSumXIntegral (k : ℤ) : Prop :=
  ∀ x y : ℚ, 0 < x → 0 < y → x ^ 3 + y ^ 3 = k → ∃ a : ℤ, x = a

/-- **Fixed-base `(3, 3, r)`, all `r = 3j + e` with `j ≥ 1` at once.** -/
theorem no_counterexample_three_three_fixed_base {A B n j e : ℕ}
    (hM : CubicSumXIntegral ((n : ℤ) ^ e)) (hj : 1 ≤ j)
    (h : IsBealCounterexample A B n 3 3 (3 * j + e)) : False := by
  have hcop : Nat.Coprime A n := gcd_ac_eq_one h
  obtain ⟨hA, hB, hn, _, _, _, _, heq⟩ := h
  have hn2 : 2 ≤ n := by
    rcases Nat.lt_or_ge n 2 with hlt | hge
    · exfalso
      have h1 : n = 1 := by omega
      rw [h1, one_pow] at heq
      have hA3 : 1 ≤ A ^ 3 := Nat.one_le_pow _ _ hA
      have hB3 : 1 ≤ B ^ 3 := Nat.one_le_pow _ _ hB
      omega
    · exact hge
  have hnq : (n : ℚ) ≠ 0 := by exact_mod_cast (by omega : n ≠ 0)
  have hnpos : (0 : ℚ) < (n : ℚ) ^ j := by positivity
  have hq : (A : ℚ) ^ 3 + (B : ℚ) ^ 3 = (n : ℚ) ^ (3 * j + e) := by exact_mod_cast heq
  have hpoint : ((A : ℚ) / (n : ℚ) ^ j) ^ 3 + ((B : ℚ) / (n : ℚ) ^ j) ^ 3 = (((n : ℤ) ^ e : ℤ) : ℚ) := by
    have e1 : ((n : ℚ) ^ j) ^ 3 = (n : ℚ) ^ (3 * j) := by rw [← pow_mul]; congr 1; ring
    have e3 : (n : ℚ) ^ (3 * j + e) = (n : ℚ) ^ (3 * j) * (n : ℚ) ^ e := pow_add _ _ _
    have h3 : (n : ℚ) ^ (3 * j) ≠ 0 := pow_ne_zero _ hnq
    rw [div_pow, div_pow, e1]
    push_cast
    field_simp
    rw [e3] at hq
    linear_combination hq
  obtain ⟨a, ha⟩ := hM _ _ (by positivity) (by positivity) hpoint
  have hdiv : (A : ℚ) = (a : ℚ) * (n : ℚ) ^ j := by
    have h2 : (n : ℚ) ^ j ≠ 0 := pow_ne_zero _ hnq
    field_simp at ha; linarith
  have hdivZ : (A : ℤ) = a * (n : ℤ) ^ j := by exact_mod_cast hdiv
  exact not_dvd_of_coprime hn2 hcop (hdivZ ▸ Dvd.dvd.mul_left (dvd_pow_self _ (by omega)) a)

end Beal

namespace Beal

/-- Every rational point of `x³ + y³ = k` has an integral `x` (any signs). For the rank-0 bases of
`references/U130/fixed_base_333.txt` and `fixed_base_333_diff.txt` both sign patterns were checked. -/
def CubicSumXIntegralAll (k : ℤ) : Prop := ∀ x y : ℚ, x ^ 3 + y ^ 3 = k → ∃ a : ℤ, x = a

/-- **Fixed-base difference arrangement** `A³ + n^r = C³`, every `r = 3j + e`, `j ≥ 1`. -/
theorem no_counterexample_three_r_three_fixed_base {A n C j e : ℕ}
    (hM : CubicSumXIntegralAll ((n : ℤ) ^ e)) (hn : 2 ≤ n) (hj : 1 ≤ j)
    (h : IsBealCounterexample A n C 3 (3 * j + e) 3) : False := by
  have hcop : Nat.Coprime n C := gcd_bc_eq_one h
  obtain ⟨_, _, _, _, _, _, _, heq⟩ := h
  have hnq : (n : ℚ) ≠ 0 := by exact_mod_cast (by omega : n ≠ 0)
  have hq : (A : ℚ) ^ 3 + (n : ℚ) ^ (3 * j + e) = (C : ℚ) ^ 3 := by exact_mod_cast heq
  have hpoint : ((C : ℚ) / (n : ℚ) ^ j) ^ 3 + (-(A : ℚ) / (n : ℚ) ^ j) ^ 3 = (((n : ℤ) ^ e : ℤ) : ℚ) := by
    have e1 : ((n : ℚ) ^ j) ^ 3 = (n : ℚ) ^ (3 * j) := by rw [← pow_mul]; congr 1; ring
    have e3 : (n : ℚ) ^ (3 * j + e) = (n : ℚ) ^ (3 * j) * (n : ℚ) ^ e := pow_add _ _ _
    have h3 : (n : ℚ) ^ (3 * j) ≠ 0 := pow_ne_zero _ hnq
    rw [div_pow, div_pow, e1]
    push_cast
    field_simp
    rw [e3] at hq
    linear_combination -hq
  obtain ⟨a, ha⟩ := hM _ _ hpoint
  have hdiv : (C : ℚ) = (a : ℚ) * (n : ℚ) ^ j := by
    have h2 : (n : ℚ) ^ j ≠ 0 := pow_ne_zero _ hnq
    field_simp at ha; linarith
  have hdivZ : (C : ℤ) = a * (n : ℤ) ^ j := by exact_mod_cast hdiv
  exact not_dvd_of_coprime hn hcop.symm (hdivZ ▸ Dvd.dvd.mul_left (dvd_pow_self _ (by omega)) a)

end Beal
