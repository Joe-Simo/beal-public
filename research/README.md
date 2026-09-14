# Research Index

## Current status

No complete proof or counterexample for Beal's conjecture has been verified.

## Authoritative global coverage state

The current coverage ledger is `checkpoints/U42_coverage_ledger_rebuild.md`, followed by the partial all-even reconstruction `checkpoints/U43_all_even_chain_reconstruction.md`.

These supersede earlier informal claims about how much of Beal's conjecture was covered. In particular, the repository does not contain the former U1-U14 derivations, so claims depending on those missing files are not credited globally unless rebuilt from elementary arguments or primary sources.

### Universally valid reductions now preserved

For a primitive counterexample:

- the three bases are pairwise coprime;
- a base equal to 1 is impossible by Catalan-Mihailescu;
- each exponent may be reduced independently to either 4 or an odd prime while preserving a primitive solution;
- `gcd(x,y,z)` cannot have a divisor at least 3, by Fermat's Last Theorem, so `gcd(x,y,z)` is 1 or 2;
- if all three exponents are even, writing `x=2r`, `y=2s`, `z=2t` gives the reconstructed primitive Pythagorean system in U42-U43.

This still leaves infinitely many mixed signatures, including signatures involving exponent 4 and triples of distinct odd primes.

## All-even branch reconstruction

U43 proves directly that any primitive all-even solution can be written

`A^r=2mn`, `B^s=m^2-n^2`, `C^t=m^2+n^2`,

with `m,n` coprime of opposite parity, and then

`m-n=u^s`, `m+n=v^s`,

`{m,n}={a^r,2^(r-1)b^r}`.

Hence

`C^t=a^(2r)+2^(2r-2)b^(2r)`

and

`2C^t=u^(2s)+v^(2s)`.

Published generalized-Fermat results then give the following conditional step: if `17|t` and every prime divisor of `r` and `s` is at least 5, Michaud-Jacobs Theorem 3 forces one of `r,s` to be a pure power of 5.

The two orientations are reconstructed exactly:

- if `s` is a 5-power, one obtains `X^10+Y^10=2Z^17`;
- if `r` is a 5-power, one obtains `X^10+256Y^10=Z^17`.

The two remaining obligations in this chain are explicit:

1. prove from preserved evidence/primary sources that `r` and `s` have no prime factors 2 or 3;
2. eliminate the coefficient-2 orientation `X^10+Y^10=2Z^17` (the previously cited 2011 Q-curve theorem does not automatically cover exponent 17).

## Weighted `(10,10,17)` subbranch — candidate elimination completed, verification still open

The latest mathematically connected modular checkpoint is `modular-method/U41_weighted_level2000_q11_elimination.md`.

For the weighted equation

`X^10 + 256 Y^10 = Z^17`,

writing `U=X^2`, `V=2Y^2` gives

`U^5 + 8 V^5 = Z^17`.

U41 corrects U40's Frey-model sign and local-parameter errors and obtains a candidate elimination via a genus-2 Frey Jacobian over `Q(sqrt(5))`, corrected lowered level norm `2000`, an eight-orbit Hilbert-newform inventory, and a q=11 trace sieve eliminating all eight candidates in both good and toric cases.

Remaining verification obligations for U41:

1. independently reconstruct the full Hilbert newspace at level `(2)^2*r_5^3` with Magma/Sage or another implementation; the present finite-space completeness claim uses LMFDB;
2. independently audit the Breuil-Diamond level-lowering adaptation replacing Azon's packaged Hypothesis-5 route;
3. reproduce the q=11 elimination with the authors' Magma package when an appropriate runtime is available.

Until the U43 prerequisites are closed, U41 is not counted as eliminating the entire all-even `17|t` branch.

## Weighted Gaussian / quadratic-field descent

U15-U25 and U33-U39 remain preserved as independent arithmetic work on `X^10+256Y^10=Z^17`: Gaussian factorization, mod-11 structural elimination, quadratic-field norm reduction, unit-class collapse, integral-basis equations, exact 5- and 17-adic locking, moving-factor coprimality, and cyclotomic allocation restrictions.

These support the weighted branch but do not replace the global coverage obligations in U42-U43.

## Auxiliary unweighted modular-method study

`modular-method/U26` through `U31` analyze Michaud-Jacobs' unweighted equation

`x^(2l) + y^(2m) = z^17`.

U32 established that those files do not directly cover the weighted Beal equation; they remain method-development artifacts only.

## Current research priority

1. Close or refute the U43 prerequisite excluding prime factors 2 and 3 from `r,s` in the all-even branch.
2. Resolve the coefficient-2 orientation `X^10+Y^10=2Z^17`.
3. Independently certify U41.
4. Then reassess the remaining all-even cases, especially `17∤t`, before returning to the much larger mixed-parity signature space.

## Durable checkpoints

- `checkpoints/U42_coverage_ledger_rebuild.md` — authoritative global coverage ledger.
- `checkpoints/U43_all_even_chain_reconstruction.md` — reconstructed all-even/17-divisible chain and explicit remaining gaps.
- `checkpoints/U32_weighted_branch_scope_correction.md` — correction separating the weighted branch from the unweighted Michaud-Jacobs problem.
- `modular-method/U40_weighted_frey_genus2_route.md` — superseded route-construction checkpoint; see its correction notice.
- `modular-method/U41_weighted_level2000_q11_elimination.md` — corrected weighted level and finite newform elimination.

## Conventions

- `U##_*` files are chronological research units, not claims of complete solution.
- A result marked verified means verified within the evidence stated in that artifact; it does not imply independent expert or formal verification of Beal's conjecture.
- Failed, blocked, or scope-invalidated routes are retained rather than deleted.
- Exact computations that materially support a theorem record the expression, assumptions, arithmetic domain, and tool or code used.
- New research belongs in the route-specific directory rather than directly under `research/`.
