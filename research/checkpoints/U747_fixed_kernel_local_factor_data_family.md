# U747: Local Beal factor data can grow with a fixed sextic kernel

**Date checked:** 2026-09-24

**Status:** exact family of necessary-factor-data witnesses; it does not construct Beal solutions. It shows the near-square, noncube, local residue, and sixth-power-free-kernel bounds alone do not control `C`.

Fix a prime `p≥19`, `p≡1 (mod 3)`. Let `E0=72a1`. By Chebotarev, choose distinct primes `q,r>p` that split completely in the finite Galois extension `Q(E0[p],ζ3)`. Then

```text
q≡r≡1 (mod 3p),
a_q(E0)≡a_r(E0)≡2≡q+1≡r+1 (mod p).
```

Thus the rational curve `72a1` satisfies the numerical trace congruence that U738 would require at primes `q,r|C`, with sign `+1`; since `q,r>p`, they also exceed U738's Hasse lower cutoff. There is no Frey curve at these data until `A,B` are reconstructed, so this is only compatibility with the necessary congruence.

The irrational number `θ=log_9(r)` has dense fractional parts `nθ mod 1`. Hence there are infinitely many positive integers `n,k` such that

```text
q^(−1/3)·108^(−1/(3p)) < r^n/9^k < q^(−1/3)·27^(−1/(3p)).
```

Set

```text
c1=3^(3k),       c2=q r^(3n),       C=c1 c2,
S=c1^p/3,         Q=3c2^p.
```

Then `c1,c2` are positive, odd and coprime; `3|c1`, `3∤c2`, `p∤C`, and `c2` is noncube. Also `S Q=C^p`, and

```text
108^(−1/p) < c2/c1² < 27^(−1/p),
1/4 < Q/S² = 27(c2/c1²)^p < 1.
```

These are the factorization and near-square conditions forced by a positive `(3,3,p)` solution. The selected primes in `c2` meet the local trace and Hasse conditions, while `C→∞` as `n,k→∞`.

Nevertheless, the sixth-power-free kernel is fixed:

```text
−432C² = (−432q²)·(3^k r^n)^6,
```

so `d=−432q²` for every member of the family. This confirms that the Zhao bound on `d` cannot bound `C` using only the exponent residues, near-square interval, and local trace conditions.

The factor data reconstruct positive integers `A,B` exactly when

```text
D² = (4Q−S²)/3
```

is a square: `1/4<Q/S²<1` gives `0<D<S`, and since `S` is odd, any integral square root `D` is odd; then `A=(S+D)/2`, `B=(S−D)/2` are positive integers with the desired `S,Q`. In this family `gcd(S,Q)=3` and `v₃(Q)=1`, so `gcd(A,B)=1`; `A³+B³=SQ=C^p` then gives pairwise coprimality with `C` as well.


There is a clean reason the square condition cannot hold in U727's target range. Here the full `c1=3^(3k)` has 3-free part `1`. If `D²` were a square, the reconstructed pair would be a primitive Beal solution, and U727's exact factorization would give `c1=bδ_E=1`, hence `b=δ_E=±1` and `U_p=δ_E^p=±1`. U744 checks that the resulting Lucas pair is regular; the Bilu–Hanrot–Voutier theorem gives a primitive divisor of `U_p` for `p>30`, contradiction. Thus for this constructed family the square condition is impossible in the target `p>10^9` range. This is a special-family exclusion only; actual Beal solutions may have arbitrary 3-free `c1`.

The factor-data family is an exact obstruction to using only the weaker support, height, and local-congruence conditions, with no novelty claim: it realizes unbounded `C` and fixed kernel, while the missing square condition removes this particular family in the target range.

## Local pth-power and square compatibility

The corrected U735 auxiliary-prime conditions also admit simultaneous local compatibility. For a prime ℓ, set (t=A/B\in\mathbb F_\ell) and

\[
R(t)=\frac{t^2-t+1}{(t+1)^2}.
\]

In the 3-divisible branch, U735 requires (R(t)/27) to be a pth power. The value (R(t)=27) reduces to

\[
26t^2+55t+26=0,
\]

whose discriminant is (321). Choose primes ℓ that split completely in (\mathbb Q(\zeta_{2p},\sqrt{321})); Chebotarev gives infinitely many, and each satisfies ℓ=2kp+1 with (321) a square modulo ℓ. Then this quadratic has a root (t), (R(t)/27=1) is a pth power, and

\[
\left(\frac{A-B}{A+B}\right)^2
=\frac{4R(t)-1}{3}=\frac{107}{3}=\frac{321}{9}
\]

is also a square modulo ℓ. This checks local compatibility of the corrected coset condition and the D-square condition at infinitely many auxiliary primes. It does not make the corresponding global integer (D^2=(4Q-S^2)/3) a square and does not give a Beal solution.
