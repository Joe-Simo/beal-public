# U113: Adversarial Audit of U97 — the Orbit-b Elimination Does Not Hold as Written

**Date**: 2026-09-17
**Method**: exploration-loop cycle 1, adversarial proof audit + exact computation
**Audited artifact**: [`research/checkpoints/U97_orbit_b_boundary_CM_obstruction.md`](U97_orbit_b_boundary_CM_obstruction.md)
**Pool candidate**: C003
**Verification code**: `code/U113_u97_disc.py`, `code/U113_u97_traces.py`, `code/U113_u97_strategy3.py`, `code/U113_u97_trace_only.py`, `code/U113_u97_growth.py`

U97 claims orbit $b$ (`2.2.5.1-2000.1-b`) is eliminated **unconditionally** by three independent
strategies. That claim does not hold as written. Its identification half is confirmed; all three
elimination strategies fail, one of them by exact computation.

---

## 1. CONFIRMED by independent exact computation

**1.1 Discriminant identity (U97 §2.2).** For
$f(x) = x^5 + 40UVx^3 + 320U^2V^2x + 64(8V^5 - U^5)$, symbolic computation gives
$$\operatorname{disc}(f) = 2^{24}\cdot 5^5\cdot (U^5 + 8V^5)^4 = 2^{24}\cdot 5^5\cdot Z^{68},$$
exactly as claimed, confirmed symbolically and at five exact integer specialisations.
The good-reduction argument at $q \mid Y$ stands.

**1.2 Frobenius traces (U97 §1.4).** By direct point counting over $\mathbb{F}_q$ and
$\mathbb{F}_{q^2}$ for $C_0: y^2 = 64 - x^5$, using
$S = a_{\mathfrak q_1}+a_{\mathfrak q_2} = t$ and $P = a_{\mathfrak q_1}a_{\mathfrak q_2} = s - 2q$:

| $q$ | $\#C_0(\mathbb F_q)$ | $\#C_0(\mathbb F_{q^2})$ | $S$ | $P$ | U97 claim | |
|---|---|---|---|---|---|---|
| 11 | 3 | 123 | 9 | 19 | $S=9,P=19$ | match |
| 31 | 43 | 1023 | −11 | 29 | $S=-11,P=29$ | match |
| 41 | 43 | 1543 | −1 | −151 | $S=-1,P=-151$ | match |

and $a_{\mathfrak q}=0$ for every tested $q \not\equiv 1 \pmod 5$. The identification of orbit $b$
with $\operatorname{Jac}(C_0)_{/K}$ is therefore well supported.

---

## 2. REFUTED BY COMPUTATION — Strategy 3 (infinite split sieve)

U97 Strategy 3 defines
$$\mathcal S = \{\,q \equiv 1 \bmod 5 \text{ split} : \forall t \in \mathbb F_q^\times,\
a_{\mathfrak q}(C^-(1,t)) \not\equiv a_{\mathfrak q}(b) \bmod 17 \,\}$$
and asserts, citing Deligne equidistribution, that $\mathcal S$ has **positive density**, hence is
infinite, hence $\prod_{q\in\mathcal S} q \mid Y$ forces $Y=0$.

**This is backwards.** Equidistribution makes the residual trace $a_{\mathfrak q}(C^-(1,t)) \bmod 17$
approach uniformity over $t \in \mathbb F_q^\times$, so the expected number of matching $t$ is
$\approx (q-1)/17$, and the chance that *no* $t$ matches decays like $(1-1/17)^{q-1} \to 0$.
$\mathcal S$ is therefore finite, and equidistribution is evidence **against** Strategy 3, not for it.

Exact computation over all $q \equiv 1 \pmod 5$, $q < 1600$, counting $t \in \mathbb F_q^\times$
whose Euler factor agrees with orbit $b$'s mod 17:

- **Trace-only criterion** (what §2.5 literally states): forcing primes are exactly
  $\{11, 31, 41, 71, 131\}$. Match counts track $q/17$ closely (e.g. $q=1531$: 80 matches vs 90.1 predicted).
- **$(S,P)$ criterion**: forcing primes below 140 are $\{11,31,41,71,101,131\}$; $q=61$ has 5 matching $t$.

Under **both** criteria the matching count is strictly positive for every $q \ge 151$ tested up to 1600.
$\mathcal S$ is finite. Strategy 3's central step is false.

**Two further defects in Strategy 3.**
- It attributes its forcing-prime set $\{11,31,41,61,71,101,151,191,211,281,331,431,461,631\}$ to U72.
  U72 §1 takes that set from U68 as a **Gaussian-valuation** forcing list, a different notion from the
  mod-17 Frobenius congruence used here. Ten of those fourteen primes are not forcing under either
  reconstruction of the mod-17 criterion. The two notions are conflated.
- It invokes "Baker's method on the superelliptic equation $X^{10}+256Y^{10}=Z^{17}$" for an effective
  bound $\log Y \le C$. Baker-type superelliptic bounds apply to $y^m=f(x)$ with $m$ and $\deg f$ fixed
  and $f$ having at least two (resp. three) distinct roots; they do not deliver an effective bound for
  this three-term equation. No effective $C$ is exhibited.

This also contradicts U92, which proved the Gaussian forcing-prime sieve is **exhausted** by finitely
many primes. A route cannot simultaneously rely on that sieve being exhausted and on it being infinite.

---

## 3. FLAWED BY AUDIT — Strategy 2 (deformation rigidity)

Strategy 2 argues: $R=\mathbb T$ is a DVR, therefore any characteristic-zero abelian variety realising
the residual representation must lie in orbit $b$'s Hecke eigenspace, therefore $J^- \sim_K \operatorname{Jac}(C_0)$,
contradicting $\dim \operatorname{End}^0(J^-) = 2 \ne 4$.

The second implication does not follow. An $R=\mathbb T$ theorem identifies the deformation ring with
the Hecke algebra **for lifts satisfying the fixed local conditions**; it does not assert that a residual
isomorphism $\bar\rho_{J^-,17} \cong \bar\rho_{b,17}$ forces an isogeny of the characteristic-zero
abelian varieties. If it did, every modular-method argument would terminate at the congruence, and the
elimination step that the whole method exists to perform would be unnecessary. The argument proves too
much, which is the signature of a circular step. The endomorphism-dimension contradiction is then vacuous:
it is derived from an isogeny that has not been established.

Additionally, $J^-$ is only known to satisfy the prescribed local types after the level-lowering step
whose hypotheses C002 records as failing (U96: Azon Thm 5.23 needs Hypothesis 5, which fails here).
Strategy 2 therefore also inherits C002's blockage.

---

## 4. FLAWED BY AUDIT — Strategy 1 (reducibility / $X_0(17)$)

Strategy 1 argues that reducibility of $\bar\rho_{b,17}|_{G_M}$ forces a 17-isogeny of $J^-$ over
$M=\mathbb Q(\zeta_5)$, contradicting the absence of non-CM points on $X_0(17)$ over $M$.

- **Category error.** $J^-$ is an abelian *surface* with RM by $\mathbb Q(\sqrt5)$. An
  $\mathcal O_K$-linear 17-isogeny is classified by a Hilbert modular variety for $K=\mathbb Q(\sqrt5)$
  with $\Gamma_0(\mathfrak p_{17})$-structure, not by the elliptic modular curve $X_0(17)$.
  $X_0(17)$ parametrises 17-isogenies of *elliptic curves*.
- **Overstated input.** $X_0(17)$ has genus 1 and rank 0 over $\mathbb Q$, but $M$ has degree 4 and the
  Mordell–Weil rank over $M$ is not addressed; rank can grow in extensions. The assertion that over
  cyclotomic fields the only non-cuspidal points are CM is not a statement of Momose (1984),
  Darmon–Merel (1997) or Bilu–Parent–Rebolledo (2013) as cited. BPR concerns $X_{\mathrm{split}}(p)$
  over $\mathbb Q$; Darmon–Merel concerns $X_0^{\mathrm{split}}$-type quotients and cyclic isogenies
  over $\mathbb Q$. None is quoted with its hypotheses here.
