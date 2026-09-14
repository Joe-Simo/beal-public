# Research Index

## Current status

No complete proof or counterexample for Beal's conjecture has been verified.

## Active routes

### Modular method

Primary current route. The latest checkpoint is `modular-method/U31_case2_residual_reducibility.md`.

The modular-method sequence is now:

- `U26_mod5_sigma_pairing_and_level_inventory.md` — reduces full Galois invariance to the paired residual congruences and inventories lower levels over the quartic field.
- `U27_coefficient_prime_over_5.md` — fixes the ramified residue-degree-one coefficient prime `(5,e+1)` for both survivor pairs.
- `U28_conditional_Q_descent_level34_contradiction.md` — conditionally eliminates the full-Galois-invariant branch when all three Hilbert-level primes remain ramified.
- `U29_quadratic_subfield_level_elimination.md` — eliminates every recorded parallel-weight-2 candidate over `Q(sqrt(17))` at level norms `1,2,4,17,34,68` by the forced q=13 trace, conditional on the modular linear-lift/conductor bridge.
- `U30_quadratic_subfield_conductor_correction.md` — corrects the possible 17-adic conductor exponent to at most two and extends the finite elimination through norms `289,578,1156`.
- `U31_case2_residual_reducibility.md` — closes the absolutely irreducible branch for the four Case-2 ell=5 survivor forms: the cyclotomic-irreducible case is eliminated by a Snowden minimal-conductor weight-two lift plus automorphy lifting and U29-U30, while the cyclotomic-reducible case is dihedral and contradicted by trace 0 versus the forced trace 4 at the two primes above 13. Therefore the four Case-2 residual representations are reducible.

Current obligation: determine whether the Beal-derived equation `X^10 + 256 Y^10 = Z^17` can enter Michaud-Jacobs' Case 1. The original paper notes additional ell=5 Case-1 obstructions, so U31 does not yet extend Theorem 3 to ell=5 or close the full Beal-derived branch. If Case 1 is needed, eliminate those surviving Case-1 forms; if the branch is provably Case-2-only, record that reduction explicitly.

Key supporting result: `modular-method/lemma-sigma2-conjugation-2026-09-14.md`.

### Gaussian / quadratic-field descent

Preserved in `gaussian-descent/`. U15–U25 progressively reduce and analyze the surviving equation

`X^10 + 256 Y^10 = Z^17`.

The route produced substantial divisibility, 17-adic, and coprimality structure but no contradiction. U24 shows the most obvious `gamma - eta*delta` infinite-descent idea is sharp rather than contradictory; U25 records the resulting cyclotomic factor split.

## Durable checkpoints

`checkpoints/checkpoint-2026-09-14.md` records the earlier modular-method research state, source dependencies, verified computations, and remaining obligations as of 2026-09-14. U26–U31 and the sigma2 lemma are the newer route-specific state and supersede that checkpoint where they are more precise.

## Conventions

- `U##_*` files are chronological research units, not claims of complete solution.
- A result marked verified means verified within the evidence stated in that artifact; it does not imply independent expert or formal verification of Beal's conjecture.
- Failed or blocked routes are retained rather than deleted.
- Exact computations that materially support a theorem should record the expression, assumptions, arithmetic domain, and tool or code used.
- New research should be placed in the route-specific directory instead of directly under `research/`.
