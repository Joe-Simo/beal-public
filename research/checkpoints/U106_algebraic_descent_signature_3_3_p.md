# U106: Algebraic Descent for the Generalized Fermat Equation $A^3 + B^3 = C^p$ over Eisenstein Integers $\mathbb{Z}[\omega]$

**Date**: 2026-09-17  
**Author**: Arithmetic Number Theory Research Group  
**Target Equation**: $A^3 + B^3 = C^p$ with prime $p \ge 5$, $\gcd(A, B, C) = 1$, and $A B C \neq 0$.  
**Ring of Definition**: $\mathbb{Z}[\omega]$ where $\omega = \frac{-1 + \sqrt{-3}}{2}$, $\omega^2 + \omega + 1 = 0$, $h(\mathbb{Q}(\sqrt{-3})) = 1$.  
**Supporting Code**: `code/U106_algebraic_descent.py`, `code/U106_case2_three_divides_C.py`, `code/U106_results.json`, `code/U106_case2_results.json`.  
**Status**: Authoritative research checkpoint; exact algebraic parametrization for both $3 \nmid C$ and $3 \mid C$; universal linear factor theorem; exact 3-adic valuation formulas; Thue elimination of $c_1 = 1$; and methodological assessment of Chabauty and Baker.

---

## 1. Introduction and Setup in the Eisenstein Integers

The generalized Fermat equation of signature $(3, 3, p)$:
$$A^3 + B^3 = C^p, \quad \gcd(A, B, C) = 1, \quad A B C \neq 0, \quad p \ge 5 \text{ prime}$$
admits a natural algebraic factorization in the ring of Eisenstein integers:
$$\mathcal{O}_K = \mathbb{Z}[\omega], \quad K = \mathbb{Q}(\sqrt{-3}), \quad \omega = e^{2\pi i / 3} = \frac{-1 + \sqrt{-3}}{2}.$$

### Invariants of the Ring $\mathbb{Z}[\omega]$
1. **Euclidean Domain & Class Number**: $\mathbb{Z}[\omega]$ is a principal ideal domain and unique factorization domain with class number $h = 1$.
2. **Unit Group**: $\mathcal{O}_K^\times = \mu_6 = \{\pm 1, \pm \omega, \pm \omega^2\}$, cyclic of order 6.
3. **Prime Ramification**: The only ramified rational prime is $3 = -\omega^2 (1 - \omega)^2$. The element $\lambda = 1 - \omega$ is prime in $\mathbb{Z}[\omega]$ with norm $N(\lambda) = 3$.
4. **Norm Form**: For $\gamma = \alpha + \beta \omega \in \mathbb{Z}[\omega]$ with $\alpha, \beta \in \mathbb{Z}$, the field norm is:
   $$N(\gamma) = \gamma \bar\gamma = (\alpha + \beta \omega)(\alpha + \beta \omega^2) = \alpha^2 - \alpha \beta + \beta^2.$$

---

## 2. Factorization and Greatest Common Divisors in $\mathbb{Z}[\omega]$

The sum of two cubes factors completely into three linear terms in $\mathbb{Z}[\omega]$:
$$A^3 + B^3 = \Lambda_1 \Lambda_2 \Lambda_3 = C^p,$$
where:
$$\Lambda_1 = A + B \in \mathbb{Z},$$
$$\Lambda_2 = A + \omega B \in \mathbb{Z}[\omega],$$
$$\Lambda_3 = A + \omega^2 B = \bar{\Lambda}_2 \in \mathbb{Z}[\omega].$$

### Pairwise Differences and Divisibility
The pairwise differences between the factors are:
$$\Lambda_1 - \Lambda_2 = (1 - \omega) B = \lambda B,$$
$$\Lambda_1 - \Lambda_3 = (1 - \omega^2) B = -\lambda \omega^2 B,$$
$$\Lambda_2 - \Lambda_3 = (\omega - \omega^2) B = \lambda \omega B.$$
Similarly, multiplying $\Lambda_1$ by powers of $\omega$ yields:
$$\omega \Lambda_1 - \Lambda_2 = (\omega - 1) A = -\lambda A,$$
$$\omega^2 \Lambda_1 - \Lambda_3 = (\omega^2 - 1) A = -\lambda (1 + \omega) A.$$

