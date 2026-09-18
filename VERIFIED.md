# Verified results — Beal conjecture project

**Beal's conjecture is not solved.** This file lists only what is *machine-checked* or
*independently re-verified*, and states plainly what each thing is and is not.

Environment: Lean 4.14.0 (arm64-apple-darwin, commit `410fab728470`) + mathlib v4.14.0.
Every theorem below was checked with `#print axioms` and depends on **no axioms beyond
Lean's standard three** (`propext`, `Classical.choice`, `Quot.sound`). No `sorry`, no custom
axioms anywhere in their dependency chains.

Reproduce:
```bash
cd formal && lake build Beal.Conjecture Beal.ExponentReduction Beal.Structure \
  Beal.Necessary Beal.CounterexampleChecker Beal.Valuation Beal.Taxonomy \
  Beal.KnownSolutions Beal.FermatCatalan Beal.GaussianObstruction \
  Beal.Signature3 Beal.Signature4 Beal.Signature238 Beal.Mihailescu \
  Beal.AlgebraicIdentities
```

**Module status (updated U223–U232, pool C089–C097)**: every module reachable from the root
`Beal.lean` builds, `sorry` count across `formal/` is **0**, and **custom axioms in the root build
chain are now 0** (was 4).

The four external theorems that had been declared as Lean `axiom`s — Mihăilescu, Kraus's level-18
input, Freitas's mod-3 elimination, Bruin's signature-(2,3,8) classification — are now **named
`Prop` hypotheses** (`MihailescuTheorem`, `KrausEvenCLevel18Newform`, `FreitasTheoremMod3`,
`BruinClassification238`), threaded explicitly through every theorem that uses them. Before the
fix, `#print axioms` on `beal_counterexample_bases_ge_two`, `c_must_be_odd` and
`no_beal_counterexample_3_3_5` reported those custom axioms; it now reports only the standard
three. This also means results depending on them are visibly **conditional**, which the header of
`Signature3.lean` had previously presented as established.

**[U339 CORRECTION, pool C195]** The lakefile sets `roots := #[\`Beal]`, so `lake build` builds only
the transitive import closure of `Beal.lean` — **29 of the 33 files**. FOUR are outside the build
entirely, not one as previously stated: `SquarefreeCore.lean`, `Valuation.lean`,
`FermatCatalan.lean` and `GaussianObstruction.lean`. Nothing in them is checked by any build, so
nothing in them may be cited. Only `SquarefreeCore.lean` was named here before; the other three were
not, which overstated the coverage.

`Beal/SquarefreeCore.lean` still declares four `padicValNat` axioms. It does **not** compile and is
**not** imported by the root; the same facts are proved from mathlib in `Beal/Valuation.lean`. A
stale compiled artifact for it was removed so it cannot be imported as though verified.

## The statement, as formalised

```lean
def IsBealCounterexample (A B C x y z : ℕ) : Prop :=
  0 < A ∧ 0 < B ∧ 0 < C ∧ 3 ≤ x ∧ 3 ≤ y ∧ 3 ≤ z ∧
    A ^ x + B ^ y = C ^ z ∧ Nat.gcd (Nat.gcd A B) C = 1
```
Six positive integers; all exponents `≥ 3` (exponent 2 excluded); exact equality; the coprimality
condition on the **bases**; bases equal to 1 permitted.

## The consolidated statement

Everything below is assembled into one machine-checked theorem,
`Beal.necessary_conditions` (`formal/Beal/Necessary.lean`):

> If `(A,B,C,x,y,z)` is a Beal counterexample, then the three bases are **pairwise coprime**,
> `A ≠ B`, the exponents are **not all divisible by 3**, `x` and `y` are **not both divisible by 4
> with `z` even**, and **neither 3 nor 4 divides `gcd(x,y,z)`**.

