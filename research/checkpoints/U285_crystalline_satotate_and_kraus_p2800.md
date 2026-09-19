# U285: Crystalline Slopes & Sato-Tate Obstruction Audit and Kraus Sieve Elimination up to p = 2800

**Author**: Antigravity Assistant & Beal Exploration Loop  
**Date**: September 18, 2026  
**Status**: Milestones 129–131 Verification & Candidate Audit (C308, C309, C310)  

---

## 1. Executive Summary

This research cycle accomplished four primary objectives:
1. **Jev Batch Screen**: Screened Candidates C308 (Kraus sieve $p \in [2701, 2800]$), C309 (Crystalline Frobenius Newton polygons across variable signatures), and C310 (Vertical Sato-Tate equidistribution on Frey families); persisted decisions in `research/pool/evidence/`.
2. **Computational Verification & Independent PARI/GP Audit (Milestones 129 & 130)**:
   Extended the algorithmic Kraus sieve for signature $(3, 3, p)$ to all prime exponents $p \in [2701, 2800]$ with $p \equiv 1 \pmod 3$ ($p \in \{2707, 2713, 2719, 2731, 2749, 2767, 2791, 2797\}$). All 8 primes were unconditionally eliminated with a 100% elimination rate across auxiliary primes $q = 2kp + 1 \le 100000$ (`code/U316_kraus_sieve_p2701_p2800.py`), and independently audited in PARI/GP (`code/U317_gp_kraus_audit.gp`).
3. **Crystalline Frobenius Slopes & Newton Polygon Audit (Milestone 131, Candidate C309)**:
   Investigated whether $p$-adic crystalline Frobenius slopes on $H_{\text{crys}}^1(C_{p, q, r} / W(k))$ can bound exponents $(p, q, r)$ without fixing Hodge numbers. Confirmed that Mazur's inequality ($\text{Newton polygon} \ge \text{Hodge polygon}$) holds identically for all smooth projective curves of all genera $g$. Crystalline slope theory establishes an internal consistency relation between $p$-adic valuations of Frobenius eigenvalues and Hodge filtration, but imposes no upper bound on the genus $g$ or the exponents. Candidate C309 is classified as `BLOCKED`.
4. **Sato-Tate Distribution & Coprimality Blindness Audit (Milestone 131, Candidate C310)**:
   Analyzed vertical trace distributions $\{ a_q(E_t) / 2\sqrt{q} \}_{t \in \mathbb{F}_q}$ for the Kraus Frey family $E_t: y^2 = x^3 + 3tx + (1 - t^3)$. Confirmed that vertical moments converge to the standard Sato-Tate / Wigner semicircle distribution governed by the geometric monodromy group $\operatorname{SL}_2$. Demonstrated that statistical trace equidistribution is uniform across all residue classes and provides no Diophantine filter for integer coprimality $\gcd(A, B, C) = 1$. Candidate C310 is classified as `BLOCKED`.
5. **Formal Machine Verification in Lean 4**:
   Formally proved and machine-checked in Lean 4:
   - `no_beal_counterexample_3_3_up_to_2800` in `formal/Beal/Signature3.lean`
   - `post_century_signature_3_3_p_elimination_2800` in `formal/Beal/PostCentennial.lean`
   All theorems compiled with 0 errors, 0 `sorry`, and standard axioms only (`[propext, Classical.choice, Quot.sound]`).

---

## 2. Kraus Sieve Verification for $p \in [2701, 2800]$ (Milestones 129 & 130)

### Eliminating Auxiliary Primes

| Exponent $p$ | Eliminating $q = 2kp + 1$ | $k$ | $a_q(72a1)$ | $a_q(144a1)$ | Elimination Rate |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **2707** | 43313 | 8 | $334$ | $334$ | **100.0%** |
| **2713** | 10853 | 2 | $82$ | $82$ | **100.0%** |
| **2719** | 27191 | 5 | $-312$ | $312$ | **100.0%** |
| **2731** | 60083 | 11 | $-12$ | $12$ | **100.0%** |
| **2749** | 82471 | 15 | $-64$ | $64$ | **100.0%** |
| **2767** | 11069 | 2 | $-70$ | $-70$ | **100.0%** |
| **2791** | 16747 | 3 | $116$ | $-116$ | **100.0%** |
| **2797** | 44753 | 8 | $126$ | $126$ | **100.0%** |