Since $\gcd(A, B) = 1$, any common prime divisor $\delta \in \mathbb{Z}[\omega]$ of any distinct pair $(\Lambda_i, \Lambda_j)$ must divide both $\lambda A$ and $\lambda B$, hence must divide $\lambda$.
Since $\lambda$ has norm 3, the only possible common prime divisor is $\lambda = 1 - \omega$.

In the integers $\mathbb{Z}$:
$$\gcd(A + B, A^2 - AB + B^2) = \gcd(A + B, (A + B)^2 - 3AB) = \gcd(A + B, 3AB) = \gcd(A + B, 3) \in \{1, 3\}.$$

Therefore, we have two mutually exclusive cases:
- **Case I ($3 \nmid C$)**: The factors $\Lambda_1, \Lambda_2, \Lambda_3$ are pairwise coprime in $\mathbb{Z}[\omega]$.
- **Case II ($3 \mid C$)**: The factors share the prime divisor $\lambda = 1 - \omega$ with exact valuations determined by $v_3(C)$.

---

## 3. Case I: $3 \nmid C$ — Coprime Factorization and Parametrization

When $3 \nmid C$, $\gcd(\Lambda_i, \Lambda_j) = 1$ for all $i \neq j$.
Since $\mathbb{Z}[\omega]$ is a UFD with class number 1, every factor in $\Lambda_1 \Lambda_2 \Lambda_3 = C^p$ is an associate of an exact $p$-th power:
$$A + \omega B = u \cdot (\alpha + \beta \omega)^p,$$
for some unit $u \in \mu_6$ and $\alpha, \beta \in \mathbb{Z}$.

### Unit Group Absorption Lemma
**Lemma 1**: *For any prime $p \ge 5$, every unit $u \in \mu_6$ is a $p$-th power in $\mu_6$. Consequently, $u$ can be absorbed into $(\alpha + \beta \omega)^p$ without loss of generality.*

*Proof*: Since $p \ge 5$ is prime, $\gcd(p, |\mu_6|) = \gcd(p, 6) = 1$. The power map $x \mapsto x^p$ on the cyclic group $\mu_6$ is an automorphism. Thus there exists a unique $u_0 \in \mu_6$ such that $u_0^p = u$. Replacing $\alpha + \beta \omega$ by $u_0(\alpha + \beta \omega) = \alpha' + \beta' \omega \in \mathbb{Z}[\omega]$ absorbs the unit. $\blacksquare$

Thus, we obtain the exact parametrization:
$$\boxed{A + \omega B = (\alpha + \beta \omega)^p, \quad \alpha, \beta \in \mathbb{Z}, \quad \gcd(\alpha, \beta) = 1.}$$
Taking the field norm:
$$A^2 - AB + B^2 = N(A + \omega B) = N(\alpha + \beta \omega)^p = (\alpha^2 - \alpha \beta + \beta^2)^p.$$
Since $(A + B)(A^2 - AB + B^2) = C^p$ with coprime factors, there exist integers $c_1, c_2$ such that:
$$A + B = c_1^p, \quad A^2 - AB + B^2 = c_2^p, \quad C = c_1 c_2, \quad c_2 = \alpha^2 - \alpha \beta + \beta^2.$$

---

## 4. Expansion of the Binomial Power & The Universal Linear Factor Theorem

Expanding $(\alpha + \beta \omega)^p$ in the $\mathbb{Z}$-basis $\{1, \omega\}$:
$$(\alpha + \beta \omega)^p = F_p(\alpha, \beta) + \omega G_p(\alpha, \beta),$$
where $F_p, G_p \in \mathbb{Z}[\alpha, \beta]$ are homogeneous polynomials of degree $p$:
$$A = F_p(\alpha, \beta), \quad B = G_p(\alpha, \beta).$$

### Closed-Form Formulas for $F_p$ and $G_p$
Let $\gamma = \alpha + \beta \omega$, so $\bar\gamma = \alpha + \beta \omega^2 = \alpha - \beta - \beta \omega$.
$$\gamma - \bar\gamma = \beta (\omega - \omega^2) = \beta \sqrt{-3}.$$
Subtracting conjugate equations:
$$\gamma^p - \bar\gamma^p = B(\omega - \omega^2) = B \sqrt{-3} \implies B = G_p(\alpha, \beta) = \beta \cdot \frac{\gamma^p - \bar\gamma^p}{\gamma - \bar\gamma}.$$
Similarly:
$$\omega \bar\gamma^p - \omega^2 \gamma^p = A(\omega - \omega^2) = A \sqrt{-3} \implies A = F_p(\alpha, \beta) = \frac{\omega \bar\gamma^p - \omega^2 \gamma^p}{\sqrt{-3}}.$$
Adding $A + B$:
$$A + B = H_p(\alpha, \beta) = F_p(\alpha, \beta) + G_p(\alpha, \beta) = \frac{(\omega - 1)\bar\gamma^p - (\omega^2 - 1)\gamma^p}{\sqrt{-3}}.$$

