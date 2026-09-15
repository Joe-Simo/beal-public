# U48: coefficient-2 square branch — Gaussian descent

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## 1. Input from the coefficient-2 checkpoint

For a surviving primitive solution

    X^10 + Y^10 = 2 Z^17,

put a=X^2, b=Y^2. The literature-pruned factorization gives

    a+b = 2 u^17,
    Phi_5(-a,b) = a^4-a^3b+a^2b^2-ab^3+b^4 = v^17,
    gcd(u,v)=1.

X and Y are odd and coprime.

## 2. First equation is a Gaussian 17th-power equation

Set

    m=(X+Y)/2,
    n=(X-Y)/2.

Then m,n are coprime integers of opposite parity and

    X=m+n,
    Y=m-n.

The first factor equation becomes

    X^2+Y^2 = 2(m^2+n^2)=2u^17,

hence

    m^2+n^2=u^17.                                      (1)

Because gcd(m,n)=1 and they have opposite parity, m+in and m-in are coprime in Z[i]. Since Z[i] is a UFD, (1) implies, up to a Gaussian unit and conjugation,

    m+in = epsilon (r+is)^17,
    u=r^2+s^2,

for coprime r,s of opposite parity.

Thus the coefficient-2 branch has an unconditional Gaussian 17th-power parametrization.

## 3. Second factor in the new coordinates

Exact symbolic expansion gives

    a^4-a^3b+a^2b^2-ab^3+b^4
      = m^8 + 44 m^6 n^2 + 166 m^4 n^4 + 44 m^2 n^6 + n^8.

Therefore every surviving solution satisfies the simultaneous system

    m^2+n^2 = u^17,
    m^8+44m^6n^2+166m^4n^4+44m^2n^6+n^8 = v^17,       (2)

with gcd(m,n)=gcd(u,v)=1 and m,n of opposite parity.

Substituting m+in=epsilon(r+is)^17 converts the remaining branch to one explicit binary-form perfect-17th-power equation in r,s. This is a substantially narrower descent target than the original generalized-Fermat equation.

## 4. Interaction with the certified mod-103 constraint

The previous exact finite-field calculation proved

    103 | X^2-Y^2,
    103 does not divide XY.

Since

    X^2-Y^2=(X-Y)(X+Y)=4mn,

we obtain

    103 | mn.                                          (3)

As gcd(m,n)=1, exactly one of m,n is divisible by 103. Also 103 does not divide u, because (1) and coprimality imply the other coordinate is nonzero modulo 103.

This local condition can now be imposed directly on the Gaussian parametrization (r+is)^17.

## 5. Additional local-prime experiment

A direct Wolfram enumeration of the square-factor conditions was repeated at q=137,239,307. Unlike q=103, these primes admit non-diagonal ratios a/b, so the q=103 diagonal phenomenon is special and cannot presently be promoted to an infinite family by the same elementary residue test.

This negative result prevents an unjustified claim that infinitely many auxiliary primes divide X^2-Y^2.

## 6. Next obligation

Exploit (2) after substituting the Gaussian 17th-power parametrization. The concrete questions are:

1. factor the resulting binary form over useful subfields;
2. determine whether (3) forces r/s into a small residue set modulo 103;
3. search for a descent, resultant obstruction, or a Frey curve attached to the remaining binary-form equation.

No complete contradiction is claimed here.