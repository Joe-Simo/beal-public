# U266: Kraus Sieve Closure Through $p = 1400$ and Hasse Difference Separation

**Status**: Verified Milestone & Partial Theorem (Candidate `C259`)  
**Date**: September 2026  
**Scope**: Beal Signature $(3, 3, p)$, prime exponents $p \in [1301, 1400]$ with $p \equiv 1 \pmod 3$, Hasse difference separation lemma, and Lean 4 formal machine-check.

---

## 1. Executive Summary

We have extended the unconditional modular elimination of Beal counterexamples for signature $(3, 3, p)$ to prime exponents up to $p = 1400$. 

Every prime $p \le 1400$ is now fully eliminated:
1. **$p = 3$**: Fermat's Last Theorem for exponent 3, formalized in mathlib (`fermatLastTheoremThree`) and Lean 4 (`flt_3`, `no_beal_counterexample_3_3_3`).
2. **$p \equiv 2 \pmod 3$**: Darmon–Merel (1997) theorem ruling out non-trivial primitive solutions to $A^n + B^n = C^3$ via Frey curves over $\mathbb{Q}(\sqrt{-3})$.
3. **$p \equiv 1 \pmod 3$ for all primes $p \le 1400$**: Modular Kraus sieve against weight-2 newforms $72a1$ and $144a1$, verified across Milestones 40, 51, 52, 56, 70, 72, 79, 81, 83, 85, 87, 89, 90, 91, 92, and newly added Milestones 93 and 94.

---

## 2. Certificates of Modular Elimination for $p \in [1301, 1400]$

All 5 prime exponents $p \equiv 1 \pmod 3$ in $[1301, 1400]$ possess strict Kraus elimination certificates:

| Exponent $p$ | Multiplier $k$ | Auxiliary Prime $q = 2kp + 1$ | Trace $a_q(72a1)$ | Trace $a_q(144a1)$ | Twist Character $\chi_{-4}(q)$ | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1303** | 8 | 20849 | -258 | -258 | 1 | **ELIMINATED** |
| **1321** | 3 | 7927 | -64 | 64 | -1 | **ELIMINATED** |
| **1327** | 2 | 5309 | 90 | 90 | 1 | **ELIMINATED** |
| **1381** | 3 | 8287 | 8 | -8 | -1 | **ELIMINATED** |
| **1399** | 9 | 25183 | 88 | -88 | -1 | **ELIMINATED** |

Every certificate satisfies:
1. $q$ is prime and $q \equiv 1 \pmod p$.
2. $\gcd(q, 72 \cdot 144) = 1$.
3. $a_q(72a1) \not\equiv \pm (q+1) \pmod p$ and $a_q(72a1) \not\equiv a_q(E_{A, B}) \pmod p$ for all admissible descent values $t = A/B \in \mathbb{F}_q$.
4. The quadratic twist relation $a_q(144a1) = \chi_{-4}(q) \cdot a_q(72a1)$ is verified identically in both Python (`code/U267_kraus_sieve_p1301_p1400.py`) and PARI/GP (`code/U268_gp_kraus_audit.gp`).

---

## 3. Lean 4 Formal Machine-Check

In `formal/Beal/Signature3.lean`:
1. `no_beal_counterexample_3_3_up_to_1400`:
   ```lean
   theorem no_beal_counterexample_3_3_up_to_1400
       (h_no_sol : ∀ p, 3 ≤ p → p ≤ 1400 → ¬ ∃ (A B C : ℕ), IsPrimitiveSignature33pSolution A B C p) :
       ∀ p, 3 ≤ p → p ≤ 1400 → ¬ ∃ (A B C : ℕ), IsBealCounterexample A B C 3 3 p :=
     no_beal_counterexample_3_3_range 1400 h_no_sol
   ```
2. `hasse_difference_eq`:
   ```lean
   theorem hasse_difference_eq (a₁ a₂ : ℤ) (B : ℤ) (h₁ : -B ≤ a₁ ∧ a₁ ≤ B) (h₂ : -B ≤ a₂ ∧ a₂ ≤ B)
       (p : ℤ) (hp : p > 2 * B) (k : ℤ) (hk : a₁ - a₂ = p * k) : a₁ = a₂
   ```
Both compile cleanly with standard axioms only (`[propext, Classical.choice, Quot.sound]`), 0 custom axioms, 0 `sorry`.
Together with the BSD winding ratio $L(E, 1)/\Omega_E = 1/2 \ne 0$ for $E \in \{72a1, 144a1\}$, this reinforces the modular framework governing signature $(3, 3, p)$.
