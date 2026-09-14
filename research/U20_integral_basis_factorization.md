# U20: integral-basis fifth-power equation and a new factorization

Status: verified partial result only. This does not resolve Beal's conjecture.

Continue from U19. Let K=Q(sqrt(17)), w=(1+sqrt(17))/2, so O_K=Z[w] and w^2=w+4. The first fixed unit-class equation is

(P_g/sqrt(17))/eta = gamma^5,

with eta=4+sqrt(17), and its left side is

L_g = -a^8 + 4(17+3sqrt(17))a^6b^2 - 2(51+2sqrt(17))a^4b^4 + 4(17-3sqrt(17))a^2b^6 + (-17+4sqrt(17))b^8.

Exact coefficient extraction gives

L_g = A_g + B_g sqrt(17),

B_g = 4(a-b)b^2(a+b)(3a^2-b^2)(a^2+b^2).

This factorization was checked exactly in Wolfram Language.

Write gamma=u+v w with u,v in Z. Exact reduction using w^2=w+4 gives

gamma^5 = [u^5 + 40u^3v^2 + 40u^2v^3 + 100uv^4 + 36v^5]
          + [v(5u^4+10u^3v+50u^2v^2+45uv^3+29v^4)] w.

Since sqrt(17)=2w-1, the coefficient of w on L_g is 2B_g. Hence every surviving global solution satisfies the exact integer equation

v Q(u,v) = 8 b^2 (a-b)(a+b)(3a^2-b^2)(a^2+b^2),

where

Q(u,v)=5u^4+10u^3v+50u^2v^2+45uv^3+29v^4.

Because gamma and its conjugate generate coprime ideals (U18), gcd(u,v)=1. Consequently

gcd(v,Q(u,v)) divides 5,

since Q(u,v) == 5u^4 (mod v).

On the rational side, with gcd(a,b)=1, the four odd factors

a-b, a+b, 3a^2-b^2, a^2+b^2

are pairwise coprime. Also b is coprime to a-b, a+b, and a^2+b^2; gcd(b,3a^2-b^2) divides 3. Thus away from the small primes 2,3,5 the displayed equation splits prime valuations very rigidly between v and Q.

## Consequence at inert forcing primes

U16 proved that each of 11,31,41,61,71,211,431 divides B, hence divides b; each is congruent to 1 mod 5 and is inert in Q(sqrt(17)). Fix such a prime q. Since q|b and q does not divide a, reducing the fixed equation gamma^5=L_g modulo q gives

gamma^5 == -a^8 == (-A^8)^5 (mod q),

because a=A^5. In the inert residue field F_{q^2}, every fifth root of this rational element is (-A^8) times a fifth root of unity. Since q == 1 (mod 5), all fifth roots of unity already lie in F_q. Therefore gamma mod q is rational, so its w-coordinate satisfies

q | v.

As gcd(u,v)=1 and q != 5, Q(u,v) == 5u^4 is nonzero mod q. Also q divides none of the four odd a,b-factors except b itself. Therefore the exact valuation identity gives

v_q(v)=2 v_q(b)=10 v_q(B).

In particular

(11*31*41*61*71*211*431)^10 | v.

This is stronger than U16's divisibility of B: the same inert forcing primes occur to at least tenth power in the integral-basis coefficient v of gamma.

This remains a finite divisibility statement, not a contradiction. The next target is to exploit the quartic Q(u,v), the second fixed fifth-power equation for delta, or prove an infinite family of forcing primes; any of those could turn this rigidity into an actual elimination of Case III.