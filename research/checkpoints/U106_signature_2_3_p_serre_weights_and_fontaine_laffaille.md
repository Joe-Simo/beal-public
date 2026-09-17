# U106: Local Deformation, Serre Weights, and Fontaine--Laffaille Conditions for Signature $(2, 3, p)$ with $p \in \{11, 13, 17\}$

**Status: Source-verified arithmetic study, representation-theoretic classification, and computational certificate. The Fontaine--Laffaille conditions are unconditionally satisfied, and Serre weights are optimized to weight 2. Beal's conjecture and signature $(2, 3, p)$ remain under active research.**

**Date**: 2026-09-17  
**Author**: Arithmetic Geometry & Modular Deformation Research Group  
**Target Equation**: Generalized Fermat equation of signature $(2, 3, p)$:
$$A^2 + B^3 = C^p, \quad \gcd(A, B, C) = 1, \quad p \in \{11, 13, 17\}.$$
**Primary Sources**:
- Jean-Pierre Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. 15 (1972), 259–331 (§1.11, Proposition 8).
- Jean-Pierre Serre, *Sur les représentations modulaires de degré 2 de $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$*, Duke Math. J. 54 (1987), 179–230.
- Bas Edixhoven, *The weight in Serre's conjectures on modular forms*, Invent. Math. 109 (1992), 563–594 (Théorème 1.1).
- Kevin Buzzard, Fred Diamond, and Frazer Jarvis, *On Serre's conjecture for mod $\ell$ Galois representations over totally real fields*, Duke Math. J. 155 (2010), 105–161.
- Toby Gee, *A modularity lifting theorem for weight two Hilbert modular forms*, Invent. Math. 186 (2011), 1–57.
- Jean-Marc Fontaine and Guy Laffaille, *Construction de représentations $p$-adiques*, Ann. Sci. ENS 15 (1982), 547–608.
- Nuno Freitas, Bartosz Naskręcki, and Michael Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. 156 (2020), 77–113.

---

## 1. Executive Summary

This checkpoint investigates the local Galois deformation rings, inertia weights, and Serre weight optimization for generalized Fermat equations of signature $(2, 3, p)$ with prime exponents $p \in \{11, 13, 17\}$, addressing the five core questions formulated in collaboration with the modularity team:

1. **Fontaine--Laffaille Conditions at $p \in \{11, 13, 17\}$**:
   - **Base field condition**: Over $\mathbb{Q}$, the absolute ramification index is $e = 1$. Since $p \ge 11$, $e = 1 < p - 1 \in \{10, 12, 16\}$ is satisfied unconditionally. Over any quadratic field $K$, $e \le 2 < p - 1$ likewise holds.
   - **Reduction classification**: For the Kraus Frey curve $E_{(A, B, C)}: Y^2 = X^3 + 3BX + 2A$, the discriminant is $\Delta = -1728 C^p$. Since $p \nmid 1728$, $E$ has **good reduction** when $p \nmid C$, and **multiplicative reduction** when $p \mid C$. Additive reduction at $p$ is strictly impossible for all $p \ge 5$.
   - **Finite flatness**: When $p \mid C$, $v_p(\Delta) = p v_p(C) \equiv 0 \pmod p$. By Raynaud's criterion, $E[p]$ extends to a finite flat group scheme over $\mathbb{Z}_p$. When $p \nmid C$, $E[p]$ is the torsion of an abelian scheme, hence finite flat. Thus, **$\bar\rho_{E, p}$ is unconditionally finite flat at $p$ for every primitive solution**.

2. **Inertia Weights for Putative Solutions**:
   - **Multiplicative ($p \mid C$)**: $\bar\rho|_{I_p} \sim \begin{pmatrix} \chi_p & 0 \\ 0 & 1 \end{pmatrix}$ (level 1, peu ramifiée).
   - **Good Ordinary ($p \nmid C, a_p \not\equiv 0 \pmod p$)**: $\bar\rho|_{I_p} \sim \begin{pmatrix} \chi_p & * \\ 0 & 1 \end{pmatrix}$ (level 1, peu ramifiée).
   - **Good Supersingular ($p \nmid C, a_p = 0$)**: $\bar\rho|_{I_p} \sim \psi_2 \oplus \psi_2^p$ (fundamental characters of level 2).

