# U49: coefficient-2 branch — quartic factor descent over Q(sqrt(5))

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Input

From U48, every surviving primitive solution of

    X^10 + Y^10 = 2 Z^17

produces coprime opposite-parity integers m,n satisfying

    m^2+n^2=u^17,
    H(m,n)=v^17,

where

    H=m^8+44m^6n^2+166m^4n^4+44m^2n^6+n^8.

## Exact factorization

Wolfram exact algebra gives, over K=Q(sqrt(5)),

    H = H_- H_+,

    H_- = m^4+(22-8sqrt(5))m^2n^2+n^4,
    H_+ = m^4+(22+8sqrt(5))m^2n^2+n^4.

These are Galois conjugates. The resultant of the corresponding univariate quartics is

    Res_x(x^4+(22-8sqrt(5))x^2+1,
          x^4+(22+8sqrt(5))x^2+1)
      = 1638400 = 2^16*5^2.

Thus common prime-ideal divisors of the two homogenized factors, away from coordinate degeneracies already excluded by gcd(m,n)=1, can occur only above 2 or 5.

Because m,n have opposite parity,

    H(m,n) == 1 (mod 2),

so no prime above 2 divides either factor through their product. The only possible exceptional common support is therefore the ramified prime above 5.

## Exact 5-adic obstruction

Direct reduction gives

    H(m,n) mod 5 = 0

exactly in the nonzero ratio classes m/n = +/-2 mod 5 (and their reciprocal descriptions). An exhaustive symbolic residue check modulo 25 over all primitive residue pairs with 5|H gives

    H/5 == 1 (mod 5).

Therefore

    5 | H  =>  v_5(H)=1.

But H=v^17, so v_5(H) must be divisible by 17. Hence a surviving solution necessarily has

    5 does not divide H(m,n),

and consequently neither H_- nor H_+ is divisible by the unique prime above 5.

Thus the conjugate quartic factors are coprime as ideals in O_K.

## Consequence for ideal descent

Since

    (H_-)(H_+)=(v)^17

and the two principal ideals are coprime, unique factorization of ideals implies

    (H_-) = a^17,
    (H_+) = conjugate(a)^17

for some integral ideal a of K.

The next step is to use the class number and unit group of Q(sqrt(5)) to convert this ideal relation into an element equation

    H_- = epsilon * alpha^17

with epsilon reduced modulo 17th powers of units. Q(sqrt(5)) has class number one, so there is no class-group obstruction; the remaining unit ambiguity is finite modulo 17th powers.

## Gaussian substitution

U48 also gives

    m+i n = unit*(r+i s)^17.

Substituting those degree-17 forms into H_- produces a degree-68 form over Q(sqrt(5)); its norm is the degree-136 rational form H(m,n). Wolfram factorization over Q shows the degree-136 norm form is irreducible over Q, so the Q(sqrt(5)) quartic factorization is the useful descent structure rather than a hidden rational factorization.

## What this establishes

The previously uncontrolled octic perfect-power equation is now an explicit 17th-power equation in Q(sqrt(5)), up to the finite unit ambiguity:

    m^4+(22-8sqrt(5))m^2n^2+n^4
       = epsilon * alpha^17.

This is a substantially sharper Diophantine target, but no contradiction is claimed yet.

## Next obligation

1. Write O_K=Z[(1+sqrt(5))/2] and determine the fundamental unit modulo 17th powers.
2. Reduce epsilon to 17 unit classes (and sign, if not absorbed).
3. Use conjugation and the special rational shape of H_- to derive coefficient equations for alpha.
4. Combine those equations with m+i n=(r+i s)^17 and the certified 103|mn condition.
5. Search for local obstructions to each unit class before attempting a full Thue/Thue-Mahler computation.
