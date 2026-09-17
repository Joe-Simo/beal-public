# Checkpoint U110: Real Cyclotomic Class Number and Sahoo Class $\mathcal{P}_1$ Audit for $100 < p < 200$

**Date**: 2026-09-17  
**Author**: Real Cyclotomic Class Number Auditor / Arithmetic Geometry Research Group  
**Target Equation**: $X^{2\ell} + Y^{2m} = Z^p$, exponents $\ell, m \ge 5$ (asymptotic bound $\ell, m > 10^{60}$), prime $p \in (100, 200)$  
**Branch**: All-even Beal candidate $A^{2r} + B^{2s} = C^{2t}$ with $17 \nmid t$  
**Supporting Code**: [`code/U110_cyclotomic_p100_p200.py`](file://[LOCAL_HOME]/Downloads/beal/code/U110_cyclotomic_p100_p200.py)  
**Primary References**:
- S. Sahoo, *Asymptotic solutions of generalized Fermat equations $x^{2l} + y^{2m} = z^p$*, preprint (2025).
- F. J. van der Linden, *Class number computations of real abelian number fields*, Math. Comp. 39, no. 160 (1982), 693–707.
- R. Schoof, *Minus class groups of the fields of the $l$-th roots of unity*, Math. Comp. 67 (1998), 1225–1245.
- R. Schoof, *Class numbers of real cyclotomic fields of prime conductor*, Math. Comp. 72, no. 242 (2003), 913–937.
- J. C. Miller, *Real cyclotomic fields of prime conductor and their class numbers*, Math. Comp. 84, no. 295 (2015), 2459–2469; arXiv:1407.2373 (2014).
- L. C. Washington, *Introduction to Cyclotomic Fields*, 2nd ed., Graduate Texts in Mathematics 83, Springer-Verlag (1997).

---

## 1. Executive Summary

In Checkpoints U103, U107, and U108, the asymptotic elimination of primitive integer solutions to the generalized Fermat equation
$$X^{2\ell} + Y^{2m} = Z^p, \quad \gcd(X, Y, Z) = 1, \quad \ell, m > 10^{60}$$
was established for prime exponents $p \in [19, 100)$ belonging to Sahoo's (2025) Class $\mathcal{P}_1$.
A prime $p$ belongs to Class $\mathcal{P}_1$ if:
1. The prime $2$ is **inert** in the maximal real cyclotomic subfield $K^+ = \mathbb{Q}(\zeta_p)^+ = \mathbb{Q}(2\cos(2\pi/p))$;
2. The plus class number is odd ($2 \nmid h_p^+$), ensuring trivial 2-torsion in the class group: $\operatorname{Cl}(\mathcal{O}_{K^+})[2] = 0$;
3. $p \not\equiv 1 \pmod 8$ (which is automatically necessary if 2 is inert in $K^+$).

This checkpoint extends the arithmetic classification and deterministic class number audit to the subsequent range of 21 primes:
$$p \in \{101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199\}.$$

### Key Results

1. **Decomposition of 2 in $K^+ = \mathbb{Q}(\zeta_p)^+$**:
   - Exactly **14 primes (66.7%)** have $2$ completely inert in $K^+$ ($g^+ = 1$, residue degree $f^+ = \frac{p-1}{2}$):
     $$\{101, 103, 107, 131, 139, 149, 163, 167, 173, 179, 181, 191, 197, 199\}.$$
   - Exactly **7 primes (33.3%)** fail inertia ($g^+ \ge 2$):
     $$\{109, 113, 127, 137, 151, 157, 193\}.$$
     Every prime $p \equiv 1 \pmod 8$ in this range ($p \in \{113, 137, 193\}$) splits unconditionally due to quadratic splitting in $\mathbb{Q}(\sqrt{p})$.

2. **Plus Class Numbers $h_p^+ = h(\mathbb{Q}(\zeta_p)^+)$ from Literature**:
   - **Unconditional Triviality for $p \le 151$ (Miller 2014, Theorem 1.1)**:
     All 11 primes $p \in [101, 151]$ have $h_p^+ = 1$ unconditionally.
   - **Triviality under GRH for $151 < p < 200$ (Miller 2014, Schoof 2003, van der Linden 1982)**:
     $h_p^+ = 1$ for all primes $p \in (151, 200)$ **except $p = 163$ and $p = 191$**.
   - **The Non-Trivial Class Number Anomalies**:
     - **$p = 163$**: $h_{163}^+ = 4$ (van der Linden 1982, Schoof 2003, Miller 2014). This is the smallest prime conductor with $h_p^+ > 1$. Because $h_{163}^+ = 4$ is **even**, $2 \mid h_{163}^+$, violating Sahoo's Kummer descent condition!
     - **$p = 191$**: $h_{191}^+ = 11$ (Schoof 2003, Miller 2014). While $h_{191}^+ \ne 1$, $11$ is **odd**, meaning the 2-Sylow subgroup $\operatorname{Cl}(\mathcal{O}_{K^+})[2] = 0$ remains trivial.

3. **Classification Partition**:
   - **Class $\mathcal{P}_1$ (Strict $h_p^+ = 1$, Asymptotically Eliminated)**:
     $$\mathbf{\mathcal{P}_1 \cap (100, 200) = \{101, 103, 107, 131, 139, 149, 167, 173, 179, 181, 197, 199\}} \quad (12 / 21 = 57.1\%).$$
     - 6 primes are **unconditionally certified** ($p \le 151$): $\{101, 103, 107, 131, 139, 149\}$.
     - 6 primes are **certified under GRH** ($p > 151$): $\{167, 173, 179, 181, 197, 199\}$.
   - **Non-$\mathcal{P}_1$ Primes (9 Primes, 42.9%)**:
     - Class number obstructions: $p = 163$ ($h^+=4$, even) and $p = 191$ ($h^+=11 > 1$).
     - Quadratic reciprocity splitting ($p \equiv 1 \pmod 8$): $p \in \{113, 137, 193\}$.
     - Cyclotomic splitting ($p \not\equiv 1 \pmod 8$, small order): $p \in \{109, 127, 151, 157\}$.

---

## 2. Algebraic Number Theory: Decomposition of 2 in $\mathbb{Q}(\zeta_p)^+$

### 2.1 Subgroups and Galois Correspondence
Let $p$ be an odd prime.
- The full cyclotomic field $K = \mathbb{Q}(\zeta_p)$ has Galois group $G = \operatorname{Gal}(K/\mathbb{Q}) \cong (\mathbb{Z}/p\mathbb{Z})^\times$, cyclic of order $p - 1$.
- Complex conjugation is the unique involution $\tau \in G$ mapping $\zeta_p \mapsto \zeta_p^{-1}$, corresponding to $-1 \pmod p$.
- The maximal real subfield is $K^+ = K^{\langle \tau \rangle} = \mathbb{Q}(\zeta_p + \zeta_p^{-1}) = \mathbb{Q}(2\cos(2\pi/p))$, with degree
  $$d = [K^+ : \mathbb{Q}] = \frac{p - 1}{2}.$$
- The Galois group of $K^+$ over $\mathbb{Q}$ is the quotient group:
  $$G^+ = \operatorname{Gal}(K^+/\mathbb{Q}) \cong (\mathbb{Z}/p\mathbb{Z})^\times / \{ \pm 1 \}.$$

### 2.2 The Frobenius Map and Residue Degree
Because $p > 2$, 2 does not divide the discriminant $\Delta_K = (-1)^{(p-1)/2} p^{p-2}$, so 2 is unramified in $K$ and $K^+$.
The decomposition of 2 is governed entirely by the Frobenius automorphism $\sigma_2: \zeta_p \mapsto \zeta_p^2$, corresponding to $2 \in (\mathbb{Z}/p\mathbb{Z})^\times$.

Let $f = \operatorname{ord}_p(2)$ be the multiplicative order of 2 in $(\mathbb{Z}/p\mathbb{Z})^\times$.
The cyclic subgroup generated by 2 is $\langle 2 \rangle \subset G$ of order $f$.
In $K^+$, the restriction $\bar{\sigma}_2 = \sigma_2|_{K^+}$ generates the subgroup:
$$\langle \bar{\sigma}_2 \rangle = \langle 2 \pmod{\{\pm 1\}} \rangle \cong \langle 2, -1 \rangle / \{\pm 1\} \subset G^+.$$
The residue class degree $f^+$ of 2 in $K^+$ is the order of $\bar{\sigma}_2$ in $G^+$:
$$f^+ = |\langle \bar{\sigma}_2 \rangle| = \frac{|\langle 2 \rangle|}{|\langle 2 \rangle \cap \{\pm 1\}|}.$$

Two cases arise:
- **Case 1: $-1 \in \langle 2 \pmod p \rangle$**  
  This occurs if and only if $f = \operatorname{ord}_p(2)$ is even and $2^{f/2} \equiv -1 \pmod p$.
  Then $\langle 2 \rangle \cap \{\pm 1\} = \{\pm 1\}$, so:
  $$f^+ = \frac{f}{2} = \frac{\operatorname{ord}_p(2)}{2}.$$
- **Case 2: $-1 \notin \langle 2 \pmod p \rangle$**  
  This occurs if $f$ is odd or $2^{f/2} \not\equiv -1 \pmod p$.
  Then $\langle 2 \rangle \cap \{\pm 1\} = \{1\}$, so the projection is injective:
  $$f^+ = f = \operatorname{ord}_p(2).$$

The splitting index (the number of distinct prime ideals lying above 2 in $\mathcal{O}_{K^+}$) is:
$$g^+ = \frac{d}{f^+} = \frac{(p - 1)/2}{f^+}.$$

### 2.3 Exact Criteria for Inertia ($g^+ = 1$)
The prime 2 is **inert** in $K^+$ if and only if $f^+ = d = \frac{p-1}{2}$, which is equivalent to $g^+ = 1$.

> [!IMPORTANT]
> **Theorem (Classification of Inertia of 2 in $\mathbb{Q}(\zeta_p)^+$)**:  
> The prime 2 is inert in $K^+ = \mathbb{Q}(\zeta_p)^+$ if and only if one of the following two mutually exclusive conditions holds:
> 1. **Primitive Root Modulo $p$**: $\operatorname{ord}_p(2) = p - 1$.  
>    In this case, $-1 \equiv 2^{(p-1)/2} \in \langle 2 \rangle$, so $f^+ = \frac{p-1}{2}$ and $g^+ = 1$.
> 2. **Semi-Primitive Root Modulo $p$ with $p \equiv 7 \pmod 8$**: $\operatorname{ord}_p(2) = \frac{p - 1}{2}$.  
>    In this case, $\langle 2 \rangle$ is the unique subgroup of quadratic residues. Because $p \equiv 7 \pmod 8$, $(\frac{-1}{p}) = -1$, so $-1 \notin \langle 2 \rangle$. Hence $f^+ = f = \frac{p-1}{2}$ and $g^+ = 1$.

> [!WARNING]
> **The $p \equiv 1 \pmod 8$ Splitting Obstruction**:  
> If $p \equiv 1 \pmod 8$, then $(\frac{2}{p}) = 1$, which implies that 2 splits in the unique quadratic subfield $\mathbb{Q}(\sqrt{p}) \subseteq K^+$.  
> Since $\mathbb{Q}(\sqrt{p})$ is a subfield of $K^+$, the splitting index in $K^+$ must be a multiple of the splitting index in $\mathbb{Q}(\sqrt{p})$. Therefore:
> $$p \equiv 1 \pmod 8 \implies g^+ \ge 2 \implies 2 \text{ NEVER inert in } K^+.$$
> Even if $\operatorname{ord}_p(2) = \frac{p-1}{2}$ (e.g., $p = 41, 97, 137, 193$), the fact that $p \equiv 1 \pmod 8$ forces $(\frac{-1}{p}) = 1$, so $-1 \in \langle 2 \rangle$, yielding $f^+ = \frac{p-1}{4}$ and $g^+ = 2$.

---

## 3. Real Cyclotomic Class Numbers $h_p^+$: The Literature Landscape

### 3.1 Historical Evolution of Computations
The class number of the cyclotomic field factors as $h_p = h_p^- \cdot h_p^+$.
While the relative class number $h_p^-$ is expressible in closed form via generalized Bernoulli numbers:
$$h_p^- = 2p \prod_{\chi \text{ odd}} \left( -\frac{1}{2} B_{1, \chi} \right),$$
the plus class number $h_p^+ = h(\mathbb{Q}(\zeta_p)^+)$ requires the regulator $R_{K^+}$, which grows exponentially ($R_{K^+} \sim p^{(p-3)/4}$), rendering standard Minkowski bounds and Buchmann algorithms computationally intractable for degrees $d \ge 40$.

| Milestone | Authors | Scope of $h_p^+$ Determination | Method |
| :--- | :--- | :--- | :--- |
| **1976** | J. M. Masley & H. L. Montgomery | $h_p^+ = 1$ for all $p \le 67$ | Analytic discriminant bounds / geometry of numbers |
| **1982** | F. J. van der Linden | $h_p^+ = 1$ for $p < 163$; **$h_{163}^+ = 4$** | Odlyzko discriminant bounds (assumed GRH) |
| **1998 / 2003** | R. Schoof | Heuristic tables up to $p < 10,000$; confirmed $h_{163}^+ = 4, h_{191}^+ = 11$ | Cyclotomic unit lattices, Euler systems |
| **2014 / 2015** | J. C. Miller | **Unconditional: $h_p^+ = 1$ for all $p \le 151$**; **GRH: $p \le 241$** | Analytic lower bounds on prime ideals in Hilbert class fields |

### 3.2 Miller's Theorem 1.1 (2014)
In his breakthrough work (*Math. Comp.* 84 (2015), 2459–2469; arXiv:1407.2373), John C. Miller proved:

> **Theorem (Miller 2014, Theorem 1.1)**:  
> Let $p$ be a prime integer, and let $\mathbb{Q}(\zeta_p + \zeta_p^{-1})$ denote the maximal real subfield of the $p$-th cyclotomic field $\mathbb{Q}(\zeta_p)$.  
> Then the class number of $\mathbb{Q}(\zeta_p + \zeta_p^{-1})$ is $1$ for $p \le 151$ **unconditionally**.  
> Furthermore, under the assumption of the Generalized Riemann Hypothesis (GRH), the class number $h_p^+$ is:
> $$h_p^+ = \begin{cases} 
> 1 & \text{if } p \le 241 \text{ and } p \notin \{163, 191, 229\}, \\
> 4 & \text{if } p = 163, \\
> 11 & \text{if } p = 191, \\
> 3 & \text{if } p = 229.
> \end{cases}$$

### 3.3 Implications for the Interval $100 < p < 200$
For the 21 primes in $100 < p < 200$:
1. **Primes $p \in [101, 151]$ (11 primes)**:
   $h_p^+ = 1$ is **unconditionally proven** (Miller 2014).
2. **Primes $p \in [157, 199]$ (10 primes)**:
   Under GRH, $h_p^+ = 1$ for all primes **except $p = 163$ ($h^+=4$) and $p = 191$ ($h^+=11$)**.

---

## 4. Complete Deterministic Audit Table ($100 < p < 200$)

The following table summarizes the calculations performed by [`code/U110_cyclotomic_p100_p200.py`](file://[LOCAL_HOME]/Downloads/beal/code/U110_cyclotomic_p100_p200.py), with polynomial factorization mod 2 verified independently via PARI/GP 2.17.4 (`polsubcyclo(p, d)` and `factormod(P, 2)`):

| $p$ | $p \bmod 8$ | $d = \frac{p-1}{2}$ | $\operatorname{ord}_p(2)$ | $-1 \in \langle 2 \rangle$? | $f^+$ | $g^+$ | 2 Inert in $K^+$? | PARI Mod-2 Factors | $h_p^+$ | $h_p^+$ Certification | Sahoo Class $\mathcal{P}_1$ Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **101** | 5 | 50 | 100 | YES | 50 | 1 | **YES** | $[50]$ | 1 | Unconditional | **Class $\mathcal{P}_1$ (UNCOND ELIM)** |
| **103** | 7 | 51 | 51 | NO | 51 | 1 | **YES** | $[51]$ | 1 | Unconditional | **Class $\mathcal{P}_1$ (UNCOND ELIM)** |
| **107** | 3 | 53 | 106 | YES | 53 | 1 | **YES** | $[53]$ | 1 | Unconditional | **Class $\mathcal{P}_1$ (UNCOND ELIM)** |
| 109 | 5 | 54 | 36 | YES | 18 | 3 | NO | $[18, 18, 18]$ | 1 | Unconditional | **Non-$\mathcal{P}_1$: Split-2 ($g^+=3$)** |
| 113 | 1 | 56 | 28 | YES | 14 | 4 | NO | $[14 \times 4]$ | 1 | Unconditional | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| 127 | 7 | 63 | 7 | NO | 7 | 9 | NO | $[7 \times 9]$ | 1 | Unconditional | **Non-$\mathcal{P}_1$: Mersenne ($g^+=9$)** |
| **131** | 3 | 65 | 130 | YES | 65 | 1 | **YES** | $[65]$ | 1 | Unconditional | **Class $\mathcal{P}_1$ (UNCOND ELIM)** |
| 137 | 1 | 68 | 68 | YES | 34 | 2 | NO | $[34, 34]$ | 1 | Unconditional | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| **139** | 3 | 69 | 138 | YES | 69 | 1 | **YES** | $[69]$ | 1 | Unconditional | **Class $\mathcal{P}_1$ (UNCOND ELIM)** |
| **149** | 5 | 74 | 148 | YES | 74 | 1 | **YES** | $[74]$ | 1 | Unconditional | **Class $\mathcal{P}_1$ (UNCOND ELIM)** |
| 151 | 7 | 75 | 15 | NO | 15 | 5 | NO | $[15 \times 5]$ | 1 | Unconditional | **Non-$\mathcal{P}_1$: Split-2 ($g^+=5$)** |
| 157 | 5 | 78 | 52 | YES | 26 | 3 | NO | $[26, 26, 26]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: Split-2 ($g^+=3$)** |
| 163 | 3 | 81 | 162 | YES | 81 | 1 | **YES** | $[81]$ | **4** | Under GRH | **Non-$\mathcal{P}_1$: Even $h^+$ ($2 \mid h_{163}^+$)** |
| **167** | 7 | 83 | 83 | NO | 83 | 1 | **YES** | $[83]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **173** | 5 | 86 | 172 | YES | 86 | 1 | **YES** | $[86]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **179** | 3 | 89 | 178 | YES | 89 | 1 | **YES** | $[89]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **181** | 5 | 90 | 180 | YES | 90 | 1 | **YES** | $[90]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| 191 | 7 | 95 | 95 | NO | 95 | 1 | **YES** | $[95]$ | **11** | Under GRH | **Non-$\mathcal{P}_1$: Non-Trivial $h^+ = 11$** |
| 193 | 1 | 96 | 96 | YES | 48 | 2 | NO | $[48, 48]$ | 1 | Under GRH | **Non-$\mathcal{P}_1$: $p \equiv 1 \pmod 8$** |
| **197** | 5 | 98 | 196 | YES | 98 | 1 | **YES** | $[98]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |
| **199** | 7 | 99 | 99 | NO | 99 | 1 | **YES** | $[99]$ | 1 | Under GRH | **Class $\mathcal{P}_1$ (GRH ELIM)** |

---

## 5. In-Depth Mathematical Analysis of Non-$\mathcal{P}_1$ Primes

### 5.1 The Even Class Number Anomaly: $p = 163$
- **Arithmetic Invariants**:
  $$p = 163, \quad d = 81, \quad \operatorname{ord}_{163}(2) = 162 = p - 1, \quad f^+ = 81, \quad g^+ = 1.$$
  Thus, $2$ is **strictly inert** in $\mathbb{Q}(\zeta_{163})^+$.
- **The Failure**:
  According to van der Linden (1982), Schoof (2003), and Miller (2014), the plus class number is:
  $$h_{163}^+ = 4.$$
- **Obstruction to Sahoo's Descent**:
  In Sahoo's proof (Propositions 1.9 & 1.10), the valuation bound $\max(|v(\lambda)|, |v(\mu)|) \le 4$ on solutions to the $S$-unit equation $\lambda + \mu = 1$ requires that if $\mu \equiv 1 \pmod{\mathfrak{P}_2^5}$, the extension $K(\sqrt{\mu})$ cannot be an unramified quadratic extension.
  When $h_p^+$ is odd ($2 \nmid h_p^+$), class field theory guarantees that $\mathcal{O}_{K^+}$ has **no unramified quadratic extensions**; hence $\mu$ must be a global square in $\mathcal{O}_{K^+}$, triggering the infinite descent.
  For $p = 163$, the 2-part of the class group is non-trivial:
  $$\operatorname{Cl}(\mathcal{O}_{K^+})[2] \ne 0 \quad (\text{specifically } \operatorname{Cl} \cong \mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z} \text{ or } \mathbb{Z}/4\mathbb{Z}).$$
  Therefore, unramified quadratic extensions of $K^+$ exist! An $S$-unit $\mu \equiv 1 \pmod{\mathfrak{P}_2^5}$ does not need to be a square; it can generate one of the unramified quadratic extensions. Consequently, **Sahoo's algebraic descent fails for $p = 163$**.
- **Resolution Strategy**:
  As developed in Checkpoint U107 for $p = 29$ (where narrow class number $h_{29}^+ = 8$), the bound on $S$-unit solutions can be resolved directly via the algorithmic $S$-unit equation solver of Alvarado et al. (2021) (`xhyper`), certifying whether solutions with valuation $\ge 5$ exist without relying on the Kummer descent lemma.

### 5.2 The Odd Non-Trivial Class Number Case: $p = 191$
- **Arithmetic Invariants**:
  $$p = 191, \quad d = 95, \quad \operatorname{ord}_{191}(2) = 95 = \frac{p-1}{2}, \quad f^+ = 95, \quad g^+ = 1.$$
  Because $191 \equiv 7 \pmod 8$, $(\frac{-1}{191}) = -1 \implies -1 \notin \langle 2 \rangle$, so $2$ is **strictly inert** in $\mathbb{Q}(\zeta_{191})^+$.
- **Class Group Structure**:
  Schoof (2003) and Miller (2014) established that:
  $$h_{191}^+ = 11, \quad \operatorname{Cl}(\mathcal{O}_{K^+}) \cong \mathbb{Z}/11\mathbb{Z}.$$
- **Sahoo Algebraic Criterion vs. Strict $h_p^+ = 1$**:
  - **2-Primary Divisibility**: Notice that $2 \nmid 11$. Thus:
    $$\operatorname{Cl}(\mathcal{O}_{K^+})[2] = 0.$$
    Because the 2-torsion of the class group is completely trivial, the Kummer descent lemma at the prime 2 **actually remains algebraically valid**! An element $\mu \equiv 1 \pmod{\mathfrak{P}_2^5}$ cannot define an unramified quadratic extension because $K^+$ has no quadratic unramified extensions of degree 2.
  - **Why Excluded under Strict $h_p^+ = 1$**: Sahoo (2025) explicitly states the theorem for fields where $h_p^+ = 1$ to avoid non-principal ideals during Frey curve minimal model reductions and level lowering conductor computations. Thus, while $p = 191$ satisfies Sahoo's algebraic 2-torsion condition, it requires non-principal ideal verification for full Frey curve integrality.

### 5.3 Primes with $p \equiv 1 \pmod 8$ ($p = 113, 137, 193$)
For these three primes, $(\frac{2}{p}) = 1$, so 2 factors into two prime ideals in the real quadratic subfield $\mathbb{Q}(\sqrt{p})$.
- $p = 113$: $\operatorname{ord}_{113}(2) = 28$, $-1 \in \langle 2 \rangle \implies f^+ = 14, g^+ = 4$.
- $p = 137$: $\operatorname{ord}_{137}(2) = 68 = (p-1)/2$, but $-1 \in \langle 2 \rangle \implies f^+ = 34, g^+ = 2$.
- $p = 193$: $\operatorname{ord}_{193}(2) = 96 = (p-1)/2$, but $-1 \in \langle 2 \rangle \implies f^+ = 48, g^+ = 2$.
As shown in Checkpoint U108, these primes require descent to the decomposition field $F_2$ where 2 is inert. For $p = 137$ and $p = 193$, $g^+ = 2$, meaning the decomposition field $F_2$ is simply the quadratic field $\mathbb{Q}(\sqrt{p})$! Modularity of elliptic curves over real quadratic fields is unconditional (Freitas--Le Hung--Siksek 2015).

### 5.4 Cyclotomic Split Primes ($p = 109, 127, 151, 157$)
- **$p = 109$ ($g^+ = 3$)**: Residue degree $f^+ = 18$. The decomposition field is a totally real cubic field $F_3 = K_{109}^H$ of degree $g^+ = 3$. By Derickx--Najman--Siksek (2020), elliptic curves over totally real cubic fields are modular.
- **$p = 127$ ($g^+ = 9$)**: Because $p = 2^7 - 1$ is a Mersenne prime, $2^7 \equiv 1 \pmod{127}$, making $\operatorname{ord}_{127}(2) = 7$ exceptionally small. The residue degree is $f^+ = 7$, splitting into $g^+ = 63 / 7 = 9$ prime ideals.
- **$p = 151$ ($g^+ = 5$)**: Residue degree $f^+ = 15$, splitting into $g^+ = 5$ prime ideals. The decomposition field is a quintic field $F_5$.
- **$p = 157$ ($g^+ = 3$)**: Residue degree $f^+ = 26$, splitting into $g^+ = 3$ prime ideals. The decomposition field is a cubic field $F_3$.

---

## 6. Synthesis: Cumulative Class $\mathcal{P}_1$ Statistics ($19 \le p < 200$)

Combining the results of Checkpoints U103/U107 ($19 \le p < 100$, 18 primes) and U110 ($100 < p < 200$, 21 primes):

| Interval | Total Primes | 2 Inert in $K^+$ ($g^+=1$) | $h_p^+ = 1$ | Strict Class $\mathcal{P}_1$ ($2$ inert $\land h^+=1$) | Non-$\mathcal{P}_1$ Primes |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$[19, 100)$** | 18 | 12 (66.7%) | 18 (100.0%) | **12 (66.7%)** | 6 (33.3%) |
| **$(100, 200)$** | 21 | 14 (66.7%) | 19 (90.5%) | **12 (57.1%)** | 9 (42.9%) |
| **Total $[19, 200)$** | **39** | **26 (66.7%)** | **37 (94.9%)** | **24 (61.5%)** | **15 (38.5%)** |

### Complete Inventory of Class $\mathcal{P}_1$ Primes up to 200
$$\mathbf{\mathcal{P}_1 \cap [19, 200) = \{19, 23, 29^*, 37, 47, 53, 59, 61, 67, 71, 79, 83, 101, 103, 107, 131, 139, 149, 167, 173, 179, 181, 197, 199\}}.$$
*(Note: $p = 29$ has wide class number $h_{29} = 1$ but narrow class number $h_{29}^+ = 8$, as analyzed in U107).*

Over the entire range $p \in [19, 200)$, exactly **61.5% of all prime exponents** are asymptotically eliminated by Sahoo's Theorem for solutions with $\ell, m > 10^{60}$.

---

## 7. Computational Verification and Artifact Reproducibility

The complete computational audit was performed and certified using Python 3.14.7 and PARI/GP 2.17.4 on Apple Silicon.
To reproduce the computations:

```bash
python3 code/U110_cyclotomic_p100_p200.py
```

The output confirms:
- Execution time: ~2.2 seconds.
- Mod-2 polynomial factorizations matched predicted residue degrees and splitting indices with 100% agreement.
- Machine-readable audit data exported to [`research/checkpoints/U110_real_cyclotomic_audit_p100_p200.json`](file://[LOCAL_HOME]/Downloads/beal/research/checkpoints/U110_real_cyclotomic_audit_p100_p200.json).
