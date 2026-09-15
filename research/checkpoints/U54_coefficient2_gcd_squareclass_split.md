# U54: coefficient-2 branch — exact gcd and square-class split

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Input from U53

For coprime integers A,B, the surviving coefficient-2 / exponent-17 branch satisfies

    B P16(A,B) = -16 m^2 n^2,

where

    P16(A,B) = 17 A^16 + 136 A^15 B + ... + 1597 B^16,

and U53 established

    P16(A,B) == 17 A^16 (mod B),
    A == 1 (mod 8),
    v2(B) = 4 + 2 v2(mn),

with m,n coprime and of opposite parity. U53 also established that if 17|B then v17(P16)=1 and v17(B) is odd.

## Lemma 1: exact gcd restriction

Let d = gcd(B,P16(A,B)). Since d|B and P16(A,B) == 17 A^16 (mod B),

    d | 17 A^16.

But gcd(A,B)=1 and d|B, hence gcd(d,A)=1. Therefore

    d | 17.

Thus

    gcd(B,P16) in {1,17}.                         (1)

This is stronger than the tentative U53 obligation: no prime other than 17 can divide both factors.

## Lemma 2: square classes when 17 does not divide B

If 17 does not divide B, (1) gives gcd(B,P16)=1. Since

    |B P16| = (4mn)^2,

and the two factors are coprime, every prime valuation in each factor is even. Therefore there exist positive integers b,c such that, for one sign sigma in {+1,-1},

    B   = sigma b^2,
    P16 = -sigma c^2,
    b c = 4 |mn|.                                  (2)

Moreover U53 gives v2(B)>=6 and even, hence

    8 | b.                                          (3)

## Lemma 3: square classes when 17 divides B

If 17|B, U53 gives v17(P16)=1 and v17(B) odd. For every prime p != 17, (1) implies p cannot divide both B and P16, so the product-square identity forces the p-adic valuation of whichever factor contains p to be even. At p=17, both valuations are odd. Consequently there exist positive integers b,c and sigma in {+1,-1} such that

    B   = sigma 17 b^2,
    P16 = -sigma 17 c^2,
    17 b c = 4 |mn|.                                (4)

Again v2(B)>=6 and even, and 17 is odd, so

    8 | b.                                          (5)

## Unified reduction

Let delta in {1,17}. Every surviving solution satisfies

    B   = sigma delta b^2,
    P16(A,B) = -sigma delta c^2,
    delta b c = 4 |mn|,
    8 | b,

where delta=17 exactly when 17|B, and gcd(A,B)=1.

Substituting B=sigma delta b^2 into the degree-16 equation gives the explicit superelliptic equation

    P16(A, sigma delta b^2) = -sigma delta c^2.      (6)

This reduces the U53 product equation to two controlled square classes, with the only exceptional prime 17.

## Independent exact check of the key congruence

A fresh Wolfram evaluation on the explicit U53 polynomial returned

    PolynomialRemainder[P16, B, B] = 17 A^16,

and after B=17 b it factored P16 as 17 times a polynomial whose first term is A^16, consistent with the 17-adic argument in U53.

## What this establishes

This is a genuine structural reduction of the active exponent-17 coefficient-2 branch. It is not an emptiness proof for (6), and it does not resolve Beal's conjecture.

## Next obligation

Exploit (6), gcd(A,b)=1, A odd, and 8|b. First test local solubility of the two equations

    P16(A, b^2) = -sigma c^2,
    P16(A, 17 b^2) = -sigma 17 c^2

for sigma=+/-1 over carefully chosen primes. If local obstructions do not eliminate a square class, dehomogenize using gcd(A,b)=1 and identify the resulting hyperelliptic/Thue-type curve for a rigorous global attack.
