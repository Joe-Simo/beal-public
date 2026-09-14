# Research Index

## Current status

No complete proof or counterexample for Beal's conjecture has been verified.

## Active frontier

### Weighted `(10,10,17)` subbranch — candidate elimination completed, verification still open

The latest mathematically connected checkpoint is `modular-method/U41_weighted_level2000_q11_elimination.md`.

The Beal-derived weighted equation is

`X^10 + 256 Y^10 = Z^17`.

Writing `U=X^2`, `V=2Y^2` gives the genuine weighted generalized Fermat equation

`U^5 + 8 V^5 = Z^17`,

with `gcd(U,V)=1`, `U,Z` odd, and `V` even.

U40 first identified the applicable 2025 weighted Frey genus-2 framework, but U41 found and corrected two material U40 errors: the source Frey polynomial has `+40UVx^3` rather than `-40UVx^3`, and the correct `(r,r,p)` local parameter gives

`nu_q = 34 v_q(Z) - v_q(128 U^5 V^5)`.

U40 is retained only as a superseded historical checkpoint.

U41 specializes the corrected Frey construction over `K=Q(sqrt(5))` and obtains:

- absolute residual irreducibility from Azon Proposition 5.20 at the prime above 2;
- local conductor exponent `n_2=2`;
- an exact modulo-125 computation on all 793 square-shaped residue pairs proving the relevant degree-5 polynomial has no `Q_5` root, hence `n_5=3`;
- good reduction at the residual prime 17;
- removal of solution-dependent primes after level lowering;
- corrected target level

  `(2)^2 * r_5^3`, of norm `2000`;

- an LMFDB inventory of exactly eight parallel-weight-2 newform orbits at level `2000.1`;
- an independent exact Wolfram computation of all possible Frey RM trace polynomials at `q=11`;
- elimination of all eight newforms modulo 17 in both the good-reduction and toric `11|Z` cases.

The packaged level-lowering theorem in Azon's paper is not invoked outside its stated hypotheses. U41 instead records a theorem-chain adaptation using Azon's unconditional modularity, Proposition 5.20, a direct Clifford/local argument proving irreducibility after restriction to `K(sqrt(17))`, good reduction at 17, Theorem 5.21, and Breuil–Diamond Theorem 3.2.2.

Within those stated dependencies, U41 eliminates the remaining weighted `(10,10,17)` equation arising from the all-even `17|t` branch. This is **not** a solution of Beal's conjecture.

Remaining verification obligations for U41:

1. independently reconstruct the full Hilbert newspace at level `(2)^2*r_5^3` with Magma/Sage or another implementation; the present finite-space completeness claim uses LMFDB;
2. independently audit the Breuil–Diamond level-lowering adaptation replacing Azon's packaged Hypothesis-5 route;
3. reproduce the q=11 elimination with the authors' Magma package when an appropriate runtime is available.

### Weighted Gaussian / quadratic-field descent

Preserved as supporting arithmetic for U41. U15–U25 give the core valid chain for `X^10+256Y^10=Z^17`: Gaussian factorization, reduction to the sole 17-adic Case III, mod-11 elimination of the other structural cases, forcing-prime information, factorization over `Q(sqrt(17))`, unit-class collapse, integral-basis equations, exact 17-adic root locking, and the coprime cyclotomic factorization of `gamma^5-(eta*delta)^5`.

U33–U39 further give moving-factor coprimality, exact norm/resultant identities, sharp 5-adic and 17-adic locking, and cyclotomic allocation restrictions. These remain useful independent consistency checks on the weighted branch even though U41 is now the strongest elimination route.

### Auxiliary unweighted modular-method study

`modular-method/U26` through `U31` analyze the ell=5 obstruction in Michaud-Jacobs' *unweighted* equation

`x^(2l) + y^(2m) = z^17`.

U32 establishes that these do not directly cover the weighted Beal branch. They are retained as method development and are not counted as elimination of the active weighted equation.

## Next coverage obligation

Return to the Beal coverage ledger. U41 concerns only the all-even branch in which `17|t` and the surviving orientation reduces to `X^10+256Y^10=Z^17`. Determine exactly which all-even cases remain when `17` does not divide `t` (recall all prime divisors of `t` are at least 17) and which non-all-even exponent patterns remain from the original Beal statement. Do not infer full coverage from U41.

## Durable checkpoints

- `checkpoints/checkpoint-2026-09-14.md` — earlier modular-method state.
- `checkpoints/U32_weighted_branch_scope_correction.md` — correction separating the weighted branch from the unweighted Michaud-Jacobs problem.
- `modular-method/U40_weighted_frey_genus2_route.md` — superseded route-construction checkpoint; see its correction notice.
- `modular-method/U41_weighted_level2000_q11_elimination.md` — corrected weighted level and finite newform elimination.

## Conventions

- `U##_*` files are chronological research units, not claims of complete solution.
- A result marked verified means verified within the evidence stated in that artifact; it does not imply independent expert or formal verification of Beal's conjecture.
- Failed, blocked, or scope-invalidated routes are retained rather than deleted.
- Exact computations that materially support a theorem record the expression, assumptions, arithmetic domain, and tool or code used.
- New research belongs in the route-specific directory rather than directly under `research/`.
