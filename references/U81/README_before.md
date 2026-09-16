# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest checkpoint: U79 complete prime-2 condition

[U79](research/checkpoints/U79_complete_dyadic_Kummer_image.md) constructs actual local divisor classes and determines the full sixteen-dimensional Kummer image at the prime above 2 for U77's genus-eight Jacobian. With `s^17=2/phi`, an explicit basis consists of the squareclasses `1+s^n` and `1+phi*s^n` for odd n from 19 through 33.

Sixteen trace-divisor witnesses give an invertible binary certificate matrix. The norm-kernel restriction is an explicit sixteen-coordinate test. The nonzero global candidate `(s+1)/(1+s^17)`, which passed U78's prime-5 test, fails the new prime-2 test and is therefore excluded from the Selmer group.

**The global rank computation is not finished.** The class-group 2-rank, complete global candidate generators, and the restriction matrix on those generators remain uncomputed. No numerical rank upper bound, rank-zero theorem, weighted-equation elimination, or complete Beal solution is claimed.

The proof and complete Python/TypeScript arithmetic outputs agree; Wolfram verifies all sixteen square-congruence certificates and rank. Completeness uses a written local-divisor construction and the local index theorem, not a finite search alone. Independent expert or proof-assistant verification remains outstanding. The evidence package includes the unchanged U78 archive, actual logs, and replay records.

## Remaining global task and retained work

[U78](research/checkpoints/U78_explicit_descent_field_and_two_prime_criterion.md) provides the degree-34 descent field, a global candidate space of dimension `17+d`, and the explicit prime-5 condition. U79 now supplies the previously missing prime-2 subspace. To complete that descent, determine `d`, certify a full global basis, and evaluate the two local tests on it.

[U77](research/checkpoints/U77_anti_invariant_twist_reduction.md) gives the inherited implication from a positive primitive weighted solution to an infinite-order class on this Jacobian. It is not a rank-zero result. U71's common-root theorem and all subsequent applications retain their stated written/self-reviewed status.

U61/U62 concern a separate coefficient-two branch. **U41 remains invalidated by U63.** No unproved boundary congruence or incomplete modular prerequisite is reinstated. A rejected Selmer candidate is not automatically an excluded family of positive integer solutions.

The preceding index is preserved in [README before U79](references/U79/README_before.md). Earlier mathematical checkpoints were not overwritten.

## Original target

For positive integers A,B,C,x,y,z satisfying `A^x+B^y=C^z` and `x,y,z>=3`, prove `gcd(A,B,C)>1` or produce an independently verified counterexample. All bases and exponents remain unbounded. The weighted equation `X^10+256Y^10=Z^17` and the complete Beal conjecture remain unresolved.
