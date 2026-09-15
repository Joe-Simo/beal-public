# U57: coefficient-2 branch — the forced prime 103 lies in B

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Inputs

U54-U55 reduce every surviving case to

    B = -delta b^2,
    P16(A,B) = delta c^2,
    delta b c = 4 |mn|,

where delta is 1 or 17, gcd(A,B)=1, and 8|b.

U56 proves that 103|mn and, through the Gaussian parametrization, exactly one of r,s is divisible by 103.

Also gcd(B,P16)|17, so 103 cannot divide both B and P16.

## Exact finite-field test

To decide which factor carries 103, suppose first that 103 does not divide b. Since gcd(A,B)=1, A is also nonzero modulo 103 whenever 103|B; in the present alternative B is nonzero mod 103, so normalize by A and use homogeneity.

For each delta in {1,17}, enumerate the nonzero quadratic residues t=b^2/A (equivalently after projective normalization, the square-class parameter) modulo 103 and test

    P16(1,-delta t) == 0 (mod 103).

A fresh exact Wolfram enumeration returned no roots for either delta:

    delta=1:  {}
    delta=17: {}

Therefore P16 cannot be divisible by 103 in either surviving U55 square class when B is nonzero modulo 103.

Since 103 divides B*P16 = -16 m^2 n^2 and cannot divide P16 in that alternative, it follows that

    103 | B,

hence

    103 | b.                                           (1)

Because gcd(B,P16)|17,

    103 does not divide P16,
    103 does not divide c.                              (2)

## Exact valuations

From delta b c = 4|mn|, with 103 not dividing 4 delta c,

    v103(b) = v103(mn).                                 (3)

From U56, if 103|r then the Gaussian coordinate formulas satisfy

    m = r F(r,s),  F(r,s) == 17 s^16 (mod 103),
    n = s G(r,s),  G(r,s) == s^16 (mod 103),

and s is a 103-adic unit. Hence

    v103(mn)=v103(r).

Similarly, if 103|s then v103(mn)=v103(s). Therefore

    v103(b) = v103(r)  if 103|r,
    v103(b) = v103(s)  if 103|s.                       (4)

Consequently

    v103(B)=2 v103(b)=2 v103(mn),                      (5)

exactly matching the product equation.

## Interpretation

The hoped-for immediate valuation-parity contradiction does not occur: the U55 square class is compatible with the Gaussian valuation. However, the local information is now substantially sharper: the entire 103-adic contribution is forced into B (and b), never into P16 (or c), and its valuation is exactly the valuation of the divisible Gaussian base coordinate r or s.

This negative/positive distinction is important: U57 does not claim a contradiction.

## Next obligation

Repeat the factor-location test for the other forced primes 67, 409, and 883, but unlike 103 their Gaussian cofactors have roots. Track simultaneously whether each prime enters r, s, F, or G and whether the U55 square-class equation forces it into b or c. A combined incompatibility between these location patterns is now the most economical local route.
