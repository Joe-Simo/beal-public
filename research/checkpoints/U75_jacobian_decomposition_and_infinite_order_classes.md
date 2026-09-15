# U75: explicit Jacobian factors, exact torsion, and fifteen independent infinite-order classes

**Status: written, self-reviewed geometric and arithmetic theorems, with distinct exact implementations. The weighted equation and the full Beal conjecture remain unresolved. No independent expert or proof-assistant certification is claimed.**

Research date: 2026-09-15. The private repository head inspected was `e328962be7621a0b0276ff27f4c35b0838346b2d` (U73). The attached local U74 manuscript and evidence archive were read and restored additively: 46 files restored, three identical, no conflicting file overwritten. U74 was not on the remote branch when this continuation began. The new arguments below concern its explicitly defined curve, not an assumed completed classification of its points.

## 1. Result and exact scope

Let zeta be a primitive fifth root of unity, let B=Q(i,zeta), and put d=1+zeta. U74's curve

    D: T^17+zeta*S^17=d*W0^17

becomes

    F: A^17+B1^17=d*W0^17                           (1.1)

under A=T and B1=zeta^3*S, since (zeta^3)^17=zeta. Here B1 is a coordinate, whereas B is the number field. F is a smooth plane curve of degree seventeen, of genus 120. For each a=1,...,15 let C_a be the **smooth projective normalization** of

    C_a: y^17=x^a(d-x),                             (1.2)

and let J_a be its Jacobian. Every C_a has genus eight.

**Main theorem.** Over B, there are explicit degree-seventeen maps f_a:F -> C_a inducing isogenies

    Phi: J_F -> product_(a=1)^15 J_a,
    Psi: product_(a=1)^15 J_a -> J_F,
    Psi Phi=[17],  Phi Psi=[17].                    (1.3)

For all fifteen factors,

    J_a(B)_tors = <[P0-Pinfinity]> = Z/17Z,          (1.4)

where P0 and Pinfinity are the unique points above x=0 and x=infinity. The B-rational point

    Q_a=(1,zeta^3)

gives an infinite-order class [Q_a-Pinfinity]. Their pullbacks along the fifteen maps give fifteen independent classes modulo torsion on J_F(B). In particular,

    rank J_F(B) >= 15.                              (1.5)

Also every B-rational torsion class of J_F is killed by 289. This is an exponent bound, not a calculation of that full torsion group.

The new result replaces one dimension-120 Jacobian problem by explicit dimension-eight factors and supplies non-torsion starting classes. It also rules out a rank-zero or torsion-only shortcut for U74's degree-five divisor problem. **No new weighted solution, degree-five point, or complete Beal signature is eliminated.** The exact ranks, full Mordell-Weil groups, finite-index bounds, saturation, and relevant effective degree-five divisors are not computed.

The geometric and factor-arithmetic statements need only (1.1), not U71 or any earlier conjectural application. Their use for the weighted equation

    X^10+256Y^10=Z^17, X,Y,Z>0, gcd(X,Y)=1

inherits U71/U74's written common-root reduction. That application remains self-reviewed. U41 stays invalidated; no boundary-curve congruence, unchecked modular-form list, or rank conjecture is invoked here.

## 2. Quotient maps and the full decomposition

On W0=1 define

    f_a(A,B1)=(A^17,A^a B1).                        (2.1)

The relation y^17=x^a(d-x) follows directly from (1.1). A nonconstant rational map between smooth projective curves extends uniquely to a morphism. Over a field containing a primitive seventeenth root xi, its generic fiber is the orbit of

    (A,B1) -> (xi*A,xi^(-a)*B1).

These seventeen points are distinct generically, and adjoining A with A^17=x recovers B1=y/A^a. Thus the map has degree seventeen. The monomial formula (2.1) is defined over B, even though this description of all deck transformations uses an extension of B. No seventeenth root of unity is incorrectly assumed to lie in B.

The degree-seventeen map x:C_a -> P1 is ramified exactly at 0,d,infinity. The corresponding exponents are a,1,-a-1; each is coprime to seventeen. There is one point above each branch point, and all three are B-rational. Riemann-Hurwitz gives

    2g(C_a)-2=17*(-2)+3*(17-1)=14.

