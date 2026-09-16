# U56: coefficient-2 branch — audited direct Q(zeta_20) descent

Status: verified partial result within the evidence recorded here. This does not resolve Beal's conjecture.

Date: 2026-09-16.

This checkpoint re-audits a mathematically useful route that existed in an older off-main research commit and places only the rechecked conclusions onto the current `main` chain.

## 1. Input

Assume a surviving primitive positive solution

    X^10 + Y^10 = 2 Z^17,

with X,Y odd and coprime. From U46/U48,

    Phi := X^8-X^6Y^2+X^4Y^4-X^2Y^6+Y^8 = v^17,

and

    m=(X+Y)/2,
    n=(X-Y)/2,
    gcd(m,n)=1,
    m,n opposite parity,
    m+i n = Gaussian-unit*(r+i s)^17.

U46 gives Phi odd and 5 does not divide Phi.

## 2. Exact cyclotomic norm

Let xi=zeta_20 and M=Q(xi). Since

    Phi_20(T)=T^8-T^6+T^4-T^2+1,

we have the exact norm identity

    Norm_{M/Q}(Y+X xi)=Phi=v^17.                    (1)

The eight Galois conjugates Y+X xi^a, a in (Z/20Z)^*, are pairwise coprime as ideals. A common prime-ideal divisor of two distinct factors divides X(xi^a-xi^b); primitivity excludes primes dividing X, and root-of-unity differences are supported over 2 or 5. But their product Phi is odd and prime to 5.

The cyclotomic field Q(zeta_20) has class number one; the standard reference used here is J. M. Masley and H. L. Montgomery, `Cyclotomic fields with unique factorization`, J. Reine Angew. Math. 286/287 (1976), 248-256. Therefore

    Y+X xi = epsilon Gamma^17                         (2)

for a unit epsilon of O_M. Roots of unity cause no ambiguity modulo 17th powers because gcd(17,20)=1.

## 3. Real-unit basis re-audit

Let L=M^+=Q(a), a=xi+xi^(-1), so

    a^4-5a^2+5=0,
    disc(L)=2000.

The following three real units were used:

    e1=a^2-3,
    e2=a^3+a^2-3a-3,
    e3=a^2-a-2.

Wolfram `NumberFieldFundamentalUnits` independently returns a fundamental rank-three unit system for this quartic field. As a cross-check, the determinant of the logarithmic embedding matrix of e1,e2,e3 agrees with `NumberFieldRegulator[L]` to 50 decimal digits, with ratio exactly 1 at the displayed precision. Thus these units give the full real unit lattice in the computation used below.

The CM Hasse unit index [E_M : mu_M E_L] is 1 or 2, hence prime to 17. Therefore the classes of e1,e2,e3 span E_M/E_M^17 after roots of unity are discarded.

## 4. Exact q=1021 unit sieve

At q=1021, q splits completely in M and 17|(q-1). The eight roots of Phi_20 modulo q are exactly

    226, 250, 384, 486, 535, 637, 771, 795.

The exact 17th-power residue-character matrix of (e1,e2,e3) at those eight embeddings has rank 3 over F_17. Recomputing the Gaussian 17th-power projective condition for m+i n and testing every unit exponent triple in F_17^3 leaves exactly

    (j1,j2,j3)=(9,9,8), with n/m=0,
    (j1,j2,j3)=(9,8,9), with n/m=infinity.            (3)

No floating-point arithmetic enters this finite-field sieve.

The two surviving unit classes are represented by 1+xi and xi-1 respectively. Since the original equation is invariant under X -> -X and the automorphism xi -> -xi interchanges the two orientations, we may choose the plus orientation without loss:

    Y+X xi = (1+xi) Gamma^17.                         (4)

Using X=m+n and Y=m-n and putting

    mu=(xi-1)/(xi+1),

this becomes the exact untwisted equation

    m + mu n = Gamma^17.                              (5)

Together with the Gaussian descent,

    m+i n = rho^17                                    (6)

