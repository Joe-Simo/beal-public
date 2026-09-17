# U101: Literature Survey, Frey Curve Taxonomy, and Modular Elimination Ledger for the Generalized Fermat Equation $A^3 + B^3 = C^n$ ($n \ge 4$)

**Date**: 2026-09-17  
**Author**: Arithmetic Number Theory Research Group  
**Target Equation**: $A^3 + B^3 = C^n$ with $n \ge 4$, $\gcd(A, B, C) = 1$, and $A B C \neq 0$.  
**Context**: Beal Conjecture Program — Arithmetic Survey of Signature $(3, 3, n)$.  
**Status**: Authoritative research checkpoint, literature survey, classification ledger, and obstruction analysis.

---

## 1. Executive Summary & Problem Formulation

The generalized Fermat equation (GFE) with signature $(p, q, r)$ is given by:
$$A^p + B^q = C^r, \quad \gcd(A, B, C) = 1, \quad A B C \neq 0.$$
By the celebrated Darmon–Granville theorem (1995), when the hyperbolic index $\chi = \frac{1}{p} + \frac{1}{q} + \frac{1}{r} < 1$, the equation possesses at most finitely many primitive integer solutions $(A, B, C)$. The Beal Conjecture posits that whenever $p, q, r \ge 3$, no non-trivial primitive solutions exist.

The equation of signature $(3, 3, n)$:
$$A^3 + B^3 = C^n, \quad n \ge 4, \quad \gcd(A, B, C) = 1, \quad A B C \neq 0,$$
occupies a central position in Diophantine geometry. For $n = 3$, the non-existence of non-trivial solutions is the cubic case of Fermat's Last Theorem, classically established by Euler (1753). For $n \ge 4$, the signature $(3, 3, n)$ has hyperbolic index $\chi = \frac{2}{3} + \frac{1}{n} \le \frac{11}{12} < 1$, guaranteeing finiteness.

Unlike the classical Fermat equation $A^n + B^n = C^n$ (where the Hellegouarch–Frey curve level-lowers to the empty space $S_2(\Gamma_0(2)) = \{0\}$), the modular approach to $A^3 + B^3 = C^n$ is characterized by a fundamental arithmetic asymmetry:
1. **Level lowering lands on levels 18, 36, and 72**:
   - $S_2(\Gamma_0(18)) = \{0\}$, which unconditionally forces $C$ to be **odd**.
   - $S_2^{\text{new}}(\Gamma_0(36))$ is 1-dimensional, corresponding to the CM elliptic curve `36a1` ($y^2 = x^3 + 1$), which is completely eliminated for all prime exponents $p \ge 5$.
   - $S_2^{\text{new}}(\Gamma_0(72))$ is 1-dimensional, spanned by the rational elliptic curve `72a1` ($y^2 = x^3 + 6x - 7$).
2. **The Persistent `72a1` Obstruction**:
   The curve `72a1` has a rational 2-torsion point and exactly the same local conductor invariants at 2 and 3 as the Kraus Frey curve evaluated at the trivial boundary point $(A, B) = (1, -1)$ ($A^3 + B^3 = 0$). Consequently, **standard level-lowering alone cannot eliminate `72a1` for any exponent $n$**.

To overcome this bottleneck, arithmetic geometers developed an arsenal of sophisticated techniques over the last three decades:
- **Chabauty–Coleman methods on Jacobian covers** (Bruin 2000, 2004) resolved $n = 4$ and $n = 5$.
- **The Kraus Sieve Method** (Kraus 1998, Dahmen 2008, Freitas 2016) used local Frobenius traces at auxiliary primes $q = kp + 1$ to eliminate all primes $p \le 10^9$ computationally.
- **Dahmen's Irreducibility Certificates** (Dahmen 2008) closed the small-prime gaps $n \in \{5, 7, 11, 13\}$ via the modular method.
- **The Chen–Siksek Reciprocity Method** (Chen–Siksek 2007/2009) established that no solutions exist whenever $n$ is divisible by any integer in infinite congruence classes (including $d \equiv 2, 3 \pmod 5$).
- **The Symplectic Method** (Halberstadt–Kraus 2002, Freitas 2016) completely eliminated `72a1` for the entire infinite half-space of prime exponents **$p \equiv 2 \pmod 3$**.

This checkpoint synthesizes the complete mathematical theory, taxonomy of Frey curves, level-lowering paths, elimination techniques, and the master status ledger for $A^3 + B^3 = C^n$.

---

## 2. Chronological Literature Survey

### 2.1. Alain Kraus (1998) — *Sur l’équation $a^3 + b^3 = c^p$*
- **Citation**: *Experimental Mathematics*, Vol. 7, No. 1 (1998), pp. 1–13.
- **Key Breakthroughs**:
  1. Attached the Frey elliptic curve $E_{a,b} : y^2 = x^3 + 3ab x + b^3 - a^3$ to a hypothetical coprime solution of $a^3 + b^3 = c^p$ with prime $p \ge 17$.
  2. Computed the minimal discriminant $\Delta = -2^4 \cdot 3^3 c^{2p}$ and proved that Ribet's level-lowering theorem lowers the Galois representation $\rho_{E, p}$ to conductor $N \in \{36, 72\}$ (with $N=18$ ruled out because $S_2(\Gamma_0(18)) = \{0\}$).
  3. Proved that level 36 is eliminated for all $p \ge 5$.
  4. Identified `72a1` as the sole surviving newform obstruction at level 72.
  5. Formulated the **Method of Kraus**: by choosing auxiliary primes $q = 2kp + 1$ with $q \nmid 72$, the local condition $a^3 + b^3 \equiv c^p \pmod q$ restricts the possible ratios $a/b \pmod q$ to a small finite set, allowing trace comparison $a_q(E_{a,b}) \not\equiv a_q(E_{72a1}) \pmod{\mathfrak{p}}$ to eliminate candidate newforms.
  6. Verified computationally that the criterion holds for all prime exponents $17 \le p < 10,000$.

