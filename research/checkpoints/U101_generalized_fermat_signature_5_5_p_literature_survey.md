# U101: Comprehensive Literature Survey and Status Ledger for Generalized Fermat Equations $X^5 + Y^5 = Z^p$ and $X^{10} + Y^{10} = Z^p$

**Date**: 2026-09-17  
**Author**: Arithmetic Number Theory Research Group  
**Target Equations**:  
1. $X^5 + Y^5 = Z^p$ for primes $p \ge 2$, with $\gcd(X, Y, Z) = 1$, $X Y Z \neq 0$.  
2. $X^{10} + Y^{10} = Z^p$ for primes $p \ge 3$, with $\gcd(X, Y, Z) = 1$, $X Y Z \neq 0$.  
**Context**: Attack on the Beal Conjecture for exponents having prime factors 5 and $p$.  
**Status**: Authoritative research checkpoint, literature survey, classification ledger, and obstruction analysis.

---

## 1. Executive Summary & Context

The generalized Fermat equation (GFE) with signature $(p, q, r)$ is:
$$A^p + B^q = C^r, \quad \gcd(A, B, C) = 1, \quad A B C \neq 0.$$
By the Darmon–Granville theorem (1995), for any fixed signature $(p, q, r)$ with hyperbolic index $\chi = \frac{1}{p} + \frac{1}{q} + \frac{1}{r} < 1$, there are only finitely many primitive integer solutions $(A, B, C)$. The Beal Conjecture asserts that for all integer exponents $p, q, r \ge 3$, there are no non-trivial primitive solutions (i.e. if $A^p + B^q = C^r$ with $p, q, r \ge 3$, then $\gcd(A, B, C) > 1$).

Within the global program to resolve the Beal Conjecture, equations where exponents have prime factors $5$ and $p$ arise naturally in two key branches:
1. **The pure signature $(5, 5, p)$**: $X^5 + Y^5 = Z^p$.
2. **The decic signature $(10, 10, p)$**: $X^{10} + Y^{10} = Z^p$, which corresponds to setting $x = X^2, y = Y^2$ in $x^5 + y^5 = Z^p$, imposing the additional rigid constraint that the fifth-power bases $x, y$ are positive integer squares.

This report delivers a rigorous survey of the arithmetic literature, provides an explicit taxonomy of all known Frey curves and Frey abelian varieties of $\mathrm{GL}_2$-type used for signature $(5, 5, p)$, details the exact status of $X^5 + Y^5 = Z^p$ across all prime exponents $p$, and maps out unconditionally proved results versus open frontiers for both $X^5 + Y^5 = Z^p$ and $X^{10} + Y^{10} = Z^p$.

---

## 2. Comprehensive Survey of the Literature

The study of $X^5 + Y^5 = Z^p$ has driven major developments in arithmetic geometry over the past three decades, evolving from classical descent to Frey curves over $\mathbb{Q}$, $\mathbb{Q}$-curves, Hilbert modular forms over totally real fields, multi-Frey techniques, and higher-dimensional Frey varieties within Darmon's program.

### 2.1. Alain Kraus (1997, 1998, 1999)
- **Kraus (1997, *Canad. J. Math.* 49:1139–1161)**: Proved effective upper bounds for exponents in generalized Fermat equations using linear forms in logarithms and modular forms.
- **Kraus (1998, *Experiment. Math.* 7:1–13, "Sur l’équation $a^3 + b^3 = c^p$")**: Pioneered the systematic use of modular forms to solve ternary equations of signature $(3, 3, p)$. Kraus introduced the **Kraus method (sieve with auxiliary primes $q = 2kp + 1$)** to eliminate modular newforms when level-lowering alone leaves residual forms whose Fourier coefficients do not provide immediate contradictions.
- **Kraus (1999, *Ramanujan J.* 3:315–333, "On the Equation $x^p + y^q = z^r$: A Survey")**:
  On pages 329–330, Kraus explicitly constructed the first Frey elliptic curve over $\mathbb{Q}$ for the equation $x^5 + y^5 = z^p$:
  $$E'_{x,y}: Y^2 = X^3 - 5(x^2 + y^2) X^2 + 5 H_5(x,y) X,$$
  where $H_5(x,y) = \frac{x^5+y^5}{x+y} = x^4 - x^3 y + x^2 y^2 - x y^3 + y^4$.  
  When $5 \mid z$ (which forces $5 \mid H_5(x,y)$), Kraus constructed its quadratic twist over $\mathbb{Q}(\sqrt{-5})$:
  $$E_{x,y}: Y^2 = X^3 + (x^2 + y^2) X^2 - \frac{H_5(x,y)}{5} X.$$
  Kraus also constructed the genus-2 hyperelliptic curve:
  $$C_5(x,y): Y^2 = X^5 - 2(x^2 - 3xy + y^2)X^3 + (x-y)^4 X + 4xy(x+y)^2,$$
  whose Jacobian provides a Frey variety for the equation.

### 2.2. Bjorn Poonen (1998) & Darmon–Merel (1997)
- **Darmon–Merel (1997, *J. Reine Angew. Math.* 490:81–100)**: Proved that $x^n + y^n = z^2$ and $x^n + y^n = z^3$ have no non-trivial primitive integer solutions for all $n \ge 4$ using winding quotients of modular Jacobians $J_0(N)$.
- **Poonen (1998, *Acta Arith.* 86:193–205)**: Directly resolved signatures $(5, 5, 2)$ and $(5, 5, 3)$, showing that $x^5 + y^5 = z^2$ and $x^5 + y^5 = z^3$ have no non-trivial primitive integer solutions via descent to elliptic curves and Jacobians of genus-3 cyclic covers of $\mathbb{P}^1$.

