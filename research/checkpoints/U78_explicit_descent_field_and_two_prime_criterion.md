# U78: an explicit descent field and a two-prime Selmer criterion

**Status: written, self-reviewed field and descent-reduction theorems, corroborated by exact arithmetic. No numerical rank upper bound, weighted-equation exclusion, or solution of Beal's conjecture is obtained. Independent expert and proof-assistant verification remain outstanding.**

Research date: 2026-09-15. The private remote was read at `11becf1c733016efd853d136e2f1e85dab319b13` (U77). Its attached archive was restored additively: 50 files restored, two identical, no conflicts overwritten, and all manifest hashes verified. The full U77 Python output reproduced unchanged into a new record. This is repeatability, not independent mathematical verification.

## 1. What is established and what remains unknown

Keep U77's fixed curve and Jacobian

    k=Q(phi), phi^2-phi-1=0, phi=(1+sqrt(5))/2,
    C: v^2=phi+2-4(3-phi)u^17, J=Jac(C).             (1.1)

U77's written argument says that a primitive positive solution of `X^10+256Y^10=Z^17` would force an infinite-order class in J(k). Its application still inherits the earlier common-root proof. The present field and descent statements concern the explicitly defined curve (1.1) and do not require a weighted solution as a hypothesis.

**Theorem.** Let

    F=k(s), s^17=2/phi=2phi-2,
    f(T)=T^34+2T^17-4,
    d=dim_F2 Cl(O_F)[2].

Then:

* F is the root field for the odd-degree 2-descent, has signature (2,16), and

      O_F=Z[phi,s],
      basis: s^j, phi*s^j for 0<=j<=16,
      disc(F)=2^32*5^17*17^34,
      [O_F:Z[s]]=2^17.                               (1.2)

* There is a finite global candidate space V of dimension **17+d** and a precisely defined linear map

      Psi: V -> (H_2/W_2) direct_sum F_2,
      dim(H_2/W_2)=16,
      Sel_2(J/k)=ker(Psi).                           (1.3)

  The final F_2 coordinate is an explicit local square test at the prime above 5. The prime above 17 and both real places have zero local norm-kernel space and impose no further condition. Good places outside 2,5,17 are already accounted for by the definition of V.

Consequently, writing r_Psi for the rank of this particular restriction map,

    dim Sel_2(J/k)=17+d-r_Psi,
    rank J(k) <= 17+d-r_Psi.                         (1.4)

**Neither d nor r_Psi has been computed.** In particular, (1.4) is not a numerical rank bound. The 16-dimensional local Kummer image W_2 is defined and its dimension proved, but a basis for it is not supplied. The global candidate basis and the entries of Psi also remain to be computed. “Seventeen conditions” denotes the dimension of the target; it does not assert that their restrictions to V are independent.

A sufficient certificate for the rank-zero route would be

    d=0 and r_Psi=17.                               (1.5)

Together with U77, this would exclude the active weighted equation, not the complete Beal conjecture. U78 proves the reduction to (1.5), **not** either assertion in (1.5). A nonzero Selmer group would not, by itself, prove positive Mordell-Weil rank either.

## 2. Identifying the correct field and proving its integer ring

Put c=2phi-2. The quadratic ring is O_k=Z[phi]. Both 2 and 17 are inert: `T^2-T-1` is irreducible modulo each. At the prime of k above 2, c has valuation one, so `T^17-c` is Eisenstein. Thus [F:k]=17. Also phi=(s^17+2)/2 belongs to Q(s), which proves [F:Q]=34 and proves that f is its minimal polynomial.

The relative discriminant of the basis 1,s,...,s^16 is

    17^17*c^16.

Only the base primes above 2 and 17 can divide its relative index. At 2, s is a uniformizer of a totally ramified extension and generates its local integer ring. For the prime above 17, use the integral shift a=-2phi. Exact reduction in Z[phi] gives

    a^17-c = -129368062-209321986phi,
    (a^17-c)/17 = 11+8phi modulo17,
    Norm_(k/Q)(11+8phi) = 9 modulo17.                (2.1)

All intermediate coefficients of `(T+a)^17-c` are divisible by 17, and its constant term has valuation exactly one. The shifted polynomial is therefore Eisenstein at this prime as well. Its root s-a generates the same local order as s and is a uniformizer, proving local maximality. The Eisenstein/uniformizer statement is used over the completion of k, not over Q_17 with a discarded quadratic coefficient field; see [S1, Proposition 7.55 and Remark 7.56].

There are no remaining possible relative index primes. Hence O_F=O_k[s]. In particular the ramification of k at 5 was already included by working over O_k; it is not a missing exceptional case.

