# U69: joint scalar-quotient obstruction and an all-precision local limitation

**Status: written, self-reviewed partial results with distinct exact arithmetic checks. Neither the weighted equation nor the full Beal conjecture is solved. No independent expert or proof-assistant certification is claimed.**

Research date: 2026-09-15. Private remote revision inspected: `9ed3f2c0b04b59222516183b62282c13ea2c58c8` (U68). The attached U68 archive was restored additively; no conflicting files were overwritten. U68's Python computation was replayed with exactly the same mathematical output, into a new log rather than replacing the old evidence.

## 1. Scope and result

The active weighted equation is

    (W) X^10 + 256Y^10 = Z^17,
        X,Y,Z positive integers, gcd(X,Y)=1.

The remote quintic U65 supplies the written necessary condition

    (Q) beta^17 = X^2 + 2rho^3 Y^2,
        rho^5=2, rho>0,
        beta=b0+b1rho+b2rho^2+b3rho^3+b4rho^4 in Z[rho].

Gaussian factorization independently gives

    (G) (a+ib)^17 = X^5 + 16iY^5.

U68 reconstructs the Gaussian cases and proves that 17 and every prime in

    Pset={11,31,41,61,71,101,151,191,211,281,331,431,461,631}

divide Y. In particular X is a unit at 17. Write

    P=product(Pset)=433992707035920672833426144791,
    T=max(X,Y).

The weighted applications here inherit the written/self-reviewed U65 implication (W)=>(Q). No boundary-curve congruence, Hilbert-newspace completeness claim, U41 elimination, or conjectural rank is used.

Define a rational prime q to be **jointly exceptional** when

    q mod340 is in {1,67,69,137,203,273,339},           (1.1)

and, in the class q=1 modulo 340 only, additionally

    2^((q-1)/5)=1 modulo q.                          (1.2)

Let J be the product of q^v_q(XY) over these primes, retaining the full multiplicity of each prime. The main weighted consequence is

    J^2 > 17^15 P^30 > 10^906,
    therefore J > 10^453.                            (1.3)

Thus at least one prime from this more restrictive set must divide XY, and those primes must account for a large product of prime powers. This does **not** forbid all other primes from dividing X or Y, does not bound a single prime below by 10^453, and does not give an upper bound on J.

U68's separate bounds T>10^514 and its broader exceptional product >10^483 remain unchanged. The new result is a restriction on which primes must support part of that large product, not a claim to have increased the 515-digit base bound.

The limiting result is also explicit: at q=137 there are compatible solutions of (Q), (G), and both norm equations in the 137-adic integers for every positive valuation of Y. Both roots can remain nonscalar modulo 137. Section 7 proves this for all precisions and supplies a checked example modulo 137^12. It is not an integer solution of (W).

## 2. Root uniqueness in a quotient, not in the full unit group

For a prime q and n>=1, put

    R(q,n)=(Z/q^n Z)[rho]/(rho^5-2),
    C(q,n)=(Z/q^n Z)^*,

where C embeds as the scalar units of R. If the finite quotient group R(q,n)^*/C(q,n) has order prime to 17, then

    u^17 scalar and invertible  =>  u scalar.        (2.1)

Indeed the class of u in that quotient is killed by 17, so it is the identity. This does not require the power map on the full unit group to be injective; scalar seventeenth roots of unity are harmless here.

Reduction modulo q induces a surjection of these quotient groups. Its kernel is a q-group: after multiplication by a scalar lift, a representative in this kernel is 1 modulo q, and successive congruence subquotients are additive groups in characteristic q. Consequently, for q!=17 it suffices to test the quotient modulo q.

For q away from 2 and 5, factor rho^5-2 into irreducibles of degrees d1,...,ds over F_q. The Chinese remainder decomposition shows that this quotient has order

    product(q^dj-1)/(q-1).                           (2.2)

U68's affine-Frobenius argument gives precisely these factor-degree patterns:

| q modulo 5 | Factor degrees |
|---|---|
| 1 | (5) or (1,1,1,1,1) |
| 2 or 3 | (1,4) |
| 4 | (1,2,2) |