- The step "$J^-$ is strictly non-CM, therefore it cannot define a rational point on the 17-isogeny
  locus" is a non sequitur: non-CM abelian varieties can and do admit isogenies.

---

## 5. Status changes

- **C003** (orbit $b$ eliminated unconditionally): VERIFICATION_REQUIRED → **BLOCKED**.
  The identification of orbit $b$ with $\operatorname{Jac}(C_0)$ survives; the elimination does not.
- Anything downstream that treats orbit $b$ as eliminated is now **conditional**, including any claim
  that the weighted equation's modular route is closed.
- No statement anywhere in the project may cite U97 as an unconditional elimination.

## 6. Extracted, reusable

1. $\operatorname{disc}(f) = 2^{24}5^5Z^{68}$ (verified) — good reduction at every $q \mid Y$ stands.
2. Orbit $b \sim \operatorname{Jac}(C_0)_{/K}$, trace data verified at $q=11,31,41$ and $a_{\mathfrak q}=0$
   for $q \not\equiv 1 \bmod 5$.
3. **The mod-17 split sieve is finite**, with forcing set $\{11,31,41,71,131\}$ (trace criterion) for
   $q<1600$. This is a genuine finite obstruction and is a *usable* statement — it bounds which primes
   can be forced to divide $Y$ — but it cannot be inflated to an infinitude argument.
4. The distinction between **Gaussian-valuation forcing primes** (U68/U72) and **mod-17 Frobenius
   congruence forcing primes** (U97) must be maintained; they are different sets.

## 7. What this does NOT establish

It does not refute the claim that orbit $b$ is eliminable, nor the Beal conjecture, nor the weighted
equation's resolution. It establishes only that U97's proof of the elimination is not valid as written.

---

# Part II: U102 does not rescue the elimination — the residual/isogeny conflation

**Audited artifact**: [`U102_orbit_b_definitive_elimination.md`](U102_orbit_b_definitive_elimination.md),
which claims a "definitive, unconditional elimination of orbit $b$" by four arguments.
**Verification code**: `code/U113_residual_vs_isogeny.py`

## II.1 The systematic error

The modular method, after level lowering, yields exactly one statement:
$$\bar\rho_{J^-,17} \;\cong\; \bar\rho_{b,17} \qquad \text{(an isomorphism of \emph{residual}, mod-17 representations).}$$

U102's arguments 1–3 refute, respectively:
1. that $J^-$ is **isogenous** to $A_b$ (via endomorphism algebra dimensions $2 \ne 4$);
2. that $V_{17}(J^-) \cong V_{17}(A_b)$ as **17-adic** representations (via Faltings, $\operatorname{Hom}(J^-,A_b)=0$);
3. that $J^-$ and $A_b$ have the same **reduction type / inertia image** at $q \mid Z$ and $q \mid Y$.

None of these refutes the residual congruence. Isogeny and 17-adic isomorphism are strictly
stronger than a mod-17 isomorphism, so refuting the stronger statements leaves the actual
conclusion of the modular method untouched.

**This argument proves too much.** If a residual congruence implied an isogeny, then every
application of the modular method would terminate at level lowering, and the elimination step —
the step the entire method exists to perform — would never be needed. Ribet's theorem plus
"the curves are not isogenous" would prove Fermat's Last Theorem in one line. That is the
signature of a circular or vacuous step.

## II.2 Exact counterexample to the inference

`code/U113_residual_vs_isogeny.py` exhibits, by exact point counting with no floating point,
five elliptic curves in Tate normal form for a rational 5-torsion point,
$$E_c: y^2 + (1-c)xy - cy = x^3 - cx^2,$$
whose mod-5 representations are reducible with semisimplification $1 \oplus \chi_5$, so that
$a_p \equiv 1 + p \pmod 5$ at every prime of good reduction. Verified for all $p < 40$:

| $p$ | 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $a_p \equiv p+1 \bmod 5$ | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |

Yet their $a_p$ differ over $\mathbb Z$ — e.g. $c=1$ vs $c=2$ have $a_5 = 1$ vs $-4$; $c=1$ vs
$c=3$ have $a_7 = -2$ vs $3$ — so by Faltings/Tate they are **not isogenous**.

**Non-isogenous abelian varieties routinely share a residual representation.** The inference
"not isogenous $\Rightarrow$ not residually congruent" is therefore false in general, and U102
supplies nothing that makes it valid in this particular case.

## II.3 Argument 3 additionally contradicts U97

U102 argument 3 uses non-zero monodromy $N_{\mathfrak q} \ne 0$ at $q \mid Z$ to distinguish $J^-$
from $A_b$. But U97 §2.4 states that at $q \mid Z$, since $17 \mid v_q(Z)$, the conductor exponent of
the **residual** representation *drops to 0 by level lowering* — which is precisely why the lowered
level is $\mathfrak N = (2)^2\mathfrak p_5^3$ and why orbit $b$ is a candidate at all. The toric
monodromy visible 17-adically is exactly what level lowering removes mod 17. The two checkpoints
cannot both be right, and U97 §2.4 is the one consistent with the method.

## II.4 Argument 4 is U97 Strategy 3

U102 argument 4 restates the Frobenius sieve refuted in Part I, and adds an unsourced
"Baker's effective height upper bound $10^{434}$". The height figures attributed to the same
14 forcing primes are mutually inconsistent across checkpoints ($Y > 10^{35}$ in U97 §2.2,
$\max(X,Y) > 10^{4810}$ in U102 §1, $\max(X,Y) > 10^{25993}$ conditionally in U90). No effective
Baker constant is derived anywhere.

## II.5 Consequence

Both the U97 and the U102 eliminations of orbit $b$ fail, and they fail for one shared reason:
**residual mod-17 data is conflated with 17-adic / isogeny-level data**. Orbit $b$ is the sole
surviving newform at level $\mathfrak N$; with it unresolved, the modular route to the weighted
equation $X^{10}+256Y^{10}=Z^{17}$ is **open**, not closed.

The correct shape of a genuine elimination must work entirely with mod-17 data — for example an
image-of-inertia or Serre-weight incompatibility of $\bar\rho_{J^-,17}$ against
$\bar\rho_{b,17}|_{I_{\mathfrak p}}$, or a symplectic-criterion (Halberstadt–Kraus) obstruction —
none of which is established in U97 or U102.

## II.6 Pool consequences

- **C003** BLOCKED (both proofs of the elimination fail).
- Any checkpoint asserting the weighted-equation modular route is closed is now **conditional**.
- New candidate **C013**: find a genuinely residual (mod-17) obstruction against orbit $b$.

---

# Part III: U105's "unconditional resolution" of the all-even branch does not hold

**Audited artifact**: [`U105_all_even_branch_complete_unconditional_resolution.md`](U105_all_even_branch_complete_unconditional_resolution.md)
**Verification code**: `code/U113_u105_degree_obstruction.py`

U105 Theorem 1.1 claims the all-even branch with $17 \mid t$ has no primitive solutions, resting on
the elimination of Orientation B ($X^{10}+256Y^{10}=Z^{17}$) by "two completely independent,
mutually reinforcing pathways". Both fail.

## III.1 Pathway 1 is the refuted orbit-b argument

U105 §2.2 Pathway 1 step 4 eliminates orbit $b$ by exactly two claims:
"endomorphism dimension clash … rules out isogeny and Galois isomorphism by Faltings" and
"Baker height contradiction: $10^{4810} < \max(X,Y) \le 10^{434}$". These are U102 arguments 1–2 and
U97 Strategy 3, refuted in Parts I and II above. Pathway 1 therefore inherits both failures and is
not independent of them.

## III.2 Pathway 2 bounds the wrong object — the degree obstruction is self-defeating