For F, a basis of holomorphic differentials in the affine chart is

    omega_(r,s)=A^(r-1)*B1^(s-17)*dA,
    r,s>=1, r+s<=16.                               (2.2)

This is the usual plane-curve differential basis: it has 120 elements, and its displayed exponents make it regular at the coordinate branches and infinity. The subgroup for a acts on it by xi^(r-a*s). Therefore the pullback differentials from C_a occupy exactly the eight pairs satisfying

    r=a*s modulo 17.                               (2.3)

Every pair in (2.2) occurs in exactly one of the fifteen blocks. Indeed s is nonzero modulo 17, so it determines a=r/s; a=16 is excluded because r+s<17. The complete 120-entry partition is retained in the finite output.

Set Phi=(f_(a*) )_a and Psi=sum f_a^*, using the pushforward and pullback maps on Jacobians. The usual divisor identities for a degree-seventeen quotient are

    f_(a*) f_a^*=[17],
    f_a^* f_(a*)=sum over its seventeen deck transformations.

The second identity acts on (2.2) as seventeen times the projector to block a. Summing over all a gives [17]. For different blocks b and a the composite f_(b*) f_a^* is zero: after extension to C its differential is zero by the disjoint character spaces, and a homomorphism of complex tori with zero differential is zero. The identities descend to B. This proves both equations in (1.3). They imply finite kernels and surjectivity, so these are isogenies, not merely dimension counts.

One must not replace an isogeny by an isomorphism on rational torsion or on integral Mordell-Weil lattices. Its seventeen-primary kernels matter later.

### 2.1 Eight displayed equations suffice, but distinctness is not asserted

Let b be the inverse of a modulo seventeen and k=(ab-1)/17. The rational formulas

    x'=d-x,  y'=y^b/x^k                            (2.4)

give an isomorphism C_a -> C_b. Raising the second expression to the seventeenth power verifies the target equation. Applying the analogous map back gives

    y''=y^(ab)/(x^(ak)*(d-x)^k)=y,

using y^17=x^a(d-x). The maps extend at the omitted affine points by smooth projectivity.

The resulting pairs are

    (1,1), (2,9), (3,6), (4,13),
    (5,7), (8,15), (10,12), (11,14).

Thus eight listed models suffice to represent these fifteen factors under these explicit isomorphisms. This is **not** a proof that the eight representatives are mutually nonisomorphic, and repeated isomorphic factors must not be dropped from the product.

## 3. Exact finite-field group orders

We compute at three rational primes,

    q=1021,1361,2381.

Each is 1 modulo 340, and so splits completely in B. To fix the prime of B rather than silently identifying conjugate places, choose the smallest primitive root g modulo q and use

    zeta -> g^((q-1)/5),  i -> g^((q-1)/4).

The g and zeta values are respectively

| q | g | zeta modulo q |
|---:|---:|---:|
| 1021 | 10 | 802 |
| 1361 | 3 | 211 |
| 2381 | 3 | 1347 |

Here d=1+zeta is nonzero. Each curve has good reduction at the chosen prime. In fact the three branch sections 0,d,infinity stay disjoint, and seventeen is invertible. Locally at a branch, after an unramified extension the unit in the Kummer equation has a seventeenth root; normalization is given by x=s^17 and y=s^a, with the coprime branch exponents above. These local normalizations and the etale locus form a smooth proper model. The Jacobian therefore has good reduction too. This argument concerns the normalized curve, not the possibly singular naive affine equation for a>1.

### 3.1 A source-checked group-order formula, including its sign

Let chi(g)=xi, with xi a complex primitive seventeenth root, and extend nontrivial characters by zero at zero. Define

    S_a=sum_(x!=0,d) chi(x)^a*chi(d-x)
       =chi(d)^(a+1) J(chi^a,chi).                 (3.1)

All three characters chi^a,chi,chi^(a+1) are nontrivial. The Davenport-Hasse norm-lifting formula [S1, Theorem 1.1] therefore applies. For every n>=1 the corresponding sum over F_(q^n), using the norm-lifted character, is

    S_(a,n)=(-1)^(n-1)*S_a^n.

