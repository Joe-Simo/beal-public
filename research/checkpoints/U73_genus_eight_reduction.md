# U73: a fixed genus-eight reduction, its actual point field, and the absence of an elliptic quotient

**Status: written, self-reviewed reduction and method-obstruction theorems, with distinct exact arithmetic checks. Neither the weighted equation nor the full Beal conjecture is solved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-15. Remote input inspected: `79b63d464ce5fbd1295d5c65d931a6beb46920db` in private `Joe-Simo/beal`. The attached local U72 archive was restored additively and its distinct manuscript was read. No earlier mathematical checkpoint is replaced.

## 1. The result and the two U72 versions

The current remote U72 is `U72_root_closed_order_and_full_support.md`: its subject is the smaller order, all ten coefficients of the common root, and their exact divisibility profiles. The attached local U72 is `U72_common_root_constant_obstructions.md`: its subject is constant seventeenth-power tests modulo Z^17. They are different research continuations, not interchangeable filenames. Their source identifiers and preservation status are recorded separately in `references/U73/sources.json`.

The present theorem needs only the common-root conclusion of U71, not either U72 refinement. Starting from a hypothetical primitive positive solution of

    (W) X^10+256Y^10=Z^17,

that written/self-reviewed result supplies

    L=Q(rho,i), rho^5=2, rho>0,
    c=i*rho^4, c^10=-256,
    theta in O_L, theta^17=X+cY, and 289|Y.        (1.1)

U73 constructs a point on the fixed curve

    H: (3-phi)V^2 = 4U^17-phi^2,
       phi=(1+sqrt(5))/2.                          (1.2)

It proves three precise statements.

1. H has genus eight. The point forced by (1.1) lies in K=L(phi), and its coordinate field is **exactly K**, of degree twenty over Q and degree ten over Q(phi). In particular, computing only H(Q(phi)) cannot capture any point arising from positive X,Y in W.
2. The Jacobian of H is absolutely simple. H has no nonconstant map, even after extension to an algebraic closure in characteristic zero, to a smooth projective curve of genus one through seven. In particular H has no elliptic quotient.
3. The second coordinate has an additional required form V=R^17 with R in L and relative norm one. Retaining this condition gives an explicit degree-seventeen cover of H of genus 256. Arbitrary points on H(K) cannot be treated as weighted solutions.

These are a global reduction and two exclusions of proposed shortcuts. **No new integer solution range, prime class, or complete Beal signature is eliminated here.** No rank, complete point set, or effective upper height bound is computed. The genus-eight curve is a necessary target, not a certified parametrization equivalent to W.

## 2. The fields, with no hidden descent assumption

Let zeta be a primitive fifth root of unity, chosen so

    phi=1+zeta+zeta^(-1)=-zeta^2-zeta^3.

The last equality uses Phi_5(zeta)=0. It follows that phi^2=phi+1. Define

    F=Q(phi), K=L(phi), M=L(zeta).

The field Q(rho) has degree five by Eisenstein at 2. It is contained in R in the specified embedding, so adjoining i doubles its degree. Thus [L:Q]=10. Also

    rho=c^4/8, i=c^5/16,

so Q(c)=L.

The real quadratic field F cannot be contained in L: otherwise the distinct quadratic fields F and Q(i) would generate a biquadratic subfield of L, whose degree four cannot divide ten. Therefore

    L intersect F=Q, [K:Q]=20, [K:L]=2, [K:F]=10.   (2.1)

The cyclic quartic field Q(zeta) has unique quadratic subfield F. Its intersection with L is Q: a larger intersection would contain F, just ruled out. Since Q(zeta)/Q is Galois, these fields are linearly disjoint. Consequently

    [M:L]=4, [M:Q]=40, [M:K]=2.                   (2.2)

The involution of M that fixes L and sends zeta to zeta^(-1) has fixed field K. This involution must not be confused with complex conjugation on L, which sends c to -c.

## 3. The exact map from the common root

Write theta=p(c), with p a polynomial of degree at most nine over Q. Its coefficients need not be integral for this construction. For j modulo five put

    theta_j=p(c*zeta^j), tau_j=X+c*zeta^j*Y.

The assignment c -> c*zeta^j is an embedding of L into M: it sends c to another root of its irreducible polynomial. Hence

    theta_j^17=tau_j.