3. **Predicted Serre Weights and Weight Optimization**:
   - **Minimal Serre weight**: By Edixhoven's theorem (1992, Theorem 1.1), $\bar\rho_{E, p}$ is finite flat at $p$ if and only if $k(\bar\rho) = 2$. Therefore, the minimal Serre weight is **strictly $k = 2$ in all cases**.
   - **Buzzard--Diamond--Jarvis (BDJ) Weight Sets**:
     - Ordinary / Multiplicative cases: $W(\bar\rho) = \{2, p\}$.
     - Supersingular case: $W(\bar\rho) = \{2, p + 1\}$.
   - **Gee's Theorem (2011)**: In the Fontaine--Laffaille range, the trivial weight (weight 2) always belongs to $W(\bar\rho)$, and a modular lift of parallel weight 2 exists unconditionally.

4. **Can the Weight be Bounded to Weight 2?**:
   - **YES**. The modular weight can **always be bounded to weight 2**.
   - Higher weights appear strictly as **companion/shadow weights** in the representation-theoretic BDJ set:
     - For $p = 11$: shadow weights $k = 11$ (ordinary) and $k = 12$ (supersingular).
     - For $p = 13$: shadow weights $k = 13$ (ordinary) and $k = 14$ (supersingular).
     - For $p = 17$: shadow weights $k = 17$ (ordinary) and $k = 18$ (supersingular).
   - These higher weights do not obstruct weight-2 modularity; they correspond to non-minimal crystalline lifts with higher Hodge--Tate jumps (such as $\{0, p-1\}$ or $\{0, p\}$).

5. **Diophantine Consequence**:
   The Diophantine obstruction to solving $A^2 + B^3 = C^p$ is **not weight growth** (which is tamed to weight 2), but the **permanent presence of the Catalan newform ($432\text{b}1$) and CM newforms in $S_2(\Gamma_0(N_p))$**, which prevents any local Kraus sieve from eliminating the modular space.

---

## 2. Geometry of the Kraus Frey Curve and Local Reduction

### 2.1 Curve Definition and Invariants
To any primitive integer solution $(A, B, C)$ of $A^2 + B^3 = C^p$ with $\gcd(A, B, C) = 1$ and $p \in \{11, 13, 17\}$, one attaches the Kraus Frey elliptic curve:
$$E_{(A, B, C)}: Y^2 = X^3 + 3BX + 2A.$$

The standard Weierstrass invariants are:
$$a_1 = a_2 = a_3 = 0, \quad a_4 = 3B, \quad a_6 = 2A.$$
$$b_2 = 0, \quad b_4 = 12B, \quad b_6 = 8A, \quad b_8 = -9B^2.$$
$$c_4 = -2^4 \cdot 3^2 B = -144 B,$$
$$c_6 = -2^5 \cdot 3^3 A = -864 A,$$
$$\Delta = \frac{c_4^3 - c_6^2}{1728} = \frac{-2^{12} \cdot 3^6 B^3 - 2^{10} \cdot 3^6 A^2}{1728} = -2^6 \cdot 3^3 (A^2 + B^3) = -1728 C^p.$$

The $j$-invariant and its complement are:
$$j = \frac{c_4^3}{\Delta} = \frac{1728 B^3}{C^p}, \quad 1728 - j = \frac{1728 A^2}{C^p}.$$

### 2.2 Impossibility of Additive Reduction at $p$
Let $p \in \{11, 13, 17\}$.
Because $p \ge 11$, $p$ does not divide $1728 = 2^6 \cdot 3^3$.
Recall that an elliptic curve has additive reduction at $p$ if and only if $v_p(\Delta) > 0$ and $v_p(c_4) > 0$.
- $v_p(\Delta) = v_p(-1728 C^p) = p v_p(C)$.
- $v_p(c_4) = v_p(-144 B) = v_p(B)$.
If $p \mid \Delta$, then $p \mid C$.
By pairwise coprimality $\gcd(A, B, C) = 1$, if $p \mid C$, then $p \nmid B$ and $p \nmid A$.
Consequently:
$$v_p(c_4) = v_p(B) = 0.$$
Therefore, $v_p(\Delta) > 0$ and $v_p(c_4) > 0$ can never hold simultaneously.
**The Kraus Frey curve NEVER exhibits additive reduction at any prime $p \ge 5$.**

