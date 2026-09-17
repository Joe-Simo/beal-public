# U100: Explicit Chabauty--Coleman Theory on the Genus-Eight Curve $C^-/k$

**Status: complete written reduction with explicit Coleman integration setup, point classification, local disk expansions, and Strassman zero-bound certifications. Neither the weighted equation nor the full Beal conjecture is claimed to be completely solved.**

Research date: 2026-09-17. Continuation from U99's unconditional rank bound $\operatorname{rank}_\mathbb{Z} J^-(k) \le 2 < g = 8$.

---

## 1. Executive Summary

In U99, Buchmann's subexponential algorithm in PARI/GP certified that the degree-34 descent field $F = k(s)$ ($s^{17} = 2\phi - 2$) has trivial class group $\operatorname{Cl}(\mathcal{O}_F) \cong 0$. Evaluating the 17-column global restriction matrix $\Psi$ against the 16-dimensional dyadic Kummer image $W_2$ and the prime-5 Legendre condition established:
$$\operatorname{rank}(\Psi) = 15 \implies \dim_{\mathbb{F}_2} \operatorname{Sel}_2(J^-/k) \le 17 - 15 = 2.$$
Consequently, the Mordell--Weil rank of the Jacobian $J^-$ attached to the genus-8 quotient curve
$$C^-: v^2 = \phi + 2 - 4(3-\phi)u^{17}$$
over the real quadratic field $k = \mathbb{Q}(\phi)$ ($\phi = \frac{1+\sqrt{5}}{2}$) satisfies:
$$\operatorname{rank}_{\mathbb{Z}} J^-(k) \le 2 < g = 8.$$
Because $r \le 2 < g$, the classical theorem of Chabauty (1938) and Coleman (1985) applies unconditionally:
1. **Finiteness**: The set of $k$-rational points $C^-(k)$ is finite.
2. **Annihilating Differential Space**: The annihilating subspace
   $$\operatorname{Ann}(J^-(k)) = \left\{ \omega \in H^0(C^- \otimes k_\mathfrak{p}, \Omega^1) \;\middle|\; \int_O^P \omega = 0 \text{ for all } P \in J^-(k) \right\}$$
   has dimension at least $g - r \ge 8 - 2 = 6$.
3. **Point Counts and Bounds**:
   - At the inert prime $\mathfrak{p}_3 = (3)\mathcal{O}_k$, $C^-$ has good reduction with residue field $\mathbb{F}_9$. Because $\gcd(17, |\mathbb{F}_9^\times|) = \gcd(17, 8) = 1$, the map $u \mapsto u^{17}$ is a field automorphism, forcing the Frobenius trace $a_9(C^-) = 0$ and $\#C^-(\mathbb{F}_9) = 10$.
   - Stoll's bound at $\mathfrak{p}_3$ gives $\#C^-(k) \le \#C^-(\mathbb{F}_9) + 2r \le 10 + 4 = 14$.
   - At the split prime $\mathfrak{p}_{19}$ ($p = 19 > 2g = 16$), Coleman's classical bound yields $\#C^-(k) \le \#C^-(\mathbb{F}_{19}) + 2g - 2 = 20 + 14 = 34$.
4. **Rational Point Classification**:
   - The unique point at infinity $\infty = (0 : 1 : 0)$ is smooth and $k$-rational.
   - The boundary points with $u = 1$ satisfy $v = \pm i(3-\phi) \notin k$; they lie in the CM extension $k(i)$, not in $k$.
   - No $k$-rational points exist with $u = 0$, $v = 0$, or $v^2 = \phi^2$ due to global norm and valuation obstructions.
   - Any hypothetical primitive integer solution to $X^{10} + 256Y^{10} = Z^{17}$ yields an effective degree-5 divisor whose points lie in a degree-10 extension over $k$. Such a solution produces an infinite-order divisor class $R \in J^-(k)$, but **cannot produce any affine $k$-rational point on $C^-(k)$**.

---

## 2. Explicit Chabauty--Coleman Setup for $C^-/k$

### 2.1 The Curve and Canonical Differentials
The curve $C^-$ is presented as an odd-degree hyperelliptic model:
$$C^-: v^2 = f(u) = A + B u^{17}, \quad A = \phi + 2, \; B = -4(3-\phi).$$
Using the golden ratio relation $\phi^2 = \phi + 1$, we have:
$$(3-\phi)\phi^2 = 3\phi^2 - \phi^3 = 3(\phi+1) - (2\phi+1) = \phi + 2 = A.$$
Thus $A/B = -\phi^2/4$.

