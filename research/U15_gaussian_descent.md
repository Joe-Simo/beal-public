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

Because gcd(a,b)=1, reducing G modulo a and H modulo b gives

G ≡ 17 b^16 (mod a),
H ≡ 17 a^16 (mod b),

so gcd(a,G) | 17 and gcd(b,H) | 17.

Also H is odd because a is odd and b is even, so v2(b)=4 mod 5. More precisely v2(b)=4+5k.

If 17 | b, then v17(H)=1 (the first term 17a^16 has valuation 1 and every other term has valuation at least 2), hence v17(b) ≡ 4 (mod 5). If 17 ∤ b then every prime valuation in b except the forced 2-adic residue is a multiple of 5. Therefore

b = 16 B^5   or   b = 16*17^4 B^5

for some integer B (with extra 17^5 factors absorbed into B^5).

The identical argument on aG=X^5 gives

a = A^5   or   a = 17^4 A^5,

with gcd(a,b)=1 preventing both a and b from carrying the 17^4 exceptional factor simultaneously.

This produces a finite 17-adic case split for the remaining equation. It does not yet eliminate those cases. A bounded modular search over primes q ≡ 1 (mod 170) below 20000 found local nonzero solutions at every tested prime, so no one-prime congruence obstruction was found in that range.

Next: derive the corresponding degree-16 fifth-power equations G(a,b)=5th power or 17 times a fifth power and H(a,b)=5th power or 17 times a fifth power for the three 17-adic cases, then test whether any known Thue/Thue-Mahler or modular result applies uniformly.