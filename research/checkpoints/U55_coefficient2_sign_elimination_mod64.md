# U55: coefficient-2 branch — eliminate the positive-B square classes modulo 64

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Input from U54

Every survivor has

    B = sigma delta b^2,
    P16(A,B) = -sigma delta c^2,

where delta is 1 or 17, sigma is +/-1, A is odd, 8|b, and gcd(A,B)=1. Also gcd(B,P16)=delta, hence gcd(b,c)=1.

## Modulo 64 reduction

Because 8|b, one has 64|B for either delta. Every term of P16 except the leading term contains B, so

    P16(A,B) == 17 A^16 (mod 64).

For odd A,

    A^16 == 1 (mod 64),

hence

    P16(A,B) == 17 (mod 64).                       (1)

The U54 square-class equation therefore requires

    -sigma delta c^2 == 17 (mod 64).                (2)

Since P16 is odd, c is odd. The odd square residues modulo 64 are exactly

    {1,9,17,25,33,41,49,57}.

### delta = 1

If sigma=+1, (2) requires c^2 == -17 == 47 (mod 64), impossible because 47 is not an odd square residue.

Thus sigma=-1.

### delta = 17

Since 17 is invertible modulo 64 (17^{-1}=49), sigma=+1 would require

    c^2 == -1 == 63 (mod 64),

again impossible. Thus sigma=-1.

## Conclusion

The sign ambiguity in U54 disappears completely. Every surviving solution in this branch must satisfy, for delta in {1,17},

    B = -delta b^2,
    P16(A,-delta b^2) = delta c^2,
    delta b c = 4 |mn|,
    gcd(b,c)=1,
    gcd(A,b)=1,
    A odd,
    8|b.                                            (3)

In particular B is necessarily negative.

A fresh Wolfram check returned the complete odd-square residue set modulo 64 as

    {1,9,17,25,33,41,49,57},

confirmed that 17 is present but 47 is absent, and returned 17^{-1} mod 64 = 49.

## Additional local scan

A direct exact finite-field scan of the U54 equations for odd primes below 100 (excluding 5 and 17) found local solutions for all four pre-U55 square classes, so no single small odd-prime obstruction was available at that level. The mod-64 condition is strictly stronger for the sign question and removes both sigma=+1 classes.

## Next obligation

Only two equations remain:

    P16(A,-b^2) = c^2,
    P16(A,-17 b^2) = 17 c^2,

with gcd(A,b)=gcd(b,c)=1, A odd, and 8|b. The next target is to combine these equations with the Gaussian 17th-power parametrization of m,n and delta*b*c=4|mn|, rather than treating the superelliptic equations in isolation. Prime-support separation from gcd(b,c)=1 may force a rigid allocation of the Gaussian factors into b and c.