# U113: Exponent Reduction — machine-checked in Lean 4 + mathlib

**Date**: 2026-09-17
**Status**: **VERIFIED by the Lean kernel.** First machine-checked result in this project.
**Source**: [`formal/Beal/ExponentReduction.lean`](../../formal/Beal/ExponentReduction.lean)
**Exact computation**: [`code/U113_exponent_reduction.py`](../../code/U113_exponent_reduction.py)

## Statement

```lean
def IsBealCounterexample (A B C x y z : ℕ) : Prop :=
  0 < A ∧ 0 < B ∧ 0 < C ∧ 3 ≤ x ∧ 3 ≤ y ∧ 3 ≤ z ∧
    A ^ x + B ^ y = C ^ z ∧ Nat.gcd (Nat.gcd A B) C = 1

def Reduced (e : ℕ) : Prop := e = 4 ∨ (Nat.Prime e ∧ Odd e)

theorem reduction {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    ∃ A' B' C' x' y' z' : ℕ,
      IsBealCounterexample A' B' C' x' y' z' ∧ Reduced x' ∧ Reduced y' ∧ Reduced z'
```

In words: **if a Beal counterexample exists at all, one exists whose three exponents each lie in
`{4} ∪ {odd primes}`.** Hence refuting those signatures suffices.

Note the definition encodes the conjecture faithfully: six positive integers, all three exponents
`≥ 3` (exponent 2 excluded), exact equality, the coprimality condition on the **bases**, and bases
equal to 1 permitted.

## Verification

```
$ lake build Beal.ExponentReduction
✔ [892/892] Built Beal.ExponentReduction
Build completed successfully.

$ #print axioms Beal.reduction
'Beal.reduction' depends on axioms: [propext, Classical.choice, Quot.sound]
'Beal.exists_reduced_factor' depends on axioms: [propext, Classical.choice, Quot.sound]
'Beal.gcd_pow_eq_one' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Only the three standard Lean axioms. **No `sorry`, no custom axioms, no project-specific
assumptions.** Environment: Lean 4.14.0 (arm64-apple-darwin, commit 410fab728470), mathlib v4.14.0.

## Why it was needed

The project's own discipline forbids restricting the exponent range without proving the restriction
covers every case. Every signature-by-signature result in this repository — `(3,3,p)`, `(5,5,p)`,
`(2,4,n)`, the all-even branch — tacitly assumes this reduction. It had never been proved.

## The two steps that required care

1. **Powers of two.** An exponent `e ≥ 3` that is a power of 2 satisfies `e ≥ 4`, hence `4 ∣ e`.
   Proved without `Nat.factorization`: the least prime factor of `e` cannot be odd (hypothesis), so
   it is 2; writing `e = 2t`, the least prime factor of `t` cannot be odd either, so `2 ∣ t`.

2. **Primitivity is preserved.** `gcd_pow_eq_one`: if `gcd (gcd A B) C = 1` then
   `gcd (gcd (A^a) (B^b)) (C^c) = 1`. A prime dividing `A ^ a` divides `A`, so any common prime
   divisor of the powers is a common prime divisor of the bases. This is the step that must not be
   waved through — the reduction would be worthless if it could turn an imprimitive solution into a
   primitive one.

Independently cross-checked by exact computation: 6,655 cases with the equation and primitivity
preserved in every one, and a countersearch confirming primitivity is never *created*
(0 of 24,389 imprimitive triples became primitive under `q ↦ q^m`).

## Consequence for coverage

After reduction every exponent lies in `{4} ∪ {3,5,7,11,13,…}`, and
`1/x + 1/y + 1/z ≤ 1` always, with equality **only** at `(3,3,3)` (the Fermat cubic, exact integer
comparison `27/27`). Every other reduced Beal signature is hyperbolic.

## What this does NOT establish

It does not resolve any signature, and it does not bear on Beal's conjecture itself. It makes the
signature-by-signature *strategy* legitimate, which it previously was not.

---

# Part II: An infinite family of Beal signatures, kernel-verified

**Added**: 2026-09-17. Same file, same verification standard.

mathlib v4.14.0 contains a complete `fermatLastTheoremFour : FermatLastTheoremFor 4`.
(It does **not** contain a complete FLT for exponent 3 — `FLT/Three.lean` has only
`fermatLastTheoremThree_case_1` and `fermatLastTheoremThree_of_three_dvd_only_c`, so the
project's `flt_3` axiom cannot yet be discharged from this mathlib version.)

```lean
theorem no_counterexample_diagonal_of_four_dvd {n : ℕ} (hn : 4 ∣ n)
    {A B C : ℕ} (h : IsBealCounterexample A B C n n n) : False
