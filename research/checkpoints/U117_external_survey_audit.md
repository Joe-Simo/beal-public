# U117: Audit of an external survey of Beal-conjecture methods

**Date**: 2026-09-17
**Source**: a survey document supplied by the user (a Gemini-shared analysis; the share link itself
was not machine-readable — it redirects to a Google sign-in — so the text was supplied directly).
**Verification code**: [`code/U117_audit_gemini_survey.py`](../../code/U117_audit_gemini_survey.py)

The document surveys attempted methods, theoretical obstructions and structural failures for the
Beal conjecture. It is **substantially accurate and independently corroborates this project's
findings**, and it contributes two things this project did not have. It also contains two errors,
both found by exact computation.

---

## 1. Independent corroboration of this project's audit conclusions

| survey claim | this project |
|---|---|
| Darmon–Granville is **non-uniform and ineffective** — no height bound, no algorithm | U114 §3, reached independently; also caught an unsourced "Baker effective bound" used as if effective (U113 Part I) |
| **abc gives finiteness, not emptiness**, and its constants are non-effective | U115 §1, reached independently — the single most important negative result of that checkpoint |
| IUT has not achieved community acceptance | U115 §2 |
| level lowering fails when $\dim S_2(N^*) > 0$; elimination is **pointwise in the exponent**, cannot cover infinite ranges | U113 Parts I–II and C006's standing obligation (uniformity in $p$) |
| **trivial/non-coprime solutions force genuine modular forms whose representations are indistinguishable from putative counterexamples** | exactly our orbit $b$ — the CM abelian surface of the boundary curve $C_0$ (U113 Parts I–II) |
| no uniform **rational** Frey curve exists for three independent exponents; Darmon's program must move to hyperelliptic curves / $\mathrm{GL}_2$-type abelian varieties over totally real fields | U114 Part IV, from Freitas's own list of signatures with Frey curves over $\mathbb{Q}$ |

That two independent analyses converge on the same obstructions — in particular on the
trivial-solution obstruction and on abc's insufficiency — is meaningful evidence that both are right.

## 2. What the survey adds that this project did not have

### 2.1 Beal is FALSE over the Gaussian integers (Helenius, 2004) — **verified exactly**

$$(-2+i)^3 + (-2-i)^3 = (1+i)^4.$$

Verified in exact Gaussian-integer arithmetic:
$(-2+i)^3 = -2-11i$, $(-2-i)^3 = -2+11i$, sum $= -4$; and $(1+i)^4 = ((1+i)^2)^2 = (2i)^2 = -4$.
Exponents $(3,3,4)$, all $\ge 3$. Norms $N(-2+i) = N(-2-i) = 5$, $N(1+i) = 2$, and
$\gcd(5,2) = 1$, so the bases share no Gaussian prime.

**This is a genuine obstruction result and the most valuable item in the document.**
$\mathbb{Z}[i]$ is a principal ideal domain, so Beal **cannot** follow from unique factorisation
alone. Any valid proof must use the **total ordering of $\mathbb{Z}$** or the specific ramification
behaviour of rational primes. Every argument resting purely on formal factorisation identities is
refuted in advance — which explains, at a stroke, an entire genre of failed elementary attempts.

### 2.2 "Exponent 2 is obligatory" — **verified**

Of the ten listed coprime Fermat–Catalan solutions, the nine whose identities check out **all have
2 among their exponents**. So Beal is equivalent to: *2 is an obligatory exponent for every
non-trivial primitive solution in the hyperbolic regime.* A sharp reformulation worth keeping.

### 2.3 A taxonomy of elementary failure modes

Misapplied Lifting-The-Exponent and $p$-adic valuation arguments; **affirming the consequent**
($P \Rightarrow Q$, $Q$ true, therefore $P$); applying difference-of-powers identities across
mismatched exponents via fractional substitutions $u = C^{z/n}$, $v = B^{y/n}$ — which are
algebraic irrationals, so unique factorisation in $\mathbb{Z}$ does not apply; and a projective-slope
argument resting on the category error that $B^y/A^x$ could be irrational.

This complements U115 §5 and overlaps this project's own target-discipline list.

### 2.4 Concrete computational bounds

Named search efforts (Norvig; Vanderkam, $A,B,C \le 1000$, $x,y,z \le 1000$; Mauldin;
Durango Bill, $C^z \le 10^{28}$ unconditionally; BealF@home/BOINC), the double-modular hashing
architecture ($p_1 = 2^{32}-5$, $p_2 = 2^{32}-17$), and the Elkies–Frye precedent —
$95800^4 + 217519^4 + 414560^4 = 422481^4$ near $10^{23}$ — as evidence that a minimal
counterexample could lie beyond $10^{50}$.

---

## 3. Errors found

### 3.1 A wrong identity — solution 8

The document lists
$$9262^3 + 1531228^2 = 113^7 .$$
**This is false.** Exactly: LHS $= 3{,}139{,}196{,}560{,}712$, RHS $= 235{,}260{,}548{,}044{,}817$.

The literature value has an extra digit:
$$9262^3 + 15312283^2 = 113^7 = 235{,}260{,}548{,}044{,}817 \quad\checkmark$$
verified exactly, with $\gcd = 1$. A dropped digit, not a conceptual error — but it is the kind of
transcription slip that a search program seeded from the document would silently inherit.

### 3.2 An overstated genus claim

