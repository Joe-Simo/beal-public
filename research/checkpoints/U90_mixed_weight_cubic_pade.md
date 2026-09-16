# U90: mixed-weight cubic Padé cancellation pushes the weighted lower bound beyond 10^25993

**Status: written partial theorem with exact integer/rational computation and independent Wolfram corroboration. The weighted equation and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. This executes U89's next step: allow homogeneous monomials whose index weights differ by multiples of ten, because `c^10=-256` makes those terms live in the same local `T`-residue class after extracting powers of `S=T^10`.

## 1. Setup

Assume a primitive positive solution

    X^10+256Y^10=Z^17.                               (W)

Retain

    c^10=-256,
    theta=sum_(j=0)^9 a_j c^j in Z[c],
    theta^17=X+cY.                                   (1.1)

At a strong prime q dividing Y, write

    T=Y/X,
    S=T^10,
    a_j=x*T^j*F_j(S),
    F_j(S)=sum_(m>=0) B_(j+10m)(-256)^m S^m,
    B_n=binomial(1/17,n),
    x^17=X.                                          (1.2)

As before let

    P=433992707035920672833426144791                 (1.3)

be the product of the fourteen U72-forced primes, all of which lie in the strong scalar-root family.

## 2. The full cubic residue-nine space

Consider every degree-three coefficient monomial

    a_i a_j a_k, 0<=i<=j<=k<=9,

whose total index is congruent to 9 modulo 10. There are exactly twenty-two. Their actual index sums are 9 or 19.

For a monomial of weight `W=9+10h`, equation (1.2) gives

    a_i a_j a_k
      =x^3*T^9*S^h*F_i(S)F_j(S)F_k(S).              (2.1)

Thus all twenty-two monomials live in one common series space after factoring only `x^3*T^9`. This is the mixed-weight enlargement omitted from U88/U89.

Let `M_1(S),...,M_22(S)` denote those twenty-two shifted product series. Form the exact 21-by-22 coefficient matrix for powers

    S^0,S^1,...,S^20.                                (2.2)

Its rank is 21. Let `lambda in Z^22` be the unique primitive integer null-vector, normalized by positive last coordinate. Then

    G(S)=sum lambda_r M_r(S)                          (2.3)

satisfies

    [S^n]G=0 for n=0,...,20.                         (2.4)

The next coefficient is nonzero:

    C=[S^21]G !=0.                                   (2.5)

Consequently

    G(S)=C*S^21+O(S^22).                             (2.6)

## 3. A nonzero cubic integer invariant of local order 219

Use the same `lambda` on the corresponding twenty-two integer coefficient monomials and call the resulting integer `J_9`. Then

    J_9 in Z.                                        (3.1)

Equations (2.1) and (2.6) give, for every strong q with `e=v_q(Y)>0`,

    J_9=x^3*T^9*G(T^10)
       =x^3*C*T^219+terms of T-adic order at least 229. (3.2)

Hence

    v_q(J_9)>=219e.                                  (3.3)

If `Y_s` is the strong-prime part of Y,

    Y_s^219 | J_9.                                   (3.4)

### 3.1 Forced nonvanishing

The leading coefficient C is a 31-adic unit. The exact reduced fraction satisfies

    numerator(C)=22 mod31,
    denominator(C)=21 mod31.                         (3.5)

Since U72 forces `31|Y`, equation (3.2) yields

    v_31(J_9)=219*v_31(Y).                           (3.6)

Thus

    J_9 !=0.                                         (3.7)

All fourteen primes in P divide Y and are strong, so

    P^219 | J_9.                                     (3.8)

## 4. Height bound

Let

    kappa=2^(4/5),
    H=X+kappa Y,
    M=max(X,Y).

Fourier inversion gives

    |a_j|<=kappa^(-j)H^(1/17).                       (4.1)

The twenty-two monomials have total weight 9 or 19, so each is bounded by

    |a_i a_j a_k|<=kappa^(-9)H^(3/17)<H^(3/17).     (4.2)

Let

    L=sum |lambda_r|.                                (4.3)

The exact primitive relation has

    max lambda digit length=1903,
    L digit length=1904.                             (4.4)

Therefore

    0<|J_9|<L*H^(3/17).                              (4.5)

Together with (3.8),

    P^219<L*H^(3/17).                                (4.6)

Since `H<X+2Y<=3M`, a hypothetical `M<=10^25993` would imply

    P^(219*17)<27*L^17*10^(3*25993).                 (4.7)

The exact integer certificate gives the reverse inequality, while the next threshold reverses back:

    P^(3723)>27*L^17*10^(3*25993),
    P^(3723)<27*L^17*10^(3*25994).                   (4.8)

Hence any primitive positive solution of (W) must satisfy

    max(X,Y)>10^25993.                               (4.9)

At least one base must therefore contain **at least 25,994 decimal digits**.

This is stronger than U88's `10^21122` lower bound. It is still not a proof of nonexistence.

## 5. Exact audit

`code/U90_mixed_weight_cubic_pade.py` reconstructs the twenty-two monomials, shifts the weight-19 series by one power of S, row-scales the first twenty-one rational coefficient equations to primitive integer rows, and computes the exact integer nullspace using SymPy's `DomainMatrix` over `ZZ`.

It verifies

    total degree-three monomials=220,
    residue-nine monomials=22,
    actual weights={9,19},
    nullspace dimension=1,
    S^0,...,S^20 cancellations exact,
    S^21 coefficient nonzero,
    local Y-order=219,
    maximum lambda length=1903 digits,
    L length=1904 digits,
    leading residues mod31=(22,21),
    both decimal-threshold inequalities in (4.8).

A separate Wolfram calculation rebuilt the mixed-weight series and nullspace from scratch. It returned

    {22,21,{9,19},1904,1903,22,21,True,True},

corresponding respectively to monomial count, matrix rank, actual weights, L digits, maximum coefficient digits, the two leading residues modulo 31, and the two exact threshold comparisons.

No floating-point estimate enters the theorem.

## 6. Research consequence

Allowing weights separated by ten materially improves the order/height tradeoff: the cubic local order rises from U88's 155 to 219, while the primitive coefficient height grows enough to leave a net improvement from `10^21122` to `10^25993`.

The natural next step is now the **full degree-four residue-class space**, not another fixed-weight slice. Preliminary modular arithmetic shows those spaces are much larger, so exact algebraic relations and primitive-vector height must be handled carefully. The key criterion remains the final certified decimal bound, not vanishing order alone.
