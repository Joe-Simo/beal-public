# Beal Research Index

## Status

**The Beal conjecture is not solved.** Nothing in this repository is a complete proof or a verified counterexample.

The exact target is: for positive integers `A,B,C,x,y,z` with `x,y,z >= 3` and `A^x+B^y=C^z`, prove `gcd(A,B,C)>1` or exhibit an exact primitive counterexample.

## Repository structure

- `research/checkpoints/` — chronological durable checkpoints, coverage ledgers, corrections, and active branch reductions.
- `research/gaussian-descent/` — the independent Gaussian/quadratic-field route for the coefficient-256 weighted branch.
- `research/modular-method/` — Hilbert/Frey modular-method experiments and their correction history.
- `research/computations/` — preserved computation records when present.
- `code/` — reproducible exact checkers and experiments when present.
- `references/` — source records when present.
- `formal/` — proof-assistant material when present.

Checkpoint numbers are chronological research labels, not theorem numbers and not claims of completeness. Some historical labels were duplicated before the repository was structured; filenames are retained to preserve history. Use this index and each artifact's status line rather than assuming numerical order alone establishes dependency.

## Global coverage state

The authoritative starting coverage ledger is `checkpoints/U42_coverage_ledger_rebuild.md`, followed by the reconstructed all-even chain in U43-U47.

For a primitive hypothetical counterexample, preserved reductions establish:

- the bases are pairwise coprime;
- base `1` is impossible by Catalan-Mihailescu;
- exponents can be reduced independently to `4` or an odd prime while preserving primitivity;
- `gcd(x,y,z)` is `1` or `2` by Fermat's Last Theorem;
- in the all-even branch, writing `x=2r,y=2s,z=2t` gives the primitive Pythagorean system reconstructed in U43;
- the boundary `t=2` is eliminated in the dedicated U46 checkpoint;
- every prime divisor of `r` and `s` in a surviving all-even candidate is at least `5`;
- every prime divisor of `t` is at least `17`.

Thus the all-even branch splits into:

1. **`17|t`** — Michaud-Jacobs' theorem forces one of `r,s` to be a pure power of `5`, yielding one of two explicit equations:
   - `X^10+Y^10=2Z^17`;
   - `X^10+256Y^10=Z^17`.
2. **`17∤t`** — every prime divisor of `t` is at least `19`; current literature gives important asymptotic/effective results but not a complete elimination of this family.

The full Beal conjecture still also contains infinitely many mixed-parity signatures outside the all-even branch.

## Active coefficient-2 branch

The current active chain on `main` is:

- `U46_coefficient2_square_branch_literature_and_mod103.md` — published local-case pruning and the first mod-103 restriction.
- `U48_coefficient2_gaussian_descent.md` — `m^2+n^2=u^17` and `m+i n` as a Gaussian seventeenth power.
- `U49_coefficient2_quartic_factor_descent.md` — factor the octic over `Q(sqrt(5))` and obtain an ideal seventeenth-power descent.
- `U50_coefficient2_unit_classes.md` — finite unit ambiguity.
- `U51_coefficient2_combined_q67_sieve.md` — combine Gaussian and real-quadratic power conditions.
- `U52_coefficient2_q409_eliminates_unit15.md` — eliminate the final nontrivial real-quadratic unit class.
- `U53_coefficient2_alpha_coefficient_equations.md` — exact coefficient forms for `(A+B omega)^17`.
- `U54_lucas_reduction_and_squareclass17.md` — identify the degree-16 coefficient as `U_17(P,Q)` and reduce to the exceptional squareclass `U_17=17 S^2`.
- `U55_cyclotomic_unit_collapse_and_difference17.md` — exact `Q(zeta_5)` equation `X^2+zeta_5 Y^2=(1+zeta_5)gamma^17` and the difference-of-seventeenth-powers descent.
- `U56_direct_zeta20_descent_reaudited.md` — direct `Q(zeta_20)` linear-factor descent, re-audited unit sieve, simultaneous exact quadratic descents, and the current fixed Kummer ratio target.

Current strongest coefficient-2 equations include

`m+i n = rho^17`,

`m+mu n = Gamma^17`,  where `mu=(zeta_20-1)/(zeta_20+1)`,

and the `Q(zeta_5)` relation

`gamma^17-u^17 = 2 tau m n`, where `tau=(1-zeta_5)/(1+zeta_5)`.

In the chosen `Q(zeta_20)` orientation, exact split-prime sieves currently force

`228392811525274638941 | n`.

This is a finite divisibility theorem, not an infinite descent and not a contradiction. Local Hensel lifting shows that repeatedly increasing precision at those same primes is not by itself a viable proof route.

## Coefficient-256 weighted branch

`research/gaussian-descent/` preserves U15-U25 and U33-U39: Gaussian factorization, modular forcing primes, quadratic-field norm reduction, unit collapse, integral-basis identities, exact 5- and 17-adic locking, and moving-factor/cyclotomic coprimality results for

`X^10+256Y^10=Z^17`.

`research/modular-method/U40...` and `U41...` contain a later Frey/Hilbert modular attempt. **Do not count U41 as an independently verified elimination of this branch.** Its theorem-chain and finite-newspace computations require independent reconstruction/audit, and the arithmetic descent remains the safer preserved evidence.

## Current research priorities

1. **Coefficient-2:** exploit the global Kummer ratio
   `(m+mu n)/(m+i n)=(Gamma/rho)^17`
   together with `n/m in Q`, rather than accumulating more isolated forcing primes.
2. **Coefficient-2 parallel route:** investigate the explicit genus-three quotient arising from the surviving Lucas squareclass, retaining the square and reconstruction constraints.
3. **Coefficient-256:** continue the independently preserved algebraic descent or independently rebuild the modular computation before crediting an elimination.
4. **All-even large-prime branch:** study `17∤t`, where all prime divisors of `t` are at least `19`.
5. Return to the much larger mixed-signature coverage only when one of these focused branches reaches a useful stopping point.

## Conventions

- Preserve failed and corrected routes; do not silently rewrite history.
- A computational certificate proves only its stated finite/exact assertion.
- External theorems must be recorded with hypotheses and checked against the branch where used.
- “Verified” inside an artifact means verified within its recorded evidence; it is not independent expert review or proof-assistant certification of Beal.
- No partial branch elimination changes the global success status unless every Beal case is covered.
