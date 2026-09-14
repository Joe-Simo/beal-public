# U23: 17-adic locking of both fifth roots

Status: verified partial result only. This does not resolve Beal's conjecture.

Continue from U22. In the surviving Case III branch,

a=A^5,
b=16*17^4*B^5,
gcd(a,b)=1,

and the fixed fifth-power equations are

L_g=(P_g/sqrt(17))/eta = gamma^5,
L_h=(P_h/sqrt(17))/eta^4 = delta^5,

with eta=4+sqrt(17), gamma=u+v w, delta=r+s w, and w=(1+sqrt(17))/2.

Let

n=2 v_17(b)=8+10 v_17(B).

## Exact b^2 congruences

Exact Wolfram symbolic factorization gives

L_g + a^8
= b^2 * (68 a^6 +12 sqrt(17) a^6 -102 a^4 b^2 -4 sqrt(17) a^4 b^2 +68 a^2 b^4 -12 sqrt(17) a^2 b^4 -17 b^6 +4 sqrt(17) b^6).

Hence

L_g == -a^8 (mod b^2 O_K),

and therefore in particular

L_g == -a^8 (mod 17^n O_K).

Since a=A^5,

-a^8 = (-A^8)^5.

Similarly, exact Wolfram factorization gives

L_h + eta^(-5) a^8
= b^2 * T/(17 eta^5)

for an explicit algebraic-integer expression T; in particular the right side is divisible by b^2 in O_K in the present Case III because b has v_17 at least 4 and the denominator contributes only the already-accounted ramified factor. Thus

L_h == -eta^(-5) a^8 (mod 17^n O_K).

But

-eta^(-5) a^8 = (-eta^(-1) A^8)^5.

## Fifth-root uniqueness at the ramified prime

Let lambda=sqrt(17), the prime element above 17. The residue field O_K/(lambda) is F_17. Since 5 is invertible modulo 17, if x and y are lambda-adic units with x^5 congruent to y^5 modulo lambda^m and x congruent to y modulo lambda, then

x^5-y^5=(x-y)(x^4+x^3y+x^2y^2+xy^3+y^4),

and the second factor is congruent to 5y^4 modulo lambda, hence is a lambda-adic unit. Therefore

v_lambda(x-y)=v_lambda(x^5-y^5).

The fifth-power map on F_17^* is bijective because gcd(5,16)=1, so the required congruence modulo lambda is unique.

Applying this to gamma and -A^8 gives

gamma == -A^8 (mod 17^n O_K).

Applying it to delta and -eta^(-1)A^8 gives

delta == -eta^(-1) A^8 (mod 17^n O_K).

Since eta^(-1)=sqrt(17)-4=2w-5,

-eta^(-1)A^8=(5-2w)A^8.

Therefore the integral-basis coordinates satisfy the strong simultaneous congruences

u := u + A^8 == 0 (mod 17^n),
v == 0 (mod 17^n),

r - 5 A^8 == 0 (mod 17^n),
s + 2 A^8 == 0 (mod 17^n).

Equivalently,

gamma = -A^8 + 17^n Gamma_1,
delta = (5-2w)A^8 + 17^n Delta_1

for some Gamma_1,Delta_1 in O_K.

U22 already showed the v-coordinate has exact valuation n, so the first congruence is sharp in its w-coordinate:

v_17(v)=n=8+10v_17(B).

The delta congruence is consistent with U22's v_17(s)=0 because s is congruent to -2A^8 modulo 17.

## Significance

This replaces separate mod-17 residue statements by a full 17-adic locking to precision 17^(8+10v_17(B)). Both algebraic fifth roots are determined to that precision by A alone:

- gamma is forced extremely close to the rational integer -A^8;
- delta is forced extremely close to the fixed unit multiple (5-2w)A^8.

No contradiction follows yet. The next obligation is to exploit these high-precision simultaneous approximations, for example by combining gamma and eta*delta (which are both congruent to -A^8 modulo 17^n) and examining whether their difference can be related algebraically to b strongly enough to force a descent or impossible valuation.