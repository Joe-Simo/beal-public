# Research Index

## Current status

No complete proof or counterexample for Beal's conjecture has been verified.

## Active routes

### Modular method

Primary current route. The latest checkpoint is `modular-method/U26_mod5_sigma_pairing_and_level_inventory.md`.

Current obligation: certify the paired residual congruences `r ≃ s (mod λ)` and `v ≃ w (mod λ)` at the ramified prime `λ | 5`, preferably via a finite mod-5 Hecke-module multiplicity-one computation. If that is unavailable, pursue rigorous conductor/level-lowering elimination against the finite lower-level inventory.

Key supporting result: `modular-method/lemma-sigma2-conjugation-2026-09-14.md`.

### Gaussian / quadratic-field descent

Preserved in `gaussian-descent/`. U15–U25 progressively reduce and analyze the surviving equation

`X^10 + 256 Y^10 = Z^17`.

The route produced substantial divisibility, 17-adic, and coprimality structure but no contradiction. U24 shows the most obvious `gamma - eta*delta` infinite-descent idea is sharp rather than contradictory; U25 records the resulting cyclotomic factor split.

## Durable checkpoints

`checkpoints/checkpoint-2026-09-14.md` records the modular-method research state, source dependencies, verified computations, and remaining obligations as of 2026-09-14.

## Conventions

- `U##_*` files are chronological research units, not claims of complete solution.
- A result marked verified means verified within the evidence stated in that artifact; it does not imply independent expert or formal verification of Beal's conjecture.
- Failed or blocked routes are retained rather than deleted.
- Exact computations that materially support a theorem should record the expression, assumptions, arithmetic domain, and tool or code used.
- New research should be placed in the route-specific directory instead of directly under `research/`.