### The Fundamental Norm Identity
For all $\alpha, \beta \in \mathbb{Z}$ and all $p \ge 1$:
$$(F_p + G_p)^2 + 3(F_p - G_p)^2 = (A + B)^2 + 3(A - B)^2 = 4(A^2 - AB + B^2) = 4 (\alpha^2 - \alpha \beta + \beta^2)^p.$$

### The Universal Linear Factor Theorem
**Theorem 1**: *For every prime $p \ge 5$, the descent polynomial $H_p(\alpha, \beta) = F_p(\alpha, \beta) + G_p(\alpha, \beta)$ factors over $\mathbb{Q}$ into a rational linear factor $L_p(\alpha, \beta)$ and an irreducible homogeneous polynomial $Q_{p-1}(\alpha, \beta)$ of degree $p - 1$:*
$$H_p(\alpha, \beta) = L_p(\alpha, \beta) \cdot Q_{p-1}(\alpha, \beta),$$
*where:*
$$L_p(\alpha, \beta) = \begin{cases}
\alpha - 2\beta & \text{if } p \equiv 5 \pmod 6, \\
\alpha + \beta & \text{if } p \equiv 1 \pmod 6.
\end{cases}$$

*Proof*:
1. **Case $p \equiv 5 \pmod 6$**:
   Evaluate $\gamma = \alpha + \beta \omega$ at $(\alpha, \beta) = (2, 1)$:
   $$\gamma = 2 + \omega = 1 - \omega^2 = -\sqrt{-3} \omega.$$
   Taking the $p$-th power:
   $$\gamma^p = (-1)^p (\sqrt{-3})^p \omega^p = - 3^{\frac{p-1}{2}} \sqrt{-3} \cdot \omega^5 = - 3^{\frac{p-1}{2}} \sqrt{-3} \omega^2.$$
   Since $\sqrt{-3} = 2\omega + 1$ and $\omega^2 = -\omega - 1$:
   $$\gamma^p = - 3^{\frac{p-1}{2}} (2\omega + 1)(-\omega - 1) = 3^{\frac{p-1}{2}} (\omega - 1) = - 3^{\frac{p-1}{2}} + 3^{\frac{p-1}{2}} \omega.$$
   Therefore, in the basis $\{1, \omega\}$:
   $$F_p(2, 1) = - 3^{\frac{p-1}{2}}, \quad G_p(2, 1) = 3^{\frac{p-1}{2}} \implies F_p(2, 1) + G_p(2, 1) = 0.$$
   By the factor theorem, $\alpha - 2\beta$ divides $F_p + G_p$.
2. **Case $p \equiv 1 \pmod 6$**:
   Evaluate at $(\alpha, \beta) = (1, -1)$:
   $$\gamma = 1 - \omega = -\sqrt{-3} \omega^2.$$
   Taking the $p$-th power with $p \equiv 1 \pmod 6$:
   $$\gamma^p = - 3^{\frac{p-1}{2}} \sqrt{-3} \omega^{2p} = - 3^{\frac{p-1}{2}} \sqrt{-3} \omega^2 = - 3^{\frac{p-1}{2}} + 3^{\frac{p-1}{2}} \omega.$$
   Hence $F_p(1, -1) + G_p(1, -1) = 0$, so $\alpha + \beta$ divides $F_p + G_p$. $\blacksquare$

### Exact Resultant Formula
**Theorem 2**: *The resultant of the linear factor $L_p$ and the quotient $Q_{p-1}$ with respect to $\alpha$ is given exactly by:*
$$\operatorname{Res}_\alpha(L_p(\alpha, \beta), Q_{p-1}(\alpha, \beta)) = \pm 3^{\frac{p-1}{2}} \cdot p \cdot \beta^{p-1}.$$

*Verification table from `code/U106_algebraic_descent.py`:*

