# U131 — Signature (2m, 2n, 3), m, n ≥ 4: closed via ℤ[i] and Bennett–Skinner

**Status: VERIFICATION_REQUIRED.** Steps S1–S5, S8 are elementary and exact; S6/S7 invoke a
peer-reviewed theorem read from its primary source (saved in `references/U130/`). Nothing here is
machine-checked yet; the Lean obligations are listed at the end. This does **not** resolve Beal.

## Statement

> There is no Beal counterexample $A^{2m}+B^{2n}=C^3$ with $m \ge 4$, $n \ge 4$.

## Chain

| step | content | status |
|---|---|---|
| S1 | $x=2m$, $y=2n$ both even ⟹ $C$ odd | kernel-verified `not_both_exponents_even_of_even_C` |
| S2 | $a=A^m$, $b=B^n$: $a^2+b^2=C^3$, $\gcd(a,b)=1$, $C$ odd ⟹ $a+bi$, $a-bi$ coprime in $\mathbb{Z}[i]$ | exact (a common prime divides $2a$, $2b$, $C^3$) |
| S3 | $\mathbb{Z}[i]$ UFD, every unit is a cube ⟹ $a+bi=(u+vi)^3$, so $a=\lvert u(u^2-3v^2)\rvert$, $b=\lvert v(3u^2-v^2)\rvert$, $\gcd(u,v)=1$ | exact; cross-checked: all 126 coprime $a^2+b^2=C^3$, $C<400$ odd, arise this way |
| S4 | $\gcd(u,u^2-3v^2)=\gcd(u,3)$, $\gcd(v,3u^2-v^2)=\gcd(v,3)$; at most one of $u,v$ divisible by 3 | exact; 0 violations $u,v<300$ |
| S5 | $3\nmid u$ ⟹ $u=s^m$, $u^2-3v^2=\pm t^m$, $(s,t,v)$ nonzero pairwise coprime, $3\nmid st$ ⟹ $(s^2)^m+(\mp t)^m=3v^2$ | exact |
| S6 | **Bennett–Skinner, Canad. J. Math. 56 (2004) 23–54, Thm 1.1:** for integer $n\ge4$ and $C\in\{1,2,3,5,6,10,11,13,17\}$, $x^n+y^n=Cz^2$ has no nonzero pairwise coprime solutions except the listed ones — none with $C=3$. Applied with $n=m\ge4$. | primary source, quoted verbatim in `references/U130/bennett_skinner.txt` lines 73–83 |
| S7 | $3\nmid v$ ⟹ $(p^2)^n+(\mp q)^n=3u^2$, forbidden for $n\ge4$ | symmetric |
| S8 | at most one of $u,v$ is divisible by 3, so S6 or S7 applies | exact |

Consistency checks of my reading of S6: exact search of $x^n+y^n=3z^2$, $3\le n\le 9$, $\lvert x\rvert,\lvert y\rvert\le150$
finds solutions **only for $n=3$** — $(11,-2,21)$ and $(83,61,516)$ — and none for $4\le n\le 9$.
That is exactly why the theorem starts at $n\ge4$ and why $m=3$ ($x=6$) is *not* covered here.

## Relation to the literature (survey arXiv:2412.11933, Table 1.1)

Solved rows touching this family: $(n,n,3)$, $n\ge3$ [55, 117]; $(4,2n,3)^*$, $n\ge2$ [9];
$(2j,2k,n)^*$, $j,k\ge5$ **prime**, $n\in\{3,5,7,11,13\}$ [1 = Anni–Siksek 2016, 20 = Billerey–Chen–Dembélé–Dieulefait–Freitas 2023].

The chain above covers all **integers** $m,n\ge4$, so it also reaches e.g. $(8,12,3)$, $(12,18,3)$,
$(8,16,3)$ — pairs where neither $m$ nor $n$ has a prime factor $\ge5$ and $m\ne n$, which no listed row
covers. Whether this is already in [9] (Bennett–Chen–Dahmen–Yazdani, *Generalized Fermat equations: a
miscellany*, 2015) is an **open obligation**; the survey table does not list it. No novelty is claimed
until that is checked.

## What is NOT covered

