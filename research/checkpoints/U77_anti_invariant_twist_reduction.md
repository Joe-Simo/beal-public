# U77: the missing quadratic-twist component of the degree-five target

**Status: written, self-reviewed reduction and subgroup-exclusion theorems, with distinct exact arithmetic checks. The weighted equation and the full Beal conjecture remain unresolved. No independent expert or proof-assistant certification is claimed.**

Research date: 2026-09-15. The private remote was inspected at `869b2e349f55d1bb7f9a734e2ecf8d68e43165dd` (U75). The attached U76 archive and full manuscript were read and restored additively: 45 restored entries, three identical entries, no conflicting content overwritten. Every archived manifest hash was checked. The entire U76 Python output was replayed unchanged into a new U77 record. This establishes repeatability, not independent mathematical verification.

## 1. Main result: an infinite-order target outside the known subgroup

Let

    k=Q(phi), phi=(1+sqrt(5))/2,
    E=Q(zeta), zeta a primitive fifth root of unity,
    B=E(i), d=1+zeta.

Choose zeta so that phi=1+zeta+zeta^(-1). As before, the genus-120 curve is

    F: A^17+B1^17=d*W^17,

and its first quotient is C_1: y^17=x(d-x), understood as its smooth projective normalization.

Define the fixed genus-eight curve over the **real quadratic field k**

    Cminus: (3-phi) w^2 = phi^2-4u^17.              (1.1)

Equivalently, setting v=(3-phi)w gives the integral model

    v^2 = phi+2-4(3-phi)u^17.                       (1.2)

Write Jminus for its Jacobian. This curve is the quadratic twist by -1 of U73's curve; it is not that curve with an interchangeable sign.

**Theorem A.** A primitive positive solution of the weighted equation

    X^10+256Y^10=Z^17                               (W)

together with U71's written common-root conclusion produces an explicitly described **infinite-order class in Jminus(k)**. Consequently

    a weighted solution implies rank Jminus(k) >= 1.             (1.3)

Here and below the application to W inherits U71's self-reviewed common-root theorem. The construction uses the actual cyclic orbit from U74, not arbitrary points on a genus-eight quotient.

**Theorem B.** For the degree-five weighted orbit Delta on F, put

    H=[Delta-5Pplus], Pplus=(1:zeta^3:1).

There is no positive integer n for which

    nH belongs to J_F(E)+J_F(B)_tors.                (1.4)

In particular H is outside the saturation, even modulo torsion, of the rank-fifteen subgroup and its index-17 enlargement constructed in U75/U76. Those known generators are all defined over E. Merely saturating them cannot enumerate the required weighted target: a solution would require a genuinely additional quadratic-extension component.

**Theorem C.** The rational torsion of the new Jacobian is trivial:

    Jminus(k)_tors=0.                               (1.5)

This is proved both from the existing factor torsion theorem and by fresh exact good-reduction computations. It does not prove that Jminus(k) is the zero group.

Thus one concrete remaining route is to certify `rank Jminus(k)=0`. Such a certificate would exclude the active weighted equation through (1.3), but would not by itself solve all signatures of Beal's conjecture. **No rank upper bound or rank-zero certificate has been obtained in U77.** An attempted unconditional Magma rank calculation returned a tool timeout without calculation output. A bounded affine search also found no points, but neither result is a rank computation. The new theorem identifies the arithmetic component that must be controlled; it does not assume its vanishing.

## 2. The two involutions must be kept separate

Put

    epsilon=zeta^2-zeta^3, Delta0=3-phi.

Direct identities in Q[zeta] are

    epsilon^2=phi-3=-Delta0,
    d=-zeta^3*phi,
    Delta0*phi^2=phi+2,
    Norm_(k/Q)(Delta0)=5.                           (2.1)

In particular Delta0 and -Delta0 are not squares in k, because their rational norm is not a square. Also -1 is not a square in this real field. Hence

    E=k(epsilon), B=k(epsilon,i)

is a biquadratic extension of k. Its two commuting generators will be denoted

    eta(i)=-i, eta(zeta)=zeta;
    kappa(zeta)=zeta^(-1), kappa(i)=i.

Thus kappa(epsilon)=-epsilon and eta(epsilon)=epsilon. This is not a use of one ambiguous “complex conjugation” for both actions.

