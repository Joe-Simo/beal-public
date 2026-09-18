# Beal conjecture — status at U158 (2026-09-18)

# We have not solved Beal's conjecture yet.

## Verified in the Lean 4 kernel (mathlib v4.14.0), standard axioms only, 0 sorry, no custom axioms

| file | content |
|---|---|
| `Residual.lean` | `residual_of_counterexample`: any counterexample yields one with exponents in {4} ∪ odd primes, not (4,4,4), not (3,3,3), exactly one even base, C even ⟹ (x,y) ≠ (4,4), no cancellation, pairwise coprime distinct bases. `beal_of_no_residual`: refuting every residual shape proves Beal. |
| `Structure.lean`, `Necessary.lean`, `ExponentReduction.lean` | 40+ elementary constraints (mod 8, mod 9, exponent order, dominant-term dichotomy, exact exponent reduction). All shown **exponent-2-blind** (C053). |
| `GaussianCube.lean`, `GaussianPow.lean` | `even_even_odd_reduction`: a counterexample of signature (2m, 2n, z), z odd, is a z-th power in ℤ[i] with coprime coordinates. |
| `SameOddPrime.lean` | `ppr_dichotomy`: for (p,p,r), either p ∤ A+B and A+B, S are r-th powers, or p ∣ A+B with v_p(A+B)+1 = r·v_p(C), v_p(S) = 1 (LTE). |
| `ClosedFamilies.lean` | `closed_unconditional`: (4k,4l,2j) and (3k,3l,3j) carry no counterexample (mathlib FLT₄/FLT₃). |

## Kernel-assembled relative to named hypotheses (VERIFICATION_REQUIRED)

Hypotheses (never axioms; all quoted from primary sources saved in `references/U130/`):
`BennettSkinnerThree` (Canad. J. Math. 56 (2004) Thm 1.1, C=3), `BCDYFourTwoNThree` (IJNT 11 (2015) Thm 1, row (4,2n,3)),
`Mordell27` (y²=x³+27: LMFDB 144.a4 rank 0, PARI 2-descent bound 0), `Quartic400g2`, `Quartic400b2` (rational points of two genus-1 quartics; Jacobians LMFDB 400.g2, 400.b2, rank 0; PARI 2-descent bound 0).

| family | theorem |
|---|---|
| (2m, 2n, 3), all m, n ≥ 2 | `no_counterexample_even_even_three_all` (`SixTwoNThree.lean`) |
| (4, 2n, 5), (2m, 4, 5), m, n ≥ 2 | `no_counterexample_four_two_n_five`, `no_counterexample_two_m_four_five` (`FourTwoNFive.lean`) |
| up to divisibility: no (2\|x, 2\|y, 3\|z), (4\|x, 2\|y, 5\|z), (2\|x, 4\|y, 5\|z) | `closed_conditional_dvd` (`ClosedFamilies.lean`) |

Mechanism: both summands are perfect powers, so on the classical ℤ[i] parametrisation the branch avoiding
the bad prime is always available on at least one side; that branch is killed by a one-sided published
theorem (z = 3) or lands on a rank-0 elliptic curve (exponent-3 side at z = 3; exponent-4 side at z = 5).
Not found in BCDY 2015 Tables 1–3 or the 2024 survey; not claimed novel (post-2015 searches found nothing).

## What remains
The residual core of `Residual.lean`: (4,4,p), (4,p,q), (p,q,r) with all exponents in {4} ∪ odd primes.
Every one needs Chabauty, Hilbert modular forms, or Q-curve descent over a number field (C052, C061, C063);
none is executable with PARI/GP + Lean at $0.

## Boundaries proved or recorded (do not re-derive)
Local sieves never reach zero (C036, C041, C054); the height-gap hypothesis is false on Fermat–Catalan
solutions (C042); (2m,2n,5) with m,n odd needs cross-side equations (C048); no one-sided identity for
z ≥ 7 (C049); the exponent-4 side is genus ≥ 2 for z ≥ 7 (C061); all elementary conditions are
Fermat–Catalan-blind (C053); (p,p,r) stops at the Thue equation S = e^r (C055/C056).

