/-
# Signature `(2m, 2n, 3)`, `m, n ≥ 4`: kernel-checked assembly (U131/U134)

Three external inputs are stated as explicit **named hypotheses** (never `axiom`s), so that
`#print axioms` shows only the standard axioms and the dependency is visible in the statement:

* `GaussianCubeStep` — S2–S3: `a² + b² = c³`, `c` odd, `a, b` coprime ⟹ `a + bi = (u + vi)³`.
* `BennettSkinnerThree` — Bennett–Skinner, Canad. J. Math. 56 (2004), Thm 1.1 with `C = 3`.
* `BCDYFourTwoNThree` — Bennett–Chen–Dahmen–Yazdani, IJNT 11 (2015), Thm 1, row `(4, 2n, 3)`.

Everything else — the odd-`C` step, coprimality bookkeeping, the sign analysis that was wrong in the
first draft of S5, and the case split — is proved here.
-/
import Beal.Structure
import Mathlib.Algebra.GCDMonoid.Basic
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.RingTheory.Int.Basic

namespace Beal

/-- **S2–S3.** Coprime `a, b` with `a² + b² = c³` and `c` odd come from a Gaussian cube. -/
def GaussianCubeStep : Prop :=
  ∀ a b c : ℤ, IsCoprime a b → ¬ (2 : ℤ) ∣ c → a ^ 2 + b ^ 2 = c ^ 3 →
    ∃ u v : ℤ, IsCoprime u v ∧ a = u * (u ^ 2 - 3 * v ^ 2) ∧ b = v * (3 * u ^ 2 - v ^ 2)

/-- **Bennett–Skinner Thm 1.1, `C = 3`.**  For `n ≥ 4` the equation `xⁿ + yⁿ = 3z²` has no solution
in nonzero integers with `x, y, 3z` pairwise coprime. -/
def BennettSkinnerThree : Prop :=
  ∀ n : ℕ, 4 ≤ n → ∀ x y z : ℤ, x ≠ 0 → y ≠ 0 → z ≠ 0 →
    IsCoprime x y → IsCoprime x (3 * z) → IsCoprime y (3 * z) → x ^ n + y ^ n ≠ 3 * z ^ 2

/-- **BCDY Thm 1, row `(4, 2n, 3)`.**  No coprime positive solution of `a⁴ + b^{2n} = c³`, `n ≥ 2`. -/
def BCDYFourTwoNThree : Prop :=
  ∀ a b c n : ℕ, 2 ≤ n → 0 < a → 0 < b → 0 < c → Nat.Coprime a b → a ^ 4 + b ^ (2 * n) = c ^ 3 → False

/-! ### Elementary lemmas -/

/-- If `3 ∤ u` and `gcd u v = 1` then `u` is coprime to `u² - 3v²`. -/
lemma isCoprime_u_cofactor {u v : ℤ} (huv : IsCoprime u v) (h3 : ¬ (3 : ℤ) ∣ u) :
    IsCoprime u (u ^ 2 - 3 * v ^ 2) := by
  have h3u : IsCoprime u 3 :=
    ((Int.prime_three.irreducible.coprime_iff_not_dvd).mpr h3).symm
  have h1 : IsCoprime u (3 * v ^ 2) := h3u.mul_right (huv.pow_right)
  have h2 : IsCoprime u (-(3 * v ^ 2) + u * u) := h1.neg_right.add_mul_left_right u
  have : -(3 * v ^ 2) + u * u = u ^ 2 - 3 * v ^ 2 := by ring
  rwa [this] at h2

/-- `v` is coprime to `u² - 3v²` whenever `gcd u v = 1`. -/
lemma isCoprime_v_cofactor {u v : ℤ} (huv : IsCoprime u v) :
    IsCoprime (u ^ 2 - 3 * v ^ 2) v := by
  have h1 : IsCoprime (u * u) v := huv.mul_left huv
  have h2 : IsCoprime (u * u + v * (-3 * v)) v := h1.add_mul_left_left (-3 * v)
  have : u * u + v * (-3 * v) = u ^ 2 - 3 * v ^ 2 := by ring
  rwa [this] at h2

/-- A coprime product in `ℤ` that is a `k`-th power has each factor `± (k`-th power`)`. -/
lemma int_factor_pow {u w c : ℤ} {k : ℕ} (h : IsCoprime u w) (hk : u * w = c ^ k) :
    ∃ s : ℤ, u = s ^ k ∨ u = -(s ^ k) := by
  have hu : IsUnit (gcd u w) := by
    rw [← Int.coe_gcd, Int.gcd_eq_one_iff_coprime.mpr h]; exact isUnit_one
  obtain ⟨s, hs⟩ := exists_associated_pow_of_mul_eq_pow hu hk
  exact ⟨s, (Int.associated_iff.mp hs).elim (fun e => Or.inl e.symm) (fun e => Or.inr (by rw [e]; ring))⟩

/-! ### The one-sided Bennett–Skinner step (odd exponent) -/