With `reduced_counterexample_satisfies_necessary`: if a counterexample exists at all, one exists
with every exponent in `{4} ∪ {odd primes}` *and* satisfying all of the above. Any search may
assume these; any claimed counterexample violating one is refuted outright.

Non-vacuity checked: the instances `(12,12,12)`, `(9,9,9)` and `(8,8,6)` are each excluded by a
different clause, and all three type-check.

## Kernel-verified theorems

| Theorem | Statement |
|---|---|
| `reduction` | a counterexample implies one with all exponents in `{4} ∪ {odd primes}` |
| `gcd_pow_eq_one` | primitivity survives raising bases to powers |
| `gcd_ab_eq_one`, `gcd_ac_eq_one`, `gcd_bc_eq_one` | the bases are **pairwise** coprime |
| `not_eq_bases`, `not_both_one` | no counterexample with `A = B` |
| `no_counterexample_of_three_dvd_all` | none with `3 ∣ x`, `3 ∣ y`, `3 ∣ z` |
| `no_counterexample_of_four_four_even` | none with `4 ∣ x`, `4 ∣ y`, `z` even |
| `no_counterexample_of_three_or_four_dvd_gcd` | none when `3 ∣ gcd(x,y,z)` or `4 ∣ gcd(x,y,z)` |
| `no_counterexample_diagonal_of_three_or_four` | none diagonal `(n,n,n)` with `3 ∣ n` or `4 ∣ n` |
| `checkBealNat_sound` / `checkBealNat_complete` | the executable checker is **sound and complete** |
| `beal_parabolic_unique`, `curvature_upper_bound_beal` | $(3,3,3)$ is the unique Euclidean Beal signature; all others have curvature numerator $\le -3$ |
| `not_beal_counterexample_of_exponent_two`, `catalan_not_beal`, `sol_2_7_3_not_beal` | every known Fermat–Catalan solution fails Beal **because it has an exponent 2** |
| `no_beal_counterexample_4_4_even` | signature $(4,4,2k)$, via the project's own descent scaffolding |
| `allEven_isPythagorean` | an all-even counterexample is a primitive Pythagorean triple of perfect powers |
| `factorization_pow_eq` + 3 others | the four `SquarefreeCore` axioms, proved |
| `necessary_conditions` | all verified constraints on a counterexample, in one theorem |
| **`beal_false_over_gaussianInt`** | **Beal is FALSE over `ℤ[i]`** (Helenius): `(-2+i)^3 + (-2-i)^3 = (1+i)^4`, exponents `(3,3,4)`, norms `5,5,2`. Since `ℤ[i]` is a PID, **no proof of Beal can rest on unique factorisation alone**. Depends on `[propext]` alone |
| `fc1`–`fc10`, `fc_all_fail_beal` | the ten known Fermat–Catalan solutions, each verified exactly and each failing Beal **for the same reason — an exponent equal to 2**. So Beal ⟺ "2 is obligatory in the hyperbolic regime" |

## Independently re-verified computations

- **Counterexample checker**: an independent implementation, written from the conjecture statement,
  agrees with `code/section8_counterexample_checker.py` on every required vector *and on the
  discriminating reason*. True-branch reachability proven by mutating only the exponent gate.
- **`disc(f) = 2²⁴·5⁵·Z⁶⁸`** for the weighted Frey polynomial — symbolically and at 5 exact
  specialisations.
- **Orbit `b` ↔ `Jac(C₀)`**: `(S,P) = (9,19), (−11,29), (−1,−151)` at `q = 11, 31, 41` by point
  counting, and `a_q = 0` for every tested `q ≢ 1 mod 5`.
- **Kraus sieve data**: 0 Hasse violations, 0 inconsistencies across 88 repeated `(newform, q)` pairs.

## What these results are NOT

