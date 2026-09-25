# U751: literature scope for the residual (3,3,p) equation

**Date checked:** 2026-09-24

**Status:** bounded primary-source audit; no checked theorem eliminates every untwisted primitive solution with prime \(p>10^9\), \(p\equiv1\pmod3\), and \(p\nmid C\).

## Exact remaining slice

The local Beal reductions isolate

\[
A^3+B^3=C^p,\qquad \gcd(A,B,C)=1,\qquad
p\text{ prime},\ p>10^9,\ p\equiv1\pmod3,\ p\nmid C.
\]

The separate \(p\mid C\) case is eliminated in U725 for \(p\ge17\). The surviving \(p\nmid C\), \(p\equiv1\pmod3\) case also has the noncube and Lucas restrictions in U737 and U744; those are necessary conditions, not an exclusion theorem.

## What the checked primary results cover

1. **Chen–Siksek, Theorem 1, and Bennett–Bruni–Freitas, Theorem 1.1.** They exclude the untwisted equation in explicit exponent congruence classes and in the finite range \(3\le n\le10^9\). The congruence classes do not cover every prime \(p\equiv1\pmod3\); the papers do not assert an all-prime result for the residual class.

2. **Freitas (2016), Theorem 3.** For prime \(p\ge17\), it excludes primitive nontrivial solutions when \(\left(\frac{-3}{p}\right)=-1\), equivalently \(p\equiv2\pmod3\). This does not cover \(p\equiv1\pmod3\).

3. **Bennett–Bruni–Freitas, Theorems 1.2–1.4.** Their other modular results treat the distinct twisted equation \(A^3+B^3=q^\alpha C^p\) with prime \(q\ge5\); they do not specialize to the untwisted coefficient \(q=1\).

4. **Kraus–Freitas–Sánchez-Rodríguez (2025), Theorems 1.1–1.4.** This develops local symplectic criteria for mod-\(p\) congruences of elliptic-curve torsion representations and illustrates them on bounded-conductor curves. It gives no theorem eliminating the full untwisted (3,3,p) residual slice.

These sources close many finite and congruence-selected cases, but leave the stated infinite exponent class outside their theorem statements. This is a scoped literature audit, not a proof that no theorem exists anywhere.

## Cross-problem consequence

The residual Beal route needs a uniform arithmetic statement, such as a bound on the varying Lucas parameters/cofactor or a trace-avoidance theorem for every residual \(p\). Classical RH's prime-counting estimate and the checked GRH least-prime estimates do not supply this; U750 shows the available bounds miss the required Hasse window and still leave the \(q\)-dependent trace-avoidance condition. The local Hodge–BSD and P=NP routes also supply no uniform cutoff for this exponent slice.

Primary sources: [Chen–Siksek](https://samirsiksek.github.io/siksek.github.io/papers/qr8.pdf), [Bennett–Bruni–Freitas](https://arxiv.org/html/1702.07827), [Freitas](https://ems.press/content/serial-article-files/43415?nt=1), [Kraus–Freitas–Sánchez-Rodríguez](https://arxiv.org/html/2509.19938v2).

Local inputs: [U725](U725_p_divides_base_level24_local_obstruction.md), [U737](U737_cm_isogeny_cube_branch_parity_exclusion.md), [U744](U744_lucas_aggregate_and_p2_congruence.md), and [U750](U750_ap_prime_bounds_miss_kraus_hasse_window.md).