/-- **S5–S6.** If `3 ∤ u`, `gcd u v = 1`, `v ≠ 0`, `m ≥ 5` odd, and `u (u² - 3v²) = ± cᵐ` with
`c ≠ 0`, then Bennett–Skinner is violated. -/
lemma side_odd (hBS : BennettSkinnerThree) {m : ℕ} (hm : 5 ≤ m) (hodd : Odd m)
    {u v c : ℤ} (huv : IsCoprime u v) (h3 : ¬ (3 : ℤ) ∣ u) (hv : v ≠ 0) (hc : c ≠ 0)
    (h : u * (u ^ 2 - 3 * v ^ 2) = c ^ m ∨ u * (u ^ 2 - 3 * v ^ 2) = -(c ^ m)) : False := by
  set w := u ^ 2 - 3 * v ^ 2 with hw
  have hcop : IsCoprime u w := isCoprime_u_cofactor huv h3
  -- normalise the sign: `u * w = c'^m` with `c' = ± c`
  obtain ⟨c', hc', hprod⟩ : ∃ c' : ℤ, c' ≠ 0 ∧ u * w = c' ^ m := by
    rcases h with h | h
    · exact ⟨c, hc, h⟩
    · exact ⟨-c, neg_ne_zero.mpr hc, by rw [hodd.neg_pow, h]⟩
  have hu0 : u ≠ 0 := by
    intro h0; apply hc'; rw [h0, zero_mul] at hprod; exact pow_eq_zero_iff (by omega) |>.mp hprod.symm
  have hw0 : w ≠ 0 := by
    intro h0; apply hc'; rw [h0, mul_zero] at hprod; exact pow_eq_zero_iff (by omega) |>.mp hprod.symm
  obtain ⟨s, hs⟩ := int_factor_pow hcop hprod
  obtain ⟨t, ht⟩ := int_factor_pow hcop.symm (by rw [mul_comm]; exact hprod)
  -- `u² = s^{2m}` regardless of the sign of `u`
  have hu2 : u ^ 2 = (s ^ 2) ^ m := by
    rcases hs with hs | hs <;> rw [hs] <;> ring
  have hs0 : s ≠ 0 := by
    intro h0; apply hu0; rcases hs with hs | hs <;> rw [hs, h0, zero_pow (by omega)]; simp
  have ht0 : t ≠ 0 := by
    intro h0; apply hw0; rcases ht with ht | ht <;> rw [ht, h0, zero_pow (by omega)]; simp
  -- the Bennett–Skinner equation `(s²)^m + y^m = 3 v²` with `y = -t` or `y = t`
  obtain ⟨y, hy0, hyt, heq⟩ : ∃ y : ℤ, y ≠ 0 ∧ (y = t ∨ y = -t) ∧ (s ^ 2) ^ m + y ^ m = 3 * v ^ 2 := by
    rcases ht with ht | ht
    · refine ⟨-t, neg_ne_zero.mpr ht0, Or.inr rfl, ?_⟩
      rw [hodd.neg_pow, ← ht, ← hu2, hw]; ring
    · refine ⟨t, ht0, Or.inl rfl, ?_⟩
      have : t ^ m = -w := by rw [ht]; ring
      rw [this, ← hu2, hw]; ring
  -- coprimality bookkeeping
  have hst : IsCoprime s t := by
    have e1 : IsCoprime (s ^ m) w := by
      rcases hs with hs | hs
      · rw [← hs]; exact hcop
      · have := hcop.neg_left; rw [hs, neg_neg] at this; exact this
    have e2 : IsCoprime (s ^ m) (t ^ m) := by
      rcases ht with ht | ht
      · rw [← ht]; exact e1
      · have := e1.neg_right; rw [ht, neg_neg] at this; exact this
    exact (IsCoprime.pow_iff (by omega) (by omega)).mp e2
  have hsy : IsCoprime (s ^ 2) y := by
    rcases hyt with rfl | rfl
    · exact hst.pow_left
    · exact hst.pow_left.neg_right
  have h3s : ¬ (3 : ℤ) ∣ s := by
    intro hd; apply h3
    rcases hs with hs | hs <;> rw [hs]
    · exact dvd_pow hd (by omega)
    · exact (dvd_pow hd (by omega)).neg_right
  have h3t : ¬ (3 : ℤ) ∣ t := by
    intro hd
    have h1 : (3 : ℤ) ∣ w := by
      rcases ht with ht | ht <;> rw [ht]
      · exact dvd_pow hd (by omega)
      · exact (dvd_pow hd (by omega)).neg_right
    have h2 : (3 : ℤ) ∣ u ^ 2 := by
      have : u ^ 2 = w + 3 * v ^ 2 := by rw [hw]; ring
      rw [this]; exact dvd_add h1 (dvd_mul_right 3 _)
    exact h3 (Int.prime_three.dvd_of_dvd_pow h2)
  have hsv : IsCoprime s v := by
    have : IsCoprime (s ^ m) v := by
      rcases hs with hs | hs
      · rw [← hs]; exact huv
      · have := huv.neg_left; rw [hs, neg_neg] at this; exact this
    exact (IsCoprime.pow_left_iff (by omega)).mp this
  have htv : IsCoprime t v := by
    have hwv : IsCoprime w v := isCoprime_v_cofactor huv
    have : IsCoprime (t ^ m) v := by
      rcases ht with ht | ht
      · rw [← ht]; exact hwv
      · have := hwv.neg_left; rw [ht, neg_neg] at this; exact this
    exact (IsCoprime.pow_left_iff (by omega)).mp this
  have hs3 : IsCoprime s 3 := ((Int.prime_three.irreducible.coprime_iff_not_dvd).mpr h3s).symm
  have ht3 : IsCoprime t 3 := ((Int.prime_three.irreducible.coprime_iff_not_dvd).mpr h3t).symm
  have hx3z : IsCoprime (s ^ 2) (3 * v) := (hs3.mul_right hsv).pow_left
  have hy3z : IsCoprime y (3 * v) := by
    rcases hyt with rfl | rfl
    · exact ht3.mul_right htv
    · exact (ht3.mul_right htv).neg_left
  exact hBS m (by omega) (s ^ 2) y v (pow_ne_zero 2 hs0) hy0 hv hsy hx3z hy3z heq

