# U84: a fixed pair-product discriminant captures every prime-to-170 divisor of Y

**Status: written partial theorem with an exact affine-orbit certificate and independent Wolfram corroboration. The weighted equation and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. This continues the weighted branch after U83. Unlike U81-U83, the theorem below does not discard a positive-density Frobenius complement: it packages all primes dividing Y outside 2,5,17 into one fixed nonzero discriminant attached to the hypothetical common root. The resulting height bound is not strong enough by itself to prove impossibility.

## 1. Setup and a twenty-element Galois orbit

Assume a primitive positive solution

    X^10+256Y^10=Z^17.

Retain

    c^10=-256, c^5=16i,
    theta=P(c) in Z[c],
    theta^17=X+cY.

Let zeta be a primitive tenth root of unity and write

    c_j=c*zeta^j,
    theta_j=P(c_j),  j in Z/10Z.

These are the ten conjugates of theta. The normal closure acts on j through the forty affine transformations

    j -> a*j+t,  a in {1,3,7,9}, t in Z/10Z.

On unordered pairs of labels this group has exactly three orbits, of sizes

    5, 20, 20,

corresponding respectively to cyclic distances `{5}`, `{1,3}`, and `{2,4}`. This is checked exactly in `code/U84_pair_product_orbit.ts` and independently in Wolfram.

Choose the twenty-element orbit

    O={ {j,k}: cyclic distance between j,k is 1 or 3 }.

For p={j,k} in O put

    beta_p=theta_j*theta_k.                            (1.1)

## 2. The twenty beta_p are globally distinct

Suppose

    theta_i theta_j = theta_k theta_l.

Raising to the seventeenth power and using theta_m^17=X+c_mY gives

    (X+c_iY)(X+c_jY)=(X+c_kY)(X+c_lY).

After cancelling the common X^2 term and dividing by cY,

    X A + cY B = 0,                                  (2.1)

where

    A=zeta^i+zeta^j-zeta^k-zeta^l,
    B=zeta^(i+j)-zeta^(k+l)

belong to Q(zeta).

Now c is not in Q(zeta). Indeed c^5=16i, whereas Q(zeta_10)=Q(zeta_5) has unique quadratic subfield Q(sqrt(5)) and does not contain i. If B were nonzero, (2.1) would put c in Q(zeta), impossible. Hence B=0, and then A=0. Equality of both sum and product of the two roots of unity implies

    {zeta^i,zeta^j}={zeta^k,zeta^l}.

Thus the unordered pairs are equal. In particular the twenty numbers beta_p for p in O are pairwise distinct.

## 3. A nonzero integer discriminant

Define

    Q_O(T)=product_(p in O) (T-beta_p).               (3.1)

The orbit O is stable under the full Galois group of the normal closure, so Q_O has rational coefficients. Every beta_p is an algebraic integer, hence

    Q_O(T) in Z[T].                                   (3.2)

Section 2 proves it is separable. Therefore its discriminant

    Delta_O=product_(p<r in O) (beta_p-beta_r)^2     (3.3)

is a fixed nonzero rational integer attached to the hypothetical solution.

This nonvanishing matters: using a discriminant that vanished identically would give no arithmetic information.

## 4. Every q-adic factor of Y outside 2,5,17 enters Delta_O twice

Let q be a rational prime outside {2,5,17} and let

    e=v_q(Y)>0.

Primitivity gives q not dividing X. The normal closure of T^10+256 is ramified only over 2 and 5, so q is unramified there. Fix a prime ideal Q above q.

For every p={j,k} in O,

    beta_p^17=(X+c_jY)(X+c_kY) = X^2 mod Q.          (4.1)

The residue field contains at most seventeen roots of T^17-X^2, but O contains twenty beta_p. Hence two distinct p,r in O satisfy

    beta_p=beta_r mod Q.                              (4.2)

Put u=beta_p and v=beta_r. Their seventeenth-power difference is

    u^17-v^17
      =Y * [ X(c_i+c_j-c_k-c_l)
              +Y(c_i c_j-c_k c_l) ],                 (4.3)

for the corresponding pairs. The bracket is integral, so

    v_Q(u^17-v^17) >= e.

Because u and v are Q-adic units and q is not 17,

    (u^17-v^17)/(u-v)

reduces to 17u^16 and is a Q-adic unit. Therefore

    v_Q(u-v) >= e.                                    (4.4)

The discriminant contains (u-v)^2, hence

    v_Q(Delta_O) >= 2e.

Since q is unramified and Delta_O is a rational integer, its Q-adic and q-adic valuations agree. Consequently

    q^(2e) | Delta_O.                                 (4.5)

Let

    Y_* = product_(q notin {2,5,17}) q^v_q(Y).

Applying (4.5) prime by prime gives the global divisibility theorem

    Y_*^2 | Delta_O.                                  (4.6)

This is an all-primes statement, not a density assertion and not a bounded search.

## 5. Height bound and its limitation

Let

    kappa=|c|=2^(4/5),
    H=X+kappa Y.

Every conjugate satisfies

    |theta_j| <= H^(1/17),

so

    |beta_p| <= H^(2/17),
    |beta_p-beta_r| <= 2 H^(2/17).

A degree-twenty discriminant has C(20,2)=190 squared differences. Therefore

    |Delta_O| <= (2 H^(2/17))^380
              = 2^380 H^(760/17).                   (5.1)

Combining with (4.6),

    Y_*^2 <= 2^380 H^(760/17),                       (5.2)

or equivalently

    Y_*^34 <= 2^6460 H^760.                          (5.3)

This is much weaker metrically than U83's high-power coefficient restrictions. Its value is structural: the previous density complement no longer represents primes that escape every fixed global invariant. All prime-to-170 support of Y is forced into one explicitly defined nonzero integer discriminant.

No contradiction follows because the discriminant itself can grow very rapidly with theta.

## 6. Exact finite audit

`code/U84_pair_product_orbit.ts` enumerates all 45 unordered pairs of ten labels under the forty affine transformations. A strict TypeScript 5.8.3 compile with

    --strict --noUncheckedIndexedAccess --noUnusedLocals --noUnusedParameters

and Node 22.16.0 execution returned

    pair orbit sizes: 5,20,20,
    distance classes: {5}, {1,3}, {2,4},
    chosen orbit size: 20 > 17,
    discriminant pair count: 190,
    squared difference count: 380,
    theta-magnitude exponent: 760.

An independently written Wolfram enumeration returned the same orbit sizes and distance classes. These finite checks support the Galois-orbit bookkeeping; they do not replace Sections 2-4.

## 7. Research consequence

The density approach has reached a natural stopping point. U83 gives much sharper valuations on a density-553/640 set through the fixed coefficients a9 and a5, while U84 shows that every remaining prime divisor of Y outside 2,5,17 is still captured by a fixed nonzero degree-twenty pair-product discriminant.

The next high-value question is whether the two size-twenty pair-product orbits produce discriminants whose common arithmetic factor can be bounded or identified more sharply than the individual height estimate (5.1). A second route is to return to U80's exact class-group bottleneck if a reliable class-group engine becomes available. Neither route currently yields an elimination of the weighted equation.
