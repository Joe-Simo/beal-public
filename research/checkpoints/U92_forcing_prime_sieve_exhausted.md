# U92: the U72 Gaussian forcing-prime sieve is globally exhausted

**Status: written partial theorem with a complete finite scan, an exact Kummer-cover genus calculation, Hasse-Weil coverage of the infinite tail, and independent Wolfram corroboration. The weighted equation and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. This checkpoint revisits U72's fourteen primes not to enlarge the search, but to answer a precise global question: **can the same finite-field criterion ever force any additional rational prime into `Y`?** The answer is no.

## 1. Exact finite-field criterion

Assume a primitive positive solution of the weighted equation

    X^10+256Y^10=Z^17.                               (W)

U71/U72 reconstruct the Gaussian case III. In the notation of `code/U72_full_support.py`, after projective normalization `A=1` one has

    a=1,
    b=K B^5,     K=16*17^4,                          (1.1)

and the two Gaussian cofactors must satisfy

    G(b^2) is a fifth power,
    H(b^2)/17 is a fifth power                         (1.2)

modulo every rational prime `q` for which the reduction is used, where

    G(v)=17v^8-680v^7+6188v^6-19448v^5+24310v^4
         -12376v^3+2380v^2-136v+1,

    H(v)=v^8-136v^7+2380v^6-12376v^5+24310v^4
         -19448v^3+6188v^2-680v+17.                 (1.3)

If there is any `B != 0 (mod q)` satisfying (1.2), this criterion cannot force `q|B`, hence cannot force `q|Y` by this route.

For `q != 5` with `q not congruent to 1 (mod 5)`, the fifth-power map on `F_q^*` is an automorphism, so this criterion cannot force `B=0`. Thus only primes

    q = 1 (mod 5)                                    (1.4)

need to be considered. The prime 17 is outside (1.4) and is handled separately upstream.

## 2. The Kummer curve of simultaneous survivors

For `q=1 (mod 5)`, introduce the affine curve

    R^5 = b/K,
    C^5 = G(b^2),
    D^5 = H(b^2)/17.                                 (2.1)

A rational point with

    b R C D != 0                                     (2.2)

gives a nonzero survivor of (1.2): simply take `B=R`.

We now prove that such a point must exist for every sufficiently large `q`.

### 2.1 Geometric connectedness and degree

Over an algebraic closure, the three Kummer classes

    b/K,  G(b^2),  H(b^2)/17                         (2.3)

are independent in `k(b)^*/k(b)^{*5}`. Indeed:

- at `b=0`, only the first function has valuation one;
- at a simple root of `G(b^2)`, only the second has valuation one;
- at a simple root of `H(b^2)`, only the third has valuation one.

Hence any relation

    (b/K)^r G(b^2)^s (H(b^2)/17)^t = fifth power

forces `r=s=t=0 (mod 5)`. The smooth projective normalization of (2.1) is therefore geometrically connected of degree

    5^3=125                                           (2.4)

over the `b`-line.

The needed simplicity/disjointness of the finite branch loci is exact:

    Res(G,H)=2^136,
    Disc(G)=Disc(H)=2^112*17^7.                      (2.5)

Thus for every `q=1 (mod 5)` all sixteen roots of `G(b^2)` and all sixteen roots of `H(b^2)` are simple and mutually disjoint; such a prime is never 2 or 17.

### 2.2 Branch points and genus

The branch points over an algebraic closure are

- `b=0`;
- the sixteen roots of `G(b^2)`;
- the sixteen roots of `H(b^2)`;
- `b=infinity`.

There are exactly

    34 branch points.                                (2.6)

At each one the inertia subgroup has order five. Since the cover has degree 125, there are 25 geometric points above each branch point and each contributes `5-1=4` to the tame ramification divisor. Riemann-Hurwitz therefore gives

    2g-2 = -2*125 + 34*25*4
         = 3150,

so

    g=1576.                                           (2.7)

This uses the standard tame Riemann-Hurwitz formula; the precise source is recorded in `references/U92/sources.json`.

## 3. Hasse-Weil eliminates every large forcing prime

For the smooth geometrically connected projective curve `C_q` above, Hasse-Weil gives

    #C_q(F_q) >= q+1-2g*sqrt(q)
              = q+1-3152*sqrt(q).                    (3.1)

