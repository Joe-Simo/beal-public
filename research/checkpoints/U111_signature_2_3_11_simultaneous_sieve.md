# U111: Multi-Prime Simultaneous Sieve for Signature (2, 3, 11)

**Date**: 2026-09-17  
**Status**: Exact multi-prime simultaneous sieve formulation, density analysis, Catalan residue constraints, and bounded integer verification.  
**Target Equation**: Generalized Fermat equation of signature $(2, 3, 11)$:
$$A^2 + B^3 = C^{11}, \quad \gcd(A, B, C) = 1.$$
**Primary Sources**:
- Henri Darmon and Andrew Granville, *On the equations $z^m = F(x, y)$ and $Ax^p + By^q = Cz^r$*, Bull. London Math. Soc. 27 (1995), 513–543.
- Sander R. Dahmen, *Classical and modular methods applied to Diophantine equations*, PhD Thesis, Universiteit Utrecht (2008).
- Nuno Freitas, Bartosz Naskręcki, and Michael Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. 156 (2020), 77–113.
- Executable Verification Script: [`code/U111_signature_2_3_11_simultaneous_sieve.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_signature_2_3_11_simultaneous_sieve.py)
- Structured Sieve Ledger: [`references/U111_signature_2_3_11_simultaneous_sieve.json`](file://[LOCAL_HOME]/Downloads/beal/references/U111_signature_2_3_11_simultaneous_sieve.json)

---

## 1. Formulation of the Multi-Prime Simultaneous Sieve

### 1.1 Sieve Primes and Modulus
We formulate a simultaneous CRT sieve across the 8 good auxiliary primes:
$$\mathcal{Q} = \{5, 7, 13, 17, 19, 23, 29, 31\}.$$
The global sieve modulus is the squarefree product:
$$M = \prod_{q \in \mathcal{Q}} q = 5 \cdot 7 \cdot 13 \cdot 17 \cdot 19 \cdot 23 \cdot 29 \cdot 31 = 3,038,795,305.$$
The ambient residue space of non-zero pairs $(A, B) \pmod M$ with $\gcd(A, B, M) = 1$ has size:
$$\Omega_M = \prod_{q \in \mathcal{Q}} (q^2 - 1) = 24 \cdot 48 \cdot 168 \cdot 288 \cdot 360 \cdot 528 \cdot 840 \cdot 960 \approx 8.5436 \times 10^{18}.$$

### 1.2 Local Admissibility Conditions at $q \in \mathcal{Q}$
For any primitive integer solution $(A, B, C)$ of $A^2 + B^3 = C^{11}$, its reduction $(a_q, b_q) \equiv (A, B) \pmod q$ must satisfy:
1. **Equation Congruence**:
   $$a_q^2 + b_q^3 \equiv c_q^{11} \pmod q \quad \text{for some } c_q \in \mathbb{F}_q.$$
   Thus $a_q^2 + b_q^3 \in \mu_{11}(\mathbb{F}_q) = \{c^{11} \pmod q : c \in \mathbb{F}_q\}$.
2. **Coprimality**: $(a_q, b_q) \not\equiv (0, 0) \pmod q$.
3. **Trace Compatibility with Newform $f$**:
   - If $a_q^2 + b_q^3 \not\equiv 0 \pmod q$ ($q \nmid C$, good reduction):
     The Kraus Frey curve $E_{(a_q, b_q)}: Y^2 = X^3 + 3b_q X + 2a_q$ has Frobenius trace $a_q(E_{(a_q, b_q)}) = q + 1 - \#E_{(a_q, b_q)}(\mathbb{F}_q)$, which must satisfy:
     $$a_q(E_{(a_q, b_q)}) \equiv a_q(f) \pmod{11}.$$
   - If $a_q^2 + b_q^3 \equiv 0 \pmod q$ ($q \mid C$, multiplicative reduction):
     The newform eigenvalue must satisfy the Deligne/Tate congruence:
     $$a_q(f) \equiv \pm(q + 1) \pmod{11}.$$

---

## 2. Simultaneous Sieve Results Across Candidate Newforms

### 2.1 Local Counts and Global Sieve Density
For each rational newform $f \in S_2^{\mathrm{new}}(432) \cup S_2^{\mathrm{new}}(864)$, we compute the number of locally compatible pairs $N_f(q)$ at each prime $q$, and by the Chinese Remainder Theorem, the total number of simultaneous residue classes:
$$N_f(M) = \prod_{q \in \mathcal{Q}} N_f(q), \quad \rho_f = \frac{N_f(M)}{\Omega_M}.$$

| Form Label | Level | $N(5)$ | $N(7)$ | $N(13)$ | $N(17)$ | $N(19)$ | $N(23)$ | $N(29)$ | $N(31)$ | Total CRT Classes $N_f(M)$ | Sieve Density $\rho_f$ | $\log_{10}(\rho_f)$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **`432_1`** | 432 | 1 | 9 | 12 | 40 | 21 | 5 | 84 | 115 | $4,381,776,000$ | $5.13 \times 10^{-10}$ | $-9.29$ |
| **`432_2`** | 432 | 2 | 4 | 17 | 32 | 45 | 5 | 112 | 75 | $8,225,280,000$ | $9.63 \times 10^{-10}$ | $-9.02$ |
| **`432_3`** | 432 | 2 | 9 | 17 | 28 | 45 | 25 | 112 | 115 | $124,150,320,000$ | $1.45 \times 10^{-8}$ | $-7.84$ |
| **`432_4`** | 432 | 2 | 9 | 17 | 28 | 45 | 25 | 112 | 115 | $124,150,320,000$ | $1.45 \times 10^{-8}$ | $-7.84$ |
| **`432_5`** | 432 | 2 | 4 | 17 | 32 | 45 | 5 | 112 | 75 | $8,225,280,000$ | $9.63 \times 10^{-10}$ | $-9.02$ |
| **`432_6`** | 432 | 1 | 9 | 12 | 40 | 21 | 5 | 84 | 115 | $4,381,776,000$ | $5.13 \times 10^{-10}$ | $-9.29$ |
| **`432_7`** (CM) | 432 | 4 | 4 | 17 | 32 | 48 | 6 | 84 | 115 | $24,215,224,320$ | $2.83 \times 10^{-9}$ | $-8.55$ |
| **`432_8`** (CM) | 432 | 4 | 1 | 17 | 32 | 21 | 6 | 84 | 115 | $2,648,540,160$ | $3.10 \times 10^{-10}$ | $-9.51$ |
| **`864_1`** | 864 | 3 | 9 | 18 | 28 | 21 | 5 | 98 | 100 | $14,002,632,000$ | $1.64 \times 10^{-9}$ | $-8.79$ |
| **`864_2`** | 864 | 3 | 4 | 12 | 32 | 36 | 5 | 98 | 90 | $7,315,660,800$ | $8.56 \times 10^{-10}$ | $-9.07$ |
| **`864_3`** | 864 | 3 | 4 | 12 | 32 | 36 | 5 | 98 | 90 | $7,315,660,800$ | $8.56 \times 10^{-10}$ | $-9.07$ |
| **`864b1`** (Form 4) | 864 | 3 | 9 | 18 | 28 | 21 | 5 | 98 | 100 | $14,002,632,000$ | $1.64 \times 10^{-9}$ | $-8.79$ |
| **`864_5`** | 864 | 2 | 9 | 12 | 40 | 36 | 5 | 84 | 75 | $9,797,760,000$ | $1.15 \times 10^{-9}$ | $-8.94$ |
| **`864_6`** | 864 | 2 | 9 | 12 | 40 | 36 | 5 | 84 | 75 | $9,797,760,000$ | $1.15 \times 10^{-9}$ | $-8.94$ |
| **`864_7`** | 864 | 2 | 9 | 12 | 40 | 36 | 5 | 84 | 75 | $9,797,760,000$ | $1.15 \times 10^{-9}$ | $-8.94$ |
| **`864a1`** (Form 8) | 864 | 2 | 9 | 12 | 40 | 36 | 5 | 84 | 75 | $9,797,760,000$ | $1.15 \times 10^{-9}$ | $-8.94$ |
| **`864_9`** | 864 | 3 | 9 | 18 | 28 | 21 | 5 | 98 | 100 | $14,002,632,000$ | $1.64 \times 10^{-9}$ | $-8.79$ |
| **`864c1`** (Form 10) | 864 | 3 | 4 | 12 | 32 | 36 | 5 | 98 | 90 | $7,315,660,800$ | $8.56 \times 10^{-10}$ | $-9.07$ |
| **`864_11`** | 864 | 3 | 4 | 12 | 32 | 36 | 5 | 98 | 90 | $7,315,660,800$ | $8.56 \times 10^{-10}$ | $-9.07$ |
| **`864_12`** | 864 | 3 | 9 | 18 | 28 | 21 | 5 | 98 | 100 | $14,002,632,000$ | $1.64 \times 10^{-9}$ | $-8.79$ |
| **$E_{\mathrm{Cat}}$** | 1728 | 3 | 9 | 18 | 28 | 21 | 5 | 98 | 100 | $14,002,632,000$ | $1.64 \times 10^{-9}$ | $-8.79$ |
| **`288a1`** (CM) | 288 | 1 | 6 | 17 | 28 | 36 | 6 | 49 | 100 | $3,022,790,400$ | $3.54 \times 10^{-10}$ | $-9.45$ |

### 2.2 Sieve Effectiveness Analysis
1. **Dramatic Density Reduction**: The multi-prime simultaneous sieve shrinks the ambient pair space by **9 orders of magnitude** ($\rho_f \approx 10^{-9}$). Over $99.99999985\%$ of all candidate residue classes modulo $M$ are eliminated.
2. **Local Solvability vs Global Solvability**:
   Notice that $N_f(q) > 0$ for every prime $q \in \mathcal{Q}$ and every newform $f$.
   Consequently, the local sieve *alone* cannot completely eliminate any of these 22 rational newforms. This is the precise arithmetic obstruction identified by Freitas--Naskręcki--Stoll (2020):
   Each candidate form possesses local points at all small primes, so local trace congruences cannot rule them out. Eliminating `864a1`, `864c1`, etc. fundamentally requires global Diophantine tools, specifically **Selmer Group Chabauty** on $X_0(11)$ over degree-12 number fields $K_E$.

---

## 3. Structural Residue Constraints on the Catalan Form (`864b1` / $E_{\mathrm{Cat}}$)

The Catalan identity $3^2 + (-2)^3 = 1^{11}$ ensures that the Catalan solution $(A, B) = (3, -2)$ unconditionally survives the sieve at every prime $q$.
Analyzing the allowable residue classes reveals powerful local rigidity:

### 3.1 Strict Coordinate Locking at $q = 5$
At $q = 5$, there are exactly 3 compatible pairs for $E_{\mathrm{Cat}}$ ($a_5 = -2$):
$$\mathcal{S}_5 = \{(0, 3), (2, 3), (3, 3)\} \subset \mathbb{F}_5^2.$$
**Theorem (Universal $B$-Coordinate Locking at 5)**:
Every single admissible pair satisfies $B \equiv 3 \equiv -2 \pmod 5$.
Therefore, any primitive integer solution $(A, B, C)$ associated with the Catalan form **MUST satisfy $B \equiv -2 \pmod 5$**!

### 3.2 Euler Residue Collapse at $q = 23$
At $q = 23$, $\gcd(11, 23 - 1) = 11$, forcing $C^{11} \equiv \left(\frac{C}{23}\right) \in \{0, 1, 22\} \pmod{23}$.
Out of 528 non-zero pairs in $\mathbb{F}_{23}^2$, only **5 pairs** are compatible with the Catalan trace $a_{23} = -6$:
$$\mathcal{S}_{23} = \{(2, 11), (3, 21), (8, 8), (15, 3), (18, 22)\} \subset \mathbb{F}_{23}^2.$$
- The pair $(3, 21) \equiv (3, -2) \pmod{23}$ is the exact reduction of the Catalan solution!
- For every one of these 5 pairs, $A^2 + B^3 \equiv \pm 1 \pmod{23}$ is satisfied!

---

## 4. Bounded Integer Search in $[-2000, 2000] \times [-200, 200]$

To test whether any spurious integer solutions survive the simultaneous sieve, [`code/U111_signature_2_3_11_simultaneous_sieve.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_signature_2_3_11_simultaneous_sieve.py) performed an exhaustive search across the box:
$$\mathcal{B} = \{(A, B) \in \mathbb{Z}^2 : |A| \le 2000, |B| \le 200, \gcd(A, B) = 1\}.$$
Total pairs tested in box: $\approx 1.6 \times 10^6$.

