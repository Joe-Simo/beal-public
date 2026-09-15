# U65: the last Hecke check and an untwisted quintic descent

**Status: written partial theorems and exhaustive finite certificates, with same-model self-review and distinct exact implementations. The weighted equation and the full Beal conjecture remain unresolved. No independent expert or proof-assistant certification is claimed.**

Date: 2026-09-15 UTC. Base private repository revision: `43e60e0480485cb3c4f003f6ec8232674083848d` (U64). Existing U63/U64 archives, manuscripts, code and the current remote README were inspected before this extension. U41 remains invalidated; this checkpoint does not reinstate it.

## 1. Scope and results

The original target remains the positive-integer implication

    A^x+B^y=C^z, x,y,z>=3  =>  gcd(A,B,C)>1.

The active weighted auxiliary equation is

    X^10+256Y^10=Z^17, X,Y,Z>0, gcd(X,Y)=1.             (W)

Put U=X^2, V=2Y^2, and let rho be the positive real fifth root of 2. The new, unconditional necessary condition for (W), at the written-proof/computational-certificate level, is

    X^2+2*rho^3*Y^2 = beta^17,
    beta in Z[rho], Norm(beta)=Z,
    17 divides exactly one of X,Y.                    (1)

In particular, there is **no remaining unit ambiguity** in this quintic-field equation. The proof first establishes 289 explicit unit classes, then excludes 288 using necessary congruences modulo 17^2 and the independent Gaussian factorization. This does not say that (1) has no solutions. It does not classify all Beal signatures.

Separately, the newly recovered Hecke data for orbit h exclude h at 11. Thus b is the only survivor in U64's recorded eight-orbit list. The intended global level-lowering application and independent completeness of that list are still outstanding. The proof of (1) does not depend on these modular obligations, on identifying b with a CM object, or on U61/U62.

## 2. The recovered h record: an exclusion valid at every embedding

The primary LMFDB JSON for `2.2.5.1-2000.1-h` was retrieved successfully. It was a cached response with source timestamp 2026-09-14T23:11:48.936324; the exact selected entries and retrieval distinctions are in `references/U65/sources.json`. The common prime-ideal ordering is the previously inspected official exporter and explicit table, not a new guessed offset.

At the two norm-11 ideals, its eigenvalues are

    a = (-2e^3+15e^2+18e+120)/91,
    b = ( 2e^3-15e^2-18e+335)/91,
    F(e)=e^4-10e^3-13e^2+190e+241=0.

Writing N=-2e^3+15e^2+18e+120, exact division gives

    N^2-455N+5*91^2 = 0  (mod F).

Thus a and b=5-a each satisfy Q(T)=T^2-5T+5. The denominator 91 is prime to 17, so this relation holds at every prime of the coefficient field above 17.

For the corrected curve y^2=-f(x), U64's complete square/twice-square enumeration at 11 gives possible RM trace polynomials

    T^2+3T-9,  T^2-T-1,  T^2-9T+19.                (2)

Their integer resultants with Q(T) are respectively -44, -4, -4, none divisible by 17. Hence none has a common root with Q over any extension of F_17. This excludes either h eigenvalue from being the required residual trace; no assumption that two h entries are Galois conjugate at the two base primes is needed. Python produces Bezout certificates, TypeScript checks all elements of F_(17^2), and Wolfram reproduces the resultants and polynomial remainder.

The 35 parameter pairs in this prime-11 domain are nonsingular, including permitted individual zero coordinates. U64's proof of that complete domain is retained. This is the seventh excluded orbit, not a solution of (W): b survives and the modular prerequisites have not disappeared.

## 3. A parameter-independent splitting field and an exact index

Define

    f(T)=T^5+40UVT^3+320U^2V^2T+64(8V^5-U^5),
    F0=Q(rho),  rho^5=2,
    M=Q(rho,zeta),  zeta a primitive fifth root of unity.

A direct identity, valid for rational U,V, is

    Res_R(R^5-2, T-(2RU-2R^4V)) = f(T).            (3)

