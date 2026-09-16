# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest checkpoint: U86 symmetric coefficient-support program

The surviving weighted equation remains

`X^10+256Y^10=Z^17`.

[U86](research/checkpoints/U86_symmetric_X_support.md) shows that the coefficient-support mechanism developed in U81-U83 applies to both coprime bases, not only `Y`. On each side, disjoint Frobenius families of total natural density `553/640` force high powers of the corresponding prime factors into fixed nonzero coefficients of the common integral seventeenth root.

For `Y`, U82-U83 give strong/semi-strong/weak restrictions through `a9` and `a5`; for `X`, U86 gives their shifted analogues through `a4` and `a8`. These are genuine infinite support restrictions, **not** impossibility theorems.

[U85](research/checkpoints/U85_ratio_collision_invariant.md) removes the remaining density complement as a support-classification issue. Using all ninety ordered conjugate ratios, it constructs a fixed nonzero integer `C_theta` such that the prime-to-170 part `Y_*` satisfies

`Y_*^390 | C_theta`

and the explicit height inequality

`Y_*^221 <= 2^4539 (X+2^(4/5)Y)^534`.

U86 constructs the analogous all-prime invariant on the `X` side after the integral normalization `psi_j=c_j^7 theta_j`. The collision invariants grow too quickly to force a contradiction, so the weighted equation is still open.

[U84](research/checkpoints/U84_pair_product_discriminant_support.md) is the lower-degree precursor: a degree-twenty pair-product discriminant captures every prime-to-170 divisor of `Y` with at least six times its `Y`-valuation.

## Parallel U80 Selmer bottleneck

[U80](research/checkpoints/U80_norm_redundancy_hecke_audit.md) shows that two proposed shortcuts do not finish the genus-eight 2-descent: the extra quadratic-norm shape is automatic on the current Selmer group, and the inspected Hecke-reciprocity theorem is vacuous for this field. The degree-34 class-group 2-rank `d=dim_F2 Cl(O_F)[2]` remains uncomputed.

[U79](research/checkpoints/U79_complete_dyadic_Kummer_image.md) determines the full prime-2 Kummer image. [U78](research/checkpoints/U78_explicit_descent_field_and_two_prime_criterion.md) reduces a rank-zero certificate to computing the global candidate space and its seventeen local conditions. A certified `d=0` together with a full-rank restriction matrix would exclude the weighted equation through [U77](research/checkpoints/U77_anti_invariant_twist_reduction.md), but neither assertion has been proved.

## Global coverage

The coefficient-two orientation `X^10+Y^10=2Z^17` is closed by the corrected Freitas–Dieulefait theorem application preserved in U56. The coefficient-256 weighted orientation remains unresolved. The all-even `17∤t` branch and the much larger mixed-signature part of Beal also remain unresolved.

**U41 remains invalidated by U63.** No incomplete modular elimination, failed class-group computation, bounded search, density statement, or collision invariant is counted as a solution.

The preceding root README is preserved in [README before U86](references/U86/README_before.md).

## Original target

For positive integers `A,B,C,x,y,z` satisfying `A^x+B^y=C^z` and `x,y,z>=3`, prove `gcd(A,B,C)>1` or produce an independently verified counterexample. All bases and exponents remain unbounded.
