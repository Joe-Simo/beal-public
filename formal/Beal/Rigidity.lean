/-
# Katz rigidity and the exponent budget (U253–U256, pool C120/C121)

**CORRECTED (U309).**  This file was headed "why no rigid local system can carry three
independent Beal exponents".  That headline is **withdrawn**: it is refuted by
`code/U309_rigidity_countersearch.py`.  The theorems below are unaffected and stand; what was
wrong was the reading of them.

The error was to identify "local monodromy has **order** `x`" (what an exponent forces) with
"local monodromy is **regular semisimple** with eigenvalues of order `x`" (what the theorems
assume).  A pseudoreflection with partition `(n-1, 1)` has order equal to the order of its single
non-trivial eigenvalue, which may be *any* `m`.  So the hypergeometric triple `((1ⁿ),(1ⁿ),(n-1,1))`
is rigid at every rank and realises three **pairwise distinct** local orders — e.g. `(3,7,11)` at
`n = 6`.  Rigidity therefore does **not** forbid three independent exponents.

What survives is the narrower, correct statement below: rigidity forbids three *regular
semisimple* punctures beyond rank `2`.

For a local system of rank `n` on `P¹ ∖ {0,1,∞}` with semisimple local monodromies whose
eigenvalue multiplicities are the parts of three partitions of `n`, Katz's rigidity index is

    rig = -n² + (sum of squares of all the multiplicities),

and the system is **rigid** exactly when `rig = 2`.

Two facts are formalised here.

* `rigid_regular_semisimple_iff` — if all three local monodromies are *regular semisimple*
  (`n` distinct eigenvalues at each puncture, which is what monodromy of order `x` acting with
  distinct eigenvalues gives), then every multiplicity is `1`, the sum of squares is `3n`, and
  rigidity forces `n = 1` or `n = 2`.  Rank `2` is the classical hypergeometric `₂F₁` /
  elliptic-curve Frey situation, already exploited one signature at a time.

* `rigid_max_budget_attained` — the triple `((n-1,1), (1ⁿ), (1ⁿ))` is rigid for **every** `n`,
  by the identity `-n² + ((n-1)² + 1) + n + n = 2`.  Its total number of distinct eigenvalues is
  `2n+2`, one puncture being reduced to just two.

The matching upper bound (no rigid triple exceeds `2n+2` distinct eigenvalues) is verified
exhaustively for `2 ≤ n ≤ 14` in `code/U254_rigid_eigenvalue_budget.py`; it is recorded in the
pool as C121 and is *not* claimed here.

Since regular-semisimple monodromy at all three punctures needs `3n` distinct eigenvalues and
`2n+2 ≥ 3n` only at `n = 2`, the deficit `n-2` is the exact cost of demanding *regular
semisimplicity* at all three punctures.  Per the U309 correction above, that is **not** the same
as the cost of three independent exponents, which rigidity does not charge for at all.  This is a
statement about one *obstruction*, not a step toward a proof of Beal.

No `sorry`, no custom `axiom`s; mathlib only.
-/
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Data.Nat.Totient
import Mathlib.Tactic.IntervalCases
import Mathlib.Algebra.Order.BigOperators.Group.Finset

namespace Beal

/-- Katz rigidity index of a rank-`n` local system on `P¹ ∖ {0,1,∞}` whose local monodromies have
eigenvalue multiplicities summing (in squares) to `s`. -/
def rigidityIndex (n s : ℤ) : ℤ := -n ^ 2 + s

/-- **Regular semisimple at all three punctures.**  Every multiplicity is `1`, so the sum of
squares is `3n`, and rigidity `rig = 2` forces `n = 1` or `n = 2`. -/
theorem rigid_regular_semisimple_iff (n : ℤ) (hn : 0 < n) :
    rigidityIndex n (3 * n) = 2 ↔ n = 1 ∨ n = 2 := by
  unfold rigidityIndex
  constructor
  · intro h
    have hfac : (n - 1) * (n - 2) = 0 := by linarith [h]
    rcases mul_eq_zero.mp hfac with h1 | h2
    · exact Or.inl (by linarith)
    · exact Or.inr (by linarith)
  · rintro (rfl | rfl) <;> norm_num