### 4.1 Search Results by Form

| Candidate Form | Expected Spurious Points ($4XY \cdot \rho$) | Actual Integer Points Found in Box | Identified Exact Solution |
|:---|:---:|:---:|:---|
| **$E_{\mathrm{Cat}}$** (`864b1` twist) | $1.6 \times 10^6 \times 1.64 \times 10^{-9} \approx 0.0026$ | **Exactly 1** | **$(3, -2)$** ($3^2 + (-2)^3 = 1^{11}$) |
| **`288a1`** | $1.6 \times 10^6 \times 3.54 \times 10^{-10} \approx 0.0006$ | **Exactly 1** | **$(0, 1)$** ($0^2 + 1^3 = 1^{11}$) |
| **`864a1`** | $1.6 \times 10^6 \times 1.15 \times 10^{-9} \approx 0.0018$ | **0** (Empty) | None |
| **`864c1`** | $1.6 \times 10^6 \times 8.56 \times 10^{-10} \approx 0.0014$ | **0** (Empty) | None |
| **`432_1`** | $1.6 \times 10^6 \times 5.13 \times 10^{-10} \approx 0.0008$ | **0** (Empty) | None |
| **`432_2`** | $1.6 \times 10^6 \times 9.63 \times 10^{-10} \approx 0.0015$ | **0** (Empty) | None |
| **`432_7`** (CM) | $1.6 \times 10^6 \times 2.83 \times 10^{-9} \approx 0.0045$ | **0** (Empty) | None |

