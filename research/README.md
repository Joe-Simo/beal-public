# Research Index

## Current status

No complete proof or counterexample for Beal's conjecture has been verified.

## Active routes

### Modular method

Primary current route. The latest checkpoint is `modular-method/U29_quadratic_subfield_level_elimination.md`.

The modular-method sequence is now:

- `U26_mod5_sigma_pairing_and_level_inventory.md` — reduces full Galois invariance to the paired residual congruences and inventories lower levels over the quartic field.
- `U27_coefficient_prime_over_5.md` — fixes the ramified residue-degree-one coefficient prime `(5,e+1)` for both survivor pairs.
- `U28_conditional_Q_descent_level34_contradiction.md` — conditionally eliminates the full-Galois-invariant branch when all three Hilbert-level primes remain ramified.
- `U29_quadratic_subfield_level_elimination.md` — eliminates every recorded parallel-weight-2 candidate over `Q(sqrt(17))` at level norms `1,2,4,17,34,68` by the forced q=13 trace, conditional on the modular linear-lift/conductor bridge.

Current obligations are: (1) certify the paired residual congruences `r ≃ s (mod λ)` and `v ≃ w (mod λ)` at the ramified prime `λ | 5`, preferably via a finite mod-5 Hecke-module multiplicity-one computation; or (2) complete the quadratic-subfield route by promoting projective mod-5 automorphy to the specific linear residual representation and verifying level optimization to its Artin conductor, including the local conductor behavior at the primes above 2 and 17.

Key supporting result: `modular-method/lemma-sigma2-conjugation-2026-09-14.md`.

### Gaussian / quadratic-field descent

Preserved in `gaussian-descent/`. U15–U25 progressively reduce and analyze the surviving equation

`X^10 + 256 Y^10 = Z^17`.

The route produced substantial divisibility, 17-adic, and coprimality structure but no contradiction. U24 shows the most obvious `gamma - eta*delta` infinite-descent idea is sharp rather than contradictory; U25 records the resulting cyclotomic factor split.

## Durable checkpoints

`checkpoints/checkpoint-2026-09-14.md` records the modular-method research state, source dependencies, verified computations, and remaining obligations as of 2026-09-14. U26–U29 and the sigma2 lemma are the newer route-specific state and supersede that checkpoint where they are more precise.

## Conventions

- `U##_*` files are chronological research units, not claims of complete solution.
- A result marked verified means verified within the evidence stated in that artifact; it does not imply independent expert or formal verification of Beal's conjecture.
- Failed or blocked routes are retained rather than deleted.
- Exact computations that materially support a theorem should record the expression, assumptions, arithmetic domain, and tool or code used.
- New research should be placed in the route-specific directory instead of directly under `research/`.
