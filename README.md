# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

> ## ⚠ AUDIT NOTICE (2026-09-17)
>
> A systematic audit ([U113](research/checkpoints/U113_orbit_b_elimination_audit.md)) and a
> literature check ([U114](research/checkpoints/U114_literature_state_of_the_art_and_dead_ends.md))
> **withdrew several claims made below and elsewhere in this repository.** Read those two
> checkpoints and the [corrected coverage ledger](research/checkpoints/U113_corrected_coverage_ledger.md)
> before relying on anything here. For the machine-checked subset, see [VERIFIED.md](VERIFIED.md).
>
> Headlines:
> - The **orbit `b` elimination is WITHDRAWN** — U97 and U102 both conflate a residual mod-17
>   congruence with an isogeny/17-adic statement. The weighted-equation modular route is **open**.
> - The **Chabauty route is WITHDRAWN** — it bounds `C^-(k)` while solutions give points of
>   degree 10 over `k` (minimal polynomial `x^10 + 256`).
> - Several "unconditional" labels were **relabelled conditional** (GRH, finiteness of Ш, or
>   Cohen–Lenstra/Cohen–Martinet heuristics used to "remove" GRH via GRH-conditional Bach bounds).
> - The Lean development **had never compiled**; the lakefile was malformed. It is partly repaired:
>   6 of 14 modules now build with zero `sorry` and zero custom axioms.
> ## ⚠ SECOND AUDIT NOTICE (2026-09-18) — the milestone layer
>
> The 2026-09-17 notice corrected the *checkpoint* layer. A second pass (pool C109–C113) found the
> **milestone harness** (`code/verify_all_milestones.py`, 67/67 passing) still asserts claims this
> repository has already withdrawn, because the two layers were never cross-checked:
>
> - **"Universal Serre surjectivity proved"** (U111–U112 commit message) is **not established**
>   (C110). `U111_general_cartan_elimination.py` proves a true but narrow fact — Cartan normalizer
>   orders are prime to `p` — for `p ∈ {5,7,11,13}` only, and never touches the Borel case.
> - **`U111_universal_borel_elimination.py`** claims `ρ̄` is *unconditionally surjective for all
>   `p ≥ 11`* while its own Mazur list contains `p = 11, 13, 17, 37` (C111). Its irreducibility
>   inputs are signature-specific and presuppose a Frey curve for three independent exponents.
> - **`U102_orbit_b_definitive_elimination.py`** still asserts the *withdrawn* orbit-`b`
>   elimination and still passes (C112). A warning header has been added to the file.
> - **`(4,4,p)`** is genuinely closed, but by BCDY Table 1 row `(2,4,n)` plus `(3,4,4)`, **not** by
>   the Hilbert-forms route the milestone claims (C113).
>
> A green 67/67 means 67 scripts executed and self-reported success. It is not evidence about Beal.
>
> Six defects were also removed from the Lean conditional chain: a citation with no source (C101),
> an unsupported unbounded family (C102), an unverifiable level-lowering input (C103, replaced by
> the *stronger* BCDY Proposition 7), plus the three milestone items above.

> - **Literature supersession**: `(3,3,p)` is solved in the literature for `p ≤ 10^9`; this repo
>   certified `p ≤ 700`. `(n,n,n)` for all `n ≥ 3` is Wiles–Taylor. The smallest OPEN Beal
>   signature is `(3,5,7)` **by largest exponent, and by sum** — the ordering matters and was
>   previously unstated (U331). Lexicographically the first open signature is `(3,4,11)`, and
>   `(3,4,11)` is also the smallest open one containing a `4`. Verified by
>   `code/U168_instance_closure.py`: 34 distinct unordered signatures are open in the tested box.

