/-
# Elementary structure of a Beal counterexample

Unconditional, kernel-verified constraints on any counterexample.
No `sorry`, no custom `axiom`s, no external deep theorems.
-/
import Beal.ExponentReduction
import Mathlib.NumberTheory.FLT.Four
import Mathlib.NumberTheory.FLT.Three
import Mathlib.Tactic.IntervalCases

namespace Beal

/-- **The bases are pairwise coprime: `gcd A B = 1`.**
A prime dividing `A` and `B` divides `A^x + B^y = C^z`, hence divides `C`, hence divides
`gcd (gcd A B) C = 1`. -/
theorem gcd_ab_eq_one {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    Nat.gcd A B = 1 := by
  obtain ⟨hA, hB, hC, hx, hy, hz, hgcd, heq⟩ := h
  rw [Nat.eq_one_iff_not_exists_prime_dvd]
  rintro p hp hdvd
  have hpA : p ∣ A := hdvd.trans (Nat.gcd_dvd_left A B)
  have hpB : p ∣ B := hdvd.trans (Nat.gcd_dvd_right A B)
  have hpC : p ∣ C := by
    refine hp.dvd_of_dvd_pow (n := z) ?_
    rw [← heq]
    exact Nat.dvd_add (dvd_pow hpA (by omega)) (dvd_pow hpB (by omega))
  have hfin : p ∣ gcd3 A B C := by
    unfold gcd3
    exact Nat.dvd_gcd hpA (Nat.dvd_gcd hpB hpC)
  rw [hgcd] at hfin
  exact hp.one_lt.ne' (Nat.dvd_one.mp hfin)

/-- `gcd A C = 1`.  A prime dividing `A` and `C` divides `B^y = C^z - A^x`. -/
theorem gcd_ac_eq_one {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    Nat.gcd A C = 1 := by
  have hab := gcd_ab_eq_one h
  obtain ⟨hA, hB, hC, hx, hy, hz, hgcd, heq⟩ := h
  rw [Nat.eq_one_iff_not_exists_prime_dvd]
  rintro p hp hdvd
  have hpA : p ∣ A := hdvd.trans (Nat.gcd_dvd_left A C)
  have hpC : p ∣ C := hdvd.trans (Nat.gcd_dvd_right A C)
  have hpB : p ∣ B := by
    refine hp.dvd_of_dvd_pow (n := y) ?_
    have hsub : B ^ y = C ^ z - A ^ x := by omega
    rw [hsub]
    exact Nat.dvd_sub' (dvd_pow hpC (by omega)) (dvd_pow hpA (by omega))
  have hfin : p ∣ Nat.gcd A B := Nat.dvd_gcd hpA hpB
  rw [hab] at hfin
  exact hp.one_lt.ne' (Nat.dvd_one.mp hfin)

/-- `gcd B C = 1`. -/
theorem gcd_bc_eq_one {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    Nat.gcd B C = 1 := by
  have hab := gcd_ab_eq_one h
  obtain ⟨hA, hB, hC, hx, hy, hz, hgcd, heq⟩ := h
  rw [Nat.eq_one_iff_not_exists_prime_dvd]
  rintro p hp hdvd
  have hpB : p ∣ B := hdvd.trans (Nat.gcd_dvd_left B C)
  have hpC : p ∣ C := hdvd.trans (Nat.gcd_dvd_right B C)
  have hpA : p ∣ A := by
    refine hp.dvd_of_dvd_pow (n := x) ?_
    have hsub : A ^ x = C ^ z - B ^ y := by omega
    rw [hsub]
    exact Nat.dvd_sub' (dvd_pow hpC (by omega)) (dvd_pow hpB (by omega))
  have hfin : p ∣ Nat.gcd A B := Nat.dvd_gcd hpA hpB
  rw [hab] at hfin
  exact hp.one_lt.ne' (Nat.dvd_one.mp hfin)

/-- Two is not a perfect power with exponent at least 3. -/
private theorem two_ne_pow {C z : ℕ} (hz : 3 ≤ z) : C ^ z ≠ 2 := by
  intro hC2
  have h : C = 0 ∨ C = 1 ∨ 2 ≤ C := by omega
  rcases h with rfl | rfl | hge
  · rw [zero_pow (by omega)] at hC2; omega
  · rw [one_pow] at hC2; omega
  · have h8 : (8 : ℕ) ≤ C ^ z := by
      calc (8 : ℕ) = 2 ^ 3 := by norm_num
        _ ≤ 2 ^ z := Nat.pow_le_pow_right (by omega) hz
        _ ≤ C ^ z := Nat.pow_le_pow_left hge z
    omega

/-- **No Beal counterexample has `A = B`.**
Pairwise coprimality forces `A = gcd A A = 1`, so the equation reads `1 + 1 = C^z` with
`z ≥ 3`, and `2` is not a perfect power of exponent `≥ 3`. -/
theorem not_eq_bases {A C x y z : ℕ} (h : IsBealCounterexample A A C x y z) : False := by
  have hab := gcd_ab_eq_one h
  rw [Nat.gcd_self] at hab
  obtain ⟨hA, hB, hC, hx, hy, hz, hgcd, heq⟩ := h
  subst hab
  rw [one_pow, one_pow] at heq
  exact two_ne_pow hz heq.symm

/-- **No Beal counterexample has `A = B = 1`.** -/
theorem not_both_one {C x y z : ℕ} (h : IsBealCounterexample 1 1 C x y z) : False :=
  not_eq_bases h



/-! ## A non-diagonal infinite family via mathlib's `not_fermat_42` -/

section FourFourEven

/-- **No Beal counterexample has `4 ∣ x`, `4 ∣ y` and `z` even.**

Writing `x = 4a`, `y = 4b`, `z = 2c` turns the equation into
`(A^a)^4 + (B^b)^4 = (C^c)^2`, which mathlib's `not_fermat_42` forbids.

This family is genuinely **non-diagonal**: the three exponents vary independently over the
infinite sets `4ℕ`, `4ℕ` and `2ℕ`.  It subsumes the diagonal family `(n,n,n)` with `4 ∣ n`.
No coprimality hypothesis is used, so the equation itself has no positive solutions. -/
theorem no_counterexample_of_four_four_even {A B C x y z : ℕ}
    (hx : 4 ∣ x) (hy : 4 ∣ y) (hz : 2 ∣ z)
    (h : IsBealCounterexample A B C x y z) : False := by
  obtain ⟨hA, hB, hC, hx3, hy3, hz3, _, heq⟩ := h
  obtain ⟨a, ha⟩ := hx
  obtain ⟨b, hb⟩ := hy
  obtain ⟨c, hc⟩ := hz
  have hA' : ((A ^ a : ℕ) : ℤ) ≠ 0 := by
    have : 0 < A ^ a := Nat.pos_pow_of_pos _ hA
    exact Int.natCast_ne_zero.mpr (by omega)
  have hB' : ((B ^ b : ℕ) : ℤ) ≠ 0 := by
    have : 0 < B ^ b := Nat.pos_pow_of_pos _ hB
    exact Int.natCast_ne_zero.mpr (by omega)
  refine not_fermat_42 (c := ((C ^ c : ℕ) : ℤ)) hA' hB' ?_
  have hnat : (A ^ a) ^ 4 + (B ^ b) ^ 4 = (C ^ c) ^ 2 := by
    rw [← pow_mul, ← pow_mul, ← pow_mul, mul_comm a 4, mul_comm b 4, mul_comm c 2,
      ← ha, ← hb, ← hc]
    exact heq
  exact_mod_cast hnat

/-- Instance: signature `(4, 4, 2k)` for every `k ≥ 2`. -/
theorem no_counterexample_4_4_two_mul {A B C k : ℕ}
    (h : IsBealCounterexample A B C 4 4 (2 * k)) : False :=
  no_counterexample_of_four_four_even ⟨1, by norm_num⟩ ⟨1, by norm_num⟩ ⟨k, rfl⟩ h

/-- Instance: signature `(8, 12, 6)` — exponents pairwise distinct. -/
theorem no_counterexample_8_12_6 {A B C : ℕ}
    (h : IsBealCounterexample A B C 8 12 6) : False :=
  no_counterexample_of_four_four_even ⟨2, by norm_num⟩ ⟨3, by norm_num⟩ ⟨3, by norm_num⟩ h

end FourFourEven



/-! ## A second non-diagonal family via mathlib's FLT for exponent 3 -/

section ThreeThreeThree

/-- **No Beal counterexample has `3 ∣ x`, `3 ∣ y` and `3 ∣ z`.**

Writing `x = 3a`, `y = 3b`, `z = 3c` gives `(A^a)^3 + (B^b)^3 = (C^c)^3`, forbidden by
mathlib's `fermatLastTheoremThree`.  Again non-diagonal and requiring no coprimality. -/
theorem no_counterexample_of_three_dvd_all {A B C x y z : ℕ}
    (hx : 3 ∣ x) (hy : 3 ∣ y) (hz : 3 ∣ z)
    (h : IsBealCounterexample A B C x y z) : False := by
  obtain ⟨hA, hB, hC, hx3, hy3, hz3, _, heq⟩ := h
  obtain ⟨a, ha⟩ := hx
  obtain ⟨b, hb⟩ := hy
  obtain ⟨c, hc⟩ := hz
  refine fermatLastTheoremThree (A ^ a) (B ^ b) (C ^ c)
    (by have : 0 < A ^ a := Nat.pos_pow_of_pos _ hA; omega)
    (by have : 0 < B ^ b := Nat.pos_pow_of_pos _ hB; omega)
    (by have : 0 < C ^ c := Nat.pos_pow_of_pos _ hC; omega) ?_
  rw [← pow_mul, ← pow_mul, ← pow_mul, mul_comm a 3, mul_comm b 3, mul_comm c 3,
    ← ha, ← hb, ← hc]
  exact heq

/-- Instance: the Fermat cubic signature `(3,3,3)`. -/
theorem no_counterexample_3_3_3 {A B C : ℕ}
    (h : IsBealCounterexample A B C 3 3 3) : False :=
  no_counterexample_of_three_dvd_all ⟨1, by norm_num⟩ ⟨1, by norm_num⟩ ⟨1, by norm_num⟩ h

/-- Instance: signature `(6, 9, 12)` — exponents pairwise distinct. -/
theorem no_counterexample_6_9_12 {A B C : ℕ}
    (h : IsBealCounterexample A B C 6 9 12) : False :=
  no_counterexample_of_three_dvd_all ⟨2, by norm_num⟩ ⟨3, by norm_num⟩ ⟨4, by norm_num⟩ h

/-- Every diagonal signature `(n,n,n)` with `n ≥ 3` divisible by 3 or by 4 is excluded. -/
theorem no_counterexample_diagonal_of_three_or_four {A B C n : ℕ}
    (hn : 3 ∣ n ∨ 4 ∣ n) (h : IsBealCounterexample A B C n n n) : False := by
  rcases hn with h3 | h4
  · exact no_counterexample_of_three_dvd_all h3 h3 h3 h
  · exact no_counterexample_diagonal_of_four_dvd h4 h

end ThreeThreeThree



/-! ## Unified statement of the verified coverage -/

section Unified

/-- **Unified coverage theorem.**  If `3 ∣ gcd(x,y,z)` or `4 ∣ gcd(x,y,z)`, then
`A^x + B^y = C^z` has no positive solutions, so no Beal counterexample has such a signature.

This packages the two verified families: `3 ∣ d` gives `3 ∣ x, y, z` (mathlib
`fermatLastTheoremThree`), and `4 ∣ d` gives `4 ∣ x`, `4 ∣ y` and `z` even (mathlib
`not_fermat_42`).  No coprimality hypothesis is used. -/
theorem no_counterexample_of_three_or_four_dvd_gcd {A B C x y z : ℕ}
    (h3or4 : 3 ∣ Nat.gcd x (Nat.gcd y z) ∨ 4 ∣ Nat.gcd x (Nat.gcd y z))
    (h : IsBealCounterexample A B C x y z) : False := by
  have hx : ∀ {d : ℕ}, d ∣ Nat.gcd x (Nat.gcd y z) → d ∣ x :=
    fun hd => hd.trans (Nat.gcd_dvd_left x _)
  have hy : ∀ {d : ℕ}, d ∣ Nat.gcd x (Nat.gcd y z) → d ∣ y :=
    fun hd => hd.trans ((Nat.gcd_dvd_right x _).trans (Nat.gcd_dvd_left y z))
  have hz : ∀ {d : ℕ}, d ∣ Nat.gcd x (Nat.gcd y z) → d ∣ z :=
    fun hd => hd.trans ((Nat.gcd_dvd_right x _).trans (Nat.gcd_dvd_right y z))
  rcases h3or4 with hd | hd
  · exact no_counterexample_of_three_dvd_all (hx hd) (hy hd) (hz hd) h
  · exact no_counterexample_of_four_four_even (hx hd) (hy hd)
      ((by norm_num : (2 : ℕ) ∣ 4).trans (hz hd)) h

end Unified



/-! ## The all-even case is a Pythagorean triple of perfect powers -/

section AllEven

/-- **Reduction of the all-even case.**
If a Beal counterexample has all three exponents even, `x = 2r`, `y = 2s`, `z = 2t`, then
`(A^r, B^s, C^t)` is a **primitive Pythagorean triple** whose three entries are perfect powers
with exponents `r, s, t ≥ 2`.

This is the precise sense in which the all-even branch is the problem of perfect powers in
Pythagorean triples. Note `x ≥ 3` and `x = 2r` force `r ≥ 2`, so the exponents really are `≥ 2`
and the triple is not merely `(A, B, C)` itself. -/
theorem allEven_isPythagorean {A B C r s t : ℕ}
    (h : IsBealCounterexample A B C (2 * r) (2 * s) (2 * t)) :
    (A ^ r) ^ 2 + (B ^ s) ^ 2 = (C ^ t) ^ 2 ∧
      gcd3 (A ^ r) (B ^ s) (C ^ t) = 1 ∧
      2 ≤ r ∧ 2 ≤ s ∧ 2 ≤ t ∧ 0 < A ^ r ∧ 0 < B ^ s ∧ 0 < C ^ t := by
  obtain ⟨hA, hB, hC, hx, hy, hz, hgcd, heq⟩ := h
  refine ⟨?_, gcd_pow_eq_one hgcd, by omega, by omega, by omega,
    Nat.pos_pow_of_pos _ hA, Nat.pos_pow_of_pos _ hB, Nat.pos_pow_of_pos _ hC⟩
  rw [← pow_mul, ← pow_mul, ← pow_mul, mul_comm r 2, mul_comm s 2, mul_comm t 2]
  exact heq

/-- In the all-even case the three perfect-power entries are **pairwise** coprime. -/
theorem allEven_pairwise_coprime {A B C r s t : ℕ}
    (h : IsBealCounterexample A B C (2 * r) (2 * s) (2 * t)) :
    Nat.gcd (A ^ r) (B ^ s) = 1 ∧ Nat.gcd (A ^ r) (C ^ t) = 1 ∧
      Nat.gcd (B ^ s) (C ^ t) = 1 := by
  have h1 := gcd_ab_eq_one h
  have h2 := gcd_ac_eq_one h
  have h3 := gcd_bc_eq_one h
  exact ⟨Nat.Coprime.pow _ _ h1, Nat.Coprime.pow _ _ h2, Nat.Coprime.pow _ _ h3⟩

end AllEven



/-! ## Parity: exactly one of the three bases is even

Jev's ranking over a 300-element mechanism space put valuation / p-adic reasoning at the top.
At `p = 2` it gives a clean trichotomy, from pairwise coprimality alone.
-/

section Parity

/-- **Exactly one of `A`, `B`, `C` is even.**

Not both `A` and `B`, by coprimality.  And if `A` and `B` are both odd then `A^x + B^y` is even,
so `C` is even.  Hence exactly one. -/
theorem exactly_one_even {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    (A % 2 = 0 ∧ B % 2 = 1 ∧ C % 2 = 1) ∨
    (A % 2 = 1 ∧ B % 2 = 0 ∧ C % 2 = 1) ∨
    (A % 2 = 1 ∧ B % 2 = 1 ∧ C % 2 = 0) := by
  have hab := gcd_ab_eq_one h
  have hac := gcd_ac_eq_one h
  have hbc := gcd_bc_eq_one h
  obtain ⟨hA, hB, hC, hx, hy, hz, _, heq⟩ := h
  -- A and B are not both even
  have hnAB : ¬ (A % 2 = 0 ∧ B % 2 = 0) := by
    rintro ⟨h1, h2⟩
    have : 2 ∣ Nat.gcd A B := Nat.dvd_gcd (Nat.dvd_of_mod_eq_zero h1) (Nat.dvd_of_mod_eq_zero h2)
    rw [hab] at this
    exact absurd (Nat.le_of_dvd one_pos this) (by omega)
  have hnAC : ¬ (A % 2 = 0 ∧ C % 2 = 0) := by
    rintro ⟨h1, h2⟩
    have : 2 ∣ Nat.gcd A C := Nat.dvd_gcd (Nat.dvd_of_mod_eq_zero h1) (Nat.dvd_of_mod_eq_zero h2)
    rw [hac] at this
    exact absurd (Nat.le_of_dvd one_pos this) (by omega)
  have hnBC : ¬ (B % 2 = 0 ∧ C % 2 = 0) := by
    rintro ⟨h1, h2⟩
    have : 2 ∣ Nat.gcd B C := Nat.dvd_gcd (Nat.dvd_of_mod_eq_zero h1) (Nat.dvd_of_mod_eq_zero h2)
    rw [hbc] at this
    exact absurd (Nat.le_of_dvd one_pos this) (by omega)
  -- parity of the equation: A^x + B^y = C^z
  have pA : A ^ x % 2 = A % 2 := by
    rw [Nat.pow_mod]
    rcases Nat.mod_two_eq_zero_or_one A with h' | h'
    · rw [h', Nat.zero_pow (by omega : 0 < x)]
    · rw [h', one_pow]
      norm_num
  have pB : B ^ y % 2 = B % 2 := by
    rw [Nat.pow_mod]
    rcases Nat.mod_two_eq_zero_or_one B with h' | h'
    · rw [h', Nat.zero_pow (by omega : 0 < y)]
    · rw [h', one_pow]
      norm_num
  have pC : C ^ z % 2 = C % 2 := by
    rw [Nat.pow_mod]
    rcases Nat.mod_two_eq_zero_or_one C with h' | h'
    · rw [h', Nat.zero_pow (by omega : 0 < z)]
    · rw [h', one_pow]
      norm_num
  have hsum : (A ^ x + B ^ y) % 2 = C ^ z % 2 := by rw [heq]
  rcases Nat.mod_two_eq_zero_or_one A with hA2 | hA2 <;>
    rcases Nat.mod_two_eq_zero_or_one B with hB2 | hB2 <;>
      rcases Nat.mod_two_eq_zero_or_one C with hC2 | hC2 <;> omega

end Parity



/-! ## A mod-8 condition: if `C` is even, the exponents `x` and `y` are not both even

Found by drilling into the p-adic direction that Jev's 300-mechanism ranking put first.

If `C` is even then `A` and `B` are both odd (`exactly_one_even`), and `8 ∣ C^z` because
`z ≥ 3`.  For odd `n`, `n^2 ≡ 1 (mod 8)`, so an even exponent sends `A^x` and `B^y` both to
`1 (mod 8)` and their sum to `2`, which is never `0`.
-/

section ModEight

/-- For odd `n` and even `k`, `n ^ k ≡ 1 (mod 8)`. -/
theorem odd_pow_even_mod_eight {n k : ℕ} (hn : n % 2 = 1) (hk : k % 2 = 0) :
    n ^ k % 8 = 1 := by
  obtain ⟨j, rfl⟩ : ∃ j, k = 2 * j := ⟨k / 2, by omega⟩
  rw [pow_mul, Nat.pow_mod]
  have h8 : n ^ 2 % 8 = 1 := by
    have : n % 8 = 1 ∨ n % 8 = 3 ∨ n % 8 = 5 ∨ n % 8 = 7 := by omega
    rw [Nat.pow_mod]
    rcases this with h | h | h | h <;> rw [h] <;> norm_num
  rw [h8, one_pow]
  norm_num

/-- **If `C` is even then `x` and `y` are not both even.** -/
theorem not_both_exponents_even_of_even_C {A B C x y z : ℕ}
    (h : IsBealCounterexample A B C x y z) (hC : C % 2 = 0) :
    ¬ (x % 2 = 0 ∧ y % 2 = 0) := by
  rintro ⟨hx2, hy2⟩
  -- `A` and `B` are odd, since exactly one base is even and that one is `C`
  rcases exactly_one_even h with ⟨_, _, hC1⟩ | ⟨_, _, hC1⟩ | ⟨hA1, hB1, _⟩
  · omega
  · omega
  · obtain ⟨hA, hB, hCpos, hx, hy, hz, _, heq⟩ := h
    -- `8 ∣ C ^ z`
    have h8C : C ^ z % 8 = 0 := by
      obtain ⟨c, rfl⟩ : 2 ∣ C := Nat.dvd_of_mod_eq_zero hC
      obtain ⟨w, rfl⟩ : ∃ w, z = 3 + w := ⟨z - 3, by omega⟩
      have : (2 * c) ^ (3 + w) = 8 * (c ^ 3 * (2 * c) ^ w) := by ring
      rw [this]
      omega
    -- both powers are `1 mod 8`
    have hA8 := odd_pow_even_mod_eight hA1 hx2
    have hB8 := odd_pow_even_mod_eight hB1 hy2
    -- so the sum is `2 mod 8`, contradicting `0`
    have : (A ^ x + B ^ y) % 8 = 2 := by omega
    rw [heq] at this
    omega




/-! ### The remaining mod-8 cases: conditions on the bases -/

/-- For odd `n` and odd `k`, `n ^ k ≡ n (mod 8)`. -/
theorem odd_pow_odd_mod_eight {n k : ℕ} (hn : n % 2 = 1) (hk : k % 2 = 1) :
    n ^ k % 8 = n % 8 := by
  obtain ⟨j, rfl⟩ : ∃ j, k = 2 * j + 1 := ⟨k / 2, by omega⟩
  rw [pow_succ, Nat.mul_mod, odd_pow_even_mod_eight hn (by omega), one_mul, Nat.mod_mod]

/-- **If `C` is even and both exponents are odd, then `8 ∣ A + B`.** -/
theorem eight_dvd_add_of_even_C {A B C x y z : ℕ}
    (h : IsBealCounterexample A B C x y z) (hC : C % 2 = 0)
    (hx2 : x % 2 = 1) (hy2 : y % 2 = 1) : (A + B) % 8 = 0 := by
  rcases exactly_one_even h with ⟨_, _, hC1⟩ | ⟨_, _, hC1⟩ | ⟨hA1, hB1, _⟩
  · omega
  · omega
  · obtain ⟨hA, hB, hCpos, hx, hy, hz, _, heq⟩ := h
    have h8C : C ^ z % 8 = 0 := by
      obtain ⟨c, rfl⟩ : 2 ∣ C := Nat.dvd_of_mod_eq_zero hC
      obtain ⟨w, rfl⟩ : ∃ w, z = 3 + w := ⟨z - 3, by omega⟩
      have : (2 * c) ^ (3 + w) = 8 * (c ^ 3 * (2 * c) ^ w) := by ring
      rw [this]; omega
    have hA8 := odd_pow_odd_mod_eight hA1 hx2
    have hB8 := odd_pow_odd_mod_eight hB1 hy2
    have hsum : (A ^ x + B ^ y) % 8 = 0 := by rw [heq]; exact h8C
    omega

/-- **If `C` is even and `x` is even, then `B ≡ 7 (mod 8)`.** -/
theorem seven_mod_eight_of_even_exp {A B C x y z : ℕ}
    (h : IsBealCounterexample A B C x y z) (hC : C % 2 = 0)
    (hx2 : x % 2 = 0) : B % 8 = 7 := by
  -- derive this BEFORE destructuring `h`, which consumes it
  have hy2 : y % 2 = 1 := by
    rcases Nat.mod_two_eq_zero_or_one y with hy | hy
    · exact absurd ⟨hx2, hy⟩ (not_both_exponents_even_of_even_C h hC)
    · exact hy
  rcases exactly_one_even h with ⟨_, _, hC1⟩ | ⟨_, _, hC1⟩ | ⟨hA1, hB1, _⟩
  · omega
  · omega
  · obtain ⟨hA, hB, hCpos, hx, hy, hz, _, heq⟩ := h
    have h8C : C ^ z % 8 = 0 := by
      obtain ⟨c, rfl⟩ : 2 ∣ C := Nat.dvd_of_mod_eq_zero hC
      obtain ⟨w, rfl⟩ : ∃ w, z = 3 + w := ⟨z - 3, by omega⟩
      have : (2 * c) ^ (3 + w) = 8 * (c ^ 3 * (2 * c) ^ w) := by ring
      rw [this]; omega
    have hA8 := odd_pow_even_mod_eight hA1 hx2
    have hsum : (A ^ x + B ^ y) % 8 = 0 := by rw [heq]; exact h8C
    have hB8 := odd_pow_odd_mod_eight hB1 hy2
    omega



/-! ### The `C` odd case: conditions relating `B` and `C` mod 8

If `A` is even then `B` and `C` are odd (`exactly_one_even`), and `8 ∣ A^x` since `x ≥ 3`,
so `B^y ≡ C^z (mod 8)`.  The same three-way split as before then applies.
-/

/-- **If `A` is even and both `y`, `z` are odd, then `B ≡ C (mod 8)`.** -/
theorem B_eq_C_mod_eight_of_even_A {A B C x y z : ℕ}
    (h : IsBealCounterexample A B C x y z) (hA : A % 2 = 0)
    (hy2 : y % 2 = 1) (hz2 : z % 2 = 1) : B % 8 = C % 8 := by
  rcases exactly_one_even h with ⟨_, hB1, hC1⟩ | ⟨hA1, _, _⟩ | ⟨hA1, _, _⟩
  · obtain ⟨hApos, hB, hC, hx, hy, hz, _, heq⟩ := h
    have h8A : A ^ x % 8 = 0 := by
      obtain ⟨a, rfl⟩ : 2 ∣ A := Nat.dvd_of_mod_eq_zero hA
      obtain ⟨w, rfl⟩ : ∃ w, x = 3 + w := ⟨x - 3, by omega⟩
      have : (2 * a) ^ (3 + w) = 8 * (a ^ 3 * (2 * a) ^ w) := by ring
      rw [this]; omega
    have hB8 := odd_pow_odd_mod_eight hB1 hy2
    have hC8 := odd_pow_odd_mod_eight hC1 hz2
    have hsum : (A ^ x + B ^ y) % 8 = C ^ z % 8 := by rw [heq]
    omega
  · omega
  · omega

/-- **If `A` is even and `z` is even, then `B ≡ 1 (mod 8)`.** -/
theorem B_one_mod_eight_of_even_A_even_z {A B C x y z : ℕ}
    (h : IsBealCounterexample A B C x y z) (hA : A % 2 = 0)
    (hy2 : y % 2 = 1) (hz2 : z % 2 = 0) : B % 8 = 1 := by
  rcases exactly_one_even h with ⟨_, hB1, hC1⟩ | ⟨hA1, _, _⟩ | ⟨hA1, _, _⟩
  · obtain ⟨hApos, hB, hC, hx, hy, hz, _, heq⟩ := h
    have h8A : A ^ x % 8 = 0 := by
      obtain ⟨a, rfl⟩ : 2 ∣ A := Nat.dvd_of_mod_eq_zero hA
      obtain ⟨w, rfl⟩ : ∃ w, x = 3 + w := ⟨x - 3, by omega⟩
      have : (2 * a) ^ (3 + w) = 8 * (a ^ 3 * (2 * a) ^ w) := by ring
      rw [this]; omega
    have hB8 := odd_pow_odd_mod_eight hB1 hy2
    have hC8 := odd_pow_even_mod_eight hC1 hz2
    have hsum : (A ^ x + B ^ y) % 8 = C ^ z % 8 := by rw [heq]
    omega
  · omega
  · omega

end ModEight

section ModNine

/-- `3 ∤ n` is inherited by every power of `n`. -/
theorem three_not_dvd_pow {n k : ℕ} (hn : n % 3 ≠ 0) : n ^ k % 3 ≠ 0 := by
  intro hc
  have hp : Nat.Prime 3 := Nat.prime_three
  have hd : (3 : ℕ) ∣ n ^ k := Nat.dvd_of_mod_eq_zero hc
  obtain ⟨c, rfl⟩ := hp.dvd_of_dvd_pow hd
  omega

/-- Every cube is `0`, `1` or `8` mod `9`. -/
theorem cube_mod_nine (t : ℕ) : t ^ 3 % 9 = 0 ∨ t ^ 3 % 9 = 1 ∨ t ^ 3 % 9 = 8 := by
  rw [Nat.pow_mod]
  have h : t % 9 < 9 := Nat.mod_lt _ (by norm_num)
  interval_cases h9 : (t % 9) <;> norm_num

/-- A cube of a number coprime to `3` is `1` or `8` mod `9`. -/
theorem cube_unit_mod_nine {t : ℕ} (ht : t % 3 ≠ 0) : t ^ 3 % 9 = 1 ∨ t ^ 3 % 9 = 8 := by
  rcases cube_mod_nine t with h | h | h
  · exfalso
    have h3 : t ^ 3 % 3 = 0 := by omega
    rw [Nat.pow_mod] at h3
    have : t % 3 < 3 := Nat.mod_lt _ (by norm_num)
    interval_cases h9 : (t % 3) <;> simp_all
  · exact Or.inl h
  · exact Or.inr h

/-- **If `3 ∤ n` and `3 ∣ k` then `n ^ k ≡ ±1 (mod 9)`.** -/
theorem pow_mod_nine_of_three_dvd_exp {n k : ℕ} (hn : n % 3 ≠ 0) (hk : 3 ∣ k) :
    n ^ k % 9 = 1 ∨ n ^ k % 9 = 8 := by
  obtain ⟨m, rfl⟩ := hk
  have hnm : (n ^ m) % 3 ≠ 0 := three_not_dvd_pow hn
  have : n ^ (3 * m) = (n ^ m) ^ 3 := by rw [← pow_mul, Nat.mul_comm]
  rw [this]
  exact cube_unit_mod_nine hnm

/-- **The mod-9 analogue of the mod-8 analysis.**
If `3` divides neither base nor `C`, and both `x` and `y` are multiples of `3`, then the two
terms on the left are cubes, so each is `±1 (mod 9)`; their sum is `0`, `2` or `7`, and `0` is
excluded because `3 ∤ C`.  Hence `C ^ z ≡ ±2 (mod 9)`. -/
theorem pow_C_mod_nine {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    (hA3 : A % 3 ≠ 0) (hB3 : B % 3 ≠ 0) (hC3 : C % 3 ≠ 0)
    (hx3 : 3 ∣ x) (hy3 : 3 ∣ y) : C ^ z % 9 = 2 ∨ C ^ z % 9 = 7 := by
  obtain ⟨_, _, _, _, _, _, _, heq⟩ := h
  have hAm := pow_mod_nine_of_three_dvd_exp hA3 hx3
  have hBm := pow_mod_nine_of_three_dvd_exp hB3 hy3
  have hsum : (A ^ x + B ^ y) % 9 = C ^ z % 9 := by rw [heq]
  -- the remaining case `C ^ z ≡ 0 (mod 9)` is killed by `3 ∤ C`
  have hCz : C ^ z % 3 ≠ 0 := three_not_dvd_pow hC3
  omega

/-- **Corollary: under the same hypotheses, `3 ∤ z`.**
If `3 ∣ z` then `C ^ z` would itself be `±1 (mod 9)`, contradicting `C ^ z ≡ ±2`. -/
theorem not_three_dvd_z_of_three_dvd_xy {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    (hA3 : A % 3 ≠ 0) (hB3 : B % 3 ≠ 0) (hC3 : C % 3 ≠ 0)
    (hx3 : 3 ∣ x) (hy3 : 3 ∣ y) : ¬ (3 ∣ z) := by
  intro hz3
  have h1 := pow_C_mod_nine h hA3 hB3 hC3 hx3 hy3
  have h2 := pow_mod_nine_of_three_dvd_exp hC3 hz3
  omega

end ModNine

section ExponentOrder
/-! ## Exponent order forced by base order (cycle U123, Jev cell "gap/threshold × tail") -/

/-- **If `C` is the largest base then `z ≤ max x y`.**
`C^z = A^x + B^y < C^x + C^y ≤ 2·C^max`, while `z ≥ max + 1` would give `C^z ≥ 2·C^max`. -/
theorem z_le_max_of_C_largest {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    (hAC : A < C) (hBC : B < C) : z ≤ max x y := by
  obtain ⟨hA, _, _, hx, hy, _, _, heq⟩ := h
  by_contra hlt
  push_neg at hlt
  have hC2 : 2 ≤ C := by omega
  have hAx : A ^ x < C ^ x := Nat.pow_lt_pow_left hAC (by omega)
  have hBy : B ^ y < C ^ y := Nat.pow_lt_pow_left hBC (by omega)
  have hxm : C ^ x ≤ C ^ (max x y) := Nat.pow_le_pow_right (by omega) (le_max_left _ _)
  have hym : C ^ y ≤ C ^ (max x y) := Nat.pow_le_pow_right (by omega) (le_max_right _ _)
  have hz : C ^ (max x y + 1) ≤ C ^ z := Nat.pow_le_pow_right (by omega) hlt
  have hsucc : C ^ (max x y + 1) = C ^ (max x y) * C := pow_succ _ _
  have h2m : 2 * C ^ (max x y) ≤ C ^ (max x y) * C := by
    rw [Nat.mul_comm 2]; exact Nat.mul_le_mul_left _ hC2
  have hsum : A ^ x + B ^ y < 2 * C ^ (max x y) := by omega
  rw [← heq] at hz
  omega

/-- **If `C` is the smallest base then `z > max x y`.**
`C^z > A^x ≥ (C+1)^x > C^x` forces `z > x`, and symmetrically `z > y`. -/
theorem max_lt_z_of_C_smallest {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    (hCA : C < A) (hCB : C < B) : max x y < z := by
  obtain ⟨_, _, hC, hx, hy, _, _, heq⟩ := h
  have hCx : C ^ x < A ^ x := Nat.pow_lt_pow_left hCA (by omega)
  have hCy : C ^ y < B ^ y := Nat.pow_lt_pow_left hCB (by omega)
  have hBpos : 0 < B ^ y := by positivity
  have hApos : 0 < A ^ x := by positivity
  have h1 : C ^ x < C ^ z := by rw [← heq]; omega
  have h2 : C ^ y < C ^ z := by rw [← heq]; omega
  have hC2 : 1 < C := by
    rcases Nat.lt_or_ge 1 C with hc | hc
    · exact hc
    · have : C = 1 := by omega
      subst this; simp at h1
  have hxz : x < z := (Nat.pow_lt_pow_iff_right hC2).mp h1
  have hyz : y < z := (Nat.pow_lt_pow_iff_right hC2).mp h2
  exact max_lt hxz hyz

/-- **If `A^x ≤ B^y` and `C ≤ B` then `z > y`.**  Since `C^z > B^y ≥ C^y`. -/
theorem y_lt_z_of_C_le_B {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    (hCB : C ≤ B) : y < z := by
  obtain ⟨hA, _, hC, _, _, _, _, heq⟩ := h
  have hApos : 0 < A ^ x := by positivity
  have hCy : C ^ y ≤ B ^ y := Nat.pow_le_pow_left hCB _
  have h1 : C ^ y < C ^ z := by rw [← heq]; omega
  have hC2 : 1 < C := by
    rcases Nat.lt_or_ge 1 C with hc | hc
    · exact hc
    · have : C = 1 := by omega
      subst this; simp at h1
  exact (Nat.pow_lt_pow_iff_right hC2).mp h1

end ExponentOrder

section Dominant
/-! ## The dominant term (cycle U124, machine-generated statement selected by Jev) -/

/-- **If `A^x` is the dominant term and `A < C` then `z ≤ x`.**
`C^z = A^x + B^y ≤ 2A^x < 2C^x ≤ C^{x+1}`. -/
theorem z_le_x_of_dominant_A_lt_C {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    (hAC : A < C) (hdom : B ^ y ≤ A ^ x) : z ≤ x := by
  obtain ⟨hA, _, _, hx, _, _, _, heq⟩ := h
  by_contra hlt
  push_neg at hlt
  have hC2 : 2 ≤ C := by omega
  have hAx : A ^ x < C ^ x := Nat.pow_lt_pow_left hAC (by omega)
  have hz : C ^ (x + 1) ≤ C ^ z := Nat.pow_le_pow_right (by omega) hlt
  have hsucc : C ^ (x + 1) = C ^ x * C := pow_succ _ _
  have h2m : 2 * C ^ x ≤ C ^ x * C := by
    rw [Nat.mul_comm 2]; exact Nat.mul_le_mul_left _ hC2
  rw [← heq] at hz
  omega

/-- Symmetric form: if `B^y` is dominant and `B < C` then `z ≤ y`. -/
theorem z_le_y_of_dominant_B_lt_C {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    (hBC : B < C) (hdom : A ^ x ≤ B ^ y) : z ≤ y := by
  obtain ⟨_, hB, _, _, hy, _, _, heq⟩ := h
  by_contra hlt
  push_neg at hlt
  have hC2 : 2 ≤ C := by omega
  have hBy : B ^ y < C ^ y := Nat.pow_lt_pow_left hBC (by omega)
  have hz : C ^ (y + 1) ≤ C ^ z := Nat.pow_le_pow_right (by omega) hlt
  have hsucc : C ^ (y + 1) = C ^ y * C := pow_succ _ _
  have h2m : 2 * C ^ y ≤ C ^ y * C := by
    rw [Nat.mul_comm 2]; exact Nat.mul_le_mul_left _ hC2
  rw [← heq] at hz
  omega

/-- **If `C < A` then `x < z`** (no dominance hypothesis needed): `C^x < A^x < C^z`. -/
theorem x_lt_z_of_C_lt_A {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    (hCA : C < A) : x < z := by
  obtain ⟨_, hB, hC, hx, _, _, _, heq⟩ := h
  have hCx : C ^ x < A ^ x := Nat.pow_lt_pow_left hCA (by omega)
  have hBpos : 0 < B ^ y := by positivity
  have h1 : C ^ x < C ^ z := by rw [← heq]; omega
  have hC2 : 1 < C := by
    rcases Nat.lt_or_ge 1 C with hc | hc
    · exact hc
    · have : C = 1 := by omega
      subst this; simp at h1
  exact (Nat.pow_lt_pow_iff_right hC2).mp h1

/-- **Dichotomy for the dominant term.**  When `A^x ≥ B^y` and `A ≠ C` (automatic from
coprimality), `z ≤ x ↔ A < C`. -/
theorem dominant_dichotomy {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    (hdom : B ^ y ≤ A ^ x) : (z ≤ x ↔ A < C) := by
  have hne : A ≠ C := by
    intro hAC
    have hg := gcd_ac_eq_one h
    subst hAC
    obtain ⟨_, hB, _, _, _, _, _, heq⟩ := h
    simp at hg
    subst hg
    have : 0 < B ^ y := by positivity
    simp at heq
    omega
  constructor
  · intro hzx
    rcases Nat.lt_or_ge A C with hlt | hge
    · exact hlt
    · have hCA : C < A := lt_of_le_of_ne hge (Ne.symm hne)
      have := x_lt_z_of_C_lt_A h hCA
      omega
  · intro hAC
    exact z_le_x_of_dominant_A_lt_C h hAC hdom

end Dominant

section GaussianCubeArithmetic
/-! ## Elementary arithmetic behind the `(2m, 2n, 3)` chain (U131, step S4) -/

/-- **S4 (ℕ form).** If a prime `p` divides both `u` and `u^2 + 3*v^2 - 6*v^2`... stated directly:
if `p ∣ u` and `p ∣ u^2 - 3 v^2` (as naturals with `3 v^2 ≤ u^2`) and `Nat.Coprime u v`, then `p = 3`. -/
theorem prime_dvd_u_and_cofactor_eq_three {u v p : ℕ} (hp : p.Prime) (huv : Nat.Coprime u v)
    (h3 : 3 * v ^ 2 ≤ u ^ 2) (hu : p ∣ u) (hw : p ∣ u ^ 2 - 3 * v ^ 2) : p = 3 := by
  have hu2 : p ∣ u ^ 2 := hu.trans (dvd_pow_self u two_ne_zero)
  have h3v : p ∣ 3 * v ^ 2 := by
    have := (Nat.dvd_sub' hu2 hw)
    rwa [Nat.sub_sub_self h3] at this
  rcases (Nat.Prime.dvd_mul hp).mp h3v with h | h
  · exact (Nat.prime_dvd_prime_iff_eq hp Nat.prime_three).mp h
  · exfalso
    have hv : p ∣ v := hp.dvd_of_dvd_pow h
    have : p ∣ Nat.gcd u v := Nat.dvd_gcd hu hv
    rw [huv] at this
    exact hp.one_lt.ne' (Nat.dvd_one.mp this)

/-- **Mod-3 fact used to see why even `m` is trivial in S6:** a sum of two squares coprime to 3
is never divisible by 3. -/
theorem three_not_dvd_sum_sq {a b : ℕ} (ha : a % 3 ≠ 0) (hb : b % 3 ≠ 0) :
    (a ^ 2 + b ^ 2) % 3 ≠ 0 := by
  have ha' : a % 3 = 1 ∨ a % 3 = 2 := by omega
  have hb' : b % 3 = 1 ∨ b % 3 = 2 := by omega
  rw [Nat.add_mod, Nat.pow_mod, Nat.pow_mod (b)]
  rcases ha' with h | h <;> rcases hb' with h' | h' <;> simp [h, h']

end GaussianCubeArithmetic


/-! ### Divisor powers of `C` (U233, pool C098)

The kernel above proves `8 ∣ A^x + B^y` when `C` is even.  The equation gives strictly more: every
divisor of `C` contributes its full `z`-th power.  Taking `d = 2` and `z ≥ 3` recovers the mod-8
statement, and `d = 2` with the actual `z` is far stronger — on 7,437 generic coprime non-power
triples with even sum, `2^3 ∣ a + b` holds for 23.3%, `2^7 ∣ a + b` for 0.43%, and `2^8` for none
(`code/U233_two_adic_strengthen.py`).

Gate 1 note: it holds on all three even-`C` Fermat–Catalan solutions, so on that set it is blind;
its force comes from `z` being large, and those solutions have `z ∈ {2, 9}`. -/

/-- **Every divisor of `C` contributes its `z`-th power to the sum.**  If `d ∣ C` then
`d ^ z ∣ A ^ x + B ^ y`. -/
theorem pow_dvd_add_of_dvd_C {A B C x y z d : ℕ} (h : IsBealCounterexample A B C x y z)
    (hd : d ∣ C) : d ^ z ∣ A ^ x + B ^ y := by
  rw [h.2.2.2.2.2.2.2]
  exact pow_dvd_pow_of_dvd hd z

/-- **Specialisation to `d = 2`.**  If `C` is even then `2 ^ z ∣ A ^ x + B ^ y`; with `z ≥ 3` this
subsumes `eight_dvd_add_of_even_C`. -/
theorem two_pow_z_dvd_add_of_even_C {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    (hC : 2 ∣ C) : 2 ^ z ∣ A ^ x + B ^ y :=
  pow_dvd_add_of_dvd_C h hC

/-! ### The specialisation point is tame exactly at counterexamples (U311, pool C171)

A solution gives `t = A^x / C^z` in `P¹ ∖ {0,1,∞}`, with `1 - t = B^y / C^z`.  For a local system
with local monodromy of order `x, y, z` at the three punctures to pull back *unramified* at a prime
`p`, the `p`-adic valuation of `t` (or of `1-t`) must be divisible by the corresponding order.

The lemmas below are the exact arithmetic behind that, and the point is the **disjointness**:
by pairwise coprimality a prime divides at most one of `A, B, C`, so at each prime exactly one of
the three valuations is nonzero and it is a multiple of that base's own exponent.  Checked
numerically on all ten Fermat–Catalan solutions in `code/U311_tame_specialisation.py`
(56 exact valuations), together with non-coprime controls — `3³+6³=3⁵`, `7⁶+7⁷=98³`, `2⁹+8³=4⁵` —
on which the statement **fails**, as it must: the hypothesis really is coprimality.

That is the route's logic, and it is not circular: a Beal counterexample has `gcd = 1` by
definition, so this is the counterexample hypothesis, not an extra assumption.  It is also not
progress on Beal — it says nothing about obligation (b) of C169, the motivic realisation of a
rank-`n` sheaf, for which no automorphy theorem exists when `n > 2`. -/

/-- A prime dividing `A` divides neither `B` nor `C`. -/
theorem support_disjoint_A {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    {p : ℕ} (hp : p.Prime) (hpA : p ∣ A) : ¬ p ∣ B ∧ ¬ p ∣ C := by
  have hab := gcd_ab_eq_one h
  have hac := gcd_ac_eq_one h
  constructor
  · intro hpB
    have : p ∣ Nat.gcd A B := Nat.dvd_gcd hpA hpB
    rw [hab] at this; exact hp.one_lt.ne' (Nat.dvd_one.mp this)
  · intro hpC
    have : p ∣ Nat.gcd A C := Nat.dvd_gcd hpA hpC
    rw [hac] at this; exact hp.one_lt.ne' (Nat.dvd_one.mp this)

/-- A prime dividing `C` divides neither `A` nor `B`. -/
theorem support_disjoint_C {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    {p : ℕ} (hp : p.Prime) (hpC : p ∣ C) : ¬ p ∣ A ∧ ¬ p ∣ B := by
  have hac := gcd_ac_eq_one h
  have hbc := gcd_bc_eq_one h
  constructor
  · intro hpA
    have : p ∣ Nat.gcd A C := Nat.dvd_gcd hpA hpC
    rw [hac] at this; exact hp.one_lt.ne' (Nat.dvd_one.mp this)
  · intro hpB
    have : p ∣ Nat.gcd B C := Nat.dvd_gcd hpB hpC
    rw [hbc] at this; exact hp.one_lt.ne' (Nat.dvd_one.mp this)

/-- **H1.**  At a prime dividing `A`, the valuation of `A^x` is `x` times that of `A` — a multiple
of the order at the puncture `0` — and the other two contribute nothing. -/
theorem tame_valuation_at_A {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    {p : ℕ} (hp : p.Prime) (hpA : p ∣ A) :
    (A ^ x).factorization p = x * A.factorization p ∧
      (B ^ y).factorization p = 0 ∧ (C ^ z).factorization p = 0 := by
  obtain ⟨hB, hC⟩ := support_disjoint_A h hp hpA
  refine ⟨by rw [Nat.factorization_pow]; simp [mul_comm], ?_, ?_⟩
  · rw [Nat.factorization_pow]; simp [Nat.factorization_eq_zero_of_not_dvd hB]
  · rw [Nat.factorization_pow]; simp [Nat.factorization_eq_zero_of_not_dvd hC]

/-- **H3.**  At a prime dividing `C`, both `t` and `1 - t` have valuation `-z·v_p(C)`, a multiple
of the order at the puncture `∞`; `A` and `B` contribute nothing.  This is the case that is easy
to state wrongly: the divisibility there is by `z`, not by `x` or `y`. -/
theorem tame_valuation_at_C {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    {p : ℕ} (hp : p.Prime) (hpC : p ∣ C) :
    (C ^ z).factorization p = z * C.factorization p ∧
      (A ^ x).factorization p = 0 ∧ (B ^ y).factorization p = 0 := by
  obtain ⟨hA, hB⟩ := support_disjoint_C h hp hpC
  refine ⟨by rw [Nat.factorization_pow]; simp [mul_comm], ?_, ?_⟩
  · rw [Nat.factorization_pow]; simp [Nat.factorization_eq_zero_of_not_dvd hA]
  · rw [Nat.factorization_pow]; simp [Nat.factorization_eq_zero_of_not_dvd hB]

end Beal
