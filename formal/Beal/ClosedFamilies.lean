/-
# Ledger of closed signature families (U156)

One statement collecting every family closed in this repository, with its exact dependencies.
Unconditional families come from mathlib (FLT₄ via `not_fermat_42`, FLT₃); conditional families
carry their named hypotheses in the statement. Nothing here is an `axiom`.
-/
import Beal.Residual
import Beal.SixTwoNThree
import Beal.FourTwoNFive

namespace Beal

/-- **Unconditional (mathlib only).** `(4k, 4l, 2j)` and `(3k, 3l, 3j)` carry no counterexample. -/
theorem closed_unconditional {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    ¬ (4 ∣ x ∧ 4 ∣ y ∧ 2 ∣ z) ∧ ¬ (3 ∣ x ∧ 3 ∣ y ∧ 3 ∣ z) :=
  ⟨fun ⟨hx, hy, hz⟩ => no_counterexample_of_four_four_even hx hy hz h,
   fun ⟨hx, hy, hz⟩ => no_counterexample_of_three_dvd_all hx hy hz h⟩

/-- **Conditional ledger.** Under the five named hypotheses, no counterexample has signature
`(2m, 2n, 3)` with `m, n ≥ 2`, nor `(4, 2n, 5)` / `(2m, 4, 5)` with `m, n ≥ 2`. -/
theorem closed_conditional (hBS : BennettSkinnerThree) (hBCDY : BCDYFourTwoNThree)
    (hM : Mordell27) (h1 : Quartic400g2) (h3 : Quartic400b2) {A B C : ℕ} :
    (∀ m n, 2 ≤ m → 2 ≤ n → ¬ IsBealCounterexample A B C (2 * m) (2 * n) 3) ∧
    (∀ n, 2 ≤ n → ¬ IsBealCounterexample A B C 4 (2 * n) 5) ∧
    (∀ m, 2 ≤ m → ¬ IsBealCounterexample A B C (2 * m) 4 5) :=
  ⟨fun m n hm hn h => no_counterexample_even_even_three_all hBS hBCDY hM hm hn h,
   fun n hn h => no_counterexample_four_two_n_five h1 h3 hn h,
   fun m hm h => no_counterexample_two_m_four_five h1 h3 hm h⟩

end Beal

namespace Beal

/-- Pulling a counterexample back along exponent divisibility: if `a ∣ x`, `b ∣ y`, `c ∣ z` then
`(A^{x/a}, B^{y/b}, C^{z/c})` is a counterexample of signature `(a, b, c)` provided `a, b, c ≥ 3`. -/
theorem counterexample_of_dvd {A B C x y z a b c : ℕ} (h : IsBealCounterexample A B C x y z)
    (ha : a ∣ x) (hb : b ∣ y) (hc : c ∣ z) (ha3 : 3 ≤ a) (hb3 : 3 ≤ b) (hc3 : 3 ≤ c) :
    IsBealCounterexample (A ^ (x / a)) (B ^ (y / b)) (C ^ (z / c)) a b c := by
  obtain ⟨hA, hB, hC, hx, hy, hz, hg, heq⟩ := h
  refine ⟨by positivity, by positivity, by positivity, ha3, hb3, hc3, gcd_pow_eq_one hg, ?_⟩
  rw [← pow_mul, ← pow_mul, ← pow_mul, Nat.div_mul_cancel ha, Nat.div_mul_cancel hb,
    Nat.div_mul_cancel hc]
  exact heq

/-- **Closed families up to exponent divisibility** (conditional on the five named hypotheses):
no counterexample has `2 ∣ x, 2 ∣ y, 3 ∣ z`; nor `4 ∣ x, 2 ∣ y, 5 ∣ z`; nor `2 ∣ x, 4 ∣ y, 5 ∣ z`. -/
theorem closed_conditional_dvd (hBS : BennettSkinnerThree) (hBCDY : BCDYFourTwoNThree)
    (hM : Mordell27) (h1 : Quartic400g2) (h3 : Quartic400b2)
    {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    ¬ (2 ∣ x ∧ 2 ∣ y ∧ 3 ∣ z) ∧ ¬ (4 ∣ x ∧ 2 ∣ y ∧ 5 ∣ z) ∧ ¬ (2 ∣ x ∧ 4 ∣ y ∧ 5 ∣ z) := by
  have hx : 3 ≤ x := h.2.2.2.1
  have hy : 3 ≤ y := h.2.2.2.2.1
  refine ⟨?_, ?_, ?_⟩
  · rintro ⟨⟨m, rfl⟩, ⟨n, rfl⟩, ⟨k, rfl⟩⟩
    have h' := counterexample_of_dvd h (a := 2 * m) (b := 2 * n) (c := 3) dvd_rfl dvd_rfl
      (dvd_mul_right 3 k) (by omega) (by omega) le_rfl
    rw [Nat.div_self (by omega), Nat.div_self (by omega), pow_one, pow_one] at h'
    exact no_counterexample_even_even_three_all hBS hBCDY hM (by omega) (by omega) h'
  · rintro ⟨⟨m, rfl⟩, ⟨n, rfl⟩, ⟨k, rfl⟩⟩
    have h' := counterexample_of_dvd h (a := 4) (b := 2 * n) (c := 5) (dvd_mul_right 4 m) dvd_rfl
      (dvd_mul_right 5 k) (by norm_num) (by omega) (by norm_num)
    rw [Nat.div_self (by omega), pow_one] at h'
    exact no_counterexample_four_two_n_five h1 h3 (by omega) h'
  · rintro ⟨⟨m, rfl⟩, ⟨n, rfl⟩, ⟨k, rfl⟩⟩
    have h' := counterexample_of_dvd h (a := 2 * m) (b := 4) (c := 5) dvd_rfl (dvd_mul_right 4 n)
      (dvd_mul_right 5 k) (by omega) (by norm_num) (by norm_num)
    rw [Nat.div_self (by omega), pow_one] at h'
    exact no_counterexample_two_m_four_five h1 h3 (by omega) h'

end Beal

namespace Beal

/-- **Darmon–Merel 1997 / Poonen 1998** (BCDY 2015 Table 1, row `(n, n, 2)`, `n ≥ 4`):
`xⁿ + yⁿ = z²` has no solution in coprime nonzero integers. Stated for positive naturals. -/
def DarmonMerelNN2 : Prop :=
  ∀ a b c n : ℕ, 4 ≤ n → 0 < a → 0 < b → 0 < c → Nat.Coprime a b → a ^ n + b ^ n = c ^ 2 → False

/-- Under `DarmonMerelNN2`, no counterexample has `x = y ≥ 4` and `z` even. -/
theorem no_counterexample_nn_even (hDM : DarmonMerelNN2) {A B C n z : ℕ} (hn : 4 ≤ n) (hz : 2 ∣ z)
    (h : IsBealCounterexample A B C n n z) : False := by
  have hab : Nat.Coprime A B := gcd_ab_eq_one h
  obtain ⟨k, rfl⟩ := hz
  obtain ⟨hA, hB, hC, _, _, _, _, heq⟩ := h
  refine hDM A B (C ^ k) n hn hA hB (by positivity) hab ?_
  rw [← pow_mul, mul_comm k 2]; exact heq

end Beal

namespace Beal

/-- Darmon–Merel / Poonen over `ℤ` (signs allowed): for `n ≥ 4`, `xⁿ + yⁿ = z²` has no solution in
coprime nonzero integers. -/
def DarmonMerelNN2Int : Prop :=
  ∀ n : ℕ, 4 ≤ n → ∀ x y z : ℤ, x ≠ 0 → y ≠ 0 → z ≠ 0 → IsCoprime x y → x ^ n + y ^ n ≠ z ^ 2

/-- Under `DarmonMerelNN2Int`, no counterexample of signature `(4, p, p)` with `p ≥ 5` odd
(`Cᵖ + (−B)ᵖ = (A²)²`). -/
theorem no_counterexample_four_pp (hDM : DarmonMerelNN2Int) {A B C p : ℕ} (hp : 5 ≤ p)
    (hodd : Odd p) (h : IsBealCounterexample A B C 4 p p) : False := by
  have hbc : Nat.Coprime B C := gcd_bc_eq_one h
  obtain ⟨hA, hB, hC, _, _, _, _, heq⟩ := h
  have hA0 : (A : ℤ) ^ 2 ≠ 0 := pow_ne_zero _ (by exact_mod_cast hA.ne')
  have hB0 : (-(B : ℤ)) ≠ 0 := neg_ne_zero.mpr (by exact_mod_cast hB.ne')
  have hC0 : (C : ℤ) ≠ 0 := by exact_mod_cast hC.ne'
  have hcop : IsCoprime (C : ℤ) (-(B : ℤ)) := (Nat.isCoprime_iff_coprime.mpr hbc.symm).neg_right
  refine hDM p (by omega) (C : ℤ) (-(B : ℤ)) ((A : ℤ) ^ 2) hC0 hB0 hA0 hcop ?_
  rw [hodd.neg_pow, ← pow_mul]
  have : ((A : ℤ) ^ 4 + (B : ℤ) ^ p) = (C : ℤ) ^ p := by exact_mod_cast heq
  linear_combination -this

/-- Symmetric: `(p, 4, p)`. -/
theorem no_counterexample_p_four_p (hDM : DarmonMerelNN2Int) {A B C p : ℕ} (hp : 5 ≤ p)
    (hodd : Odd p) (h : IsBealCounterexample A B C p 4 p) : False :=
  no_counterexample_four_pp hDM hp hodd (swap_counterexample h)

end Beal

namespace Beal

/-- The residual shape after the conditional closures: on top of `ResidualShape`, the reduced
signature is not `(4,4,3)`, `(4,4,5)`, `(n,n,4)` with `n ≥ 4`, `(4,p,p)` or `(p,4,p)` with `p ≥ 5`. -/
def ConditionalResidual (A B C x y z : ℕ) : Prop :=
  ResidualShape A B C x y z ∧
  ¬ (x = 4 ∧ y = 4 ∧ z = 3) ∧ ¬ (x = 4 ∧ y = 4 ∧ z = 5) ∧
  ¬ (x = y ∧ 4 ≤ x ∧ z = 4) ∧ ¬ (x = 4 ∧ y = z ∧ 5 ≤ y) ∧ ¬ (y = 4 ∧ x = z ∧ 5 ≤ x)

/-- **Conditional "what remains".** Under the seven named hypotheses, any counterexample yields a
`ConditionalResidual`. -/
theorem conditional_residual_of_counterexample (hBS : BennettSkinnerThree)
    (hBCDY : BCDYFourTwoNThree) (hM : Mordell27) (h1 : Quartic400g2) (h3 : Quartic400b2)
    (hDM : DarmonMerelNN2) (hDMI : DarmonMerelNN2Int)
    {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    ∃ A' B' C' x' y' z' : ℕ, ConditionalResidual A' B' C' x' y' z' := by
  obtain ⟨A', B', C', x', y', z', hr⟩ := residual_of_counterexample h
  refine ⟨A', B', C', x', y', z', hr, ?_, ?_, ?_, ?_, ?_⟩
  · rintro ⟨rfl, rfl, rfl⟩
    exact no_counterexample_even_even_three_all hBS hBCDY hM (m := 2) (n := 2) le_rfl le_rfl hr.1
  · rintro ⟨rfl, rfl, rfl⟩
    exact no_counterexample_four_two_n_five h1 h3 (n := 2) le_rfl hr.1
  · rintro ⟨rfl, hx4, rfl⟩
    exact no_counterexample_nn_even hDM hx4 ⟨2, rfl⟩ hr.1
  · rintro ⟨rfl, rfl, hy5⟩
    have hodd : Odd y' := by
      rcases hr.2.2.1 with h4 | ⟨_, ho⟩
      · omega
      · exact ho
    exact no_counterexample_four_pp hDMI hy5 hodd hr.1
  · rintro ⟨rfl, rfl, hx5⟩
    have hodd : Odd x' := by
      rcases hr.2.1 with h4 | ⟨_, ho⟩
      · omega
      · exact ho
    exact no_counterexample_p_four_p hDMI hx5 hodd hr.1

end Beal

namespace Beal

/-- **BCDY 2015 Theorem 1, row `(3, 3, 2n)`, `n ≥ 2`:** no coprime nonzero solution of `x³ + y³ = z^{2n}`. -/
def BCDYThreeThreeTwoN : Prop :=
  ∀ a b c n : ℕ, 2 ≤ n → 0 < a → 0 < b → 0 < c → Nat.Coprime a b → a ^ 3 + b ^ 3 = c ^ (2 * n) → False

theorem no_counterexample_three_three_even (hT : BCDYThreeThreeTwoN) {A B C z : ℕ} (hz : 2 ∣ z)
    (h : IsBealCounterexample A B C 3 3 z) : False := by
  have hab : Nat.Coprime A B := gcd_ab_eq_one h
  obtain ⟨k, rfl⟩ := hz
  obtain ⟨hA, hB, hC, _, _, hz3, _, heq⟩ := h
  exact hT A B C k (by omega) hA hB hC hab heq

/-- Residual after adding `(3, 3, 2n)`: also not `(3, 3, 4)`. -/
theorem conditional_residual_of_counterexample' (hBS : BennettSkinnerThree)
    (hBCDY : BCDYFourTwoNThree) (hM : Mordell27) (h1 : Quartic400g2) (h3 : Quartic400b2)
    (hDM : DarmonMerelNN2) (hDMI : DarmonMerelNN2Int) (hT : BCDYThreeThreeTwoN)
    {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    ∃ A' B' C' x' y' z' : ℕ, ConditionalResidual A' B' C' x' y' z' ∧ ¬ (x' = 3 ∧ y' = 3 ∧ z' = 4) := by
  obtain ⟨A', B', C', x', y', z', hr⟩ :=
    conditional_residual_of_counterexample hBS hBCDY hM h1 h3 hDM hDMI h
  refine ⟨A', B', C', x', y', z', hr, ?_⟩
  rintro ⟨rfl, rfl, rfl⟩
  exact no_counterexample_three_three_even hT ⟨2, rfl⟩ hr.1.1

end Beal

namespace Beal

/-- Fermat's Last Theorem (Wiles 1995, Taylor–Wiles), positive-integer form. -/
def FLTHyp : Prop := ∀ a b c n : ℕ, 3 ≤ n → 0 < a → 0 < b → 0 < c → a ^ n + b ^ n = c ^ n → False

/-- Darmon–Merel 1997 / Poonen 1998, `(n, n, 3)`, `n ≥ 3` (BCDY Table 1). -/
def DarmonMerelNN3 : Prop :=
  ∀ a b c n : ℕ, 3 ≤ n → 0 < a → 0 < b → 0 < c → Nat.Coprime a b → a ^ n + b ^ n = c ^ 3 → False

/-- Dahmen–Siksek (BCDY Table 2): `(5,5,7)`, `(5,5,19)`, `(7,7,5)` have no coprime solutions. -/
def DahmenSiksek : Prop :=
  ∀ a b c : ℕ, 0 < a → 0 < b → 0 < c → Nat.Coprime a b →
    (a ^ 5 + b ^ 5 ≠ c ^ 7) ∧ (a ^ 5 + b ^ 5 ≠ c ^ 19) ∧ (a ^ 7 + b ^ 7 ≠ c ^ 5)

/-- **Residual matching the published frontier** (eleven named hypotheses). -/
theorem published_residual (hBS : BennettSkinnerThree) (hBCDY : BCDYFourTwoNThree)
    (hM : Mordell27) (h1 : Quartic400g2) (h3 : Quartic400b2) (hDM : DarmonMerelNN2)
    (hDMI : DarmonMerelNN2Int) (hT : BCDYThreeThreeTwoN) (hF : FLTHyp) (hD3 : DarmonMerelNN3)
    (hDS : DahmenSiksek) {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    ∃ A' B' C' x' y' z' : ℕ, ConditionalResidual A' B' C' x' y' z' ∧
      ¬ (x' = 3 ∧ y' = 3 ∧ z' = 4) ∧ ¬ (x' = y' ∧ y' = z') ∧ ¬ (x' = y' ∧ z' = 3) ∧
      ¬ (x' = 5 ∧ y' = 5 ∧ z' = 7) ∧ ¬ (x' = 5 ∧ y' = 5 ∧ z' = 19) ∧ ¬ (x' = 7 ∧ y' = 7 ∧ z' = 5) := by
  obtain ⟨A', B', C', x', y', z', hr, h334⟩ :=
    conditional_residual_of_counterexample' hBS hBCDY hM h1 h3 hDM hDMI hT h
  have hc := hr.1.1
  have hab : Nat.Coprime A' B' := gcd_ab_eq_one hc
  obtain ⟨hA, hB, hC, hx, hy, hz, _, heq⟩ := hc
  refine ⟨A', B', C', x', y', z', hr, h334, ?_, ?_, ?_, ?_, ?_⟩
  · rintro ⟨rfl, rfl⟩; exact hF A' B' C' x' hx hA hB hC heq
  · rintro ⟨rfl, rfl⟩; exact hD3 A' B' C' x' hx hA hB hC hab heq
  · rintro ⟨rfl, rfl, rfl⟩; exact (hDS A' B' C' hA hB hC hab).1 heq
  · rintro ⟨rfl, rfl, rfl⟩; exact (hDS A' B' C' hA hB hC hab).2.1 heq
  · rintro ⟨rfl, rfl, rfl⟩; exact (hDS A' B' C' hA hB hC hab).2.2 heq

end Beal

namespace Beal

/-- **Ellenberg; Bennett–Ellenberg–Ng 2010; Bruin** (BCDY 2015 Table 1, row `(2, 4, n)`, `n ≥ 4`):
`x² + y⁴ = zⁿ` has no solution in coprime nonzero integers. Positive-natural form. -/
def BEN24n : Prop :=
  ∀ a b c n : ℕ, 4 ≤ n → 0 < a → 0 < b → 0 < c → Nat.Coprime a b → a ^ 2 + b ^ 4 = c ^ n → False

/-- Under `BEN24n`: no counterexample with `4 ∣ x`, `2 ∣ y`, `z ≥ 4` (so `(4,4,p)` is closed for all
`p ≥ 5`, and every `(4k, 2j, z)`). -/
theorem no_counterexample_four_even_any (hBEN : BEN24n) {A B C x y z : ℕ} (hx : 4 ∣ x) (hy : 2 ∣ y)
    (hz : 4 ≤ z) (h : IsBealCounterexample A B C x y z) : False := by
  have hab : Nat.Coprime A B := gcd_ab_eq_one h
  obtain ⟨k, rfl⟩ := hx
  obtain ⟨j, rfl⟩ := hy
  obtain ⟨hA, hB, hC, _, _, _, _, heq⟩ := h
  refine hBEN (B ^ j) (A ^ k) C z hz (by positivity) (by positivity) hC
    ((hab.symm.pow_left j).pow_right k) ?_
  rw [← pow_mul, ← pow_mul, mul_comm j 2, mul_comm k 4, add_comm]; exact heq

end Beal

namespace Beal

/-- "No coprime positive solution of `a^x + b^y = c^z`." -/
def NoCoprimeSol (x y z : ℕ) : Prop :=
  ∀ a b c : ℕ, 0 < a → 0 < b → 0 < c → Nat.Coprime a b → a ^ x + b ^ y = c ^ z → False

/-- Literature rows found by the instance check U168 (all over `ℤ`, so every arrangement follows,
the moved exponents being odd): Poonen–Schaefer–Stoll `x²+y³=z⁷` (no solution with `x` a square),
Siksek–Stoll `(3,4,5)`, Cohen GTM 240 Prop. 14.6.6 `(3,4,4)`, and `(2,n,4)` for `(p,4,4)`, `p ≥ 5`. -/
structure InstanceRows : Prop where
  pss347 : NoCoprimeSol 3 4 7 ∧ NoCoprimeSol 3 7 4 ∧ NoCoprimeSol 4 7 3
  ss345 : NoCoprimeSol 3 4 5 ∧ NoCoprimeSol 3 5 4 ∧ NoCoprimeSol 4 5 3
  cohen344 : NoCoprimeSol 3 4 4
  p44 : ∀ p, 5 ≤ p → NoCoprimeSol p 4 4

theorem no_counterexample_of_noCoprimeSol {x y z : ℕ} (hN : NoCoprimeSol x y z) {A B C : ℕ}
    (h : IsBealCounterexample A B C x y z) : False := by
  have hab : Nat.Coprime A B := gcd_ab_eq_one h
  obtain ⟨hA, hB, hC, _, _, _, _, heq⟩ := h
  exact hN A B C hA hB hC hab heq

/-- Signatures `{3,4,7}`, `{3,4,5}` (every arrangement), `(3,4,4)`, `(4,3,4)`.
The `(p,4,4)`, `(4,p,4)` rows are the separate theorem `closed_p_four_four` below. -/
theorem closed_instance_rows (hI : InstanceRows) {A B C x y z : ℕ}
    (h : IsBealCounterexample A B C x y z) :
    ¬ ((x, y, z) ∈ ({(3,4,7),(4,3,7),(3,7,4),(7,3,4),(4,7,3),(7,4,3),
                     (3,4,5),(4,3,5),(3,5,4),(5,3,4),(4,5,3),(5,4,3),(3,4,4),(4,3,4)} :
                     Finset (ℕ × ℕ × ℕ))) := by
  intro hm
  simp only [Finset.mem_insert, Finset.mem_singleton, Prod.mk.injEq] at hm
  rcases hm with ⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|
    ⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩|⟨rfl,rfl,rfl⟩
  · exact no_counterexample_of_noCoprimeSol hI.pss347.1 h
  · exact no_counterexample_of_noCoprimeSol hI.pss347.1 (swap_counterexample h)
  · exact no_counterexample_of_noCoprimeSol hI.pss347.2.1 h
  · exact no_counterexample_of_noCoprimeSol hI.pss347.2.1 (swap_counterexample h)
  · exact no_counterexample_of_noCoprimeSol hI.pss347.2.2 h
  · exact no_counterexample_of_noCoprimeSol hI.pss347.2.2 (swap_counterexample h)
  · exact no_counterexample_of_noCoprimeSol hI.ss345.1 h
  · exact no_counterexample_of_noCoprimeSol hI.ss345.1 (swap_counterexample h)
  · exact no_counterexample_of_noCoprimeSol hI.ss345.2.1 h
  · exact no_counterexample_of_noCoprimeSol hI.ss345.2.1 (swap_counterexample h)
  · exact no_counterexample_of_noCoprimeSol hI.ss345.2.2 h
  · exact no_counterexample_of_noCoprimeSol hI.ss345.2.2 (swap_counterexample h)
  · exact no_counterexample_of_noCoprimeSol hI.cohen344 h
  · exact no_counterexample_of_noCoprimeSol hI.cohen344 (swap_counterexample h)

/-- `(p, 4, 4)` and `(4, p, 4)` for `p ≥ 5`, under `InstanceRows.p44` (the `(2, n, 4)` row). -/
theorem closed_p_four_four (hI : InstanceRows) {A B C p : ℕ} (hp : 5 ≤ p) :
    ¬ IsBealCounterexample A B C p 4 4 ∧ ¬ IsBealCounterexample A B C 4 p 4 :=
  ⟨fun h => no_counterexample_of_noCoprimeSol (hI.p44 p hp) h,
   fun h => no_counterexample_of_noCoprimeSol (hI.p44 p hp) (swap_counterexample h)⟩

/-- **The residual after every closure in this repository** (named hypotheses: the eleven of
`published_residual`, plus `BEN24n` and `InstanceRows`). In addition to `published_residual`:
no reduced residual has `x' = y' = 4`; none is an arrangement of `{3,4,7}` or `{3,4,5}`;
none is `(3,4,4)`, `(4,3,4)`, `(p,4,4)` or `(4,p,4)` with `p ≥ 5`. -/
theorem final_residual (hBS : BennettSkinnerThree) (hBCDY : BCDYFourTwoNThree)
    (hM : Mordell27) (h1 : Quartic400g2) (h3 : Quartic400b2) (hDM : DarmonMerelNN2)
    (hDMI : DarmonMerelNN2Int) (hT : BCDYThreeThreeTwoN) (hF : FLTHyp) (hD3 : DarmonMerelNN3)
    (hDS : DahmenSiksek) (hBEN : BEN24n) (hI : InstanceRows)
    {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    ∃ A' B' C' x' y' z' : ℕ, IsBealCounterexample A' B' C' x' y' z' ∧
      Reduced x' ∧ Reduced y' ∧ Reduced z' ∧
      ¬ (x' = 4 ∧ y' = 4) ∧
      ¬ ((x', y', z') ∈ ({(3,4,7),(4,3,7),(3,7,4),(7,3,4),(4,7,3),(7,4,3),
                          (3,4,5),(4,3,5),(3,5,4),(5,3,4),(4,5,3),(5,4,3),(3,4,4),(4,3,4)} :
                          Finset (ℕ × ℕ × ℕ))) ∧
      ¬ (5 ≤ x' ∧ y' = 4 ∧ z' = 4) ∧ ¬ (x' = 4 ∧ 5 ≤ y' ∧ z' = 4) ∧
      ¬ (x' = y' ∧ y' = z') ∧ ¬ (x' = y' ∧ z' = 3) ∧ ¬ (x' = y' ∧ 4 ≤ x' ∧ z' = 4) ∧
      ¬ (x' = 4 ∧ y' = z' ∧ 5 ≤ y') ∧ ¬ (y' = 4 ∧ x' = z' ∧ 5 ≤ x') ∧
      ¬ (x' = 3 ∧ y' = 3 ∧ z' = 4) := by
  obtain ⟨A', B', C', x', y', z', hr, h334, hdiag, hnn3, _, _, _⟩ :=
    published_residual hBS hBCDY hM h1 h3 hDM hDMI hT hF hD3 hDS h
  obtain ⟨⟨hc, hx, hy, hz, _⟩, _, _, hnn4, h4pp, hp4p⟩ := hr
  refine ⟨A', B', C', x', y', z', hc, hx, hy, hz, ?_, closed_instance_rows hI hc, ?_, ?_,
    hdiag, hnn3, hnn4, h4pp, hp4p, h334⟩
  · rintro ⟨rfl, rfl⟩
    rcases hz with rfl | ⟨hp, hodd⟩
    · exact no_counterexample_of_four_four_even (by norm_num) (by norm_num) (by norm_num) hc
    · rcases Nat.lt_or_ge z' 4 with hlt | hge
      · have h3 : z' = 3 := by have := hp.two_le; rw [Nat.odd_iff] at hodd; omega
        subst h3
        exact no_counterexample_even_even_three_all hBS hBCDY hM (m := 2) (n := 2) le_rfl le_rfl hc
      · exact no_counterexample_four_even_any hBEN ⟨1, rfl⟩ ⟨2, rfl⟩ hge hc
  · rintro ⟨hp5, rfl, rfl⟩; exact (closed_p_four_four hI hp5).1 hc
  · rintro ⟨rfl, hp5, rfl⟩; exact (closed_p_four_four hI hp5).2 hc

end Beal
