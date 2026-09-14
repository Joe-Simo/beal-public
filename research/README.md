# Research Index

## Current status

No complete proof or counterexample for Beal's conjecture has been verified.

## Active routes

### Modular method

Primary current route. The latest checkpoint is `modular-method/U30_quadratic_subfield_conductor_correction.md`.

The modular-method sequence is now:

- `U26_mod5_sigma_pairing_and_level_inventory.md` — reduces full Galois invariance to the paired residual congruences and inventories lower levels over the quartic field.
- `U27_coefficient_prime_over_5.md` — fixes the ramified residue-degree-one coefficient prime `(5,e+1)` for both survivor pairs.
- `U28_conditional_Q_descent_level34_contradiction.md` — conditionally eliminates the full-Galois-invariant branch when all three Hilbert-level primes remain ramified.
- `U29_quadratic_subfield_level_elimination.md` — eliminates every recorded parallel-weight-2 candidate over `Q(sqrt(17))` at level norms `1,2,4,17,34,68` by the forced q=13 trace, conditional on the modular linear-lift/conductor bridge.
- `U30_quadratic_subfield_conductor_correction.md` — corrects the possible 17-adic conductor exponent to at most two, extends the finite elimination through norms `289,578,1156`, and closes the projective-to-linear automorphy/weight-2 portion of the quadratic-subfield bridge under absolute irreducibility. The remaining theorem-level gap is level optimization to the residual Artin conductor.

Current obligations are: (1) complete the quadratic-subfield route by verifying the exact Hilbert level-optimization theorem chain for the absolutely irreducible `G_K` extension, including the exceptional `Norm(v) ≡ 1 (mod 5)` case; or (2) certify the paired residual congruences `r ≃ s (mod λ)` and `v ≃ w (mod λ)` at the ramified prime `λ | 5` for the direct full-Galois route.

Key supporting result: `modular-method/lemma-sigma2-conjugation-2026-09-14.md`.

### Gaussian / quadratic-field descent

Preserved in `gaussian-descent/`. U15–U25 progressively reduce and analyze the surviving equation

`X^10 + 256 Y^10 = Z^17`.

The route produced substantial divisibility, 17-adic, and coprimality structure but no contradiction. U24 shows the most obvious `gamma - eta*delta` infinite-descent idea is sharp rather than contradictory; U25 records the resulting cyclotomic factor split.

## Durable checkpoints

`checkpoints/checkpoint-2026-09-14.md` records the modular-method research state, source dependencies, verified computations, and remaining obligations as of 2026-09-14. U26–U30 and the sigma2 lemma are the newer route-specific state and supersede that checkpoint where they are more precise.

## Conventions

- `U##_*` files are chronological research units, not claims of complete solution.
- A result marked verified means verified within the evidence stated in that artifact; it does not imply independent expert or formal verification of Beal's conjecture.
- Failed or blocked routes are retained rather than deleted.
- Exact computations that materially support a theorem should record the expression, assumptions, arithmetic domain, and tool or code used.
- New research should be placed in the route-specific directory instead of directly under `research/`.
