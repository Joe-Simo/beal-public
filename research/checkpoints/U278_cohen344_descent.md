> **[U314/U315 UPDATE — 2026-09-18]**
>
> 1. The **same-parity branch is now fully machine-checked** with no prose step:
>    `Beal.three_four_four_same_parity` in `formal/Beal/ThreeFourFour.lean`, axioms
>    `[propext, Classical.choice, Quot.sound]`, sole external input mathlib's `fermatLastTheoremThree`.
>
> 2. **The elliptic-Chabauty reduction below is SUPERSEDED.** The opposite-parity branch does not
>    need it. When exactly one of `B, C` is even, all three factors of `A³ = (C−B)(C+B)(C²+B²)` are
>    **odd**, hence pairwise coprime and each a cube outright; the identity
>    `(C−B)² + (C+B)² = 2(C²+B²)` turns the branch into **Euler's equation** `a³ + b³ = 2c³`. The
>    reduction is machine-checked as `Beal.opposite_parity_reduction`. The Mordell-curve work below
>    (rank 1, generator `(13,35)`, the `120 ∣ n` sieve) is correct and preserved — it is simply not
>    needed. Recorded as pool C172.
>
> **Still open:** Euler's theorem is not in mathlib, so the opposite-parity branch is reduced, not
> closed. And by C157 none of this reaches Beal's open core.

# U271–U278: the `(3,4,4)` input, reduced

**Beal's conjecture is not solved, and nothing here closes `(3,4,4)`.** This records an explicit
reduction of the one unauditable component of the open-core statement, together with everything
computed about it.

## Why this input

`final_residual` (the theorem stating what remains open) takes thirteen named hypotheses. Twelve
were audited faithful against primary sources (C100, C104). The thirteenth, `InstanceRows`, has a
component `cohen344` — the claim that `A³ + B⁴ = C⁴` has no coprime positive solution — attributed
to Cohen, *Number Theory II*, Prop. 14.6.6. That book is not available at zero budget, so the
claim was **unaudited** (C142). Rather than leave it, the input was attacked directly.

## The descent (C143)

`A³ = C⁴ − B⁴ = (C−B)(C+B)(C²+B²)`. With `gcd(B,C)=1` and `B, C` of **opposite parity** the three
factors are pairwise coprime, so each is a cube:
$$C-B=r^3,\qquad C+B=s^3,\qquad C^2+B^2=t^3,\qquad rst=A .$$
Then `2C = r³+s³`, `2B = s³−r³`, and substituting into `C²+B²=t³`:
$$\frac{(r^3+s^3)^2+(s^3-r^3)^2}{4}=\frac{r^6+s^6}{2}=t^3 \quad\Longrightarrow\quad r^6+s^6=2t^3 ,$$
verified symbolically. So this branch is signature `(6,6,3)` **with coefficient 2** — not covered
by any row held in `references/U130/`.

## Reduction to one form (C144)

`r⁶+s⁶ = (r²+s²)(r⁴−r²s²+s⁴)`, the second factor odd, gcd dividing 3. On the branch where 3 does
not divide: `r²+s² = 2u³` and `r⁴−r²s²+s⁴ = v³`. With `p=(r+s)/2`, `q=(r−s)/2` this gives
`p²+q² = u³` — **exactly `GaussianCubeStep`, which is proved in `formal/Beal/GaussianCube.lean`**,
not assumed. Hence `p = a(a²−3b²)`, `q = b(3a²−b²)`, so
$$r=a^3+3a^2b-3ab^2-b^3,\qquad s=a^3-3a^2b-3ab^2+b^3,$$
and the branch reduces to: the degree-12 form
$$W(a,b)=a^{12}+114a^{10}b^2-705a^8b^4+1436a^6b^6-705a^4b^8+114a^2b^{10}+b^{12}$$
is never a non-trivial cube. Exact search `|a|,|b| ≤ 60`: four hits, all with `|r|=|s|=1`.

## What does not work (C145)

No congruence closes it. At `m = 7, 9, 13, 19, 27, 31, 37, 43, 63, 133` the admissible values of
`W` always meet the cube residues. `W = v³` is a genuine Thue-type equation and will not yield to
a residue obstruction.

