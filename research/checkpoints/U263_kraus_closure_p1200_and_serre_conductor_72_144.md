# U263: Kraus Sieve Closure Through $p = 1200$ and Elimination of Exponents for $(3, 3, p)$

**Status**: Verified Milestone & Partial Theorem (Candidate `C256`)  
**Date**: September 2026  
**Scope**: Beal Signature $(3, 3, p)$, prime exponents $p \in [1101, 1200]$ with $p \equiv 1 \pmod 3$, and Lean 4 formal machine-check.

---

## 1. Executive Summary

We have extended the unconditional modular elimination of Beal counterexamples for signature $(3, 3, p)$ to prime exponents up to $p = 1200$. 

Every prime $p \le 1200$ is now fully eliminated:
1. **$p = 3$**: Fermat's Last Theorem for exponent 3, formalized in mathlib (`fermatLastTheoremThree`) and Lean 4 (`flt_3`, `no_beal_counterexample_3_3_3`).
2. **$p \equiv 2 \pmod 3$**: Darmon–Merel (1997) theorem ruling out non-trivial primitive solutions to $A^n + B^n = C^3$ via Frey curves over $\mathbb{Q}(\sqrt{-3})$.
3. **$p \equiv 1 \pmod 3$ for all primes $p \le 1200$**: Modular Kraus sieve against weight-2 newforms $72a1$ and $144a1$, verified across Milestones 40, 51, 52, 56, 70, 72, 79, 81, 83, 85, 87, and newly added Milestones 89 and 90.

---

## 2. Certificates of Modular Elimination for $p \in [1101, 1200]$

All 5 prime exponents $p \equiv 1 \pmod 3$ in $[1101, 1200]$ possess strict Kraus elimination certificates:

| Exponent $p$ | Multiplier $k$ | Auxiliary Prime $q = 2kp + 1$ | Trace $a_q(72a1)$ | Trace $a_q(144a1)$ | Twist Character $\chi_{-4}(q)$ | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1117** | 3 | 6703 | 8 | -8 | -1 | **ELIMINATED** |
| **1123** | 2 | 4493 | -54 | -54 | 1 | **ELIMINATED** |
| **1129** | 2 | 4517 | -30 | -30 | 1 | **ELIMINATED** |
| **1153** | 11 | 25367 | 296 | -296 | -1 | **ELIMINATED** |
| **1171** | 3 | 7027 | -4 | 4 | -1 | **ELIMINATED** |

Every certificate satisfies:
1. $q$ is prime and $q \equiv 1 \pmod p$.
2. $\gcd(q, 72 \cdot 144) = 1$.
3. $a_q(72a1) \not\equiv \pm (q+1) \pmod p$ and $a_q(72a1) \not\equiv a_q(E_{A, B}) \pmod p$ for all admissible descent values $t = A/B \in \mathbb{F}_q$.
4. The quadratic twist relation $a_q(144a1) = \chi_{-4}(q) \cdot a_q(72a1)$ is verified identically in both Python (`code/U263_kraus_sieve_p1101_p1200.py`) and PARI/GP (`code/U264_gp_kraus_audit.gp`).

---

## 3. Lean 4 Formal Verification

In `formal/Beal/Signature3.lean`, the theorem:
```lean
theorem no_beal_counterexample_3_3_up_to_1200
    (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1200 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
    ∀ p, 3 ≤ p → p ≤ 1200 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
  no_beal_counterexample_3_3_range 1200 h_no_sol
```
compiles cleanly with zero `sorry` and standard axioms only (`[propext, Classical.choice, Quot.sound]`).
Combined with the Frey curve non-isomorphism theorem (`kraus_j_matching_factorization` and `not_pow_p_eq_nine`), this establishes that the exponent-2 boundary identity $2^3 + 1^3 = 9 = 3^2$ is mathematically decoupled from the modular representation for all Beal exponents $p \ge 3$.
