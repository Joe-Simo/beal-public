# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest checkpoint: U81 clean-prime support theorem

[U81](research/checkpoints/U81_clean_prime_density_and_coefficient_support.md) studies the surviving weighted equation

`X^10+256Y^10=Z^17`.

Using U71/U72's common integral seventeenth root `theta=sum(a_j c^j)` with `c^10=-256` and `a9!=0`, U81 defines a rational prime `q` to be *clean* when the residue algebra of `T^10+256` modulo `q` has no nontrivial seventeenth roots of unity. It proves that if `q^e|Y` for a clean prime, then `q^(9e)|a9`.

The clean primes have natural density `105/128`, from an exact forty-element affine Galois-action enumeration plus Chebotarev. If `Y_clean` is the clean-prime part of `Y`, the global coefficient bound gives

`Y_clean^153 < X+2Y`.

This is a new infinite support restriction, **not** an impossibility theorem. The complementary dirty primes have density `23/128` and remain a possible support for a hypothetical solution.

## Parallel U80 Selmer bottleneck

[U80](research/checkpoints/U80_norm_redundancy_hecke_audit.md) shows that two proposed shortcuts do not finish the genus-eight 2-descent: the extra quadratic-norm shape is automatic on the current Selmer group, and the inspected Hecke-reciprocity theorem is vacuous for this field. The degree-34 class-group 2-rank `d=dim_F2 Cl(O_F)[2]` remains uncomputed.

[U79](research/checkpoints/U79_complete_dyadic_Kummer_image.md) already determines the full prime-2 Kummer image. [U78](research/checkpoints/U78_explicit_descent_field_and_two_prime_criterion.md) reduces a rank-zero certificate to computing the global candidate space and its seventeen local conditions. A certified `d=0` together with a full-rank restriction matrix would exclude the weighted equation through [U77](research/checkpoints/U77_anti_invariant_twist_reduction.md), but neither assertion has been proved.

## Global coverage

The coefficient-two orientation `X^10+Y^10=2Z^17` is closed by the corrected Freitas–Dieulefait theorem application preserved in U56. The coefficient-256 weighted orientation above remains unresolved. The all-even `17∤t` branch and the much larger mixed-signature part of Beal also remain unresolved.

**U41 remains invalidated by U63.** No incomplete modular elimination, failed class-group computation, bounded search, or rejected Selmer candidate is counted as a solution.

The preceding root README is preserved in [README before U81](references/U81/README_before.md).

## Original target

For positive integers `A,B,C,x,y,z` satisfying `A^x+B^y=C^z` and `x,y,z>=3`, prove `gcd(A,B,C)>1` or produce an independently verified counterexample. All bases and exponents remain unbounded.