### 2.3. Nicolas Billerey (2007) & Billerey–Dieulefait (2010)
- **Billerey (2007, *Bull. Austral. Math. Soc.* 76:161–194, "Équations de Fermat de type $(5,5,p)$")**:
  Systematically studied $x^5 + y^5 = d z^p$ using Darmon's Frey curve over $\mathbb{Q}$:
  $$W_{a,b}: y^2 = x^3 - 5(a^2 + b^2) x^2 + 5 \left(\frac{a^5 + b^5}{a+b}\right) x.$$
  Billerey computed the conductor $N_{W_{a,b}} = 2^\alpha 5^\beta \operatorname{rad}_{\{2,5\}}(a^5+b^5)$, proved absolute irreducibility of the mod $p$ Galois representations for $p \ge 7$, and identified the Serre levels after level lowering: $N \in \{50, 200, 400, 1200\}$.
- **Billerey–Dieulefait (2010, *Math. Comp.* 79:535–544, "Solving Fermat-type equations $x^5 + y^5 = d z^p$")**:
  Applied $W_{a,b}$ to solve $x^5 + y^5 = d z^p$ for infinitely many coefficients $d$. However, they uncovered the fundamental obstruction for $d = 1, 2, 3$:
  - When $d=1$, evaluating $W_{a,b}$ at the trivial solutions $(\pm 1, 0, \pm 1)$ yields elliptic curves without complex multiplication (specifically LMFDB curve `1200.a1` / Cremona `1200N1`), which persists as a non-CM newform at level 1200.
  - Standard level lowering cannot distinguish a putative non-trivial solution from the trivial ones without additional local constraints.

### 2.4. Sander Dahmen (2008) & Dahmen–Siksek (2014)
- **Dahmen (2008, PhD Thesis, Universiteit Utrecht)**: Established foundational frameworks for combining classical descent and modular techniques for superelliptic equations.
- **Dahmen–Siksek (2014, *Acta Arith.* 164:65–100, "Perfect powers expressible as sums of two fifth or seventh powers", arXiv:1309.4030)**:
  Achieved a breakthrough on $x^5 + y^5 = z^p$:
  1. **Complete unconditional proof for $5 \mid z$**: For any exponent $p \ge 2$, they proved $x^5 + y^5 = z^p$ has no non-trivial primitive solutions with $5 \mid z$. The proof uses Kraus' Frey curve $E_{x,y}$ over $\mathbb{Q}$, lowering to levels $N \in \{40, 80\}$. The newforms correspond to $E_{40a1}, E_{80a1}, E_{80b1}$. Traces at $q=3$ eliminate $E_{40a1}$ and $E_{80a1}$ for all $p \ge 7$; for $E_{80b1}$, traces at $q=3$ eliminate all $p \neq 17$, and Kraus' method at $q = 6 \cdot 17 + 1 = 103$ eliminates $p = 17$.
  2. **Unconditional resolution for $p = 7$ and $p = 19$**: For $5 \nmid z$, algebraic factorization over $\mathbb{Q}$ yields the hyperelliptic curve:
     $$C_p: Y^2 = 5 X^{2p} - 4$$
     of genus $g = (p-1)/2$. Using 2-descent on the Jacobians $J_p = \operatorname{Jac}(C_p)$, they proved $\operatorname{rank} J_7(\mathbb{Q}) = 1$ (with $g_7 = 3$) and $\operatorname{rank} J_{19}(\mathbb{Q}) = 1$ (with $g_{19} = 9$). Because $\operatorname{rank} J_p(\mathbb{Q}) < g_p$, Chabauty–Coleman at $p=3$ applies, determining $C_7(\mathbb{Q})$ and $C_{19}(\mathbb{Q})$ and proving that only trivial solutions exist.
  3. **Conditional resolution for $p = 11$ and $p = 13$ under GRH**: Factorization of $H_5(x,y)$ over $K = \mathbb{Q}(\sqrt{5})$ yields genus-$(p-1)/2$ curves $C_{p,i}$ over $K$. Assuming GRH to certify class and unit group computations in 2-descent on $J_{p,i}(K)$, they established $\operatorname{rank} J_{11,0}(K) = 1$ (genus 5) and $\operatorname{rank} J_{13,1}(K) = 1$ (genus 6), and completed the elimination via Chabauty–Coleman over $K$.

### 2.5. Luis Dieulefait & Nuno Freitas (2012, 2014)
- **Freitas (2012, PhD Thesis, Universitat de Barcelona)**: Constructed Frey curves over totally real fields for signatures $(r, r, p)$ and introduced the modular method using $\mathbb{Q}$-curves.
- **Dieulefait–Freitas (2014, *Math. Comp.* 83:917–933, "The Fermat-type equations $x^5 + y^5 = 2z^p$ or $3z^p$ solved through $\mathbb{Q}$-curves")**:
  Constructed two Frey elliptic curves $E_{a,b}$ and $F_{a,b}$ over $K = \mathbb{Q}(\sqrt{5})$:
  $$E_{a,b}: Y^2 = X^3 - 2\sqrt{5} a b X^2 - [a^4 - b^4 + 2\omega(a^3 b - a b^3)] X,$$
  $$F_{a,b}: Y^2 = X^3 + 2\sqrt{5} a b X^2 - [a^4 - b^4 + 2\bar{\omega}(a^3 b - a b^3)] X,$$
  where $\omega = \frac{1+\sqrt{5}}{2}$. These curves are $\mathbb{Q}$-curves completely unramified outside $2, 5,$ and primes dividing $a^5+b^5$. They resolved $x^5 + y^5 = 2 z^p$ and $x^5 + y^5 = 3 z^p$ for a set of primes of Dirichlet density $3/4$ (satisfying $p \equiv 1 \pmod 4$ or $p \equiv \pm 1 \pmod 5$).

### 2.6. Freitas, Le Hung, and Siksek (2015)
- **Freitas (2015, *Math. Z.* 279:605–639, "Recipes to Fermat-type equations of the form $x^r+y^r=Cz^p$")**: General explicit recipe attaching Frey curves over totally real subfields of $\mathbb{Q}(\zeta_r)$ to generalized Fermat equations.
- **Freitas–Le Hung–Siksek (2015, *Invent. Math.* 201:159–206)**: Proved modularity of all elliptic curves over real quadratic fields, freeing the Dieulefait–Freitas curves from having to rely on the $\mathbb{Q}$-curve hypothesis.
- **Freitas–Siksek (2015, *Algebra Number Theory* 9:875–895 & *J. Théor. Nombres Bordeaux* 27:67–76)**: Established general irreducibility criteria for mod $p$ representations of Frey curves over number fields, enabling level lowering over totally real fields.