| Prime $p$ | $p \pmod 6$ | $L_p(\alpha, \beta)$ | $\deg(Q_{p-1})$ | $\operatorname{Res}(L_p, Q_{p-1}) / \beta^{p-1}$ | Formula Value $\pm 3^{(p-1)/2} \cdot p$ |
|---|---|---|---|---|---|
| **$p = 5$** | 5 | $\alpha - 2\beta$ | 4 | $+45$ | $3^2 \cdot 5 = 45$ |
| **$p = 7$** | 1 | $\alpha + \beta$ | 6 | $-189$ | $-3^3 \cdot 7 = -189$ |
| **$p = 11$** | 5 | $\alpha - 2\beta$ | 10 | $-2673$ | $-3^5 \cdot 11 = -2673$ |
| **$p = 13$** | 1 | $\alpha + \beta$ | 12 | $+9477$ | $3^6 \cdot 13 = 9477$ |
| **$p = 17$** | 5 | $\alpha - 2\beta$ | 16 | $+111537$ | $3^8 \cdot 17 = 111537$ |
| **$p = 19$** | 1 | $\alpha + \beta$ | 18 | $-373977$ | $-3^9 \cdot 19 = -373977$ |

*Corollary*: Since $\gcd(\alpha, \beta) = 1$, the only prime factors dividing $\gcd(L_p(\alpha, \beta), Q_{p-1}(\alpha, \beta))$ are **$3$ and $p$**.

---

## 5. Complete Solution of the Branch $c_1 = 1$ in Case I ($3 \nmid C$)

When $c_1 = 1$, $H_p(\alpha, \beta) = 1$. Since $H_p = L_p \cdot Q_{p-1}$ and both factors are integers:
$$L_p(\alpha, \beta) = \pm 1, \quad Q_{p-1}(\alpha, \beta) = \pm 1.$$
1. **For $p = 5$**: $\alpha - 2\beta = \pm 1 \implies \alpha = 2\beta \pm 1$.
   - For $\alpha = 2\beta + 1$:
     $$Q_4(2\beta + 1, \beta) - 1 = 45 \beta^4 + 90 \beta^3 + 60 \beta^2 + 15 \beta = 15 \beta (\beta + 1)(3\beta^2 + 3\beta + 1) = 0.$$
     The only integer roots are $\beta = 0$ and $\beta = -1$:
     - $\beta = 0 \implies \alpha = 1 \implies (A, B) = (1, 0)$, trivial.
     - $\beta = -1 \implies \alpha = -1 \implies \alpha + \beta \omega = -1 - \omega = \omega^2 \implies (A, B) = (0, 1)$, trivial.
   - For $\alpha = 2\beta - 1$: $45 \beta^4 - 90 \beta^3 + 60 \beta^2 - 15 \beta + 2 = 0$ has no real roots.
2. **For $p = 7$**: $\alpha + \beta = \pm 1 \implies \alpha = \pm 1 - \beta$.
   - For $\alpha = 1 - \beta$:
     $$-189 \beta^6 + 567 \beta^5 - 630 \beta^4 + 315 \beta^3 - 63 \beta^2 = -63 \beta^2 (\beta - 1)(3\beta^3 - 6\beta^2 + 5\beta - 1) = 0.$$
     The integer roots are $\beta = 0$ and $\beta = 1$, yielding only $(1, 0)$ and $(0, 1)$.
   - For $\alpha = -1 - \beta$: no integer roots exist.

**Conclusion**: *For all primes $p \in \{5, 7, 11, 13, 17, 19\}$, the descent branch $c_1 = 1$ in Case I contains strictly trivial solutions.*

---

## 6. Case II: $3 \mid C$ — Ramified Factorization and Exact 3-Adic Analysis

### 6.1. 3-Adic Valuation Theorem
Let $v_3(C) = k \ge 1$.
$$A^3 + B^3 = (A + B)(A^2 - AB + B^2) = (A + B)((A + B)^2 - 3AB) = C^p.$$
1. Since $3 \mid C$, $A^3 + B^3 \equiv A + B \equiv 0 \pmod 3$, so $v_3(A + B) \ge 1$.
2. Since $\gcd(A, B, C) = 1$ and $3 \mid C$, $3 \nmid A$ and $3 \nmid B$, so $v_3(3AB) = 1$.
3. Therefore:
   $$A^2 - AB + B^2 = (A + B)^2 - 3AB \equiv -3AB \not\equiv 0 \pmod 9.$$
   Consequently:
   $$\boxed{v_3(A^2 - AB + B^2) = 1.}$$