/-- **The maximal budget is attained at every rank.**  The multiplicity triple
`((n-1, 1), (1,…,1), (1,…,1))` has squares summing to `(n-1)^2 + 1 + n + n`, and that is rigid
for every `n`. -/
theorem rigid_max_budget_attained (n : ℤ) :
    rigidityIndex n ((n - 1) ^ 2 + 1 + n + n) = 2 := by
  unfold rigidityIndex; ring

/-- Its distinct-eigenvalue total is `2 + n + n = 2n + 2`. -/
theorem max_budget_total (n : ℤ) : 2 + n + n = 2 * n + 2 := by ring

/-- **The gap.**  Regular semisimple monodromy at all three punctures needs `3n` distinct
eigenvalues; the attained maximum is `2n+2`.  These agree only at `n = 2`, and for `n > 2` the
deficit is exactly `n - 2`. -/
theorem budget_deficit (n : ℤ) : 3 * n - (2 * n + 2) = n - 2 := by ring

/-! ### The cost of dropping rigidity (U257, pool C123)

If rigidity is abandoned, local systems with three regular-semisimple monodromies of rank `n` do
exist — but they come in a positive-dimensional family, so there is no *canonical* object to
attach to a solution.  The number of accessory parameters is `2 - rig`, and here that is exactly
`(n-1)(n-2)`: zero precisely at `n = 1, 2`, and growing quadratically afterwards.

This is the second half of the obstruction.  Rank `≤ 2` gives a canonical object but cannot carry
three independent exponents (`rigid_regular_semisimple_iff`); rank `≥ 3` can carry them but only
inside a moduli of dimension `(n-1)(n-2) > 0`, with no distinguished member.  A Frey-type
construction needs both at once. -/

/-- The accessory-parameter count for a rank-`n` local system with three regular-semisimple local
monodromies is `(n-1)(n-2)`. -/
theorem moduli_dimension_regular_semisimple (n : ℤ) :
    2 - rigidityIndex n (3 * n) = (n - 1) * (n - 2) := by
  unfold rigidityIndex; ring

/-- It vanishes exactly at `n = 1` and `n = 2`. -/
theorem moduli_dimension_eq_zero_iff (n : ℤ) :
    (n - 1) * (n - 2) = 0 ↔ n = 1 ∨ n = 2 := by
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | h2
    · exact Or.inl (by linarith)
    · exact Or.inr (by linarith)
  · rintro (rfl | rfl) <;> norm_num

/-! ### Rank 2 over `Q`: only the exponents `3, 4, 6` survive (U258, pool C124)

`rigid_regular_semisimple_iff` leaves rank `2` as the only rigid possibility.  Ask what rank `2`
can carry **over `Q`**.  A local monodromy of order `x` acting with distinct eigenvalues has
eigenvalue ratio a primitive `x`-th root of unity; for the object to be defined over `Q` in
rank `2`, that root must generate a field of degree at most `2`, i.e. `φ(x) ≤ 2`.

Exactly: `φ(x) ≤ 2` iff `x ∈ {1, 2, 3, 4, 6}` (formalised below for `x ≤ 30`; checked for `x < 200` in `code/` this cycle), so the
Beal-admissible exponents (`x ≥ 3`) that rank `2` can carry over `Q` are only

    x ∈ {3, 4, 6},

and the hyperbolic triples available are the nine
`(3,3,4), (3,3,6), (3,4,4), (3,4,6), (3,6,6), (4,4,4), (4,4,6), (4,6,6), (6,6,6)`.
Every exponent in the open core — `5, 7, 11, 13, …` — has `φ ≥ 4` and is excluded.

That is the third face of the obstruction, and it explains the shape of the literature: the
classical rank-2 route reaches a new signature only after a *reduction* (to `(p,p,p)`, `(n,n,2)`,
`(n,n,3)`, …) that pushes the large exponent out of the monodromy data. -/

