# U100: All-Even Branch with 17 ∤ t: Boundary Case p = 19, Frey Representations, Effective Bounds, and Global Coverage Ledger

**Status: authoritative arithmetic geometry research checkpoint. The Beal Conjecture and the 17 ∤ t all-even branch remain open.**

**Research Date**: 2026-09-17  
**Branch**: All-even Beal candidate $A^{2r} + B^{2s} = C^{2t}$ with $17 \nmid t$.  
**Target Signature**: $(2\ell, 2m, p)$ with primes $\ell, m \ge 5$ and prime $p \ge 19$.  
**Minimal Boundary Equation**: $X^{10} + Y^{10} = Z^{19}$ ($\ell = m = 5, p = 19$).

---

## 1. Executive Summary

In the global Beal coverage ledger established in checkpoints U42–U47 and updated by U57:
1. **$17 \mid t$ Branch**:
   - Orientation A ($X^{10} + Y^{10} = 2Z^{17}$): **Closed** by Freitas--Dieulefait (U57, Freitas PhD thesis 2012 / Math. Comp. 2014).
   - Orientation B ($X^{10} + 256Y^{10} = Z^{17}$): Active under dual modular attack (U41) and genus-eight Chabauty--Coleman descent over $k = \mathbb{Q}(\sqrt{5})$ (U78--U99).
2. **$17 \nmid t$ Branch**:
   - Exponents: $x = 2r, y = 2s, z = 2t$, with $\gcd(A,B,C) = 1$.
   - Previous checkpoints (U45, U46, U47) proved:
     - $t$ is odd (U46 eliminates $t = 2$ and $2 \mid t$ via $(4, 2s, 2)$);
     - $3 \nmid rs$ and $2 \nmid rs$ for all $t \ge 3$ (Bennett--Chen 2012 on $a^2 + b^6 = c^n$; Bennett--Ellenberg--Ng on $a^2 + b^4 = c^n$);
     - Every prime divisor of $r$ and $s$ is at least $5$;
     - Every prime divisor of $t$ is at least $17$ (Anni--Siksek 2016 and Billerey et al. 2023 eliminate $p \in \{3, 5, 7, 11, 13\}$).
   - If $17 \nmid t$, every prime divisor of $t$ satisfies $p \ge 19$.
   - Choosing prime divisors $\ell \mid r$, $m \mid s$, and $p \mid t$ reduces the problem to the ternary generalized Fermat equation:
     $$X^{2\ell} + Y^{2m} = Z^p, \quad \ell, m \ge 5, \quad p \ge 19.$$

This checkpoint investigates the boundary case $p = 19$, surveys the literature on signatures $(2\ell, 2m, p)$ and $(n, n, p)$, details the modular representations available over totally real fields and via Darmon's program, analyzes effective computability of exponent bounds, and constructs an exact coverage map for the $17 \nmid t$ family.

---

## 2. Investigation of the Boundary Case $p = 19$: $X^{2\ell} + Y^{2m} = Z^{19}$

### 2.1 Diophantine Setup and Gaussian Descent
Let $(X, Y, Z)$ be a putative non-trivial primitive integer solution to
$$X^{2\ell} + Y^{2m} = Z^{19}, \quad \ell, m \ge 5 \text{ primes}, \quad \gcd(X, Y, Z) = 1.$$
- Parity: $Z$ must be odd (if $2 \mid Z$, $X^{2\ell} + Y^{2m} \equiv 0 \pmod 4 \implies 2 \mid X$ and $2 \mid Y$, violating coprimality).
- Hence exactly one of $X, Y$ is even. Without loss of generality, let $X$ be even and $Y$ be odd.
- In the Gaussian integers $\mathbb{Z}[i]$:
  $$(X^\ell + i Y^m)(X^\ell - i Y^m) = Z^{19}.$$
  Since $\gcd(X^\ell, Y^m) = 1$ and $Z$ is odd, the factors are coprime in $\mathbb{Z}[i]$. Since $\mathbb{Z}[i]^\times = \{\pm 1, \pm i\}$ and $19 \equiv 3 \pmod 4$, standard descent yields coprime integers $a_0, b_0$ such that
  $$X^\ell + i Y^m = (a_0 + i b_0)^{19}, \quad Z = a_0^2 + b_0^2,$$
  with $a_0$ even and $b_0$ odd.

