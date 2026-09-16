# U88: a cubic Padé invariant pushes the weighted lower bound beyond 10^21122

**Status: written partial theorem with exact Python/SymPy arithmetic and independent Wolfram corroboration. The weighted equation and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. This continues U87's systematic Padé route. It uses the same fourteen forced prime divisors of `Y`, but replaces the quadratic invariant by a degree-three invariant with much larger local intersection multiplicity.

## 1. Setup

Assume a primitive positive solution

    X^10+256Y^10=Z^17.                               (W)

Keep U71/U72's common integral root

    c^10=-256,
    theta=a0+a1*c+...+a9*c^9 in Z[c],
    theta^17=X+cY.                                   (1.1)

Let

    kappa=|c|=2^(4/5),
    H=X+kappa Y,
    M=max(X,Y).

U72 forces the fourteen primes

    11,31,41,61,71,101,151,191,211,281,331,431,461,631

to divide `Y`; their product is

    P=433992707035920672833426144791.                (1.2)

All fourteen are U81-clean and hence belong to the scalar-root regime.

## 2. Fifteen cubic monomials of common weight fifteen

At a strong prime q dividing Y, put `T=Y/X` and `S=T^10`. As in U81/U87,

    a_j=x*T^j*F_j(S),
    F_j(S)=sum_(m>=0) B_(j+10m)(-256)^m S^m,
    B_n=binomial(1/17,n),
    x^17=X.                                          (2.1)

There are exactly fifteen degree-three monomials in the ten coefficients whose index sum is fifteen:

    a0*a6*a9,  a0*a7*a8,
    a1*a5*a9,  a1*a6*a8,  a1*a7^2,
    a2*a4*a9,  a2*a5*a8,  a2*a6*a7,
    a3^2*a9,  a3*a4*a8,  a3*a5*a7,  a3*a6^2,
    a4^2*a7,  a4*a5*a6,  a5^3.                      (2.2)

Every one has common local factor `x^3*T^15`.

Let `M_1(S),...,M_15(S)` be the corresponding products of three `F_j` series. Form the 14-by-15 rational matrix whose row n is the coefficient of `S^n` in these series for n=0,...,13.

Exact arithmetic gives

    rank = 14.                                       (2.3)

Therefore its nullspace is one-dimensional. Let

    lambda=(lambda_1,...,lambda_15) in Z^15           (2.4)

be the unique primitive integer generator, with its last coordinate positive. The largest coefficient has 866 decimal digits. This definition fixes the huge vector unambiguously without printing it into the manuscript; `code/U88_cubic_pade.py` reconstructs it exactly from (2.1)-(2.3).

Define

    G(S)=sum lambda_r M_r(S).                         (2.5)

By construction,

    [S^n]G=0  for n=0,...,13.                        (2.6)

The next coefficient is nonzero:

    C=[S^14]G !=0.                                   (2.7)

Thus

    G(S)=C*S^14+O(S^15).                             (2.8)

## 3. A nonzero integer invariant of local order 155

Let `J` be the same lambda-linear combination of the fifteen integer monomials in (2.2). Then

    J in Z.                                          (3.1)

Using (2.1) and (2.8), at any strong q with `e=v_q(Y)>0`,

    J=x^3*T^15*G(T^10)
     =x^3*C*T^155+terms of T-adic order at least 165. (3.2)

All `B_n` are q-integral for q!=17, hence

    v_q(J)>=155e.                                    (3.3)

If `Y_s` is the strong-prime part of Y,

    Y_s^155 | J.                                     (3.4)

### 3.1 Forced nonvanishing at q=31

As in U87, the forced prime 31 certifies that the global invariant is not zero. The exact leading coefficient C in (2.7), after reduction to lowest terms, satisfies

    numerator(C)=13 mod31,
    denominator(C)=20 mod31.                         (3.5)

Both are units. Since U72 forces `31|Y`, equation (3.2) gives

    v_31(J)=155*v_31(Y).                             (3.6)

Therefore

    J !=0.                                           (3.7)

All fourteen primes in (1.2) divide Y and are strong, so

    P^155 | J.                                       (3.8)

## 4. Archimedean height bound

Fourier inversion gives

    |a_j|<=kappa^(-j) H^(1/17).                      (4.1)

Every cubic monomial in (2.2) has total index fifteen. If

    L=sum |lambda_r|,                                (4.2)

then

    0<|J|<=L*kappa^(-15) H^(3/17)
           <L*H^(3/17).                              (4.3)

The exact `L` has 867 decimal digits and is computed directly from the primitive null-vector by the checker.

Combining (3.8) and (4.3),

    P^155 < L*H^(3/17).                              (4.4)

Because `H<X+2Y<=3M`, a hypothetical bound `M<=10^21122` would imply

    P^(155*17) < 27*L^17*10^(3*21122).               (4.5)

The exact integer computation gives the reverse strict inequality:

    P^(2635) > 27*L^17*10^(63366).                   (4.6)

The next decimal threshold goes the other way:

    P^(2635) < 27*L^17*10^(3*21123).                 (4.7)

Hence every primitive positive solution of (W) must satisfy

    max(X,Y) > 10^21122.                             (4.8)

At least one of the two bases therefore has **at least 21,123 decimal digits**.

This improves U87's `10^12155` barrier and U72's earlier `10^4810` barrier. It is still a lower bound, not a proof that no solution exists.

## 5. Exact audit

`code/U88_cubic_pade.py` uses Python `Fraction` for the binomial coefficients and row scaling, then SymPy's exact rational nullspace for the 14-by-15 matrix. It does not hard-code the 866-digit coefficients. The checker verifies

    monomial count = 15,
    matrix rank = 14,
    nullspace dimension = 1,
    S^0,...,S^13 coefficients = 0,
    S^14 coefficient !=0,
    numerator(C) mod31 =13,
    denominator(C) mod31 =20,
    local order =155,
    max |lambda_r| has 866 digits,
    L has 867 digits,
    P^2635 >27 L^17 10^(3*21122),
    P^2635 <27 L^17 10^(3*21123).

The same exact construction was replayed independently in Wolfram Language without importing the Python null-vector. Wolfram returned

    rank 14,
    L digit length 867,
    maximum lambda digit length 866,
    leading residues 13 and 20 modulo 31,
    both threshold comparisons true.

The computation deciding (4.8) uses integers and rationals only; no floating-point logarithm enters the certificate.

## 6. Research consequence

The Padé mechanism is now substantially stronger than the single-coefficient route: degree three achieves q-adic order 155 while its archimedean size grows only like `H^(3/17)`.

The next question is whether degree four produces a genuinely nonzero invariant after quotienting the exact algebraic relations among the coefficient functions. Preliminary modular linear algebra indicates that exact relations begin to appear in that degree, so simply counting monomials is no longer valid. The correct next step is to compute the degree-four restriction space, separate identically-zero relations from a maximal-order nonzero Padé class, and compare the resulting coefficient height against the gain in local order.