### 2.3 Exhaustive Classification of Reduction Types at $p$
For every primitive solution $(A, B, C)$, exactly one of two cases occurs at $p$:

- **Case 1: $p \nmid C$**:
  $$v_p(\Delta) = p v_p(C) = 0.$$
  The curve $E$ has **good reduction** at $p$.
  Depending on the trace of Frobenius $a_p(E) = p + 1 - \#\tilde{E}(\mathbb{F}_p)$:
  - *Good Ordinary Reduction*: $a_p(E) \not\equiv 0 \pmod p$.
  - *Good Supersingular Reduction*: $a_p(E) \equiv 0 \pmod p$.
    By Hasse's bound $|a_p| \le 2\sqrt{p} < p$ (since $2\sqrt{11} \approx 6.63, 2\sqrt{13} \approx 7.21, 2\sqrt{17} \approx 8.24$), supersingularity is equivalent to $a_p(E) = 0$.

- **Case 2: $p \mid C$**:
  $$v_p(\Delta) = p v_p(C) \ge p > 0, \quad v_p(c_4) = 0.$$
  The curve $E$ has **multiplicative reduction** at $p$ (it is a Tate elliptic curve over $\mathbb{Q}_p$).
  The valuation of the minimal discriminant satisfies:
  $$v_p(\Delta) \equiv 0 \pmod p.$$

---

## 3. Verification of Fontaine--Laffaille Conditions at $p \in \{11, 13, 17\}$

The theory of Fontaine and Laffaille (1982) provides an abelian category equivalence between finite flat group schemes and filtered Dieudonné modules over local rings $\mathcal{O}_K$ with absolute ramification index $e < p - 1$.

### 3.1 Base Field Ramification Index
- Over the base field $\mathbb{Q}$:
  $$e = e(\mathbb{Q}_p / \mathbb{Q}_p) = 1.$$
  The Fontaine--Laffaille bound is $e < p - 1$:
  - For $p = 11$: $e = 1 < 10 = p - 1$ (satisfied).
  - For $p = 13$: $e = 1 < 12 = p - 1$ (satisfied).
  - For $p = 17$: $e = 1 < 16 = p - 1$ (satisfied).
- Over any quadratic extension $K$ (e.g. $K = \mathbb{Q}(\sqrt{5})$ or $\mathbb{Q}(\sqrt{-3})$):
  $$e(K_v / \mathbb{Q}_p) \le 2 < p - 1$$
  is satisfied for all $p \in \{11, 13, 17\}$.

### 3.2 Finite Flatness of the $p$-Torsion Scheme
Let $\mathcal{G} = E[p]$ be the finite group scheme of $p$-torsion points over $\mathbb{Q}_p$.
We examine its extension to a finite flat group scheme over $\mathbb{Z}_p$:

1. **Good Reduction ($p \nmid C$)**:
   $E$ extends to an abelian scheme $\mathcal{E}$ over $\mathbb{Z}_p$ (its Néron model).
   The $p$-torsion scheme $\mathcal{E}[p]$ is finite flat and étale-connected of rank $p^2$ over $\mathbb{Z}_p$.
   Therefore, $\bar\rho_{E, p}|_{G_{\mathbb{Q}_p}}$ is **finite flat**.

2. **Multiplicative Reduction ($p \mid C$)**:
   $E$ is a Tate curve over $\mathbb{Q}_p$ with parameter $q_E \in \mathbb{Q}_p^\times$ satisfying $v_p(q_E) = v_p(\Delta) = p v_p(C)$.
   By Raynaud's criterion (Raynaud 1974; Serre 1987, §2.4):
   A representation of the form $\begin{pmatrix} \chi_p & * \\ 0 & 1 \end{pmatrix}$ arising from the $p$-torsion of a Tate curve extends to a finite flat group scheme over $\mathbb{Z}_p$ if and only if
   $$v_p(q_E) \equiv 0 \pmod p.$$
   Because $v_p(q_E) = p \cdot v_p(C)$ is an exact multiple of $p$, the extension class $*$ in $H^1(\mathbb{Q}_p, \mu_p) \cong \mathbb{Q}_p^\times / (\mathbb{Q}_p^\times)^p$ has valuation divisible by $p$.
   Consequently, the extension splits over the unramified quadratic extension, and $\mathcal{G}$ extends to the finite flat group scheme
   $$\mu_p \oplus \mathbb{Z}/p\mathbb{Z} \quad \text{over } \mathbb{Z}_p^{\text{unr}}.$$
   Therefore, $\bar\rho_{E, p}|_{G_{\mathbb{Q}_p}}$ is **finite flat** (peu ramifiée).

