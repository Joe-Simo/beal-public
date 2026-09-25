# U744: Aggregate Lucas congruence and the forced mod-p-squared condition

**Date checked:** 2026-09-24

**Status:** necessary conditions in U727's residual `(3,3,p)` branch; no contradiction or global Beal proof. No novelty claim.

Assume U727's primitive residual branch with `p>10^9`, `p≡1 (mod 3)`, `3|C`, and `p∤C`. Keep its notation

```text
γ=α+βω,       T=γ+γbar=2α−β,       N=γγbar=α²−αβ+β²=c2,
U0=0, U1=1,  U_(n+2)=T U_(n+1)−N U_n,
U_p=(γ^p−γbar^p)/(γ−γbar)=δ_E^p.
```

Here `p∤β`, `p∤N`, and `3∤N`. The aggregate residue below must be proved directly; it does not follow just by multiplying the split `+1` and inert `−1` residue classes for prime divisors of `δ_E`.

## Aggregate congruence modulo `6p`

At `p`, Frobenius gives

```text
γ^p−γbar^p ≡ (γ−γbar)^p  (mod p).
```

The denominator `γ−γbar=β√−3` is a unit modulo `p`, since `p∤β` and `p≠3`. Therefore

```text
U_p ≡ (γ−γbar)^(p−1)
    = (−3β²)^((p−1)/2)
    ≡ (−3/p) ≡ 1  (mod p),
```

using `β^(p−1)≡1 (mod p)` and the splitting criterion `p≡1 (mod 3)`. Since `U_p=δ_E^p` and `x^p≡x (mod p)`, this gives `δ_E≡1 (mod p)`.

At 3, `β≡0`, `N≡α²≠0`, and

```text
U_p = Σ_(i=0)^(p−1) γ^(p−1−i) γbar^i ≡ p α^(p−1) ≡ 1 (mod 3).
```

At 2, U737's Kraus parity gives `C` odd. Thus `A^3+B^3` and `S=A+B` are odd; the exact identity `S=3βU_p` makes `U_p` odd, so `δ_E` is odd. Consequently

```text
δ_E ≡ 1 (mod 2),  δ_E ≡ 1 (mod 3),  δ_E ≡ 1 (mod p),
therefore δ_E ≡ 1 (mod 6p).
```

In particular, `c1=bδ_E≡b (mod 6p)` in U727's notation.

## The p-adic lift forced by the perfect power

Writing `δ_E=1+kp` immediately gives

```text
U_p = δ_E^p ≡ 1 (mod p²).
```

This has an explicit Fermat-quotient form. Since `p` splits in `K=Q(√−3)`, the quotient ring `O_K/(p²)` has two `Z/p²Z` components. Let `ζ` be either Hensel lift of a primitive cube root of unity modulo `p²`, and set

```text
g+ = α+βζ,       g− = α+βζ²,
f_p(u) = (u^(p−1)−1)/p  (mod p) for a p-adic unit u.
```

Both `g+` and `g−` are units, and `g+−g−` is a unit modulo `p`; these facts use `p∤N`, `p∤β`, and `p≠3`. Componentwise in `O_K/(p²)`,

```text
U_p ≡ 1 + p · (g+ f_p(g+) − g− f_p(g−))/(g+−g−)  (mod p²).
```

Thus a hypothetical Beal solution in this branch must satisfy

```text
g+ f_p(g+) ≡ g− f_p(g−)  (mod p).
```

This is a concrete Lucas/Fermat-quotient sieve condition, but the coefficients `α,β` vary with the hypothetical solution. No uniform theorem or consequence of the existing Beal identities has been found that makes the condition impossible. In the coefficient shape `β=3^(hp−2)b^p`, it can also be written as one polynomial congruence in `x=α/β (mod p)`:

```text
H_p(x) ≡ 2 f_p(3) (mod p),
H_p(x)=Σ_(k=1)^(p−1) (-1)^(k−1) L_k x^(p−k)/k,
L_k=1,0,−1 according as k≡1,0,2 (mod 3).
```

Here `L_k=(ω^k−ωbar^k)/(ω−ωbar) (mod p)`; the formula follows by expanding the split-component expression. A residue-level witness matching the other simple branch constraints is described below; it is not a Lucas perfect-power or Beal solution.

More explicitly, the binomial expansion gives

```text
U_p ≡ β^(p−1)(1+p H_p(x)) (mod p²).
```

For `f_p(u)=(u^(p−1)−1)/p (mod p)`, the exact coefficient shape `β=3^(hp−2)b^p`, with `p∤3b`, gives `f_p(β)≡−2f_p(3) (mod p)`. Therefore, within this branch, the polynomial condition is equivalent to the required lift:

```text
U_p ≡ 1 (mod p²)  iff  H_p(x) ≡ 2 f_p(3) (mod p).
```

