# U80: a density-105/128 coefficient-support theorem for the weighted branch

**Status: written partial theorem with an exact finite group certificate and independent Wolfram corroboration. The weighted equation and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. The private repository was inspected through U79 before this continuation. U41 remains invalidated by U63. U65/U71/U72 are used only at their stated written/self-reviewed level.

## 1. Scope

Assume a primitive positive solution of the active weighted equation

    X^10 + 256 Y^10 = Z^17.                           (W)

U71/U72 provide

    L=Q(c), c^10=-256,
    theta=a0+a1*c+...+a9*c^9 in Z[c],
    theta^17=X+cY,
    a9 != 0.                                          (1.1)

U72 proved exact divisibility profiles at fourteen already-forced primes. The purpose here is different: isolate an **infinite, positive-density set of rational primes** at which every prime divisor of Y necessarily contributes its full ninth power to a9.

This is still a necessary-condition theorem. An integer can avoid a positive-density set of primes, so the density statement is not an impossibility proof.

## 2. Clean primes

For a rational prime q not in {2,5,17}, factor

    T^10+256 mod q = product_i f_i(T)

into distinct irreducibles of degrees d_i. Call q **clean** when

    17 does not divide q^(d_i)-1 for every i.         (2.1)

Equivalently, the finite etale algebra

    A_q = F_q[T]/(T^10+256)

has no nontrivial seventeenth root of unity. Indeed

    |A_q^*| = product_i (q^(d_i)-1).

### Theorem 1

If q is clean and q^e exactly divides Y, then

    v_q(a9) = 9e + v_q(658767450) >= 9e.             (2.2)

Consequently, if

    Y_clean = product_{q clean} q^(v_q(Y)),

then

    Y_clean^9 divides a9.                             (2.3)

### Proof

Because gcd(X,Y)=1, q does not divide X. Reducing theta^17=X+cY modulo q gives

    theta^17 = X in A_q.

Cleanliness says the seventeenth-power map on A_q^* is injective. Since 17 does not divide q-1, X has a unique scalar seventeenth root x modulo q. Hence theta is congruent to x modulo q.

The derivative 17*x^16 is a q-adic unit, so the same root lifts uniquely in the q-adic completion. Therefore the actual theta is represented by the convergent binomial series

    theta = x * sum_{k>=0} B_k (cY/X)^k,
    B_k = binomial(1/17,k).                           (2.4)

For q != 17 the coefficients B_k are q-adically integral. Grouping powers with c^10=-256 gives

    a9 = x * sum_{m>=0} B_(9+10m) (-256)^m
                    (Y/X)^(9+10m).                   (2.5)

The leading coefficient is the exact reduced rational number already checked in U72,

    B_9 = 658767450 / 17^9,
    658767450 = 2*3*5^2*11*59*67*101.               (2.6)

Thus the leading term has q-adic valuation `9e+v_q(658767450)`, at most `9e+2`. Every tail term has valuation at least `19e`, because all B_k are q-integral and q is odd. Since `9e+2<19e` for e>=1, the leading term cannot cancel. This proves (2.2), hence (2.3).

No finite search or heuristic root choice is used in this argument.

## 3. Exact density of the clean primes

Let S be the splitting field of T^10+256. Put rho^5=2 and choose c=i*rho^4. Then

    c^10=-256,
    c^4=8rho,
    c^5=16i.

The ten roots are c*zeta_10^j. Hence

    S=Q(rho,zeta_5,i).                                (3.1)

The splitting field Q(rho,zeta_5) of T^5-2 has degree 20 and Galois group C5 semidirect C4. Its unique quadratic subfield is Q(sqrt(5)), so adjoining i doubles the degree. Thus [S:Q]=40.

On the ten root labels j in Z/10Z, the Galois group acts as the full affine group

    j -> a*j+t,
    a in (Z/10Z)^*={1,3,7,9}, t in Z/10Z.            (3.2)

The exact 40-element enumeration has these cycle types:

    1^10             : 1
    10               : 4
    5,5              : 4
    2,2,2,2,2        : 6
    1,1,4,4          : 10
    2,4,4            : 10
    1,1,2,2,2,2      : 5.                            (3.3)

For an unramified q, these cycle lengths are exactly the irreducible-factor degrees of T^10+256 modulo q.

Now combine S with Q(zeta_17). The first field is ramified only over 2 and 5; the second only over 17. Since both are Galois, their intersection would be a Galois extension of Q unramified at every finite prime, hence is Q. Therefore their compositum has Galois group

    Gal(S/Q) x (Z/17Z)^*.                             (3.4)

