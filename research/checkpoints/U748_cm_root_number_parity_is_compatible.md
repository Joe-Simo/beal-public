# U748: The CM root number creates no rank-parity contradiction

**Date checked:** 2026-09-24

**Status:** exact local root-number formula and compatibility audit in the residual noncube branch; no BSD or Beal proof.

For the curve forced by U736/U741,

```text
E_C: y²=x³−432C²,
```

write `C=3^a c`, with `a≥1`, `c` odd, and `3∤c` (Kraus gives `C` odd and `3|C`). Várilly-Alvarado, Proposition 4.4, gives the root number in terms of `α=−432C²`. After combining its 2-adic, 3-adic, and real-place factors,

```text
w(E_C)=−w3(a,c)(−1)^N,
N=#{ℓ≥5 : ℓ|C, ℓ≡2 (mod 3), 3∤vℓ(C)},
```

where the combined 3-adic factor `w3(a,c)` is `−1` exactly when

```text
a≡1 (mod 3),  or  a≡0 (mod 3) and c≡±1 (mod 9);
```

it is `+1` otherwise. At a prime `ℓ≥5`, the local factor is `+1` when `3|vℓ(C)` and
`(−3/ℓ)` otherwise, so only inert primes with exponent not divisible by 3 contribute to `N`. [Várilly-Alvarado, Proposition 4.4](https://msp.org/ant/2011/5-5/ant-v5-n5-p04-p.pdf).

The Beal constraints recorded in U735/U737 do not determine `a mod 3`, `c mod 9`, or the parity of `N`. In particular, the fact that prime factors of `c₂` split in `Q(√−3)` does not control inert primes in the other factor of `C`.

U741 shows that a hypothetical solution in the residual noncube branch gives `rank E_C(Q)≥1`. Under BSD, if `w(E_C)=+1`, the analytic (and conjecturally algebraic) rank is even, so it could be `2,4,…`; if `w(E_C)=−1`, it could be `1,3,…`. Both cases are compatible with the known lower bound. No rank upper bound or root-sign contradiction follows.

This closes only the attempted root-number parity obstruction. It does not rule out a deeper use of the CM `L`-function, BSD, or the other conjectures. No novelty claim is made.
