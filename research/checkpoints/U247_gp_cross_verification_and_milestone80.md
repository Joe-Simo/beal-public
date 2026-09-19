# Checkpoint U247: Independent PARI/GP Kraus Sieve Cross-Verification (Milestone 80) and Chabauty–Kim Evaluation

**Status**: Research Checkpoint  
**Formal Environment**: Lean 4 `v4.14.0` + mathlib (127 machine-checked theorems in `Euler.lean`, expanded `FidelityCheck.lean`, 0 errors, standard axioms only)  
**Audit Suite**: 80/80 Milestones Passing  
**Candidates Addressed**: C247 (PARTIAL_RESULT), C248 (ACTIVE)

---

## 1. Executive Summary

This cycle achieves an independent, multi-language validation milestone and evaluates the higher-depth arithmetic geometry frontier:

1. **Independent PARI/GP Cross-Verification (Candidate C247, Milestone 80)**:
   In [`code/U247_gp_kraus_audit.gp`](file://[LOCAL_HOME]/Downloads/beal/code/U247_gp_kraus_audit.gp), we independently re-implemented the modular trace evaluation and quadratic twist validation for the Kraus sieve in PARI/GP. All 9 primes $p \equiv 1 \pmod 3$ in $[601, 700]$ were re-evaluated:
   $$\{601, 607, 613, 619, 631, 643, 661, 673, 691\}$$
   The Fourier traces $a_q(72a1)$ and $a_q(144a1)$ were certified with exact integer arithmetic, confirming the quadratic twist relation:
   $$a_q(144a1) = \left(\frac{-4}{q}\right) a_q(72a1)$$
   with zero discrepancy between Python and PARI/GP.

2. **Chabauty–Kim Depth Evaluation (Candidate C248)**:
   We conducted a literature audit of Minhyong Kim's non-abelian Chabauty method on hyperbolic modular curves:
   - Classical Chabauty–Coleman corresponds to depth $d = 1$, requiring $\operatorname{rank}_{\mathbb{Z}} J(\mathbb{Q}) < g$.
   - Non-abelian Chabauty (depth $d \ge 2$) replaces the Jacobian with unipotent fundamental group quotients $U_n = \pi_1^{\text{un}}(X) / Z_{n+1}$, cutting out $p$-adic points via iterated Coleman integrals.
   - **Critical Obstruction**: Computing the Selmer varieties $\operatorname{Sel}(U_n)$ unconditionally across arbitrary exponent families requires the Bloch–Kato / Fontaine–Mazur conjectures. It cannot provide an unconditional resolution of Beal without these open conjectures.

---

## 2. PARI/GP Independent Trace Verification Table

Results from [`code/U247_gp_kraus_audit.gp`](file://[LOCAL_HOME]/Downloads/beal/code/U247_gp_kraus_audit.gp):

| $p$ | Auxiliary Prime $q$ | $a_q(72a1)$ | $\chi_{-4}(q)$ | $a_q(144a1)$ | Cross-Language Status |
|---|---|---|---|---|---|
| 601 | 3607 | -64 | -1 | 64 | **MATCH (Python & GP)** |
| 607 | 3643 | -28 | -1 | 28 | **MATCH (Python & GP)** |
| 613 | 6131 | -12 | -1 | 12 | **MATCH (Python & GP)** |
| 619 | 2477 | 42 | +1 | 42 | **MATCH (Python & GP)** |
| 631 | 6311 | -104 | -1 | 104 | **MATCH (Python & GP)** |
| 643 | 21863 | -104 | -1 | 104 | **MATCH (Python & GP)** |
| 661 | 3967 | 88 | -1 | -88 | **MATCH (Python & GP)** |
| 673 | 2693 | 98 | +1 | 98 | **MATCH (Python & GP)** |
| 691 | 8293 | -58 | +1 | -58 | **MATCH (Python & GP)** |

Positive control: $a_5(72a1) = 2$ and $a_{13}(72a1) = -2$ verified against LMFDB standards.

---

## 3. Master Reproducibility Suite Status

With Milestone 80 integrated into [`code/verify_all_milestones.py`](file://[LOCAL_HOME]/Downloads/beal/code/verify_all_milestones.py):
- Total Milestones: 80
- Milestones Passing: 80 / 80 (100% pass rate)
- Suite Script: [`code/verify_all_milestones.py`](file://[LOCAL_HOME]/Downloads/beal/code/verify_all_milestones.py)