Consequently the five roots of f are

    r_j=2*rho*zeta^j*U-2*rho^4*zeta^(-j)*V,
    j=0,...,4.                                    (4)

The substitution into f and the resultant in (3) were checked symbolically. This is a classical radical/Dickson-polynomial identity specialized here; no novelty claim is made.

The discriminant is

    disc(f)=2^24*5^5*(U^5+8V^5)^4.                  (5)

For U^5+8V^5!=0 the five roots are distinct. The extension M has degree 20: X^5-2 is Eisenstein, [F0:Q]=5, Q(zeta)/Q is Galois of degree 4, and adjoining that Galois field preserves the relatively prime degree 5. Its automorphisms act on the labels in (4) by all maps j -> a*j+b over F_5 with a!=0. Distinct labels give distinct roots, so this action is faithful. Therefore the splitting field of f is exactly M for every such parameter pair, including U=1,V=0.

An exact refinement is useful. Let theta=2*rho*U-2*rho^4*V. Relative to 1,rho,...,rho^4, the coordinate matrix of 1,theta,...,theta^4 has determinant

    1024*(U^5+8V^5)^2.                             (6)

Section 4 proves Z[rho] is the full integer ring. For integral U,V and nonzero U^5+8V^5, (6) is therefore the order index

    [O_F0:Z[theta]]=2^10*|U^5+8V^5|^2.

For a solution of (W), this equals 2^10*Z^34. Thus the solution-dependent primes in the polynomial discriminant can enter an order index even though its splitting field is constant. One must not interpret (5) as an identical statement about field ramification.

Python and Wolfram compute (6) symbolically. TypeScript supplies an independent interpolation certificate: each side has degree at most 10 in each parameter, and agrees on the 11-by-11 grid U,V=-5,...,5. The degree bound follows because column j of the determinant has degree j. This finite grid proves a polynomial identity with that bound, not an integer-height exclusion.

### 3.1 What the constant field does and does not imply

On a genus-two curve y^2=-f(x), let W_j=(r_j,0) and let infinity denote the unique point at infinity. The divisor classes D_j=[W_j-infinity] satisfy 2D_j=0 and sum D_j=0. They generate the four-dimensional 2-torsion, with no other relation: a function of pole order at most four at infinity is a polynomial in x and cannot have an odd simple zero at just one of the W_j; the function y gives the single relation involving all five. Equivalently this is the usual branch-point description of hyperelliptic 2-torsion.

The label action above is the same for every parameter pair. Sending these labeled classes to those of the boundary curve C0:y^2=64-x^5 therefore gives an isomorphism of rational Galois modules on **2-torsion**. This is a global statement, not a four-prime numerical match. It does not identify the 17-torsion representation, prove that b is the boundary form, or show the Jacobians are isogenous. It closes a tempting but unproductive attempt to distinguish the survivor by its root field or mod-2 module alone.

## 4. The quintic integer ring and class number, with a small certificate

The polynomial R^5-2 has discriminant 50000=2^4*5^5. Thus only 2 and 5 can divide the index of Z[rho] in O_F0. At 2 it is Eisenstein, and at 5 the polynomial (R+2)^5-2 is Eisenstein, its constant being 30. In each completion the indicated generator (rho or rho-2) is a uniformizer of the totally ramified degree-five extension and generates its integer ring. To see the last assertion directly, expand an integral element successively in powers of the uniformizer using residue representatives in Z_p; the finite Z_p-algebra generated by the uniformizer is complete and contains these limits. Hence neither 2 nor 5 divides the index, and

    O_F0=Z[rho],  disc(F0)=50000,  signature=(1,2).

SymPy's exact integer-basis algorithm independently reproduces this basis and discriminant. The proof does not rest on a decimal approximation.

Minkowski's ideal-class bound [S2] is

    (5!/5^5)*(4/pi)^2*sqrt(50000).

