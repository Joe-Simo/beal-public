# U62: closing the coefficient-two implication and recording its exact Beal coverage

Status: complete written proof of a partial theorem, with self-review and exact computational corroboration. Independent expert review and proof-assistant verification remain outstanding. The full Beal conjecture is not solved.

Research session: 2026-09-14, America/New_York. Base remote revision inspected: f772322044f1ce18cc2aa6c4876d07f0fe88f3ec (U60). U61 was recovered from its actual attached evidence archive and its mathematical computations were replayed, not inferred from an earlier chat summary.

## 1. Claims and scope

**Theorem 1 (coefficient two).** For positive integers X,Y,Z with gcd(X,Y)=1,

    X^10 + Y^10 = 2 Z^17

implies (X,Y,Z)=(1,1,1).

**Corollary 2 (a family in the original Beal problem).** For integers r>=2, k>=1, l>=1, there is no solution in positive integers E,O,C to

    E^(2r) + O^(10k) = C^(34l),
    gcd(E,O,C)=1,
    E even, O odd.

The letters E and O specify the parities of the bases; they are not an ordering by size. Interchanging the two summands gives the same covered family. The equation with an even base carrying exponent 10k and an odd base carrying the other exponent is NOT automatically covered by this statement.

These claims depend on the written U61 exclusion and the established external theorem identified below. They are not claims of a complete Beal solution, global novelty, independent expert acceptance, formal verification, or prize eligibility.

## 2. External dependency checked at its original source

Billerey, Chen, Dieulefait and Freitas, *A multi-Frey approach to Fermat equations of signature (r,r,p)*, Transactions of the AMS 371 (2019), 8651-8677, DOI 10.1090/tran/7477. The inspected author text is arXiv:1703.06530v4, Theorem 5 and its proof in section 5.1, together with Proposition 4(2).

The application needed here is only this: a nontrivial primitive solution of a^5+b^5=2c^17 cannot have 5 dividing a+b. The source's nontriviality and primitivity definitions were checked. Its proof covers p=17 without an additional congruence restriction. This is a use of an established theorem, not a claim to have rerun the authors' Hilbert-newform computation. The source/version record is in references/U62_sources.md.

## 3. Reduction to two coprime seventeenth powers

Suppose X,Y,Z satisfy Theorem 1. If X=Y, coprimality gives X=Y=1 and the equation gives Z=1. Hence assume X!=Y for the remainder of the contradiction argument. A base equal to one is not otherwise excluded.

The equation modulo 2 says X and Y have the same parity. Their coprimality makes both odd. Their tenth powers are 1 modulo 8, so Z is odd as well. Any prime dividing X and Z would divide Y by the equation, and conversely; thus the three bases are pairwise coprime.

Put a=X^2 and b=Y^2. Then gcd(a,b)=1 and

    a^5+b^5=2Z^17.

This is nontrivial in the source's sense: X!=Y and positivity imply |abZ|>1. Section 2 therefore gives 5 not dividing a+b.

Define

    Phi(a,b)=a^4-a^3b+a^2b^2-ab^3+b^4.

The identities

    (a+b)Phi(a,b)=a^5+b^5,
    Phi(a,b) mod (a+b) = 5b^4

show that gcd(a+b,Phi) divides 5: gcd(a+b,b)=1. Since 5 does not divide a+b, the two factors are coprime. They are positive; Phi is odd and a+b is twice an odd number because a and b are odd squares. Unique factorization of positive integers now gives coprime positive u,v with

    a+b=2u^17,   Phi(a,b)=v^17,   Z=uv.             (3.1)

The exact exponent of 2 is checked here rather than discarded by a normalization of unequal exponents. At an odd prime only one of the two coprime factors can carry its valuation, which must be a multiple of 17.

## 4. The Gaussian equation, including signs and primitive coordinates

Set

    m=(X+Y)/2,    n=(X-Y)/2.

Both are integers, m>0 and n!=0. Their gcd is one: a common divisor would divide X and Y. Also m+n=X is odd, so m and n have opposite parity. No assumption X>Y is made; n may be negative. Equation (3.1) gives

    m^2+n^2=u^17.                                  (4.1)

A common Gaussian prime divisor of m+in and m-in divides both 2m and 2n. Bezout for gcd(m,n)=1 forces it above 2, but 1+i does not divide m+in when the coordinates have opposite parity. The Gaussian factors are therefore coprime.

The Euclidean property of Z[i] and (4.1) imply m+in=eta*beta^17, where eta is a Gaussian unit. Since eta^17=eta, replace beta by eta*beta to absorb the unit. Write beta=r+is. Then

    m+in=(r+is)^17.                                (4.2)

If a rational prime divided r and s it would divide m and n, so gcd(r,s)=1. If r and s were both odd, their norm would be even and so would m^2+n^2, which it is not. They cannot both be even by coprimality. Thus r,s have opposite parity. All Gaussian hypotheses of U61's Theorem A are present.

## 5. Quadratic-field ideal descent with every exceptional prime retained

