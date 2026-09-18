/-
# The same-parity branch of `(3,4,4)` (U279–U281, pool C151)

`A³ + B⁴ = C⁴` with `gcd(B,C) = 1` and `B, C` **both odd** has no solution in positive integers.

The descent (worked out and numerically checked in `code/`, recorded as pool C151) is:

* `B, C` odd ⟹ `C² + B² ≡ 2 (mod 8)`, so `v₂(C²+B²) = 1`;
* exactly one of `C−B`, `C+B` has `v₂ = 1` and the other has `v₂ = k ≥ 2` — if both were `1`,
  then `C` would be even;
* `v₂(A³) = 1 + k + 1 = k+2` must be divisible by `3`, so `k ≡ 1 (mod 3)` and `k ≥ 4`; hence
  `3 ∣ k−1` and `4^(k-1) = (2^(2(k-1)/3))³` is a **perfect cube**;
* the odd parts of `C−B`, `C+B`, `(C²+B²)/2` are pairwise coprime, so each is a cube:
  `C−B = 2^α μ³`, `C+B = 2^β ν³`, `(C²+B²)/2 = τ³` with `{α,β} = {1,k}`;
* taking `α = 1`: `C = μ³ + 2^{k-1}ν³`, `B = 2^{k-1}ν³ − μ³`, so
  `(C²+B²)/2 = μ⁶ + 4^{k-1}ν⁶ = τ³`;
* with `λ = 2^{2(k-1)/3}` this is `(μ²)³ + (λν²)³ = τ³`.

The last line is **Fermat's equation for exponent 3**, so it has no solution in positive integers.
The case `α = k` is symmetric.

**What is formalised below, and what is not.**

| step | status |
|---|---|
| (i) `v₂(C²+B²) = 1` | `odd_sq_add_sq_mod_eight` |
| (ii) `{v₂(C−B), v₂(C+B)} = {1,k}`, `k ≥ 2` | `exactly_one_two_mod_four` |
| (iii) `3 ∣ k+2` ⟹ `4^(k−1)` is a cube | `k_mod_three_of_three_dvd`, `four_pow_cube_of_valuation` |
| (iv a) the three odd parts are pairwise coprime | `odd_common_divisor_*` (three lemmas) |
| (iv b) pairwise coprime factors of a cube are cubes | `isCoprime_of_forall_common_unit`, `three_coprime_factors_cubes` |
| closing `(μ²)³ + (λν²)³ = τ³` | `no_sixth_power_cube_relation` |
| assembly a: `2^e·odd` decomposition is unique, `3 ∣ e` and odd part a cube are *derived* | `two_pow_mul_odd_inj`, `odd_part_cube` |
| assembly b: `A³ = (C−B)(C+B)(C²+B²)`, and the 2-adic split of all three factors | `quartic_factorisation`, `descent_two_adic` |
| assembly c: the three odd parts are cubes; `1 ≤ a, b` and `a = 1 ∨ b = 1` | `odd_parts_cubes`, `two_exponents` |
| assembly d: the substitution `w = μ⁶ + 4^(b−1)ν⁶` and the two symmetric cases | `sq_sub_add`, `three_four_four_same_parity` |

**The branch is now closed with no prose step.**  `three_four_four_same_parity` has the statement

    ∀ {A B C : ℕ}, 0 < A → Odd B → Odd C → B < C → Nat.Coprime B C → A^3 + B^4 = C^4 → False

with `#print axioms` reporting only `[propext, Classical.choice, Quot.sound]`.  The only external
input is mathlib's `fermatLastTheoremThree`.  The numerical check in `code/` over all odd coprime
`1 ≤ B < C < 300` (9,116 pairs, zero violations) is now redundant evidence rather than the support
for the claim.

**Scope, which this does not change.**  This is one branch of one signature, and the descent needs
`C⁴ − B⁴` to factor, i.e. `gcd(y,z) > 1`.  Among reduced exponents that means two exponents are
equal.  Beal's open core has three pairwise distinct reduced exponents and no such factorisation,
so nothing here reaches it (pool C157).

No `sorry`, no custom `axiom`s; mathlib only.
-/
import Mathlib.NumberTheory.FLT.Three
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace Beal

/-- **The step that closes the same-parity branch.**  A relation `μ⁶ + λ³·ν⁶ = τ³` in positive
integers is Fermat's equation for exponent `3` in disguise: it reads `(μ²)³ + (λν²)³ = τ³`. -/
theorem no_sixth_power_cube_relation {μ ν τ lam : ℕ}
    (hμ : 0 < μ) (hν : 0 < ν) (hτ : 0 < τ) (hlam : 0 < lam)
    (h : μ ^ 6 + lam ^ 3 * ν ^ 6 = τ ^ 3) : False := by
  have hrw : (μ ^ 2) ^ 3 + (lam * ν ^ 2) ^ 3 = τ ^ 3 := by
    rw [← h]; ring
  exact fermatLastTheoremThree (μ ^ 2) (lam * ν ^ 2) τ
    (by positivity) (by positivity) (by positivity) hrw

/-- The same statement with the cube written as `4 ^ (k-1)` for `k ≡ 1 (mod 3)`, which is the form
the descent produces: `3 ∣ k - 1` makes `4 ^ (k-1)` a cube. -/
theorem four_pow_is_cube {k : ℕ} (hk : 3 ∣ k - 1) :
    4 ^ (k - 1) = (2 ^ (2 * ((k - 1) / 3))) ^ 3 := by
  obtain ⟨m, hm⟩ := hk
  rw [hm]
  have h3 : 3 * m / 3 = m := by omega
  rw [h3, show (4 : ℕ) = 2 ^ 2 by norm_num, ← pow_mul, ← pow_mul]
  ring_nf

/-! ### The `3 ∣ gcd` branch is empty (U282, pool C152)

The reduction in C144 split on `d = gcd(r²+s², r⁴−r²s²+s⁴)`, which divides `3`.  The branch
`d = 3` never occurs: squares mod `3` are `0` and `1`, so `3 ∣ r²+s²` forces `3 ∣ r` and `3 ∣ s`,
contradicting coprimality.  Verified exactly for all coprime `r, s < 400` (no pair), and the gcd
takes only the value `1` over all coprime `r, s < 200`. -/