## Process
Every cycle opened with a Jev routing call (≈3,520 persisted results, all `HYPOTHESIS_ONLY`; Jev was
wrong on 14/15 blindness predictions — calibration recorded in C053). One flaw in my own chain (sign for
even m in S5) was found while writing the Lean statement and repaired (U134). Nothing committed,
published, or sent externally.


## Addendum U159
`no_counterexample_nn_even`: under `DarmonMerelNN2` (Darmon–Merel 1997 / Poonen 1998, (n,n,2), n ≥ 4), no counterexample has x = y ≥ 4 with z even — in reduced terms (p,p,4), p ≥ 5, is closed. Six named hypotheses now in the conditional ledger.

## Addendum U160
(4,p,p) and (p,4,p), odd p ≥ 5, closed under `DarmonMerelNN2Int` (permutation of Darmon–Merel (n,n,2)). Residual (4,p,q) now means p ≠ q.

## Addendum U161
`ConditionalResidual`: the machine-checked residual after all conditional closures. Remaining reduced signatures: (4,4,p) p ≥ 7; (4,p,q) p ≠ q odd primes; (3,3,4); (p,q,r) odd primes.

## Addendum U162
(3,3,2k) closed under `BCDYThreeThreeTwoN` (BCDY Thm 1). Remaining reduced signatures: (4,4,p) p ≥ 7; (4,p,q) p ≠ q odd primes; (p,q,r) odd primes (with (p,p,p), (p,p,3) and the listed (p,p,r) cases closed in the literature but not yet in the ledger). Eight named hypotheses.

## Addendum U163
`published_residual`: the machine-checked residual now matches the published frontier (BCDY Tables 1-2) up to the numerically bounded (3,3,n) results. Genuinely open core: (4,4,p) p ≥ 7; (4,p,q) p ≠ q odd primes; (p,q,r) odd primes not all equal, excluding (p,p,3) and the three Dahmen–Siksek triples. Eleven named hypotheses.

## Addendum U165 — pause declaration

# Research is paused, and we have not verified a solution.

Every mechanism executable with the available tools (Lean 4 + mathlib v4.14.0, PARI/GP 2.17 over ℚ,
exact Python, Jev routing) has been run to its boundary and the boundary is recorded in the pool
(C036, C041, C042, C048, C049, C053, C054, C061, C063). The open core — (4,4,p) p ≥ 7, (4,p,q) p ≠ q,
(p,q,r) odd primes — requires at least one of: Chabauty over number fields, Hilbert modular forms,
Q-curve descent. What would resume the loop: (a) a tool that performs one of those (Magma is paid;
Sage lacks general Chabauty), (b) a new rank-0 elliptic-curve or one-sided-theorem mechanism, or
(c) a new published result changing the frontier. All state is preserved: 69 pool candidates,
22 Lean modules (0 sorry), 11 named hypotheses with saved sources, ≈3,540 Jev results.

## Addendum U166–U167 — pause withdrawn; two errors of mine corrected

# We have not solved Beal's conjecture yet.

The pause was my decision, not the user's, and it was premature: a Jev-at-scale sweep aimed at the
residual core (288 cells, `residual_mechanism_space_U166.json`) pointed at (4,4,p), and working it found:

1. **C061 was partly wrong.** The z = 7 branch curves are genus 2 but even in V, so they have elliptic
   quotients; PARI gives rank 0 (trivial torsion) for y² = x³−21x²+35x−7, y² = 7(x³−21x²+35x−7) and
   y² = −7(−7x³+35x²−21x+1), and the remaining branch dies mod 8. So the exponent-4 side closes at z = 7.
2. **C052 was wrong.** (4,4,p) is *not* open: x⁴+y⁴=z^p is an instance of X²+Y⁴=Z^p, closed for all
   p ≥ 4 by Bennett–Ellenberg–Ng 2010 (BCDY Table 1, row (2,4,n)). Likewise every (4k, 2j, z).
   C060 ((4,2n,5)) is therefore a literature duplicate — an independent elementary re-derivation.

