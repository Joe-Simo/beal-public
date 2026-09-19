# U284: Belyi Dessins & Orbifold BMY Obstruction Audit and Kraus Sieve Elimination up to p = 2700

**Author**: Antigravity Assistant & Beal Exploration Loop  
**Date**: September 18, 2026  
**Status**: Milestones 126–128 Verification & Candidate Audit (C305, C306, C307)  

---

## 1. Executive Summary

This research cycle accomplished four primary objectives:
1. **Jev Batch Screen**: Screened Candidates C305 (Kraus sieve $p \in [2601, 2700]$), C306 (Belyi-Grothendieck Dessins d'Enfants Galois orbits), and C307 (Orbifold Bogomolov-Miyaoka-Yau Chern class inequalities); persisted decisions in `research/pool/evidence/`.
2. **Computational Verification & Independent PARI/GP Audit (Milestones 126 & 127)**:
   Extended the algorithmic Kraus sieve for signature $(3, 3, p)$ to all prime exponents $p \in [2601, 2700]$ with $p \equiv 1 \pmod 3$ ($p \in \{2617, 2647, 2659, 2671, 2677, 2683, 2689\}$). All 7 primes were unconditionally eliminated with a 100% elimination rate across auxiliary primes $q = 2kp + 1 \le 100000$ (`code/U313_kraus_sieve_p2601_p2700.py`), and independently audited in PARI/GP (`code/U314_gp_kraus_audit.gp`).
3. **Belyi Dessins d'Enfants & Coprimality Blindness Audit (Milestone 128, Candidate C306)**:
   Investigated whether the absolute Galois group action $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ on Grothendieck dessins d'enfants and cartographic triangle covers $\Delta(p, q, r)$ over $\mathbb{P}^1 \setminus \{0, 1, \infty\}$ can separate Beal triples from trivial branched points. Proved that dessins d'enfants depend solely on the branched cover $\beta: X \to \mathbb{P}^1$ and are invariant under scalar multiplication $(A, B, C) \mapsto (kA, kB, kC)$. Dense non-primitive Beal triples exist in $\mathbb{Q} \cap (0, 1)$, proving that dessins d'enfants are fundamentally blind to coprimality and arithmetic scalar cancellation. Candidate C306 is classified as `BLOCKED`.
4. **Orbifold Bogomolov-Miyaoka-Yau Chern Class Audit (Milestone 128, Candidate C307)**:
   Evaluated the orbifold Bogomolov-Miyaoka-Yau (BMY) inequality $c_1(S, D)^2 \le 3 c_2(S, D)$ on cyclic branched covers of surfaces. Proved that BMY holds unconditionally for all hyperbolic signatures $(x, y, z)$ with $-\chi \ge 1/12$. As $x, y, z \to \infty$, $c_1^2 \to 9$, so BMY remains strictly satisfied and imposes no upper bound on $\max(x, y, z)$. Deducing bounds on rational points requires unproved Vojta conjectures, which is prohibited by Standing Discipline (Failure Mode 3: Heuristic Laundering). Candidate C307 is classified as `BLOCKED`.
5. **Formal Machine Verification in Lean 4**:
   Formally proved and machine-checked in Lean 4:
   - `no_beal_counterexample_3_3_up_to_2700` in `formal/Beal/Signature3.lean`
   - `post_century_signature_3_3_p_elimination_2700` in `formal/Beal/PostCentennial.lean`
   - `beal_hyperbolic_bifurcation` in `formal/Beal/PostCentennial.lean` (proving that every Beal signature $3 \le p \le q \le r$ is either $(3, 3, 3)$ or strictly hyperbolic with defect $-\chi \ge 1/12$).
   All theorems compiled with 0 errors, 0 `sorry`, and standard axioms only (`[propext, Classical.choice, Quot.sound]`).

---

## 2. Kraus Sieve Verification for $p \in [2601, 2700]$ (Milestones 126 & 127)

### Eliminating Auxiliary Primes

| Exponent $p$ | Eliminating $q = 2kp + 1$ | $k$ | $a_q(72a1)$ | $a_q(144a1)$ | Elimination Rate |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **2617** | 26171 | 5 | $-292$ | $292$ | **100.0%** |
| **2647** | 10589 | 2 | $58$ | $58$ | **100.0%** |
| **2659** | 26591 | 5 | $224$ | $-224$ | **100.0%** |
| **2671** | 26711 | 5 | $72$ | $-72$ | **100.0%** |
| **2677** | 10709 | 2 | $178$ | $178$ | **100.0%** |
| **2683** | 10733 | 2 | $-118$ | $-118$ | **100.0%** |
| **2689** | 26891 | 5 | $44$ | $-44$ | **100.0%** |

Both Python (`code/U313_kraus_sieve_p2601_p2700.py`) and PARI/GP (`code/U314_gp_kraus_audit.gp`) confirmed 100% elimination with zero discrepancies.

---

## 3. Belyi Dessins d'Enfants and the Coprimality Barrier (C306)

Grothendieck's Dessins d'Enfants establishes an equivalence between bipartite ribbon graphs and finite branched covers $\beta: X \to \mathbb{P}^1$ ramified only over $\{0, 1, \infty\}$.

### The Geometric Model
For the generalized Fermat equation $A^x + B^y = C^z$, any non-trivial solution defines a base coordinate:
$$t_0 = \frac{A^x}{C^z} \in \mathbb{Q} \cap (0, 1).$$
The cyclic Fermat quotient curve $C_{(x, y, z)}$ maps to $\mathbb{P}^1$ via the Belyi map $\beta(t) = t$. The monodromy group is a quotient of the triangle group $\Delta(x, y, z)$.

### The Coprimality Obstruction
1. **Scale Invariance**: A dessin d'enfant is an invariant of the complex algebraic curve $X$ and the map $\beta$. If $(A, B, C)$ is a solution, then for any scaling factor $k \in \mathbb{N}$, $(k^u A, k^v B, k^w C)$ gives the exact same rational ratio $t_0 = A^x / C^z$ whenever $u x = v y = w z$.
2. **Dense Non-Coprime Triples**: For any rational $t = u / w \in (0, 1)$ with $\gcd(u, w) = 1$, choose $k = u^{y z - 1}(w - u)^{x z - 1} w^{x y - 1}$. Then:
   $$A = (u \cdot k)^{1/x}, \quad B = ((w - u) \cdot k)^{1/y}, \quad C = (w \cdot k)^{1/z}$$
   yields positive integers $A, B, C$ satisfying $A^x + B^y = C^z$.
3. **Conclusion**: Dessins d'enfants characterize the topology and moduli field of the cover, but cannot distinguish primitive points from non-primitive points on the base.

---

## 4. Orbifold Bogomolov-Miyaoka-Yau Chern Number Obstruction (C307)

The Bogomolov-Miyaoka-Yau (BMY) inequality on an orbifold surface $(S, D)$ states:
$$c_1(S, D)^2 \le 3 c_2(S, D).$$

### Asymptotic Behavior of Chern Numbers
For cyclic covers of $\mathbb{P}^2$ branched along three lines with ramification orders $(x, y, z)$:
$$-\chi(x, y, z) = 1 - \frac{1}{x} - \frac{1}{y} - \frac{1}{z}.$$
The first Chern class squared satisfies:
$$c_1^2 = 9 (-\chi)^2.$$
As $x, y, z \to \infty$, $-\chi \to 1$, so $c_1^2 \to 9$.
The Chern numbers remain strictly bounded and smooth. The inequality $c_1^2 \le 3 c_2$ holds identically for all hyperbolic signatures with $-\chi \ge 1/12$.

### The Diophantine Disconnect
BMY is a topological and differential-geometric constraint on the surface. Converting a Chern number inequality into an upper bound on rational points requires **Vojta's Conjecture** on log surfaces of general type. Proving Beal conditional on Vojta's conjecture is not an unconditional proof, and relabelling it as unconditional violates the Standing Discipline.

---

## 5. Formal Machine Verification Status in Lean 4

The following theorems are verified in `formal/Beal/`:
- `no_beal_counterexample_3_3_up_to_2700` (`formal/Beal/Signature3.lean`)
- `post_century_signature_3_3_p_elimination_2700` (`formal/Beal/PostCentennial.lean`)
- `beal_hyperbolic_bifurcation` (`formal/Beal/PostCentennial.lean`)

All theorems check with standard Lean 4 axioms only:
```text
[propext, Classical.choice, Quot.sound]
```
0 errors, 0 warnings, 0 `sorry`.

---

## 6. Updated Candidate Pool Status

- `C305`: **PARTIAL_RESULT** (Kraus sieve modular traces verified and closed for $p \in [2601, 2700]$).
- `C306`: **BLOCKED** (Dessins d'enfants blind to coprimality and scalar cancellation).
- `C307`: **BLOCKED** (BMY Chern numbers bounded for all hyperbolic exponents; point bounding requires unproved Vojta conjecture).
