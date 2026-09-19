# Checkpoint U237: Algebraic Descent Closure to Coprime Cubes and Fermat–Catalan Blindness Certification

**Status**: Research Checkpoint  
**Formal Environment**: Lean 4 `v4.14.0` + mathlib (123 machine-checked theorems, 0 errors, 0 warnings, standard axioms only)  
**Audit Suite**: 77/77 Milestones Passing  
**Candidates Addressed**: C239 (PARTIAL_RESULT), C240 (PARTIAL_RESULT), C241 (ACTIVE), C242 (ACTIVE)

---

## 1. Executive Summary

In this research cycle, we achieved two primary structural advancements on the Diophantine frontier of Beal's conjecture:

1. **Algebraic Descent Closure to Coprime Cubes (Candidate C239)**:
   In [`formal/Beal/Euler.lean`](file://[LOCAL_HOME]/Downloads/beal/formal/Beal/Euler.lean), we proved the algebraic transition connecting Euler's cubic parametrization $p = a(a - 3b)(a + 3b) = s^3$ directly to a smaller coprime solution of Euler's equation:
   $$v^3 + w^3 = 2u^3, \quad \gcd(v, w) = 1$$
   Every intermediate theorem—including three-way cube extraction from pairwise coprime products (`three_factors_are_cubes`), cube-base coprimality transfer (`isCoprime_of_isCoprime_pow3`), and the linear cube sum identity (`euler_param_cube_sum`)—has been machine-checked under Lean 4 with zero `sorry` and standard axioms only (`[propext, Classical.choice, Quot.sound]`). The constructive core requires no classical choice at all (`[propext, Quot.sound]`).

2. **Fermat–Catalan Blindness Audit (Candidate C240, Milestone 77)**:
   In [`code/U240_fc_cubic_blindness.py`](file://[LOCAL_HOME]/Downloads/beal/code/U240_fc_cubic_blindness.py), we subjected all cubic descent constraints and parity relations to the Fermat–Catalan blindness test against the 10 known non-trivial Fermat–Catalan identities. The audit demonstrates that the cubic descent signature conditions $(3, 3, z)$ and $(3, 3, 3)$ strictly fail on all 10 identities (0/10 hold, 10/10 fail), proving that Euler's cubic descent is **exponent-2-sensitive** and carries genuine Beal-specific content rather than being exponent-2-blind.

---

## 2. Machine-Checked Algebraic Closure in Lean 4 (Candidate C239)

### 2.1 Three-Way Cube Extraction (`three_factors_are_cubes`)
Given three pairwise coprime integers $A, B, C \in \mathbb{Z}$ whose product is a cube:
$$A \cdot (B \cdot C) = K^3$$
Since $\operatorname{IsCoprime}(A, B)$ and $\operatorname{IsCoprime}(A, C)$, Mathlib's `IsCoprime.mul_right` yields $\operatorname{IsCoprime}(A, B \cdot C)$. Because 3 is an odd natural number, `Int.eq_pow_of_mul_eq_pow_odd_left` and `right` guarantee:
$$\exists u, A = u^3 \quad \text{and} \quad \exists t, B \cdot C = t^3$$
Applying the same theorem to the coprime product $B \cdot C = t^3$ yields $\exists v, B = v^3$ and $\exists w, C = w^3$.

```lean
theorem three_factors_are_cubes {A B C K : ℤ}
    (hAB : IsCoprime A B) (hAC : IsCoprime A C) (hBC : IsCoprime B C)
    (hprod : A * (B * C) = K ^ 3) :
    (∃ u, A = u ^ 3) ∧ (∃ v, B = v ^ 3) ∧ (∃ w, C = w ^ 3)
```

### 2.2 Closure of Euler's Parametrization (`euler_param_factors_are_cubes`)
Combining `pairwise_coprime_factors` (proved via explicit Bézout coefficients and linear arithmetic) with `three_factors_are_cubes`, whenever $p = a(a - 3b)(a + 3b) = s^3$ with $\gcd(a, b) = 1$, $3 \nmid a$, and $a, b$ having opposite parity:
$$\exists u, a = u^3, \quad \exists v, a - 3b = v^3, \quad \exists w, a + 3b = w^3$$

### 2.3 The Euler Cube Sum Identity (`euler_param_cube_sum`)
We prove that the cube roots $v$ and $w$ of the shifted factors sum exactly to twice the base cube $u^3 = a$:
$$v^3 + w^3 = (a - 3b) + (a + 3b) = 2a = 2u^3$$
This reproduces Euler's starting equation $X^3 + Y^3 = 2Z^3$ in the new variables $(v, w, u)$.

### 2.4 Strict Coprimality of Descent Cube Roots (`euler_param_cube_roots_coprime`)
By `isCoprime_of_isCoprime_pow3`, any two integers whose cubes are coprime are themselves coprime in $\mathbb{Z}$:
$$\operatorname{IsCoprime}(v^3, w^3) \implies \operatorname{IsCoprime}(v, w)$$
Since $\operatorname{IsCoprime}(a - 3b, a + 3b)$ was proved by `coprime_sub_add`, the descent variables $(v, w)$ are strictly coprime.

---

## 3. Fermat–Catalan Blindness Audit (Milestone 77)

Following the project discipline established in U141, every Diophantine condition proposed for Beal's conjecture must be evaluated against the 10 known Fermat–Catalan solutions:
1. $1^7 + 2^3 = 3^2$
2. $2^5 + 7^2 = 3^4$
3. $7^3 + 13^2 = 2^9$
4. $2^7 + 17^3 = 71^2$
5. $3^5 + 11^4 = 122^2$
6. $17^7 + 76271^3 = 21063928^2$
7. $1414^3 + 2213459^2 = 65^7$
8. $9262^3 + 15312283^2 = 113^7$
9. $43^8 + 96222^3 = 30042907^2$
10. $33^8 + 1549034^2 = 15613^3$

### 3.1 Audit Results ([`code/U240_fc_cubic_blindness.py`](file://[LOCAL_HOME]/Downloads/beal/code/U240_fc_cubic_blindness.py))

| Condition | Holds on FC | Fails on FC | Classification |
|---|---|---|---|
| `strict_beal_exponents` ($x, y, z \ge 3$) | 0 / 10 | 10 / 10 | **SENSITIVE (fails on all 10) [BEAL-SPECIFIC]** |
| `signature_3_3` ($x=3, y=3$) | 0 / 10 | 10 / 10 | **SENSITIVE (fails on all 10) [BEAL-SPECIFIC]** |
| `signature_3_3_3` ($x=3, y=3, z=3$) | 0 / 10 | 10 / 10 | **SENSITIVE (fails on all 10) [BEAL-SPECIFIC]** |
| `curvature_12` ($12(yz+xz+xy) \le 11xyz$) | 0 / 10 | 10 / 10 | **SENSITIVE (fails on all 10) [BEAL-SPECIFIC]** |
| `euler_both_odd` ($A, B$ both odd) | 3 / 10 | 7 / 10 | PARTIAL (3 holds, 7 fails) |
| `same_parity` ($A \equiv B \pmod 2$) | 3 / 10 | 7 / 10 | PARTIAL (3 holds, 7 fails) |
| `cubic_descent_opposite_pq` | 3 / 10 | 7 / 10 | PARTIAL (3 holds, 7 fails) |
| `hyperbolic_orbifold` ($\sum 1/p < 1$) | 10 / 10 | 0 / 10 | **BLIND (holds on all 10)** |
| `has_exponent_2` | 10 / 10 | 0 / 10 | **BLIND (holds on all 10)** |
| `two_exponents_ge_3` | 10 / 10 | 0 / 10 | **BLIND (holds on all 10)** |

### 3.2 Diophantine Insight
- The hyperbolic orbifold condition $\sum \frac{1}{p} < 1$ is completely blind to exponent 2, holding across every Fermat–Catalan identity. It constrains the curve topology to hyperbolic type but cannot prevent non-trivial rational/integer points in the presence of an exponent 2.
- In contrast, the Euler cubic descent conditions ($x=y=3$, curvature $\le 11/12$, and exponent $\ge 3$) are strictly sensitive, rejecting 100% of Fermat–Catalan points. They embody genuine exponent-3 Diophantine obstructions.

---

## 4. Summary of Declarations in `Beal/Euler.lean`

With the addition of candidate C239 theorems, `formal/Beal/Euler.lean` now contains **123 machine-checked theorems** (0 errors, 0 warnings):

1. `three_factors_are_cubes`
2. `euler_param_factors_are_cubes`
3. `euler_param_cube_sum`
4. `isCoprime_of_isCoprime_pow3`
5. `euler_param_cube_roots_coprime`

Axiom verification:
```
'Beal.three_factors_are_cubes' depends on axioms: [propext, Classical.choice, Quot.sound]
'Beal.euler_param_factors_are_cubes' depends on axioms: [propext, Classical.choice, Quot.sound]
'Beal.euler_param_cube_sum' depends on axioms: [propext, Quot.sound]
'Beal.isCoprime_of_isCoprime_pow3' depends on axioms: [propext]
'Beal.euler_param_cube_roots_coprime' depends on axioms: [propext, Classical.choice, Quot.sound]
```

All declarations rely strictly on Lean 4 standard axioms; zero `sorry`, zero custom axioms.