> ## ⚠ THIRD AUDIT NOTICE (2026-09-18) — the obstruction layer
>
> A third pass (pool C169–C185) corrected the *obstruction* layer, and one of the corrections is a
> refutation of this repository's own headline claim.
>
> - **WITHDRAWN: "no rigid object carries three Beal exponents"** (U258). Refuted by
>   `code/U309_rigidity_countersearch.py` (C169). The error was conflating *local monodromy has
>   order x* with *local monodromy is regular semisimple with eigenvalues of order x*. A
>   pseudoreflection `(n−1,1)` has the order of its single non-trivial eigenvalue, so the
>   hypergeometric triple `((1ⁿ),(1ⁿ),(n−1,1))` is rigid at **every** rank and carries three
>   pairwise distinct orders — `(3,7,11)` at `n = 6`. The rigidity-index arithmetic in
>   `formal/Beal/Rigidity.lean` is correct and stands; only the conclusion was wrong.
> - **The obstruction that does hold is regularity, over ℚ only** (C174, C175, C176). Regular
>   Hodge–Tate weights force a pseudoreflection, which is ℚ-rational only when `φ(m) = 1`. But a
>   base field of degree `φ(r)/p` — between **2 and 6** for every triple with exponents ≤ 19 —
>   already reconciles the ranks, so the obstruction must not be quoted as field-independent.
> - **Two distinct walls, both priced** (C185). Automorphy fails on the *rank of one object*;
>   effective Diophantine geometry fails on *uniformity over a family whose genus grows without
>   bound* (`g ≥ 49855/2` already at signature `(3,4,9973)`). Neither is reachable at $0.
> - **A false hypothesis kept the build green** (C177, U322). `EulerDescentStep` was recorded as the
>   residual gap of the `(3,4,4)` chain and was **false** — `p = 0, q = 1, c = 0`. Everything
>   downstream still type-checked, because an implication from a false hypothesis is a theorem. All
>   fourteen named Props are now counterexample-searched (`code/U323_named_prop_countersearch.py`,
>   with a control that must recover the known-false variant).
>
> **What is genuinely new and unconditional**: `Beal.three_four_four_same_parity` in
> `formal/Beal/ThreeFourFour.lean` closes `A³ + B⁴ = C⁴` for odd coprime `B, C` outright, its only
> external input being mathlib's `fermatLastTheoremThree`. By C157 this cannot reach the open core,
> which needs three pairwise distinct reduced exponents.

> **[MERGE NOTE, 2026-09-18]** The body below is the U113–U118 audited status from the
> remote branch, which already supersedes the older U96–U99 section this local branch
> carried; that section has been dropped rather than merged, because U113–U118 corrects it.
> The three audit notices above are newer still and take precedence over anything below.

## Current audited status — U113–U118 (2026-09-17)

The strongest active weighted branch remains

`X^10 + 256Y^10 = Z^17`.

Earlier checkpoints U97–U105 contained several claims that were stronger than their evidence. U113–U118 preserve the corrections below and **supersede any older statement that the weighted equation or orbit b has been eliminated**.

### 1. U113 — universal transvection/Cartan argument refuted
[U113](research/checkpoints/U113_exploration_population_and_transvection_audit.md) checks the Tate-curve hypothesis omitted by U110–U111. At the natural solution-variable primes, the displayed discriminant valuation is divisible by the representation prime, so multiplicative reduction alone does not provide the asserted order-p transvection. The universal Cartan-elimination/surjectivity claim is therefore invalid.

### 2. U114 — genus-8 Chabauty closure refuted
[U114](research/checkpoints/U114_u105_geometric_closure_audit.md) finds two independent gaps:
- a dimension bound on the Chabauty annihilator was incorrectly turned into a claim that six prescribed canonical differentials annihilate the Mordell–Weil group;
- the Diophantine construction produces higher-degree Galois-orbit/divisor data, not a k-rational point, so classifying `C^-(k)` does not classify the relevant symmetric-power points.

The genus-8 curve computations remain possible ingredients, but the recorded geometric pathway is not a proof of the weighted equation.

### 3. U115–U116 — modular pathway repaired only through level lowering
[U115](research/checkpoints/U115_u105_modular_pathway_audit.md) removes a mixed genus-8/genus-2 dependency, an impossible `V_4`/order-5 projective-image combination, and an inapplicable Allen–Khare–Thorne citation.

[U116](research/checkpoints/U116_repaired_breuil_diamond_bridge.md) reconstructs a coherent **partial** modular path for the correct genus-2 negative Frey Jacobian:
- Azon's negative compatible-system theorem supplies modularity;
- direct local analysis at 2 supplies conductor exponent 2 and residual irreducibility;
- a Clifford-theory argument supplies irreducibility after adjoining `zeta_17`;
- Breuil–Diamond Theorem 3.2.2 can be applied using actual geometric local lifts, without the old deformation-ring uniqueness claims;
- the resulting fixed target level is `p_2^2 p_5^3`, norm 2000.

