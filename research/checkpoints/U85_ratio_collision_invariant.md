# U85: ninety conjugate ratios force a 390-fold all-prime support invariant

**Status: written partial theorem with exact combinatorial certificate and independent Wolfram corroboration. The weighted equation and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. This strengthens U84 by replacing twenty pair products with all ninety ordered ratios of distinct conjugates. The price is clearing denominators by cross multiplication; the benefit is a much larger forced collision multiplicity at every prime dividing Y outside 2,5,17.

## 1. Setup

Assume a primitive positive solution

    X^10+256Y^10=Z^17.

Use U71/U72's integral common root

    c^10=-256, c^5=16i,
    theta=P(c),
    theta^17=X+cY,
    Norm_(L/Q)(theta)=Z,

where L=Q(c) has degree ten. Let zeta be a primitive tenth root and put

    c_j=c*zeta^j,
    theta_j=P(c_j),   j in Z/10Z.

Every theta_j is nonzero.

For each ordered pair i!=j define

    r_(i,j)=theta_i/theta_j.                          (1.1)

There are 10*9=90 such ratios.

## 2. All ninety ratios are globally distinct

Suppose

    theta_i/theta_j = theta_k/theta_l

with i!=j and k!=l. Cross multiplication gives

    theta_i theta_l = theta_k theta_j.                (2.1)

Raise to the seventeenth power. As in U84,

    X A + cY B=0,                                    (2.2)

where

    A=zeta^i+zeta^l-zeta^k-zeta^j,
    B=zeta^(i+l)-zeta^(k+j)

belong to Q(zeta_10).

Since c^5=16i and Q(zeta_10)=Q(zeta_5) does not contain i, one has c notin Q(zeta_10). Equation (2.2) therefore forces A=B=0. Equality of the sum and product of the two roots of unity says that the multisets

    {i,l} and {k,j}

coincide modulo 10. One possibility gives i=k and l=j, hence the original ordered pairs agree. The swapped possibility would give i=j, contradicting i!=j. Thus all ninety r_(i,j) are distinct.

## 3. A nonzero integral cross-difference invariant

Let R be the set of ninety ordered pairs (i,j), i!=j. For two distinct elements alpha=(i,j), beta=(k,l), define

    D_(alpha,beta)=theta_i theta_l-theta_k theta_j.   (3.1)

Section 2 proves every D_(alpha,beta) is nonzero. Define

    C_theta = product_{ {alpha,beta} subset R }
                D_(alpha,beta)^2,                    (3.2)

where the product is over the C(90,2)=4005 unordered pairs of distinct ratio labels.

The normal-closure Galois group permutes R. Squaring removes the sign from exchanging alpha and beta, so the complete product is Galois invariant. Every factor is an algebraic integer. Hence

    C_theta is a nonzero integer.                    (3.3)

It is the numerator-cleared analogue of the discriminant of the ninety ratios; no denominator integrality is assumed.

## 4. Every prime-to-170 part of Y enters C_theta to exponent at least 390

Let q notin {2,5,17} and let e=v_q(Y)>0. Primitivity implies q does not divide X or Z: if q divided Y and Z, the weighted equation would force q to divide X.

Fix a prime Q of the normal closure above q. Since Norm(theta)=Z and every theta_j is integral, q not dividing Z makes all theta_j Q-adic units. Thus every ratio (1.1) is a Q-adic unit.

Moreover

    r_(i,j)^17=(X+c_iY)/(X+c_jY) = 1 mod Q.          (4.1)

Therefore the ninety ratio residues occupy at most the seventeen roots of T^17-1.

If the nonempty residue classes have multiplicities m_1,...,m_s, then s<=17 and sum m_i=90. The quantity

    sum binomial(m_i,2)

is minimized by balancing the occupancies as evenly as possible. Since

    90=5*17+5,

five classes have size six and twelve have size five in the minimizing configuration. Hence there are at least

    5*binomial(6,2)+12*binomial(5,2)
      =75+120
      =195                                             (4.2)