```

**For every `n` divisible by 4, the diagonal signature `(n,n,n)` admits no Beal counterexample.**
A counterexample would give `(A^m)^4 + (B^m)^4 = (C^m)^4` with all three nonzero, contradicting
`fermatLastTheoremFour`. Instances `no_counterexample_4_4_4` and `no_counterexample_8_8_8` are
included.

Note the result needs no coprimality hypothesis at all — it refutes the equation outright, which
is strictly stronger than refuting a *primitive* solution.

## Verification

```
$ lake build Beal.ExponentReduction
✔ [1180/1180] Built Beal.ExponentReduction
Build completed successfully.

$ #print axioms
'Beal.reduction'                             : [propext, Classical.choice, Quot.sound]
'Beal.no_counterexample_diagonal_of_four_dvd': [propext, Classical.choice, Quot.sound]
'Beal.no_counterexample_4_4_4'               : [propext, Classical.choice, Quot.sound]
'Beal.no_counterexample_8_8_8'               : [propext, Classical.choice, Quot.sound]
```

No `sorry`, no custom axioms, in this file or in its dependency chain.

## Significance and limits

This is the first **infinite family** of Beal signatures closed with machine verification in this
project, and it is closed unconditionally — no GRH, no finiteness of Sha, no heuristic, no
unverified citation. It supersedes `Signature4.lean`, whose `fermat_4_2` is a bare `sorry` that
`fermat_4_4` then depends on.

The limit is real and should not be oversold: `{(n,n,n) : 4 ∣ n}` is a measure-zero corner of the
Beal exponent space. It says nothing about any non-diagonal signature, and the bulk of the
conjecture is untouched.

---

# Part III: Elementary structure of a counterexample, kernel-verified

**Source**: [`formal/Beal/Structure.lean`](../../formal/Beal/Structure.lean)
**Selection**: candidate lemmas were triaged by Jev (`code/U113_lemma_triage.py`) on truth,
elementarity and structural value before any Lean effort was spent.

```lean
theorem gcd_ab_eq_one : IsBealCounterexample A B C x y z → Nat.gcd A B = 1
theorem gcd_ac_eq_one : IsBealCounterexample A B C x y z → Nat.gcd A C = 1
theorem gcd_bc_eq_one : IsBealCounterexample A B C x y z → Nat.gcd B C = 1
theorem not_eq_bases  : IsBealCounterexample A A C x y z → False
theorem not_both_one  : IsBealCounterexample 1 1 C x y z → False
```

**The bases of a Beal counterexample are pairwise coprime**, and **no counterexample has `A = B`**.
The Beal hypothesis is only `gcd (gcd A B) C = 1`; pairwise coprimality is a consequence, not an
assumption, and it is used tacitly throughout this project's checkpoints without ever having been
proved here.

`not_eq_bases` follows because pairwise coprimality forces `A = gcd A A = 1`, so the equation reads
`1 + 1 = C^z` with `z ≥ 3`, and `2` is not a perfect power of exponent `≥ 3` (proved as a private
lemma by the bound `8 = 2^3 ≤ 2^z ≤ C^z`).

## Verification

```
$ lake build Beal.Structure
✔ [1181/1181] Built Beal.Structure

