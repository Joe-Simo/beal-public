# U86: the coefficient-support and all-prime collision mechanisms also control X

**Status: written partial theorem with an exact TypeScript certificate and Wolfram algebra corroboration. The weighted equation and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. This is the X-side counterpart of U81-U85. It uses only the recorded common-root theorem and the same fixed Frobenius partition; it does not assume any symmetry of the original weighted equation.

## 1. Setup

Assume a primitive positive solution

    X^10+256Y^10=Z^17.

Retain

    c^10=-256,
    theta=sum_(j=0)^9 a_j c^j in Z[c],
    theta^17=X+cY,

with all ten a_j nonzero. Let kappa=|c|=2^(4/5) and H=X+kappa Y.

For q not in {2,5,17}, write e=v_q(X)>0. Then q does not divide Y. The key normalization is

    (c^3)^17=c^51=(-256)^5 c.                       (1.1)

Thus, whenever x^17=Y/(-256)^5 in Q_q, the element x*c^3 is a seventeenth root of cY.

The strong/semi-strong/weak Frobenius families are exactly those defined in U82/U83; their disjoint densities are

    529/640, 8/640, 16/640,

with residual density 87/640.

## 2. Strong primes force the ninth power of the X-part into a4

Let q be strong. In the U81-clean cases the seventeenth-power map on the residue root algebra is injective, so the reduction of theta is the unique root of cY. Since 17 does not divide q-1, Y/(-256)^5 has a unique scalar seventeenth root x and

    theta = x*c^3 mod q.

For the additional strong family q=1 mod17 with irreducible degree-ten root algebra, the same scalar conclusion holds: Q_q contains the seventeenth roots of unity, and a seventeenth root of the scalar Y/(-256)^5 inside an extension of degree ten would generate a Kummer subextension of degree dividing both 17 and 10, hence degree one. Any remaining root-of-unity factor is already scalar.

Lift x q-adically and set delta=x*c^3. Then delta^17=cY and theta/delta is 1 modulo q. Therefore

    theta=x*c^3*sum_(n>=0) B_n (X/(cY))^n,
    B_n=binomial(1/17,n).                            (2.1)

Grouping powers modulo ten, the c^4 coefficient begins at n=9:

    a4=x*sum_(m>=0) B_(9+10m)(-256)^(-m-1)
                 (X/Y)^(9+10m).                     (2.2)

The exact leading numerator is

    B_9=658767450/17^9.

For q outside 2,5,17 its q-adic valuation is at most one, while every tail term has valuation at least 19e. Hence

    v_q(a4)=9e+v_q(658767450)>=9e.                  (2.3)

Thus if X_s denotes the strong-prime part of X,

    X_s^9 | a4.                                      (2.4)

## 3. Semi-strong primes force fourth powers into a4 and a9

Let q be semi-strong. Apply the same normalization by c^3. U82's local-field argument says that the root-of-unity ambiguity belongs to

    Q_q+Q_q*c^5=Q_q(i).

Hence the exact root delta of cY matching theta modulo q lies in

    span_Qq{c^3,c^8}.                                (3.1)

In the expansion

    theta=delta*sum_(n>=0)B_n(X/(cY))^n,

reaching coefficient c^4 from c^3 requires n=9 mod10, while reaching it from c^8 requires n=4 mod10. Thus every contribution to a4 contains at least X^4. The same calculation for c^9 has first indices 4 and 9. Consequently

    q^(4e) | a4,
    q^(4e) | a9.                                     (3.2)

If X_m is the semi-strong part,

    X_s^9 X_m^4 | a4.                               (3.3)

## 4. Weak primes force their X-part into a8

Let q be weak: q=1 mod17, the affine Frobenius has odd translation, and its cycle is not one of the already-strong 10-cycles.

Normalize the local root as

    delta=x*c^3*epsilon,

where x is scalar and epsilon is a seventeenth root of unity in each residue factor. Since q=1 mod17, Frobenius fixes all seventeenth roots of unity, so epsilon is constant on each Frobenius orbit of the ten root labels.

