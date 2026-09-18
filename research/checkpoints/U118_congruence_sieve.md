# U118: A congruence sieve from the verified necessary conditions

**Verification code**: `code/U118_congruence_obstruction.py`, `code/U118_sieve_smooth.py`
**Route selection**: Jev restart-triage over six materially new mechanisms
(`code/U118_restart_mechanisms.py`) ranked this first on new × executable × payoff.

## 1. The structural observation that makes it work

For $\gcd(A,m)=1$, the set $\{A^x \bmod m : x \ge 3\}$ is exactly the **cyclic subgroup
$\langle A\rangle \le (\mathbb Z/m)^\times$** — because $x \ge 3$ already sweeps a full period of
the powers of $A$. The exponent constraint $x \ge 3$ therefore costs nothing locally; what
constrains is the subgroup structure.

So a Beal counterexample forces, at every modulus $m$:
$$\exists\, a \in S_A,\ b \in S_B,\ c \in S_C \ \text{ with } a + b \equiv c \pmod m,$$
with $S_X = \langle X\rangle$ when $\gcd(X,m)=1$ and $S_X = \{0\}$ when $m \mid X$. Combined with
the **kernel-verified pairwise coprimality** of the bases — no prime divides two of $A,B,C$ — this
is a checkable local condition.

## 2. Results

| $m$ | coprime residue triples | admissible | **rejected** |
|---|---|---|---|
| 12 | 640 | 312 | 51.2% |
| 24 | 5,120 | 2,024 | 60.5% |
| 48 | 40,960 | 15,624 | 61.9% |
| 120 | 573,440 | 144,624 | 74.8% |
| 180 | 1,935,360 | 653,046 | 66.3% |
| **240** | **4,587,520** | **1,024,072** | **77.7%** |
| 360 | 15,482,880 | 3,881,788 | 74.9% |

No modulus admits **zero** triples, and none can: Beal has no purely local obstruction, so this
family of tests cannot prove the conjecture. That is a genuine negative result about the method,
established rather than assumed.

## 3. What it does give

A **counterexample-search sieve of a different kind from the ones in the literature.** Published
searches use double-modular *hashing* — compute $A^x + B^y$, reduce mod two machine-word primes,
compare against precomputed residues of $C^z$. This sieve instead rejects an $(A,B,C)$ **residue
class** before any power is computed, using only the subgroup structure and pairwise coprimality.

At $m = 240$ it discards **77.7%** of coprime residue classes. The constraining moduli are all
2-3-smooth ($12, 24, 48, 120, 240$), which is consistent with the known solutions' dependence on
small primes.

## 4. Honest limits

- It cannot prove Beal, for the reason in §2.
- The gain is a constant factor on an exponentially large search space — it does not change the
  asymptotics that U115 §6 identified as the reason computation cannot decide this problem.
- The rejection fraction is over *residue classes*, not over integers; the induced saving on a real
  search depends on how the search enumerates.

---

# Part II (M6): Why classical descent cannot close the all-even branch

**Verification code**: `code/U118_descent_step.py`

Jev ranked this mechanism highest on payoff (2.24). It is materially different from every blocked
route: Fermat-style infinite descent on the Pythagorean parametrisation, using no Frey curve, no
Chabauty and no abc.

## The descent step, derived and verified

From the kernel-verified `allEven_isPythagorean`, an all-even counterexample gives
$(A^r)^2 + (B^s)^2 = (C^t)^2$ primitive, so with $\gcd(m,n)=1$ of opposite parity
$$A^r = m^2-n^2,\qquad B^s = 2mn,\qquad C^t = m^2+n^2 .$$
The odd leg splits into coprime odd factors, giving $m-n = p^r$, $m+n = q^r$, $A = pq$, hence
$2m = q^r+p^r$, $2n = q^r-p^r$, and therefore
$$\boxed{\;C^t - B^s = p^{2r},\qquad C^t + B^s = q^{2r},\qquad 2C^t = p^{2r} + q^{2r}.\;}$$
Verified symbolically for $r = 2, 3, 5$: $m^2-n^2 = (pq)^r$, $2(m^2+n^2) = p^{2r}+q^{2r}$,
$2(2mn) = q^{2r}-p^{2r}$.

