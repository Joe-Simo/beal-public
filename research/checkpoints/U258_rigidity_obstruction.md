> **[U309 CORRECTION — 2026-09-18] THE HEADLINE OF THIS CHECKPOINT IS WITHDRAWN.**
>
> The title claim — "no rigid object carries three independent Beal exponents" — is **refuted**
> by `code/U309_rigidity_countersearch.py`. The rigidity-index computations in this document are
> correct; their interpretation was not. The document silently identified
>
> * *local monodromy has **order** `x`* — what a Beal exponent forces — with
> * *local monodromy is **regular semisimple** with eigenvalues of order `x`* — what the
>   computations assume.
>
> These differ. A pseudoreflection `(n-1,1)` has order equal to the order of its one non-trivial
> eigenvalue, so it realises *any* order with only two distinct eigenvalues. The hypergeometric
> triple `((1^n),(1^n),(n-1,1))` has `rig = 2` at every rank and realises three pairwise distinct
> orders — `(3,4,5)` at `n = 3,4`, `(3,5,7)` at `n = 5`, `(3,7,11)` at `n = 6,7`.
>
> **Rigidity does not forbid three independent exponents.** What it forbids is three *regular
> semisimple* punctures beyond rank 2. Read everything below with that substitution. Propagated
> to `formal/Beal/Rigidity.lean`, the pool (C169), and memory, per the layering rule.

# U253–U258: why no rigid object carries three independent Beal exponents

**Beal's conjecture is not solved.** Nothing here is a step toward a proof. This is an exact,
partly machine-checked account of *one obstruction*, namely the survey's observation that no
Frey-type object is known for three independent exponents.

Setting: local systems on $\mathbb P^1 \setminus \{0,1,\infty\}$ of rank $n$ with semisimple local
monodromies whose eigenvalue multiplicities are the parts of three partitions of $n$. Katz's
rigidity index is
$$\mathrm{rig} \;=\; -n^2 + \sum_{i=1}^{3}\sum_j m_{ij}^2, \qquad \text{rigid} \iff \mathrm{rig}=2 .$$

## Face 1 — rigidity forces rank ≤ 2 (C120, C122)

If all three local monodromies are **regular semisimple** — which is what monodromy of order
$x,y,z$ acting with distinct eigenvalues gives — then every $m_{ij}=1$, so $\mathrm{rig}=-n^2+3n$,
and $\mathrm{rig}=2 \iff n\in\{1,2\}$.

Machine-checked: `Beal.rigid_regular_semisimple_iff` (`formal/Beal/Rigidity.lean`).
Exhaustive enumeration over all multiplicity partitions, $n\le 14$, agrees: the number of rigid
triples is $1,3,10,22,78,151,392,870,1878,3635,7989,14463,28278$ for $n=2..14$, of which the
number that are regular semisimple at all three punctures is $1,0,0,\dots,0$.

## Face 2 — the eigenvalue budget is 2n+2, not 3n (C121)

For any rigid triple the total number of **distinct** local eigenvalues is at most $2n+2$.

* *Attained*: $((n-1,1),(1^n),(1^n))$ has squares summing to $(n-1)^2+1+n+n=n^2+2$, so
  $\mathrm{rig}=2$ identically — rigid at every rank, with budget $2+n+n=2n+2$.
  Machine-checked: `Beal.rigid_max_budget_attained`.
* *Bound*: a partition of $n$ into $k$ parts has $\sum m^2 \le (n-k+1)^2+(k-1)$. Rigidity forces
  the three sums to total $n^2+2$, and no $(k_1,k_2,k_3)$ with $\sum k_i > 2n+2$ satisfies the
  resulting inequality (checked exhaustively, $n\le 14$).

A monodromy of order $x$ at a puncture with $k$ distinct eigenvalues uses only $k$ of the $x$-th
roots of unity, so $k$ *is* the exponent-information budget there. The deficit is
$3n-(2n+2)=n-2$: the more room a rigid object has, the less of the exponents it sees per unit of
rank. Equality only at $n=2$.

## Face 3 — rank 2 over ℚ sees only the exponents 3, 4, 6 (C124)

For a rank-2 object **over ℚ**, the eigenvalue ratio at a puncture of order $x$ is a primitive
$x$-th root of unity generating a field of degree $\le 2$, so $\varphi(x)\le 2$, i.e.
$x\in\{1,2,3,4,6\}$. Beal-admissible ($x\ge 3$): $x\in\{3,4,6\}$, and only nine hyperbolic
triples. Every open-core exponent is excluded: $\varphi(5)=4$, $\varphi(7)=6$, $\varphi(11)=10$,
$\varphi(13)=12$.