/-- Over `ZMod 3`, `a² + b² = 0` forces `a = b = 0`: squares are `0` and `1`. -/
theorem zmod_three_sq_add_sq (a b : ZMod 3) (h : a ^ 2 + b ^ 2 = 0) : a = 0 ∧ b = 0 := by
  revert h; revert a b; decide

/-- For coprime `r, s`, `3` never divides `r² + s²`. -/
theorem three_not_dvd_sq_add_sq {r s : ℕ} (h : Nat.Coprime r s) : ¬ (3 ∣ r ^ 2 + s ^ 2) := by
  intro hdvd
  have hz : ((r : ZMod 3)) ^ 2 + ((s : ZMod 3)) ^ 2 = 0 := by
    have : ((r ^ 2 + s ^ 2 : ℕ) : ZMod 3) = 0 :=
      (ZMod.natCast_zmod_eq_zero_iff_dvd _ 3).mpr hdvd
    push_cast at this
    exact this
  obtain ⟨hr, hs⟩ := zmod_three_sq_add_sq _ _ hz
  have hr3 : (3 : ℕ) ∣ r := (ZMod.natCast_zmod_eq_zero_iff_dvd _ 3).mp hr
  have hs3 : (3 : ℕ) ∣ s := (ZMod.natCast_zmod_eq_zero_iff_dvd _ 3).mp hs
  have : (3 : ℕ) ∣ Nat.gcd r s := Nat.dvd_gcd hr3 hs3
  rw [h] at this
  omega

/-! ### Formalising more of the same-parity descent (U303, pool C168)

The closing step is `no_sixth_power_cube_relation`.  Two of the arithmetic steps that lead to it
are formalised here, reducing what is left to prose.  Both are `decide` computations in `ZMod 8`.

Step (i): `B, C` odd gives `C² + B² ≡ 2 (mod 8)`, hence `v₂(C²+B²) = 1`.
Step (ii): `B, C` odd gives `(C-B)` and `(C+B)` of opposite type mod 4 — exactly one is
`≡ 2 (mod 4)` — which is why `{v₂(C-B), v₂(C+B)} = {1, k}` with `k ≥ 2`. -/

/-- Over `ZMod 8`, an odd square is `1`. -/
theorem zmod_eight_odd_sq (a : ZMod 8) (h : a = 1 ∨ a = 3 ∨ a = 5 ∨ a = 7) : a ^ 2 = 1 := by
  rcases h with rfl | rfl | rfl | rfl <;> decide

/-- **Step (i).**  For odd `B, C`, `C² + B² ≡ 2 (mod 8)`. -/
theorem odd_sq_add_sq_mod_eight {B C : ℕ} (hB : Odd B) (hC : Odd C) :
    (C ^ 2 + B ^ 2) % 8 = 2 := by
  obtain ⟨b, rfl⟩ := hB
  obtain ⟨c, rfl⟩ := hC
  have hb : b % 4 = 0 ∨ b % 4 = 1 ∨ b % 4 = 2 ∨ b % 4 = 3 := by omega
  have hc : c % 4 = 0 ∨ c % 4 = 1 ∨ c % 4 = 2 ∨ c % 4 = 3 := by omega
  have key : ∀ n : ℕ, (2 * n + 1) ^ 2 % 8 = 1 := by
    intro n
    have h4 : n % 4 = 0 ∨ n % 4 = 1 ∨ n % 4 = 2 ∨ n % 4 = 3 := by omega
    have : (2 * n + 1) ^ 2 = 4 * (n * (n + 1)) + 1 := by ring
    rw [this]
    obtain ⟨m, hm⟩ := (Nat.even_mul_succ_self n).two_dvd
    rw [hm]
    omega
  have h1 := key c
  have h2 := key b
  omega

/-- **Step (ii).**  For odd `B < C`, exactly one of `C - B`, `C + B` is `≡ 2 (mod 4)`.
Writing `B = 2b+1`, `C = 2c+1` with `b ≤ c`: `C - B = 2(c-b)` and `C + B = 2(c+b+1)`, and
`c - b` and `c + b + 1` have opposite parity, so exactly one of the two is twice an odd number.
This is why `{v₂(C-B), v₂(C+B)} = {1, k}` with `k ≥ 2`. -/
theorem exactly_one_two_mod_four {B C : ℕ} (hB : Odd B) (hC : Odd C) (hlt : B < C) :
    ((C - B) % 4 = 2) ↔ ¬ ((C + B) % 4 = 2) := by
  obtain ⟨b, rfl⟩ := hB
  obtain ⟨c, rfl⟩ := hC
  have hbc : b < c := by omega
  have hsub : 2 * c + 1 - (2 * b + 1) = 2 * (c - b) := by omega
  have hadd : 2 * c + 1 + (2 * b + 1) = 2 * (c + b + 1) := by omega
  rw [hsub, hadd]
  have h1 : (c - b) % 2 = 0 ∨ (c - b) % 2 = 1 := by omega
  have h2 : (c + b + 1) % 2 = 0 ∨ (c + b + 1) % 2 = 1 := by omega
  have hpar : (c - b) % 2 = (c + b) % 2 := by omega
  omega

/-- **Step (iii).**  The 2-adic valuation of `A³` is `k + 2`, so `3 ∣ k + 2`, which is exactly
`k ≡ 1 (mod 3)`; hence `3 ∣ k - 1` and `4^(k-1)` is a cube by `four_pow_is_cube`. -/
theorem k_mod_three_of_three_dvd {k : ℕ} (hk : 2 ≤ k) (h : 3 ∣ k + 2) : k % 3 = 1 ∧ 3 ∣ k - 1 := by
  obtain ⟨m, hm⟩ := h
  constructor
  · omega
  · exact ⟨m - 1, by omega⟩