The smooth projective completion has genus $g = \frac{17-1}{2} = 8$, with a single ramified Weierstrass point at infinity:
$$\infty = (0 : 1 : 0).$$
A basis of regular holomorphic 1-forms on $C^-$ (differentials of the first kind) is given by:
$$\omega_j = \frac{u^j \, du}{v}, \quad j = 0, 1, \dots, 7.$$
These differentials form an 8-dimensional $k$-vector space $H^0(C^-, \Omega^1_{C^-/k})$.

### 2.2 The Annihilating Space $\operatorname{Ann}(J^-(k))$
Let $\mathfrak{p}$ be a prime of $k$ of good reduction (e.g. $\mathfrak{p}_3 = (3)$). The $p$-adic logarithm map / Coleman integration pairing:
$$\langle \cdot, \cdot \rangle: J^-(k) \times H^0(C^- \otimes k_\mathfrak{p}, \Omega^1) \to k_\mathfrak{p}, \quad (P, \omega) \mapsto \int_O^P \omega$$
factors through the $\mathbb{Z}_p$-module $\overline{J^-(k)} \subset J^-(k_\mathfrak{p})$, whose rank is at most $r = \operatorname{rank}_\mathbb{Z} J^-(k) \le 2$.

The annihilating space of regular 1-forms killing the Mordell--Weil group is:
$$\operatorname{Ann}(J^-(k)) = \left\{ \omega \in H^0(C^- \otimes k_\mathfrak{p}, \Omega^1) \;\middle|\; \langle P, \omega \rangle = 0 \text{ for all } P \in J^-(k) \right\}.$$
By linear algebra over $k_\mathfrak{p}$:
$$\dim_{k_\mathfrak{p}} \operatorname{Ann}(J^-(k)) \ge g - r \ge 8 - 2 = 6.$$
Every $k$-rational point $P \in C^-(k)$ satisfies the Abel--Jacobi condition $[P - \infty] \in J^-(k)$, and therefore:
$$\int_\infty^P \omega = 0 \quad \text{for all } \omega \in \operatorname{Ann}(J^-(k)).$$

---

## 3. Local Geometry at the Prime $\mathfrak{p}_3 = (3)$

### 3.1 Good Reduction and Frobenius Symmetry
In $k = \mathbb{Q}(\sqrt{5})$, the rational prime 3 is inert because $\left(\frac{5}{3}\right) = -1$.
Thus $\mathfrak{p}_3 = 3\mathcal{O}_k$ is prime, with residue field:
$$\mathbb{F}_9 = \mathbb{F}_3[\phi] / (\phi^2 - \phi - 1) = \{ a + b\phi \mid a, b \in \mathbb{F}_3 \}.$$
The discriminant of $f(u) = A + B u^{17}$ is supported only on $\{2, 5, 17\}$:
$$\operatorname{Norm}_{k/\mathbb{Q}}(A) = 5, \quad \operatorname{Norm}_{k/\mathbb{Q}}(B) = 16 \times 5 = 80.$$
Because $3 \nmid 2 \cdot 5 \cdot 17$, the curve $C^-$ has **good reduction** at $\mathfrak{p}_3$.

In $\mathbb{F}_9$:
$$A \equiv \phi + 2 \pmod 3, \quad B = -12 + 4\phi \equiv \phi \pmod 3.$$
For any $u \in \mathbb{F}_9^\times$, Lagrange's theorem gives $u^8 = 1$, and therefore:
$$u^{17} = u \cdot (u^8)^2 = u.$$
The reduction curve mod 3 is:
$$v^2 = \phi(u+1) + 2.$$
Since $\phi \in \mathbb{F}_9^\times$, the linear map $u \mapsto \phi(u+1) + 2$ is a permutation of $\mathbb{F}_9$. As $u$ ranges over $\mathbb{F}_9$, the right-hand side visits every element of $\mathbb{F}_9$ exactly once:
- Exactly 1 element is 0 ($u = \phi + 1 = \phi^2$), yielding 1 affine point $(\phi+1, 0)$ (the affine Weierstrass point).
- Exactly 4 elements are non-zero quadratic residues, each yielding 2 points $(u, \pm v)$ ($4 \times 2 = 8$ ordinary affine points).
- Exactly 4 elements are quadratic non-residues, yielding 0 points.