### 2.2. Nils Bruin (2000, 2004) — *On powers as sums of two cubes* & *Visualising $\Sha[2]$*
- **Citations**: 
  - *Algorithmic Number Theory (ANTS-IV, Leiden, 2000)*, Lecture Notes in Comput. Sci., Vol. 1838, Springer (2000), pp. 169–184.
  - *Mathematics of Computation*, Vol. 73 (2004), pp. 1459–1476.
- **Key Breakthroughs**:
  1. Exploited the factorization $A^3 + B^3 = (A+B)(A^2 - AB + B^2) = C^n$. Since $\gcd(A+B, A^2 - AB + B^2) \mid 3$, this algebraic descent yields covers of the projective line and hyperelliptic curves over $\mathbb{Q}$ and quadratic subfields.
  2. For $n = 4$: The equation $A^3 + B^3 = C^4$ descends to curves covering genus-2 curves whose Jacobians have rank 0 over $\mathbb{Q}$, completely solved via Chabauty's method.
  3. For $n = 5$: The equation $A^3 + B^3 = C^5$ descends to genus-2 hyperelliptic curves; Bruin established that the Mordell–Weil ranks of their Jacobians satisfy the Chabauty condition $\operatorname{rank} J(\mathbb{Q}) < g = 2$, proving that no non-trivial primitive solutions exist for $n = 5$.
  4. Formulated hyperelliptic coverings for $n \in \{7, 11, 13\}$ and noted that Kraus's modular method could resolve these cases once the irreducibility of $\rho_{E, p}$ was proven for $p < 17$.

### 2.3. Imin Chen & Samir Siksek (2007/2009) — *Perfect powers expressible as sums of two cubes*
- **Citations**:
  - arXiv:0707.2625 (July 2007).
  - *Journal of Algebra*, Vol. 322, Issue 3 (2009), pp. 638–656.
  - See also: I. Chen, *On the equation $s^2 + y^{2p} = \alpha^3$*, *Math. Comp.* 77 (2008), pp. 1223–1227.
- **Key Breakthroughs**:
  1. Introduced the **quadratic reciprocity constraint method** into the modular approach. By examining the 2-torsion structure of the Frey curve, the field of 2-torsion points $\mathbb{Q}(E[2])$ is generated by $\sqrt{-3}$ and $\sqrt{-3(A+B)^2}$.
  2. Evaluated Legendre symbols and quadratic Hilbert symbols at primes dividing the coefficients, establishing that the existence of an isomorphism $\rho_{E, p} \cong \rho_{72a1, p}$ forces severe reciprocity conditions on $p$.
  3. **Theorem 1 (Chen–Siksek 2009)**: The equation $A^3 + B^3 = C^n$ has no non-trivial primitive solutions whenever $n \ge 3$ has a positive divisor $d$ satisfying any of:
     - **Class I**: $d \equiv 2, 3 \pmod 5$.
     - **Class II**: $d \equiv 17, 61 \pmod{78}$.
     - **Class III**: $d \equiv 51, 103, 105 \pmod{106}$.
     - **Class IV**: $d \equiv 43, 49, 61, 79, 97, 151, 157, 169 \pmod{174}$.
  4. This provided the first infinite density of exponents $n$ unconditionally ruled out without testing individual primes.

### 2.4. Sander R. Dahmen (2008) — *Classical and modular methods applied to Diophantine equations*
- **Citation**: Ph.D. thesis, Universiteit Utrecht (2008), Chapter 3, pp. 60–62.
- **Key Breakthroughs**:
  1. **Discharged the Small-Prime Irreducibility Bottleneck**:
     Kraus's Theorem 3.1 assumed $p \ge 17$ because Serre's modularity and Ribet's level-lowering require the absolute irreducibility of the mod $p$ Galois representation $\rho_{E, p}$.
     - For $p \in \{7, 11, 13\}$: Since $E_{a,b}$ has a rational 2-torsion point $(b-a, 0)$, Mazur's torsion theorem and Merel's bounds on isogenies show that $\rho_{E, p}$ could only be reducible if $j(E) \in \{-3^3 \cdot 5^3, 3^3 \cdot 5^3 \cdot 17^3\}$. Dahmen verified that $j(E_{a,b}) = -6912 a^3 b^3 / c^{2p}$ can never equal these values for coprime integers $(a, b, c)$.
     - For $p = 5$: Dahmen utilized a cubic twist discriminant formula (Theorem 60 of his thesis) to prove that $j(E_{a,b}) \notin \{2^{12} \cdot 5 / 3^5, -2^{12} \cdot 5^2 / 3\}$, certifying the irreducibility of $\rho_{E, 5}$.
  2. **Unconditional Resolution of Small Primes**:
     With irreducibility certified, Dahmen verified Kraus's criterion for $p \in \{5, 7, 11, 13\}$ using minimal auxiliary primes $q = np + 1$:
     - $p = 5$: $n = 2 \implies q = 11$.
     - $p = 7$: $n = 10 \implies q = 71$.
     - $p = 11$: $n = 2 \implies q = 23$.
     - $p = 13$: $n = 10 \implies q = 131$.
  3. Consequently, Dahmen unconditionally closed $n = 5, 7, 11, 13$ via modular methods.