/-- Chaining (iii) with `four_pow_is_cube`: from `3 ∣ k + 2` and `k ≥ 2`, the factor `4^(k-1)`
appearing in `(C²+B²)/2 = μ⁶ + 4^(k-1) ν⁶` is a perfect cube. -/
theorem four_pow_cube_of_valuation {k : ℕ} (hk : 2 ≤ k) (h : 3 ∣ k + 2) :
    4 ^ (k - 1) = (2 ^ (2 * ((k - 1) / 3))) ^ 3 :=
  four_pow_is_cube (k_mod_three_of_three_dvd hk h).2

/-! ### Step (iv), first half: the three odd parts are pairwise coprime (U306, pool C168)

The descent writes `A³ = (C-B)(C+B)(C²+B²)` and needs each *odd part* to be a cube.  That needs
the three odd parts to be pairwise coprime.  Formalised here over `ℤ`, in the form that is
actually used: **every odd common divisor of two of the factors is a unit.**  Powers of `2` are
excluded by hypothesis, which is exactly what "odd part" means, and their distribution is the
content of steps (i)–(iii) above.

The three lemmas cover the three pairs.  Each is a two-line Bézout argument. -/

/-- An odd common divisor of `C-B` and `C+B` divides both `2B` and `2C`, hence `B` and `C`. -/
theorem odd_common_divisor_sub_add {B C d : ℤ} (h : IsCoprime B C)
    (hodd : ¬ (2 : ℤ) ∣ d) (hs : d ∣ C - B) (ha : d ∣ C + B) : IsUnit d := by
  have h2 : IsCoprime (2 : ℤ) d := (Int.prime_two.irreducible.coprime_iff_not_dvd).mpr hodd
  have hC : d ∣ 2 * C := by have := dvd_add hs ha; simpa [two_mul] using this
  have hB : d ∣ 2 * B := by
    have := dvd_sub ha hs; simpa [two_mul] using this
  have hC' : d ∣ C := (h2.symm).dvd_of_dvd_mul_left hC
  have hB' : d ∣ B := (h2.symm).dvd_of_dvd_mul_left hB
  exact h.isUnit_of_dvd' hB' hC'

/-- An odd common divisor of `C-B` and `C²+B²` divides `2BC`, hence `BC`; but it is coprime to
both `B` and `C` because `C ≡ B` modulo it. -/
theorem odd_common_divisor_sub_sqsum {B C d : ℤ} (h : IsCoprime B C)
    (hodd : ¬ (2 : ℤ) ∣ d) (hs : d ∣ C - B) (hq : d ∣ C ^ 2 + B ^ 2) : IsUnit d := by
  have h2 : IsCoprime (2 : ℤ) d := (Int.prime_two.irreducible.coprime_iff_not_dvd).mpr hodd
  -- `C² + B² = (C - B)² + 2BC`
  have hkey : d ∣ 2 * (B * C) := by
    have hsq : d ∣ (C - B) ^ 2 := Dvd.dvd.pow hs (by norm_num)
    have : C ^ 2 + B ^ 2 - (C - B) ^ 2 = 2 * (B * C) := by ring
    calc d ∣ (C ^ 2 + B ^ 2) - (C - B) ^ 2 := dvd_sub hq hsq
      _ = 2 * (B * C) := this
  have hBC : d ∣ B * C := (h2.symm).dvd_of_dvd_mul_left hkey
  -- `d ∣ C - B` turns coprimality of `B, C` into coprimality of `d` with each of them
  have hdB : IsCoprime d B := by
    obtain ⟨u, v, huv⟩ := h
    obtain ⟨t, ht⟩ := hs
    exact ⟨v * t, u + v, by linear_combination huv - v * ht⟩
  have hdC : IsCoprime d C := by
    obtain ⟨u, v, huv⟩ := h
    obtain ⟨t, ht⟩ := hs
    exact ⟨-(u * t), u + v, by linear_combination huv + u * ht⟩
  exact (hdB.mul_right hdC).isUnit_of_dvd' dvd_rfl hBC

/-- The symmetric statement for `C+B`: `C² + B² = (C + B)² - 2BC`. -/
theorem odd_common_divisor_add_sqsum {B C d : ℤ} (h : IsCoprime B C)
    (hodd : ¬ (2 : ℤ) ∣ d) (ha : d ∣ C + B) (hq : d ∣ C ^ 2 + B ^ 2) : IsUnit d := by
  have hs : d ∣ C - (-B) := by simpa using ha
  have hq' : d ∣ C ^ 2 + (-B) ^ 2 := by simpa using hq
  exact odd_common_divisor_sub_sqsum (B := -B) (C := C) h.neg_left hodd hs hq'

/-! ### Step (iv b): coprime factors of a cube are cubes (U307, pool C168)

The earlier note that this step is blocked because `ℤˣ` is not a subsingleton was **wrong**, and
is corrected here: for an **odd** exponent mathlib has the integral version outright,
`Int.eq_pow_of_mul_eq_pow_odd`, and `3` is odd.  The sign ambiguity that makes the general
statement fail over `ℤ` (e.g. `(-1)·(-1) = 1²`) is absorbed by `(-d)^k = -(d^k)` for odd `k`.

Two lemmas below: a bridge turning "every common divisor is a unit" — the shape the three
`odd_common_divisor_*` lemmas produce — into `IsCoprime`, and the three-factor cube splitting. -/

/-- Over `ℤ`, "every common divisor is a unit" is `IsCoprime`. -/
theorem isCoprime_of_forall_common_unit {a b : ℤ}
    (H : ∀ d : ℤ, d ∣ a → d ∣ b → IsUnit d) : IsCoprime a b := by
  rw [Int.isCoprime_iff_gcd_eq_one]
  have hu : IsUnit ((Int.gcd a b : ℕ) : ℤ) := H _ (Int.gcd_dvd_left) (Int.gcd_dvd_right)
  rcases Int.isUnit_iff.mp hu with h | h
  · exact_mod_cast h
  · omega