Using pi>3 and sqrt(50000)<224 bounds it strictly by 28672/1875<16. Every ideal class therefore contains an integral ideal of norm at most 15. The necessary prime-ideal factors are determined by the following exact polynomial factorizations:

- at 2: R^5;
- at 3: (R-2)(R^4-R^3+R^2-R+1), with the quartic irreducible;
- at 5: (R-2)^5;
- at 7: (R-4)(R^4-3R^3+2R^2+R-3), with the quartic irreducible;
- at 11: R^5-2 is irreducible;
- at 13: (R-6)(R^4+6R^3-3R^2-5R-4), with the quartic irreducible.

The only prime ideals of norm at most 15 have norms 2,3,5,7,13, one each. In particular there are no omitted degree-two or degree-three primes of norms 4,8,9. Their generators are certified by

| Element | Field norm |
|---|---:|
| rho | 2 |
| 1+rho | 3 |
| 1+rho^2 | 5 |
| 1+rho+rho^2 | 7 |
| 1+rho^3-rho^4 | 13 |

An integral element of prime absolute norm generates an ideal of that prime norm. Every prime ideal required by the bound is therefore principal. Factoring a representative ideal proves

    class number(F0)=1.                            (7)

This is a proved field invariant, not an assumption of unique factorization in an unspecified number ring.

## 5. From the weighted equation to a seventeenth-power ideal

For a hypothetical solution of (W), X must be odd: if X is even, Y is odd and the left side has 2-adic valuation exactly 8, impossible for Z^17. Thus Z is odd and gcd(U,V)=1. U64's elementary modulo-25 argument also gives 5 not dividing Z; alternatively, unit tenth powers are +/-1 modulo 25 and a sum divisible by 5 has valuation exactly one.

Set

    gamma=U+rho^3*V=X^2+2*rho^3*Y^2.

Its norm satisfies the identity

    Norm(gamma)=U^5+8V^5=Z^17.                     (8)

Let p divide Z. Then p is odd, p does not divide V, and p does not divide U, by primitivity. For any prime ideal P above p dividing gamma, reduction gives

    rho^3=-U/V,
    rho=(rho^3)^2/2=U^2/(2V^2)  (mod P).           (9)

Since O_F0 is generated by rho, its residue field is F_p. Moreover (9) determines a unique prime ideal above p. Thus exactly one degree-one prime over p can divide gamma. In the ideal norm formula its valuation is therefore

    ord_P(gamma)=17*v_p(Z).

It follows that (gamma)=a^17, where a is an integral ideal of norm Z. By (7), a=(beta) for an integral beta. Hence

    gamma=epsilon*beta^17,  epsilon a unit.

The real embedding is unique. The sign of a field norm equals the sign in that embedding. If necessary replace beta by -beta and epsilon by -epsilon, preserving this equation because 17 is odd. We may and do arrange Norm(beta)=Z and Norm(epsilon)=1. No sign or common-base normalization is discarded.

## 6. Exactly 289 explicit unit representatives, without a regulator assumption

Define the integral units

    epsilon1=rho-1,
    epsilon2=rho^3+rho+1.

Their norms are both one, as direct resultant computations verify. Let E+ be the norm-one unit group. By the unit theorem [S2], E+ is free abelian of rank two: F0 has signature (1,2), its only roots of unity are +/-1, and -1 has norm -1.

We do **not** assert these two units form a fundamental system. It suffices to prove that their classes form a basis of E+/(E+)^17. The following two exact residue characters do that.

Reduce rho to 17 in F_103 and to 9 in F_137. These are fifth roots of 2 in the indicated fields. At q=103 use the order-17 element 64, and at q=137 use the order-17 element 119. For a unit eta define its character as the discrete logarithm of eta^((q-1)/17) with respect to that order-17 element. This is a homomorphism annihilating all seventeenth powers of units. Exact values are

| q | rho mod q | order-17 generator | character(epsilon1) | character(epsilon2) |
|---:|---:|---:|---:|---:|
| 103 | 17 | 64 | 4 | 14 |
| 137 | 9 | 119 | 3 | 3 |