Both Python (`code/U316_kraus_sieve_p2701_p2800.py`) and PARI/GP (`code/U317_gp_kraus_audit.gp`) confirmed 100% elimination with zero discrepancies.

---

## 3. Crystalline Cohomology and Slope Bounds (C309)

Let $C$ be the Fermat quotient curve $C_{p, q, r}$ of genus $g$.
The crystalline cohomology $H_{\text{crys}}^1(C / W(\mathbb{F}_q))$ is an $F$-crystal of rank $2g$.
- **Hodge Polygon**: Has $g$ slopes equal to 0 and $g$ slopes equal to 1, with vertices $(0, 0)$, $(g, 0)$, and $(2g, g)$.
- **Newton Polygon**: Slopes $\lambda_i = v_q(\alpha_i)$ where $\alpha_i$ are Frobenius eigenvalues on $H_{\text{crys}}^1$.
By Mazur's theorem (Katz conjecture), the Newton polygon lies on or above the Hodge polygon.
However:
1. Every smooth projective curve satisfies Mazur's inequality unconditionally.
2. The endpoints are fixed at $(0, 0)$ and $(2g, g)$ by the Weil conjectures / Poincaré duality.
3. No inequality on slopes $\lambda_i \in [0, 1]$ can force $g$ or $(p, q, r)$ to be bounded.
Hence, crystalline slope theory cannot bound exponents across an infinite family of curves.

---

## 4. Sato-Tate Equidistribution and Statistical Invariance (C310)

For the Kraus family $E_t: y^2 = x^3 + 3tx + (1 - t^3)$ over $\mathbb{P}^1$:
- The geometric monodromy group is $\mathcal{G}_{\text{geom}} = \operatorname{SL}_2$.
- By Deligne's equidistribution theorem, the Frobenius angles $\theta_t$ are equidistributed with respect to the Sato-Tate measure:
  $$d\mu_{\text{ST}} = \frac{2}{\pi} \sin^2\theta \, d\theta.$$
- As confirmed in `code/U318_motivic_satotate_audit.py`, the moments of the trace distribution over $\mathbb{F}_q$ converge to the Catalan moments of the semicircle law.
- **The Blindness Barrier**: Sato-Tate describes an asymptotic statistical property of the entire family. It cannot decide whether a specific rational point $t_0 \in \mathbb{P}^1(\mathbb{Q})$ satisfies $\gcd(A, B, C) = 1$. The modular method's success comes not from statistical density, but from rigid congruence conditions $a_q(E_t) \equiv a_q(f) \pmod p$ at isolated auxiliary primes $q$.

---

## 5. Formal Machine Verification Status in Lean 4

The following theorems are verified in `formal/Beal/`:
- `no_beal_counterexample_3_3_up_to_2800` (`formal/Beal/Signature3.lean`)
- `post_century_signature_3_3_p_elimination_2800` (`formal/Beal/PostCentennial.lean`)

All theorems check with standard Lean 4 axioms only:
```text
[propext, Classical.choice, Quot.sound]
```
0 errors, 0 warnings, 0 `sorry`.

---

## 6. Updated Candidate Pool Status

- `C308`: **PARTIAL_RESULT** (Kraus sieve modular traces verified and closed for $p \in [2701, 2800]$).
- `C309`: **BLOCKED** (Mazur's Newton $\ge$ Hodge inequality holds for all curves of all genera; crystalline slopes cannot bound exponents).
- `C310`: **BLOCKED** (Vertical Sato-Tate equidistribution reflects full geometric monodromy $\operatorname{SL}_2$, but provides no Diophantine filter for coprimality).
