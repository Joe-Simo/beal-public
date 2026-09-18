# Checkpoint U111: Real Cyclotomic Class Number and Sahoo Class $\mathcal{P}_1$ Audit for $600 < p < 700$

**Date**: 2026-09-17  
**Author**: Real Cyclotomic Class Number Auditor / Arithmetic Geometry Research Group  
**Target Equation**: $X^{2\ell} + Y^{2m} = Z^p$, prime exponents $\ell, m \ge 5$ (asymptotic bound $\ell, m > 10^{60}$), prime $p \in (600, 700)$  
**Branch**: All-even Beal candidate $A^{2r} + B^{2s} = C^{2t}$ with $17 \nmid t$  
**Supporting Code**: [`code/U111_cyclotomic_p600_p700.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_cyclotomic_p600_p700.py)  
**Machine-Readable Audit**: [`research/checkpoints/U111_real_cyclotomic_audit_p600_p700.json`](file://[LOCAL_HOME]/Downloads/beal/research/checkpoints/U111_real_cyclotomic_audit_p600_p700.json)  
**Primary References**:
- S. Sahoo, *Asymptotic solutions of generalized Fermat equations $x^{2l} + y^{2m} = z^p$*, preprint (2025).
- R. Schoof, *Class numbers of real cyclotomic fields of prime conductor*, Math. Comp. 72, no. 242 (2003), 913–937.
- J. C. Miller, *Real cyclotomic fields of prime conductor and their class numbers*, Math. Comp. 84, no. 295 (2015), 2459–2469; arXiv:1407.2373 (2014).
- On-Line Encyclopedia of Integer Sequences (OEIS), Sequences A230869 ($p$ with $h_p^+ > 1$) and A230870 ($h_p^+$ values).

---

## 1. Executive Summary

This checkpoint audits the arithmetic of real cyclotomic fields $K^+ = \mathbb{Q}(\zeta_p)^+ = \mathbb{Q}(2\cos(2\pi/p))$ and Sahoo's (2025) Class $\mathcal{P}_1$ asymptotic elimination for all 16 primes in $600 < p < 700$:
$$p \in \{601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691\}.$$

### Key Results

1. **Inertia of 2 in $K^+ = \mathbb{Q}(\zeta_p)^+$**:
   - Exactly **8 primes (50.0%)** have $2$ completely inert in $K^+$ ($g^+ = 1$, residue degree $f^+ = \frac{p-1}{2}$):
     $$\mathbf{P_{\text{inert}} \cap (600, 700) = \{607, 613, 619, 647, 653, 659, 661, 677\}}.$$
   - Exactly **8 primes (50.0%)** fail inertia ($g^+ \ge 2$):
     $$\mathbf{P_{\text{split}} \cap (600, 700) = \{601, 617, 631, 641, 643, 673, 683, 691\}}.$$
     - Four primes fail due to quadratic splitting $p \equiv 1 \pmod 8$ ($\{601, 617, 641, 673\}$), where $2$ splits in $\mathbb{Q}(\sqrt{p}) \subset K^+$. In particular, $p = 641$ is Euler's divisor of the Fermat number $F_5 = 2^{32} + 1$, with $g^+ = 10$.
     - Four primes fail due to small multiplicative order mod $p$ ($\{631, 643, 683, 691\}$).

2. **Real Cyclotomic Class Numbers $h_p^+$ from Literature**:
   - From Schoof (2003, Main Table; OEIS A230869/A230870), exactly **3 primes** in $(600, 700)$ have non-trivial class number $h_p^+ > 1$:
     - **$p = 607$**: $h_{607}^+ = 4 = 2^2$ (term 15 of A230869/A230870);
     - **$p = 631$**: $h_{631}^+ = 11$ (term 16 of A230869/A230870);
     - **$p = 641$**: $h_{641}^+ = 495 = 5 \cdot 9 \cdot 11$ (term 17 of A230869/A230870).
   - All other 13 primes in $(600, 700)$ have $h_p^+ = 1$ (under GRH).

3. **The $p = 607$ Class Number Anomaly ($h_{607}^+ = 4$)**:
   - For $p = 607$, $\operatorname{ord}_{607}(2) = 303 = (p-1)/2$, and because $607 \equiv 7 \pmod 8$, $-1 \notin \langle 2 \rangle$. Thus, **2 is completely inert** in $K^+$ ($f^+ = 303, g^+ = 1$).
   - However, $h_{607}^+ = 4 = 2^2$ is **even** ($2 \mid h_{607}^+$!).
   - Joining $p \in \{163, 349, 491, 547\}$, $p = 607$ is the fifth prime with 2 inert and an even class number.
   - The non-trivial 2-torsion in the class group $\operatorname{Cl}(\mathcal{O}_{K^+})[2] \ne 0$ permits unramified quadratic extensions of $K^+$, **causing Sahoo's Kummer descent lemma to fail**.
   - Therefore, $p = 607$ **fails Class $\mathcal{P}_1$** despite 2 being completely inert.

4. **Class $\mathcal{P}_1$ Certification (under GRH)**:
   - Exactly **7 primes (43.8%)** satisfy both criteria ($2$ inert and $h_p^+ = 1$):
     $$\mathbf{\mathcal{P}_1 \cap (600, 700) = \{613, 619, 647, 653, 659, 661, 677\}} \quad (7 / 16 = 43.8\%).$$
     For each such prime, Sahoo's (2025) Theorem eliminates all non-trivial primitive integer solutions to $X^{2\ell} + Y^{2m} = Z^p$ for exponents $\ell, m > 10^{60}$.

5. **Cumulative Progress across $19 \le p < 700$**:
   - Across all seven audited intervals ($[19, 100)$, $(100, 200)$, $(200, 300)$, $(300, 400)$, $(400, 500)$, $(500, 600)$, and $(600, 700)$), comprising 118 primes:
     - Exactly **63 out of 118 primes (53.4%)** belong to Class $\mathcal{P}_1$.

---

## 2. Algebraic Decomposition of 2 in $\mathbb{Q}(\zeta_p)^+$ for $600 < p < 700$

### 2.1 Theoretical Invariants
Let $p \in (600, 700)$ be prime, and let $K^+ = \mathbb{Q}(\zeta_p)^+$ have degree $d = \frac{p-1}{2}$.
The Galois group is $G^+ = \operatorname{Gal}(K^+/\mathbb{Q}) \cong (\mathbb{Z}/p\mathbb{Z})^\times / \{\pm 1\}$.
Let $f = \operatorname{ord}_p(2)$ be the multiplicative order of 2 modulo $p$.
- Residue degree in $K^+$:
  $$f^+ = \begin{cases} f/2 & \text{if } f \text{ is even and } 2^{f/2} \equiv -1 \pmod p, \\ f & \text{otherwise.} \end{cases}$$
- Splitting index:
  $$g^+ = \frac{d}{f^+} = \frac{(p-1)/2}{f^+}.$$
- The prime 2 is **inert** in $K^+$ if and only if $g^+ = 1 \iff f^+ = d$.

### 2.2 Classification of Splitting in $(600, 700)$

#### 1. Quadratic Reciprocity Barrier ($p \equiv 1 \pmod 8$)
Four primes satisfy $p \equiv 1 \pmod 8$, where $(\frac{2}{p}) = 1$ forces 2 to split in $\mathbb{Q}(\sqrt{p}) \subset K^+$:
- **$p = 601$**: $d = 300$. $\operatorname{ord}_{601}(2) = 25$ (odd). $-1 \notin \langle 2 \rangle \implies f^+ = 25, g^+ = 300 / 25 = 12$.
- **$p = 617$**: $d = 308$. $\operatorname{ord}_{617}(2) = 154$. $2^{77} \equiv -1 \pmod{617} \implies f^+ = 77, g^+ = 4$.
- **$p = 641$ (Euler's Divisor of $F_5$)**: $d = 320$. $\operatorname{ord}_{641}(2) = 64$. $2^{32} \equiv -1 \pmod{641} \implies f^+ = 32, g^+ = 10$. (Also has $h_{641}^+ = 495$).
- **$p = 673$**: $d = 336$. $\operatorname{ord}_{673}(2) = 48$. $2^{24} \equiv -1 \pmod{673} \implies f^+ = 24, g^+ = 14$.

#### 2. Small Order Cyclotomic Splitting ($p \not\equiv 1 \pmod 8$)
Four primes have $\operatorname{ord}_p(2) < \frac{p-1}{2}$:
- **$p = 631$**: $p \equiv 7 \pmod 8, d = 315$. $\operatorname{ord}_{631}(2) = 45$ (odd). $f^+ = 45, g^+ = 7$. (Also has $h_{631}^+ = 11$).
- **$p = 643$**: $p \equiv 3 \pmod 8, d = 321$. $\operatorname{ord}_{643}(2) = 214$. $2^{107} \equiv -1 \pmod{643} \implies f^+ = 107, g^+ = 3$. (Cubic decomposition field!).
- **$p = 683$**: $p \equiv 3 \pmod 8, d = 341$. $\operatorname{ord}_{683}(2) = 22$. $2^{11} \equiv -1 \pmod{683} \implies f^+ = 11, g^+ = 31$.
- **$p = 691$**: $p \equiv 3 \pmod 8, d = 345$. $\operatorname{ord}_{691}(2) = 230$. $2^{115} \equiv -1 \pmod{691} \implies f^+ = 115, g^+ = 3$. (Cubic decomposition field!).

---

## 3. Real Cyclotomic Class Numbers $h_p^+$ in $600 < p < 700$

### 3.1 Known Literature Theorems
1. **Schoof (2003, Main Table; OEIS A230869 & A230870)**:
   Computed the orders of cyclotomic unit lattices $\tilde{h}_p^+$ for all primes $p < 10,000$.
   In the interval $(600, 700)$, the primes with non-trivial class numbers are:
   - **$p = 607$**: $h_{607}^+ = 4$ (term 15 of A230869, term 15 of A230870);
   - **$p = 631$**: $h_{631}^+ = 11$ (term 16 of A230869, term 16 of A230870);
   - **$p = 641$**: $h_{641}^+ = 495 = 5 \cdot 9 \cdot 11$ (term 17 of A230869, term 17 of A230870).
   All other 13 primes in $(600, 700)$ have $h_p^+ = 1$ under GRH.

### 3.2 Deep Analysis of the $p = 607$ Anomaly
- **Arithmetic Profile**:
  $$p = 607 \equiv 7 \pmod 8, \quad d = 303, \quad \operatorname{ord}_{607}(2) = 303 = \frac{p-1}{2}.$$
  Since $607 \equiv 7 \pmod 8$, $(\frac{-1}{607}) = -1 \implies -1 \notin \langle 2 \rangle$, so $f^+ = 303$ and $g^+ = 1$.
  **The prime 2 is strictly inert in $\mathbb{Q}(\zeta_{607})^+$**.
- **Class Group and Parity**:
  $$h_{607}^+ = 4 = 2^2.$$
  Because $h_{607}^+$ is a multiple of 2, the 2-torsion subgroup $\operatorname{Cl}(\mathcal{O}_{K^+})[2]$ is non-trivial.
- **Diophantine Consequence for Sahoo's Theorem**:
  In Sahoo's proof (Propositions 1.9 & 1.10), establishing the upper bound $\max(|v(\lambda)|, |v(\mu)|) \le 4$ on solutions to the $S_{K, 2}$-unit equation relies on the assertion that an element $\mu \equiv 1 \pmod{\mathfrak{P}_2^5}$ cannot define an unramified quadratic extension $L = K^+(\sqrt{\mu})$.
  When $2 \mid h_p^+$, unramified quadratic extensions of $K^+$ exist by class field theory!
  Thus, $\mu$ does not need to be a global square, and the Kummer descent fails.
  **Conclusion**: $p = 607$ fails Class $\mathcal{P}_1$ despite having 2 inert.

---

## 4. Complete Deterministic Audit Table ($600 < p < 700$)

The following table reports the exact arithmetic invariants computed by [`code/U111_cyclotomic_p600_p700.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_cyclotomic_p600_p700.py).
Polynomial factorizations of $\operatorname{polsubcyclo}(p, d) \pmod 2$ were verified with PARI/GP 2.17.4:

