# U35: exact norm polynomial for R and resultants with the fifth-power forms

Status: verified partial result only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Setting

Continue from U33-U34 in the valid weighted branch

    X^10 + 256 Y^10 = Z^17.

The surviving Case III data are

    a=A^5,
    b=16*17^4*B^5,
    gcd(a,b)=1,

and with t=b^2/a^2 the two rational degree-8 forms are

    G(a,b)=a^16 g(t)=C^5,
    H(a,b)=a^16 h(t)=17 D^5,

where

    g(t)=1-136t+2380t^2-12376t^3+24310t^4-19448t^5+6188t^6-680t^7+17t^8,

    h(t)=17-680t+6188t^2-19448t^3+24310t^4-12376t^5+2380t^6-136t^7+t^8.

U24-U25 give

    gamma^5-(eta delta)^5=(8b^2/17)R(a,b),

with R in K=Q(sqrt(17)). U34 showed that the moving prime support of R is the obstruction to a fixed-S tenth-power reduction.

## 1. Exact rational norm of R

Exact Wolfram computation gives

    Norm_{K/Q}(R(a,b)) = 17 F(a,b),

where

    F(a,b)=323 a^12 -1326 a^10 b^2 -867 a^8 b^4
           +7548 a^6 b^6 -7667 a^4 b^8
           +1938 a^2 b^10 -13 b^12.

Equivalently,

    F(a,b)=a^12 f(t),

with

    f(t)=323-1326t-867t^2+7548t^3-7667t^4+1938t^5-13t^6.

The discriminant is

    Disc(f)=2^68 * 11^2 * 13^2 * 17^5 * 151.

Thus outside {2,11,13,17,151}, roots of f modulo a prime are simple.

In Case III,

    t = 2^8 * 17^8 * (B/A)^10.

Therefore every nonexceptional rational prime divisor of F(a,b) with q not dividing A corresponds to a simple root of f in the special tenth-power coset

    2^8*17^8*(F_q^*)^10.

This gives a possible local sieve on the moving R-support, but it is not itself a contradiction.

## 2. Exact resultants with g and h

Exact Wolfram computations give

    Res_t(f,g)
      = -2^96 * 239 * 342107,

and

    Res_t(f,h)
      = 2^96 * 17^6 * 239.

The integer 342107 is prime in the exact factorization returned by Wolfram.

Consequences, after the standard homogenization check using gcd(a,b)=1:

- if a rational prime q outside {2,239,342107} divides both F(a,b) and G(a,b), then q must divide the homogenizing denominator a; in particular for q not dividing a this cannot occur;
- if q outside {2,17,239} divides both F(a,b) and H(a,b), then again q must divide a; for q not dividing a this cannot occur.

Since a=A^5, primes dividing a are already tightly separated from b by gcd(A,B)=1.

## 3. Why this still does not force a power structure on R

The relations

    G=C^5,
    H=17D^5

would be highly useful if every prime divisor of F(a,b) were forced also to divide G or H. The resultant computations show that such simultaneous divisibility would be restricted to a tiny exceptional set.

But there is no proved implication

    q | F(a,b)  =>  q | G(a,b) H(a,b).

A prime may divide R (hence F) while x=gamma and y=eta delta remain nonzero modulo that prime and merely satisfy

    x^5 == y^5.

Such a prime contributes to one cyclotomic factor of x^5-y^5 without dividing x or y, so it need not divide either norm-fifth-power equation G or H.

Therefore the new resultants do **not** make the outside-S valuations of R multiples of 5 or 10. The fixed-S Thue-Mahler reduction remains unproved.

## 4. Additional exact identities checked

The difference and sum of g and h factor as

    g-h = 16 (t-1)(t+1)(t^2-6t+1)
              (t^4-28t^3+70t^2-28t+1),

    g+h = 2 (t-3)(3t-1)
             (t^3-33t^2+27t-3)
             (3t^3-27t^2+33t-1).

These factorizations are exact. They provide lower-degree auxiliary factors relating the two fifth-power equations, but no immediate contradiction follows because g and h are not equal fifth powers: h carries the fixed factor 17.

## 5. Research consequence

The direct attempt to make R a fixed-S tenth power via resultants with G and H fails for a precise reason: R-primes can divide the difference x^5-y^5 without dividing x or y.

The most useful next directions are now narrowed to:

1. exploit the special tenth-power coset condition on roots of f modulo q, possibly together with the restriction from U33 that nonexceptional inert primes of Q(sqrt(17)) cannot divide R;
2. use the exact low-degree factorization of g-h and g+h to derive a separate Diophantine equation whose moving support is better controlled;
3. construct a Frey object directly for U^5+8V^5=Z^17, rather than forcing the present R-factorization into a fixed-S shape.

No weighted Beal subbranch is eliminated by U35 alone.
