# U32: weighted-branch scope correction

Status: verified research-state correction only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Correction

The active surviving Beal-derived equation from U15 is

    X^10 + 256 Y^10 = Z^17,

with gcd(X,Y)=1 and X,Z odd. The coefficient 256 is essential: it is not a tenth power, and no rational common rescaling can simultaneously turn both left-hand terms into integral tenth powers. U15 already recorded that Michaud-Jacobs' unweighted theorem for

    x^(2l) + y^(2m) = z^17

and its ell=5 Hilbert-newform obstructions do not directly cover the weighted equation.

The modular-method files U26--U31 study the unweighted Michaud-Jacobs ell=5 obstruction. Those calculations may be mathematically useful as method development, but they do not currently eliminate any case of the weighted equation X^10+256Y^10=Z^17 unless a new, proved reduction from the weighted equation to that Hilbert-modular setup is supplied.

Therefore the previous research-state language suggesting that Case 1 versus Case 2 in Michaud-Jacobs determined coverage of the weighted branch was incorrect. No such correspondence has been proved.

## Current valid state of the weighted branch

The valid chain for X^10+256Y^10=Z^17 is U15--U25 in `research/gaussian-descent/`:

- Gaussian factorization in Z[i];
- the surviving 17-adic Case III

      a=A^5,
      b=16*17^4 B^5,
      G=C^5,
      H=17 D^5;

- elimination of Cases I and II modulo 11;
- the finite list of forcing primes and proof that a single forcing prime does not iterate to an infinite p-adic descent;
- factorization over Q(sqrt(17)), collapse to fixed unit classes, integral-basis coefficient equations, exact 17-adic root locking, and coprime cyclotomic factorization of gamma^5-(eta delta)^5.

The latest valid weighted checkpoint is U25. Its next obligation is global: exploit the cyclotomic factorization in K(zeta_5), derive a Thue/Thue-Mahler or superelliptic contradiction, or construct a modular method adapted to the coefficient 256 itself.

## Literature check

A search of the 2024 survey `Generalised Fermat equation: a survey of solved cases` and direct searches for the exact equation found no published theorem directly resolving

    X^10 + 256 Y^10 = Z^17

or equivalently the weighted signature-(5,5,17) form

    U^5 + 8 V^5 = Z^17,

where U=X^2 and V=2Y^2.

The survey records unit-coefficient (5,5,n) solutions for n=7 and 19 and Michaud-Jacobs' unweighted (2l,2m,17) result for l,m !=5, but not the present weighted coefficient-8/256 equation.

## Consequence for coverage

U26--U31 remain preserved as auxiliary modular-method research, but they are not counted toward elimination of the active Beal-derived weighted branch. The research program returns to U25 as the mathematically connected frontier.
