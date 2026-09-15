# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest checkpoint: U65

[U65: the last Hecke check and an untwisted quintic descent](research/checkpoints/U65_weighted_quintic_unit_elimination.md) excludes the previously unexamined orbit h at 11, leaving only b in the recorded eight-orbit modular list. The global level-lowering and independent newspace-completeness obligations remain open.

Independently of those modular obligations, U65 proves the following necessary condition for a primitive positive solution of `X^10+256Y^10=Z^17`: with `rho^5=2`,

    X^2+2rho^3Y^2=beta^17, beta in Z[rho], Norm(beta)=Z,
    17 divides exactly one of X,Y.

The class-number calculation and explicit unit characters first give 289 complete unit classes; a full modulo-289 test combined with the Gaussian equation eliminates every nontrivial class. The remaining pure-power equation is **not** proved impossible. The constant splitting field and common mod-2 module explain why those invariants alone cannot separate the boundary curve; they do not identify a mod-17 representation.

Exact Python split-algebra, TypeScript unsplit-algebra and Wolfram computations agree. Source metadata, compact certificates, failed attempts and replay logs are preserved with this checkpoint. The delivered evidence archive additionally retains both complete finite outputs, including all 24 rows and 544 square-root witness pairs; those full output files are not claimed as copied to the remote. These are written/self-reviewed partial results, not independent expert or proof-assistant certification. No novelty or prize claim is made.

## Retained work and corrections

U61/U62 retain their written partial proof that the only primitive positive solution of `X^10+Y^10=2Z^17` is `(1,1,1)`, with a precisely parity-scoped Beal corollary. They do not cover the weighted equation or the full conjecture. Their independent verification remains outstanding.

**U41's weighted elimination remains invalidated by U63.** U64 repairs specific local hypotheses, not the original elimination. U60 records corrections to U57-U59; their old restricted projective tables are not complete pruning rules. Historical success labels do not constitute certification.

## Next question

Analyze the simultaneous integral coefficient conditions in U65's pure seventeenth-power equation, retaining the Gaussian equation and all square/positivity constraints. A global contradiction or a certified rational-point reduction is still missing. In parallel, the boundary-type modular survivor b and the remaining global lifting hypotheses must be audited; finite boundary-compatible prime tests are not an elimination.

## Original target

For positive integers A,B,C,x,y,z satisfying `A^x+B^y=C^z`, with `x,y,z>=3`, prove `gcd(A,B,C)>1` or produce an independently verified exact counterexample. All exponents and bases remain unbounded. No partial result in this repository resolves that statement.
