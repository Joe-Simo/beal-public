/-
# Euler's `a³ + b³ = 2c³`, reduced to its descent step (U321, pool C177)

`Cohen344.lean` closes `(3,4,4)` given `EulerCubicTwo`.  This file shrinks that gap: the elementary
half of Euler's argument is proved here, leaving only the step where the factorisation in `ℤ[ω]`
is actually needed.

* `euler_both_odd` — in `a³ + b³ = 2c³` with `a, b` coprime, both are odd (equal parity from the
  cube-parity fact `n³ ≡ n (mod 2)`, and both-even is excluded by coprimality).
* `euler_identity` — `(p+q)³ + (p−q)³ = 2p(p² + 3q²)`, one `ring` call.
* `euler_of_descent` — with `p = (a+b)/2`, `q = (a−b)/2` (integers, since `a, b` are odd) and
  `IsCoprime p q`, the equation becomes `p(p² + 3q²) = c³`, so `q = 0` gives `a = b`.

What remains is `EulerDescentStep`: `p ≠ 0 → IsCoprime p q → p(p² + 3q²) = c³ → q = 0`.

**The hypothesis `p ≠ 0` is not decoration.**  The statement without it is **false**: `p = 0`,
`q = 1`, `c = 0` satisfies `IsCoprime 0 1` (as `0·0 + 1·1 = 1`) and `0·(0 + 3) = 0³`, with `q ≠ 0`.
That counterexample was found by exact search in this cycle, *after* the `Prop` had been recorded
without the hypothesis — see pool C177, where the error is preserved.  With `0 < p` an exact search
over `1 ≤ p, q ≤ 4000` finds nothing, and over `-1200 ≤ p < 0` likewise.  The Euler reduction does
supply `p ≠ 0`, since `p = (a+b)/2` with `a, b > 0`.

The rest is the classical part — one shows `p² + 3q² = (p + q√-3)(p − q√-3)` has coprime factors in `ℤ[ω]`, each a
cube, giving `p = s(s−3t)(s+3t)` with pairwise coprime factors, hence a strictly smaller solution.

**It is feasible here but not done.**  mathlib has `IsPrincipalIdealRing (𝓞 K)` for
`K = ℚ(ζ₃)` (`Mathlib/NumberTheory/Cyclotomic/PID.lean`, `three_pid`), so the unique factorisation
needed is available; the unit group has order `6`, so the cube-extraction needs unit bookkeeping
rather than a `Subsingleton` instance.  Estimated at a few hundred lines; not attempted.

`EulerDescentStep` is a stated `Prop`, so every use shows in the type.

No `sorry`, no custom `axiom`s; mathlib only.
-/
import Beal.Cohen344
import Mathlib.Data.Nat.Factors

namespace Beal

/-- The substitution identity behind Euler's descent: with `a = p+q`, `b = p-q`,
`a³ + b³ = 2p(p² + 3q²)`. -/
theorem euler_identity (p q : ℤ) : (p + q) ^ 3 + (p - q) ^ 3 = 2 * (p * (p ^ 2 + 3 * q ^ 2)) := by
  ring

/-- In `a³ + b³ = 2c³` with `a, b` coprime, both `a` and `b` are odd. -/
theorem euler_both_odd {a b c : ℕ} (hab : Nat.Coprime a b) (h : a ^ 3 + b ^ 3 = 2 * c ^ 3) :
    a % 2 = 1 ∧ b % 2 = 1 := by
  have hcube : ∀ n : ℕ, n ^ 3 % 2 = n % 2 := by
    intro n
    rcases Nat.even_or_odd n with ⟨j, hj⟩ | ⟨j, hj⟩
    · subst hj; have e : (j + j) ^ 3 = 2 * (4 * j ^ 3) := by ring
      rw [e]; omega
    · subst hj
      have e : (2 * j + 1) ^ 3 = 2 * (4 * j ^ 3 + 6 * j ^ 2 + 3 * j) + 1 := by ring
      rw [e]; omega
  have ha := hcube a
  have hb := hcube b
  have hsum : (a ^ 3 + b ^ 3) % 2 = 0 := by omega
  -- a and b have the same parity; coprimality rules out both even
  have hpar : a % 2 = b % 2 := by omega
  rcases Nat.even_or_odd a with hae | hao
  · exfalso
    obtain ⟨k, hk⟩ := hae
    have hbe : b % 2 = 0 := by omega
    have : 2 ∣ Nat.gcd a b := Nat.dvd_gcd ⟨k, by omega⟩ ⟨b / 2, by omega⟩
    rw [hab] at this; omega
  · rw [Nat.odd_iff] at hao; exact ⟨hao, by omega⟩

/-- **The descent step, isolated.**  Euler's theorem reduces to this statement about
`p(p² + 3q²) = c³`, which is where the factorisation in `ℤ[ω]` is needed.  Stated, not proved. -/
def EulerDescentStep : Prop :=
  ∀ p q c : ℤ, p ≠ 0 → IsCoprime p q → p * (p ^ 2 + 3 * q ^ 2) = c ^ 3 → q = 0

/-- In Euler descent, when `a` is odd and `a = p + q`, `p` and `q` must have opposite parity. -/
theorem euler_pq_opposite_parity {a : ℕ} (haodd : a % 2 = 1) {p q : ℤ}
    (hap : (a : ℤ) = p + q) : ¬ (2 : ℤ) ∣ (p - q) := by
  intro h2
  obtain ⟨k, hk⟩ := h2
  have ha_even : (2 : ℤ) ∣ (a : ℤ) := by
    refine ⟨k + q, ?_⟩
    calc (a : ℤ) = p + q := hap
      _ = (p - q) + 2 * q := by ring
      _ = 2 * k + 2 * q := by rw [hk]
      _ = 2 * (k + q) := by ring
  have ha_mod : (a : ℤ) % 2 = 0 := by
    obtain ⟨m, hm⟩ := ha_even
    omega
  have ha_nat : a % 2 = 0 := by exact_mod_cast ha_mod
  omega

/-- Euler's theorem follows from the descent step.  The reduction is elementary: `a, b` are both
odd, so `p = (a+b)/2` and `q = (a-b)/2` are integers, they are coprime, and `euler_identity`
turns `a³ + b³ = 2c³` into `p(p² + 3q²) = c³`.  Then `q = 0` gives `a = b`. -/
theorem euler_of_descent (H : EulerDescentStep) : EulerCubicTwo := by
  intro a b c ha hb hc hab heq
  obtain ⟨haodd, hbodd⟩ := euler_both_odd hab heq
  -- work in ℤ
  set p : ℤ := ((a : ℤ) + (b : ℤ)) / 2 with hp
  set q : ℤ := ((a : ℤ) - (b : ℤ)) / 2 with hq
  have h2a : (2 : ℤ) ∣ ((a : ℤ) + (b : ℤ)) := by
    obtain ⟨j, hj⟩ : ∃ j, a = 2 * j + 1 := ⟨a / 2, by omega⟩
    obtain ⟨k, hk⟩ : ∃ k, b = 2 * k + 1 := ⟨b / 2, by omega⟩
    exact ⟨(j : ℤ) + (k : ℤ) + 1, by subst hj; subst hk; push_cast; ring⟩
  have h2s : (2 : ℤ) ∣ ((a : ℤ) - (b : ℤ)) := by
    obtain ⟨j, hj⟩ : ∃ j, a = 2 * j + 1 := ⟨a / 2, by omega⟩
    obtain ⟨k, hk⟩ : ∃ k, b = 2 * k + 1 := ⟨b / 2, by omega⟩
    exact ⟨(j : ℤ) - (k : ℤ), by subst hj; subst hk; push_cast; ring⟩
  have hap : (a : ℤ) = p + q := by
    rw [hp, hq]; obtain ⟨s, hs⟩ := h2a; obtain ⟨t, ht⟩ := h2s
    rw [hs, ht]; omega
  have hbp : (b : ℤ) = p - q := by
    rw [hp, hq]; obtain ⟨s, hs⟩ := h2a; obtain ⟨t, ht⟩ := h2s
    rw [hs, ht]; omega
  have hcop : IsCoprime p q := by
    have hZ : IsCoprime (a : ℤ) (b : ℤ) := by
      rw [Int.isCoprime_iff_gcd_eq_one]; simpa using hab
    obtain ⟨u, v, huv⟩ := hZ
    exact ⟨u + v, u - v, by rw [hap, hbp] at huv; linarith⟩
  have hkey : p * (p ^ 2 + 3 * q ^ 2) = (c : ℤ) ^ 3 := by
    have hZ : ((a : ℤ)) ^ 3 + ((b : ℤ)) ^ 3 = 2 * ((c : ℤ)) ^ 3 := by exact_mod_cast heq
    rw [hap, hbp, euler_identity] at hZ
    linarith
  have hppos : p ≠ 0 := by
    have : (0 : ℤ) < (a : ℤ) + (b : ℤ) := by positivity
    rw [hap, hbp] at this
    intro h0; rw [h0] at this; omega
  have hq0 : q = 0 := H p q (c : ℤ) hppos hcop hkey
  have : (a : ℤ) = (b : ℤ) := by rw [hap, hbp, hq0]; ring
  exact_mod_cast this

/-- The whole `(3,4,4)` signature, from the descent step alone. -/
theorem cohen344_of_descent (H : EulerDescentStep) : NoCoprimeSol 3 4 4 :=
  cohen344_of_euler (euler_of_descent H)

/-! ### First steps of the descent (U324, pool C179)

`EulerDescentStep` splits on whether `3 ∣ p`, because `gcd(p, p² + 3q²)` divides `3q²` and hence,
by coprimality of `p` and `q`, divides `3`.  The `3 ∤ p` branch is set up here: the two factors are
coprime, so each is a cube, by the same `Int.eq_pow_of_mul_eq_pow_odd` used for the `(3,4,4)`
descent.  The `3 ∣ p` branch is rewritten into the shape the classical argument uses.

**What is still missing** is the heart: from `p² + 3q² = t³` with `p, q` coprime, the factorisation
in `ℤ[ω]` gives `p = s(s − 3t')(s + 3t')` with pairwise coprime factors, hence three cubes and a
strictly smaller solution.  That is the part needing `three_pid`, and it is not written. -/

/-- If `3 ∤ p` and `p, q` are coprime then `p` and `p² + 3q²` are coprime. -/
theorem coprime_p_norm {p q : ℤ} (hpq : IsCoprime p q) (h3 : ¬ (3 : ℤ) ∣ p) :
    IsCoprime p (p ^ 2 + 3 * q ^ 2) := by
  have hq2 : IsCoprime p (q ^ 2) := hpq.pow_right
  have h3p : IsCoprime p 3 := by
    have : IsCoprime (3 : ℤ) p := (Int.prime_three.irreducible.coprime_iff_not_dvd).mpr h3
    exact this.symm
  have h3q2 : IsCoprime p (3 * q ^ 2) := h3p.mul_right hq2
  -- p^2 + 3q^2 ≡ 3q^2 modulo p
  obtain ⟨u, v, huv⟩ := h3q2
  exact ⟨u - v * p, v, by linear_combination huv⟩

/-- The `3 ∣ p` branch: writing `p = 3p'`, the equation becomes `9p'(3p'² + q²) = c³`. -/
theorem three_dvd_p_rewrite {p q c p' : ℤ} (hp : p = 3 * p')
    (h : p * (p ^ 2 + 3 * q ^ 2) = c ^ 3) :
    9 * (p' * (3 * p' ^ 2 + q ^ 2)) = c ^ 3 := by
  subst hp; linear_combination h

/-- In the `3 ∣ p` branch, `9 ∣ c³` forces `3 ∣ c`. -/
theorem three_dvd_c_of_nine_dvd {c : ℤ} (h : (9 : ℤ) ∣ c ^ 3) : (3 : ℤ) ∣ c := by
  have : (3 : ℤ) ∣ c ^ 3 := dvd_trans (by decide) h
  exact Int.prime_three.dvd_of_dvd_pow this

/-- Step 1 of `3 ∣ p` reduction: substituting `c = 3c'` divides out 9, yielding
`p'(q² + 3p'²) = 3c'³`. -/
theorem three_dvd_p_branch_step1 {p' q c c' : ℤ}
    (hc : c = 3 * c')
    (h : 9 * (p' * (3 * p' ^ 2 + q ^ 2)) = c ^ 3) :
    p' * (q ^ 2 + 3 * p' ^ 2) = 3 * c' ^ 3 := by
  have h27 : c ^ 3 = 9 * (3 * c' ^ 3) := by
    calc c ^ 3 = (3 * c') ^ 3 := by rw [hc]
      _ = 9 * (3 * c' ^ 3) := by ring
  rw [h27] at h
  have h9 : (9 : ℤ) ≠ 0 := by decide
  have heq : p' * (3 * p' ^ 2 + q ^ 2) = 3 * c' ^ 3 := mul_left_cancel₀ h9 h
  calc p' * (q ^ 2 + 3 * p' ^ 2) = p' * (3 * p' ^ 2 + q ^ 2) := by ring
    _ = 3 * c' ^ 3 := heq