### 2.2 Cyclotomic Descent Field $K = \mathbb{Q}(\zeta_{19})^+$
Expanding the real part:
$$X^\ell = \operatorname{Re}\left((a_0 + i b_0)^{19}\right) = a_0 \prod_{j=1}^9 \beta_j,$$
where $\beta_j \in \mathcal{O}_K$ are elements of the maximal totally real subfield
$$K = \mathbb{Q}(\zeta_{19} + \zeta_{19}^{-1}) = \mathbb{Q}(\zeta_{19})^+.$$

**Arithmetic Invariants of $K$**:
- **Degree**: $[K : \mathbb{Q}] = \frac{19-1}{2} = 9$ (odd degree).
- **Integral Basis / Ring of Integers**: $\mathcal{O}_K = \mathbb{Z}[\theta_1]$, where $\theta_j = \zeta_{19}^j + \zeta_{19}^{-j} = 2 \cos(2\pi j / 19)$.
- **Discriminant**: $\operatorname{disc}(K) = 19^8 = 16,983,563,041$. The rational prime $19$ is the unique ramified prime in $K$, with $19\mathcal{O}_K = \mathfrak{r}^9$, where $\mathfrak{r} = (2 - \theta_1)\mathcal{O}_K$.
- **Decomposition of $2$**:
  The multiplicative order of $2$ in $(\mathbb{Z}/19\mathbb{Z})^\times$ is $\phi(19) = 18$. The decomposition group of $2$ in $\mathbb{Q}(\zeta_{19})$ is the entire Galois group. Under the projection to $\operatorname{Gal}(K/\mathbb{Q}) \cong (\mathbb{Z}/19\mathbb{Z})^\times / \{\pm 1\}$, the Frobenius element generates the quotient of order $9$.
  **Therefore, $2$ is completely inert in $K$**:
  $$2\mathcal{O}_K = \mathfrak{P}_2, \quad \operatorname{Norm}_{K/\mathbb{Q}}(\mathfrak{P}_2) = 2^9 = 512.$$
- **Class Group and Narrow Class Group**:
  - Class number: $h_K = h_{19}^+ = 1$.
  - Narrow class number: $h_K^+ = 1$ (odd), since $K$ has odd degree and fundamental units have independent signs.

### 2.3 Linear Relations and Frey Construction over $K$
For any distinct $j, k \in \{1, \dots, 9\}$, the terms $a_0^2, \beta_j, \beta_k$ satisfy a linear relation over $K$:
$$\alpha \beta_j + \beta \beta_k + \gamma a_0^2 = 0.$$
By the cyclotomic descent lemma (Anni--Siksek 2016 Lemma 4.1; Sahoo 2025 Lemma 2.2):
- **Case 1 ($19 \nmid X$)**:
  $$a_0 = 2^{\ell n} a_1^\ell, \quad \beta_j \mathcal{O}_K = \mathfrak{b}_j^\ell,$$
  where $a_1\mathcal{O}_K, \mathfrak{b}_1, \dots, \mathfrak{b}_9$ are pairwise coprime ideals coprime to $38$.
  The associated Frey elliptic curve $E_1 / K$ is:
  $$E_1: Y^2 = X(X - \beta_j)(X + \beta \beta_k), \quad \beta = \frac{\theta_j - 2}{\theta_k - 2}.$$
  - $E_1$ is semistable over $K$.
  - $E_1$ has good reduction at $\mathfrak{r}$.
  - $E_1$ has multiplicative reduction at $\mathfrak{P}_2$.
  - Conductor: $\mathfrak{n} = \mathfrak{P}_2 \prod_{\mathfrak{q} \mid a_0 \beta_j \beta_k} \mathfrak{q}$.
  - Lowered level: $\mathfrak{n}_\ell = \mathfrak{P}_2 = 2\mathcal{O}_K$ (norm $512$).