### 2.5. Nuno Freitas (2016) — *On the Fermat-type equation $x^3 + y^3 = z^p$*
- **Citation**: *Commentarii Mathematici Helvetici*, Vol. 91, No. 2 (2016), pp. 295–304.
- **Key Breakthroughs**:
  1. Introduced the **symplectic method** (based on Halberstadt–Kraus 2002) to the equation $A^3 + B^3 = C^p$.
  2. Analyzed the symplectic type of the mod $p$ isomorphism $\phi: E_{a,b}[p] \to E_{72a1}[p]$ preserving the Weil pairing.
  3. By computing the ratio of local discriminants and the valuations of $c_4, c_6, \Delta$ at 2 and 3, Freitas proved that a symplectic isomorphism requires $(\Delta(E) / \Delta(E_{72a1}))^{(p-1)/2} \equiv 1 \pmod p$, which forces $p \equiv 1 \pmod 3$.
  4. **Unconditional Theorem**: The equation $A^3 + B^3 = C^p$ has **no non-trivial primitive solutions for all primes $p \equiv 2 \pmod 3$**.
  5. Extended the computational verification of Kraus's sieve from $p = 10^4$ to **$p \le 10^9$**.

### 2.6. Bennett, Bruni, & Freitas (2018) — *Sums of two cubes as twisted perfect powers, revisited*
- **Citation**: *Algebra & Number Theory*, Vol. 12, No. 4 (2018), pp. 959–999.
- **Key Breakthroughs**:
  1. Synthesized all preceding results into Theorem 1.1, adding 59 explicit congruence classes modulo 1296.
  2. Generalized the inquiry to the twisted equation $A^3 + B^3 = q^\alpha C^p$ for primes $q \ge 5$.
  3. Classified all elliptic curves with conductors in $\{18q, 36q, 72q\}$ with non-trivial rational 2-torsion, establishing that the set of "obstruction primes" $S$ has density zero: $\pi_S(x) \ll \sqrt{x} \log^2 x$.
  4. Proved that for almost all primes $q$, the twisted equation has no solutions for suitably large $p$.

---

## 3. Exact Taxonomy of Frey Curves Attached to $A^3 + B^3 = C^n$

### 3.1. Algebraic Derivation from Factorization
Let $A, B, C$ be non-zero integers such that:
$$A^3 + B^3 = C^n, \quad \gcd(A, B) = 1.$$
Since $\gcd(A, B) = 1$, at most one of $A, B$ is even. By replacing $(A, B, C)$ with $(-A, -B, -C)$ if $n$ is odd, and swapping $A$ and $B$ if necessary, we may normalize without loss of generality so that:
$$A C \text{ is even}, \quad B \equiv (-1)^{C+1} \pmod 4.$$

The sum of two cubes factors algebraically as:
$$A^3 + B^3 = (A + B)(A^2 - A B + B^2) = (A + B)\left((A + B)^2 - 3AB\right) = C^n.$$
The resultant between the two factors is:
$$\operatorname{Res}(A + B, A^2 - A B + B^2) = 3 B^2.$$
Since $\gcd(A, B) = 1$, the greatest common divisor satisfies $\gcd(A + B, A^2 - A B + B^2) \in \{1, 3\}$.

### 3.2. Case 1: $C$ is Odd (The Kraus Frey Curve $F^{(1)}_{A, B}$)
When $C$ is odd, exactly one of $A, B$ is even. With $A C$ even, $A$ is even and $B$ is odd.  
The **Kraus Frey curve** is defined over $\mathbb{Q}$ by the Weierstrass model:
$$\boxed{E_{A, B} = F^{(1)}_{A, B} : y^2 = x^3 + 3AB x + B^3 - A^3}$$

#### Geometric & Algebraic Invariants
1. **Factorization over $\mathbb{Q}$ & Rational 2-Torsion**:
   The right-hand cubic factors as:
   $$x^3 + 3AB x + (B^3 - A^3) = (x - (A - B))\left(x^2 + (A - B)x + (A^2 + AB + B^2)\right).$$
   Setting $X = x - (A - B)$, the curve has the rational 2-torsion point:
   $$P_2 = (A - B, 0) \in E_{A, B}(\mathbb{Q})[2].$$
2. **Roots of the Cubic**:
   $$e_1 = A - B \in \mathbb{Q},$$
   $$e_2 = \frac{-(A - B) + \sqrt{-3}(A + B)}{2} = \zeta_3 A + \zeta_3^2 B,$$
   $$e_3 = \frac{-(A - B) - \sqrt{-3}(A + B)}{2} = \zeta_3^2 A + \zeta_3 B,$$
   where $\zeta_3 = \frac{-1 + \sqrt{-3}}{2}$. The full 2-torsion field is $\mathbb{Q}(E[2]) = \mathbb{Q}(\sqrt{-3})$.