| $p$ | $p \bmod 8$ | $d = \frac{p-1}{2}$ | $\operatorname{ord}_p(2)$ | $-1 \in \langle 2 \rangle$? | $f^+$ | $g^+$ | 2 Inert in $K^+$? | PARI Mod-2 Factors | $h_p^+$ | $h_p^+$ Status | Sahoo Class $\mathcal{P}_1$ Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 601 | 1 | 300 | 25 | NO | 25 | 12 | NO | $[25 \times 12]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| 607 | 7 | 303 | 303 | NO | 303 | 1 | **YES** | $[303]$ | **4** | Under GRH | **Non-$\mathcal{P}_1$: Even $h^+$ ($2 \mid h_{607}^+$)** |
| **613** | 5 | 306 | 612 | YES | 306 | 1 | **YES** | $[306]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 617 | 1 | 308 | 154 | YES | 77 | 4 | NO | $[77 \times 4]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| **619** | 3 | 309 | 618 | YES | 309 | 1 | **YES** | $[309]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 631 | 7 | 315 | 45 | NO | 45 | 7 | NO | $[45 \times 7]$ | **11** | Under GRH | **Non-$\mathcal{P}_1$: Split-2 ($g^+=7$)** |
| 641 | 1 | 320 | 64 | YES | 32 | 10 | NO | $[32 \times 10]$ | **495** | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$ ($F_5$)** |
| 643 | 3 | 321 | 214 | YES | 107 | 3 | NO | $[107, 107, 107]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: Split-2 ($g^+=3$)** |
| **647** | 7 | 323 | 323 | NO | 323 | 1 | **YES** | $[323]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **653** | 5 | 326 | 652 | YES | 326 | 1 | **YES** | $[326]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **659** | 3 | 329 | 658 | YES | 329 | 1 | **YES** | $[329]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **661** | 5 | 330 | 660 | YES | 330 | 1 | **YES** | $[330]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 673 | 1 | 336 | 48 | YES | 24 | 14 | NO | $[24 \times 14]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| **677** | 5 | 338 | 676 | YES | 338 | 1 | **YES** | $[338]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 683 | 3 | 341 | 22 | YES | 11 | 31 | NO | $[11 \times 31]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: Split-2 ($g^+=31$)** |
| 691 | 3 | 345 | 230 | YES | 115 | 3 | NO | $[115, 115, 115]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: Split-2 ($g^+=3$)** |