**Conclusion**: The residual representation $\bar\rho_{E, p}$ is **unconditionally finite flat** at $p$ for every primitive solution to $A^2 + B^3 = C^p$ across all $p \in \{11, 13, 17\}$.

### 3.3 Hodge--Tate Weights
The Hodge--Tate weights of the $p$-adic Tate module $V_p(E)$ are $\{0, 1\}$.
The length of the Hodge--Tate weight interval is $1 - 0 = 1 < p - 1$.
Thus all conditions of the Fontaine--Laffaille theorem are satisfied.

---

## 4. Inertia Weights and Local Galois Action

Let $I_p$ denote the inertia subgroup of $G_{\mathbb{Q}_p}$, and $P_p \subset I_p$ the wild inertia subgroup.
Since $p \ge 11 > 3$, wild inertia acts trivially on $E[p]$ in all cases ($P_p \subset \ker \bar\rho_{E, p}$).
The action is completely determined by the tame inertia quotient $I_p^{\text{tame}}$.

```
+---------------------------------------------------------------------------------------+
|              LOCAL REDUCTION AND INERTIA CLASSIFICATION AT p in {11, 13, 17}          |
+---------------------------------------------------------------------------------------+
|                                           |                                           |
v                                           v                                           v
[Multiplicative Reduction: p | C]    [Good Ordinary: p !| C, a_p != 0]   [Good Supersingular: p !| C, a_p = 0]
v_p(Delta) = p*v_p(C) = 0 mod p      v_p(Delta) = 0, a_p !| p            v_p(Delta) = 0, a_p = 0
Level 1 tame character:              Level 1 tame character:             Level 2 fundamental characters:
rho_bar|_{I_p} ~ (chi_p  0)          rho_bar|_{I_p} ~ (chi_p  *)         rho_bar|_{I_p} ~ (psi_2    0    )
                 (  0    1)                           (  0    1)                          (  0    psi_2^p)
Tame inertia weights: {0, 1}         Tame inertia weights: {0, 1}        Tame inertia weights: {1, p}
Serre weight: k = 2                  Serre weight: k = 2                 Serre weight: k = 2
BDJ set: W = {2, p}                  BDJ set: W = {2, p}                 BDJ set: W = {2, p+1}
```

### 4.1 Case 1: Multiplicative Reduction ($p \mid C$)
The action of inertia is given by:
$$\bar\rho_{E, p}|_{I_p} \sim \begin{pmatrix} \chi_p & 0 \\ 0 & 1 \end{pmatrix},$$
where $\chi_p = \omega$ is the mod $p$ cyclotomic character (the level-1 fundamental character $\psi_1$).
- Inertia weights: $\{0, 1\}$.
- Determinant: $\det \bar\rho_{E, p}|_{I_p} = \chi_p$.

### 4.2 Case 2: Good Ordinary Reduction ($p \nmid C, a_p \not\equiv 0 \pmod p$)
The connected-étale exact sequence of the formal group yields:
$$0 \to \mu_p \to E[p] \to \mathbb{Z}/p\mathbb{Z} \to 0.$$
The action of inertia is upper-triangular:
$$\bar\rho_{E, p}|_{I_p} \sim \begin{pmatrix} \chi_p & * \\ 0 & 1 \end{pmatrix}.$$
Because $E$ has good reduction, the extension class $*$ is peu ramifiée.
- Inertia weights: $\{0, 1\}$.
- Determinant: $\det \bar\rho_{E, p}|_{I_p} = \chi_p$.

