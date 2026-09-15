# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest checkpoint: U78 explicit descent field and two-prime criterion

[U78](research/checkpoints/U78_explicit_descent_field_and_two_prime_criterion.md) proves the integral basis, discriminant, and complete relevant prime decomposition of the degree-34 field for U77's genus-eight Jacobian. The integer ring is `Z[phi,s]`, where `s^17=2/phi`; its discriminant is `2^32*5^17*17^34` and its index over `Z[s]` is `2^17`.

It gives an exact 2-descent formulation: a global candidate space of dimension `17+d`, where `d` is the **uncomputed** class-group 2-rank, maps to a local quotient of dimension seventeen. Only the primes above 2 and 5 remain in this map. The local condition at 5 is solved explicitly; at 2 the image dimension is proved but its basis remains uncomputed.

**No rank-zero result or numerical rank upper bound is established.** The class-group contribution, complete global generators, dyadic Kummer image, and global restriction matrix still need computation. Proving `d=0` and full rank of that matrix would rule out the weighted branch through U77, but neither is claimed here. No new weighted solution case or complete Beal signature is eliminated.

Python's symbolic discriminants and TypeScript's trace/multiplication matrices agree on the complete exact certificate output. Wolfram corroborates the field and local arithmetic. A public Magma call returned the same constructed-order data, not maximality or a rank; the maximality argument is written in the proof. The rank request timed out. Unsuccessful or blocked requests supplied no mathematical conclusions.

The manuscript, both verifiers, offline replay script, sources, and core records are preserved. Verification remains written same-model review with distinct arithmetic checks, not independent expert or proof-assistant certification. The evidence archive also retains the unchanged U77 archive and complete replay logs.

## Retained target and corrections

[U77](research/checkpoints/U77_anti_invariant_twist_reduction.md) proves that a positive primitive solution of `X^10+256Y^10=Z^17` would give an infinite-order class on the Jacobian of `(3-phi)w^2=phi^2-4u^17` over `Q(sqrt(5))`. Its nonzero-class argument, not an unproved rank claim, is the upstream weighted implication used here.

U71 supplies the common-root theorem. U75/U76's known subgroups do not exhaust U77's extension component. U68-U72's large lower bounds are not upper bounds or impossibility proofs. U61/U62 retain their separate coefficient-two scope and verification obligations. **U41 remains invalidated by U63.** No boundary congruence or incomplete modular prerequisite is reinstated.

The previous research index is retained unchanged in [README before U78](references/U78/README_before.md). No earlier mathematical checkpoint was overwritten.

## Original target

For positive integers A,B,C,x,y,z with `A^x+B^y=C^z` and `x,y,z>=3`, prove `gcd(A,B,C)>1` or exhibit an independently verified counterexample. All bases and exponents remain unbounded. The weighted equation and the full Beal conjecture remain unresolved.
