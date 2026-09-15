# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest mathematical checkpoint

[U62: coefficient-two theorem and exact Beal coverage](research/checkpoints/U62_coefficient_two_coverage.md) supplies the complete upstream implication into [U61's auxiliary exclusion](research/checkpoints/U61_elliptic_chabauty_auxiliary_exclusion.md).

At the complete-written-proof level, the resulting partial claims are:

- The only positive solution of `X^10+Y^10=2Z^17` with `gcd(X,Y)=1` is `(1,1,1)`.
- There is no primitive positive solution of `E^(2r)+O^(10k)=C^(34l)` with `r>=2`, `k,l>=1`, **E even and O odd**.

The second statement is parity-specific. It does not settle the reversed parity orientation, the weighted equation `X^10+256Y^10=Z^17`, all all-even signatures, or the complete conjecture.

**Verification:** same-model written proof and adversarial self-review, established-source checking, and distinct exact arithmetic implementations. U61 computations were replayed in U62. Independent expert and proof-assistant verification remain outstanding. The precise dependencies are in the manuscripts; successful code execution does not replace them. No novelty, publication, acceptance or prize award is claimed.

## Evidence and continuity

[U60](research/checkpoints/U60_audit_and_mod289_reduction.md) records corrections to U57-U59; their historical restricted square-residue tables must not be reused as complete pruning rules. U61 establishes the auxiliary exclusion. U62 checks all upstream hypotheses, including the boundary `(1,1,1)`, the ramified prime over 5, coordinate coprimality, units, signs, and full-scale split-algebra images.

Exact source code is under `code/`, computation records under `research/computations/`, and checked source information under `references/`. The local evidence archive also retains historical outputs and the old U61 patch. `U62_preservation.json` records which files were actually copied to the remote; an old checkpoint's then-current write limitation is historical, not a current capability claim.

Next mathematical task: audit the weighted orientation from its actual preserved Frey-curve and level-lowering assumptions. Do not repeat a completed finite sieve as though it were new progress. Independent verification of U61 remains a separate priority.

## Original target

For positive integers A,B,C,x,y,z satisfying `A^x+B^y=C^z` with `x,y,z>=3`, prove `gcd(A,B,C)>1`, or exhibit and independently verify a counterexample. No partial result here is a complete resolution of that target.
