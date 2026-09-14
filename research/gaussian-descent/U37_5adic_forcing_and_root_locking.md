# U37: rational refinement of the d-tower and sharp 5-adic forcing/root locking

Status: verified partial result only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Setting

Continue from U36 in the valid weighted branch

    X^10 + 256 Y^10 = Z^17.

The sole surviving Gaussian-descent case is

    a=A^5,
    b=16*17^4*B^5,
    gcd(A,B)=1,
    G(a,b)=C^5,
    H(a,b)=17D^5,

with a odd and b even. Put K=Q(sqrt(17)), w=(1+sqrt(17))/2, eta=4+sqrt(17),

    gamma=u+v w,
    delta=r+s w.

The fixed unit-class equations are

    L_g=(P_g/sqrt(17))/eta = gamma^5,
    L_h=(P_h/sqrt(17))/eta^4 = delta^5.

## 1. The proposed 2-power norm tower refines already over Q

U36 introduced

    d3=a^4-6a^2b^2+b^4,
    d4=a^8-28a^6b^2+70a^4b^4-28a^2b^6+b^8.

Exact Wolfram factorization gives

    d3=(a^2+2ab-b^2)(a^2-2ab-b^2),

and

    d4=(a^4+4a^3b-6a^2b^2-4ab^3+b^4)
       (a^4-4a^3b-6a^2b^2+4ab^3+b^4).

Thus the d-side of U36 is already a product of six integral forms of degrees

    2,2,2,2,4,4.

Together with d1=b^2-a^2 and d2=a^2+b^2, call these six factors e1,...,e6. Exact pairwise resultants with respect to b, after removing powers of a, are powers of 2 only. Representative constants are

    4, 8, 16, 64, 128, 65536.

Since every evaluated e_i is odd and gcd(a,b)=1, the six evaluated factors are pairwise coprime.

This sharpens U36 but does not create a fifth-power ideal descent: their product is U/8=(C^5-17D^5)/16, not a fifth power. The 2-power cyclotomic norm interpretation therefore does not by itself constrain the prime exponents in the individual factors.

## 2. New local obstruction at 5: every global solution has 5|B

The forcing-prime scan in U16 deliberately concentrated on primes q congruent to 1 mod 5 and did not include q=5. We now examine q=5 directly.

An exact enumeration modulo 25 was performed in Wolfram Language. For every pair (A,B) mod 25 with not both divisible by 5, set

    a=A^5,
    b=16*17^4*B^5

modulo 25 and require simultaneously

    G(a,b) is a fifth power mod 25,
    H(a,b) is 17 times a fifth power mod 25.

There are exactly 100 compatible residue pairs. Their reductions modulo 5 are exactly

    (1,0),(2,0),(3,0),(4,0).

Hence every global Case-III solution satisfies

    5 does not divide A,
    5 divides B.

The same enumeration modulo 125 has solutions with v5(B)=1, so the congruence does not by itself force 25|B.

This adds 5 to the list of globally forced divisors of B.

## 3. 5 is inert in K and the fifth-power map on the residue field is bijective

The discriminant of K is 17, and 17 == 2 mod 5 is a quadratic nonresidue. Therefore 5 is inert in K and

    O_K/(5) ~= F_25.

Its multiplicative group has order 24, so x -> x^5 is an automorphism of F_25^*.

Write

    k5=v5(B) >= 1,
    m=v5(b)=5 k5,
    N=2m-1=10 k5-1.

Let

    beta=b/5^m,

which is a 5-adic unit.

## 4. Sharp locking of gamma at 5

U23 gives the exact identity

    L_g+a^8
      =b^2(68a^6+12sqrt(17)a^6 + terms divisible by b^2).

The leading coefficient 68+12sqrt(17) is a 5-adic unit because its norm is not divisible by 5. Hence

    v5(L_g+a^8)=2m.

Since a=A^5,

    -a^8=(-A^8)^5.

Modulo 5 the fifth-power map is bijective, so gamma is congruent to -A^8 modulo 5. For two 5-adic units congruent modulo 5, the standard factorization of x^5-y^5 gives

    v5(x^5-y^5)=v5(x-y)+1.

Therefore

    v5(gamma+A^8)=2m-1=N.

More precisely, after dividing by 5^N and reducing modulo 5 in O_K, the leading residue is

    (gamma+A^8)/5^N
      == beta^2 A^(-2) (3+2sqrt(17))   (mod 5).

Since sqrt(17)=2w-1, this is

    beta^2 A^(-2) (1+4w)   (mod 5).

