# Checkpoint U111: Real Cyclotomic Class Number and Sahoo Class $\mathcal{P}_1$ Audit for $300 < p < 400$

**Date**: 2026-09-17  
**Author**: Real Cyclotomic Class Number Auditor / Arithmetic Geometry Research Group  
**Target Equation**: $X^{2\ell} + Y^{2m} = Z^p$, prime exponents $\ell, m \ge 5$ (asymptotic bound $\ell, m > 10^{60}$), prime $p \in (300, 400)$  
**Branch**: All-even Beal candidate $A^{2r} + B^{2s} = C^{2t}$ with $17 \nmid t$  
**Supporting Code**: [`code/U111_cyclotomic_p300_p400.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_cyclotomic_p300_p400.py)  
**Machine-Readable Audit**: [`research/checkpoints/U111_real_cyclotomic_audit_p300_p400.json`](file://[LOCAL_HOME]/Downloads/beal/research/checkpoints/U111_real_cyclotomic_audit_p300_p400.json)  
**Primary References**:
- S. Sahoo, *Asymptotic solutions of generalized Fermat equations $x^{2l} + y^{2m} = z^p$*, preprint (2025).
- R. Schoof, *Minus class groups of the fields of the $l$-th roots of unity*, Math. Comp. 67 (1998), 1225–1245.
- R. Schoof, *Class numbers of real cyclotomic fields of prime conductor*, Math. Comp. 72, no. 242 (2003), 913–937.
- J. C. Miller, *Real cyclotomic fields of prime conductor and their class numbers*, Math. Comp. 84, no. 295 (2015), 2459–2469; arXiv:1407.2373 (2014).
- On-Line Encyclopedia of Integer Sequences (OEIS), Sequences A230869 ($p$ with $h_p^+ > 1$) and A230870 ($h_p^+$ values).

---

## 1. Executive Summary

This checkpoint audits the arithmetic of real cyclotomic fields $K^+ = \mathbb{Q}(\zeta_p)^+ = \mathbb{Q}(2\cos(2\pi/p))$ and Sahoo's (2025) Class $\mathcal{P}_1$ asymptotic elimination for all 16 primes in $300 < p < 400$:
$$p \in \{307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397\}.$$

### Key Results

1. **Inertia of 2 in $K^+ = \mathbb{Q}(\zeta_p)^+$**:
   - Exactly **10 primes (62.5%)** have $2$ completely inert in $K^+$ ($g^+ = 1$, residue degree $f^+ = \frac{p-1}{2}$):
     $$\mathbf{P_{\text{inert}} \cap (300, 400) = \{311, 317, 347, 349, 359, 367, 373, 379, 383, 389\}}.$$
   - Exactly **6 primes (37.5%)** fail inertia ($g^+ \ge 2$):
     $$\mathbf{P_{\text{split}} \cap (300, 400) = \{307, 313, 331, 337, 353, 397\}}.$$
     - Three primes fail due to quadratic splitting $p \equiv 1 \pmod 8$ ($\{313, 337, 353\}$), where $2$ splits in $\mathbb{Q}(\sqrt{p}) \subset K^+$.
     - Three primes fail due to small multiplicative order mod $p$ ($\{307, 331, 397\}$).

2. **Real Cyclotomic Class Numbers $h_p^+$ from Literature**:
   - From Schoof (2003, Main Table; OEIS A230869/A230870), exactly **3 primes** in $(300, 400)$ have non-trivial class number $h_p^+ > 1$:
     - **$p = 313$**: $h_{313}^+ = 7$ (term 6 of A230869/A230870);
     - **$p = 349$**: $h_{349}^+ = 16$ (term 7 of A230869/A230870);
     - **$p = 397$**: $h_{397}^+ = 4$ (term 8 of A230869/A230870).
   - All other 13 primes in $(300, 400)$ have $h_p^+ = 1$ (under GRH).

3. **The $p = 349$ Class Number Anomaly ($h_{349}^+ = 16$)**:
   - For $p = 349$, $\operatorname{ord}_{349}(2) = 348 = p - 1$, so **2 is completely inert** in $K^+$ ($f^+ = 174, g^+ = 1$).
   - However, $h_{349}^+ = 16 = 2^4$ is **even** ($2 \mid h_{349}^+$!).
   - Just like $p = 163$ ($h_{163}^+ = 4$), the non-trivial 2-torsion in the class group $\operatorname{Cl}(\mathcal{O}_{K^+})[2] \ne 0$ permits unramified quadratic extensions of $K^+$, **causing Sahoo's Kummer descent lemma to fail**.
   - Therefore, $p = 349$ **fails Class $\mathcal{P}_1$** despite 2 being completely inert.

4. **Class $\mathcal{P}_1$ Certification (under GRH)**:
   - Exactly **9 primes (56.2%)** satisfy both criteria ($2$ inert and $h_p^+ = 1$):
     $$\mathbf{\mathcal{P}_1 \cap (300, 400) = \{311, 317, 347, 359, 367, 373, 379, 383, 389\}} \quad (9 / 16 = 56.2\%).$$
     For each such prime, Sahoo's (2025) Theorem eliminates all non-trivial primitive integer solutions to $X^{2\ell} + Y^{2m} = Z^p$ for exponents $\ell, m > 10^{60}$.

5. **Cumulative Progress across $19 \le p < 400$**:
   - Across all four audited intervals ($[19, 100)$, $(100, 200)$, $(200, 300)$, and $(300, 400)$), comprising 71 primes:
     - Exactly **40 out of 71 primes (56.3%)** belong to Class $\mathcal{P}_1$.

---

## 2. Algebraic Decomposition of 2 in $\mathbb{Q}(\zeta_p)^+$ for $300 < p < 400$

### 2.1 Theoretical Invariants
Let $p \in (300, 400)$ be prime, and let $K^+ = \mathbb{Q}(\zeta_p)^+$ have degree $d = \frac{p-1}{2}$.
The Galois group is $G^+ = \operatorname{Gal}(K^+/\mathbb{Q}) \cong (\mathbb{Z}/p\mathbb{Z})^\times / \{\pm 1\}$.
Let $f = \operatorname{ord}_p(2)$ be the multiplicative order of 2 modulo $p$.
- Residue degree in $K^+$:
  $$f^+ = \begin{cases} f/2 & \text{if } f \text{ is even and } 2^{f/2} \equiv -1 \pmod p, \\ f & \text{otherwise.} \end{cases}$$
- Splitting index:
  $$g^+ = \frac{d}{f^+} = \frac{(p-1)/2}{f^+}.$$
- The prime 2 is **inert** in $K^+$ if and only if $g^+ = 1 \iff f^+ = d$.

### 2.2 Classification of Splitting in $(300, 400)$

#### 1. Quadratic Reciprocity Barrier ($p \equiv 1 \pmod 8$)
Three primes satisfy $p \equiv 1 \pmod 8$, where $(\frac{2}{p}) = 1$ forces 2 to split in $\mathbb{Q}(\sqrt{p}) \subset K^+$:
- **$p = 313$**: $d = 156$. $\operatorname{ord}_{313}(2) = 156 = (p-1)/2$. Because $2^{78} \equiv -1 \pmod{313}$, $f^+ = 78, g^+ = 2$. (Also has $h_{313}^+ = 7$).
- **$p = 337$**: $d = 168$. $\operatorname{ord}_{337}(2) = 21$ (odd). $f^+ = 21, g^+ = 168 / 21 = 8$.
- **$p = 353$**: $d = 176$. $\operatorname{ord}_{353}(2) = 88$. $2^{44} \equiv -1 \pmod{353} \implies f^+ = 44, g^+ = 176 / 44 = 4$.

#### 2. Small Order Cyclotomic Splitting ($p \not\equiv 1 \pmod 8$)
Three primes have $\operatorname{ord}_p(2) < \frac{p-1}{2}$:
- **$p = 307$**: $p \equiv 3 \pmod 8, d = 153$. $\operatorname{ord}_{307}(2) = 102$. $2^{51} \equiv -1 \pmod{307} \implies f^+ = 51, g^+ = 3$. (Cubic decomposition field!).
- **$p = 331$**: $p \equiv 3 \pmod 8, d = 165$. $\operatorname{ord}_{331}(2) = 30$. $2^{15} \equiv -1 \pmod{331} \implies f^+ = 15, g^+ = 11$.
- **$p = 397$**: $p \equiv 5 \pmod 8, d = 198$. $\operatorname{ord}_{397}(2) = 44$. $2^{22} \equiv -1 \pmod{397} \implies f^+ = 22, g^+ = 9$. (Also has $h_{397}^+ = 4$).

---

## 3. Real Cyclotomic Class Numbers $h_p^+$ in $300 < p < 400$

### 3.1 Known Literature Theorems
1. **Schoof (2003, Main Table; OEIS A230869 & A230870)**:
   Computed the orders of cyclotomic unit lattices $\tilde{h}_p^+$ for all primes $p < 10,000$.
   In the interval $(300, 400)$, the primes with non-trivial class numbers are:
   - **$p = 313$**: $h_{313}^+ = 7$ (term 6 of A230869, term 6 of A230870);
   - **$p = 349$**: $h_{349}^+ = 16$ (term 7 of A230869, term 7 of A230870);
   - **$p = 397$**: $h_{397}^+ = 4$ (term 8 of A230869, term 8 of A230870).
   All other 13 primes in $(300, 400)$ have $h_p^+ = 1$ under GRH.

### 3.2 Deep Analysis of the $p = 349$ Anomaly
- **Arithmetic Profile**:
  $$p = 349 \equiv 5 \pmod 8, \quad d = 174, \quad \operatorname{ord}_{349}(2) = 348 = p - 1.$$
  Since 2 is a primitive root mod 349, $2^{174} \equiv -1 \pmod{349}$, so $f^+ = 174$ and $g^+ = 1$.
  **The prime 2 is strictly inert in $\mathbb{Q}(\zeta_{349})^+$**.
- **Class Group and Parity**:
  $$h_{349}^+ = 16 = 2^4.$$
  Because $h_{349}^+$ is a multiple of 2, the 2-torsion subgroup $\operatorname{Cl}(\mathcal{O}_{K^+})[2]$ is non-trivial.
- **Diophantine Consequence for Sahoo's Theorem**:
  In Sahoo's proof (Propositions 1.9 & 1.10), establishing the upper bound $\max(|v(\lambda)|, |v(\mu)|) \le 4$ on solutions to the $S_{K, 2}$-unit equation relies on the assertion that an element $\mu \equiv 1 \pmod{\mathfrak{P}_2^5}$ cannot define an unramified quadratic extension $L = K^+(\sqrt{\mu})$.
  When $2 \mid h_p^+$, unramified quadratic extensions of $K^+$ exist by class field theory!
  Thus, $\mu$ does not need to be a global square, and the Kummer descent fails.
  **Conclusion**: $p = 349$ fails Class $\mathcal{P}_1$ despite having 2 inert.

---

## 4. Complete Deterministic Audit Table ($300 < p < 400$)

The following table reports the exact arithmetic invariants computed by [`code/U111_cyclotomic_p300_p400.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_cyclotomic_p300_p400.py).
Polynomial factorizations of $\operatorname{polsubcyclo}(p, d) \pmod 2$ were verified with PARI/GP 2.17.4:

| $p$ | $p \bmod 8$ | $d = \frac{p-1}{2}$ | $\operatorname{ord}_p(2)$ | $-1 \in \langle 2 \rangle$? | $f^+$ | $g^+$ | 2 Inert in $K^+$? | PARI Mod-2 Factors | $h_p^+$ | $h_p^+$ Status | Sahoo Class $\mathcal{P}_1$ Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 307 | 3 | 153 | 102 | YES | 51 | 3 | NO | $[51, 51, 51]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: Split-2 ($g^+=3$)** |
| **311** | 7 | 155 | 155 | NO | 155 | 1 | **YES** | $[155]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 313 | 1 | 156 | 156 | YES | 78 | 2 | NO | $[78, 78]$ | **7** | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| **317** | 5 | 158 | 316 | YES | 158 | 1 | **YES** | $[158]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 331 | 3 | 165 | 30 | YES | 15 | 11 | NO | $[15 \times 11]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: Split-2 ($g^+=11$)** |
| 337 | 1 | 168 | 21 | NO | 21 | 8 | NO | $[21 \times 8]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| **347** | 3 | 173 | 346 | YES | 173 | 1 | **YES** | $[173]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 349 | 5 | 174 | 348 | YES | 174 | 1 | **YES** | $[174]$ | **16** | Under GRH | **Non-$\mathcal{P}_1$: Even $h^+$ ($2 \mid h_{349}^+$)** |
| 353 | 1 | 176 | 88 | YES | 44 | 4 | NO | $[44 \times 4]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| **359** | 7 | 179 | 179 | NO | 179 | 1 | **YES** | $[179]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **367** | 7 | 183 | 183 | NO | 183 | 1 | **YES** | $[183]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **373** | 5 | 186 | 372 | YES | 186 | 1 | **YES** | $[186]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **379** | 3 | 189 | 378 | YES | 189 | 1 | **YES** | $[189]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **383** | 7 | 191 | 191 | NO | 191 | 1 | **YES** | $[191]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **389** | 5 | 194 | 388 | YES | 194 | 1 | **YES** | $[194]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 397 | 5 | 198 | 44 | YES | 22 | 9 | NO | $[22 \times 9]$ | **4** | Under GRH | **Non-$\mathcal{P}_1$: Split-2 ($g^+=9$)** |