/-! ### Assembly -/

/-- **Main theorem (U131/U134).**  No Beal counterexample of signature `(2m, 2n, 3)` with `m, n ≥ 4`,
given the three named external inputs. -/
theorem no_counterexample_even_even_three
    (hZ : GaussianCubeStep) (hBS : BennettSkinnerThree) (hBCDY : BCDYFourTwoNThree)
    {A B C m n : ℕ} (hm : 4 ≤ m) (hn : 4 ≤ n)
    (h : IsBealCounterexample A B C (2 * m) (2 * n) 3) : False := by
  have hab : Nat.Coprime A B := gcd_ab_eq_one h
  have hCodd : C % 2 = 1 := by
    have := not_both_exponents_even_of_even_C (h := h)
    by_contra hc
    exact this (by omega) ⟨by omega, by omega⟩
  obtain ⟨hA, hB, hC, -, -, -, -, heq⟩ := h
  -- even `m` ⟹ signature `(4, 2n, 3)` ⟹ BCDY
  rcases Nat.even_or_odd m with ⟨k, hk⟩ | hmodd
  · refine hBCDY (A ^ k) B C n (by omega) (by positivity) hB hC (hab.pow_left k) ?_
    have e : (A ^ k) ^ 4 = A ^ (2 * m) := by rw [← pow_mul]; congr 1; omega
    rw [e]; exact heq
  rcases Nat.even_or_odd n with ⟨l, hl⟩ | hnodd
  · refine hBCDY (B ^ l) A C m (by omega) (by positivity) hA hC (hab.symm.pow_left l) ?_
    have e : (B ^ l) ^ 4 = B ^ (2 * n) := by rw [← pow_mul]; congr 1; omega
    rw [e, add_comm]; exact heq
  -- both odd, hence `≥ 5`: the Gaussian route
  have hm5 : 5 ≤ m := by obtain ⟨k, hk⟩ := hmodd; omega
  have hn5 : 5 ≤ n := by obtain ⟨l, hl⟩ := hnodd; omega
  have hsq : ((A : ℤ) ^ m) ^ 2 + ((B : ℤ) ^ n) ^ 2 = (C : ℤ) ^ 3 := by
    have : A ^ (2 * m) + B ^ (2 * n) = C ^ 3 := heq
    rw [← pow_mul, ← pow_mul, mul_comm m 2, mul_comm n 2]
    exact_mod_cast this
  have hcop : IsCoprime ((A : ℤ) ^ m) ((B : ℤ) ^ n) :=
    (Nat.isCoprime_iff_coprime.mpr hab).pow
  have hC2 : ¬ (2 : ℤ) ∣ (C : ℤ) := by
    intro hd; have := Int.natCast_dvd_natCast.mp hd; omega
  obtain ⟨u, v, huv, ha, hb⟩ := hZ _ _ _ hcop hC2 hsq
  have hA0 : (A : ℤ) ≠ 0 := by exact_mod_cast hA.ne'
  have hB0 : (B : ℤ) ≠ 0 := by exact_mod_cast hB.ne'
  have hu0 : u ≠ 0 := by
    intro h0; apply pow_ne_zero m hA0; rw [ha, h0]; ring
  have hv0 : v ≠ 0 := by
    intro h0; apply pow_ne_zero n hB0; rw [hb, h0]; ring
  by_cases h3u : (3 : ℤ) ∣ u
  · -- then `3 ∤ v`; use the Im side, `v (v² - 3u²) = -(Bⁿ)`
    have h3v : ¬ (3 : ℤ) ∣ v := by
      intro hd
      have := Int.isCoprime_iff_gcd_eq_one.mp huv
      have h := Int.dvd_gcd h3u hd
      rw [this] at h
      exact absurd (Int.eq_one_of_dvd_one (by norm_num) h) (by norm_num)
    refine side_odd hBS hn5 hnodd huv.symm h3v hu0 hB0 (Or.inr ?_)
    rw [hb]; ring
  · exact side_odd hBS hm5 hmodd huv h3u hv0 hA0 (Or.inl ha.symm)

end Beal