Per [U114](research/checkpoints/U114_literature_state_of_the_art_and_dead_ends.md), the exponent
families above are **special cases of known theorems** — `(p,p,p)` for all `p ≥ 3` is Wiles–Taylor,
`(p,p,2)` for `p ≥ 5` is Darmon–Merel. They are **formalisation** contributions, valuable only
because mathlib lacks full FLT, `(p,p,2)`, `(p,p,3)` and `(2,4,r)`. **They are not new mathematics
and must never be presented as such.**

Signatures with an odd prime exponent `≥ 5` — the overwhelming majority — are untouched. The
smallest open Beal signature is `(3,5,7)`, resolved by Dahmen–Siksek only under divisibility
conditions. The Darmon-program survey states that signatures with minimum exponent three "remain
largely inaccessible through current techniques".

## Corrections issued during this work

See [U113](research/checkpoints/U113_orbit_b_elimination_audit.md) and
[the corrected ledger](research/checkpoints/U113_corrected_coverage_ledger.md). Withdrawn:
the orbit-`b` elimination (U97 **and** U102), the all-even `17 ∣ t` branch, and several
"unconditional" labels that rested on GRH, on finiteness of Ш, or on Cohen–Martinet heuristics.

## U134 — `formal/Beal/EvenEvenThree.lean`

`no_counterexample_even_even_three`: no Beal counterexample of signature (2m, 2n, 3) with m, n ≥ 4,
**relative to three named hypotheses** (ℤ[i] cube step; Bennett–Skinner 2004 Thm 1.1 with C = 3;
BCDY 2015 Thm 1 row (4,2n,3)). Axioms: `[propext, Classical.choice, Quot.sound]`, 0 sorry.
Not an unconditional kernel result; the external theorems are peer-reviewed and quoted from primary
sources in `references/U130/`.

Module build status at U134 (`lake build Beal.<M>` each, Lean 4.14.0 / mathlib v4.14.0):
OK — Conjecture, CounterexampleChecker, AlgebraicIdentities, ExponentReduction, Structure, Necessary,
GaussianObstruction, FermatCatalan, Taxonomy, Signature3, Signature4, Signature238, KnownSolutions,
Mihailescu, EvenEvenThree (15). FAIL — TaxonomyExtensions (pre-existing, tracked, partially repaired
case analysis), SquarefreeCore (untracked, known failing since U113; its import was removed from the
root `Beal.lean`). Nothing in the verified chain depends on either failing module.

## U136 — `formal/Beal/GaussianCube.lean`

`gaussianCubeStep`: the ℤ[i] cube step is now a mathlib theorem (standard axioms, 0 sorry), so
`no_counterexample_even_even_three'` — no Beal counterexample of signature (2m, 2n, 3), m, n ≥ 4 —
depends on exactly two named external hypotheses: Bennett–Skinner 2004 Thm 1.1 (C = 3) and
BCDY 2015 Thm 1 (4, 2n, 3). Module build: 16 OK (GaussianCube added), 2 pre-existing FAIL.

## U139 — `formal/Beal/Residual.lean`

`residual_of_counterexample` / `beal_of_no_residual`: the machine-checked "what remains" — every
counterexample reduces to a `ResidualShape` (exponents in {4} ∪ odd primes; not (4,4,4); not (3,3,3);
exactly one even base; C even ⟹ (x,y) ≠ (4,4); no cancellation; pairwise coprime distinct bases).
Standard axioms, 0 sorry, no external hypotheses. Modules OK: 17.

## U144 — `formal/Beal/GaussianPow.lean`

`gaussian_odd_pow_step`: for odd z, coprime a, b and odd c with a² + b² = c^z, (a, b) is the
real/imaginary part of a z-th power in ℤ[i] with coprime coordinates. Standard axioms, 0 sorry.
Generalises `gaussianCubeStep`; gives the exact reduction behind C045 for every (2m, 2n, z odd).
Modules OK: 18.
`even_even_odd_reduction` (same file): every Beal counterexample of signature (2m, 2n, z), z odd,
is a z-th power in ℤ[i] with coprime coordinates — the C045 reduction, unconditional in the kernel.

