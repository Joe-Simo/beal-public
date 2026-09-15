# U56: coefficient-2 branch — Gaussian parametrization and the q=103 projective constraint

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Inputs

U48 gives, up to Gaussian unit/conjugation,

    m + i n = epsilon (r+i s)^17,

with gcd(r,s)=1 and r,s of opposite parity. Earlier exact local work gives

    103 | mn.

U55 leaves only the negative-B square classes in the independent Q(sqrt(5)) descent.

## Exact Gaussian coordinate forms

For epsilon=1, exact expansion gives

    m = r F(r,s),
    n = s G(r,s),

where

    F = r^16 -136 r^14 s^2 +2380 r^12 s^4 -12376 r^10 s^6
        +24310 r^8 s^8 -19448 r^6 s^10 +6188 r^4 s^12
        -680 r^2 s^14 +17 s^16,

    G = 17 r^16 -680 r^14 s^2 +6188 r^12 s^4 -19448 r^10 s^6
        +24310 r^8 s^8 -12376 r^6 s^10 +2380 r^4 s^12
        -136 r^2 s^14 +s^16.

Multiplication by a Gaussian unit only swaps/signs the two coordinates, so the divisibility statement 103|mn is invariant.

## Exact q=103 computation

For every finite projective ratio t=r/s in F_103, exact Wolfram enumeration found

    F(t,1) != 0,
    G(t,1) != 0.

The only finite ratio for which m*n=0 mod 103 is t=0, coming from the explicit factor r in m. The projective point at infinity s=0 gives n=0.

Therefore, for primitive (r,s),

    103 | mn   ==>   103 | r s.                    (1)

Because gcd(r,s)=1, exactly one of r,s is divisible by 103.

This pushes the earlier local divisor one full step backward through the Gaussian 17th-power map: it cannot arise from either degree-16 cofactor F or G.

## Cross-check / exceptional-prime structure

A fresh exact resultant calculation gives

    Res_x(F(x,1),G(x,1)) = 2^272.

Thus F and G have no common root modulo any odd prime, consistent with the q=103 enumeration. This resultant alone does not prove that F or G individually have no roots modulo 103; the explicit root enumeration above supplies that stronger q=103 fact.

For comparison, F and G do have roots modulo 67, 409, and 883, so the q=103 property is genuinely special and must not be generalized to the other previously forced divisors.

## Consequence for the active branch

Every surviving coefficient-2 exponent-17 solution now has

    103 | r s,
    gcd(r,s)=1,

in addition to the U55 negative-B square-class equations. Hence one Gaussian base coordinate is itself divisible by 103, not merely the much larger coordinates m or n.

## Next obligation

Use 103|r or 103|s to substitute into the U55 equations. Since m,n are degree-17 forms in r,s and B is a square-class factor tied to m*n, compare 103-adic valuations on both descents. The target is to determine whether the exact valuation forced by the Gaussian expansion is compatible with B=-b^2 or B=-17b^2, or whether it forces an impossible parity of v_103(B).