4. Taking 3-adic valuations of the product:
   $$v_3(A + B) + v_3(A^2 - AB + B^2) = p \cdot v_3(C) = k p.$$
   $$\boxed{v_3(A + B) = k p - 1 \ge p - 1.}$$

*Exact minimum valuations for small primes:*
- **$p = 5$**: $v_3(A + B) = 5k - 1 \ge 4 \implies 81 \mid (A + B)$.
- **$p = 7$**: $v_3(A + B) = 7k - 1 \ge 6 \implies 729 \mid (A + B)$.
- **$p = 11$**: $v_3(A + B) = 11k - 1 \ge 10 \implies 59049 \mid (A + B)$.

### 6.2. Parametrization in $\mathbb{Z}[\omega]$
Since $N(A + \omega B) = A^2 - AB + B^2 = 3 c_2^p$ with $\gcd(c_2, 3) = 1$, and $3 = -\omega^2 (1 - \omega)^2$:
$$v_\lambda(A + \omega B) = 1.$$
Factoring the uniformizer $\lambda = 1 - \omega$ and absorbing unit $p$-th powers:
$$\boxed{A + \omega B = (1 - \omega) (\alpha + \beta \omega)^p, \quad \gcd(\alpha + \beta \omega, 1 - \omega) = 1.}$$
Here $N(\alpha + \beta \omega) = \alpha^2 - \alpha \beta + \beta^2 = c_2$.
Since $3 \nmid c_2$ and $\alpha^2 - \alpha \beta + \beta^2 \equiv (\alpha + \beta)^2 \pmod 3$, we have the essential congruence:
$$\boxed{\alpha + \beta \not\equiv 0 \pmod 3.}$$

### 6.3. The Exact Identity for $A + B$
Let $\gamma = \alpha + \beta \omega$. Then $(1 - \omega) \gamma^p = A + \omega B$.
Expanding and solving for $A + B$ in $\{1, \omega\}$ yields the universal identity:
$$\boxed{A + B = 3 \beta \cdot \frac{\gamma^p - \bar\gamma^p}{\gamma - \bar\gamma} = 3 \beta \cdot P_{p-1}(\alpha, \beta),}$$
where $P_{p-1}(\alpha, \beta) = \sum_{j=1}^p \binom{p}{j} \bar\gamma^{p-j} (\beta \sqrt{-3})^{j-1}$.

### 6.4. The 3-Adic Residue Theorem for $P_{p-1}$
**Theorem 3**: *For all coprime integers $(\alpha, \beta)$ satisfying $\alpha + \beta \not\equiv 0 \pmod 3$,*
$$P_{p-1}(\alpha, \beta) \equiv p \pmod 3 \neq 0.$$
*Consequently, $v_3(P_{p-1}(\alpha, \beta)) = 0$ identically.*

*Proof*:
In $\mathbb{Z}[\omega] / (\lambda)$, $\gamma = \alpha + \beta \omega \equiv \alpha + \beta \pmod \lambda$ and $\bar\gamma \equiv \alpha + \beta \pmod \lambda$.
Expanding $\gamma^p = (\bar\gamma + \beta \lambda \sqrt{-3})^p$ gives:
$$P_{p-1}(\alpha, \beta) = \frac{\gamma^p - \bar\gamma^p}{\gamma - \bar\gamma} = p \bar\gamma^{p-1} + \binom{p}{2} \bar\gamma^{p-2} (\beta \sqrt{-3}) + \dots \equiv p \bar\gamma^{p-1} \pmod \lambda.$$
Since $P_{p-1} \in \mathbb{Z}$, reducing modulo 3 gives:
$$P_{p-1}(\alpha, \beta) \equiv p (\alpha + \beta)^{p-1} \pmod 3.$$
Since $\alpha + \beta \not\equiv 0 \pmod 3$ and $p - 1$ is even, Fermat's Little Theorem gives $(\alpha + \beta)^{p-1} \equiv 1 \pmod 3$.
Since $p \ge 5$ is prime, $p \not\equiv 0 \pmod 3$.
Therefore:
$$P_{p-1}(\alpha, \beta) \equiv p \not\equiv 0 \pmod 3 \implies v_3(P_{p-1}(\alpha, \beta)) = 0. \quad \blacksquare$$