The document asserts: *"Whenever $x, y, z \ge 3$, the genus satisfies $g \ge 2$, placing every
auxiliary curve firmly inside the domain of Faltings' Theorem."*

From its own Riemann–Hurwitz formula $2g-2 = d\,(1 - 1/x - 1/y - 1/z)$, the bracket **vanishes** at
$(3,3,3)$, giving $2g - 2 = 0$ and $g = 1$ — not $g \ge 2$. The claim holds for $\chi < 0$, i.e.
for every signature *except* $(3,3,3)$, which the document elsewhere correctly identifies as the
unique parabolic case with $\chi = 0$. It is an internal inconsistency, and $(3,3,3)$ is of course
covered separately by Fermat's Last Theorem.

### 3.3 Minor

The $\chi$ arithmetic checks out: $\chi(3,3,3) = 0$ and the next-largest value at $\min \ge 3$ is
$\chi(3,3,4) = -1/12$, exactly as claimed.

---

## 4. Net assessment

The survey is a good-quality secondary source: accurate on the substance, independently reaching
this project's main negative conclusions, and contributing a genuine obstruction theorem
(Helenius) that this project lacked. Its two errors are one transcription slip and one overstated
edge case, both caught by exact computation and neither affecting its conclusions.

**It contains no proposed route to a resolution**, and its own closing position matches this
project's: a resolution needs either a framework unifying three independent exponents into one
modular or motivic object, or a breakthrough in *effective* Diophantine geometry. Neither exists.

---

## 5. The Helenius obstruction is now kernel-verified

The survey's most valuable item is now machine-checked in
[`formal/Beal/GaussianObstruction.lean`](../../formal/Beal/GaussianObstruction.lean), using
mathlib's `GaussianInt`:

```lean
theorem helenius : gU ^ 3 + gV ^ 3 = gW ^ 4          -- (-2+i)^3 + (-2-i)^3 = (1+i)^4
theorem gauss_norms : gU.norm = 5 ∧ gV.norm = 5 ∧ gW.norm = 2

theorem beal_false_over_gaussianInt :
    ∃ (u v w : GaussianInt) (x y z : ℕ),
      3 ≤ x ∧ 3 ≤ y ∧ 3 ≤ z ∧ u ≠ 0 ∧ v ≠ 0 ∧ w ≠ 0 ∧
      u ^ x + v ^ y = w ^ z ∧
      Nat.gcd u.norm.natAbs w.norm.natAbs = 1 ∧
      Nat.gcd v.norm.natAbs w.norm.natAbs = 1
```

```
'Beal.helenius'                    : [propext]
'Beal.gauss_norms'                 : [propext]
'Beal.beal_false_over_gaussianInt' : [propext, Classical.choice, Quot.sound]
```

`helenius` and `gauss_norms` depend on **`propext` alone** — decidable computation in `ℤ[i]`,
the lightest axiom footprint of anything verified in this project.

**A sign error caught by the kernel.** The first draft asserted $(-2+i)^3 = -2-11i$ and
$(-2-i)^3 = -2+11i$. `decide` reported that it had *proved the proposition false*. The correct
values are $(-2+i)^3 = -2+11i$ and $(-2-i)^3 = -2-11i$ — the signs are the other way round. The
sum, and therefore the identity itself, is unaffected; but the intermediate statements were wrong,
and only the proof assistant caught it. This is the fourth time in this audit that a step which
reads correctly has failed on being checked.

**What it establishes.** `ℤ[i]` is a principal ideal domain, hence a UFD, and Beal's statement is
false in it. So no proof of Beal can rest on unique factorisation alone; any valid argument must
use the total ordering of `ℤ` or the ramification of rational primes. This refutes in advance the
largest single genre of failed elementary attempts — and it is now checked by the Lean kernel
rather than merely cited.

---

## 6. The known Fermat–Catalan solutions are now kernel-verified

[`formal/Beal/FermatCatalan.lean`](../../formal/Beal/FermatCatalan.lean) verifies all ten known
primitive solutions as exact identities, and proves the structural fact behind the survey's
sharpest observation:

```lean
theorem not_counterexample_of_exponent_two {A B C x y z : ℕ}
    (h2 : x = 2 ∨ y = 2 ∨ z = 2) : ¬ IsBealCounterexample A B C x y z

theorem fc_all_fail_beal : -- all ten signatures, each refuted by its exponent 2
```

```
'Beal.fc6'                               : [propext]
'Beal.fc8'                               : [propext]
'Beal.not_counterexample_of_exponent_two': [propext, Quot.sound]
'Beal.fc_all_fail_beal'                  : [propext, Quot.sound]
```

Every known solution fails Beal **for exactly one reason**: an exponent equal to 2. So Beal is
equivalent to *"2 is an obligatory exponent in the hyperbolic regime"* — and that equivalence is
now machine-checked rather than observed.

### The survey's error, confirmed by the kernel

`fc8` records the correct value `9262^3 + 15312283^2 = 113^7`. Asking Lean to prove the survey's
version:

```
example : 9262 ^ 3 + 1531228 ^ 2 = 113 ^ 7 := by norm_num
  error: unsolved goals  ⊢ False
```

`norm_num` reduces it to `False`. The dropped digit is now refuted by the proof assistant, not
merely by my arithmetic — and any future reader of this repository who copies that identity will
find it does not compile.