For completeness, Frobenius permutes the roots rho*zeta_5^j by j->qj+c. A nonidentity slope can be translated to fix zero, giving the displayed nonzero orbit lengths; slope one gives either five fixed points or a five-cycle.

For the irreducible pattern (5), the order in (2.2) is

    q^4+q^3+q^2+q+1.

It is never divisible by 17. If q=1 modulo 17 its value is 5; otherwise a zero would imply that the order of q modulo 17 divides both 5 and 16, which is impossible. Thus **every irreducible quintic residue prime is good for (2.1)**, even if scalar units have nontrivial seventeenth roots of unity.

In the other three patterns, the quotient orders are respectively (q-1)^4, q^4-1, and (q^2-1)^2. Therefore the quintic bad-prime set is exactly U68's eleven classes modulo 85,

    {1,13,18,33,38,47,52,67,69,72,84},               (2.3)

with the following refinement: in class q=1 modulo 85 a prime is bad only when 2 is a fifth power modulo q. When q=1 modulo 5, a fifth root of 2 gives all five roots; absence of one gives the five-cycle and irreducibility.

At 2 and 5 the ramified residue unit groups have orders 16 and 4*5^4. Their scalar quotients and all higher reduction kernels have orders prime to 17. They are good primes. The prime 17 is treated separately below, with the one-digit valuation loss retained.

This refines U68's sufficient full-unit-group criterion. It does not invalidate that earlier criterion or its conclusions.

## 3. The refined quintic support inequality

Let S_Q be the part of XY supported outside the refined quintic bad set. Include 2,5,17 in S_Q when they divide XY.

For q!=17 dividing Y to exponent e, (Q) modulo q^(2e) makes beta^17 the scalar unit X^2. If q is good, (2.1) forces beta to be scalar, and hence

    q^(2e) divides b1,b2,b3,b4.

For an odd good prime q dividing X to exponent e, normalize beta by rho^4. The identity

    (beta/rho^4)^17 = Y^2/2^12 + X^2 rho^2/2^14

makes its seventeenth power scalar modulo q^(2e). The constant coefficient of beta/rho^4 is b4, and its other coefficients are b0/2,b1/2,b2/2,b3/2. Thus q^(2e) divides b0,b1,b2,b3. Only units were divided out. X is odd, so a prime 2 dividing X is not an omitted case.

At 17, U68's explicit binomial leading-term proof gives divisibility by 17^(2e-1), not 17^(2e), for the relevant nonconstant coefficients. It uses the reduced residue algebra and the facts that binomial(17,j) has valuation one for 1<=j<=16 and higher terms have strictly higher valuation. No injectivity on principal units at the exponent prime is asserted.

Combining these statements gives

    S_Q^2/17 divides b1,b2,b3.                       (3.1)

The divisor is integral because 17|Y. U68's binomial sparsity calculation proves that these three coefficients cannot all vanish for X,Y>0. Its Fourier inversion bound on all five actual conjugates then proves, with exactly the same argument and now the enlarged good set,

    S_Q^34 < 17^17 T^2,
    S_Q < sqrt(17) T^(1/17).                         (3.2)

The supporting sparsity and archimedean arguments are U68 Sections 5 and 6, not a new unverified lemma. Changing the good-prime criterion only strengthens their divisibility input.

## 4. A complementary Gaussian support inequality

The corresponding scalar quotient for

    A(q,n)=(Z/q^n Z)[i]/(i^2+1)

has, for odd q, residue order

    q-1 if q=1 modulo4,
    q+1 if q=3 modulo4.                             (4.1)

In the split case divide F_q^* x F_q^* by its diagonal scalars; in the nonsplit case divide F_(q^2)^* by F_q^*. Higher kernels are q-groups as before.

For q!=17, this quotient has 17-torsion exactly when

    q=1 modulo68 or q=67 modulo68.                  (4.2)

It is not enough that q be plus or minus one modulo 17: the splitting behavior at i matters. For instance 101 and 103 have no such relative torsion despite being -1 and 1 modulo17, respectively.

Let S_G be the part of XY outside the set (4.2), again including 2 and 17. For a good odd q!=17 dividing Y to exponent e, (G) modulo q^(5e) makes (a+ib)^17 scalar. The quotient argument forces q^(5e)|b. If q divides X, apply it to -i(a+ib)=b-ia, whose seventeenth power is 16Y^5-iX^5; it gives q^(5e)|a.

