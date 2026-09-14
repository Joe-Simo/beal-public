# U45: small-prime factors of r,s are excluded when t >= 3

Status: verified partial coverage result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## 1. Setup

Let a primitive all-even Beal candidate be

    A^(2r) + B^(2s) = C^(2t),

with r,s,t >= 2 and pairwise coprime positive bases A,B,C.

U44 reduced the cases 2|r and 2|s to quartic perfect-power equations but did not have a uniform theorem. The literature audit below closes those cases for every t>=3 and also closes 3|r or 3|s for every t>=3.

## 2. Excluding 3 | r or 3 | s for t >= 3

Assume 3|r. Put

    X = A^(r/3),
    Y = B^s,
    Z = C^2.

Then

    X^6 + Y^2 = Z^t,

or after swapping the two left terms,

    Y^2 + X^6 = Z^t.

The transformed bases X,Y,Z remain positive and gcd(X,Y)=1.

Michael A. Bennett and Imin Chen, `Multi-Frey Q-curves and the Diophantine equation a^2+b^6=c^n`, Algebra & Number Theory 6 (2012), 707-730, DOI 10.2140/ant.2012.6.707, Theorem 1, states:

    Let n >= 3 be an integer. Then a^2+b^6=c^n
    has no solutions in positive integers a,b,c with gcd(a,b)=1.

Taking (a,b,c,n)=(Y,X,Z,t) gives a contradiction for every t>=3.

The same argument with A and B interchanged excludes 3|s.

Therefore

    t >= 3  =>  3 does not divide r*s.                       (1)

## 3. Excluding 2 | r or 2 | s for t >= 4

Assume 2|r. Put

    X = A^(r/2),
    Y = B^s,
    Z = C^2.

Then

    X^4 + Y^2 = Z^t,

which is the generalized-Fermat equation a^2+b^4=c^n after swapping X and Y.

The complete resolution assembled from Ellenberg, Bennett-Ellenberg-Ng, and the remaining n=6 case states that

    a^2+b^4=c^n

has no solutions in nonzero coprime integers for every n>=4.

Hence 2|r is impossible for t>=4. By symmetry 2|s is impossible for t>=4.

## 4. The boundary t=3 is also excluded for 2 | r or 2 | s

The preceding (2,4,n) theorem starts at n=4, so t=3 must be treated without silently extending it.

If 2|r, retain the full other exponent rather than collapsing it to a square:

    X=A^(r/2),
    Z=C^2.

Then

    X^4 + B^(2s) = Z^3.

This has signature (4,2s,3), with s>=2.

M. A. Bennett, I. Chen, S. R. Dahmen, and S. Yazdani, `Generalized Fermat equations: A miscellany`, International Journal of Number Theory 11 (2015), DOI 10.1142/S179304211530001X, Theorem 1, includes the infinite family

    (4,2n,3), n>=2,

among the signatures for which x^p+y^q=z^r has no nonzero coprime integer solutions.

Taking n=s contradicts the putative solution. The case 2|s follows by symmetry.

Thus

    t = 3  =>  2 does not divide r*s.                        (2)

Combining with the t>=4 argument,

    t >= 3  =>  2 does not divide r*s.                       (3)

## 5. Combined result

From (1) and (3):

    t >= 3  => every prime divisor of r and s is at least 5. (4)

This rigorously supplies the missing prerequisite used in U43, but only when t>=3.

Consequently, in the subbranch t>=3 with 17|t, U43's published Michaud-Jacobs step is now fully justified:

    17|t and t>=3
      => one of r,s is a positive power of 5
      => either X^10+Y^10=2 Z^17
         or X^10+256Y^10=Z^17.

The coefficient-256 branch is the U41 candidate elimination; the coefficient-2 branch remains open in this repository.

## 6. Boundary not covered

The case

    t=2,

corresponding to original right exponent z=4, is not covered by the theorems above. For example the reductions become equations of the shape

    X^4+Y^2=Z^2

or

    X^6+Y^2=Z^2,

for which the cited n>=3/n>=4 generalized-Fermat theorems do not apply.

Therefore this checkpoint does NOT assert that every prime divisor of r and s is >=5 when t=2.

## 7. Next obligation

Treat the all-even t=2 branch directly. The first question is whether the primitive Pythagorean parametrization plus the fact that both legs are perfect powers rules out

    A^(2r)+B^(2s)=C^4

for all r,s>=2. Only after that boundary case is resolved can the small-prime-factor statement be made unqualified across the full all-even branch.