/-- **Step (iv b).**  If `u·v·w` is a cube and the three factors are pairwise coprime, each factor
is a cube.  This is the statement the descent applies to `u = C−B`, `v = C+B`, `w = (C²+B²)/2`
after the powers of `2` have been split off by steps (i)–(iii). -/
theorem three_coprime_factors_cubes {u v w c : ℤ}
    (huv : IsCoprime u v) (huw : IsCoprime u w) (hvw : IsCoprime v w)
    (h : u * v * w = c ^ 3) :
    (∃ a, u = a ^ 3) ∧ (∃ b, v = b ^ 3) ∧ (∃ e, w = e ^ 3) := by
  have h3 : Odd 3 := ⟨1, by norm_num⟩
  have hu : u * (v * w) = c ^ 3 := by rw [← h]; ring
  have hv : v * (u * w) = c ^ 3 := by rw [← h]; ring
  have hw : w * (u * v) = c ^ 3 := by rw [← h]; ring
  refine ⟨Int.eq_pow_of_mul_eq_pow_odd_left (huv.mul_right huw) h3 hu,
    Int.eq_pow_of_mul_eq_pow_odd_left (huv.symm.mul_right hvw) h3 hv,
    Int.eq_pow_of_mul_eq_pow_odd_left (huw.symm.mul_right hvw.symm) h3 hw⟩

/-! ### Assembly, part 1: the 2-adic bookkeeping is *derived*, not assumed (U308, pool C168)

Step (iii) above took `3 ∣ k+2` as a hypothesis.  It is in fact a consequence, and the two lemmas
below prove it: uniqueness of the decomposition `n = 2^e · odd`, and then the extraction of the
odd part of a cube.  `odd_part_cube` says that if `2^e · P = A³` with `P` odd, then automatically
`3 ∣ e` **and** `P` is a cube — which is exactly what the descent needs about
`(C−B)(C+B)(C²+B²)`, whose 2-part is `2^(1+k+1)` by steps (i)–(ii). -/

theorem two_pow_mul_odd_inj : ∀ {i j m n : ℕ}, Odd m → Odd n → 2 ^ i * m = 2 ^ j * n →
    i = j ∧ m = n := by
  intro i
  induction i with
  | zero =>
    intro j m n hm hn h
    simp only [pow_zero, one_mul] at h
    cases j with
    | zero => simp only [pow_zero, one_mul] at h; exact ⟨rfl, h⟩
    | succ j =>
      exfalso
      have : (2 : ℕ) ∣ m := ⟨2 ^ j * n, by rw [h]; ring⟩
      rcases hm with ⟨k, hk⟩; omega
  | succ i ih =>
    intro j m n hm hn h
    cases j with
    | zero =>
      exfalso
      simp only [pow_zero, one_mul] at h
      have : (2 : ℕ) ∣ n := ⟨2 ^ i * m, by rw [← h]; ring⟩
      rcases hn with ⟨k, hk⟩; omega
    | succ j =>
      have h' : 2 ^ i * m = 2 ^ j * n := by
        have : 2 * (2 ^ i * m) = 2 * (2 ^ j * n) := by
          have e1 : (2:ℕ) ^ (i+1) = 2 * 2 ^ i := by ring
          have e2 : (2:ℕ) ^ (j+1) = 2 * 2 ^ j := by ring
          rw [e1, e2] at h; linarith [h]
        omega
      obtain ⟨hij, hmn⟩ := ih hm hn h'
      exact ⟨by omega, hmn⟩

theorem odd_part_cube {e P A : ℕ} (hP : Odd P) (hA : A ≠ 0) (h : 2 ^ e * P = A ^ 3) :
    ∃ s t, Odd t ∧ A = 2 ^ s * t ∧ e = 3 * s ∧ P = t ^ 3 := by
  obtain ⟨s, t, ht, rfl⟩ := Nat.exists_eq_two_pow_mul_odd hA
  refine ⟨s, t, ht, rfl, ?_, ?_⟩ <;>
  · have hcube : (2 ^ s * t) ^ 3 = 2 ^ (3 * s) * t ^ 3 := by
      rw [Nat.mul_pow, ← pow_mul]; ring_nf
    rw [hcube] at h
    obtain ⟨h1, h2⟩ := two_pow_mul_odd_inj hP (ht.pow) h
    first | exact h1 | exact h2

/-! ### Assembly, part 2: the factorisation and the 2-adic split (U312, pool C168)

`quartic_factorisation` produces `A³ = (C−B)(C+B)(C²+B²)` with no `ℕ`-subtraction pain, by
substituting `C = B + d`.  `descent_two_adic` then splits all three factors into `2^e · odd` and
feeds the product to `odd_part_cube`, which returns **both** halves of what the descent needs:
`3 ∣ a+b+1` (step (iii), no longer a hypothesis) and the fact that the product of the three odd
parts is a cube. -/
theorem quartic_factorisation {A B C : ℕ} (hlt : B < C) (h : A ^ 3 + B ^ 4 = C ^ 4) :
    A ^ 3 = (C - B) * (C + B) * (C ^ 2 + B ^ 2) := by
  obtain ⟨d, rfl⟩ : ∃ d, C = B + d := ⟨C - B, by omega⟩
  have hd : B + d - B = d := by omega
  have hadd : B + d + B = 2 * B + d := by omega
  rw [hd, hadd]
  have expand : d * (2 * B + d) * ((B + d) ^ 2 + B ^ 2) + B ^ 4 = (B + d) ^ 4 := by ring
  omega


/-- The odd part of `C²+B²` for odd `B, C`: it is `2·w'` with `w'` odd. -/
theorem sq_sum_two_mul_odd {B C : ℕ} (hB : Odd B) (hC : Odd C) :
    ∃ w, Odd w ∧ C ^ 2 + B ^ 2 = 2 * w := by
  have h := odd_sq_add_sq_mod_eight hB hC
  refine ⟨(C ^ 2 + B ^ 2) / 2, ?_, by omega⟩
  rw [Nat.odd_iff]
  omega

