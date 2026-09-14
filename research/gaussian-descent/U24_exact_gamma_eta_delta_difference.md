# U24: exact valuation of gamma - eta*delta

Status: verified partial result only. This does not resolve Beal's conjecture.

Continue from U23. In the surviving Case III branch, let

eta=4+sqrt(17),
gamma^5=(P_g/sqrt(17))/eta,
delta^5=(P_h/sqrt(17))/eta^4,

a=A^5,
b=16*17^4*B^5,
gcd(a,b)=1.

Set y=eta*delta. Then

y^5=eta^5 delta^5 = eta*(P_h/sqrt(17)),

so

gamma^5-y^5 = (P_g-eta^2 P_h)/(sqrt(17) eta).

An exact Wolfram simplification and factorization gives

 gamma^5-y^5
 = (8 b^2/17) R(a,b),

where

R(a,b)=(102+17sqrt(17))a^6 +(34+51sqrt(17))a^4b^2
       +(-102-85sqrt(17))a^2b^4 +(-34+9sqrt(17))b^6.

Equivalently,

R(a,b)/17 = (6+sqrt(17))a^6 + terms divisible by b^2/17.

Let lambda=sqrt(17), and write m=v_17(b)=4+5v_17(B). Since 17 does not divide a and b is divisible by 17^4, R/17 is a lambda-adic unit; modulo lambda it is congruent to 6a^6. Therefore

ord_lambda(gamma^5-y^5)=ord_lambda(b^2)=4m.

U23 proved gamma congruent to y modulo 17^(2m) O_K, hence in particular modulo lambda. Factoring

gamma^5-y^5=(gamma-y)S,

S=gamma^4+gamma^3 y+gamma^2 y^2+gamma y^3+y^4,

and reducing modulo lambda gives

S == 5 A^32 (mod lambda),

which is nonzero. Hence S is a lambda-adic unit and the valuation transfers exactly:

ord_lambda(gamma-eta*delta)=4m.

Equivalently, with n=2m=8+10v_17(B),

gamma-eta*delta is divisible by 17^n O_K but not by a higher power of the prime above 17.

This proves that the high-precision congruence from U23 is sharp; it does not produce an infinite descent.

A first-order residue is also explicit. Dividing the factorization by b^2 and reducing modulo lambda,

((gamma-eta*delta)/b^2) * S == 8*(R/17) == 48 A^30 (mod lambda).

Since S == 5 A^32, we obtain

(gamma-eta*delta)/b^2 == 13 A^(-2) (mod lambda),

because 48/5 == 13 in F_17. Thus the quotient (gamma-eta*delta)/b^2 is a lambda-adic unit with a fixed leading residue.

An exact factorization attempt for the cubic R in x=a^2,y=b^2 over Q(sqrt(17)) found no further factorization. Its dehomogenized discriminant is nonzero, so this direct difference route closes as a sharp valuation identity rather than a contradiction.

Next obligation: use the exact b^2-normalized relation globally, likely by combining it with the cyclotomic factorization of gamma^5-(eta delta)^5 over K(zeta_5), or return to a modular/Thue-Mahler elimination of the final Case III branch.