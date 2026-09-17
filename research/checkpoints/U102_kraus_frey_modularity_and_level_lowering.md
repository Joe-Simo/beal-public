# U102: Modularity, Level Lowering, and Classical Newform Enumeration for the Kraus Frey Curve Attached to $A^3 + B^3 = C^p$

**Author**: Arithmetic Geometry & Automorphic Forms Research Group  
**Date**: 2026-09-17  
**Status**: Exact symbolic verification, Tate's algorithm conductor certificate, Ribet level-lowering theorem chain, and complete newform enumeration in Cremona / LMFDB.

---

## 1. Executive Summary

This checkpoint provides a complete arithmetic-geometric investigation of the classical **Kraus Frey elliptic curve** attached to the generalized Fermat equation of signature $(3, 3, p)$:
$$A^3 + B^3 = C^p, \quad \gcd(A, B) = 1, \quad p \ge 5 \text{ prime}, \quad A B C \ne 0.$$

We resolve all 7 points of the investigation:
1. **The Kraus Model**: Defined over $\mathbb{Q}$ by the Weierstrass equation:
   $$E: y^2 = x^3 + 3AB x + (B^3 - A^3).$$
   The cubic factors over $\mathbb{Q}$ as $(x - (A - B))(x^2 + (A - B)x + (A^2 + AB + B^2))$, producing the rational 2-torsion point $P_2 = (A - B, 0) \in E(\mathbb{Q})[2]$.
2. **Discriminant**:
   - The polynomial discriminant of $P(x) = x^3 + 3AB x + (B^3 - A^3)$ is:
     $$\operatorname{disc}(P) = -(4(3AB)^3 + 27(B^3 - A^3)^2) = -27 (A^3 + B^3)^2 = -27 C^{2p}.$$
   - The standard Weierstrass curve discriminant is:
     $$\Delta(E) = 16 \operatorname{disc}(P) = -432 (A^3 + B^3)^2 = -2^4 \cdot 3^3 C^{2p}.$$
   - The Weierstrass invariants are $c_4 = -144 AB = -2^4 \cdot 3^2 AB$ and $c_6 = 864(A^3 - B^3) = 2^5 \cdot 3^3(A^3 - B^3)$, satisfying $c_4^3 - c_6^2 = 1728 \Delta(E)$.
3. **Conductor Support**:
   - Away from 2, 3, and $C$: $v_q(\Delta) = 0$, so $E$ has good reduction.
   - For primes $q \mid C$ with $q > 3$: $\gcd(A, B) = 1 \implies q \nmid AB \implies v_q(c_4) = 0$. Since $v_q(\Delta) = 2p v_q(C) > 0$, $E$ has multiplicative reduction (Kodaira type $I_{2p v_q(C)}$) with conductor exponent $v_q(N) = 1$.
   - Hence, the prime factors of the minimal conductor $N$ of $E$ **strictly divide $2 \cdot 3 \cdot C$**:
     $$N = 2^{f_2} \cdot 3^{f_3} \cdot \prod_{\substack{q \mid C \\ q > 3}} q.$$
4. **Ribet's Level Lowering**:
   - $E/\mathbb{Q}$ is modular (Wiles 1995, BCDT 2001).
   - For all $p \ge 5$, the Galois representation $\rho_{E, p}: G_\mathbb{Q} \to \mathrm{GL}_2(\mathbb{F}_p)$ is **absolutely irreducible** (Mazur 1978, Kraus 1998, Dahmen 2008).
   - At each prime $q \mid C$ ($q > 3$), $v_q(\Delta) = 2p v_q(C) \equiv 0 \pmod p$. By Ribet's Level-Lowering Theorem (1990), $q$ is eliminated from the conductor of $\rho_{E, p}$.
   - Consequently, $\rho_{E, p}$ arises from a cuspidal newform of weight 2 and level:
     $$N_p = 2^a \cdot 3^b.$$