## U145 — `formal/Beal/SameOddPrime.lean`

`ppr_factorisation`: for a counterexample of signature (p, p, r), p odd prime, (A+B)·S = C^r with
S = Σ A^i(−B)^{p−1−i} and every common divisor of A+B and S dividing p. Standard axioms, 0 sorry.
Modules OK: 19. Also `ppr_coprime_branch` (p ∤ A+B: both factors are r-th powers) and `ppr_padic_branch` (p | A+B: v_p(A+B)+1 = r·v_p(C), v_p(cofactor) = 1, via mathlib LTE).

## U151 — `formal/Beal/SixTwoNThree.lean`

`no_counterexample_six_two_n_three` ((6, 2n, 3), n ≥ 3) and `no_counterexample_even_even_three_all`
((2m, 2n, 3) for ALL m, n ≥ 2): standard axioms, 0 sorry, relative to three named hypotheses —
`BennettSkinnerThree`, `BCDYFourTwoNThree`, `Mordell27` (y² = x³ + 27 has only O and (−3, 0):
LMFDB 144.a4 rank 0; PARI 2-descent bound 0, output in `references/U130/`). `swap_counterexample`
on `[propext]` alone. Modules OK: 20. Not an unconditional kernel result.

## U154 — `formal/Beal/FourTwoNFive.lean`

`no_counterexample_four_two_n_five` ((4, 2n, 5), n ≥ 2) and `no_counterexample_two_m_four_five`:
standard axioms, 0 sorry, relative to two named hypotheses `Quartic400g2`, `Quartic400b2` (rational
points of two genus-1 quartics; Jacobians LMFDB 400.g2 / 400.b2, rank 0, torsion ℤ/2; PARI 2-descent
bound 0). Congruence obstructions decided in `ZMod 16`. Modules OK: 21. Not an unconditional result.

## U156 — `formal/Beal/ClosedFamilies.lean`

`closed_unconditional` (mathlib only: (4k,4l,2j) and (3k,3l,3j) carry no counterexample) and
`closed_conditional` (under the five named hypotheses `BennettSkinnerThree`, `BCDYFourTwoNThree`,
`Mordell27`, `Quartic400g2`, `Quartic400b2`: no counterexample of signature (2m,2n,3), (4,2n,5) or
(2m,4,5) with m, n ≥ 2) and `closed_conditional_dvd` (the same up to exponent divisibility: no counterexample with 2|x,2|y,3|z, nor 4|x,2|y,5|z, nor 2|x,4|y,5|z). Standard axioms, 0 sorry. Modules OK: 22.

`no_counterexample_nn_even` (ClosedFamilies.lean, U159): under the named hypothesis `DarmonMerelNN2` ((n,n,2), n ≥ 4), no counterexample with x = y ≥ 4 and z even; standard axioms, 0 sorry.

`no_counterexample_four_pp` / `no_counterexample_p_four_p` (U160): under `DarmonMerelNN2Int`, no counterexample of signature (4,p,p) or (p,4,p), odd p ≥ 5; standard axioms, 0 sorry.

`conditional_residual_of_counterexample` (U161): under the seven named hypotheses every counterexample reduces to a `ConditionalResidual` (reduced signature not (4,4,3), (4,4,5), (n,n,4) n≥4, (4,p,p), (p,4,p) p≥5); standard axioms, 0 sorry.

`no_counterexample_three_three_even`, `conditional_residual_of_counterexample'` (U162): under the eighth named hypothesis `BCDYThreeThreeTwoN` the residual also excludes (3,3,4); standard axioms, 0 sorry.

`published_residual` (U163): under eleven named hypotheses the residual also excludes (n,n,n), (n,n,3), (5,5,7), (5,5,19), (7,7,5); standard axioms, 0 sorry.

