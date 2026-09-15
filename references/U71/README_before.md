# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest checkpoint: U69

[U69: joint scalar-quotient obstruction](research/checkpoints/U69_joint_scalar_quotient_obstruction.md) combines restrictions on the same quintic and Gaussian roots. Through U65's preserved pure-root implication, any positive primitive solution of `X^10+256Y^10=Z^17` requires a prime-power product exceeding `10^453` supported on seven classes modulo 340, with an additional fifth-residue condition for 2 in class 1.

This narrows the unavoidable exceptional support. It does not forbid every other prime divisor, give that lower bound for a single prime, or increase U68's base-height threshold. The bounds are `S_Q<sqrt(17) T^(1/17)` and `S_G<T^(2/17)`, with shared support retained when combining them.

U69 also proves compatible nonscalar roots with the same norm exist at every 137-adic precision. The example modulo `137^12` is checked in Python, TypeScript and Wolfram. These are local solutions, not integer solutions or Beal counterexamples; simultaneous norms alone do not force scalar roots.

The proof, exact checkers, reproduction commands, source mapping and compact certificates are preserved. **Verification is same-model review plus distinct arithmetic checks, not independent expert or proof-assistant certification.** The weighted equation remains unresolved. The next obligation is global control of the jointly exceptional choices for one integral root, or an effective upper bound; neither is supplied here.

## Retained results and corrections

[U68](research/checkpoints/U68_global_coefficient_height_obstruction.md) gives `max(X,Y)>10^514` and a broader exceptional prime-power product exceeding `10^483`, under the preserved quintic descent. These are lower bounds for the weighted equation, not for every possible Beal counterexample.

[Quintic U65](research/checkpoints/U65_weighted_quintic_unit_elimination.md) supplies the pure seventeenth-power equation and removes its unit ambiguity. [U67](research/checkpoints/U67_unconditional_Kummer_obstructions.md) supplies boundary-independent Kummer restrictions. These are written/self-reviewed partial results. The boundary congruence and outstanding global modular prerequisites remain unproved; only one candidate survives in the recorded eight-orbit modular list.

U61/U62 retain their separate written partial coefficient-two result and precisely parity-scoped Beal corollary, with independent verification outstanding. **U41's weighted elimination remains invalidated by U63.** U60 corrects historical U57-U59 computations; their restricted projective tables must not be reused as complete pruning rules.

The previous full research index is retained unchanged in [README before U69](references/U69/README_before.md). No older mathematical checkpoint was overwritten.

## Original target

For positive integers A,B,C,x,y,z with `A^x+B^y=C^z` and `x,y,z>=3`, prove `gcd(A,B,C)>1` or produce an independently verified exact counterexample. All bases and exponents remain unbounded; no partial result here resolves that statement.