The matrix determinant is 4 modulo 17, so these two unit classes are independent. Since the quotient has dimension two over F_17, they are a basis. Consequently every hypothetical solution can be written

    gamma=epsilon1^a*epsilon2^b*beta^17,
    0<=a,b<=16, Norm(beta)=Z.                      (10)

This proves completeness of the 289 representatives. It neither guesses a regulator nor assumes that a discovered subgroup is the full unit group.

## 7. A modulo-289 certificate that retains zero divisors

Let R=(Z/289Z)[rho]/(rho^5-2), and put q=17^4=83521. Its residue algebra satisfies rho^q=rho; the executable check reduces this polynomial identity modulo 17. Frobenius then gives z^q=z for **every** element of the residue algebra.

For any beta in R, write beta^q=beta+17c. Raising to the seventeenth power yields beta^(17q)=beta^17 modulo 289 by the binomial theorem. Thus every seventeenth power t satisfies t^q=t, including nonunits and zero divisors.

For epsilon_i define the five coefficient vectors

    L_i=(epsilon_i^(q-1)-1)/17  (mod 17).

They are well-defined because epsilon_i is a unit. Direct calculation gives

    L1=(0,10,4,3,12),
    L2=(0,14,13,7,6).

Equation (10) therefore implies, in the full five-dimensional residue algebra,

    (gamma^q-gamma)/17 = gamma*(a*L1+b*L2) (mod17). (11)

No inverse of gamma is used. This is important when 17 divides Z. Equation (11) is a necessary finite test; it is not claimed to be sufficient for a global seventeenth power.

The finite domain consists of every U that is a square modulo 289 and every V that is twice a square, excluding only U=V=0 (the only such pair divisible by 17 in both coordinates). There are 137 values of each kind, hence 18768 pairs. First retain Norm(gamma)=U^5+8V^5 in the complete scalar seventeenth-power image modulo 289, which includes zero and has 17 values. Exactly 1104 pairs remain.

Solving all five equations (11) for every remaining pair leaves exactly 24 parameter pairs. The unit classes are

    (a,b)=(0,0): 16 pairs,
    (a,b)=(0,14): 8 pairs.                         (12)

The TypeScript implementation uses precisely this full-algebra calculation. The Python implementation instead factors R into its lifted linear component rho=49 and an unramified quartic component, uses separate Fermat quotients, and explicitly retains the possible nonunit linear component. Their entire 24-row output, including all square-root choices used below, agrees. Wolfram independently reproduces the full-algebra count. A rank failure would stop the checker, not silently prune a pair; none occurs in this complete domain.

## 8. The Gaussian equation removes the last nontrivial class

In Z[i], the factors X^5+16iY^5 and X^5-16iY^5 are coprime. A common Gaussian prime divides both 2X^5 and 32iY^5; away from 2 this contradicts gcd(X,Y)=1, while the prime above 2 cannot divide X^5+16iY^5 because X is odd. Their product is Z^17. Unique factorization therefore gives

    X^5+16iY^5=(r+is)^17                            (13)

for integers r,s, after absorbing the Gaussian unit; every Gaussian unit is its own seventeenth power.

Modulo 289, i can be sent to 38 or -38, which are distinct simple square roots of -1. Thus for every pair X,Y lifting one of the U,V rows in (12), both

    X^5+38*16Y^5,  X^5-38*16Y^5

must belong to the complete scalar seventeenth-power image modulo 289. Python tests both split components for every square-root choice. TypeScript instead tests G^17=G directly in (Z/289Z)[i], avoiding the split implementation. Wolfram reproduces the split comparison.

All eight rows with (a,b)=(0,14) fail. The 16 surviving rows have (a,b)=(0,0). They are exactly

    U=0, V in {18,43,100,106,183,189,246,271},
    V=0, U in {1,38,110,134,155,179,251,288}.

Each has 34 compatible pairs X,Y modulo 289, for 544 total. These are modular residue pairs, not global weighted solutions. Individual zero coordinates are retained: a positive integer can be divisible by 17. Coprimality only excludes simultaneous divisibility.

