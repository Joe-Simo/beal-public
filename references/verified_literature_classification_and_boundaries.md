# Rigorously Verified Mathematical Classification & Boundaries: Beal & Generalized Fermat-Catalan

This document serves as the permanent reference compendium and exclusion registry for the Beal Conjecture Autonomous Resolution Pipeline. It incorporates all published, peer-reviewed mathematical breakthroughs, classifying them into four distinct categories to prevent redundant re-computation and enforce rigorous mathematical hygiene.

---

## 1. All 10 Known Coprime Solutions (Fermat–Catalan)

Under the generalized Fermat–Catalan equation:
$$A^x + B^y = C^z \quad \text{with } \frac{1}{x} + \frac{1}{y} + \frac{1}{z} < 1 \quad \text{and } \gcd(A, B, C) = 1$$
only **10 distinct primitive integer solutions** have ever been identified in the history of mathematics:

| # | Verified Equation | Exact Arithmetic Identity | Exponent Signature $(x, y, z)$ |
| :-: | :--- | :--- | :---: |
| **1** | $1^m + 2^3 = 3^2$ | $1 + 8 = 9$ | $(m, 3, 2)$ for any $m > 5$ |
| **2** | $2^5 + 7^2 = 3^4$ | $32 + 49 = 81$ | $(5, 2, 4)$ |
| **3** | $7^3 + 13^2 = 2^9$ | $343 + 169 = 512$ | $(3, 2, 9)$ |
| **4** | $2^7 + 17^3 = 71^2$ | $128 + 4,913 = 5,041$ | $(7, 3, 2)$ |
| **5** | $3^5 + 11^4 = 122^2$ | $243 + 14,641 = 14,884$ | $(5, 4, 2)$ |
| **6** | $17^7 + 76,271^3 = 21,063,928^2$ | $410,338,673 + 443,689,476,057,999 = 443,689,886,396,672$ | $(7, 3, 2)$ |
| **7** | $1,414^3 + 2,213,459^2 = 65^7$ | $2,827,145,944 + 4,899,398,579,681 = 4,902,225,725,625$ | $(3, 2, 7)$ |
| **8** | $9,262^3 + 15,312,283^2 = 113^7$ | $794,539,151,528 + 234,466,010,776,089 = 235,260,549,927,617$ | $(3, 2, 7)$ |
| **9** | $43^8 + 96,222^3 = 30,042,907^2$ | $116,823,817,473 + 890,855,219,904,728 = 890,972,043,722,201$ | $(8, 3, 2)$ |
| **10** | $33^8 + 1,549,034^2 = 15,613^3$ | $1,406,408,618,241 + 2,399,506,333,156 = 3,805,914,951,397$ | $(8, 2, 3)$ |

> **Architectural Law (U141 Fermat–Catalan Blindness Test)**: Every single verified coprime solution features an exponent of **2**. Because the Beal Conjecture specifies that all three exponents must satisfy $x, y, z \ge 3$, not a single known solution violates the conjecture. Any elementary condition that holds on all 10 is *exponent-2-blind* and cannot prove Beal on its own.

---

## 2. Infinite Families of Exponents Proven Impossible

Using modularity theorems, Frey-Hellegouarch elliptic curves, and Galois representations (Darmon's program), the literature has established that **zero non-trivial coprime solutions exist** for the following infinite families:

* **$(n, n, n)$ for $n \ge 3$**: Andrew Wiles and Richard Taylor (1995) — *Fermat's Last Theorem*.
* **$(n, n, 2)$ for $n \ge 4$**: Henri Darmon and Loïc Merel (1997) — *Winding quotients and variants of FLT*.
* **$(n, n, 3)$ for $n \ge 3$**: Henri Darmon and Loïc Merel (1997); Bjorn Poonen (1998).
* **$(2, 4, n)$ for $n \ge 4$**: Jordan Ellenberg (2004); Michael Bennett, Ellenberg, and Nathan Ng (2010).
* **$(2, 6, n)$ for $n \ge 3$**: Michael Bennett and Imin Chen (2012).
* **$(2, n, 4)$ for $n \ge 4$**: Michael Bennett and Chris Skinner (2004).
* **$(3, 3, 2n)$ for $n \ge 2$**: Alain Kraus (1998) and Nils Bruin (1999).
* **$(2n, 2n, 5)$ for $n \ge 2$**: Michael Bennett (2006).
* **$(3j, 3k, n)$ for $j, k \ge 2$ and $n \ge 3$**: Michael Bennett, Imin Chen, Sander Dahmen, and Soroosh Yazdani (2015).

---

## 3. Fully Solved Exponent Signatures

Through the Chabauty-Coleman method and descent algorithms over algebraic curves, every integer solution has been classified for these specific exponent triples:

* **$\{2, 3, 7\}$**: Bjorn Poonen, Edward Schaefer, and Michael Stoll (2007) — *Duke Math. J.*.
* **$\{2, 3, 8\}$ and $\{2, 3, 9\}$**: Nils Bruin (1999, 2004).
* **$\{2, 4, 5\}$**: Nils Bruin (2003) — *Compositio Math.*.
* **$\{3, 3, 4\}$ and $\{3, 3, 5\}$**: Alain Kraus (1998); Nils Bruin and Michael Stoll (2009).
* **$\{3, 3, p\}$ for all primes $17 \le p \le 10,000$**: Alain Kraus (1998); Sander Dahmen (2008).
* **$\{2, 2q, 3\}$ for all primes $7 < q < 1,000$ (except $q = 31$)**: Imin Chen and Sander Dahmen (2013).

In every signature above where $x, y, z \ge 3$ (such as $\{3, 3, 4\}$, $\{3, 3, 5\}$, or $\{3, 3, p\}$), published proofs confirm **zero coprime solutions exist**.

---

## 4. Published Computational Search Boundaries

Supercomputing clusters and exhaustive verification engines have established the following empirical frontiers:

* **Adam S. Sikora (University at Buffalo, 2024)**:
  * Minimum exponent = 2: all terms verified up to $2^{71} \approx 2.36 \times 10^{21}$.
  * Minimum exponent = 3: all terms verified up to $2^{80} \approx 1.21 \times 10^{24}$.
  * Minimum exponent = 4: all terms verified up to $2^{100} \approx 1.27 \times 10^{30}$.
  * Exponents $\ge 5$ (up to exponent 113): all terms verified up to $2^{113} \approx 1.04 \times 10^{34}$.
* **Peter Norvig**: Checked all bases $A, B \le 250,000$ for powers $3 \le x, y \le 7$, and all bases up to $10,000$ for powers up to $100$.
* **Dan Vanderkam**: Evaluated all combinations for $A, B, C, x, y, z \le 1,000$.
* **Bill Bradford (Durango Bill)**: Cataloged **51,660 positive non-coprime solutions** up to $C^z \le 10^{28}$, verifying that 100% have $\gcd(A, B, C) \ge 2$.

---

## Directives for the Autonomous Engine

1. **Strict Non-Duplication**: Never re-search or treat as open any signature in Section 2 or Section 3.
2. **Exclusion Validation**: Every candidate or test must check whether its condition is satisfied by the 10 Fermat-Catalan seeds. If so, it is exponent-2 blind.
3. **Frontier Alignment**: Focus search compute strictly outside of and complementary to the Sikora 2024 and Norvig domains.