## The field (C146)

`W` is **irreducible over ℚ**. Substituting `X = a²/b²` gives `p(X) = X⁶+114X⁵−705X⁴+1436X³
−705X²+114X+1`, irreducible, discriminant `2⁶²·3¹¹`. It is palindromic, so `Z = X+1/X` reduces it
to `Z³+114Z²−708Z+1208`, whose real root is exactly `−38 − 28·3^{1/3} − 20·3^{2/3}`. The natural
field is the pure cubic `ℚ(3^{1/3})`.

## What does work (C147–C149)

* **PARI's Thue solver reaches this form.** `thue` is complete for each fixed right-hand side;
  over all cubes `w³`, `w ≤ 60`, there are 32 solutions in total and **none** with `u, v` both
  nonzero coprime squares.
* **The branch is effectively finite.** Dehomogenised at `v=1` it is the superelliptic curve
  `w³ = p(u)`, `p` squarefree of degree 6, genus 4. Integral points on `y³=f(x)` with `f`
  squarefree of degree ≥ 3 are effectively bounded (Baker; LeVeque). Direct scan `|u| ≤ 20000`:
  exactly two integral points, `(0,1)` and `(3,16)` with `p(3)=4096=16³`, and **neither is
  admissible** since `3` is not a square.
* **The descent obstruction is absent.** `ℚ(3^{1/3})`: discriminant `−243`, class number 1, unit
  rank 1. The sextic field: discriminant `2⁶·3¹¹`, **class number 1**, signature `[2,2]`, unit
  rank 3, regulator `38.994…`. Since `3 ∤ h`, the ideal `(u − θv)` is a cube outright and
  `u − θv = ε·γ³` with `ε` in a finite set of cube cosets.

## The other two branches, resolved (C151, C152)

* **Same parity** (`B, C` both odd) — **closed unconditionally by FLT3**. `v₂(C²+B²)=1`; exactly
  one of `C∓B` has `v₂=1`, the other `v₂=k≥2`; `3 ∣ k+2` forces `k ≡ 1 (mod 3)`, so `4^{k-1}` is a
  cube; the three odd parts are pairwise coprime hence cubes; substituting gives
  `(μ²)³ + (λν²)³ = τ³`, impossible. Closing step machine-checked as
  `Beal.no_sixth_power_cube_relation` in `formal/Beal/ThreeFourFour.lean`, with
  `Beal.four_pow_is_cube`. Numerically: zero violations over all odd coprime `1 ≤ B < C < 300`
  (9,116 pairs).
* **`3 ∣ gcd`** — **empty**. Squares mod 3 are `0, 1`, so `3 ∣ r²+s²` forces `3 ∣ r` and `3 ∣ s`.
  Machine-checked as `Beal.three_not_dvd_sq_add_sq` via `decide` over `ZMod 3`.

So the input reduces to **one** surviving condition: the opposite-parity branch with `d = 1`.

## The survivor, as sharply as it goes (C153–C156)

`p` is palindromic, so `w³ = p(u)` carries `u ↦ 1/u`, `w ↦ w/u²`. With `z = u + 1/u`, `W = w/u`:
$$W^3 = z^3 + 114z^2 - 708z + 1208,$$
a plane cubic — **genus 1**. It is the Mordell curve `y² = x³ − 972`: conductor 972, `j = 0`,
trivial torsion, **rank 1**, generator `(13,35)`; integral points to height `10⁷` are `(13,±35)`.

*Cross-check*: the affine rational point `(z,W) = (10/3, 16/3)` (verified exactly,
`q(10/3) = 4096/27`) pulls back to `u = 3` — the same point the direct scan of C148 found as
`(u,w) = (3,16)`. Two routes, one answer. It is inadmissible since `3` is not a square.

