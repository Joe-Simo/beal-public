# Research Index

## Current status

No complete proof or counterexample for Beal's conjecture has been verified.

## Active route

### Weighted Gaussian / quadratic-field descent

Primary current route. The latest scope checkpoint is `checkpoints/U32_weighted_branch_scope_correction.md`; the latest mathematically connected derivation is `gaussian-descent/U39_J_cyclotomic_allocation.md`.

The surviving Beal-derived equation is

`X^10 + 256 Y^10 = Z^17`.

The coefficient `256` is essential and cannot be absorbed into an integral tenth power. U15–U25 give the core valid chain for this weighted equation: Gaussian factorization, reduction to the sole 17-adic Case III, mod-11 elimination of the other structural cases, forcing-prime information, factorization over `Q(sqrt(17))`, unit-class collapse, integral-basis equations, exact 17-adic root locking, and the coprime cyclotomic factorization of `gamma^5-(eta*delta)^5`.

U33 proves that the auxiliary cubic factor `R(a,b)` is coprime to the rational factors carrying the forced divisibility outside a finite exceptional set, and that `R` and its quadratic conjugate can share prime ideals only above `{2,11,13,17}`. Over `Q(sqrt(17),zeta_5)`, the five factors `gamma-zeta_5^i eta delta` are pairwise coprime away from 5, so every forcing prime outside `{2,5,17,19}` contributes its full tenth-power valuation to exactly one linear factor.

U34 determines the arithmetic of `L=Q(sqrt(17),zeta_5)`: degree 8, discriminant `5^6*17^4`, conductor 85, Galois group `C4 x C2`, class number 1, roots-of-unity group of order 10, and unit rank 3. It also shows that the hoped-for fixed-`S` tenth-power reduction does **not** yet follow because the moving factor `R(a,b)` can introduce primes outside the fixed exceptional set with valuations not known to be multiples of 10.

U35 computes the exact rational norm polynomial of `R`, its discriminant, and exact resultants against the rational fifth-power forms `G` and `H`; these restrict simultaneous divisibility but do not force the moving `R`-primes into fifth- or tenth-power valuations.

U36 exploits the exact factorizations of `G-H` and `G+H`. Writing `U=(G-H)/2` and `V=(G+H)/2` gives `gcd(U,V)=1`, `U+V=C^5`, `V-U=17D^5`, with `U` and `V` factored into eight low-degree odd binary forms. The four factors on the `U` side are pairwise coprime and are coprime to every factor on the `V` side; the only possible overlap among the four `V` factors is an explicitly controlled factor `3` in one of two pairs.

U37 refines the `U`-side further: the apparent degree-4 and degree-8 norm factors split over `Q`, giving six pairwise-coprime odd factors of degrees `2,2,2,2,4,4`, so the 2-power norm tower alone does not create fifth-power ideal exponents. More importantly, an exact modulo-25 computation proves that every global Case-III solution has `5|B` and `5∤A`. Since 5 is inert in `Q(sqrt(17))`, U37 derives sharp 5-adic root locking at precision `5^(10 v5(B)-1)`: `v5(v)=10v5(B)-1`, `v5(r)=1`, `v5(s)=0`, and `v5(gamma-eta*delta)=10v5(B)-1`, with explicit first-order residues.

U38 translates the simultaneous 5-/17-adic locking to rational norms. It obtains exact valuations of `C-A^16`, `D-A^16`, and `C-D`, and the identity

`(C-D) Phi_5(C,D) = -2^13 * 17^7 * B^10 * J(a,b)`

for an explicit degree-14 form `J`. The discriminant of the dehomogenized J-polynomial is supported only at `{2,3,17}`, and exact resultants show that odd J-primes away from 17 are disjoint from `CD`.

U39 sharpens the cyclotomic allocation of J-primes. If `q != 5,17` divides `J(a,b)` and `q != 1 (mod 5)`, then necessarily `q | C-D`; only primes `q == 1 (mod 5)` can enter `Phi_5(C,D)`. U39 also proves the exact local facts

- `v2(C-D)=13+10 v2(B)`,
- `v5(J)=0`,
- `v17(J)=1`,

and confirms by exact finite-field search that the `q == 1 (mod 5)` branch is locally genuine, so it cannot be discarded by a simple congruence argument.

Current obligation: isolate the remaining `q == 1 (mod 5)` prime divisors of `J` that may enter `Phi_5(C,D)`. Priority routes are fifth-power reciprocity/residue-symbol constraints using the special tenth-power parameter `t=2^8*17^8(B/A)^10`, an independent factorization of `J` controlling exactly those primes, or—if this stalls—a Frey construction genuinely adapted to `U^5+8V^5=Z^17`.

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