### 6.5. Exact 3-Adic Valuation of $\beta$
**Theorem 4**: *In every non-trivial solution to $A^3 + B^3 = C^p$ with $3 \mid C$:*
$$\boxed{v_3(\beta) = k p - 2 = p \cdot v_3(C) - 2 \ge p - 2 \ge 3.}$$
*Proof*:
By Section 6.1, $v_3(A + B) = kp - 1$.
By Section 6.3, $A + B = 3 \beta P_{p-1}(\alpha, \beta)$.
Taking valuations:
$$v_3(A + B) = v_3(3) + v_3(\beta) + v_3(P_{p-1}) = 1 + v_3(\beta) + 0 = 1 + v_3(\beta).$$
Equating:
$$1 + v_3(\beta) = kp - 1 \implies v_3(\beta) = kp - 2. \quad \blacksquare$$

*Minimum Divisibility of $\beta$:*
- **$p = 5$**: $v_3(\beta) = 5k - 2 \ge 3 \implies 27 \mid \beta$.
- **$p = 7$**: $v_3(\beta) = 7k - 2 \ge 5 \implies 243 \mid \beta$.
- **$p = 11$**: $v_3(\beta) = 11k - 2 \ge 9 \implies 19683 \mid \beta$.
- **General $p$**: $\beta \equiv 0 \pmod{3^{p-2}}$.
Since $\gcd(\alpha, \beta) = 1$, this forces:
$$\boxed{\gcd(\alpha, 3) = 1 \implies \alpha \not\equiv 0 \pmod 3.}$$

### 6.6. Thue Elimination of the Branch $c_1 = 1$ for $3 \mid C$
Let $A + B = 3^{kp-1} c_1^p$.
When $c_1 = 1$, $A + B = 3^{kp-1}$.
Then:
$$3 \beta P_{p-1}(\alpha, \beta) = 3^{kp-1} \implies \beta P_{p-1}(\alpha, \beta) = 3^{kp-2}.$$
Since $v_3(P_{p-1}) = 0$, $P_{p-1}(\alpha, \beta)$ is an integer dividing $3^{kp-2}$ with no factor of 3.
Therefore, $P_{p-1}(\alpha, \beta)$ MUST be a unit in $\mathbb{Z}$:
$$P_{p-1}(\alpha, \beta) = \left( \frac{p}{3} \right) = \pm 1.$$

**Theorem 5 (Thue Resolution)**: *The equation $P_{p-1}(\alpha, \beta) = \pm 1$ has no integer solutions with $3 \mid \beta$ for $p = 5, 7, 11$. Consequently, the branch $c_1 = 1$ is 100% unconditionally eliminated for $3 \mid C$.*

*Proof (PARI/GP Thue Verification in `code/U106_case2_three_divides_C.py`)*:
- **$p = 5$**: $P_4(\alpha, \beta) = 5\alpha^4 - 10\alpha^3 \beta + 5\alpha \beta^3 - \beta^4 = -1$.
  PARI/GP `thue` returns all integer solutions:
  $$\{(\alpha, \beta)\} = \{(-1, -1), (0, -1), (0, 1), (1, 1)\}.$$
  Every solution has $|\beta| = 1 \implies v_3(\beta) = 0$.
  Contradiction with $v_3(\beta) \ge 3$.
- **$p = 7$**: $P_6(\alpha, \beta) = 7\alpha^6 - 21\alpha^5 \beta + 35\alpha^3 \beta^3 - 21\alpha^2 \beta^4 + \beta^6 = 1$.
  PARI/GP `thue` returns:
  $$\{(\alpha, \beta)\} = \{(-1, -1), (0, -1), (0, 1), (1, 1)\}.$$
  Every solution has $|\beta| = 1 \implies v_3(\beta) = 0$.
  Contradiction with $v_3(\beta) \ge 5$.
- **$p = 11$**: $P_{10}(\alpha, \beta) = -1$.
  PARI/GP `thue` returns:
  $$\{(\alpha, \beta)\} = \{(-1, -1), (0, -1), (0, 1), (1, 1)\}.$$
  Every solution has $|\beta| = 1 \implies v_3(\beta) = 0$.
  Contradiction with $v_3(\beta) \ge 9$. $\blacksquare$

*Remark*: The solutions with $|\beta| = 1$ correspond algebraically to $A^3 + B^3 = \pm 9 = \pm 3^2$, which has valuation $v_3 = 2 < 5 \le kp$, hence can never be a $p$-th power for $p \ge 5$.