Let omega=(1+sqrt(5))/2 and K5=Q(sqrt(5)). Its integer ring is Z[omega], with omega^2=omega+1. Define

    h0=m^4+30m^2n^2+n^4,    h1=-16m^2n^2,
    H_-=h0+h1*omega,         H_+=conjugate(H_-).

Exact polynomial identities give

    Phi((m+n)^2,(m-n)^2)
      =m^8+44m^6n^2+166m^4n^4+44m^2n^6+n^8
      =H_- H_+=v^17.                              (5.1)

Suppose a prime ideal divides both H_- and H_+. Their difference is -16sqrt(5)m^2n^2. At a residue characteristic other than 2 and 5, this would force m or n to vanish in the residue field. The other coordinate is nonzero, by integer coprimality, and H_- then becomes its nonzero fourth power. This is a contradiction.

No prime above 2 divides either factor: the norm in (5.1) is odd. No prime above 5 divides either factor: Phi(a,b)=(a+b)^4 modulo 5 and 5 does not divide a+b. This separately disposes of the ramified prime; no argument based only on a generic resultant is used.

Consequently (H_-) and (H_+) are coprime ideals. Equation (5.1) and unique factorization of ideals give (H_-)=J^17 for an integral ideal J.

K5 has class number one: its real-quadratic Minkowski bound is sqrt(5)/2<2, so every class contains an integral ideal of norm one. The units are +/-omega^j. For completeness, omega is fundamental: a positive unit eta with 1<eta<omega would have eta=(a+b sqrt(5))/2 and conjugate eta'=+/-eta^(-1). Then b=(eta-eta')/sqrt(5) lies strictly between zero and one for either norm sign, impossible for an integer b. The rank-one unit theorem completes the generation claim.

It follows that for integers A,B and some j in {0,...,16},

    H_-=omega^j (A+B*omega)^17.                    (5.2)

The sign is absorbed because 17 is odd; any exponent of omega is reduced modulo 17 by multiplying A+B*omega by an integral unit.

**Coordinate coprimality.** The integer coefficients h0,h1 are coprime. Indeed, h0 is odd, and an odd prime dividing h1 divides m or n, in which case h0 is the fourth power of the other, nonzero coordinate modulo that prime. If a rational prime divided both A and B, equation (5.2) would place H_- in that prime times Z[omega], even after multiplication by a unit; this would make both h0 and h1 divisible by that prime. Thus gcd(A,B)=1.

This verifies a hypothesis that must not be inferred just from the field norm.

## 6. Full-scale finite certificates eliminating nonzero unit classes

The following local test is a necessary condition for equations (4.2) and (5.2). For each q, enumerate the full algebras

    Rg=(Z/qZ)[i]/(i^2+1),
    R5=(Z/qZ)[omega]/(omega^2-omega-1).

Let Ig be the set of all seventeenth powers in Rg except (0,0), and I5 the set of all seventeenth powers in R5, including zero. For every j, retain precisely those (m,n) in Ig for which H_-(m,n) belongs to omega^j I5. Only the simultaneous Gaussian zero is excluded, since gcd(m,n)=1. Individual zero coordinates and nonzero zero divisors are not omitted. No projective scaling, assumption that b^2/A is square, or choice of a seventeenth root is involved.

The complete counts, reproduced this run, are:

| q | Gaussian nonzero power images | All quadratic power images | j | Compatible pairs |
|---|---:|---:|---:|---:|
| 67 | 264 | 265 | 0 | 132, all mn=0 |
| 67 | 264 | 265 | 15 | 132, all m=+/-n |
| 67 | 264 | 265 | every other j | 0 |
| 409 | 624 | 625 | 0 | 48, all mn=0 |
| 409 | 624 | 625 | 15 | 0 |

Here mn=0 and m=+/-n refer only to the indicated finite field, not to equality of the integer coordinates. At q=409 the algebras split; 48 nonzero Gaussian power images of norm zero were explicitly included before the test. None survives its j=0 test, and j=15 has no survivor at all.

Python independently enumerates q^2 base elements in each algebra and uses seventeen successive multiplications. TypeScript uses bigint and binary exponentiation; at q=409 it instead reconstructs the complete image from both split components. Wolfram independently performs this split calculation. At q=409 the roots are i=143,266 and omega=130,280; there are 25 scalar seventeenth-power values including zero. Thus the split implementation enumerates all 25^2 ordered component outputs and is exhaustive for that image, not a sampled search.

The q=67 result leaves j=0,15; q=409 eliminates j=15. Therefore every integer solution under investigation satisfies

    H_-=(A+B*omega)^17.                            (6.1)

These finite checks eliminate a finite unit ambiguity. They are not finite evidence being substituted for an infinite height bound.

## 7. Application of U61 and completion of Theorem 1

The recovered U61 manuscript's Theorem A rules out the simultaneous system consisting of (4.2), (6.1), gcd(r,s)=gcd(m,n)=gcd(A,B)=1, opposite parities of r,s, and mn!=0. Sections 3-6 above establish every one of these hypotheses from a nontrivial positive primitive coefficient-two solution.

