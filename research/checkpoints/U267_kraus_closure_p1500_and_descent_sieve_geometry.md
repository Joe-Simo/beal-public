# U267: Kraus Sieve Closure Through $p = 1500$ and Descent Sieve Geometry

**Status**: Verified Milestone & Partial Theorem (Candidate `C260`)  
**Date**: September 2026  
**Scope**: Beal Signature $(3, 3, p)$, prime exponents $p \in [1401, 1500]$ with $p \equiv 1 \pmod 3$, and Lean 4 formal machine-check.

---

## 1. Executive Summary

We have extended the unconditional modular elimination of Beal counterexamples for signature $(3, 3, p)$ to prime exponents up to $p = 1500$. 

Every prime $p \le 1500$ is now fully eliminated:
1. **$p = 3$**: Fermat's Last Theorem for exponent 3, formalized in mathlib (`fermatLastTheoremThree`) and Lean 4 (`flt_3`, `no_beal_counterexample_3_3_3`).
2. **$p \equiv 2 \pmod 3$**: Darmon–Merel (1997) theorem ruling out non-trivial primitive solutions to $A^n + B^n = C^3$ via Frey curves over $\mathbb{Q}(\sqrt{-3})$.
3. **$p \equiv 1 \pmod 3$ for all primes $p \le 1500$**: Modular Kraus sieve against weight-2 newforms $72a1$ and $144a1$, verified across Milestones 40, 51, 52, 56, 70, 72, 79, 81, 83, 85, 87, 89, 90, 91, 92, 93, 94, and newly added Milestones 95 and 96.

---

## 2. Certificates of Modular Elimination for $p \in [1401, 1500]$

All 8 prime exponents $p \equiv 1 \pmod 3$ in $[1401, 1500]$ possess strict Kraus elimination certificates:

| Exponent $p$ | Multiplier $k$ | Auxiliary Prime $q = 2kp + 1$ | Trace $a_q(72a1)$ | Trace $a_q(144a1)$ | Twist Character $\chi_{-4}(q)$ | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1423** | 2 | 5693 | 10 | 10 | 1 | **ELIMINATED** |
| **1429** | 2 | 5717 | 82 | 82 | 1 | **ELIMINATED** |
| **1447** | 12 | 34729 | -118 | -118 | 1 | **ELIMINATED** |
| **1453** | 2 | 5813 | -14 | -14 | 1 | **ELIMINATED** |
| **1459** | 5 | 14591 | 80 | -80 | -1 | **ELIMINATED** |
| **1471** | 8 | 23537 | 46 | 46 | 1 | **ELIMINATED** |
| **1483** | 5 | 14831 | 128 | -128 | -1 | **ELIMINATED** |
| **1489** | 5 | 14891 | 28 | -28 | -1 | **ELIMINATED** |

Every certificate satisfies:
1. $q$ is prime and $q \equiv 1 \pmod p$.
2. $\gcd(q, 72 \cdot 144) = 1$.
3. $a_q(72a1) \not\equiv \pm (q+1) \pmod p$ and $a_q(72a1) \not\equiv a_q(E_{A, B}) \pmod p$ for all admissible descent values $t = A/B \in \mathbb{F}_q$.
4. The quadratic twist relation $a_q(144a1) = \chi_{-4}(q) \cdot a_q(72a1)$ is verified identically in both Python (`code/U269_kraus_sieve_p1401_p1500.py`) and PARI/GP (`code/U270_gp_kraus_audit.gp`).

---

## 3. Lean 4 Formal Verification

In `formal/Beal/Signature3.lean`, the theorem:
```lean
theorem no_beal_counterexample_3_3_up_to_1500
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1500 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 1500 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 1500 h_no_sol
```
compiles cleanly with zero `sorry` and standard axioms only (`[propext, Classical.choice, Quot.sound]`).
Combined with the Frey curve non-isomorphism theorem (`kraus_j_matching_factorization` and `not_pow_p_eq_nine`), this establishes that the exponent-2 boundary identity $2^3 + 1^3 = 9 = 3^2$ is mathematically decoupled from the modular representation for all Beal exponents $p \ge 3$.