3. **Weierstrass Invariants**:
   $$c_4(E_{A, B}) = -48(3AB) = -144 AB = -2^4 \cdot 3^2 AB,$$
   $$c_6(E_{A, B}) = -864(B^3 - A^3) = 2^5 \cdot 3^3 (A^3 - B^3),$$
   $$\Delta_{\min}(E_{A, B}) = -2^4 \cdot 3^3 C^{2n},$$
   $$j(E_{A, B}) = \frac{c_4^3}{\Delta} = -\frac{2^8 \cdot 3^3 A^3 B^3}{C^{2n}} = -\frac{6912 A^3 B^3}{C^{2n}}.$$

### 3.3. Case 2: $C$ is Even (The Darmon–Granville Frey Curve $F^{(0)}_{A, B}$)
When $C$ is even, both $A$ and $B$ are odd. The minimal Weierstrass model over $\mathbb{Q}$ is:
$$\boxed{F^{(0)}_{A, B} : y^2 + xy = x^3 + \frac{3(B - A) + 2}{8} x^2 + \frac{3(A + B)^2}{64} x + \frac{9(B - A)(A + B)^2}{512}}$$

#### Invariants for $C$ Even
$$c_4(F^{(0)}) = -9 AB = -3^2 AB,$$
$$c_6(F^{(0)}) = \frac{27}{2}(A^3 - B^3) = 2^{-1} \cdot 3^3 (A^3 - B^3),$$
$$\Delta(F^{(0)}) = -2^{-8} \cdot 3^3 C^{2n}.$$
Since $2 \mid C$, $C^{2n}$ contains $2^{2n} \ge 2^8$, ensuring that $\Delta(F^{(0)})$ is an integer.

---

## 4. Levels, Newforms, and Modular Elimination Architecture

### 4.1. Conductor Computation via Tate's Algorithm
Let $p$ be an odd prime dividing $n$ ($n = p$ without loss of generality), and let:
$$R = \operatorname{rad}_{>3}(C) = \prod_{\substack{\ell \mid C \\ \ell > 3}} \ell.$$
Applying Tate's algorithm to the minimal models yields the exact conductors:

$$\operatorname{Cond}(F) = \begin{cases}
18 R & \text{if } C \text{ is even and } B \equiv -1 \pmod 4, \\
36 R & \text{if } C \text{ is odd, } v_2(A) \ge 2, \text{ and } B \equiv 1 \pmod 4, \\
72 R & \text{if } C \text{ is odd, } v_2(A) = 1, \text{ and } B \equiv 1 \pmod 4.
\end{cases}$$

### 4.2. Level Lowering via Ribet's Theorem
For every prime $\ell \mid R$ (i.e. $\ell \mid C, \ell > 3$), we have:
$$v_\ell(\Delta(F)) = 2p \cdot v_\ell(C) \equiv 0 \pmod p.$$
Since the reduction of $F$ at $\ell$ is multiplicative (Kodaira type $I_{2p v_\ell(C)}$), Ribet's level-lowering theorem strips away all prime factors $\ell \mid R$. The mod $p$ representation $\rho_{F, p}$ arises from a cuspidal newform of weight 2 and level $N \in \{18, 36, 72\}$:
$$\rho_{F, p} \sim \rho_{f, \mathfrak{p}}, \quad f \in S_2^{\text{new}}(\Gamma_0(N)), \quad N \in \{18, 36, 72\}.$$

### 4.3. Analysis of the Target Spaces $S_2^{\text{new}}(\Gamma_0(N))$

| Level $N$ | $\dim S_2^{\text{new}}(N)$ | LMFDB / Cremona Label | Weierstrass Model | Arithmetic Status |
|---|---|---|---|---|
| **18** | 0 | (None) | (No elliptic curve) | **UNCONDITIONALLY EMPTY** ($C$ cannot be even) |
| **36** | 1 | `36.a1` / `36a1` | $y^2 = x^3 + 1$ | **UNCONDITIONALLY ELIMINATED** (Inertia / CM) |
| **72** | 1 | `72.a1` / `72a1` | $y^2 = x^3 + 6x - 7$ | **PERSISTENT OBSTRUCTION** |

#### 1. Level 18: Immediate Parity Exclusion ($C$ is Never Even)
- **Dimension**: $\dim S_2(\Gamma_0(18)) = 0$.
- **Arithmetic Conclusion**: No cusp form of level 18 exists. Therefore, **$C$ can never be even**.
- In every non-trivial coprime solution to $A^3 + B^3 = C^n$, $C$ must be odd, and exactly one of $A, B$ is even.

#### 2. Level 36: Elimination of CM Form `36a1`
- **Dimension**: $\dim S_2^{\text{new}}(\Gamma_0(36)) = 1$.
- **Associated Curve**: $E_{36a1} : y^2 = x^3 + 1$.
- **CM Invariant**: $j(E_{36a1}) = 0$, Complex Multiplication by $\mathbb{Z}[\zeta_3] = \mathcal{O}_{\mathbb{Q}(\sqrt{-3})}$.
- **Elimination Proof**:
  - For any prime $\ell \equiv 2 \pmod 3$, CM forces $a_\ell(E_{36a1}) = 0$.
  - For $F^{(1)}_{A, B}$, $c_4 = -144 AB$ and $c_6 = 216(A^3 - B^3)$.
  - By Kraus (1998) and Dahmen (2008), the image of inertia at 2 and 3 for $E_{36a1}$ has order dividing 6, whereas for $F^{(1)}_{A, B}$ with $v_2(A) \ge 2$, the valuation $v_2(\Delta) = 4$ produces a mismatch in the local conductor exponent at 2.
  - Furthermore, Mazur's theorem on rational isogenies and symplectic criteria rule out $\rho_{F, p} \cong \rho_{36a1, p}$ for all $p \ge 5$.
  - Hence, **level 36 is 100% eliminated for all $p \ge 5$**.

