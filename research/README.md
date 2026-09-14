# Research Index

## Current status

No complete proof or counterexample for Beal's conjecture has been verified.

## Active routes

### Modular method

Primary current route. The latest checkpoint is `modular-method/U27_conditional_Q_descent_level34_contradiction.md`.

U27 conditionally closes the full-Galois-invariant, absolutely irreducible branch when the residual representation remains ramified at both primes over 2 and the unique prime over 17: descent to `G_Q`, twisting, and Serre modularity force the unique weight-2 level-34 trivial-character newform, but its `a_13 = 2` contradicts the survivor trace `a_Q ≡ 4 (mod λ)` for every `Q|13`.

Current obligations remain: (1) certify the paired residual congruences `r ≃ s (mod λ)` and `v ≃ w (mod λ)` at the ramified prime `λ | 5`, preferably via a finite mod-5 Hecke-module multiplicity-one computation; and (2) prove that residual ramification at the Hilbert-level primes cannot drop, or enumerate and eliminate the resulting lower-conductor classical branches.

Key supporting results: `modular-method/U26_mod5_sigma_pairing_and_level_inventory.md` and `modular-method/lemma-sigma2-conjugation-2026-09-14.md`.

### Gaussian / quadratic-field descent

Preserved in `gaussian-descent/`. U15–U25 progressively reduce and analyze the surviving equation

`X^10 + 256 Y^10 = Z^17`.

The route produced substantial divisibility, 17-adic, and coprimality structure but no contradiction. U24 shows the most obvious `gamma - eta*delta` infinite-descent idea is sharp rather than contradictory; U25 records the resulting cyclotomic factor split.

## Durable checkpoints

`checkpoints/checkpoint-2026-09-14.md` records the modular-method research state, source dependencies, verified computations, and remaining obligations as of 2026-09-14. U27 should be read as the newer route-specific state for the conditional Q-descent branch.

## Conventions

- `U##_*` files are chronological research units, not claims of complete solution.
- A result marked verified means verified within the evidence stated in that artifact; it does not imply independent expert or formal verification of Beal's conjecture.
- Failed or blocked routes are retained rather than deleted.
- Exact computations that materially support a theorem should record the expression, assumptions, arithmetic domain, and tool or code used.
- New research should be placed in the route-specific directory instead of directly under `research/`.