/-- The totient bound behind the rank-2 restriction: a primitive `x`-th root of unity lies in a
field of degree `φ(x)`, so rank `2` over `Q` needs `φ(x) ≤ 2`. -/
theorem totient_le_two_of_rank_two (x : ℕ) (hx : x ≤ 30) (h : Nat.totient x ≤ 2) :
    x = 0 ∨ x = 1 ∨ x = 2 ∨ x = 3 ∨ x = 4 ∨ x = 6 := by
  interval_cases x <;> revert h <;> decide

/-! ### Enlarging the field: the degree grows linearly in the exponent (U259, pool C126)

Face 3 restricted rank `2` **over ℚ** to exponents `3, 4, 6`.  Over a number field `F` of degree
`d` the same argument gives `φ(x) ≤ 2d`: the eigenvalue ratio is a primitive `x`-th root of unity,
`ℚ(ζ_x) ⊆ F(ζ_x)`, and `[F(ζ_x) : ℚ] ≤ 2d`.  So

    d ≥ φ(x)/2,

and for `x = p` an odd prime, `d ≥ (p-1)/2`.

That bound is **sharp**, and it is exactly the shape of the literature: `(p-1)/2` is the degree of
`ℚ(ζ_p)⁺ = ℚ(ζ_p + ζ_p⁻¹)`, the field over which Darmon's Frey abelian varieties for signature
`(p,p,r)` are built.  So the base field cannot stay bounded as the exponent grows: **no rank-2
route can be uniform in `p`**, and the objects one must control get harder at a linear rate.
This is the fourth face of the same obstruction. -/

/-- Minimal base-field degree for a rank-2 object carrying a monodromy of order `x`: `2d ≥ φ(x)`. -/
def minBaseDegree (x : ℕ) : ℕ := (Nat.totient x + 1) / 2

/-- For an odd prime `p`, the bound is `(p-1)/2`, the degree of the maximal real subfield of the
`p`-th cyclotomic field. -/
theorem minBaseDegree_prime {p : ℕ} (hp : p.Prime) (hodd : p % 2 = 1) :
    minBaseDegree p = (p - 1) / 2 := by
  unfold minBaseDegree
  rw [Nat.totient_prime hp]
  have h2 : 2 ≤ p := hp.two_le
  omega

/-! ### Three exponents at once: the degree is multiplicative (U260, pool C127)

Face 4 bounded the degree for ONE monodromy order.  A rank-2 object carrying **all three** orders
`x, y, z` needs `ℚ(ζ_x), ℚ(ζ_y), ℚ(ζ_z)` simultaneously, hence `ℚ(ζ_L)` with `L = lcm(x,y,z)`,
inside a field of degree `2d`.  So

    d ≥ φ(lcm(x,y,z)) / 2 ,

and for three **distinct** odd primes `p, q, r` that is `(p-1)(q-1)(r-1)/2` — *multiplicative* in
the exponents, not linear.

Concretely: `(3,5,7)` needs `d ≥ 24`, `(4,5,7)` needs `24`, `(5,7,11)` needs `120`,
`(7,11,13)` needs `360`.  Compare the single-exponent bound of Face 4, which for those same
signatures is only `3, 3, 5, 6`.

This is the quantitative core of the whole obstruction.  The equal-exponent case `(p,p,r)` costs
`(p-1)(r-1)/2`, already multiplicative, which is why even Darmon's program is stated one signature
at a time; three *independent* exponents multiply one factor more. -/

/-- Minimal base-field degree for a rank-2 object carrying all three monodromy orders. -/
def minBaseDegreeTriple (x y z : ℕ) : ℕ := (Nat.totient (Nat.lcm x (Nat.lcm y z)) + 1) / 2

/-- The triple bound dominates each single-exponent bound, since `x ∣ lcm x (lcm y z)`. -/
theorem minBaseDegree_le_triple (x y z : ℕ) (hx : 0 < x) (hy : 0 < y) (hz : 0 < z) :
    Nat.totient x ≤ Nat.totient (Nat.lcm x (Nat.lcm y z)) :=
  Nat.le_of_dvd (Nat.totient_pos.mpr (Nat.lcm_pos hx (Nat.lcm_pos hy hz)))
    (Nat.totient_dvd_of_dvd (Nat.dvd_lcm_left x (Nat.lcm y z)))