Since Norm(c)=-4 and disc(k)=5, the discriminant tower formula yields

    disc(F)=5^17 * Norm(17^17*c^16)
           =2^32*5^17*17^34.                        (2.2)

Its sign is positive. For each of the two real embeddings of k, the odd-degree polynomial has one real root and eight pairs of nonreal roots. Thus F has signature (2,16), consistent with (2.2).

Replacing phi*s^j by `s^j+s^(17+j)/2` gives basis determinant 2^(-17) relative to the s power basis. It follows that `[O_F:Z[s]]=2^17`. The polynomial discriminant is correspondingly `2^66*5^17*17^34`.

Python verifies the polynomial discriminant and the rational basis determinant. TypeScript independently constructs the 34-by-34 trace Gram matrix by Newton sums and computes its determinant by exact integer elimination. Magma returned the same **order** discriminant and index for `Order([s,phi])`; it did not complete a maximal-order computation. Maximality here comes from the local proof above, not from mislabeling that order output.

### 2.1 The field belongs to the actual curve

Write A=-4(3-phi) and B=phi+2. The change of variables

    x=A*u, y=A^8*v

gives the monic odd-degree model

    y^2=x^17+A^16*B.                                (2.3)

A root of the original right-hand side satisfies `r^17=phi^2/4`. In F take

    r=s^(-2)=(s^32+2s^15)/4.

Conversely s=c*r^8. Thus k(r)=F, and the root in (2.3) is xi=A*r. The exact identity `(3-phi)phi^2=phi+2` verifies its equation. This also proves irreducibility of the monic degree-seventeen polynomial over k. Hence J(k)[2]=0 by the branch-point description of 2-torsion.

The norm to Q of the discriminant of the monic polynomial is

    2^1024*5^272*17^34.                              (2.4)

In particular its integral model, and hence J, has good reduction outside the primes above 2,5,17. The large exponents in (2.4) are polynomial-model data, not the field discriminant (2.2).

## 3. All four primes needed by the global descent

Let S contain the three finite primes of k above 2,5,17, and S_F all primes of F above them. Set pi=2phi-1=s^17+1, a uniformizer of k at 5, and

    h(s)=s^16-s^15+s^14-...-s+1,
    (s+1)h(s)=pi.

There are exactly four primes in S_F:

| Rational prime | Absolute ramification index | Absolute residue degree | Ideal norm | Principal/class information |
|---:|---:|---:|---:|---|
| 2 | 17 | 2 | 4 | P_2=(s) |
| 5 | 2 | 1 | 5 | P_(5,1)=(s+1) |
| 5 | 2 | 16 | 5^16 | P_(5,16)=(h(s)) |
| 17 | 17 | 2 | 289 | (17)=P_17^17 |

The claims at 2 and 17 follow from Section 2. At 5, reduction modulo pi gives phi=3, c=-1, and

    T^17+1=(T+1)*Phi_34(T).

The factor Phi_34 has degree sixteen and is irreducible modulo 5, since the multiplicative order of 5 modulo 17 is sixteen. The relative extension is unramified at 5. This gives the two residue degrees and absolute ramification indices in the table.

The exact signed norms are

    Norm(s)=-4, Norm(s+1)=-5, Norm(h(s))=5^16.

Moreover h(-1)=17 is a unit at 5. Thus s+1 belongs only to the degree-one prime and h(s) only to the degree-sixteen prime; the norms show that each ideal occurs to the first power. At 17 its prime's class has order dividing seventeen, not necessarily one.

The localization map from Cl(O_F) to the S-class group kills the classes of these primes. Three are principal and the fourth has odd order. It therefore leaves the 2-primary class group unchanged; in particular the dimension of its 2-torsion remains d. **This proves no value for d.**

## 4. The complete global squareclass space

Define

    F(S,2)={alpha in F*/F*^2 : ord_P(alpha) is even for P outside S_F}.

The familiar ideals-and-units sequence gives the exact sequence

    0 -> O_(F,S)* / O_(F,S)*^2 -> F(S,2)
      -> Cl(O_(F,S))[2] -> 0.                       (4.1)

For example, the last map takes the ideal square outside S to its ideal class; its kernel is exactly an S-unit times a square. Surjectivity follows by squaring an ideal representative of a 2-torsion class. This is the S-integer version of [S2, Lemma 4.9], with the specialized class-group observation in Section 3 retained.

The signature and four S-primes give S-unit rank `2+16+4-1=21` by [S1, Theorem 5.11]. The only roots of unity in F are ±1, since it has a real embedding. Therefore

    dim F(S,2)=22+d.

The base field k has class number one: its Minkowski ideal-class bound is sqrt(5)/2<2, so every class has an ideal representative of norm one. With unit rank one, three S-primes and ±1, this gives

    dim k(S,2)=5.