## Relation to known Lucas perfect-power results

The Lucas sequence is nondegenerate: the only units in `Q(√−3)` are `±1,±ω,±ω²`; if `γ/γbar=1` then `β=0`, and each of the other five cases forces `3|N` from `v₃(β)=hp−2>0`. Both alternatives contradict the branch hypotheses. The proof below also establishes `gcd(T,N)=1`, while `N≠0` and `T²−4N=−3β²≠0`; hence the Lucas pair has the regularity required by the Bilu–Hanrot–Voutier primitive-divisor theorem. Since `p>10^9`, that theorem gives a primitive prime divisor of `U_p`, but does not say its valuation is one. A prime `q` with `q∥U_p` would contradict `U_p=δ_E^p`, because every prime valuation in a perfect `p`th power is divisible by `p`.

Bugeaud–Luca–Mignotte–Siksek's Conjecture 7 proposes that every sufficiently late term of a **fixed** nondegenerate Lucas sequence has a primary divisor (a primitive `q` with `q∥U_n`); the paper describes this as out of reach. Such a divisor immediately contradicts `U_p=δ_E^p`. Their proved Theorem 1 gives an effective upper bound `n<c(U,S)` for a perfect-power equation in a fixed recurrence, but the constant depends on the Lucas sequence. U727's coefficients vary with the hypothetical Beal solution, so neither result supplies the required uniform inequality `c(T,N,S)<p`. This identifies a precise missing uniform valuation theorem, not a proof of Beal. [Bugeaud–Luca–Mignotte–Siksek, Theorem 1 and Conjecture 7](https://samirsiksek.github.io/siksek.github.io/papers/lucasprod16.pdf); [Bilu–Hanrot–Voutier](https://doi.org/10.1515/crll.2001.080).

## Residue-level compatibility witness

Take `p=19`, `h=1`, `b=1`, `δ_E=1`, `β=3^17=129140163`, and `α=5β+19·33984256=1291401679`. Exact arithmetic gives

```text
T=2α−β ≡ 345 (mod 361),
N=α²−αβ+β² = 1517623654899151933 ≡ 91 (mod 361),
N ≡ 15 (mod 19),    N ≡ 1 (mod 3),
U_19 ≡ 1 (mod 361), U_19 ≡ 2 (mod 5).
```

Set `C=3N` and define the exact Eisenstein coefficients by `A+Bω=(1−ω)(α+βω)^19`. Direct integer arithmetic verifies `A,B>0`, `gcd(A,B,C)=1`, `v₂(A)=1`, `(A,B)≡(40,303) (mod 361)`, and `A³+B³≡C^19≡292 (mod 361)`. The equality fails over the integers, since `U_19≡2 (mod 5)` while `δ_E^19=1`. This shows the p-adic condition is compatible with the normalized parity, positivity, primitivity, and Kraus factorization constraints at this small exponent; it does not address the `p>10^9` tail or provide a global Lucas perfect power.

## Missing `q|N` case in the primitive-factor argument

For completeness, no prime `q|N` can divide `U_p`. First, `gcd(T,N)=1`: if `q|T,N` for a rational prime `q≠3`, then `β≡2α (mod q)` and `N≡3α² (mod q)`, so `q|α,β`. Hence `q^p` divides both Eisenstein coefficients of `(1−ω)γ^p=A+Bω`, forcing `q|A,B`, contrary to primitivity. The prime `q=3` cannot divide `N=c2` by U737. Now if `q|N`, then `q∤T`; reducing the Lucas recurrence modulo `q` gives `U_p≡T^(p−1)≠0 (mod q)`. This supplies the case needed before defining `γ/γbar` as a unit for the order argument in U727.

The aggregate congruence and the `q|N` recurrence check strengthen U727's necessary conditions. They do not bound `b`, `c2`, or the varying Lucas parameters, and do not exclude any global solution. The local residue witness is not a claim of existence of a Beal solution.

## Consequence for the Kraus trace-avoidance route

Every prime `q|δ_E` also divides `C`. Conditional on the residual representation statement, multiplicative reduction therefore gives `a_q(72a1)≡±(q+1) (mod p)`. For a split factor `q≡1 (mod 6p)`, this is `±2 (mod p)`, exactly the `q|C` alternative admitted by the Kraus sieve when `q≡1 (mod 2p)`. An inert factor `q≡−1 (mod 6p)` instead forces trace `0 (mod p)` and lies outside the sieve's stated `q≡1 (mod 2p)` progression; extending the local set to that inert multiplicative case still admits the forced trace. Thus no prime factor of `δ_E` itself supplies a trace-avoiding witness. The aggregate sign only imposes `sgn(δ_E)(−1)^(total inert valuation)=1`; it gives no individual factor class or control of the moving trace set. The exact admissible-set scope is audited in U733/U735.
