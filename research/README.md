# Research Index

## Current status

No complete proof or counterexample for Beal's conjecture has been verified.

## Active route

### Weighted Gaussian / quadratic-field descent

Primary current route. The latest scope checkpoint is `checkpoints/U32_weighted_branch_scope_correction.md`; the latest mathematically connected derivation is `gaussian-descent/U33_R_factor_coprimality.md`.

The surviving Beal-derived equation is

`X^10 + 256 Y^10 = Z^17`.

The coefficient `256` is essential and cannot be absorbed into an integral tenth power. U15–U25 give the core valid chain for this weighted equation: Gaussian factorization, reduction to the sole 17-adic Case III, mod-11 elimination of the other structural cases, forcing-prime information, factorization over `Q(sqrt(17))`, unit-class collapse, integral-basis equations, exact 17-adic root locking, and the coprime cyclotomic factorization of `gamma^5-(eta*delta)^5`.

U33 strengthens the active frontier by proving that the auxiliary cubic factor `R(a,b)` is coprime to the rational factors carrying the forced divisibility outside a finite exceptional set, and that `R` and its quadratic conjugate can share prime ideals only above `{2,11,13,17}`. Over `Q(sqrt(17),zeta_5)`, the five factors `gamma-zeta_5^i eta delta` are pairwise coprime away from 5, so every forcing prime outside `{2,5,17,19}` contributes its full tenth-power valuation to exactly one linear factor.

Current obligation: work in `L=Q(sqrt(17),zeta_5)`, determine the class-group/unit data needed to turn those linear-factor assignments into an explicit finite `S`-unit or Thue-Mahler system, with exceptional support above `{2,5,11,13,17,19}`.

### Auxiliary modular-method study

`modular-method/U26` through `U31` analyze the ell=5 obstruction in Michaud-Jacobs' *unweighted* equation

`x^(2l) + y^(2m) = z^17`.

Those files contain useful modular-method work, culminating in a reducibility argument for four Case-2 survivor forms, but U32 establishes that no proved reduction currently connects that unweighted Hilbert-newform problem to the weighted Beal branch `X^10+256Y^10=Z^17`. Therefore U26–U31 are retained as auxiliary method development and are **not** counted as elimination of the active Beal-derived branch.

Key correction: the earlier plan to classify the weighted branch as Michaud-Jacobs Case 1 or Case 2 was invalid; those cases belong to a different, unit-coefficient equation.

## Durable checkpoints

- `checkpoints/checkpoint-2026-09-14.md` — earlier modular-method state.
- `checkpoints/U32_weighted_branch_scope_correction.md` — current coverage correction and active-frontier reset.

## Conventions

- `U##_*` files are chronological research units, not claims of complete solution.
- A result marked verified means verified within the evidence stated in that artifact; it does not imply independent expert or formal verification of Beal's conjecture.
- Failed, blocked, or scope-invalidated routes are retained rather than deleted.
- Exact computations that materially support a theorem should record the expression, assumptions, arithmetic domain, and tool or code used.
- New research should be placed in the route-specific directory instead of directly under `research/`.