/-! ### Sharpest form: a rigid object carries at most TWO exponents (U261, pool C128)

Call a puncture *full* if its local monodromy is regular semisimple, i.e. has `n` distinct
eigenvalues — the state that can carry a whole exponent.  Then for `n ≥ 3`:

* **at most two** punctures are full, and
* when exactly two are, the third has **exactly 2** distinct eigenvalues.

The counting proof is immediate from Face 2: two full punctures already consume `2n` of the
`2n+2` budget, leaving at most `2` for the third; three would need `3n`, and `3n > 2n+2` exactly
when `n > 2`.  Verified by exhaustive enumeration for `3 ≤ n ≤ 12`
(`code/U261_two_of_three.py`), where the maximum number of full punctures is `2` in every rank
and the third puncture always has exactly `2`.

This is the obstruction in its sharpest form: **two exponents fit, the third does not.**  It is
exactly why the literature proceeds by reductions — `(p,p,r)`, `(n,n,2)`, `(n,n,3)`, `(2,3,n)` —
each of which has at most two independent exponents to carry. -/

/-- `3n > 2n + 2` exactly when `n > 2`: three full punctures overflow the rigid budget. -/
theorem three_full_exceeds_budget (n : ℤ) : 2 < n → 2 * n + 2 < 3 * n := by
  intro h; linarith

/-- Two full punctures leave at most `2` of the budget for the third. -/
theorem two_full_leaves_two (n : ℤ) : (2 * n + 2) - 2 * n = 2 := by ring

/-! ### The two live directions cost the same number (U269, pool C137)

For two **distinct primes** `p, q` the minimal base-field degree of Face 5, `φ(pq)/2`, equals the
genus `(p-1)(q-1)/2` of the Darmon–Granville pair-curve `u^p + v^q = 1`.  The modular cost and the
geometric cost of a pair of exponents are the same integer, so the survey's two live directions
meet the same barrier at the same size: `(3,5,7)` gives `4, 12, 6` on both sides.

The identity is about `φ`, not about `p-1`, so it holds **only** for prime exponents: `φ(4·5)/2 = 4`
while `(4-1)(5-1)/2 = 6`. -/

/-- For distinct primes, `φ(p·q) = (p-1)(q-1)`. -/
theorem totient_mul_primes {p q : ℕ} (hp : p.Prime) (hq : q.Prime) (hne : p ≠ q) :
    Nat.totient (p * q) = (p - 1) * (q - 1) := by
  rw [Nat.totient_mul ((Nat.coprime_primes hp hq).mpr hne), Nat.totient_prime hp,
    Nat.totient_prime hq]

/-! ### The corrected obstruction: rationality, not rigidity (U310, pool C170)

U309 showed rigidity alone does not forbid three pairwise distinct exponents.  U310 then tested
definability over `ℚ`.  A local system defined over `ℚ` has local characteristic polynomials in
`ℚ[T]`, so each eigenvalue multiset is stable under `Gal(ℚ(ζₘ)/ℚ)`: it is a choice of one
multiplicity `c d` per divisor `d ∣ m`, applied to all `φ d` primitive `d`-th roots at once, and
the monodromy has order exactly `m` precisely when `c m ≥ 1`.

The theorem below is the consequence that matters: **a `ℚ`-rational local monodromy of order `m`
forces rank at least `φ m`.**  Exact computation in `code/U310_galois_stable_rigid.py` shows this
bound is attained for every reduced exponent up to `19`.

This does **not** restore the withdrawn U258 headline.  Rigid `ℚ`-rational triples with three
pairwise distinct orders do exist — the smallest is rank `4`, orders `(3,4,5)`, partitions
`((2,1,1),(2,2),(1⁴))`, with `rig = -16 + 6 + 8 + 4 = 2`.  What the bound gives is a *uniformity*
obstruction rather than an existence one: the rank grows at least like `φ` of the largest
exponent, so no single object of bounded rank can carry unboundedly many exponents. -/

