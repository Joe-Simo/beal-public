# U120: Jev at scale, and the p-adic direction it surfaced

## 1. Using Jev at a scale a person cannot match

Earlier batches generated five or six mechanisms by hand and ranked them — human-scale triage,
which wastes the tool. This batch built the space **systematically** as
(tool) × (target) × (angle): 10 tools × 6 targets × 5 angles = **300 mechanisms**, every one
ranked on three narrow questions (*would it fail for a new reason*, *is it executable now*,
*what is the payoff*).

Verification code: `code/U120_mechanism_space.py`; full ranking persisted at
`research/pool/evidence/mechanism_space_ranking.json`.

### The signal

**Valuation / p-adic reasoning took 9 of the top 18 slots**, converging across different targets
(odd-prime signatures, necessary conditions, the frontier $(3,5,7)$) and different angles (exploit
a verified fact, seek an invariant, invert the question).

That is not a direction I would have chosen. My own priors pointed at modular or descent methods —
both already blocked. The convergence across independent cells is the kind of signal a
300-element ranking gives and a six-element one cannot.

## 2. What the p-adic direction produced: exactly one base is even

Acting on the top-ranked cell (p-adic × necessary conditions × exploit a verified fact), at
$p = 2$:

```lean
theorem exactly_one_even (h : IsBealCounterexample A B C x y z) :
    (A % 2 = 0 ∧ B % 2 = 1 ∧ C % 2 = 1) ∨
    (A % 2 = 1 ∧ B % 2 = 0 ∧ C % 2 = 1) ∨
    (A % 2 = 1 ∧ B % 2 = 1 ∧ C % 2 = 0)
```
```
'Beal.exactly_one_even' : [propext, Classical.choice, Quot.sound]
```

**Exactly one of $A$, $B$, $C$ is even.** Not two, by the verified pairwise coprimality; not zero,
because two odd bases make $A^x + B^y$ even and force $C$ even. It chains directly off
`gcd_ab_eq_one`, `gcd_ac_eq_one`, `gcd_bc_eq_one` — which is what "exploit a verified fact" meant.

Cross-checked on all ten known Fermat–Catalan solutions: every one has exactly one even base, and
all three positions occur — $(1,0,1)$, $(0,1,1)$, $(1,1,0)$ — so the condition is non-vacuous and
not an artifact of a single pattern.

## 3. N3: the local conditions are correlated, and the correlation compounds

Verification code: `code/U119_n3_correlation.py`.

If the congruence conditions at coprime moduli were independent, the admissible fraction would be
multiplicative: $f(m_1m_2) = f(m_1)f(m_2)$. Measured:

| $m_1$ | $m_2$ | $f(m_1)f(m_2)$ | $f(m_1m_2)$ | ratio |
|---|---|---|---|---|
| 8 | 9 | 0.5066 | 0.3927 | **0.775** |
| 8 | 5 | 0.5663 | 0.4714 | 0.833 |
| 9 | 5 | 0.6990 | 0.6211 | 0.889 |
| 16 | 9 | 0.5019 | 0.3788 | 0.755 |
| 32 | 9 | 0.5008 | 0.3751 | **0.749** |

and with three factors the shortfall roughly doubles:

| moduli | product | actual | ratio |
|---|---|---|---|
| (8, 9, 5) | 0.4478 | 0.2507 | **0.560** |
| (16, 9, 5) | 0.4437 | 0.2218 | **0.500** |

**Every ratio is below 1**, so the conditions are positively correlated as constraints: satisfying
several simultaneously is harder than independence predicts, and the effect deepens as more primes
are added. That is the phenomenon adelic / Brauer–Manin methods are built to detect, measured here
directly.

**Honest limit**: this cannot reach zero. U118 established that no local obstruction exists, so
the combined fraction stays positive however many primes are used. The correlation is a real
structural fact about the constraint system and a genuine search improvement; it is not a proof
route.

## 4. Status

- `exactly_one_even`: **kernel-verified**, added to the necessary conditions.
- N3 correlation: **measured**, recorded, not a proof route.
- The ranking is preserved so the next cells — p-adic × odd-prime signatures, p-adic × $(3,5,7)$ —
  can be taken up without regenerating it.

---

## 5. The full mod-8 trichotomy, kernel-verified

Drilling further into the p-adic direction gives the complete case analysis when $C$ is even
(so $A$, $B$ are both odd by `exactly_one_even`, and $8 \mid C^z$ since $z \ge 3$).

For odd $n$: $n^k \equiv 1 \pmod 8$ when $k$ is even, and $n^k \equiv n \pmod 8$ when $k$ is odd —
both now lemmas (`odd_pow_even_mod_eight`, `odd_pow_odd_mod_eight`).

| $x,y$ parity | consequence | theorem |
|---|---|---|
| both even | **impossible** ($1+1 = 2 \not\equiv 0$) | `not_both_exponents_even_of_even_C` |
| $x$ even, $y$ odd | $B \equiv 7 \pmod 8$ | `seven_mod_eight_of_even_exp` |
| both odd | $8 \mid A + B$ | `eight_dvd_add_of_even_C` |

