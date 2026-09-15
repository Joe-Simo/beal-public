# U58: coefficient-2 branch — exact factor-location tables for q=67,409,883

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Input

U57 forces q=103 entirely into the B=-delta b^2 factor. The other previously forced primes q=67,409,883 divide mn, but unlike 103 the Gaussian degree-16 cofactors F and G have roots modulo q.

We now compute both sides of the location problem exactly.

## Gaussian side

For m=r F(r,s), n=s G(r,s), normalize s=1 when s is nonzero modulo q. Exact Wolfram enumeration gives 16 roots of F(t,1) and 16 roots of G(t,1) for each q in {67,409,883}. Thus q|mn can arise from four projective locations: r=0, s=0, F=0, or G=0.

The root sets are:

q=67:
F roots = {4,5,6,8,13,15,16,22,45,51,52,54,59,61,62,63}
G roots = {3,9,11,17,21,25,27,31,36,40,42,46,50,56,58,64}

q=409:
F roots = {13,41,80,81,132,158,180,190,219,229,251,277,328,329,368,396}
G roots = {10,25,44,46,63,101,127,189,220,282,308,346,363,365,384,399}

q=883:
F roots = {55,66,98,156,233,238,351,400,483,532,645,650,727,785,817,828}
G roots = {9,72,117,161,256,289,300,388,495,583,594,627,722,766,811,874}

## Q(sqrt(5)) square-class side

U55 gives

    B=-delta b^2,
    P16(A,B)=delta c^2,

with delta in {1,17}. If q does not divide b, normalize A=1 and ask whether q can instead divide P16 through a nonzero square t=b^2/A. Exact enumeration shows that it can: the numbers of admissible nonzero square roots t are

q=67: 8 for delta=1, 8 for delta=17;
q=409: 7 for delta=1, 7 for delta=17;
q=883: 7 for delta=1, 7 for delta=17.

Hence, unlike q=103, none of these primes is individually forced into b. Each may lie either in b (equivalently B) or in c (equivalently P16).

Exact admissible t sets:

q=67:
delta=1:  {16,64,14,10,26,39,60,19}
delta=17: {9,64,55,56,39,40,22,37}

q=409:
delta=1:  {375,45,389,394,229,231,191}
delta=17: {324,407,71,147,182,230,360}

q=883:
delta=1:  {756,747,550,666,839,408,727}
delta=17: {361,875,195,24,718,344,460}

## Interpretation

The hoped-for one-prime contradiction does not occur at 67,409,883. The local problem is now finite and explicit: for each prime, the Gaussian ratio r/s must occupy one of 32 cofactor roots (or a coordinate axis), while the quadratic-field factor chooses B or P16; if P16, its normalized square parameter must belong to the listed 7/8-element set.

The useful next step is therefore not another independent prime. We must compute the algebraic map from the Gaussian projective ratio r/s to the normalized U55 square parameter b^2/A (or an equivalent invariant). Once that map is explicit, intersect its images of the Gaussian root sets with the listed P16-admissible sets simultaneously at 67,409,883, with q=103 forcing the B branch. A missing intersection would be a rigorous local contradiction.