Odd translation flips the parity of every label. Every orbit therefore contains equally many even and odd labels. Fourier inversion gives zero c^5 coefficient for epsilon. Multiplication by c^3 says precisely that

    coefficient of c^8 in delta = 0.                 (4.1)

In the binomial expansion of theta around delta, the n=0 contribution to a8 is therefore absent and every remaining term contains at least one factor X. Hence

    q^e | a8.                                        (4.2)

Writing X_w for the weak-prime part,

    X_w | a8.                                        (4.3)

Thus the same density-553/640 union that controls Y also controls X, through shifted coefficients.

## 5. Global X-support height inequalities

Fourier inversion on the ten complex embeddings gives

    |a4|<=kappa^(-4) H^(1/17),
    |a8|<=kappa^(-8) H^(1/17).                       (5.1)

From Sections 2-4,

    kappa^68 X_s^153 X_m^68 <= H,                   (5.2)
    kappa^136 X_w^17 <= H.                           (5.3)

In particular

    X_s^153 X_m^68 < X+2Y,
    X_w^17 < X+2Y.                                   (5.4)

These are the direct X-side analogues of U83's Y-side inequalities. They do not force a specific integer to possess primes in any one density class.

## 6. An all-prime invariant for the remaining X support

The U85 ratio construction can also be normalized integrally on the X side. For each conjugate put

    psi_j=c_j^7*theta_j.                              (6.1)

This is integral. Since 7*17+1=120,

    psi_j^17
      =(-256)^11 X c_j^9 + (-256)^12 Y.              (6.2)

Hence for q not in {2,5,17} with q|X,

    psi_j^17 = (-256)^12 Y mod q,                    (6.3)

independently of j. Also q does not divide Norm(psi)=256^7 Z, so all psi_j are q-adic units.

The ninety ordered ratios psi_i/psi_j, i!=j, are globally distinct. Indeed equality of two such ratios gives after taking seventeenth powers

    X A+cY B=0

with A,B in Q(zeta_10), after cancellation of the common powers of the root labels. As in U84/U85, c notin Q(zeta_10), so the sum-and-product argument forces equality of the ordered pairs.

Define C_psi by multiplying the squared cross differences

    (psi_i psi_l-psi_k psi_j)^2

over all C(90,2)=4005 pairs of distinct ratio labels. The same Galois-invariance and integrality argument as U85 gives a nonzero integer.

At a prime q|X outside 2,5,17, the ninety ratio residues satisfy T^17=1, so the balanced pigeonhole count again supplies at least 195 colliding pairs. The derivative quotient is a q-adic unit, and each collision contributes at least e=v_q(X) before squaring. Therefore, for

    X_* = product_(q notin {2,5,17}) q^v_q(X),

one has

    X_*^390 | C_psi.                                 (6.4)

The height estimate now carries only a fixed power of kappa:

    |C_psi| <= (2*kappa^14*H^(2/17))^8010.           (6.5)

This is a genuine all-primes X-support invariant, but as on the Y side its height exponent is too large to force a contradiction.

## 7. Exact audit

`code/U86_symmetric_x_support.ts` was compiled under TypeScript 5.8.3 with

    --strict --noUncheckedIndexedAccess --noUnusedLocals --noUnusedParameters

and executed with Node 22.16.0. It returned

    category counts 529,8,16,87,
    3*17=51 == 1 mod10,
    7*17+1=120 == 0 mod10,
    semi-strong first indices for a4,a9: 4,4,
    weak first index for a8 after d8=0: 1,
    ratio collision lower bound: 195,
    all-prime valuation multiplier: 390.

Wolfram separately checked the exponent congruences and the relevant exact binomial numerator data. The finite certificate does not replace the local-field and Fourier arguments above.

## 8. Research consequence

U86 removes an asymmetry in the support program: both coprime bases X and Y now have density-553/640 high-power coefficient restrictions and separate fixed all-prime collision invariants.

This still does not solve the weighted equation because a density statement does not constrain the support of an individual integer, while the all-prime ratio invariants grow too rapidly with H. The next useful route is to combine the simultaneous X- and Y-side coefficient bounds with the coprimality and norm equation, looking for a shared low-height invariant; in parallel, U80's class-group/Selmer bottleneck remains unresolved.