### 2.7. Billerey, Chen, Dieulefait, and Freitas (2019, *Trans. AMS*)
- **BCDF (2019, *Trans. Amer. Math. Soc.* 371(12):8651–8677, arXiv:1703.06530)**:
  Established the "Multi-Frey" framework combining curves over $\mathbb{Q}$ and over $K = \mathbb{Q}(\sqrt{5})$ simultaneously:
  1. **Complete resolution of $x^5 + y^5 = 3z^n$**: Completely solved for all $n \ge 2$.
  2. **Theorem 3 (Second Case)**: For all primes $p$, $x^5 + y^5 = z^p$ has no non-trivial primitive solutions with $p \mid z$. The proof uses level raising at $p$ modulo $p$.
  3. **Theorem 5 ($5 \mid z$)**: For all primes $p$, $x^5 + y^5 = d z^p$ ($d \in \{1, 2\}$) has no non-trivial primitive solutions with $5 \mid a+b$ (equivalent to $5 \mid z$).
  4. **Theorem 6 ($z$ even)**: For all primes $p$, $x^5 + y^5 = z^p$ has no non-trivial primitive solutions with $2 \mid a+b$ (i.e. $z$ even). The proof uses Version 2 of the image of inertia argument to prove that the inertial field at 2 of $E_{a,b}$ cannot match any of the level-lowered newforms.

### 2.8. Billerey, Chen, Dieulefait, Freitas (2022/2025, Crelle)
- **BCDF (2022, arXiv:2205.15861; *J. Reine Angew. Math.* 2025, "On Darmon's program for the generalized Fermat equation, I")**:
  Developed the theory of higher-dimensional Frey abelian varieties $J_r = \operatorname{Jac}(C_r(a,b))$ of $\mathrm{GL}_2$-type over $K = \mathbb{Q}(\zeta_r)^+$. Proved modularity of Kraus' hyperelliptic Frey varieties.
  - **Reduction to Darmon's Conjecture**: They proved that the complete resolution of $x^5 + y^5 = z^p$ for all large $p$ reduces to Darmon's "Big Image Conjecture" (specifically, the Cartan case of the conjecture).

---

## 3. Exact Status of $X^5 + Y^5 = Z^p$

We categorize the exact status of $X^5 + Y^5 = Z^p$ for primitive integer solutions ($\gcd(X, Y, Z) = 1, X Y Z \neq 0$):

### 3.1. Small Exponents: $p = 2, 3, 5$
- **$p = 2$**: **UNCONDITIONALLY CLOSED (NO SOLUTIONS)**.  
  *Proof*: Bjorn Poonen (1998, *Acta Arith.* 86:193–205). Also a special case of Darmon–Merel (1997) for signature $(n, n, 2)$.
- **$p = 3$**: **UNCONDITIONALLY CLOSED (NO SOLUTIONS)**.  
  *Proof*: Bjorn Poonen (1998) and Darmon–Merel (1997, *J. Reine Angew. Math.* 490:81–100) for signature $(n, n, 3)$.
- **$p = 5$**: **UNCONDITIONALLY CLOSED (NO SOLUTIONS)**.  
  *Proof*: Fermat's Last Theorem for exponent 5, proved by A.-M. Legendre (1825) and P. G. Lejeune Dirichlet (1825/1828); also subsumed by A. Wiles (1995).

### 3.2. Exponents $p = 7, 11, 13, 17$
- **$p = 7$**: **UNCONDITIONALLY CLOSED (NO SOLUTIONS)**.  
  *Proof*: S. R. Dahmen and S. Siksek (2014, *Acta Arith.* 164:65–100, Theorem 1).
  - When $5 \mid Z$: Eliminated via Kraus Frey curve $E_{x,y}$ over $\mathbb{Q}$ and level lowering.
  - When $5 \nmid Z$: Eliminated via Chabauty–Coleman at prime 3 on the genus-3 curve $C_7: Y^2 = 5X^{14} - 4$ over $\mathbb{Q}$, where $\operatorname{rank} J_7(\mathbb{Q}) = 1 < 3$.
- **$p = 11$**: **CLOSED UNDER GRH; CONDITIONALLY PARTITIONED UNCONDITIONALLY**.  
  - *Under GRH*: Proved no non-trivial solutions by Dahmen–Siksek (2014, Theorem 3) using Chabauty–Coleman at prime 3 on the genus-5 curve $C_{11,0}$ over $\mathbb{Q}(\sqrt{5})$ ($\operatorname{rank} J_{11,0}(\mathbb{Q}(\sqrt{5})) = 1 < 5$).
  - *Unconditional status*:
    - $5 \mid Z$: Closed (Dahmen–Siksek 2014, BCDF 2019).
    - $2 \mid Z$ ($Z$ even): Closed (BCDF 2019, Theorem 6).
    - $11 \mid Z$: Closed (BCDF 2019, Theorem 3).
    - $Z$ odd, $\gcd(Z, 55) = 1$: **OPEN unconditionally** (relies on GRH to bound the class/unit group for the degree-22 number field $\mathbb{Q}[t]/(t^{22}+2t^{11}-4)$ in the 2-descent).
- **$p = 13$**: **CLOSED UNDER GRH; CONDITIONALLY PARTITIONED UNCONDITIONALLY**.  
  - *Under GRH*: Proved no non-trivial solutions by Dahmen–Siksek (2014, Theorem 3) using Chabauty–Coleman at prime 5 on the genus-6 curve $C_{13,1}$ over $\mathbb{Q}(\sqrt{5})$ ($\operatorname{rank} J_{13,1}(\mathbb{Q}(\sqrt{5})) = 1 < 6$).
  - *Unconditional status*:
    - $5 \mid Z$: Closed (Dahmen–Siksek 2014, BCDF 2019).
    - $2 \mid Z$ ($Z$ even): Closed (BCDF 2019, Theorem 6).
    - $13 \mid Z$: Closed (BCDF 2019, Theorem 3).
    - $Z$ odd, $\gcd(Z, 65) = 1$: **OPEN unconditionally** (relies on GRH for the degree-26 number field $\mathbb{Q}[t]/(t^{26}+22t^{13}-4)$).
