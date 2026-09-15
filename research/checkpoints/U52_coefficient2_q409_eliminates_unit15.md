# U52: coefficient-2 branch — q=409 eliminates the omega^15 unit class

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Input

U51 reduced the unit exponent in

    H_-(m,n)=omega^k alpha^17

to k in {0,15}, while m+i n is a Gaussian 17th power up to a Gaussian unit.

## Choosing a second discriminating prime

For a rational prime q, the Gaussian projective 17th-power condition is informative when 17 divides q-chi_{-1}(q), and the Q(sqrt(5)) projective condition is informative when 17 divides q-chi_5(q).

The next small prime after 67 satisfying both conditions is

    q=409.

At 409, -1 and 5 are both squares. The Gaussian 17th-power condition leaves 26 projective ratios n/m (including infinity).

The polynomial T^2-T-1 splits modulo 409 with roots

    omega = 130 or 280.

Thus the Q(sqrt5) equation can be tested independently in both F_409 components, avoiding any ambiguity from the split residue algebra.

## Exact combined sieve

For every Gaussian-compatible projective ratio t=n/m, test whether in both embeddings omega -> 130,280,

    1+30t^2+t^4-16t^2 omega

belongs to omega^k*(F_409)^17.

Results:

- k=15: no compatible projective ratio.
- k=0: exactly t=0 and t=infinity survive.

Therefore the omega^15 global unit class is impossible.

Every surviving coefficient-2 solution must satisfy the untwisted equation

    H_-(m,n)=alpha^17,

and the q=409 local condition

    409 | m*n.

Since gcd(m,n)=1, exactly one of m,n is divisible by 409.

Combining with U48 and U51, a surviving solution now has

    103 | m*n,
    67  | m*n,
    409 | m*n,

with exactly one coordinate divisible by each prime (not necessarily the same coordinate).

## Independent q=883 check

The next inert/inert discriminating prime q=883 was also tested for the remaining k=0 class. Its Gaussian 17th powers give 52 projective ratios, and after imposing the Q(sqrt5) 17th-power condition only

    t=0, infinity

survive. Thus q=883 supplies another forced divisor

    883 | m*n.

This does not itself contradict primitivity because different large primes may divide one coordinate.

## Current strongest form

The coefficient-2 branch is now reduced to

    H_-(m,n)=alpha^17

with no unit twist, together with the Gaussian equation

    m+i n = epsilon*(r+i s)^17,

and the forced divisibility

    67*103*409*883 | m*n.

No complete contradiction is claimed.

## Next obligation

Exploit the untwisted equality itself rather than accumulating divisibility primes indefinitely. Since the omega coefficient of H_- is exactly -16m^2n^2, compare it with the omega coefficient of (A+B omega)^17. This gives an explicit degree-17 binary form equal to -16m^2n^2. Factor/resultant analysis of that coefficient form may force A or B to carry the growing prime divisors and create a descent or valuation contradiction.
