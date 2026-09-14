# Research Index

## Current status

No complete proof or counterexample for Beal's conjecture has been verified.

## Active route

### Direct weighted Frey genus-2 route

Primary current route. The latest scope checkpoint is `checkpoints/U32_weighted_branch_scope_correction.md`; the latest mathematically connected modular checkpoint is `modular-method/U40_weighted_frey_genus2_route.md`.

The surviving Beal-derived equation is

`X^10 + 256 Y^10 = Z^17`.

Set `U=X^2`, `V=2Y^2`. Then the active equation is exactly

`U^5 + 8 V^5 = Z^17`,

with `gcd(U,V)=1`.

U40 identifies a current Frey construction that genuinely allows non-unit fixed coefficients `A,B,C` in equations `A a^5+B b^5=C c^p`. For `(A,B,C,p)=(1,8,1,17)` it gives the genus-2 Frey curve

`y^2 = x^5 - 40 U V x^3 + 320 U^2 V^2 x + 64(8 V^5-U^5)`.

Its Jacobian has real multiplication by `Q(sqrt(5))`, yielding a 2-dimensional mod-17 representation. The source supplies modularity, irreducibility criteria, and level lowering for this weighted `(5,5,p)` framework. The exact specialized lowered level and complete newform elimination are still unverified obligations.

Exact Wolfram computation gives the specialized hyperelliptic polynomial discriminant

`2^24 * 5^5 * (U^10 - 48 U^5 V^5 + 64 V^10)^2`.

The naive curve discriminant therefore has moving support, so the source's representation-theoretic conductor and level-lowering analysis must be used; no fixed level is inferred from the raw discriminant.

The Beal-derived parity is favorable at 2: `U,Z` are odd and `V` is even, so for `s0=U^5/Z^17`, one has `v2(s0)=0` and `v2(s0-1)=3+5v2(V)>=8`.

Current obligation: specialize Theorem 5.23 and Tables 2/3 completely for `A=1,B=8,C=1,r=5,p=17`, verify unconditional residual irreducibility in this exact specialization, determine the finite lowered level(s) over `Q(sqrt(5))`, enumerate all parallel-weight-2 Hilbert newforms there, and eliminate them by exact mod-17 trace comparisons.

### Weighted Gaussian / quadratic-field descent

Preserved as the strongest auxiliary arithmetic route. U15–U25 give the core valid chain for `X^10+256Y^10=Z^17`: Gaussian factorization, reduction to the sole 17-adic Case III, mod-11 elimination of the other structural cases, forcing-prime information, factorization over `Q(sqrt(17))`, unit-class collapse, integral-basis equations, exact 17-adic root locking, and the coprime cyclotomic factorization of `gamma^5-(eta*delta)^5`.

U33–U39 further develop the auxiliary arithmetic: moving-factor coprimality, class-number-one arithmetic of `Q(sqrt(17),zeta_5)`, exact norm/resultant identities, low-degree sum/difference factorizations, sharp 5-adic and 17-adic locking, and the cyclotomic allocation of the degree-14 factor `J(a,b)`.

In particular U39 proves that if `q != 5,17` divides `J(a,b)` and `q != 1 (mod 5)`, then `q | C-D`; only `q == 1 (mod 5)` may enter `Phi_5(C,D)`. It also proves `v2(C-D)=13+10v2(B)`, `v5(J)=0`, and `v17(J)=1`.

An exact differential identity found while transitioning to U40 is

`h(t) = g(t) - (2/17)(1+t)g'(t)`

and hence

`h(t)-17g(t)=32t J(t)`.

This confirms that the J-prime allocation problem is intrinsic to the 17th-power Gaussian structure, but local fifth-power residue conditions alone do not eliminate the `q == 1 (mod 5)` branch.

### Auxiliary unweighted modular-method study

`modular-method/U26` through `U31` analyze the ell=5 obstruction in Michaud-Jacobs' *unweighted* equation

`x^(2l) + y^(2m) = z^17`.

Those files contain useful modular-method work, but U32 establishes that no proved reduction connects that unweighted Hilbert-newform problem to the weighted Beal branch. They are retained as method development and are **not** counted as elimination of the active weighted branch.

## Durable checkpoints

- `checkpoints/checkpoint-2026-09-14.md` — earlier modular-method state.
- `checkpoints/U32_weighted_branch_scope_correction.md` — coverage correction and active-frontier reset.
- `modular-method/U40_weighted_frey_genus2_route.md` — direct weighted Frey construction and current modular obligations.

## Conventions

- `U##_*` files are chronological research units, not claims of complete solution.
- A result marked verified means verified within the evidence stated in that artifact; it does not imply independent expert or formal verification of Beal's conjecture.
- Failed, blocked, or scope-invalidated routes are retained rather than deleted.
- Exact computations that materially support a theorem should record the expression, assumptions, arithmetic domain, and tool or code used.
- New research should be placed in the route-specific directory instead of directly under `research/`.
