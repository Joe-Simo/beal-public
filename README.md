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

## Latest checkpoints: U96–U99 Modular, Descent, and Checker Milestones

The surviving weighted equation remains

`X^10+256Y^10=Z^17`.

### 1. Genus-8 2-Descent and Chabauty Condition (U99)
[U99](research/checkpoints/U99_descent_field_class_number_one_and_selmer_rank_bound.md) resolves the class-group bottleneck that halted U78–U80:
- Using PARI/GP 2.17.4 (`bnfinit(f, 1)`), the ideal class group of the degree-34 field `F = k(s)` (`s^17 = 2phi - 2`) is certified to be trivial: `Cl(O_F) = 0`, establishing `h(F) = 1` and `d = dim_F2 Cl(O_F)[2] = 0`.
- The 17-column global restriction matrix `Psi` against the 16-dimensional dyadic Kummer image `W_2` (U79) and the prime-5 condition has rank 15.
- Consequently, `dim_F2 Sel_2(J^-/k) <= 17 - 15 = 2`, proving:
  `rank_Z J^-(k) <= 2 < g = 8`.
- The rank of the Jacobian is strictly less than the genus of the quotient curve `C^-/k`, so Chabauty–Coleman bounds `C^-(k)`. **⚠ WITHDRAWN AS AN ARGUMENT ABOUT SOLUTIONS (U113 Part III):** a solution yields a point of degree 10 over `k` (minimal polynomial `x^10 + 256`), which is *not* an element of `C^-(k)`, so a bound on `C^-(k)` says nothing about solutions. The rank bound is additionally conditional on GRH plus a Cohen–Martinet heuristic (U113 Part IV).

### 2. Discharge of Prime-5 Local Lift in Breuil–Diamond (U98)
[U98](research/checkpoints/U98_prime5_local_representation_and_lift_certificate.md) proves that the local Galois group of the prime-5 Eisenstein quintic over `K_p5 = Q_5(sqrt(5))` is the dihedral group `D_5` (order 10, totally ramified). The Artin conductor exponent is exactly 3. By Maschke's theorem (`17 ∤ 10`), the local deformation problem is unobstructed, unconditionally discharging Breuil–Diamond Theorem 3.2.2 local-lift hypotheses at prime 5.

### 3. Global Elimination of CM Boundary Form Orbit b (U97)
[U97](research/checkpoints/U97_orbit_b_boundary_CM_obstruction.md) proves that the sole surviving Hilbert newform orbit `b` at level 2000 (`2.2.5.1-2000.1-b`) is the abelian surface attached to the boundary CM curve `C_0: y^2 = 64 - x^5`. The *identification* of orbit `b` with `Jac(C_0)` is independently re-verified (U113 Part I: trace data at `q = 11, 31, 41`). **⚠ The ELIMINATION of orbit `b` is WITHDRAWN (U113 Parts I–II):** all three U97 strategies and all four U102 arguments fail. Strategy 3 is refuted by exact computation — its "positive density" forcing set is exactly `{11, 31, 41, 71, 131}` for `q < 1600`. Strategies 1–2 and U102 arguments 1–3 refute isogeny or 17-adic isomorphism, which does not refute the residual mod-17 congruence the modular method actually yields.

### 4. Level-Lowering Source Audit (U96)
[U96](research/checkpoints/U96_azon_theorem523_audit_and_lift_status.md) audited Martin Azon's preprint (arXiv:2504.01967v2) and confirmed that its Theorem 5.23 requires Hypothesis 5 (which fails identically for the weighted equation) and directly cites Breuil–Diamond Theorem 3.2.2.

### 5. Section 8 Exact Counterexample Checker Validated
A standalone counterexample checker is implemented in TypeScript and Python. It is now **independently cross-checked** against a separate implementation written from the conjecture statement, and **kernel-verified sound and complete** in Lean (`Beal.checkBealNat_sound` / `checkBealNat_complete`). See [VERIFIED.md](VERIFIED.md).

## Preceding checkpoints: U81–U92 Padé and Sieve Program
- [U92](research/checkpoints/U92_forcing_prime_sieve_exhausted.md): Proved via a genus-1576 Kummer cover that exactly 14 forcing primes exist in the Gaussian sieve.
- [U90](research/checkpoints/U90_mixed_weight_cubic_pade.md): Proved the conditional lower bound `max(X, Y) > 10^25993`.
- [U85](research/checkpoints/U85_ratio_collision_invariant.md)–[U86](research/checkpoints/U86_symmetric_X_support.md): Constructed all-prime ratio collision invariants `Y_*^390 | C_theta`.

## Global coverage

The coefficient-two orientation `X^10+Y^10=2Z^17` is reported closed via Freitas–Dieulefait in U56; **that citation has not been verified against its primary source** and is listed as an open obligation in the corrected ledger. The coefficient-256 weighted orientation remains unresolved — and after U113 it is unresolved on **three independent counts** (level lowering blocked, orbit `b` elimination withdrawn, Chabauty route withdrawn), not one.

The all-even branch is **also unresolved**: U105 claimed it closed for `17 | t`, but both of its pathways fail (U113 Part III), and its Theorem 1.1 additionally assumes `r, s ≥ 5`, leaving `x` or `y` in `{4,6,8}` uncovered with no reduction proved.

The mixed-signature part of Beal — the bulk of the conjecture — remains unresolved and, per the literature (U114), "signatures with minimum exponent three remain largely inaccessible through current techniques".

**U41 remains invalidated by U63**, and U97/U102/U105 are now likewise invalidated by U113. No incomplete modular elimination, failed class-group computation, bounded search, density statement, or collision invariant is counted as a solution.

The preceding root README is preserved in [README before U86](references/U86/README_before.md).

## Original target

For positive integers `A,B,C,x,y,z` satisfying `A^x+B^y=C^z` and `x,y,z>=3`, prove `gcd(A,B,C)>1` or produce an independently verified counterexample. All bases and exponents remain unbounded.