Machine-checked for $x\le 30$: `Beal.totient_le_two_of_rank_two`.

## The dichotomy (C123)

Dropping rigidity does not help. For three regular-semisimple monodromies of rank $n$ the
accessory-parameter count is
$$2-\mathrm{rig} \;=\; n^2-3n+2 \;=\;(n-1)(n-2),$$
zero exactly at $n=1,2$. So:

| rank | canonical object? | three independent exponents? |
|---|---|---|
| $\le 2$ | yes (rigid) | **no** — only $3,4,6$ over ℚ |
| $\ge 3$ | **no** — moduli of dimension $(n-1)(n-2)>0$ | yes |

A Frey-type construction needs both. Machine-checked:
`Beal.moduli_dimension_regular_semisimple`, `Beal.moduli_dimension_eq_zero_iff`.

## Face 4 — the base field degree grows linearly in the exponent (C126)

Over a number field $F$ of degree $d$ the same argument gives $\varphi(x)\le 2d$, so
$$d \;\ge\; \varphi(x)/2, \qquad\text{and } d\ge (p-1)/2 \text{ for } x=p \text{ an odd prime.}$$
Sharp: $(p-1)/2$ is the degree of $\mathbb Q(\zeta_p)^+$, the field over which Darmon's Frey
abelian varieties for $(p,p,r)$ are built — the bound is attained by the literature's own
construction. So no rank-2 route is uniform in $p$.
Machine-checked: `Beal.minBaseDegree_prime`.

## Face 5 — three exponents at once: the degree is multiplicative (C127)

Carrying **all three** orders needs $\mathbb Q(\zeta_L)$ with $L=\operatorname{lcm}(x,y,z)$:
$$d \;\ge\; \varphi(\operatorname{lcm}(x,y,z))/2,$$
which for three distinct odd primes is $(p-1)(q-1)(r-1)/2$.

| signature | triple bound | single-exponent bound |
|---|---|---|
| $(3,5,7)$ | **24** | 3 |
| $(4,5,7)$ | **24** | 3 |
| $(3,5,11)$ | **40** | 5 |
| $(5,7,11)$ | **120** | 5 |
| $(7,11,13)$ | **360** | 6 |

The gap between the columns *is* the cost of independence. The equal-exponent case $(p,p,r)$ costs
$(p-1)(r-1)/2$, already multiplicative — which is why even Darmon's program is stated one
signature at a time.
Machine-checked dominance: `Beal.minBaseDegree_le_triple`; the multiplicativity of $\varphi$ is
computed, not formalised.

## Face 6 — at rank ≥ 3, only two exponents fit (C128)

Call a puncture **full** when its local monodromy is regular semisimple ($n$ distinct
eigenvalues), the state that can carry a whole exponent. For $n \ge 3$:

* at most **two** punctures are full, and
* when exactly two are, the third has **exactly 2** distinct eigenvalues.

Counting proof from Face 2: two full punctures consume $2n$ of the $2n+2$ budget, leaving at most
$2$; three would need $3n$, and $3n > 2n+2$ exactly when $n>2$. Exhaustive for $3\le n\le 12$.
Machine-checked: `Beal.three_full_exceeds_budget`, `Beal.two_full_leaves_two`.

Together with Face 1 the picture is complete. **Rank 2** carries all three exponents — that is the
classical hypergeometric case — but at the multiplicative field cost of Face 5. **Rank $\ge 3$**
buys nothing, because only two exponents fit.

## A constructive idea, tested and refuted (C129)

If two exponents fit, use **three** objects covering the three pairs. The saving is real:
$(3,5,7)$ costs degree $24$ as a triple but $4, 12, 6$ pairwise; $(7,11,13)$ costs $360$ against
$30, 60, 36$.

It buys nothing. A pairwise object for $(x,y)$ sees $A^x + B^y = N$ with $N$ unconstrained, and
that is vacuous: all $24{,}303$ coprime pairs with $A,B<200$ satisfy $A^3+B^5=N$ for some $N$,
while **zero** have that sum a perfect $7$th power. Each object is attached to an equation with
infinitely many solutions; the whole problem lives in the compatibility between them, which is
exactly the three-exponent data Face 6 forbids.

**Lemma kept:** a Frey-type object must see all three exponents *simultaneously*; splitting into
pairs is not a decomposition of the problem.

## Scope: which picture is bounded (C130)

Three **solved** signatures violate the Face-4/5 degree bounds: $(2,3,7)$ over $\mathbb Q$
(Poonen–Schaefer–Stoll) against a demand of degree $\ge 3$; $(3,4,5)$ over $\mathbb Q$
(Siksek–Stoll) against $\ge 2$; $(5,5,7)$ over $\mathbb Q(\sqrt 5)$ against $\ge 3$.