unordered pairs of distinct ratio labels that collide modulo Q.

For one such collision alpha=(i,j), beta=(k,l), put

    u=theta_i theta_l,
    v=theta_k theta_j.

Then u=v mod Q. Also

    u^17-v^17
      =Y * [ X(c_i+c_l-c_k-c_j)
              +Y(c_i c_l-c_k c_j) ].                 (4.3)

The bracket is integral, so v_Q(u^17-v^17)>=e. Since u is a Q-adic unit and q!=17,

    (u^17-v^17)/(u-v)

reduces to 17u^16 and is a unit. Thus

    v_Q(D_(alpha,beta))=v_Q(u-v)>=e.                 (4.4)

There are at least 195 distinct colliding unordered ratio pairs, and each corresponding factor is squared in C_theta. Consequently

    v_Q(C_theta)>=390e.                              (4.5)

The normal closure is unramified at q because its ramification is supported over 2 and 5. Since C_theta is rational, v_Q(C_theta)=v_q(C_theta). Therefore

    q^(390e) | C_theta.                              (4.6)

Writing

    Y_* = product_(q notin {2,5,17}) q^v_q(Y),

we obtain the all-primes divisibility theorem

    Y_*^390 | C_theta.                               (4.7)

This is independent of Frobenius density and covers the seven residual classes left outside U83 as well as all previously controlled classes.

## 5. Global height bound

Put

    kappa=|c|=2^(4/5),
    H=X+kappa Y.

Each conjugate satisfies

    |theta_j|<=H^(1/17).

Hence every cross difference in (3.1) satisfies

    |D_(alpha,beta)|
      <= |theta_i theta_l|+|theta_k theta_j|
      <= 2 H^(2/17).                                 (5.1)

There are 4005 squared factors, so

    |C_theta|
      <= (2 H^(2/17))^8010
      =2^8010 H^(16020/17).                          (5.2)

Combining (4.7) and (5.2),

    Y_*^390 <= 2^8010 H^(16020/17).                  (5.3)

Raise to the seventeenth power and simplify the common factor 30 in the exponents:

    Y_*^221 <= 2^4539 H^534.                         (5.4)

This is substantially stronger than U84's pair-product-discriminant height inequality, but its exponent of H still exceeds its exponent of Y_*. It therefore does not contradict the existence of a large solution.

## 6. Exact audit

`code/U85_ratio_collision.ts` contains no floating-point arithmetic. It verifies

    ordered ratios: 90,
    residue values: at most 17,
    minimizing occupancies: five 6s and twelve 5s,
    minimum collision pairs: 195,
    valuation multiplier after squaring: 390,
    unordered ratio comparisons: 4005,
    squared cross-difference factors: 8010,
    theta-magnitude exponent: 16020,
    simplified inequality exponents: 221,4539,534.

The file was compiled before preservation with TypeScript 5.8.3 using

    --strict --noUncheckedIndexedAccess --noUnusedLocals --noUnusedParameters

and executed with Node 22.16.0. An independently written Wolfram arithmetic check returned

    {5,5,195,390,8010,16020,30,{221,534,4539}},

corresponding to the same balanced-occupancy and exponent calculation.

The finite checks certify the combinatorics and arithmetic only. Distinctness, integrality, local-unit status and the valuation transfer are proved in Sections 2-4.

## 7. Research consequence

U85 eliminates the remaining density complement as a support-classification issue: every prime divisor of Y away from 2,5,17 contributes with exponent at least 390 times its Y-valuation to one fixed nonzero global integer C_theta.

What remains is a height-strength problem, not a missing-prime problem. The current bound (5.4) is too weak to force a contradiction because C_theta contains 8010 cross-difference factors. A useful continuation would need a lower-degree Galois-invariant collision certificate, or an arithmetic relation causing substantial cancellation/factorization of C_theta. The independent U80 Selmer/class-group route remains open as well.
