# U96: Azon Theorem 5.23 requires Hypothesis 5 and invokes Breuil--Diamond directly; no shortcut bypasses the local-lift construction

**Status: source-verified modular-route audit. The weighted equation and Beal's conjecture remain unresolved.**

Research date: 2026-09-17. Inspected primary source: Martin Azon, *Effective Darmon's program for the generalised Fermat equation*, arXiv:2504.01967v2, 2025-07-03.

## 1. Resolution of the U95 binary alternative

U95 proposed testing whether Azon's level-lowering result (referenced as Theorem 5.22 in the paper's overview) could apply directly to the corrected negative twist and our specialization `(r,r,p)=(5,5,17)`, thereby bypassing the explicit reconstruction of the Breuil--Diamond local characteristic-zero lifts mapped in U94.

A direct audit of the full preprint arXiv:2504.01967v2 resolves this question definitively:

1. In the text of Section 5.3.3, label 5.22 is **Definition 5.22** (defining the conductor factor $\mathfrak{n}_{\operatorname{tor},\not\equiv 0 (p)}$), and the actual level-lowering theorem is **Theorem 5.23**.
2. Theorem 5.23 explicitly assumes **Hypothesis 5**.
3. For our weighted equation $X^{10}+256Y^{10}=Z^{17}$, **Hypothesis 5 fails identically**.
4. The proof of Theorem 5.23 does not establish an independent level-lowering mechanism; it literally applies Breuil--Diamond [BD14, Theorem 3.2.2] under the umbrella of Hypothesis 5.

Therefore, Azon's work does not provide an automatic shortcut around Breuil--Diamond Theorem 3.2.2. The explicit local-lift construction at the prime over 5 remains the genuine, inescapable mathematical obligation.

## 2. Detailed audit of Azon Theorem 5.23 and Hypothesis 5

In Azon's notation, Hypothesis 5 states:

> **Hypothesis 5.** *There is at least one prime number $q' \nmid 2r$ such that $\nu_{q'} < 0$, $\nu_{q'} \not\equiv 0 \pmod r$, and $\operatorname{ord}^\times(q' \pmod r)$ is even.*

For signature $(r,r,p)$ with $r=5$ and $p=17$, our specialization parameters from Proposition 3.22 are:
$$U = X^2, \quad V = 2Y^2, \quad A = 1, \quad B = 8, \quad C = 1, \quad a = U, \quad b = V, \quad c = Z,$$
governing the equation $U^5 + 8V^5 = Z^{17}$.

The valuation $\nu_q$ defined in the preprint is:
$$\nu_q = 34 v_q(Z) - v_q(128 U^5 V^5).$$

Let $q' \nmid 2r = 10$ be any odd rational prime away from 5:

- **Case 1: $q' \mid Z$.** By pairwise coprimality of $X, Y, Z$, $q'$ does not divide $UV$. Hence $v_{q'}(UV) = 0$ and:
  $$\nu_{q'} = 34 v_{q'}(Z) > 0.$$
  This violates the condition $\nu_{q'} < 0$.

- **Case 2: $q' \mid UV$.** By pairwise coprimality, $q'$ does not divide $Z$, so $v_{q'}(Z) = 0$. Hence:
  $$\nu_{q'} = -v_{q'}(128 U^5 V^5) = -5 v_{q'}(UV) < 0.$$
  However, this valuation satisfies:
  $$\nu_{q'} \equiv -5 v_{q'}(UV) \equiv 0 \pmod 5.$$
  This directly violates the second condition $\nu_{q'} \not\equiv 0 \pmod r$.

- **Case 3: $q' \nmid UVZ$.** Then $\nu_{q'} = 0$, violating $\nu_{q'} < 0$.

Consequently, **there does not exist any prime $q'$ satisfying Hypothesis 5** for a primitive positive solution of the weighted equation.

## 3. Why Azon imposed Hypothesis 5

Examining the proof of Theorem 5.23 (lines 3664--3668 of the author manuscript) reveals why the author required Hypothesis 5:

1. **Unipotent reduction**: Hypothesis 5 guarantees that the Jacobian has unipotent reduction at $q'$, producing a supercuspidal Weil--Deligne representation at $q'$ whose inertial restriction has order $r$ or $2r$.
2. **Coefficient field inclusion**: Via [BCDF25, Proposition 8.4], that supercuspidal type forces the field of coefficients $K_g$ of the lowered form to contain $\mathcal{K} = \mathbb{Q}(\sqrt{5})$.
3. **Absolute irreducibility**: Hypothesis 5 was used to invoke [BCDF25, Lemma 6.9] to establish that $\bar\rho|_{G_{\mathcal{K}(\zeta_p)}}$ is absolutely irreducible.

Crucially, **U64 already proved absolute irreducibility unconditionally** through a completely different route:
- Local absolute irreducibility at the prime over 2 was proved directly from the tame inertia action $\Phi_5$ on the good flat model $C^-$ over $F(\pi)$;
- Global absolute irreducibility on $G_{K(\zeta_{17})}$ was then deduced via the cyclic-restriction lemma (Lemma 3 in U64) because the prime above 2 splits in $K(\sqrt{17})/K$.

Thus, while U64 bypassed Azon's need for Hypothesis 5 to prove residual irreducibility, it cannot use Azon's Theorem 5.23 as a packaged black box because the preprint did not state a version of level-lowering without Hypothesis 5.

## 4. The proof of Azon Theorem 5.23 contains no new lowering theorem

Azon's proof of Theorem 5.23 explicitly states:

> *"The first claim follows from combining Theorem 5.21 with Theorem 3.2.2 in [BD14]."*

The author did not develop a new level-lowering machine; he cited Breuil--Diamond (2014) Theorem 3.2.2.

This settles the research priority:
- There is no separate "Azon lowering theorem" that bypasses Breuil--Diamond.
- The author's Magma package (`level&irred.m`) computes the predicted conductor exponents (confirming exponent 2 at 2 and exponent 3 at 5) and runs the Hecke sieve, but it relies mathematically on Breuil--Diamond Theorem 3.2.2 for existence of the lowered form.

## 5. Summary of the modular obligation

With the literature shortcut closed, the requirements to make the level-2000 Hilbert newform comparison unconditional remain exactly as mapped in U94:

1. **Determinant lift $\psi$**: Fix the determinant character lifting $\det(\bar\rho)$ such that $\psi \epsilon^{-1}$ is of finite order.
2. **Local lift at $\mathfrak{p}_5$**: At the unique prime $\mathfrak{p}_5 = (\sqrt{5})$ in $\mathcal{K} = \mathbb{Q}(\sqrt{5})$, the defining quintic is uniformly Eisenstein (U64 Lemma 1). Construct an explicit 2-dimensional characteristic-zero representation $\rho_{\mathfrak{p}_5}$ with Artin conductor exponent 3, the Eisenstein Weil--Deligne type, and determinant $\psi|_{I_{\mathfrak{p}_5}}$.
3. **Local lift at $\mathfrak{p}_2$**: Construct the characteristic-zero lift for the tame order-5 inertial action compatible with conductor exponent 2 and determinant $\psi|_{I_{\mathfrak{p}_2}}$.
4. **Local lift at $\mathfrak{p}_{17}$**: Supply the potentially Barsotti--Tate lift satisfying finite flatness.

If these local deformation lifts are constructed, Breuil--Diamond Theorem 3.2.2 guarantees the existence of the lowered Hilbert newform at level $\mathcal{N} = (2)^2 \mathfrak{p}_5^3$ (norm 2000). The surviving CM orbit $b$ must then be addressed globally.

## 6. Next concrete action

The next checkpoint should address the local lift at $\mathfrak{p}_5$. Because $f(T - U - 2V)$ is Eisenstein over $\mathbb{Q}_5$ uniformly for all primitive solutions, the local Galois action is governed by the Galois group of this Eisenstein quintic over $\mathcal{K}_{\mathfrak{p}_5} = \mathbb{Q}_5(\sqrt{5})$. The objective is to write down the explicit local deformation or cite a recognized local lifting theorem for Eisenstein extensions.