Norm sends F(S,2) to k(S,2). It is split surjective: inclusion of a base-field squareclass is a section because its norm is its seventeenth power, the same squareclass. Consequently

    V=ker(N:F(S,2)->k(S,2)), dim V=17+d.             (4.2)

This norm restriction is taken globally. It must not be silently omitted when extending a Q-based descent implementation to a nontrivial base field; compare [S2, end of Section 4].

## 5. Local conditions and one explicit binary test at 5

For a place v of k put

    H_v=ker((F tensor k_v)*/(F tensor k_v)*^2 -> k_v*/k_v*^2),
    W_v=image(J(k_v)/2J(k_v) -> H_v).

For an odd-degree monic hyperelliptic model the Kummer map is the usual `x-xi` map on divisor classes. The branch-root description identifies J[2] with the kernel of the product map from seventeen copies of mu_2 to mu_2, equivariantly. The diagonal section splits this map because seventeen is odd. Kummer theory then identifies H^1(k_v,J[2]) with H_v, and likewise globally. This explains the use over k here, rather than merely quoting a statement formulated over Q. The explicit maps and local index formula are [S2, Lemmas 4.1, 4.3 and 4.4].

For a finite local field with m irreducible branch factors, the dimensions are

    dim J(k_v)/2J(k_v)=m-1+8[k_v:Q_2]  if v divides 2,
    dim J(k_v)/2J(k_v)=m-1              otherwise,
    dim H_v=2 dim W_v.                              (5.1)

Here `[k_v:Q_2]` is used only at 2. The three finite places give:

| Place over | Relative branch degrees | dim H_v | dim W_v | dim H_v/W_v |
|---:|---|---:|---:|---:|
| 2 | 17 | 32 | 16 | 16 |
| 5 | 1,16 | 2 | 1 | 1 |
| 17 | 17 | 0 | 0 | 0 |

At either real embedding the root algebra is R times C^8. Its norm on squareclasses is an isomorphism onto R*/R*^2, so H_v=0. At all good finite places outside S, the local image is precisely the unramified norm-kernel space. In odd residue characteristic this means even valuations at every factor: the Kummer image is unramified by good reduction, and its dimension equals that space. Those conditions were already imposed in (4.2).

Thus only W_2 and W_5 need further work. **The dimension sixteen does not specify W_2 as a subspace of H_2.** Determining it remains an explicit uncompleted task.

### 5.1 Computing W_5 completely

At 5 the algebra is k_5 times its unramified extension K_16 of degree sixteen. Use pi in both factors as uniformizer. A local squareclass is specified by four bits

    (e1,b1,e16,b16),

where e is the valuation modulo two and b is zero for a square residue unit, one for a nonsquare residue unit after removing that valuation. The norm map imposes

    e1=0, b1=b16.                                  (5.2)

Indeed norms multiply valuations by the residue degrees 1 and 16. For units, the finite-field norm preserves the square/nonsquare bit. Thus H_5 has the four classes listed by (5.2).

