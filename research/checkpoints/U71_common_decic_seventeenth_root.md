# U71: a common global seventeenth root in the degree-ten field

**Status: complete written proof of a necessary-condition theorem, with same-model review and distinct exact arithmetic checks. The weighted equation and the full Beal conjecture remain unresolved. Independent expert and proof-assistant verification are outstanding.**

Research date: 2026-09-15. Remote head inspected: `517ecd362bc1a735eb3059501c6b4b3c189752a9` (U69). The attached U70 manuscript and evidence archive were read and restored additively before this work; conflicting content was retained separately. U70 was still local at the start of this run. No other mathematical project was accessed or modified.

## 1. Result and scope

Let

    (W) X^10 + 256Y^10 = Z^17,
        X,Y,Z positive integers, gcd(X,Y)=1.

Write rho for the positive real fifth root of 2 and set

    L=Q(rho,i),  t=i*rho,  t^10=-4,
    tau=X+i*rho^4*Y=X+(t^9/2)Y.

**Theorem.** Every solution of (W) has a unique algebraic integer theta in L with

    theta^17=tau,   Norm_(L/Q)(theta)=Z,              (1.1)
    17^2 | Y.                                        (1.2)

In particular, the two previously studied roots can be obtained from **one common global element**:

    beta = Norm_(L/Q(rho))(theta),
    gamma = Norm_(L/Q(i))(theta),

and satisfy, without unit factors,

    beta^17=X^2+2*rho^3*Y^2,
    gamma^17=X^5+16iY^5.                              (1.3)

Moreover beta is in Z[rho] and gamma is in Z[i].

This proof reconstructs the needed Gaussian step directly from W. It does **not** invoke the earlier quintic unit-elimination theorem Q65, the coefficient-two argument U61/U62, U67's Kummer conditions, the U68–U70 height bounds, the boundary congruence, the invalidated U41, or a modular-form database. Thus it also provides a separate derivation of the pure quintic equation used upstream.

It does not prove that theta cannot exist, that W has no positive primitive solutions, or that Beal's conjecture is true. A local common root still exists in each of U70's remaining prime classes. Section 7 verifies this limitation and also shows that (1.2) cannot simply be strengthened to 17^3|Y by the same local argument.

## 2. The field and a finite class-number certificate

### 2.1 Degree, signature, and an integral lattice

Q(rho) has degree five by Eisenstein at 2 and is contained in R under the specified embedding. Thus i is not in it and [L:Q]=10. The identities

    i=t^5/2,   rho=-t^6/2

show L=Q(t), with minimal polynomial f(T)=T^10+4. It has no real embeddings, so its signature is (0,5).

Consider the ten elements

    1,t,t^2,t^3,t^4,t^5/2,t^6/2,t^7/2,
    u=t^3/2+t^8/4,  v=t^4/2+t^9/4.                 (2.1)

They are integral. For the middle three, use i,-rho,-i*rho^2. For the last two, the exact identities are

    u^10+2u^5+2=0,
    v^10+4v^5+8=0.

Equivalently u=(1-i)rho^3/2 has u^5=-1+i, and v=(1+i)rho^4/2 has v^5=-2-2i.

Their coordinate determinant in the t power basis is 1/128. The lattice Lambda they span has discriminant

    disc(Lambda)=disc(f)/128^2=-160000000000.        (2.2)

All these are exact polynomial/determinant identities. Closure under multiplication is also checked, but the class-number argument needs only Lambda contained in the full ring of integers O_L. The change-of-lattice discriminant formula implies

    |disc(L)| <= 160000000000.

We do not need to assume that a software-reported basis is maximal to use this upper bound. Likewise, the index of Z[t] in O_L has prime factors only 2 and 5, because disc(f) has no other prime factor. At every other rational prime the polynomial f therefore describes the full residue algebra.

### 2.2 Why checking norms below 520 is sufficient

Minkowski's ideal-class bound [S1, Theorem 4.3] gives an integral representative of every ideal class with norm at most

    (10!/10^10)*(4/pi)^5*sqrt(|disc(L)|)
      < (10!/10^10)*(40/31)^5*400000
      = 14863564800/28629151 < 520.                 (2.3)