---

## 5. Synthesis: Cumulative Class $\mathcal{P}_1$ Inventory for $19 \le p < 400$

| Interval | Total Primes | 2 Inert in $K^+$ ($g^+=1$) | $h_p^+ = 1$ | Class $\mathcal{P}_1$ Primes ($2$ inert $\land h^+=1$) | $\mathcal{P}_1$ Percentage |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$[19, 100)$ (U103/U107)** | 18 | 12 | 18 | **12** | 66.7% |
| **$(100, 200)$ (U110)** | 21 | 14 | 19 | **12** | 57.1% |
| **$(200, 300)$ (U111)** | 16 | 7 | 13 | **7** | 43.8% |
| **$(300, 400)$ (U111)** | 16 | 10 | 13 | **9** | 56.2% |
| **Total $[19, 400)$** | **71** | **43 (60.6%)** | **63 (88.7%)** | **40 (56.3%)** | **56.3%** |

### Complete Inventory of the 40 Class $\mathcal{P}_1$ Exponents in $[19, 400)$:
$$\begin{aligned}
\mathbf{\mathcal{P}_1 \cap [19, 400) = \{ } & 19, 23, 29^*, 37, 47, 53, 59, 61, 67, 71, 79, 83, \\
& 101, 103, 107, 131, 139, 149, 167, 173, 179, 181, 197, 199, \\
& 211, 227, 239, 263, 269, 271, 293, \\
& 311, 317, 347, 359, 367, 373, 379, 383, 389 \mathbf{ \} }.
\end{aligned}$$
*(Note: $p = 29$ has wide class number $h=1$ and narrow class number $h^+=8$, as analyzed in U107).*

Over the entire range $p \in [19, 400)$, exactly **56.3% of all prime exponents** are asymptotically eliminated by Sahoo's Theorem for solutions with $\ell, m > 10^{60}$.

---

## 6. Computational Reproducibility

The complete computational audit can be re-run via:

```bash
python3 code/U111_cyclotomic_p300_p400.py
```

The execution takes ~1.0 second on Apple Silicon, confirming:
- Every predicted splitting index matches PARI's `factormod(polsubcyclo(p, d), 2)` with 100% agreement.
- Machine-readable JSON exported to [`research/checkpoints/U111_real_cyclotomic_audit_p300_p400.json`](file://[LOCAL_HOME]/Downloads/beal/research/checkpoints/U111_real_cyclotomic_audit_p300_p400.json).