Consequently the integral-basis coordinates satisfy the exact valuations

    v5(u+A^8)=N,
    v5(v)=N,

and the leading residues

    (u+A^8)/5^N == beta^2 A^(-2)       (mod 5),
    v/5^N        == 4 beta^2 A^(-2)    (mod 5).

The valuation of v can also be recovered independently from the U20 coefficient identity

    v Q(u,v)=8b^2(a-b)(a+b)(3a^2-b^2)(a^2+b^2).

Because 5|v, gcd(u,v)=1, and

    Q(u,v)=5u^4+10u^3v+50u^2v^2+45uv^3+29v^4,

we have v5(Q)=1 exactly, while the right side has valuation 2m. Hence v5(v)=2m-1 again.

## 5. Sharp locking of delta at 5

U23 also gives

    L_h+eta^(-5)a^8
      = b^2 T/(17 eta^5),

where the b=0 leading term of T is

    (340+68sqrt(17))a^6=68(5+sqrt(17))a^6.

After division by 17 eta^5 this is a 5-adic unit. Thus

    v5(L_h+eta^(-5)a^8)=2m.

Since

    -eta^(-5)a^8=(-eta^(-1)A^8)^5,

bijectivity modulo 5 and the same fifth-power valuation formula give

    v5(delta+eta^(-1)A^8)=N.

Using eta^(-1)=sqrt(17)-4=2w-5,

    -eta^(-1)A^8=(5-2w)A^8.

The coordinate congruences are therefore

    r == 5A^8       (mod 5^N),
    s == -2A^8      (mod 5^N).

In particular

    v5(r)=1,
    v5(s)=0.

The normalized leading residue is

    (delta+eta^(-1)A^8)/5^N
      == beta^2 A^(-2)(4+3w)   (mod 5),

so in fact

    (r-5A^8)/5^N == 4 beta^2 A^(-2)  (mod 5),
    (s+2A^8)/5^N == 3 beta^2 A^(-2)  (mod 5).

## 6. Exact 5-adic valuation of gamma-eta*delta

Put x=gamma and y=eta delta as in U24-U25. Since 5|b,

    x^5-y^5=(8b^2/17)R(a,b).

Modulo 5 and b, the leading coefficient of R is

    (102+17sqrt(17))a^6,

whose norm is a 5-adic unit. Hence

    v5(x^5-y^5)=2m.

Also x == y mod 5 because the fifth-power map on F_25 is bijective. Therefore

    v5(gamma-eta delta)=2m-1=N.

The two root-locking residues above give the sharper first-order formula

    (gamma-eta delta)/5^N
       == beta^2 A^(-2) w   (mod 5).

Equivalently, if eta delta=(3r+8s)+(2r+5s)w, then

    v5(2r+5s)=N

and

    (2r+5s)/5^N == 3 beta^2 A^(-2)  (mod 5).

This is compatible with, and strictly sharper than, v5(r)=1 and v5(s)=0.

## 7. Combined prime-divisibility consequence

Any global solution now has

    5*11*31*41*61*71*101*151*191*211*281*331*431*461*631 | B.

At the same time the gamma coefficient v has exact 5-adic valuation

    v5(v)=10v5(B)-1,

while U22 gives its exact 17-adic valuation

    v17(v)=8+10v17(B).

The delta coordinates have the opposite 5-adic shape

    v5(r)=1,
    v5(s)=0,

and the high-precision linear relation

    2r+5s == 0 (mod 5^(10v5(B)-1)).

These are new global compatibility conditions, but they do not yet yield a contradiction because there is no independent upper bound on the relevant coordinates.

## Verification record

- Wolfram exact factorization was used for d3 and d4.
- All pairwise resultants of the six refined d-factors were computed exactly; after powers of a they are powers of 2.
- The modulo-25 Case-III scan returned exactly 100 admissible pairs and proved B == 0 mod 5, A != 0 mod 5.
- The 5-adic valuation arguments above use exact symbolic identities already preserved in U20 and U23 plus the elementary valuation formula for fifth powers of congruent 5-adic units.

## Next obligation

The strongest new input is the simultaneous sharp locking at the two distinct primes 5 and 17. The next route should combine

    gamma near -A^8 at 5 and 17,
    eta delta near -A^8 at 5 and 17,

with the exact integral-basis equations, seeking either a two-prime Thue/Mahler bound or a linear-form/primitive-divisor argument. If that does not create a decreasing or bounded quantity, pivot to a Frey construction genuinely adapted to U^5+8V^5=Z^17.