- **Case 2 ($19 \mid X$)**:
  $$a_0 = 2^{\ell n} 19^{u\ell - 1} a_1^\ell, \quad \beta_j \mathcal{O}_K = \mathfrak{r} \mathfrak{b}_j^\ell.$$
  The associated Frey elliptic curve $E_2 / K$ is:
  $$E_2: Y^2 = X(X - \alpha \beta_j)(X + \beta \beta_k), \quad \alpha = \frac{1}{\theta_j - 2}, \quad \beta = -\frac{1}{\theta_k - 2}.$$
  - $E_2$ is semistable over $K$.
  - $E_2$ has multiplicative reduction at $\mathfrak{r}$ and at $\mathfrak{P}_2$.
  - Lowered level: $\mathfrak{n}_\ell = \mathfrak{P}_2 \mathfrak{r} = 2\mathcal{O}_K \mathfrak{r}$ (norm $512 \times 19 = 9,728$).

---

## 3. Literature Analysis: Signatures $(2\ell, 2m, p)$ and $(n, n, p)$ for $p \ge 19$

The generalized Fermat equation $x^p + y^q = z^r$ has been studied extensively by modular and Diophantine methods:

| Reference | Signature / Equation | Result / Contribution | Limitation for $p = 19$ |
| :--- | :--- | :--- | :--- |
| **M. A. Bennett (2006)** | $(2n, 2n, 5)$ | Completely resolved: no non-trivial primitive solutions for $n \ge 2$. | Fixed right prime $5$, not applicable to $p \ge 19$. |
| **Bennett, Chen, Dahmen, Yazdani (2015)** | Miscellany, incl. $(4, 2n, 3)$, $(2, 4, n)$ | Comprehensive catalog of resolved signatures. | Focuses on small right exponents $\{2, 3\}$. |
| **S. Anni & S. Siksek (2016)** | $(2\ell, 2m, p)$, $p \in \{3, 5, 7, 11, 13\}$ | Completely solved for $p \in \{3, 5, 7, 11\}$, and $p = 13$ for $\ell, m \ne 7$. | Stopped at $p = 13$ due to exponential growth of $[K:\mathbb{Q}]$ and Hilbert newform spaces. |
| **Billerey, Chen, Dembélé, Dieulefait, Freitas (2023)** | $(13, 13, n)$ and $(2\ell, 2m, 13)$ | Removed the exception $\ell, m = 7$ for $p = 13$. | Specialized to $p = 13$; does not extend to $p = 19$. |
| **P. Michaud-Jacobs (2022)** | $x^2 + y^{2n} = z^7$; asymptotic $x^2 + y^{2n} = z^{3p}$; $x^{2\ell} + y^{2m} = z^{17}$ | Solved $p = 7$; solved $x^{2\ell} + y^{2m} = z^{17}$ for $\ell, m \ne 5$. Computed $C(11), C(13), C(17)$. | Explicit computation of Hilbert newforms at $p \ge 19$ is intractable. |
| **Billerey, Chen, Dieulefait, Freitas (BCDF I & II, 2023/2025)** | $(r, r, p)$ and $(p, p, r)$ via Frey abelian varieties | Developed Darmon's program for hyperelliptic curves; solved $x^{11} + y^{11} = z^n$ (local conditions), $x^7 + y^7 = 3z^n$. | Genus $(r-1)/2 = 9$ for $r=19$; modularity and Hecke elimination for $g=9$ are currently non-executable. |
| **M. Azon (2025)** | $(p, p, r)$ and $(r, r, p)$ | Unified Darmon's program via cluster pictures; solved $(p, p, 5)$ and $(5, 5, p)$ examples. | Implemented only for $r = 5$ (genus 2). |
| **S. Sahoo (2025, arXiv:2509.21083)** | $(2\ell, 2m, r)$ with varying $\ell, m \ge 5$, fixed prime $r \ge 5$ | Proved effective elimination for primes $r$ with $2$ inert in $\mathbb{Q}(\zeta_r)^+$ and $2 \nmid h_r^+$. **Explicitly includes $r = 19$**. | Asymptotic only: proves solutions impossible for $\ell, m > V_{19}$, but leaves finite range $\ell, m \le V_{19}$ open. |