`no_counterexample_four_even_any` (U167): under `BEN24n` ((2,4,n), n ≥ 4) no counterexample with 4|x, 2|y, z ≥ 4 — closes (4,4,p) for all p; standard axioms, 0 sorry. C060 reclassified DUPLICATE, C052 REFUTED (my literature error).

`closed_instance_rows` (U169): under the bundled named hypothesis `InstanceRows` (PSS {3,4,7}; Siksek–Stoll {3,4,5}; Cohen (3,4,4); (2,n,4) for (p,4,4)), those signatures carry no counterexample; standard axioms, 0 sorry.

## U177 — full `lake build` succeeds
`TaxonomyExtensions.lean` repaired: `spherical_signatures_exhaustive` and `parabolic_signatures_exhaustive` re-proved (statements unchanged), standard axioms, 0 sorry. The root `lake build` now completes for every tracked module (23). `SquarefreeCore.lean` remains untracked and unimported.

`final_residual` (U180): the machine-checked statement of what remains after every closure (thirteen named hypotheses); standard axioms, 0 sorry. Open reduced signatures: (4,q,r) with q ≠ r odd primes except {3,4,5},{3,4,7}; (p,q,r) odd primes not all equal, except (p,p,3) and the Dahmen–Siksek triples.

## U190–U192 — `formal/Beal/MordellFixedBase.lean`
`fixed_base_cube_plus_square`, `no_counterexample_three_four_fixed_base`: for a fixed base n with `MordellXIntegral (n^e)` (rank-0 Mordell curve y²=x³+nᵉ, PARI 2-descent; Nagell–Lutz), no counterexample A³+B⁴=n^r for ANY r = 6j+e, j ≥ 1. Standard axioms, 0 sorry. Found by a 1000-cell Jev sweep.

U193: all three {3,4,r} arrangements kernel-checked (`fixed_base_general`, `no_counterexample_three_r_four_fixed_base`, `no_counterexample_four_r_three_fixed_base`). LMFDB confirms the base-2 curves: y²=x³+32 = 1728.p2 and y²=x³−32 = 1728.m1, rank 0, trivial torsion.

U195: `no_counterexample_three_three_fixed_base` — fixed-base (3,3,r) for every r = 3j+e, j ≥ 1, under the named hypothesis `CubicSumXIntegral (n^e)`; standard axioms, 0 sorry. Per-base PARI list saved (153 (n,e) pairs with 2 ≤ n ≤ 150).

U204: `no_solution_bases_3_5_7` / `no_counterexample_bases_3_5_7` (formal/Beal/FixedBasesExample.lean) — kernel-checked instance of the fixed-bases sieve: 3^x+5^y≠7^z for all exponents (mod 8); axioms `[propext, Quot.sound]` only.


## How much of the kernel is actually about the exponents (U232, pool C097)

Two gates are now applied to every claimed necessary condition:

1. **Fermat–Catalan blindness** — a condition holding on all ten exponent-2 solutions carries no
   Beal-specific content.
2. **Gate 2 (new, C094)** — a condition whose *proof* does not use `A^x + B^y = C^z` is the
   exponent hypothesis in disguise, however it scores on gate 1.

Tested on 9,374 generic coprime triples `a + b = c` with **no** term a perfect power:

| kernel condition | holds on generic triples | Fermat–Catalan |
|---|---|---|
| pairwise coprimality of the values | 9374/9374 | 10/10 |
| no cancellation, `c > max(a,b)` | 9374/9374 | 10/10 |
| size window, `c < 2·max(a,b)` | 9374/9374 | 10/10 |
| exactly one of `a,b,c` even | 9374/9374 | 10/10 |
| mod-3 condition | 9374/9374 | 10/10 |
| **`eight_dvd_add_of_even_C`** | **6901/9374** | **9/10** |