Lean: `no_counterexample_four_even_any` under the named hypothesis `BEN24n` (standard axioms, 0 sorry).

**Corrected open core:** (4,p,q) with p ≠ q odd primes, and (p,q,r) odd primes not all equal
(minus (p,p,3) and the three Dahmen–Siksek triples). Twelve named hypotheses.

**Prize conditions (user, U167):** a solution must be a peer-reviewed proof of the conjecture or a
verified counterexample. Nothing in this repository is either; conditional closures of sub-families
do not count, and no claim to the contrary is made anywhere.

## Addendum U168–U169
Instance-closure check: 72 of 288 reduced signatures (primes ≤ 19) are instances of closed literature rows; new: {3,4,7}, {3,4,5}, (3,4,4), (p,4,4). Smallest open: (3,5,7), (4,5,7), {3,4,11} (GRH-conditional in the literature — not counted). Jev sweep over these × 8 executable mechanisms: no cell above the no-signal threshold.

## Addendum U170–U174 — primary-source audits of named hypotheses
Read and saved in `references/U130/`: PSS Thm 1.1 (16 solutions; none with |x| a nonzero square, yz≠0); Siksek–Stoll Thm 1.1 ((3,4,5): only trivial solutions); Darmon–Merel Main Theorem ((n,n,2) n≥4 unconditional; (n,n,3) n≥3 assuming modularity of elliptic curves over ℚ — since proved by Breuil–Conrad–Diamond–Taylor 2001); Bennett–Skinner Thm 1.1; BCDY Thms 1–2 and Tables 1–3; Bennett 2006. Not yet read from a primary source: Cohen GTM 240 Prop. 14.6.6 ((3,4,4); an independent rank-0 re-derivation stands in), Dahmen–Siksek, Bennett–Ellenberg–Ng (table citation only).

## Addendum U175
Bennett–Ellenberg–Ng Theorem 1 read from the primary source: A⁴ + B² = Cⁿ has no coprime solutions for n ≥ 4. `BEN24n` audited. Remaining un-audited named hypotheses: Dahmen–Siksek triples, Cohen (3,4,4) (independent rank-0 re-derivation stands in), FLT (Wiles; standard).

## Addendum U176–U177
Dahmen–Siksek Theorems 1–2 read from the primary source (only trivial coprime solutions for (5,5,7), (5,5,19), (7,7,5)); `DahmenSiksek` audited. `TaxonomyExtensions.lean` repaired — root `lake build` completes, 0 sorry.

## Addendum U178–U180
Two Jev fidelity screens over all new Lean files (62 declarations): one real defect found and fixed (a docstring claimed (p,4,4) that the theorem did not prove; `closed_p_four_four` added), three docstrings tightened. `final_residual` now states the corrected open core in the kernel.

## Addendum U190–U192
1000-cell Jev sweep on the open core → fixed-base Mordell mechanism (C078): for rank-0 curves y²=x³±nᵉ the {3,4,r} signatures with base n are closed for all primes r ≡ e (mod 6), r ≥ 7, simultaneously — the first unconditional statement touching {3,4,11}. Kernel-checked scaling step; ranks for 2 ≤ n ≤ 120 saved.

## Addendum U194–U201
Fixed-base (3,3,r) closures (C079, Lean + PARI + LMFDB sample). Fixed-three-bases covering sieve (C080): of 3,607 pairwise-coprime triples with bases ≤ 30, 3,566 have NO solution with x,y,z ≥ 3 for any exponents (rigorous covering; independently re-implemented, 0 mismatches), 12 more by Mihăilescu, 29 open (they shadow genuine small-exponent identities such as 2⁵+7²=3⁴). First statements in the repo that cover (3,5,7)/(4,5,7) — for small bases only.

## Addendum U202–U203
C080 completed for bases ≤ 30: all 3,607 pairwise-coprime triples have no solution with x,y,z ≥ 3 for ANY exponents (3,595 by covering sieve incl. 29 shadow cases separated by prime powers of the shadowed base; 12 by Mihăilescu). Independently re-implemented in pure Python: 0 mismatches. Small bases only — no signature closed.