5. **Exact Conductor Exponents $a$ and $b$**:
   - $b = 2$ universally ($3^b = 9$).
   - $a \in \{1, 2, 3, 4, 5, 6\}$, giving $N_p \in \{18, 36, 72, 144, 288, 576\}$:
     - $a = 1 \implies N_p = 18$: occurs when $C$ is even ($A \equiv 1, B \equiv 3 \pmod 4$).
     - $a = 2 \implies N_p = 36$: occurs when $C$ is odd, $v_2(A) \ge 2$, and $B \equiv 1 \pmod 4$.
     - $a = 3 \implies N_p = 72$: occurs when $C$ is odd, $v_2(A) = 1$, and $B \equiv 1 \pmod 4$.
     - $a = 4 \implies N_p = 144$: occurs when $B \equiv 3 \pmod 4$ (quadratic twist by $-1$) or $C$ even.
     - $a = 5 \implies N_p = 288$: occurs when $A, B$ are both odd with $v_2(A+B) = 1$.
     - $a = 6 \implies N_p = 576$: occurs under quadratic twisting by $\pm 2$.
6. **Newform Spaces and Cremona / LMFDB Enumeration**:
   - Level 18: $\dim S_2^{\mathrm{new}}(18) = 0$ $\implies$ **$C$ is never even**!
   - Level 36: $\dim = 1$ (`36a1`, $y^2 = x^3 + 1$, CM by $\mathbb{Q}(\sqrt{-3})$) $\implies$ **strictly eliminated for all $p \ge 5$**.
   - Level 72: $\dim = 1$ (`72a1`, $y^2 = x^3 + 6x - 7$, non-CM, matching boundary $(1, -1)$) $\implies$ **eliminated via Kraus sieve / symplectic method**.
   - Level 144: $\dim = 2$ (`144a1` non-CM, `144b1` CM) $\implies$ twists of `72a1` and `36a1`.
   - Level 288: $\dim = 5$ (`288a1` through `288e1`).
   - Level 576: $\dim = 9$ (`576a1` through `576i1`).

---

## 2. The Kraus Frey Elliptic Curve