Across all 34 branch fibres there are at most

    34*(125/5)=850                                   (3.2)

geometric points, hence at most 850 rational points. Therefore a nonbranch rational point satisfying (2.2) must exist as soon as

    q+1-3152*sqrt(q) > 850.                          (3.3)

For `q>849`, squaring the positive sides makes (3.3) equivalent to

    (q-849)^2 > 3152^2 q.                            (3.4)

Exact integer arithmetic shows that the least integer satisfying (3.4) is

    q0 = 9,936,802.                                   (3.5)

Indeed the left-minus-right value is negative at `q0-1` and equals `720801>0` at `q0`.

Consequently **no prime `q=1 (mod 5)` with `q>=9,936,802` can be a forcing prime for (1.2)**.

## 4. Complete finite range below ten million

The remaining range is finite and overlaps the theoretical range because

    9,936,802 < 10,000,000.                           (4.1)

`code/U92_forcing_prime_exhaustion.ts` performs an exact sieve of Eratosthenes and tests every prime

    q<10^7, q=1 (mod 5).                              (4.2)

There are exactly

    166,104                                           (4.3)

such primes.

For every non-forcing prime the program produces an explicit nonzero `B` satisfying (1.2). Searching only `1<=B<=1000` already succeeds for every non-forcing prime; the largest first witness is

    B=370 at q=2,344,241.                             (4.4)

The only primes with no such nonzero witness are exactly

    11, 31, 41, 61, 71, 101, 151,
    191, 211, 281, 331, 431, 461, 631.               (4.5)

At each of these fourteen primes the program then drops the witness cutoff and exhausts **every** `B in F_q` in the `A=1` chart, finding only `B=0`. U72's original complete projective scan also retained and rejected the separate `A=0` axis, so no projective case is omitted.

A separate exact Python computation independently reproduced the same 166,104-prime scan, the same fourteen-prime list, and the same maximal first witness `(370,2344241)`. The TypeScript implementation compiled under TypeScript 5.8.3 with strict checking and executed under Node 22.16.0 in about five seconds.

## 5. The complete forcing list

Combining Sections 3 and 4 proves:

**Theorem.** Among all rational primes to which U72's Gaussian case-III fifth-power criterion applies, the only primes forced into `B`, and hence into `Y`, by that criterion are

    11, 31, 41, 61, 71, 101, 151,
    191, 211, 281, 331, 431, 461, 631.               (5.1)

Their product remains

    P=433992707035920672833426144791.                (5.2)

There are **no additional forcing primes at larger size** waiting to be found by extending the same search.

This statement is scoped to the exact U72 finite-field criterion. It does not say that no other argument can force additional primes into `Y`, and it does not classify all local consequences of (W).

## 6. Computation audit

Two exact certificates are preserved:

- `code/U92_forcing_prime_exhaustion.ts` — the complete finite prime range and explicit nonzero witnesses;
- `code/U92_kummer_branch_certificate.py` — the resultants, discriminants, branch count, Riemann-Hurwitz genus, branch-fibre cap, and exact Hasse-Weil threshold.

Wolfram independently returned

    Res(G,H)=2^136,
    Disc(G)=Disc(H)=2^112*17^7,
    2g-2=3150,
    g=1576,
    q0=9,936,802.                                    (6.1)

An earlier malformed Wolfram genus expression added the constant in the wrong place and returned 1577; it was immediately rejected. The corrected Riemann-Hurwitz expression returned 1576 and is the one used here.

The finite TypeScript scan and the separate Python scan agree on the full forcing list and witness maximum. No floating-point number decides a finite-field classification or the threshold.

## 7. Research consequence

U92 closes a concrete research route rather than merely extending it: **searching more primes with the U72 criterion cannot strengthen the fourteen-prime product used in U90's Padé height obstruction.** The fixed product `P` is complete for this sieve.

Therefore the `10^25993` lower bound from U90 cannot be improved simply by enlarging that same forcing-prime search. Further progress on the weighted equation must obtain a genuinely new global restriction: for example a different local criterion, a better-height invariant, the unresolved U80 class-group/Selmer computation, or a completed corrected modular argument.

No contradiction, counterexample, weighted-equation impossibility theorem, or complete Beal solution is claimed.
