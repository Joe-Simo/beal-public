# U79: the complete dyadic Kummer image and an excluded global candidate

**Status: written, self-reviewed local-image theorem and global-candidate exclusion, with distinct exact arithmetic checks. The class-group computation, full global restriction matrix, numerical rank upper bound, weighted equation, and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-15. Remote input read: `e5457c3a63843b1e664a4ee7dca83b334bc2c22b` in private `Joe-Simo/beal`. The attached U78 archive was restored additively: 50 new entries, two identical entries, no conflicting file overwritten. All manifest hashes were checked and the entire U78 Python output was reproduced unchanged. No other mathematical project was accessed.

## 1. Result and precise scope

Keep U78's curve

    k=Q(phi), phi^2-phi-1=0,
    C: v^2=phi+2-4(3-phi)u^17, J=Jac(C).

Let K=k_2 be the completion at its unique prime above 2. It is the unramified quadratic extension of Q_2. Set

    E=K(s), s^17=2/phi=2phi-2,
    O_E=O_K[s], v_s(s)=1, v_s(2)=17.

Its residue field is F_4, with basis 1,phi over F_2. As in U78, H_2 is the norm kernel in E*/E*^2 and W_2 is the image of J(K)/2J(K) under the odd-degree Kummer map.

**Theorem 1 (complete image).** The following sixteen squareclasses form a basis of W_2:

    [1+s^n], [1+phi*s^n], n=19,21,23,25,27,29,31,33.    (1.1)

Thus the previously missing local subspace is determined, not only its dimension. The proof constructs sixteen actual local divisor classes, certifies their Kummer images as explicit products of (1.1), and proves that the resulting sixteen-by-sixteen binary matrix is invertible.

**Theorem 2 (explicit test).** Normalize a class of H_2 to a principal unit by dividing out a square valuation factor and a square lift of its residue. In the ordered unit-squareclass basis

    [1+s^n], [1+phi*s^n], n=1,3,...,33,
    [1+s^34],                                             (1.2)

the class belongs to W_2 if and only if its sixteen coordinates at odd levels 1,3,...,15 vanish. This defines an explicit surjective linear map

    lambda_2:H_2 -> F_2^16, ker(lambda_2)=W_2.             (1.3)

The normal-form procedure and its exact arithmetic implementation are supplied below. The statement is restricted to the norm kernel; dropping that hypothesis would make the sixteen-coordinate test insufficient.

**Corollary (a genuine candidate exclusion).** U78's nonzero global candidate

    alpha=(s+1)/(1+s^17)=1/h(s),
    h(s)=s^16-s^15+...-s+1,

passes the prime-5 condition but fails (1.3). Therefore it is not in Sel_2(J/k). This is an exclusion of one explicitly named squareclass in U78's global candidate space, not an exclusion of every candidate or a new weighted solution family.

Writing d=dim Cl(O_F)[2] as in U78, the remaining global map is now explicit locally:

    Psi:V -> F_2^16 direct_sum F_2,
    alpha -> (lambda_2(loc_2(alpha)), lambda_5(loc_5(alpha))),
    dim V=17+d, Sel_2(J/k)=ker(Psi).                       (1.4)

A complete global basis of V and d remain unknown, so the matrix of (1.4) on that basis is not computed. No numerical rank upper bound or rank-zero claim follows from this checkpoint. U77's implication from a weighted solution to positive rank is retained only as the inherited application, not as a premise of the local theorem.

## 2. Local squareclasses with a certified precision cutoff

The polynomial S^17-2/phi is Eisenstein over O_K, so E/K is totally ramified of degree seventeen and s is a uniformizer. In particular the ring used by both checkers is the correct local integer ring. Modulo 8 it is represented in the free basis

    s^j, phi*s^j, 0<=j<=16.

A coefficient a+b*phi in K has 2-adic valuation min(v_2(a),v_2(b)), because their reductions in F_4 are independent. The valuation of the j-th coefficient term is therefore

    j+17*min(v_2(a),v_2(b)).

The different j have different residues modulo seventeen, so they cannot cancel each other's lowest valuation. The two equations for the ring are retained exactly; it is not replaced by F_4[s] when carries by 2 matter.

Every unit in 1+s^35 O_E is a square. Indeed the polynomial Z^2-a at Z=1 has derivative of valuation seventeen and residual valuation at least 35>2*17; the elementary strong Hensel criterion applies. Hence equal unit residues modulo s^35 have equal squareclasses. Working modulo 8 loses only terms of valuation at least 51 and is more precise than required.

### 2.1 Constructive normal form

After an initial residue normalization, let a be in 1+s O_E. For successive depths n=1,...,33, remove its leading coefficient as follows.