/-- **Rank is at least the totient of the order, over `ℚ`.**  If a Galois-stable eigenvalue
multiset assigns multiplicity `c d` to each of the `φ d` primitive `d`-th roots of unity, and the
monodromy has order exactly `m` (so `c m ≥ 1`), then the rank `∑_{d ∣ m} φ d * c d` is at least
`φ m`.  The primitive `m`-th roots alone already contribute that much. -/
theorem rank_ge_totient {m : ℕ} (hm : m ≠ 0) (c : ℕ → ℕ) (hc : 1 ≤ c m) :
    Nat.totient m ≤ ∑ d ∈ m.divisors, Nat.totient d * c d := by
  have hmem : m ∈ m.divisors := Nat.mem_divisors_self m hm
  calc Nat.totient m = Nat.totient m * 1 := by ring
    _ ≤ Nat.totient m * c m := Nat.mul_le_mul_left _ hc
    _ ≤ ∑ d ∈ m.divisors, Nat.totient d * c d :=
        Finset.single_le_sum (f := fun d => Nat.totient d * c d) (fun i _ => Nat.zero_le _) hmem

/-- The smallest rigid `ℚ`-rational triple with three pairwise distinct reduced exponents:
rank `4`, orders `(3,4,5)`, partitions `((2,1,1),(2,2),(1,1,1,1))`.  Its rigidity index is `2`,
so U258's headline claim really does fail. -/
theorem smallest_rational_rigid_witness :
    rigidityIndex 4 ((2 ^ 2 + 1 + 1) + (2 ^ 2 + 2 ^ 2) + (1 + 1 + 1 + 1)) = 2 := by
  unfold rigidityIndex; norm_num

/-! ### A second obstruction: the object is never regular (U317, pool C174)

C171 recorded automorphy as the one missing input for the three-exponent route.  That understates
it.  The potential-automorphy theorems available in rank `> 2` require the representation to be
**regular** — distinct Hodge–Tate weights — which for a local system on `P¹ ∖ {0,1,∞}` means the
monodromies at `0` and `∞` are regular semisimple, partition `(1ⁿ)`.

Those two punctures then contribute `n + n` to the rigidity budget, so `rig = 2` forces the third
to contribute `n² - 2n + 2`, which for `n ≥ 3` is the pseudoreflection `(n-1, 1)`.  And a
pseudoreflection is `ℚ`-rational only if its one non-trivial eigenvalue lies in `ℚ` — that is, only
if `φ(m) = 1`, so `m ≤ 2`, which the Beal exponent range excludes.

Exhaustive check in `code/U317_regularity_obstruction.py`: of **792** rigid `ℚ`-rational triples
with three pairwise distinct reduced exponents at ranks `2 … 14`, **none** is regular at both `0`
and `∞`, and `(n-1,1)` is `ℚ`-rational for **no** reduced exponent at any rank `3 … 8`.

Essential self-duality, by contrast, is free: a Galois orbit over `ℚ` is closed under
`α ↦ α⁻¹` since `-1` is coprime to `m`.  Only regularity bites.

The two arithmetic facts are below.  The step from "local system defined over `ℚ`" to the
combinatorial model of Galois-stable multiplicity vectors is standard and is **not** formalised
here, so this is an obstruction made precise, not a theorem about Beal. -/

/-- **Regularity forces the pseudoreflection budget.**  If two punctures are regular semisimple,
each contributing `n` to the sum of squares, rigidity fixes the third puncture's contribution at
`n² - 2n + 2` — the value attained by `(n-1, 1)`. -/
theorem regular_forces_pseudoreflection (n s : ℤ) :
    rigidityIndex n (n + n + s) = 2 ↔ s = n ^ 2 - 2 * n + 2 := by
  unfold rigidityIndex; constructor <;> intro h <;> linarith

/-- The pseudoreflection's budget is exactly what `(n-1, 1)` contributes. -/
theorem pseudoreflection_budget (n : ℤ) : (n - 1) ^ 2 + 1 = n ^ 2 - 2 * n + 2 := by ring

/-- **A `ℚ`-rational pseudoreflection has order at most `2`.**  Its non-trivial eigenvalue is a
single primitive `m`-th root of unity with multiplicity `1`; Galois-stability makes the whole orbit
share that multiplicity, so the orbit has size `1`, i.e. `φ m = 1`.  Beal exponents are `≥ 3`, so
no pseudoreflection is available. -/
theorem rational_pseudoreflection_order_le_two {m : ℕ} (h : Nat.totient m = 1) : m = 1 ∨ m = 2 :=
  Nat.totient_eq_one_iff.mp h