- $m\in\{2,3\}$ or $n\in\{2,3\}$: $(4,2n,3)$ is solved in [9]; $(6,2n,3)$ with $3\nmid u$ leads to
  $s^6\mp t^3=3v^2$ where $x^3+y^3=3z^2$ has genuine solutions, so BS gives nothing.
- $z\ge5$ odd: the $\mathbb{Z}[i]$ step still gives $a+bi=(u+vi)^z$, but $\mathrm{Re}$ no longer
  factors as $u\cdot(\text{quadratic})$ with a coprime cofactor of the BS shape.
- The $3\mid u$ (resp. $3\mid v$) branch is never needed here because the *other* side is killed;
  it would be needed only if one exponent were $\le3$.

## Jev usage this cycle

Routing (`route_U131`, `route_U131b`): chose $r=3$, $m\ne n$; then chose the $3\mid u$ branch first
(0.63) — on execution that branch turned out to be unnecessary, as recorded above. Dependency audit
(`C047_audit_S1..S9`): flagged S1 (2.48), S6 (2.35), S8 (2.16) as most likely to hide a gap; each
was re-derived by hand above and found sound (S1 is a direct instance of a kernel theorem; S6's
pairwise-coprimality convention $3\nmid xy$ is met because $3\nmid s$ and $t^m\equiv u^2\not\equiv0$).
All 645+ Jev results remain `HYPOTHESIS_ONLY`.

## Lean obligations (to move to PARTIAL_RESULT with a kernel-checked chain modulo S6)

1. S4 as a lemma on ℕ.
2. S2–S3 via mathlib `GaussianInt` (`Zsqrtd (-1)`), Euclidean domain, units, and coprime cube ⟹ cube.
3. The assembly S1–S8 with S6 as an explicit **named hypothesis** (no `axiom`), so the dependency is visible in `#print axioms`.

## U132 addendum — literature resolution and first Lean pieces

**BCDY 2015 read from primary source** (`references/U130/bcdy.txt`, IJNT 11(1) 2015 1–28):
- §4.1 uses *exactly* the mechanism of this chain — parametrisation (7) $(x,y,z)=(s(s^2-3t^2),\,t(3s^2-t^2),\,s^2+t^2)$
  plus Bennett–Skinner Thm 1.1 [their ref 8] — to prove **Prop. 16**: $a^2+b^{2n}=c^3$ forces $b\equiv3\pmod 6$
  (the $\delta=0$ branch, $3\nmid b$, is killed by BS; the $\delta=1$ branch is the hard one).
- **Prop. 18 / Theorem 2:** $(2m,2n,3)$ solved for $m\ge2$ and $n\equiv3\pmod4$ only. **Table 1** lists
  $(4,2n,3)$, $n\ge2$; **Table 3** lists $(2m,2n,3)$ with "$m\ge2$ and $n\equiv-1\pmod4$".
- Neither BCDY nor the 2024 survey states $(2m,2n,3)$ for all $m,n\ge4$.

The observation this chain adds is only: when **both** $a$ and $b$ are perfect powers, $3$ divides at
most one of $s,t$, so the $\delta=0$ branch — the one BS handles — is available on at least one side.
Jev's status call (`route_U132b`, HYPOTHESIS_ONLY): "new stated theorem, two-line corollary of
published tools" (0.91). I record it as an *unstated corollary*, not as a discovery.

**Lean (this cycle), both axiom-free:**
- `prime_dvd_u_and_cofactor_eq_three` — S4: a prime dividing $u$ and $u^2-3v^2$ with $\gcd(u,v)=1$ is $3$.
- `three_not_dvd_sum_sq` — a sum of two squares coprime to 3 is not divisible by 3 (why even $m$ is trivial in S6).

**Open worry being checked now (COUNTERSEARCH):** BS Thm 1.1 states "$n\ge4$ an integer". For
$m=3^k$ ($9, 27,\dots$) the reduction to a prime exponent lands on $n=3$, where $x^3+y^3=3z^2$ *has*
solutions. Whether BS's proof covers $n=9$ for $C=3$ must be confirmed from their text before the
chain is used for $m$ or $n$ a power of 3.

