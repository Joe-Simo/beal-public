# U67: two boundary-independent Kummer obstructions, with explicit roots modulo Z^17

**Status: written partial theorems, an upstream proof audit, and exact arithmetic corroboration. The weighted equation and the full Beal conjecture remain unresolved.** “Unconditional” below means that the new weighted implications do not assume the boundary congruence (BC), a level-lowering adaptation, database completeness, or a conjectural rank computation. They inherit the written/self-reviewed quintic descent identified precisely below. No independent expert or proof-assistant certification, novelty, publication, or prize claim is made.

Research date: 2026-09-15. Remote input inspected: `a15e419765463f68a641ed71fd549aafae2cc95d` in private `Joe-Simo/beal`.

## 0. Continuity: two different checkpoints numbered U65

The preceding local U66 used `U65_last_orbit_and_CM_boundary.md` from the attached evidence archive. During this continuation the remote repository had advanced along another route to `U65_weighted_quintic_unit_elimination.md`, at the revision above. These are different manuscripts, not alternate filenames for the same proof. The old archive was restored additively before new work, and neither U65 is silently replaced. The source mapping is in `references/U67/sources.json`.

The remote quintic U65 supplies the following written necessary condition for a primitive positive solution of

    (W)  X^10 + 256Y^10 = Z^17,   gcd(X,Y)=1:

    (Q)  X^2 + 2*rho^3*Y^2 = beta^17,
         rho^5=2, beta in Z[rho], Norm(beta)=Z.

The associated Gaussian equation, which also follows directly from (W), is

    (G)  X^5 + 16*i*Y^5 = (r0+i*s0)^17.

Its Gaussian unit is absorbed, since each Gaussian unit is its own seventeenth power. The remote argument removes all quintic unit twists; that removal is essential to this continuation. Section 7 records what was actually rechecked rather than treating an earlier success label as certification.

U41 remains invalidated. U61/U62 concern the coefficient-two equation and are not used. U66's hypothesis (BC) remains unproved for all weighted solutions; none of Sections 1–5 below invokes it.

## 1. Main partial theorem

Let X,Y,Z be positive integers satisfying (W), and suppose the pure element equation (Q) holds. Put

    N=Z^17,  A=Z/NZ,  phi=(1+sqrt(5))/2,  c=5/32.

Then there are units d in A and w in A[phi]=A[T]/(T^2-T-1) such that

    d^17=c,                  w^17=phi.                  (1.1)

The fraction c is interpreted using the inverse of 32 modulo N. Thus the two statements hold simultaneously modulo the entire Z^17, not merely modulo one selected prime. The proof gives the roots explicitly in terms of beta and the Gaussian root.

**Weighted corollary.** Applying the remote quintic U65 implication (W) => (Q), every primitive positive weighted solution satisfies (1.1). In particular, at every prime q dividing Z, the rational constant 5/32 and the quadratic unit phi pass their respective seventeenth-power tests. This is an implication about an unbounded family, not an emptiness theorem for that family.

### 1.1 Exceptional primes and legitimate inverses

If X is even, coprimality makes Y odd. The left side of (W) then has 2-adic valuation exactly 8, whereas a seventeenth power has valuation divisible by 17. Therefore X and Z are odd. A prime dividing Z and either X or Y would divide both, so X and Y are units modulo N.

Also 5 does not divide Z. When both X and Y are 5-adic units their tenth powers modulo 25 are in {1,-1}. Since 256=6 modulo 25, the possible sums are 7,5,-5,-7: any sum divisible by 5 has valuation exactly one. If just one of X,Y is divisible by 5, the sum is a unit. Both alternatives exclude 5|Z.

Set U=X^2 and V=2Y^2. Thus 2,5,U,V,X,Y are units of A. Positivity implies Z>1, so the zero ring modulo one is not involved.

## 2. Explicit construction of the rational seventeenth root

Define in A

    a=U^2/(2V^2).

The following rational-function identities, whose denominators are units here, prove that a is a fifth root of 2 modulo N and that the linear component of gamma vanishes:

    32V^10*(a^5-2)=(U^5+8V^5)(U^5-8V^5),
    8V^5*(V*a^3+U)=U*(U^5+8V^5).

