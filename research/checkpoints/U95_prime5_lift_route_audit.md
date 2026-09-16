# U95: the prime-5 conductor is explicit, but it does not by itself construct the Breuil--Diamond local lift

**Status: source/code audit of the modular route. The weighted equation and Beal's conjecture remain unresolved.**

Research date: 2026-09-16.

## 1. Target inherited from U94

U94 isolated the next modular obligation: at the unique prime over 5 in K=Q(sqrt(5)), construct a characteristic-zero local lift of the residual two-dimensional RM component with the determinant and Weil--Deligne type required by Breuil--Diamond Theorem 3.2.2.

U64 already proves uniformly that the relevant quintic is irreducible over Q_5 (indeed its translate is Eisenstein) and records, from Azon's conductor theorem, Artin conductor exponent 3 for the two-dimensional component.

## 2. What the author's implementation actually certifies

The electronic resources accompanying Azon's preprint were inspected directly. In `level&irred.m`, for signature `(r,r,p)`, the routine `ExponentOfTheLevelAt_r` returns exponent 3 when the coefficient product is prime to r and the user-supplied/established `gminus_irreducible` flag is true. The level routine then uses that exponent in the Hilbert-newform level.

For our specialization r=5 this agrees with U64's intended prime-5 exponent 3. This is useful independent code-level corroboration that the source's elimination implementation treats precisely this irreducible local branch as level exponent 3.

However, the public Magma implementation computes the predicted level and performs the elimination step. It does not expose a construction of the local characteristic-zero representation required as input to Breuil--Diamond 3.2.2, nor does the inspected routine specify its Weil--Deligne matrices or fixed determinant.

Therefore the implementation cannot be used as a substitute for the missing local-lift proof.

## 3. A route correction

The preprint itself advertises a dedicated level-lowering theorem (Theorem 5.22 in the paper's overview) for the Frey systems, whereas U64/U94 attempted to rebuild the needed global lift through the more general Breuil--Diamond theorem. This suggests a potentially shorter rigorous route:

1. test whether Azon's own Theorem 5.22 applies directly to the corrected negative twist and our specialization `(r,r,p)=(5,5,17)`;
2. distinguish it carefully from the more restrictive packaged statement U64 recorded as Theorem 5.23/Hypothesis 5;
3. if 5.22 already supplies the required lowered modular representation under hypotheses that U64 has proved, the explicit Breuil--Diamond local-lift construction may be unnecessary;
4. if 5.22 still invokes local deformation choices not verified in our case, return to the explicit prime-5 lift problem.

This is now higher priority than guessing a Weil--Deligne type from the conductor exponent alone.

## 4. What is not claimed

Conductor exponent 3 does not uniquely determine a Weil--Deligne type. Eisenstein irreducibility of the defining quintic does not, by itself, construct a two-dimensional fixed-determinant characteristic-zero lift. The author's Magma level routine is corroboration of the intended level formula, not a proof of Breuil--Diamond's local hypotheses.

No level-2000 comparison is upgraded to unconditional status in this checkpoint.

## 5. Next obligation

The next checkpoint should source-audit the exact statement and hypotheses of Azon Theorem 5.22 against the specialization already proved in U64. This has a binary payoff: either it bypasses U94's explicit local-lift reconstruction, or it identifies exactly which local datum remains missing.
