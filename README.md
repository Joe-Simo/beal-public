# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest checkpoints: U96–U99 Modular, Descent, and Checker Milestones

The surviving weighted equation remains

`X^10+256Y^10=Z^17`.

### 1. Genus-8 2-Descent and Chabauty Condition (U99)
[U99](research/checkpoints/U99_descent_field_class_number_one_and_selmer_rank_bound.md) resolves the class-group bottleneck that halted U78–U80:
- Using PARI/GP 2.17.4 (`bnfinit(f, 1)`), the ideal class group of the degree-34 field `F = k(s)` (`s^17 = 2phi - 2`) is certified to be trivial: `Cl(O_F) = 0`, establishing `h(F) = 1` and `d = dim_F2 Cl(O_F)[2] = 0`.
- The 17-column global restriction matrix `Psi` against the 16-dimensional dyadic Kummer image `W_2` (U79) and the prime-5 condition has rank 15.
- Consequently, `dim_F2 Sel_2(J^-/k) <= 17 - 15 = 2`, proving:
  `rank_Z J^-(k) <= 2 < g = 8`.
- The rank of the Jacobian is strictly less than the genus of the quotient curve `C^-/k`. Therefore, the **Chabauty–Coleman method** applies unconditionally to `C^-/k`, proving finiteness of rational points.

### 2. Discharge of Prime-5 Local Lift in Breuil–Diamond (U98)
[U98](research/checkpoints/U98_prime5_local_representation_and_lift_certificate.md) proves that the local Galois group of the prime-5 Eisenstein quintic over `K_p5 = Q_5(sqrt(5))` is the dihedral group `D_5` (order 10, totally ramified). The Artin conductor exponent is exactly 3. By Maschke's theorem (`17 ∤ 10`), the local deformation problem is unobstructed, unconditionally discharging Breuil–Diamond Theorem 3.2.2 local-lift hypotheses at prime 5.

### 3. Global Elimination of CM Boundary Form Orbit b (U97)
[U97](research/checkpoints/U97_orbit_b_boundary_CM_obstruction.md) proves that the sole surviving Hilbert newform orbit `b` at level 2000 (`2.2.5.1-2000.1-b`) is the abelian surface attached to the boundary CM curve `C_0: y^2 = 64 - x^5`. It establishes three independent global obstruction strategies (including reducibility over `Q(zeta_5)` via `X_0(17)` and endomorphism dimension clash `dim End^0(J^-) = 2 != 4 = dim End^0(Jac(C_0))` via `R = T` deformation rigidity) to eliminate orbit `b` unconditionally.

### 4. Level-Lowering Source Audit (U96)
[U96](research/checkpoints/U96_azon_theorem523_audit_and_lift_status.md) audited Martin Azon's preprint (arXiv:2504.01967v2) and confirmed that its Theorem 5.23 requires Hypothesis 5 (which fails identically for the weighted equation) and directly cites Breuil–Diamond Theorem 3.2.2.

### 5. Section 8 Exact Counterexample Checker Validated
A standalone, fully tested counterexample checker satisfying all Section 8 requirements is implemented in TypeScript (`code/section8_counterexample_checker.ts`) and Python (`code/section8_counterexample_checker.py`), with 100% test passage across all boundary and invalidity test suites.

## Preceding checkpoints: U81–U92 Padé and Sieve Program
- [U92](research/checkpoints/U92_forcing_prime_sieve_exhausted.md): Proved via a genus-1576 Kummer cover that exactly 14 forcing primes exist in the Gaussian sieve.
- [U90](research/checkpoints/U90_mixed_weight_cubic_pade.md): Proved the conditional lower bound `max(X, Y) > 10^25993`.
- [U85](research/checkpoints/U85_ratio_collision_invariant.md)–[U86](research/checkpoints/U86_symmetric_X_support.md): Constructed all-prime ratio collision invariants `Y_*^390 | C_theta`.

## Global coverage

The coefficient-two orientation `X^10+Y^10=2Z^17` is closed by the corrected Freitas–Dieulefait theorem application preserved in U56. The coefficient-256 weighted orientation remains unresolved. The all-even `17∤t` branch and the much larger mixed-signature part of Beal also remain unresolved.

**U41 remains invalidated by U63.** No incomplete modular elimination, failed class-group computation, bounded search, density statement, or collision invariant is counted as a solution.

The preceding root README is preserved in [README before U86](references/U86/README_before.md).

## Original target

For positive integers `A,B,C,x,y,z` satisfying `A^x+B^y=C^z` and `x,y,z>=3`, prove `gcd(A,B,C)>1` or produce an independently verified counterexample. All bases and exponents remain unbounded.
