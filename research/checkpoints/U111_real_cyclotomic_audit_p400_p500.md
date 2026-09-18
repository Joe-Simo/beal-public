# Checkpoint U111: Real Cyclotomic Class Number and Sahoo Class $\mathcal{P}_1$ Audit for $400 < p < 500$

**Date**: 2026-09-17  
**Author**: Real Cyclotomic Class Number Auditor / Arithmetic Geometry Research Group  
**Target Equation**: $X^{2\ell} + Y^{2m} = Z^p$, prime exponents $\ell, m \ge 5$ (asymptotic bound $\ell, m > 10^{60}$), prime $p \in (400, 500)$  
**Branch**: All-even Beal candidate $A^{2r} + B^{2s} = C^{2t}$ with $17 \nmid t$  
**Supporting Code**: [`code/U111_cyclotomic_p400_p500.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_cyclotomic_p400_p500.py)  
**Machine-Readable Audit**: [`research/checkpoints/U111_real_cyclotomic_audit_p400_p500.json`](file://[LOCAL_HOME]/Downloads/beal/research/checkpoints/U111_real_cyclotomic_audit_p400_p500.json)  
**Primary References**:
- S. Sahoo, *Asymptotic solutions of generalized Fermat equations $x^{2l} + y^{2m} = z^p$*, preprint (2025).
- R. Schoof, *Class numbers of real cyclotomic fields of prime conductor*, Math. Comp. 72, no. 242 (2003), 913–937.
- J. C. Miller, *Real cyclotomic fields of prime conductor and their class numbers*, Math. Comp. 84, no. 295 (2015), 2459–2469; arXiv:1407.2373 (2014).
- On-Line Encyclopedia of Integer Sequences (OEIS), Sequences A230869 ($p$ with $h_p^+ > 1$) and A230870 ($h_p^+$ values).

---

## 1. Executive Summary

This checkpoint audits the arithmetic of real cyclotomic fields $K^+ = \mathbb{Q}(\zeta_p)^+ = \mathbb{Q}(2\cos(2\pi/p))$ and Sahoo's (2025) Class $\mathcal{P}_1$ asymptotic elimination for all 17 primes in $400 < p < 500$:
$$p \in \{401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499\}.$$

### Key Results

1. **Inertia of 2 in $K^+ = \mathbb{Q}(\zeta_p)^+$**:
   - Exactly **9 primes (52.9%)** have $2$ completely inert in $K^+$ ($g^+ = 1$, residue degree $f^+ = \frac{p-1}{2}$):
     $$\mathbf{P_{\text{inert}} \cap (400, 500) = \{419, 421, 443, 461, 463, 467, 479, 487, 491\}}.$$
   - Exactly **8 primes (47.1%)** fail inertia ($g^+ \ge 2$):
     $$\mathbf{P_{\text{split}} \cap (400, 500) = \{401, 409, 431, 433, 439, 449, 457, 499\}}.$$
     - Five primes fail due to quadratic splitting $p \equiv 1 \pmod 8$ ($\{401, 409, 433, 449, 457\}$), where $2$ splits in $\mathbb{Q}(\sqrt{p}) \subset K^+$.
     - Three primes fail due to small multiplicative order mod $p$ ($\{431, 439, 499\}$).

2. **Real Cyclotomic Class Numbers $h_p^+$ from Literature**:
   - From Schoof (2003, Main Table; OEIS A230869/A230870), exactly **3 primes** in $(400, 500)$ have non-trivial class number $h_p^+ > 1$:
     - **$p = 401$**: $h_{401}^+ = 45$ (term 9 of A230869/A230870);
     - **$p = 457$**: $h_{457}^+ = 5$ (term 10 of A230869/A230870);
     - **$p = 491$**: $h_{491}^+ = 8$ (term 11 of A230869/A230870).
   - All other 14 primes in $(400, 500)$ have $h_p^+ = 1$ (under GRH).

3. **The $p = 491$ Class Number Anomaly ($h_{491}^+ = 8$)**:
   - For $p = 491$, $\operatorname{ord}_{491}(2) = 490 = p - 1$, so **2 is completely inert** in $K^+$ ($f^+ = 245, g^+ = 1$).
   - However, $h_{491}^+ = 8 = 2^3$ is **even** ($2 \mid h_{491}^+$!).
   - Joining $p = 163$ ($h_{163}^+ = 4$) and $p = 349$ ($h_{349}^+ = 16$), $p = 491$ is the third prime with 2 inert and an even class number.
   - The non-trivial 2-torsion in the class group $\operatorname{Cl}(\mathcal{O}_{K^+})[2] \ne 0$ permits unramified quadratic extensions of $K^+$, **causing Sahoo's Kummer descent lemma to fail**.
   - Therefore, $p = 491$ **fails Class $\mathcal{P}_1$** despite 2 being completely inert.

4. **Class $\mathcal{P}_1$ Certification (under GRH)**:
   - Exactly **8 primes (47.1%)** satisfy both criteria ($2$ inert and $h_p^+ = 1$):
     $$\mathbf{\mathcal{P}_1 \cap (400, 500) = \{419, 421, 443, 461, 463, 467, 479, 487\}} \quad (8 / 17 = 47.1\%).$$
     For each such prime, Sahoo's (2025) Theorem eliminates all non-trivial primitive integer solutions to $X^{2\ell} + Y^{2m} = Z^p$ for exponents $\ell, m > 10^{60}$.

5. **Cumulative Progress across $19 \le p < 500$**:
   - Across all five audited intervals ($[19, 100)$, $(100, 200)$, $(200, 300)$, $(300, 400)$, and $(400, 500)$), comprising 88 primes:
     - Exactly **48 out of 88 primes (54.5%)** belong to Class $\mathcal{P}_1$.

---

## 2. Algebraic Decomposition of 2 in $\mathbb{Q}(\zeta_p)^+$ for $400 < p < 500$

### 2.1 Theoretical Invariants
Let $p \in (400, 500)$ be prime, and let $K^+ = \mathbb{Q}(\zeta_p)^+$ have degree $d = \frac{p-1}{2}$.
The Galois group is $G^+ = \operatorname{Gal}(K^+/\mathbb{Q}) \cong (\mathbb{Z}/p\mathbb{Z})^\times / \{\pm 1\}$.
Let $f = \operatorname{ord}_p(2)$ be the multiplicative order of 2 modulo $p$.
- Residue degree in $K^+$:
  $$f^+ = \begin{cases} f/2 & \text{if } f \text{ is even and } 2^{f/2} \equiv -1 \pmod p, \\ f & \text{otherwise.} \end{cases}$$
- Splitting index:
  $$g^+ = \frac{d}{f^+} = \frac{(p-1)/2}{f^+}.$$
- The prime 2 is **inert** in $K^+$ if and only if $g^+ = 1 \iff f^+ = d$.

### 2.2 Classification of Splitting in $(400, 500)$

#### 1. Quadratic Reciprocity Barrier ($p \equiv 1 \pmod 8$)
Five primes satisfy $p \equiv 1 \pmod 8$, where $(\frac{2}{p}) = 1$ forces 2 to split in $\mathbb{Q}(\sqrt{p}) \subset K^+$:
- **$p = 401$**: $d = 200$. $\operatorname{ord}_{401}(2) = 200 = (p-1)/2$. Because $2^{100} \equiv -1 \pmod{401}$, $f^+ = 100, g^+ = 2$. (Also has $h_{401}^+ = 45$).
- **$p = 409$**: $d = 204$. $\operatorname{ord}_{409}(2) = 204 = (p-1)/2$. Because $2^{102} \equiv -1 \pmod{409}$, $f^+ = 102, g^+ = 2$.
- **$p = 433$**: $d = 216$. $\operatorname{ord}_{433}(2) = 72$. $2^{36} \equiv -1 \pmod{433} \implies f^+ = 36, g^+ = 6$.
- **$p = 449$**: $d = 224$. $\operatorname{ord}_{449}(2) = 224 = (p-1)/2$. Because $2^{112} \equiv -1 \pmod{449}$, $f^+ = 112, g^+ = 2$.
- **$p = 457$**: $d = 228$. $\operatorname{ord}_{457}(2) = 76$. $2^{38} \equiv -1 \pmod{457} \implies f^+ = 38, g^+ = 6$. (Also has $h_{457}^+ = 5$).

#### 2. Small Order Cyclotomic Splitting ($p \not\equiv 1 \pmod 8$)
Three primes have $\operatorname{ord}_p(2) < \frac{p-1}{2}$:
- **$p = 431$**: $p \equiv 7 \pmod 8, d = 215$. $\operatorname{ord}_{431}(2) = 43$ (odd). $f^+ = 43, g^+ = 5$.
- **$p = 439$**: $p \equiv 7 \pmod 8, d = 219$. $\operatorname{ord}_{439}(2) = 73$ (odd). $f^+ = 73, g^+ = 3$. (Cubic decomposition field!).
- **$p = 499$**: $p \equiv 3 \pmod 8, d = 249$. $\operatorname{ord}_{499}(2) = 166$. $2^{83} \equiv -1 \pmod{499} \implies f^+ = 83, g^+ = 3$. (Cubic decomposition field!).

---

## 3. Real Cyclotomic Class Numbers $h_p^+$ in $400 < p < 500$

### 3.1 Known Literature Theorems
1. **Schoof (2003, Main Table; OEIS A230869 & A230870)**:
   Computed the orders of cyclotomic unit lattices $\tilde{h}_p^+$ for all primes $p < 10,000$.
   In the interval $(400, 500)$, the primes with non-trivial class numbers are:
   - **$p = 401$**: $h_{401}^+ = 45$ (term 9 of A230869, term 9 of A230870);
   - **$p = 457$**: $h_{457}^+ = 5$ (term 10 of A230869, term 10 of A230870);
   - **$p = 491$**: $h_{491}^+ = 8$ (term 11 of A230869, term 11 of A230870).
   All other 14 primes in $(400, 500)$ have $h_p^+ = 1$ under GRH.

### 3.2 Deep Analysis of the $p = 491$ Anomaly
- **Arithmetic Profile**:
  $$p = 491 \equiv 3 \pmod 8, \quad d = 245, \quad \operatorname{ord}_{491}(2) = 490 = p - 1.$$
  Since 2 is a primitive root mod 491, $2^{245} \equiv -1 \pmod{491}$, so $f^+ = 245$ and $g^+ = 1$.
  **The prime 2 is strictly inert in $\mathbb{Q}(\zeta_{491})^+$**.
- **Class Group and Parity**:
  $$h_{491}^+ = 8 = 2^3.$$
  Because $h_{491}^+$ is a power of 2, the 2-torsion subgroup $\operatorname{Cl}(\mathcal{O}_{K^+})[2]$ is non-trivial.
- **Diophantine Consequence for Sahoo's Theorem**:
  In Sahoo's proof (Propositions 1.9 & 1.10), establishing the upper bound $\max(|v(\lambda)|, |v(\mu)|) \le 4$ on solutions to the $S_{K, 2}$-unit equation relies on the assertion that an element $\mu \equiv 1 \pmod{\mathfrak{P}_2^5}$ cannot define an unramified quadratic extension $L = K^+(\sqrt{\mu})$.
  When $2 \mid h_p^+$, unramified quadratic extensions of $K^+$ exist by class field theory!
  Thus, $\mu$ does not need to be a global square, and the Kummer descent fails.
  **Conclusion**: $p = 491$ fails Class $\mathcal{P}_1$ despite having 2 inert.

---

## 4. Complete Deterministic Audit Table ($400 < p < 500$)

The following table reports the exact arithmetic invariants computed by [`code/U111_cyclotomic_p400_p500.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_cyclotomic_p400_p500.py).
Polynomial factorizations of $\operatorname{polsubcyclo}(p, d) \pmod 2$ were verified with PARI/GP 2.17.4:

| $p$ | $p \bmod 8$ | $d = \frac{p-1}{2}$ | $\operatorname{ord}_p(2)$ | $-1 \in \langle 2 \rangle$? | $f^+$ | $g^+$ | 2 Inert in $K^+$? | PARI Mod-2 Factors | $h_p^+$ | $h_p^+$ Status | Sahoo Class $\mathcal{P}_1$ Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 401 | 1 | 200 | 200 | YES | 100 | 2 | NO | $[100, 100]$ | **45** | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| 409 | 1 | 204 | 204 | YES | 102 | 2 | NO | $[102, 102]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| **419** | 3 | 209 | 418 | YES | 209 | 1 | **YES** | $[209]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **421** | 5 | 210 | 420 | YES | 210 | 1 | **YES** | $[210]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 431 | 7 | 215 | 43 | NO | 43 | 5 | NO | $[43 \times 5]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: Split-2 ($g^+=5$)** |
| 433 | 1 | 216 | 72 | YES | 36 | 6 | NO | $[36 \times 6]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| 439 | 7 | 219 | 73 | NO | 73 | 3 | NO | $[73, 73, 73]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: Split-2 ($g^+=3$)** |
| **443** | 3 | 221 | 442 | YES | 221 | 1 | **YES** | $[221]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 449 | 1 | 224 | 224 | YES | 112 | 2 | NO | $[112, 112]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| 457 | 1 | 228 | 76 | YES | 38 | 6 | NO | $[38 \times 6]$ | **5** | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| **461** | 5 | 230 | 460 | YES | 230 | 1 | **YES** | $[230]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **463** | 7 | 231 | 231 | NO | 231 | 1 | **YES** | $[231]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **467** | 3 | 233 | 466 | YES | 233 | 1 | **YES** | $[233]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **479** | 7 | 239 | 239 | NO | 239 | 1 | **YES** | $[239]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **487** | 7 | 243 | 243 | NO | 243 | 1 | **YES** | $[243]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 491 | 3 | 245 | 490 | YES | 245 | 1 | **YES** | $[245]$ | **8** | Under GRH | **Non-$\mathcal{P}_1$: Even $h^+$ ($2 \mid h_{491}^+$)** |
| 499 | 3 | 249 | 166 | YES | 83 | 3 | NO | $[83, 83, 83]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: Split-2 ($g^+=3$)** |