In (10), (a,b)=(0,0) means the unit factor was a seventeenth power of an integral unit and can be absorbed into beta. This proves (1). The axis condition gives 17|X or 17|Y, never both. This is not a descent to zero, nor a bound on either base.

## 9. Adversarial review and limitations

The argument was checked for the earlier normalization errors that affected this project. It uses no projective rescaling, does not assume that a ratio of squares is square when its denominator is arbitrary, and does not divide bases with unequal exponents. Positive bases equal to one are not discarded. The quintic field F0, quadratic RM field K, and Gaussian field are distinct and are not conflated.

The new norm descent is independent of the invalidated U41 and the unresolved level-lowering adaptations. The CM-boundary and mod-2 module observation is not used to identify a mod-17 representation. The prime-field unit characters establish a basis modulo seventeenth powers only; that is exactly the unit ambiguity needed. The modulo-289 computation explicitly allows 17|Z and uses all lifts of square parameters, including zeros and all signs.

Passing code is not a certificate of the whole mathematical inference. The finite enumerations and polynomial identities have distinct exact implementations; the written field, ideal and Galois arguments have only same-model review. A fresh expert or proof assistant has not verified this result. U61/U62 retain their previous limited status and are neither strengthened nor invalidated here.

An initial Wolfram resultants call had an invalid Table iterator; the resultants portion remained unevaluated and was not used. A corrected call returned the exact resultants above. An initial TypeScript command used a nonexistent absolute compiler path and therefore did not execute; the PATH-resolved compiler was then run successfully. These failures and the actual successful commands are retained, not counted as passed checks.

## 10. Research state and next executable question

The weighted equation remains open. The new algebraic target is the untwisted identity

    (b0+b1*rho+b2*rho^2+b3*rho^3+b4*rho^4)^17
        = X^2+2*rho^3*Y^2,
    Norm(beta)=Z, gcd(X,Y)=1, X,Y,Z>0, 17|XY.

The coefficients of rho, rho^2 and rho^4 must vanish exactly; the constant and rho^3 coefficients have the indicated square forms. Eliminating these simultaneous integral conditions, rather than increasing a finite prime list that admits the boundary, is the next arithmetic task. A certified parametrization or a global impossibility argument is still missing. No height bound, rational-point classification or weighted-equation solution is asserted.

The modular track separately has only orbit b left in its recorded list, but still needs the prescribed global lifts, independent newspace completeness, and a global identification or exclusion of the boundary-type mod-17 representation. The full original Beal conjecture still has infinitely many signatures not covered by any of these partial steps.

## Sources and reproducibility

[S1] LMFDB `hmf_hecke` record `2.2.5.1-2000.1-h`; exact selected entries and cached-response metadata are retained in `references/U65/sources.json`. U64 records the other seven entries and their common prime ordering. No claim is made that the full raw API body was downloaded to this container.

[S2] J.S. Milne, *Algebraic Number Theory*, version 3.08 (2020-07-19), Proposition 3.53 (printed p.66), Theorem 4.3 (p.70), and Theorem 5.1 (p.85). Original PDF text and the corresponding page images were inspected this run. These supply Eisenstein ramification, the ideal-class norm bound, and the unit rank. The specialized class-number calculation, explicit quotient basis and unit cancellation are derived above.

[S3] Martin Azon, *Effective Darmon's program for the generalised Fermat equation*, arXiv:2504.01967v2 (2025-07-03), is the upstream source for the Frey-family/RM setup in U63/U64. U65 does not invoke an unproved global level-lowering conclusion. The root, norm and index identities are checked directly here.

Run the commands in `research/computations/U65/reproduce.py`. This executes the Python and TypeScript checkers, strict type checking, Python compilation/tabnanny, and the complete row comparison. Actual Wolfram inputs/outputs and recovered-source metadata are also retained. No Lean, Magma, Sage, standalone linter, parallel independent agent, external expert contact, publication, or prize submission is claimed.
