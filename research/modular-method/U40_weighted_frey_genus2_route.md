# U40: direct weighted Frey genus-2 route for U^5 + 8 V^5 = Z^17

Status: **superseded/corrected by U41**. This file is retained as a historical checkpoint and must not be used for the final curve sign, local parameter, or lowered level.

Date: 2026-09-14.

## Correction notice

U41 (`U41_weighted_level2000_q11_elimination.md`) found and corrected two material errors in this checkpoint:

1. The Frey polynomial from the authors' executable `Frey_cvs.m` has **+40 U V x^3**, not `-40 U V x^3`.
2. This checkpoint used the `(p,p,r)` parameter `s0=U^5/Z^17` for an `(r,r,p)` equation. The correct local valuation formula is

       nu_q = 34 v_q(Z) - v_q(128 U^5 V^5).

   Consequently the 2-adic case is negative, not positive: `nu_2=-(12+10v_2(Y))`, and the local conductor exponent at 2 is 2.

All mathematical claims below depending on the wrong sign or wrong local parameter are superseded. The route construction itself—namely that the current weighted equation fits the 2025 effective Darmon framework over Q(sqrt(5))—remains valid.

## 1. Active weighted equation

The valid Beal-derived branch is

    X^10 + 256 Y^10 = Z^17,

with gcd(X,Y)=1 and X,Z odd.

Set

    U = X^2,
    V = 2 Y^2.

Then

    U^5 + 8 V^5 = Z^17,

and gcd(U,V)=1 because X is odd and gcd(X,Y)=1.

This is a primitive generalized Fermat equation of signature (5,5,17) with fixed coefficients

    A=1, B=8, C=1.

Unlike the auxiliary unweighted Michaud-Jacobs problem studied in U26-U31, this is exactly the active weighted branch.

## 2. Applicable modern Frey construction

Martin Azon, `Effective Darmon's program for the generalised Fermat equation` (arXiv:2504.01967, 2025), develops Frey hyperelliptic curves and 2-dimensional Galois representations for equations

    A a^r + B b^r = C c^p

with fixed prime r and varying prime p, including non-unit coefficients A,B,C.

The route therefore genuinely incorporates the coefficient 8 instead of replacing the weighted equation by a unit-coefficient surrogate.

The exact specialized curve and local analysis are given in U41.

## 3. What remained useful from this checkpoint

The following scope statements remain valid:

- the active weighted equation is an instance `(A,B,C,r,p)=(1,8,1,5,17)` of the source's `(r,r,p)` framework;
- the RM field is `Q(zeta_5)^+=Q(sqrt(5))`;
- a prime above 17 gives a 2-dimensional residual representation suitable for the modular method;
- the naive hyperelliptic discriminant has moving support, so representation-theoretic conductor analysis is required rather than reading a fixed level directly from the raw curve discriminant.

For the corrected theorem chain, exact local conductor, level norm 2000, complete q=11 elimination, and remaining audit obligations, use U41 only.
