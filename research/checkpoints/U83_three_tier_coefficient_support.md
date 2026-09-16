# U83: three-tier coefficient support controls density 553/640

**Status: written partial theorem with an exact TypeScript certificate and independent Wolfram group-count corroboration. The weighted equation and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. This extends U82's strong and semi-strong families. The only inherited arithmetic input is U71/U72's common integral seventeenth root and nonvanishing of all ten coefficients, together with U81/U82's already written local expansions.

## 1. Setup

Assume a primitive positive solution

    X^10+256Y^10=Z^17.

Let

    c^10=-256, c^5=16i,
    theta=sum_(j=0)^9 a_j c^j in Z[c],
    theta^17=X+cY,

with every a_j nonzero. Let S be the degree-40 splitting field of T^10+256. Its Galois group acts on the ten roots c*zeta_10^j by

    j -> a*j+t,
    a in {1,3,7,9}, t in Z/10Z.

As in U81, S is linearly disjoint from Q(zeta_17), so Frobenius data are pairs from a set of 40*16=640 group elements.

U82 partitions two controlled classes:

- **strong**: density 529/640, with q^(9v_q(Y)) | a9;
- **semi-strong**: density 8/640=1/80, with q^(4v_q(Y)) dividing both a4 and a9.

This checkpoint finds a third disjoint family of density 16/640=1/40 controlled by the fixed coefficient a5.

## 2. The weak family

Let q not be 2,5,17. Write the affine Frobenius on root labels as

    g(j)=a*j+t mod 10.

Call q **weak** when

1. q is congruent to 1 modulo 17;
2. t is odd;
3. g is not a 10-cycle.

The exclusion of 10-cycles only keeps the categories disjoint: those four cases already belong to U82's strong family.

### Theorem 1

If q is weak and e=v_q(Y)>0, then

    q^e | a5.                                         (2.1)

### Proof

Because q is 1 modulo 17, all seventeenth roots of unity lie in Q_q. As in U82, the residual seventeenth roots of X occurring in each factor of the etale root algebra come from a scalar seventeenth root x of X, multiplied by a seventeenth root of unity. Thus the exact q-adic root delta of X matching theta modulo q is constant on each Frobenius orbit of the ten roots.

Write

    delta=d0+d1*c+...+d9*c^9.

Let r_j=c*zeta_10^j. Fourier inversion gives

    d5*c^5 = (1/10) sum_(j=0)^9 delta(r_j) zeta_10^(-5j)
            = (1/10) sum_(j=0)^9 delta(r_j) (-1)^j.   (2.2)

Since a is odd and t is odd, g flips parity at every application:

    parity(g(j)) = parity(j)+1 mod 2.

Every Frobenius orbit therefore has even length and contains equally many even and odd labels. The value delta(r_j) is constant on each orbit, so the alternating sum in (2.2) vanishes orbit by orbit. Hence

    d5=0.                                             (2.3)

Now put T=Y/X. The local root is

    theta = delta * sum_(n>=0) B_n(cT)^n,
    B_n=binomial(1/17,n),                             (2.4)

with all B_n q-integral. The c^5 coefficient is obtained from terms d_j B_n c^(j+n) with j+n congruent to 5 modulo 10. The only possible term with n=0 would be d5, which is zero by (2.3). Every remaining contributing term has n>=1 and therefore contains T^n, hence is divisible by q^e. This proves (2.1).

The proof is all-precision and does not infer divisibility from a finite residue search.

## 3. Density count

There are twenty affine elements with odd translation t: four choices of a and five odd choices of t. Among them, exactly four are 10-cycles, namely the multiplier-one translations by 1,3,7,9. Those four are already strong.

Thus sixteen affine elements remain. The weak condition also fixes the cyclotomic Frobenius to the identity, the unique element corresponding to q congruent to 1 modulo 17. Therefore the weak family occupies

    16/640 = 1/40                                    (3.1)

of the compositum Galois group.

Chebotarev gives the same natural density for the corresponding unramified rational primes. The exact group enumeration in `code/U83_three_tier_support.ts` gives the disjoint counts

    strong        529,
    semi-strong     8,
    weak           16,
    uncontrolled   87,
    total         640.                               (3.2)

A separately written Wolfram enumeration returned exactly `{529,8,16,87}` and densities `{529/640,1/80,1/40,87/640}`.

## 4. Global support inequalities

Let

    Y_s = product over strong q of q^v_q(Y),
    Y_m = product over semi-strong q of q^v_q(Y),
    Y_w = product over weak q of q^v_q(Y).

The supports are disjoint. U82 and Theorem 1 give

    Y_s^9 Y_m^4 | a9,
    Y_w | a5.                                         (4.1)

Let kappa=|c|=2^(4/5) and H=X+kappa Y. Fourier inversion over the ten complex embeddings gives

    |a9| <= kappa^(-9) H^(1/17),
    |a5| <= kappa^(-5) H^(1/17).                     (4.2)

Therefore

    kappa^153 Y_s^153 Y_m^68 <= H,                   (4.3)
    kappa^85  Y_w^17 <= H.                           (4.4)

In particular

    Y_s^153 Y_m^68 < X+2Y,
    Y_w^17 < X+2Y.                                   (4.5)

Multiplying the two weaker displayed inequalities also gives

    Y_s^153 Y_m^68 Y_w^17 < (X+2Y)^2.                (4.6)

The union of the three controlled prime families has density

    (529+8+16)/640 = 553/640.                         (4.7)

Thus the coefficient method now controls more than 86 percent of rational primes in the Chebotarev-density sense. The remaining set has density 87/640.

This still does not prove impossibility. Density is not a lower bound on how many prime divisors a specific integer must have, and no upper bound for X in terms of Y is obtained here.

## 5. Exact certificate and audit

`code/U83_three_tier_support.ts` was compiled with TypeScript 5.8.3 under

    --strict --noUncheckedIndexedAccess --noUnusedLocals --noUnusedParameters

and executed with Node 22.16.0 before preservation. It reproduced the seven affine cycle-type counts, the four category counts in (3.2), and the densities in (4.7). It also rechecks the exact numerators

    B_4=-1100/17^4,
    B_9=658767450/17^9,

used in the upstream coefficient expansions.

The Wolfram count is independent of the TypeScript control flow. Neither finite computation replaces the Fourier-orbit proof of d5=0 or the q-adic binomial expansion.

## 6. Research consequence

U83 reduces the residual prime-support set from U81's density 23/128 to density 87/640. The remaining Frobenius pairs are precisely the cases where this fixed-coordinate-vanishing mechanism does not yet supply one of the three divisibility tiers above.

The next useful question is no longer to add isolated forcing primes. It is to determine whether the remaining 87/640 Frobenius classes satisfy a fixed algebraic relation among several coefficients of the local seventeenth root, strong enough to produce a nonzero global integer covariant with controlled height. In parallel, U80's class-group/Selmer route remains the more direct route if an exact class-group engine becomes available.