All theta_j are nonzero. Define

    U=theta_1*theta_(-1)/theta_0^2,
    V=(X-cY)/(X+cY).                               (3.1)

The zeta-inversion involution exchanges theta_1 and theta_(-1) and fixes theta_0. Thus U belongs to K; V belongs to L.

The elementary identity

    4(X+c*zeta*Y)(X+c*zeta^(-1)*Y)
      =(phi+1)(X+cY)^2+(3-phi)(X-cY)^2             (3.2)

holds identically. To check it, use zeta+zeta^(-1)=phi-1 and expand the three quadratic expressions. Dividing by the nonzero (X+cY)^2 and using phi+1=phi^2 gives exactly (1.2).

The affine equation is smooth: its defining polynomial has partial derivatives proportional to U^16 and V, and their simultaneous zero U=V=0 does not lie on the curve. For the smooth projective completion, the degree-two map to the U-line branches at the seventeen distinct roots of 4U^17-phi^2 and at infinity. Its eighteen simple branch points give

    2g(H)-2=2*(-2)+18=14,
    g(H)=8.                                        (3.3)

This is a fixed curve over F: its coefficients do not depend on X,Y,Z or theta.

## 4. The point has degree ten over F, not degree one

Positivity ensures X,Y are nonzero. In (3.1), V=1 would force Y=0 and V=-1 would force X=0. Neither is possible. The recovery identity

    c=X(1-V)/(Y(1+V))                              (4.1)

therefore holds. Since X/Y is rational, Q(V) contains c and hence equals L. The degree-ten polynomial

    X^10(1-V)^10+256Y^10(1+V)^10                    (4.2)

vanishes at V. It is irreducible over Q up to a nonzero scalar: (4.1) proves that V has degree ten, and (4.2) has degree ten with nonzero leading coefficient X^10+256Y^10. No sample factorization is substituted for this argument.

The curve equation can also be rearranged using phi^2=phi+1:

    (1-V^2)*phi=4U^17-1-3V^2.                      (4.3)

Since V^2 is not one, (4.3) recovers phi from U,V. As both coordinates already lie in K, (4.1) and (4.3) prove

    Q(U,V)=K.                                      (4.4)

In particular U is not in L: if it were, (4.3) would put phi in L, contradicting Section 2. Viewed as a point of a curve over F, its field is F(U,V)=K and its degree is ten.

This rules out the shortcut of attempting to prove H(F) consists only of boundary points and then applying that conclusion to W. Those hypothetical weighted points are not F-rational in the first place. The boundary points (U,V)=(1,1) and (1,-1) do belong to H(F); they correspond to the excluded zero-base cases in (3.1), not positive weighted solutions.

## 5. Why there is no elliptic or other smaller positive-genus quotient

Over an algebraic closure of F, rescale U and V by nonzero constants to obtain

    H_0: y^2=x^17-1.                               (5.1)

For instance take x=lambda*U with lambda^17=4/phi^2 and y=mu*V with mu^2=(3-phi)/phi^2. Thus geometric properties of its Jacobian can be assessed on H_0.

Let eta be a primitive **seventeenth**, not fifth, root of unity. The automorphism

    sigma(x,y)=(eta*x,y)

acts on the holomorphic differential basis

    x^(j-1) dx/y, j=1,...,8,

with eigenvalues eta^j. The conjugate part of first cohomology contributes eta^(-j). Therefore all sixteen nontrivial seventeenth roots occur, each once. The characteristic and minimal polynomials of this rational cohomology action are Phi_17.

The induced action on the Jacobian is faithful on rational first cohomology, so it embeds

    E=Q(eta) into End^0(Jac(H_0)), [E:Q]=16=2g.     (5.2)

The field polynomial is irreducible directly: Phi_17(T+1) is Eisenstein at 17. The finite-order automorphism preserves the canonical polarization, with Rosati sending it to its inverse. Its CM type, up to the harmless conjugate convention, is the set of exponents {1,2,...,8}.

The Galois group of E/Q is cyclic of order sixteen; 3 modulo 17 generates it. Every nontrivial subgroup of a cyclic group of order sixteen contains its unique involution, exponent -1 modulo 17. That involution is complex conjugation. It follows that **every proper subfield of E is totally real**. In particular E has no proper CM subfield, so the exhibited CM type is primitive. A second exact check enumerates its multiplicative stabilizer and obtains only the identity.

