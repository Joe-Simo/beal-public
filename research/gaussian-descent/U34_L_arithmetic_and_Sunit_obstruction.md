# U34: arithmetic of L=Q(sqrt(17),zeta_5) and obstruction to a fixed S-unit reduction

Status: verified partial result only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Setting

Continue from U33 in the valid weighted branch

    X^10 + 256 Y^10 = Z^17.

Put K=Q(sqrt(17)), eta=4+sqrt(17), x=gamma, y=eta*delta, and

    L = K(zeta_5) = Q(sqrt(17), zeta_5).

U33 gives

    x^5-y^5 = product_{i=0}^4 (x-zeta_5^i y)
            = (8 b^2/17) R(a,b),

with pairwise coprime linear factors away from primes above 5. It also separates R from the known forced divisors of b outside the finite exceptional rational set {2,5,11,13,17,19}.

The purpose here is to determine the arithmetic of L exactly and test whether U33 already implies a finite S-unit / Thue-Mahler system.

## 1. Exact number-field data

A defining polynomial for L is

    f(T)=T^8-T^7+5T^6-9T^5+29T^4+36T^3+80T^2+64T+256.

The current LMFDB record is

    8.0.1305015625.1.

Its exact database data are:

- degree 8;
- signature (0,4), so unit rank 3 by Dirichlet;
- discriminant 1305015625 = 5^6*17^4;
- conductor 85;
- Galois group 8T2 = C4 x C2;
- class number 1 and trivial class group;
- narrow class number 1;
- torsion subgroup of the unit group has order 10;
- relative class number 1;
- the LMFDB record marks `used_grh=false`.

Thus every ideal of O_L is principal. The full unit group has the form

    O_L^* ~= mu_10 x Z^3.

Wolfram independently computes three fundamental units for this same field. In the LMFDB polynomial generator alpha they may be represented by

    eps1 = AlgebraicNumber(alpha,{1,-51/116,181/464,0,0,0,1/116,1/464}),
    eps2 = AlgebraicNumber(alpha,{-1,-1,-181/464,0,0,0,0,-1/464}),
    eps3 = AlgebraicNumber(alpha,{49/29,5/29,-81/464,-9/64,5/64,-45/1856,25/1856,-9/1856}).

Only the existence of a rank-3 basis is used below; the precise basis can be changed later for convenience.

## 2. Prime decomposition counts for the candidate exceptional set

Take the rational exceptional set from U33

    S_Q={2,5,11,13,17,19}.

Since L/Q is abelian with Galois group C4 x C2, the splitting counts can be read from the quadratic character for Q(sqrt(17)) and the order modulo 5 for Q(zeta_5).

Exact residue checks give

    (17/11)=-1,
    (17/13)=1,
    (17/19)=1,
    (17/5)=-1,

and

    ord_5(2)=4,
    ord_5(11)=1,
    ord_5(13)=4,
    ord_5(19)=2.

Therefore the numbers of prime ideals of L above these rational primes are:

- 2: two primes (unramified, residue degree 4);
- 5: one prime (ramification index 4, residue degree 2);
- 11: four primes (unramified, residue degree 2);
- 13: two primes (unramified, residue degree 4);
- 17: one prime (ramification index 2, residue degree 4);
- 19: four primes (unramified, residue degree 2).

Hence there are 14 prime ideals above S_Q.

The corresponding S-unit group has free rank

    3 + 14 = 17.

Modulo tenth powers its abstract quotient therefore has size

    |O_{L,S}^*/(O_{L,S}^*)^10| = 10^18,

because mu_10 contributes one additional factor of order 10.

This is finite, but far too large to enumerate naively; any useful Thue-Mahler reduction needs substantially more structure.

## 3. Class number one does NOT yet imply tenth powers up to fixed S-units

For a fixed finite S, to conclude

    x-zeta_5^i y = epsilon_i * theta_i^10

with epsilon_i an S-unit, one must know that every prime ideal outside S occurs in the linear factor with valuation divisible by 10.

U33 proves this divisibility for primes coming from the forced b^2 contribution: if q|b and q is outside {2,5,17,19}, then the full contribution

    2 v_q(b)=10 v_q(B)

lands in exactly one linear factor over each relevant prime.

However, the second factor R(a,b) has moving prime support. U33 only proved that R is coprime to the forced b-part away from a finite exceptional set; it did not prove that primes dividing R lie in a fixed S or occur to valuations divisible by 10.

This is a real obstruction, not a technicality. The rational norm of R is

    Norm_{K/Q}(R)
      = 17*(323 a^12 -1326 a^10 b^2 -867 a^8 b^4
             +7548 a^6 b^6 -7667 a^4 b^8
             +1938 a^2 b^10 -13 b^12).

For generic coprime parity-compatible inputs, this norm acquires primes outside S_Q with exponent 1. For example, at (a,b)=(1,2), exact factorization gives

    |Norm(R(1,2))| = 13 * 17 * 33287.

The prime 33287 is outside S_Q and occurs only to the first power. This example is not asserted to satisfy the full Case-III equations; it demonstrates that no polynomial identity confines the support of R to the fixed exceptional set or forces tenth-power valuations automatically.

Therefore the proposed implication

    pairwise-coprime linear factors + class number one
      => each factor is a tenth power up to a fixed S-unit

is currently invalid.

## 4. What class number one DOES buy us

The class-number computation is still useful:

1. Any ideal-theoretic tenth-power statement that can be proved later immediately lifts to an element statement, with only unit ambiguity.
2. The unit ambiguity has rank only 3 before S-primes are introduced.
3. The only obstruction to a fixed-S tenth-power formulation is now explicit: control of the moving prime divisors of R(a,b).

Thus the next useful target is not further ideal principalization. It is to force a power structure on R, eliminate R, or replace the factorization by an auxiliary equation in which the moving R-support disappears.

## 5. Literature check

A fresh search for the exact weighted equation

    U^5 + 8 V^5 = Z^17

(and the original X^10+256Y^10=Z^17 form) found no direct published resolution. The current generalized-Fermat survey likewise does not list this weighted signature-(5,5,17) equation as solved.

## Next obligation

Do not enumerate the 10^18 S-unit classes. Instead attack the moving factor R. The most promising concrete options are:

- derive an independent power/norm constraint on R from the simultaneous gamma/delta equations;
- construct a Frey object directly for U^5+8V^5=Z^17 so the coefficient 8 is built into the conductor calculation;
- or find a second algebraic factorization whose gcd with R forces its outside-S prime valuations into multiples of 5 or 10.

Until such a step is proved, U33 does not reduce the weighted branch to a finite fixed-S Thue-Mahler system.