# U105: Mod-7 Representation $\rho_{E, 7}$ and the Modular Curve $X_0(14)$ for $A^3 + B^3 = C^7$: Absolute Irreducibility via the 2-Torsion Lift and CM Valuation Obstructions

**Date**: 2026-09-17  
**Context**: Generalized Fermat equation $A^3 + B^3 = C^7$ with $\gcd(A, B) = 1$, $A, B \in \mathbb{Z}$.  
**Target**: The Kraus Frey curve $E: y^2 = x^3 + 3AB x + (B^3 - A^3)$ and its mod-7 Galois representation $\rho_{E, 7}$.  
**Companion Script**: [`code/U105_mod7_representation_and_x0_14.py`](file://[LOCAL_HOME]/Downloads/beal/code/U105_mod7_representation_and_x0_14.py)  
**JSON Certificate**: [`research/checkpoints/U105_mod7_x0_14.json`](file://[LOCAL_HOME]/Downloads/beal/research/checkpoints/U105_mod7_x0_14.json)

---

## 1. Executive Summary

In checkpoint U104, we proved that for all primes $p \ge 11$, the mod-$p$ Galois representation $\rho_{E, p}$ attached to the Kraus Frey curve
$$E: y^2 = x^3 + 3AB x + (B^3 - A^3)$$
is unconditionally and absolutely irreducible, because the rational 2-torsion point $P_2 = (A - B, 0) \in E(\mathbb{Q})[2]$ forces any rational $p$-isogeny to lift to a rational cyclic $2p$-isogeny, and by Kenku's Theorem (1981), no elliptic curve over $\mathbb{Q}$ can admit a rational cyclic $2p$-isogeny for any $2p \ge 22$.

For the exponent $p = 7$, $2p = 14$, which lies inside the classical Kenku list $\{4, \dots, 27\}$, corresponding to the modular curve $X_0(14)$.

This checkpoint resolves the arithmetic geometry of $X_0(14)$ and establishes the definitive absolute irreducibility of $\rho_{E, 7}$:

1. **The 7-to-14 Isogeny Lift**:
   Because $(A - B, 0)$ is a non-trivial rational 2-torsion point on $E$, any rational 7-isogeny on $E$ generates a rational cyclic 14-isogeny $C_{14} = C_2 \oplus C_7$, defining a $\mathbb{Q}$-rational point on the modular curve $X_0(14)$.

2. **Arithmetic Geometry of $X_0(14)$**:
   The modular curve $X_0(14)$ has genus $g = 1$, conductor 14, index $[SL_2 : \Gamma_0(14)] = 24$, and 4 cusps.
   It is isomorphic over $\mathbb{Q}$ to the elliptic curve **14a1** (Cremona label):
   $$14a1: y^2 + xy + y = x^3 + 4x - 6, \quad \Delta = -21952 = -2^6 \cdot 7^3.$$
   The Mordell--Weil group is finite of order 6 (rank 0):
   $$X_0(14)(\mathbb{Q}) \cong \mathbb{Z}/6\mathbb{Z}.$$

3. **Complete Inventory of Rational Points on $X_0(14)$**:
   The 6 rational points on $X_0(14)$ partition cleanly into:
   - **4 cusps**: $\infty, 0, 1/2, 1/7$ (all $\mathbb{Q}$-rational, corresponding to degenerate fibers with $j = \infty$).
   - **2 CM points**: fixed by the Atkin--Lehner involution $w_7$, with exact integer $j$-invariants:
     $$j_1 = -15^3 = -3375 \quad (\text{CM by maximal order of } \mathbb{Q}(\sqrt{-7}), \text{disc } -7),$$
     $$j_2 = 255^3 = 16581375 \quad (\text{CM by order of conductor 2 in } \mathbb{Q}(\sqrt{-7}), \text{disc } -28).$$
   - **0 non-CM points**: $X_0(14)$ possesses **NO non-CM rational points**!

4. **Valuation and Multiplicative Reduction Obstruction**:
   The $j$-invariant of the Kraus curve is $j(E) = \frac{6912 A^3 B^3}{C^{14}} = \frac{2^8 \cdot 3^3 A^3 B^3}{C^{14}}$.
   For any primitive solution to $A^3 + B^3 = C^7$ with $C > 1$:
   - $\gcd(AB, C) = 1$.
   - At every prime $q \mid C$, the $q$-adic valuation is strictly negative:
     * For $q \ge 5$: $v_q(j(E)) = -14 v_q(C) \le -14 < 0$.
     * For $q = 2$: $A, B$ odd $\implies v_2(AB) = 0 \implies v_2(j(E)) = 8 - 14 v_2(C) \le -6 < 0$.
     * For $q = 3$: $v_3(AB) = 0 \implies v_3(j(E)) = 3 - 14 v_3(C) \le -11 < 0$.
   - In all cases, $j(E)$ has strictly negative valuations, whereas $j_1 = -3375$ and $j_2 = 16581375$ are integers ($v_q(j_i) \ge 0$ for all $q$).
   - For $C = 1$, $A^3 + B^3 = 1 \implies AB = 0 \implies j(E) = 0 \notin \{j_1, j_2\}$.
   - For $C = 0$, $B = -A$ is the degenerate boundary cusp.

5. **Conclusion**:
   $E$ cannot correspond to any rational point on $X_0(14)$.
   Therefore, $E$ has **NO rational 14-isogeny**, and consequently **NO rational 7-isogeny**.
   The mod-7 representation $\rho_{E, 7}: \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \mathrm{GL}_2(\mathbb{F}_7)$ is **ABSOLUTELY IRREDUCIBLE**.

---

## 2. The Rational 2-Torsion Point and the 7-to-14 Isogeny Lift

From U104, the 2-torsion polynomial of the Kraus Frey curve
$$E: y^2 = x^3 + 3AB x + (B^3 - A^3)$$
factors completely as:
$$x^3 + 3AB x + (B^3 - A^3) = (x - (A - B))\left( x^2 + (A - B)x + (A^2 + AB + B^2) \right).$$
The point:
$$P_2 = (A - B, 0) \in E(\mathbb{Q})[2]$$
is a non-trivial rational 2-torsion point on $E$.
The subgroup $C_2 = \langle P_2 \rangle \cong \mathbb{Z}/2\mathbb{Z}$ is $\mathbb{Q}$-rational.

Now suppose for contradiction that $\rho_{E, 7}: \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \mathrm{GL}_2(\mathbb{F}_7)$ is reducible.
Then $E$ admits a $\mathbb{Q}$-rational subgroup $C_7 \subset E[7]$ of order 7, which defines a $\mathbb{Q}$-rational 7-isogeny:
$$\phi_7: E \longrightarrow E' = E / C_7.$$

Because $\gcd(2, 7) = 1$, the direct sum of these two independent cyclic subgroups:
$$C_{14} = C_2 \oplus C_7 \subset E[14]$$
is a $\mathbb{Q}$-rational cyclic subgroup of order 14!
The quotient map:
$$\phi_{14}: E \longrightarrow E / C_{14}$$
is a $\mathbb{Q}$-rational cyclic 14-isogeny.
The pair $(E, C_{14})$ defines a **$\mathbb{Q}$-rational point on the modular curve $X_0(14)$**.

---

## 3. Arithmetic Geometry of the Modular Curve $X_0(14)$

### 3.1 Invariants of $X_0(14)$
The modular curve $X_0(14) = \Gamma_0(14) \backslash \mathcal{H}^*$ has the following invariants:
- **Index**:
  $$\mu = [\mathrm{SL}_2(\mathbb{Z}) : \Gamma_0(14)] = 14 \prod_{p \mid 14} \left(1 + \frac{1}{p}\right) = 14 \times \left(1 + \frac{1}{2}\right) \times \left(1 + \frac{1}{7}\right) = 14 \times \frac{3}{2} \times \frac{8}{7} = 24.$$
- **Elliptic Points**:
  For $\Gamma_0(14)$, because $4 \mid 14$ is false, $\nu_2 = \prod_{p \mid 14} (1 + (-1/p)) = 0$ (since $(-1/2) = 0$).
  Also $\nu_3 = 0$ (since $(-3/2) = 0$).
- **Cusps**:
  The number of cusps is:
  $$c = \sum_{d \mid 14} \phi\left(\gcd\left(d, \frac{14}{d}\right)\right) = \phi(1) + \phi(1) + \phi(1) + \phi(1) = 4.$$
  The 4 cusps correspond to the fractions $\infty$, $0$, $1/2$, and $1/7$.
  All 4 cusps are defined over $\mathbb{Q}$.
- **Genus**:
  $$g(X_0(14)) = 1 + \frac{\mu}{12} - \frac{\nu_2}{4} - \frac{\nu_3}{3} - \frac{c}{2} = 1 + \frac{24}{12} - 0 - 0 - \frac{4}{2} = 1 + 2 - 2 = 1.$$
  Thus $X_0(14)$ is a curve of genus 1 defined over $\mathbb{Q}$.

### 3.2 The Modular Model: Cremona 14a1
Because $g(X_0(14)) = 1$ and $X_0(14)$ has rational cusps, $X_0(14)$ is an elliptic curve over $\mathbb{Q}$.
Its conductor is $N = 14$.
In Cremona's classification of elliptic curves over $\mathbb{Q}$, the optimal modular curve in isogeny class 14a is **14a1**:
$$14a1: y^2 + xy + y = x^3 + 4x - 6.$$
- **Weierstrass Coefficients**: $[a_1, a_2, a_3, a_4, a_6] = [1, 0, 1, 4, -6]$.
- **Discriminant**: $\Delta = -21952 = -2^6 \cdot 7^3$.
- **Mordell--Weil Rank**: $\operatorname{rank}_\mathbb{Z} X_0(14)(\mathbb{Q}) = 0$.
- **Torsion Subgroup**:
  $$X_0(14)(\mathbb{Q}) = X_0(14)(\mathbb{Q})_{\mathrm{tors}} \cong \mathbb{Z}/6\mathbb{Z}.$$
- **Generator**: $P_1 = (9, 23)$.
  The complete list of all 6 rational points on $14a1$ is:
  1. $k = 0$: $O = [0 : 1 : 0]$ (the point at infinity).
  2. $k = 1$: $P_1 = (9, 23)$ (order 6).
  3. $k = 2$: $P_2 = (2, 2)$ (order 3).
  4. $k = 3$: $P_3 = (1, -1)$ (order 2).
  5. $k = 4$: $P_4 = (2, -5)$ (order 3).
  6. $k = 5$: $P_5 = (9, -33)$ (order 6).

---

## 4. Exact Classification of Rational Points and $j$-Invariants on $X_0(14)$

The 6 rational points on $X_0(14)$ correspond to the moduli of cyclic 14-isogenies over $\mathbb{Q}$.
They classify as follows:

```
                            Rational Points on X_0(14) (Total: 6)
                                              |
                     +------------------------+------------------------+
                     |                                                 |
                     v                                                 v
             [4 Rational Cusps]                                [2 Rational CM Points]
             j = infinity                                      Fixed by w_7
             (Degenerate Fibers)                               (Non-Cuspidal)
                     |                                                 |
         +-----------+-----------+                         +-----------+-----------+
         |           |           |                         |                       |
         v           v           v                         v                       v
      Cusp inf    Cusp 0     Cusps 1/2, 1/7             Point 1                 Point 2
                                                     CM by disc -7           CM by disc -28
                                                     j_1 = -3375             j_2 = 16581375
```

### 4.1 The 4 Cusps
Under the modular parametrization, exactly 4 of the 6 rational points correspond to the 4 rational cusps:
$$\text{Cusps: } \left\{ \infty, 0, \frac{1}{2}, \frac{1}{7} \right\}.$$
At each cusp, the modular $j$-invariant has a pole:
$$j(\text{cusp}) = \infty.$$
On the Frey curve $E$, $j(E) = \infty \iff C = 0 \iff B = -A$.
This corresponds to the degenerate nodal boundary fiber studied in U104 (Section 2), not to non-trivial integer solutions with $C > 1$.

### 4.2 The 2 CM Points
The remaining $6 - 4 = 2$ rational points are **non-cuspidal**.
By the theory of Atkin--Lehner involutions, the involution $w_7$ acts on $X_0(14)$ with 2 rational fixed points.
These two points parametrize elliptic curves with Complex Multiplication:
1. **CM Point 1**:
   Corresponds to elliptic curves with Complex Multiplication by the maximal order $\mathcal{O}_K$ of the imaginary quadratic field $K = \mathbb{Q}(\sqrt{-7})$ (fundamental discriminant $D = -7$).
   The class number of $\mathbb{Q}(\sqrt{-7})$ is $h(-7) = 1$.
   The unique CM $j$-invariant for discriminant $-7$ is:
   $$j_1 = j\left(\frac{1 + \sqrt{-7}}{2}\right) = -15^3 = -3375 = -3^3 \cdot 5^3.$$

2. **CM Point 2**:
   Corresponds to elliptic curves with Complex Multiplication by the non-maximal order $\mathcal{O}_{2}$ of conductor $f = 2$ in $\mathbb{Q}(\sqrt{-7})$ (order discriminant $D = 4 \times (-7) = -28$).
   The class number of the order of discriminant $-28$ is $h(-28) = 1$.
   The unique CM $j$-invariant for discriminant $-28$ is:
   $$j_2 = j(\sqrt{-7}) = 255^3 = 16581375 = 3^3 \cdot 5^3 \cdot 17^3.$$

3. **Absence of Non-CM Rational Points**:
   Every rational point on $X_0(14)$ is either a cusp or one of these two CM points.
   There are **NO non-CM rational points on $X_0(14)$**:
   $$X_0(14)(\mathbb{Q})_{\text{non-CM}} = \emptyset.$$

---

## 5. Valuation and Diophantine Obstruction on $j(E)$

We compare the $j$-invariant of the Kraus Frey curve
$$j(E) = \frac{6912 A^3 B^3}{C^{14}} = \frac{2^8 \cdot 3^3 A^3 B^3}{C^{14}}$$
against the $j$-invariants of all rational points on $X_0(14)$.

### 5.1 Primitivity and Factor Coprimality
Let $(A, B, C)$ be a non-trivial primitive integer solution to $A^3 + B^3 = C^7$ with $\gcd(A, B) = 1$ and $C > 1$.
- Any prime $q \mid C$ divides $A^3 + B^3 = C^7$.
- If $q \mid A$, then $q \mid (C^7 - A^3) = B^3 \implies q \mid B$, which contradicts $\gcd(A, B) = 1$.
- Hence $\gcd(A, C) = 1$ and $\gcd(B, C) = 1$.
- Consequently:
  $$\gcd(AB, C) = 1.$$
The factor $A^3 B^3$ is strictly coprime to $C^{14}$.

### 5.2 $q$-Adic Valuation Analysis for $C > 1$

Let $q$ be any prime dividing $C$. We compute $v_q(j(E))$:
$$v_q(j(E)) = v_q(2^8 \cdot 3^3) + 3 v_q(AB) - 14 v_q(C) = v_q(2^8 \cdot 3^3) - 14 v_q(C).$$

We distinguish three cases:

1. **Case 1: $q \ge 5$**:
   - $v_q(2^8 \cdot 3^3) = 0$.
   - Because $q \mid C$, $v_q(C) \ge 1$.
   - Therefore:
     $$v_q(j(E)) = -14 v_q(C) \le -14 < 0.$$
   - However, $j_1 = -3^3 \cdot 5^3$ and $j_2 = 3^3 \cdot 5^3 \cdot 17^3$ are integers.
   - For $q \neq 5, 17$: $v_q(j_1) = 0$ and $v_q(j_2) = 0$.
   - For $q = 5$: $v_5(j_1) = 3$ and $v_5(j_2) = 3$.
   - For $q = 17$: $v_{17}(j_1) = 0$ and $v_{17}(j_2) = 3$.
   - In every case:
     $$v_q(j(E)) \le -14 < 0 \le v_q(j_i) \quad \text{for } i \in \{1, 2\}.$$
   - This contradiction eliminates all solutions where $C$ has any prime factor $q \ge 5$.

2. **Case 2: $q = 2$ ($2 \mid C$)**:
   - If $2 \mid C$, then $C^7$ is even, so $A^3 + B^3$ is even.
   - Because $\gcd(A, B) = 1$, $A$ and $B$ cannot both be even.
   - Hence $A$ and $B$ must both be **ODD**!
   - Thus $v_2(AB) = 0$.
   - The numerator power of 2 is strictly $v_2(2^8) = 8$.
   - The denominator power of 2 is $14 v_2(C) \ge 14$.
   - Therefore:
     $$v_2(j(E)) = 8 - 14 v_2(C) \le 8 - 14 = -6 < 0.$$
   - However:
     $$v_2(j_1) = v_2(-3^3 \cdot 5^3) = 0, \quad v_2(j_2) = v_2(3^3 \cdot 5^3 \cdot 17^3) = 0.$$
   - Both $j_1$ and $j_2$ are odd integers ($v_2 = 0$).
   - Since $v_2(j(E)) \le -6 < 0 = v_2(j_i)$, $j(E)$ cannot equal $j_1$ or $j_2$!

3. **Case 3: $q = 3$ ($3 \mid C$)**:
   - If $3 \mid C$, then $A^3 + B^3 \equiv 0 \pmod 3$.
   - Because $\gcd(A, B) = 1$, 3 cannot divide both $A$ and $B$.
   - If $3 \mid A$, then $3 \mid B^3$, contradiction.
   - Thus neither $A$ nor $B$ is divisible by 3, so $v_3(AB) = 0$.
   - The numerator power of 3 is strictly $v_3(3^3) = 3$.
   - The denominator power of 3 is $14 v_3(C) \ge 14$.
   - Therefore:
     $$v_3(j(E)) = 3 - 14 v_3(C) \le 3 - 14 = -11 < 0.$$
   - However:
     $$v_3(j_1) = v_3(-3^3 \cdot 5^3) = 3, \quad v_3(j_2) = v_3(3^3 \cdot 5^3 \cdot 17^3) = 3.$$
   - Since $v_3(j(E)) \le -11 < 0 < 3 = v_3(j_i)$, $j(E)$ cannot equal $j_1$ or $j_2$!

### 5.3 Boundary Cases: $C = 1$ and $C = 0$
- **Case $C = 1$**:
  $A^3 + B^3 = 1$ with $A, B \in \mathbb{Z}$.
  By Euler's theorem on sums of two cubes (or Catalan's conjecture), the only integer solutions to $A^3 + B^3 = 1$ are $(A, B) \in \{(1, 0), (0, 1)\}$.
  For both solutions:
  $$AB = 0 \implies j(E) = 0.$$
  Neither CM point on $X_0(14)$ has $j = 0$ ($j_1 = -3375 \neq 0$, $j_2 = 16581375 \neq 0$).
  Thus $C = 1$ does not produce a rational point on $X_0(14)$.

- **Case $C = 0$**:
  $A^3 + B^3 = 0 \iff B = -A$.
  This is the degenerate nodal cubic $y^2 = (x + A)^2 (x - 2A)$ where $\Delta = 0$ and $j = \infty$, which corresponds to the cusps.

**Theorem 5.** *No non-trivial primitive integer solution to $A^3 + B^3 = C^7$ can match any rational point on the modular curve $X_0(14)$.* \qed

---

## 6. Absolute Irreducibility of $\rho_{E, 7}$

**Theorem 6.** *Let $(A, B, C)$ be any primitive integer solution to $A^3 + B^3 = C^7$ with $C > 1$. The mod-7 Galois representation
$$\rho_{E, 7}: \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \longrightarrow \mathrm{GL}_2(\mathbb{F}_7)$$
is **ABSOLUTELY IRREDUCIBLE**.*

*Proof.*
1. Suppose $\rho_{E, 7}$ were reducible over $\overline{\mathbb{F}}_7$.
2. Since $\det \rho_{E, 7} = \bar{\chi}_7$ is the cyclotomic character (taking values in $\mathbb{F}_7^\times$), the eigenvalues on any stable line must be defined over $\mathbb{F}_7$.
   Thus $\rho_{E, 7}$ is reducible over $\overline{\mathbb{F}}_7$ if and only if it is reducible over $\mathbb{F}_7$.
3. Reducibility over $\mathbb{F}_7$ is equivalent to the existence of a $\mathbb{Q}$-rational subgroup $C_7 \subset E[7]$ of order 7, i.e., a $\mathbb{Q}$-rational 7-isogeny.
4. By Section 2, the existence of the rational 2-torsion point $P_2 = (A - B, 0) \in E(\mathbb{Q})[2]$ implies that $C_{14} = C_2 \oplus C_7$ is a $\mathbb{Q}$-rational cyclic subgroup of order 14 on $E$.
5. The pair $(E, C_{14})$ defines a $\mathbb{Q}$-rational point on the modular curve $X_0(14)$.
6. By Section 4, all $\mathbb{Q}$-rational points on $X_0(14)$ are either cusps ($j = \infty$) or the two CM points ($j_1 = -3375, j_2 = 16581375$).
7. By Section 5, for any solution with $C > 1$, $j(E)$ has strictly negative $q$-adic valuations for all $q \mid C$, preventing $j(E)$ from matching $j_1$ or $j_2$, while $C > 1$ prevents $j(E)$ from being a cusp.
8. This contradiction proves that $E$ cannot possess a $\mathbb{Q}$-rational 14-isogeny.
9. Consequently, $E$ cannot possess a $\mathbb{Q}$-rational 7-isogeny.
10. Therefore, $\rho_{E, 7}$ is **ABSOLUTELY IRREDUCIBLE**. \qed

---

## 7. Audit and Verification Ledger

The complete mathematical verifier `code/U105_mod7_representation_and_x0_14.py` was executed cleanly on the system architecture with exit code 0.
The companion certificate `research/checkpoints/U105_mod7_x0_14.json` confirms:

```json
{
  "checkpoint": "U105",
  "x0_14_geometry": {
    "level": 14,
    "genus": 1,
    "index": 24,
    "cusps": 4,
    "cremona_label": "14a1",
    "weierstrass_model": "y^2 + xy + y = x^3 + 4x - 6",
    "discriminant": -21952,
    "mordell_weil_rank": 0,
    "rational_torsion_group": "Z/6Z",
    "total_rational_points": 6
  },
  "rational_points": {
    "total_points": 6,
    "cusps_count": 4,
    "cm_points_count": 2,
    "non_cm_points_count": 0,
    "cm_points": [
      {
        "disc": -7,
        "order": "maximal order of Q(sqrt(-7))",
        "j_invariant": -3375,
        "prime_factors": {"3": 3, "5": 3}
      },
      {
        "disc": -28,
        "order": "order of conductor 2 in Q(sqrt(-7))",
        "j_invariant": 16581375,
        "prime_factors": {"3": 3, "5": 3, "17": 3}
      }
    ]
  },
  "valuation_obstructions": {
    "valuation_contradictions_verified": true,
    "c_equals_1_case": "j(E) = 0 not in {-3375, 16581375}",
    "c_equals_0_case": "degenerate cusp (B = -A)"
  },
  "irreducibility": {
    "2_torsion_rational": true,
    "isogeny_lift_7_to_14": true,
    "x0_14_non_cm_points": 0,
    "valuation_obstruction_cm": true,
    "cusp_obstruction": true,
    "rho_E_7_absolutely_irreducible": true
  }
}
```

---

## 8. Combined Grand Table of Mod-$p$ Irreducibility for the Kraus Curve

Combining checkpoints U104 and U105 yields the complete irreducibility ledger for the Kraus Frey curve $E$ attached to $A^3 + B^3 = C^p$:

| Exponent $p$ | Level $p$ Modular Curve $X_0(p)$ | Level $2p$ Modular Curve $X_0(2p)$ | Obstruction Mechanism on $E$ | Irreducibility of $\rho_{E, p}$ |
|:---:|:---:|:---:|:---:|:---:|
| **$p \ge 19$ ($p \neq 37, 43, 67, 163$)** | $g \ge 1$, cusps only | $g \ge 4$ | **Mazur (1977)**: no non-cuspidal rational points on $X_0(p)$ | **ABSOLUTELY IRREDUCIBLE** |
| **$p \in \{37, 43, 67, 163\}$** | $g \ge 2$, CM points only | $g \ge 8$ | **Kenku (1981)**: $2p \ge 74 \implies$ no rational $2p$-isogenies | **ABSOLUTELY IRREDUCIBLE** |
| **$p = 17$** | $g = 1$, 2 CM points only | $g = 3$ ($X_0(34)$) | **Kenku (1981)** + CM valuation obstruction ($v_q(j) < 0$) | **ABSOLUTELY IRREDUCIBLE** |
| **$p = 13$** | $g = 0$, $\infty$-many points | $g = 2$ ($X_0(26)$) | **Kenku (1981)**: $X_0(26)$ has no non-cuspidal rational points | **ABSOLUTELY IRREDUCIBLE** |
| **$p = 11$** | $g = 1$, 3 non-CM points | $g = 2$ ($X_0(22)$) | **Kenku (1981)**: $X_0(22)$ has no non-cuspidal rational points | **ABSOLUTELY IRREDUCIBLE** |
| **$p = 7$** | $g = 0$, $\infty$-many points | $g = 1$ ($X_0(14)$) | **U105 Theorem 6**: $X_0(14)$ rational points are 4 cusps + 2 CM points ($v_q(j) < 0$) | **ABSOLUTELY IRREDUCIBLE** |

**Conclusion**:  
For every prime exponent $p \ge 7$, the mod-$p$ Galois representation $\rho_{E, p}$ on the Kraus Frey curve is **ABSOLUTELY IRREDUCIBLE** for all non-trivial primitive solutions to $A^3 + B^3 = C^p$.

---

## 9. References

1. **Kraus, A.** (1998). *Sur l'équation $a^3 + b^3 = c^p$*, Experimental Mathematics 7(1), 1–13.
2. **Mazur, B.** (1977). *Modular curves and the Eisenstein ideal*, Publications Mathématiques de l'IHÉS 47, 33–186.
3. **Kenku, M.A.** (1981). *The modular curve $X_0(169)$ and complete determination of cyclic isogenies*, Journal of the London Mathematical Society (2) 24(3), 415–427.
4. **Cremona, J.E.** (1997). *Algorithms for Modular Elliptic Curves*, Cambridge University Press. Record 14a1.
5. Checkpoints: `U103_galois_representation_17_torsion_irreducibility_and_image.md`, `U104_kraus_frey_curve_torsion_and_irreducibility.md`.
