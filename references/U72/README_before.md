# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest checkpoint: U71 common global root

[U71](research/checkpoints/U71_common_decic_seventeenth_root.md) gives a written necessary-condition theorem for a primitive positive solution of `X^10+256Y^10=Z^17`. With `rho^5=2`, there must be one algebraic integer `theta` in `Q(rho,i)` such that

    theta^17=X+i*rho^4*Y,
    Norm(theta)=Z,
    289 divides Y.

Both the quintic and Gaussian roots are exact relative norms of this common global element. The argument starts from the weighted equation, reconstructs the Gaussian input, proves class number one with explicit norm certificates for all 92 prime ideals needed by the Minkowski bound, and eliminates units with a complete four-dimensional quotient and one nonsingular minor. It does not invoke the earlier Q65 unit elimination, a boundary congruence, or the invalidated U41 argument.

**This is not an impossibility theorem.** Common local roots still exist in both previously remaining prime classes, and valuation exactly two for Y at 17 also survives locally. Excluding a global integral theta with the required sparse seventeenth power is the remaining task. The weighted equation and the full Beal conjecture remain unresolved.

Verification is a complete written argument with same-model audit and distinct Python, TypeScript and Wolfram arithmetic checks. Independent expert or proof-assistant certification remains outstanding. The manuscript, exact certificate, both verifiers, reproduction commands and compact computation records are preserved here; the delivered U71 evidence archive also retains complete logs, candidate-discovery records and the unchanged upstream U70 archive.

## Continuity and retained work

U70 was available as an attached local manuscript and evidence archive; it had not been pushed when U71 began. It is retained in the delivered evidence package and is not a hypothesis of U71. Remote preservation details are recorded explicitly rather than silently claiming all old archives were uploaded.

[U69](research/checkpoints/U69_joint_scalar_quotient_obstruction.md) restricts the jointly exceptional prime-power support. [U68](research/checkpoints/U68_global_coefficient_height_obstruction.md) gives the earlier weighted base-height bound `max(X,Y)>10^514`. These are necessary conditions, not bounds for every possible Beal counterexample.

[Quintic U65](research/checkpoints/U65_weighted_quintic_unit_elimination.md) and [U67](research/checkpoints/U67_unconditional_Kummer_obstructions.md) retain their previous written/self-reviewed status. U71 provides a separate derivation of their underlying pure quintic equation; it is not independent expert verification of every downstream argument.

U61/U62 concern the separate coefficient-two equation and retain their prior limited status. **U41's weighted elimination remains invalidated by U63.** The unproved global modular prerequisites and boundary congruence are not reinstated. Historical success labels are not certification.

The previous remote index is preserved in [README before U71](references/U71/README_before.md). No earlier mathematical checkpoint was replaced.

## Original target

For positive integers A,B,C,x,y,z satisfying `A^x+B^y=C^z` with `x,y,z>=3`, prove `gcd(A,B,C)>1` or produce an independently verified counterexample. All bases and exponents remain unbounded. No partial result here resolves that statement.