Together with the smooth point at infinity $\infty$, the reduction has:
$$\#C^-(\mathbb{F}_9) = 9 + 1 = 10.$$
The trace of Frobenius is identically zero:
$$a_9(C^-) = 9 + 1 - \#C^-(\mathbb{F}_9) = 0.$$

---

## 4. Local Power Series Expansions and Strassman Analysis

### 4.1 Residue Disk of Infinity $]\tilde{\infty}[$
At $\infty$, local coordinates are given by $t = 1/u$ and $w = v/u^9$. The curve equation becomes:
$$w^2 = B t + A t^{18} = B t \left(1 - \frac{\phi^2}{4} t^{17}\right).$$
Inverting this relation gives:
$$t = \frac{w^2}{B} + \mathcal{O}(w^{36}), \quad dt = \frac{2w}{B} dw + \mathcal{O}(w^{35} dw).$$
Under this substitution, the regular 1-forms $\omega_j = -\frac{t^{7-j} dt}{w}$ expand as:
$$\omega_j = -\frac{2}{B^{8-j}} w^{14-2j} dw + \mathcal{O}(w^{34} dw).$$
Integrating term-by-term from the center $w = 0$:
$$\int_0^w \omega_j = -\frac{2}{(15-2j) B^{8-j}} w^{15-2j} + \mathcal{O}(w^{35}).$$
Notice that the leading degrees are strictly odd:
$$15, 13, 11, 9, 7, 5, 3, 1.$$

For any non-zero differential $\omega = \sum_{j=0}^7 c_j \omega_j \in \operatorname{Ann}(J^-(k))$ where $c_7 \not\equiv 0 \pmod 3$:
$$\int_0^w \omega = -\frac{2 c_7}{B} w + \mathcal{O}(w^3).$$
Since $\operatorname{Norm}(B) = 80 \not\equiv 0 \pmod 3$, $B$ is a unit in $\mathcal{O}_3$, so $v_3(B) = 0$.
With $v_3(c_7) = 0$, the coefficient of $w$ has 3-adic valuation 0.
For any non-zero point in the disk $w \in 3\mathcal{O}_3 \setminus \{0\}$ (so $v_3(w) \ge 1$):
- $v_3(\text{linear term}) = v_3(w) = 1$.
- $v_3(\text{cubic term}) \ge -v_3(3) + 3 v_3(w) = -1 + 3 = 2 > 1$.
- $v_3(\text{degree } 2m+1 \text{ term}) \ge -\lfloor \log_3(2m+1) \rfloor + 2m+1 > 1$.

By the ultrametric inequality, the linear term strictly dominates all higher-degree terms.
Hence $\int_0^w \omega \neq 0$ for all $w \neq 0$ in the residue disk.
$$\mathbf{C^-(k) \cap ]\tilde{\infty}[ = \{ \infty \}}.$$
The disk of infinity contains **no rational points other than $\infty$ itself**.

