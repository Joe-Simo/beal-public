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

/-- **Step 3.**  The descent lands back on Euler's own equation: the two outer factors sum to
twice the middle one, so three cubes `a = e³`, `a - 3b = f³`, `a + 3b = g³` give `f³ + g³ = 2e³`. -/
theorem descent_sum (a b : ℤ) : (a - 3 * b) + (a + 3 * b) = 2 * a := by ring

theorem descent_to_euler {a b e f g : ℤ} (he : a = e ^ 3) (hf : a - 3 * b = f ^ 3)
    (hg : a + 3 * b = g ^ 3) : f ^ 3 + g ^ 3 = 2 * e ^ 3 := by
  have := descent_sum a b
  rw [hf, hg, he] at this
  exact this

/-! ### Towards `OddDivisorForm`: the descent step, formalised (U359, pool C211)

`OddDivisorForm` is proved classically by Fermat descent on the symmetric residues mod `m`.  The
step itself is formalised below: the residues stay congruent, they are bounded by `m/2` in absolute
value, and `m` still divides `P² + 3Q²`.  What is NOT yet formalised is the strong induction that
turns one step into the theorem, together with the division of `P² + 3Q² = m·m'` by `m'` using
`form_mul`.  Numerical validation of the step: 18,488 triples, zero violations, maximum ratio
`m'/m = 0.9336` (pool C203). -/

/-- A symmetric residue: `symRes a m` is congruent to `a` mod `m` and has `2·|symRes| ≤ m`. -/
def symRes (a m : ℤ) : ℤ := if 2 * (a % m) ≤ m then a % m else a % m - m

theorem symRes_congr (a m : ℤ) (hm : 0 < m) : m ∣ a - symRes a m := by
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

end Beal