/-- Consequently no reduced Beal exponent admits a `ℚ`-rational pseudoreflection. -/
theorem no_rational_pseudoreflection_for_exponent {m : ℕ} (hm : 3 ≤ m) : Nat.totient m ≠ 1 := by
  intro h
  rcases rational_pseudoreflection_order_le_two h with rfl | rfl <;> omega

/-! ### The regularity obstruction does not depend on rigidity (U318, pool C175)

C174 listed non-rigid families as its first escape: dropping `rig = 2` costs a moduli of dimension
`(n-1)(n-2)` but also removes the constraint that forced the pseudoreflection.  The escape
**closes**, and rigidity turns out to play no part in the obstruction at all.

Regular semisimple at a puncture means partition `(1ⁿ)`: every multiplicity is `1`.  Over `ℚ` the
eigenvalue multiset is a union of Galois orbits with equal multiplicities inside each orbit, so
with all multiplicities `1` it is a union of **whole** orbits taken once, and

    n = ∑ φ(d) over a set of divisors of m containing m.

Hence `φ(m) ≤ n ≤ ∑_{d ∣ m} φ(d) = m`, i.e. `n ∈ [φ(m), m]` — a constraint using no rigidity.
For three pairwise distinct reduced exponents `p < q < r` these intervals cannot meet: `r` must be
an odd prime (if `r = 4` there is only one smaller reduced exponent), so `φ(r) = r - 1 ≥ p + 1 > p`,
while `n ≤ p` from the smallest.  Exhaustive confirmation in
`code/U318_regularity_without_rigidity.py`: **all 165** pairwise-distinct triples from
`{3,4,5,7,11,13,17,19,23,29,31}` give an empty rank set, while the controls `(p,p,p)` and the mixed
`(3,3,4)`, `(4,4,5)` are non-empty, so the test is not vacuous.

Combined with C174: over `ℚ`, regular Hodge–Tate weights and three pairwise distinct Beal exponents
are incompatible for **any** local system on the thrice-punctured line, rigid or not.

**Scope correction (U319, pool C176): this is a statement about `ℚ` only.**  Over a number field `K`
the orbits of primitive `m`-th roots have size `φ(m) / [K ∩ ℚ(ζₘ) : ℚ]`, so the admissible rank
interval widens, and reconciling the largest exponent with the smallest one's ceiling needs only
`[K:ℚ] ≥ φ(r)/p` — which is between `2` and `6` for every pairwise distinct triple of reduced
exponents up to `19`.  The escape is real and cheap, and the obstruction must not be quoted as
field-independent.  What it does not do is give a route: over `K` the method still needs automorphy
in rank `> 2` over `K`, which is harder than over `ℚ`.  Still not a theorem about Beal. -/

theorem regular_rank_upper (m : ℕ) : ∑ d ∈ m.divisors, Nat.totient d = m := Nat.sum_totient m

theorem regular_rank_lower {m n : ℕ} (hm : m ≠ 0) (c : ℕ → ℕ) (hc : 1 ≤ c m)
    (hn : n = ∑ d ∈ m.divisors, Nat.totient d * c d) : Nat.totient m ≤ n := by
  subst hn
  have hmem : m ∈ m.divisors := Nat.mem_divisors_self m hm
  calc Nat.totient m = Nat.totient m * 1 := by ring
    _ ≤ Nat.totient m * c m := Nat.mul_le_mul_left _ hc
    _ ≤ _ := Finset.single_le_sum (f := fun d => Nat.totient d * c d)
        (fun i _ => Nat.zero_le _) hmem

theorem no_common_regular_rank {p r n : ℕ} (hrp : r.Prime) (hodd : r % 2 = 1)
    (hpr : p + 2 ≤ r) (hle : n ≤ p) (hge : Nat.totient r ≤ n) : False := by
  rw [Nat.totient_prime hrp] at hge
  omega

end Beal
