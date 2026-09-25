# U746: The degree-70 Fermat Jacobian has no elliptic factor isogenous to the Beal CM curve

**Date checked:** 2026-09-24

**Status:** exact obstruction to a direct isogeny-factor transfer from the degree-70 Fermat Jacobian to `E_C`; it does not rule out other motive correspondences or prove any of the six open problems.

The Beal Kummer curve from U736 is

```text
E_C: y²=x³−432C²,
```

so `j(E_C)=0` and its CM field is `Q(√−3)`. The function-field BSD construction in U728 instead uses the Jacobian `J(F_70)` of the degree-70 Fermat curve.

Aoki's decomposition theorem describes its characteristic-zero isogeny factors. For each diagonal character orbit `S` of triples `(a0,a1,a2)` with nonzero entries modulo `m` and sum zero, it defines a CM abelian variety `A_S`; Theorem 1.3 gives

```text
dim A_S = φ(d_S)/2,      CM(A_S) by Q(ζ_(d_S)),
d_S = m/gcd(m,a0,a1,a2),    d_S | m.
```

Theorem 1.6 decomposes `A_S` up to isogeny as powers of a simple abelian variety `B_S`, whose CM field is the fixed field `Q(ζ_(d_S))^{W_a}`. Therefore the CM field of every simple isogeny factor of `J(F_m)` is a subfield of a cyclotomic field `Q(ζ_d)` with `d|m`.

For `m=70`, no such field contains `Q(√−3)`: that quadratic field has conductor 3, while every `d|70` is coprime to 3 and every subfield of `Q(ζ_d)` has conductor dividing `d`. Thus `J(F_70)` has no elliptic isogeny factor with CM by `Q(√−3)`. In particular, `E_C` cannot be a characteristic-zero elliptic isogeny factor of this Jacobian for any `C`.

This rules out the direct elliptic-factor/Weil-restriction route for transferring the finite-field BSD formula to `E_C`. It does not rule out arbitrary higher-dimensional algebraic correspondences, and U46's special-fiber codimension-two cycle correspondence is a different construction. That correspondence tracks Hodge/Tate cycle classes; it does not identify Mordell–Weil rank, Sha, regulator, Tamagawa factors, or `L`-orders. Kang's result already settles the degree-70 Fermat fourfold's Hodge-class existence question independently.

Primary source: N. Aoki, *Simple factors of the Jacobian of a Fermat curve and the Picard number of a product of Fermat curves*, MPI preprint 89-82, Theorems 1.3 and 1.6: [author/institute copy](https://archive.mpim-bonn.mpg.de/1240/1/preprint_1989_82.pdf). The conclusion is a scope obstruction to one natural transfer, not a novelty claim or a theorem that no future BSD/Hodge bridge can exist.