Since U^5+8V^5=N=0 in A,

    a^5=2,        U=-V*a^3.                          (2.1)

Factor

    R^5-2=(R-a)h(R),
    h(R)=R^4+aR^3+a^2R^2+a^3R+a^4.

Because h(a)=5a^4 is a unit, the factors are comaximal even when N is composite. Hence the actual ring decomposition is

    A[R]/(R^5-2) = A x A[R]/h.

This is not a projective normalization and does not discard a zero divisor.

Let beta4 denote beta in the second, rank-four algebra, and let

    s4=Norm_(A[R]/h / A)(beta4).

Here norm means the determinant of multiplication on a free module, so it is defined over A without any field assumption. Reducing (Q), using (2.1), and taking that norm gives

    s4^17 = Norm(V*(R^3-a^3)) = 5a^12V^4 = 5U^4 = 5X^8.     (2.2)

The middle identity is exact:

    Res_R(h(R),V*(R^3-a^3))=5a^12V^4.

It also follows by multiplying the four terms a^3V*(zeta^(3j)-1), j=1,...,4. For the equality 5a^12V^4=5U^4, use U=-Va^3, not an illicit cancellation of a solution-dependent quantity. Equation (2.2) proves that s4 is a unit.

To use (G), set

    j=X^5/(16Y^5) in A.

Equation (W) gives j^2=-1. Evaluation i -> j is therefore a ring homomorphism from A[i] to A, including for composite N. With

    tG=r0+j*s0,

it gives

    tG^17=2X^5.                                      (2.3)

Thus tG is a unit. Now the explicit element

    d=X*s4/tG^5

satisfies

    d^17 = X^17*(5X^8)/(2X^5)^5 = 5/32.

Only units were inverted. In particular beta's vanishing linear component was never inverted. This proves the first assertion of (1.1).

## 3. Explicit construction of the quadratic-unit root

Work temporarily in the rank-four algebra

    C=A[zeta]/(1+zeta+zeta^2+zeta^3+zeta^4).

For k=1,2, the substitution rho -> a*zeta^(2k) defines a homomorphism into C. Let bk be the corresponding value of beta. Equations (Q) and (2.1) give

    bk^17=U*(1-zeta^k),  k=1,2.                     (3.1)

The elements 1-zeta^k are units, because their product over k=1,...,4 is 5, a unit. Consequently b1,b2 are units.

In C define

    phi=1+zeta+zeta^(-1).

It satisfies phi^2-phi-1=0. Either conjugate root of that quadratic is allowed by the construction; the two seventeenth-power conditions are equivalent since the conjugate is -phi^(-1). Exact cyclotomic reduction yields

    (-zeta)^17*(1+zeta)=phi.

Therefore

    v=-zeta*b2/b1,        v^17=phi.                  (3.2)

To obtain a root in the quadratic algebra rather than merely in C, write D=A[phi]. The algebra C is free of rank two over D: one presentation adjoins zeta with

    zeta^2-(phi-1)zeta+1=0.

This presentation gives the inverse of the rank-four cyclotomic presentation, since phi=1+zeta+zeta^(-1). Its involution is zeta -> zeta^(-1). If n2=Norm_(C/D)(v), then n2 is a unit and (3.2) gives

    n2^17=phi^2.

It follows that

    w=n2^9/phi,          w^17=phi^(18-17)=phi.

This proves the second assertion of (1.1), with no choice of a residue-field embedding required.

### 3.1 A consistency check at the residual prime

The rational obstruction independently excludes 17|Z. Indeed, modulo 289 the constant c is 244, and

    244^16=256 != 1  (mod289).

If c=d^17 with d a unit modulo 289, Euler's theorem would give c^16=d^272=1, a contradiction. If 17|Z, reduction of (1.1) modulo 289 would be available because 289 divides Z^17. Thus 17 does not divide Z.

This is a consistency check rather than an additional branch elimination: the remote U65 modulo-289 axes already imply that 17 divides exactly one of X,Y, hence not Z.