Let c=i*2^(4/5). Then c^5=16i. In M=B(c), extend eta by eta(c)=-c and extend kappa by kappa(c)=c. These actions commute. The extension M/B has degree five and is cyclic, with sigma(c)=zeta*c. One can see the degree directly at a prime of B over 2: its ramification index over Q is two, so the valuation of 16i is eight, not a multiple of five. A root c has valuation 8/5, forcing a degree divisible by five. Its polynomial has degree five, so that is the degree. The five roots are already c*zeta^j.

In particular c^2 is not in B. Otherwise c=(c^2)^3/(16i) would be in B. This simple degree observation is used to prove that the projected points have distinct hyperelliptic coordinates.

## 3. A normalized first quotient and its actual orbit

The first quotient has a B-independent normalization over E:

    Cplus: v^2=phi^2-4u^17,
    u=y/zeta^3, v=(2x-d)/zeta^3.                    (3.1)

Substituting y^17=x(d-x), and using (2.1), proves this is a birational isomorphism of smooth projective genus-eight curves. Its inverse is

    y=zeta^3*u, x=(d+zeta^3*v)/2.

Both have a unique rational point at infinity, which the isomorphism identifies. The polynomial phi^2-4u^17 is separable and of odd degree seventeen, so the genus is eight.

The common-root input supplies theta in Q(c), integral, with

    theta^17=X+cY.

Choose its rational-coefficient polynomial in c and put

    theta_j=sigma^j(theta), tau_j=X+zeta^j*cY,
    s_j=zeta^j*cY/X,
    u_j=theta_(j+1)*theta_(j-1)/theta_j^2,
    V_j=(1-s_j)/(1+s_j), v_j=epsilon*V_j.           (3.2)

The indices are modulo five. These are not independent root choices: all are built from the same theta. The normalized first-quotient points are P_j=(u_j,v_j), and

    u_j^17=1+(phi-3)*s_j/(1+s_j)^2,
    v_j^2=phi^2-4u_j^17.                            (3.3)

All denominators are nonzero, and each v_j is nonzero. Indeed s_j=1 or s_j=-1 would put c in B. The effective divisor

    D=P_0+...+P_4

is B-rational, and let

    Aclass=[D-5infinity] in Jplus(B).                (3.4)

Because theta is a rational-coefficient expression in c, kappa(theta_j)=theta_(-j). Therefore

    kappa(u_j)=u_(-j), kappa(v_j)=-v_(-j).

Writing iota for the hyperelliptic involution (u,v)->(u,-v), this is the exact divisor relation

    kappa(D)=iota(D), hence kappa(Aclass)=-Aclass.    (3.5)

The involution iota acts by negation on the Jacobian based at infinity: the divisor of u-u(P) gives [P-infinity]+[iota(P)-infinity]=0. Equation (3.5) has no unspecified torsion correction.

## 4. The other involution changes the divisor class nontrivially

Set

    Zclass=Aclass-eta(Aclass)=[D-eta(D)].             (4.1)

We prove Zclass is nonzero, taking care that distinct effective divisors need not generally have distinct Jacobian classes.

### 4.1 The degree-five divisor has only one effective representative

First all five u_j are distinct. If s_l=h*s_j for h=zeta^(l-j) with l!=j, then

    s/(1+s)^2 - h*s/(1+h*s)^2
      = s*(1-h)*(1-h*s^2)/((1+s)^2*(1+h*s)^2).     (4.2)

Since s and 1-h are nonzero, equality of u_j^17 and u_l^17 would imply s_j^2=h^(-1) in B. This contradicts c^2 not in B. Thus even their seventeenth powers, and hence their u-coordinates, are pairwise distinct.

The eight holomorphic differentials on Cplus are

    u^r du/v, r=0,...,7.

At each P_j, u-u_j is a local parameter because v_j!=0. The evaluation matrix of these differentials at the five points has entries u_j^r/v_j. Its first five columns form a Vandermonde matrix times nonzero row scalars. By distinctness of the u_j its rank is five. Vanishing at D consequently imposes five independent conditions on the eight-dimensional canonical space, so

    h0(K_C-D)=3,
    h0(D)=5+1-8+3=1.                               (4.3)

