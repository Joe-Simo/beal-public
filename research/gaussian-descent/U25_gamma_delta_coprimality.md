# U25: coprimality of gamma and eta*delta

Status: verified partial result only. This does not resolve Beal's conjecture.

Continue from U24. Put

x=gamma,
y=eta*delta.

Then

x^5=(P_g/sqrt(17))/eta,
y^5=eta*(P_h/sqrt(17)).

Dehomogenize in t=(b/a)^2 and compute the exact resultant of the two degree-4 polynomials defining x^5 and y^5. Wolfram gives

Res_t(x^5-polynomial,y^5-polynomial)
 = -19859928776704*(2177+528 sqrt(17))
 = -2^36*17^2*eta^4.

Since eta is a unit, any common prime-ideal divisor of the two evaluated fifth powers can lie only above 2 or 17, apart from the standard homogenization check. The Case III hypotheses have a odd and b even, and U18 already established that the normalized factors are not divisible by primes above 2. U23 shows both x and y are 17-adic units. Therefore

(x,y)=1 as ideals of O_K.

Consequently

x^5-y^5=(x-y) Phi_5(x,y),

Phi_5(x,y)=x^4+x^3 y+x^2 y^2+x y^3+y^4,

has

gcd((x-y),Phi_5(x,y)) supported only above 5.

Indeed modulo x-y, Phi_5(x,y) is congruent to 5 y^4, and gcd(x,y)=1.

Combining with U24,

(x-y)Phi_5(x,y)=(8 b^2/17)R(a,b),

where

R=(102+17sqrt(17))a^6 +(34+51sqrt(17))a^4b^2
  +(-102-85sqrt(17))a^2b^4 +(-34+9sqrt(17))b^6.

For any rational prime q|b with q not in {17,19}, R is a q-adic unit: modulo b,

R == 17(6+sqrt(17))a^6,

and Norm(6+sqrt(17))=19. Hence every such q contributes exactly

2 v_q(b)=10 v_q(B)

to exactly one of the coprime factors x-y or Phi_5(x,y), provided q !=5. In particular this applies to all currently known inert forcing primes from U20.

Thus each known forcing prime is assigned wholly, with a valuation divisible by 10, to one of the two cyclotomic factors. This is a stronger global structural split than the local divisibility statement alone, but it is not yet a contradiction because either assignment is locally possible when q is congruent to 1 modulo 5.

Next obligation: determine whether the global norm/sign constraints or the second conjugate equation force a consistent assignment of these forcing primes, or pass to K(zeta_5) and analyze the five linear factors of x^5-y^5 with the exact b^2 valuation data.