$ #print axioms
'Beal.gcd_ab_eq_one': [propext, Classical.choice, Quot.sound]
'Beal.gcd_ac_eq_one': [propext, Classical.choice, Quot.sound]
'Beal.gcd_bc_eq_one': [propext, Classical.choice, Quot.sound]
'Beal.not_eq_bases' : [propext, Classical.choice, Quot.sound]
'Beal.not_both_one' : [propext, Classical.choice, Quot.sound]
```

## A false lemma caught before any effort was spent

The triage also considered *"in any Beal counterexample exactly one of `A`, `B` is even and `C` is
odd"*. Jev scored its truth at 0.71 — the lowest of the eight candidates — and it is indeed
**false as stated**: `A` and `B` may both be odd, forcing `C` even, which contradicts nothing,
since the Beal hypothesis does not require `C` odd. It was dropped before any Lean time was spent.
The two candidates needing deep external input (Mihailescu for `A = 1`, FLT3 for the `3 ∣ n`
diagonal family) were correctly scored non-elementary at 0.10 and 0.06 and left for later.

## Limits

These are structural constraints on a hypothetical counterexample, not the elimination of any
signature. They narrow the search space and remove assumptions that were previously used without
proof; they do not bear on whether a counterexample exists.

---

# Part IV: A non-diagonal infinite family, kernel-verified

**Source**: `formal/Beal/Structure.lean`
**Selection**: Jev repair-triage (`code/U113_repair_triage.py`) ranked `Signature4` the best of nine
broken modules (value 1.92, repairable 0.71) while correctly scoring `Signature238` (0.07),
`Mihailescu` (0.05) and `Signature3` (0.12) as unrepairable without custom axioms — mathlib has
neither FLT3 nor Mihailescu.

Repairing `Signature4` in place proved wasteful (its own helper lemmas do not compile either), so
its one valuable idea was extracted and proved in a strictly more general form.

```lean
theorem no_counterexample_of_four_four_even {A B C x y z : ℕ}
    (hx : 4 ∣ x) (hy : 4 ∣ y) (hz : 2 ∣ z)
    (h : IsBealCounterexample A B C x y z) : False
```

**Whenever `4 ∣ x`, `4 ∣ y` and `z` is even, `A^x + B^y = C^z` has no positive solutions.**
Writing `x = 4a`, `y = 4b`, `z = 2c` gives `(A^a)^4 + (B^b)^4 = (C^c)^2`, forbidden by mathlib's
`not_fermat_42`. No coprimality hypothesis is used, so this refutes the equation outright, not
merely primitive solutions.

This family is **non-diagonal**: the three exponents range independently over `4ℕ`, `4ℕ`, `2ℕ`.
It strictly subsumes the earlier diagonal family `(n,n,n)` with `4 ∣ n`. Instances proved:
`(4,4,2k)` for every `k`, and `(8,12,6)` with all three exponents distinct.

## Verification

```
$ lake build Beal.Structure
Build completed successfully.

$ #print axioms
'Beal.no_counterexample_of_four_four_even': [propext, Classical.choice, Quot.sound]
'Beal.no_counterexample_4_4_two_mul'      : [propext, Classical.choice, Quot.sound]
'Beal.no_counterexample_8_12_6'           : [propext, Classical.choice, Quot.sound]
```

## Limits

Still a thin slice: it requires both `x` and `y` divisible by 4. Under the exponent reduction
theorem, an exponent divisible by 4 reduces to exactly 4, so in reduced terms this handles
signatures `(4,4,z)` with `z` even — while the reduced signatures with an odd prime exponent, which
are the overwhelming majority, are untouched.

---

# Part V: FLT3 family verified — and a correction

## V.1 Correction to Part II

Part II stated that mathlib v4.14.0 "does **not** contain a complete FLT for exponent 3". **That
was wrong.** `theorem fermatLastTheoremThree : FermatLastTheoremFor 3` is present at
`Mathlib/NumberTheory/FLT/Three.lean:757`. The earlier conclusion came from a grep pattern that
failed to match, and silence from a search was treated as a negative result. It is not one.

## V.2 The family

```lean
theorem no_counterexample_of_three_dvd_all {A B C x y z : ℕ}
    (hx : 3 ∣ x) (hy : 3 ∣ y) (hz : 3 ∣ z)
    (h : IsBealCounterexample A B C x y z) : False