The twist has not been omitted: the lifted chi evaluated at d equals chi(d)^n. Counting the three ramified points and the nonbranch fibers yields

    #C_a(F_(q^n))=q^n+1+(-1)^(n-1)*Tr(S_a^n)
                 =q^n+1-Tr((-S_a)^n).              (3.2)

The curve/Jacobian Frobenius relation [S2] and the abelian-variety group-order formula [S3] now give

    #J_a(F_q)=Norm_(Q(xi)/Q)(1+S_a).                (3.3)

In particular the sign is **plus**, not minus. The derivation uses all n via the lifting theorem; one point count by itself would not determine a genus-eight Jacobian order.

To evaluate (3.3), enumerate the integers

    n_j=#{x!=0,d: a*log_g(x)+log_g(d-x)=j modulo17}.

Then S_a=sum n_j*xi^j, and its required norm is the exact integer resultant

    Res_U(Phi_17(U),1+sum_(j=0)^16 n_j U^j).        (3.4)

Python computes (3.4) symbolically. TypeScript uses the multiplication matrix in Z[U]/Phi_17 and a bigint fraction-free determinant, and obtains the characters from an order-seventeen subgroup instead of the full discrete-log table. All 45 character vectors, point counts and group orders agree exactly. The output also verifies S_a*conjugate(S_a)=q in the cyclotomic field.

As an additional sign and extension check, an integer-only direct enumeration on the hyperelliptic model for C_1,

    v^2=d^2-4u^17,

counts all 1,042,441 inputs u in F_(1021^2). Including infinity, it gives 1,041,015 points, exactly q^2+1-Tr(S_1^2). This is a separate finite calibration, not a substitute for the all-n source theorem.

The complete forty-five group orders are in `research/computations/U75/reduction_orders.md` and both full JSON outputs. For example the three orders for a=1 are

    1262503088987509144646987,
    10650026769976589503484113,
    883742138162535843505714261.

## 4. The full B-rational torsion of every factor

The divisor of x on C_a is

    div(x)=17(P0-Pinfinity).

The class P0-Pinfinity is not zero. A function with that divisor would have exactly one simple pole and give a degree-one map to P1, contrary to genus eight. Thus J_a(B) contains a cyclic subgroup of order seventeen.

For the upper bound, at a good prime of residue characteristic q the reduction map is injective on prime-to-q torsion. Its kernel is a formal group filtered by additive groups of residue characteristic q; multiplication by any other prime is invertible there. Properness allows all rational points to reduce.

For every a, the gcd of the three computed orders is exactly seventeen. For a torsion prime ell different from the three residue characteristics, its primary subgroup injects into all three reductions and its order divides their gcd. This excludes all such ell except seventeen and bounds the seventeen-primary subgroup by seventeen.

**The residue characteristics themselves require an extra check.** For each q in the three-prime set and each a, at least one of the other two reduction orders is not divisible by q. Thus q-primary torsion is excluded using good reduction of a different residue characteristic. The full nonzero-residue certificates are stored, rather than assuming that q-primary torsion injects at q. This distinction is material: at a=11 and a=14, the order at 1361 is divisible by 1021, and the third prime supplies the needed alternative.

Together these computations prove (1.4), including exact cyclic structure because the known subgroup already has the maximal allowed order. The statement is over B. It is not promoted to the larger field M or to all bounded-degree extensions.

## 5. A proof that fifteen explicit classes have infinite order

Every C_a contains Q_a=(1,zeta^3), since (zeta^3)^17=zeta=d-1. We prove

    17[Q_a-Pinfinity] != 0.                         (5.1)

By Section 4 this excludes all torsion possibilities for that class.

### 5.1 A complete, explicit Riemann-Roch space

For 1<=k<=16 let

    r_k=ak modulo17 in {1,...,16},
    h_k=y^k/x^floor(ak/17).

At P0 this function has order r_k, at the point above d it has order k, and its only pole is at infinity of order

    w_k=k+r_k.

Exactly eight k satisfy w_k<=17. The functions

    1, x, and these eight h_k                       (5.2)

