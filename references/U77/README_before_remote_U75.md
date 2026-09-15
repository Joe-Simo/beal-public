# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest checkpoint: U75 explicit Jacobian factors and positive rank

[U75](research/checkpoints/U75_jacobian_decomposition_and_infinite_order_classes.md) gives B-defined maps that decompose the genus-120 curve's Jacobian, up to isogeny, into fifteen genus-eight Jacobians, where B=Q(i,zeta_5). Both compositions of the displayed isogenies are multiplication by seventeen.

For every factor it proves that the full B-rational torsion is cyclic of order seventeen and constructs an explicit infinite-order class. Their pullbacks yield **fifteen independent classes modulo torsion**, so the original Jacobian has rank at least fifteen over B. This is a lower bound, not an exact rank or a finite-index basis. The original B-rational torsion is killed by 289; its full structure is not claimed.

The source-checked Jacobi-sum formula is evaluated exactly at three good primes. Python and TypeScript agree on all 45 character vectors and group orders and all 15 jet matrices. Wolfram corroborates the orders and determinants after a rejected preliminary expression was corrected. A direct count over F_(1021^2) separately checks the Frobenius sign. The common degree-five coordinate polynomial and norm-one conditions are retained across all factors.

**No relevant degree-five points or weighted solutions are excluded by U75.** The result supplies smaller arithmetic components and excludes a torsion-only shortcut. Certified rank upper bounds, finite-index/saturation data, and the simultaneous effective-divisor conditions are still missing. The weighted equation `X^10+256Y^10=Z^17` and the complete Beal conjecture remain unresolved.

Verification is a complete written argument and same-model review, with distinct exact computations, not independent expert or proof-assistant certification. The proof, three checkers, reproduction script, order table and core records are preserved in the repository. The delivered U75 archive also contains complete outputs/logs and the unchanged U74 archive; U74's previously local files are not silently claimed as pushed.

## Continuity and retained work

U74's local manuscript defines the genus-120 diagonal plane curve and its cyclic degree-five target, classifies a boundary line, and retains an unenumerated finite point problem. Its unchanged manuscript and archive are included in the delivered U75 evidence package. U75's explicitly defined curve theorems do not assume that point set has been classified; their weighted application retains the earlier common-root hypotheses.

[U73](research/checkpoints/U73_genus_eight_reduction.md), the remote predecessor, concerns the fixed genus-eight target and its field and quotient limitations. [U71](research/checkpoints/U71_common_decic_seventeenth_root.md) supplies the written common global root and `289|Y`. U72's separate full-support result remains a necessary lower-bound theorem, not an impossibility proof.

U61/U62 retain their separate coefficient-two scope and outstanding independent-verification obligations. **U41 remains invalidated by U63.** No boundary congruence or unresolved modular prerequisite is reinstated, and no new complete Beal signature is marked solved.

The previous remote index is retained in [README before U75](references/U75/README_before_remote_U73.md). No older remote checkpoint was replaced.

## Original target

For positive integers A,B,C,x,y,z satisfying `A^x+B^y=C^z` with `x,y,z>=3`, prove `gcd(A,B,C)>1` or produce an independently verified exact counterexample. All bases and exponents remain unbounded. None of the partial results here resolves that statement.
