# Research Index

## Current status

No complete proof or counterexample for Beal's conjecture has been verified.

## Active route

### Weighted Gaussian / quadratic-field descent

Primary current route. The latest scope checkpoint is `checkpoints/U32_weighted_branch_scope_correction.md`; the latest mathematically connected derivation is `gaussian-descent/U36_sum_difference_coprime_factorization.md`.

The surviving Beal-derived equation is

`X^10 + 256 Y^10 = Z^17`.

The coefficient `256` is essential and cannot be absorbed into an integral tenth power. U15–U25 give the core valid chain for this weighted equation: Gaussian factorization, reduction to the sole 17-adic Case III, mod-11 elimination of the other structural cases, forcing-prime information, factorization over `Q(sqrt(17))`, unit-class collapse, integral-basis equations, exact 17-adic root locking, and the coprime cyclotomic factorization of `gamma^5-(eta*delta)^5`.

U33 proves that the auxiliary cubic factor `R(a,b)` is coprime to the rational factors carrying the forced divisibility outside a finite exceptional set, and that `R` and its quadratic conjugate can share prime ideals only above `{2,11,13,17}`. Over `Q(sqrt(17),zeta_5)`, the five factors `gamma-zeta_5^i eta delta` are pairwise coprime away from 5, so every forcing prime outside `{2,5,17,19}` contributes its full tenth-power valuation to exactly one linear factor.

U34 determines the arithmetic of `L=Q(sqrt(17),zeta_5)`: degree 8, discriminant `5^6*17^4`, conductor 85, Galois group `C4 x C2`, class number 1, roots-of-unity group of order 10, and unit rank 3. It also shows that the hoped-for fixed-`S` tenth-power reduction does **not** yet follow because the moving factor `R(a,b)` can introduce primes outside the fixed exceptional set with valuations not known to be multiples of 10.

U35 computes the exact rational norm polynomial of `R`, its discriminant, and exact resultants against the rational fifth-power forms `G` and `H`; these restrict simultaneous divisibility but do not force the moving `R`-primes into fifth- or tenth-power valuations.

U36 exploits the exact factorizations of `G-H` and `G+H`. Writing `U=(G-H)/2` and `V=(G+H)/2` gives `gcd(U,V)=1`, `U+V=C^5`, `V-U=17D^5`, with `U` and `V` factored into eight low-degree odd binary forms. The four factors on the `U` side are pairwise coprime and are coprime to every factor on the `V` side; the only possible overlap among the four `V` factors is an explicitly controlled factor `3` in one of two pairs. This yields a primitive eight-factor decomposition but not yet separate fifth-power equations.

Current obligation: exploit the norm-tower interpretation of the U36 factors, especially `d3` and `d4` over the 2-power cyclotomic tower, to see whether `a=A^5` and `b=16*17^4 B^5` force fifth-power ideal structure; otherwise pivot to a Frey construction genuinely adapted to `U^5+8V^5=Z^17`.

### Auxiliary modular-method study

`modular-method/U26` through `U31` analyze the ell=5 obstruction in Michaud-Jacobs' *unweighted* equation

`x^(2l) + y^(2m) = z^17`.

Those files contain useful modular-method work, but U32 establishes that no proved reduction currently connects that unweighted Hilbert-newform problem to the weighted Beal branch `X^10+256Y^10=Z^17`. Therefore U26–U31 are retained as auxiliary method development and are **not** counted as elimination of the active Beal-derived branch.

## Durable checkpoints

- `checkpoints/checkpoint-2026-09-14.md` — earlier modular-method state.
- `checkpoints/U32_weighted_branch_scope_correction.md` — current coverage correction and active-frontier reset.

## Conventions

- `U##_*` files are chronological research units, not claims of complete solution.
- A result marked verified means verified within the evidence stated in that artifact; it does not imply independent expert or formal verification of Beal's conjecture.
- Failed, blocked, or scope-invalidated routes are retained rather than deleted.
- Exact computations that materially support a theorem should record the expression, assumptions, arithmetic domain, and tool or code used.
- New research should be placed in the route-specific directory instead of directly under `research/`.