That is not a contradiction — it is the scope. Those proofs do **not** use an object whose local
monodromy orders are the exponents. The classical Frey curve carries the exponents through the
*valuation of its discriminant*, and level lowering removes them; PSS used a nonabelian descent to
twists of the Klein quartic, and the others descent plus Chabauty.

So everything above bounds the **hypergeometric / Darmon-style** picture, where the exponents
*are* the monodromy orders — the direction the survey names as live. It says nothing about the
discriminant-valuation Frey picture, which is precisely why that method still closes signatures,
one at a time. $(3,3,p)$ and $(4,4,p)$ over $\mathbb Q$ respect the bound, since
$\varphi(3)/2=\varphi(4)/2=1$.

## The other picture: classical Frey curves (C131–C134)

C130 showed the bounds above do not reach the discriminant-valuation Frey curve. That picture has
its own obstruction.

**Naive curve.** For $E: Y^2=X(X-a)(X+b)$ with $a=A^x$, $b=B^y$, $c=C^z$, $\Delta=16(abc)^2$, and
level lowering strips a bad prime $\ell$ iff $p \mid v_\ell(\Delta)$. Coprimality makes exactly
one of $A,B,C$ divisible by $\ell$, so the strip conditions are $p\mid 2x,\,2y,\,2z$, i.e.
$$p \mid 2\gcd(x,y,z).$$
For pairwise coprime exponents $\gcd=1$ and no odd $p$ works.

**Working curves** evade this by having discriminant a power of a *single* term — verified
symbolically: Kraus's $(3,3,p)$ curve $Y^2=X^3+3ABX+(B^3-A^3)$ has $\mathrm{disc}=-27(A^3+B^3)^2$,
and the $(2,3,n)$ curve $Y^2=X^3+3bX+2a$ has $\mathrm{disc}=-108(a^2+b^3)$.

**Which pairs admit such an identity?** Requiring both that $4P^3+27Q^2$ be a constant times a
power of $A^x+B^y$ **and** that $P,Q$ be functionally independent (nonzero Jacobian, so the model
separates $A$ from $B$ — the condition C133 found missing, without which the trinomial
$X^n+A^a+B^b$ makes the question vacuous), a symbolic search over degree $\le 4$ returns only
$(2,3)$, $(2,6)$, $(2,9)$, $(3,4)$, $(4,6)$, $(4,9)$ — all the $(2,3)$ model under
$A\mapsto A^k$, $B\mapsto B^m$ — together with the equal-exponent Kraus case $(3,3)$.

**So the classical picture absorbs only the pairs $(2,3)$ and $(n,n)$**, leaving the third
exponent as the modular one. Two carried, one free — the same count as Face 6, from unrelated
mathematics.

## The two live directions cost the same number (C137)

For two **distinct primes** $p,q$ the Face-5 minimal base-field degree $\varphi(pq)/2$ equals the
genus $(p-1)(q-1)/2$ of the Darmon–Granville pair-curve $u^p+v^q=1$.

| signature | field degrees | pair-curve genera |
|---|---|---|
| $(3,5,7)$ | 4, 12, 6 | 4, 12, 6 |
| $(5,7,11)$ | 12, 30, 20 | 12, 30, 20 |
| $(7,11,13)$ | 30, 60, 36 | 30, 60, 36 |

So the survey's two live directions — a unifying modular object, and effective Diophantine
geometry — meet the same barrier at the same size. Chabauty on the $(3,5,7)$ pair-curves would
need Jacobian rank below $4, 12, 6$.

**Scope.** The identity is about $\varphi$, not about $p-1$, so it holds only for **prime**
exponents: $\varphi(4\cdot 5)/2 = 4$ while $(4-1)(5-1)/2 = 6$, and there are 232 mismatches among
coprime pairs below 25. Machine-checked for the prime case: `Beal.totient_mul_primes`.

## What this does not show

It is an obstruction *inside the local-system setting*. A construction could evade it by using
non-regular-semisimple monodromy — which costs exponent information, quantified in Face 2 — or by
leaving this setting entirely, which is what Darmon's hypergeometric abelian varieties do. Those
still require the unproved modularity and big-image inputs recorded as **C083**.

It also explains the shape of the literature: the rank-2 route reaches a signature only after a
*reduction* (to $(p,p,p)$, $(n,n,2)$, $(n,n,3)$, …) that pushes the large exponent out of the
monodromy data — which is why every published closure is a reduction plus a finite check.

Scripts: `code/U253_rigidity_index.py`, `code/U254_rigid_eigenvalue_budget.py`.
Lean: `formal/Beal/Rigidity.lean` (0 `sorry`, standard axioms only).