```

Verified, together with instances `(3,3,3)`, `(6,9,12)`, and the combined diagonal statement
`no_counterexample_diagonal_of_three_or_four`:

```
$ lake build Beal.Structure
✔ [2628/2629] Built Mathlib.NumberTheory.FLT.Three
✔ [2629/2629] Built Beal.Structure
Build completed successfully.

$ #print axioms
'Beal.no_counterexample_of_three_dvd_all'         : [propext, Classical.choice, Quot.sound]
'Beal.no_counterexample_3_3_3'                    : [propext, Classical.choice, Quot.sound]
'Beal.no_counterexample_6_9_12'                   : [propext, Classical.choice, Quot.sound]
'Beal.no_counterexample_diagonal_of_three_or_four': [propext, Classical.choice, Quot.sound]
'Beal.no_counterexample_of_four_four_even'        : [propext, Classical.choice, Quot.sound]
```

## V.3 Status after the U114 literature check — this is FORMALISATION, not new mathematics

U114 established that $(p,p,p)$ for **all** $p \ge 3$ is Wiles–Taylor, and $(p,p,2)$ for $p \ge 5$
is Darmon–Merel. Every family verified in this file is therefore a **special case of a known
theorem**.

Their value is precise and limited: mathlib contains FLT for exponents 3 and 4 but **not** full
FLT, nor $(p,p,2)$, $(p,p,3)$ or $(2,4,r)$. Machine-checking Beal-shaped consequences of what
mathlib does have is a legitimate formalisation contribution. It is **not** new mathematics and
must never be presented as such.

## V.4 Complete verified inventory

| Theorem | Content |
|---|---|
| `reduction` | exponents reduce to $\{4\} \cup \{\text{odd primes}\}$ |
| `gcd_pow_eq_one` | primitivity survives taking powers of bases |
| `gcd_ab_eq_one`, `gcd_ac_eq_one`, `gcd_bc_eq_one` | bases are pairwise coprime |
| `not_eq_bases`, `not_both_one` | no counterexample with $A = B$ |
| `no_counterexample_of_four_four_even` | $4\mid x$, $4\mid y$, $z$ even |
| `no_counterexample_of_three_dvd_all` | $3\mid x$, $3\mid y$, $3\mid z$ |
| `no_counterexample_diagonal_of_three_or_four` | diagonal $(n,n,n)$, $3\mid n$ or $4\mid n$ |

All depend only on `[propext, Classical.choice, Quot.sound]`. No `sorry`, no custom axioms.

---

# Part VI: The all-even branch is perfect powers in a Pythagorean triple

**Motivation**: U114 Part IV records Freitas's observation that signatures of the form
$(2\ell, 2m, p)$ have Frey curves only over *totally real fields*, not over $\mathbb{Q}$ — which is
exactly why this project's all-even work needs Hilbert modular forms and meets the obstructions of
U113. That prompted asking what the all-even case *is*, structurally. The answer is elementary and
had never been stated here.

```lean
theorem allEven_isPythagorean {A B C r s t : ℕ}
    (h : IsBealCounterexample A B C (2 * r) (2 * s) (2 * t)) :
    (A ^ r) ^ 2 + (B ^ s) ^ 2 = (C ^ t) ^ 2 ∧
      Nat.gcd (Nat.gcd (A ^ r) (B ^ s)) (C ^ t) = 1 ∧
      2 ≤ r ∧ 2 ≤ s ∧ 2 ≤ t ∧ 0 < A ^ r ∧ 0 < B ^ s ∧ 0 < C ^ t

theorem allEven_pairwise_coprime … :
    Nat.gcd (A ^ r) (B ^ s) = 1 ∧ Nat.gcd (A ^ r) (C ^ t) = 1 ∧ Nat.gcd (B ^ s) (C ^ t) = 1
