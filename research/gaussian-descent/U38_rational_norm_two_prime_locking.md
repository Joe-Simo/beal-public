# U38: rational norms, exact 5/17-adic asymmetry, and a classical cyclotomic factorization

Status: verified partial result only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Setting

Continue from U18-U25 and U37 in the valid weighted branch

    X^10 + 256 Y^10 = Z^17.

The sole surviving Case III has

    a=A^5,
    b=16*17^4*B^5,
    gcd(A,B)=1,
    G(a,b)=C^5,
    H(a,b)=17 D^5,

with a odd, b even, 5|B and 5∤A.

Let K=Q(sqrt(17)), w=(1+sqrt(17))/2, eta=4+sqrt(17), gamma=u+v w, delta=r+s w.

## 1. Rational norms

From U18 and the fixed unit classes,

    Norm(gamma)=C,
    Norm(delta)=-D.

Since w^2=w+4,

    C=u^2+uv-4v^2,
    -D=r^2+rs-4s^2.

## 2. Exact 5-adic asymmetry

Write k5=v5(B)>=1 and m5=v5(b)=5k5.

Exact factorization gives

    G-a^16=-17 b^2(8a^14-140a^12b^2+728a^10b^4-1430a^8b^6+1144a^6b^8-364a^4b^10+40a^2b^12-b^14).

The parenthesis is a 5-adic unit, so v5(G-a^16)=2m5=10k5. Since G=C^5 and a^16=(A^16)^5, LTE gives

    v5(C-A^16)=10k5-1.

Also

    H/17-a^16=-(b^2/17)(680a^14-6188a^12b^2+19448a^10b^4-24310a^8b^6+12376a^6b^8-2380a^4b^10+136a^2b^12-b^14).

Its leading term is -40a^14b^2 and all later terms have larger 5-adic valuation, hence

    v5(D^5-A^80)=10k5+1,
    v5(D-A^16)=10k5.

Thus

    v5(C-A^16)=10k5-1,
    v5(D-A^16)=10k5.

## 3. Exact 17-adic asymmetry

Write k17=v17(B) and m17=v17(b)=4+5k17.

The same formulas give

    v17(G-a^16)=2m17+1=9+10k17,
    v17(H/17-a^16)=2m17=8+10k17.

Because gcd(5,16)=1, the fifth-power map on F_17^* is bijective, so

    v17(C-A^16)=9+10k17,
    v17(D-A^16)=8+10k17.

The one-step asymmetry reverses at 17.

## 4. Exact valuation of C-D

Subtracting the two approximations to A^16, the unequal exact valuations prevent cancellation. Therefore

    v5(C-D)=10k5-1,
    v17(C-D)=8+10k17.

In particular C!=D. U36 gives gcd(C,D)=1, so neither 5 nor 17 divides CD.

## 5. Rational factorization of C^5-D^5

Exact Wolfram factorization gives

    C^5-D^5=G-H/17=-(32 b^2/17) J(a,b),

where

    J(a,b)=51a^14-1071a^12b^2+5967a^10b^4-12155a^8b^6+9945a^6b^8-3213a^4b^10+357a^2b^12-9b^14.

Since b=16*17^4*B^5,

    C^5-D^5=-2^13*17^7*B^10*J(a,b).

Also

    C^5-D^5=(C-D)Phi_5(C,D),

    Phi_5(C,D)=C^4+C^3D+C^2D^2+CD^3+D^4.

Since gcd(C,D)=1, gcd(C-D,Phi_5)|5. Here 5|C-D and 5∤D, so v5(Phi_5)=1. At 17, Phi_5==5D^4 is a unit; and C,D are odd, so Phi_5 is odd. Hence

    gcd(C-D,Phi_5)=5.

The fixed-prime allocation is exact:

    v5(C-D)=10k5-1,    v5(Phi_5)=1,
    v17(C-D)=8+10k17,  v17(Phi_5)=0.

## 6. Arithmetic of J

Put

    j(t)=51-1071t+5967t^2-12155t^3+9945t^4-3213t^5+357t^6-9t^7.

Exact Wolfram computations give

    Disc(j)=2^74*3^11*17^6,
    Res(j,g)=2^96,
    Res(j,h)=2^96*17^7.

Thus outside {2,3,17}, roots of j modulo a prime are simple. After homogenization using gcd(a,b)=1, any odd prime q!=17 dividing J(a,b) is disjoint from both G(a,b)=C^5 and H(a,b)=17D^5, hence q∤CD.

Also J(a,0)=51a^14, so if q|b and q|J(a,b), then q is supported only at {3,17}. Therefore gcd(J(a,b),B) is supported only at {3,17}.

## 7. Prime allocation from B

Let q|B with q not in {3,5,17}. Then q∤J and q∤CD. The right side of

    (C-D)Phi_5(C,D)=-2^13*17^7*B^10*J

has exact q-adic valuation 10v_q(B). Because q!=5, the two left factors are q-coprime. Therefore the whole valuation 10v_q(B) is carried by exactly one of C-D or Phi_5(C,D).

This recovers the earlier prime-assignment phenomenon over the simpler cyclotomic setting Q(zeta_5), without the degree-8 compositum.

## 8. Research consequence

U38 does not eliminate the weighted branch. The moving factor J remains and may contribute new primes. But J is rational, has discriminant supported only at {2,3,17}, is coprime to CD outside {2,17}, and is coprime to B outside {3,17}. The next route is to analyze how J-primes split between C-D and Phi_5(C,D), preferably in Q(zeta_5), and determine whether this forces a fifth/tenth-power ideal relation or a finite Thue-Mahler system.