## 4. Completeness of the two tests on the toric residue fiber

The obstruction is not simply two arbitrary necessary tests: in the following precisely stated local setting it is complete.

**Theorem 2.** Let q be a prime outside {2,5,17}, and let X,Y be nonzero elements of F_q with

    X^10+256Y^10=0.

Assume X^5+16iY^5 is a seventeenth power in F_q[i]/(i^2+1). Then gamma=X^2+2rho^3Y^2 is a seventeenth power in F_q[rho]/(rho^5-2) if and only if

    5/32 is a seventeenth power in F_q^*,
    phi is a seventeenth power in (F_q[phi])^*.      (4.1)

The quadratic algebra in (4.1) may be split or a field. Every component is included.

**Proof.** Necessity is the argument of Sections 2–3 with A=F_q; it does not use a global solution.

For sufficiency, the toric equation gives a fifth root a=U^2/(2V^2) of 2 and a square root j of -1 in F_q. The two Gaussian evaluations are 0 and 2X^5. Thus the Gaussian hypothesis says precisely that 2X^5 is a seventeenth power. If c is a seventeenth power, so is

    5U^4=5X^8=c*(2X^5)^5/X^17.                    (4.2)

Let L=F_q(zeta_5). The nonzero conjugates of gamma are U*(1-zeta^k), k=1,...,4; the remaining conjugate is zero. Relative to k=1, their ratios are

    1,  -zeta^3*phi,  zeta*phi,  -zeta^4.

These identities follow by factoring 1-zeta^k. The subgroup generated by -1 and zeta has order dividing 10, on which raising to the seventeenth power is bijective. The phi condition in (4.1) therefore makes all four conjugates equal as classes in L^*/(L^*)^17. Their product is 5U^4, a seventeenth power by (4.2). The quotient has exponent 17, and multiplication by 4 is invertible on it. Their common class is consequently zero.

Finally each nonzero orbit of roots a*zeta^(2k) has length ord_5(q), because a is in F_q and k!=0. Its residue field is L, not a smaller field in which a root might fail to descend. All nonzero components therefore have seventeenth roots in their actual component fields. The zero component has root zero. The product algebra has a root as required. QED.

### 4.1 Arbitrarily high q-adic precision does not add a new obstruction here

Suppose X,Y are q-adic units and Z is a nonzero multiple of q satisfying (W) in Z_q. Suppose the Gaussian power identity holds and (4.1) holds in the residue field. Then the quintic power identity has a solution beta in Z_q[rho].

Here is the lifting argument, including the nonunit component. Lift the distinguished residue root a of R^5-2 to a root alpha in Z_q; its derivative 5a^4 is a unit. The linear factor and its degree-four complement remain comaximal. The residue root in the complementary algebra is a unit; its seventeenth power lifts uniquely, since multiplication by 17*beta4^16 is an invertible linear operator. Explicitly, at each stage the error is corrected by that inverse in the next coefficient digit. This is the usual simple-root lifting proved by the first-order binomial expansion, not a finite-precision assertion.

Let s4 be the norm of the lifted complementary root, so s4 is a q-adic unit. The exact norm of gamma is Z^17. Its linear component must therefore equal (Z/s4)^17. Combining the linear root Z/s4 with the lifted complementary root gives beta in the full algebra. This disposes of the one component where the derivative of the seventeenth-power map is not a unit.

Thus increasing q-adic precision at a passing prime does not invalidate this pair of descent equations by itself. A global condition on the common integral beta, or other genuinely additional information, is still needed.

## 5. A fixed degree-9248 splitting field, independent of the boundary torsion field

Let

    F=Q(sqrt(5)),  B=F(zeta_17),
    T=B(phi^(1/17), (5/32)^(1/17)).                (5.1)

**Theorem 3.** The two radical classes are independent in B^*/(B^*)^17. Consequently [T:B]=289 and [T:Q]=9248. The extension T/Q is Galois and is unramified outside {2,5,17}.