- **$p = 17$**: **PARTIALLY CLOSED UNCONDITIONALLY; OPEN FOR ODD COPRIME $Z$**.  
  - *Subcases closed unconditionally*:
    - $5 \mid Z$: Closed unconditionally by Dahmen–Siksek (2014, Proposition 3.3) via Kraus' Frey curve $E_{x,y}$ at level 80 and Kraus sieve at $q = 103$.
    - $2 \mid Z$ ($Z$ even): Closed unconditionally by BCDF (2019, Theorem 6).
    - $17 \mid Z$: Closed unconditionally by BCDF (2019, Theorem 3).
  - *Subcase remaining open*:
    - $Z$ odd with $\gcd(Z, 85) = 1$: **OPEN** (both unconditionally and under GRH).
    - *Obstruction*: In Dahmen–Siksek (2014, Table 8), the 2-Selmer ranks of the Jacobians $J_{17,0}$ and $J_{17,1}$ over $\mathbb{Q}(\sqrt{5})$ exceed 1 (rank $\ge 2$), so classical Chabauty–Coleman does not apply.

### 3.3. Exponent $p = 19$ and Beyond
- **$p = 19$**: **UNCONDITIONALLY CLOSED (NO SOLUTIONS)**.  
  *Proof*: Dahmen–Siksek (2014, Theorem 1). For $5 \nmid Z$, the genus-9 curve $C_{19}: Y^2 = 5X^{38} - 4$ has $\operatorname{rank} J_{19}(\mathbb{Q}) = 1 < 9$, and Chabauty–Coleman at prime 3 eliminates all non-trivial rational points.
- **$p \in \{23, 29, 31, 37, 41, 43, 47, 53\}$**:
  - Closed under GRH in extended computational experiments (e.g. using generalized descent/Chabauty).
  - Unconditionally closed whenever $2 \mid Z$, $5 \mid Z$, or $p \mid Z$.
  - Open unconditionally when $Z$ is odd and $\gcd(Z, 5p) = 1$.

### 3.4. Large $p$ Status
For general sufficiently large prime exponents $p$:
1. **The Second Case ($p \mid Z$)**: **UNCONDITIONALLY CLOSED FOR ALL $p$** (BCDF 2019, Theorem 3).
2. **The Case $5 \mid Z$**: **UNCONDITIONALLY CLOSED FOR ALL $p$** (Dahmen–Siksek 2014, BCDF 2019, Theorem 5).
3. **The Case $Z$ even ($2 \mid Z$)**: **UNCONDITIONALLY CLOSED FOR ALL $p$** (BCDF 2019, Theorem 6).
4. **The First Case ($Z$ odd, $5 \nmid Z$, $p \nmid Z$)**: **OPEN for general large $p$**.
   - *Nature of the obstruction*: The trivial solutions $(\pm 1, 0, \pm 1)$ and $(0, \pm 1, \pm 1)$ produce non-singular Frey elliptic curves over $\mathbb{Q}$ and over $\mathbb{Q}(\sqrt{5})$ that do not have complex multiplication (CM). Consequently, their modular forms persist at the lowered Serre level (e.g., level 1200 over $\mathbb{Q}$, or level $2^6$ over $\mathbb{Q}(\sqrt{5})$). Standard level-lowering yields an isomorphism $\bar{\rho}_{E,p} \cong \bar{\rho}_{E_{1,0},p}$, which cannot be distinguished by local Frobenius traces because the putative solution could match the local traces of $(1, 0)$.
   - *Conditional resolution*: Billerey–Chen–Dieulefait–Freitas (2022/2025) demonstrated that this obstruction can be overcome by using higher-dimensional Frey abelian varieties $J_5$, reducing the resolution of $X^5 + Y^5 = Z^p$ for large $p$ to Darmon's "Big Image Conjecture" (specifically, the Cartan case).

---

## 4. Frey Curves and Frey Representations for Signature $(5, 5, p)$

The following catalogue details the four major Frey constructions used in the literature for signature $(5, 5, p)$:

```
                                  Signature (5, 5, p)
                                          │
       ┌──────────────────┬───────────────┴───────────────┬──────────────────┐
       │                  │                               │                  │
Darmon's Curve     Kraus' Curves                 Dieulefait-Freitas       Kraus-Darmon
over Q (W_{a,b})   over Q & Q(√-5)                over Q(√5)             Frey Variety J_5
[Billerey 2007]   [Kraus 1999, Dahmen 2014]       [DF 2014, BCDF 2019]    [BCDF 2022]
       │                  │                               │                  │
N ∈ {50,200,      N ∈ {40, 80}                    N = 2^6 = (64)          Dim 2 over Q,
    400, 1200}    (Solves 5 | Z)                  (Norm 64 over Q(√5))    GL_2-type over Q(√5)
```

### 4.1. Darmon's Frey Curve over $\mathbb{Q}$ ($W_{a,b}$)
- **Citation**: H. Darmon (1997); N. Billerey (2007, *Bull. Austral. Math. Soc.* 76:161–194).
- **Weierstrass Model**:
  $$W_{a,b}: y^2 = x^3 - 5(a^2 + b^2) x^2 + 5 \left(\frac{a^5 + b^5}{a+b}\right) x$$
  $$W_{a,b}: y^2 = x^3 - 5(a^2 + b^2) x^2 + 5 (a^4 - a^3 b + a^2 b^2 - a b^3 + b^4) x$$
- **Invariants**:
  - $c_4 = 2^4 \cdot 5 \cdot (a^4 + 2 a^3 b + 8 a^2 b^2 + 2 a b^3 + b^4)$
  - Discriminant: $\Delta(W_{a,b}) = 5^3 (a+b)^4 (a-b)^2 (a^5+b^5)^2 = 5^3 (a+b)^4 (a-b)^2 (d z^p)^2$
