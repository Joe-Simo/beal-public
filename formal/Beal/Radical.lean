/-
# An unconditional, exponent-2-sensitive necessary condition (U226, pool C092)

Every Beal counterexample satisfies

    rad(A·B·C)³ ≤ A^x · B^y · C^z ,

where `rad n` is the product of the distinct primes dividing `n`.  The proof is three lines: the
radical divides its argument, and `x, y, z ≥ 3` upgrades `(ABC)³` to `A^x B^y C^z`.

The **blindness test** (`code/U141_countersearch_fc.py`, `code/U222_radical_sharp.py`) puts it
above the fourteen blind kernel conditions of U141: the ten Fermat–Catalan solutions all have an
exponent equal to `2`, and the condition **fails** on four of them — the witness
`2^7 + 17^3 = 71^2` is formalised below as
`radical_cube_fails_on_fermat_catalan_2_7_17_3_71_2`.

But the countersearch in the last section of this file (U228, pool C092 addendum) corrects an
overstatement: passing the blindness test does **not** make the condition independent arithmetic
content.  Its proof uses only `rad n ∣ n` and `A^3 ≤ A^x`, never the equation, so it is a strictly
weaker consequence of the exponent hypothesis — the same status as `|χ| ≥ 1/12`.  The four
failures are a size accident: `2^5 + 7^2 = 3^4` has an exponent `2` and satisfies it anyway.

It is **not** a route to a proof.  Turning it into a contradiction requires a lower bound on
`rad(abc)` relative to `c`, which is the abc conjecture; the bound available here,
`rad(abc) ≤ C^z / 4^(1/3)`, gives an abc-quality lower bound tending to `1` and is vacuous
(pool candidate C088, `REFUTED`).

No `sorry`, no custom `axiom`s; mathlib only.
-/
import Beal.Conjecture
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Tactic.NormNum.Prime
import Mathlib.Tactic.Ring

namespace Beal

open Finset

/-- `rad n` is the product of the distinct primes dividing `n` (the *radical*, or squarefree
kernel).  `rad 0 = rad 1 = 1`. -/
def rad (n : ℕ) : ℕ := ∏ p ∈ n.primeFactors, p

/-- The radical divides its argument. -/
theorem rad_dvd (n : ℕ) : rad n ∣ n := Nat.prod_primeFactors_dvd n

/-- The radical is at most its argument, for positive `n`. -/
theorem rad_le (n : ℕ) (hn : 0 < n) : rad n ≤ n := Nat.le_of_dvd hn (rad_dvd n)

/-- For `1 ≤ A` and `3 ≤ x`, `A ^ 3 ≤ A ^ x`. -/
theorem pow_three_le_pow (A x : ℕ) (hA : 1 ≤ A) (hx : 3 ≤ x) : A ^ 3 ≤ A ^ x :=
  Nat.pow_le_pow_right hA hx

/-- **Unconditional necessary condition.**  In every Beal counterexample,

    rad(A·B·C)³ ≤ A^x · B^y · C^z.