Here pi>31/10 is an elementary strict lower bound; no decimal rounding decides the threshold.

It is enough to prove every prime ideal of norm below 520 principal. Indeed every prime-ideal factor of an integral ideal of norm below 520 also has norm below 520.

### 2.3 The unramified primes: 89 explicit ideal certificates

`references/U71/certificate.json` contains one row `[p,g,n]` for each of the 89 prime ideals of norm below 520 at rational primes p other than 2 and 5. In a row:

- g is the coefficient vector, in increasing degree order, of a monic irreducible factor of T^10+4 over F_p;
- n is a length-ten integer vector defining a=(sum n_j t^j)/4;
- the exact tests certify that a is integral, g divides its numerator modulo p, and Norm_(L/Q)(a)=p^deg(g).

Consequently the prime ideal defined by g divides (a), and the two ideals have equal norm. They are equal, so that prime is principal. This also treats non-linear factors; checking only rational primes that have degree-one factors would be insufficient.

The exceptional non-linear entries in this norm range are:

    p=3: degrees 2,4,4 (norms 9,81,81);
    p=7: degree 2 (norm 49);
    p=19: five factors of degree 2 (norm 361 each).

The completely split prime 241 contributes ten distinct degree-one primes, all retained. The remaining entries in the list have degree one.

Completeness is checked independently in two ways. Python factors f at every rational prime below 520 and retains every factor with p^degree<520. TypeScript does not call a polynomial factorizer: for every such prime and every d with p^d<520, it computes

    gcd(f(T),T^(p^d)-T) over F_p

and verifies that it is exactly the product of the supplied factors whose degrees divide d. These identities certify that no eligible factor is omitted or duplicated. Python separately checks each supplied factor irreducible. Every generator norm is recomputed by a symbolic resultant in Python and by an exact, fraction-free multiplication-matrix determinant in TypeScript.

Floating-point enumeration was used only to discover candidates in a small lattice box. It is not used by either verifier, by the completeness argument, or to infer absence of elements. Only the successful candidates, all rechecked exactly, enter the proof.

### 2.4 The three prime ideals above 2 and 5

The equation for u in Section 2.1 is Eisenstein at 2 and has degree ten. Thus u generates L and 2 is totally ramified [S1, Proposition 3.53]. There is exactly one prime above 2, of norm 2, and Norm(u)=2 proves it principal.

At 5, Q_5(rho) has degree five and is totally ramified: (T+2)^5-2 is Eisenstein at 5. The polynomial I^2+1 splits into two distinct roots over Q_5, by lifting its simple roots modulo 5. Hence L has exactly two primes above 5, both of residue degree one. The integral elements rho+i and rho-i have absolute norms 5. Their ideals are distinct, since their difference is 2i, a unit at 5. These are the required two principal primes.

Sections 2.3 and 2.4 certify all **92** prime ideals needed by (2.3). Factoring the small representative of any ideal class now proves

    class number(L)=1.                              (2.4)

This is a finite norm-and-factorization proof of the invariant, not an invocation of the unsuccessful class-number software request recorded in Section 8.

## 3. Four complete unit classes modulo seventeenth powers

Let E=O_L^*. Dirichlet's unit theorem [S1, Theorem 5.1] gives rank(E)=4. There is no seventeenth root of unity other than 1 in L, since Q(zeta_17) has degree 16 whereas [L:Q]=10. The torsion of E therefore has order prime to 17, and

    E/E^17 is a four-dimensional vector space over F_17.

We do not need a fundamental unit system or a regulator. The four integral units below are enough; their displayed norms are all exactly one:

    epsilon1=(-2t^3+2t^5-t^8)/4,
    epsilon2=(-2t^3+2t^5+2t^6-t^8)/4,
    epsilon3=(2t^3-2t^4+2t^5-2t^6+2t^7-t^8+t^9)/4,
    epsilon4=(2t^3-2t^5+2t^6-t^8)/4.                (3.1)

Their integrality follows by writing them in (2.1). A norm-one integral element is a unit.

Because 17 does not divide the power-basis index, reduction of O_L modulo 289 is identified with

    A=(Z/289Z)[t]/(t^10+4).