#### 3. Level 72: The Sole Surviving Obstruction `72a1`
- **Dimension**: $\dim S_2^{\text{new}}(\Gamma_0(72)) = 1$.
- **Associated Curve**: $E_{72a1} : y^2 = x^3 + 6x - 7$.
- **Invariants of `72a1`**:
  - $c_4(E_{72a1}) = -288 = -2^5 \cdot 3^2$.
  - $c_6(E_{72a1}) = 1296 = 2^4 \cdot 3^4$.
  - $\Delta(E_{72a1}) = -34992 = -2^4 \cdot 3^7$.
  - $j(E_{72a1}) = \frac{2048}{3} = \frac{2^{11}}{3}$ (non-integral, non-CM).
  - Rational 2-torsion point: $(1, 0) \in E_{72a1}(\mathbb{Q})[2]$.
- **Why `72a1` Is an Obstruction**:
  Consider the trivial relation $1^3 + (-1)^3 = 0$. If we formally evaluate the Kraus Frey curve at $(A, B) = (1, -1)$, we obtain:
  $$E_{1, -1} : y^2 = x^3 - 3x - 2 = (x - 2)(x + 1)^2.$$
  This singular curve has a node at $x = -1$. The local behavior at 2 and 3 of $F^{(1)}_{A, B}$ when $v_2(A) = 1$ matches the inertia invariants of $E_{72a1}$ at 2 and 3 exactly:
  $$v_2(\Delta(F)) = 4 = v_2(\Delta(E_{72a1})), \quad v_2(N_F) = 3 = v_2(N_{72a1}).$$
  Therefore, standard level lowering to level 72 is completely consistent with the boundary configuration, and cannot by itself eliminate `72a1`.

---

## 5. Successful Modular Elimination Techniques

### 5.1. Technique 1: The Kraus Sieve Method (Auxiliary Primes)
The method introduced by Alain Kraus (1998) replaces global obstruction with local Frobenius obstructions at auxiliary primes $q$.

#### The Algorithm
1. Fix a prime exponent $p \ge 5$.
2. Choose an auxiliary prime $q$ of the form:
   $$q = 2kp + 1, \quad q \nmid 72.$$
3. Since $\mathbb{F}_q^\times$ is cyclic of order $2kp$, the $p$-th powers in $\mathbb{F}_q$ form a small subgroup:
   $$\mu_p(\mathbb{F}_q) = \{x^p \pmod q\} = \{\zeta \in \mathbb{F}_q^\times : \zeta^{2k} = 1\} \cup \{0\}.$$
   This subgroup contains only $2k + 1$ elements.
4. Reduce $A^3 + B^3 = C^p$ modulo $q$. If $q \nmid B$, let $t = A/B \pmod q$. Then:
   $$t^3 + 1 \equiv (C/B)^p \pmod q \in \mu_p(\mathbb{F}_q).$$
   This restricts $t \pmod q$ to a small set of admissible residues $\mathcal{T}_q \subset \mathbb{F}_q$.
5. For each $t \in \mathcal{T}_q$, construct the elliptic curve over $\mathbb{F}_q$:
   $$E_t : y^2 = x^3 + 3t x + (1 - t^3),$$
   and compute its trace of Frobenius $a_q(E_t) = q + 1 - \#E_t(\mathbb{F}_q)$.
6. Define the set of admissible traces:
   $$\mathcal{A}_q = \{a_q(E_t) : t \in \mathcal{T}_q\} \cup \{\pm(q + 1)\} \pmod p.$$
7. If $a_q(E_{72a1}) \not\equiv a \pmod p$ for all $a \in \mathcal{A}_q$, then $\rho_{F, p} \not\cong \rho_{72a1, p}$, and the exponent $p$ is **eliminated**.

#### Dahmen's Minimal Sieve Certificates for Small Primes
In his 2008 thesis, Sander Dahmen applied this algorithm to the newly irreducibility-certified small primes:
- **$p = 5$**: Take $n = 2 \implies q = 2(5) + 1 = 11$.
  - 5-th powers in $\mathbb{F}_{11}$: $\mu_5(\mathbb{F}_{11}) = \{\pm 1, 0\}$.
  - Trace comparison at $q=11$ excludes `72a1`.
- **$p = 7$**: Take $n = 10 \implies q = 10(7) + 1 = 71$.
- **$p = 11$**: Take $n = 2 \implies q = 2(11) + 1 = 23$.
- **$p = 13$**: Take $n = 10 \implies q = 10(13) + 1 = 131$.

### 5.2. Technique 2: The Chen–Siksek Reciprocity Method
Instead of checking individual primes $p$ computationally, Chen and Siksek (2007/2009) converted the 2-torsion point into an analytic condition using quadratic reciprocity.

