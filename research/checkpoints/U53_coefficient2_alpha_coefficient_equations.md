# U53: coefficient-2 branch — coefficient equations for the untwisted 17th power

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Input

U52 proves the unit twist is trivial. Hence for O_K=Z[omega], omega=(1+sqrt(5))/2,

    H_-(m,n)=(A+B omega)^17,

where

    H_- = m^4+30m^2n^2+n^4 -16m^2n^2 omega.

## Exact expansion

Write

    (A+B omega)^17 = P0(A,B) + B P16(A,B) omega.

Exact Wolfram expansion gives P16 homogeneous of degree 16:

    P16 = 17 A^16 + 136 A^15 B + 1360 A^14 B^2
          + 7140 A^13 B^3 + 30940 A^12 B^4
          + 99008 A^11 B^5 + 252824 A^10 B^6
          + 510510 A^9 B^7 + 826540 A^8 B^8
          + 1069640 A^7 B^9 + 1101464 A^6 B^10
          + 891072 A^5 B^11 + 554540 A^4 B^12
          + 256360 A^3 B^13 + 82960 A^2 B^14
          + 16779 A B^15 + 1597 B^16.

Therefore the omega coefficient gives the exact Diophantine identity

    B P16(A,B) = -16 m^2 n^2.                    (1)

The rational coefficient P0 is the corresponding degree-17 form and satisfies

    P0(A,B)=m^4+30m^2n^2+n^4.                    (2)

The resultant of P0 and P16 (as univariate forms after dehomogenization) has coefficient prime support only at 5; the exact nonzero constant is 5^136 (up to the displayed homogenizing B power in the raw resultant). This matches the earlier exceptional-prime structure.

## Strong 2-adic information

Since m,n are coprime and of opposite parity,

    H_- == 1 (mod 8)

in O_K. Solving

    (A+B omega)^17 == 1 (mod 8)

exactly in O_K/8 gives the unique residue class

    A == 1 (mod 8),
    B == 0 (mod 8).

In particular A is odd and 8|B.

For A odd and 8|B, the form P16 is odd because its leading term 17 A^16 is odd and every remaining term contains B. Taking 2-adic valuations in (1) therefore yields

    v2(B) = 4 + 2 v2(m n).                        (3)

Exactly one of m,n is even, so v2(mn)>=1 and consequently

    v2(B)>=6,

with v2(B) even.

## 17-adic structure

Modulo 17,

    P16(A,B) == -B^16 (mod 17).

If 17|B and gcd(A,B)=1, then substituting B=17B1 shows the leading term 17A^16 has exact valuation 1 while all other terms have larger valuation, hence

    v17(P16)=1.

Equation (1) then forces

    v17(B)+1 = 2 v17(mn),

so whenever 17|B, v17(B) is odd.

If 17 does not divide B, then P16 is a 17-adic unit and 17 does not divide mn through (1).

## Norm relation

The norm of A+B omega is

    A^2+A B-B^2.

Since Norm(H_-)=H(m,n)=v^17, one has

    (A^2+A B-B^2)^17=v^17,

so up to the sign fixed by the real embedding,

    A^2+A B-B^2 = v.

This ties the new variables directly to the original second factor.

## Current state

Together with U52, every surviving solution must satisfy

    B P16(A,B)=-16m^2n^2,
    A==1 mod8,
    v2(B)=4+2v2(mn),
    67*103*409*883 | mn,

plus the Gaussian 17th-power equation m+i n=epsilon(r+i s)^17.

No contradiction is claimed yet.

## Next obligation

Analyze gcd(B,P16). For gcd(A,B)=1, any common prime divisor is forced toward 17 because P16(A,B) == 17 A^16 (mod B). If this yields gcd(B,P16)|17, equation (1) splits the square m^2n^2 between two nearly coprime factors B and P16. That should force each factor to be a square times a controlled power of 2 and 17, producing a new hyperelliptic/Thue equation of substantially lower complexity.