* If n is even, write the leading coefficient as b^2 in F_4 and divide by the square (1+b*s^(n/2))^2. Since n/2<17, its leading term is exactly b^2*s^n; the cross term has strictly greater valuation.
* If n is odd, express the leading coefficient in the basis 1,phi and divide by the corresponding product of 1+s^n and 1+phi*s^n, recording the two exponents modulo two. All cross terms occur at greater depth.

At depth 34, squares of 1+b*s^17 have coefficient

    b^2+phi*b=phi^2*((b/phi)^2+b/phi).

The image is the one-dimensional subgroup phi^2*AS(F_4), where AS(z)=z^2+z. The remaining squareclass bit is

    Tr_(F_4/F_2)(coefficient/phi^2).

The element 1+s^34 represents the nonzero bit. The rest, at depth at least 35, is a square by the preceding cutoff. This proves that (1.2) generates the unit squareclasses.

It also proves independence. A square (1+w)^2 with 0<v_s(w)<17 has first term at the even level 2v_s(w); for v_s(w)>=17 it has first term at level at least 34. It cannot have first term at an odd level below 34. At a fixed odd level, 1 and phi are F_2-independent. Finally the trace test distinguishes the top level from squares. Thus (1.2) is a basis, with 35 elements. Including the valuation class [s] gives the expected 36-dimensional full squareclass space.

The Python implementation returns this normal form for principal units. Arbitrary representatives must first be normalized as stated; it does not silently accept elements of odd valuation as norm-kernel candidates. Squaring all 35 basis generators, testing their distinct coordinates, and checking 32 deterministic product comparisons validate the implementation against this proved basis. They do not replace the basis proof.

## 3. Actual local divisors producing the sixteen witnesses

Write

    Delta=3-phi, A=-4Delta, B=phi+2=Delta*phi^2,
    b0=A^16*B=2^32*Delta^17*phi^2.

The change x=A*u, y=A^8*v gives the monic model

    y^2=x^17+b0.                                        (3.1)

Its branch root in E is xi=A/s^2=-4Delta/s^2. It generates E because its rescaled root s^(-2) recovers s using s^17=2/phi. In particular the branch polynomial has exactly one irreducible factor over K.

For each odd d in {1,3,5,7,9,11,13,15} and each a in {1,phi}, introduce the degree-d extension

    K_d=K(pi), pi^d=2/a,
    z=2/pi.

The polynomial for pi is Eisenstein; for d=1 this just means K_d=K. Define

    w=b0/z^34=Delta^17*phi^2*pi^(34-2d)/a^2.

It has positive pi-adic valuation 34-2d. The equation

    H^16(1-H)=w

has a unique solution H=1 modulo pi, since its derivative at H=1 is -1. The point

    P_(d,a)=(x,y)=(z^2*H, z^17*H^8)                    (3.2)

is an actual K_d-point on (3.1), as direct substitution shows. Its trace divisor minus d*infinity defines an element of J(K), regardless of whether its coordinates generate all of K_d. This construction does not rely on a bounded point search or a list of residue solutions.

The Kummer map on a trace divisor is the corresponding norm of x-xi [S1, Lemma 4.3 and Section 6]. The tensor compositum E K_d is a field: the polynomial for pi remains irreducible over E because its Newton slope has denominator d, using gcd(17,d)=1. Put

    q=Delta*pi^2/s^2.

Then q^17=w, and

    x-xi=z^2*(H+q).

The factor z^2 has square norm and can be discarded in E*/E*^2. Thus the required Kummer class is the norm of H+q. This proves membership in W_2 before any computation of a residue or matrix rank.

### 3.1 Integral norm series

Let H(q) be the unique formal solution

    H(q)^16*(1-H(q))=q^17, H(0)=1.

Its coefficients are integers, either by its implicit equation with unit derivative or by the explicit series below. Over a field containing the d-th roots of unity define

    N_d(t)=product_(omega^d=1)(H(omega*q)+omega*q), t=q^d.

Because d is odd, conjugating pi permutes q by all d-th roots, so this is exactly the norm just used. The product is invariant under q->omega*q. Its coefficients are rational algebraic integers and hence integers; thus N_d is in Z[[t]]. In our local field

    t=phi^2*Delta^d*a^(-2)*s^(34-2d),                 (3.3)

of positive valuation. All the series converge, and the finite precision used below has a uniform rigorous tail bound.

For transparency, two separate coefficient formulas are used.

**Python formula.** Put R=q/H. Then R=q(1+R^17) and H+q=(1+R)/(1+R^17). Formal Lagrange inversion gives

    K_n=n*[q^n]log(H(q)+q)
       =sum_(j=0)^floor((n-1)/17) (-1)^(n-1-17j)*binomial(n,j)
        -17*binomial(n-1,(n-17)/17) if 17 divides n,

