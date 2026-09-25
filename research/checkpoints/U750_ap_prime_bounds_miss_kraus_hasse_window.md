# U750: available least-prime bounds miss the Kraus Hasse window

**Date checked:** 2026-09-24

**Status:** source-verified comparison; neither classical zeta-RH nor the checked stronger GRH/AP bounds supplies the small trace-avoiding prime required by U733.

## Required prime range

For a residual exponent prime `p`, U733 uses auxiliary primes

```text
q = 2kp + 1,   q ∤ 72.
```

The current parity-refined Hasse condition for the `q ∤ C` branch is `q < p²/4`; in this range a signed trace congruence modulo `p` lifts to exact equality. In the `q | C` branch the corresponding exact lift holds for `q < (p−1)²`. The smaller bound `q < p²/4` is therefore a sufficient common scale for the sieve certificate. The older generic `q < p²/16` condition in U733 was superseded by its parity refinement.

For odd `p`, the least prime in the class `1 mod p` is also the least prime in `1 mod 2p`: such a prime is odd, so congruence to 1 modulo `p` forces congruence to 1 modulo `2p`.

## Strongest checked GRH bound

Lamzouri–Li–Soundararajan, Corollary 1.2, assumes GRH for the Dirichlet `L`-functions relevant to the modulus and gives

```text
P(a,m) ≤ (φ(m) log m)².
```

With `m=p`, `a=1`, this bounds the least candidate by `((p−1) log p)²`. Its ratio to the required cutoff is

```text
((p−1) log p)² / (p²/4)
  = 4(1−1/p)²(log p)²,
```

which grows without bound (about 297 at `p=5501`). The estimate therefore does not guarantee a prime in the Hasse window. More importantly, the theorem assumes GRH for Dirichlet `L`-functions; ordinary RH for `ζ(s)` alone is not its hypothesis.

Relative to the separate \(q\mid C\) cutoff \((p-1)^2\), the ratio is \((\log p)^2\), which also grows without bound.

## Unconditional bound

Meng's least-prime result gives `P(a,m) ≪ m^(9/2)` when the modulus has bounded cubic part. The modulus `m=2p` is squarefree, so the result applies, but its scale is `O(p^(9/2))`, above `p²/4` by an unbounded factor of order `p^(5/2)`.

## Remaining obstruction

Even a theorem supplying a prime `q` below `p²/4` would not finish the modular argument. It must also prove that the target trace avoids the entire `q`-dependent admissible set built from the ratio curves, boundary model, and `q | C` alternatives. U735's estimate counts admissible parameters; it does not give this trace avoidance. Thus these least-prime results add no uniform exponent elimination and no proof of Beal.

Primary sources: [Lamzouri–Li–Soundararajan, Corollary 1.2](https://arxiv.org/html/1309.3595v3); [Meng, *A Note on the Least Prime in an Arithmetic Progression*](https://xbna.pku.edu.cn/EN/Y2001/V37/I1/20), and Meng's [author-posted note](https://arxiv.org/html/1010.3544).

Local inputs: [U733](U733_kraus_hasse_trace_lift_and_gate_audit.md), [U735](U735_cubic_kraus_pth_power_coset_correction.md).