This is a level-lowering bridge, **not** a solution.

### 4. U117 — fresh level-2000 inventory: 7/8 eliminated, orbit b survives
[U117](research/checkpoints/U117_level2000_inventory_and_cm_obstruction_audit.md) re-queries the live LMFDB inventory and verifies exactly eight target newform orbits.

Current LMFDB CM classification:
- non-CM: `a,c,f,g,h`;
- CM: `b,d,e`.

Thus the older statement “seven non-CM forms plus a unique CM form b” is false.

The exact prime-11 Frey trace sieve eliminates
`a,c,d,e,f,g,h`.
Only orbit `b` survives.

The later U97/U102 “definitive elimination” of b is **not established**:
- residual mod-17 congruence was incorrectly upgraded to characteristic-zero isomorphism;
- characteristic-zero ramification was compared across a level-lowering step where residual ramification can disappear;
- finite forcing-prime checks were extrapolated without proof;
- the claimed `10^434` Baker bound was misattributed and not verified;
- the classical `X_0(17)` argument was not translated to the actual RM abelian-surface moduli problem.

### 5. U118 — uniform auxiliary-prime forcing refuted at q=211
[U118](research/checkpoints/U118_cartan_character_and_q211_counterexample.md) tests the proposed global escape

> orbit-b congruence forces `V=0 mod q` for every good `q == 1 mod 5`.

It is false.

At `q=211`, the admissible non-boundary residues
`X=1, Y=31, Z=4` give
`U=1, V=23 != 0`
and satisfy the local weighted equation. Direct exact point counts give the same Frobenius data as the boundary curve:
`#C(F_211)=193`,
`#C(F_211^2)=44983`,
`(S,P)=(19,-11)`.
A separate Wolfram computation reproduced the result.

The exact checker is [`code/U118_q211_orbit_b_counterexample.py`](code/U118_q211_orbit_b_counterexample.py).

Therefore no proof may extrapolate the successful q=11,31,41 boundary sieve to all split primes.

## Active exploration population

The persistent exploration tree is stored in
[`research/exploration/population.json`](research/exploration/population.json).

It records:
- parent/inspiration links;
- exact objectives;
- evidence and unresolved obligations;
- evaluator outcomes;
- failure mechanisms;
- novelty;
- status;
- bounded routing scores.

**Jev/Typesafe is not callable in the current research runtime.** No mathematical result is attributed to Jev. The routing fields are transparent research-management metadata only, not probabilities and not proof evidence.

The current highest-leverage restart is to eliminate surviving orbit b by a genuinely global mechanism: an RM 17-isogeny/Cartan-locus argument, a second compatible Frey system, or a Gaussian-descent invariant that is incompatible with the boundary CM specialization. Additional isolated prime sieves are deprioritized.

## Preserved earlier partial results

- [U92](research/checkpoints/U92_forcing_prime_sieve_exhausted.md): the specific Gaussian forcing-prime criterion has exactly fourteen forcing primes; blindly extending that search cannot create more.
- [U85](research/checkpoints/U85_ratio_collision_invariant.md)–[U86](research/checkpoints/U86_symmetric_X_support.md): all-prime ratio-collision/support invariants provide lower-bound and divisibility information but no contradiction.
- The Section 8 exact counterexample checker remains useful for validating explicit six-integer candidates; passing checker tests does not prove Beal.

## Global coverage

The coefficient-256 weighted orientation is unresolved. The larger mixed-signature portion of Beal is unresolved. No bounded computation, density statement, partial modular elimination, Chabauty rank bound, or AI/model agreement is counted as a solution.

Historical files are retained for provenance; downstream claims must use the U113–U118 corrected status when they conflict with older checkpoints.

## Original target

For positive integers `A,B,C,x,y,z` satisfying

`A^x + B^y = C^z`

with `x,y,z >= 3`, prove

`gcd(A,B,C) > 1`

or produce an independently verified counterexample. All bases and exponents remain unbounded.