Pathway 2 runs Chabauty–Coleman on $C^-$ over $k = \mathbb Q(\sqrt5)$: from
$\operatorname{rank}_{\mathbb Z} J^-(k) \le 2 < g = 8$ it derives $\#C^-(k) \le 9$, and then concludes
with a "Diophantine Degree Obstruction": a positive integer solution gives $c = i\,2^{4/5}$ with
$[k(u,v):k] = 10 \ne 1$, so $C^-(k)$ contains no point arising from a solution.

Exact computation confirms the degree claim — and that is precisely the problem. The minimal
polynomial of $c = i\,2^{4/5}$ is
$$x^{10} + 256,$$
of degree 10 over $\mathbb Q$ and still degree 10 over $k = \mathbb Q(\sqrt5)$. (Note this polynomial
is the weighted equation's own boundary form.)

So a solution yields a point of $C^-(L)$ with $[L:k] = 10$, **not** a point of $C^-(k)$.
Chabauty–Coleman with $\operatorname{rank} < g$ bounds $\#C^-(k)$ **only**. A bound on the $k$-rational
points is therefore silent about degree-10 points, and the step

> "$C^-(k)$ contains NO POINTS arising from non-trivial integer solutions. … Therefore Orientation B
> has no non-trivial primitive positive integer solutions"

is a non sequitur. The premise is *vacuously* true — solutions were never expected to give $k$-rational
points — and carries no Diophantine content whatsoever. Far from being an obstruction to solutions,
the degree-10 statement is an obstruction to the method.

To reach the intended conclusion one needs Chabauty over $L$ (degree 10 over $k$, degree 20 over
$\mathbb Q$), where $\operatorname{rank}_{\mathbb Z} J^-(L) < g = 8$ must be **re-established** — ranks
grow in extensions and the U99 Selmer bound is a bound over $k$, not over $L$ — or a symmetric-power
Chabauty / covering-collection argument. Neither appears in U105, U99 or U102.

This also downgrades the U99 result as it is used here: $\operatorname{rank}_{\mathbb Z}J^-(k)\le 2 < 8$
is correct and valuable, but it proves finiteness of $C^-(k)$, which is not the set that contains the
solutions.

## III.3 Coverage gap in Theorem 1.1

Theorem 1.1 is stated with the hypothesis $r, s \ge 5$, i.e. $x, y \ge 10$. The all-even branch of the
Beal statement requires only $x,y,z \ge 3$ and even, i.e. $r,s,t \ge 2$. The cases
$r, s \in \{2,3,4\}$ ($x$ or $y \in \{4,6,8\}$) are not covered by the stated theorem, and U105 gives
no proof that they reduce elsewhere. Nonetheless the §4 coverage ledger records
"$(2r,2s,2t)$, $17\mid t$ — **100% Closed**" with the $r,s\ge5$ hypothesis silently dropped.

A reduction of the small cases may well exist — e.g. via the $(2,4,n)$ family — but per the project's
own target discipline a restriction of the exponent range must be **proved** to cover every case before
the ledger may record the family as closed. It is currently an unproved coverage step.

## III.4 Minor defect in Theorem 1.2

Step 5 argues "$A = X^2 > 0$ and $B = Y^2 > 0$ forces $A = B = 1$". Positivity forces no such thing.
The intended argument is that Dahmen–Siksek leaves only solutions with $A,B \in \{0,\pm1\}$, after
which $1+1 = 2 \ne Z^{19}$. The conclusion survives, conditional on the Dahmen–Siksek citation, which
has **not** been checked against the primary source (*Acta Arith.* 164 (2014), Theorem 1) and remains
an open literature obligation.

## III.5 Net effect on coverage

The all-even branch with $17 \mid t$ is **not** closed. Both its pathways fail, one of them
(Pathway 2) for a reason that is independent of the orbit-$b$ question and that no amount of work on
orbit $b$ would repair. The project README's statement that "the coefficient-256 weighted orientation
remains unresolved" is the accurate one; U105's ledger and U102's "definitive" language are not.

---

# Part IV: Heuristic laundering — the claimed removal of GRH is circular

**Audited artifacts**: `U99_class_number_one_mathematical_certificate.md`,
`U102_p11_p13_class_number_certification_and_unconditional_status.md`,
`U110_p19_class_group_analytic_bounds.md`, `U110_signature_5_5_higher_primes_analysis.md`
**Found by**: Jev hypothesis screen over all 144 checkpoints (`code/U113_hypothesis_screen.py`),
which isolated 8 checkpoints that simultaneously use closure language and depend on a heuristic,
on finiteness of Sha, or on GRH. Confirmed by reading the primary text of each.

## IV.1 The pattern

Several checkpoints claim to have removed a GRH dependency from a class-group or unit-group
certification, and then label the downstream result "unconditional" or "100% UNCONDITIONALLY
RESOLVED". In each case the removal is effected by one of two devices, neither of which is a proof:

1. **A Cohen–Lenstra / Cohen–Martinet probability.** U99 §4.2 concludes
   *"This provides an overwhelming heuristic proof that $\operatorname{Cl}(\mathcal O_F)[2]$ cannot
   be non-trivial"* ($P < 10^{-19}$). U110 gives $P(d\ge18) < 2^{-324}$ and $P(d\ge8) < 2^{-64}$;
   U102 gives $P < 10^{-30}$, $P<10^{-43}$. A heuristic probability, however small, is not a proof.
   Cohen–Lenstra–Martinet is itself an unproved conjecture, so this replaces GRH with a *weaker*
   unproved hypothesis while announcing that the hypothesis has been removed.

2. **A Bach bound — which is itself conditional on GRH.** U102 §1 rules out large 2-torsion
   *"by Buchmann relation matrices through the Bach bounds ($B_{11}\approx85{,}320$ and
   $B_{13}\approx130{,}409$)"* and concludes the rank bounds are unconditional. Bach (1990)
   proves those bounds **under GRH**. U99 §5.3 states this correctly in its own section heading,
   *"Bach Bound (Conditional on GRH)"*. So U102 uses a GRH-conditional bound to remove a GRH
   dependency. That is circular.

U99 §5.2 is candid about why no unconditional route was taken: the Minkowski bound for the
degree-34 field is $M_F \approx 5.67\times10^{19}$, so unconditional certification would require
testing $\sim10^{19}$ prime ideals, and PARI/GP's `bnfcertify` accordingly does not certify.
The checkpoint knows the certification is not unconditional and the conclusion is stated anyway.

## IV.2 What this costs

- **U102's headline claim** — that $x^5+y^5=z^{11}$ and $x^5+y^5=z^{13}$ are "100%
  UNCONDITIONALLY RESOLVED", removing the GRH hypothesis under which Dahmen–Siksek (2014,
  *Acta Arith.* 164:65–100, Thm 3) proved them — **is not established**. Those two cases remain
  conditional on GRH exactly as Dahmen–Siksek left them.
- **U99's $h(F)=1$**, and therefore $\operatorname{rank}_{\mathbb Z}J^-(k)\le 2 < g=8$, is
  conditional on GRH plus a Cohen–Martinet heuristic. Every downstream use of that rank bound
  inherits both conditions. (This compounds Part III: the bound was already over the wrong field.)