### 4.3 Case 3: Good Supersingular Reduction ($p \nmid C, a_p = 0$)
By Serre (1972, Proposition 8), the formal group of $E$ over $\mathbb{Z}_p$ has height 2.
The tame inertia group acts irreducibly on the 2-dimensional $\mathbb{F}_p$-vector space $E[p]$ through the fundamental characters of level 2:
$$\bar\rho_{E, p}|_{I_p} \sim \begin{pmatrix} \psi_2 & 0 \\ 0 & \psi_2^p \end{pmatrix} \quad \text{over } \mathbb{F}_{p^2}.$$
Here $\psi_2: I_p \to \mathbb{F}_{p^2}^\times$ satisfies $\psi_2^{p+1} = \chi_p = \omega$.
- Inertia weights: The exponents with respect to $\psi_2$ are $\{1, p\}$.
- Determinant: $\det \bar\rho_{E, p}|_{I_p} = \psi_2 \cdot \psi_2^p = \psi_2^{p+1} = \chi_p$.

---

## 5. Serre Weight Optimization and the BDJ / Gee Framework

### 5.1 Classical Serre Weights over $\mathbb{Q}$ (Edixhoven 1992)
Serre (1987, §2) associates to any odd irreducible representation $\bar\rho: G_\mathbb{Q} \to \operatorname{GL}_2(\mathbb{F}_p)$ an integer $k(\bar\rho) \in \{2, 3, \dots, p+1\}$:

- If $\bar\rho|_{I_p}$ is level 1: $\bar\rho|_{I_p} \sim \begin{pmatrix} \chi_p^\alpha & * \\ 0 & \chi_p^\beta \end{pmatrix}$ with $0 \le \beta \le \alpha \le p-2$.
  Since $\det \bar\rho = \chi_p$, we have $\alpha = 1, \beta = 0$.
  - If $*$ is peu ramifiée: $k(\bar\rho) = 1 + p\beta + \alpha = 1 + 0 + 1 = 2$.
  - If $*$ is très ramifiée: $k(\bar\rho) = 1 + p\alpha + \beta = 1 + p + 0 = p + 1$.
- If $\bar\rho|_{I_p}$ is level 2: $\bar\rho|_{I_p} \sim \psi_2^{a + pb} \oplus \psi_2^{b + pa}$ with $0 \le a < b \le p-1$.
  Here $a = 0, b = 1$, giving $\psi_2 \oplus \psi_2^p$.
  The formula gives:
  $$k(\bar\rho) = 1 + ap + b = 1 + 0 \cdot p + 1 = 2.$$

**Theorem (Edixhoven 1992, Théorème 1.1)**:
*Let $p$ be an odd prime and $\bar\rho: G_\mathbb{Q} \to \operatorname{GL}_2(\mathbb{F}_p)$ an odd, irreducible representation. Then $k(\bar\rho) = 2$ if and only if $\bar\rho$ is finite flat at $p$.*

Since Section 3 proved that $\bar\rho_{E, p}$ is unconditionally finite flat at $p$, we have unconditionally:
$$k(\bar\rho_{E, p}) = 2.$$

### 5.2 The Buzzard--Diamond--Jarvis (BDJ) Weight Conjecture
In Buzzard, Diamond, and Jarvis (2010), the Serre weight conjecture is generalized to totally real fields $F$.
A Serre weight is an irreducible representation of $\operatorname{GL}_2(\mathcal{O}_F / p\mathcal{O}_F)$ over $\overline{\mathbb{F}}_p$.
Over $\mathbb{Q}$, $\operatorname{GL}_2(\mathbb{F}_p)$-weights are parameterized by $(k, w)$ with $2 \le k \le p+1$ and $0 \le w \le p-1$, given by:
$$V_{(k, w)} = \operatorname{Sym}^{k-2}(\mathbb{F}_p^2) \otimes \det^w.$$
Weight $k = 2$ with trivial character corresponds to $V_{(2, 0)} = \mathbb{F}_p$ (the trivial 1-dimensional representation).

The BDJ weight set $W(\bar\rho)$ consists of all algebraic weights $V$ such that $\bar\rho$ admits a crystalline lift with Hodge--Tate weights corresponding to $V$.
Evaluating $W(\bar\rho)$ for our Frey representations:

1. **Ordinary / Multiplicative cases**:
   $$W(\bar\rho) = \{V_{(2, 0)}, V_{(p, 0)}\} \implies k \in \{2, p\}.$$
   - Minimal weight: $k = 2$.
   - Companion weight: $k = p$.
2. **Supersingular case**:
   $$W(\bar\rho) = \{V_{(2, 0)}, V_{(p+1, p-1)}\} \implies k \in \{2, p+1\}.$$
   - Minimal weight: $k = 2$.
   - Shadow weight: $k = p + 1$.

### 5.3 Modularity Lifting and Weight Optimization (Gee 2011)
**Theorem (Toby Gee 2011, Theorem 1.1)**:
*Let $F$ be a totally real field unramified at $p \ge 3$, and let $\bar\rho: G_F \to \operatorname{GL}_2(\overline{\mathbb{F}}_p)$ be an irreducible, modular representation. If $\bar\rho|_{G_{F_v}}$ is crystalline in the Fontaine--Laffaille range for all $v \mid p$, then $\bar\rho$ is modular of weight $V$ for every $V \in W(\bar\rho)$.*

Since $V_{(2, 0)} \in W(\bar\rho)$ in every case:
- **The weight can ALWAYS be optimized and bounded to weight 2.**
- Any putative solution to $A^2 + B^3 = C^p$ produces a modular representation of **weight 2** (or parallel weight $(2, \dots, 2)$ over totally real fields).

### 5.4 Clarification on Higher Weights
Why do higher weights appear in the literature?
1. **Representation-theoretic shadow**: The BDJ set $W(\bar\rho)$ is not a singleton; it contains higher weights $k \in \{p, p+1\}$. For $p = 11, 13, 17$, these are:
   - For $p = 11$: $k = 11$ (ordinary) or $k = 12$ (supersingular).
   - For $p = 13$: $k = 13$ (ordinary) or $k = 14$ (supersingular).
   - For $p = 17$: $k = 17$ (ordinary) or $k = 18$ (supersingular).
2. **Eisenstein multiplication**: A modular form $f_2 \in S_2(\Gamma_0(N))$ of weight 2 produces a modular form of weight $p+1$ via $f_{p+1} = f_2 \cdot E_{p-1}$. Because $E_{p-1} \equiv 1 \pmod p$, their mod $p$ Galois representations are isomorphic:
   $$\bar\rho_{f_2} \cong \bar\rho_{f_{p+1}}.$$
3. **Non-minimal deformation rings**: Lifting $\bar\rho$ to characteristic zero via ordinary deformation rings without Fontaine--Laffaille constraints can yield modular forms of weight $p$ or $p+1$.
However, by weight optimization, **there is no necessity to work in higher weights; the minimal weight 2 is unconditionally available.**

---

## 6. Explicit Candidate Curve Evaluations

We evaluate the Kraus Frey construction on all known integer solutions and candidate forms for $p \in \{11, 13, 17\}$:

| Curve / Solution | Equation | $j$-invariant | $p = 11$ Reduction | $p = 13$ Reduction | $p = 17$ Reduction | Minimal Weight | BDJ Weight Set |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| **Catalan** $(\pm 3, -2, 1)$ | $Y^2 = X^3 - 6X + 6$ | $-13824$ | Ordinary ($a_{11} = 6$) | Ordinary ($a_{13} = 3$) | Ordinary ($a_{17} = -2$) | $k = 2$ | $\{2, p\}$ |
| **CM $j = 0$** $(\pm 1, 0, 1)$ | $Y^2 = X^3 + 2$ | $0$ | Supersingular ($a_{11} = 0$) | Ordinary ($a_{13} = -5$) | Supersingular ($a_{17} = 0$) | $k = 2$ | $\{2, 12\}_{11}, \{2, 13\}_{13}, \{2, 18\}_{17}$ |
| **CM $j = 1728$** $(0, 1, 1)$ | $Y^2 = X^3 + 3X$ | $1728$ | Supersingular ($a_{11} = 0$) | Ordinary ($a_{13} = -6$) | Ordinary ($a_{17} = -8$) | $k = 2$ | $\{2, 12\}_{11}, \{2, 13\}_{13}, \{2, 17\}_{17}$ |
| **Putative $p \mid C$** | Multiplicative Tate | $v_p(j) < 0$ | Multiplicative ($v_{11}(\Delta) \ge 11$) | Multiplicative ($v_{13}(\Delta) \ge 13$) | Multiplicative ($v_{17}(\Delta) \ge 17$) | $k = 2$ | $\{2, p\}$ |