**Worry closed (BS §7, lines 1150–1200 of the extracted text):** Theorem 1.1 is proved for primes
$\ge7$ by the modular method and for $n\in\{4,5,6,9\}$, $C\in\{2,3,5,6,10,11,13,17\}$ by appeal to
Bruin [their ref 6]. Every integer $n\ge4$ has a divisor in $\{4,6,9\}$ or a prime divisor $\ge5$
(exact check to $2\cdot10^5$: no exceptions; proof: if $4\nmid n$ and no prime $\ge5$ divides $n$
then $n=2^a3^b$ with $a\le1$, $n\ge4$, so $6\mid n$ or $9\mid n$), and $x^n=(x^{n/d})^d$ preserves
pairwise coprimality. So S6 applies to every integer $m\ge4$, including $m=3^k$.

## U134 — FLAW FOUND in S5 while preparing the Lean assembly, and repaired

**Flaw.** S5 wrote $(s^2)^m+(\mp t)^m=3v^2$ from $u^2-3v^2=\pm t^m$. For **even** $m$ this is wrong:
$(\mp t)^m=t^m$, and the equation actually obtained is $s^{2m}-t^m=3v^2$ (the sign $u^2-3v^2=-t^m$ is
impossible mod 3 since $s^{2m}\equiv t^m\equiv1$). A *difference* of $m$-th powers is not the
Bennett–Skinner shape, so S6 does not apply to even $m$. The same holds for even $n$ on the Im side.

**Repair.** Even $m$ means $4\mid 2m$, so $A^{2m}=(A^{m/2})^4$ and the counterexample has signature
$(4,2n,3)$ with coprime bases $(A^{m/2},B,C)$ — excluded by **BCDY 2015, Theorem 1** (Table 1 row
$(4,2n,3)$, $n\ge2$; primary source `references/U130/bcdy.txt` lines 107–111). Symmetrically for even $n$.
For $m,n$ both odd (hence $\ge5$) the original chain is correct: $u^2-3v^2=\varepsilon t^m$ gives
$(s^2)^m+(-\varepsilon t)^m=3v^2$ because $m$ is odd.

**Corrected statement and dependencies.**
> No Beal counterexample of signature $(2m,2n,3)$ with $m,n\ge4$.
> Dependencies: kernel theorems of this repo; the $\mathbb{Z}[i]$ cube step (S2–S3, exact, Lean pending);
> Bennett–Skinner 2004 Thm 1.1 ($C=3$, odd $n\ge5$); BCDY 2015 Thm 1 ($(4,2n,3)$).

Found by hand while writing the Lean statement — before any kernel check — which is the point of
formalising: the sign of $(\mp t)^m$ is exactly what a proof assistant refuses to wave through.

## U134 (cont.) — kernel-checked assembly: `formal/Beal/EvenEvenThree.lean`

```
'Beal.no_counterexample_even_even_three' depends on axioms: [propext, Classical.choice, Quot.sound]
'Beal.side_odd'                          depends on axioms: [propext, Classical.choice, Quot.sound]
'Beal.int_factor_pow'                    depends on axioms: [propext, Classical.choice, Quot.sound]
```
0 `sorry`, no custom axioms. The three external inputs are **named hypotheses** in the statement:

```lean
theorem no_counterexample_even_even_three
    (hZ : GaussianCubeStep) (hBS : BennettSkinnerThree) (hBCDY : BCDYFourTwoNThree)
    {A B C m n : ℕ} (hm : 4 ≤ m) (hn : 4 ≤ n)
    (h : IsBealCounterexample A B C (2 * m) (2 * n) 3) : False
```
Proved in the kernel: the odd-`C` step, the even-`m`/even-`n` reduction to `(4,2n,3)`, the sign
analysis for odd `m` (the U134 flaw), `gcd(u, u²−3v²) = 1` when `3 ∤ u`, coprime product ⟹ `±` powers
(`exists_associated_pow_of_mul_eq_pow`), all coprimality side conditions of Bennett–Skinner, and the
"3 divides at most one of `u, v`" case split.