---

## 5. Synthesis: Cumulative Class $\mathcal{P}_1$ Inventory for $19 \le p < 500$

| Interval | Total Primes | 2 Inert in $K^+$ ($g^+=1$) | $h_p^+ = 1$ | Class $\mathcal{P}_1$ Primes ($2$ inert $\land h^+=1$) | $\mathcal{P}_1$ Percentage |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$[19, 100)$ (U103/U107)** | 18 | 12 | 18 | **12** | 66.7% |
| **$(100, 200)$ (U110)** | 21 | 14 | 19 | **12** | 57.1% |
| **$(200, 300)$ (U111)** | 16 | 7 | 13 | **7** | 43.8% |
| **$(300, 400)$ (U111)** | 16 | 10 | 13 | **9** | 56.2% |
| **$(400, 500)$ (U111)** | 17 | 9 | 14 | **8** | 47.1% |
| **Total $[19, 500)$** | **88** | **52 (59.1%)** | **77 (87.5%)** | **48 (54.5%)** | **54.5%** |

### Complete Inventory of the 48 Class $\mathcal{P}_1$ Exponents in $[19, 500)$:
$$\begin{aligned}
\mathbf{\mathcal{P}_1 \cap [19, 500) = \{ } & 19, 23, 29^*, 37, 47, 53, 59, 61, 67, 71, 79, 83, \\
& 101, 103, 107, 131, 139, 149, 167, 173, 179, 181, 197, 199, \\
& 211, 227, 239, 263, 269, 271, 293, \\
& 311, 317, 347, 359, 367, 373, 379, 383, 389, \\
& 419, 421, 443, 461, 463, 467, 479, 487 \mathbf{ \} }.
\end{aligned}$$
*(Note: $p = 29$ has wide class number $h=1$ and narrow class number $h^+=8$, as analyzed in U107).*

Over the entire range $p \in [19, 500)$, exactly **54.5% of all prime exponents** are asymptotically eliminated by Sahoo's Theorem for solutions with $\ell, m > 10^{60}$.

---

## 6. Computational Reproducibility

The complete computational audit can be re-run via:

```bash
python3 code/U111_cyclotomic_p400_p500.py
```

The execution takes ~1.0 second on Apple Silicon, verifying that:
- Every predicted splitting index matches PARI's `factormod(polsubcyclo(p, d), 2)` with 100% fidelity.
- Machine-readable JSON exported to [`research/checkpoints/U111_real_cyclotomic_audit_p400_p500.json`](file://[LOCAL_HOME]/Downloads/beal/research/checkpoints/U111_real_cyclotomic_audit_p400_p500.json).