```
'Beal.odd_pow_even_mod_eight'             : [propext, Quot.sound]
'Beal.odd_pow_odd_mod_eight'              : [propext, Quot.sound]
'Beal.not_both_exponents_even_of_even_C'  : [propext, Classical.choice, Quot.sound]
'Beal.eight_dvd_add_of_even_C'            : [propext, Classical.choice, Quot.sound]
'Beal.seven_mod_eight_of_even_exp'        : [propext, Classical.choice, Quot.sound]
```

### What this adds

By the kernel-verified exponent reduction every exponent is in $\{4\} \cup \{\text{odd primes}\}$,
so "even" means exactly 4. Hence, whenever $C$ is even:

- **signature $(4,4,z)$ is excluded outright** — checked to fire, not vacuous;
- if one exponent is 4, the *other* base is $\equiv 7 \pmod 8$;
- in the generic case (both exponents odd primes), $8 \mid A+B$ — a congruence on the bases
  rather than on a residue class, and therefore usable as a search filter.

### Method note

Every one of these came from the p-adic cell that Jev's 300-mechanism ranking placed first, drilled
into by a second Jev pass over 25 concrete claims. Three of my Lean drafts failed to compile
(a wrong `Nat.zero_pow` signature, an unclosed `1 % 8 = 1`, an `h` consumed by `obtain` before
reuse) — the kernel caught each one.

---

## 6. The mod-8 picture, completed: the `C` odd case

If $A$ is even then $B$ and $C$ are odd and $8 \mid A^x$ (since $x \ge 3$), so
$B^y \equiv C^z \pmod 8$ — the same three-way split, now relating $B$ to $C$:

| $y,z$ parity ($A$ even) | consequence | theorem |
|---|---|---|
| both odd | $B \equiv C \pmod 8$ | `B_eq_C_mod_eight_of_even_A` |
| $y$ odd, $z$ even | $B \equiv 1 \pmod 8$ | `B_one_mod_eight_of_even_A_even_z` |

```
'Beal.B_eq_C_mod_eight_of_even_A'       : [propext, Classical.choice, Quot.sound]
'Beal.B_one_mod_eight_of_even_A_even_z' : [propext, Classical.choice, Quot.sound]
```

By symmetry in $A \leftrightarrow B$ the same holds with the roles exchanged when $B$ is even.

### Exhaustive cross-check of the whole picture

Enumerating every $(A,B,C \bmod 8;\ x,y,z \text{ parities})$ consistent with *exactly one base
even* and the divisibility forced by $8$ dividing the even term: **544 admissible tuples**, and
every derived condition matches the enumeration exactly —

- $C$ even: 96 tuples; **no tuple has both exponents even**; $x$ even with $y$ odd always gives
  $B \equiv 7$; both odd always gives $8 \mid A+B$.
- $A$ even: 224 tuples; $y,z$ both odd always gives $B \equiv C$; $y$ odd with $z$ even always
  gives $B \equiv 1$.

So the Lean theorems and the independent enumeration agree on every case — the derivation is not
just checked by the kernel, it is confirmed against a brute-force model of the same statement.

### Current mod-8 inventory

Nine theorems, all on standard axioms, covering **every parity configuration**:
`exactly_one_even`, `odd_pow_even_mod_eight`, `odd_pow_odd_mod_eight`,
`not_both_exponents_even_of_even_C`, `eight_dvd_add_of_even_C`, `seven_mod_eight_of_even_exp`,
`B_eq_C_mod_eight_of_even_A`, `B_one_mod_eight_of_even_A_even_z`, plus `no_cancellation`.

---

## 7. Cycle U122 — the p = 3 analogue (mod 9)

Jev ranked 20 concrete mod-9 claims (`research/pool/evidence/mod9_claim_ranking.json`,
`code/U122_mod9_claims.py`). The top-scored cell was the cube-residue argument, which turned out
to be the one genuinely new thing at $p=3$.

### The argument

Units mod 9 are $\{1,2,4,5,7,8\}$; **cubes among them are exactly $\{1,8\}$** ($=\pm1$), because
$(\mathbb{Z}/9)^\times$ is cyclic of order 6. So if $3 \nmid A,B,C$ and $3 \mid x$, $3 \mid y$:

$$A^x, B^y \in \{1,8\} \pmod 9 \implies A^x+B^y \in \{2,0,7\} \pmod 9,$$

and $0$ is excluded since $3 \nmid C$. Hence

$$\boxed{C^z \equiv 2 \text{ or } 7 \pmod 9.}$$

Neither $2$ nor $7$ is a cube mod 9, so **$3 \nmid z$** follows immediately. (This is *not*
subsumed by `no_counterexample_of_three_dvd_all`: that theorem needs $3$ to divide all three
exponents and invokes FLT₃; this one needs only $3 \mid x$ and $3 \mid y$ and is elementary.)

### Kernel-verified (`formal/Beal/Structure.lean`, `section ModNine`)