**Statement-fidelity screen (Jev, `C047_fidelity_*`, HYPOTHESIS_ONLY):** flagged `GaussianCubeStep`
for units (1.62) and `BennettSkinnerThree` for the coprimality convention (1.61). Hand check: units of
ℤ[i] are all cubes, so the sign is absorbed into `u+vi` and the exact equalities are faithful; the
Lean BS hypothesis demands `x, y` coprime to `3z` (the paper's `aA, bB, cC` convention), which is at
least as strong a side condition as the paper's, so the hypothesis assumed is *weaker or equal* to the
published theorem — safe in the right direction.

Honest status: **VERIFICATION_REQUIRED** — the chain is kernel-checked *relative to* two published
theorems and one classical ℤ[i] step that is exact on paper but not yet in mathlib terms.

## U136 — `GaussianCubeStep` discharged in mathlib: `formal/Beal/GaussianCube.lean`

```
'Beal.gaussianCubeStep'                    depends on axioms: [propext, Classical.choice, Quot.sound]
'Beal.no_counterexample_even_even_three''  depends on axioms: [propext, Classical.choice, Quot.sound]
```
0 `sorry`. Proof in the kernel: `α = a + bi` and `star α` have a common divisor `g` only if
`g ∣ 2` (Bezout from `IsCoprime a b`) and `g ∣ c³`, so `norm g ∣ gcd(4, c⁶) = 1` (`c` odd) and `g` is a
unit; with `α · star α = c³` in the UFD `ℤ[i]` (`UniqueFactorizationMonoid.toGCDMonoid`,
`exists_associated_pow_of_mul_eq_pow`) `α` is a unit times a cube; every unit satisfies `ε⁴ = 1`
(norm-1 case analysis), hence `ε = (ε⁻¹)³` and `α = (u+vi)³`; `gcd(u,v) = 1` is inherited from
`gcd(a,b) = 1`. The `(2m,2n,3)` theorem now depends on **exactly two** named external hypotheses:
`BennettSkinnerThree` and `BCDYFourTwoNThree`.

## U145–U148 — the `(p, p, r)` chain and its literature frontier

`formal/Beal/SameOddPrime.lean` (standard axioms, 0 sorry, no external hypotheses):
`ppr_factorisation` ((A+B)·S = C^r, common divisors of A+B and S divide p), `ppr_coprime_branch`
(p ∤ A+B ⟹ A+B = d^r, S = e^r), `ppr_padic_branch` (p ∣ A+B ⟹ v_p(A+B)+1 = r·v_p(C), v_p(S) = 1,
via mathlib's Lifting-the-Exponent `padicValNat.pow_add_pow`).

Literature (C056): (p,p,p), (p,p,3) closed for all p; (3,3,r) closed to r ≤ 10⁹ and in residue
classes; (5,5,7), (5,5,19), (7,7,5) closed; the rest of (p,p,r), r ≥ 5, is open and begins exactly
at the Thue-type equation S = e^r where the kernel chain stops.

## U151 — `(6, 2n, 3)` closed and `(2m, 2n, 3)` completed for all `m, n ≥ 2`

New ingredient: a rank-0 elliptic curve. On a `3`-free side with exponent `3`, the reduction gives
$3v^2 = s^6 - \varepsilon t^3$, $s \ne 0$; dehomogenising ($T=-\varepsilon t/s^2$, $V=v/s^3$) puts
$(3T, 9V)$ on $Y^2 = X^3 + 27$. That curve is **LMFDB 144.a4**: rank 0, torsion $\mathbb{Z}/2$
generated by $(-3,0)$; PARI/GP 2.17 independently: conductor 144, torsion $[2]$ from $(-3,0)$,
2-descent rank upper bound 0 (unconditional), analytic rank 0
(`code/U151_mordell27.gp`, output saved). So $V = 0$, $v = 0$ — contradiction.

Case analysis for `(6, 2n, 3)`: `3 ∤ u` ⟹ curve on the `Re` side; `3 ∣ u` ⟹ `3 ∤ v` and on the `Im`
side: `n` even ⟹ BCDY `(4,2n,3)` (via `B^{2n} = (B^{n/2})^4`, the U134 sign lesson), `n = 3` ⟹ curve,
odd `n ≥ 5` ⟹ Bennett–Skinner. Kernel-checked: `no_counterexample_six_two_n_three`
(`formal/Beal/SixTwoNThree.lean`, standard axioms, 0 sorry) relative to `BennettSkinnerThree`,
`BCDYFourTwoNThree`, `Mordell27`.

Why BCDY did not have it: their Prop. 18 uses one side only and needs $n \equiv 3 \pmod 4$; using
that *both* summands are powers makes the good side always available, and the exponent-3 side needs
only this rank-0 curve.

Status: VERIFICATION_REQUIRED (two published theorems + one LMFDB/PARI rank fact as named hypotheses).