The last equality is Riemann-Roch. Therefore D is the unique effective divisor in its linear-equivalence class. This is a direct argument with the actual degree-five divisor, not an assumption that every degree-five divisor on a hyperelliptic curve is nonspecial. In particular it excludes the possibility of concealed hyperelliptic pairs in this orbit.

### 4.2 D and eta(D) are different divisors

The original x-coordinates of the five points are

    x_j=(1+zeta*s_j)/(1+s_j).

Let lambda=16i*(Y/X)^5. Since s_j^5=lambda, their monic polynomial is

    H_lambda(x)=((x-1)^5+lambda*(x-zeta)^5)/(1+lambda).          (4.4)

Positive rational X,Y imply lambda is nonzero and purely imaginary in the specified embedding; neither 1+lambda nor 1-lambda vanishes. Eta fixes zeta and sends lambda to -lambda. The two normalized polynomials differ by

    H_lambda-H_(-lambda)
     =2lambda*((x-zeta)^5-(x-1)^5)/(1-lambda^2).     (4.5)

The polynomial in the numerator is nonzero: its x^4 coefficient is 5(1-zeta). Therefore D and eta(D) cannot be equal, since the inverse coordinate map in (3.1) would give the same x-multiset for equal divisors.

By (4.3), different effective divisors cannot here be linearly equivalent. Hence Zclass!=0. Also, using the commutativity of eta and kappa and (3.5),

    eta(Zclass)=-Zclass, kappa(Zclass)=-Zclass.       (4.6)

This is a nonzero class in a specific pair of Galois eigenspaces, not merely a different representative of zero.

## 5. Descent to the new curve over the real quadratic field

Let q0=i*epsilon. Then q0^2=Delta0 and each of eta,kappa sends q0 to -q0. Over B the isomorphism

    I:Cminus -> Cplus, (u,w)->(u,q0*w)

identifies their Jacobians. It satisfies I^eta=-I and I^kappa=-I as a map of Jacobians, where the minus is the hyperelliptic involution.

Put R=I^(-1)(Zclass). From (4.6),

    g(R)=(I^g)^(-1)g(Zclass)=(-I)^(-1)(-Zclass)=R

for g=eta,kappa. Galois descent therefore gives R in Jminus(k), and R is nonzero because I is an isomorphism. This is descent of a divisor **class**; it does not claim that each one of its ten signed support points is k-rational.

To see directly that R has infinite order using the preserved U75 input, recall that J_1(B)_tors is cyclic of order seventeen generated by [P0-Pinfinity]. This entire torsion group is defined over E. The isomorphism (3.1) is also defined over E, so all rational torsion in Jplus(B) is fixed by eta. A torsion class satisfying eta(Zclass)=-Zclass would then be killed by both 2 and 17, and would be zero. Our Zclass is nonzero. Thus it has infinite order, as does R. This proves Theorem A.

The same argument applies to any torsion R in Jminus(k): its image under I is eta-anti-invariant and must vanish. This proves Theorem C from the existing torsion theorem. Section 7 supplies a separate finite-reduction certificate for this assertion about the new Jacobian itself.

### 5.1 Why the known generators cannot capture this target by saturation

The curve F, Pplus, O=(1:-1:0), all quotient maps, and all U75 classes f_a^*[Q_a-Pinfinity] are defined over E. So is the U76 adjoined class [Pplus-O]. Every one is fixed by eta.

For the weighted class H=[Delta-5Pplus], the pushforward through f_1 and (3.1) is

    Aclass-5[Qplus-infinity], Qplus=(1,epsilon).

The subtracted class is defined over E. Its eta-difference vanishes, so the eta-difference of this pushforward is exactly Zclass, of infinite order.

Suppose nH=S+T with n>0, S in J_F(E), and T torsion in J_F(B). Apply this pushforward and then 1-eta. The S term vanishes and the T term remains torsion, whereas the left side is nZclass of infinite order. This contradiction proves (1.4).

This excludes the whole smaller-field subgroup and its saturation modulo torsion as a location for the weighted trace, not just the fifteen exhibited generators. It does not prove that the missing component is absent. U75's rank lower bound and U76's index-17 enlargement remain correct at their prior written/self-reviewed level; U77 identifies a limitation of using those data to solve this particular target.