Five of the six follow from the equation plus coprimality of the *values* alone. Only
`eight_dvd_add_of_even_C` passes both gates. It is a mod-8 congruence, a category the survey lists
as unable to resolve Beal, so this is a characterisation of the kernel, **not** progress toward a
proof.

## Radical bounds (U226–U228, pool C092/C093)

`formal/Beal/Radical.lean`, unconditional, standard axioms only:

* `radical_cube_le` — `rad(A·B·C)³ ≤ A^x·B^y·C^z`;
* `radical_pow_le` — `rad(A·B·C)^(xyz) ≤ (C^z)^(yz+xz+xy)`, i.e. an abc-quality floor
  `q ≥ 1/(1/x+1/y+1/z)`;
* `radical_cube_fails_on_fermat_catalan_2_7_17_3_71_2` — the exponent-2 solution `2^7+17^3=71^2`
  violates the first.

**Both fail gate 2.** Their proofs use only `rad n ∣ n` and `A³ ≤ A^x`; they never use the
equation. They are strictly weaker consequences of the exponent hypothesis, the same status as
`|χ| ≥ 1/12`. Survey category: abc. Not a proof route.


## Milestone-layer audit (U246–U250, pool C109–C117)

`code/verify_all_milestones.py` reports **67/67 passing**. That means 67 scripts executed and
self-reported success. It is **not** evidence about Beal, and eight of the claims those scripts
print were found to be defective:

| pool | script / claim | verdict |
|---|---|---|
| C110 | "Universal Serre surjectivity proved" | **REFUTED** — proves Cartan/exceptional elimination for `p ∈ {5,7,11,13}` only; Borel never addressed. |
| C111 | `universal_borel_elimination`: `ρ̄` surjective for all `p ≥ 11` | **REFUTED** — contradicts its own Mazur list at `p = 11,13,17,37`; irreducibility inputs are per-signature. |
| C112 | `orbit_b_definitive_elimination` | **REFUTED** — residual/isogeny conflation; already withdrawn in the README since 2026-09-17. Warning header added. |
| C113 | `(4,4,p)` via Hilbert forms over `Q(√2)` | conclusion **correct**, but via BCDY `(2,4,n)` + `(3,4,4)`; the CM step is unauditable here. |
| C115 | Q-curves: `(2k,4m,n)`, `(4k,4m,n)` | conclusions **correct**, but by a one-line substitution, not the Q-curve machinery. |
| C116 | `(10,10,23)` "100% unconditionally closed" | **REFUTED** — Chabauty over the wrong field; branch is OPEN. Script patched. |
| C117 | Serre uniformity "reduces the Beal Conjecture" | **REFUTED** — needs a Frey curve per signature; none exists for three independent exponents (C083). Script patched. |

**What survives, and is reusable.** For every prime `p ≥ 5` the order of a Cartan normalizer in
`GL₂(F_p)` is prime to `p` (verified for 25 primes, 5..103), so an order-`p` transvection in the
image rules out the Cartan and exceptional maximal subgroups. Surjectivity therefore reduces
*exactly* to irreducibility, which must be supplied per signature.

**Pattern.** Five of the seven families the milestone layer claims are subsumed by plain instance
closure from held sources; the elaborate modular apparatus was not needed for any of them.


## Obstruction lemmas (U253–U269, pool C120–C138)

`formal/Beal/Rigidity.lean` — 0 `sorry`, standard axioms only. These are statements about *why*
the modular method does not reach three independent exponents. **None is a step toward a proof of
Beal**, and the file header says so.