## Addendum U204–U206
Fixed three bases, all exponents, bases ≤ 50: all 17,594 pairwise-coprime triples have no solution with x,y,z ≥ 3 (20 of them via Mihăilescu). Two implementations sharing no code path agree exactly (15,971 single / 1,509 joint / 94 shadow / 20 A=1 / 0 open). Lean exemplar: bases (3,5,7), all exponents. Small bases only; no signature closed.

## Addendum U213–U215 (2026-09-18)
- U213: 384-cell Jev sweep on function-field (Mason–Stothers) transfer mechanisms. HYPOTHESIS_ONLY.
- C084 REFUTED: Fermat-quotient Wronskian. abc | a·δ_p(b) − b·δ_p(a) for EVERY coprime a+b=c (exact derivation + exact check), so it is blind and gives no size drop.
- C085 REFUTED: eight explicit descent maps; each increases height or lands on an exponent 2.
- U215 audit note: (3,4,4) attribution. Survey 2412.11933 footnote 4 states Cohen, *Number Theory II* (GTM 240), Prop. 14.6.6 proves (3,4,4). The book is not freely available ($0 budget), so the primary source is NOT audited; the secondary citation plus our rank-0 re-derivation (`references/U130/sig344_pari_output.txt`) stand in. Hypothesis stays a named hypothesis in `ClosedFamilies.lean`.

## Addendum U223–U232 (2026-09-18): verification-integrity sweep and the second gate

| pool | what |
|---|---|
| C089 | 3 root-chain theorems depended on Lean `axiom`s; all 4 external inputs converted to named `Prop`s. `#print axioms` now standard-only. |
| C090 | `formal/Beal/FidelityCheck.lean` machine-checks the root definition against every target-discipline trap. |
| C091 | `Signature3.lean` header presented conditional results as established; corrected. Stale `SquarefreeCore` olean removed. |
| C092 | `rad(ABC)³ ≤ A^x B^y C^z` formalised; **overstated** as non-blind content, corrected in C094. |
| C093 | Sharpened `rad(ABC)^(xyz) ≤ (C^z)^(yz+xz+xy)`; abc-quality floor `1/(1/x+1/y+1/z)`. Raw inequality is blind. |
| C094 | **Second gate**: does the proof use the equation? Added to `CLAUDE.md`. |
| C095 | Gate-2 screen over the pool: null result, labelling already consistent. |
| C096 | Galois z-roots cell fails gate 2 (3+5=2³ etc.). Gate-2 counterexample generator extracted. |
| C097 | Gate-2 countersearch on the kernel: 5 of 6 conditions hold on 100% of 9,374 generic non-power triples. Only `eight_dvd_add_of_even_C` has content. |

**Net effect on the mathematics: none.** The open cases in `final_residual` are unchanged. What
changed is the accuracy of the account: the build is now genuinely axiom-free in the root chain,
the conditional results are labelled, and the kernel's actual content is measured rather than
assumed.

## Addendum U233–U245 (2026-09-18): hypothesis audit and its consequences

| pool | what |
|---|---|
| C098 | `d ∣ C → d^z ∣ A^x+B^y` machine-checked; subsumes the fixed modulus 8. |
| C099 | `full_unconditional_account` — one theorem holding every unconditional constraint, each gate-tagged. |
| C100 | 16 named hypotheses audited against primary sources; 10 faithful. Jev calibration rule added. |
| C101 | **Defect**: a "Bruin 2004 Crelle" citation with no supporting source. Replaced by survey Table 1.1/1.2 attribution. |
| C102 | **Defect**: `FreitasTheoremMod3` (all primes p ≡ 2 mod 3) unsupported — no mod-3 class in any held source. Marked UNVERIFIED; supported `BCDYThreeThreeBounded` added. |
| C103 | **Defect**: `KrausEvenCLevel18Newform` unsupported. Replaced by `KrausProp7` (BCDY Prop. 7, quoted verbatim), which is *stronger*: `C ≡ 3 (mod 6)`. |
| C104 | Audit closed. `not_three_dvd_z_of_three_dvd_xy` is **vacuous** on signature (3,3,z). |
| C105 | The (p,p,r) dichotomy **collapses at p = 3**: the coprime branch is empty, so `3^(z-1) ∣ A+B`. |
| C106 | Open-core recomputation; {3,4,7} closure re-verified via the PSS square check. |
| C107 | Instance closure **exhausted** — no new signature closable from held literature. |
| C108 | Exact (3,3,z) descent: 1,112 candidates, 0 solutions. Closes nothing. |

