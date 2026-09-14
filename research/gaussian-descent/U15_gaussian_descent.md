# U15 Gaussian descent checkpoint

Status: partial research only; does not resolve Beal's conjecture.

For the surviving all-even branch with 17 | t and r a positive power of 5, prior reduction gives the primitive positive equation

X^10 + 256 Y^10 = Z^17.

Assume gcd(X,Y)=1. A 2-adic valuation argument forces X odd, hence Z odd and gcd(X,16Y)=1. Therefore in Z[i], the factors X^5 ± 16 i Y^5 are coprime. Since Z[i] is a UFD and 17 is odd, after absorbing a unit there exist coprime integers a,b with

X^5 + 16 i Y^5 = (a+bi)^17,
Z = a^2+b^2.

Parity forces a odd and b even. Writing

Re((a+bi)^17)=a G(a,b),
Im((a+bi)^17)=b H(a,b),

we have

G = a^16 - 136 a^14 b^2 + 2380 a^12 b^4 - 12376 a^10 b^6 + 24310 a^8 b^8 - 19448 a^6 b^10 + 6188 a^4 b^12 - 680 a^2 b^14 + 17 b^16,

H = 17 a^16 - 680 a^14 b^2 + 6188 a^12 b^4 - 19448 a^10 b^6 + 24310 a^8 b^8 - 12376 a^6 b^10 + 2380 a^4 b^12 - 136 a^2 b^14 + b^16.

Thus

a G = X^5,
b H = 16 Y^5.

Because gcd(a,b)=1,

gcd(a,G) | 17,  gcd(b,H) | 17.

Also H is odd because a is odd and b is even, so v2(b)=4 mod 5.

Exact 17-adic analysis gives three cases only:

Case I: a=A^5, b=16 B^5, G=C^5, H=D^5.

Case II: a=17^4 A^5, b=16 B^5, G=17 C^5, H=D^5.

Case III: a=A^5, b=16*17^4 B^5, G=C^5, H=17 D^5.

The two exceptional 17^4 factors cannot occur simultaneously because gcd(a,b)=1. Exact symbolic reduction modulo 17 gives G(a,b) ≡ a^16 and H(a,b) ≡ b^16, and substituting a=17u or b=17v shows G(17u,b)/17 ≡ b^16 and H(a,17v)/17 ≡ a^16 (mod 17), so the exceptional factor has exact 17-adic valuation 1 in G or H.

A separate exact resultant computation gives

Res_a(G(a,1),H(a,1)) = 2^272,

so G and H have no common odd prime divisor when gcd(a,b)=1; since both are odd here, gcd(G,H)=1.

## New modulo-11 elimination

The fifth-power residues modulo 11 are exactly {0,1,-1}. Exhaustive exact enumeration of the 120 nonzero pairs (A,B) modulo 11 gives:

- Case I: no pair satisfies both required fifth-power conditions.
- Case II: no pair satisfies both required fifth-power conditions.
- Case III: the only surviving projective class has B ≡ 0 (mod 11).

Therefore Cases I and II are impossible. Any remaining solution to this branch must be in Case III and must satisfy 11 | B.

Equivalently the sole surviving structure is

a=A^5,
b=16*17^4 B^5,
G=C^5,
H=17D^5,
11 | B,

with gcd(A,B)=1. Consequently 11 does not divide A.

A bounded exact finite-field scan of Case III for primes q ≡ 1 (mod 5), q<20000, found no prime giving a complete local contradiction. For several small primes (including 11,31,41,61,71,101,151,191,211,281,331,431,461,631) the only local projective solution similarly has B ≡ 0 (mod q), forcing divisibility by each such prime, but this finite list alone is not an infinite descent or a proof of impossibility.

Relevant published context: Michaud-Jacobs, Mathematika 68 (2022), proves x^(2l)+y^(2m)=z^17 for primes l,m != 5 and explicitly leaves exponent 5 outside that theorem; its Corollary 4 separately handles equal unweighted exponents x^(2n)+y^(2n)=z^17 using the known x^5+y^5=z^17 result. Our weighted equation X^10+256Y^10=Z^17 is not covered by that corollary because 256 is not a tenth power (nor can it be absorbed into Y over the integers).

Next: attack Case III only, preferably through the superelliptic equation H(A^5,16*17^4 B^5)=17D^5 together with G(A^5,16*17^4 B^5)=C^5, using the forced small-prime divisibility as auxiliary local information.