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

/-- In the branch `3 ∤ p`, both factors are cubes. -/
theorem factors_are_cubes {p q c : ℤ} (hpq : IsCoprime p q) (h3 : ¬ (3 : ℤ) ∣ p)
    (h : p * (p ^ 2 + 3 * q ^ 2) = c ^ 3) :
    (∃ s, p = s ^ 3) ∧ (∃ t, p ^ 2 + 3 * q ^ 2 = t ^ 3) := by
  have hcop := coprime_p_norm hpq h3
  have hodd : Odd 3 := ⟨1, by norm_num⟩
  exact ⟨Int.eq_pow_of_mul_eq_pow_odd_left hcop hodd h,
    Int.eq_pow_of_mul_eq_pow_odd_right hcop hodd h⟩

end Beal