U61 reduces this system, using U60's corrected coefficient identities and modulo-289 certificate, to rational

    g(t)=17w^2,   t>2,
    g(t)=t^8+t^7-7t^6-6t^5+15t^4+10t^3-10t^2-4t+1.

It excludes that region by an explicit quadratic-field elliptic descent and a one-variable 3-adic rationality argument. The rationality function, two-isogeny rank calculation, needed 3-saturation, and integral higher-order estimate are in U61; they are not replaced here by a claim that numerical tests prove rational-point completeness.

Invoking that written exclusion contradicts mn!=0. The discarded X=Y boundary was exactly (1,1,1), so Theorem 1 follows.

**Verification status of this invocation:** U61 is a complete written partial proof with self-review and exact arithmetic support, not an independently certified external theorem. U62's conclusion inherits this status. Any subsequently discovered flaw in U60 or U61 invalidates the dependent coverage until repaired.

## 8. Direct proof of the original-Beal corollary

Suppose a solution of Corollary 2 existed. For the original coefficient-one equation, a prime dividing two bases divides the third, so gcd(E,O,C)=1 gives pairwise coprimality. The positive integers

    E^r,   O^(5k),   C^(17l)

form a primitive Pythagorean triple, with the first leg even and the second odd. The primitive Pythagorean parametrization gives coprime M>N>0 of opposite parity with

    E^r=2MN,
    O^(5k)=M^2-N^2,
    C^(17l)=M^2+N^2.                               (8.1)

The two factors M-N and M+N are positive, odd, and coprime. For their gcd divides 2M and 2N and is odd. Their product is O^(5k), so unique factorization yields coprime odd integers u<v with

    M-N=u^(5k),   M+N=v^(5k).

Adding their squares and using (8.1) gives

    u^(10k)+v^(10k)=2C^(17l).

Put X=u^k, Y=v^k, Z=C^l. These are positive, gcd(X,Y)=1, and satisfy Theorem 1. It forces X=Y=1, contradicting u<v. This proves Corollary 2 without an unverified historical chain of exponent reductions.

Both left exponents and the right exponent are >=3. No base was divided by a common factor in an unequal-exponent equation. The only term interchange permitted is that of the two summands. The proof does not bound k,l,r or the bases.

## 9. Adversarial audit of the inherited partial proof

U61's actual text and supporting code were inspected, and its global reduction, elliptic computations, scale audit, finite-field computations and independent TypeScript checks were rerun. The mathematical outputs reproduce the archived outputs. The review specifically checked:

- The norm/total-positivity distinction in the quartic twist over Q(sqrt(17)). The two quadratic fields in the investigation are kept separate.
- The upper bounds and attained classes in the two Kummer images, rather than assuming a full Mordell-Weil generator.
- The explicit parameter of 8P used to prove the required 3-saturation.
- The inclusion of all residue disks, the absence of denominator poles, and the integral factorial estimate for the nonlinear analytic coefficients.
- The strict t>2 region and the surviving t=2 boundary, not an unjustified classification of all real regions.
- Full scale and zero divisors in the q=409 unit elimination, and signed n in the Gaussian equation.

No gap was found in these inspected steps. This is additional scrutiny by the same model, not a fresh mathematician, a fresh independent agent, or a proof-checking kernel. Agreement of computational implementations does not certify all mathematical inferences.

A replay comparator initially failed because it compared a wall-clock field called elapsed_seconds. Recursive comparison showed that field was the only discrepancy. Both output files are preserved unchanged, and reconciliation.json explicitly excludes that timing metadata only. No mathematical mismatch was suppressed.

The new Python and TypeScript checks completed. Strict TypeScript type checking, Python compilation, and tabnanny completed. No standalone linter or Lean/Magma/Sage runtime is installed; none is reported as having run. The source's modular-form computation is an established-literature dependency rather than a newly executed calculation here.

## 10. Coverage, outstanding verification, and next research question

At the written-proof level, this checkpoint adds:

1. The coefficient-two theorem with its sole positive primitive solution (1,1,1).
2. The infinite parity-specified Beal family of Corollary 2.

It does NOT establish the whole original conjecture, all all-even cases, all exponent-17 cases, the reversed parity orientation, the weighted equation X^10+256Y^10=Z^17, or the mixed odd-prime signatures. Historical modular-method claims about the weighted equation are not promoted by this result.

Best next mathematical action: audit the separate weighted orientation against its actual preserved Frey-curve and level-lowering hypotheses, beginning at its earliest unsupported implication. This is a different branch; another run of the already completed q=67/409 sieve would not advance it. Independent expert or formal verification of U61 remains the verification priority for the present partial theorem. Novelty has not been established by the documented search.

Preservation details and current commit status are recorded separately in U62_preservation.json so that old U61 statements about its then-unavailable write connection are not silently rewritten. All prior mathematical files are retained unchanged.
