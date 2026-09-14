# U29: finite quadratic-subfield level elimination

Status: verified conditional partial result only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Purpose

Continue the modular route from U26--U28 and the certified `sigma^2`-conjugation lemma. Let

    F = Q(w),  w^4-w^3-6w^2+w+1 = 0

be the cyclic quartic field of conductor 17, and let

    K = Q(sqrt(17))

be its quadratic subfield. The four obstructing level-272 Hilbert newforms over `F` are `r,s,v,w`.

The previously certified `sigma^2` relation gives residual invariance under `Gal(F/K)` at the ramified residue-degree-one prime `lambda | 5`. Under irreducibility, Clifford theory therefore supplies an extension of each residual representation from `G_F` to `G_K`. What remained unclear was whether, if such an extension were known to be modular of parallel weight 2 with conductor dividing the expected `K`-level, any Hilbert newform over `K` could realize it.

This file closes that *finite form-elimination* question. It does **not** prove the needed modularity/weight/conductor bridge.

## Forced traces at the two primes of K above 13

The rational prime 13 splits in `K`. Each of its two primes then splits in `F`, giving the four `F`-primes used in the q=13 blocks.

For `r,s`, the q=13 coefficients are combinations of `e` and `-e-2`, with coefficient polynomial

    e^2 + 2e - 4.

At the ramified prime `lambda=(5,e+1)`, both reduce to

    e == -1 == 4 (mod lambda),
    -e-2 == -1 == 4 (mod lambda).

For `v,w`, U27 fixes the relevant residue-degree-one prime again by `e -> -1 (mod 5)`, and the previously checked q=13 blocks reduce to the same trace 4 at all four primes.

Therefore any `G_K` extension whose restriction is one of the four survivor residual representations must have

    a_q == 4 (mod 5)

at **both** primes `q | 13` of `K`.

## Candidate conductor levels over K

In `K=Q(sqrt(17))`, 2 splits into two primes of norm 2 and 17 has the unique ramified prime of norm 17. Restricting an extension to `F/K` can only preserve or drop the local conductor exponents relevant here. Thus the divisor norms of the expected level are among

    1, 2, 4, 17, 34, 68.

For safety the LMFDB queries were by level norm, so all recorded ideals of those norms were included, even when an ideal is not literally a divisor of the expected squarefree product.

Current LMFDB inventory checked on 2026-09-14:

- norm 1: no forms;
- norm 2: no forms;
- norm 4: `2.2.17.1-4.1-a`;
- norm 17: `2.2.17.1-17.1-a`, `2.2.17.1-17.1-b`;
- norm 34: `2.2.17.1-34.1-a`, `34.1-b`, `34.2-a`, `34.2-b`;
- norm 68: `2.2.17.1-68.1-a`, `68.2-a`, `68.3-a`.

So there are ten recorded candidates in total.

## Elimination by q=13

The LMFDB prime ordering for `K` begins with the two norm-2 primes, the norm-9 prime, and then the two norm-13 primes. This ordering is visible on the standard Hilbert form pages; e.g. `2.2.17.1-26.3-a` lists

    norm 2, norm 2, norm 9, norm 13, norm 13, norm 17, ...

### Level norm 68

All three forms have the two norm-13 eigenvalues

    (-2,-2).

Modulo 5 these are `(3,3)`, not `(4,4)`. Hence all level-68 forms are excluded.

### Level norm 34

`34.1-a` has q=13 pair `(-1,-2)`.

`34.2-a` has q=13 pair `(-2,-1)`.

Thus each rational-coefficient form is excluded immediately.

The degree-2 forms `34.1-b` and `34.2-b` have coefficient polynomial

    x^2 + x - 4.

Their q=13 pairs are respectively

    (-3e-1, -2),
    (-2, -3e-1).

The rational entry `-2 == 3 (mod 5)` already contradicts the required trace 4, independently of the choice of prime above 5 in the quadratic coefficient field. Hence both degree-2 forms are excluded.

### Level norm 17

`17.1-a` has q=13 pair `(-2,-2)`, giving `(3,3)` modulo 5.

`17.1-b` has Hecke polynomial `x^2-3` and q=13 pair `(2,-2)`, giving rational residues `(2,3)` modulo 5.

Hence both are excluded.

### Level norm 4

For `4.1-a`, the first six stored Hecke eigenvalues are

    -1, -1, -2, 2, 2, -6.

Using the standard prime ordering above, the fourth and fifth entries are the two norm-13 coefficients, namely `(2,2)`. These reduce to `(2,2)` modulo 5, so the form is excluded.

Norms 1 and 2 have no recorded forms.

## Conditional conclusion

There is no weight-2 Hilbert newform over `K=Q(sqrt(17))` at any recorded level whose norm divides the expected conductor norm 68 (indeed, none among all recorded forms at norms 1,2,4,17,34,68) whose two q=13 traces can match the forced residual trace `(4,4)`.

Therefore:

> If one of the four survivor residual representations extends from `G_F` to an absolutely irreducible, totally odd `G_K` representation that is modular of parallel weight 2 and whose conductor divides the expected product of the two primes above 2 and the ramified prime above 17, then that extension is impossible.

This is a genuine finite elimination, but the antecedent is not yet fully proved.

## Modularity source investigated

Allen--Khare--Thorne, *Modularity of PGL2(F_p)-representations over totally real fields* (PNAS 118, 2021; arXiv:2104.14732), Theorem 1.2, proves automorphy for absolutely irreducible totally odd projective mod-5 representations over totally real fields under the stated cyclotomic/determinant-parity alternatives. For `K=Q(sqrt(17))`, `[K(zeta_5):K]=4` because the quadratic subfield of `Q(zeta_5)` is `Q(sqrt(5))`, not `K`.

The paper defines projective automorphy through a regular algebraic GL2 automorphic representation of weight 0, which is the automorphic normalization corresponding to parallel Hilbert weight 2. However, Theorem 1.2 is projective and does not by itself identify the exact linear mod-5 lift or prove that its Artin conductor divides the expected level. Those local/global compatibility points remain proof obligations.

Primary source checked:

- https://arxiv.org/abs/2104.14732

Relevant level-optimization literature located for the remaining bridge:

- F. Jarvis, *Level lowering for modular mod ell representations over totally real fields*, Math. Ann. 313 (1999), 141--160.
- K. Fujiwara, *Level optimization in the totally real case* (2006), which gives optimal level reduction away from ell for ell>2, including the even-degree totally real case.

Applicability of these theorems to the present extension has not yet been verified hypothesis-by-hypothesis.

## Current obligations

1. Prove or refute the paired residual congruences `r ~= s (mod lambda)` and `v ~= w (mod lambda)`. Combined with the certified base-field sigma action, this would give full `Gal(F/Q)` invariance and potentially permit descent directly to Q.
2. Alternatively, complete the `G_K` bridge: start from projective automorphy, recover an automorphic linear lift of the specific residual representation up to a finite character twist, then justify level optimization to its Artin conductor.
3. Prove the local conductor statement at both primes above 2 and at the prime above 17 rather than assuming it.

No Beal case is declared closed by U29.