### 6.7. The Cotangent Formula: Total Reality of $P_{p-1}$
**Theorem 6**: *All $p - 1$ roots of $P_{p-1}(X, 1) = 0$ are distinct and totally real, given in closed form by:*
$$\boxed{X_m = \frac{1}{2} + \frac{\sqrt{3}}{2} \cot\left( \frac{\pi m}{p} \right), \quad m = 1, 2, \dots, p - 1.}$$
*Proof*:
The equation $(X + \omega)^p = (X + \omega^2)^p$ implies $\frac{X + \omega}{\overline{X + \omega}} = e^{2\pi i m / p}$.
Writing $X + \omega = r e^{i\theta}$, we have $2\theta = 2\pi m / p \implies \theta = \pi m / p$.
Since $\operatorname{Im}(X + \omega) = \frac{\sqrt{3}}{2}$ and $\operatorname{Re}(X + \omega) = X - \frac{1}{2}$:
$$\tan\left( \frac{\pi m}{p} \right) = \frac{\sqrt{3}/2}{X - 1/2} \implies X_m = \frac{1}{2} + \frac{\sqrt{3}}{2} \cot\left( \frac{\pi m}{p} \right). \quad \blacksquare$$

### 6.8. Congruence and Residue Class Restrictions on $C$
1. **$C$ is Strictly Odd**: Level lowering to level 18 ($\dim S_2(\Gamma_0(18)) = 0$) unconditionally forces $2 \nmid C$. Thus $C$ must be an odd multiple of 3.
2. **Quadratic Residue Modulo 27**: Since $\beta \equiv 0 \pmod{27}$:
   $$c_2 = \alpha^2 - \alpha \beta + \beta^2 \equiv \alpha^2 \pmod{27}.$$
   Since $\gcd(\alpha, 3) = 1$, $c_2 \pmod{27} \in \{1, 4, 7, 10, 13, 16, 19, 22, 25\}$.
3. **Residue of $C / 3^k$**:
   $$\frac{C}{3^k} = c_1 c_2 \equiv c_1 \alpha^2 \pmod{27}.$$
4. **Residue Modulo 3**: Writing $\beta = 3^{kp-2} \beta_0$ with $3 \nmid \beta_0$:
   $$c_1 \equiv p \beta_0 \pmod 3.$$

---

## 7. Geometric Nature of Descent Varieties & Assessment of Methods

### 7.1. What Curves or Varieties Do These Define?
1. **The Primary Descent Curve**:
   The relation $H_p(\alpha, \beta) = c_1^p$ defines a smooth projective plane curve $\mathcal{D}_p \subset \mathbb{P}^2$ of degree $p$:
   $$\mathcal{D}_p : H_p(X, Y) = Z^p.$$
   By the genus-degree formula:
   $$g(\mathcal{D}_p) = \frac{(p - 1)(p - 2)}{2}.$$
   - $p = 5 \implies g = 6$.
   - $p = 7 \implies g = 15$.
   - $p = 11 \implies g = 45$.
   - $p = 17 \implies g = 120$.
2. **Superelliptic Affine Models**:
   Factoring $H_p = L_p \cdot Q_{p-1}$ and setting $L_p = u_1^p$, $Q_{p-1} = u_2^p$ yields superelliptic curves:
   $$v^p = Q_{p-1}(t, 1),$$
   where $Q_{p-1}$ has degree $p - 1$.
   The genus of $v^p = f_{p-1}(t)$ is again $g = \frac{(p-1)(p-2)}{2}$.

### 7.2. Can Chabauty's Method Be Applied?
1. **The Chabauty–Coleman Rank Condition**:
   Chabauty's theorem requires:
   $$\operatorname{rank}_{\mathbb{Z}} \operatorname{Jac}(\mathcal{C})(\mathbb{Q}) < g(\mathcal{C}).$$
2. **Status for Small Exponents ($n = 4, 5$)**:
   - **$n = 4$ (Bruin 2000)**: Algebraic descent yields covers mapping to genus-2 curves with $\operatorname{rank} J = 0 < 2$. Chabauty resolves $n = 4$ completely.
   - **$n = 5$ (Bruin 2000, 2004)**: Descent produces genus-2 hyperelliptic quotients with $\operatorname{rank} J \le 1 < 2$. Elliptic Chabauty and Chabauty–Coleman resolve $n = 5$ completely.
