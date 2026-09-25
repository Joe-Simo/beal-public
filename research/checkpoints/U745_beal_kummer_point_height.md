# U745: The Beal-derived CM point has an explicit canonical height

**Date checked:** 2026-09-24

**Status:** exact height consequence of a hypothetical `(3,3,p)` solution; it does not contradict BSD or prove Beal. No novelty claim.

Assume U727's surviving primitive branch: `p>10^9` is prime, `p≡1 (mod 3)`, `p∤C`, `3|C`, and `p=3e+1`. Use U736/U737's exact factorization

```text
S=A+B=c1^p/3,       Q=A²−AB+B²=3c2^p,       C=c1c2.
```

U736 maps the hypothetical solution to

```text
E_C: Y²=X³−432C²,
X=12 C^(e+1)/S,      Y=36 C(A−B)/S.
```

Set `D=A−B`. Since `C^p=SQ`, `Q=3c2^p`, and `D²=Q−AB`, direct simplification gives

```text
X³/Y² = (4/3) C^p/(S D²) = 4c2^p/D².
```

This fraction is reduced. Kraus parity makes `D` odd. If a prime `q|c2` also divided `D`, then `q|Q` and `q|D` would imply `q|AB`; pairwise coprimality and `q|Q` rule that out. Also

```text
0 < D² = Q−AB < 3c2^p < 4c2^p.
```

Therefore its absolute logarithmic height is exactly

```text
h(X³/Y²)=log(4c2^p)=log 4+p log c2.
```

Write `−432C²=d u^6` with `d` sixth-power-free. The change of variables `X=u²x`, `Y=u³y` identifies `E_C` over `Q` with `E_d:y²=x³+d` and preserves canonical height. Zhao's Lemma 2.2 gives `hhat(P)=1/6 h(X³/Y²)+O(1)`, with an absolute additive constant for this fixed sextic-twist family. Thus

```text
hhat_E_C(P) = (p/6) log c2 + O(1).
```

Moreover `Q/S²=27(c2/c1²)^p` and `1/4≤Q/S²<1`, so `log(c2/c1²)=O(1/p)`. Since `C=c1c2`, this yields

```text
log c2 = (2/3)log C + O(1/p),
hhat_E_C(P) = (p/9)log C + O(1).
```

In the residual noncube branch, U741 proves that `P` is non-torsion. Zhao's Proposition 2.5 gives the universal lower bound `hhat(P) >> |d|^(1/36)` for every non-torsion point on every sixth-power-free Mordell curve `E_d`. Combining it with the exact height above gives only

```text
|d| << (p log C)^36.
```

The noncube condition gives a prime `q|c2` with `3∤v_q(c2)`. Then `q²|d`, while U738 gives `q≥(sqrt(p)−1)²`; hence `|d|` has only the lower bound of order `p²`, or `|d|^(1/36) >> p^(1/18)`. That is far below `hhat(P)~p log C` and yields no contradiction. Sixth-power normalization discards large sixth-power parts of `C`; the existing constraints do not force `|d|` to be comparable to a positive power of `C`.

The density-one strengthening in Zhao's Theorem 1.6 cannot be used for this individual family: its proof requires a small square part of `d`, whereas here `C` is odd and divisible by 3, so `|d|/3` is itself a square and is not small relative to `|d|`.

This gives a precise Beal-to-BSD input: a hypothetical solution supplies a positive-rank CM curve and a point of height approximately `(p/9)log C`. BSD allows positive rank and places a regulator in its leading-term formula, but the point's height alone does not determine that regulator. Rank exactly one, a generator/index control, or a much stronger lower bound involving the sixth-power-free kernel would be additional input. Sources: [U736](U736_beal_cm_dual_3isogeny_kummer_class.md), [U741](U741_noncube_cm_point_positive_rank.md), [U738](U738_c2_prime_factor_hasse_cutoff.md), [Zhao, Lemma 2.2 and Proposition 2.5](https://arxiv.org/html/2108.10953v2).