where the last term is absent otherwise. If N_d(t)=sum c_m t^m, then

    c_0=1, m*c_m=sum_(j=1)^m K_(dj)*c_(m-j).          (3.4)

**TypeScript formula.** Write V=1-H. Its equation is V=q^17*(1-V)^(-16), giving

    V=sum_(m>=1) binomial(17m-2,m-1)/m * q^(17m).

The implementation builds H+q from these coefficients, obtains the logarithmic derivative by polynomial coefficient recurrence, and then takes the norm by retaining the indices divisible by d. It does not use Python's closed formula for K_n.

To determine N_d(t) modulo 8 it suffices to retain m<=floor(50/(34-2d)): all further terms have s-valuation at least 51. Integrality of the norm coefficients ensures there is no denominator loss in this estimate. The proof uses an infinite convergent series with a certified tail, not an assumption that a polynomial truncation is the exact global root.

## 4. Finite certificates, independence, and completeness

Let e_(n,0)=[1+s^n] and e_(n,1)=[1+phi*s^n], in increasing odd n from 19 to 33. Number these sixteen columns 0 through 15. A binary integer is a compact notation for the product of those basis candidates whose bit is one.

The sixteen trace-divisor witnesses have the following exact codes:

| d | a=1 | a=phi |
|---:|---:|---:|
| 1 | 16384 | 49152 |
| 3 | 12288 | 8192 |
| 5 | 2048 | 1024 |
| 7 | 256 | 768 |
| 9 | 192 | 128 |
| 11 | 32 | 16 |
| 13 | 2052 | 2060 |
| 15 | 3 | 2 |

These are not guessed labels. For each row the supplied certificate lists a product Q(s) of factors 1+(b0+b1*phi)s^m, together with the exact coefficients of N_d at (3.3), and verifies

    N_d(t) = Q(s)^2 * product e_(n,j)^(bit) modulo s^35.   (4.1)

Both sides are units. The cutoff in Section 2 turns (4.1) into equality of squareclasses. Python constructs the square corrections through the normal-form algorithm; TypeScript independently constructs the norm series and verifies all the proposed congruences directly. The same corrections and codes are also checked modulo 16, without changing the s^35 criterion.

The sixteen codes have binary rank sixteen. More explicitly, order the rows by d=15,13,...,1: their first nonzero levels are respectively 19,21,...,33, with two independent F_4 coefficients at each first level. The extra level-29 component for d=13 does not spoil the triangular rank argument.

Each witness is in W_2 by Section 3. The high unit classes are independent by Section 2, so there are sixteen independent elements in W_2. The local index formula gives

    dim_F2 J(K)/2J(K)=dim J(K)[2]+8[K:Q_2]=0+16,

and the Kummer map is injective [S1, Lemmas 4.1 and 4.4]. Therefore these witnesses span the entire W_2. Invertibility of the code matrix proves that the simpler sixteen classes (1.1) themselves form a basis. This dimension comparison is the completeness argument missing from a mere search for some local images.

Wolfram verifies all sixteen congruences and the rank using separate polynomial-remainder arithmetic. Its actual residual valuation bounds, in the row order above, are 49,49,45,45,41,41,37,37,41,41,35,35,37,37,36,36. Every bound is at least 35; values are truncated at 51 because calculations are modulo 8.

## 5. Sixteen explicit quotient coordinates

Every norm-kernel class has even s-valuation: E/K is totally ramified of residue degree one, so the norm preserves valuation parity. Divide by an even power of s and by a square lift of the residue to enter the principal-unit normal form.

For n odd, n!=17, multiplication of conjugates gives

    N_(E/K)(1+b*s^n)=1+b^17*(2/phi)^n.

For n>=3 this is a square in K by the strong Hensel criterion, since its difference from 1 has 2-adic valuation at least three. This includes every high generator in (1.1).

If the sixteen low coordinates n=1,3,...,15 vanish, the only possible non-high coordinates left in (1.2) are the two at n=17 and the top coordinate n=34. Their representatives are already scalar elements of K:

    g1=1+s^17=2phi-1,
    g2=1+phi*s^17=3,
    g3=1+s^34=1+(2/phi)^2.

Their norms from E to K are their seventeenth powers, the same squareclasses. These three classes are independent in K*/K*^2. The check is small and exact: modulo 8, O_K has 48 units and their squares form a subgroup of size six; the eight products of g1,g2,g3 occupy eight distinct square cosets. Squarehood of a unit congruent to a square modulo 8 lifts by Hensel. Hence those three norms form the full three-dimensional unit squareclass group of K.

A class of H_2 with no low coordinates must therefore have zero coordinates at these last three positions as well. It is exactly in the span (1.1). Conversely all of (1.1) is in H_2 and has no low coordinates. This proves Theorem 2. The resulting quotient has dimension sixteen and the sixteen-coordinate map is surjective by rank-nullity.