The branch needs `u = a²`, `v = b²`, i.e. `z = y² − 2` with `y = h + 1/h`. Substituting gives
`W³ = Y³+108Y²−1152Y+3072` with `Y = y²` — but that is `q(Y−2)`, a **shift**, so the same curve.
The square condition is the entire remaining content. A direct rational search on
`W³ = y⁶+108y⁴−1152y²+3072` over `|m| ≤ 300`, `n ≤ 300` finds nothing, **but has no positive
control** (the degenerate `a=b=1` gives `r=0`), so it is weak evidence only.

**The obligation, stated exactly:** find the rational points on `y² = x³ − 972` whose `Y`-coordinate
is a perfect square. That is elliptic Chabauty over a quadratic field — Bruin's method, the tool
Poonen–Schaefer–Stoll and Siksek–Stoll used for `(2,3,7)` and `(3,4,5)`. Not available at zero
budget here.

## The survivor, computationally (C160–C167)

Four models of the branch all give the **same** elliptic curve `y² = x³ − 972` (conductor 972,
rank 1, trivial torsion, generator `(13,35)`): the cubic `W³ = Q(Y)`, the shifted cubic in
`Y = y²`, the quartic `y² = D(s)` with `D(s) = -3s(s³-144s²-2304s-12288)`, and the cubic
`w² = 36864t³+6912t²+432t-3` obtained from `s = 1/t`. **No reformulation escapes it** (C163).

The recurring point `(Y,W) = (16/3, 16/3)` — found independently by an integral scan (C148), a
rational search on the quotient (C154) and a complete Thue enumeration (C161) — is the **tangency
of the line `W = Y`**, which passes through the rational point at infinity. All three methods were
bound to find it, and it is inadmissible each time because `3` is not a square (C162).

**Mordell–Weil enumeration.** Rank 1 and trivial torsion mean every rational point is `nP`, with
`P = (1024, 143360)` on the model `[0,6912,0,15925248,-4076863488]`, where `t = X/36864`. For
`n ≤ 40`, computing `Y` exactly and testing for a rational square gives **zero** admissible hits
(C164).

**Mordell–Weil sieve.** The tiny primes force `120 ∣ n`: `p = 5, 7` give `n` even, `11` gives
`4 ∣ n`, `13, 19` give `3 ∣ n`, `29` gives `5 ∣ n` (C166). Since `h(nP) = n²h(P)` with
`h(P) = 2.99936797…`, any admissible point has canonical height `≥ 120²h(P) = 43190.9`, so its
`x`-coordinate has about **37,500 decimal digits** (C167). That is why every bounded search here
found nothing, and those nulls are not evidence.

**Why the sieve cannot finish.** The class `n ≡ 0` always survives — it is the identity, where the
map degenerates — so the sieve can never exclude everything. It gives `n ≡ 0 (mod N)`; ruling out
`n = N, 2N, …` needs a *height bound*, which is what elliptic Chabauty supplies.

**The Chabauty prerequisite is satisfiable** (C165): elliptic Chabauty over `K = ℚ(√d)` needs
`rank_E(K) < 2`, i.e. the twist `y² = x³ − 972d³` of rank 0. That holds for
`d = -30, -23, -22, -15, -13, -11, -10, -1, 3, 5, 10` among squarefree `|d| ≤ 30`. PARI 2.17.4 has
no `ellintegralpoints` and no Chabauty, so the remaining obstruction is **tooling, not arithmetic**.

**Two false positives, both mine, both recorded.** C164: `sqrt()` returns a float and `issquare`
then tests a real, giving spurious hits; fixed with `issquare(D,&r)`, exact on rationals. C166: a
termination test read "one surviving class `0 mod 2`" as "only `n = 0`", when it means `n` even.

## What remains

1. The unit-coset enumeration: rank 3 and torsion 2 give at most 27 cosets up to torsion, hence a
   few dozen Thue-type equations over the sextic field. **Not run** — needs a Thue solver over a
   sextic field, beyond PARI's direct capability.
2. The branch where `3` divides `gcd(r²+s², r⁴−r²s²+s⁴)`.
3. The **same-parity** branch of the original descent (`B, C` both odd).
4. Every search here is bounded and proves nothing beyond its range.

Scripts: `code/U276_thue_cubes.gp`, `code/U277_superelliptic.gp`, `code/U278_sextic_descent.gp`.