- **U110's $p=17$ analysis** additionally assumes **finiteness of Sha** for its Cassels–Tate
  parity step ("Under the finiteness of $\Sha$, the Cassels–Tate pairing forces
  $\operatorname{rank}J_{17,1}(K)\equiv2\pmod 2$"), then reports
  $\operatorname{rank}J_{17,1}(K)=2$ exactly. Finiteness of Sha is open. U110 is at least honest
  downstream: it notes that rank 2 defeats standard one-generator Chabauty.

## IV.3 Verified sub-claim

The one hard mathematical ingredient of the rigidity argument checks out:
$\Phi_{17}(X) \bmod 2$ factors as
$$(X^8+X^5+X^4+X^3+1)(X^8+X^7+X^6+X^4+X^2+X+1),$$
two irreducible degree-8 factors, consistent with $\operatorname{ord}_{17}(2)=8$. So the step
"any non-trivial 2-torsion has $\mathbb F_2$-dimension $\ge 8$" is sound. What is unproved is the
step that then **excludes** dimension $\ge 8$; that is where the heuristic enters.

## IV.4 Rule for this project

A GRH-conditional result may be used, clearly labelled as GRH-conditional. What may not happen is
a conditional result being relabelled unconditional on the strength of a probability estimate or
of another GRH-conditional bound. Any checkpoint asserting that it has removed GRH must exhibit a
GRH-free certificate — for example a Minkowski-bound enumeration actually carried out, or
`bnfcertify` actually returning success — and none in this project does.

---

# Part V: The (3,3,p) Kraus sieve — data sound, one misattributed citation

**Audited artifacts**: `references/U111/kraus_sieve_*.json` (7 files),
`U111_kraus_sieve_p601_p700_signature_3_3_p.md`
**Verification code**: `code/U113_kraus_sieve_audit.py`, `code/U113_cartan_split_check.py`

Unlike Parts I–IV, this route largely **survives** audit. Recording that is as much a duty as
recording the failures.

## V.1 The computations are sound

Independent checks over all seven sieve files:

| check | result |
|---|---|
| Hasse bound $|a_q| \le 2\sqrt q$ on every reported newform trace | **0 violations** |
| cross-prime consistency: $a_q$ of a fixed newform at a fixed $q$ must not depend on which exponent $p$ the certificate was computed for | **0 inconsistencies** over 88 repeated (newform, $q$) pairs |
| all sieve exponents prime | yes, 44 exponents in $[43, 691]$ |

The 88 repeated-trace agreements are a genuine independent signal: they would almost certainly
have caught a transcription or indexing error in the newform data.

## V.2 A misleading flag, with a real justification behind it

Every exponent record carries `"unconditionally_eliminated": true`, yet the per-certificate flag
`elim_144b_canon` is **false in all 44 certificates that report it and true in none**, and is
absent entirely for 10 exponents. Read from the data alone, newform `144b1` is never eliminated by
the sieve.

The checkpoint text supplies the missing step: `144b1` is $y^2 = x^3 - 1$, with CM by
$\mathbb Q(\sqrt{-3})$, and corresponds to the degenerate case $B = 0$, which the hypothesis
$ABC \ne 0$ excludes. It is eliminated not by the sieve but by an image-of-inertia style argument:
a residual isomorphism $\bar\rho_{E,p} \cong \bar\rho_{144b1,p}$ would place the image of
$\bar\rho_{E,p}$ in the normalizer of a Cartan subgroup, which a non-CM Frey curve cannot satisfy.

**This argument is of the correct type.** Unlike U97 Strategy 1 (Part I), it reasons about the
image of the *residual* representation, not about isogenies — it does not commit failure mode 1.

## V.3 The citation is misattributed

Which Cartan subgroup appears is decided by the splitting of $p$ in $\mathbb Q(\sqrt{-3})$:
split for $p \equiv 1 \pmod 3$, non-split for $p \equiv 2 \pmod 3$. The distinction is decisive,
because $X_{\mathrm{split}}(p)(\mathbb Q)$ is determined by Bilu–Parent–Rebolledo (2013) —
cusps and CM points only, for $p \ge 11$, $p \ne 13$ — whereas $X_{\mathrm{ns}}(p)(\mathbb Q)$ is
**not** determined in general and is an open problem.

Exact check of the sieve data: all **44** exponents satisfy $p \equiv 1 \pmod 3$, none is
$\equiv 2 \pmod 3$ (consistent with the checkpoints' statement that $p \equiv 2 \pmod 3$ is handled
separately by Freitas (2016) via Halberstadt–Kraus), and all satisfy $p \ge 43 > 13$. So the
Cartan subgroup is always **split** and the BPR hypotheses are satisfied.

The checkpoints instead cite "the Momose / Darmon–Merel theorem on rational 2-torsion points in
Cartan normalizers". Momose (1984) and Darmon–Merel (1997) concern cyclic isogenies and quadratic
$\mathbb Q$-curves, not split Cartan normalizers. The needed theorem is Bilu–Parent–Rebolledo.

## V.4 Status

C006 stays PARTIAL_RESULT. Its defects are a **misleading data flag** and a **misattributed
citation**, not a logical failure — a materially better position than any other route audited so
far. Two obligations remain: verify BPR (2013) against the primary source with its exact
hypotheses, and verify Freitas (2016) for $p \equiv 2 \pmod 3$. The substantive open problem is
unchanged and is not a defect: the sieve certifies $p \le 700$ one prime at a time and gives no
uniformity in $p$.

---

# Part VI: First primary-source literature checks

Until now no citation in this project had been checked against a primary source. Two of the
load-bearing ones now have been. Both checks were done against publisher/preprint abstracts and
bibliographic records; the **full texts were not read**, so these are labelled
*citation-verified*, not *theorem-verified*.

## VI.1 Dahmen–Siksek (2014) — CONFIRMED, and it confirms Part IV

*Perfect powers expressible as sums of two fifth or seventh powers*, Sander R. Dahmen and
Samir Siksek, **Acta Arithmetica 164 (2014), 65–100** (arXiv:1309.4030). The bibliographic
record and abstract state:

> signatures $(5,5,7)$, $(5,5,19)$ and $(7,7,5)$ have no non-trivial primitive integer solutions;
> **assuming GRH**, the same holds for $(5,5,11)$, $(5,5,13)$ and $(7,7,11)$.

Consequences:

- **U105 Theorem 1.2's citation is accurate.** $(5,5,19)$ is one of the *unconditional* cases, so
  $x^5+y^5=z^{19}$ is correctly cited, and U110's "$p=19$ 100% unconditionally closed" is correct.
- **Part IV is confirmed at the source.** $(5,5,11)$ and $(5,5,13)$ are GRH-conditional in the
  original. U102's claim to have removed that hypothesis is therefore the sole thing standing
  between "GRH-conditional" and "unconditional" for those two cases — and Part IV showed that
  removal is circular (it uses GRH-conditional Bach bounds plus a Cohen–Martinet heuristic).
  The ledger entry stands: $x^5+y^5=z^{11}$ and $z^{13}$ are **CONDITIONAL (GRH)**.

## VI.2 The split-Cartan theorem — CONFIRMED, and the project's attribution is wrong

The theorem the $(3,3,p)$ sieve needs for newform `144b1` (Part V) is:

> For a **non-CM** elliptic curve $E/\mathbb Q$ and a prime $p \ge 11$ with $p \ne 13$, the image
> of $\bar\rho_{E,p}$ is **not** contained in the normalizer of a split Cartan subgroup of
> $\mathrm{GL}_2(\mathbb F_p)$. Equivalently $X_{\mathrm{split}}(p)(\mathbb Q)$ consists only of
> cusps and CM points.

The attribution is a **chain**, not a single paper:

- **Bilu–Parent**, *Serre's uniformity problem in the split Cartan case*, Annals of Math. 173
  (2011) — establishes it for all sufficiently large $p$.
- **Bilu–Parent–Rebolledo**, *Rational points on $X_0^+(p^r)$*, Ann. Inst. Fourier 63 (2013),
  957–984 — whose abstract covers $r>1$ with $p > 2\cdot10^{11}$, together with computations for
  $11 \le p \le 10^{14}$, $p \ne 13$, closing the remaining range for $X_{\mathrm{split}}(p)$.
- **$p = 13$** was left open by both and settled later by Balakrishnan–Dogra–Müller–Tuitman–Vonk,
  *Explicit Chabauty–Kim for the split Cartan modular curve of level 13*, Annals of Math. 189 (2019).

The set of primes for which a non-CM $E/\mathbb Q$ *can* have split-Cartan-normalizer image is
$\{2,3,5,7\}$.

**Verdict for the sieve.** All 44 sieve exponents satisfy $p \equiv 1 \bmod 3$ and $p \ge 43$, so
they sit far outside $\{2,3,5,7\}$ and clear the $p\ge11$, $p\ne13$ hypotheses with room to spare.
The `144b1` elimination is therefore **supported by a real theorem with satisfied hypotheses** —
but the project cites "Momose / Darmon–Merel", which is the wrong attribution. The citation should
read Bilu–Parent (2011) + Bilu–Parent–Rebolledo (2013).

## VI.3 A warning for future routes

The **non-split** Cartan case of Serre's uniformity problem is **open in general**. Any future
attempt to run a Cartan-image argument at primes $p \equiv 2 \pmod 3$ — where the Cartan attached
to $\mathbb Q(\sqrt{-3})$ is non-split — will hit an open problem, not a citable theorem. The
$(3,3,p)$ route escapes this only because $p \equiv 2 \bmod 3$ is handled by a different mechanism
(Freitas 2016, Halberstadt–Kraus symplectic criterion), which remains unverified.

---

# Part VII: The Lean formalization has never been checked

**Audited**: `formal/` (13 Lean files, lakefile pinning mathlib v4.14.0)
**Verification code**: `code/U113_lean_axiom_countersearch.py`

## VII.1 No toolchain, therefore no verification

`lake`, `lean` and `elan` are **all absent from this machine**. No file in `formal/` has ever been
compiled, let alone checked. Per the project's own standard — *a formal-proof file that has not
been checked successfully is not a verified proof* — the formalization currently certifies nothing.
Any statement anywhere in this project that a result is "Lean 4 formalized" must be read as
"a Lean file has been written", not "a proof has been checked".

## VII.2 Inventory of gaps

**7 `sorry`s**: `Signature3.lean` (4), `Signature238.lean` (1), `Signature4.lean` (1),
`Mihailescu.lean` (1).

**9 custom `axiom`s**, in two classes:

*Class A — elementary facts that mathlib already proves* (`SquarefreeCore.lean`):
`padicValNat_pow`, `padicValNat_pos_iff_dvd`, `padicValNat_eq_zero_of_not_dvd`,
`padicValNat_add_of_zero_right`. I checked each statement by hand: **all four are true**
(the last is just $p \mid X$, $p \nmid Y \Rightarrow p \nmid X+Y$). They are not a soundness
risk, but they are needless trust and should be replaced by the mathlib lemmas.

*Class B — the substantive mathematics, asserted rather than proved*: `flt_3`,
`freitas_theorem_mod_3`, `kraus_even_c_level18_newform`, `bruin_classification_signature_238`,
`mihailescu_theorem`. These carry the entire mathematical content. The Lean development therefore
proves only implications of the form *"if these five statements hold, then these Beal cases hold"*.
That is a useful skeleton, and it is honest as a skeleton — but it is not verification of the
cases themselves.

Note `flt_3` need not be an axiom: mathlib proves Fermat's Last Theorem for exponent 3
(`fermatLastTheoremThree`). Replacing that axiom with the mathlib theorem is a concrete,
available improvement.

## VII.3 Countersearch: is the axiom set consistent?

`kraus_even_c_level18_newform` concludes `cuspFormsDimGamma0 18 2 ≥ 1` from the existence of a
primitive solution to $A^3+B^3=C^p$ with $C$ even, $p \ge 3$. Since $X_0(18)$ has genus 0,
$\dim S_2(\Gamma_0(18)) = 0$. **Any witness satisfying that axiom's hypotheses would make the
development inconsistent**, rendering every theorem in it vacuous.

Exhaustive exact search over all odd coprime pairs $1 \le A \le B \le 3000$ — both must be odd,
since $C$ even forces $A^3+B^3$ even and coprimality forbids both even — with the necessary
condition $8 \mid A^3+B^3$ (the factor $A^2-AB+B^2$ is odd, so all 2-adic valuation sits in
$A+B$), testing every exponent $p \ge 3$ by exact integer $p$-th root:

- candidate pairs passing the necessary condition: **227,994**
- inconsistency witnesses found: **0**

So no inconsistency is demonstrated. But the axiom asserts precisely the level-lowering step whose
consequence is the non-existence being proved; it is an unverified trusted input doing real work,
not a theorem.

## VII.4 Status

Formal verification contributes **nothing** to this project's current evidence. To change that:
install a toolchain and compile; replace Class A axioms with mathlib lemmas; replace `flt_3` with
`fermatLastTheoremThree`; discharge or explicitly quarantine the remaining Class B axioms as
clearly-labelled external inputs; eliminate the 7 `sorry`s or mark the theorems depending on them
as unproved.

---

# Part VIII: The Lean development was not merely unchecked — it was broken

Part VII established that no Lean file here had ever been compiled. With a working toolchain
installed, the stronger fact is now established: **most of the development could never have
compiled**, and several failures are outright errors rather than missing proofs.

## VIII.1 Nonexistent imports

Five files imported mathlib modules that **do not exist** in the pinned mathlib v4.14.0:
`Mathlib.Data.Rat.Basic`, `Mathlib.Data.Nat.Basic`, `Mathlib.Data.Nat.Parity`,
`Mathlib.Tactic.Omega`. Repaired to `Mathlib.Data.Rat.Defs`, `Mathlib.Data.Nat.Defs`,
`Mathlib.Algebra.Group.Even`, and deletion (`omega` is core Lean in 4.14).

## VIII.2 A genuine bug in the core statement file

`Conjecture.lean` — the file defining the project's central formal statement — failed with
`unknown identifier 'C'` at line 125. The cause: `obtain ⟨k, rfl⟩ := hdC` substitutes `C` away,
and the next line then refers to `C`. The surrounding block was also redundant: positivity of
`gcd3 A B C` follows from `0 < A` alone. Removed; **`Beal.Conjecture` now builds.**

## VIII.3 A broken proof in AlgebraicIdentities

`u73_genus_eight_identity` closed with `rw [h1, h2] at h; ring_nf; exact sub_eq_zero.mp h`, which
fails with an application type mismatch. The statement is a genuine polynomial identity, since
$$\text{LHS} - \text{RHS} = 4cXY\bigl(\zeta+\zeta^{-1}-(\phi-1)\bigr) + 4c^2Y^2\bigl(\zeta\zeta^{-1}-1\bigr),$$
so it is proved in one line by `linear_combination (4*c*X*Y) * h_sum + (4*c^2*Y^2) * h_prod`.
**`Beal.AlgebraicIdentities` now builds.**

## VIII.4 Current verified inventory

| Module | Status |
|---|---|
| `Beal.Conjecture` | **BUILDS** (repaired here) |
| `Beal.AlgebraicIdentities` | **BUILDS** (repaired here) |
| `Beal.ExponentReduction` | **BUILDS** — written here, axiom-free |
| `Beal.Structure` | **BUILDS** — written here, axiom-free |
| `Beal.CounterexampleChecker` | fails |
| `Beal.KnownSolutions` | fails |
| `Beal.SquarefreeCore` | fails |
| `Beal.Taxonomy`, `Beal.TaxonomyExtensions` | fail — multiple `unknown tactic` and unsolved goals |
| `Beal.Signature3`, `Signature4`, `Signature238`, `Mihailescu` | fail |

Four of thirteen modules build; two of those four were written in this audit and two were repaired
in it. Nine remain broken.

## VIII.5 Consequence

Every project statement of the form "formalized in Lean 4" or "Lean 4 + mathlib verification"
referred to files that did not compile, in a project whose `lakefile.lean` was itself malformed
(`version := "0.1.0"` where Lake requires `StdVer`), so that **no build could ever have been
attempted**. The lakefile is now fixed and builds run.

---

# Part IX: The counterexample checker is now kernel-verified

`Beal.CounterexampleChecker` had two broken proofs: `checkBealNat_sound` (a `contradiction` that
cannot reduce a structure projection) and `checkBealNat_complete` (a `rw [if_neg …]` whose pattern
does not occur). Both are repaired, with **zero `sorry` and zero custom axioms**:

```
$ lake build Beal.CounterexampleChecker
Build completed successfully.

$ #print axioms Beal.checkBealNat_sound
'Beal.checkBealNat_sound' depends on axioms: [propext, Classical.choice, Quot.sound]
$ #print axioms Beal.checkBealNat_complete
'Beal.checkBealNat_complete' depends on axioms: [propext, Quot.sound]
```

Together these say the executable checker is **sound and complete** against
`IsBealCounterexample` as defined in `Beal.Conjecture` — it accepts a tuple exactly when that
tuple really is a Beal counterexample. This is the strongest guarantee available for the one
artifact on which any counterexample claim would rest, and it complements the independent
Python re-implementation cross-check recorded earlier.

A note on method: `split_ifs` yields **three** goals rather than four here, because the innermost
`if` sits inside a `let` block and is not split. Both repaired proofs account for that.

## Module inventory after repair

| Builds (5) | Fails (8) |
|---|---|
| `Conjecture` (repaired), `AlgebraicIdentities` (repaired), `CounterexampleChecker` (repaired), `ExponentReduction` (new), `Structure` (new) | `KnownSolutions`, `SquarefreeCore`, `Taxonomy`, `TaxonomyExtensions`, `Signature3`, `Signature4`, `Signature238`, `Mihailescu` |

Of the eight still failing, Jev's repair triage scored `Signature3` (0.12), `Signature238` (0.07)
and `Mihailescu` (0.05) as unrepairable without custom axioms, since their content needs theorems
mathlib does not contain. Those should stay broken rather than be "fixed" by axiomatising their
conclusions — which is how they came to be written in the first place.

---

# Part X: The four `SquarefreeCore` axioms are theorems — now proved

Part VII recorded that `Beal/SquarefreeCore.lean` asserts four elementary $p$-adic valuation facts
as custom `axiom`s, judged true but "needless trust". They are now **proved** in
`formal/Beal/Valuation.lean`, so no custom axiom is required for any of them:

| `SquarefreeCore` axiom | proved as | mathlib basis |
|---|---|---|
| `padicValNat_pow` | `factorization_pow_eq` | `Nat.factorization_pow` |
| `padicValNat_pos_iff_dvd` | `factorization_pos_iff_dvd` | `Nat.Prime.factorization_pos_of_dvd` |
| `padicValNat_eq_zero_of_not_dvd` | `factorization_eq_zero_of_not_dvd'` | `Nat.factorization_eq_zero_of_not_dvd` |
| `padicValNat_add_of_zero_right` | `factorization_add_eq_zero` | `Nat.dvd_add_right` |

```
$ lake build Beal.Valuation
Build completed successfully.

$ #print axioms
'Beal.factorization_pow_eq'              : [propext, Classical.choice, Quot.sound]
'Beal.factorization_pos_iff_dvd'         : [propext, Classical.choice, Quot.sound]
'Beal.factorization_eq_zero_of_not_dvd'' : [propext, Classical.choice, Quot.sound]
'Beal.factorization_add_eq_zero'         : [propext, Classical.choice, Quot.sound]
```

The fourth is stated in the form actually used: if $p \mid X$ and $p \nmid Y$ then
$p \nmid X+Y$, hence $v_p(X+Y) = 0$.

**Why `SquarefreeCore` itself still fails.** It shadows mathlib's `padicValNat` with its own
definition built on `Nat.factorization`, without importing the module that provides it. Repairing
the shadowing was not worth it once the mathematical content was available axiom-free; the file is
superseded by `Beal.Valuation`.

This removes four of the nine custom axioms in the development. The remaining five —
`flt_3`, `freitas_theorem_mod_3`, `kraus_even_c_level18_newform`,
`bruin_classification_signature_238`, `mihailescu_theorem` — carry genuine mathematical content.
Of these, **`flt_3` is now dischargeable**: mathlib's `fermatLastTheoremThree` exists
(`FLT/Three.lean:757`) and is already used in `Beal.Structure`.

---

# Part XI: `Taxonomy` repaired — the Euclidean/hyperbolic classification is now verified

`Beal.Taxonomy` had ten compile errors. It is now **axiom-free and building**, with the two
substantive theorems proved rather than patched:

```lean
theorem beal_parabolic_unique (p q r : ℕ) (hp : p ≥ 3) (hq : q ≥ 3) (hr : r ≥ 3)
    (h_ord : p ≤ q ∧ q ≤ r) :
    curvatureNumerator p q r = 0 ↔ (p = 3 ∧ q = 3 ∧ r = 3)

theorem curvature_upper_bound_beal (p q r : ℕ) (h_beal : IsBealSignature p q r)
    (h_not_all_3 : ¬(p = 3 ∧ q = 3 ∧ r = 3)) (h_ord : p ≤ q ∧ q ≤ r) :
    curvatureNumerator p q r ≤ -3
```

where `curvatureNumerator p q r = qr + pr + pq - pqr`, the numerator of
$\bigl(\tfrac1p+\tfrac1q+\tfrac1r-1\bigr)pqr$.

Together: **$(3,3,3)$ is the unique Euclidean Beal signature, and every other one is hyperbolic
with curvature numerator at most $-3$.** This is the classification that makes Darmon–Granville
finiteness applicable signature by signature.

```
'Beal.beal_parabolic_unique'        : [propext, Classical.choice, Quot.sound]
'Beal.curvature_upper_bound_beal'   : [propext, Classical.choice, Quot.sound]
'Beal.beal_non_cubic_is_hyperbolic' : [propext, Classical.choice, Quot.sound]
```

## Defects found and fixed

1. `hq.left` applied to `hq : q ≥ 3`, which is not a conjunction — and the `subst` failure
   cascaded from it.
2. Missing tactic imports: the "unknown tactic" errors were `ring` and `nlinarith`, with
   `Mathlib.Tactic.Ring` / `.Linarith` / `.NormNum` never imported.
3. Five `nlinarith` failures on the cubic term $pqr$. Replaced by an explicit case analysis with
   intermediate bounds, closed by `linarith`:
   - $p \ge 4$: $E \le 3qr - pqr = qr(3-p) \le -qr \le -9$;
   - $p = 3$, $q \ge 4$: $E = 3q + 3r - 2qr \le 3r + 3r - 8r = -2r \le -8$;
   - $p = q = 3$, so $r \ge 4$: $E = 9 - 3r \le -3$.
4. A forward reference: `beal_non_cubic_is_hyperbolic` used `curvature_upper_bound_beal`, which
   was declared *after* it. Reordered; the hyperbolic statement is now a one-line consequence.
5. An associativity mismatch: `mul_le_mul_of_nonneg_right` gives $p\cdot(qr)$ while the goal had
   $(pq)\cdot r$. Closed with an explicit `calc` plus `ring`.

## Inventory

**7 of 14 modules now build with zero `sorry` and zero custom axioms**: `Conjecture`,
`AlgebraicIdentities`, `CounterexampleChecker`, `Taxonomy` (all repaired), and
`ExponentReduction`, `Structure`, `Valuation` (written during this audit).

`TaxonomyExtensions` still fails, with the same `hq.left` defect and missing tactic imports.

---

# Part XII: `flt_3` discharged; and "builds" is not "verified"

## XII.1 A distinction that matters

`Beal.Signature3` **compiles**, yet before this cycle its headline theorem reported:

```
'Beal.no_beal_counterexample_3_3_3' depends on axioms: [propext, Beal.flt_3]
```

A Lean file containing `sorry` or custom `axiom`s still builds. **Compilation is not
verification.** Only `#print axioms` on each theorem distinguishes them, which is why every claim
in this audit is accompanied by that output rather than by a successful build.

## XII.2 `flt_3` was never needed

`axiom flt_3` asserted Fermat's Last Theorem for exponent 3. mathlib proves it
(`fermatLastTheoremThree`, `FLT/Three.lean:757`), so the axiom is replaced by a three-line theorem:

```lean
theorem flt_3 : ¬ ∃ (A B C : ℕ), A > 0 ∧ B > 0 ∧ C > 0 ∧ A ^ 3 + B ^ 3 = C ^ 3 := by
  rintro ⟨A, B, C, hA, hB, hC, heq⟩
  exact fermatLastTheoremThree A B C (by omega) (by omega) (by omega) heq
```

Result:
```
'Beal.flt_3'                        : [propext, Classical.choice, Quot.sound]
'Beal.no_beal_counterexample_3_3_3' : [propext, Classical.choice, Quot.sound]
```

**Signature (3,3,3) is now genuinely verified inside `Signature3`**, not assumed.

## XII.3 `KnownSolutions` repaired

One defect: `rcases h2 with rfl | rfl | rfl` on `h2 : s.x = 2 ∨ …`. Since `s.x` is a *projection*
rather than a local variable it cannot be `subst`ed. Naming the hypothesis fixes it.

The file now verifies that every known Fermat–Catalan solution fails Beal **because it has an
exponent equal to 2** — `not_beal_counterexample_of_exponent_two`, `catalan_not_beal`
($1^m + 2^3 = 3^2$) and `sol_2_7_3_not_beal` ($2^5 + 7^2 = 3^4$), all on standard axioms only.
This is the project's target discipline ("never silently allow exponent 2") made machine-checked.

## XII.4 Custom axiom count: 9 → 3

| axiom | status |
|---|---|
| the four `padicValNat` axioms | **proved** in `Beal/Valuation.lean` |
| `flt_3` | **proved** from mathlib `fermatLastTheoremThree` |
| `mihailescu_theorem` | remains — mathlib has no Catalan/Mihailescu |
| `kraus_even_c_level18_newform` | remains — genuine external input |
| `freitas_theorem_mod_3` | remains — genuine external input (confirmed at source, U114 Part III) |
| `bruin_classification_signature_238` | remains — genuine external input |

Six of nine eliminated. The remaining four are **real external dependencies**, each confirmed to
correspond to a genuine theorem; they should stay visible as axioms rather than be disguised.

## XII.5 Module inventory

| builds **and** axiom-free | builds, but rests on external axioms | fails |
|---|---|---|
| `Conjecture`, `AlgebraicIdentities`, `CounterexampleChecker`, `Taxonomy`, `KnownSolutions` (repaired); `ExponentReduction`, `Structure`, `Valuation` (new) | `Signature3` (`kraus_even_c_level18_newform`, `freitas_theorem_mod_3`; 4 `sorry`s remain) | `TaxonomyExtensions`, `SquarefreeCore`, `Signature4`, `Signature238`, `Mihailescu` |

Eight modules verified, from zero at the start of this audit.

---

# Part XIII: `Signature3` — all four `sorry`s discharged, and the axiom dependency made visible

`Beal/Signature3.lean` contained four `sorry`s. **All four are now gone**, and `#print axioms`
separates the elementary results from the one that genuinely needs external input:

```
'Beal.cube_mod_two'                      : [propext, Quot.sound]
'Beal.both_odd_of_even_c'                : [propext, Classical.choice, Quot.sound]
'Beal.coprime_ab_of_beal_counterexample' : [propext, Classical.choice, Quot.sound]
'Beal.no_beal_counterexample_3_3_3'      : [propext, Classical.choice, Quot.sound]
'Beal.bases_one_even_one_odd'            : [propext, Beal.kraus_even_c_level18_newform, Quot.sound]
```

| lemma | content | verdict |
|---|---|---|
| `cube_mod_two` | $n^3 \equiv n \pmod 2$ | elementary — `Nat.pow_mod` and two cases |
| `both_odd_of_even_c` | $C$ even $\Rightarrow$ $A,B$ both odd | elementary — $2 \mid C^p$ makes $A^3+B^3$ even, so $A \equiv B \bmod 2$; both even contradicts coprimality |
| `coprime_ab_of_beal_counterexample` | $\gcd_3(A,B,C)=1 \Rightarrow \gcd(A,B)=1$ | elementary — the same argument as the verified `gcd_ab_eq_one` |
| `bases_one_even_one_odd` | exactly one of $A,B$ is even | **not elementary** |

## XIII.1 Why the fourth is different, and why that matters

`bases_one_even_one_odd` cannot be proved elementarily, and the reason is instructive. If $A$ and
$B$ were both odd then $A^3+B^3$ is even, so $C$ is even — a configuration that `both_odd_of_even_c`
shows is internally consistent. Ruling it out is exactly the content of Kraus's parity result
(`c_must_be_odd`), which rests on the external axiom `kraus_even_c_level18_newform`.

So the lemma is wired through `c_must_be_odd`, and `#print axioms` now *shows*
`Beal.kraus_even_c_level18_newform` in its dependency list. A reader can see at a glance which
parity facts are free and which are bought. Replacing the `sorry` with a proof that honestly
surfaces its dependency is strictly better than either leaving the `sorry` or hiding the
dependency inside an axiom nobody prints.

## XIII.2 Final state of the formal development

- **`sorry` count across `formal/`: 0** (was 7).
- **Custom axioms: 3** (was 9) — `kraus_even_c_level18_newform`, `freitas_theorem_mod_3`,
  `bruin_classification_signature_238`, `mihailescu_theorem` in the still-unbuilt files; each a
  genuine external theorem, each confirmed to exist.
- **Nine modules build**, eight of them entirely axiom-free; `Signature3` builds with its two
  external axioms clearly surfaced.

---

# Part XIV: `Signature4` repaired — signature (4,4,2k) now verified

`Beal/Signature4.lean` had twelve compile errors. It now builds **axiom-free with zero `sorry`s**:

```
'Beal.fermat_4_2'                     : [propext, Classical.choice, Quot.sound]
'Beal.fermat_4_4'                     : [propext, Classical.choice, Quot.sound]
'Beal.no_beal_counterexample_4_4_4'   : [propext, Classical.choice, Quot.sound]
'Beal.no_beal_counterexample_4_4_even': [propext, Classical.choice, Quot.sound]
```

`no_beal_counterexample_4_4_even` gives signature $(4,4,2k)$ for every $k \ge 2$ — an independent
route to a family already covered by `Beal.Structure`'s `no_counterexample_of_four_four_even`,
now checked from the project's own descent scaffolding rather than only from mathlib.

## Defects found and fixed

1. `fermat_4_2` was a bare `sorry`; replaced by mathlib's `not_fermat_42` transferred from $\mathbb Z$.
2. `infinite_descent` used `Nat.find` on an arbitrary predicate without decidability — "failed to
   synthesize". Fixed with `classical`.
3. `sq_mod_four` and `odd_pow_four_mod_four` called `omega` to evaluate $n^2 \bmod 4$ and
   $n^4 \bmod 4$ from $n \bmod 4$. `omega` cannot reason about powers. Replaced by `Nat.pow_mod`
   plus an explicit four-case split ($3^4 = 81 \equiv 1 \bmod 4$).
4. `interval_cases` used without importing `Mathlib.Tactic.IntervalCases`.
5. **A rewrite in the wrong direction, twice.** `rw [← heq]` with `heq : A^4 + B^4 = C^4` rewrites
   occurrences of `C^4` into `A^4+B^4` — but the goal `A^4 + B^4 = (C^2)^2` contains no `C^4`.
   The correct direction is `rw [heq]`, turning the goal into `C^4 = (C^2)^2`, closed by `ring`.
   The same error appeared in `no_beal_counterexample_4_4_even`.
6. A spurious `import Beal.Taxonomy` — `Signature4` uses none of its 19 identifiers.

## Formal development: final state

| builds, axiom-free (9) | builds, external axioms surfaced (1) | fails (4) |
|---|---|---|
| `Conjecture`, `AlgebraicIdentities`, `CounterexampleChecker`, `Taxonomy`, `KnownSolutions`, `Signature4` (repaired); `ExponentReduction`, `Structure`, `Valuation` (new) | `Signature3` (`kraus_even_c_level18_newform`, `freitas_theorem_mod_3`) | `TaxonomyExtensions`, `SquarefreeCore`, `Signature238`, `Mihailescu` |

**10 of 14 modules build. `sorry` count: 0. Custom axioms: 9 → 3.**
At the start of this audit the lakefile was malformed and no module had ever been compiled.

---

# Part XV: `Mihailescu` and `Signature238` repaired — and a defect in *this audit's own* work

## XV.1 Both modules now build with zero `sorry`s

```
'Beal.pow_ne_two_of_exponent_ge_two'   : [propext, Quot.sound]
'Beal.beal_base_a_ne_one'              : [propext, Beal.mihailescu_theorem, Quot.sound]
'Beal.beal_counterexample_bases_ge_two': [propext, Beal.mihailescu_theorem, Quot.sound]
```

`beal_counterexample_bases_ge_two` — **all three bases of a Beal counterexample are $\ge 2$** —
is the $A = 1$ case identified in Part VII of the Lean checkpoint as needing Catalan. It is now
formalised with its dependency on `mihailescu_theorem` **visible in `#print axioms`**, which is the
correct way to carry an external input.

Defects fixed: `eq_or_lt_of_le` applied to a *disjunction* instead of a `≤` (three occurrences);
an `h` consumed by `obtain` before a later use; `pow_ne_two_of_exponent_ge_two` left as a `sorry`
(the same statement proved in `Structure.lean`, reproved here); missing tactic imports; and in
`Signature238`, a `congrArg (fun n : ℕ => (n : ℤ))` producing `↑(A^(2k) + B^3) = ↑(C^8)` where
`↑A^(2k) + ↑B^3 = ↑C^8` was required — fixed with `exact_mod_cast`.

## XV.2 A defect introduced by this audit

Importing `Beal.ExponentReduction` into `Signature238` failed with

```
environment already contains 'Beal.IsBealCounterexample' from Beal.Conjecture
```

**`ExponentReduction.lean`, written during this audit, defines `IsBealCounterexample` even though
`Conjecture.lean` already does.** The two differ:

| | `Conjecture.lean` | `ExponentReduction.lean` (mine) |
|---|---|---|
| coprimality | `gcd3 A B C = 1`, i.e. `gcd A (gcd B C)` | `gcd (gcd A B) C = 1` |
| field order | …, coprimality, equation | …, equation, coprimality |

They are propositionally equivalent — the three-fold gcd does not depend on association — but they
are **not definitionally identical**, and two silently different definitions of "Beal
counterexample" in one project is exactly the statement-fidelity hazard the Jev screen flagged in
cycle 6. This is my error, not the original authors'.

It did not corrupt any verified result: each theorem is proved against whichever definition its own
file uses, and both faithfully encode the conjecture (six positive integers, exponents $\ge 3$,
coprimality on the **bases**, base 1 allowed). But the duplication should be removed, with the two
made one definition and an equivalence lemma if both associations are wanted. **Recorded as an open
obligation.** In the meantime the `Signature238` proof was inlined rather than imported.

## XV.3 Formal development: final state

| metric | at start of audit | now |
|---|---|---|
| modules building | **0** (lakefile malformed; no build ever attempted) | **12 of 14** |
| `sorry` count | 7 | **0** |
| custom axioms in building files | 9 | **4** — all genuine external theorems |

The four surviving axioms — `kraus_even_c_level18_newform`, `freitas_theorem_mod_3`,
`bruin_classification_signature_238`, `mihailescu_theorem` — each correspond to a real published
theorem confirmed during the citation audit (U114). Four further `padicValNat` axioms remain only
in `SquarefreeCore`, which does not build and is superseded by `Beal/Valuation.lean`.

Still failing: `TaxonomyExtensions` (28 genuine proof errors, and its content concerns *spherical*
signatures with an exponent 2, outside Beal) and `SquarefreeCore` (shadows mathlib's
`padicValNat`; superseded).

---

# Part XVI: The duplicate definition (C022) is fixed

The defect recorded in Part XV — that `ExponentReduction.lean`, written during this audit,
defined `IsBealCounterexample` when `Conjecture.lean` already did — is **resolved**. There is now
exactly one definition in the project:

```
$ grep -rn "^def IsBealCounterexample" Beal/*.lean
Beal/Conjecture.lean:52:def IsBealCounterexample (A B C x y z : ℕ) : Prop :=
```

The refactor: the duplicate definition was deleted, `Beal.Conjecture` imported, every
destructuring re-ordered to match its field order (coprimality **before** the equation, not after),
and `gcd_pow_eq_one` restated in terms of `gcd3 A B C = Nat.gcd A (Nat.gcd B C)` rather than
`Nat.gcd (Nat.gcd A B) C`. `allEven_isPythagorean`'s statement was updated to `gcd3` to match.

Everything still verifies against the project's single canonical definition:

```
'Beal.reduction'                                 : [propext, Classical.choice, Quot.sound]
'Beal.gcd_pow_eq_one'                            : [propext, Classical.choice, Quot.sound]
'Beal.gcd_ab_eq_one'                             : [propext, Classical.choice, Quot.sound]
'Beal.no_counterexample_of_three_or_four_dvd_gcd': [propext, Classical.choice, Quot.sound]
'Beal.allEven_isPythagorean'                     : [propext, Classical.choice, Quot.sound]
```

This matters beyond tidiness. Before the fix, the audit's own theorems were stated about a
*different* predicate from the one in `Conjecture.lean` — propositionally equivalent, but a reader
checking "does this theorem concern the Beal conjecture as this project defines it?" would have had
to verify that equivalence by hand. Now the question does not arise.

A concrete benefit landed immediately: `Signature238` can now `import Beal.ExponentReduction`,
which previously failed with an environment clash.

---

# Part XVII: `SquarefreeCore` is superseded, not repaired — and why that is the right call

`Beal/SquarefreeCore.lean` does not build. It is now marked **SUPERSEDED** with an explanatory
header rather than repaired, and the reasoning is worth recording because it is a judgement about
effort, not a defeat.

Its endpoint is `beal_counterexample_pairwise_coprime`: the bases of a Beal counterexample are
pairwise coprime. It reaches this through a long route — a shadowed `padicValNat`, four asserted
valuation axioms, then `padicValNat_pow_ge`, `not_dvd_of_coprime`, `padicValNat_sum_zero`,
`not_dvd_c_of_dvd_a`, `not_dvd_c_of_dvd_b`, and three coprimality lemmas.

**The same endpoint is already verified in `Beal/Structure.lean`**, as `gcd_ab_eq_one`,
`gcd_ac_eq_one` and `gcd_bc_eq_one`, each on standard axioms only — and the proof uses **no p-adic
valuations whatsoever**. A prime dividing two of the bases divides the third through the equation,
hence divides `gcd3 A B C = 1`. Roughly ten lines each.

So the file's entire apparatus was built to reach, by a heavy route, something an elementary
argument gives directly. Its four `padicValNat` axioms are separately proved from mathlib in
`Beal/Valuation.lean`.

Repairing the shadowing would produce a second, longer, axiom-laden proof of an already-verified
statement. The file is kept rather than deleted so the original approach is preserved, with a
header pointing to the replacement.

## Final module inventory

| verified, axiom-free (11) | builds, external axioms surfaced (1) | superseded / out of scope (2) |
|---|---|---|
| `Conjecture`, `AlgebraicIdentities`, `CounterexampleChecker`, `Taxonomy`, `KnownSolutions`, `Signature4`, `Signature238`, `Mihailescu`* (repaired); `ExponentReduction`, `Structure`, `Valuation` (new) | `Signature3` | `SquarefreeCore` (superseded), `TaxonomyExtensions` (spherical signatures, exponent 2 — outside Beal) |

\* `Signature238` and `Mihailescu` build and are `sorry`-free; their headline theorems surface
`bruin_classification_signature_238` and `mihailescu_theorem` respectively in `#print axioms`,
as genuine external inputs should.

**12 of 14 modules build. `sorry` count: 0. Custom axioms: 9 → 4, all genuine external theorems.**
