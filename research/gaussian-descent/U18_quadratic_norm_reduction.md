# U18: quadratic-field norm reduction of the final Case III branch

Status: verified partial result only. This does not resolve Beal's conjecture.

We continue from U16/U17. The only surviving structural case is

a=A^5,
b=16*17^4*B^5,
G(a,b)=C^5,
H(a,b)=17D^5,

gcd(a,b)=1, with a odd and b even.

Let K=Q(sqrt(17)), write l=sqrt(17), and O_K=Z[(1+l)/2].

## Exact factorization over K

Set s=(b/a)^2. Exact Wolfram factorization gives

G(a,b)=Norm_K/Q(P_g(a,b))/17,
H(a,b)=Norm_K/Q(P_h(a,b)),

where

P_g(a,b)=(-17-4l)a^8 +(1972+476l)a^6b^2 +(-2006-476l)a^4b^4 +(340+68l)a^2b^6 -17b^8,

P_h(a,b)=(-17+4l)a^8 +(68-12l)a^6b^2 +(-102-4l)a^4b^4 +(68+12l)a^2b^6 -b^8.

The exact polynomial resultants of each dehomogenized factor with its conjugate are

Res(P_g-factor, conjugate)= -2^32*17^6,
Res(P_h-factor, conjugate)= -2^32*17^2.

Thus any common prime-ideal divisor of an evaluated factor and its conjugate can lie only above 2 or 17 (with the usual homogenization check when a is divisible by the underlying rational prime).

## Removing the ramified prime above 17

In Case III, 17 does not divide a and 17^4 divides b. Since l^2=17, the leading a^8 coefficient of each P is divisible by l exactly once, while every b-dependent correction has strictly larger l-adic valuation. Hence

v_l(P_g)=v_l(P_h)=1.

Therefore

R_g=P_g/l,
R_h=P_h/l

are algebraic integers not divisible by the prime above 17.

Because a is odd and b is even, the evaluated P_g and P_h are not divisible by primes above 2. Combining this with the resultant calculation shows that R_g and its conjugate are coprime ideals, and likewise R_h and its conjugate.

Their norms are

Norm(R_g)=-C^5,
Norm(R_h)=-D^5,

because Norm(l)=-17.

## Class number one

K has discriminant 17. Minkowski's bound for a real quadratic field is sqrt(17)/2 < 2.1, so every ideal class contains an integral ideal of norm 1 or 2. The element (5+l)/2 has norm 2, so the primes above 2 are principal. Hence every ideal class is principal and h(K)=1.

## Fifth-power ideal consequence

Since (R_g) and its conjugate are coprime and their product is a fifth-power rational ideal, each is itself a fifth power of an ideal. Class number one makes that ideal principal. Therefore

R_g = u * gamma^5,
R_h = v * delta^5

for some gamma,delta in O_K and units u,v in O_K^*.

A fundamental unit is eta=4+sqrt(17), with norm -1. Since -1=(-1)^5, unit classes modulo fifth powers are represented by eta^j, j=0,1,2,3,4. Thus there exist j,k in {0,1,2,3,4} such that

P_g/l = eta^j gamma^5,
P_h/l = eta^k delta^5.

This converts the final rational branch into ten finite unit classes (five for each norm equation) over the fixed quadratic field Q(sqrt(17)). It is a genuinely global strengthening of U16 and avoids the failed single-prime infinite-descent route.

## Verification notes

Exact Wolfram factorization returned the two degree-8 conjugate factors over Q(sqrt(17)). Exact resultants factored as 2^32*17^6 and 2^32*17^2 respectively. The class-number-one argument above is independent and elementary via Minkowski's bound.

## Next obligation

Exploit the finite unit classes. The immediate target is to expand gamma=u+v*(1+sqrt(17))/2 and delta=r+s*(1+sqrt(17))/2, compare coefficients in

P_g/l = eta^j gamma^5,
P_h/l = eta^k delta^5,

and determine whether one of the five unit classes in either equation can be eliminated by congruences or reduced to explicit Thue/Thue-Mahler equations. A complete elimination of all classes would resolve this final (10,10,17) subbranch, not the full Beal conjecture by itself.