The normalization is by squares, so its class and these coordinates do not depend on the allowed preliminary square normalization. The actual full restriction matrix still requires localization of a complete global basis, which has not been supplied.

## 6. The former prime-5 survivor is excluded

Let pi0=2phi-1=1+s^17. Then

    alpha=(s+1)/pi0=1/h(s),
    N_(F/k)(alpha)=pi0^(-16),

a square. Its only odd prime-ideal valuation is at the degree-sixteen prime above 5, part of U78's permitted set S_F. Thus alpha is a nonzero class of V; the odd valuation also proves that it is not a global square.

At the degree-one 5-adic factor, h(s) reduces at s=-1 to h(-1)=17, a nonsquare residue modulo 5. At the degree-sixteen factor alpha has odd valuation. Together with the norm condition this gives the bits (0,1,1,1), the nonzero class in U78's local image W_5. This recovers the earlier passing test, rather than silently changing it.

At 2, however, alpha=1+s modulo s^2. Its first nonzero principal-unit level is the odd level one. It cannot be in W_2, whose classes have high representatives and no low coordinates. More fully, inverse and direct factors have the same squareclass, so

    [alpha]=[1+s]*[1+s^17].

Its code in (1.2) is 65537, and its lower sixteen-coordinate code is 1. Thus alpha is excluded from Sel_2(J/k).

This confirms a nonzero restriction on the global candidate space. It does not show that all remaining restrictions on that space are independent or that the whole kernel is zero. No new positive weighted solution family is ruled out just by rejecting this one squareclass.

## 7. Audit, reproducibility, and remaining work

The theorem is local and does not assume the uncomputed class-group 2-rank, global units, a numerical regulator, GRH, BSD, or a boundary-curve identification. Its weighted relevance is via U77/U78; those wider implications retain their self-reviewed status. U41 remains invalidated, and the unrelated coefficient-two branch is not used.

The main potential failure points were checked explicitly: the extension degrees and norm compatibility, the sign and factor 4 in xi, the fact that local Hensel points (not just residues) give divisor classes, the trace over odd extensions even when their degrees exceed the genus, integrality and convergence of the norm series, the s^35 rather than s^34 square cutoff, the special trace bit at depth 34, and the indispensable global/local norm-kernel hypotheses. The sixteen-dimensional local index is used only after constructing and checking sixteen independent images.

`code/U79_dyadic_image.py` implements the closed coefficient formula and complete principal-unit normalization. `code/U79_dyadic_image.ts` builds the implicit series by a different recurrence and checks proposed square factors directly. They agree on their entire returned mathematical output, including every coefficient vector and correction. Their higher-precision checks retain the same classes. A preliminary Wolfram expression returned a syntax error and no arithmetic result; it is rejected as evidence. The corrected actual evaluation returned the congruences and rank stated above.

`research/computations/U79/reproduce.py` runs both exact checkers, strict TypeScript compilation with unchecked-index and unused-variable checks, Python compilation/tabnanny, and full-output comparison. Bun and a standalone linter are not installed in this runtime; neither is reported as executed. The script is offline. No external calculator retry, paid job, publication, expert contact, or other-project write occurred in this continuation.

**Remaining global obligations:** determine d=dim Cl(O_F)[2], obtain and certify a complete basis for V (including any ideal-class contribution), and evaluate the now-explicit local tests on that basis. A certified rank-zero argument is still absent. This checkpoint resolves one genuine local bottleneck, not the weighted equation or the original Beal conjecture.

## Sources

[S1] Michael Stoll, *Implementing 2-descent for Jacobians of hyperelliptic curves*, Acta Arithmetica 98 (2001), 245–277, DOI 10.4064/aa98-3-4. Primary publisher PDF: https://www.impan.pl/shop/en/publication/transaction/download/product/83397 . Lemmas 4.1, 4.3 and 4.4, printed pp.250–251, and the norm/trace compatibility in Section 6, printed pp.269–270. The original parsed text and page images at PDF indices 5,6,24,25 were inspected. These give the general Kummer map, local dimension formula and compatibility, not the particular basis (1.1), which is constructed and proved here.

[S2] U78, `research/checkpoints/U78_explicit_descent_field_and_two_prime_criterion.md`, pinned commit `e5457c3a63843b1e664a4ee7dca83b334bc2c22b`. Used for continuity, the global candidate space and its prime-5 description. The attached archive was hash-verified and its entire Python output replayed. These are project sources, not independent expert certification.

The local ring, squareclass normalization, Hensel witnesses, norm coefficients and candidate exclusion are derived above. No novelty, independent certification, publication, prize eligibility or full-conjecture resolution is asserted.
