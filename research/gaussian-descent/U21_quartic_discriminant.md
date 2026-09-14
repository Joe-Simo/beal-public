# U21: quartic discriminant structure in the surviving branch

Status: verified partial result only. This does not resolve Beal's conjecture.

Continue from U20. The surviving Case III branch yields

v Q(u,v) = 8 b^2 (a-b)(a+b)(3a^2-b^2)(a^2+b^2),

with

Q(u,v)=5u^4+10u^3v+50u^2v^2+45uv^3+29v^4,

and gcd(u,v)=1.

An exact Wolfram computation of the resultant of Q with its u-derivative gives

Res_u(Q, dQ/du) = 3017196125 v^24 = 5^3 * 17^6 * v^24.

Therefore, for any rational prime p with p not in {5,17} and p not dividing v, the reduction of Q(u,v) as a polynomial in u is separable modulo p. Equivalently, if p divides Q(u,v) under those hypotheses, then dQ/du is nonzero modulo p at the corresponding residue class.

Since gcd(u,v)=1, this applies in particular to every prime p != 5,17 dividing Q(u,v) but not v. Thus the only rational primes at which Q can have repeated-root behavior in the primitive (u,v) setting are 5 and 17.

This does not by itself contradict the surviving branch. It narrows any p-adic lifting analysis of the quartic factor to ordinary simple-root Hensel behavior away from 5 and 17, so any exceptional obstruction must come from the small primes 5 or 17, or from compatibility with the second fixed fifth-power equation for delta.

Verification record: exact symbolic resultant and exact integer factorization were computed in Wolfram Language. No numerical approximation was used.

Next obligation: combine the simple-root structure of Q away from 5 and 17 with the second delta-equation, rather than seeking repeated-root obstructions at the forcing primes.