Modulo 17, the exact identity t^(17^4)=t and the absence of repeated roots of f imply z^(17^4)=z for every element of the residue algebra. In particular, every unit z satisfies z^(17^4-1)=1 modulo 17.

Put Q=17^4. For a local unit eta define the coefficient vector

    ell(eta)=(eta^(Q-1)-1)/17 modulo 17.             (3.2)

Division means taking the integral coefficients of a representative divisible by 17; the resulting residue vector is well-defined. This is a homomorphism to the additive residue algebra. It annihilates seventeenth powers, since (1+17a)^17=1 modulo 289.

In the basis 1,t,...,t^9 the exact unit logarithms are

    ell(epsilon1)=(0,10,2,2,3,0,5,14,6,2),
    ell(epsilon2)=(0,14,2,13,11,0,11,3,12,13),
    ell(epsilon3)=(0,10,15,2,14,0,12,14,11,2),
    ell(epsilon4)=(0,3,2,4,11,0,11,14,12,4).         (3.3)

Adjoin to these four columns the columns for 1 and t^9. The minor on coefficient rows 0,1,2,4,7,9 has integer determinant

    -28765 = 16 modulo 17,                           (3.4)

which is nonzero. Thus all six columns are independent. In particular, the four unit classes (3.1) are independent in E/E^17 and hence form a complete basis. Also their logarithmic span intersects the span of 1,t^9 only in zero.

This establishes exactly the finite quotient needed; it is not an assumption that the four units generate E itself. It is also not an appeal to a general conjecture about p-adic regulators.

## 4. The Gaussian step needed to ensure 17 divides Y

We reconstruct this input rather than inheriting a historical success label. If X were even, Y would be odd by coprimality and the left side of W would have 2-adic valuation exactly 8, impossible for Z^17. Thus X and Z are odd.

In Z[i], the factors X^5+16iY^5 and X^5-16iY^5 are coprime. A common Gaussian prime must divide both 2X^5 and 32iY^5. Odd such primes contradict gcd(X,Y)=1; the prime above 2 cannot divide a Gaussian integer whose real coordinate is odd and imaginary coordinate even. Gaussian unique factorization gives

    X^5+16iY^5=(a+ib)^17,
    gcd(a,b)=1, a odd, b even.                       (4.1)

Every Gaussian unit is its own seventeenth power, so it is absorbed without adding a unit class. Both a and b are nonzero by X,Y>0.

Write aG=X^5 and bH=16Y^5, where

    G=sum_(j=0)^8 (-1)^j binomial(17,2j)a^(16-2j)b^(2j),
    H=sum_(j=0)^8 (-1)^j binomial(17,2j+1)a^(16-2j)b^(2j).

One has gcd(a,G)|17 and gcd(b,H)|17 by reduction modulo a and b. The two cofactors are odd. Also G=a^16 and H=b^16 modulo 17. If 17|a then v_17(G)=1; if 17|b then v_17(H)=1, by examining the first nonzero term in the corresponding expansion. Both cannot occur because gcd(a,b)=1.

Unique factorization of rational integers therefore gives exactly these cases, allowing signed integers A,B,C,D:

| Case | a | b | G | H |
|---|---|---|---|---|
| I | A^5 | 16B^5 | C^5 | D^5 |
| II | 17^4 A^5 | 16B^5 | 17C^5 | D^5 |
| III | A^5 | 16*17^4 B^5 | C^5 | 17D^5 |

The factor 16 is fixed by v_2(b)=4+5v_2(Y). No sign or exceptional prime is dropped.

Both new verifiers enumerate all 120 nonzero pairs (A,B) modulo 11, separately for each case, against the complete fifth-power image {0,1,-1}. The numbers of surviving pairs are exactly

    I: 0;  II: 0;  III: 10,

and in III the survivors have B=0 and A nonzero modulo 11. There is no projective normalization or omitted axis in this calculation.

Consequently a weighted solution must be in III. Its identity bH=16Y^5 gives Y=17BD. In particular,

    17|Y, 17 does not divide X or Z.                 (4.2)

Only (4.2), not the larger list of forcing primes, is used below.

Also 5 does not divide Z. If both X and Y are units modulo 5, their tenth powers modulo 25 are ±1, so X^10+256Y^10 is one of 7,5,-5,-7 modulo 25. If divisible by 5 its valuation is exactly one, not a multiple of 17. If just one base is divisible by 5, the sum is a 5-adic unit.