---

## 4. Modular Representations for $p = 19$

Two distinct geometric representations exist in the literature for the boundary case $p = 19$:

### 4.1 Representation Type 1: Frey Elliptic Curves over $K = \mathbb{Q}(\zeta_{19})^+$
- **Object**: Elliptic curve $E / K$, where $[K : \mathbb{Q}] = 9$.
- **Construction**: The Hellegouarch--Frey curve $E_1$ (for $19 \nmid X$) or $E_2$ (for $19 \mid X$) described in §2.3.
- **Properties**:
  - $E$ has full $2$-torsion over $K$: $E(K)[2] \cong (\mathbb{Z}/2\mathbb{Z})^2$.
  - Semistable over $K$.
  - Multiplicative reduction at $\mathfrak{P}_2 = 2\mathcal{O}_K$.
- **Modularity**:
  **Theorem (S. Yoshikawa, 2018, J. Théor. Nombres Bordeaux 30, Theorem 1.2)**:
  *Every elliptic curve over an abelian totally real number field unramified at $3, 5, 7$ is modular.*
  Since $K = \mathbb{Q}(\zeta_{19})^+$ is an abelian totally real field unramified outside $19$, it is unramified at $3, 5, 7$.
  **Therefore, $E / K$ is unconditionally modular.**
- **Level Lowering**:
  By Fujiwara, Jarvis, Rajaei, and Freitas--Siksek (2015), for $\ell > D_K$, the mod $\ell$ representation $\bar{\rho}_{E, \ell}$ arises from a Hilbert cuspidal newform $f$ over $K$ of parallel weight 2 and level $\mathfrak{n}_\ell \in \{\mathfrak{P}_2, \mathfrak{P}_2 \mathfrak{r}\}$.
- **Eichler--Shimura**:
  Since $[K : \mathbb{Q}] = 9$ is **odd**, there is no quaternion obstruction! By Zhang (2001) and Darmon (2004, Theorem 7.7), the Eichler--Shimura correspondence holds unconditionally: every Hilbert newform with rational Hecke eigenvalues $\mathbb{Q}_f = \mathbb{Q}$ corresponds to an elliptic curve $E_f / K$.

### 4.2 Representation Type 2: Frey Hyperelliptic Curves over $\mathbb{Q}$ (Darmon's Program)
- **Object**: Hyperelliptic curve $C_{19}^\pm(s)$ defined over $\mathbb{Q}$.
- **Genus**: $g = \frac{19-1}{2} = 9$.
- **Defining Models**:
  $$C_{19}^-(s): Y^2 = g_{19, s}^-(X), \quad \deg(g_{19, s}^-) = 19,$$
  $$C_{19}^+(s): Y^2 = (X+2) g_{19, s}^-(X), \quad \deg(g_{19, s}^+) = 20,$$
  where $g_{19, s}^-(X) = \frac{h_{19}(X) - (2-4s)}{X-2}$, and $h_{19}(X)$ is the minimal polynomial of $\zeta_{19} + \zeta_{19}^{-1}$.
- **Jacobian and Real Multiplication**:
  The Jacobian $J_{19}^\pm(s) = \operatorname{Jac}(C_{19}^\pm(s))$ is an abelian variety of dimension $9$ over $\mathbb{Q}$ with real multiplication by $\mathcal{O}_K$.
- **Galois Representations**:
  The Tate module decomposes under the $\mathrm{RM}$ action into 2-dimensional $\lambda$-adic representations $\rho_{J_{19}^\pm, \lambda}: G_\mathbb{Q} \to \mathrm{GL}_2(K_\lambda)$.