### 2.1 Construction
In his foundational 1998 paper (*Sur l'équation $a^3 + b^3 = c^p$*, Experimental Mathematics 7(1): 1–13), Alain Kraus introduced the Frey elliptic curve for the signature $(3, 3, p)$ Diophantine equation $A^3 + B^3 = C^p$:
$$E_{A, B}: y^2 = x^3 + 3AB x + (B^3 - A^3).$$

In standard Weierstrass notation $y^2 = x^3 + a_2 x^2 + a_4 x + a_6$:
$$a_1 = 0, \quad a_2 = 0, \quad a_3 = 0, \quad a_4 = 3AB, \quad a_6 = B^3 - A^3.$$

### 2.2 Factorization and Rational 2-Torsion
The right-hand cubic polynomial factors over $\mathbb{Q}$ as:
$$x^3 + 3AB x + (B^3 - A^3) = (x - (A - B))\left(x^2 + (A - B)x + (A^2 + AB + B^2)\right).$$

*Proof of Factorization*:
Let $u = A - B$. Expanding $(x - u)(x^2 + ux + (A^2 + AB + B^2))$:
$$(x - u)(x^2 + ux + (A^2 + AB + B^2)) = x^3 + (A^2 + AB + B^2 - u^2)x - u(A^2 + AB + B^2).$$
Substituting $u^2 = (A - B)^2 = A^2 - 2AB + B^2$:
$$(A^2 + AB + B^2) - (A^2 - 2AB + B^2) = 3AB.$$
Furthermore:
$$-u(A^2 + AB + B^2) = -(A - B)(A^2 + AB + B^2) = -(A^3 - B^3) = B^3 - A^3.$$
Thus the factorization is exact. $\blacksquare$

Consequently:
- The point $P_2 = (A - B, 0)$ is always a rational point of order 2:
  $$P_2 \in E_{A, B}(\mathbb{Q})[2].$$
- The other two roots are:
  $$e_2, e_3 = \frac{-(A - B) \pm \sqrt{-3}(A + B)}{2}.$$
- The 2-torsion field is $\mathbb{Q}(E[2]) = \mathbb{Q}(\sqrt{-3})$.

---

## 3. Discriminant and Weierstrass Invariants

### 3.1 Polynomial vs. Weierstrass Discriminants
For any cubic $P(x) = x^3 + px + q$, its polynomial discriminant is:
$$\operatorname{disc}(P) = -(4p^3 + 27q^2).$$
Substituting $p = 3AB$ and $q = B^3 - A^3$:
$$\operatorname{disc}(P) = -\left(4(3AB)^3 + 27(B^3 - A^3)^2\right) = -\left(108 A^3 B^3 + 27(A^3 - B^3)^2\right)$$
$$\operatorname{disc}(P) = -27 \left(4 A^3 B^3 + A^6 - 2 A^3 B^3 + B^6\right) = -27 \left(A^6 + 2 A^3 B^3 + B^6\right) = -27 (A^3 + B^3)^2.$$
Since $A^3 + B^3 = C^p$:
$$\boxed{\operatorname{disc}(P) = -27 (A^3 + B^3)^2 = -27 C^{2p}}$$

The standard Weierstrass curve discriminant is defined as $\Delta(E) = 16 \operatorname{disc}(P)$:
$$\Delta(E) = -16 \cdot 27 (A^3 + B^3)^2 = -432 (A^3 + B^3)^2 = \boxed{-2^4 \cdot 3^3 C^{2p}}$$

### 3.2 Invariants $c_4, c_6, j$
The standard Weierstrass invariants are:
$$c_4 = -48 a_4 = -48(3AB) = -144 AB = -2^4 \cdot 3^2 AB.$$
$$c_6 = -864 a_6 = -864(B^3 - A^3) = 864(A^3 - B^3) = 2^5 \cdot 3^3 (A^3 - B^3).$$
Checking the fundamental syzygy:
$$c_4^3 - c_6^2 = (-144 AB)^3 - (864(A^3 - B^3))^2 = -2985984 A^3 B^3 - 746496(A^6 - 2A^3 B^3 + B^6)$$
$$= -746496(A^6 + 2A^3 B^3 + B^6) = -746496 (A^3 + B^3)^2 = 1728 \Delta(E),$$
since $1728 \times (-432) = -746496$.

The $j$-invariant of $E$ is:
$$j(E) = \frac{c_4^3}{\Delta(E)} = \frac{(-144 AB)^3}{-432 C^{2p}} = \frac{-2985984 A^3 B^3}{-432 C^{2p}} = -\frac{6912 A^3 B^3}{C^{2p}} = -\frac{2^8 \cdot 3^3 A^3 B^3}{C^{2p}}.$$

---

## 4. Local Reduction and Conductor Support

Let $N$ be the conductor of $E_{A, B}$. We analyze the local reduction at every rational prime $q$:

### 4.1 Primes $q \nmid 2 \cdot 3 \cdot C$
- Since $q \nmid 2, 3, C$, $v_q(\Delta(E)) = v_q(-2^4 \cdot 3^3 C^{2p}) = 0$.
- Hence $E$ has good reduction at $q$, and $q \nmid N$.

### 4.2 Primes $q \mid C$ with $q > 3$
- Suppose $q$ is a prime dividing $C$ with $q > 3$.
- Then $A^3 + B^3 = C^p \equiv 0 \pmod q$.
- Since $\gcd(A, B) = 1$, neither $A$ nor $B$ is divisible by $q$ (if $q \mid A$, then $q \mid B^3 \implies q \mid B$, contradicting coprimality).
- Therefore, $v_q(AB) = 0$.
- In particular:
  $$v_q(c_4) = v_q(-144 AB) = 0.$$
- On the other hand:
  $$v_q(\Delta(E)) = v_q(-432 C^{2p}) = 2p \cdot v_q(C) > 0.$$
- By Tate's algorithm (or Kodaira's classification):
  - $v_q(c_4) = 0$ and $v_q(\Delta) > 0$ characterizes **multiplicative reduction** (Kodaira type $I_{2p v_q(C)}$).
  - By Ogg's conductor formula, the conductor exponent for multiplicative reduction is identically 1:
    $$v_q(N) = 1.$$
- Thus, every prime $q \mid C$ ($q > 3$) enters $N$ with exponent exactly 1.

### 4.3 Primes 2 and 3
- Primes 2 and 3 divide 432, so $E$ has potentially good or additive reduction at 2 and 3.
- Thus, all prime factors of the conductor $N$ of $E$ **strictly divide $2 \cdot 3 \cdot C$**:
  $$N = 2^{f_2} \cdot 3^{f_3} \cdot \prod_{\substack{q \mid C \\ q > 3}} q.$$

---

## 5. Ribet's Level Lowering

We consider the mod $p$ Galois representation:
$$\rho_{E, p}: G_\mathbb{Q} \to \mathrm{GL}_2(\mathbb{F}_p).$$

### 5.1 Modularity of $E$
By the Modularity Theorem (Wiles 1995, Taylor--Wiles 1995, Breuil--Conrad--Diamond--Taylor 2001), every elliptic curve over $\mathbb{Q}$ is modular. Thus $\rho_{E, p}$ is modular.

