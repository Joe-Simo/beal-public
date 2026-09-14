# U16: mod-11 elimination of two Gaussian-descent cases

Status: verified partial result only. This does not resolve Beal's conjecture.

Starting point is U15. For a primitive positive solution of

X^10 + 256 Y^10 = Z^17,

Gaussian descent yields coprime integers a,b with a odd, b even,

X^5 + 16 i Y^5 = (a+bi)^17,

a G(a,b) = X^5,

b H(a,b) = 16 Y^5,

where

G = a^16 - 136 a^14 b^2 + 2380 a^12 b^4 - 12376 a^10 b^6 + 24310 a^8 b^8 - 19448 a^6 b^10 + 6188 a^4 b^12 - 680 a^2 b^14 + 17 b^16,

H = 17 a^16 - 680 a^14 b^2 + 6188 a^12 b^4 - 19448 a^10 b^6 + 24310 a^8 b^8 - 12376 a^6 b^10 + 2380 a^4 b^12 - 136 a^2 b^14 + b^16.

The U15 valuation argument gives exactly three possible structural cases:

I. a=A^5, b=16 B^5. Then G=C^5 and H=D^5.

II. a=17^4 A^5, b=16 B^5. Since v17(G)=1, G=17 C^5 and H=D^5.

III. a=A^5, b=16*17^4 B^5. Then G=C^5 and H=17 D^5.

(The two exceptional 17^4 factors cannot occur simultaneously because gcd(a,b)=1.)

## Exact mod-11 computation

The fifth-power residues modulo 11 are {0,1,10}.

An exhaustive residue check over these structural cases was independently run in Wolfram Language using exact modular arithmetic. The result was:

- Case I: no residue pairs (a,b) mod 11 satisfy both G fifth-power and H fifth-power conditions.
- Case II: no residue pairs satisfy G in 17*(fifth powers) and H a fifth power.
- Case III: the only residue pairs satisfying G a fifth power and H in 17*(fifth powers) have b == 0 mod 11.

Therefore Cases I and II are impossible.

Any surviving solution must be Case III and satisfy 11 | b. Since b=16*17^4 B^5 and 11 is coprime to 16*17, this implies 11 | B, hence v11(b) is a positive multiple of 5.

## Additional exact local restrictions

The same exact residue test was run for

q in {11,31,41,61,71,101,151,191,211,281,331,431,461,631}.

For every q in this list, every Case-III residue solution has b == 0 mod q. Consequently each of these primes divides B for any global Case-III solution.

Thus

11*31*41*61*71*101*151*191*211*281*331*431*461*631 | B.

This is a strong finite divisibility restriction but not yet a contradiction, because no a priori upper bound on B has been proved.

A broader computational scan found no comparable single-prime obstruction that eliminates Case III outright; local nonzero solutions occur for larger primes such as 181 and 241.

## Next obligation

Exploit the surviving Case III structure

a=A^5,

b=16*17^4 B^5,

G(a,b)=C^5,

H(a,b)=17 D^5,

plus the forced large divisor of B. Promising directions are: (1) p-adic lifting/infinite-descent at one of the forcing primes such as 11; (2) a Thue/Thue-Mahler reformulation of the degree-16 forms; or (3) a modular-method argument specialized to this final branch.