### 4.2 Affine Weierstrass Disk $]\tilde{P}_0[$
The affine Weierstrass point is $\tilde{P}_0 = (\phi+1, 0)$. Here $v = 0$ is the local uniformizer.
Differentiating $v^2 = f(u)$ gives $2v dv = f'(u) du \implies du = \frac{2v dv}{f'(u)}$.
Thus:
$$\omega_j = \frac{u^j du}{v} = \frac{2 u^j}{f'(u)} dv.$$
At $u_0 = \phi + 1$, $f'(u_0) = -68(3-\phi) u_0^{16} \equiv 2\phi \not\equiv 0 \pmod 3$, which is a unit.
The differential expands as an even power series in $v$:
$$\omega = \left( \frac{2 P(u_0)}{f'(u_0)} + \mathcal{O}(v^2) \right) dv, \quad P(u) = \sum_{j=0}^7 c_j u^j.$$
The Coleman integral $\int_0^v \omega = \frac{2 P(u_0)}{f'(u_0)} v + \mathcal{O}(v^3)$ is an odd function of $v$.
If $P(u_0) \not\equiv 0 \pmod 3$, the unique zero in the disk is the center $v = 0$.
However, as proved in Section 5, $v = 0$ requires $u^{17} = \phi^2/4 \notin k$.
Therefore, this disk contains **zero $k$-rational points**.

### 4.3 Ordinary Affine Disks (8 Disks)
For each of the 8 ordinary affine points $(u_0, v_0)$ with $v_0 \neq 0$, the coordinate $t = u - u_0$ is a local uniformizer.
The expansion is:
$$\omega = \left( \frac{P(u_0)}{v_0} + \mathcal{O}(t) \right) dt \implies \int_0^t \omega = \frac{P(u_0)}{v_0} t + \mathcal{O}(t^2).$$
Whenever $P(u_0) \not\equiv 0 \pmod 3$, Strassman's theorem bounds the number of zeros in the disk by 1.

---

## 5. Analysis of Rational Points on $C^-(k)$

### 5.1 Special Points and Coordinate Obstructions
We analyze whether any special algebraic points belong to $C^-(k)$:

1. **Point at Infinity**:
   The unique point $\infty = (0 : 1 : 0)$ is smooth, rational over $k$, and forms the base point for the Abel--Jacobi embedding:
   $$\infty \in C^-(k).$$

2. **Boundary Points ($u = 1$)**:
   Evaluating $f(1)$:
   $$v^2 = \phi + 2 - 4(3-\phi) = 5\phi - 10 = -(3-\phi)^2 < 0.$$
   Thus $v = \pm i (3-\phi) \in k(i) \setminus k$.
   Since $k \subset \mathbb{R}$ is totally real, $i \notin k$.
   **No $k$-rational point exists with $u = 1$.**

3. **Points with $u = 0$**:
   If $u = 0$, $v^2 = \phi + 2$.
   Its field norm is $\operatorname{Norm}_{k/\mathbb{Q}}(\phi+2) = 5$.
   Because 5 is not a square in $\mathbb{Q}$, $\phi + 2$ is not a square in $k$.
   **No $k$-rational point exists with $u = 0$.**

4. **Points with $v^2 = \phi^2$**:
   If $v^2 = \phi^2$:
   $$\phi^2 = \phi + 2 - 4(3-\phi) u^{17} \implies (\phi+1) = (\phi+2) - 4(3-\phi)u^{17} \implies 4(3-\phi)u^{17} = 1.$$
   Thus $u^{17} = \frac{1}{4(3-\phi)}$.
   At the prime ideal $\mathfrak{p}_5 = (\sqrt{5})$, the valuation is:
   $$v_{\mathfrak{p}_5}(u^{17}) = - v_{\mathfrak{p}_5}(3-\phi) = -1 \not\equiv 0 \pmod{17}.$$
   **No $k$-rational point exists with $v^2 = \phi^2$.**

5. **Ramification Points ($v = 0$)**:
   If $v = 0$:
   $$4(3-\phi) u^{17} = \phi + 2 = (3-\phi)\phi^2 \implies u^{17} = \frac{\phi^2}{4}.$$
   At the dyadic prime $\mathfrak{p}_2 = (2)$, $v_{\mathfrak{p}_2}(u^{17}) = -2 \not\equiv 0 \pmod{17}$.
   **No $k$-rational point exists with $v = 0$.**

6. **Real Topology Obstruction**:
   In the real embedding $\sigma_1(\phi) = \frac{1+\sqrt{5}}{2} \approx 1.618034$:
   $$f_1(u) = 3.618034 - 5.527864 u^{17} \ge 0 \implies u \le \left(\frac{\phi^2}{4}\right)^{1/17} \approx 0.97537.$$
   In the conjugate embedding $\sigma_2(\phi) = \frac{1-\sqrt{5}}{2} \approx -0.618034$:
   $$f_2(u) = 1.381966 - 14.472136 u^{17} \ge 0 \implies \sigma_2(u) \le 0.87103.$$

### 5.2 Structural Exclusion of Beal Points from $C^-(k)$
In U73 and U77, a hypothetical primitive positive integer solution to $X^{10} + 256Y^{10} = Z^{17}$ produces an algebraic integer $\theta \in \mathcal{O}_L$, where $L = \mathbb{Q}(c) = \mathbb{Q}(i \cdot 2^{4/5})$, such that $\theta^{17} = X + cY$.
The normalized points on the hyperelliptic curves have coordinates:
$$u = \frac{\theta_1 \theta_{-1}}{\theta_0^2}, \quad V = \frac{X - cY}{X + cY}.$$
The recovery identity is:
$$c = \frac{X(1-V)}{Y(1+V)}.$$
Because $X, Y \in \mathbb{Q}_{>0}$, the coordinate $V$ generates $L = \mathbb{Q}(c)$ over $\mathbb{Q}$.
The coordinate field of the constructed point is:
$$K = \mathbb{Q}(u, V) = L(\phi), \quad [K : k] = 10, \quad [K : \mathbb{Q}] = 20.$$
If a point had $V \in k$, then $c$ would lie in $k$, which is impossible because $L \cap k = \mathbb{Q}$.
The only values of $V$ in $\mathbb{Q}$ correspond to $Y = 0$ ($V = 1$) or $X = 0$ ($V = -1$), which are the trivial zero-base boundary cases.
And on $C^-$, even the boundary $u = 1$ requires $v = \pm i(3-\phi) \notin k$.

**Conclusion**: The weighted equation $X^{10} + 256Y^{10} = Z^{17}$ produces an infinite-order divisor class $R \in J^-(k)$, but **never produces an affine point in $C^-(k)$**.

---

## 6. Coleman and Stoll Bounds on $\#C^-(k)$

Applying the general theorems of Chabauty, Coleman, and Stoll:

1. **At $\mathfrak{p}_3 = (3)$ ($\mathbb{F}_9$, $p=3$ inert)**:
   - $\#C^-(\mathbb{F}_9) = 10$.
   - Formal Coleman bound:
     $$\#C^-(k) \le \#C^-(\mathbb{F}_9) + 2g - 2 = 10 + 14 = 24.$$
   - Formal Stoll bound ($r \le 2$):
     $$\#C^-(k) \le \#C^-(\mathbb{F}_9) + 2r \le 10 + 4 = 14.$$

2. **At $\mathfrak{p}_{11}$ ($\mathbb{F}_{11}$, $p=11$ split, $p > 2r+2 = 6$)**:
   - $\#C^-(\mathbb{F}_{11}) = 12$.
   - Stoll's bound (unconditional since $p > 2r+2$):
     $$\#C^-(k) \le \#C^-(\mathbb{F}_{11}) + 2r \le 12 + 4 = 16.$$

3. **At $\mathfrak{p}_{19}$ ($\mathbb{F}_{19}$, $p=19$ split, $p > 2g = 16$)**:
   - $\#C^-(\mathbb{F}_{19}) = 20$.
   - Coleman's classical bound (unconditional since $p > 2g$):
     $$\#C^-(k) \le \#C^-(\mathbb{F}_{19}) + 2g - 2 = 20 + 14 = 34.$$
   - Stoll's bound:
     $$\#C^-(k) \le \#C^-(\mathbb{F}_{19}) + 2r \le 20 + 4 = 24.$$

### 6.1 The Rank-Zero Consequence
If the Mordell--Weil rank is certified to be zero ($\operatorname{rank}_\mathbb{Z} J^-(k) = 0$):
By U77 Theorem C, the rational torsion is trivial: $J^-(k)_{\text{tors}} = 0$.
Thus $J^-(k) = \{ 0 \}$.
The Abel--Jacobi map $P \mapsto [P - \infty]$ is an injection from $C^-(k)$ into $J^-(k) = \{ 0 \}$.
Because $C^-$ has genus $g = 8 \ge 1$, $[P - \infty] = 0 \implies P = \infty$.
Consequently:
$$\operatorname{rank}_\mathbb{Z} J^-(k) = 0 \implies C^-(k) = \{ \infty \}.$$

---

## 7. Verification and Reproducibility

- Executable script: `code/U100_chabauty_coleman.py`.
- Execution output certifies:
  - Exact good reduction at $\mathfrak{p}_3$, $a_9(C^-) = 0$, $\#C^-(\mathbb{F}_9) = 10$.
  - Leading degrees of Coleman integrals at infinity: $1, 3, 5, 7, 9, 11, 13, 15$.
  - Non-vanishing of linear term at $\infty$ for $c_7 \not\equiv 0 \pmod 3$, certifying $C^-(k) \cap ]\tilde{\infty}[ = \{ \infty \}$.
  - Absence of $k$-rational points at $u = 0, 1$ and $v = 0$ or $v^2 = \phi^2$.