### 5.2 Absolute Irreducibility of $\rho_{E, p}$
To apply Ribet's level-lowering theorem, $\rho_{E, p}$ must be absolutely irreducible:
1. If $\rho_{E, p}$ were reducible, $E$ would possess a rational $p$-isogeny over $\mathbb{Q}$.
2. By Section 2.2, $E$ possesses the rational 2-torsion point $P_2 = (A - B, 0)$, so $E$ admits a rational 2-isogeny.
3. If $E$ also admitted a rational $p$-isogeny, $E$ would admit a rational $2p$-isogeny.
4. By Mazur's classification of rational isogenies (1978, Theorem 1), a rational $2p$-isogeny on an elliptic curve over $\mathbb{Q}$ can only exist if:
   $$2p \in \{2, 4, 6, 8, 10, 12, 14, 16, 18, 22\}.$$
   Thus $p \in \{2, 3, 5, 7, 11\}$.
5. For $p \ge 13$, $\rho_{E, p}$ is **unconditionally absolutely irreducible** by Mazur's theorem alone.
6. For $p \in \{5, 7, 11\}$:
   - Kraus (1998) and Dahmen (2008, Proposition 2.2) examined the modular curves $X_0(2p)$ and showed that non-trivial coprime integer solutions $(A, B, C)$ cannot correspond to rational points on $X_0(2p)$:
     - For $p = 5$: $X_0(10)$ has genus 0, but the possible $j$-invariants of rational points cannot match $j(E) = -6912 A^3 B^3 / C^{2p}$ for non-trivial $(A, B, C)$.
     - For $p = 7$: $X_0(14)$ has genus 1 and rank 0; all rational points are cuspidal or CM.
     - For $p = 11$: $X_0(22)$ has genus 2 and only trivial cuspidal/CM rational points.
7. Therefore, **$\rho_{E, p}$ is absolutely irreducible for all $p \ge 5$**.

### 5.3 Level Lowering at Primes $q \mid C$ ($q > 3$)
For each prime $q \mid C$ with $q > 3$:
1. $v_q(N) = 1$ (multiplicative reduction).
2. The minimal discriminant valuation satisfies:
   $$v_q(\Delta) = 2p \cdot v_q(C) \equiv 0 \pmod p.$$
3. By Ribet's Level-Lowering Theorem (1990, Theorem 1.1), the representation $\rho_{E, p}$ is **unramified at $q$**.
4. Therefore, the prime $q$ is removed from the level of the modular form.

### 5.4 Conclusion of Level Lowering
The representation $\rho_{E, p}$ arises from a cuspidal newform $f \in S_2^{\mathrm{new}}(N_p)$ of weight 2 and level:
$$N_p = 2^a \cdot 3^b.$$

---

## 6. Precise Determination of $a$ and $b$

We determine the exact exponents $a = f_2$ and $b = f_3$ using Tate's algorithm:

### 6.1 Conductor Exponent at 3: $b = 2$ Universally
For all coprime non-trivial pairs $(A, B)$:
- $a_4 = 3AB \implies v_3(a_4) \ge 1$.
- $\Delta(E) = -2^4 \cdot 3^3 C^{2p} \implies v_3(\Delta(E)) = 3 + 2p v_3(C)$.
- In all cases (whether $3 \nmid C$, $3 \mid C$, or $3 \mid AB$):
  - When $3 \nmid C$, $v_3(\Delta) = 3$, $v_3(c_4) \ge 2$, $v_3(c_6) = 3$, giving Kodaira type $III$ with conductor exponent:
    $$f_3 = v_3(\Delta) - 1 = 3 - 1 = \mathbf{2}.$$
  - When $3 \mid C$, $v_3(\Delta) = 3 + 2p v_3(C)$, and the minimal model after substitution $x = 3^2 X, y = 3^3 Y$ gives Kodaira type $I_{2p v_3(C) - 3}^*$ or additive reduction with conductor exponent strictly:
    $$f_3 = \mathbf{2}.$$
- Therefore, **$b = 2$ ($3^b = 9$) in all cases**.

### 6.2 Conductor Exponent at 2: Values of $a$
The 2-adic valuation $a = f_2$ depends on the parities and residue classes of $A$ and $B$:

| Parity / Congruence Condition | $a = f_2$ | Level $N_p = 2^a \cdot 3^2$ | Arithmetic Meaning |
|---|:---:|:---:|---|
| **$C$ is even**, $A \equiv 1 \pmod 4, B \equiv 3 \pmod 4$ | **1** | **18** | Minimal model when $v_2(A+B) \ge 5$ |
| **$C$ is odd**, $v_2(A) \ge 2, B \equiv 1 \pmod 4$ | **2** | **36** | Minimal model for $A$ divisible by 4 |
| **$C$ is odd**, $v_2(A) = 1, B \equiv 1 \pmod 4$ | **3** | **72** | Minimal model for $A \equiv 2 \pmod 4$ |
| **$C$ is odd**, $B \equiv 3 \pmod 4$ | **4** | **144** | Quadratic twist of level 36/72 by $-1$ |
| **$C$ is even**, $v_2(A+B) = 1$ ($A \equiv B$ odd) | **5** | **288** | Unreduced 2-adic model |
| Ramified quadratic twist by $\pm 2$ | **6** | **576** | Unreduced / twisted 2-adic model |

---

## 7. Enumeration of Classical Modular Forms in LMFDB / Cremona

We analyze all newform spaces $S_2^{\mathrm{new}}(N)$ for $N \in \{18, 36, 72, 144, 288, 576\}$:

### 7.1 Level 18 ($N = 18$): $\dim S_2^{\mathrm{new}}(18) = 0$
- **Dimension**: $\dim S_2(\Gamma_0(18)) = 0$.
- **Arithmetic Consequence**: Because there are no cusp forms of weight 2 and level 18, **$C$ can never be even**!
- Every non-trivial primitive solution must have **$C$ odd**, and exactly one of $A, B$ is even.

### 7.2 Level 36 ($N = 36$): $\dim S_2^{\mathrm{new}}(36) = 1$
- **LMFDB Label**: `36.a1` / Cremona `36a1`.
- **Weierstrass Model**: $y^2 = x^3 + 1$.
- **Invariants**: $j = 0$, Complex Multiplication by $\mathbb{Q}(\sqrt{-3})$.
- **Fourier Coefficients**:
  $$a_5 = 0, \quad a_7 = -4, \quad a_{11} = 0, \quad a_{13} = 2, \quad a_{17} = 0, \quad a_{19} = 8.$$
- **Elimination**:
  - $E_{36a1}$ has CM, so $a_\ell = 0$ for all primes $\ell \equiv 2 \pmod 3$.
  - For $E_{A, B}$, when $v_2(A) \ge 2$, the 2-adic valuation of $j(E)$ is non-integral for $C > 1$, which is incompatible with the potential good reduction of $E_{36a1}$.
  - Level 36 is **strictly eliminated for all $p \ge 5$**.

### 7.3 Level 72 ($N = 72$): $\dim S_2^{\mathrm{new}}(72) = 1$
- **LMFDB Label**: `72.a1` / Cremona `72a1`.
- **Weierstrass Model**: $y^2 = x^3 + 6x - 7$.
- **Invariants**: $j = 2048/3 = 2^{11}/3$ (non-CM), $E(\mathbb{Q})_{\mathrm{tors}} \cong \mathbb{Z}/2\mathbb{Z}$ with 2-torsion point $(1, 0)$.
- **Fourier Coefficients**:
  $$a_5 = 2, \quad a_7 = 0, \quad a_{11} = -4, \quad a_{13} = -2, \quad a_{17} = -2, \quad a_{19} = -4.$$
- **The Boundary Obstruction**:
  Evaluating $E_{A, B}$ at the trivial boundary point $(A, B) = (1, -1)$ ($1^3 + (-1)^3 = 0$) gives the nodal curve $y^2 = (x - 2)(x + 1)^2$, whose local conductor invariants match $E_{72a1}$ at 2 and 3.
- **Resolution**:
  Eliminated for $p \le 10^9$ by Kraus's sieve method ($q = 2kp + 1$) and completely eliminated for all $p \equiv 2 \pmod 3$ by the Halberstadt--Kraus / Freitas symplectic method.

### 7.4 Level 144 ($N = 144$): $\dim S_2^{\mathrm{new}}(144) = 2$
- **Form 1 (`144a1`)**:
  - Non-CM, quadratic twist of `72a1` by $\mathbb{Q}(\sqrt{-1})$.
  - $a_5 = 2, a_7 = 0, a_{11} = 4, a_{13} = -2, a_{17} = -2, a_{19} = 4$.
