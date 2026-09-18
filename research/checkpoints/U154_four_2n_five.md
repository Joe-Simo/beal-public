# U154 — Signature (4, 2n, 5) for all n ≥ 2 (and (2m, 4, 5)): closed relative to two rank-0 curves

**Status: VERIFICATION_REQUIRED.** Kernel-assembled (`formal/Beal/FourTwoNFive.lean`, standard axioms,
0 sorry) relative to two named hypotheses on rational points of genus-1 quartics whose Jacobians are
LMFDB 400.g2 and 400.b2 (rank 0, torsion ℤ/2; independently PARI/GP 2-descent bound 0). Not a
resolution of Beal.

## Argument
1. $x=4$, $y=2n$ even ⟹ $C$ odd (kernel). $(A^2, B^n)$ are the coordinates of $w^5$, $w\in\mathbb{Z}[i]$,
   $\gcd(\operatorname{re} w, \operatorname{im} w)=1$ (kernel theorem `even_even_odd_reduction`).
2. $A^2 = u\,Q$, $Q = u^4-10u^2v^2+5v^4$, and $\gcd(u,Q)\mid 5$. Opposite parity of $u,v$ (kernel, via
   $\mathbb{Z}/2$: both odd would make $A^2$ and $B^n$ even).
3. $5\nmid u$: $u=\pm s^2$, $Q=\pm t^2$ (same sign).
   * $+$: $(v/s^2,\ t/s^4)$ lies on $C_1: W^2=5V^4-10V^2+1$; hypothesis `Quartic400g2` ⟹ $v=0$.
   * $-$: $t^2=-(s^8-10s^4v^2+5v^4)\equiv 7,11,15 \pmod{16}$ for $s+v$ odd — impossible (decided in `ZMod 16`).
4. $5\mid u$: $u=5u'$, $Q=5Q'$, $Q'=125u'^4-50u'^2v^2+v^4$, $u'Q'=(A/5)^2$, $\gcd(u',Q')=1$, $u'=\pm s^2$, $Q'=\pm t^2$.
   * $+$: $(5s^2/v,\ 5t/v^2)$ lies on $C_3: W^2=5(U^4-10U^2+5)$; hypothesis `Quartic400b2` ⟹ $u=0$.
   * $-$: $t^2=-(125s^8-50s^4v^2+v^4)$ impossible mod 16 (decided).
5. The $2n$ side is never used, so the theorem holds for every $n\ge1$; $n=1$ is $(2,4,5)$, consistent
   with Bennett–Ellenberg–Ng's $(2,4,n)$, $n\ge4$.

## Evidence
`code/U154_four_2n_five.gp` and `references/U130/four_2n_five_pari_output.txt` (four quartics; $C_2$ has
Jacobian rank 1 and is handled by the congruence; $C_4$ has no 2-adic points). Exact search: $\operatorname{re}(w^5)$
is never $\pm$ a square for coprime opposite-parity $u,v\le400$. LMFDB fetched for both Jacobians.

## Literature
Not found in BCDY 2015 Tables 1–3 nor in the 2024 survey; two web searches found nothing on
$x^4+y^{2n}=z^5$. Not claimed novel.