At 17 the same leading-term argument, or the exact Gaussian cofactor valuations in U68 Section 7, gives exponent 5e-1 on the appropriate coordinate. Modulo 17 the Gaussian algebra splits, and its seventeenth-power map is the identity. The divisible coordinate is consequently divisible by 17, while the other is a unit, so the leading-term argument applies.

At 2 the root has a odd and b even. The imaginary coordinate form H is odd, and bH=16Y^5 gives exactly

    v2(b)=4+5v2(Y).

Since gcd(X,Y)=1 and both a,b are nonzero, all these valuations combine into

    16 S_G^5/17 divides ab.                          (4.3)

The factors 16 and 17 are explicit; neither is silently lost. The Gaussian norm gives a^2+b^2=Z and hence |ab|<=Z/2. Thus

    S_G^5 <= 17Z/32,
    S_G^85 <= (17/32)^17 (X^10+256Y^10)
             <= [257*17^17/32^17] T^10 < T^10.

The final strict inequality is the exact integer comparison

    212600747304788548393489
      < 38685626227668133590597632.

Consequently

    S_G < T^(2/17).                                 (4.4)

## 5. Combining two roots for the same X,Y

Let D=gcd(S_Q,S_G). Each support part retains the full exponent v_q(XY), so prime by prime

    S_Q S_G = D*XY/J,                               (5.1)

where J is the part of XY bad for both quotient arguments. Combining (3.2), (4.4), and (5.1) yields

    J > D*XY/[sqrt(17) T^(3/17)].                    (5.2)

This is a global inequality involving the same X,Y and their common prime support, rather than independent local variables.

Intersecting (2.3) and (4.2) gives exactly the seven classes (1.1). The only class in the intersection where quintic irreducibility can remove the exception is q=1 modulo340; there the extra condition is precisely (1.2). This proves the claimed description of J.

Every prime in Pset is good for both quotients: it is 1 modulo5 but not 1 modulo17, and it is not plus or minus one modulo68. Since 17P divides Y, we obtain D>=17P. Also XY>=T, and U68 gives T^2>(17P^2)^17. Therefore

    J > sqrt(17) P T^(14/17)
      > sqrt(17) P (17P^2)^7
       =17^(15/2) P^15.

Squaring proves (1.3). Exact exponentiation gives a 908-digit integer for 17^15 P^30 and confirms that it exceeds 10^906. No floating-point estimate decides the threshold.

In particular there is no weighted solution, under the inherited pure-root implication, whose prime support entirely avoids this jointly exceptional set. An unbounded product on that set, however, remains compatible with the inequality. This is not a full elimination of the weighted equation or of any remaining complete Beal exponent signature.

## 6. Exact checks of the relative criteria

The Python checker factors T^5-2 at all 300 primes 3<=q<2000 other than 5 and17, computes (2.2) from the actual degrees, and compares it with the refined criterion and seven-class intersection. These finite checks corroborate the uniform proofs; they do not replace them.

At class-one primes the distinction is visible directly:

| Prime q | 2^((q-1)/5) modulo q | Factor degrees | Jointly exceptional? |
|---:|---:|---|---|
| 1021 | 589 | (5) | No |
| 1361 | 211 | (5) | No |
| 2381 | 1 | (1,1,1,1,1) | Yes |
| 3061 | 1 | (1,1,1,1,1) | Yes |

The TypeScript checker separately counts the actual fifth roots for these four primes, without relying on the factorization routine. Both implementations enumerate all Gaussian norm-one seventeenth roots over q=13,19,67,101,103,137 and obtain kernel sizes 1,1,17,1,1,17. This checks the relative-kernel refinement at primes where the older full-unit criterion would have been unnecessarily restrictive.

## 7. A surviving joint local system, at every precision

The remaining exception cannot be removed by assuming that at least one of the two roots must become scalar at every prime of XY. Here is an explicit counterexample to that proposed local lemma.

At q=137, choose a0=9 with a0^5=2 and zeta=119 of order17 in F_137. Factor

    T^5-2=(T-a0)h(T),
    h(T)=T^4+a0T^3+a0^2T^2+a0^3T+a0^4.