Let xi0=A*r0 be the degree-one root of the monic polynomial (2.3). The other roots lie in the degree-sixteen factor. The local 2-torsion class T=[(xi0,0)-infinity] has Kummer components

    (f_monic'(xi0), xi0-xi)
      = (17*xi0^16, A*(r0-r)).                      (5.3)

This is the branch-point evaluation formula in [S2, Lemma 4.3]. One has ord_pi(A)=1 and r0,r are units with distinct reductions, so the second component has valuation one. The first component has even valuation and residue-unit squareclass 17, a nonsquare modulo 5. The norm condition gives b16=b1=1. Consequently

    delta(T)=(0,1,1,1) != 0.

Since dim W_5=1, this nonzero class spans the whole image. An explicit test is therefore

    alpha belongs to W_5  iff  b1+e16=0 in F_2.     (5.4)

Equivalently the quadratic character of the normalized unit in the degree-one component equals `(-1)^ord_(P_(5,16))(alpha)`.

This does not require testing points of bounded height. As a check on its scope, the global candidate `alpha=(s+1)/pi=1/h(s)` has norm pi^(-16), hence belongs to V, and has local bits (0,1,1,1). It passes (5.4). We have not determined its image at 2 or concluded that it is a Selmer class. The existence of a local test is not an assertion that it eliminates every global candidate.

## 6. The exact remaining linear map

Choose no uncomputed basis implicitly. Define the map intrinsically by

    Psi(alpha)=(loc_2(alpha) modulo W_2, b1(alpha)+e16(alpha)).

Its target has dimension 16+1=17. By the definition of the 2-Selmer group, the global norm condition, and the complete local analysis above,

    Sel_2(J/k)=ker(Psi).                            (6.1)

This proves (1.3) and its dimension formula. Since the branch polynomial is irreducible over k, J(k)[2]=0, and the injection J(k)/2J(k) -> Sel_2 gives (1.4).

Once complete global generators and a local basis are known, Psi is a binary matrix with seventeen rows and 17+d columns. **That matrix has not been filled or tested here.** To establish (1.5) it would be necessary to certify absence of class-group 2-torsion, certify completeness of the S-unit/squareclass generators, compute W_2, and then obtain a full-rank restriction certificate. Merely finding some units, or assuming a returned subgroup is the full unit group, does not suffice.

Even a nonzero 2-Selmer class can arise from the 2-torsion in the Shafarevich–Tate group rather than a positive-rank rational point. No use is made of BSD, GRH, or a conjectural rank parity.

## 7. Executed computations, failures, and preservation

**Completed.** Both exact checkers agree on their complete certificate output. Python uses symbolic resultants, discriminants and a rational basis determinant. TypeScript uses Newton traces, a 34-dimensional integer Gram determinant, separate multiplication-matrix norms, and a Frobenius-gcd irreducibility certificate at 5. They check the shift (2.1), prime degrees, generators, monic-model and root-field identities, and every local squareclass in (5.2)–(5.4). Their dimension counts corroborate the proof; printing those counts is not a computation of W_2 or a Selmer group. Wolfram separately corroborates the exact identities and finite-field tests; its warning on a preliminary uppercase-symbol expression is retained, with a corrected clean call.

The public Magma calculator was reached through its documented HTTP endpoint after HTTPS connectivity failed. Actual Magma 2.29-10 responses confirm genus eight and, in a separate short job, the constructed order's discriminant, index 131072 and signature (2,16). The exact requests and returned XML are preserved.

**Not completed.** The unconditional `RankBound` request produced a gateway timeout, with no mathematical output. A default maximal-order request also timed out. A subsequent exploratory GRH class-group request and an alternative-algorithm maximal-order request were blocked before execution. They supplied no class-group, maximal-order or rank evidence, and were not retried through another route. No conjectural output is used. A small exact unit-discovery experiment found only a low-rank subgroup in its stated polynomial domain; it is not a unit basis or a rank certificate. These limitations and unsuccessful requests remain in the evidence record.

The reproduction script is offline and runs strict TypeScript checking, both exact verifiers, Python compilation/tabnanny and full-output comparison. It does not call the external calculator. A fresh-extraction replay checks the delivered manifest and reruns these tests. Availability of Bun and separate lint tools is recorded from this runtime, not inferred from earlier turns. No external expert was contacted, no paper or claim was submitted, and no additional paid resource was authorized.

U77's nonzero-class argument was read and its complete arithmetic output replayed, but not independently certified. The original weighted implication and all other project claims retain their stated scope. U41 remains invalidated. U61/U62 concern a separate coefficient-two branch. **U78 eliminates no new weighted solution case and no complete Beal signature.**

## Sources

[S1] J.S. Milne, *Algebraic Number Theory*, version 3.08, 19 July 2020, https://www.jmilne.org/math/CourseNotes/ANT.pdf . Proposition 7.55 and Remark 7.56, printed pp.129–130, and Theorem 5.11, p.90, were inspected in the original PDF and page images. The specialized field and prime-ideal calculations above are derived here.

[S2] Michael Stoll, *Implementing 2-descent for Jacobians of hyperelliptic curves*, Acta Arithmetica 98 (2001), 245–277, DOI 10.4064/aa98-3-4. Primary publisher PDF: https://www.impan.pl/shop/en/publication/transaction/download/product/83397 . Section 4, especially Lemmas 4.1, 4.3, 4.4, 4.9 and Corollary 4.7; the number-field norm caveat at the end of Section 4. Relevant text and printed pp.250–253 page images were inspected. The base-field specialization, dimensions and explicit local-5 line are proved above, not read as results about our curve from that paper.

[S3] Official Magma documentation, *Jacobians over Number Fields or Q*, https://docs.magma-maths.org/ArithmeticGeometry/HyperellipticCurves/jacobians-number-fields.html ; *Number Fields and Orders—Creation*, https://docs.magma-maths.org/GlobalFields/NumberFieldsAndOrders/creation.html . The distinction between constructing an order and proving maximality is retained. The public calculator's actual returned limits and successful output are in the execution evidence.

[S4] U77, `research/checkpoints/U77_anti_invariant_twist_reduction.md`, pinned private commit `11becf1c733016efd853d136e2f1e85dab319b13`. Used only for continuity and the conditional application of a future rank-zero certificate to the weighted equation. The new field and Selmer-reduction statements are about (1.1) itself.

No novelty, independent expert or formal verification, publication, prize eligibility or full-conjecture resolution is claimed.