**Proof of independence.** The quadratic field F has discriminant 5, while Q(zeta_17) is unramified outside 17. They are disjoint, so [B:F]=16 and [B:Q]=32. Also B is contained in Q(zeta_85), so 2 is unramified in B.

Suppose phi^a*c^b=h^17 in B with 0<=a,b<17. At a prime over 2, the normalized valuation of c is -5 and phi is a unit. The equality forces 17 to divide 5b, hence b=0. Now h is a unit. Taking the norm from B to F gives

    Norm(h)^17=phi^(16a).

The units of O_F are +/-phi^n. One elementary way to check the fundamental generator is to suppose 1<eta<phi is a positive real unit and write eta=(u+v*sqrt(5))/2. Its conjugate is +/-eta^(-1); then v=(eta-eta')/sqrt(5) lies strictly between zero and one, impossible for an integer. Together with the rank-one unit theorem this proves the asserted generation. Comparing unit exponents in the norm identity yields 17|16a, so a=0.

Since B contains all seventeenth roots of unity, adjoining a nontrivial seventeenth root gives a cyclic extension of degree 17 [S1]. If the second radical acquired a root in the first extension, that root would be an eigenvector of its cyclic generator; in the basis 1,c^(1/17),...,c^(16/17), every eigenspace is one-dimensional. This would make phi equal to c^k times a seventeenth power in B, contrary to independence. Therefore the two successive degrees are 17, proving the degree claim. The integer products printed by the checkers are arithmetic confirmations only; this argument, not a guessed polynomial degree, proves the field degree.

Conjugation of phi gives -phi^(-1), whose seventeenth roots already lie in T whenever those of phi do. The constant c is rational and all root-of-unity factors are present. Thus every conjugate of either radical is in T, proving normality; characteristic zero supplies separability. Finally phi is a unit and one may replace c^(1/17) by its double, whose seventeenth power is 5*2^12. The discriminants of the two radical polynomials, together with that of B, have support only at 2,5,17. This proves the ramification assertion. QED.

### 5.1 Prime-divisor interpretation

For q outside {2,5,17} which splits completely in B, the two tests (4.1) are equivalent to complete splitting in T. Indeed q=1 modulo 17, all seventeenth roots of unity are in F_q, and both embeddings of phi are present. A single root of each radical polynomial then gives all its roots. Conversely complete splitting supplies such roots. The conjugate phi'=-phi^(-1) passes exactly when phi passes, so there is no untested second prime of F.

Every prime divisor q of Z is 1 modulo 4 by (G), regardless of (BC). Consequently, for divisors that also split in B, the relevant rational residue classes modulo 340 are 1 and 69. In particular, a divisor q=1 modulo 340 must split completely in the single fixed field T of degree 9248. This does not assert that all divisors of Z split in B, nor that these splitting conditions force Z=1.

### 5.2 The new extension is not hidden inside the old CM torsion field

Write M0=Q(J0[17]) for J0=Jac(y^2=64-x^5). The following fact about M0 does not assume (BC). The order-five automorphism tau:x->zeta_5*x satisfies Phi_5(tau)=0 on J0, since its quotient has genus zero. The polynomial Phi_5 is irreducible modulo 17: its nonzero exponent orbit under multiplication by 17 modulo 5 is 1,2,4,3. Hence J0[17] is a one-dimensional vector space over F_(17^4).

Conjugation by rational Galois acts on this field through a subgroup of its four automorphisms. Choosing a field basis makes the whole action semilinear, so its image is contained in

    F_(17^4)^* semidirect Gal(F_(17^4)/F_17).

Therefore

    [M0:Q] divides 4*(17^4-1)=334080,

which is prime to 17. No assertion that the image fills this group is made. This is the direct argument recorded in the archived U66, extended from the real-quadratic Galois subgroup to all of G_Q.

Now [B*M0:B] is prime to 17, while [T:B]=17^2. Their intersection has degree dividing both, so

    T intersect (B*M0) = B.                       (5.2)

As both extensions are Galois, they are linearly disjoint over B. This proves that the two Kummer directions are not already contained in the boundary's 17-torsion field. It does not establish or refute (BC), identify a modular-form label globally, or turn two compatible splitting requirements into a contradiction.

## 6. Exact witnesses and nonredundancy

The new finite question was whether the two separate constants add different information after the Gaussian toric condition, not whether a bounded search can resolve (W). At the following primes q=1 modulo 340, both phi and c are in F_q. A nonzero unit is a seventeenth power precisely when its (q-1)/17 power is 1.

| q | phi | c=5/32 | c^((q-1)/17) | phi^((q-1)/17) | Gaussian-compatible toric (X,Y) |
|---:|---:|---:|---:|---:|---:|
| 2381 | 1774 | 521 | 1787 | 477 | (726,22) |
| 17681 | 1932 | 6078 | 1 | 1219 | (9456,12) |
| 610301 | 412274 | 438654 | 54536 | 1 | (25040,10) |

Each witness satisfies X^10+256Y^10=0 and makes 2X^5 a seventeenth power modulo q. Thus the Gaussian test has not been bypassed by throwing away scale. The second row passes c but fails phi; the third passes phi but fails c. All three primes are excluded as divisors of Z under the weighted corollary. The exclusion of 2381 no longer needs U66's unproved boundary connection.

These are residue witnesses, not positive-integer solutions of (W). Primality and every displayed value were checked exactly by Python, a distinct bigint TypeScript implementation, and Wolfram.

### Full finite-domain verification of Theorem 2

For the stated split primes, every nonzero Y and every tenth-root ratio X/Y was tested, including all scales. The complete quintic split-component image was compared against the two constants:

| q | Toric pairs | Gaussian-compatible pairs | Also quintic-compatible | Constant tests |
|---:|---:|---:|---:|---|
| 241 | 2400 | 2400 | 2400 | pass |
| 2381 | 23800 | 1400 | 0 | fail |
| 17681 | 176800 | 10400 | 0 | fail |

The code asserts that each test domain and its Gaussian subset is nonempty, and checks equivalence for each pair, not just matching final counts. These finite calculations corroborate the algebraic theorem; they are not its proof for arbitrary q.

### A passing example also compatible with U66's elementary class filter

At q=13 take (X,Y,Z)=(6,1,0) as residues. In F_13[rho]/(rho^5-2),

    (1+6rho+3rho^2+7rho^4)^17 = 10+2rho^3.

In F_13[i],

    (5+i)^17=2+3i=X^5+16iY^5.

Moreover 9^17=3=5/32 modulo 13, and in the quadratic algebra

    (3+5phi)^17=phi.

All four identities were checked independently. Thus these local conditions are consistent; no emptiness claim is justified. The Z=0 here is only a residue class of a potential integer multiple of 13.

## 7. Upstream audit and actual computational evidence

The remote quintic U65 manuscript was read through its final section at the pinned revision, not inferred from the remote README. Its proof checks were inspected as follows:

- The integer ring Z[rho], class number one, and the norm descent treat the primes 2 and 5 separately. The explicit Minkowski argument uses only ideals of norm below 16 and supplies generators of norms 2,3,5,7,13.
- Its two unit classes are shown to form a basis modulo seventeenth powers by the determinant-4 residue-character matrix, rather than assuming a full regulator computation.
- The unit sieve uses the full mod-289 algebra, including zero divisors; the two Gaussian components and every square-root sign are retained.

A fresh unsplit Python implementation of that last certificate reproduced: 18768 square/twice-square pairs, 1104 norm-compatible pairs, 24 unit-compatible pairs distributed as 16 in class (0,0) and 8 in class (0,14), and exactly 16 pairs/544 root witnesses after the Gaussian test, all in class (0,0). The entire 24-row output is retained. Wolfram independently reproduced the two five-coordinate unit logarithms used in this replay. The source's earlier split Python and unsplit TypeScript agreement is an inherited record, not claimed as a newly executed replay of both original programs.

For the new results, `code/U67_kummer.py` uses SymPy resultants and exact finite-field residues. `code/U67_kummer.ts` uses integer quotient-ring arithmetic, a fraction-free multiplication determinant, trial-division primality, and independently generated roots. Its quartic-norm identity is certified by a 13-point integer grid with an explicit degree bound 12 in a, and degree 4 in V; the former also follows by scaling each root R=a*zeta^j. A large-integer evaluation tests bigint behavior. These are polynomial identity checks, not sampled Diophantine bounds.

The complete named residue values, all tenth-root lists, Gaussian witnesses, finite equivalence counts, the passing q=13 identities, and the mod-289 constant check agree between the two new implementations. Wolfram supplies separate resultant/cyclotomic identities and both negative and positive residue witnesses. The exact expressions and returned outputs are stored, not only an assertion that a tool agreed.

`research/computations/U67/reproduce.py` runs the new Python and TypeScript programs, strict TypeScript checking with unused/index checks and `--noEmitOnError`, Python bytecode compilation, and tabnanny. Each command and exit status is recorded. No standalone linter, proof assistant, external expert, independent agent, or new modular-form reconstruction was run.

### Failures and limitations retained

An initial proposed finite domain at 101 and 1361 had no toric pairs. Those empty rows were not credited as exclusions and the exploratory output was retained; nonempty domains and assertions replaced them. An initial TypeScript expression with an unparenthesized negative exponentiation operand failed compilation; it was corrected before a successful strict run, and the failure is recorded.

The first Wolfram named-prime test used Y=1 and correctly returned Gaussian characters different from one. Those were toric-only witnesses, not joint witnesses. The later check used the scale-retaining pairs in the table and returned Gaussian character one for each. Both outputs are preserved. A source-download attempt failed; no inaccessible private raw URL was sent to web, and no downloaded source was claimed. The source was read through the authorized GitHub connector, and a new replay was implemented separately.

A preliminary exploratory search for nonredundancy examples considered 229 primes q=1 modulo 340, q<=2000000, with 2 a fifth power; it found the opposite pass/fail examples above. Its failure to find an example passing both in that exploratory range is not a theorem, a density calculation, or a reason to discard any remaining class. The passing q=13 and q=241 examples show directly why no general emptiness conclusion follows.

## 8. Mathematical status and next obligation

The completed new argument produces explicit seventeenth roots of two constants modulo Z^17, identifies their independent degree-17 extensions, and proves an exact local equivalence on the toric fiber. The weighted implications are boundary-independent but inherit the written/self-reviewed upstream quintic reduction; the geometric and number-field arguments have not been checked by an independent expert or kernel.

No weighted solution was produced or excluded in full. No new original-Beal exponent family is marked solved. The older seven-of-eight modular-candidate count is unchanged, U41 remains invalid, and U61/U62 retain their separate limited status.

The next global question is the simultaneous integrality of the single quintic root beta. Its seventeenth power has zero rho, rho^2, and rho^4 coefficients, while the other coefficients are X^2 and 2Y^2; it must also coexist with (G). Section 4.1 shows why repeating higher precision at an already passing prime cannot replace that global step. A useful advance would be a proved lower-dimensional rational-point reduction or an integral descent using these simultaneous equations, not another finite list of excluded prime factors. The unresolved boundary-representation/lowering track remains separate.

## References

[S1] The Stacks Project, Section 9.24, tag 09I6, and Lemma 9.24.1, tag 09DX, read on 2026-09-15. Only the elementary cyclic radical extension/eigenvector facts are used; the specialized independence and degree arguments are proved in Section 5. The subextension lemma with its additional root-of-unity hypothesis is not needed.

[S2] Project source: `research/checkpoints/U65_weighted_quintic_unit_elimination.md`, revision `a15e419765463f68a641ed71fd549aafae2cc95d`, blob `c3b180d626e6434116cc9aed54a6e585b5e0ac28`. This is self-reviewed research, not an independently certified published theorem. It records its Milne algebraic-number-theory sources and exact finite certificates.

[S3] Archived local `U66_nonsplit_Cartan_toric_obstruction.md`, Section 3, recovered from the actual U66 archive and retained. The semilinear torsion-field argument is restated in Section 5.2 so its field-degree bound does not depend on assuming the boundary congruence.
