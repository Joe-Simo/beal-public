# U50: coefficient-2 branch — unit classes over Q(sqrt(5))

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Input from U49

For a surviving solution, with K=Q(sqrt(5)),

    H_- = m^4+(22-8sqrt(5))m^2n^2+n^4

has principal ideal equal to a 17th power, and the conjugate factor is coprime to it. Since K has class number 1, H_- is a unit times an element 17th power.

## Integral basis and unit ambiguity

Let

    omega=(1+sqrt(5))/2,

so O_K=Z[omega], omega^2=omega+1, and Norm(omega)=-1. The unit group is generated, up to sign, by omega.

In this basis

    H_- = m^4+30m^2n^2+n^4 - 16m^2n^2 omega.

Because the exponent 17 is odd, -1 itself is a 17th power (-1)^17, so sign contributes no separate class. Modulo 17th powers of units, the only ambiguity is therefore

    epsilon = omega^k,  k=0,...,16.

Thus every surviving solution satisfies

    m^4+30m^2n^2+n^4-16m^2n^2 omega
       = omega^k (A+B omega)^17                 (1)

for some integers A,B and one of exactly 17 unit classes k.

Wolfram exact arithmetic also verifies

    omega^17 = 987+1597 omega.

## Local unit-class sieve

A finite-field implementation of O_K/q = F_q[omega]/(omega^2-omega-1) was used to test equation (1) modulo auxiliary primes. For q=67, the 17th-power map is nontrivial and the quartic shape eliminates six unit classes outright.

The surviving classes modulo 17 are

    k in {0,1,2,3,4,6,9,13,14,15,16}.

The eliminated classes are

    k in {5,7,8,10,11,12}.

Checks at q=101,103,137 did not further reduce the unit classes in the unrestricted quartic equation. Imposing U48's special condition 103|mn also leaves all 17 unit classes locally possible at 103, so no false strengthening is claimed.

## Consequence

The coefficient-2 branch has now been reduced from an arbitrary algebraic 17th-power relation to eleven explicit unit-twisted equations of the form (1), together with

    gcd(m,n)=1,
    m,n opposite parity,
    103|mn,
    m+i n = Gaussian-unit*(r+i s)^17.

This is finite in the unit parameter.

## Next obligation

Use several primes q with 17 dividing |(O_K/q)^*| and include the Gaussian-17th-power condition simultaneously, not merely the quartic equation. The q=67 sieve ignored that additional structure. A combined local sieve should classify tuples (m:n,k) compatible with both

    m+i n = (r+i s)^17

and (1), and may eliminate more or all eleven surviving unit classes.
