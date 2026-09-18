# Checkpoint U111: Real Cyclotomic Class Number and Sahoo Class $\mathcal{P}_1$ Audit for $500 < p < 600$

**Date**: 2026-09-17  
**Author**: Real Cyclotomic Class Number Auditor / Arithmetic Geometry Research Group  
**Target Equation**: $X^{2\ell} + Y^{2m} = Z^p$, prime exponents $\ell, m \ge 5$ (asymptotic bound $\ell, m > 10^{60}$), prime $p \in (500, 600)$  
**Branch**: All-even Beal candidate $A^{2r} + B^{2s} = C^{2t}$ with $17 \nmid t$  
**Supporting Code**: [`code/U111_cyclotomic_p500_p600.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_cyclotomic_p500_p600.py)  
**Machine-Readable Audit**: [`research/checkpoints/U111_real_cyclotomic_audit_p500_p600.json`](file://[LOCAL_HOME]/Downloads/beal/research/checkpoints/U111_real_cyclotomic_audit_p500_p600.json)  
**Primary References**:
- S. Sahoo, *Asymptotic solutions of generalized Fermat equations $x^{2l} + y^{2m} = z^p$*, preprint (2025).
- R. Schoof, *Class numbers of real cyclotomic fields of prime conductor*, Math. Comp. 72, no. 242 (2003), 913–937.
- J. C. Miller, *Real cyclotomic fields of prime conductor and their class numbers*, Math. Comp. 84, no. 295 (2015), 2459–2469; arXiv:1407.2373 (2014).
- On-Line Encyclopedia of Integer Sequences (OEIS), Sequences A230869 ($p$ with $h_p^+ > 1$) and A230870 ($h_p^+$ values).

---

## 1. Executive Summary

This checkpoint audits the arithmetic of real cyclotomic fields $K^+ = \mathbb{Q}(\zeta_p)^+ = \mathbb{Q}(2\cos(2\pi/p))$ and Sahoo's (2025) Class $\mathcal{P}_1$ asymptotic elimination for all 14 primes in $500 < p < 600$:
$$p \in \{503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599\}.$$

### Key Results

1. **Inertia of 2 in $K^+ = \mathbb{Q}(\zeta_p)^+$**:
   - Exactly **9 primes (64.3%)** have $2$ completely inert in $K^+$ ($g^+ = 1$, residue degree $f^+ = \frac{p-1}{2}$):
     $$\mathbf{P_{\text{inert}} \cap (500, 600) = \{503, 509, 523, 541, 547, 557, 563, 587, 599\}}.$$
   - Exactly **5 primes (35.7%)** fail inertia ($g^+ \ge 2$):
     $$\mathbf{P_{\text{split}} \cap (500, 600) = \{521, 569, 571, 577, 593\}}.$$
     - Four primes fail due to quadratic splitting $p \equiv 1 \pmod 8$ ($\{521, 569, 577, 593\}$), where $2$ splits in $\mathbb{Q}(\sqrt{p}) \subset K^+$.
     - One prime fails due to small order mod $p$ ($p = 571$, $g^+ = 5$).

2. **Real Cyclotomic Class Numbers $h_p^+$ from Literature**:
   - From Schoof (2003, Main Table; OEIS A230869/A230870), exactly **3 primes** in $(500, 600)$ have non-trivial class number $h_p^+ > 1$:
     - **$p = 521$**: $h_{521}^+ = 27 = 3^3$ (term 12 of A230869/A230870);
     - **$p = 547$**: $h_{547}^+ = 4 = 2^2$ (term 13 of A230869/A230870);
     - **$p = 577$**: $h_{577}^+ = 7$ (term 14 of A230869/A230870).
   - All other 11 primes in $(500, 600)$ have $h_p^+ = 1$ (under GRH).

3. **The $p = 547$ Class Number Anomaly ($h_{547}^+ = 4$)**:
   - For $p = 547$, $\operatorname{ord}_{547}(2) = 546 = p - 1$, so **2 is completely inert** in $K^+$ ($f^+ = 273, g^+ = 1$).
   - However, $h_{547}^+ = 4 = 2^2$ is **even** ($2 \mid h_{547}^+$!).
   - Joining $p = 163$ ($h_{163}^+ = 4$), $p = 349$ ($h_{349}^+ = 16$), and $p = 491$ ($h_{491}^+ = 8$), $p = 547$ is the fourth prime with 2 inert and an even class number.
   - The non-trivial 2-torsion in the class group $\operatorname{Cl}(\mathcal{O}_{K^+})[2] \ne 0$ permits unramified quadratic extensions of $K^+$, **causing Sahoo's Kummer descent lemma to fail**.
   - Therefore, $p = 547$ **fails Class $\mathcal{P}_1$** despite 2 being completely inert.

4. **Class $\mathcal{P}_1$ Certification (under GRH)**:
   - Exactly **8 primes (57.1%)** satisfy both criteria ($2$ inert and $h_p^+ = 1$):
     $$\mathbf{\mathcal{P}_1 \cap (500, 600) = \{503, 509, 523, 541, 557, 563, 587, 599\}} \quad (8 / 14 = 57.1\%).$$
     For each such prime, Sahoo's (2025) Theorem eliminates all non-trivial primitive integer solutions to $X^{2\ell} + Y^{2m} = Z^p$ for exponents $\ell, m > 10^{60}$.

5. **Cumulative Progress across $19 \le p < 600$**:
   - Across all six audited intervals ($[19, 100)$, $(100, 200)$, $(200, 300)$, $(300, 400)$, $(400, 500)$, and $(500, 600)$), comprising 102 primes:
     - Exactly **56 out of 102 primes (54.9%)** belong to Class $\mathcal{P}_1$.

---

## 2. Algebraic Decomposition of 2 in $\mathbb{Q}(\zeta_p)^+$ for $500 < p < 600$

### 2.1 Theoretical Invariants
Let $p \in (500, 600)$ be prime, and let $K^+ = \mathbb{Q}(\zeta_p)^+$ have degree $d = \frac{p-1}{2}$.
The Galois group is $G^+ = \operatorname{Gal}(K^+/\mathbb{Q}) \cong (\mathbb{Z}/p\mathbb{Z})^\times / \{\pm 1\}$.
Let $f = \operatorname{ord}_p(2)$ be the multiplicative order of 2 modulo $p$.
- Residue degree in $K^+$:
  $$f^+ = \begin{cases} f/2 & \text{if } f \text{ is even and } 2^{f/2} \equiv -1 \pmod p, \\ f & \text{otherwise.} \end{cases}$$
- Splitting index:
  $$g^+ = \frac{d}{f^+} = \frac{(p-1)/2}{f^+}.$$
- The prime 2 is **inert** in $K^+$ if and only if $g^+ = 1 \iff f^+ = d$.

### 2.2 Classification of Splitting in $(500, 600)$

#### 1. Quadratic Reciprocity Barrier ($p \equiv 1 \pmod 8$)
Four primes satisfy $p \equiv 1 \pmod 8$, where $(\frac{2}{p}) = 1$ forces 2 to split in $\mathbb{Q}(\sqrt{p}) \subset K^+$:
- **$p = 521$**: $d = 260$. $\operatorname{ord}_{521}(2) = 260 = (p-1)/2$. Because $2^{130} \equiv -1 \pmod{521}$, $f^+ = 130, g^+ = 2$. (Also has $h_{521}^+ = 27$).
- **$p = 569$**: $d = 284$. $\operatorname{ord}_{569}(2) = 284 = (p-1)/2$. Because $2^{142} \equiv -1 \pmod{569}$, $f^+ = 142, g^+ = 2$.
- **$p = 577$**: $d = 288$. $\operatorname{ord}_{577}(2) = 144$. $2^{72} \equiv -1 \pmod{577} \implies f^+ = 72, g^+ = 4$. (Also has $h_{577}^+ = 7$).
- **$p = 593$**: $d = 296$. $\operatorname{ord}_{593}(2) = 148$. $2^{74} \equiv -1 \pmod{593} \implies f^+ = 74, g^+ = 4$.

#### 2. Small Order Cyclotomic Splitting ($p \not\equiv 1 \pmod 8$)
Only one prime has $\operatorname{ord}_p(2) < \frac{p-1}{2}$:
- **$p = 571$**: $p \equiv 3 \pmod 8, d = 285$. $\operatorname{ord}_{571}(2) = 114$. $2^{57} \equiv -1 \pmod{571} \implies f^+ = 57, g^+ = 5$.

---

## 3. Real Cyclotomic Class Numbers $h_p^+$ in $500 < p < 600$

### 3.1 Known Literature Theorems
1. **Schoof (2003, Main Table; OEIS A230869 & A230870)**:
   Computed the orders of cyclotomic unit lattices $\tilde{h}_p^+$ for all primes $p < 10,000$.
   In the interval $(500, 600)$, the primes with non-trivial class numbers are:
   - **$p = 521$**: $h_{521}^+ = 27$ (term 12 of A230869, term 12 of A230870);
   - **$p = 547$**: $h_{547}^+ = 4$ (term 13 of A230869, term 13 of A230870);
   - **$p = 577$**: $h_{577}^+ = 7$ (term 14 of A230869, term 14 of A230870).
   All other 11 primes in $(500, 600)$ have $h_p^+ = 1$ under GRH.

### 3.2 Deep Analysis of the $p = 547$ Anomaly
- **Arithmetic Profile**:
  $$p = 547 \equiv 3 \pmod 8, \quad d = 273, \quad \operatorname{ord}_{547}(2) = 546 = p - 1.$$
  Since 2 is a primitive root mod 547, $2^{273} \equiv -1 \pmod{547}$, so $f^+ = 273$ and $g^+ = 1$.
  **The prime 2 is strictly inert in $\mathbb{Q}(\zeta_{547})^+$**.
- **Class Group and Parity**:
  $$h_{547}^+ = 4 = 2^2.$$
  Because $h_{547}^+$ is a multiple of 2, the 2-torsion subgroup $\operatorname{Cl}(\mathcal{O}_{K^+})[2]$ is non-trivial.
- **Diophantine Consequence for Sahoo's Theorem**:
  In Sahoo's proof (Propositions 1.9 & 1.10), establishing the upper bound $\max(|v(\lambda)|, |v(\mu)|) \le 4$ on solutions to the $S_{K, 2}$-unit equation relies on the assertion that an element $\mu \equiv 1 \pmod{\mathfrak{P}_2^5}$ cannot define an unramified quadratic extension $L = K^+(\sqrt{\mu})$.
  When $2 \mid h_p^+$, unramified quadratic extensions of $K^+$ exist by class field theory!
  Thus, $\mu$ does not need to be a global square, and the Kummer descent fails.
  **Conclusion**: $p = 547$ fails Class $\mathcal{P}_1$ despite having 2 inert.

---

## 4. Complete Deterministic Audit Table ($500 < p < 600$)

The following table reports the exact arithmetic invariants computed by [`code/U111_cyclotomic_p500_p600.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_cyclotomic_p500_p600.py).
Polynomial factorizations of $\operatorname{polsubcyclo}(p, d) \pmod 2$ were verified with PARI/GP 2.17.4:

| $p$ | $p \bmod 8$ | $d = \frac{p-1}{2}$ | $\operatorname{ord}_p(2)$ | $-1 \in \langle 2 \rangle$? | $f^+$ | $g^+$ | 2 Inert in $K^+$? | PARI Mod-2 Factors | $h_p^+$ | $h_p^+$ Status | Sahoo Class $\mathcal{P}_1$ Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **503** | 7 | 251 | 251 | NO | 251 | 1 | **YES** | $[251]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **509** | 5 | 254 | 508 | YES | 254 | 1 | **YES** | $[254]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 521 | 1 | 260 | 260 | YES | 130 | 2 | NO | $[130, 130]$ | **27** | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| **523** | 3 | 261 | 522 | YES | 261 | 1 | **YES** | $[261]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **541** | 5 | 270 | 540 | YES | 270 | 1 | **YES** | $[270]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 547 | 3 | 273 | 546 | YES | 273 | 1 | **YES** | $[273]$ | **4** | Under GRH | **Non-$\mathcal{P}_1$: Even $h^+$ ($2 \mid h_{547}^+$)** |
| **557** | 5 | 278 | 556 | YES | 278 | 1 | **YES** | $[278]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **563** | 3 | 281 | 562 | YES | 281 | 1 | **YES** | $[281]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 569 | 1 | 284 | 284 | YES | 142 | 2 | NO | $[142, 142]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| 571 | 3 | 285 | 114 | YES | 57 | 5 | NO | $[57 \times 5]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: Split-2 ($g^+=5$)** |
| 577 | 1 | 288 | 144 | YES | 72 | 4 | NO | $[72 \times 4]$ | **7** | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| **587** | 3 | 293 | 586 | YES | 293 | 1 | **YES** | $[293]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 593 | 1 | 296 | 148 | YES | 74 | 4 | NO | $[74 \times 4]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| **599** | 7 | 299 | 299 | NO | 299 | 1 | **YES** | $[299]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |

---

## 5. Synthesis: Cumulative Class $\mathcal{P}_1$ Inventory for $19 \le p < 600$

| Interval | Total Primes | 2 Inert in $K^+$ ($g^+=1$) | $h_p^+ = 1$ | Class $\mathcal{P}_1$ Primes ($2$ inert $\land h^+=1$) | $\mathcal{P}_1$ Percentage |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$[19, 100)$ (U103/U107)** | 18 | 12 | 18 | **12** | 66.7% |
| **$(100, 200)$ (U110)** | 21 | 14 | 19 | **12** | 57.1% |
| **$(200, 300)$ (U111)** | 16 | 7 | 13 | **7** | 43.8% |
| **$(300, 400)$ (U111)** | 16 | 10 | 13 | **9** | 56.2% |
| **$(400, 500)$ (U111)** | 17 | 9 | 14 | **8** | 47.1% |
| **$(500, 600)$ (U111)** | 14 | 9 | 11 | **8** | 57.1% |
| **Total $[19, 600)$** | **102** | **61 (59.8%)** | **88 (86.3%)** | **56 (54.9%)** | **54.9%** |

### Complete Inventory of the 56 Class $\mathcal{P}_1$ Exponents in $[19, 600)$:
$$\begin{aligned}
\mathbf{\mathcal{P}_1 \cap [19, 600) = \{ } & 19, 23, 29^*, 37, 47, 53, 59, 61, 67, 71, 79, 83, \\
& 101, 103, 107, 131, 139, 149, 167, 173, 179, 181, 197, 199, \\
& 211, 227, 239, 263, 269, 271, 293, \\
& 311, 317, 347, 359, 367, 373, 379, 383, 389, \\
& 419, 421, 443, 461, 463, 467, 479, 487, \\
& 503, 509, 523, 541, 557, 563, 587, 599 \mathbf{ \} }.
\end{aligned}$$
*(Note: $p = 29$ has wide class number $h=1$ and narrow class number $h^+=8$, as analyzed in U107).*

Over the entire range $p \in [19, 600)$, exactly **54.9% of all prime exponents** are asymptotically eliminated by Sahoo's Theorem for solutions with $\ell, m > 10^{60}$.

---

## 6. Computational Reproducibility

The complete computational audit can be re-run via:

```bash
python3 code/U111_cyclotomic_p500_p600.py
```

The execution takes ~1.0 second on Apple Silicon, verifying that:
- Every predicted splitting index matches PARI's `factormod(polsubcyclo(p, d), 2)` with 100% fidelity.
- Machine-readable JSON exported to [`research/checkpoints/U111_real_cyclotomic_audit_p500_p600.json`](file://[LOCAL_HOME]/Downloads/beal/research/checkpoints/U111_real_cyclotomic_audit_p500_p600.json).