Only `A, B, C > 0` and `x, y, z ≥ 3` are used; the coprimality hypothesis is not needed. -/
theorem radical_cube_le {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    (rad (A * B * C)) ^ 3 ≤ A ^ x * B ^ y * C ^ z := by
  obtain ⟨hA, hB, hC, hx, hy, hz, -, -⟩ := h
  have hpos : 0 < A * B * C := by positivity
  have h1 : rad (A * B * C) ≤ A * B * C := rad_le _ hpos
  calc (rad (A * B * C)) ^ 3 ≤ (A * B * C) ^ 3 := Nat.pow_le_pow_left h1 3
    _ = A ^ 3 * B ^ 3 * C ^ 3 := by rw [Nat.mul_pow, Nat.mul_pow]
    _ ≤ A ^ x * B ^ y * C ^ z := by
        have ha : A ^ 3 ≤ A ^ x := pow_three_le_pow A x hA hx
        have hb : B ^ 3 ≤ B ^ y := pow_three_le_pow B y hB hy
        have hc : C ^ 3 ≤ C ^ z := pow_three_le_pow C z hC hz
        exact Nat.mul_le_mul (Nat.mul_le_mul ha hb) hc

/-- **The condition is not exponent-2-blind.**  The Fermat–Catalan solution
`2^7 + 17^3 = 71^2` is coprime and has all the shape of a counterexample except that one exponent
is `2`; it **violates** `radical_cube_le`.  Hence the condition above genuinely uses `x, y, z ≥ 3`
and is not a restatement of a fact about arbitrary coprime triples `a + b = c`. -/
theorem radical_cube_fails_on_fermat_catalan_2_7_17_3_71_2 :
    2 ^ 7 + 17 ^ 3 = 71 ^ 2 ∧ ¬ (rad (2 * 17 * 71)) ^ 3 ≤ 2 ^ 7 * 17 ^ 3 * 71 ^ 2 := by
  constructor
  · norm_num
  · have h2 : Nat.Prime 2 := Nat.prime_two
    have h17 : Nat.Prime 17 := by norm_num
    have h71 : Nat.Prime 71 := by norm_num
    have hrad : rad (2 * 17 * 71) = 2414 := by
      have hsplit : (2 * 17 * 71 : ℕ) = 2 * (17 * 71) := by ring
      unfold rad
      rw [hsplit, Nat.primeFactors_mul (by norm_num) (by norm_num),
          Nat.primeFactors_mul (by norm_num) (by norm_num),
          h2.primeFactors, h17.primeFactors, h71.primeFactors]
      decide
    rw [hrad]
    norm_num

/-! ## The sharpened form, in terms of `C^z` alone

`rad(ABC) ≤ ABC` combines with `A^x ≤ C^z`, `B^y ≤ C^z` to give an inequality whose exponents are
the Beal exponents themselves.  Writing `c = C^z`, the real-analytic reading is
`log c / log rad(abc) ≥ 1 / (1/x + 1/y + 1/z)`.

Unlike `radical_cube_le`, the *raw inequality* below holds on all ten Fermat–Catalan solutions, so
it is blind on its own; the exponent-2 sensitivity lives in the derived quality floor
`1/(1/x+1/y+1/z)`, which is `≥ 1` exactly when `x, y, z ≥ 3` and `< 1` as soon as an exponent is
`2` (verified numerically in `code/U227_sharp_radical.py`).  It is still not a proof route: no
unconditional upper bound on abc-quality is known. -/

/-- Each summand is at most `C^z`. -/
theorem pow_le_target {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    A ^ x ≤ C ^ z ∧ B ^ y ≤ C ^ z := by
  obtain ⟨hA, hB, -, -, -, -, -, heq⟩ := h
  have ha : 1 ≤ A ^ x := Nat.one_le_pow _ _ hA
  have hb : 1 ≤ B ^ y := Nat.one_le_pow _ _ hB
  omega

/-- **Sharpened unconditional bound.**  In every Beal counterexample,

    rad(A·B·C) ^ (x·y·z) ≤ (C^z) ^ (y·z + x·z + x·y).

Dividing logarithms, this is `log C^z / log rad ≥ 1/(1/x + 1/y + 1/z)`. -/
theorem radical_pow_le {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    (rad (A * B * C)) ^ (x * y * z) ≤ (C ^ z) ^ (y * z + x * z + x * y) := by
  have hA := h.1
  have hB := h.2.1
  have hC := h.2.2.1
  have hpos : 0 < A * B * C := by positivity
  have h1 : rad (A * B * C) ≤ A * B * C := rad_le _ hpos
  obtain ⟨hax, hby⟩ := pow_le_target h
  have hsplit : (A * B * C) ^ (x * y * z)
      = (A ^ x) ^ (y * z) * ((B ^ y) ^ (x * z) * (C ^ z) ^ (x * y)) := by
    have e1 : (A ^ x) ^ (y * z) = A ^ (x * y * z) := by
      rw [← Nat.pow_mul]; congr 1; ring
    have e2 : (B ^ y) ^ (x * z) = B ^ (x * y * z) := by
      rw [← Nat.pow_mul]; congr 1; ring
    have e3 : (C ^ z) ^ (x * y) = C ^ (x * y * z) := by
      rw [← Nat.pow_mul]; congr 1; ring
    rw [Nat.mul_pow, Nat.mul_pow, e1, e2, e3, Nat.mul_assoc]
  calc (rad (A * B * C)) ^ (x * y * z) ≤ (A * B * C) ^ (x * y * z) :=
        Nat.pow_le_pow_left h1 _
    _ = (A ^ x) ^ (y * z) * ((B ^ y) ^ (x * z) * (C ^ z) ^ (x * y)) := hsplit
    _ ≤ (C ^ z) ^ (y * z) * ((C ^ z) ^ (x * z) * (C ^ z) ^ (x * y)) :=
        Nat.mul_le_mul (Nat.pow_le_pow_left hax _)
          (Nat.mul_le_mul (Nat.pow_le_pow_left hby _) le_rfl)
    _ = (C ^ z) ^ (y * z + x * z + x * y) := by
        rw [← Nat.pow_add, ← Nat.pow_add]; ring_nf

/-! ## Countersearch (U228): what the cube condition actually contains

`radical_cube_le` is **not** independent arithmetic content.  Its proof uses only two facts —
`rad n ∣ n` and `A ^ 3 ≤ A ^ x` for `x ≥ 3` — so it is a strictly weaker *consequence* of the
exponent hypothesis, not an extra constraint derived from the equation.  The lemma below makes
that explicit in the squarefree case, where `rad (A*B*C) = A*B*C` and the condition collapses to
`A^3 B^3 C^3 ≤ A^x B^y C^z`.

It fails on four of the ten Fermat–Catalan solutions, but that is a size accident rather than
arithmetic: `2^5 + 7^2 = 3^4` has an exponent `2` and still satisfies it.  Compare `|χ| ≥ 1/12`,
which is likewise the exponent hypothesis restated. -/

/-- For a squarefree product of bases the radical is the product itself, so the cube condition is
equivalent to the plain inequality `A^3 B^3 C^3 ≤ A^x B^y C^z`. -/
theorem radical_cube_iff_of_rad_eq {A B C x y z : ℕ} (hsf : rad (A * B * C) = A * B * C) :
    (rad (A * B * C)) ^ 3 ≤ A ^ x * B ^ y * C ^ z ↔ A ^ 3 * B ^ 3 * C ^ 3 ≤ A ^ x * B ^ y * C ^ z := by
  rw [hsf, Nat.mul_pow, Nat.mul_pow]

end Beal