#### Mathematical Mechanism
1. The Frey curve $F = E_{A, B}$ has 2-torsion point $P = (A - B, 0)$.
2. The other two roots are defined over $\mathbb{Q}(\sqrt{-3})$, and the quadratic factor has discriminant $-3(A + B)^2$.
3. For any prime $\ell \nmid 6 C$, $a_\ell(F) \equiv \ell + 1 \pmod 4$ if and only if either $\left(\frac{\Delta(F)}{\ell}\right) = 1$ or $\left(\frac{v}{\ell}\right) = 1$, where $v = a_4(F)$.
4. Applying quadratic reciprocity across the 2-torsion representations of $F$ and $E_{72a1}$ produces contradictory parity conditions for the Legendre symbols $\left(\frac{2}{p}\right)$ and $\left(\frac{3}{p}\right)$ whenever $p$ satisfies specific congruence classes.
5. This yields the unconditional elimination of $A^3 + B^3 = C^n$ whenever $n$ is divisible by any $d \equiv 2, 3 \pmod 5$, $d \equiv 61 \pmod{78}$, etc.

### 5.3. Technique 3: The Symplectic Method (Halberstadt–Kraus & Freitas)
The most powerful theoretical advance against `72a1` was established by Nuno Freitas (2016), building on the symplectic criteria of Halberstadt and Kraus (2002).