```
'Beal.three_not_dvd_pow'                 : [propext, Classical.choice, Quot.sound]
'Beal.cube_mod_nine'                     : [propext, Classical.choice, Quot.sound]
'Beal.cube_unit_mod_nine'                : [propext, Classical.choice, Quot.sound]
'Beal.pow_mod_nine_of_three_dvd_exp'     : [propext, Classical.choice, Quot.sound]
'Beal.pow_C_mod_nine'                    : [propext, Classical.choice, Quot.sound]
'Beal.not_three_dvd_z_of_three_dvd_xy'   : [propext, Classical.choice, Quot.sound]
```

### Exhaustive cross-check (`code/U122_mod9_exact.py`)

Enumerating the mod-9 model over all units $A,B,C$ and all $x,y,z \in [3,38]$ with
$3 \mid x$, $3 \mid y$: **46,656 admissible tuples**, and **zero** violate either
$C^z \in \{2,7\}$ or $3 \nmid z$. Separately, $3$ dividing each of $A$, $B$, $C$ is individually
possible mod 9 (8640 / 8640 / 6048 admissible tuples), so no base is excluded from carrying the
factor 3 — mod 9 gives a *conditional* restriction, not the unconditional split mod 8 gave.

### Honest assessment

Mod 9 is strictly weaker than mod 8: mod 8 forced *exactly one base even* unconditionally,
whereas mod 9 says nothing unless two exponents are multiples of 3. The value here is the
conjunction — combining the mod-8 and mod-9 conditions gives a mod-72 sieve — and the fact that
`not_three_dvd_z_of_three_dvd_xy` closes the $(3a, 3b, z)$ family by elementary means where the
literature reaches for FLT₃.

---

## 8. Cycle U123 — EXPLORATION: base order forces exponent order

Per the loop policy this cycle deliberately left the mined p-adic cells. Jev's mechanism ranking
placed **gap/threshold × the large-exponent tail × exploit a verified fact** as the top unmined
cell; 18 concrete claims were then Jev-ranked (`code/U123_tail_claims.py`,
`research/pool/evidence/tail_claim_ranking.json`). The verified fact exploited is `no_cancellation`.

### Kernel-verified (`section ExponentOrder`)

| statement | theorem | axioms |
|---|---|---|
| $C$ largest base $\Rightarrow z \le \max(x,y)$ | `z_le_max_of_C_largest` | `[propext, Quot.sound]` |
| $C$ smallest base $\Rightarrow z > \max(x,y)$ | `max_lt_z_of_C_smallest` | standard |
| $C \le B \Rightarrow z > y$ | `y_lt_z_of_C_le_B` | standard |

Proof of the first: $C^z = A^x + B^y < C^x + C^y \le 2C^{\max}$, but $z \ge \max+1$ gives
$C^z \ge C\cdot C^{\max} \ge 2C^{\max}$.

### Cross-check (`code/U123_tail_exact.py`)

All **5,690** solutions of $A^x+B^y=C^z$ with $A,B,C\le 60$, $x,y,z \le 12$ — exponents 1 and 2
deliberately *allowed*, since the proofs use only positivity — satisfy all three statements.
Zero violations.

### What this buys

Every counterexample now has its exponent order pinned to its base order: the largest base
carries an exponent no larger than the other two's maximum, and the smallest base's exponent
exceeds both others. Together with the trichotomy $|\chi| \ge 1/12$ this rules out, e.g., any
counterexample with $C > A, B$ and $z > x, y$ — the "all-large-at-C" corner — unconditionally.

---

## 9. Cycle U124 — NOVEL COMBINATION at Jev scale: the conjecture mill

`code/U124_conjecture_mill.py` machine-generates implications *P(bases) ⟹ Q(exponents)* from
13 atomic hypotheses and 14 atomic conclusions, filters them **exactly** on the full solution model
(5,392 solutions of $A^x+B^y=C^z$ with $A \ne B$, bases ≤ 60, exponents ≤ 12, exponents 1 and 2
included), drops vacuous ones (support < 40) and ones already implied by proved theorems, and
hands the **177 surviving true statements** to Jev to rank by provability × payoff
(`research/pool/evidence/conjecture_mill_ranking.json`). Jev decided nothing about truth —
enumeration did — it only chose what to prove first.

### Kernel-verified (`section Dominant`)

| statement | theorem | axioms |
|---|---|---|
| $B^y \le A^x,\ A < C \Rightarrow z \le x$ | `z_le_x_of_dominant_A_lt_C` | `[propext, Quot.sound]` |
| $A^x \le B^y,\ B < C \Rightarrow z \le y$ | `z_le_y_of_dominant_B_lt_C` | `[propext, Quot.sound]` |
| $C < A \Rightarrow x < z$ | `x_lt_z_of_C_lt_A` | standard |
| $B^y \le A^x \Rightarrow (z \le x \iff A < C)$ | `dominant_dichotomy` | standard |

`dominant_dichotomy` is the clean statement: **for the dominant term, the exponent of $C$ is
bounded by the dominant exponent exactly when the dominant base is smaller than $C$.**
($A = C$ is impossible: it would force $C = 1$ and then $1 + B^y = 1$.)

This sharpens §8: `z_le_max_of_C_largest` needed *both* $A, B < C$; the dominant version needs
only the dominant base below $C$.