/-- Assembly of the 2-adic data: the three factors split as `2^a u'`, `2^b v'`, `2 w'` with odd
parts, the total 2-exponent `a+b+1` is divisible by `3`, and the product of the odd parts is a
cube.  Both conclusions come from `odd_part_cube` applied to `A³`. -/
theorem descent_two_adic {A B C : ℕ} (hA : A ≠ 0) (hB : Odd B) (hC : Odd C) (hlt : B < C)
    (h : A ^ 3 + B ^ 4 = C ^ 4) :
    ∃ a b u v w t, Odd u ∧ Odd v ∧ Odd w ∧ Odd t ∧
      C - B = 2 ^ a * u ∧ C + B = 2 ^ b * v ∧ C ^ 2 + B ^ 2 = 2 * w ∧
      3 ∣ a + b + 1 ∧ u * v * w = t ^ 3 := by
  obtain ⟨w, hwodd, hw⟩ := sq_sum_two_mul_odd hB hC
  obtain ⟨a, u, huodd, hu⟩ := Nat.exists_eq_two_pow_mul_odd (n := C - B) (by omega)
  obtain ⟨b, v, hvodd, hv⟩ := Nat.exists_eq_two_pow_mul_odd (n := C + B) (by omega)
  have hfac := quartic_factorisation hlt h
  have hprod : 2 ^ (a + b + 1) * (u * (v * w)) = A ^ 3 := by
    rw [hfac, hu, hv, hw]; ring
  obtain ⟨s, t, htodd, hAs, hexp, hcube⟩ :=
    odd_part_cube (huodd.mul (hvodd.mul hwodd)) hA hprod
  exact ⟨a, b, u, v, w, t, huodd, hvodd, hwodd, htodd, hu, hv, hw, ⟨s, hexp⟩,
    by rw [← hcube]; ring⟩

/-! ### Assembly, part 3: the odd parts are cubes, and the 2-adic exponents (U313, pool C168)

`odd_parts_cubes` is the join: it casts the three odd parts to `ℤ`, feeds every odd common divisor
to the three `odd_common_divisor_*` lemmas through `isCoprime_of_forall_common_unit`, and applies
`three_coprime_factors_cubes`.  `two_exponents` is step (ii) in the form the reconstruction needs:
both 2-adic exponents are at least `1` and at least one of them equals `1` — if both were `≥ 2`
then `4 ∣ 2B`, making `B` even. -/

theorem not_two_dvd_of_dvd_odd {n : ℕ} (hn : Odd n) {d : ℤ} (hd : d ∣ (n : ℤ)) :
    ¬ (2 : ℤ) ∣ d := by
  intro h2
  have h : (2 : ℤ) ∣ (n : ℤ) := h2.trans hd
  have : (2 : ℕ) ∣ n := by exact_mod_cast h
  rcases hn with ⟨k, hk⟩
  omega