## 5. The ideal of tau is a seventeenth power

The exact identities are

    Norm_(L/Q)(tau)=X^10+256Y^10=Z^17,
    Norm_(L/Q(rho))(tau)=X^2+2rho^3Y^2,
    Norm_(L/Q(i))(tau)=X^5+16iY^5.                  (5.1)

They follow by multiplying conjugates; the verifiers and Wolfram check them independently by resultants or polynomial identities.

Fix a rational prime q dividing Z. It is not 2 or 5 by Section 4, and X,Y are units modulo q by primitivity. If a prime ideal P above q divides tau, its residue field satisfies

    X+(t^9/2)Y=0,  t^10=-4,
    hence t=2Y/X.                                   (5.2)

Thus t is a specified element of F_q. Because q does not divide the power-basis index, there is exactly one possible prime ideal P dividing tau above q, and its residue degree is one. It follows from the norm in (5.1) that

    ord_P(tau)=17*v_q(Z).

No prime over a rational prime outside Z divides tau. Unique factorization of ideals therefore gives

    (tau)=a^17,  Norm(a)=Z,

for an integral ideal a. By (2.4), a=(delta) with delta integral, and hence

    tau=epsilon*delta^17, epsilon in E.              (5.3)

All norms of nonzero elements of L are positive, since the embeddings pair by complex conjugation. A unit has absolute norm one, so Norm(delta)=Z. This argument neither assumes element unique factorization before proving the class number nor confuses polynomial discriminants with field ramification.

## 6. Eliminating the remaining units and proving the common-root theorem

Use (3.1) as a complete basis modulo seventeenth powers to write (5.3), after absorbing a unit into delta, as

    tau=epsilon1^c1*epsilon2^c2*epsilon3^c3*epsilon4^c4*delta^17,
    0<=c1,c2,c3,c4<=16.                              (6.1)

By (4.2), tau is a unit modulo 17 and

    tau=X*(1+(Y/(2X))*t^9).

Since 17|Y, expand to precision 289. With Q=17^4, Q-1=-1 modulo 17, so

    ell(tau)=ell(X)*1 - [Y/(34X)]*t^9 modulo 17.    (6.2)

Here Y/(34X) means (Y/17)/(2X) modulo 17; there is no division by 17 of a nonintegral quantity. The scalar ell(X) is defined by (3.2); no Teichmuller assumption about X is made in advance.

On the other hand, ell(delta^17)=0, so (6.1) gives

    ell(tau)=sum cj*ell(epsilonj).

The six-column independence (3.4) forces every cj=0, ell(X)=0, and (Y/17)/(2X)=0 modulo 17. This proves simultaneously

    tau=theta^17 for an integral theta in L,
    289|Y.

A second seventeenth root in L would differ from theta by an element of order 17, excluded in Section 3. The norm is Z by (5.1) and positivity of norms. This proves (1.1)–(1.2).

Taking the two relative norms of theta proves (1.3) with no remaining unit factors. These norm roots are unique in their subfields, since neither subfield contains nontrivial seventeenth roots of unity. They are therefore the same roots obtained by the corresponding separate descents, not independently selected local roots.

For completeness, O_(Q(rho))=Z[rho]: only 2 and 5 could divide the index, by disc(T^5-2)=50000. At 2, rho is the uniformizer of an Eisenstein degree-five extension; at 5, rho-2 is such a uniformizer. In either totally ramified completion, successive expansion in the uniformizer with scalar residue representatives shows that its complete Z_p-algebra is the integer ring. Neither prime divides the index. Hence beta is indeed in Z[rho]. The Gaussian norm is in Z[i], the Gaussian integer ring.

## 7. Executed follow-up and the surviving global gap

The common root is an additional global conclusion, but it does not make the local systems inconsistent.

At q=1019 and q=2381, representatives of U70's two remaining prime classes, the new Python verifier constructs nonscalar seventeenth roots of unity in

    F_q[t]/(t^10+4),