The external theorem used here is the CM classification: an abelian variety with a degree-2g CM field action is determined up to isogeny by its CM pair, and primitive CM pairs correspond to simple abelian varieties. Milne's Propositions 3.3, 3.12 and 3.13 supply these implications [S1]. Applying them to (5.2) proves that Jac(H_0), and hence Jac(H), is simple over C and absolutely simple in characteristic zero.

Now suppose H mapped nonconstantly to a smooth projective curve D of genus d, with 1<=d<=7. The map is finite. Pullback and pushforward on Jacobians compose to multiplication by its nonzero degree. Thus pullback has finite kernel, and its image is a positive-dimensional abelian subvariety of Jac(H) of dimension d<8. This contradicts absolute simplicity. The same argument works after any characteristic-zero field extension, since the proof is geometric.

The scope is important. The hyperelliptic map to genus zero still exists. Covers of H or other auxiliary curves may have additional Jacobian factors. This theorem does **not** forbid every possible elliptic method for W, and does not address reductions of this Jacobian in positive characteristic. It specifically excludes a lower positive-genus quotient of H, including one obtained merely by enlarging the number field.

This CM field Q(eta_17) is different from the Q(zeta_5) CM field of the older boundary genus-two curve. Nothing in this argument assumes the unproved boundary congruence.

## 6. Retaining the seventeenth-power condition produces a genus-256 cover

Let bar denote the automorphism of L fixing rho and sending i to -i, hence c to -c. The ratio

    R=bar(theta)/theta in L

satisfies

    R^17=V, R*bar(R)=1.                             (6.1)

The second identity is an actual relative norm-one condition, not an independently selectable sign or local root.

Consequently the image also lies on the fixed curve

    C: 4U^17-(3-phi)R^34=phi^2,                    (6.2)

mapping to H by (U,R) -> (U,R^17). The smooth projective normalization of C is geometrically connected and has genus 256. Here is a direct ramification calculation. On H, V has seventeen simple zeros, and its unique pole at infinity has order seventeen. Adjoining a seventeenth root of V gives a degree-seventeen extension because any simple zero prevents V from being a seventeenth power in the function field. Each of the seventeen zeros is fully ramified, while the pole order divisible by seventeen gives no ramification at infinity over an algebraic closure. Therefore

    2g(C)-2=17*(2*8-2)+17*(17-1)=510,
    g(C)=256.                                      (6.3)

Equivalently, project (6.2) to the R-line. Its right-hand polynomial for U^17 has 34 simple zeros and degree 34 divisible by 17, giving -2*17+34*16=510 again.

Because V=R^17 generates L, so does R. Equations (4.1) and (4.3) then also show Q(U,R)=K. This does not turn the cover point into an F-rational point.

Even (6.2) is not a sufficient condition for a weighted solution. One must recover the same global integral theta with theta^17=X+cY, positive rational-integer coprime X,Y, and the norm condition. At a minimum, the quotient point must obey V in L, R in L with (6.1), and

    (1-V)/(c*(1+V))=Y/X in Q_{>0}.                 (6.4)

Neither an arbitrary H(K) point nor an arbitrary C(K) point can be labeled a solution of W.

## 7. Executed local follow-up: the new reduction is not locally empty

The constructions are compatible with the known local disk at 17. To check this with the common root retained, take the three inputs

    X=1,Y=17^2;
    X=1,Y=17^3;
    X=2^17,Y=3*17^2.

These specify local tests, not integer solutions of W. Python constructs theta at precision 17^12 using the binomial series for (X+cY)^(1/17), with the supplied scalar root of X. If e=v_17(Y)>=2, the k-th term has valuation

    k(e-1)-v_17(k!) > k(e-1-1/16).

A cutoff derived from this inequality bounds every omitted term, not just the next coefficient. TypeScript instead starts at the scalar residue and lifts the power equation digit by digit; it computes one extra output digit to retain the root precision genuinely determined at 17.

