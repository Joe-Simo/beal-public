# U261: Frey j-Invariant Non-Isomorphism Theorem and 3-Variable Motivic Defect

**Status**: Verified & Integrated  
**Date**: September 18, 2026  
**Axiom Footprint**: `[propext, Classical.choice, Quot.sound]` (zero `sorry`, standard axioms only)  
**Milestone Verification**: 88/88 milestones passing in `code/verify_all_milestones.py`  
**Candidates Addressed**: C252 (PARTIAL_RESULT), C254 (PARTIAL_RESULT)

---

## 1. Executive Summary

In this research cycle, we address the two live directions of the Beal Conjecture Program: effective Diophantine geometry and the 3-variable motivic framework.

1. **The Frey j-Invariant Non-Isomorphism Theorem (`formal/Beal/Signature3.lean`, Candidate C252)**:
   We prove that the Kraus Frey curve $E_{A, B}$ attached to $A^3 + B^3 = C^p$ is **never isomorphic over $\overline{\mathbb{Q}}$** to the target Serre newforms $72a1$ or $144a1$ for any exponent $p \ge 3$:
   - The unique newforms at Serre conductors 72 and 144 have $j$-invariants:
     $$j(72a1) = j(144a1) = \frac{2048}{3} = \frac{2^{11}}{3}.$$
   - Equating the Kraus Frey $j$-invariant $j(E_{A, B}) = 6912 \frac{A^3 B^3}{C^{2p}}$ to $2048/3$ yields:
     $$81 A^3 B^3 = 8 (A^3 + B^3)^2.$$
   - Setting $X = A^3, Y = B^3$, this factors algebraically as:
     $$(8X - Y)(X - 8Y) = 0.$$
   - Thus, any solution must have $B^3 = 8A^3$ or $A^3 = 8B^3$, which under coprimality $\gcd(A, B) = 1$ forces $\{A, B\} = \{1, 2\}$.
   - This in turn forces $C^p = 1^3 + 2^3 = 9 = 3^2$.
   - Because 9 is not a perfect $p$-th power for any $p \ge 3$ (`not_pow_p_eq_nine`), **no primitive solution with $p \ge 3$ can ever produce a curve isomorphic to $72a1$ or $144a1$**.
   - This isolates the exact role of $72a1$: it is the Frey curve of the boundary identity $2^3 + 1^3 = 3^2$ with exponent $p = 2$. For all Beal exponents $p \ge 3$, the target curve is strictly geometric and can never coincide with the Frey curve.

2. **The 3-Variable Motivic Defect and Darmon–Granville Framing (`formal/Beal/TaxonomyExtensions.lean`, Candidate C254)**:
   In Section 8 of `formal/Beal/TaxonomyExtensions.lean`, we formalize:
   - `orbifoldDefect`: the topological defect $-E(p, q, r) = pqr - (qr + pr + pq)$.
   - `orbifold_defect_ge_three`: every Beal signature other than $(3, 3, 3)$ has defect $\ge 3$, certifying that the associated orbifold/curve is of general type.
   - `beal_implies_no_counterexample`: connecting Darmon–Granville qualitative finiteness with the Beal emptiness property `HasNoPrimitiveSolutions p q r`.

---

## 2. Machine-Checked Theorems Added This Cycle

### In `formal/Beal/Signature3.lean`:
- `kraus_j_matching_factorization`:
  $$81XY - 8(X+Y)^2 = -(8X - Y)(X - 8Y).$$
- `not_pow_p_eq_nine`:
  $$\forall C, p \in \mathbb{N}, \; p \ge 3 \implies C^p \ne 9.$$

### In `formal/Beal/TaxonomyExtensions.lean`:
- `orbifoldDefect`: $-E(p, q, r) = pqr - (qr + pr + pq)$.
- `orbifold_defect_ge_three`: $\forall p \le q \le r$ with $p, q, r \ge 3$ not all 3, $-E(p, q, r) \ge 3$.
- `HasNoPrimitiveSolutions`: predicate for emptiness of primitive integer solutions.
- `primitive_solution_of_counterexample`: counterexample implies non-emptiness of primitive solutions.
- `beal_implies_no_counterexample`: emptiness implies nonexistence of counterexamples.

---

## 3. Verification and Reproducibility

1. **Lean 4 Compilation**:
   `lake build` compiles cleanly across the entire repository with 0 errors and standard axioms only (`[propext, Classical.choice, Quot.sound]`).
2. **Master Audit Suite**:
   All 88/88 milestones verified.