then scales them to have norm one. The scaling is legitimate because 10*12=1 modulo 17. Set X=1 and Y=q. In each case, tau is 1 modulo q and the derivative 17*theta^16 is a unit. The root lifts at every q-adic precision. Its norm starts at one and is the unique scalar seventeenth root in that residue disk of 1+256Y^10. Thus both relative norm roots come from the same lifted theta, not just from compatible independent choices.

The exact finite examples are checked through q^6. Their complete vectors and norm residues are in `python_output.json`. These examples certify local compatibility only; the all-precision statement follows from the invertible derivative, not from six digits of data.

At 17, take X=1 and Y=17^2. Then tau=1+17^2*t^9/2. There is a principal-unit seventeenth root in the unramified 17-adic algebra. One can see this directly: put theta=1+17h, divide the equation by 17^2, and observe that the resulting equation for h has derivative one modulo 17. Both Python and TypeScript construct the root through 17^9 and return exactly the same coefficients. This shows why the new divisibility 289|Y is not an infinite descent to Y=0; the local case v_17(Y)=2 still survives.

The unresolved global task is to exclude a single **integral** theta satisfying the sparse equation (1.1), with rational positive X,Y and the primitive/norm conditions. Independent p-adic roots do not produce that element. Conversely, a lower bound on its size is not an upper bound. No height bound, rational-point classification, new complete Beal exponent family, or full solution is claimed here.

## 8. Verification, failures, and source scope

The arithmetic certificate is deliberately small: ten lattice basis vectors, 89 unramified ideal rows, two ramified norm generators (the second also used with its conjugate), four units, and one six-by-six minor. No numerical regulator, conjectural class-group computation, or unproved boundary hypothesis is used.

Python checks norms by resultants and completeness by polynomial factorization. TypeScript uses bigint fraction-free determinants and prime-field Frobenius gcd identities for completeness. Its small-prime polynomial operations use exact integers bounded strictly below 2^53, reducing after each operation; there is no approximate polynomial arithmetic. Its master norm identity is also checked on an 11-by-11 grid with an explicit degree-at-most-ten bound in each variable. The grid is a polynomial identity certificate, not a height search for integer solutions.

Wolfram separately checks the integral-lattice discriminant, the norm identities of 48 generator representatives and all four units, their logarithm vectors, the determinant -28765, the Frobenius identity, and the common norm formulas. The full 89-row coverage is independently checked by Python and TypeScript. These are separate arithmetic implementations, not independent expert review of the whole mathematical argument.

The initial Wolfram class-number request returned unevaluated with a message that the invariant was unavailable. Its fundamental-unit output also emitted a precision warning. Neither was used to prove a class number or a unit basis. Attempts to retrieve a local PARI distribution failed; no PARI run is claimed. The explicit finite certificates replaced these attempted dependencies.

Approximate candidate discovery and its bounded search are preserved separately. The proof uses only subsequent exact checks. SymPy's existing modular-integer ordering deprecation warning is retained in stderr; no package was downgraded. Strict TypeScript checking, both verifiers, Python compilation and tabnanny are run by the reproduction script. A standalone linter and Bun are not available in this environment; neither is reported as executed.

The same-model audit checked the missing higher-degree small prime ideals, all ten primes over 241, both primes over 5, the nonmaximal-lattice discriminant bound, the full unit quotient rather than a guessed fundamental system, the scalar term in (6.2), legitimate inverses, signs, zero residue coordinates, and the distinction between a common global root and local norm compatibility. Independent mathematical or proof-assistant verification remains outstanding.

### Sources

[S1] J.S. Milne, *Algebraic Number Theory*, version 3.08, 19 July 2020. Original text and page images inspected: Proposition 3.53 (printed p.66), Theorem 4.3 (p.70), Theorem 5.1 (p.85). Source: https://www.jmilne.org/math/CourseNotes/ANT.pdf . These supply the Eisenstein ramification fact, the ideal-class norm bound, and the unit rank. The specific field, ideal generators, unit quotient, and weighted implications are derived in this checkpoint.

[S2] The preserved U70 manuscript motivated the common-field investigation. Its results are not hypotheses of this theorem. U41 remains invalidated; the earlier independent coefficient-two branch keeps its prior status.

No novelty, expert acceptance, formal verification, publication, prize eligibility, or prize award is asserted.