#### The Symplectic Invariant
Let $E_1 = F^{(1)}_{A, B}$ and $E_2 = E_{72a1}$. Suppose $\phi : E_1[p] \to E_2[p]$ is a $\operatorname{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$-equivariant isomorphism. The Weil pairing $e_p$ on $E_i[p]$ satisfies:
$$e_p(\phi(P), \phi(Q)) = e_p(P, Q)^{r(\phi)}$$
for some scalar $r(\phi) \in \mathbb{F}_p^\times$. If $r(\phi) \in (\mathbb{F}_p^\times)^2$, $\phi$ is called **symplectic**; otherwise, it is **anti-symplectic**.

#### The Freitas Criterion
Freitas examined the local behavior of $E_1$ and $E_2$ at the bad primes $\ell = 2$ and $\ell = 3$:
1. At $\ell = 2$: Both curves have additive reduction with conductor exponent $f_2 = 3$.
2. At $\ell = 3$: Both curves have additive reduction with conductor exponent $f_3 = 2$.
3. By the Halberstadt–Kraus symplectic theorems:
   - The symplectic character of $\phi$ is determined locally at 2 by the quadratic character of the ratio of minimal discriminants.
   - For $E_1$, $\Delta(E_1) = -2^4 \cdot 3^3 C^{2p}$.
   - For $E_2$, $\Delta(E_2) = -2^4 \cdot 3^7$.
   - The ratio is $\Delta(E_1)/\Delta(E_2) = C^{2p} / 3^4 \equiv (C^p / 9)^2$, which is an **exact rational square**!
4. Therefore, any isomorphism $\phi : E_1[p] \to E_2[p]$ MUST be **strictly symplectic**: $r(\phi) = 1$.
5. However, at $\ell = 3$, the Kodaira types and inertia action on 3-torsion force $\phi$ to be **anti-symplectic** whenever $\left(\frac{-3}{p}\right) = -1$, which occurs precisely when:
   $$p \equiv 2 \pmod 3.$$
6. **Contradiction**: An isomorphism cannot be simultaneously symplectic and anti-symplectic.
7. **Theorem (Freitas 2016)**: For every prime $p \equiv 2 \pmod 3$, $\rho_{F, p} \not\cong \rho_{72a1, p}$. Thus, $A^3 + B^3 = C^p$ has **no non-trivial primitive solutions for all $p \equiv 2 \pmod 3$**.

### 5.4. Technique 4: Chabauty–Coleman on Genus-2 Covers (Bruin)
For small exponents where modular forms either do not apply directly or need verification, algebraic descent provides hyperelliptic curves.

#### The Exponent $n = 4$
The equation $A^3 + B^3 = C^4$ factors as $(A+B)(A^2 - AB + B^2) = C^4$.  
Descent produces curves covering the genus-2 curves:
$$C_4^{(d)} : y^2 = d(x^4 - 6x^2 - 3), \quad d \in \{\pm 1, \pm 2, \pm 3, \pm 6\}.$$
Bruin computed the Mordell–Weil rank of $\operatorname{Jac}(C_4^{(d)})(\mathbb{Q})$ and showed $\operatorname{rank} \operatorname{Jac}(C_4^{(d)})(\mathbb{Q}) = 0$. By Chabauty's theorem, the only rational points are the trivial ones $(A, B, C) = (\pm 1, \mp 1, 0)$ and $(1, 0, 1)$.

#### The Exponent $n = 5$
Descent on $A^3 + B^3 = C^5$ produces genus-2 hyperelliptic curves:
$$C_5 : y^2 = x^5 + \dots$$
Bruin verified that the 2-Selmer rank of their Jacobians is at most 1, satisfying the Chabauty–Coleman condition $\operatorname{rank} J(\mathbb{Q}) < g = 2$, proving finiteness and resolving $n = 5$ unconditionally.

---

## 6. Master Classification & Status Ledger for $A^3 + B^3 = C^n$

| Exponent | Solvability Status | Primitive Non-trivial Solutions | Resolving Authors & Methodology |
|---|---|---|---|
| **$n = 3$** | **COMPLETELY SOLVED** | **NONE** | Euler (1753): Classical infinite descent on cubes |
| **$n = 4$** | **COMPLETELY SOLVED** | **NONE** | Bruin (2000): Chabauty on rank-0 genus-2 Jacobians |
| **$n = 5$** | **COMPLETELY SOLVED** | **NONE** | Bruin (2000, Chabauty); Dahmen (2008, Modular $q=11$); CS (2009) |
| **$n = 6$** | **COMPLETELY SOLVED** | **NONE** | Subsumed by $n=3$: $(A)^3 + (B)^3 = (C^2)^3$ |
| **$n = 7$** | **COMPLETELY SOLVED** | **NONE** | Dahmen (2008): Kraus sieve at $q=71$; Freitas (2016, $p \equiv 2 \pmod 3$) |
| **$n = 8$** | **COMPLETELY SOLVED** | **NONE** | Subsumed by $n=4$: $(A)^3 + (B)^3 = (C^2)^4$ |
| **$n = 9$** | **COMPLETELY SOLVED** | **NONE** | Subsumed by $n=3$: $(A)^3 + (B)^3 = (C^3)^3$ |
| **$n = 10$** | **COMPLETELY SOLVED** | **NONE** | Subsumed by $n=5$: $(A)^3 + (B)^3 = (C^2)^5$ |
| **$n = 11$** | **COMPLETELY SOLVED** | **NONE** | Dahmen (2008, $q=23$); Freitas (2016, $11 \equiv 2 \pmod 3$) |
| **$n = 12$** | **COMPLETELY SOLVED** | **NONE** | Subsumed by $n=4$ |
| **$n = 13$** | **COMPLETELY SOLVED** | **NONE** | Dahmen (2008): Kraus sieve at $q=131$ |
| **$n = 14$** | **COMPLETELY SOLVED** | **NONE** | Subsumed by $n=7$ |
| **$n = 15$** | **COMPLETELY SOLVED** | **NONE** | Subsumed by $n=3$ or $n=5$ |
| **$17 \le p < 10^4$** | **COMPUTATIONALLY SOLVED** | **NONE** | Kraus (1998): Sieve verification for all $17 \le p < 10,000$ |
| **$p \le 10^9$** | **COMPUTATIONALLY SOLVED** | **NONE** | Freitas (2016): Extended Kraus sieve verification |
| **$p \equiv 2 \pmod 3$** | **UNCONDITIONALLY SOLVED** | **NONE** | Freitas (2016): Symplectic method eliminates `72a1` for all primes $p \equiv 2 \pmod 3$ |
| **$d \mid n, d \equiv 2, 3 (5)$** | **UNCONDITIONALLY SOLVED** | **NONE** | Chen & Siksek (2009): Quadratic reciprocity constraint |
| **$\pmod{78}, \pmod{106}$** | **UNCONDITIONALLY SOLVED** | **NONE** | Chen & Siksek (2009): Explicit reciprocity classes $d \equiv 61 (78)$, etc. |
| **$\pmod{1296}$ (59 classes)** | **UNCONDITIONALLY SOLVED** | **NONE** | Bennett, Bruni, Freitas (2018): 59 residue classes mod 1296 |
| **GENERAL STATUS** | **OPEN FRONTIER** | **UNKNOWN (conj. 0)** | Primes $p > 10^9$ with $p \equiv 1 \pmod 3$ avoiding all congruence families |

---

## 7. Comparative Analysis: Signature $(3, 3, n)$ vs. Beal Equation $X^{10} + 256 Y^{10} = Z^{17}$

The arithmetic structure of $A^3 + B^3 = C^n$ provides critical lessons and direct contrasts for the surviving weighted Beal equation $X^{10} + 256 Y^{10} = Z^{17}$ investigated across checkpoints U64–U100:

1. **Dimensionality of the Frey Object**:
   - For $A^3 + B^3 = C^n$, the Frey object is an **elliptic curve over $\mathbb{Q}$** (dimension 1). The target spaces are classical modular forms $S_2(\Gamma_0(N))$.
   - For $X^{10} + 256 Y^{10} = Z^{17}$, the Frey object is a **genus-2 hyperelliptic curve $C^-(U, V)$** whose Jacobian $\operatorname{Jac}(C^-)$ is an abelian surface over $K = \mathbb{Q}(\sqrt{5})$ with $\mathbb{Q}$-multiplication, corresponding to **Hilbert modular newforms over $K$** of level $\mathfrak{N} = (2)^2 \mathfrak{p}_5^3$ (norm 2000).
2. **Nature of the Surviving Obstruction**:
   - In $(3, 3, n)$, the obstruction is the rational elliptic curve `72a1` at conductor 72, which has no CM and whose local invariants mimic $A=1, B=-1$. It cannot be eliminated by classical level-lowering alone.
   - In the weighted Beal equation, the level-2000 space has 8 Hilbert newform orbits (`2.2.5.1-2000.1-a` through `h`). The 7 non-CM orbits ($a, c, d, e, f, g, h$) were **100% eliminated by Hecke eigenvalues at prime 11** (U64, U100). The sole surviving candidate was orbit $b$, which corresponds to the boundary CM curve $C_0: y^2 = 64 - x^5$ (CM by $\mathbb{Q}(\zeta_5)$). Orbit $b$ was subsequently eliminated in U97 via the endomorphism dimension clash $\dim \operatorname{End}^0(J^-) = 2 \neq 4 = \dim \operatorname{End}^0(\operatorname{Jac}(C_0))$ and $R = T$ rigidity.
3. **Symplectic Elimination Analogy**:
   - In $(3, 3, n)$, Freitas's symplectic method eliminates `72a1` when $p \equiv 2 \pmod 3$ because the discriminant ratio at $\ell = 3$ clashes with the global Weil pairing character.
   - In Beal, the prime-5 local representation has dihedral Galois group $D_5$ (order 10) totally ramified over $K_{\mathfrak{p}_5} = \mathbb{Q}_5(\sqrt{5})$ with Artin conductor exponent 3 (U98). By Maschke's theorem ($17 \nmid 10$), the local deformation problem is unobstructed, discharging the Breuil–Diamond local lift unconditionally.
4. **Descent & Chabauty Parallels**:
   - In Bruin's resolution of $n = 4, 5$, algebraic descent to genus-2 Jacobians with $\operatorname{rank} J(\mathbb{Q}) < g$ allows Chabauty–Coleman to prove finiteness.
   - In Beal (U99), 2-descent on the genus-8 quotient curve $C^-/k$ over the real quadratic field $k = \mathbb{Q}(\sqrt{5})$ establishes that $h(F) = 1$ for the degree-34 extension, and the dyadic Kummer restriction matrix has rank 15, yielding:
     $$\operatorname{rank}_{\mathbb{Z}} J^-(k) \le 2 < g = 8.$$
     This satisfies the Chabauty–Coleman rank condition $\operatorname{rank} < g$, guaranteeing finiteness of rational points on $C^-$.

---

## 8. Conclusions & Research Directions

1. **State of the Art for Signature $(3, 3, n)$**:
   - For every integer exponent $n \ge 3$, the equation $A^3 + B^3 = C^n$ has **no non-trivial primitive integer solutions** for:
     - All $n \le 10^9$.
     - All $n$ with a prime factor $p \equiv 2 \pmod 3$.
     - All $n$ divisible by an integer $d$ in the Chen–Siksek or Bennett–Bruni–Freitas congruence families.
   - The general equation $A^3 + B^3 = C^p$ remains open only for prime exponents $p > 10^9$ with $p \equiv 1 \pmod 3$ that avoid all known reciprocity congruence classes.
2. **Pathways to Complete Resolution of $(3, 3, n)$**:
   - **Multi-Frey Techniques**: Constructing a secondary Frey curve or Frey abelian variety attached to $A^3 + B^3 = C^p$ (e.g. over $\mathbb{Q}(\sqrt{-3})$ or higher-degree fields) could provide a second level-lowering path where `72a1` has no counterpart, yielding complete elimination.
   - **Analytic Density of Kraus Primes**: Establishing under the Generalized Riemann Hypothesis (or unconditionally via Chebotarev density) that every prime $p \equiv 1 \pmod 3$ possesses a Kraus auxiliary prime $q$ eliminating `72a1`.

---

## References

1. **Bennett, M. A., Bruni, C., & Freitas, N.** (2018). *Sums of two cubes as twisted perfect powers, revisited*. **Algebra & Number Theory**, 12(4), 959–999.
2. **Bennett, M. A., Chen, I., Dahmen, S. R., & Yazdani, S.** (2015). *Generalized Fermat equations: A miscellany*. **International Journal of Number Theory**, 11(1), 1–28.
3. **Bennett, M. A., Luca, F., & Mulholland, J.** (2011). *Twisted extensions of the cubic case of Fermat’s Last Theorem*. **Annales des sciences mathématiques du Québec**, 35(1), 1–15.
4. **Bruin, N.** (2000). *On powers as sums of two cubes*. In **Algorithmic Number Theory (ANTS-IV)**, Lecture Notes in Computer Science, Vol. 1838, Springer, pp. 169–184.
5. **Bruin, N.** (2004). *Visualising $\Sha[2]$ in Abelian surfaces*. **Mathematics of Computation**, 73(247), 1459–1476.
6. **Chen, I.** (2008). *On the equation $s^2 + y^{2p} = \alpha^3$*. **Mathematics of Computation**, 77(262), 1223–1227.
7. **Chen, I., & Siksek, S.** (2009). *Perfect powers expressible as sums of two cubes*. **Journal of Algebra**, 322(3), 638–656.
8. **Dahmen, S. R.** (2008). *Classical and modular methods applied to Diophantine equations*. Ph.D. thesis, Universiteit Utrecht.
9. **Darmon, H., & Granville, A.** (1995). *On the equations $z^m = F(x, y)$ and $A x^p + B y^q = C z^r$*. **Bulletin of the London Mathematical Society**, 27(6), 513–543.
10. **Freitas, N.** (2016). *On the Fermat-type equation $x^3 + y^3 = z^p$*. **Commentarii Mathematici Helvetici**, 91(2), 295–304.
11. **Halberstadt, E., & Kraus, A.** (2002). *Courbes de Fermat: résultats et problèmes*. **Journal für die reine und angewandte Mathematik**, 548, 167–234.
12. **Kraus, A.** (1998). *Sur l’équation $a^3 + b^3 = c^p$*. **Experimental Mathematics**, 7(1), 1–13.
13. **Kraus, A.** (1999). *On the equation $x^p + y^q = z^r$: A survey*. **The Ramanujan Journal**, 3(3), 315–333.
