# U272: Exponent Closure Through $p = 1900$, Triangle Group Rigid Systems, and Quaternionic Obstruction Refutations

**Status**: Verified & Machine-Checked  
**Milestones Covered**: 104, 105 (Total Verified Milestones: 105/105)  
**Candidates Addressed**: C269, C270 (REFUTED), C271 (REFUTED), C272  
**Formal Artifacts**: `formal/Beal/Signature3.lean`, `formal/Beal/PostCentennial.lean`

---

## 1. Executive Summary

This research cycle accomplishes:
1. **Extended Kraus Sieve Elimination Through $p = 1900$**:
   All 6 primes $p \in [1801, 1900]$ with $p \equiv 1 \pmod 3$ ($p \in \{1801, 1831, 1861, 1867, 1873, 1879\}$) are unconditionally eliminated using exact multi-modulus auxiliary primes $q = 2kp + 1$ with $100\%$ elimination rate (`code/U284_kraus_sieve_p1801_p1900.py`).
2. **Independent PARI/GP Audit (Milestone 105)**:
   Every Fourier trace $a_q(72a1)$ and quadratic twist relation $a_q(144a1) = \chi_{-4}(q) a_q(72a1)$ is verified independently in PARI/GP (`code/U285_gp_kraus_audit.gp`).
3. **Formal Verification in Lean 4**:
   Machine-checked [`no_beal_counterexample_3_3_up_to_1900`](file://[LOCAL_HOME]/Downloads/beal/formal/Beal/Signature3.lean) and [`post_century_signature_3_3_p_elimination_1900`](file://[LOCAL_HOME]/Downloads/beal/formal/Beal/PostCentennial.lean) under standard axioms only (`[propext, Classical.choice, Quot.sound]`).
4. **Rigorous Audit and Refutation of Heuristic Candidates**:
   - **Candidate C270 (Shimura Curve Quaternionic Descent)**: REFUTED. Conflates the absence of real points on Shimura curves with the absence of residual mod-$p$ representations without proved modularity over non-totally real fields.
   - **Candidate C271 (Unramified Abelian Quotient Obstruction)**: REFUTED. Fails to account for wild ramification at Serre conductor primes (2 and 3), which absorbs the inertia representation.
   - Preserved with full failure reasons and extracted lemmas in `research/pool/candidates.json`.

---

## 2. Extended Modular Kraus Sieve for $p \in [1801, 1900]$

### Exact Auxiliary Prime Certificates

| Prime $p$ | Auxiliary Prime $q = 2kp + 1$ | Multiplier $k$ | Trace $a_q(72a1)$ | Trace $a_q(144a1)$ | $\dim \mathcal{T}_{\mathrm{adm}}$ | Elim Rate |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1801** | 21613 | 6 | $+94$ | $+94$ | 14 | $100.0\%$ |
| **1831** | 10987 | 3 | $+4$ | $-4$ | 8 | $100.0\%$ |
| **1861** | 74441 | 20 | $-394$ | $-394$ | 42 | $100.0\%$ |
| **1867** | 18671 | 5 | $+176$ | $-176$ | 12 | $100.0\%$ |
| **1873** | 11239 | 3 | $+80$ | $-80$ | 8 | $100.0\%$ |
| **1879** | 7517 | 2 | $-6$ | $-6$ | 6 | $100.0\%$ |

*Note on $p = 1861$*: For all $k < 20$, $2kp + 1$ is composite. The first auxiliary prime occurs at $k = 20$ ($q = 74,441$), which unconditionally eliminates the prime with $100\%$ elimination rate across all tested auxiliary primes.

---

## 3. Audited Refutations of Dead-End Hypotheses

### Refutation of Candidate C270 (Shimura Curve Descent)
- **Claim**: Indefinite quaternion algebras $B / \mathbb{Q}$ have Shimura curves $X_D$ with no real points ($X_D(\mathbb{R}) = \emptyset$), supposedly forcing the rational points of generalized Frey varieties to be empty.
- **Flaw**: A Frey variety having an $\ell$-adic representation matching a quaternionic modular form does not mean the Frey variety itself is a point on $X_D(\mathbb{Q})$. The modularity of higher-dimensional abelian varieties over number fields not totally real is an open conjecture, and conflating the representation with the curve is Failure Mode 1.
- **Status**: REFUTED.

### Refutation of Candidate C271 (Unramified Abelian Quotient)
- **Claim**: The inertia representation at $p$ forces an unramified abelian quotient of $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}(\zeta_p))$, contradicting class field theory.
- **Flaw**: The Serre conductor primes 2 and 3 can absorb the inertia representation through wild ramification, so the resulting extension is not unramified at 2 and 3.
- **Status**: REFUTED.