/-- Step 2 of `3 ∣ p` reduction: since `gcd(3p', q) = 1`, 3 cannot divide `q² + 3p'²`,
hence 3 must divide `p'`. -/
theorem three_dvd_p'_of_coprime {p' q c' : ℤ}
    (hcop : IsCoprime (3 * p') q)
    (hprod : p' * (q ^ 2 + 3 * p' ^ 2) = 3 * c' ^ 3) :
    (3 : ℤ) ∣ p' := by
  have hdvd : (3 : ℤ) ∣ p' * (q ^ 2 + 3 * p' ^ 2) := ⟨c' ^ 3, by rw [hprod]⟩
  rcases Int.prime_three.dvd_mul.mp hdvd with h3p' | h3q
  · exact h3p'
  · exfalso
    have hq2 : (3 : ℤ) ∣ q ^ 2 := by
      have : q ^ 2 = (q ^ 2 + 3 * p' ^ 2) - 3 * p' ^ 2 := by ring
      rw [this]
      exact dvd_sub h3q ⟨p' ^ 2, rfl⟩
    have h3_dvd_q : (3 : ℤ) ∣ q := Int.prime_three.dvd_of_dvd_pow hq2
    have h3_dvd_3p' : (3 : ℤ) ∣ (3 * p') := ⟨p', rfl⟩
    have : (3 : ℤ) ∣ (1 : ℤ) := by
      obtain ⟨u, v, huv⟩ := hcop
      have : (3 : ℤ) ∣ u * (3 * p') + v * q := dvd_add (dvd_mul_of_dvd_right h3_dvd_3p' u) (dvd_mul_of_dvd_right h3_dvd_q v)
      rwa [huv] at this
    have : (3 : ℤ) ≤ 1 := Int.le_of_dvd (by decide) this
    omega

/-- Step 3 of `3 ∣ p` reduction: writing `p' = 3p''` cancels the remaining 3, yielding
`p''(q² + 3(3p'')²) = c'³`. The roles of the coordinates are swapped, and `3 ∤ q`. -/
theorem three_dvd_p_branch_step3 {p' p'' q c' : ℤ}
    (hp' : p' = 3 * p'')
    (hprod : p' * (q ^ 2 + 3 * p' ^ 2) = 3 * c' ^ 3) :
    p'' * (q ^ 2 + 3 * (3 * p'') ^ 2) = c' ^ 3 := by
  rw [hp'] at hprod
  have h3 : (3 : ℤ) ≠ 0 := by decide
  have : 3 * (p'' * (q ^ 2 + 3 * (3 * p'') ^ 2)) = 3 * c' ^ 3 := by
    calc 3 * (p'' * (q ^ 2 + 3 * (3 * p'') ^ 2))
        = (3 * p'') * (q ^ 2 + 3 * (3 * p'') ^ 2) := by ring
      _ = 3 * c' ^ 3 := hprod
  exact mul_left_cancel₀ h3 this

/-- Absolute value inequality transfers to `Nat.natAbs`. -/
theorem natAbs_lt_of_abs_lt {x y : ℤ} (h : |x| < |y|) : x.natAbs < y.natAbs := by
  have hx : |x| = (x.natAbs : ℤ) := (Int.natCast_natAbs x).symm
  have hy : |y| = (y.natAbs : ℤ) := (Int.natCast_natAbs y).symm
  rw [hx, hy] at h
  exact Int.ofNat_lt.mp h

/-- In the `3 ∣ p` branch, `c` strictly decreases in natural magnitude: `c'.natAbs < c.natAbs` when `c ≠ 0`. -/
theorem three_dvd_c_natAbs_lt {c c' : ℤ} (hc : c = 3 * c') (hc_ne : c ≠ 0) :
    c'.natAbs < c.natAbs := by
  have hc'ne : c' ≠ 0 := by
    rintro rfl
    apply hc_ne
    rw [hc]
    ring
  have hpos : 0 < |c'| := abs_pos.mpr hc'ne
  have hlt : |c'| < |c| := by
    rw [hc, abs_mul]
    have : |(3 : ℤ)| = 3 := by decide
    rw [this]
    linarith
  exact natAbs_lt_of_abs_lt hlt

/-- Coprimality of factors in the swapped equation of the `3 ∣ p` branch. -/
theorem coprime_p''_norm {p'' q : ℤ} (hcop : IsCoprime (9 * p'') q) :
    IsCoprime p'' (q ^ 2 + 3 * (3 * p'') ^ 2) := by
  have hcop_p'' : IsCoprime p'' q := by
    obtain ⟨u, v, huv⟩ := hcop
    refine ⟨u * 9, v, ?_⟩
    calc u * 9 * p'' + v * q = u * (9 * p'') + v * q := by ring
      _ = 1 := huv
  have hq2 : IsCoprime p'' (q ^ 2) := hcop_p''.pow_right
  have h27 : q ^ 2 + 3 * (3 * p'') ^ 2 = q ^ 2 + (27 * p'') * p'' := by ring
  rw [h27]
  exact hq2.add_mul_right_right (27 * p'')

/-- In the swapped equation of the `3 ∣ p` branch, both factors are cubes. -/
theorem factors_are_cubes_swapped {p'' q c' : ℤ} (hcop : IsCoprime (9 * p'') q)
    (hprod : p'' * (q ^ 2 + 3 * (3 * p'') ^ 2) = c' ^ 3) :
    (∃ s, p'' = s ^ 3) ∧ (∃ t, q ^ 2 + 3 * (3 * p'') ^ 2 = t ^ 3) := by
  have hcop_factors := coprime_p''_norm hcop
  have hodd : Odd 3 := ⟨1, by norm_num⟩
  exact ⟨Int.eq_pow_of_mul_eq_pow_odd_left hcop_factors hodd hprod,
    Int.eq_pow_of_mul_eq_pow_odd_right hcop_factors hodd hprod⟩


/-- In the branch `3 ∤ p`, both factors are cubes. -/
theorem factors_are_cubes {p q c : ℤ} (hpq : IsCoprime p q) (h3 : ¬ (3 : ℤ) ∣ p)
    (h : p * (p ^ 2 + 3 * q ^ 2) = c ^ 3) :
    (∃ s, p = s ^ 3) ∧ (∃ t, p ^ 2 + 3 * q ^ 2 = t ^ 3) := by
  have hcop := coprime_p_norm hpq h3
  have hodd : Odd 3 := ⟨1, by norm_num⟩
  exact ⟨Int.eq_pow_of_mul_eq_pow_odd_left hcop hodd h,
    Int.eq_pow_of_mul_eq_pow_odd_right hcop hodd h⟩

/-- **Sub-step (2) of `EulerDescentStep` (U345, pool C200).**  With `gcd(a,b) = 1` and `3 ∤ a`, the
integer `a` is coprime to `3b`, hence to `a ± 3b`. -/
theorem coprime_a_three_b {a b : ℤ} (hab : IsCoprime a b) (h3 : ¬ (3 : ℤ) ∣ a) :
    IsCoprime a (3 * b) := by
  have h3a : IsCoprime a 3 :=
    ((Int.prime_three.irreducible.coprime_iff_not_dvd).mpr h3).symm
  exact h3a.mul_right hab

theorem coprime_a_sub {a b : ℤ} (hab : IsCoprime a b) (h3 : ¬ (3 : ℤ) ∣ a) :
    IsCoprime a (a - 3 * b) := by
  obtain ⟨u, v, huv⟩ := coprime_a_three_b hab h3
  exact ⟨u + v, -v, by linear_combination huv⟩

theorem coprime_a_add {a b : ℤ} (hab : IsCoprime a b) (h3 : ¬ (3 : ℤ) ∣ a) :
    IsCoprime a (a + 3 * b) := by
  obtain ⟨u, v, huv⟩ := coprime_a_three_b hab h3
  exact ⟨u - v, v, by linear_combination huv⟩

/-- Both `a - 3b` and `a + 3b` are odd when `a, b` have opposite parity. -/
theorem sub_add_odd {a b : ℤ} (hpar : (Even a ∧ Odd b) ∨ (Odd a ∧ Even b)) :
    Odd (a - 3 * b) ∧ Odd (a + 3 * b) := by
  rcases hpar with ⟨⟨k, hk⟩, ⟨m, hm⟩⟩ | ⟨⟨k, hk⟩, ⟨m, hm⟩⟩ <;> subst hk <;> subst hm <;>
    constructor <;> [exact ⟨k - 3 * m - 2, by ring⟩; exact ⟨k + 3 * m + 1, by ring⟩;
                     exact ⟨k - 3 * m, by ring⟩; exact ⟨k + 3 * m, by ring⟩]

/-- Two-to-one linear combination lift: if `C₁·X + C₂·Y = 2` and `X` is odd (`X = 2k + 1`),
then `(1 - k·C₁)·X - (k·C₂)·Y = 1`. -/
theorem coprime_of_two_linear_comb {X Y C₁ C₂ k : ℤ}
    (hcomb : C₁ * X + C₂ * Y = 2) (hodd : X = 2 * k + 1) :
    IsCoprime X Y := by
  refine ⟨1 - k * C₁, - (k * C₂), ?_⟩
  linear_combination -k * hcomb + hodd

/-- **Pairwise coprimality completed.**  When `gcd(a, b) = 1`, `3 ∤ a`, and `a, b` have
opposite parity, the two shifted factors `a - 3b` and `a + 3b` are mutually coprime. -/
theorem coprime_sub_add {a b : ℤ} (hab : IsCoprime a b) (h3 : ¬ (3 : ℤ) ∣ a)
    (hpar : (Even a ∧ Odd b) ∨ (Odd a ∧ Even b)) :
    IsCoprime (a - 3 * b) (a + 3 * b) := by
  obtain ⟨u, v, huv⟩ := coprime_a_three_b hab h3
  have hcomb : (u - v) * (a - 3 * b) + (u + v) * (a + 3 * b) = 2 := by
    calc (u - v) * (a - 3 * b) + (u + v) * (a + 3 * b)
        = 2 * (u * a + v * (3 * b)) := by ring
      _ = 2 * 1 := by rw [huv]
      _ = 2 := by ring
  obtain ⟨⟨k, hk⟩, -⟩ := sub_add_odd hpar
  exact coprime_of_two_linear_comb hcomb hk

/-- **The complete pairwise coprimality triplet of the factors of `p`.** -/
theorem pairwise_coprime_factors {a b : ℤ} (hab : IsCoprime a b) (h3 : ¬ (3 : ℤ) ∣ a)
    (hpar : (Even a ∧ Odd b) ∨ (Odd a ∧ Even b)) :
    IsCoprime a (a - 3 * b) ∧ IsCoprime a (a + 3 * b) ∧ IsCoprime (a - 3 * b) (a + 3 * b) :=
  ⟨coprime_a_sub hab h3, coprime_a_add hab h3, coprime_sub_add hab h3 hpar⟩

/-- When three pairwise coprime integers have a cube product, each factor is a cube. -/
theorem three_factors_are_cubes {A B C K : ℤ}
    (hAB : IsCoprime A B) (hAC : IsCoprime A C) (hBC : IsCoprime B C)
    (hprod : A * (B * C) = K ^ 3) :
    (∃ u, A = u ^ 3) ∧ (∃ v, B = v ^ 3) ∧ (∃ w, C = w ^ 3) := by
  have hA_BC : IsCoprime A (B * C) := hAB.mul_right hAC
  have hodd : Odd 3 := ⟨1, by norm_num⟩
  have hA_cube : ∃ u, A = u ^ 3 := Int.eq_pow_of_mul_eq_pow_odd_left hA_BC hodd hprod
  have hBC_cube : ∃ t, B * C = t ^ 3 := Int.eq_pow_of_mul_eq_pow_odd_right hA_BC hodd hprod
  obtain ⟨t, ht⟩ := hBC_cube
  have hB_cube : ∃ v, B = v ^ 3 := Int.eq_pow_of_mul_eq_pow_odd_left hBC hodd ht
  have hC_cube : ∃ w, C = w ^ 3 := Int.eq_pow_of_mul_eq_pow_odd_right hBC hodd ht
  exact ⟨hA_cube, hB_cube, hC_cube⟩

/-- **Closure of Euler's cubic parametrization to three cube factors.**
When `p = a * (a - 3*b) * (a + 3*b) = s^3` with coprime `a, b`, `3 ∤ a`, and opposite parity,
all three factors `a`, `a - 3*b`, and `a + 3*b` are integer cubes. -/
theorem euler_param_factors_are_cubes {a b s : ℤ}
    (hab : IsCoprime a b) (h3 : ¬ (3 : ℤ) ∣ a)
    (hpar : (Even a ∧ Odd b) ∨ (Odd a ∧ Even b))
    (hprod : a * (a - 3 * b) * (a + 3 * b) = s ^ 3) :
    (∃ u, a = u ^ 3) ∧ (∃ v, a - 3 * b = v ^ 3) ∧ (∃ w, a + 3 * b = w ^ 3) := by
  have ⟨h1, h2, h3c⟩ := pairwise_coprime_factors hab h3 hpar
  have hprod' : a * ((a - 3 * b) * (a + 3 * b)) = s ^ 3 := by
    calc a * ((a - 3 * b) * (a + 3 * b)) = a * (a - 3 * b) * (a + 3 * b) := by ring
      _ = s ^ 3 := hprod
  exact three_factors_are_cubes h1 h2 h3c hprod'

/-- **Euler's cube sum identity.**
The cube roots `v` and `w` of the shifted factors sum to twice the cube `u³ = a`. -/
theorem euler_param_cube_sum {a b u v w : ℤ}
    (ha : a = u ^ 3) (hv : a - 3 * b = v ^ 3) (hw : a + 3 * b = w ^ 3) :
    v ^ 3 + w ^ 3 = 2 * u ^ 3 := by
  calc v ^ 3 + w ^ 3
    _ = (a - 3 * b) + (a + 3 * b) := by rw [← hv, ← hw]
    _ = 2 * a := by ring
    _ = 2 * u ^ 3 := by rw [ha]

/-- Coprimality of cubes implies coprimality of their bases in `ℤ`. -/
theorem isCoprime_of_isCoprime_pow3 {x y : ℤ} (h : IsCoprime (x ^ 3) (y ^ 3)) :
    IsCoprime x y := by
  have hx : x ∣ x ^ 3 := ⟨x ^ 2, by ring⟩
  have hy : y ∣ y ^ 3 := ⟨y ^ 2, by ring⟩
  exact (h.of_isCoprime_of_dvd_left hx).of_isCoprime_of_dvd_right hy

/-- **Strict coprime descent solution.**
The cube roots `v` and `w` from the parametrization factors are coprime. -/
theorem euler_param_cube_roots_coprime {a b v w : ℤ}
    (hab : IsCoprime a b) (h3 : ¬ (3 : ℤ) ∣ a)
    (hpar : (Even a ∧ Odd b) ∨ (Odd a ∧ Even b))
    (hv : a - 3 * b = v ^ 3) (hw : a + 3 * b = w ^ 3) :
    IsCoprime v w := by
  have ⟨_, _, h3c⟩ := pairwise_coprime_factors hab h3 hpar
  have hpow : IsCoprime (v ^ 3) (w ^ 3) := by
    rwa [← hv, ← hw]
  exact isCoprime_of_isCoprime_pow3 hpow

/-! ### The Euler descent, skeletonised (U349, pool C204)

`EulerDescentStep` is decomposed into five steps.  Three are proved here outright; the two that
carry the classical content are stated as named `Prop`s, so every use shows in the type — the same
discipline as `EulerCubicTwo` itself. -/

/-- **Step 1a.**  The form `x² + 3y²` is multiplicative. -/
theorem form_mul (a b c d : ℤ) :
    (a ^ 2 + 3 * b ^ 2) * (c ^ 2 + 3 * d ^ 2)
      = (a * c - 3 * b * d) ^ 2 + 3 * (a * d + b * c) ^ 2 := by ring

/-- **Step 1b**, stated not proved: every ODD divisor of `p² + 3q²` with `p, q` coprime is itself
of the form `u² + 3v²`.  The oddness is not decoration — `2 ∣ 1² + 3·1²` while `2` is not of the
form, and `14 ∣ 1² + 3·3²` likewise (pool C202).  Classical proof: Fermat descent on the symmetric
residues mod `m`, whose strictness is checked in `code/U320_regression_checks.py` (pool C203). -/
def OddDivisorForm : Prop :=
  ∀ m p q : ℤ, ¬ (2 : ℤ) ∣ m → m ∣ p ^ 2 + 3 * q ^ 2 → IsCoprime p q →
    ∃ u v : ℤ, m = u ^ 2 + 3 * v ^ 2

/-- **Step 1c**, stated not proved: the parametrisation of cubes of the form.  Numerically
confirmed with zero unmatched cases in pool C199. -/
def CubeFormParam : Prop :=
  ∀ p q t : ℤ, IsCoprime p q → ¬ (2 : ℤ) ∣ (p - q) → p ^ 2 + 3 * q ^ 2 = t ^ 3 →
    ∃ a b : ℤ, p = a * (a - 3 * b) * (a + 3 * b) ∧ q = 3 * b * (a ^ 2 - b ^ 2)

/-- The factorisation used by step 1c, as a ring identity. -/
theorem param_factor (a b : ℤ) :
    a * (a - 3 * b) * (a + 3 * b) = a ^ 3 - 9 * a * b ^ 2 := by ring

theorem param_q (a b : ℤ) : 3 * b * (a ^ 2 - b ^ 2) = 3 * a ^ 2 * b - 3 * b ^ 3 := by ring

/-- The cubic norm identity for the Euler cube parametrisation:
`(a(a² - 9b²))² + 3(3b(a² - b²))² = (a² + 3b²)³`. -/
theorem cube_param_norm (a b : ℤ) :
    (a * (a - 3 * b) * (a + 3 * b)) ^ 2 + 3 * (3 * b * (a ^ 2 - b ^ 2)) ^ 2 = (a ^ 2 + 3 * b ^ 2) ^ 3 := by
  ring

/-- **Step 3.**  The descent lands back on Euler's own equation: the two outer factors sum to
twice the middle one, so three cubes `a = e³`, `a - 3b = f³`, `a + 3b = g³` give `f³ + g³ = 2e³`. -/
theorem descent_sum (a b : ℤ) : (a - 3 * b) + (a + 3 * b) = 2 * a := by ring

theorem descent_to_euler {a b e f g : ℤ} (he : a = e ^ 3) (hf : a - 3 * b = f ^ 3)
    (hg : a + 3 * b = g ^ 3) : f ^ 3 + g ^ 3 = 2 * e ^ 3 := by
  have := descent_sum a b
  rw [hf, hg, he] at this
  exact this

/-- **Descent loop closed.**  From the cube parametrization `p = a(a-3b)(a+3b) = s³`,
the factors give a new solution to Euler's equation `f³ + g³ = 2e³` with `e³ = a`,
`a - 3b = f³`, and `a + 3b = g³`. -/
theorem descent_step_to_euler {a b s : ℤ}
    (hab : IsCoprime a b) (h3 : ¬ (3 : ℤ) ∣ a)
    (hpar : (Even a ∧ Odd b) ∨ (Odd a ∧ Even b))
    (hprod : a * (a - 3 * b) * (a + 3 * b) = s ^ 3) :
    ∃ e f g : ℤ, f ^ 3 + g ^ 3 = 2 * e ^ 3 ∧ a = e ^ 3 ∧
      a - 3 * b = f ^ 3 ∧ a + 3 * b = g ^ 3 := by
  have ⟨h1, h2, h3c⟩ := pairwise_coprime_factors hab h3 hpar
  obtain ⟨⟨e, he⟩, ⟨f, hf⟩, ⟨g, hg⟩⟩ := three_coprime_factors_cubes h1 h2 h3c hprod
  exact ⟨e, f, g, descent_to_euler he hf hg, he, hf, hg⟩


/-- Squares modulo 3 are 0 or 1. -/
theorem sq_mod_three (X : ℤ) : X ^ 2 % 3 = 0 ∨ X ^ 2 % 3 = 1 := by
  have h3 : X % 3 = 0 ∨ X % 3 = 1 ∨ X % 3 = 2 := by omega
  have he : X ^ 2 % 3 = (X % 3) ^ 2 % 3 := by
    have : X = 3 * (X / 3) + X % 3 := by omega
    nth_rewrite 1 [this]
    have : (3 * (X / 3) + X % 3) ^ 2 = 3 * (3 * (X / 3) ^ 2 + 2 * (X / 3) * (X % 3)) + (X % 3) ^ 2 := by ring
    rw [this]
    omega
  rw [he]
  rcases h3 with h0 | h1 | h2
  · left; rw [h0]; decide
  · right; rw [h1]; decide
  · right; rw [h2]; decide

/-- For `3 ∤ a` and `b ≠ 0`, the difference `|a² - 9b²|` is strictly at least 2.
This proves that the parameter `a` is strictly smaller in magnitude than `p`. -/
theorem abs_diff_sq_ge_two {a b : ℤ} (h3 : ¬ (3 : ℤ) ∣ a) (hb : b ≠ 0) :
    2 ≤ |a ^ 2 - 9 * b ^ 2| := by
  have hsq := sq_mod_three a
  have ha1 : a ^ 2 % 3 = 1 := by
    rcases hsq with h0 | h1
    · exfalso
      have : (3 : ℤ) ∣ a ^ 2 := Int.dvd_of_emod_eq_zero h0
      exact h3 (Int.prime_three.dvd_of_dvd_pow this)
    · exact h1
  have hdiff : (a ^ 2 - 9 * b ^ 2) % 3 = 1 := by
    have : a ^ 2 - 9 * b ^ 2 = 3 * (-3 * b ^ 2) + a ^ 2 := by ring
    rw [this]
    omega
  by_contra! hc
  have hvals : a ^ 2 - 9 * b ^ 2 = -1 ∨ a ^ 2 - 9 * b ^ 2 = 0 ∨ a ^ 2 - 9 * b ^ 2 = 1 := by
    have h1 : -2 < a ^ 2 - 9 * b ^ 2 := neg_lt_of_abs_lt hc
    have h2 : a ^ 2 - 9 * b ^ 2 < 2 := lt_of_abs_lt hc
    omega
  rcases hvals with hneg1 | h0 | h1
  · have : (-1 : ℤ) % 3 = 2 := by decide
    omega
  · have : (0 : ℤ) % 3 = 0 := by decide
    omega
  · have hprod : (a - 3 * b) * (a + 3 * b) = 1 := by
      calc (a - 3 * b) * (a + 3 * b) = a ^ 2 - 9 * b ^ 2 := by ring
        _ = 1 := h1
    have hcases := Int.mul_eq_one_iff_eq_one_or_neg_one.mp hprod
    rcases hcases with ⟨h1a, h1b⟩ | ⟨h2a, h2b⟩
    · have : 6 * b = 0 := by linear_combination h1b - h1a
      omega
    · have : 6 * b = 0 := by linear_combination h2b - h2a
      omega

/-- **Strict magnitude descent.**  The parameter `a` satisfies `|a| < |p|`,
ensuring that the new solution `e³ = a` has strictly smaller magnitude `|e| < |s|`. -/
theorem abs_a_lt_abs_p {a b p : ℤ} (h3 : ¬ (3 : ℤ) ∣ a) (ha : a ≠ 0) (hb : b ≠ 0)
    (hp : p = a * (a ^ 2 - 9 * b ^ 2)) :
    |a| < |p| := by
  have hge := abs_diff_sq_ge_two h3 hb
  have hpos : 0 < |a| := abs_pos.mpr ha
  rw [hp, abs_mul]
  nlinarith

/-- Cube of absolute value is absolute value of cube. -/
theorem abs_pow_three (x : ℤ) : |x ^ 3| = |x| ^ 3 := by
  have h3 : x ^ 3 = x * (x * x) := by ring
  have h3' : |x| ^ 3 = |x| * (|x| * |x|) := by ring
  rw [h3, h3', abs_mul, abs_mul]

/-- Monotonicity of absolute cube: `|x³| < |y³|` implies `|x| < |y|`. -/
theorem abs_lt_of_cube_lt {e s : ℤ} (h : |e ^ 3| < |s ^ 3|) : |e| < |s| := by
  rw [abs_pow_three e, abs_pow_three s] at h
  by_contra! hc
  have he0 : 0 ≤ |e| := abs_nonneg e
  have hs0 : 0 ≤ |s| := abs_nonneg s
  have hs2 : |s| ^ 2 ≤ |e| ^ 2 := by nlinarith
  have hs3 : |s| ^ 3 ≤ |e| ^ 3 := by
    have : |s| ^ 3 = |s| * |s| ^ 2 := by ring
    have : |e| ^ 3 = |e| * |e| ^ 2 := by ring
    nlinarith
  linarith


/-- The new cube root `e` is strictly smaller in magnitude than `s`. -/
theorem abs_e_lt_abs_s {a b p e s : ℤ} (h3 : ¬ (3 : ℤ) ∣ a) (ha : a ≠ 0) (hb : b ≠ 0)
    (hp : p = a * (a ^ 2 - 9 * b ^ 2)) (he : a = e ^ 3) (hs : p = s ^ 3) :
    |e| < |s| := by
  have hlt : |a| < |p| := abs_a_lt_abs_p h3 ha hb hp
  rw [he, hs] at hlt
  exact abs_lt_of_cube_lt hlt

/-- The cube root `s` of `p` is strictly smaller in magnitude than `c` when `q ≠ 0`. -/
theorem abs_s_lt_abs_c {p q c s t : ℤ} (hp : p ≠ 0) (hq : q ≠ 0)
    (hprod : p * (p ^ 2 + 3 * q ^ 2) = c ^ 3)
    (hs : p = s ^ 3) (ht : p ^ 2 + 3 * q ^ 2 = t ^ 3) :
    |s| < |c| := by
  have ht_ge : 3 ≤ t ^ 3 := by
    have hq2 : 1 ≤ q ^ 2 := by
      have : 0 < q ^ 2 := sq_pos_of_ne_zero hq
      omega
    have hp2 : 0 ≤ p ^ 2 := sq_nonneg p
    linarith [ht.symm]
  have ht_gt_one : 2 ≤ t := by
    by_contra! hc
    have : t ^ 3 ≤ 1 := by
      rcases le_or_lt t 0 with ht0 | ht1
      · have : t ^ 3 ≤ 0 := by
          have : t ^ 3 = t * t ^ 2 := by ring
          have : 0 ≤ t ^ 2 := sq_nonneg t
          nlinarith
        omega
      · have : t = 1 := by omega
        subst this
        norm_num
    omega
  have ht_abs_ge : 2 ≤ |t| := by
    have : t ≤ |t| := le_abs_self t
    omega
  have hc3 : |c ^ 3| = |s ^ 3| * |t ^ 3| := by
    have : c ^ 3 = s ^ 3 * t ^ 3 := by rw [← hs, ← ht, ← hprod]
    rw [this, abs_mul]
  rw [abs_pow_three c, abs_pow_three s, abs_pow_three t] at hc3
  have hs_pos : 0 < |s| := by
    have : s ≠ 0 := by
      rintro rfl
      rw [hs] at hp
      exact hp (by norm_num)
    exact abs_pos.mpr this
  have hs3_pos : 0 < |s| ^ 3 := by
    have : |s| ^ 3 = |s| * (|s| * |s|) := by ring
    rw [this]
    positivity
  have ht3_ge : 8 ≤ |t| ^ 3 := by
    have : |t| ^ 3 = |t| * (|t| * |t|) := by ring
    rw [this]
    nlinarith
  have hlt : |s| ^ 3 < |c| ^ 3 := by
    calc |s| ^ 3 < |s| ^ 3 * 8 := by linarith
      _ ≤ |s| ^ 3 * |t| ^ 3 := by nlinarith
      _ = |c| ^ 3 := hc3.symm
  have hlt' : |s ^ 3| < |c ^ 3| := by
    rwa [abs_pow_three s, abs_pow_three c]
  exact abs_lt_of_cube_lt hlt'

/-- **Combined strict descent on Euler cubic parameter.**
The new base `e` satisfies `|e| < |c|`, strictly decreasing the magnitude. -/
theorem abs_e_lt_abs_c {a b p q c e s t : ℤ}
    (h3 : ¬ (3 : ℤ) ∣ a) (ha : a ≠ 0) (hb : b ≠ 0)
    (hp_ne : p ≠ 0) (hq_ne : q ≠ 0)
    (hp_param : p = a * (a ^ 2 - 9 * b ^ 2))
    (hprod : p * (p ^ 2 + 3 * q ^ 2) = c ^ 3)
    (he : a = e ^ 3) (hs : p = s ^ 3) (ht : p ^ 2 + 3 * q ^ 2 = t ^ 3) :
    |e| < |c| := by
  have h1 := abs_e_lt_abs_s h3 ha hb hp_param he hs
  have h2 := abs_s_lt_abs_c hp_ne hq_ne hprod hs ht
  exact lt_trans h1 h2

/-- **The complete Euler descent step.**
From a non-trivial solution to the cubic parameterization with `q ≠ 0` in the `3 ∤ p` branch,
the descent produces a new integer solution `(f, g, e)` to `f³ + g³ = 2e³` with
`e ≠ 0`, `f ≠ g`, and strictly smaller base magnitude `|e| < |c|`. -/
theorem descent_step_smaller_solution {a b p q c s t : ℤ}
    (hp_ne : p ≠ 0) (hq_ne : q ≠ 0) (h3 : ¬ (3 : ℤ) ∣ p)
    (hab : IsCoprime a b) (hpar : (Even a ∧ Odd b) ∨ (Odd a ∧ Even b))
    (hp_param : p = a * (a - 3 * b) * (a + 3 * b))
    (hq_param : q = 3 * b * (a ^ 2 - b ^ 2))
    (hprod : p * (p ^ 2 + 3 * q ^ 2) = c ^ 3)
    (hs : p = s ^ 3) (ht : p ^ 2 + 3 * q ^ 2 = t ^ 3) :
    ∃ e f g : ℤ, f ^ 3 + g ^ 3 = 2 * e ^ 3 ∧ e ≠ 0 ∧ f ≠ g ∧ |e| < |c| := by
  have ha_ne : a ≠ 0 := by
    rintro rfl
    rw [hp_param] at hp_ne
    apply hp_ne
    ring
  have hb_ne : b ≠ 0 := by
    rintro rfl
    rw [hq_param] at hq_ne
    apply hq_ne
    ring
  have h3a : ¬ (3 : ℤ) ∣ a := by
    intro h3_dvd_a
    have ha_dvd : a ∣ p := ⟨(a - 3 * b) * (a + 3 * b), by rw [hp_param]; ring⟩
    have : (3 : ℤ) ∣ p := dvd_trans h3_dvd_a ha_dvd
    exact h3 this
  have hp_eq : a * (a - 3 * b) * (a + 3 * b) = s ^ 3 := by rw [← hp_param, hs]
  obtain ⟨e, f, g, heuler, he, hf, hg⟩ := descent_step_to_euler hab h3a hpar hp_eq
  have he_ne : e ≠ 0 := by
    rintro rfl
    rw [he] at ha_ne
    exact ha_ne (by norm_num)
  have hfg : f ≠ g := by
    intro heq
    have heq3 : f ^ 3 = g ^ 3 := by rw [heq]
    rw [← hf, ← hg] at heq3
    have : b = 0 := by omega
    exact hb_ne this

  have hp_param2 : p = a * (a ^ 2 - 9 * b ^ 2) := by
    rw [hp_param]
    ring
  have he_lt_c := abs_e_lt_abs_c h3a ha_ne hb_ne hp_ne hq_ne hp_param2 hprod he hs ht
  exact ⟨e, f, g, heuler, he_ne, hfg, he_lt_c⟩

/-- Coprimality transfers from `(p, q)` to the parameter pair `(a, b)`. -/
theorem coprime_a_b_of_param {a b p q : ℤ}
    (hp : p = a * (a - 3 * b) * (a + 3 * b))
    (hq : q = 3 * b * (a ^ 2 - b ^ 2))
    (hcop : IsCoprime p q) :
    IsCoprime a b := by
  obtain ⟨u, v, huv⟩ := hcop
  refine ⟨u * ((a - 3 * b) * (a + 3 * b)), v * (3 * (a ^ 2 - b ^ 2)), ?_⟩
  calc u * ((a - 3 * b) * (a + 3 * b)) * a + v * (3 * (a ^ 2 - b ^ 2)) * b
      = u * (a * (a - 3 * b) * (a + 3 * b)) + v * (3 * b * (a ^ 2 - b ^ 2)) := by ring
    _ = u * p + v * q := by rw [← hp, ← hq]
    _ = 1 := huv

/-- Opposite parity of `(p, q)` forces opposite parity of `(a, b)`. -/
theorem opp_parity_a_b_of_param {a b p q : ℤ}
    (hp : p = a * (a - 3 * b) * (a + 3 * b))
    (hq : q = 3 * b * (a ^ 2 - b ^ 2))
    (hodd_diff : ¬ (2 : ℤ) ∣ (p - q)) :
    (Even a ∧ Odd b) ∨ (Odd a ∧ Even b) := by
  rcases Int.even_or_odd a with hae | hao <;> rcases Int.even_or_odd b with hbe | hbo
  · exfalso
    obtain ⟨k, rfl⟩ := hae
    obtain ⟨m, rfl⟩ := hbe
    have h2p : (2 : ℤ) ∣ p := by
      rw [hp]
      exact ⟨k * (2 * k - 3 * (2 * m)) * (2 * k + 3 * (2 * m)), by ring⟩
    have h2q : (2 : ℤ) ∣ q := by
      rw [hq]
      exact ⟨3 * m * ((2 * k) ^ 2 - (2 * m) ^ 2), by ring⟩
    apply hodd_diff
    exact dvd_sub h2p h2q
  · left; exact ⟨hae, hbo⟩
  · right; exact ⟨hao, hbe⟩
  · exfalso
    obtain ⟨k, rfl⟩ := hao
    obtain ⟨m, rfl⟩ := hbo
    have hsub : (2 : ℤ) ∣ (2 * k + 1 - 3 * (2 * m + 1)) := ⟨k - 3 * m - 1, by ring⟩
    have h2p : (2 : ℤ) ∣ p := by
      rw [hp]
      obtain ⟨d, hd⟩ := hsub
      exact ⟨(2 * k + 1) * d * (2 * k + 1 + 3 * (2 * m + 1)), by rw [hd]; ring⟩
    have hsq : (2 : ℤ) ∣ ((2 * k + 1) ^ 2 - (2 * m + 1) ^ 2) := ⟨2 * k ^ 2 + 2 * k - 2 * m ^ 2 - 2 * m, by ring⟩
    have h2q : (2 : ℤ) ∣ q := by
      rw [hq]
      obtain ⟨d, hd⟩ := hsq
      exact ⟨3 * (2 * m + 1) * d, by rw [hd]; ring⟩
    apply hodd_diff
    exact dvd_sub h2p h2q

/-- **Connecting `CubeFormParam` to strict descent.**
Given `CubeFormParam`, any non-trivial solution to `p(p² + 3q²) = c³` with `q ≠ 0`,
`3 ∤ p`, and opposite parities `¬ 2 ∣ (p - q)` yields a strictly smaller non-trivial
solution to Euler's equation `f³ + g³ = 2e³` with `|e| < |c|`. -/
theorem descent_step_of_param (Hparam : CubeFormParam)
    {p q c : ℤ} (hp_ne : p ≠ 0) (hq_ne : q ≠ 0) (h3 : ¬ (3 : ℤ) ∣ p)
    (hcop : IsCoprime p q) (hodd_diff : ¬ (2 : ℤ) ∣ (p - q))
    (hprod : p * (p ^ 2 + 3 * q ^ 2) = c ^ 3) :
    ∃ e f g : ℤ, f ^ 3 + g ^ 3 = 2 * e ^ 3 ∧ e ≠ 0 ∧ f ≠ g ∧ |e| < |c| := by
  have ⟨⟨s, hs⟩, ⟨t, ht⟩⟩ := factors_are_cubes hcop h3 hprod
  obtain ⟨a, b, hp_param, hq_param⟩ := Hparam p q t hcop hodd_diff ht
  have hab := coprime_a_b_of_param hp_param hq_param hcop
  have hpar := opp_parity_a_b_of_param hp_param hq_param hodd_diff
  exact descent_step_smaller_solution hp_ne hq_ne h3 hab hpar hp_param hq_param hprod hs ht

/-- **Strict well-founded descent on `ℕ` for the Euler cubic.**
The new solution `(f, g, e)` strictly decreases the natural magnitude `e.natAbs < c.natAbs`,
establishing the well-founded order on `ℕ` that rules out non-trivial solutions. -/
theorem descent_step_smaller_natAbs (Hparam : CubeFormParam)
    {p q c : ℤ} (hp_ne : p ≠ 0) (hq_ne : q ≠ 0) (h3 : ¬ (3 : ℤ) ∣ p)
    (hcop : IsCoprime p q) (hodd_diff : ¬ (2 : ℤ) ∣ (p - q))
    (hprod : p * (p ^ 2 + 3 * q ^ 2) = c ^ 3) :
    ∃ e f g : ℤ, f ^ 3 + g ^ 3 = 2 * e ^ 3 ∧ e ≠ 0 ∧ f ≠ g ∧ e.natAbs < c.natAbs := by
  obtain ⟨e, f, g, heuler, he_ne, hfg, he_lt_c⟩ :=
    descent_step_of_param Hparam hp_ne hq_ne h3 hcop hodd_diff hprod
  exact ⟨e, f, g, heuler, he_ne, hfg, natAbs_lt_of_abs_lt he_lt_c⟩

/-- **Unified Euler descent branch dispatch (Candidate C230).**
For any integer solution to `p(p² + 3q²) = c³` with `p ≠ 0`, `q ≠ 0`, and `IsCoprime p q`,
either:
1. `3 ∤ p` and `¬ 2 ∣ (p - q)`, so `CubeFormParam` yields a strictly smaller Euler solution with `e.natAbs < c.natAbs`; or
2. `3 ∣ p`, in which case `c = 3c'` divides strictly by 3 (`c'.natAbs < c.natAbs`), swapping coordinates to `p''(q² + 3(3p'')²) = c'³` with `3 ∤ q`. -/
theorem euler_descent_dispatch (Hparam : CubeFormParam)
    {p q c : ℤ} (hp_ne : p ≠ 0) (hq_ne : q ≠ 0) (hcop : IsCoprime p q)
    (hprod : p * (p ^ 2 + 3 * q ^ 2) = c ^ 3) :
    (3 : ℤ) ∣ p ∨ (∃ e f g : ℤ, f ^ 3 + g ^ 3 = 2 * e ^ 3 ∧ e ≠ 0 ∧ f ≠ g ∧ e.natAbs < c.natAbs) ∨ (2 : ℤ) ∣ (p - q) := by
  by_cases h3 : (3 : ℤ) ∣ p
  · left; exact h3
  · right
    by_cases hpar : (2 : ℤ) ∣ (p - q)
    · right; exact hpar
    · left; exact descent_step_smaller_natAbs Hparam hp_ne hq_ne h3 hcop hpar hprod

/-- Dispatcher under odd coordinate difference: eliminates the parity branch. -/
theorem euler_descent_dispatch_odd (Hparam : CubeFormParam)
    {p q c : ℤ} (hp_ne : p ≠ 0) (hq_ne : q ≠ 0) (hcop : IsCoprime p q)
    (hodd_diff : ¬ (2 : ℤ) ∣ (p - q))
    (hprod : p * (p ^ 2 + 3 * q ^ 2) = c ^ 3) :
    (3 : ℤ) ∣ p ∨ (∃ e f g : ℤ, f ^ 3 + g ^ 3 = 2 * e ^ 3 ∧ e ≠ 0 ∧ f ≠ g ∧ e.natAbs < c.natAbs) := by
  have h := euler_descent_dispatch Hparam hp_ne hq_ne hcop hprod
  rcases h with h3 | hdesc | heven
  · left; exact h3
  · right; exact hdesc
  · contradiction

/-- A non-trivial Euler solution with magnitude `n = c.natAbs`:
there exist `a, b, c : ℤ` such that `a³ + b³ = 2c³`, `c ≠ 0`, `a ≠ b`, and `c.natAbs = n`. -/
def HasEulerNonTrivialSolAt (n : ℕ) : Prop :=
  ∃ a b c : ℤ, a ^ 3 + b ^ 3 = 2 * c ^ 3 ∧ c ≠ 0 ∧ a ≠ b ∧ c.natAbs = n

/-- **Universal descent termination schema on ℕ (Candidate C242).**
If every non-trivial Euler solution at magnitude `n` yields another non-trivial
Euler solution at magnitude `m < n`, then no non-trivial Euler solutions exist. -/
theorem euler_descent_termination
    (hstep : ∀ n, HasEulerNonTrivialSolAt n → ∃ m, HasEulerNonTrivialSolAt m ∧ m < n) :
    ∀ n, ¬ HasEulerNonTrivialSolAt n := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn
    obtain ⟨m, hm, hmlt⟩ := hstep n hn
    exact ih m hmlt hm

/-- As an immediate corollary, any non-trivial Euler solution gives `a = b`. -/
theorem euler_eq_of_no_non_trivial_sol
    (hterm : ∀ n, ¬ HasEulerNonTrivialSolAt n)
    {a b c : ℤ} (heq : a ^ 3 + b ^ 3 = 2 * c ^ 3) (hc : c ≠ 0) :
    a = b := by
  by_contra hne
  exact hterm c.natAbs ⟨a, b, c, heq, hc, hne, rfl⟩

/-! ### Towards `OddDivisorForm`: the descent step, formalised (U359, pool C211)

`OddDivisorForm` is proved classically by Fermat descent on the symmetric residues mod `m`.  The
step itself is formalised below: the residues stay congruent, they are bounded by `m/2` in absolute
value, and `m` still divides `P² + 3Q²`.  What is NOT yet formalised is the strong induction that
turns one step into the theorem, together with the division of `P² + 3Q² = m·m'` by `m'` using
`form_mul`.  Numerical validation of the step: 18,488 triples, zero violations, maximum ratio
`m'/m = 0.9336` (pool C203). -/

/-- A symmetric residue: `symRes a m` is congruent to `a` mod `m` and has `2·|symRes| ≤ m`. -/
def symRes (a m : ℤ) : ℤ := if 2 * (a % m) ≤ m then a % m else a % m - m

theorem symRes_congr (a m : ℤ) (_hm : 0 < m) : m ∣ a - symRes a m := by
  unfold symRes
  split
  · exact Int.dvd_sub_of_emod_eq rfl
  · have : a - (a % m - m) = (a - a % m) + m := by ring
    rw [this]
    exact dvd_add (Int.dvd_sub_of_emod_eq rfl) dvd_rfl

theorem symRes_abs_le (a m : ℤ) (hm : 0 < m) : 2 * |symRes a m| ≤ m + m := by
  unfold symRes
  have h0 : 0 ≤ a % m := Int.emod_nonneg a (by omega)
  have h1 : a % m < m := Int.emod_lt_of_pos a hm
  split
  · rw [abs_of_nonneg h0]; omega
  · rename_i h
    rw [abs_of_nonpos (by omega)]; omega

/-- **The descent step for `OddDivisorForm`.**  If `m` divides `p² + 3q²`, it also divides
`P² + 3Q²` for the symmetric residues, because `P ≡ p` and `Q ≡ q` modulo `m`. -/
theorem descent_dvd {m p q : ℤ} (hm : 0 < m) (h : m ∣ p ^ 2 + 3 * q ^ 2) :
    m ∣ (symRes p m) ^ 2 + 3 * (symRes q m) ^ 2 := by
  obtain ⟨s, hs⟩ := symRes_congr p m hm
  obtain ⟨t, ht⟩ := symRes_congr q m hm
  have hp : symRes p m = p - m * s := by linarith
  have hq : symRes q m = q - m * t := by linarith
  rw [hp, hq]
  obtain ⟨c, hc⟩ := h
  exact ⟨c - 2 * p * s - 6 * q * t + m * s ^ 2 + 3 * m * t ^ 2, by linear_combination hc⟩

/-- For ODD `m` the symmetric residue satisfies the STRICT bound `2|symRes| ≤ m - 1`, because
`2|symRes| = m` would need `m` even. -/
theorem symRes_abs_le_odd {a m : ℤ} (hm : 0 < m) (hodd : ¬ (2 : ℤ) ∣ m) :
    2 * |symRes a m| ≤ m - 1 := by
  have h := symRes_abs_le a m hm
  have h2 : 2 * |symRes a m| ≠ m := by
    intro heq
    exact hodd ⟨|symRes a m|, by omega⟩
  unfold symRes at *
  have h0 : 0 ≤ a % m := Int.emod_nonneg a (by omega)
  have h1 : a % m < m := Int.emod_lt_of_pos a hm
  split at h2 <;> split <;> rename_i hs
  · rw [abs_of_nonneg h0] at *; omega
  · omega
  · omega
  · rw [abs_of_nonpos (by omega)] at *; omega

/-- **The descent is strict.**  For odd `m > 1` the symmetric residues satisfy
`P² + 3Q² ≤ (m-1)² < m²`, so writing `P² + 3Q² = m·m'` gives `0 ≤ m' < m`.
No integer division is used: from `2|P| ≤ m-1` we square to `4P² ≤ (m-1)²`. -/
theorem descent_strict {m p q : ℤ} (hm : 1 < m) (hodd : ¬ (2 : ℤ) ∣ m) :
    (symRes p m) ^ 2 + 3 * (symRes q m) ^ 2 ≤ (m - 1) ^ 2 := by
  have hP := symRes_abs_le_odd (a := p) (by omega) hodd
  have hQ := symRes_abs_le_odd (a := q) (by omega) hodd
  have hPa : 0 ≤ |symRes p m| := abs_nonneg _
  have hQa : 0 ≤ |symRes q m| := abs_nonneg _
  have hP4 : 4 * (symRes p m) ^ 2 ≤ (m - 1) ^ 2 := by
    have : (2 * |symRes p m|) ^ 2 ≤ (m - 1) ^ 2 := by nlinarith
    calc 4 * (symRes p m) ^ 2 = (2 * |symRes p m|) ^ 2 := by rw [mul_pow, sq_abs]; ring
      _ ≤ (m - 1) ^ 2 := this
  have hQ4 : 4 * (symRes q m) ^ 2 ≤ (m - 1) ^ 2 := by
    have : (2 * |symRes q m|) ^ 2 ≤ (m - 1) ^ 2 := by nlinarith
    calc 4 * (symRes q m) ^ 2 = (2 * |symRes q m|) ^ 2 := by rw [mul_pow, sq_abs]; ring
      _ ≤ (m - 1) ^ 2 := this
  linarith

/-- The symmetric residue vanishes exactly when `m` divides the argument. -/
theorem symRes_eq_zero_iff {a m : ℤ} (hm : 0 < m) : symRes a m = 0 ↔ m ∣ a := by
  constructor
  · intro h
    obtain ⟨s, hs⟩ := symRes_congr a m hm
    exact ⟨s, by rw [← hs, h]; ring⟩
  · intro h
    unfold symRes
    rw [Int.emod_eq_zero_of_dvd h]
    simp [le_of_lt hm]

/-- **Non-degeneracy of the descent.**  For coprime `p, q` and `m > 1`, the two symmetric residues
cannot both vanish: that would make `m` a common divisor of `p` and `q`. -/
theorem descent_nondegenerate {m p q : ℤ} (hm : 1 < m) (hcop : IsCoprime p q) :
    ¬ (symRes p m = 0 ∧ symRes q m = 0) := by
  rintro ⟨hp, hq⟩
  have hdp : m ∣ p := (symRes_eq_zero_iff (by omega)).mp hp
  have hdq : m ∣ q := (symRes_eq_zero_iff (by omega)).mp hq
  have : IsUnit m := hcop.isUnit_of_dvd' hdp hdq
  rcases Int.isUnit_iff.mp this with h | h <;> omega

/-- Consequently the quotient `m'` is strictly positive: `P² + 3Q² > 0`. -/
theorem descent_quotient_pos {m p q : ℤ} (hm : 1 < m) (hcop : IsCoprime p q) :
    0 < (symRes p m) ^ 2 + 3 * (symRes q m) ^ 2 := by
  have h := descent_nondegenerate hm hcop
  rcases eq_or_ne (symRes p m) 0 with hp | hp
  · have hq : symRes q m ≠ 0 := fun hq => h ⟨hp, hq⟩
    have : 0 < (symRes q m) ^ 2 := by positivity
    rw [hp]; nlinarith
  · have : 0 < (symRes p m) ^ 2 := by positivity
    nlinarith [sq_nonneg (symRes q m)]

/-- **The quotient is strictly smaller than the modulus.**
Writing `P² + 3Q² = m · m'` for the symmetric residues of odd `m > 1`,
we have `m' < m`. -/
theorem descent_quotient_lt {m p q m' : ℤ} (hm : 1 < m) (hodd : ¬ (2 : ℤ) ∣ m)
    (hprod : (symRes p m) ^ 2 + 3 * (symRes q m) ^ 2 = m * m') :
    m' < m := by
  have hbound := descent_strict hm hodd (p := p) (q := q)
  rw [hprod] at hbound
  by_contra! hc
  have hm_pos : 0 < m := by omega
  have : m ^ 2 ≤ m * m' := by nlinarith
  have : (m - 1) ^ 2 < m ^ 2 := by nlinarith
  linarith

/-- The quotient `m'` is strictly positive for coprime `p, q`. -/
theorem descent_quotient_pos' {m p q m' : ℤ} (hm : 1 < m) (hcop : IsCoprime p q)
    (hprod : (symRes p m) ^ 2 + 3 * (symRes q m) ^ 2 = m * m') :
    0 < m' := by
  have hpos := descent_quotient_pos hm hcop
  rw [hprod] at hpos
  by_contra! hc
  have hm_pos : 0 < m := by omega
  have : m * m' ≤ 0 := by nlinarith
  linarith


/-- Base case of the descent: `1` is represented by the form. -/
theorem one_is_form : (1 : ℤ) = 1 ^ 2 + 3 * 0 ^ 2 := by ring

/-- `P² + 3Q²` and `P + Q` differ by an even number. -/
theorem form_sub_sum_even (P Q : ℤ) : ∃ k : ℤ, P ^ 2 + 3 * Q ^ 2 - (P + Q) = 2 * k := by
  rcases Int.even_or_odd P with ⟨a, ha⟩ | ⟨a, ha⟩ <;>
    rcases Int.even_or_odd Q with ⟨b, hb⟩ | ⟨b, hb⟩ <;> subst ha <;> subst hb
  · exact ⟨2 * a ^ 2 - a + 6 * b ^ 2 - b, by ring⟩
  · exact ⟨2 * a ^ 2 - a + 6 * b ^ 2 + 5 * b + 1, by ring⟩
  · exact ⟨2 * a ^ 2 + a + 6 * b ^ 2 - b, by ring⟩
  · exact ⟨2 * a ^ 2 + a + 6 * b ^ 2 + 5 * b + 1, by ring⟩

/-- **The parity sub-lemma the induction needs.**  `P² + 3Q²` is even exactly when `P + Q` is, so
the descent's quotient stays odd precisely when the symmetric residues have opposite parity. -/
theorem form_even_iff (P Q : ℤ) : (2 : ℤ) ∣ (P ^ 2 + 3 * Q ^ 2) ↔ (2 : ℤ) ∣ (P + Q) := by
  obtain ⟨k, hk⟩ := form_sub_sum_even P Q
  constructor <;> rintro ⟨c, hc⟩
  · exact ⟨c - k, by omega⟩
  · exact ⟨c + k, by omega⟩

/-! ### The 2-adic step, and a reduction that does NOT work (U363, pool C212)

When the symmetric residues `P, Q` share a parity the quotient `m'` is even, and the induction
needs to reduce the `2`-part before the odd-divisor hypothesis applies again.  The natural move is
one of the two halving identities below.

**Variant A is not a descent.**  It fixes the entire line `P = 3Q` — `(3,1) ↦ (3,1)` — so it makes
no progress there.  Variant B is fixed only at the origin, but `max(|P|,|Q|)` fails to decrease in
900 of 1300 same-parity pairs, so it is not a descent on the size of the pair either.

**Correction (U364).**  I then claimed the right measure was `v₂(P² + 3Q²)` and that each halving
drops it by `2`.  That is **wrong**, and an exact check refuted it in every one of 7,320 cases: the
identities `(P±3Q)² + 3(P∓Q)² = 4(P² + 3Q²)` mean the halved pair has **exactly the same value**,
so `v₂` is unchanged.  What the identities actually do is change the representation's *parity
class*, and the real step is: for `P, Q` both odd, **exactly one** of the two variants lands on a
pair with both coordinates even — verified on all 6,724 both-odd pairs with `|P|,|Q| ≤ 81`, zero
exceptions — after which dividing that pair by `2` drops the value by `4`.  The lemmas below are
the parity bookkeeping that makes the choice deterministic. -/

/-- **The halving identities.**  Both sign variants preserve the form up to a factor `4`, which is
how the `2`-part of a representation is reduced when `P` and `Q` share a parity. -/
theorem halve_identity_A (P Q : ℤ) :
    (P + 3 * Q) ^ 2 + 3 * (P - Q) ^ 2 = 4 * (P ^ 2 + 3 * Q ^ 2) := by ring

theorem halve_identity_B (P Q : ℤ) :
    (P - 3 * Q) ^ 2 + 3 * (P + Q) ^ 2 = 4 * (P ^ 2 + 3 * Q ^ 2) := by ring

/-- **Variant A cannot serve as a descent.**  It is the identity on the whole line `P = 3Q`, so
the pair `(3, 1)` is a fixed point and the transformation makes no progress there. -/
theorem halve_A_fixed_point : ((3 : ℤ) + 3 * 1) / 2 = 3 ∧ ((3 : ℤ) - 1) / 2 = 1 := by
  constructor <;> norm_num

theorem halve_A_fixed_line (Q : ℤ) : ((3 * Q) + 3 * Q) = 2 * (3 * Q) ∧ ((3 * Q) - Q) = 2 * Q := by
  constructor <;> ring

/-- **The 2-adic step, correctly stated.**  For `P, Q` both odd, exactly one of the two halving
variants lands on a pair with both coordinates even.  Writing `P = 2a+1`, `Q = 2b+1`, variant `A`
gives `(a + 3b + 2, a - b)` and variant `B` gives `(a - 3b - 1, a + b + 1)`; their second
coordinates `a - b` and `a + b + 1` have opposite parity, and so do the first. -/
theorem halve_parity_split (a b : ℤ) :
    (((2 * a + 1) + 3 * (2 * b + 1)) / 2 = a + 3 * b + 2) ∧
    (((2 * a + 1) - (2 * b + 1)) / 2 = a - b) ∧
    (((2 * a + 1) - 3 * (2 * b + 1)) / 2 = a - 3 * b - 1) ∧
    (((2 * a + 1) + (2 * b + 1)) / 2 = a + b + 1) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> omega

/-- The two candidate second coordinates have opposite parity, so exactly one variant is even
there.  This is what makes the `2`-adic step deterministic. -/
theorem halve_second_coords_opposite (a b : ℤ) :
    ((2 : ℤ) ∣ (a - b)) ↔ ¬ ((2 : ℤ) ∣ (a + b + 1)) := by
  constructor <;> intro h <;> [skip; skip] <;> omega

/-- And the first coordinates likewise, so the chosen variant is even in BOTH slots. -/
theorem halve_first_coords_opposite (a b : ℤ) :
    ((2 : ℤ) ∣ (a + 3 * b + 2)) ↔ ¬ ((2 : ℤ) ∣ (a - 3 * b - 1)) := by
  constructor <;> intro h <;> omega

/-! ### The valuation dichotomy: the even branch is ONE step, not a descent (U365, pool C213)

For coprime `P, Q` the `2`-adic valuation of `P² + 3Q²` is always `0` or exactly `2`:

* coprime `P, Q` cannot both be even;
* opposite parity makes `P² + 3Q²` odd, valuation `0`;
* both odd gives `P² + 3Q² ≡ 4 (mod 8)`, valuation exactly `2`.

Verified over all 35,088 coprime pairs with `|P|,|Q| ≤ 120`: the valuation takes **only** the
values `0` and `2`.  So the even branch of the induction needs exactly ONE parity-split halving,
which divides the value by `4` and lands on an odd quotient — there is no unbounded `2`-adic
descent to bound, which is what the two wrong measures of U363 and U364 were trying to supply. -/

/-- An odd square is `1` modulo `8`. -/
theorem odd_sq_mod_eight (a : ℤ) : (2 * a + 1) ^ 2 % 8 = 1 ∨ (2 * a + 1) ^ 2 % 8 = 1 := by
  left
  have h : (2 * a + 1) ^ 2 = 8 * ((a * (a + 1)) / 2) + 1 ∨
           (2 * a + 1) ^ 2 = 4 * (a * (a + 1)) + 1 := Or.inr (by ring)
  rcases h with h | h
  · omega
  · rcases Int.even_mul_succ_self a with ⟨k, hk⟩
    rw [h, hk]; omega

/-- **The valuation dichotomy.**  For `P, Q` both odd, `P² + 3Q² ≡ 4 (mod 8)`, so its `2`-adic
valuation is exactly `2`.  Together with the opposite-parity case (`P² + 3Q²` odd, valuation `0`)
and the fact that coprime `P, Q` cannot both be even, this says the valuation is always `0` or `2`
— so the even branch of the induction needs exactly ONE halving, never an unbounded descent. -/
theorem both_odd_mod_eight (a b : ℤ) :
    ((2 * a + 1) ^ 2 + 3 * (2 * b + 1) ^ 2) % 8 = 4 := by
  have ha := Int.even_mul_succ_self a
  have hb := Int.even_mul_succ_self b
  obtain ⟨k, hk⟩ := ha
  obtain ⟨l, hl⟩ := hb
  have e : (2 * a + 1) ^ 2 + 3 * (2 * b + 1) ^ 2
      = 4 * (a * (a + 1)) + 12 * (b * (b + 1)) + 4 := by ring
  rw [e, hk, hl]; omega

/-- Opposite parity gives an odd value, hence valuation `0`. -/
theorem opposite_parity_odd (a b : ℤ) :
    ¬ (2 : ℤ) ∣ ((2 * a) ^ 2 + 3 * (2 * b + 1) ^ 2) := by
  intro h
  obtain ⟨c, hc⟩ := h
  have e : (2 * a) ^ 2 + 3 * (2 * b + 1) ^ 2 = 2 * (2 * a ^ 2 + 6 * b ^ 2 + 6 * b + 1) + 1 := by ring
  omega

/-- Every integer square is `0`, `1`, or `4` modulo `8`. -/
theorem sq_mod_eight (X : ℤ) : X ^ 2 % 8 = 0 ∨ X ^ 2 % 8 = 1 ∨ X ^ 2 % 8 = 4 := by
  rcases Int.even_or_odd X with ⟨a, ha⟩ | ⟨a, ha⟩ <;> subst ha
  · rcases Int.even_or_odd a with ⟨k, hk⟩ | ⟨k, hk⟩ <;> subst hk
    · left
      have : (k + k + (k + k)) ^ 2 = 8 * (2 * k ^ 2) := by ring
      rw [this]; omega
    · right; right
      have : (2 * k + 1 + (2 * k + 1)) ^ 2 = 8 * (2 * k ^ 2 + 2 * k) + 4 := by ring
      rw [this]; omega
  · right; left
    rcases odd_sq_mod_eight a with h | h <;> exact h

/-- Modulo 8 obstruction: `X² + 3Y²` is never `2` modulo `8`. -/
theorem form_mod_eight_ne_two (X Y : ℤ) : (X ^ 2 + 3 * Y ^ 2) % 8 ≠ 2 := by
  intro hc
  rcases sq_mod_eight X with hX | hX | hX <;>
    rcases sq_mod_eight Y with hY | hY | hY
  all_goals
    have he : (X ^ 2 + 3 * Y ^ 2) % 8 = (X ^ 2 % 8 + 3 * (Y ^ 2 % 8)) % 8 := by
      have : X ^ 2 + 3 * Y ^ 2 = 8 * (X ^ 2 / 8 + 3 * (Y ^ 2 / 8)) + (X ^ 2 % 8 + 3 * (Y ^ 2 % 8)) := by omega
      rw [this]; omega
    rw [he, hX, hY] at hc
    revert hc; decide

/-- Modulo 8 obstruction: `X² + 3Y²` is never `6` modulo `8`. -/
theorem form_mod_eight_ne_six (X Y : ℤ) : (X ^ 2 + 3 * Y ^ 2) % 8 ≠ 6 := by
  intro hc
  rcases sq_mod_eight X with hX | hX | hX <;>
    rcases sq_mod_eight Y with hY | hY | hY
  all_goals
    have he : (X ^ 2 + 3 * Y ^ 2) % 8 = (X ^ 2 % 8 + 3 * (Y ^ 2 % 8)) % 8 := by
      have : X ^ 2 + 3 * Y ^ 2 = 8 * (X ^ 2 / 8 + 3 * (Y ^ 2 / 8)) + (X ^ 2 % 8 + 3 * (Y ^ 2 % 8)) := by omega
      rw [this]; omega
    rw [he, hX, hY] at hc
    revert hc; decide

/-- Consequently, `2 · odd` is NEVER of the form `X² + 3Y²`. -/
theorem form_ne_two_mul_odd (X Y k : ℤ) : X ^ 2 + 3 * Y ^ 2 ≠ 2 * (2 * k + 1) := by
  intro hc
  have hmod : (2 * (2 * k + 1)) % 8 = 2 ∨ (2 * (2 * k + 1)) % 8 = 6 := by
    rcases Int.even_or_odd k with ⟨j, hj⟩ | ⟨j, hj⟩ <;> subst hj
    · left
      have : 2 * (2 * (j + j) + 1) = 8 * j + 2 := by ring
      rw [this]; omega
    · right
      have : 2 * (2 * (2 * j + 1) + 1) = 8 * j + 6 := by ring
      rw [this]; omega
  rcases hmod with h2 | h6
  · have hne := form_mod_eight_ne_two X Y
    rw [hc, h2] at hne
    exact hne rfl
  · have hne := form_mod_eight_ne_six X Y
    rw [hc, h6] at hne
    exact hne rfl

/-! ### Division of the quadratic form: prime modulus quotient (U366, pool C214)

In Fermat descent `P² + 3Q² = m · m'`, dividing out the quotient `m'` using the identity
`(Qu - Pv)(Qu + Pv) = Q²(u² + 3v²) - (P² + 3Q²)v² = m'(Q² - mv²)` requires `m'` to divide one of
the factors `Qu ∓ Pv`.  For composite `m'` (first failing at `m' = 91 = 7 · 13`), prime factors
distribute across both terms and direct division fails.  For PRIME `m'`, Euclid's lemma forces
`m' ∣ (Qu - Pv)` or `m' ∣ (Qu + Pv)`, and the quotient `m` is proved unconditionally to be of the
form `X² + 3Y²`. -/

/-- The cross-product factorisation: `(Qu - Pv)(Qu + Pv)` is divisible by the modulus `m'`. -/
theorem form_cross_prod_eq (P Q u v : ℤ) :
    (Q * u - P * v) * (Q * u + P * v) = Q ^ 2 * (u ^ 2 + 3 * v ^ 2) - (P ^ 2 + 3 * Q ^ 2) * v ^ 2 := by
  ring

/-- Linear elimination identity 1 for minus-variant. -/
theorem form_elim1_minus (P Q u v : ℤ) :
    u * (P * u + 3 * Q * v) - 3 * v * (Q * u - P * v) = P * (u ^ 2 + 3 * v ^ 2) := by
  ring

/-- Linear elimination identity 2 for minus-variant. -/
theorem form_elim2_minus (P Q u v : ℤ) :
    v * (P * u + 3 * Q * v) + u * (Q * u - P * v) = Q * (u ^ 2 + 3 * v ^ 2) := by
  ring

/-- Linear elimination identity 1 for plus-variant. -/
theorem form_elim1_plus (P Q u v : ℤ) :
    u * (P * u - 3 * Q * v) + 3 * v * (Q * u + P * v) = P * (u ^ 2 + 3 * v ^ 2) := by
  ring

/-- Linear elimination identity 2 for plus-variant. -/
theorem form_elim2_plus (P Q u v : ℤ) :
    -v * (P * u - 3 * Q * v) + u * (Q * u + P * v) = Q * (u ^ 2 + 3 * v ^ 2) := by
  ring

/-- If `m' = u² + 3v²` with `u, v` coprime and `m'` divides `Qu - Pv`, then `m'` ALSO divides `Pu + 3Qv`. -/
theorem form_div_minus_dvd {P Q u v m' : ℤ} (hcop : IsCoprime u v)
    (hm' : m' = u ^ 2 + 3 * v ^ 2) (hdiv : m' ∣ (Q * u - P * v)) :
    m' ∣ (P * u + 3 * Q * v) := by
  obtain ⟨r, s, hrs⟩ := hcop
  obtain ⟨k, hk⟩ := hdiv
  have h1 : u * (P * u + 3 * Q * v) = P * m' + 3 * v * (m' * k) := by
    linear_combination -P * hm' + 3 * v * hk
  have h2 : v * (P * u + 3 * Q * v) = Q * m' - u * (m' * k) := by
    linear_combination -Q * hm' - u * hk
  have hW : P * u + 3 * Q * v = r * (u * (P * u + 3 * Q * v)) + s * (v * (P * u + 3 * Q * v)) := by
    calc P * u + 3 * Q * v = (r * u + s * v) * (P * u + 3 * Q * v) := by rw [hrs, one_mul]
      _ = r * (u * (P * u + 3 * Q * v)) + s * (v * (P * u + 3 * Q * v)) := by ring
  rw [hW, h1, h2]
  exact ⟨r * (P + 3 * v * k) + s * (Q - u * k), by ring⟩

/-- Symmetrically, for the plus-variant: if `m'` divides `Qu + Pv`, then `m'` divides `Pu - 3Qv`. -/
theorem form_div_plus_dvd {P Q u v m' : ℤ} (hcop : IsCoprime u v)
    (hm' : m' = u ^ 2 + 3 * v ^ 2) (hdiv : m' ∣ (Q * u + P * v)) :
    m' ∣ (P * u - 3 * Q * v) := by
  obtain ⟨r, s, hrs⟩ := hcop
  obtain ⟨k, hk⟩ := hdiv
  have h1 : u * (P * u - 3 * Q * v) = P * m' - 3 * v * (m' * k) := by
    linear_combination -P * hm' - 3 * v * hk
  have h2 : -v * (P * u - 3 * Q * v) = Q * m' - u * (m' * k) := by
    linear_combination -Q * hm' - u * hk
  have hW : P * u - 3 * Q * v = r * (u * (P * u - 3 * Q * v)) - s * (-v * (P * u - 3 * Q * v)) := by
    calc P * u - 3 * Q * v = (r * u + s * v) * (P * u - 3 * Q * v) := by rw [hrs, one_mul]
      _ = r * (u * (P * u - 3 * Q * v)) - s * (-v * (P * u - 3 * Q * v)) := by ring
  rw [hW, h1, h2]
  exact ⟨r * (P - 3 * v * k) - s * (Q - u * k), by ring⟩

/-- The exact division step: if `P² + 3Q² = m · m'`, `m' = u² + 3v² ≠ 0`, and `m'` divides `Qu - Pv`,
then `m` is represented as `X² + 3Y²`. -/
theorem form_quotient_of_div_minus {P Q u v m m' : ℤ} (hm'ne : m' ≠ 0)
    (hcop : IsCoprime u v) (hm' : m' = u ^ 2 + 3 * v ^ 2)
    (hprod : P ^ 2 + 3 * Q ^ 2 = m * m')
    (hdiv : m' ∣ (Q * u - P * v)) :
    ∃ X Y : ℤ, m = X ^ 2 + 3 * Y ^ 2 := by
  have hdP : m' ∣ (P * u + 3 * Q * v) := form_div_minus_dvd hcop hm' hdiv
  obtain ⟨X, hX⟩ := hdP
  obtain ⟨Y, hY⟩ := hdiv
  have hnorm : (P * u + 3 * Q * v) ^ 2 + 3 * (Q * u - P * v) ^ 2
      = (P ^ 2 + 3 * Q ^ 2) * (u ^ 2 + 3 * v ^ 2) := by ring
  rw [hX, hY, hprod, ← hm'] at hnorm
  have heq : m' ^ 2 * (X ^ 2 + 3 * Y ^ 2) = m' ^ 2 * m := by
    calc m' ^ 2 * (X ^ 2 + 3 * Y ^ 2) = (m' * X) ^ 2 + 3 * (m' * Y) ^ 2 := by ring
      _ = m * m' * m' := hnorm
      _ = m' ^ 2 * m := by ring
  have hm2ne : m' ^ 2 ≠ 0 := pow_ne_zero 2 hm'ne
  have hcancel : X ^ 2 + 3 * Y ^ 2 = m := mul_left_cancel₀ hm2ne heq
  exact ⟨X, Y, hcancel.symm⟩

/-- Symmetrically for the plus-variant. -/
theorem form_quotient_of_div_plus {P Q u v m m' : ℤ} (hm'ne : m' ≠ 0)
    (hcop : IsCoprime u v) (hm' : m' = u ^ 2 + 3 * v ^ 2)
    (hprod : P ^ 2 + 3 * Q ^ 2 = m * m')
    (hdiv : m' ∣ (Q * u + P * v)) :
    ∃ X Y : ℤ, m = X ^ 2 + 3 * Y ^ 2 := by
  have hdP : m' ∣ (P * u - 3 * Q * v) := form_div_plus_dvd hcop hm' hdiv
  obtain ⟨X, hX⟩ := hdP
  obtain ⟨Y, hY⟩ := hdiv
  have hnorm : (P * u - 3 * Q * v) ^ 2 + 3 * (Q * u + P * v) ^ 2
      = (P ^ 2 + 3 * Q ^ 2) * (u ^ 2 + 3 * v ^ 2) := by ring
  rw [hX, hY, hprod, ← hm'] at hnorm
  have heq : m' ^ 2 * (X ^ 2 + 3 * Y ^ 2) = m' ^ 2 * m := by
    calc m' ^ 2 * (X ^ 2 + 3 * Y ^ 2) = (m' * X) ^ 2 + 3 * (m' * Y) ^ 2 := by ring
      _ = m * m' * m' := hnorm
      _ = m' ^ 2 * m := by ring
  have hm2ne : m' ^ 2 ≠ 0 := pow_ne_zero 2 hm'ne
  have hcancel : X ^ 2 + 3 * Y ^ 2 = m := mul_left_cancel₀ hm2ne heq
  exact ⟨X, Y, hcancel.symm⟩

/-- **The division step for PRIME modulus `m'`.**  If `m'` is prime and represents as `u² + 3v²`,
dividing `P² + 3Q² = m · m'` by `m'` leaves `m` representing as `X² + 3Y²`. -/
theorem form_quotient_of_prime {P Q u v m m' : ℤ} (hprime : Prime m')
    (hcop : IsCoprime u v) (hm' : m' = u ^ 2 + 3 * v ^ 2)
    (hprod : P ^ 2 + 3 * Q ^ 2 = m * m') :
    ∃ X Y : ℤ, m = X ^ 2 + 3 * Y ^ 2 := by
  have hm'ne : m' ≠ 0 := hprime.ne_zero
  have hcross : (Q * u - P * v) * (Q * u + P * v) = m' * (Q ^ 2 - m * v ^ 2) := by
    calc (Q * u - P * v) * (Q * u + P * v)
        = Q ^ 2 * (u ^ 2 + 3 * v ^ 2) - (P ^ 2 + 3 * Q ^ 2) * v ^ 2 := form_cross_prod_eq P Q u v
      _ = Q ^ 2 * m' - m * m' * v ^ 2 := by rw [← hm', hprod]
      _ = m' * (Q ^ 2 - m * v ^ 2) := by ring
  have hdvd : m' ∣ (Q * u - P * v) * (Q * u + P * v) := ⟨Q ^ 2 - m * v ^ 2, hcross⟩
  rcases hprime.dvd_mul.mp hdvd with hminus | hplus
  · exact form_quotient_of_div_minus hm'ne hcop hm' hprod hminus
  · exact form_quotient_of_div_plus hm'ne hcop hm' hprod hplus

/-! ### Multiplicative closure of quadratic form representations (U368, pool C215)

The predicate `RepresentsForm n` asserts that `n` is of the form `u² + 3v²`.  It is closed under
multiplication (via `form_mul`), squaring, and division by prime divisors of the form (via
`form_quotient_of_prime`).  Consequently, a composite divisor `m` represents as `u² + 3v²` as soon
as each of its prime factors does, enabling prime-by-prime descent and avoiding direct composite
division. -/

/-- A number `n` is represented by the quadratic form `x² + 3y²`. -/
def RepresentsForm (n : ℤ) : Prop := ∃ u v : ℤ, n = u ^ 2 + 3 * v ^ 2

/-- `1` is represented by the form. -/
theorem represents_one : RepresentsForm 1 := ⟨1, 0, by ring⟩

/-- `3` is represented by the form. -/
theorem represents_three : RepresentsForm 3 := ⟨0, 1, by ring⟩

/-- `RepresentsForm` is closed under multiplication (Brahmagupta-Fibonacci identity). -/
theorem represents_mul {m₁ m₂ : ℤ} (h₁ : RepresentsForm m₁) (h₂ : RepresentsForm m₂) :
    RepresentsForm (m₁ * m₂) := by
  obtain ⟨u₁, v₁, rfl⟩ := h₁
  obtain ⟨u₂, v₂, rfl⟩ := h₂
  exact ⟨u₁ * u₂ - 3 * v₁ * v₂, u₁ * v₂ + v₁ * u₂, form_mul u₁ v₁ u₂ v₂⟩

/-- `RepresentsForm` is closed under squaring. -/
theorem represents_sq {m : ℤ} (h : RepresentsForm m) : RepresentsForm (m ^ 2) := by
  rw [sq]
  exact represents_mul h h

/-- If `P² + 3Q² = m · q` with `q = u² + 3v²` prime and `u, v` coprime, then `m` is represented by the form. -/
theorem represents_quotient_of_prime {P Q u v m q : ℤ} (hq : Prime q)
    (hcop : IsCoprime u v) (hm' : q = u ^ 2 + 3 * v ^ 2)
    (hprod : P ^ 2 + 3 * Q ^ 2 = m * q) :
    RepresentsForm m :=
  form_quotient_of_prime hq hcop hm' hprod

/-- Any prime represented by `u² + 3v²` forces `u` and `v` to be coprime. -/
theorem isCoprime_of_prime_form {u v q : ℤ} (hq : Prime q) (hform : q = u ^ 2 + 3 * v ^ 2) :
    IsCoprime u v := by
  rw [Int.isCoprime_iff_gcd_eq_one]
  by_contra h_contra
  have h_dvd_form : ((u.gcd v : ℤ) ^ 2) ∣ q := by
    rw [hform]
    have h_dvd_u : ((u.gcd v : ℤ) ^ 2) ∣ u ^ 2 := pow_dvd_pow_of_dvd Int.gcd_dvd_left 2
    have h_dvd_v : ((u.gcd v : ℤ) ^ 2) ∣ v ^ 2 := pow_dvd_pow_of_dvd Int.gcd_dvd_right 2
    have h_dvd_3v : ((u.gcd v : ℤ) ^ 2) ∣ 3 * v ^ 2 := dvd_mul_of_dvd_right h_dvd_v 3
    exact dvd_add h_dvd_u h_dvd_3v
  have h_prime_nat : Nat.Prime q.natAbs := Int.prime_iff_natAbs_prime.mp hq
  have h_dvd_nat : (u.gcd v) ^ 2 ∣ q.natAbs := by
    have h1 : (((u.gcd v) ^ 2 : ℕ) : ℤ) ∣ q := by
      push_cast
      exact h_dvd_form
    exact Int.natAbs_dvd_natAbs.mpr h1
  rcases (Nat.dvd_prime h_prime_nat).mp h_dvd_nat with h1 | hq_eq
  · have h_one : u.gcd v = 1 := Nat.eq_one_of_mul_eq_one_right (by rw [sq] at h1; exact h1)
    exact h_contra h_one
  · have h_dvd_q : u.gcd v ∣ q.natAbs := by
      rw [← hq_eq]
      exact dvd_pow_self (u.gcd v) (by decide)
    rcases (Nat.dvd_prime h_prime_nat).mp h_dvd_q with h_one' | h_q'
    · exact h_contra h_one'
    · rw [h_q'] at hq_eq
      have h_prime_gt : 1 < q.natAbs := h_prime_nat.one_lt
      nlinarith

/-- Prime-quotient representation without explicit coprime assumption on `u, v`. -/
theorem represents_quotient_of_prime' {P Q m q : ℤ} (hq : Prime q)
    (hq_form : RepresentsForm q)
    (hprod : P ^ 2 + 3 * Q ^ 2 = m * q) :
    RepresentsForm m := by
  obtain ⟨u, v, hm'⟩ := hq_form
  have hcop := isCoprime_of_prime_form hq hm'
  exact form_quotient_of_prime hq hcop hm' hprod

/-- Base case of Fermat descent: if the descent quotient is 1, q is represented directly. -/
theorem represents_of_quotient_one {p0 q0 q : ℤ}
    (h : p0 ^ 2 + 3 * q0 ^ 2 = q * 1) :
    RepresentsForm q := by
  refine ⟨p0, q0, ?_⟩
  rw [mul_one] at h
  exact h.symm

/-- When the descent quotient m' is a prime that represents, q represents. -/
theorem represents_q_of_prime_quotient {p0 q0 q m' : ℤ}
    (hm'_prime : Prime m') (hm'_form : RepresentsForm m')
    (hprod : p0 ^ 2 + 3 * q0 ^ 2 = q * m') :
    RepresentsForm q :=
  represents_quotient_of_prime' hm'_prime hm'_form hprod

/-- Strict descent on the quotient: peeling off a prime factor that represents yields
a new representation with strictly smaller quotient m1. -/
theorem descent_quotient_peel {p0 q0 q m1 p1 : ℤ}
    (hp1_prime : Prime p1) (hp1_form : RepresentsForm p1)
    (hprod : p0 ^ 2 + 3 * q0 ^ 2 = (q * m1) * p1) :
    ∃ X Y : ℤ, X ^ 2 + 3 * Y ^ 2 = q * m1 := by
  have h := represents_quotient_of_prime' hp1_prime hp1_form hprod
  obtain ⟨X, Y, hXY⟩ := h
  exact ⟨X, Y, hXY.symm⟩

/-! ### Unit classification and cubic descent in ℤ[ω] (Candidate C217)

To prove `CubeFormParam`, the unique factorisation in the maximal order `ℤ[ω]` of `ℚ(√-3)`
yields `p + q√-3 = u · α³` for a unit `u ∈ (𝓞 K)ˣ` and `α ∈ 𝓞 K`.
The unit group has order 6: `u ∈ {±1, ±ω, ±ω²}`.
Below, we formalise the parity obstructions showing that when `p - q` is odd:
1. Multiplying an element `A + B√-3` by `±ω` or `±ω²` forces the resulting difference `p - q` to be EVEN.
   Hence the hypothesis `¬ 2 ∣ (p - q)` strictly excludes the four non-trivial roots of unity `{±ω, ±ω²}`.
2. The remaining unit `-1` is absorbed into the cube via `(a, b) ↦ (-a, -b)`.
3. Every element `α ∈ ℤ[ω]` can be written as `ω^k · β` with `β ∈ ℤ[√-3]`, and since `(ω^k)³ = 1`,
   `α³ = β³ = (a + b√-3)³`, completing the cubic parametrisation. -/

/-- Unit multiplier `ω = (-1 + √-3)/2`: if `2p = -A - 3B` and `2q = A - B`, then `p - q` is even. -/
theorem unit_omega_parity_even (A B p q : ℤ)
    (hp : 2 * p = -A - 3 * B) (hq : 2 * q = A - B) :
    (2 : ℤ) ∣ (p - q) := by
  omega

/-- Unit multiplier `ω² = (-1 - √-3)/2`: if `2p = -A + 3B` and `2q = -(A + B)`, then `p - q` is even. -/
theorem unit_omega_sq_parity_even (A B p q : ℤ)
    (hp : 2 * p = -A + 3 * B) (hq : 2 * q = -(A + B)) :
    (2 : ℤ) ∣ (p - q) := by
  omega

/-- Unit multiplier `-ω = (1 - √-3)/2`: if `2p = A + 3B` and `2q = -(A - B)`, then `p - q` is even. -/
theorem unit_neg_omega_parity_even (A B p q : ℤ)
    (hp : 2 * p = A + 3 * B) (hq : 2 * q = -(A - B)) :
    (2 : ℤ) ∣ (p - q) := by
  omega

/-- Unit multiplier `-ω² = (1 + √-3)/2`: if `2p = A - 3B` and `2q = A + B`, then `p - q` is even. -/
theorem unit_neg_omega_sq_parity_even (A B p q : ℤ)
    (hp : 2 * p = A - 3 * B) (hq : 2 * q = A + B) :
    (2 : ℤ) ∣ (p - q) := by
  omega

/-- Obstruction to `ω`: odd difference `¬ 2 ∣ (p - q)` excludes unit `ω`. -/
theorem unit_omega_not_odd_diff (A B p q : ℤ) (hodd : ¬ (2 : ℤ) ∣ (p - q)) :
    ¬ (2 * p = -A - 3 * B ∧ 2 * q = A - B) := by
  rintro ⟨hp, hq⟩
  exact hodd (unit_omega_parity_even A B p q hp hq)

/-- Obstruction to `ω²`: odd difference `¬ 2 ∣ (p - q)` excludes unit `ω²`. -/
theorem unit_omega_sq_not_odd_diff (A B p q : ℤ) (hodd : ¬ (2 : ℤ) ∣ (p - q)) :
    ¬ (2 * p = -A + 3 * B ∧ 2 * q = -(A + B)) := by
  rintro ⟨hp, hq⟩
  exact hodd (unit_omega_sq_parity_even A B p q hp hq)

/-- Obstruction to `-ω`: odd difference `¬ 2 ∣ (p - q)` excludes unit `-ω`. -/
theorem unit_neg_omega_not_odd_diff (A B p q : ℤ) (hodd : ¬ (2 : ℤ) ∣ (p - q)) :
    ¬ (2 * p = A + 3 * B ∧ 2 * q = -(A - B)) := by
  rintro ⟨hp, hq⟩
  exact hodd (unit_neg_omega_parity_even A B p q hp hq)

/-- Obstruction to `-ω²`: odd difference `¬ 2 ∣ (p - q)` excludes unit `-ω²`. -/
theorem unit_neg_omega_sq_not_odd_diff (A B p q : ℤ) (hodd : ¬ (2 : ℤ) ∣ (p - q)) :
    ¬ (2 * p = A - 3 * B ∧ 2 * q = A + B) := by
  rintro ⟨hp, hq⟩
  exact hodd (unit_neg_omega_sq_parity_even A B p q hp hq)

/-- Unit `-1` absorption: negating the cubic parameterization is equivalent to
negating the parameters `(a, b) ↦ (-a, -b)`. -/
theorem cube_param_neg (a b : ℤ) :
    -(a * (a - 3 * b) * (a + 3 * b)) = (-a) * ((-a) - 3 * (-b)) * ((-a) + 3 * (-b)) ∧
    -(3 * b * (a ^ 2 - b ^ 2)) = 3 * (-b) * ((-a) ^ 2 - (-b) ^ 2) := by
  constructor <;> ring

/-- Base ring reduction case 1 (both coordinates even): already in `ℤ[√-3]`. -/
theorem eisenstein_coords_even (u v : ℤ) (hu : (2 : ℤ) ∣ u) (hv : (2 : ℤ) ∣ v) :
    ∃ a b : ℤ, 2 * a = u ∧ 2 * b = v := by
  obtain ⟨a, ha⟩ := hu
  obtain ⟨b, hb⟩ := hv
  exact ⟨a, b, by omega, by omega⟩

/-- Base ring reduction case 2a (`u ≡ v [mod 4]`): multiplication by `ω` produces
integral coordinates in `ℤ[√-3]`. -/
theorem eisenstein_coords_mod4_same (u v : ℤ) (h4 : (4 : ℤ) ∣ (u - v)) :
    (4 : ℤ) ∣ (-u - 3 * v) ∧ (4 : ℤ) ∣ (u - v) := by
  constructor
  · obtain ⟨k, hk⟩ := h4
    exact ⟨-k - v, by linear_combination -hk⟩
  · exact h4

/-- Base ring reduction case 2b (`u ≡ -v [mod 4]`): multiplication by `ω²` produces
integral coordinates in `ℤ[√-3]`. -/
theorem eisenstein_coords_mod4_opp (u v : ℤ) (h4 : (4 : ℤ) ∣ (u + v)) :
    (4 : ℤ) ∣ (-u + 3 * v) ∧ (4 : ℤ) ∣ (-(u + v)) := by
  constructor
  · obtain ⟨k, hk⟩ := h4
    exact ⟨-k + v, by linear_combination -hk⟩
  · obtain ⟨k, hk⟩ := h4
    exact ⟨-k, by linear_combination -hk⟩

/-- For any two odd integers A and B, A(A² - 9B²) is divisible by 8. -/
theorem odd_cube_real_div_eight (a b : ℤ) :
    (8 : ℤ) ∣ (2 * a + 1) * ((2 * a + 1) ^ 2 - 9 * (2 * b + 1) ^ 2) := by
  obtain ⟨k, hk⟩ := Int.even_mul_succ_self a
  obtain ⟨l, hl⟩ := Int.even_mul_succ_self b
  have ha : (2 * a + 1) ^ 2 = 4 * (a * (a + 1)) + 1 := by ring
  have hb : (2 * b + 1) ^ 2 = 4 * (b * (b + 1)) + 1 := by ring
  rw [hk] at ha
  rw [hl] at hb
  have hdiff : (2 * a + 1) ^ 2 - 9 * (2 * b + 1) ^ 2 = 8 * (k - 9 * l - 1) := by
    linear_combination ha - 9 * hb
  rw [hdiff]
  refine ⟨(2 * a + 1) * (k - 9 * l - 1), by ring⟩

/-- For any two odd integers A and B, 3B(A² - B²) is divisible by 8. -/
theorem odd_cube_imag_div_eight (a b : ℤ) :
    (8 : ℤ) ∣ 3 * (2 * b + 1) * ((2 * a + 1) ^ 2 - (2 * b + 1) ^ 2) := by
  obtain ⟨k, hk⟩ := Int.even_mul_succ_self a
  obtain ⟨l, hl⟩ := Int.even_mul_succ_self b
  have ha : (2 * a + 1) ^ 2 = 4 * (a * (a + 1)) + 1 := by ring
  have hb : (2 * b + 1) ^ 2 = 4 * (b * (b + 1)) + 1 := by ring
  rw [hk] at ha
  rw [hl] at hb
  have hdiff : (2 * a + 1) ^ 2 - (2 * b + 1) ^ 2 = 8 * (k - l) := by
    linear_combination ha - hb
  rw [hdiff]
  refine ⟨3 * (2 * b + 1) * (k - l), by ring⟩

/-- Constructive integral coordinates for the cube of any odd-coordinate Eisenstein integer. -/
theorem eisenstein_cube_coords_integral (a b : ℤ) :
    ∃ X Y : ℤ, 8 * X = (2 * a + 1) * ((2 * a + 1) ^ 2 - 9 * (2 * b + 1) ^ 2) ∧
               8 * Y = 3 * (2 * b + 1) * ((2 * a + 1) ^ 2 - (2 * b + 1) ^ 2) := by
  obtain ⟨X, hX⟩ := odd_cube_real_div_eight a b
  obtain ⟨Y, hY⟩ := odd_cube_imag_div_eight a b
  exact ⟨X, Y, hX.symm, hY.symm⟩

/-! ### Prime reduction for `OddDivisorForm` (Candidate C218)

By multiplicative closure (`represents_mul` and `represents_list_prod`), a positive integer `m`
represents as `u² + 3v²` as soon as all its prime factors do.
This reduces the entire `OddDivisorForm` problem from general composite integers to PRIME divisors,
bypassing the composite division obstruction (C214) cleanly. -/

/-- Product of representations: if every element in a list of integers is represented
by `x² + 3y²`, their product is also represented. -/
theorem represents_list_prod (l : List ℤ) (hl : ∀ x ∈ l, RepresentsForm x) :
    RepresentsForm l.prod := by
  induction' l with head tail ih
  · exact represents_one
  · rw [List.prod_cons]
    have hhead : RepresentsForm head := hl head (List.mem_cons_self head tail)
    have htail : RepresentsForm tail.prod := ih (fun x hx => hl x (List.mem_cons_of_mem head hx))
    exact represents_mul hhead htail

/-- The cast of a natural product of a list is the integer product of the cast list. -/
theorem nat_cast_list_prod (l : List ℕ) :
    ((l.prod : ℕ) : ℤ) = (l.map (fun (p : ℕ) => (p : ℤ))).prod := by
  induction' l with head tail ih
  · rfl
  · rw [List.prod_cons, List.map_cons, List.prod_cons, Nat.cast_mul, ih]

/-- If every prime factor of a positive natural `n` represents as `u² + 3v²`,
then `n` itself represents as `u² + 3v²`. -/
theorem represents_of_prime_factors (n : ℕ) (hn : n ≠ 0)
    (hprimes : ∀ p ∈ n.primeFactorsList, RepresentsForm (p : ℤ)) :
    RepresentsForm (n : ℤ) := by
  have heq : (n : ℤ) = (n.primeFactorsList.map (fun (p : ℕ) => (p : ℤ))).prod := by
    rw [← nat_cast_list_prod, Nat.prod_primeFactorsList hn]
  rw [heq]
  apply represents_list_prod
  intro x hx
  obtain ⟨p, hp, rfl⟩ := List.mem_map.mp hx
  exact hprimes p hp

/-- If every prime factor of `|m|` represents, then positive `m` represents. -/
theorem represents_of_natAbs_prime_factors (m : ℤ) (hm : 0 < m)
    (hprimes : ∀ p ∈ m.natAbs.primeFactorsList, RepresentsForm (p : ℤ)) :
    RepresentsForm m := by
  have hne : m.natAbs ≠ 0 := by omega
  have hcast : (m.natAbs : ℤ) = m := Int.natAbs_of_nonneg (by omega)
  rw [← hcast]
  exact represents_of_prime_factors m.natAbs hne hprimes

/-- **OddPrimeDivisorForm**: every odd prime dividing `P² + 3Q²` with `P, Q` coprime
is of the form `u² + 3v²`. -/
def OddPrimeDivisorForm : Prop :=
  ∀ (q : ℕ) (P Q : ℤ), Nat.Prime q → q ≠ 2 →
    IsCoprime P Q → (q : ℤ) ∣ P ^ 2 + 3 * Q ^ 2 →
    RepresentsForm (q : ℤ)

/-- Positive-modulus version of `OddDivisorForm`. -/
def OddDivisorFormPos : Prop :=
  ∀ m p q : ℤ, 0 < m → ¬ (2 : ℤ) ∣ m → m ∣ p ^ 2 + 3 * q ^ 2 → IsCoprime p q →
    RepresentsForm m

/-- **The Prime-Reduction Theorem (Candidate C218).**
`OddDivisorFormPos` reduces completely to `OddPrimeDivisorForm`.
Any composite odd divisor is represented as soon as all odd prime divisors are. -/
theorem odd_divisor_form_of_prime (Hprime : OddPrimeDivisorForm) : OddDivisorFormPos := by
  intro m p q hm hodd hdvd hcop
  apply represents_of_natAbs_prime_factors m hm
  intro pr hpr
  have hprime_nat : Nat.Prime pr := Nat.prime_of_mem_primeFactorsList hpr
  have hdvd_nat : pr ∣ m.natAbs := Nat.dvd_of_mem_primeFactorsList hpr
  have hdvd_int : (pr : ℤ) ∣ m := by
    have : (pr : ℤ) ∣ (m.natAbs : ℤ) := by exact_mod_cast hdvd_nat
    rwa [Int.natAbs_of_nonneg (by omega)] at this
  have hpr_ne_two : pr ≠ 2 := by
    intro heq
    subst heq
    have : (2 : ℤ) ∣ m := hdvd_int
    exact hodd this
  have hdvd_form : (pr : ℤ) ∣ p ^ 2 + 3 * q ^ 2 := dvd_trans hdvd_int hdvd
  exact Hprime pr p q hprime_nat hpr_ne_two hcop hdvd_form

/-! ### Constructive 4-division of the quadratic form (Candidate C219)

In the Fermat descent `P² + 3Q² = q · m'`, when `P` and `Q` share a parity, `4 ∣ (P² + 3Q²)`.
Below, we prove constructively that `(P² + 3Q²)/4` is ALWAYS represented as `X² + 3Y²`:
- If `P, Q` are both even: `X = P/2, Y = Q/2`.
- If `P, Q` are both odd with `P ≡ Q [mod 4]`: `X = P - 3k, Y = -k` where `P - Q = 4k`.
- If `P, Q` are both odd with `P ≡ -Q [mod 4]`: `X = Q - k, Y = -k` where `P + Q = 4k`.
This completely discharges the 2-part halving step of the Fermat descent. -/

/-- 4-division of the form when `4 ∣ (P - Q)`: `X = P - 3k, Y = -k` satisfies
`4 · (X² + 3Y²) = P² + 3Q²`. -/
theorem form_div_four_same (P Q : ℤ) (h4 : (4 : ℤ) ∣ (P - Q)) :
    ∃ X Y : ℤ, 4 * (X ^ 2 + 3 * Y ^ 2) = P ^ 2 + 3 * Q ^ 2 := by
  obtain ⟨k, _hk⟩ := h4
  have hQ : Q = P - 4 * k := by omega
  refine ⟨P - 3 * k, -k, ?_⟩
  rw [hQ]
  ring

/-- 4-division of the form when `4 ∣ (P + Q)`: `X = Q - k, Y = -k` satisfies
`4 · (X² + 3Y²) = P² + 3Q²`. -/
theorem form_div_four_opp (P Q : ℤ) (h4 : (4 : ℤ) ∣ (P + Q)) :
    ∃ X Y : ℤ, 4 * (X ^ 2 + 3 * Y ^ 2) = P ^ 2 + 3 * Q ^ 2 := by
  obtain ⟨k, _hk⟩ := h4
  have hP : P = 4 * k - Q := by omega
  refine ⟨Q - k, -k, ?_⟩
  rw [hP]
  ring

/-- 4-division when both `P` and `Q` are even. -/
theorem form_div_four_both_even (P Q : ℤ) (hP : (2 : ℤ) ∣ P) (hQ : (2 : ℤ) ∣ Q) :
    ∃ X Y : ℤ, 4 * (X ^ 2 + 3 * Y ^ 2) = P ^ 2 + 3 * Q ^ 2 := by
  obtain ⟨X, rfl⟩ := hP
  obtain ⟨Y, rfl⟩ := hQ
  exact ⟨X, Y, by ring⟩

/-- Parity trichotomy: two odd integers are either congruent mod 4 or opposite mod 4. -/
theorem odd_mod_four_cases (P Q : ℤ) (hP : ¬ (2 : ℤ) ∣ P) (hQ : ¬ (2 : ℤ) ∣ Q) :
    (4 : ℤ) ∣ (P - Q) ∨ (4 : ℤ) ∣ (P + Q) := by
  omega

/-- **Universal 4-division for same-parity pairs.**
Whenever `P` and `Q` have the same parity, `(P² + 3Q²)/4` is represented by `X² + 3Y²`. -/
theorem form_div_four_of_same_parity (P Q : ℤ) (hpar : (P - Q) % 2 = 0) :
    ∃ X Y : ℤ, 4 * (X ^ 2 + 3 * Y ^ 2) = P ^ 2 + 3 * Q ^ 2 := by
  rcases Int.even_or_odd P with ⟨a, ha⟩ | ⟨a, ha⟩
  · have hQ : 2 ∣ Q := by omega
    exact form_div_four_both_even P Q ⟨a, by omega⟩ hQ
  · have hPodd : ¬ (2 : ℤ) ∣ P := by omega
    have hQodd : ¬ (2 : ℤ) ∣ Q := by omega
    rcases odd_mod_four_cases P Q hPodd hQodd with hsame | hopp
    · exact form_div_four_same P Q hsame
    · exact form_div_four_opp P Q hopp

/-- 4-division of the form whenever `P² + 3Q²` is even. -/
theorem form_div_four_of_even (P Q : ℤ) (h2 : (2 : ℤ) ∣ (P ^ 2 + 3 * Q ^ 2)) :
    ∃ X Y : ℤ, 4 * (X ^ 2 + 3 * Y ^ 2) = P ^ 2 + 3 * Q ^ 2 := by
  have hsum : (2 : ℤ) ∣ (P + Q) := (form_even_iff P Q).mp h2
  have hpar : (P - Q) % 2 = 0 := by
    obtain ⟨k, hk⟩ := hsum
    omega
  exact form_div_four_of_same_parity P Q hpar

/-- Modulo 4 divisibility: if `2 ∣ (P² + 3Q²)`, then automatically `4 ∣ (P² + 3Q²)`. -/
theorem form_four_dvd_of_even (P Q : ℤ) (h2 : (2 : ℤ) ∣ (P ^ 2 + 3 * Q ^ 2)) :
    (4 : ℤ) ∣ (P ^ 2 + 3 * Q ^ 2) := by
  obtain ⟨X, Y, hXY⟩ := form_div_four_of_even P Q h2
  exact ⟨X ^ 2 + 3 * Y ^ 2, hXY.symm⟩

/-- 4-peeling on the quotient: dividing out a factor of 4 yields a representation with
quotient m1 = m'/4. -/
theorem descent_quotient_peel_four {p0 q0 q m1 : ℤ}
    (hprod : p0 ^ 2 + 3 * q0 ^ 2 = q * (4 * m1)) :
    ∃ X Y : ℤ, X ^ 2 + 3 * Y ^ 2 = q * m1 := by
  have h2 : (2 : ℤ) ∣ (p0 ^ 2 + 3 * q0 ^ 2) := by
    rw [hprod]
    refine ⟨q * (2 * m1), by ring⟩
  obtain ⟨X, Y, hXY⟩ := form_div_four_of_even p0 q0 h2
  have h4_eq : 4 * (X ^ 2 + 3 * Y ^ 2) = 4 * (q * m1) := by
    calc 4 * (X ^ 2 + 3 * Y ^ 2) = p0 ^ 2 + 3 * q0 ^ 2 := hXY
      _ = q * (4 * m1) := hprod
      _ = 4 * (q * m1) := by ring
  have h4_ne : (4 : ℤ) ≠ 0 := by decide
  exact ⟨X, Y, mul_left_cancel₀ h4_ne h4_eq⟩

/-! ### Cyclotomic Unit Elimination and Cube Integrality (Candidate C243)

Under the odd-difference condition `¬ 2 ∣ (p - q)`, the non-trivial roots of unity
`{±ω, ±ω²}` in the maximal order `ℤ[ω]` are strictly excluded because multiplying by
them forces `p - q` to be even.
The remaining unit `-1` is absorbed into the cube via `(a, b) ↦ (-a, -b)`.
Furthermore, every cube of an element in `ℤ[ω]` with integral coordinates is identically
the cube of an element in `ℤ[√-3]`. Thus, any solution represented in `ℤ[ω]` yields
genuine integer parameters `a, b : ℤ` satisfying `p = a(a - 3b)(a + 3b)` and `q = 3b(a² - b²)`. -/

/-- Ring identity for mod-4 same-parity real coordinate. -/
theorem eisenstein_cube_param_mod4_same_real (k v : ℤ) :
    (-k - v) * ((-k - v) ^ 2 - 9 * k ^ 2) * 8 = (v + 4 * k) * ((v + 4 * k) ^ 2 - 9 * v ^ 2) := by
  ring

/-- Ring identity for mod-4 same-parity imaginary coordinate. -/
theorem eisenstein_cube_param_mod4_same_imag (k v : ℤ) :
    3 * k * ((-k - v) ^ 2 - k ^ 2) * 8 = 3 * v * ((v + 4 * k) ^ 2 - v ^ 2) := by
  ring

/-- Ring identity for mod-4 opposite-parity real coordinate. -/
theorem eisenstein_cube_param_mod4_opp_real (k v : ℤ) :
    (v - k) * ((v - k) ^ 2 - 9 * (-k) ^ 2) * 8 = (4 * k - v) * ((4 * k - v) ^ 2 - 9 * v ^ 2) := by
  ring

/-- Ring identity for mod-4 opposite-parity imaginary coordinate. -/
theorem eisenstein_cube_param_mod4_opp_imag (k v : ℤ) :
    3 * (-k) * ((v - k) ^ 2 - (-k) ^ 2) * 8 = 3 * v * ((4 * k - v) ^ 2 - v ^ 2) := by
  ring

/-- Ring identity for even coordinates real coordinate. -/
theorem eisenstein_cube_param_even_real (a b : ℤ) :
    (2 * a) * ((2 * a) ^ 2 - 9 * (2 * b) ^ 2) = 8 * (a * (a ^ 2 - 9 * b ^ 2)) := by
  ring

/-- Ring identity for even coordinates imaginary coordinate. -/
theorem eisenstein_cube_param_even_imag (a b : ℤ) :
    3 * (2 * b) * ((2 * a) ^ 2 - (2 * b) ^ 2) = 8 * (3 * b * (a ^ 2 - b ^ 2)) := by
  ring

/-- **Universal Eisenstein Cube Integrality Theorem (Candidate C243).**
Every cube of an element in `ℤ[ω]` with integral coordinates `(X, Y)` is
identically the cube of an element in the base ring `ℤ[√-3]`. -/
theorem eisenstein_cube_integral_param {u v X Y : ℤ}
    (hpar : (u - v) % 2 = 0)
    (hX : 8 * X = u * (u ^ 2 - 9 * v ^ 2))
    (hY : 8 * Y = 3 * v * (u ^ 2 - v ^ 2)) :
    ∃ a b : ℤ, X = a * (a - 3 * b) * (a + 3 * b) ∧ Y = 3 * b * (a ^ 2 - b ^ 2) := by
  have h8 : (8 : ℤ) ≠ 0 := by decide
  rcases Int.even_or_odd u with ⟨a0, ha0⟩ | ⟨a0, ha0⟩
  · have h2u : (2 : ℤ) ∣ u := ⟨a0, by omega⟩
    have h2v : (2 : ℤ) ∣ v := by omega
    obtain ⟨b0, rfl⟩ := h2v
    obtain ⟨a0_val, rfl⟩ := h2u
    have hX_eq : 8 * X = 8 * (a0_val * (a0_val ^ 2 - 9 * b0 ^ 2)) := by
      calc 8 * X = (2 * a0_val) * ((2 * a0_val) ^ 2 - 9 * (2 * b0) ^ 2) := hX
        _ = 8 * (a0_val * (a0_val ^ 2 - 9 * b0 ^ 2)) := eisenstein_cube_param_even_real a0_val b0
    have hY_eq : 8 * Y = 8 * (3 * b0 * (a0_val ^ 2 - b0 ^ 2)) := by
      calc 8 * Y = 3 * (2 * b0) * ((2 * a0_val) ^ 2 - (2 * b0) ^ 2) := hY
        _ = 8 * (3 * b0 * (a0_val ^ 2 - b0 ^ 2)) := eisenstein_cube_param_even_imag a0_val b0
    have hX_val : X = a0_val * (a0_val ^ 2 - 9 * b0 ^ 2) := mul_left_cancel₀ h8 hX_eq
    have hY_val : Y = 3 * b0 * (a0_val ^ 2 - b0 ^ 2) := mul_left_cancel₀ h8 hY_eq
    refine ⟨a0_val, b0, ?_, hY_val⟩
    rw [hX_val]
    ring
  · have hu_odd : ¬ (2 : ℤ) ∣ u := by omega
    have hv_odd : ¬ (2 : ℤ) ∣ v := by omega
    rcases odd_mod_four_cases u v hu_odd hv_odd with hsame | hopp
    · obtain ⟨k, hk⟩ := hsame
      have hu : u = v + 4 * k := by omega
      have hX_eq : 8 * X = 8 * ((-k - v) * ((-k - v) ^ 2 - 9 * k ^ 2)) := by
        calc 8 * X = u * (u ^ 2 - 9 * v ^ 2) := hX
          _ = 8 * ((-k - v) * ((-k - v) ^ 2 - 9 * k ^ 2)) := by
            rw [hu]
            linear_combination -(eisenstein_cube_param_mod4_same_real k v)
      have hY_eq : 8 * Y = 8 * (3 * k * ((-k - v) ^ 2 - k ^ 2)) := by
        calc 8 * Y = 3 * v * (u ^ 2 - v ^ 2) := hY
          _ = 8 * (3 * k * ((-k - v) ^ 2 - k ^ 2)) := by
            rw [hu]
            linear_combination -(eisenstein_cube_param_mod4_same_imag k v)
      have hX_val : X = (-k - v) * ((-k - v) ^ 2 - 9 * k ^ 2) := mul_left_cancel₀ h8 hX_eq
      have hY_val : Y = 3 * k * ((-k - v) ^ 2 - k ^ 2) := mul_left_cancel₀ h8 hY_eq
      refine ⟨-k - v, k, ?_, hY_val⟩
      rw [hX_val]
      ring
    · obtain ⟨k, hk⟩ := hopp
      have hu : u = 4 * k - v := by omega
      have hX_eq : 8 * X = 8 * ((v - k) * ((v - k) ^ 2 - 9 * (-k) ^ 2)) := by
        calc 8 * X = u * (u ^ 2 - 9 * v ^ 2) := hX
          _ = 8 * ((v - k) * ((v - k) ^ 2 - 9 * (-k) ^ 2)) := by
            rw [hu]
            linear_combination -(eisenstein_cube_param_mod4_opp_real k v)
      have hY_eq : 8 * Y = 8 * (3 * (-k) * ((v - k) ^ 2 - (-k) ^ 2)) := by
        calc 8 * Y = 3 * v * (u ^ 2 - v ^ 2) := hY
          _ = 8 * (3 * (-k) * ((v - k) ^ 2 - (-k) ^ 2)) := by
            rw [hu]
            linear_combination -(eisenstein_cube_param_mod4_opp_imag k v)
      have hX_val : X = (v - k) * ((v - k) ^ 2 - 9 * (-k) ^ 2) := mul_left_cancel₀ h8 hX_eq
      have hY_val : Y = 3 * (-k) * ((v - k) ^ 2 - (-k) ^ 2) := mul_left_cancel₀ h8 hY_eq
      refine ⟨v - k, -k, ?_, hY_val⟩
      rw [hX_val]
      ring

/-- Unit negation preserves the cubic form parametrization via `(a, b) ↦ (-a, -b)`. -/
theorem cube_param_of_neg {X Y : ℤ}
    (h : ∃ a b : ℤ, X = a * (a - 3 * b) * (a + 3 * b) ∧ Y = 3 * b * (a ^ 2 - b ^ 2)) :
    ∃ a b : ℤ, -X = a * (a - 3 * b) * (a + 3 * b) ∧ -Y = 3 * b * (a ^ 2 - b ^ 2) := by
  obtain ⟨a, b, hX, hY⟩ := h
  refine ⟨-a, -b, ?_, ?_⟩
  · rw [hX]
    exact (cube_param_neg a b).1
  · rw [hY]
    exact (cube_param_neg a b).2

/-- **Cyclotomic Unit Elimination Dispatcher (Candidate C243).**
Under `¬ 2 ∣ (p - q)`, if `p + q√-3 = ± α³` for an Eisenstein integer `α`,
then `(p, q)` unconditionally satisfies the cubic parametrization `(a(a² - 9b²), 3b(a² - b²))`. -/
theorem cube_param_of_eisenstein_cube {u v p q : ℤ}
    (hpar : (u - v) % 2 = 0)
    (hsign : (8 * p = u * (u ^ 2 - 9 * v ^ 2) ∧ 8 * q = 3 * v * (u ^ 2 - v ^ 2)) ∨
             (8 * p = -(u * (u ^ 2 - 9 * v ^ 2)) ∧ 8 * q = -(3 * v * (u ^ 2 - v ^ 2)))) :
    ∃ a b : ℤ, p = a * (a - 3 * b) * (a + 3 * b) ∧ q = 3 * b * (a ^ 2 - b ^ 2) := by
  rcases hsign with ⟨hp, hq⟩ | ⟨hp, hq⟩
  · exact eisenstein_cube_integral_param hpar hp hq
  · have hneg_p : 8 * (-p) = u * (u ^ 2 - 9 * v ^ 2) := by linear_combination -hp
    have hneg_q : 8 * (-q) = 3 * v * (u ^ 2 - v ^ 2) := by linear_combination -hq
    have h_pos := eisenstein_cube_integral_param hpar hneg_p hneg_q
    have h_neg := cube_param_of_neg h_pos
    have hneg_neg_p : -(-p) = p := neg_neg p
    have hneg_neg_q : -(-q) = q := neg_neg q
    rw [hneg_neg_p, hneg_neg_q] at h_neg
    exact h_neg

end Beal