| theorem | content |
|---|---|
| `rigid_regular_semisimple_iff` | `-n² + 3n = 2 ↔ n = 1 ∨ n = 2` — a rigid local system on `P¹∖{0,1,∞}` that is regular semisimple at all three punctures has rank `≤ 2` |
| `rigid_max_budget_attained` | `-n² + ((n-1)² + 1 + n + n) = 2` — the triple `((n-1,1),(1ⁿ),(1ⁿ))` is rigid at every rank |
| `max_budget_total`, `budget_deficit` | its eigenvalue total is `2n+2`; the shortfall against `3n` is `n-2` |
| `moduli_dimension_regular_semisimple` | `2 - rig = (n-1)(n-2)` — dropping rigidity costs a positive-dimensional moduli for `n ≥ 3` |
| `moduli_dimension_eq_zero_iff` | it vanishes exactly at `n = 1, 2` |
| `three_full_exceeds_budget`, `two_full_leaves_two` | at rank `≥ 3` only **two** punctures can be regular semisimple |
| `totient_le_two_of_rank_two` | `φ(x) ≤ 2` forces `x ∈ {1,2,3,4,6}` (formalised for `x ≤ 30`) |
| `minBaseDegree_prime` | minimal base-field degree `(p-1)/2` for an odd prime exponent |
| `minBaseDegree_le_triple` | carrying all three orders costs at least `φ(lcm(x,y,z))/2` |
| `totient_mul_primes` | `φ(pq) = (p-1)(q-1)` for distinct primes — why the modular and geometric costs coincide |

The full account, including the classical Frey picture and the scope limitation, is
`research/checkpoints/U258_rigidity_obstruction.md`.

> **[U309 CORRECTION]** Every theorem in the table above still holds and is still machine-checked.
> The *conclusion* that used to be drawn from them — "no rigid object can carry three independent
> Beal exponents" — is **withdrawn**, refuted by `code/U309_rigidity_countersearch.py` and recorded
> as pool C169. The theorems constrain triples that are **regular semisimple** at all three
> punctures; a Beal exponent only forces the local monodromy to have **order** `x`, and a
> pseudoreflection `(n-1,1)` achieves any order with two eigenvalues. The hypergeometric triple
> `((1ⁿ),(1ⁿ),(n-1,1))` is rigid at every rank and carries three pairwise distinct orders. Read
> the rows above as statements about regular semisimplicity, not about exponent independence.

## The `(3,4,4)` signature (U314–U316, pool C168/C172/C173)

`formal/Beal/ThreeFourFour.lean` (28 theorems) and `formal/Beal/Cohen344.lean`, both in the root
build, no `sorry`, no custom `axiom`s.

| theorem | statement | axioms |
|---|---|---|
| `three_four_four_same_parity` | `0 < A → Odd B → Odd C → B < C → Nat.Coprime B C → A³+B⁴=C⁴ → False` | `propext, Classical.choice, Quot.sound` |
| `opposite_parity_reduction` | opposite parity reduces to `(μ²)³+(ν²)³ = 2τ³` with `μ, ν` coprime | same |
| `cohen344_of_euler` | `EulerCubicTwo → NoCoprimeSol 3 4 4` | same |
| `instanceRows_of_euler` | builds `InstanceRows` with the `cohen344` field no longer a citation | same |

**What is proved without hypotheses:** the same-parity branch, outright. Its only external input is
mathlib's `fermatLastTheoremThree`.

**What is not proved:** `EulerCubicTwo` — Euler's `a³+b³ = 2c³` has only `a = b` in coprime positive
integers (1770). It is **not in mathlib** and **not formalised here**; it is a stated `Prop`, so
every use of it shows in the type. mathlib's `FermatLastTheoremForThreeGen` does not apply: it
covers `a³+b³ = u·c³` for a *unit* `u` in `𝓞 K`, and `2` is not a unit in `ℤ[ζ₃]`.

**Scope.** This descent needs `C⁴ − B⁴` to factor, i.e. `gcd(y,z) > 1`, which among reduced
exponents means two exponents are equal. Beal's open core has three pairwise distinct reduced
exponents, so nothing here reaches it (pool C157). The value delivered is an **audit improvement**:
the one hypothesis of `final_residual` that could not be checked at $0 — a book not held in
`references/` — is replaced by a named classical theorem plus a machine-checked derivation.