```

**A Beal counterexample with all three exponents even is exactly a primitive Pythagorean triple
whose three entries are perfect powers of exponents $r, s, t \ge 2$.**

The bound $r,s,t \ge 2$ is what gives the statement content: $x \ge 3$ together with $x = 2r$
forces $r \ge 2$, so the triple is $(A^r, B^s, C^t)$ with genuine powers, not $(A,B,C)$ itself.
Primitivity transfers via the verified `gcd_pow_eq_one`, and pairwise coprimality via the verified
`gcd_ab/ac/bc_eq_one`.

Verified, standard axioms only:
```
'Beal.allEven_isPythagorean'    : [propext, Classical.choice, Quot.sound]
'Beal.allEven_pairwise_coprime' : [propext, Classical.choice, Quot.sound]
```
Non-vacuity checked: the instance $(6,10,8) = (2\cdot3, 2\cdot5, 2\cdot4)$ type-checks, giving
$(A^3)^2 + (B^5)^2 = (C^4)^2$.

## Why this is worth recording

Every primitive Pythagorean triple is $(m^2-n^2,\ 2mn,\ m^2+n^2)$ with $\gcd(m,n)=1$ of opposite
parity, so the all-even branch is precisely the question of when all three of those are perfect
powers with exponents $\ge 2$. The case $r = s = 2$ is Fermat's right-triangle theorem, which is
mathlib's `not_fermat_42` and the source of the verified $4\mid x$, $4\mid y$, $z$ even family.

This is a **restatement, not a resolution**: the general problem of perfect powers in Pythagorean
triples is exactly as hard as the all-even branch, and is studied in the literature under
signatures $(2\ell,2m,p)$. It is recorded because it names what the branch actually is, in a
machine-checked form, and because the project's own weighted equation
$X^{10}+256Y^{10}=Z^{17}$ is one particular reduction of it.

---

# Part VII: The consolidated necessary conditions

`formal/Beal/Necessary.lean` assembles every verified constraint into one theorem — the project's
"explicit account of what is proved", in kernel-checked form rather than prose.

```lean
theorem necessary_conditions {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    Nat.gcd A B = 1 ∧ Nat.gcd A C = 1 ∧ Nat.gcd B C = 1 ∧
    A ≠ B ∧
    ¬ (3 ∣ x ∧ 3 ∣ y ∧ 3 ∣ z) ∧
    ¬ (4 ∣ x ∧ 4 ∣ y ∧ 2 ∣ z) ∧
    ¬ (3 ∣ Nat.gcd x (Nat.gcd y z)) ∧ ¬ (4 ∣ Nat.gcd x (Nat.gcd y z))

theorem reduced_counterexample_satisfies_necessary … :
    ∃ A' B' C' x' y' z', IsBealCounterexample A' B' C' x' y' z' ∧
      Reduced x' ∧ Reduced y' ∧ Reduced z' ∧
      Nat.gcd A' B' = 1 ∧ Nat.gcd A' C' = 1 ∧ Nat.gcd B' C' = 1 ∧ A' ≠ B'
```

```
'Beal.necessary_conditions'                      : [propext, Classical.choice, Quot.sound]
'Beal.reduced_counterexample_satisfies_necessary' : [propext, Classical.choice, Quot.sound]
```

**Non-vacuity checked**, each by a *different* clause: `(12,12,12)` falls to the
`gcd` clause, `(9,9,9)` to the all-divisible-by-3 clause, `(8,8,6)` to the `(4,4,even)` clause.
All three instances type-check.

## Why this is the right final artifact

A prose ledger can drift from the proofs it summarises — which is precisely how this repository
came to claim results it did not have. A consolidated theorem cannot: it is checked against the
same kernel as its components, and it names its own dependencies. If a future contributor weakens
any component, this theorem stops compiling.

It also states the practical content plainly: **any search for a Beal counterexample may assume
these conditions, and any claimed counterexample violating one is refuted outright** — without
appeal to anything in this repository beyond the Lean kernel and mathlib.