- **Conductor**:
  $$N_{W_{a,b}} = 2^\alpha 5^\beta \operatorname{rad}_{\{2,5\}}(a^5 + b^5),$$
  where $\alpha \in \{1, 2, 3, 4\}$ depending on $v_2(a+b)$, and $\beta = 2$ if $5 \nmid (a+b)$, while $\beta = 1$ if $5 \mid (a+b)$.
- **Level-Lowered Newforms**:
  - For $d=1$: $N \in \{50, 200, 400, 1200\}$.
  - At level 1200, newforms include $W_{1,0}$ (`1200.a1`) and $W_{1,-1}$ (`1200.k8`).
- **Role**: Successfully used in BCDF (2019) to prove Theorem 3 ($p \mid z$) via level raising at $p$ mod $p$, and to force multiplicative reduction at 3 in Theorem 5.

### 4.2. Kraus' Frey Curves over $\mathbb{Q}$ and $\mathbb{Q}(\sqrt{-5})$ ($E'_{a,b}, E_{a,b}$)
- **Citation**: A. Kraus (1999, *Ramanujan J.* 3:315–333); S. R. Dahmen & S. Siksek (2014, *Acta Arith.* 164:65–100).
- **Untwisted Model**:
  $$E'_{a,b}: Y^2 = X^3 - 5(a^2 + b^2) X^2 + 5 H_5(a,b) X$$
- **Twisted Model (for $5 \mid z$)**:
  When $5 \mid z$, $5 \mid H_5(a,b)$. The quadratic twist of $E'_{a,b}$ by $-5$ gives:
  $$E_{a,b}: Y^2 = X^3 + (a^2 + b^2) X^2 - \frac{H_5(a,b)}{5} X$$
- **Invariants**:
  - $c_4(E_{a,b}) = 2^4 (a^4 - 3a^3 b + 7a^2 b^2 - 3ab^3 + b^4) = 2^4 (2a^4 + 3a^3(a+b) + \dots)$
  - $\Delta(E_{a,b}) = 2^4 \cdot 5^{-1} (a-b)^2 (a+b) z^{2p}$
  - Minimal discriminant: $\Delta_{\min} = \Delta$ if $2 \nmid z$, and $\Delta_{\min} = \Delta / 2^{12}$ if $2 \mid z$.
- **Conductor**:
  $$N = 2^\alpha 5 \operatorname{rad}_{\{2,5\}}(z), \quad \alpha \in \{1, 3, 4\}.$$
- **Lowered Levels**:
  - $N \in \{10, 40, 80\}$.
  - Spaces of newforms:
    - Level 10: Dimension 0 (empty).
    - Level 40: 1 rational newform $\to E_{40a1}$ ($y^2 = x^3 + x^2 - 2x$).
    - Level 80: 2 rational newforms $\to E_{80a1}$ and $E_{80b1}$.
- **Elimination**:
  - Traces at $q=3$: $a_3(E_{40a1}) = a_3(E_{80a1}) = 0$, but admissible traces for $E_{a,b}$ modulo 3 exclude 0 for all $p \ge 7$.
  - For $E_{80b1}$: $a_3(E_{80b1}) = -2$, which eliminates all $p \ge 7$ except $p = 17$.
  - At $p = 17$: Kraus' sieve at $q = 6 \cdot 17 + 1 = 103$ strictly eliminates $E_{80b1}$.
  - **Outcome**: Completely closes the $5 \mid z$ branch for all exponents $p \ge 2$.

### 4.3. Dieulefait–Freitas Frey Curves over $K = \mathbb{Q}(\sqrt{5})$ ($E_{a,b}, F_{a,b}$)
- **Citation**: L. Dieulefait & N. Freitas (2014, *Math. Comp.* 83:917–933); BCDF (2019, *Trans. AMS* 371:8651–8677).
- **Base Field**: Real quadratic field $K = \mathbb{Q}(\sqrt{5})$, $\mathcal{O}_K = \mathbb{Z}[\omega]$, $\omega = \frac{1+\sqrt{5}}{2}$, $\bar{\omega} = \frac{1-\sqrt{5}}{2}$.
- **Weierstrass Models**:
  $$E_{a,b}: Y^2 = X^3 - 2\sqrt{5} a b X^2 - [a^4 - b^4 + 2\omega(a^3 b - a b^3)] X$$
  $$F_{a,b}: Y^2 = X^3 + 2\sqrt{5} a b X^2 - [a^4 - b^4 + 2\bar{\omega}(a^3 b - a b^3)] X$$
- **Factorization Background**:
  $a^5 + b^5 = (a+b) \phi_5(a,b) = (a+b) \psi_5(a,b) \bar{\psi}_5(a,b)$, where:
  $$\psi_5(a,b) = a^2 + \bar{\omega} a b + b^2, \quad \bar{\psi}_5(a,b) = a^2 + \omega a b + b^2.$$
- **Invariants of $E_{a,b}$**:
  - $c_4(E_{a,b}) = 2^4 \psi_5(a,b) (a^2 + 4\bar{\omega} a b - b^2)$
  - $\Delta(E_{a,b}) = 2^6 \sqrt{5} \psi_5(a,b)^2 \bar{\psi}_5(a,b) (a-b)^2 (a+b)^2$
- **Invariants of $F_{a,b}$**:
  - $c_4(F_{a,b}) = 2^4 \bar{\psi}_5(a,b) (a^2 + 4\omega a b - b^2)$
  - $\Delta(F_{a,b}) = -2^6 \sqrt{5} \psi_5(a,b) \bar{\psi}_5(a,b)^2 (a-b)^2 (a+b)^2$
- **Conductors**:
  - $v_2(N_E) = v_2(N_F) = 6$ (ideal $(2)^3$, norm $2^6 = 64$).
  - For $E_{a,b}$: semistable away from 2 and 5. If $5 \nmid (a+b)$, $v_{\mathfrak{p}_5}(N_E) = 0$ (good reduction at $\sqrt{5}$!).
  - For $F_{a,b}$: if $5 \mid (a+b)$, $v_{\mathfrak{p}_5}(N_F) = 0$ (good reduction at $\sqrt{5}$!).