## 6. A precise rank-zero task, not an assumed rank result

By (1.5), a certified rank-zero result would give Jminus(k)=0 and contradict the constructed class R. The integral equation (1.2) is a valid odd-degree hyperelliptic input for a two-Selmer rank bound over a number field. Magma's current primary documentation explicitly supports this situation; it also distinguishes unconditional class-group bounds from GRH-based ones [S3].

The root algebra needed in such a descent has a concrete description. A root r of the right-hand polynomial satisfies

    r^17=phi^2/4.

At the prime of k over 2, this right side has valuation -2. Thus r has valuation -2/17, forcing its local degree to be at least seventeen. The polynomial has degree seventeen and is irreducible over k. In particular the root field has degree 34 over Q. With t=(phi/2)/r^8 one gets t^17=phi/2 and r=t^2. Its reciprocal s=1/t is integral and satisfies

    s^34+2s^17-4=0.                                (6.1)

These identities specify a field for class-group/unit work; they do not compute its class group or its two-Selmer conditions. No unproved class-group bound is supplied as a rank certificate.

The attempted calculator input is retained as `research/computations/U77/rank_attempt.magma`. It requests `RankBound` on (1.2), without setting GRH or smaller class-group bounds. The browser tool returned a timeout and no Magma computation output; it is not known from that response whether submission or calculation completed. Accordingly **no Magma rank or two-torsion output is reported as obtained**. A direct network request from the local container separately failed DNS resolution. No Sage, PARI, or installed Magma execution is claimed.

A targeted affine search tested 39,366 exact candidates u=(a+b*phi)/n^2 with -40<=a,b<=40 and 1<=n<=6, checking squares in k by exact integer norms and coordinates. It found no affine point of (1.2). This small coordinate search does not test general divisor classes, provide a height bound, or show rank zero. It remains exploration, not proof of the missing step.

## 7. Fresh torsion certificate on Jminus(k)

At the following degree-one primes of k, the integral model has good reduction. The norm of its polynomial discriminant is 2^64*5^32*17^34, so none of these primes is bad.

| q | phi modulo q | Delta0 modulo q | quadratic character of Delta0 | #Jminus(F_q) |
|---:|---:|---:|---:|---:|
| 1021 | 458 | 566 | +1 | 1262503088987509144646987 |
| 1361 | 83 | 1281 | +1 | 10650026769976589503484113 |
| 1531 | 1444 | 90 | -1 | 29460018462198273206381591 |

Each chosen phi satisfies phi^2-phi-1=0 in the residue field. To evaluate the orders, choose zeta=g^((q-1)/5), using primitive roots g=10,3,2 respectively. U75's source-checked Jacobi-sum formula for C_1 gives eigenvalues -sigma(S), where

    S=sum_(x!=0,d) chi(x)*chi(d-x), d=1+zeta,

and chi(g) is a primitive seventeenth root. Twisting multiplies all eigenvalues by e_q, the quadratic character of Delta0. Hence the exact order here is

    Norm_(Q(zeta_17)/Q)(1+e_q*S).                    (7.1)

The first two primes have e_q=+1; the third has e_q=-1. Replacing every plus by minus irrespective of the residue character would be an invalid twist calculation. The implementation checks the character from the actual Delta0, not just from a verbal twist label. Direct point counts on (1.2) give 1091,1227,1497 and agree with the corresponding traces.

Python evaluates (7.1) by an exact resultant. TypeScript constructs the multiplication matrix in Z[zeta_17] and takes its bigint fraction-free determinant, obtaining character values from an order-seventeen subgroup rather than Python's full discrete-log table. Wolfram returns the same three orders. Their gcd is one.

Prime-to-residue-characteristic torsion injects under good reduction. The three residue characteristics themselves are checked against the other two orders: the nonzero residue pairs are (239,494) modulo 1021, (626,1162) modulo 1361, and (499,1516) modulo 1531. Thus there is no omitted characteristic-primary torsion. This proves Jminus(k)_tors=0 from the reduction data and (7.1). It is **not** a proof that every k-rational point on the Jacobian is torsion or zero.

## 8. Finite orbit check and audit

