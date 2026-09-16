# U87: a quadratic Padé invariant raises the weighted lower bound past 12,155 powers of ten

**Status: written partial theorem with exact TypeScript/Python arithmetic and independent Wolfram corroboration. The weighted equation and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. This continues U81-U86. It uses the same common integral seventeenth root and the fourteen forced prime divisors of `Y`, but replaces the single-coefficient height argument by a carefully chosen nonzero quadratic invariant.

## 1. Setup

Assume a primitive positive solution

    X^10+256Y^10=Z^17.                               (W)

Retain U71/U72's common root

    c^10=-256,
    theta=a0+a1*c+...+a9*c^9 in Z[c],
    theta^17=X+cY.                                   (1.1)

Let

    kappa=|c|=2^(4/5),
    H=X+kappa Y,
    M=max(X,Y).

U72 forces the fourteen distinct primes

    11,31,41,61,71,101,151,191,211,281,331,431,461,631

to divide `Y`. Their product is

    P=433992707035920672833426144791.                (1.2)

U81 verifies that all fourteen are clean; in particular their local seventeenth root is scalar.

## 2. Five weight-ten quadratic monomials

At any strong prime q dividing Y, put

    T=Y/X,  S=T^10.

The scalar-root expansion used in U81 is

    theta=x*sum_(n>=0) B_n(cT)^n,
    B_n=binomial(1/17,n),
    x^17=X.                                          (2.1)

Grouping powers with `c^10=-256` gives

    a_j=x*T^j*F_j(S),
    F_j(S)=sum_(m>=0) B_(j+10m)(-256)^m S^m.         (2.2)

Consider the five quadratic monomials whose coefficient indices sum to ten:

    a1*a9, a2*a8, a3*a7, a4*a6, a5^2.               (2.3)

Every one has the common factor `x^2*T^10`. Put

    G_0=F_1 F_9,
    G_1=F_2 F_8,
    G_2=F_3 F_7,
    G_3=F_4 F_6,
    G_4=F_5^2.                                       (2.4)

Exact rational linear algebra gives the primitive integer vector

    lambda_0=15798242183726487723872974980213975697091265396056,
    lambda_1=-249202890961784236021683574474477003603265904312448,
    lambda_2=1216292797751835710390793468584676049161821798713448,
    lambda_3=-2877403423806299594932394239043237544733898769276736,
    lambda_4=1894513509087467786381667797189625338402082189240825.

For

    G(S)=sum_(j=0)^4 lambda_j G_j(S),                 (2.5)

the coefficients of `S^0,S^1,S^2,S^3` vanish exactly, while the coefficient `C` of `S^4` is nonzero. Therefore

    G(S)=C*S^4+O(S^5).                               (2.6)

This is a Padé-type cancellation in the exact q-adic binomial series, not a numerical fit.

## 3. The global integer invariant and its local order

Define

    I = lambda_0*a1*a9
      + lambda_1*a2*a8
      + lambda_2*a3*a7
      + lambda_3*a4*a6
      + lambda_4*a5^2.                               (3.1)

Because all `a_j` and all `lambda_j` are integers,

    I in Z.                                          (3.2)

From (2.2)-(2.6), at every strong q with `e=v_q(Y)>0`,

    I=x^2*T^10*G(T^10)
     =x^2*C*T^50+terms of T-adic order at least 60.  (3.3)

All binomial coefficients are q-integral for q!=17. Hence

    v_q(I)>=50e.                                     (3.4)

In particular, if `Y_s` is the strong-prime part of Y,

    Y_s^50 | I.                                      (3.5)

### 3.1 Why I is definitely nonzero

A high-order invariant would be useless if it could vanish on the hypothetical solution. The forced prime `q=31` prevents that.

U72 forces 31|Y and U81 shows 31 is clean. The exact coefficient `C` in (2.6), reduced to lowest terms, has numerator and denominator both congruent to 19 modulo 31. Thus C is a 31-adic unit.

If `e=v_31(Y)`, equation (3.3) gives the exact valuation

    v_31(I)=50e.                                     (3.6)

Therefore

    I != 0.                                          (3.7)

This nonvanishing is a mathematical consequence of an already-forced prime, not an assumption based on the formal series.

Since every prime in (1.2) is strong and divides Y,

    P^50 | I.                                        (3.8)

## 4. Archimedean bound

The ten complex embeddings send c to ten equally spaced points of modulus kappa. Fourier inversion gives for every j

    |a_j| <= kappa^(-j) H^(1/17).                    (4.1)

Each product in (3.1) has total index ten, so

    |a_r a_(10-r)| <= kappa^(-10) H^(2/17).

Put

    L=sum |lambda_j|
     =6253210863791113815450412054272229911598159926939513.    (4.2)

Then

    0<|I| <= L*kappa^(-10)*H^(2/17)
            < L*H^(2/17).                            (4.3)

Together with (3.8),

    P^50 < L*H^(2/17).                               (4.4)

Because `1<kappa<2`,

    H=X+kappa Y < X+2Y <=3M.                         (4.5)

If `M<=10^12155`, equations (4.4)-(4.5) would imply after raising to the seventeenth power

    P^(850) < 9*L^17*10^(2*12155).                   (4.6)

The exact integer comparison goes in the opposite direction:

    P^(850) > 9*L^17*10^(2*12155).                   (4.7)

Therefore every hypothetical primitive positive solution of (W) must satisfy

    max(X,Y) > 10^12155.                             (4.8)

So at least one of X,Y has **at least 12,156 decimal digits**.

For calibration, the previous explicit lower bound in U72 was `max(X,Y)>10^4810`. U87 more than doubles the certified decimal-exponent barrier, but remains only a lower bound, not an impossibility proof.

## 5. Exact computation audit

`code/U87_quadratic_pade.ts` uses a normalized bigint rational implementation. It independently constructs `B_n` through n=49, the five product series in (2.4), and verifies

    coefficients S^0..S^3 of G: exactly zero,
    coefficient S^4: nonzero,
    numerator(C) mod31 = 19,
    denominator(C) mod31 = 19,
    gcd(lambda_0,...,lambda_4)=1,
    L as in (4.2),
    P^(850) > 9 L^17 10^(2*12155),
    P^(850) < 9 L^17 10^(2*12156).

The certificate was separately replayed with exact Python fractions. Wolfram independently returned

    {{0,0,0,0}, True, 19, 19, L, True, True}

for the four cancellations, nonzero leading coefficient, its two residues modulo 31, the L1 coefficient norm, and the two threshold comparisons.

No floating-point computation decides the theorem or the decimal threshold.

## 6. Research consequence

The most useful new fact is not merely the larger number in (4.8): nonlinear combinations of the ten integral root coefficients can have much higher forced q-adic order than any single coefficient while retaining very small archimedean degree.

This opens a systematic Padé/intersection-multiplicity route. The next task is to determine the maximal non-identically-zero vanishing order obtainable from low-degree homogeneous coefficient invariants, while preserving a forced-prime nonvanishing certificate such as q=31. If that order-to-degree ratio can grow enough without the invariant becoming an exact algebraic relation, the height obstruction could strengthen substantially; otherwise the calculation will expose the intrinsic ceiling of this route.