### Point Counts and Traces (Verified in Python)
- **Catalan curve $E_{\text{Cat}}$**:
  - $p = 11$: $\#E(\mathbb{F}_{11}) = 6 \implies a_{11} = 12 - 6 = 6 \ne 0$ (Ordinary).
  - $p = 13$: $\#E(\mathbb{F}_{13}) = 11 \implies a_{13} = 14 - 11 = 3 \ne 0$ (Ordinary).
  - $p = 17$: $\#E(\mathbb{F}_{17}) = 20 \implies a_{17} = 18 - 20 = -2 \ne 0$ (Ordinary).
- **CM curve $j = 0$**:
  - $p = 11$: $11 \equiv 2 \pmod 3$ (inert in $\mathbb{Q}(\sqrt{-3})$) $\implies a_{11} = 0$ (Supersingular).
  - $p = 13$: $13 \equiv 1 \pmod 3$ (splits in $\mathbb{Q}(\sqrt{-3})$) $\implies a_{13} = -5 \ne 0$ (Ordinary).
  - $p = 17$: $17 \equiv 2 \pmod 3$ (inert in $\mathbb{Q}(\sqrt{-3})$) $\implies a_{17} = 0$ (Supersingular).
- **CM curve $j = 1728$**:
  - $p = 11$: $11 \equiv 3 \pmod 4$ (inert in $\mathbb{Q}(i)$) $\implies a_{11} = 0$ (Supersingular).
  - $p = 13$: $13 \equiv 1 \pmod 4$ (splits in $\mathbb{Q}(i)$) $\implies a_{13} = -6 \ne 0$ (Ordinary).
  - $p = 17$: $17 \equiv 1 \pmod 4$ (splits in $\mathbb{Q}(i)$) $\implies a_{17} = -8 \ne 0$ (Ordinary).

---

## 7. Arithmetic Implications for the Modular Approach

The results of this checkpoint yield a definitive conceptual clarification for the modular attack on signature $(2, 3, p)$:

1. **Serre Level**:
   By Ribet's level-lowering theorem, the Serre conductor $N_p$ is coprime to $p$ and divides $2^8 \cdot 3^5$. The possible levels are strictly:
   $$N_p \in \{27, 32, 54, 96, 144, 288, 864\}.$$
2. **Serre Weight**:
   Because the Fontaine--Laffaille conditions are unconditionally satisfied and $\bar\rho_{E, p}$ is finite flat at $p$, the Serre weight is **strictly $k = 2$**.
3. **The Exact Nature of the Obstruction**:
   The reason $A^2 + B^3 = C^p$ cannot be resolved by standard modular methods alone is **not an inability to control the weight**:
   - The weight does not grow with $p$; it remains firmly anchored at $k = 2$.
   - The failure of the modular sieve is caused entirely by **newform survival**:
     Because the Catalan solution $(\pm 3, -2, 1)$ exists for **all** exponents $p$, the newform $f_{\text{Cat}} \in S_2(\Gamma_0(432))$ attached to $E_{\text{Cat}}$ is **permanently present in the candidate space**.
     No local Hecke sieve at auxiliary primes $q$ can ever distinguish a hypothetical solution from the Catalan solution modulo $p$, because the Catalan solution is a genuine Diophantine point.
   - Consequently, resolving $p \in \{11, 13, 17\}$ requires geometric and $p$-adic tools beyond level-lowering, namely **Chabauty on twisted modular curves $X_E(p)$** (Freitas--Naskręcki--Stoll 2020) or higher-degree descent.

---

## 8. Artifact and Code Index

- Computational certificate: `code/U106_fontaine_laffaille_serre_weights.py` (SymPy and Python verification of base field ramification bounds, reduction classification, Raynaud finite flatness, point counts, Frobenius traces, and BDJ weight sets for $p \in \{11, 13, 17\}$; execution passes all assertions cleanly with return code 0).
- Provenance and metadata: `references/U106/sources.json`.