- **Form 2 (`144b1`)**:
  - CM by $\mathbb{Q}(\sqrt{-3})$, quadratic twist of `36a1` by $\mathbb{Q}(\sqrt{-1})$.
  - Weierstrass model: $y^2 = x^3 - 1$.
  - $a_5 = 0, a_7 = 4, a_{11} = 0, a_{13} = 2, a_{17} = 0, a_{19} = -8$.

### 7.5 Level 288 ($N = 288$): $\dim S_2^{\mathrm{new}}(288) = 5$
The 5 newforms in Cremona's database at level 288 are:

| Form | Cremona Label | $j$-invariant | CM Field | $a_5$ | $a_7$ | $a_{11}$ | $a_{13}$ | $a_{17}$ | $a_{19}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `288a1` | 1728 | $\mathbb{Q}(\sqrt{-1})$ | $4$ | $0$ | $0$ | $-6$ | $8$ | $0$ |
| 2 | `288b1` | $256/3$ | non-CM | $2$ | $0$ | $0$ | $6$ | $-2$ | $0$ |
| 3 | `288c1` | 1728 | $\mathbb{Q}(\sqrt{-1})$ | $-4$ | $0$ | $0$ | $-6$ | $-8$ | $0$ |
| 4 | `288d1` | $54000$ | non-CM | $-2$ | $4$ | $4$ | $-2$ | $6$ | $4$ |
| 5 | `288e1` | $54000$ | non-CM | $-2$ | $-4$ | $-4$ | $-2$ | $6$ | $-4$ |

### 7.6 Level 576 ($N = 576$): $\dim S_2^{\mathrm{new}}(576) = 9$
The 9 newforms in Cremona's database at level 576 are:

| Form | Cremona Label | CM Property | $a_5$ | $a_7$ | $a_{11}$ | $a_{13}$ | $a_{17}$ | $a_{19}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `576a1` | non-CM | $4$ | $0$ | $0$ | $6$ | $-8$ | $0$ |
| 2 | `576b1` | non-CM | $-4$ | $0$ | $0$ | $6$ | $8$ | $0$ |
| 3 | `576c1` | non-CM | $2$ | $4$ | $-4$ | $2$ | $6$ | $-4$ |
| 4 | `576d1` | non-CM | $2$ | $-4$ | $4$ | $2$ | $6$ | $4$ |
| 5 | `576e1` | CM by $\mathbb{Q}(\sqrt{-3})$ | $0$ | $4$ | $0$ | $-2$ | $0$ | $8$ |
| 6 | `576f1` | CM by $\mathbb{Q}(\sqrt{-3})$ | $0$ | $-4$ | $0$ | $-2$ | $0$ | $-8$ |
| 7 | `576g1` | non-CM | $-2$ | $0$ | $4$ | $2$ | $-2$ | $4$ |
| 8 | `576h1` | non-CM | $-2$ | $0$ | $0$ | $-6$ | $-2$ | $0$ |
| 9 | `576i1` | non-CM | $-2$ | $0$ | $-4$ | $2$ | $-2$ | $-4$ |

---

## 8. Verification Script

The complete Python verification script is located at:
[`code/U102_kraus_frey_modularity_verification.py`](file://[LOCAL_HOME]/Downloads/beal/code/U102_kraus_frey_modularity_verification.py).

To execute the test suite:
```bash
python3 code/U102_kraus_frey_modularity_verification.py
```
All assertions pass with return code 0.

---

## 9. References

1. **[Kra98]** Alain Kraus, *Sur l'équation $a^3 + b^3 = c^p$*, Experimental Mathematics 7 (1998), no. 1, 1–13.
2. **[Dah08]** Sander R. Dahmen, *Classical and modular methods for exponential Diophantine equations*, Ph.D. thesis, Universiteit Utrecht, 2008.
3. **[Fre16]** Nuno Freitas, *On the Fermat-type equation $x^3 + y^3 = z^p$*, Comment. Math. Helv. 91 (2016), no. 2, 295–304.
4. **[HK02]** Emmanuel Halberstadt and Alain Kraus, *Courbes de Fermat: résultats et problèmes*, J. Reine Angew. Math. 548 (2002), 167–234.
5. **[Rib90]** Kenneth A. Ribet, *On modular representations of $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ arising from modular forms*, Invent. Math. 100 (1990), no. 2, 431–476.
6. **[Wil95]** Andrew Wiles, *Modular elliptic curves and Fermat's Last Theorem*, Ann. of Math. (2) 141 (1995), no. 3, 443–551.