lie in L(17Pinfinity). Their pole orders are distinct: w_k is congruent to (a+1)k modulo17, while a+1 is nonzero modulo17, and none of these w_k equals seventeen. Hence they are linearly independent. Riemann-Roch gives

    dim L(17Pinfinity)=17+1-8=10,

because degree seventeen exceeds 2g-2. Thus (5.2) is the entire space, not just a convenient tested subset.

### 5.2 An invertible jet matrix

At Q_a, z=x-1 is a local parameter. The branch of y specified by y(Q_a)=zeta^3 gives

    h_k(z)=zeta^(3k)*(1+z)^(r_k/17)*(1-z/zeta)^(k/17).  (5.3)

Take the coefficients of z^0,...,z^9 for the ten functions (5.2). Their denominators are units at the degree-one prime of B over 41 defined by zeta->10 and i->9. Reduce the resulting ten-by-ten matrix there. The determinants for a=1,...,15 are

    18,38,18,21,19,40,20,24,18,17,12,5,19,39,11  modulo41.

All are nonzero, so the characteristic-zero jet map also has rank ten. No nonzero function in L(17Pinfinity) can vanish to order ten or more at Q_a. In particular no such function has divisor 17Q_a-17Pinfinity. This proves (5.1).

Python builds the jets by convolving two binomial series. TypeScript instead solves their differential equation coefficient by coefficient:

    (1+z)(zeta-z)h'=((r_k*zeta-k)-(r_k+k)z)h/17.

Their entire matrices, not just the fifteen determinants, agree. Wolfram independently reproduces the determinant list by exact rational reduction modulo 41. No numerical integration or rank conjecture is involved.

Let D_a=[Q_a-Pinfinity]. If a relation among f_a^*D_a were torsion in J_F(B), pushing it through f_(b*) would give 17*n_b*D_b torsion. Since D_b has infinite order, n_b=0. This holds for every b, proving independence and (1.5). Isomorphic factors in Section 2.1 still supply independent positions in this product argument.

Finally, if R is torsion in J_F(B), then 17Phi(R)=0 by (1.4). Applying Psi and (1.3) gives 289R=0. We do not claim that the whole torsion group is (Z/17Z)^15, or that every seventeen-primary kernel point is B-rational.

## 6. Retaining the original cyclic degree-five target

Decomposition alone would lose important information if projected divisor classes were allowed to vary independently. Here is the explicit common constraint for U74's weighted image.

Write theta_j=sigma^j(theta), sigma(c)=zeta*c, and let u=cY/X. Then u^5=lambda, where

    lambda=16i*(Y/X)^5 in B.

For the five conjugates of the image on F, the coordinates on C_a are

    x_j=(X+zeta^(j+1)cY)/(X+zeta^j cY),
    y_(a,j)=zeta^3*theta_(j+1)^a*theta_(j-1)/theta_j^(a+1).

The x_j are the same for all fifteen factors. They are exactly the roots of

    (x-1)^5+lambda*(x-zeta)^5.                      (6.1)

Indeed the product of the five linear expressions

    (x-1)+zeta^j*u*(x-zeta)

is (6.1). Python checks this polynomial identity symbolically modulo Phi_5; TypeScript checks it on a six-by-six exact interpolation grid with a degree-at-most-five bound in each variable. The roots have product one. Telescoping likewise gives

    product_(j=0)^4 y_(a,j)=1

for every a. The formulas retain one common theta, not independent local norm choices.

For positive X,Y, lambda is nonzero and 1+lambda is nonzero. Recovering u=(x_0-1)/(zeta-x_0) proves B(x_0)=M, the same cyclic degree-five field as in U74. Thus each projected point has that exact degree, not an arbitrary lower-degree point on C_a.

Let Delta be the five-point orbit divisor on F, and P+=(1,zeta^3,1), the image of U74's (1,1,1). Then

    Phi([Delta-5P+])_a=[sum_j (x_j,y_(a,j))-5Q_a].   (6.2)

Equations (6.1), the common field, the norm-one identities, the positive rational ratio Y/X, and the inherited common-root restrictions must all be retained. For example C_1 is hyperelliptic, so low-degree points on that quotient alone cannot classify the finite plane-curve target.