Python forms theta_1*theta_(-1) in the full rank-forty cyclotomic algebra, then verifies that the result descends to the rank-twenty algebra K. TypeScript uses a different construction: pair the coefficient products and use the recurrence for zeta^j+zeta^(-j) in the basis 1,phi. Both calculate U,V,R and agree on all complete coefficient vectors, not just a zero/nonzero label. Each example satisfies the curve, power, norm-one and undivided recovery identities at the stated precision.

They also check the leading nontrivial quadratic part. Let U' be the conjugate over L. The first-order expansion gives

    U-U' = (2phi-1)*c*Y/(17X) modulo 17^e.          (7.1)

Indeed theta_j/x=1+c*zeta^j*Y/(17X) modulo 17^e; all terms of index at least two have valuation at least e. Thus U=1+(phi-3)cY/(17X) at that precision, and phi -> 1-phi gives (7.1). Its leading factor is a unit, so the exact valuation is e-1. This is consistent with the global non-descent proof in Section 4; it is not needed to replace that proof.

The derivative argument for the divided principal-unit equation gives roots at all higher 17-adic precisions. The finite examples corroborate the identities; they do not establish existence of a global theta or classify the curve's points. No contradiction was found in these disks.

## 8. Audit, reproducibility, and remaining work

The new code is `code/U73_genus_eight.py` and `code/U73_genus_eight.ts`. Python additionally checks (3.2), the recovery identities, smoothness polynomials and the Möbius polynomial symbolically. Both verify the cyclotomic group, primitive-type stabilizer and Riemann-Hurwitz arithmetic. These finite checks support the stated calculations; the field, geometric and CM inferences still require mathematical review beyond running code.

Wolfram independently corroborates the polynomial identities, degree, primitive-type stabilizer, corrected subgroup inventory, both genus calculations, and the first-order local curve identity. Its first subgroup expression accidentally omitted the mapped variable and returned only a length-sixteen list. That subgroup output and its vacuous boolean were rejected. A corrected explicit double Table returned all five subgroup orders 1,2,4,8,16. Both inputs and outputs are retained; the rejected portion is not reported as a successful check.

The new verifiers pass strict TypeScript checking, Python compilation/tabnanny, and complete-output comparison. The upstream U71 Python verifier was replayed into new logs; its entire mathematical output agrees with the copy retained in the attached constants-U72 archive. This is a replay of arithmetic, not independent expert certification of U71. The remote full-support U72 was inspected but not replayed or assumed as a premise of the new global reduction.

The audit checked both distinct involutions, the distinction between fifth and seventeenth roots of unity, the actual coordinate field rather than the field of the curve, excluded zero-base boundaries, nonconstant-map versus cover direction, geometric rather than only base-field simplicity, the seventeenth-power condition lost by projection, and the extra precision digit required at 17.

The next correct arithmetic target is the degree-ten-over-F points on this genus-eight curve, with their L-coordinate, norm, power and rational-ratio constraints, or an alternative global argument on the original common-root system. Its Mordell-Weil rank over K, a complete point classification, and an effective upper bound have not been established. The genus-256 cover may encode further structure, but its rational points are likewise unclassified. These are outstanding research tasks, not consequences already obtained.

No new height bound, impossible prime class, complete original-Beal exponent family, independent certification, or solution is claimed. U41 remains invalidated and the boundary congruence remains unproved. Separate coefficient-two work U61/U62 is not used.

### Sources

[S1] J.S. Milne, *Complex Multiplication*, v0.10 (2020-07-14), https://www.jmilne.org/math/CourseNotes/CM.pdf . Definition 1.8 and the primitive-type definition (printed p.11), Proposition 3.3 (p.27), Propositions 3.12–3.13 (p.30). The primary PDF text and page images for pp.11 and 30 were inspected. The field action and primitive-type verification specific to H are derived above.

[S2] U71, `U71_common_decic_seventeenth_root.md`, commit `229aba18da05b84501e9de3377b992e8013320c6`, blob `72f0941699d331450f2c17e818b79cc36747339e`. The weighted application inherits its common-root theorem. With (1.1) taken as an explicit hypothesis, the new reduction is separately assessable.

[S3] The two distinct U72 continuations and their exact source identifiers are listed in `references/U73/sources.json`. They establish continuity, not additional hypotheses. No literature search is treated as evidence of novelty or completeness, and no publication or prize claim is made.