The new finite orbit test works in F_41[c]/(c^5-21), with zeta=10, i=9, X=Y=1. The polynomial is irreducible, and seventeen is coprime to 41^5-1, so the common roots can be constructed exactly. Both implementations build all five theta roots, both signs of c, the normalized u,v coordinates, and the original x-polynomials. The two x-polynomials, in increasing coefficient order, are

    [40,24,22,12,21,1], [40,30,17,4,40,1].

The norms of the two Vandermonde determinants are respectively 3 and 27 modulo 41, both nonzero. Every normalized point satisfies its curve equation, and the complete returned vectors agree between Python and TypeScript. This corroborates the transformations and distinct-orbit calculation; it is not a positive-integer solution or a calculation of a Mordell-Weil rank.

The upstream U76 argument was reviewed for its actual evaluation-map domain, the four small-pole exceptions, and the distinction between an index-17 enlargement and full saturation. No new flaw in those conclusions was established by this review. The new proof was checked for: confusing eta with kappa; ignoring that Cminus has the opposite sign to U73; equating distinct divisors with distinct classes without (4.3); missing hyperelliptic pairs; treating a class as a point on the curve; mistaking known E-generators for generators over B; the twist sign at each finite prime; and using torsion computations or a point-search failure as a rank bound.

An initial TypeScript compile rejected an unparenthesized unary minus before exponentiation. Parentheses were corrected without changing any mathematical test. The rejected run is retained and not counted as a pass. The final strict compiler and both mathematical verifiers are run by `reproduce.py`, with actual stdout/stderr and complete-output comparison. Python compilation and tabnanny also run. Bun and a standalone linter are not installed in this runtime; no such checks are reported as executed. No packages were downgraded.

## 9. Status and sources

The output is a smaller, specifically identified **global rank obstruction** and an exclusion of the existing smaller-field subgroup as the possible target. It is not a rank-zero theorem, a classification of the remaining infinite-order classes, an upper height bound, an elimination of the full weighted equation, or a resolution of Beal's conjecture. U41 remains invalidated; the unproved boundary congruence and modular prerequisites are not used. U61/U62 retain their separate coefficient-two scope.

[S1] U75, `research/checkpoints/U75_jacobian_decomposition_and_infinite_order_classes.md`, remote `869b2e349f55d1bb7f9a734e2ecf8d68e43165dd`, blob `56e1e96c4b21a43b331170c2f26addd805733445`. Used for the B-rational factor torsion and its source-checked Jacobi-sum/Frobenius formula. These remain inherited written/self-reviewed statements. The new twist orders are independently recomputed arithmetic, not independent certification of that formula's proof.

[S2] Giovanni Falcone and Giuseppe Filippone, *Mumford representation and Riemann-Roch space of a divisor on a hyperelliptic curve*, Cryptography and Communications 16 (2024), 949-959, DOI 10.1007/s12095-024-00713-2. Primary full HTML inspected. Its hyperelliptic/Riemann-Roch setup is consistent with Section 4; the actual five-point rank calculation is proved there directly, not obtained from a numerical point search. URL: https://link.springer.com/article/10.1007/s12095-024-00713-2 .

[S3] Current Magma Handbook, *Jacobians over Number Fields or Q*, sections on `TwoSelmerGroup` and `RankBound`, and *Ideal Class Groups*, proof-bound settings; official calculator page. Primary HTML inspected on this run. The documented applicability and unconditional-versus-GRH distinction were used to construct the attempted input. No returned software rank is claimed. URLs: https://docs.magma-maths.org/ArithmeticGeometry/HyperellipticCurves/jacobians-number-fields.html ; https://docs.magma-maths.org/GlobalFields/NumberFieldsAndOrders/ideal-class-group.html ; https://magma.maths.usyd.edu.au/calc/ .

[S4] U71's common-root theorem and U74's explicit degree-five orbit, as preserved in the project; local U76 manuscript and hash-verified archive. Their exact field and positivity hypotheses are retained. The new nonvanishing argument does not invoke U74's abstract finiteness statement as if it were an effective point list. Exploratory literature results on other Fermat twists and base fields do not supply a rank upper bound for (1.2).

No novelty, publication, expert acceptance, independent certification, prize eligibility or prize award is asserted.
