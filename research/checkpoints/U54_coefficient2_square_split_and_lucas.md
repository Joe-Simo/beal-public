# U54: coefficient-2 branch — exact square split and Lucas reformulation

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-16.

## Input

From U52-U53, with K=Q(sqrt(5)), omega=(1+sqrt(5))/2,

    H_-(m,n)=(A+B omega)^17,

where gcd(m,n)=1, m,n have opposite parity, and

    H_- = m^4+30m^2n^2+n^4 -16m^2n^2 omega.

The coefficient equation is

    B P16(A,B) = -16 m^2 n^2,                     (1)

where P16 is the degree-16 form recorded in U53. Also

    A == 1 (mod 8),
    B == 0 (mod 8).

## 1. Primitivity of A,B

The conjugate factors H_- and H_+ are coprime as ideals in O_K (U49). If a rational prime p divided both A and B, then p would divide alpha=A+B omega and also its conjugate, hence p would divide both H_-=alpha^17 and H_+=conjugate(alpha)^17, contradicting that ideal coprimality.

Therefore

    gcd(A,B)=1.                                      (2)

## 2. Exact gcd(B,P16)

Modulo B,

    P16(A,B) == 17 A^16 (mod B).

Using gcd(A,B)=1,

    gcd(B,P16) | 17.

If 17 does not divide B, then gcd(B,P16)=1.

If 17|B, write B=17B1. Exact expansion gives

    P16(A,17B1)=17(A^16 + terms divisible by 17),

and 17 does not divide A. Hence

    v17(P16)=1.

Thus

    gcd(B,P16) = 1   if 17 does not divide B,
    gcd(B,P16) = 17  if 17 divides B.                (3)

## 3. Square splitting of the coefficient equation

The form P16 is odd because B is divisible by 8 and

    P16 == 17 A^16 == 1 (mod 8).

Taking prime valuations in (1):

- every odd prime other than 17 occurs in B or P16 to an even exponent;
- the full 2-adic exponent lies in B and is even;
- if 17|B, then v17(P16)=1 and v17(B) is odd.

The sign is also forced. Since P16 ==1 (mod 8), it cannot be the negative of an odd square (nor the negative of 17 times an odd square). Since BP16<0, B must be negative and P16 positive.

Therefore exactly one of the following two cases holds:

Case I:

    B = -R^2,
    P16(A,B) = S^2,
    R S = 4 |mn|.

Case II:

    B = -17 R^2,
    P16(A,B) = 17 S^2,
    17 R S = 4 |mn|.

In both cases gcd(R,S)=1. In Case II, 17 does not divide S.

## 4. Case I is impossible modulo 5

Substitute B=-R^2 into P16. Exact reduction modulo 5 gives

    P16(A,-R^2) == 2 (A+2R^2)^16 (mod 5).           (4)

Since 2 is a quadratic non-residue modulo 5, the equality

    P16=S^2

forces

    A+2R^2 ==0 (mod 5).                              (5)

Now define the Lucas parameters

    T = 2A+B,
    Q = A^2+A B-B^2 = Norm(A+B omega).

In Case I, B=-R^2. Equation (5) implies

    T = 2A-R^2 ==0 (mod 5),
    Q = A^2-A R^2-R^4 ==0 (mod 5).

But gcd(T,Q)=1, as proved below. Contradiction.

Hence Case I is impossible.

Therefore every surviving coefficient-2 solution is necessarily in Case II:

    B = -17 R^2,
    P16(A,B)=17 S^2,
    17 R S =4|mn|.                                  (6)

This is a new strict restriction.

## 5. Coprime Lucas parameters

Let

    alpha=A+B omega,
    beta=A+B(1-omega).

Then

    T=alpha+beta=2A+B,
    Q=alpha beta=A^2+A B-B^2.

Since A is odd and B is divisible by 8, T is even and Q is odd.

Also

    4Q = T^2 - 5B^2.

Any common divisor d of T and Q is therefore odd and divides 5B^2. But

    gcd(T,B)=gcd(2A+B,B)=2

using gcd(A,B)=1, so d is coprime to B and hence d|5.

U49 proves 5 does not divide H(m,n). Since

    H(m,n)=Norm(H_-)=Q^17,

we have 5 does not divide Q. Therefore

    gcd(T,Q)=1.                                      (7)

## 6. Lucas sequence reformulation

Because

    alpha-beta = B sqrt(5),

we have

    P16(A,B)
      = (alpha^17-beta^17)/(alpha-beta)
      = U_17(T,Q),

where U_n(T,Q) is the Lucas sequence

    U_0=0,
    U_1=1,
    U_n=T U_{n-1}-Q U_{n-2}.

Thus the sole surviving square-split case becomes

    U_17(T,Q)=17 S^2,                                (8)

with

    gcd(T,Q)=1,
    T even,
    Q odd,
    T^2-4Q = 5*17^2 R^4.                            (9)

This is a fixed-index Lucas almost-square problem with the additional very restrictive discriminant condition (9).

Published work of Bremner and Tzanakis on Lucas sequences whose nth term is a square or almost square establishes finiteness for fixed n>=8 and gives effective reductions in many cases, but does not provide a published complete classification for n=17, k=17. Therefore (8)-(9) is a genuine remaining Diophantine problem, not a literature-closed case.

## 7. Positive-coordinate form

Substituting A=(T-B)/2 into P16 gives the exact identity

    2^16 P16 =
      17 T^16
      +3400 B^2 T^14
      +154700 B^4 T^12
      +2431000 B^6 T^10
      +15193750 B^8 T^8
      +38675000 B^10 T^6
      +37187500 B^12 T^4
      +10625000 B^14 T^2
      +390625 B^16.

All coefficients are positive. Since alpha and beta are both positive real numbers (H_- and H_+ are positive 17th powers), T>sqrt(5)|B|.

In the surviving Case II, B=-17R^2, so this is an explicit positive genus-7 hyperelliptic/Thue-type equation for (T,R,S).

## Next obligation

Attack (8)-(9) directly. The most promising options are:

1. use the fixed-index Lucas almost-square machinery for U_17(T,Q)=17S^2 with the additional discriminant 5*17^2 R^4;
2. factor U_17 cyclotomically over the quartic real field generated by a root of x^4-44x^3+166x^2-44x+1;
3. run a local sieve on the fixed hyperelliptic curve while preserving the square-denominator/discriminant condition.

No full contradiction is claimed.