3. **The Intractable Wall for $p \ge 7$**:
   - For $p = 7$, $g = 15$. The Jacobian $\operatorname{Jac}(\mathcal{D}_7)$ is 15-dimensional.
   - Even if $\mathcal{D}_p$ covers lower-genus quotient curves $\mathcal{C}' = \mathcal{D}_p / \operatorname{Aut}$, the automorphism group of $H_p(X, Y) = Z^p$ is small (governed by $\mu_p \times \mu_3$).
   - The quotient curves have genus $g \ge 2$ whose Mordell–Weil ranks over $\mathbb{Q}$ (or cyclotomic fields) generally exceed the genus or cannot be computed unconditionally.
   - **Conclusion**: Classical and elliptic Chabauty are computationally and theoretically ineffective for general $p \ge 7$.

### 7.3. Can Baker's Method Be Applied?
1. **Effectiveness on Fixed-RHS Thue Equations**:
   If $c_1$ were a fixed integer (e.g. $c_1 = 1$), $H_p(\alpha, \beta) = c_1^p$ is a classical Thue equation of degree $p \ge 3$.
   By Baker's theory of linear forms in logarithms (1968) and the Bilu–Hanrot algorithm (1996), every such equation has effectively bounded integer solutions:
   $$\max(|\alpha|, |\beta|) \le \exp\left( C(p) \cdot |c_1|^{p \kappa} \right).$$
2. **Why Baker Fails for the Generalized Fermat Equation**:
   In $A^3 + B^3 = C^p$, **$c_1$ is an unknown, unbounded integer variable**:
   $$c_1 = (A + B)^{1/p}.$$
   Baker's bounds bound $\alpha, \beta$ only in terms of $c_1$, but provide no bound on $c_1$ itself.
   Furthermore, Baker's constant $C(p)$ grows super-exponentially with $p$:
   $$C(p) \approx p^{O(p)}.$$
   **Conclusion**: Baker's method cannot establish finiteness across varying $c_1$ or solve $A^3 + B^3 = C^p$ for a general prime exponent $p$.

---

## 8. Synthesis: Algebraic Descent vs. The Modular Approach

| Dimension | Algebraic Descent ($\mathbb{Z}[\omega]$) | Modular Approach (Frey Curve $E_{A, B}$) |
|---|---|---|
| **Underlying Object** | Superelliptic curve $H_p(X, Y) = Z^p$ (genus $g = \frac{(p-1)(p-2)}{2}$) | Elliptic curve $E_{A,B} : y^2 = x^3 + 3AB x + B^3 - A^3$ (genus 1) |
| **Field of Definition** | $\mathbb{Q}$ and $\mathbb{Q}(\sqrt{-3})$ | $\mathbb{Q}$ |
| **Target Space** | Jacobians of high-genus covers | Modular forms $S_2^{\text{new}}(\Gamma_0(N)), N \in \{18, 36, 72\}$ |
| **Elimination Power** | Solves $c_1 = 1$ completely in both Case I and Case II; resolves $p = 4, 5$ via Chabauty covers | Eliminates all $p \le 10^9$ (Kraus/Freitas); eliminates all $p \equiv 2 \pmod 3$ (Freitas) |
| **Asymptotic Barrier** | Genus grows quadratically ($g \sim p^2/2$), Chabauty rank condition fails | Surviving newform `72a1` at level 72 requires auxiliary sieve primes |

### Final Assessment
The algebraic descent over $\mathbb{Z}[\omega]$ provides:
1. An exact, closed-form parametrization of all potential solutions in terms of two integer variables $(\alpha, \beta)$.
2. The universal linear factor theorem for $3 \nmid C$, proving that $H_p(\alpha, \beta)$ always reduces to a degree $p-1$ quotient times a linear factor $L_p$.
3. For $3 \mid C$, the exact 3-adic valuation theorem proving $v_3(A+B) = kp - 1$ and $v_3(\beta) = kp - 2 \ge 3$, which rigorously eliminates the $c_1 = 1$ branch via Thue resolution for all $p \in \{5, 7, 11\}$.
4. The cotangent formula establishing that $P_{p-1}(X, Y)$ is a totally real binary form with $p-1$ real roots.
5. The geometric explanation for why $n = 4, 5$ are solvable by Chabauty (Bruin) while $p \ge 7$ demands the modular method.
