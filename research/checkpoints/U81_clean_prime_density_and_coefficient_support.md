# U81: a density-105/128 coefficient-support theorem for the weighted branch

**Status: written partial theorem with an exact finite group certificate and independent Wolfram corroboration. The weighted equation and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. The repository was resumed through U80. U80's class-group bottleneck and negative shortcut audits remain unchanged. U65/U71/U72 are used only at their stated written/self-reviewed level.

## 1. Scope

Assume a primitive positive solution of

    X^10 + 256 Y^10 = Z^17.                           (W)

U71/U72 give

    L=Q(c), c^10=-256,
    theta=a0+a1*c+...+a9*c^9 in Z[c],
    theta^17=X+cY,
    a9 != 0.                                          (1.1)

U72 established exact coefficient valuations at fourteen already-forced primes. Here we isolate an infinite positive-density set of rational primes for which the same coefficient mechanism works uniformly.

## 2. Clean primes and exact coefficient valuations

For q not in {2,5,17}, factor

    T^10+256 = product_i f_i(T)  over F_q,

with irreducible degrees d_i. Call q **clean** if

    17 does not divide q^(d_i)-1 for every i.         (2.1)

Equivalently the finite etale algebra

    A_q=F_q[T]/(T^10+256)

has no nontrivial seventeenth root of unity, since

    |A_q^*|=product_i(q^(d_i)-1).

**Theorem 1.** If q is clean and q^e exactly divides Y, then

    v_q(a9)=9e+v_q(658767450) >= 9e.                  (2.2)

Hence, for

    Y_clean=product_(q clean) q^(v_q(Y)),

one has

    Y_clean^9 | a9.                                   (2.3)

### Proof

Primitivity gives q not dividing X. Reduction of theta^17=X+cY gives

    theta^17=X in A_q.

By cleanliness the seventeenth-power map on A_q^* is injective. In particular 17 does not divide q-1, so X has a unique scalar seventeenth root x modulo q. Therefore theta is congruent to x modulo q. Since 17*x^16 is a q-adic unit, this root lifts uniquely.

Thus the actual local root is the convergent binomial series

    theta=x*sum_(k>=0) B_k(cY/X)^k,
    B_k=binomial(1/17,k).                             (2.4)

For q!=17, B_k belongs to Z_q. Grouping exponents modulo ten with c^10=-256 gives

    a9=x*sum_(m>=0) B_(9+10m)(-256)^m(Y/X)^(9+10m). (2.5)

U72's exact value is

    B_9=658767450/17^9,
    658767450=2*3*5^2*11*59*67*101.                 (2.6)

The leading term therefore has valuation `9e+v_q(658767450)`, at most `9e+2`. Every tail term has valuation at least `19e`. Since `9e+2<19e` for e>=1, the leading term cannot cancel. This proves (2.2) and (2.3).

## 3. Density of the clean primes

Let S be the splitting field of T^10+256. Put rho^5=2 and c=i*rho^4. Then

    c^4=8rho, c^5=16i,

and the ten roots are c*zeta_10^j. Hence

    S=Q(rho,zeta_5,i), [S:Q]=40.                     (3.1)

The degree-20 splitting field Q(rho,zeta_5) of T^5-2 has Galois group C5 semidirect C4 and unique quadratic subfield Q(sqrt(5)); adjoining i therefore doubles the degree. On the ten root labels j in Z/10Z the Galois action is the full affine group

    j -> a*j+t,
    a in {1,3,7,9}, t in Z/10Z.                      (3.2)

Exact enumeration of its forty elements gives:

    cycle type                  count
    1^10                            1
    10                              4
    5,5                             4
    2,2,2,2,2                       6
    1,1,4,4                        10
    2,4,4                          10
    1,1,2,2,2,2                     5.              (3.3)

For unramified q these are the factor degrees of T^10+256 modulo q.

The Galois fields S and Q(zeta_17) are linearly disjoint: S is ramified only over 2 and 5, Q(zeta_17) only over 17, and a nontrivial Galois intersection would be unramified at every finite rational prime. Thus the compositum has group

    Gal(S/Q) x (Z/17Z)^*.                            (3.4)

Let r=ord_17(q). A prime is clean precisely when no cycle length in (3.3) is divisible by r. The exact clean counts among the forty affine elements are

    r=1: 0,
    r=2: 5,
    r=4: 20,
    r=8: 40,
    r=16: 40.                                        (3.5)

The cyclic group of order sixteen has respectively 1,1,2,4,8 elements of exact orders 1,2,4,8,16. Chebotarev therefore gives natural density

    (1*0+1*5+2*20+4*40+8*40)/(16*40)
      = 525/640
      = 105/128.                                     (3.6)

Thus clean primes have natural density **105/128**. The Chebotarev theorem used is Milne, *Algebraic Number Theory*, Theorem 8.31; see `references/U81/sources.json`.

## 4. Global support/height consequence

Let kappa=|c|=2^(4/5). The ten embeddings send c to ten equally spaced complex numbers of modulus kappa. Fourier inversion on the ten evaluations of theta gives

    |a9| <= kappa^(-9) max_sigma |sigma(theta)|.      (4.1)

Since theta^17=X+cY,

    max_sigma |sigma(theta)| <= (X+kappa Y)^(1/17).

Using (2.3),

    (kappa Y_clean)^153 <= X+kappa Y,                (4.2)

and therefore

    Y_clean^153 < X+2Y.                              (4.3)

This is a genuine infinite support restriction, not a contradiction. A hypothetical Y may concentrate its prime support in the complementary density-23/128 set, and this argument gives no upper bound for X in terms of Y.

## 5. Relation to the fourteen forced primes

U72 forces

    11,31,41,61,71,101,151,191,211,281,331,431,461,631

to divide Y. Every one is clean by a sufficient exact test: q=1 mod5, all relevant residue degrees divide 5 when q=1 mod4 and divide 10 when q=3 mod4, while q^d is not 1 mod17 for that d.

Their product is

    433992707035920672833426144791.

Thus U81 places U72's finite coefficient-divisibility mechanism inside a positive-density theorem. It does not by itself improve the existing explicit 4811-digit lower bound because no additional prime divisor of Y has been forced.

## 6. Exact computation audit

`code/U81_clean_prime_density.ts` enumerates all forty affine permutations, checks (3.3), checks all five clean counts in (3.5), reduces the density to 105/128, and verifies the fourteen inherited prime tests, their product, and the factorization in (2.6).

A strict TypeScript compile and Node execution of the same program succeeded before preservation, with `--strict --noUncheckedIndexedAccess --noUnusedLocals --noUnusedParameters`; the returned mathematical data were the cycle histogram above, clean counts `0,5,20,40,40`, density `105/128`, all fourteen prime rows, the exact product, and `fullBealSolved:false`.

A separate Wolfram Language enumeration using independently written cycle traversal returned the same seven cycle-type counts, the same five clean counts, and exactly `105/128`. An earlier malformed permutation expression produced messages and an incorrect intermediate value; that call is rejected as evidence.

## 7. Research consequence

U81 turns the finite prime-divisibility pattern into an infinite support theorem but also identifies its precise limitation: the complementary **dirty primes**, of density 23/128, are not controlled by this coefficient argument.

The next route is to classify those dirty Frobenius classes explicitly and test whether the Gaussian/quintic descents in U65/U71 impose incompatible support conditions. In parallel, U80's independent class-group bottleneck remains unresolved because no exact class-group engine has yet produced `d=dim_F2 Cl(O_F)[2]`.
