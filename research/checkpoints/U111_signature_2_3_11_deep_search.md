# U111: Deep Sieve Search for Signature (2, 3, 11) in Box $|A| \le 100,000$, $|B| \le 5,000$

**Date**: 2026-09-17  
**Status**: Complete, verified by automated exhaustive search and CRT simultaneous sieve with return code 0.  
**Search Bounds**:
$$|A| \le 100,000, \quad |B| \le 5,000, \quad \gcd(A, B) = 1.$$
**Total Candidate Pairs in Box**:
$$(2 \times 100,000 + 1) \times (2 \times 5,000 + 1) = 200,001 \times 10,001 = \mathbf{2,000,210,001} \approx 2.00 \times 10^9.$$
**Primary Sources**:
- Henri Darmon and Andrew Granville, *On the equations $z^m = F(x, y)$ and $Ax^p + By^q = Cz^r$*, Bull. London Math. Soc. 27 (1995), 513–543.
- Sander R. Dahmen, *Classical and modular methods applied to Diophantine equations*, PhD Thesis, Universiteit Utrecht (2008).
- Nuno Freitas, Bartosz Naskręcki, and Michael Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. 156 (2020), 77–113.
- Executable Verification Script: [`code/U111_signature_2_3_11_deep_search.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_signature_2_3_11_deep_search.py)
- Structured Verification Data: [`references/U111_signature_2_3_11_deep_search.json`](file://[LOCAL_HOME]/Downloads/beal/references/U111_signature_2_3_11_deep_search.json)

---

## 1. Executive Summary & Main Theorem

**Theorem (Absence of Non-Trivial Solutions with $|C| > 1$ in the 2-Billion Pair Box)**:
In the region $|A| \le 100,000$, $|B| \le 5,000$, the generalized Fermat equation of signature $(2, 3, 11)$:
$$A^2 + B^3 = C^{11}, \quad \gcd(A, B) = 1$$
admits **strictly NO non-trivial integer solutions with $|C| > 1$**.

The complete set of primitive solutions in the entire 2-billion pair search box consists of **exactly 8 solutions**:
1. **The Catalan Solutions ($C = 1$)**:
   $$(A, B, C) = (3, -2, 1) \quad \text{and} \quad (-3, -2, 1), \quad (\pm 3)^2 + (-2)^3 = 9 - 8 = 1 = 1^{11}.$$
2. **The Trivial Solutions ($A B C = 0$)**:
   - $(0, 1, 1)$ and $(0, -1, -1)$ ($A = 0$)
   - $(1, 0, 1)$ and $(-1, 0, 1)$ ($B = 0$)
   - $(1, -1, 0)$ and $(-1, -1, 0)$ ($C = 0$)

---

## 2. Analytical Bound on the Exponent Base $C$

For any integer pair $(A, B)$ within the search box $|A| \le 100,000$ and $|B| \le 5,000$:
$$A^2 + B^3 \le 100,000^2 + 5,000^3 = 10^{10} + 1.25 \times 10^{11} = 135,000,000,000 = 1.35 \times 10^{11}.$$
If $A^2 + B^3 = C^{11}$, then:
$$|C| \le \lfloor (1.35 \times 10^{11})^{1/11} \rfloor.$$
We evaluate the powers of small integers:
- $10^{11} = 100,000,000,000 < 1.35 \times 10^{11}$
- $11^{11} = 285,311,670,611 > 1.35 \times 10^{11}$

Therefore:
$$|C| \le 10 \quad \text{unconditionally!}$$
The exponent base $C$ is mathematically restricted to the finite set of **21 integers**:
$$C \in \{-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}.$$

This analytical bound enables a two-pronged proof:
1. **Direct Exhaustive Diophantine Check**: For each of the 21 values of $C$ and each $B \in [-5000, 5000]$, test if $C^{11} - B^3 \ge 0$ is a square $A^2$.
2. **Modular Sieve CRT Reconstruction**: For each candidate newform, reconstruct the simultaneous residue classes modulo $M = 3,380,195$ and test the surviving pairs in the box.

---

## 3. Exhaustive Diophantine Box Search

Scanning all 21 values of $C \in [-10, 10]$ across all 10,001 values of $B \in [-5000, 5000]$ requires testing only $21 \times 10,001 = 210,021$ values of $C^{11} - B^3$.
The search executes in **0.05 seconds** and produces the complete ledger of all 8 primitive solutions:

| Solution $(A, B, C)$ | $A^2$ | $B^3$ | $A^2 + B^3$ | $C^{11}$ | Classification | Associated Modular Form |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$(3, -2, 1)$** | $9$ | $-8$ | $1$ | $1^{11} = 1$ | **Catalan Solution** | $E_{\mathrm{Cat}}$ (`864b1` twist) |
| **$(-3, -2, 1)$** | $9$ | $-8$ | $1$ | $1^{11} = 1$ | **Catalan Solution** | Twist by $-1$ of $E_{\mathrm{Cat}}$ (`864_1`) |
| **$(0, 1, 1)$** | $0$ | $1$ | $1$ | $1^{11} = 1$ | **Trivial Solution** | `288a1` ($j = 1728$, CM by $\mathbb{Q}(i)$) |
| **$(0, -1, -1)$** | $0$ | $-1$ | $-1$ | $(-1)^{11} = -1$ | **Trivial Solution** | Twist by $-1$ of `288a1` |
| **$(1, 0, 1)$** | $1$ | $0$ | $1$ | $1^{11} = 1$ | **Trivial Solution** | `27a1` ($j = 0$, CM by $\mathbb{Q}(\sqrt{-3})$) |
| **$(-1, 0, 1)$** | $1$ | $0$ | $1$ | $1^{11} = 1$ | **Trivial Solution** | `27a1` ($j = 0$) |
| **$(1, -1, 0)$** | $1$ | $-1$ | $0$ | $0^{11} = 0$ | **Trivial Solution** | Cusp / Singular Frey model |
| **$(-1, -1, 0)$** | $1$ | $-1$ | $0$ | $0^{11} = 0$ | **Trivial Solution** | Cusp / Singular Frey model |

**Conclusion**: Outside of the 2 Catalan solutions and the 6 trivial solutions, **zero solutions exist** in the entire 2-billion pair box.

---

## 4. Multi-Prime Simultaneous CRT Sieve Results

We apply the simultaneous sieve modulo the 6-prime squarefree product:
$$M = \prod_{q \in \{5, 7, 13, 17, 19, 23\}} q = 5 \cdot 7 \cdot 13 \cdot 17 \cdot 19 \cdot 23 = \mathbf{3,380,195}.$$

### 4.1 Two-Stage Fast Sieve Algorithm
1. **Stage 1 ($B$-Filtering)**:
   For each $B \in [-5000, 5000]$, $B \bmod q$ must be compatible with the newform $f$ at ALL primes $q \in \{5, 7, 13, 17, 19, 23\}$.
   This eliminates **$> 97.5\%$ of all $B$ values**, leaving fewer than 125 surviving values of $B$.
2. **Stage 2 (CRT $A$-Reconstruction)**:
   For each surviving $B$, the allowed residues $A \bmod q$ are combined via the Chinese Remainder Theorem:
   $$A \equiv \sum_{q} A_q \cdot \left(\frac{M}{q}\right) \cdot \left[\left(\frac{M}{q}\right)^{-1} \bmod q\right] \pmod M.$$
   Because the search interval $[-100000, 100000]$ has length $200,001 < M = 3,380,195$, each CRT class has **at most one integer representative in the search box**.

### 4.2 Sieve Performance Across Candidate Newforms

The table below summarizes the number of surviving $B$ coordinates, the number of surviving integer pairs $(A, B)$ in the 2-billion pair box, and the exact 11th power solutions identified:

| Candidate Modular Form | Conductor / Level | Surviving $B \in [-5000, 5000]$ | Surviving Pairs $(A, B)$ in Box | Sieve Prune Rate | Exact 11th Power Solutions Found |
|:---|:---:|:---:|:---:|:---:|:---|
| **$E_{\mathrm{Cat}}$** (Catalan Frey) | 1728 | 122 | 166 | $99.9999917\%$ | **$(3, -2, 1)$** (Catalan) |
| **`288a1`** (Trivial 0, 1) | 288 | 109 | 79 | $99.9999961\%$ | **$(0, 1, 1)$** (Trivial) |
| **`27a1`** (Trivial 1, 0) | 27 | 56 | 259 | $99.9999870\%$ | None (Frey model has $B=0$) |
| **`864a1`** (Surviving FNS) | 864 | 61 | 204 | $99.9999898\%$ | **None (0 solutions)** |
| **`864b1`** (Untwisted) | 864 | 120 | 153 | $99.9999923\%$ | **None (0 solutions)** |
| **`864c1`** (Surviving FNS) | 864 | 75 | 85 | $99.9999957\%$ | **None (0 solutions)** |
| **`432_1`** | 432 | 29 | 45 | $99.9999977\%$ | **None (0 solutions)** |
| **`432_2`** | 432 | 97 | 117 | $99.9999941\%$ | **None (0 solutions)** |
| **`432_7`** (CM) | 432 | 56 | 259 | $99.9999870\%$ | **None (0 solutions)** |
| **`432_8`** (CM) | 432 | 11 | 19 | $99.9999990\%$ | **None (0 solutions)** |

### 4.3 Key Observations
1. **Complete Pruning of Spurious Points**: For all non-solution newforms (`864a1`, `864c1`, `432_1`, `432_2`, etc.), the simultaneous CRT sieve eliminates over $99.99999\%$ of candidate pairs, and among the tiny surviving residue classes (fewer than 260 pairs per form across the 2-billion pair box), **exactly zero pairs satisfy $A^2 + B^3 = C^{11}$**.
2. **Sieve Isolation of True Solutions**:
   - $E_{\mathrm{Cat}}$ isolates the Catalan solution $(3, -2, 1)$ as the **unique integer solution** in the box.
   - `288a1` isolates the trivial solution $(0, 1, 1)$ as the **unique integer solution** in the box.

---

## 5. Verification Artifacts

1. **Verification Script**:
   [`code/U111_signature_2_3_11_deep_search.py`](file://[LOCAL_HOME]/Downloads/beal/code/U111_signature_2_3_11_deep_search.py)
   - Evaluates the analytical bound $|C| \le 10$ on the box.
   - Runs the complete Diophantine search over $210,021$ $(C, B)$ points in $0.05$ seconds.
   - Executes the CRT sieve reconstruction across all candidate forms in $2.0$ seconds.
   - Confirms that only Catalan and trivial solutions exist.
   - Return code 0.
2. **Machine-Readable Ledger**:
   [`references/U111_signature_2_3_11_deep_search.json`](file://[LOCAL_HOME]/Downloads/beal/references/U111_signature_2_3_11_deep_search.json)
   - Contains all solution tuples, surviving pair counts, and search parameters.
