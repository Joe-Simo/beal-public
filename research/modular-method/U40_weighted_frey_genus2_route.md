# U40: direct weighted Frey genus-2 route for U^5 + 8 V^5 = Z^17

Status: verified route construction and scope checkpoint only. This does not resolve Beal's conjecture and does not yet eliminate the weighted branch.

Date: 2026-09-14.

## 1. Active weighted equation

The valid Beal-derived branch is

    X^10 + 256 Y^10 = Z^17,

with gcd(X,Y)=1 and X,Z odd.

Set

    U = X^2,
    V = 2 Y^2.

Then

    U^5 + 8 V^5 = Z^17,

and gcd(U,V)=1 because X is odd and gcd(X,Y)=1.

This is a primitive generalized Fermat equation of signature (5,5,17) with fixed coefficients

    A=1, B=8, C=1.

Unlike the auxiliary unweighted Michaud-Jacobs problem studied in U26-U31, this is exactly the active weighted branch.

## 2. Applicable modern Frey construction

Martin Koutsianas et al., `Effective Darmon's program for the generalised Fermat equation` (arXiv:2504.01967, 2025), develops Frey hyperelliptic curves and 2-dimensional Galois representations for equations

    A a^r + B b^r = C c^p

with fixed prime r and varying prime p, including non-unit coefficients A,B,C.

For signature (r,r,p), the paper defines the Frey curve

    y^2 = sum_{k=0}^{(r-1)/2} c_k (ABab)^k x^(r-2k)
          + (AB)^((r-1)/2)(B b^r - A a^r),

where for r=5 the coefficients are c_0=1, c_1=-5, c_2=5.

Specializing r=5, A=1, B=8, a=U, b=V gives the explicit genus-2 curve

    C_{U,V}: y^2 = x^5 - 40 U V x^3 + 320 U^2 V^2 x
                     + 64(8 V^5 - U^5).

Its Jacobian J_{U,V} has real multiplication by

    K = Q(zeta_5)^+ = Q(sqrt(5)),

so a prime lambda above p=17 gives a 2-dimensional residual representation over K of the type required by the modular method.

## 3. Relevant theorem chain from the primary source

The paper's theorem chain for the (r,r,p) Frey Jacobians includes:

- Theorem 3.5: real multiplication by K=Q(zeta_r)^+.
- Theorems 5.5/5.6: modularity of the relevant compatible systems after the prescribed twists/local hypotheses.
- Propositions 5.19/5.20: explicit absolute-irreducibility criteria for residual representations.
- Theorem 5.23: level lowering to a parallel-weight-2 Hilbert newform over K with a level whose prime support can be made independent of the putative solution after the paper's prescribed local choices.

The source explicitly treats general fixed coefficients A,B,C; therefore the coefficient 8 in U^5+8V^5=Z^17 is built into the Frey construction rather than being silently discarded.

This is the key difference from the invalid U26-U31 scope jump.

## 4. Exact discriminant computation for the specialized genus-2 polynomial

Let

    f(x)=x^5 - 40 U V x^3 + 320 U^2 V^2 x + 64(8V^5-U^5).

Exact Wolfram computation gives

    Disc_x(f)
      = 2^24 * 5^5 * (U^10 - 48 U^5 V^5 + 64 V^10)^2.

The moving factor is

    U^10 - 48 U^5 V^5 + 64 V^10
      = (U^5 + 8V^5)^2 - 64 U^5 V^5
      = Z^34 - 64 U^5 V^5.

Over Q(sqrt(2)) it factors as

    -(U^5 + (-24+16 sqrt(2))V^5)
      (-U^5 + (24+16 sqrt(2))V^5).

This raw curve discriminant has moving prime support, so one must use the paper's Galois-representation conductor and level-lowering analysis rather than infer a fixed level from the naive hyperelliptic discriminant.

## 5. Favorable 2-adic shape

For the paper's parameter

    s_0 = U^5 / Z^17,

we have

    s_0 - 1 = -8 V^5 / Z^17.

Since U and Z are odd and V=2Y^2 is even,

    v_2(s_0)=0,
    v_2(s_0-1)=3+5 v_2(V) >= 8.

Hence the local 2-adic parameter lies in the paper's positive/favorable case (the table condition denoted nu_2>0 for the relevant model), rather than in a delicate negative-valuation branch.

This is an exact consequence of the Beal-derived parity, not an extra assumption.

## 6. Differential identity from the Gaussian route

The previous cyclotomic route remains useful auxiliary information. With the U15-U39 polynomials g,h,J in t=(b/a)^2, exact Wolfram computation gives

    h(t) = g(t) - (2/17)(1+t) g'(t),

and therefore

    h(t)-17g(t)=32t J(t),

equivalently

    J(t)=-(136g(t)+(1+t)g'(t))/(272t).

Thus J-primes are critical-point primes for the polynomial/rational function structure inherited from the 17th Gaussian power. This does not itself solve the branch, but the local restrictions from U37-U39 can be retained for later newform elimination or local image arguments on the weighted Frey representation.

## 7. What is verified and what is not

Verified here:

1. The active weighted equation is exactly an instance A a^5+B b^5=C c^17 with (A,B,C)=(1,8,1).
2. The 2025 Darmon-program paper explicitly allows non-unit fixed coefficients and supplies a Frey genus-2 construction for this signature.
3. The specialized curve equation above follows exactly from the source formula.
4. Its polynomial discriminant was computed exactly.
5. The base RM field is Q(sqrt(5)).
6. The 2-adic parity of the Beal-derived solution lands in a favorable local case.

Not yet verified:

1. The exact specialized twists delta_Q and delta_K needed for the preferred plus/minus model.
2. The exact lowered ideal N^± for (A,B,C,r,p)=(1,8,1,5,17), prime by prime.
3. Which of Propositions 5.19/5.20 gives unconditional residual irreducibility in this exact specialization, or whether an additional local lemma is needed.
4. The complete Hilbert newform space over Q(sqrt(5)) at the resulting lowered level.
5. Elimination of every candidate newform.

No case of the weighted equation is declared eliminated until those items are proved.

## Next obligation

Specialize Theorem 5.23 and Tables 2/3 completely for A=1,B=8,C=1,r=5,p=17, producing the exact finite lowered level(s) over Q(sqrt(5)). Then enumerate the corresponding parallel-weight-2 Hilbert newforms and compare their residual mod-17 traces against the Frey representation using small primes compatible with the local restrictions already obtained in U37-U39.
