# Beal Research Index

## Status

**The Beal conjecture is not solved.** Nothing in this repository is a complete proof or a verified counterexample.

The exact target is: for positive integers `A,B,C,x,y,z` with `x,y,z >= 3` and `A^x+B^y=C^z`, prove `gcd(A,B,C)>1` or exhibit an exact primitive counterexample.

## Repository structure

- `research/checkpoints/` — chronological durable checkpoints, coverage ledgers, corrections, and active branch reductions.
- `research/gaussian-descent/` — independent Gaussian/quadratic-field work on the coefficient-256 weighted branch.
- `research/modular-method/` — Hilbert/Frey modular-method experiments and correction history.
- `research/computations/` — preserved computation records when present.
- `code/` — reproducible exact checkers and experiments when present.
- `references/` — source records when present.
- `formal/` — proof-assistant material when present.

Checkpoint numbers are chronological research labels, not theorem numbers and not claims of completeness. The U56 label is reserved for `U56_direct_zeta20_descent_reaudited.md`; the coefficient-2 literature closure is U57. Historical corrections are preserved rather than silently rewritten.

## Global coverage state

The authoritative starting coverage ledger is `checkpoints/U42_coverage_ledger_rebuild.md`, followed by the reconstructed all-even chain U43-U47 and the coefficient-2 correction U57.

For a primitive hypothetical counterexample, preserved reductions establish:

- the bases are pairwise coprime;
- base `1` is impossible by Catalan-Mihailescu;
- exponents can be reduced independently to `4` or an odd prime while preserving primitivity;
- `gcd(x,y,z)` is `1` or `2` by Fermat's Last Theorem;
- in the all-even branch, writing `x=2r,y=2s,z=2t` gives the primitive Pythagorean system reconstructed in U43;
- the boundary `t=2` is eliminated in U46;
- every prime divisor of `r` and `s` in a surviving all-even candidate is at least `5`;
- every prime divisor of `t` is at least `17`.

Thus the all-even branch splits into:

1. **`17|t`** — Michaud-Jacobs forces one of `r,s` to be a pure power of `5`, yielding one of two explicit equations:
   - `X^10+Y^10=2Z^17` — **closed by U57**;
   - `X^10+256Y^10=Z^17` — U41 gives a serious candidate modular elimination, but independent certification is still open.
2. **`17∤t`** — every prime divisor of `t` is at least `19`; current literature gives important asymptotic/effective results but not a complete elimination of this family.

The full Beal conjecture still also contains infinitely many mixed-parity/mixed-exponent signatures outside the all-even branch.

## U57 correction: coefficient-2 orientation is closed

The project previously treated

`X^10+Y^10=2Z^17`

as open because it relied on arXiv:1103.5388v1, where Dieulefait-Freitas stated a narrower congruence condition using

`p ≡ 1 (mod 4) AND p ≡ ±1 (mod 5)`.

U57 recovers the stronger primary source: Nuno Freitas' 2012 doctoral thesis, Theorem 2.0.3, proves that for `beta` supported only on primes not congruent to `1 mod 5`,

`x^5+y^5=2 beta z^p`

has no non-trivial primitive solutions for `p>13` whenever

`p ≡ 1 (mod 4) OR p ≡ ±1 (mod 5)`.

Taking `beta=1`, `p=17`, `x=X^2`, `y=Y^2` eliminates the Beal-derived coefficient-2 orientation. U43 has `X<Y`, so the only positive trivial solution `(1,1,1)` cannot arise.

The later joint paper is Dieulefait-Freitas, *Mathematics of Computation* 83 (2014), 917-933, DOI `10.1090/S0025-5718-2013-02731-7`; its final publication abstract reports a density-3/4 solved prime set, consistent with the strengthened OR condition rather than the old preprint's density-1/4 intersection.

U46 and U48-U56 remain useful independent arithmetic archives, but they are no longer the active route for eliminating this branch. U56 itself now contains an explicit correction notice pointing to U57.

## Coefficient-256 weighted branch

The unresolved explicit orientation is

`X^10+256Y^10=Z^17`.

`research/gaussian-descent/` preserves U15-U25 and U33-U39: Gaussian factorization, modular forcing primes, quadratic-field norm reduction, unit collapse, integral-basis identities, exact 5- and 17-adic locking, and moving-factor/cyclotomic coprimality results.

`research/modular-method/U40...` and `U41...` contain the later Frey/Hilbert modular attempt. **Do not count U41 as independently verified yet.** Its corrected route gives lowered level norm `2000` and a `q=11` trace sieve that eliminates the recorded eight Hilbert-newform orbits, but the following still need independent reconstruction:

1. the complete Hilbert newspace at the claimed level;
2. the adapted Breuil-Diamond/level-lowering bridge;
3. ideally the finite trace elimination with an independent Magma/Sage implementation or the authors' package.

Closing those obligations is the highest-value route to closing the entire currently reconstructed all-even `17|t` branch.

## All-even large-right-prime branch

If `17∤t`, every prime divisor of `t` is at least `19`. Choosing prime divisors of `r,s,t` reduces to

`X^(2l)+Y^(2m)=Z^p`,

with `l,m>=5` and `p>=19` prime.

This family is still genuinely unresolved in the current ledger. Modern effective/asymptotic results, including the preserved `p=19` literature, can bound large varying exponents for fixed right prime but do not yet remove the finite residual ranges or all right primes uniformly.

## Auxiliary unweighted modular-method study

`research/modular-method/U26` through `U31` analyze Michaud-Jacobs' unweighted equation

`x^(2l)+y^(2m)=z^17`.

U32 established that those files do not directly cover the weighted Beal equation; they remain method-development artifacts only.

## Current research priorities

1. **Independently certify or refute U41.** Success would close the currently reconstructed all-even `17|t` branch.
2. **Attack `17∤t`.** Start with the right-prime `19` finite residual problem and determine whether the effective bounds/S-unit steps are computationally executable with available exact tools.
3. **Continue global mixed-signature coverage.** Do not mistake all-even progress for the complete Beal conjecture.

## Durable recent checkpoints

- `checkpoints/U42_coverage_ledger_rebuild.md`
- `checkpoints/U43_all_even_chain_reconstruction.md`
- `checkpoints/U47_t_prime_coverage.md`
- `modular-method/U41_weighted_level2000_q11_elimination.md`
- `checkpoints/U48...` through `U56...` — independent coefficient-2 descent archive, now superseded for branch elimination
- `checkpoints/U57_coefficient2_closed_by_freitas_dieulefait.md` — authoritative coefficient-2 closure and literature correction
- `checkpoints/U100_all_even_17_does_not_divide_t_boundary_p19.md` — boundary case p=19, Frey representations, effective bounds, and coverage ledger for 17 ∤ t

## Conventions

- Preserve failed, corrected, and superseded routes; do not silently rewrite history.
- A computational certificate proves only its stated finite/exact assertion.
- External theorems must be recorded with hypotheses and checked against the exact branch where used.
- “Verified” inside an artifact means verified within its recorded evidence; it is not independent expert or proof-assistant certification of Beal.
- No partial branch elimination changes the global success status unless every Beal case is covered.