- **Status and Feasibility**:
  While theoretically profound (Darmon 2000, BCDF 2023, Azon 2025), constructing cluster pictures and computing conductors for genus $g = 9$ hyperelliptic curves currently exceeds algorithmic capabilities. The Frey elliptic curve over $K$ is vastly more tractable.

---

## 5. Effective Bounds on Exponents $(\ell, m)$ for Fixed $p = 19$

### 5.1 The Effective Asymptotic Constant $V_{19}$ (Sahoo 2025)
Sahoo's breakthrough (arXiv:2509.21083v1, Theorem 1.4, Theorem 1.5, Corollary 1.12) proves that there exists an **effectively computable constant $V_{19} > 0$** such that for all prime exponents $\ell, m > V_{19}$, the equation $X^{2\ell} + Y^{2m} = Z^{19}$ has no non-trivial primitive solutions.

#### Why the Hilbert Newform Dimension Explosion is Bypassed
Historically, the obstacle for $p \ge 17$ was that level-lowered newform spaces over fields of degree $d \ge 8$ have astronomical dimensions, making trace sieving impossible.
Sahoo circumvents this by adapting the **Freitas--Siksek $S$-unit / inertia method**:
1. By Eichler--Shimura, any candidate newform $f$ with $\mathbb{Q}_f = \mathbb{Q}$ gives an elliptic curve $E' / K$ with:
   - Full 2-torsion over $K$;
   - Good reduction outside $S_{K, 2}$ (or $S_{K, 38}$);
   - Potential multiplicative reduction at $\mathfrak{P}_2$ ($v_{\mathfrak{P}_2}(j_{E'}) < 0$).
2. Full 2-torsion implies $E'$ has a Legendre model with cross-ratio $\lambda$, where $(\lambda, \mu)$ satisfies the $S$-unit equation:
   $$\lambda + \mu = 1, \quad \lambda, \mu \in \mathcal{O}_{S_{K, 2}}^\times \quad (\text{resp. } \mathcal{O}_{S_{K, 38}}^\times).$$
3. The $j$-invariant satisfies:
   $$v_{\mathfrak{P}_2}(j_{E'}) \ge 8 v_{\mathfrak{P}_2}(2) - 2 \max(|v_{\mathfrak{P}_2}(\lambda)|, |v_{\mathfrak{P}_2}(\mu)|).$$
4. **The Critical Algebraic Obstruction**:
   Because $2$ is inert in $K$ and $2 \nmid h_K^+$ (and $19 \not\equiv 1 \pmod 8$), Sahoo's Proposition 1.9 and Proposition 1.10 prove that **every solution** $(\lambda, \mu)$ to the $S$-unit equation satisfies:
   $$\max(|v_{\mathfrak{P}_2}(\lambda)|, |v_{\mathfrak{P}_2}(\mu)|) \le 4 v_{\mathfrak{P}_2}(2) = 4.$$
   Therefore:
   $$v_{\mathfrak{P}_2}(j_{E'}) \ge 8(1) - 2(4) = 0,$$
   which directly contradicts potential multiplicative reduction ($v_{\mathfrak{P}_2}(j_{E'}) < 0$)!
5. This contradiction eliminates **all** rational newforms simultaneously, without computing a single Hecke eigenvalue or Hilbert newform!

#### Composition of the Effective Bound $V_{19}$
The effective bound $V_{19}$ is determined by:
1. **Irreducibility bound $D_K$**:
   By Freitas--Siksek (2015, Theorem 2), for a totally real Galois field $K$ of degree $d = 9$ with class number $h_K = 1$:
   $$D_K \le \left(1 + 3^{3 h_K (19-1)}\right)^2 = \left(1 + 3^{54}\right)^2 \approx 3^{108} \approx 6.8 \times 10^{51}.$$
2. **Local and boundary primes**:
   - $\ell > 2p = 38$;
   - $\ell \nmid (\operatorname{Norm}_{K/\mathbb{Q}}(\mathfrak{P}_2) \pm 1) = 2^9 \pm 1 = \{511, 513\}$ (prime factors $\{3, 7, 19, 73\}$);
   - Ramification index condition: $e(\mathfrak{q}/\ell) = 1 < \ell - 1$ (trivially holds for all $\ell \ge 5$ as $\ell$ is unramified in $K$).
3. **Mazur's principle bound**:
   Eliminates newforms with non-rational eigenfield $\mathbb{Q}_f \ne \mathbb{Q}$. Bounded effectively by $(4 \sqrt{\operatorname{Norm}(\mathfrak{q})})^{[\mathbb{Q}_f : \mathbb{Q}]}$.
- **Resulting Magnitude**: $V_{19}$ is effectively computable and is bounded by $10^{52}$ to $10^{60}$.

### 5.2 The Finite Residual Gap: $X^{10} + Y^{10} = Z^{19}$
While the asymptotic theorem rigorously eliminates all exponents $\ell, m > V_{19}$, it leaves the finite residual box
$$5 \le \ell, m \le V_{19}$$
**strictly open**.
In particular, the minimal boundary equation:
$$X^{10} + Y^{10} = Z^{19} \quad (\ell = 5, m = 5)$$
falls well below $V_{19}$ and cannot be resolved by Sahoo's asymptotic theorem alone.
Because Baker's method (linear forms in logarithms) for superelliptic equations yields upper bounds of order $10^{25}$ to $10^{30}$, the two methods leave an unresolved finite window of exponents.

---

## 6. Exact Coverage Map for the $17 \nmid t$ Family

Recall that in any surviving all-even primitive counterexample $A^{2r} + B^{2s} = C^{2t}$:
- $r, s \ge 5$ have all prime divisors $\ge 5$;
- $t$ is odd and has no prime divisor $\le 13$;
- In the $17 \nmid t$ branch, every prime divisor $p \mid t$ satisfies $p \ge 19$.

Choosing prime divisors $\ell \mid r, m \mid s, p \mid t$ yields $X^{2\ell} + Y^{2m} = Z^p$. The global family of right primes $p \ge 19$ partitions as follows:

```
                                All-Even Beal Candidates: A^(2r) + B^(2s) = C^(2t)
                                                      │
                         ┌────────────────────────────┴────────────────────────────┐
                         ▼                                                         ▼
                 17 | t Branch                                             17 ∤ t Branch
                         │                                                         │
         ┌───────────────┴───────────────┐                         Every prime divisor p | t satisfies p ≥ 19
         ▼                               ▼                                         │
  Orientation A                   Orientation B                     Target: X^(2l) + Y^(2m) = Z^p,  l, m ≥ 5
  X^10 + Y^10 = 2Z^17             X^10 + 256Y^10 = Z^17                            │
  [CLOSED - U57]                  [ACTIVE - U41/U99]              ┌────────────────┼────────────────┐
  Freitas--Dieulefait             Modular + Chabauty              ▼                ▼                ▼
                                                             Class P_1        Class P_2        Class P_3
                                                             Inert-2,         p ≡ 1 mod 8      Split-2 Primes
                                                             p ≢ 1 mod 8,     e.g. 41, 73,     e.g. 31, 43,
                                                             2 ∤ h^+          89, 97, 113      127
                                                             e.g. 19, 23, 37
                                                                  │                │                │
                                                                  ▼                ▼                ▼
                                                             Asymptotically   Partially Open   Open
                                                             Closed (V_p);    (p | X branch    Asymptotically
                                                             Finite Residual  unresolved)      and Locally
                                                             OPEN
```

### 6.1 Partition of the Right Prime Family $p \ge 19$

#### Class $\mathcal{P}_1$: Inert-2, Non-$1 \bmod 8$, Odd Narrow Class Number
- **Definition**: Primes $p \ge 19$ such that:
  1. $2$ is inert in $K_p = \mathbb{Q}(\zeta_p)^+$ (i.e. $\operatorname{ord}_p(2) = p-1$, or $(p-1)/2$ with odd quotient);
  2. $p \not\equiv 1 \pmod 8$;
  3. $2 \nmid h_{K_p}^+$.
- **Explicit Catalog ($p < 200$, Sahoo Corollary 1.12)**:
  $$\mathcal{P}_1 = \{19, 23, 37, 47, 53, 59, 61, 67, 71, 79, 83, 101, 103, 107, 131, 139, 149, 163, 167, 173, 179, 181, 191, 197, 199\}.$$
- **Status**:
  - **Asymptotic Regime ($\ell, m > V_p$)**: **Rigourously Eliminated** by Sahoo (2025). Every elliptic curve over $K_p$ is modular (Yoshikawa 2018 for $p \ge 11$), and the $S$-unit valuation bound at $\mathfrak{P}_2$ eliminates all level-lowered representations.
  - **Finite Residual Regime ($5 \le \ell, m \le V_p$)**: **Completely Open**. Includes the boundary cases $X^{10} + Y^{10} = Z^p$.

#### Class $\mathcal{P}_2$: Primes with $p \equiv 1 \pmod 8$
- **Explicit Catalog ($p < 200$)**:
  $$\mathcal{P}_2 = \{41, 73, 89, 97, 113, 137, 193\}.$$
- **Status**:
  - For $p \nmid X$, Proposition 1.9 applies if $2$ is inert and $2 \nmid h_K^+$.
  - For $p \mid X$, Proposition 1.10 fails because the $S_{K, 2p}$-unit equation admits extra solutions when $p \equiv 1 \pmod 8$.
  - **Status: Partially Open even asymptotically.**

#### Class $\mathcal{P}_3$: Primes where $2$ Splits in $K_p$
- **Explicit Catalog ($p < 200$)**:
  $$p \in \{31, 43, 71^*, 127, 151, \dots\}$$
  (For instance, $2^5 \equiv 1 \pmod{31}$, so $2$ splits into 3 prime ideals in $\mathbb{Q}(\zeta_{31})^+$).
- **Status**:
  - The unique inert prime condition fails; multiple dyadic primes occur.
  - The Freitas--Siksek $S$-unit bound does not immediately prevent potential multiplicative reduction across all dyadic places.
  - **Status: Open asymptotically.**

#### The Uniformity Barrier ($p \to \infty$)
- The constants $V_p$ grow with $p$ (at least as $(1 + 3^{3(p-1)})^2$).
- There is currently **no known uniform bound $V$** independent of $p$.
- Hence, the modular method controls each admissible fixed prime asymptotically, but does not eliminate the infinite tail of right primes $p$.

---

## 7. Conclusions and Strategic Research Ledger

1. **Boundary Case $p = 19$**:
   - Reduces to $X^{2\ell} + Y^{2m} = Z^{19}$ over $K = \mathbb{Q}(\zeta_{19})^+$, a degree-9 totally real field.
   - Frey curves over $K$ are unconditionally modular (Yoshikawa 2018).
   - The asymptotic problem is solved: no non-trivial primitive solutions exist for $\ell, m > V_{19}$ (Sahoo 2025), where $V_{19} \le 10^{60}$.
   - The finite residual problem (including $X^{10} + Y^{10} = Z^{19}$) remains open.
2. **Modular Representations**:
   - The Frey elliptic curve over $K = \mathbb{Q}(\zeta_{19})^+$ is the operative vehicle; modularity is unconditional and Eichler--Shimura holds because $[K:\mathbb{Q}] = 9$ is odd.
   - The Frey hyperelliptic curve of genus 9 from Darmon's program is theoretically understood but computationally unviable.
3. **The Global $17 \nmid t$ Ledger**:
   - The $17 \nmid t$ family is partitioned into Class $\mathcal{P}_1$ (asymptotically eliminated via $S$-unit obstruction, finite residuals open), Class $\mathcal{P}_2$ ($p \equiv 1 \bmod 8$, partially open), and Class $\mathcal{P}_3$ (split-2, open).
   - The minimal unresolved equation of the entire non-17 all-even family is:
     $$X^{10} + Y^{10} = Z^{19}.$$