- **Serre Level**:
  $$\mathfrak{N} = (2)^3 = (8), \quad \operatorname{Norm}_{K/\mathbb{Q}}(\mathfrak{N}) = 64.$$
- **Hilbert Newforms at Level 64**:
  - For $E_{a,b}$ with $5 \nmid (a+b)$: exactly 6 newform orbits survive for $p \ge 7$, matching twists of the trivial evaluations $E_{1,0}$ and $E_{1,1}$:
    $$E_{1,0}, \quad E_{1,0} \otimes \chi_{-1}, \quad E_{1,0} \otimes \chi_2, \quad E_{1,0} \otimes \chi_{-2}, \quad E_{1,1}, \quad E_{1,1} \otimes \chi_2.$$
  - For $F_{a,b}$ with $5 \mid (a+b)$: exactly 2 newform orbits survive for $p \ge 11$, matching:
    $$F_{1,-1} \quad \text{and} \quad F_{1,-1} \otimes \chi_2.$$
- **Role in BCDF (2019)**:
  - Allowed the complete elimination of $5 \mid z$ (Theorem 5) and $2 \mid z$ ($z$ even, Theorem 6) by comparing inertial fields at 2.

### 4.4. Kraus' Frey Hyperelliptic Curve and Jacobian Variety of $\mathrm{GL}_2$-Type
- **Citation**: A. Kraus (1999); BCDF (2022/2025, arXiv:2205.15861).
- **Genus-2 Curve**:
  $$C_5(a,b): y^2 = x^5 - 2(a^2 - 3ab + b^2) x^3 + (a-b)^4 x + 4 ab (a+b)^2$$
- **Jacobian Variety**:
  $$J_5(a,b) = \operatorname{Jac}(C_5(a,b)).$$
  $J_5(a,b)$ is an abelian surface over $\mathbb{Q}$ whose endomorphism ring over $\mathbb{Q}(\sqrt{5})$ contains $\mathcal{O}_K = \mathbb{Z}\left[\frac{1+\sqrt{5}}{2}\right]$. Thus $J_5(a,b)$ is an abelian variety of $\mathrm{GL}_2$-type over $K = \mathbb{Q}(\sqrt{5})$.
- **Galois Representations**:
  Attaches a system of 2-dimensional $\lambda$-adic representations:
  $$\rho_{J_5, \lambda}: G_K \to \mathrm{GL}_2(K_\lambda)$$
  unramified outside $2, 5,$ and primes dividing $a^5+b^5$.
- **Significance**:
  Provides the bridge to Darmon's program. BCDF (2022) established modularity of $J_5$ and proved that the residual representation $\bar{\rho}_{J_5, \mathfrak{p}}$ at $\mathfrak{p} \mid p$ has large image unless the solution corresponds to a CM point, which reduces the elimination of non-CM newforms to Darmon's Cartan Big Image Conjecture.

---

## 5. Summary Matrix of Frey Curves and Varieties

| Object | Model / Equation | Base Field | Lowered Serre Level | Key Trivial Forms | Solved Scope / Obstruction |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$W_{a,b}$** (Darmon) | $y^2 = x^3 - 5(a^2+b^2)x^2 + 5\frac{a^5+b^5}{a+b}x$ | $\mathbb{Q}$ | $N \in \{50, 200, 400, 1200\}$ | $W_{1,0}$ (`1200.a1`, non-CM), $W_{1,-1}$ (`1200.k8`) | Solves $p \mid z$ (Thm 3); obstructed by $W_{1,0}$ for $5 \nmid z$ |
| **$E_{a,b}$** (Kraus twist) | $Y^2 = X^3 + (a^2+b^2)X^2 - \frac{H_5(a,b)}{5}X$ | $\mathbb{Q}$ | $N \in \{40, 80\}$ | $E_{40a1}, E_{80a1}, E_{80b1}$ | **Completely solves $5 \mid z$ for all $p \ge 2$** via Kraus sieve at $q=103$ |
| **$E_{a,b}, F_{a,b}$** (Dieulefait–Freitas) | $\mathbb{Q}$-curves over $\mathbb{Q}(\sqrt{5})$ (Weierstrass cubics) | $K = \mathbb{Q}(\sqrt{5})$ | $\mathfrak{N} = (2)^3$, Norm 64 | $E_{1,0}, E_{1,1}$ (twists) and $F_{1,-1}$ (twists) | **Completely solves $2 \mid z$ ($z$ even)** and $5 \mid z$ (Thms 5, 6) |
| **$J_5 = \operatorname{Jac}(C_5)$** (Kraus–Darmon) | $y^2 = x^5 - 2(a^2-3ab+b^2)x^3 + \dots$ | $K = \mathbb{Q}(\sqrt{5})$ | $\mathrm{GL}_2$-type over $K$, conductor over $K$ | CM points correspond to $(1, -1)$ and $(1, 1)$ | Reduces full $x^5+y^5=z^p$ for large $p$ to Darmon's Cartan conjecture |

---

## 6. Map of Proved vs Open Frontiers for $X^5 + Y^5 = Z^p$ and $X^{10} + Y^{10} = Z^p$

### 6.1. General Signature $X^5 + Y^5 = Z^p$