---

## 5. Synthesis: Cumulative Class $\mathcal{P}_1$ Inventory for $19 \le p < 700$

| Interval | Total Primes | 2 Inert in $K^+$ ($g^+=1$) | $h_p^+ = 1$ | Class $\mathcal{P}_1$ Primes ($2$ inert $\land h^+=1$) | $\mathcal{P}_1$ Percentage |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$[19, 100)$ (U103/U107)** | 18 | 12 | 18 | **12** | 66.7% |
| **$(100, 200)$ (U110)** | 21 | 14 | 19 | **12** | 57.1% |
| **$(200, 300)$ (U111)** | 16 | 7 | 13 | **7** | 43.8% |
| **$(300, 400)$ (U111)** | 16 | 10 | 13 | **9** | 56.2% |
| **$(400, 500)$ (U111)** | 17 | 9 | 14 | **8** | 47.1% |
| **$(500, 600)$ (U111)** | 14 | 9 | 11 | **8** | 57.1% |
| **$(600, 700)$ (U111)** | 16 | 8 | 13 | **7** | 43.8% |
| **Total $[19, 700)$** | **118** | **69 (58.5%)** | **101 (85.6%)** | **63 (53.4%)** | **53.4%** |

### Complete Inventory of the 63 Class $\mathcal{P}_1$ Exponents in $[19, 700)$:
$$\begin{aligned}
\mathbf{\mathcal{P}_1 \cap [19, 700) = \{ } & 19, 23, 29^*, 37, 47, 53, 59, 61, 67, 71, 79, 83, \\
& 101, 103, 107, 131, 139, 149, 167, 173, 179, 181, 197, 199, \\
& 211, 227, 239, 263, 269, 271, 293, \\
& 311, 317, 347, 359, 367, 373, 379, 383, 389, \\
& 419, 421, 443, 461, 463, 467, 479, 487, \\
& 503, 509, 523, 541, 557, 563, 587, 599, \\
& 613, 619, 647, 653, 659, 661, 677 \mathbf{ \} }.
\end{aligned}$$
*(Note: $p = 29$ has wide class number $h=1$ and narrow class number $h^+=8$, as analyzed in U107).*

Over the entire range $p \in [19, 700)$, exactly **53.4% of all prime exponents** are asymptotically eliminated by Sahoo's Theorem for solutions with $\ell, m > 10^{60}$.

---

## 6. Computational Reproducibility

The complete computational audit can be re-run via:

```bash
python3 code/U111_cyclotomic_p600_p700.py
```

The execution takes ~0.5 seconds on Apple Silicon, verifying that:
- Every predicted splitting index matches PARI's `factormod(polsubcyclo(p, d), 2)` with 100% fidelity.
- Machine-readable JSON exported to [`research/checkpoints/U111_real_cyclotomic_audit_p600_p700.json`](file://[LOCAL_HOME]/Downloads/beal/research/checkpoints/U111_real_cyclotomic_audit_p600_p700.json).