**Net effect on the mathematics: none.** Three real defects were removed from the conditional
chain, and one replacement is strictly stronger than what it replaced.

## Session close (2026-09-18): C089–C159

**Beal's conjecture is not solved. No proof, no counterexample.**

**Verification state.** `lake build` clean, 0 `sorry`, 0 custom axioms outside the unimported and
non-compiling `SquarefreeCore.lean`. Milestone harness 67/67 — which means 67 scripts ran and
self-reported success, and is not evidence about Beal.

**Three lines of work.**

1. **Audit (C100–C119, C139).** Eight defects found and fixed or flagged: a citation with no
   supporting source (C101); an unsupported unbounded family (C102); an unverifiable
   level-lowering input, replaced by the *stronger* BCDY Prop. 7 (C103); three per-signature
   results stated as universal (C110, C111, C117); two claims withdrawn in one layer but still
   passing in another (C112, C116). The open-core statement `final_residual` was then checked and
   **uses none of them** (C142).

2. **The obstruction (C120–C138).** Six faces plus a dichotomy, core machine-checked in
   `formal/Beal/Rigidity.lean`, written up in `research/checkpoints/U258_rigidity_obstruction.md`.
   The survey's bare "no Frey object for three independent exponents" is replaced by exact prices,
   and the two live directions cost the *same integers* for prime signatures — 4, 12, 6 at (3,5,7).

3. **The `(3,4,4)` input (C143–C159).** The one unauditable hypothesis, attacked directly and
   reduced to three branches: same parity **closed unconditionally by FLT3**; `3 ∣ gcd` **empty**;
   survivor = elliptic Chabauty on `y² = x³ − 972`. Written up in
   `research/checkpoints/U278_cohen344_descent.md`, closing steps in
   `formal/Beal/ThreeFourFour.lean`.

**The convergence.** Three independent lines — the rigidity budget (C128), the Frey discriminant
search (C136), the factorisation descent (C157) — stop at the same boundary: **two exponents can
be related, the third cannot.** The open core is exactly the signatures with three independent
reduced exponents.

## Addendum C160–C167: the (3,4,4) survivor, computationally

**Verification queue cleared.** C047, C057, C058, C064, C065, C067, C070, C078, C151 discharged —
by primary-source reading, by exact algebra, by Lean `#print axioms`, by independent
re-implementation with a positive control, and (for `Y² = X³ + 27`) by a **second method**:
2-descent and analytic rank both give 0, with the affine points to height 10⁶ being exactly
`(-3,0)`. **C007 corrected to REFUTED**: it claimed `(5,5,p)` for all primes `p ≥ 5`, which no held
source supports — Dahmen–Siksek give `(5,5,7)`, `(5,5,19)` unconditionally and `(5,5,11)`,
`(5,5,13)` under GRH only. The Lean `DahmenSiksek` hypothesis lists only the unconditional triples,
so nothing depended on the overclaim.

**The survivor.** Four models all give `y² = x³ − 972` (rank 1, trivial torsion). The recurring
point is a forced tangency. Mordell–Weil enumeration to `n ≤ 40`: no admissible point. The sieve
forces `120 ∣ n`, hence an `x`-coordinate of ~37,500 digits — so the bounded searches were
guaranteed to find nothing. The sieve cannot finish (the identity class always survives); the
elliptic-Chabauty rank condition *is* satisfiable over eleven quadratic fields, but PARI has
neither `ellintegralpoints` nor Chabauty.

**Two false positives, both mine.** `sqrt()` returning a float where `issquare` needed exactness
(C164); a termination test reading "one class `0 mod 2`" as "only `n = 0`" (C166). Both are
recorded with their causes, because both failed in the dangerous direction.