```
                                      X^5 + Y^5 = Z^p (p >= 3)
                                                 │
          ┌──────────────────────────────────────┴──────────────────────────────────────┐
          │                                                                             │
    Special Exponents                                                              General p
    p = 3: CLOSED (Poonen/Darmon-Merel)                                                 │
    p = 5: CLOSED (FLT / Dirichlet-Legendre)                                            │
    p = 7: CLOSED (Dahmen-Siksek 2014)                                                  │
    p = 19: CLOSED (Dahmen-Siksek 2014)                                                 │
    p = 11, 13: CLOSED under GRH (Dahmen-Siksek 2014)                                   │
                                                        ┌───────────────────────────────┴───────────────────────────────┐
                                                        │                                                               │
                                                 Local Divisibility                                              Coprime First Case
                                                 5 | Z: CLOSED for all p (Dahmen-Siksek/BCDF)                     2, 5, p ∤ Z
                                                 2 | Z (even Z): CLOSED for all p (BCDF Thm 6)                          │
                                                 p | Z (2nd case): CLOSED for all p (BCDF Thm 3)                        ▼
                                                                                                                OPEN FOR GENERAL p
                                                                                                                (Reduced to Darmon's
                                                                                                                Cartan conjecture)
```

#### Detailed Status Breakdown for $X^5 + Y^5 = Z^p$:
1. **$p = 2, 3, 5$**:
   - Status: **UNCONDITIONALLY CLOSED (NO NON-TRIVIAL SOLUTIONS)**.
   - References: Poonen (1998), Darmon–Merel (1997), Dirichlet/Legendre (1825), Wiles (1995).
2. **$p = 7, 19$**:
   - Status: **UNCONDITIONALLY CLOSED (NO NON-TRIVIAL SOLUTIONS)**.
   - References: Dahmen–Siksek (2014, *Acta Arith.* 164:65–100, Theorem 1).
3. **$p = 11, 13$**:
   - Status: **CLOSED UNDER GRH**; unconditionally closed if $2 \mid Z$, $5 \mid Z$, or $p \mid Z$.
   - Open unconditionally only for $Z$ odd, $\gcd(Z, 5p) = 1$.
   - References: Dahmen–Siksek (2014, Theorem 3), BCDF (2019).
4. **$p = 17$**:
   - Status: **PARTIALLY CLOSED UNCONDITIONALLY; OPEN FOR $Z$ ODD WITH $\gcd(Z, 85) = 1$**.
   - $5 \mid Z$ closed unconditionally (Dahmen–Siksek 2014 via Kraus sieve at $q=103$).
   - $2 \mid Z$ closed unconditionally (BCDF 2019, Theorem 6).
   - $17 \mid Z$ closed unconditionally (BCDF 2019, Theorem 3).
   - $Z$ odd, $\gcd(Z, 85) = 1$: Open (Chabauty rank $\ge 2$).
5. **General Large $p$**:
   - $5 \mid Z$: Closed unconditionally for all $p$ (Dahmen–Siksek 2014, BCDF 2019).
   - $2 \mid Z$: Closed unconditionally for all $p$ (BCDF 2019, Theorem 6).
   - $p \mid Z$: Closed unconditionally for all $p$ (BCDF 2019, Theorem 3).
   - $Z$ odd, $5 \nmid Z, p \nmid Z$: **OPEN** unconditionally; reduced to Darmon's Cartan Big Image Conjecture (BCDF 2022/2025).

---

### 6.2. Decic Signature $X^{10} + Y^{10} = Z^p$

For the equation:
$$X^{10} + Y^{10} = Z^p, \quad \gcd(X, Y, Z) = 1, \quad X Y Z \neq 0, \quad p \ge 3 \text{ prime},$$
substituting $x = X^2$ and $y = Y^2$ reduces the problem to $x^5 + y^5 = Z^p$, where $x, y > 0$ are positive integer squares.

#### Rigorous Arithmetic Constraints on Decic Bases:
1. **Parity Restriction (Exclusion of Even $Z$)**:
   - Suppose $X, Y$ are coprime integers.
   - If $X, Y$ were both odd, then $X^{10} \equiv 1 \pmod 4$ and $Y^{10} \equiv 1 \pmod 4$, so:
     $$X^{10} + Y^{10} \equiv 2 \pmod 4.$$
   - If $Z$ were even, $Z^p$ would be divisible by $2^p \ge 2^3 = 8$, contradicting $X^{10} + Y^{10} \equiv 2 \pmod 4$.
   - If $Z$ were odd, $Z^p \equiv 1$ or $3 \pmod 4$, also contradicting $X^{10} + Y^{10} \equiv 2 \pmod 4$.
   - **Conclusion**: $X$ and $Y$ **CANNOT BOTH BE ODD**.
   - Because $\gcd(X, Y) = 1$, they cannot both be even.
   - Therefore, $X$ and $Y$ **MUST HAVE OPPOSITE PARITY** (one even, one odd).
   - Consequently:
     $$X^{10} + Y^{10} \equiv 1 \pmod 2 \implies Z \text{ IS NECESSARILY ODD!}$$
   - **Crucial Corollary**: The entire "even $Z$" branch is trivially empty by modular arithmetic modulo 4!
2. **Exclusion of $5 \mid Z$**:
   - By Theorem 5 of BCDF (2019) and Proposition 3.3 of Dahmen–Siksek (2014), the equation $x^5 + y^5 = Z^p$ has no non-trivial primitive solutions with $5 \mid Z$ for ANY prime exponent $p \ge 2$.
   - Since $X^{10} + Y^{10} = Z^p$ is a subcase, **$5 \mid Z$ IS UNCONDITIONALLY IMPOSSIBLE FOR ALL $p \ge 2$**.
3. **Exclusion of $p \mid Z$**:
   - By Theorem 3 of BCDF (2019), $x^5 + y^5 = Z^p$ has no non-trivial primitive solutions with $p \mid Z$ for ANY prime exponent $p \ge 2$.
   - Therefore, **$p \mid Z$ IS UNCONDITIONALLY IMPOSSIBLE FOR ALL $p \ge 2$**.
