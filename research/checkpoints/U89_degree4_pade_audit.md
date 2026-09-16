# U89: degree-four fixed-weight Padé invariants have higher local order but a weaker certified height bound

**Status: written route audit with exact arithmetic. The weighted equation and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. This executes the next step identified in U88: test whether degree four improves the certified height obstruction after accounting for the actual size of the primitive integer relation, rather than comparing local vanishing order alone.

## 1. Scope of the audit

Keep U88's notation

    theta=sum_(j=0)^9 a_j c^j,
    a_j=x*T^j*F_j(T^10),
    c^10=-256,

at a strong prime dividing `Y`.

This checkpoint studies **fixed-weight homogeneous degree-four invariants**: linear combinations of monomials

    a_i a_j a_k a_l

with one fixed index sum `i+j+k+l=W`. It does not claim to exhaust every degree-four invariant mixing weights that differ by multiples of ten.

For fixed W, factor out `x^4*T^W` and view the remaining monomial products as rational power series in `S=T^10`. If a nonzero combination cancels the first `m` coefficients in S, its local Y-order is

    W+10m.                                           (1.1)

## 2. A modular scan gives rigorous upper bounds on cancellation

`code/U89_degree4_pade_audit.py` enumerates every degree-four monomial and every weight `0<=W<=36`. It reduces the exact binomial-product series modulo the prime 5003 and computes the first row count at which each fixed-weight coefficient matrix reaches full column rank.

A nonzero minor modulo 5003 is a nonzero integer minor. Therefore whenever the modular matrix has full column rank after k rows, no rational combination can cancel all of those k coefficients. The scan consequently provides a rigorous **upper bound** on the possible exact cancellation order; it is not merely heuristic modular evidence.

The unique best fixed-weight upper bound occurs at

    W=18,
    number of monomials=43,
    first full row count=43.                         (2.1)

Hence every non-identically-zero fixed-weight degree-four invariant has local order at most

    18+10*42=438.                                    (2.2)

## 3. The extremal order 438 is attained exactly

For `W=18`, construct the exact 42-by-43 rational coefficient matrix for `S^0,...,S^41`. Exact row scaling and nullspace arithmetic give

    rank=42,
    nullspace dimension=1.                           (3.1)

Let `lambda` be its primitive integer null-vector. The coefficient of `S^42` in the resulting series is nonzero, so the corresponding degree-four integer invariant `K` has exact formal order

    T^(18+420)=T^438.                                (3.2)

At the forced prime 31, the leading rational coefficient has

    numerator=20 mod31,
    denominator=3 mod31.                             (3.3)

Thus it is a 31-adic unit. Since U72 forces `31|Y`, the same nonvanishing argument as U87/U88 proves

    K !=0,
    v_31(K)=438*v_31(Y).                             (3.4)

For the fourteen-prime product

    P=433992707035920672833426144791,

one has

    P^438 | K.                                       (3.5)

## 4. Coefficient growth overwhelms the local-order gain

The primitive degree-four null-vector is much larger than U88's cubic vector:

    max coefficient digit length = 8817,
    L1 norm digit length = 8818.                     (4.1)

Every weight-18 monomial satisfies

    |a_i a_j a_k a_l| <= kappa^(-18) H^(4/17),

so with `L_4=sum |lambda_i|`,

    0<|K|<L_4 H^(4/17).                              (4.2)

Combining with (3.5), `H<3M`, and exact integer arithmetic gives only

    max(X,Y)>10^17696.                               (4.3)

The exact threshold checks are

    P^(438*17) >81 L_4^17 10^(4*17696),
    P^(438*17) <81 L_4^17 10^(4*17697).              (4.4)

Thus the degree-four fixed-weight invariant has far greater local order than U88's cubic invariant (`438` versus `155`) but a **weaker** final decimal barrier (`17696` versus `21122`) because its primitive coefficients grow by nearly eight thousand digits.

## 5. Independent exact check

The Python audit performs both the mod-5003 all-weight scan and the exact rational reconstruction at W=18. A separate Wolfram calculation rebuilt the W=18 matrix from the binomial series and returned

    monomial count 43,
    rank 42,
    L_4 digit length 8818,
    maximum lambda digit length 8817,
    leading residues 20 and 3 modulo 31,
    both exact threshold comparisons true.           (5.1)

No decimal approximation determines (4.3).

## 6. Research consequence

U89 shows that **local vanishing order alone is the wrong optimization target**. The relevant quantity is the tradeoff between q-adic order and the arithmetic height of the primitive coefficient relation.

U88 therefore remains the strongest certified explicit lower bound in this Padé family:

    max(X,Y)>10^21122.                               (6.1)

The next Padé step should allow weights differing by multiples of ten, because they contribute to the same `T`-residue class after extracting powers of `S=T^10`. That larger restriction space may achieve a better order/height tradeoff than the fixed-weight degree-four subspaces audited here. This is the next unresolved mathematical question; no weighted-equation elimination is claimed.
