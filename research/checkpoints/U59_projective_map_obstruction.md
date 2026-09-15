# U59: coefficient-2 branch — why the proposed local map is not projectively well-defined

Status: verified partial/negative result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Question from U58

U58 proposed deriving an algebraic map from the Gaussian projective ratio r/s to the U55 normalized square parameter b^2/A, then intersecting finite local sets at q=67,409,883.

This checkpoint tests whether such a single-valued projective map actually exists.

## Exact reconstruction equation

The two descents meet through

    H_-(m,n) = (A+B omega)^17,

where omega^2=omega+1 and

    H_-(m,n) = h0 + h1 omega,
    h0=m^4+30m^2n^2+n^4,
    h1=-16m^2n^2.

The Gaussian descent gives m=rF(r,s), n=sG(r,s).

For a forced prime q dividing mn, h1=0 mod q. Since exactly one of m,n is zero mod q in the primitive local situations under study,

    H_- mod q = m^4 or n^4,

which is a nonzero rational element of O_K/q.

Thus the local reconstruction problem is

    (A+B omega)^17 in F_q^*,

not an equation retaining the detailed Gaussian root t=r/s. The information that distinguished the F- and G-root classes disappears after H_- is reduced modulo q.

## Exact Wolfram test

For representative forced Gaussian roots at q=67 and q=409, we explicitly enumerated projective pairs (A:B) satisfying

    (A+B omega)^17 proportional to H_-(m,n) mod q.

Each tested Gaussian root produced 17 projective solutions, not one. At q=67, for both an F-root t=4 and a G-root t=3, the same 17 projective classes occurred:

    (7:1),(12:1),(17:1),(18:1),(20:1),(21:1),(23:1),(29:1),
    (37:1),(43:1),(45:1),(46:1),(48:1),(49:1),(54:1),(59:1),(1:0).

The same multiplicity 17 occurs for tested q=409 roots.

This is explained by the 17th-power kernel in the quadratic algebra: for all q in {67,103,409,883}, gcd(17,q^2-1)=17. Hence taking a 17th root modulo q naturally has a 17-fold ambiguity in the relevant quadratic extension/split algebra.

## Consequence

The proposed U58 object

    r/s  ->  b^2/A mod q

is not a canonical single-valued projective map at primes q|mn. Moreover, the condition B=-delta b^2 is not itself invariant under arbitrary projective rescaling of (A:B), so simply selecting one projective representative would risk introducing a false obstruction.

Therefore the naive finite-set intersection proposed in U58 is not rigorous and must not be used to claim a contradiction.

## What survives

U58's exact root tables remain valid. U57's q=103 factor-location result remains valid. What fails is only the proposed next-step simplification to a single projective map.

## Better next route

Retain integral/valuation information instead of projectivizing away the scale. Two promising exact options are:

1. work modulo q^2 (or q^k) at q=67,409,883 so that h1=-16m^2n^2, although zero mod q, retains first nonzero valuation data and may distinguish Gaussian root lifts;
2. use the global identity delta*b*c=4|mn| together with gcd(b,c)=1 to allocate prime valuations before reducing the 17th-root equation.

The cheapest next test is q^2 lifting: for each simple F/G root modulo q, compute the valuation of the corresponding Gaussian cofactor under t=t0+qk and compare with whether q divides b or c in the U55 equation. This preserves precisely the information lost modulo q.