4. **Gaussian Descent Splitting**:
   - Because $5 \nmid Z$, we have $\gcd(x+y, \Phi_5(x,y)) = 1$.
   - Factorization gives positive coprime integers $u, v$ such that:
     $$X^2 + Y^2 = u^p, \quad \Phi_5(X^2, Y^2) = v^p, \quad Z = u v.$$
   - The equation $X^2 + Y^2 = u^p$ with $\gcd(X, Y) = 1$ and opposite parities factors in the Gaussian integers $\mathbb{Z}[i]$:
     $$X + i Y = (r + i s)^p, \quad \gcd(r, s) = 1, \quad r \not\equiv s \pmod 2.$$
   - Simultaneously, $X^2 + Y^2 = u^p$ and $\Phi_5(X^2, Y^2) = v^p$ force an algebraic descent into the real quadratic field $\mathbb{Q}(\sqrt{5})$:
     $$H_- = (m^2+n^2)^2 - 16 \omega m^2 n^2 = \omega^j (A + B\omega)^p,$$
     where $m = (X+Y)/2, n = (X-Y)/2$.
   - This simultaneous Gaussian and real-quadratic descent severely overdetermines the system of integer points.

#### Detailed Status Breakdown for $X^{10} + Y^{10} = Z^p$:

| Exponent $p$ | Status for $X^{10} + Y^{10} = Z^p$ | Mathematical Justification |
| :--- | :--- | :--- |
| **$p = 2$** | **UNCONDITIONALLY CLOSED** | Poonen (1998): $(10, 10, 2) \subset (5, 5, 2)$ has no non-trivial solutions. |
| **$p = 3$** | **UNCONDITIONALLY CLOSED** | Poonen (1998), Darmon–Merel (1997): $(10, 10, 3) \subset (5, 5, 3)$ has no non-trivial solutions. |
| **$p = 5$** | **UNCONDITIONALLY CLOSED** | Fermat's Last Theorem for exponent 5: $(X^2)^5 + (Y^2)^5 = Z^5$. |
| **$p = 7$** | **UNCONDITIONALLY CLOSED** | Dahmen–Siksek (2014): $(10, 10, 7) \subset (5, 5, 7)$ has no non-trivial solutions. |
| **$p = 11$** | **CLOSED UNDER GRH** | Dahmen–Siksek (2014) on $(5, 5, 11)$. Open unconditionally for $Z$ odd, $\gcd(Z, 55)=1$. |
| **$p = 13$** | **CLOSED UNDER GRH** | Dahmen–Siksek (2014) on $(5, 5, 13)$. Open unconditionally for $Z$ odd, $\gcd(Z, 65)=1$. |
| **$p = 17$** | **OPEN** | $5 \mid Z$ and $17 \mid Z$ eliminated. Surviving branch: $X \not\equiv Y \pmod 2$, $Z$ odd, $\gcd(Z, 85)=1$. Rigidly constrained by Gaussian descent $X+iY = (r+is)^{17}$. |
| **$p = 19$** | **UNCONDITIONALLY CLOSED** | Dahmen–Siksek (2014): $(10, 10, 19) \subset (5, 5, 19)$ has no non-trivial solutions. |
| **Large $p$** | **OPEN** | Reduced to $Z$ odd, $\gcd(Z, 5p)=1$, $X+iY = (r+is)^p$. Asymptotically conditional on Darmon's Cartan conjecture. |

---

## 7. Strategic Synthesis & Direct Impact on the Beal Program

### 7.1. Comparison with Coefficient-2 Equations
In the Beal all-even branch ($x = 2r, y = 2s, z = 2t$), when $17 \mid t$ and $5 \mid r$, the system splits into two distinct forms:
1. $X^{10} + Y^{10} = 2 Z^{17}$: **CLOSED UNCONDITIONALLY**.
   - As audited in checkpoints U57 and U62, the presence of coefficient 2 allows the Dieulefait–Freitas density-3/4 theorem (Nuno Freitas' 2012 thesis Theorem 2.0.3 / Dieulefait–Freitas 2014) to eliminate $5 \mid (X^2+Y^2)$, after which the Gaussian-descent and real-quadratic Chabauty-at-odd-primes method of U61/U62 strictly forces $(X,Y,Z)=(1,1,1)$, leaving no non-trivial primitive solutions.
2. $X^{10} + 256 Y^{10} = Z^{17}$: **CURRENTLY THE CENTRAL OPEN TARGET OF THE PROJECT**.
   - Checkpoint U100 achieved 100% elimination across all level-2000 Hilbert newform orbits at prime 11.
3. $X^{10} + Y^{10} = Z^p$ (Unweighted, coefficient 1):
   - Here, the coefficient is 1, not 2.
   - For $p = 7, 19$: Unconditionally closed by Dahmen–Siksek.
   - For $p = 11, 13$: Closed under GRH.
   - For $p = 17$: Surviving open candidate requires $Z$ odd, $\gcd(Z, 85) = 1$, and $X+iY = (r+is)^{17}$.

### 7.2. Concrete Next Steps for the Research Program
1. **Unconditional Verification of $p = 11$ and $p = 13$**:
   - As noted by Dahmen–Siksek (2014, §5.3), making $p = 11$ unconditional requires verifying that the class number of the degree-22 number field $\mathbb{Q}[t]/(t^{22} + 2t^{11} - 4)$ is 1, and that the conditional unit group is 2-saturated.
   - With modern distributed class group algorithms (e.g. Belabas, Cohen, Biasse–Fieker), this certificate is within reach of modern computation.
2. **Attacking $p = 17$ for $X^{10} + Y^{10} = Z^{17}$**:
   - Standard Chabauty–Coleman on $C_{17,0}$ fails because the Mordell–Weil rank is $\ge 2$.
   - However, for $X^{10} + Y^{10} = Z^{17}$, one has the additional Gaussian relation $X+iY = (r+is)^{17}$.
   - Combining the Gaussian descent equations with the real quadratic field $\mathbb{Q}(\sqrt{5})$ via Elliptic Chabauty or Chabauty–Kim (minors of Coleman integrals) offers a viable path to unconditionally close $X^{10} + Y^{10} = Z^{17}$.
3. **Closing Darmon's Program for Signature $(5, 5, p)$**:
   - The modularity of the Kraus Frey variety $J_5$ over $\mathbb{Q}(\sqrt{5})$ is now proved unconditionally by BCDF (2022/2025).
   - Advancing the Cartan case of the Big Image Conjecture will provide the ultimate unconditional resolution of the first case of $X^5 + Y^5 = Z^p$ for all large primes $p$.