## Why it does not close

**The descent is not a self-map.** It sends
$$\text{signature } (2r,\,2s,\,2t) \;\longmapsto\; \text{signature } (2r,\,2r,\,t) \text{ with coefficient } 2 .$$
The two left exponents **diagonalise**, the right exponent **halves**, and a coefficient 2 appears.
Nothing strictly decreases while the equation stays fixed — which is exactly what infinite descent
requires.

Contrast Fermat's right-triangle theorem ($r = s = 2$, $t = 1$ here): there the descent returns a
solution of the **same** equation with a strictly smaller hypotenuse, so descent on that single
integer closes the argument. That is why the classical case succeeds and the general one does not.

## The number of available steps is $v_2(t)$ — and it is zero for this project's equation

Each step halves the right exponent, so the descent survives exactly $v_2(t)$ iterations before the
exponent turns odd and the all-even parametrisation that generated the step is no longer available:

| $2t$ | 4 | 8 | 16 | 24 | 32 | **34** | 64 |
|---|---|---|---|---|---|---|---|
| steps | 1 | 2 | 3 | 2 | 4 | **0** | 5 |

This project's weighted equation has $z = 17$, which is **odd** — so $v_2(17) = 0$ and **the
descent is unavailable at the very first step**. That is an independent explanation, in elementary
terms, of why the weighted route needed the modular machinery at all: the classical method does
not even start there.

## Status

M6 is **BLOCKED**, for a reason genuinely different from the modular obstruction of U114/U116.
There the failure is that a *hypothesis* cannot be satisfied; here it is that the descent is not a
self-map of a single equation. Two distinct failure mechanisms, which is what the exploration
policy asks us to accumulate rather than rediscover.

---

# Part III (M5): Which reduced signatures can this project account for?

**Verification code**: `code/U118_open_signatures.py`

Enumerating all reduced signatures $(x,y,z)$ with exponents in $\{3,4,5,7,11,13,17,19,23\}$ and
$x \le y$ (since $x,y$ are interchangeable but $z$ is not): **405 signatures**, of which this
project can point to a recorded result for **40**, leaving **365** unaccounted for.

Smallest unaccounted-for, by exponent sum: $(3,4,3)$, $(3,5,3)$, $(3,7,3)$, $(4,4,5)$, $(4,5,4)$,
$(3,4,7)$, $(4,5,5)$, $(5,5,4)$, $(3,5,7)$, …

## The caveat, which matters more than the count

**This enumeration measures what *this project* has recorded, not what the field knows.** The
literature states that the smallest *open* Beal signature is $(3,5,7)$ — yet my table lists
$(3,4,3)$, $(3,5,3)$ and others as unaccounted for at smaller exponent sums. The discrepancy is
not evidence that the literature is wrong; it is evidence that **more results exist than I have
encoded**, and those smaller signatures are almost certainly closed by work I have not yet read.

So the honest reading is inverted from what the table superficially suggests:

- it is **not** a list of open problems;
- it **is** a list of signatures this project cannot currently justify, and therefore a **reading
  list** — each entry below $(3,5,7)$ in exponent sum marks a result that exists and that we are
  missing.

Recording it that way is the point. A coverage table that overstates the open set is exactly the
failure mode this audit spent thirty cycles correcting in someone else's work, and I am not going
to reproduce it in my own.

## Status

M5 is complete and its output is a **literature gap list**, not a target list. The genuine frontier
remains $(3,5,7)$, per U114 Part II.

---

# Part IV (M3): Exactly where the ordering of ℤ must enter

**Verification code**: `code/U118_where_ordering_enters.py`; formalised in
`formal/Beal/Necessary.lean`.

Jev scored this mechanism highest on novelty (0.88). It turns the Gaussian obstruction from a
negative result into a **positive specification of what any proof must contain**.

## The question

Beal is false over $\mathbb Z[i]$, which is a PID. So unique factorisation is not the missing
ingredient. What does $\mathbb Z$ have that $\mathbb Z[i]$ lacks, and at which step is it used?

## The answer: positivity forbids cancellation