If r=ord_17(q), cleanliness means that none of the cycle lengths in (3.3) is divisible by r. The exact counts among the 40 affine elements are

    r=1:   0 clean
    r=2:   5 clean
    r=4:  20 clean
    r=8:  40 clean
    r=16: 40 clean.                                  (3.5)

The cyclic group (Z/17Z)^* has respectively 1,1,2,4,8 elements of exact orders 1,2,4,8,16. Chebotarev therefore gives the natural density

    (1*0 + 1*5 + 2*20 + 4*40 + 8*40)/(16*40)
      = 525/640
      = 105/128.                                     (3.6)

Thus **clean primes have natural density 105/128**.

The Chebotarev statement used here is J. S. Milne, *Algebraic Number Theory*, Theorem 8.31; the source mapping is preserved in `references/U80/sources.json`.

## 4. A global height/support consequence

Let

    kappa=|c|=2^(4/5).

The ten complex embeddings send c to ten equally spaced numbers of modulus kappa. Fourier inversion on these ten roots gives

    |a9| <= kappa^(-9) * max_sigma |sigma(theta)|.    (4.1)

From theta^17=X+cY,

    |sigma(theta)| <= (X+kappa Y)^(1/17).

Together with (2.3),

    Y_clean^9 <= |a9|
      <= kappa^(-9)(X+kappa Y)^(1/17),               (4.2)

hence

    (kappa Y_clean)^153 <= X+kappa Y.                (4.3)

In particular, since 1<kappa<2,

    Y_clean^153 < X+2Y.                              (4.4)

This is an infinite support restriction: more than four-fifths of rational primes, in the natural-density sense, belong to a set whose contribution to Y is globally controlled by a single nonzero coefficient of the common seventeenth root.

It is not a contradiction. A hypothetical Y may be supported largely on the complementary density-23/128 set, and X is not bounded above in terms of Y by this argument.

## 5. Relation to the fourteen forced primes

U72 forced

    11,31,41,61,71,101,151,191,211,281,331,431,461,631

to divide Y. All fourteen satisfy a sufficient clean-prime test: each is 1 modulo 5; the residue degrees in Q(2^(1/5),i) divide 5 when q=1 mod4 and divide 10 when q=3 mod4, while q^d is not 1 modulo 17 for the corresponding d. The TypeScript certificate checks these values exactly.

Their product is

    433992707035920672833426144791.

Thus U80 subsumes the local coefficient-divisibility mechanism behind those fixed primes into a general positive-density theorem. It does not strengthen U72's current explicit 4811-digit lower bound without discovering additional clean prime divisors of Y.

## 6. Computation audit

`code/U80_clean_prime_density.ts` enumerates all forty affine permutations, reproduces (3.3), proves the finite counts (3.5), reduces the density to 105/128, checks the fourteen inherited primes, their product, and the factorization of the numerator in (2.6).

A strict TypeScript compile and execution were run after writing the file:

    tsc --target ES2022 --module commonjs --strict \
        --noUncheckedIndexedAccess --noUnusedLocals --noUnusedParameters ...
    node .../U80_clean_prime_density.js

The run returned the seven cycle-type counts, clean counts `0,5,20,40,40`, density `105/128`, all fourteen prime rows, the exact forced product, and `fullBealSolved:false`.

A separate Wolfram Language enumeration, written independently from the TypeScript control flow, returned the same cycle-type multiset, the same clean counts, and exactly `105/128`. An earlier malformed Wolfram permutation expression emitted errors and returned an incorrect intermediate value; it is rejected and not evidence.

## 7. Research consequence and next route

This result explains structurally why the local coefficient method is useful but cannot by density alone finish (W). It replaces a purely finite-prime viewpoint with an infinite prime-support theorem, while exposing the complementary dirty-prime support as the actual gap.

The strongest next global routes remain:

1. compute/certify the degree-34 class-group 2-rank and complete U79's Selmer restriction matrix; or
2. finish the corrected U63-U65 modular route by proving the intended level-lowering application and controlling the surviving boundary orbit b globally.

The attempted PARI GitHub workflow at commit `7370f5854c3b9f8b151dc8c7bd2085664ca062eb` failed before any observable computation steps, so it supplies no class-group evidence. Wolfram also returned the degree-34 class number as unavailable. These are execution blockers for that computational subroute, not mathematical evidence for or against d=0.