(up to an absorbable Gaussian unit).

In the chosen plus orientation, q=1021 forces

    1021 | n,
    1021 does not divide m.                           (7)

The orientation-free statement is 1021|mn.

## 5. Correct projective local test and additional forced divisors

A normalization error must be avoided here: after dividing by m, the common scalar m need not itself be a 17th power. Therefore the correct split-prime test is that the order-17 residue characters of all nonzero conjugates of

    1+i t,
    1+mu t,

where t=n/m, agree with one common scalar character; they are not required individually to be zero.

This corrected projective computation was executed exactly in Wolfram. For each of

    q = 1021, 1361, 2381, 3061, 4421, 5101,

all 20th roots split and 17|(q-1), and the only compatible projective ratio is

    t=0.

Hence, in the chosen plus orientation,

    1021*1361*2381*3061*4421*5101 | n,

and the exact product is

    228392811525274638941 | n.                        (8)

This is a strong lower-divisibility condition, not a contradiction and not an infinite-prime theorem.

## 6. Local-lifting limitation

The forced divisibility in (8) does not produce an automatic infinite descent. At any q in this list, q!=17, once n==0 mod q and m is a compatible unit, the maps

    z -> z^17

in the relevant unramified/split local algebras have derivative 17 z^16, a q-adic unit. Hensel lifting therefore supplies unique higher-precision 17th roots for arbitrary sufficiently q-divisible perturbations. Thus `q|n` cannot be iterated to `q^k|n for all k` by this local argument.

## 7. Two useful relative norm descents

Taking relative norms of Y+Xxi to the quadratic subfields gives exact identities.

To Q(i):

    R+iS = Norm_{M/Q(i)}(Y+Xxi),

where

    R=X^4-X^2Y^2+Y^4,
    S=XY(X^2-Y^2),
    R^2+S^2=Phi=v^17.

Since gcd(R,S)=1, R is odd and S even, Gaussian UFD yields

    R+iS=(C+iD)^17                                    (9)

for coprime C,D, after absorbing a unit.

To Q(sqrt(-5)):

    E+sqrt(-5)S = Norm_{M/Q(sqrt(-5))}(Y+Xxi),

where

    E=X^4-3X^2Y^2+Y^4,
    E^2+5S^2=Phi=v^17.

The class group of Q(sqrt(-5)) has order 2. Since gcd(17,2)=1, the coprime conjugate ideal factors principalize in the 17th-power relation; its units are +/-1 and are absorbed for odd exponent. Hence

    E+sqrt(-5)S=(P+Q sqrt(-5))^17.                    (10)

These are simultaneous exact descents, not heuristic congruences.

## 8. Literature check for the exact target

A fresh search of the 2024 survey `Generalised Fermat equation: a survey of solved cases` (arXiv:2412.11933) found no direct theorem or table entry resolving signature (10,10,17) or the exact equation

    X^10+Y^10=2Z^17.

The older Dieulefait-Freitas Q-curve theorem for x^5+y^5=2z^p has congruence hypotheses that do not include p=17, and the Billerey-Chen-Dieulefait-Freitas multi-Frey results used in U46 eliminate several local cases but not this surviving odd-square orientation. Therefore no published complete resolution is being imported here.

## 9. Current frontier

The coefficient-2 branch now satisfies simultaneously

    m+i n = rho^17,
    m+mu n = Gamma^17,
    R+iS = delta^17,
    E+sqrt(-5)S = eta^17,

with explicit definitions above and, in the chosen orientation,

    228392811525274638941 | n.

Merely adding more forcing primes is not the next proof step. The narrow global target is the Kummer ratio

    (m+mu n)/(m+i n) = (Gamma/rho)^17                (11)

inside Q(zeta_20), together with the requirement t=n/m in Q. The next useful investigation is to exploit the Galois/rationality constraints on this fixed Kummer equation, or the genus-three quotient from the audited older local route, rather than increasing local precision at already compatible primes.