Equation Psi Phi=[17] permits recovery of seventeen times the original divisor class from the factor classes. Actual recovery still involves seventeen-division and the finite kernel, followed by effectivity and all the conditions above. No saturation or integral-point enumeration has been supplied. The fifteen classes constructed in Section 5 are useful non-torsion generators of a subgroup, not a proven finite-index Mordell-Weil basis.

## 7. Verification, failed attempts, and limits

The executable certificate consists of explicit character blocks, all forty-five finite reduction records, their exact gcd and cross-characteristic tests, all fifteen jet matrices, and the common-orbit polynomial identity. Python uses symbolic resultants and binomial jets. TypeScript uses bigint multiplication determinants, order-seventeen character values, and differential-equation jets. The independent quadratic-extension calibration uses integer arrays with a checked signed-int64 bound and counts a precisely specified finite domain.

An initial Wolfram call was rejected as proof evidence after inspection: a polynomial initialized in a Module declaration retained a global symbol, making the intended resultants symbolic powers rather than integers; it also used Mod on rational numbers instead of finite-field rational reduction. Corrected calls construct the polynomial after localization and reduce each rational numerator times its denominator's inverse. They return the forty-five integer orders and the fifteen determinants above. The invalid output is not counted as a successful check.

The first two-prime torsion idea was also audited before the theorem was stated. Reduction at a prime does not control torsion at that same residue characteristic; the third prime and the explicit alternatives in Section 4 close that issue. A successful character partition is not presented as expert verification of the geometric isogeny argument.

The reproduction script runs Python compilation/tabnanny, strict TypeScript checking with unchecked-index and unused-variable checks, both full exact checkers, the direct quadratic-extension count, and a complete output comparison. Bun and a standalone linter are not installed in this runtime and are not claimed as executed. The scripts do not download data, access other projects, run an unbounded search, compute a conjectural rank, or contact an expert.

**Remaining gap.** U74's required off-line degree-five divisors have not been classified or excluded. The new rank bound is only a lower bound. It neither establishes the rank hypothesis for a Chabauty computation nor gives an upper height bound opposed to earlier lower bounds. The finite point set and the positive-rank ambient Jacobian are entirely compatible. The next arithmetic obligation is a certified rank upper bound and finite-index/saturation information for the factor groups, followed by the simultaneous divisor/effectivity constraints in Section 6—not a torsion-only search.

No novelty, publication, acceptance, prize eligibility, prize award, independent certification, weighted-equation resolution or full-Beal resolution is asserted.

## Sources

[S1] Akinari Hoshi and Kazuki Kanai, *Davenport and Hasse's theorems and lifts of multiplication matrices of Gaussian periods*, arXiv:2105.14872v2, 4 August 2022, Theorem 1.1, printed page 2 (PDF index 1). Primary PDF: https://arxiv.org/pdf/2105.14872 . Parsed text and page image inspected. The statement about nontrivial character products is explicitly checked in Section 3.1; the twist and sign are derived there.

[S2] J.S. Milne, *Jacobian Varieties*, Section 11, Theorem 11.1 and Corollary 11.4, primary notes https://www.jmilne.org/math/xnotes/JVs.pdf . The theorem at printed page 35 (PDF index 34) was read in text and page image. It relates complete nonsingular curve point counts to Jacobian Frobenius traces.

[S3] J.S. Milne, *Abelian Varieties*, Chapter II, Theorem 1.1 and its proof, printed pages 75–76 (PDF indices 80–81), primary notes https://www.jmilne.org/math/CourseNotes/AV.pdf . The finite-field order is the product of one minus the Frobenius eigenvalues. The relevant text and page image were inspected. The curve-specific sums and all integer evaluations are supplied above rather than taken from a database.

[S4] Local U74, `research/checkpoints/U74_unramified_cover_and_degree_five_points.md`, and `Beal_U74_evidence.zip`. These supply the preceding fixed curve, cyclic degree-five application, boundary-line classification and remaining target. Their results are retained as self-reviewed project work, not independently certified here. Remote U73 input is pinned to `e328962be7621a0b0276ff27f4c35b0838346b2d`. U71's common-root theorem is an upstream assumption only for the application back to the weighted equation, not for the explicitly defined curve theorems (1.3)–(1.5).