### 4.2 Conclusions from Bounded Search
1. **Uniqueness of Catalan**: The simultaneous sieve across the 8 primes isolates the Catalan solution $(3, -2)$ as the **unique integer pair** matching $E_{\mathrm{Cat}}$ within the search box.
2. **Uniqueness of Trivial Solution**: The sieve isolates $(0, 1)$ as the **unique integer pair** matching `288a1`.
3. **Total Emptiness of Non-Solution Forms**: All other candidate forms (`864a1`, `864c1`, and all forms at level 432) have **zero integer points** in the search region.

---

## 5. Verification Artifacts

1. **Python Sieve Script**:
   [`code/U111_signature_2_3_11_simultaneous_sieve.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_signature_2_3_11_simultaneous_sieve.py)
   - Precomputes all local Frey traces across the 8 primes.
   - Computes exact CRT counts $N_f(M)$ and densities $\rho_f$ for all 22 rational newforms.
   - Proves $B \equiv -2 \pmod 5$ is locked for Catalan.
   - Executes the bounded integer search and verifies the exact isolation of $(3, -2)$ and $(0, 1)$.
   - Clean execution with return code 0.
2. **Structured JSON Ledger**:
   [`references/U111_signature_2_3_11_simultaneous_sieve.json`](file://[LOCAL_HOME]/Downloads/beal/references/U111_signature_2_3_11_simultaneous_sieve.json)
   - Contains all numerical counts $N(q)$, global counts $N(M)$, densities, Catalan residue lists, and search findings.