Over $\mathbb Z[i]$ the size of a sum can **collapse** relative to its summands, because summands
can oppose. The Helenius identity is exactly that:
$$N\bigl((-2+i)^3\bigr) = N\bigl((-2-i)^3\bigr) = 125, \qquad N(\text{sum}) = N(-4) = 16,$$
a **7.8-fold collapse**.

Over $\mathbb Z$ with positive bases this cannot happen, and the consequence is a tight window.
Kernel-verified in `Beal/Necessary.lean`:

```lean
theorem no_cancellation (h : IsBealCounterexample A B C x y z) :
    A ^ x < C ^ z ∧ B ^ y < C ^ z ∧ C ^ z ≤ 2 * max (A ^ x) (B ^ y)
```
```
'Beal.no_cancellation'       : [propext, Classical.choice, Quot.sound]
'Beal.no_cancellation_of_le' : [propext, Classical.choice, Quot.sound]
```

Taking $z$-th roots of $B^y < C^z \le 2B^y$ (with $A^x \le B^y$) gives
$$B^{y/z} \;<\; C \;\le\; 2^{1/z}\,B^{y/z}, \qquad 2^{1/z} \le 2^{1/3} = 1.2599\ldots$$
so **$C$ is pinned to within a factor of 1.26 of $B^{y/z}$**. Verified on the known
Fermat–Catalan solutions, where the ratio $C/B^{y/z}$ is $1.1339$, $1.0455$, $1.0129$, $1.0083$,
$1.0001$, $1.0005$ — every one inside the window.

## A correction made during formalisation

My first draft asserted the **strict** bound $C^z < 2\max(A^x,B^y)$. That is **false as stated**:
if $A^x = B^y$ then $C^z = 2B^y$ exactly. (The case cannot occur — coprimality forces $A=B=1$,
excluded by `not_eq_bases` — but the unconditional inequality is `≤`.) The proof assistant forced
the correction; the Python derivation had not.

## What this specifies

**Any proof of Beal must, at some step, compare sizes.** An argument that never does would apply
verbatim over $\mathbb Z[i]$, where the conclusion is false. That rules out, in advance, every
purely formal or factorisation-theoretic strategy — and it says what a successful proof must
contain, rather than merely what it cannot be.

It also explains why **linear forms in logarithms** is the natural effective tool here: taking
logarithms of $B^y < C^z \le 2B^y$ gives $0 < z\log C - y\log B \le \log 2$, which is exactly the
shape Baker's theory addresses.

---

# Part V (M4): Height constraints yield nothing new — and a self-correction

**Verification code**: `code/U118_m4_height.py`

## The linear form carries no independent information

Taking logarithms of the kernel-verified window $B^y < C^z \le 2B^y$ gives
$$0 < z\log C - y\log B \le \log 2,$$
which looks like a linear form in logarithms and therefore like an opening for Baker's theory.
It is not, because the form is **identically determined by the ratio of the summands**:
$$z\log C - y\log B \;=\; \log\frac{C^z}{B^y} \;=\; \log\!\left(1 + \frac{A^x}{B^y}\right).$$

Verified numerically to eight decimal places on the known solutions:

| solution | $z\log C - y\log B$ | $\log(1+A^x/B^y)$ |
|---|---|---|
| $17^7+76271^3=21063928^2$ | 0.00000092 | 0.00000092 |
| $1414^3+2213459^2=65^7$ | 0.00057687 | 0.00057687 |
| $43^8+96222^3=30042907^2$ | 0.01303440 | 0.01303440 |

So the linear form is small **exactly when $A^x \ll B^y$**, which is a restatement of the equation,
not a new constraint. M4 produces **no new obstruction**.

## A correction to my own output

The first run of `U118_m4_height.py` printed the commentary *"the linear form is NOT unusually small
— it is comfortably below $\log 2$ rather than near zero."* **That was wrong**, and the table it sat
above disproved it: the $17^7$ row has linear form $9.2\times10^{-7}$, which is very small indeed.
The correct statement is the one above — the form's size is exactly $\log(1+A^x/B^y)$ and therefore
carries no information beyond that ratio. Recorded because the error was mine and the data in my own
output contradicted my own gloss on it.

## Novel combination: M3 window × M1 congruence sieve

The two constraints are independent in kind — M3 restricts the real size of $C$, M1 its residue
class — so a search may impose both:

- M3 confines $C$ to $\bigl(B^{y/z},\,2^{1/z}B^{y/z}\bigr]$, relative width $2^{1/z}-1 \le 0.2599$;
- M1 then rejects 77.7% of surviving residue classes mod 240.

Combined survival $\approx 0.26 \times 0.223 = 0.058$, a **~17× reduction**.

**Honest limit**: a constant-factor speedup on an exponentially growing space. U115 §6 already
established that computation cannot decide Beal, and a 17× saving does not change that. It is a
search engineering improvement, not progress toward a proof, and must not be presented as one.

---

# Part VI (M2): Why the exponent 2 is distinguished — a sharp separation at 1/12

**Verification code**: `code/U118_m2_chi_separation.py`; formalised in `formal/Beal/Taxonomy.lean`.

Jev rated this mechanism hardest to execute (0.22). It turns out to admit a clean quantitative
answer, in exact rational arithmetic.

## The separation

With $\chi(p,q,r) = \tfrac1p + \tfrac1q + \tfrac1r - 1$:

| region | curvature |
|---|---|
| the ten **known** primitive hyperbolic solutions | $\lvert\chi\rvert \le 1/18$ — every one |
| every hyperbolic **Beal** signature ($\min \ge 3$) | $\lvert\chi\rvert \ge 1/12$ — every one, minimum at $(3,3,4)$ |

and $1/18 < 1/12$. **The two regions are separated by a gap containing no known solution.**

Exhaustive exact check over $3 \le p,q,r < 40$ confirms the minimum of $|\chi|$ on the Beal region
is exactly $1/12$, attained precisely at the permutations of $(3,3,4)$. The known solutions have
$|\chi| \in \{1/42, 1/24, 1/20, 1/18\}$.

## So the role of the exponent 2 is quantitative

An exponent 2 contributes $1/2$ to the reciprocal sum, which is what permits $\chi$ to sit close to
zero. With every exponent $\ge 3$ the reciprocal sum is at most 1, and once it drops below 1 it is
at most $11/12$. **That is precisely why every known solution has an exponent 2.**

## Formalised

The exact half is now kernel-verified, and strictly strengthens `curvature_upper_bound_beal`
(whose bound $E \le -3$ is weak once $pqr$ is large):

```lean
theorem curvature_sharp_bound (p q r : ℕ) (hp : p ≥ 3) (hq : q ≥ 3) (hr : r ≥ 3)
    (h_not_all_3 : ¬(p = 3 ∧ q = 3 ∧ r = 3)) :
    12 * (q * r + p * r + p * q) ≤ 11 * (p * q * r)
```
```
'Beal.curvature_sharp_bound' : [propext, Classical.choice, Quot.sound]
```
which is exactly $|\chi| \ge 1/12$. Equality at $(3,3,4)$ checked: $12 \cdot 33 = 396 = 11 \cdot 36$.

## An equivalent formulation of Beal

Combining with FLT for the parabolic case $(3,3,3)$:

> **Beal's conjecture $\iff$ there is no primitive solution with $\lvert\chi\rvert \ge 1/12$.**

## Honest status

The $|\chi| \ge 1/12$ half is **proved**. The other half — that no solution lives in that region —
**is** Beal's conjecture, restated. This sharpens the question and explains the exponent-2
phenomenon quantitatively; it does not answer it. The gap between $1/18$ and $1/12$ is an
observation about the known solution set, not a theorem about all solutions.

---

# Part VII (N1): Curvature stratification — a genuinely finite near-Euclidean family

**Verification code**: `code/U119_curvature_stratification.py`

## The stratification and its exact finiteness threshold

$|\chi| < T \iff \tfrac1x+\tfrac1y+\tfrac1z > 1-T$. With $x=y=3$ the sum is $\tfrac23 + \tfrac1z$,
so $z$ is bounded **iff $1-T > \tfrac23$**, i.e. **iff $T < 1/3$**.

So Beal splits at any $T < 1/3$ into a genuinely finite near-Euclidean family and an infinite
very-hyperbolic tail. Enumerated over reduced exponents ($\{4\} \cup$ odd primes, by the
kernel-verified reduction), with $x \le y$:

| $T$ | signatures with $1/12 \le |\chi| < T$ | status |
|---|---|---|
| $1/6$ | **4** | genuine total |
| $1/4$ | **13** | genuine total |
| $3/10$ | **29** | genuine total |
| $1/3$ | 173 | **truncated** — $z$ unbounded |

The thirteen signatures with $1/12 \le |\chi| < 1/4$, in full:

$(3,3,4)$, $(3,4,3)$ — $|\chi| = 1/12$ · $(3,3,5)$, $(3,5,3)$ — $2/15$ ·
$(3,4,4)$, $(4,4,3)$ — $1/6$ · $(3,3,7)$, $(3,7,3)$ — $4/21$ ·
$(3,4,5)$, $(3,5,4)$, $(4,5,3)$ — $13/60$ · $(3,3,11)$, $(3,11,3)$ — $8/33$.

Every one of these is already closed by a recorded result — $(3,3,p)$ by Kraus/Chen–Siksek,
$(p,p,3)$ by Darmon–Merel/Poonen, $(3,4,5)$ by Siksek–Stoll, $(3,3,4)$ resolved — which is a
consistency check on both the enumeration and the coverage table.

## A correction to my own script's output

The first run printed counts for $T = 1/2, 2/3, 3/4, 9/10$ as though they were totals. They are
**truncation artifacts** of capping the exponent list at 200: at $T \ge 1/3$ the exponent $z$ is
unbounded, so no finite count exists. Only the rows with $T < 1/3$ are meaningful. Corrected here;
the error was in my own commentary, not in the arithmetic.

## Assessment

The stratification is **real and sharp** — the finiteness threshold $T < 1/3$ is exact, not
heuristic. But it does not make either part easier:

- the finite part is already closed by known results, so it buys nothing new;
- the infinite tail $|\chi| \ge 1/3$ contains every large-exponent signature, and that is precisely
  where genus grows and the modular method is weakest (U114 Part II).

**N1 is BLOCKED**: a correct and exact stratification that moves no difficulty. Recorded because
the threshold $T < 1/3$ and the thirteen-signature list are reusable, and because a future attempt
to stratify by curvature should know that this particular cut has already been made and does not
help.

---

# Part VIII (N4 / COUNTERSEARCH): the "gap" framing in C033 was an overstatement

**Verification code**: `code/U119_n4_strip.py`

C033 recorded that all ten known solutions have $|\chi| \le 1/18$ while every Beal signature has
$|\chi| \ge 1/12$, and described the region between as *"a gap containing no known solution"*.
That phrasing implies something unexplained. Attacking my own claim:

## What the strip actually contains

Enumerating $1/18 < |\chi| < 1/12$ over $x \le y < 60$, $z < 200$: **exactly two signatures up to
permutation**, $(2,3,10)$ with $|\chi| = 1/15$ and $(2,3,11)$ with $|\chi| = 5/66$.

Both have an **exponent equal to 2**, so neither is a Beal signature — consistent with the Beal
region beginning at exactly $1/12$. $(2,3,10)$ is among the signatures this project records as
solved with no solutions.

## The corrected statement

There is no mystery. The right way to say it:

> The ten known solutions occupy the low-$|\chi|$ end of the **non-Beal** region, and the non-Beal
> region stops at $1/12$ because an exponent 2 is exactly what buys $|\chi| < 1/12$.

The $1/12$ threshold is real, exact and kernel-verified. The **"gap containing no known solution"
gloss in C033 overstated it** — the region is two signatures wide, and its emptiness of solutions
is ordinary, not structural.

## A second error, in my own verification script

The script's `SOLVED` set included $(2,3,11)$. **I put it there without justification.** This
project's recorded list of solved $(2,3,n)$ is $n \in \{7,8,9,10,15\}$; $(2,3,11)$ is not in it,
and I have no source for its status. The script's output therefore labelled $(2,3,11)$ "SOLVED, no
solutions" on my say-so alone.

Corrected: **$(2,3,11)$'s status is not recorded in this project and is not asserted.** This is
precisely the failure mode — an unsupported entry silently propagating into a conclusion — that the
U113 audit found throughout the inherited work, committed here by me, inside a script written to
check my own overstatement.
