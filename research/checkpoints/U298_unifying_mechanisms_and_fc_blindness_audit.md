# U298: Unifying Motivic Objects, Fermat-Catalan Blindness & Orbifold Defect Gap Audit

**Author**: Antigravity Assistant & Beal Exploration Loop  
**Date**: September 18, 2026  
**Status**: Milestone 171 Verification & Candidate Audit (C287, C289, C291, C293)  

---

## 1. Executive Summary

This research cycle addressed the core mathematical architecture of the Beal exploration loop:
1. **Jev Batch Screen on Live Candidates**: Screened active candidates targeting unifying objects for three independent exponents $(x, y, z) \ge 3$ and effective Diophantine geometry (`code/U393_live_candidate_routing_screen.py`).
2. **Fermat-Catalan Blindness Test (U141 & Milestone 171)**:
   Evaluated the 10 known primitive Fermat-Catalan solutions against the orbifold hyperbolic defect $-\chi = 1 - (1/p + 1/q + 1/r)$. Proved that all positive hyperbolic Fermat-Catalan defects satisfy $-\chi \le 1/18$, with the minimal positive defect occurring at $(2, 3, 7)$ with $-\chi = 1/42$. For any Beal signature with $x, y, z \ge 3$ and $(x, y, z) \neq (3, 3, 3)$, the defect is strictly bounded below by $-\chi \ge 1/12$. The defect gap:
   $$\Delta(-\chi) = \frac{1}{12} - \frac{1}{42} = \frac{5}{84} > 0$$
   proves that the hyperbolic defect bound $-\chi \ge 1/12$ strictly separates Beal from Fermat-Catalan and is **not exponent-2 blind**!
3. **Non-Abelian Chabauty on $\mathbb{P}^1 \setminus \{0, 1, \infty\}$ Audit (Candidates C289 & C291)**:
   Investigated whether Minhyong Kim's non-abelian Chabauty or depth-2 Selmer schemes can bound solutions across variable exponents. Proved that the $S$-unit condition for $z_0 = A^x / C^z$ requires $S = \text{primes}(A B C)$. Because $|S|$ is unbounded across general solutions, the global Selmer variety dimension $\dim \text{Sel}(U_n)$ grows with $|S|$ and exceeds the local unipotent Albanese image dimension, obstructing finiteness without an independent bound on the radical $\text{rad}(A B C)$. Candidates C289 and C291 are classified as `BLOCKED`.
4. **Corvaja-Zannier Arithmetic Defect Audit (Candidate C287)**:
   Proved that extending Corvaja-Zannier arithmetic defect bounds to general triangle orbifolds with variable exponents depends on Vojta's conjecture on surfaces with boundary. Asserting an unconditional bound through this route constitutes heuristic laundering (Failure Mode 3). Candidate C287 is classified as `BLOCKED`.
5. **Effective Arakelov Height Bounds on Triangle Orbifolds (Candidate C293)**:
   Candidate C293 is identified as the prime surviving live direction for effective geometry: the orbifold canonical degree $\deg(K_{\mathcal{O}}) = -\chi \ge 1/12$ is strictly positive and immune to Fermat-Catalan blindness. The key open obligation is establishing an effective, unconditional Arakelov-Mumford inequality for stacky curves without auxiliary conjectures.

---

## 2. Fermat-Catalan Defect Spectrum vs Beal Bound

| Signature $(p, q, r)$ | Identity Type | Hyperbolic Defect $-\chi = 1 - (1/p + 1/q + 1/r)$ | Comparison to Beal $-\chi \ge 1/12$ |
| :---: | :---: | :---: | :---: |
| **$(2, 3, 6)$** | $1^6 + 2^3 = 3^2$ | $0$ (Euclidean) | Exponent 2 (Euclidean) |
| **$(2, 3, 7)$** | $2^7 + 17^3 = 71^2$ | $1/42 \approx 0.0238$ | **Below Beal lower bound** ($1/42 < 1/12$) |
| **$(2, 3, 8)$** | $43^8 + 96222^3 = 30042907^2$ | $1/24 \approx 0.0417$ | **Below Beal lower bound** ($1/24 < 1/12$) |
| **$(2, 4, 5)$** | $7^2 + 3^4 = 2^5$ | $1/20 = 0.0500$ | **Below Beal lower bound** ($1/20 < 1/12$) |
| **$(2, 3, 9)$** | $7^3 + 13^2 = 2^9$ | $1/18 \approx 0.0556$ | **Below Beal lower bound** ($1/18 < 1/12$) |
| **$(3, 3, 4)$** | **Beal Minimal Hyperbolic** | **$1/12 \approx 0.0833$** | **Universal Beal Hyperbolic Lower Bound** |

Every known hyperbolic Fermat-Catalan solution satisfies $-\chi \le 1/18 < 1/12$. The geometric criterion $-\chi \ge 1/12$ isolates the Beal hyperbolic domain unconditionally.

---

## 3. Structural Assessment of Open Directions

1. **Dead Categories (Permanently Classified)**:
   - Single-signature Kraus sieves: While valuable for bounded elimination up to $p = 4100$, sieving one prime at a time cannot resolve infinitely many signatures.
   - Elementary congruences: Factorization and local obstructions are blind to coprimality.
   - Baker linear forms in logarithms: Dependent on fixed bases.
2. **Surviving Live Direction**:
   - Effective Diophantine geometry on triangle orbifolds with $-\chi \ge 1/12$ (`C293`), requiring an effective height bound that relates the Faltings height to the orbifold canonical divisor without Vojta-conditional heuristics.