theorem odd_parts_cubes {B C a b u v w t : ℕ}
    (hcop : Nat.Coprime B C) (hlt : B < C)
    (huodd : Odd u) (hvodd : Odd v) (hwodd : Odd w)
    (hu : C - B = 2 ^ a * u) (hv : C + B = 2 ^ b * v) (hw : C ^ 2 + B ^ 2 = 2 * w)
    (hcube : u * v * w = t ^ 3) :
    (∃ p : ℤ, (u : ℤ) = p ^ 3) ∧ (∃ q : ℤ, (v : ℤ) = q ^ 3) ∧ (∃ r : ℤ, (w : ℤ) = r ^ 3) := by
  have hBC : IsCoprime (B : ℤ) (C : ℤ) := by
    rw [Int.isCoprime_iff_gcd_eq_one]
    simpa using hcop
  have hcastsub : ((C - B : ℕ) : ℤ) = (C : ℤ) - (B : ℤ) := by
    push_cast [Nat.cast_sub (le_of_lt hlt)]; ring
  have hdu : ((u : ℤ)) ∣ (C : ℤ) - (B : ℤ) := by
    refine ⟨(2 : ℤ) ^ a, ?_⟩
    rw [← hcastsub, hu]; push_cast; ring
  have hdv : ((v : ℤ)) ∣ (C : ℤ) + (B : ℤ) := by
    refine ⟨(2 : ℤ) ^ b, ?_⟩
    have hc : ((C + B : ℕ) : ℤ) = (C : ℤ) + (B : ℤ) := by push_cast; ring
    rw [← hc, hv]; push_cast; ring
  have hdw : ((w : ℤ)) ∣ (C : ℤ) ^ 2 + (B : ℤ) ^ 2 := by
    refine ⟨2, ?_⟩
    have hc : ((C ^ 2 + B ^ 2 : ℕ) : ℤ) = (C : ℤ) ^ 2 + (B : ℤ) ^ 2 := by push_cast; ring
    rw [← hc, hw]; push_cast; ring
  have huv : IsCoprime (u : ℤ) (v : ℤ) :=
    isCoprime_of_forall_common_unit fun d hdu' hdv' =>
      odd_common_divisor_sub_add hBC (not_two_dvd_of_dvd_odd huodd hdu')
        (hdu'.trans hdu) (hdv'.trans hdv)
  have huw : IsCoprime (u : ℤ) (w : ℤ) :=
    isCoprime_of_forall_common_unit fun d hdu' hdw' =>
      odd_common_divisor_sub_sqsum hBC (not_two_dvd_of_dvd_odd huodd hdu')
        (hdu'.trans hdu) (hdw'.trans hdw)
  have hvw : IsCoprime (v : ℤ) (w : ℤ) :=
    isCoprime_of_forall_common_unit fun d hdv' hdw' =>
      odd_common_divisor_add_sqsum hBC (not_two_dvd_of_dvd_odd hvodd hdv')
        (hdv'.trans hdv) (hdw'.trans hdw)
  have hc3 : (u : ℤ) * (v : ℤ) * (w : ℤ) = (t : ℤ) ^ 3 := by exact_mod_cast hcube
  exact three_coprime_factors_cubes huv huw hvw hc3

/-- A positive natural that is an integer cube is a natural cube. -/
theorem nat_cube_of_int_cube {n : ℕ} {p : ℤ} (h : (n : ℤ) = p ^ 3) : n = p.natAbs ^ 3 := by
  have hnn : (0 : ℤ) ≤ p ^ 3 := h ▸ Int.natCast_nonneg n
  have hp : 0 ≤ p := by nlinarith [sq_nonneg p, sq_nonneg (p + 1), sq_nonneg (p - 1)]
  have habs : ((p.natAbs : ℤ)) = p := Int.natAbs_of_nonneg hp
  have : (n : ℤ) = ((p.natAbs ^ 3 : ℕ) : ℤ) := by push_cast [habs]; exact h
  exact_mod_cast this

/-- The 2-adic exponents: both at least 1, and not both 1. -/
theorem two_exponents {B C a b u v : ℕ} (hB : Odd B) (hC : Odd C) (hlt : B < C)
    (huodd : Odd u) (hvodd : Odd v)
    (hu : C - B = 2 ^ a * u) (hv : C + B = 2 ^ b * v) :
    1 ≤ a ∧ 1 ≤ b ∧ (a = 1 ∨ b = 1) ∧ ¬ (a = 1 ∧ b = 1) := by
  obtain ⟨c, rfl⟩ := hC
  obtain ⟨d, rfl⟩ := hB
  obtain ⟨u', rfl⟩ := huodd
  obtain ⟨v', rfl⟩ := hvodd
  have hsub : 2 * c + 1 - (2 * d + 1) = 2 * (c - d) := by omega
  have hadd : 2 * c + 1 + (2 * d + 1) = 2 * (c + d + 1) := by omega
  rw [hsub] at hu
  rw [hadd] at hv
  have ha1 : 1 ≤ a := by
    by_contra hcon
    have ha0 : a = 0 := by omega
    rw [ha0, pow_zero, one_mul] at hu; omega
  have hb1 : 1 ≤ b := by
    by_contra hcon
    have hb0 : b = 0 := by omega
    rw [hb0, pow_zero, one_mul] at hv; omega
  have hnot11 : ¬ (a = 1 ∧ b = 1) := by
    rintro ⟨rfl, rfl⟩
    rw [pow_one] at hu hv
    omega
  refine ⟨ha1, hb1, ?_, hnot11⟩
  by_contra hcon
  push_neg at hcon
  obtain ⟨ha, hb⟩ := hcon
  have ha2 : 2 ≤ a := by omega
  have hb2 : 2 ≤ b := by omega
  have h4u : 4 ∣ 2 * (c - d) := by
    rw [hu]
    exact Dvd.dvd.mul_right (by simpa using pow_dvd_pow 2 ha2) _
  have h4v : 4 ∣ 2 * (c + d + 1) := by
    rw [hv]
    exact Dvd.dvd.mul_right (by simpa using pow_dvd_pow 2 hb2) _
  omega

/-! ### Assembly, part 4: the branch, closed (U314, pool C168)

The last substitution.  `(C−B)² + (C+B)² = 2(C²+B²)` gives `4^a u² + 4^b v² = 4w`; `two_exponents`
forces exactly one of `a, b` to be `1`; cancelling the `4` leaves `w = u² + 4^(b−1) v²` (or the
mirror image).  The odd parts are cubes, `3 ∣ a+b+1` makes `4^(b−1)` a cube, and
`no_sixth_power_cube_relation` — Fermat's exponent 3 — closes it.

`three_four_four_same_parity` is the branch statement itself, with no prose step left. -/

/-- The square identity behind the reconstruction: `(C-B)² + (C+B)² = 2(C²+B²)`. -/
theorem sq_sub_add {B C : ℕ} (hlt : B < C) :
    (C - B) ^ 2 + (C + B) ^ 2 = 2 * (C ^ 2 + B ^ 2) := by
  obtain ⟨d, rfl⟩ : ∃ d, C = B + d := ⟨C - B, by omega⟩
  have hd : B + d - B = d := by omega
  rw [hd]; ring

/-- **The (3,4,4) same-parity branch, closed.** -/
theorem three_four_four_same_parity {A B C : ℕ}
    (hA : 0 < A) (hB : Odd B) (hC : Odd C) (hlt : B < C) (hcop : Nat.Coprime B C)
    (h : A ^ 3 + B ^ 4 = C ^ 4) : False := by
  obtain ⟨a, b, u, v, w, t, huodd, hvodd, hwodd, htodd, hu, hv, hw, hdvd, hcube⟩ :=
    descent_two_adic (by omega) hB hC hlt h
  obtain ⟨hp, hq, hr⟩ := odd_parts_cubes hcop hlt huodd hvodd hwodd hu hv hw hcube
  obtain ⟨p, hp⟩ := hp; obtain ⟨q, hq⟩ := hq; obtain ⟨r, hr⟩ := hr
  have hP := nat_cube_of_int_cube hp
  have hQ := nat_cube_of_int_cube hq
  have hR := nat_cube_of_int_cube hr
  obtain ⟨ha1, hb1, hor, hnot11⟩ := two_exponents hB hC hlt huodd hvodd hu hv
  -- positivity of the odd parts
  have hupos : 0 < u := by rcases huodd with ⟨k, hk⟩; omega
  have hvpos : 0 < v := by rcases hvodd with ⟨k, hk⟩; omega
  have hwpos : 0 < w := by rcases hwodd with ⟨k, hk⟩; omega
  have hPpos : 0 < p.natAbs := by
    by_contra hcon; rw [hP, show p.natAbs = 0 by omega] at hupos; simp at hupos
  have hQpos : 0 < q.natAbs := by
    by_contra hcon; rw [hQ, show q.natAbs = 0 by omega] at hvpos; simp at hvpos
  have hRpos : 0 < r.natAbs := by
    by_contra hcon; rw [hR, show r.natAbs = 0 by omega] at hwpos; simp at hwpos
  -- the reconstruction: 4^a u² + 4^b v² = 4 w
  have hsq : 4 ^ a * u ^ 2 + 4 ^ b * v ^ 2 = 4 * w := by
    have h2 := sq_sub_add (B := B) (C := C) hlt
    rw [hu, hv, hw] at h2
    have e1 : (2 ^ a * u) ^ 2 = 4 ^ a * u ^ 2 := by
      rw [mul_pow, ← pow_mul, mul_comm a 2, pow_mul]; norm_num
    have e2 : (2 ^ b * v) ^ 2 = 4 ^ b * v ^ 2 := by
      rw [mul_pow, ← pow_mul, mul_comm b 2, pow_mul]; norm_num
    rw [e1, e2] at h2; omega
  rcases hor with rfl | rfl
  · -- a = 1, so b ≥ 2 and w = u² + 4^(b-1) v²
    have hb2 : 2 ≤ b := by omega
    have hkey : w = u ^ 2 + 4 ^ (b - 1) * v ^ 2 := by
      have hb : (4 : ℕ) ^ b = 4 * 4 ^ (b - 1) := by
        conv_lhs => rw [show b = 1 + (b - 1) by omega]
        rw [pow_add, pow_one]
      have h4 : 4 * (u ^ 2 + 4 ^ (b - 1) * v ^ 2) = 4 * w := by
        rw [← hsq, pow_one, hb]; ring
      exact (Nat.eq_of_mul_eq_mul_left (by norm_num) h4).symm
    have hlam := four_pow_cube_of_valuation hb2 (by omega : 3 ∣ b + 2)
    refine no_sixth_power_cube_relation (μ := p.natAbs) (ν := q.natAbs) (τ := r.natAbs)
      (lam := 2 ^ (2 * ((b - 1) / 3))) hPpos hQpos hRpos (by positivity) ?_
    have : w = p.natAbs ^ 6 + (2 ^ (2 * ((b - 1) / 3))) ^ 3 * q.natAbs ^ 6 := by
      rw [hkey, hP, hQ, ← hlam]; ring
    rw [← this, hR]
  · -- b = 1, so a ≥ 2 and w = 4^(a-1) u² + v²
    have ha2 : 2 ≤ a := by omega
    have hkey : w = v ^ 2 + 4 ^ (a - 1) * u ^ 2 := by
      have ha : (4 : ℕ) ^ a = 4 * 4 ^ (a - 1) := by
        conv_lhs => rw [show a = 1 + (a - 1) by omega]
        rw [pow_add, pow_one]
      have h4 : 4 * (v ^ 2 + 4 ^ (a - 1) * u ^ 2) = 4 * w := by
        rw [← hsq, pow_one, ha]; ring
      exact (Nat.eq_of_mul_eq_mul_left (by norm_num) h4).symm
    have hlam := four_pow_cube_of_valuation ha2 (by omega : 3 ∣ a + 2)
    refine no_sixth_power_cube_relation (μ := q.natAbs) (ν := p.natAbs) (τ := r.natAbs)
      (lam := 2 ^ (2 * ((a - 1) / 3))) hQpos hPpos hRpos (by positivity) ?_
    have : w = q.natAbs ^ 6 + (2 ^ (2 * ((a - 1) / 3))) ^ 3 * p.natAbs ^ 6 := by
      rw [hkey, hP, hQ, ← hlam]; ring
    rw [← this, hR]

/-! ### The opposite-parity branch needs no elliptic Chabauty (U315, pool C172)

The checkpoint `research/checkpoints/U278_cohen344_descent.md` and pool C155/C156 recorded the
opposite-parity branch as blocked on elliptic Chabauty for `y² = x³ − 972`.  That reduction is
**unnecessary**.  When exactly one of `B, C` is even, all three factors of
`A³ = (C−B)(C+B)(C²+B²)` are **odd**, so the 2-adic bookkeeping that made the same-parity branch
hard simply does not arise: the three factors are pairwise coprime and each is a cube outright.

Writing `C−B = μ³` and `C+B = ν³`, the identity `(C−B)² + (C+B)² = 2(C²+B²)` becomes

    (μ²)³ + (ν²)³ = 2 τ³,

which is **Euler's equation** `a³ + b³ = 2c³`.  Its only coprime solutions have `a = b`, giving
`μ = ν`, hence `C−B = C+B`, hence `B = 0` — excluded.

Formalised below is the **reduction**, not the closure: mathlib has no `a³+b³=2c³` theorem (checked
by grep over `Mathlib/`), so the branch now depends on a classical named theorem instead of on a
computation this project cannot run.  The reduction is checked numerically in
`code/U315_opposite_parity.py`: 32,335 opposite-parity coprime pairs with all three factors odd and
pairwise coprime, 364 reconstruction identities, and no solution of `a³+b³=2c³` with `a ≠ b` below
3,000 — the last being a bounded search, which the survey gate says can never prove Euler. -/

theorem sq_mod_two (n : ℕ) : n ^ 2 % 2 = n % 2 := by
  rcases Nat.even_or_odd n with ⟨j, hj⟩ | ⟨j, hj⟩
  · subst hj
    have e : (j + j) ^ 2 = 2 * (2 * j * j) := by ring
    rw [e]; omega
  · subst hj
    have e : (2 * j + 1) ^ 2 = 2 * (2 * j * j + 2 * j) + 1 := by ring
    rw [e]; omega

theorem opposite_parity_factors_odd {B C : ℕ} (hlt : B < C)
    (hpar : (Odd B ∧ Even C) ∨ (Even B ∧ Odd C)) :
    Odd (C - B) ∧ Odd (C + B) ∧ Odd (C ^ 2 + B ^ 2) := by
  have hb := sq_mod_two B
  have hc := sq_mod_two C
  rcases hpar with ⟨hBo, hCe⟩ | ⟨hBe, hCo⟩
  · rw [Nat.odd_iff] at hBo; rw [Nat.even_iff] at hCe
    exact ⟨Nat.odd_iff.mpr (by omega), Nat.odd_iff.mpr (by omega), Nat.odd_iff.mpr (by omega)⟩
  · rw [Nat.even_iff] at hBe; rw [Nat.odd_iff] at hCo
    exact ⟨Nat.odd_iff.mpr (by omega), Nat.odd_iff.mpr (by omega), Nat.odd_iff.mpr (by omega)⟩


/-- **The opposite-parity branch of `(3,4,4)` reduces to Euler's equation `a³ + b³ = 2c³`.** -/
theorem opposite_parity_reduction {A B C : ℕ} (hA : 0 < A) (hBpos : 0 < B) (hlt : B < C)
    (hcop : Nat.Coprime B C) (hpar : (Odd B ∧ Even C) ∨ (Even B ∧ Odd C))
    (h : A ^ 3 + B ^ 4 = C ^ 4) :
    ∃ m n r : ℕ, 0 < m ∧ 0 < n ∧ 0 < r ∧ Nat.Coprime m n ∧ C - B = m ^ 3 ∧ C + B = n ^ 3 ∧
      (m ^ 2) ^ 3 + (n ^ 2) ^ 3 = 2 * r ^ 3 := by
  obtain ⟨hu, hv, hw⟩ := opposite_parity_factors_odd hlt hpar
  set u := C - B with hud
  set v := C + B with hvd
  set w := C ^ 2 + B ^ 2 with hwd
  have hfac := quartic_factorisation hlt h
  have hprod : 2 ^ 0 * (u * (v * w)) = A ^ 3 := by rw [hfac]; ring
  obtain ⟨s, t, htodd, hAs, hexp, hcube⟩ := odd_part_cube (hu.mul (hv.mul hw)) (by omega) hprod
  -- coprimality over ℤ
  have hBC : IsCoprime (B : ℤ) (C : ℤ) := by
    rw [Int.isCoprime_iff_gcd_eq_one]; simpa using hcop
  have hcastsub : ((u : ℕ) : ℤ) = (C : ℤ) - (B : ℤ) := by
    rw [hud]; push_cast [Nat.cast_sub (le_of_lt hlt)]; ring
  have hcastadd : ((v : ℕ) : ℤ) = (C : ℤ) + (B : ℤ) := by rw [hvd]; push_cast; ring
  have hcastsq : ((w : ℕ) : ℤ) = (C : ℤ) ^ 2 + (B : ℤ) ^ 2 := by rw [hwd]; push_cast; ring
  have huv : IsCoprime (u : ℤ) (v : ℤ) :=
    isCoprime_of_forall_common_unit fun d hd1 hd2 =>
      odd_common_divisor_sub_add hBC (not_two_dvd_of_dvd_odd hu hd1)
        (hcastsub ▸ hd1) (hcastadd ▸ hd2)
  have huw : IsCoprime (u : ℤ) (w : ℤ) :=
    isCoprime_of_forall_common_unit fun d hd1 hd2 =>
      odd_common_divisor_sub_sqsum hBC (not_two_dvd_of_dvd_odd hu hd1)
        (hcastsub ▸ hd1) (hcastsq ▸ hd2)
  have hvw : IsCoprime (v : ℤ) (w : ℤ) :=
    isCoprime_of_forall_common_unit fun d hd1 hd2 =>
      odd_common_divisor_add_sqsum hBC (not_two_dvd_of_dvd_odd hv hd1)
        (hcastadd ▸ hd1) (hcastsq ▸ hd2)
  have hcube' : u * v * w = t ^ 3 := by rw [← hcube]; ring
  have hc3 : (u : ℤ) * (v : ℤ) * (w : ℤ) = (t : ℤ) ^ 3 := by exact_mod_cast hcube'
  obtain ⟨⟨p, hp⟩, ⟨q, hq⟩, ⟨r, hr⟩⟩ := three_coprime_factors_cubes huv huw hvw hc3
  have hP := nat_cube_of_int_cube hp
  have hQ := nat_cube_of_int_cube hq
  have hR := nat_cube_of_int_cube hr
  have hupos : 0 < u := by rw [hud]; omega
  have hvpos : 0 < v := by rw [hvd]; omega
  have hwpos : 0 < w := by rw [hwd]; positivity
  have hcopmn : Nat.Coprime p.natAbs q.natAbs := by
    have huvnat : Nat.Coprime u v := by
      rw [Nat.coprime_iff_gcd_eq_one]
      have := Int.isCoprime_iff_gcd_eq_one.mp huv
      simpa using this
    rw [hP, hQ] at huvnat
    have h1 : Nat.Coprime p.natAbs (q.natAbs ^ 3) :=
      (Nat.coprime_pow_left_iff (n := 3) (by norm_num) _ _).mp huvnat
    exact (Nat.coprime_pow_right_iff (n := 3) (by norm_num) _ _).mp h1
  refine ⟨p.natAbs, q.natAbs, r.natAbs, ?_, ?_, ?_, hcopmn, hP, hQ, ?_⟩
  · by_contra hc; rw [hP, show p.natAbs = 0 by omega] at hupos; simp at hupos
  · by_contra hc; rw [hQ, show q.natAbs = 0 by omega] at hvpos; simp at hvpos
  · by_contra hc; rw [hR, show r.natAbs = 0 by omega] at hwpos; simp at hwpos
  · have h2 := sq_sub_add (B := B) (C := C) hlt
    rw [← hud, ← hvd, ← hwd] at h2
    rw [hP, hQ, hR] at h2
    have e1 : ((p.natAbs ^ 3) ^ 2 : ℕ) = (p.natAbs ^ 2) ^ 3 := by ring
    have e2 : ((q.natAbs ^ 3) ^ 2 : ℕ) = (q.natAbs ^ 2) ^ 3 := by ring
    rw [e1, e2] at h2
    omega

/-! ### The infinite family this closes (U331, pool C186) -/

/-- **The infinite family the same-parity theorem actually closes.**  Instance closure: if
`3 ∣ x`, `4 ∣ y`, `4 ∣ z` then `A^x + B^y = C^z` reads `(A^k)^3 + (B^m)^4 = (C^n)^4`, so the
same-parity theorem applies whenever the two rewritten bases `B^m`, `C^n` are odd and coprime. -/
theorem three_four_four_family {A B C k m n : ℕ}
    (hA : 0 < A) (hk : 0 < k)
    (hB : Odd (B ^ m)) (hC : Odd (C ^ n)) (hlt : B ^ m < C ^ n)
    (hcop : Nat.Coprime (B ^ m) (C ^ n))
    (h : A ^ (3 * k) + B ^ (4 * m) = C ^ (4 * n)) : False := by
  have hrw : (A ^ k) ^ 3 + (B ^ m) ^ 4 = (C ^ n) ^ 4 := by
    rw [← pow_mul, ← pow_mul, ← pow_mul]
    rw [mul_comm k 3, mul_comm m 4, mul_comm n 4] at *
    exact h
  exact three_four_four_same_parity (by positivity) hB hC hlt hcop hrw

end Beal