The idempotent e0=h(rho)/(5a0^4) projects onto the linear factor. Set

    eta=zeta+(zeta^(-4)-zeta)e0
       =67+116rho+89rho^2+86rho^3+40rho^4.

Its components are zeta^(-4) and the scalar zeta in the rank-four factor. Therefore eta^17=1 and Norm(eta)=zeta^(-4)*zeta^4=1. It is nonscalar, and each of its rho,rho^2,rho^3 coefficients is nonzero.

For the Gaussian algebra take i0=37, a square root of -1 modulo137. The element with split components (zeta,zeta^(-1)) is

    theta=10+77i,
    theta^17=1, Norm(theta)=1.

For any integer e>=1, now set X=1 and Y=137^e in the 137-adic integers. The targets

    1+2rho^3Y^2,  1+16iY^5

are both 1 modulo137. Starting from eta and theta, their seventeenth roots lift to all powers of137: the derivative 17u^16 is a unit at each starting point. Explicitly, if u is a root modulo q^n, add q^n times the uniquely determined correction obtained by multiplying the error quotient by the inverse derivative modulo q. This inductively constructs compatible roots for every n, and completeness gives roots in the corresponding finite free Z_137-algebras.

The scalar equation

    Z^17=1+256Y^10, Z=1 modulo137

also has a unique compatible lift. Multiplicativity of the two algebra norms shows that both root norms are seventeenth roots of this same scalar target, congruent to1 modulo137. Scalar uniqueness therefore gives Norm(beta)=Norm(a+ib)=Z throughout. Both roots retain their nonscalar residues.

An exact example for e=1 and n=12 is stored in `certificate_summary.json`. The modulus is

    137^12=43716643078717303412870881.

Python, TypeScript, and Wolfram directly check the full quintic and Gaussian power equations, both norm equations, and (W) modulo that modulus. The infinite-precision assertion follows from the explicit derivative/lifting proof above, not from testing twelve digits.

These are local solutions only. They need not be positive rational integers, and the stored representatives do not satisfy (W) as an integer equality. They do show that joint local precision at a prime such as137 cannot by itself prove J absent or bounded. No conclusion about compatibility at all primes or existence of a global point is inferred.

## 8. Verification, continuity, and next action

The new source files are `code/U69_joint_support.py` and `.ts`. Python uses SymPy factorizations/resultants and direct cyclic ring multiplication; TypeScript uses bigint, a multiplication-matrix determinant, full fifth-root enumeration in the specified examples, and seventeen successive multiplications. Their complete shared summary, including all coefficients of the local witness, agrees exactly. Wolfram reproduces the factor degrees, torsion identities, modular witnesses, norms, and exact inequalities.

The reproduction script runs both checkers, strict TypeScript checking, Python compilation and tabnanny, and compares the certificates. Bun, a standalone linter, and a proof-assistant runtime are not installed; none is reported as run. SymPy's internal modular-integer ordering warning is retained in stderr. The initial Wolfram call returned evaluated checks but included a global-symbol advisory for X,Y; a separate call using only numeric targets returned the same zero residuals without that advisory. Both records are retained.

The mathematical audit checked: scalar quotient versus full-unit injectivity; the irreducible quintic case at q=1 modulo17; the split/inert distinction for the Gaussian group; the lost digit at17; the extra factor16 at2; use of full prime multiplicities in (5.1); signs and nonzero Gaussian coordinates; distinguishing a large prime-power product from a large single prime; and separating a local witness from an integer counterexample.

This is same-model proof review and distinct arithmetic corroboration, not independent expert review, an isolated mathematical agent, or a proof-checking kernel. The explicit system (Q),(G) and the inherited U65 implication must remain visible in the dependency chain. U41 stays invalidated; U61/U62 retain their separate previous status.

**Next global obligation:** control the choices of nonscalar seventeenth roots at the jointly exceptional primes for one common integral beta and one common Gaussian root, or obtain an effective upper bound on the sparse integral root. Section 7 rules out the shortcut that simultaneous norms or unlimited one-prime lifting automatically force scalar roots. U69 supplies no upper bound on J, so increasing its lower bound or merely extending the old forcing-prime list is not a resolution of this obligation.
