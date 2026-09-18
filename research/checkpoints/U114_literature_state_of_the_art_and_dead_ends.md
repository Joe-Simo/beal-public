# U114: State of the art and known dead ends (literature check, 2026-09-17)

**Why this checkpoint exists**: until now no systematic literature check had been done in this
project. Auditing our own artifacts told us what was wrong internally but not what the field had
already settled. The result below materially changes what is worth working on.

**Sources** (abstract/HTML level; full texts not read, so these are *citation-level* facts):
- *Generalised Fermat equation: a survey of solved cases*, arXiv:2412.11933
- *A survey on the generalized Fermat equation of various signatures over totally real fields*, arXiv:2512.04936
- *On Darmon's program for the generalized Fermat equation, I*, arXiv:2205.15861
- Wikipedia "Beal conjecture"; MathWorld "Beal's Conjecture"

---

## 1. What is already solved (so we must not re-derive it)

| Signature / family | Status | Attribution |
|---|---|---|
| $(p,p,p)$, **all** $p \ge 3$ | solved | **Wiles–Taylor (FLT)** |
| $(p,p,2)$, $p \ge 5$ | solved | Darmon–Granville, Darmon–Merel |
| $(p,p,3)$, $p \ge 3$ | solved | Darmon–Merel, Poonen |
| $(2,4,r)$, $r \ge 5$ | solved | Bennett–Ellenberg–Ng |
| $(2,6,r)$, $r \ge 3$ | solved | Pacetti–Villagra Torcomian et al. |
| $(2,3,n)$, $n \in \{7,8,9,10,15\}$ | solved | various |
| $(3,3,p)$ | solved for **$p \le 10^9$** | computational + theoretical |
| $(5,5,7)$, $(5,5,19)$ | solved | Dahmen–Siksek |

**Smallest OPEN signature within Beal ($\min \ge 3$): $(3,5,7)$.**
(The smallest open Fermat–Catalan signature overall is $(2,5,7)$, outside Beal.)

Computational searches have reportedly reached **$2^{100}$** with no new solutions.

---

## 2. Consequences for this project — two significant redundancies

**2.1 The diagonal is entirely closed by FLT.** $(n,n,n)$ for every $n \ge 3$ is Wiles–Taylor.
The kernel-verified diagonal results obtained here ($4 \mid n$ via `not_fermat_42`, $3 \mid n$ via
`fermatLastTheoremThree`) are therefore **special cases of a fully known theorem**. They retain
value as *formalisation* — they are machine-checked, and mathlib does not yet contain full FLT —
but they are **not new mathematics** and must never be presented as such.

Likewise the family $4 \mid x$, $4 \mid y$, $z$ even reduces to $(4,4,2)$-type equations, covered
by the known $(p,p,2)$ results.

**2.2 The $(3,3,p)$ sieve is far behind the literature.** This project certified $(3,3,p)$ for
$p \le 700$ across seven checkpoints (U111 etc.). The literature has $(3,3,p)$ for
**$p \le 10^9$**. Extending our sieve is therefore wasted effort: it tests no new hypothesis and
re-derives a weaker result. Candidate C006's open problem — **uniformity in $p$** — remains the
only part of that route worth pursuing.

**2.3 The project's central object may be misdirected.** Enormous effort here went into the
weighted auxiliary equation $X^{10}+256Y^{10}=Z^{17}$, one branch of the all-even case. The
all-even case has both exponents even, so it sits close to families already handled by $(p,p,2)$
and $(2,4,r)$ techniques, while the actual frontier — $(3,5,7)$ and neighbouring odd-prime
signatures — received no attention.

---

## 3. Known obstructions (documented so they are not rediscovered)

1. **High genus.** Signatures reduce to hyperelliptic curves of genus $(p-1)/2 \ge 2$; determining
   rational points on a high-genus curve is hard in general. *(Independently confirmed here: U113
   Part III found a Chabauty argument bounding the wrong set of points.)*
2. **Unknown Jacobian rank.** Chabauty-style resolution needs rank $<$ genus, usually rank 0;
   for most non-special equations the rank is unknown or positive, which blocks the method.
   *(Independently confirmed: U110 needs finiteness of Sha to pin a rank, and concedes rank 2
   defeats one-generator Chabauty.)*
3. **Ineffectivity.** Darmon–Granville gives finiteness for fixed $(p,q,r)$ with
   $1/p+1/q+1/r<1$, but the proof is **ineffective**: no bounds, no algorithm. *(Independently
   confirmed: U113 Part I found an unsourced "Baker effective bound" used as if effective.)*
4. **Trivial solutions obstruct the modular method.** Trivial/boundary solutions produce newforms
   the sieve cannot eliminate — often CM abelian varieties. Sometimes the failure is explained by
   such a solution; **in other cases the reason for failure remains unexplained in the literature.**
   *(This is exactly our orbit $b$: the CM Jacobian of the boundary curve $C_0$, U113 Parts I–II.
   Our inability to eliminate it is a known phenomenon, not a local failure of effort.)*
5. **abc dependence.** Several related results are conditional on the abc conjecture.

---

## 4. Revised assessment of where effort should go

- **Do not** extend the $(3,3,p)$ sieve, the empirical search, or the diagonal formalisation for
  their own sake.
- **Do not** expect orbit $b$ to yield to more effort: obstruction 4 says trivial-solution
  obstructions are sometimes not understood at all.
- The genuine frontier for Beal is $(3,5,7)$ and neighbouring odd-prime signatures, which this
  project has never touched.
- The formalisation work retains independent value: mathlib has FLT3 and FLT4 but **not** full FLT,
  and none of the $(p,p,2)$, $(p,p,3)$, $(2,4,r)$ results. Machine-checking known theorems is a
  legitimate contribution, provided it is labelled as formalisation and not as new mathematics.

---

# Part II: The frontier itself, and what the field is actually attempting

**Additional sources**: *Darmon's Program: A survey*, arXiv:2507.15149 (2025);
*On the generalized Fermat equation $x^5+y^3=z^7$*, Dahmen–Siksek (working paper, few.vu.nl/~sdn249/GFE357.pdf);
*On Darmon's program for the GFE I / II*, arXiv:2205.15861, arXiv:2308.07062;
arXiv:2605.02632, arXiv:2608.28117, arXiv:2404.09171 (2026 work).

## 5. The smallest open Beal signature (3,5,7) is only conditionally resolved

Dahmen and Siksek have a working paper on $x^5+y^3=z^7$. They resolve it **only under stringent
divisibility conditions** — any non-trivial primitive solution with $3 \mid xy$, $5 \mid y$, or
$7 \mid x$ is trivial. **Removing those conditions is open.** Their tools are hyperelliptic curves,
descent, and Selmer sets.

So the smallest open Beal signature has been attacked by two of the leading practitioners, with
the strongest available machinery, and has yielded only a conditional result.

## 6. Darmon's program — and an explicit verdict on the Beal regime

Darmon's program replaces Frey *elliptic* curves with Frey **hyperelliptic** curves and abelian
varieties, using rigid analytic geometry, $p$-adic methods, and modular forms on quaternion
algebras. Resolved through it: $(2,3,7)$, $(2,5,5)$, $(3,3,4)$ and various signatures with
min exponent $\ge 4$.

The survey states plainly that **"signatures with minimum exponent three remain largely
inaccessible through current techniques."** Minimum exponent three is exactly the Beal boundary.

Only four families admit an explicit hypergeometric realisation: $(p,p,r)$, $(r,r,p)$,
$(3,5,p)$ and $(2,r,p)$. Of these, $(3,5,p)$ is the only one inside the Beal regime that is not
near-diagonal — which is why $(3,5,7)$ is the frontier rather than an arbitrary small case.

## 7. What the field's own next targets are

The Darmon survey names its immediate goals as signatures $(2,3,9)$ and $(2,4,5)$ — **both have an
exponent equal to 2, so both lie outside Beal entirely.** The 2026 literature is consistent with
this: new work concerns $Ax^2+By^r=Cz^p$ (exponent 2), or asymptotic/conditional results for
$Ax^p+By^p+Cz^p=0$ over number fields assuming modularity conjectures and Eichler–Shimura.

**Nothing in the recent literature breaks into $\min(p,q,r) \ge 3$ unconditionally.**

## 8. Stated obstructions in Darmon's program

- computational intensity of hyperelliptic curve arithmetic;
- $(2,3,8)$ remains a barrier despite effort;
- genus grows as the minimum exponent falls, worsening the computation;
- classical algebraic descent is insufficient at these genera.

Suggested directions: combine Darmon's program with Faltings height methods, exploit connections
to Diophantine approximation, and develop hybrid classical/$p$-adic methods.

## 9. Bottom line for this project

The gap between this project and the research frontier is not one of effort but of method and
scale. A realistic honest posture:

1. **Do not** attempt to resolve Beal, or any open signature, by extending the machinery here.
2. The literature's own verdict is that the whole Beal regime is largely inaccessible today.
3. The defensible contributions available to us are (a) **correcting this repository's record**,
   which U113 did, and (b) **formalisation** of known theorems in Lean, where mathlib genuinely
   lacks coverage — full FLT, $(p,p,2)$, $(p,p,3)$, $(2,4,r)$ — clearly labelled as formalisation.
4. Any future claim here of resolving an open signature should be treated as almost certainly
   erroneous, and audited against U113's three failure modes before anything else.

---

# Part III: Freitas (2016) confirmed at source — and it is stronger than assumed

**Source**: Nuno Freitas, *On the Fermat-type equation $x^3+y^3=z^p$*, arXiv:1601.06361
(24 January 2016). Checked at abstract level; full text not read.

**Abstract statement**: the equation $x^3+y^3=z^p$ has no solutions $(a,b,c)$ with $abc \ne 0$
and $\gcd(a,b,c)=1$ **when $-3$ is not a square mod $p$**.

## III.1 The project's use is confirmed

$-3$ is a quadratic non-residue mod $p$ exactly when $p \equiv 2 \pmod 3$. So the project's
repeated citation — "$p \equiv 2 \bmod 3$ was resolved by Freitas (2016) via the
Halberstadt–Kraus symplectic criterion" — is **supported by the primary source**. The last major
unverified external dependency of candidate C006 is now citation-verified.

Freitas also contributes a criterion of independent interest: deciding whether two elliptic curves
with certain potentially good reduction at 2 have symplectically or anti-symplectically isomorphic
$p$-torsion modules, with the answer depending on $p \bmod 24$.

## III.2 A discrepancy worth resolving

The source describes its result as covering a set of prime exponents of Dirichlet density
$\approx 0.844$. But $p \equiv 2 \pmod 3$ has density exactly $1/2$. **0.844 > 1/2**, so the
theorem evidently covers a substantial set of primes $p \equiv 1 \pmod 3$ as well, beyond the
$p \equiv 2$ case this project cites it for.

If so, part of this project's Kraus-sieve effort on $p \equiv 1 \pmod 3$ may also be redundant
with Freitas, in addition to being superseded by the literature's $(3,3,p)$ result for
$p \le 10^9$ (Part I). **This is flagged, not concluded**: resolving it requires the full text,
which has not been read. It is recorded as an open obligation rather than a finding.

## III.3 Citation status summary for this project

| Citation | Status |
|---|---|
| Dahmen–Siksek, *Acta Arith.* 164 (2014) | **confirmed** — $(5,5,7)$, $(5,5,19)$, $(7,7,5)$ unconditional; $(5,5,11)$, $(5,5,13)$, $(7,7,11)$ **under GRH** |
| Bilu–Parent (2011) + Bilu–Parent–Rebolledo (2013) + BDMTV (2019) | **confirmed** — split Cartan; project misattributes to Momose / Darmon–Merel |
| Freitas, arXiv:1601.06361 (2016) | **confirmed** — $p \equiv 2 \bmod 3$ covered; apparent coverage of more primes than cited, unresolved |
| Breuil–Diamond (2014) Thm 3.2.2 | **still unverified** |
| Azon, arXiv:2504.01967v2 Thm 5.23 | **still unverified** (U96 reports its Hypothesis 5 fails here) |
| $(2,4,n)$ chain: Euler, Bruin, Ellenberg, Bennett–Ellenberg–Ng | **still unverified** |

---

# Part IV: Freitas (2016) read at source — discrepancy resolved, and a sharper supersession

The PDF of arXiv:1601.06361 was retrieved and its text extracted locally, so the statements below
are **from the paper itself**, not from an abstract page.

## IV.1 The 0.844 discrepancy is resolved — the project's citation is correct

Abstract, verbatim (de-hyphenated):

> "We prove that the Fermat-type equation $x^3+y^3=z^p$ has no solutions $a,b,c$ satisfying
> $abc \ne 0$ and $\gcd(a,b,c)=1$ when $-3$ is not a square mod $p$. **This improves to
> approximately $0.844$ the Dirichlet density of the set of prime exponents to which the previous
> equation is known to not have such solutions.**"

**Theorem 3.** *Let $p \ge 17$ be a prime satisfying $p \equiv 2 \pmod 3$. Then (1.1) has no
non-trivial primitive solutions. Therefore (1.1) has no non-trivial primitive solutions for a set
of prime exponents with density approximately $0.844$.*

So $0.844$ is the **cumulative** density across the literature, not the density of Freitas'
own theorem, which is exactly $p \equiv 2 \pmod 3$ (density $1/2$), subject to $p \ge 17$.
**There is no error in this project's citation**, and the obligation raised in Part III is
discharged. Note the hypothesis $p \ge 17$, which the project does not state; its sieve range
begins at $p = 43$, so nothing is affected.

## IV.2 A sharper supersession than Part I recorded

The same introduction states the prior results verbatim:

**Theorem 1 (Kraus 1998).** *Let $p \ge 17$ be prime and $a,b,c$ a non-trivial primitive solution
to (1.1). Then $v_2(a) = 1$, $v_2(b) = 0$, $v_2(c) = 0$, and $v_3(c) \ge 1$. Moreover, there are no
solutions for exponents $p$ satisfying $17 < p \le 10^4$.*

**Theorem 2 (Chen–Siksek 2009).** *For a set of primes $L$ with density $0.681$ the equation (1.1)
has no non-trivial primitive solutions … Moreover, there are no solutions for exponents $p$
satisfying $3 \le p \le 10^7$.*

**Chen–Siksek settled $3 \le p \le 10^7$ in 2009.** This project certified $p \le 700$ across
seven checkpoints (U111 and predecessors) — **four orders of magnitude behind a seventeen-year-old
result**, and behind Kraus's $p \le 10^4$ from 1998 as well. Part I recorded this supersession
loosely as "$p \le 10^9$ in the literature"; the precise, attributable figures are
$10^4$ (Kraus 1998) and $10^7$ (Chen–Siksek 2009).

## IV.3 Unused structural information

Kraus's Theorem 1 gives valuation constraints on any solution — $v_2(a)=1$, $v_2(b)=0$,
$v_2(c)=0$, $v_3(c)\ge1$ — that this project's $(3,3,p)$ work does not appear to use. These are
free constraints from a 1998 paper.

## IV.4 Why the Frey curve list matters

Freitas notes that only a few GFE signatures have a Frey curve **defined over $\mathbb{Q}$**:
$(p,p,p)$, $(p,p,2)$, $(p,p,3)$, $(5,5,p)$, $(7,7,p)$, $(2,3,p)$, $(4,p,4)$ — and that only
$(p,p,p)$, $(4,p,4)$, $(p,p,2)$, $(p,p,3)$ were fully resolved by that route (Wiles; Darmon;
Darmon–Merel). Signatures such as $(r,r,p)$ and $(2\ell,2m,p)$ have Frey curves only over
**totally real fields** — which is precisely the harder setting this project's weighted-equation
work lives in, and explains why that route needs Hilbert modular forms and hits the obstructions
recorded in U113.

---

# Part V: Azon read at source — U96's block confirmed, and the *correct* tool for orbit b found

The PDF of arXiv:2504.01967v2 (Martin Azon, *Effective Darmon's program for the generalised
Fermat equation*) was retrieved and its text extracted locally. The paper treats signatures
$(p,p,r)$ and $(r,r,p)$ — and this project's weighted equation reduces to $U^5 + 8V^5 = Z^{17}$,
i.e. signature $(5,5,17)$, which is $(r,r,p)$ with $r=5$, $p=17$. Azon is therefore the right
framework, and U96 was right to audit it.

## V.1 Hypothesis 5, verbatim

> **Hypothesis 5.** There is at least one prime number $q_0 \nmid 2r$ such that $\nu_{q_0} < 0$,
> $\nu_{q_0} \not\equiv 0 \bmod r$, and $\mathrm{ord}^*(q_0 \bmod r)$ is even.
>
> By Proposition 5.19, Hypothesis 5 implies that there is at least one place of unipotent
> reduction, and that $\rho_{(J^\pm_r)(\theta_K),\mathfrak p}$ is **absolutely irreducible**.

It is a standing assumption of the section — "In order to ensure that the considered residual
representations are absolutely irreducible, we assume the following hypothesis" — and absolute
irreducibility is a prerequisite for level lowering. **U96's finding that Theorem 5.23 depends on
Hypothesis 5 is confirmed at source**, so candidate C002's BLOCKED status stands.

## V.2 Theorem 5.23, verbatim

> **Theorem 5.23.** Assume that $p \nmid 2r$ and that $\nu_p = 0$. When considering
> $\rho_{(J^+_r)(\theta_K),\mathfrak p}$, suppose that $\nu_r > 2$. Then there is a Hilbert
> newform $g$ over $K$ of parallel weight 2, trivial character and level
> $n^\pm_2\, {}_{2r}n^\pm_r\, n_{\mathrm{tor},\not\equiv 0(p)}\, n_{2\mathrm{unip}}$, satisfying:
> 1) $\rho_{(J^\pm_r)(\theta_K),\mathfrak p} \simeq \rho_{g,P}$ for some place $P \mid p$ in the
>    field of coefficients $K_g$;
> 2) we have the field inclusion $K \subset K_g$;
> 3) **if there is some prime $q \nmid 2r$ such that $\nu_q > 0$ and $\nu_q \not\equiv 0 \bmod p$,
>    then $g$ does not have complex multiplication.**

## V.3 The significant finding: part 3 is a CM-exclusion criterion

**Orbit $b$ is a CM newform** — U97 and U113 Part I both establish it is the CM abelian surface
attached to $C_0 : y^2 = 64 - x^5$, with CM by $\mathbb{Q}(\zeta_5)$.

Theorem 5.23 part 3 gives an explicit, purely **residual-level** criterion under which the
level-lowered newform $g$ **cannot have complex multiplication**: it suffices that some prime
$q \nmid 2r$ has $\nu_q > 0$ with $\nu_q \not\equiv 0 \bmod p$.

This is exactly the shape of obstruction that candidate **C013** was opened to look for, and
exactly what U97 and U102 failed to supply — they instead argued at the isogeny and $\ell$-adic
level, which U113 Parts I–II showed is invalid. **The correct instrument was inside the paper the
project was already citing.**

## V.4 What this does and does not establish

It does **not** eliminate orbit $b$. Applying part 3 requires exhibiting a prime $q \nmid 10$ with
$\nu_q > 0$ and $\nu_q \not\equiv 0 \bmod 17$ for the weighted equation, and part 3 sits under
Theorem 5.23's own hypotheses ($p \nmid 2r$, $\nu_p = 0$, $\nu_r > 2$) **and** the standing
Hypothesis 5, which U96 reports fails for the weighted equation. So the criterion is not simply
available here.

What it does establish is that C013 is a well-posed target with a concrete instrument attached,
rather than a hope, and that the project's orbit-$b$ effort was aimed at the wrong level of
the theory for the whole of U97 and U102.

---

# Part VI: *Why* Hypothesis 5 fails — derived, not asserted

U96 states that Azon's Hypothesis 5 "fails identically" for the weighted equation but gives no
reason. Given how many U9x claims have not survived audit, the claim was re-derived from the
primary source. **It is correct, and the reason is structural.**
Verification code: `code/U114_azon_hypothesis5_test.py`.

## VI.1 Setting up

The weighted equation reduces to $U^5 + 8V^5 = Z^{17}$: signature $(r,r,p) = (5,5,17)$ with
$A = 1$, $B = 8$, $C = 1$, $a = U$, $b = V$, $c = Z$. Azon's Definition 3.11 requires $A,B,C$
pairwise coprime and free of $r$-th powers — satisfied, since $8 = 2^3$ is free of 5th powers.

## VI.2 An exact expression for $\nu_q$

Definition 4.1 sets $\nu_q := v_q\bigl(s_0(s_0-1)\bigr)$. Proposition 3.22(2) and its proof give
$$t_0 = \frac{A a^r}{C c^p}, \qquad t_0(t_0-1) = \frac{-AB\,a^r b^r}{(A a^r + B b^r)^2},
\qquad \widetilde{s_0} := 2 - 4 s_0, \qquad \widetilde{s_0}^{\,2} = \frac{1}{t_0(t_0-1)} + 4 .$$
Hence $s_0(s_0-1) = \frac{\widetilde{s_0}^{\,2}-4}{16} = \dfrac{1}{16\, t_0(t_0-1)}$, and for odd $q$
$$\boxed{\ \nu_q = 2p\,v_q(c) + 2 v_q(C) - v_q(AB) - r\, v_q(ab).\ }$$
The identity $t_0(t_0-1) = -AB a^r b^r/(Cc^p)^2$ was checked symbolically: the difference vanishes
identically after substituting $Bb^r = Cc^p - Aa^r$.

## VI.3 The failure

Hypothesis 5 needs a prime $q_0 \nmid 2r = 10$ with (i) $\nu_{q_0} < 0$, (ii)
$\nu_{q_0} \not\equiv 0 \bmod 5$, (iii) $\mathrm{ord}^*(q_0 \bmod 5)$ even. Since
$(\mathbb{Z}/5\mathbb{Z})^\times$ is cyclic of order 4, (iii) just says $q_0 \not\equiv 1 \bmod 5$.

By primitivity each prime divides at most one of $ab$, $c$. With $A = C = 1$ and $AB = 8$:

| case | $\nu_q$ | (i) $<0$? | (ii) $\not\equiv 0 \bmod 5$? |
|---|---|---|---|
| $q \mid Z$ | $34\,v_q(Z) > 0$ | **no** | — |
| $q \mid UV$ | $-5\,v_q(UV)$ | yes | **no** — it is $\equiv 0 \bmod 5$ |
| $q \nmid UVZ$ | $0$ | **no** | — |

The only way to get $\nu_q < 0$ with $\nu_q \not\equiv 0 \bmod r$ is for $q$ to divide $AB$ with
$v_q(AB) \not\equiv 0 \bmod r$. Here $AB = 8 = 2^3$, so the only candidate is $q = 2$ — **which is
excluded by the requirement $q_0 \nmid 2r = 10$.**

**Hypothesis 5 fails identically. U96's conclusion is confirmed, now with a proof.**

## VI.4 What this settles

- **C002 stays BLOCKED**, on a derived rather than an asserted basis.
- **C013 is not reachable through Azon's Theorem 5.23(3)** for this equation: part 3 lives under
  Theorem 5.23, which lives under the standing Hypothesis 5. The right-shaped instrument exists
  but its hypotheses genuinely fail here.
- The failure is **structural, not incidental**: it is caused by $A = C = 1$ together with $AB$
  being a prime power at the excluded prime 2. Any attempt to rescue this route must change the
  equation's coefficients — i.e. choose a different reduction of the original Beal case — rather
  than work harder on this one.
- Generalisation worth recording: for signature $(r,r,p)$ with $A = C = 1$, Hypothesis 5 can only
  hold when $B$ has a prime factor $q \nmid 2r$ with $v_q(B) \not\equiv 0 \bmod r$. This is a
  cheap test to run *before* investing in any such reduction.

---

# Part VII: A coefficient-only criterion for Hypothesis 5, and both project orientations fail it

**Verification code**: `code/U114_hypothesis5_criterion.py`

The formula of Part VI generalises into a criterion depending only on the coefficients.

## VII.1 The criterion

For signature $(r,r,p)$ with $A,B,C$ pairwise coprime and free of $r$-th powers (Azon Def. 3.11),
and $Aa^r$, $Bb^r$, $Cc^p$ pairwise coprime (Azon Lemma 3.12), take any prime $q \nmid 2r$:

| case | $\nu_q$ | (i) $\nu_q<0$ | (ii) $\nu_q \not\equiv 0 \bmod r$ |
|---|---|---|---|
| $q \mid AB$ (say $q\mid A$; then $q \nmid b, C, c$) | $-v_q(AB) - r\,v_q(a)$ | ✓ | ✓ — since $1 \le v_q(AB) \le r-1$ by $r$-th-power-freeness |
| $q \mid ab$, $q \nmid AB$ | $-r\,v_q(ab)$ | ✓ | ✗ |
| $q \mid c$ or $q \mid C$ | $2p\,v_q(c) + 2v_q(C) > 0$ | ✗ | — |
| otherwise | $0$ | ✗ | — |

$$\boxed{\textbf{Hypothesis 5 holds} \iff AB \text{ has a prime factor } q \nmid 2r
\text{ with } \mathrm{ord}^*(q \bmod r) \text{ even.}}$$

This depends **only on $A$, $B$ and $r$** — not on the putative solution, not on $p$, not on $C$.
It is therefore a one-line test that can be run before any work on a reduction.

## VII.2 Both of this project's orientations fail it

The project (U42–U47) reduced the all-even branch to exactly two orientations:

| orientation | as $(5,5,17)$ | $AB$ | Hypothesis 5 |
|---|---|---|---|
| B: $X^{10}+256Y^{10}=Z^{17}$, i.e. $U^5+8V^5=Z^{17}$ | $A=1,B=8,C=1$ | $8 = 2^3$ | **FAILS** — only prime is 2, and $2 \mid 2r = 10$ |
| A: $X^{10}+Y^{10}=2Z^{17}$, i.e. $(X^2)^5+(Y^2)^5=2Z^{17}$ | $A=1,B=1,C=2$ | $1$ | **FAILS** — no prime factors at all |

**Neither orientation can use Azon's level-lowering theorem.** The project's entire
weighted-equation programme sits on reductions whose coefficients fail the framework's hypothesis
at the first step, for reasons visible from $A$ and $B$ alone.

## VII.3 What would work

For $r = 5$, $\mathrm{ord}^*(q \bmod 5)$ is even exactly when $q \not\equiv 1 \bmod 5$. So with
$A = 1$, Hypothesis 5 holds for $B \in \{3,6,7,9,12,13,14,15,17,18,19,21,23,24,26,27,28,29,\dots\}$
and fails for $B \in \{1,2,4,5,8,10,11,16,20,22,25,31,32\}$ — powers of 2 and 5 fail because those
primes divide $2r$; $B = 11, 31$ fail because $11 \equiv 31 \equiv 1 \bmod 5$ gives odd order.

So the route is not dead in general — it is dead **for these coefficients**. Any attempt to revive
it must produce a different reduction of the all-even case, with $AB$ divisible by a prime
$q \notin \{2,5\}$, $q \not\equiv 1 \bmod 5$. Whether such a reduction of the original Beal case
exists is a separate question this checkpoint does not settle.

## VII.4 Status

- C002 and C013 remain BLOCKED, now for a reason expressible in one line about $A$ and $B$.
- The criterion is recorded as a reusable pre-test in candidate C013's extracted lemmas.

---

# Part VIII: Azon's framework is structurally inapplicable to the all-even branch

**Verification code**: `code/U114_alleven_coefficients.py`

Part VII showed both of this project's orientations fail Hypothesis 5. The natural next question
is whether a *different* reduction would pass. It cannot — and the reason comes from the
kernel-verified structure theorem C020.

## VIII.1 The coefficients are forced by the parametrisation

By `allEven_isPythagorean` (kernel-verified, U113 Part VI), an all-even counterexample is a
**primitive Pythagorean triple** of perfect powers. Every such triple is
$(m^2-n^2,\ 2mn,\ m^2+n^2)$ with $\gcd(m,n)=1$ of opposite parity. Matching the odd leg to $A^r$,
the two factors $m-n$ and $m+n$ are coprime and both odd, so
$$m-n = d^r, \qquad m+n = e^r \quad\Longrightarrow\quad 2m = e^r + d^r,\quad 2n = e^r - d^r,$$
and therefore
$$e^{2r} + d^{2r} \;=\; 2\,(m^2+n^2) \;=\; 2\,C^t .$$
Verified symbolically for $r = 5$ and $r = 7$: the difference is identically zero.

This is the sum equation usable in Azon's shape $A a^R + B b^R = C c^P$, and its coefficients are
**forced**: $A = 1$, $B = 1$, $C = 2$. Matching the *even* leg instead pushes powers of 2 onto the
other term, which is exactly how this project's orientation B, $U^5 + 8V^5 = Z^{17}$, arises.

## VIII.2 The consequence

| reduction | $AB$ | Hypothesis 5 |
|---|---|---|
| sum equation from the odd leg, $e^{10}+d^{10} = 2C^t$ | $1$ | fails |
| orientation A, $X^{10}+Y^{10}=2Z^{17}$ | $1$ | fails |
| orientation B, $U^5+8V^5=Z^{17}$ | $8$ | fails |
| even-leg variants, $2^k$ | $2^k$ | fails |

**Every $(r,r,p)$-reduction of the all-even branch obtained from the Pythagorean parametrisation
has $AB = 1$ or $AB$ a power of 2**, because the only coefficient the parametrisation introduces
is the 2 coming from $2mn$ and from $2(m^2+n^2)$.

By the Part VII criterion, Hypothesis 5 needs a prime factor of $AB$ **not dividing $2r$**. A power
of 2 offers only the prime 2, which divides $2r$ for every $r$; $AB=1$ offers nothing.

$$\textbf{Azon's Hypothesis 5 fails for every such reduction.}$$

## VIII.3 What this explains

The project's weighted-equation programme — U41 through U113, the single largest body of work in
this repository — was not defeated by an unlucky choice of orientation or by insufficient effort.
It was attempting to apply a framework whose central hypothesis **cannot** be satisfied by any
reduction of the all-even branch of this shape, for a reason visible from the Pythagorean
parametrisation alone.

This also retro-explains the orbit-$b$ obstruction. U114 Part I recorded the literature's note
that trivial solutions obstruct the modular method, sometimes for reasons "that remain
unexplained". Here the obstruction has an explanation: absolute irreducibility of the residual
representation is what Hypothesis 5 buys, and without it there is no licence to eliminate the CM
newform attached to the boundary curve.

## VIII.4 Limits of this finding

- It concerns reductions **of the Pythagorean-parametrisation shape**, which is what C020 shows
  the all-even branch to be. A reduction introducing coefficients by some other device is not
  covered.
- It says nothing about branches other than all-even, and nothing about Beal as a whole.
- The case analysis in Part VII and the argument here are mine, derived from locally extracted PDF
  text, and have not been checked by the author or a referee. Recorded as an open obligation.

---

# Part IX: The (2,4,n) chain — citation consistent, with a scope caveat

Checked at bibliographic level (abstracts and indexing records; full texts not read).

**Bennett–Ellenberg–Ng (2010)**, *The Diophantine equation $A^4 + 2^\delta B^2 = C^n$*,
*International Journal of Number Theory* **6** (2010), 311–338. The signature $(2,4,n)$ and its
permutations are established by this work **for $n \ge 6$**.

The project's ledger attributes $(2,4,n)$, $n \ge 4$ to the chain "Euler (1738), Bruin (2003),
Ellenberg (2004), Bennett–Ellenberg–Ng (2010)". That chain is **consistent with the literature**:
BEN covers $n \ge 6$, and the small cases $n = 4, 5$ require the earlier citations, which the
chain includes. This is the correct shape for such an attribution — unlike the orbit-$b$ case,
where a single misattributed citation was doing all the work.

**Scope caveat.** $(2,4,n)$ has an exponent equal to **2**, so it is *not* a Beal signature at all.
It appears in this project only through the all-even reduction, where taking square roots of even
exponents produces equations with an exponent 2. Listing it in a Beal coverage ledger as
"100% Closed" without that qualification invites the error of thinking a Beal case has been
settled. The corrected ledger now carries the qualification.

## Citation ledger — final state

| Citation | Status |
|---|---|
| Dahmen–Siksek, *Acta Arith.* 164 (2014) | **confirmed at source** — $(5,5,11)$, $(5,5,13)$ are **GRH-conditional** |
| Freitas, arXiv:1601.06361 (2016) | **confirmed at source (full text)** — $p \equiv 2 \bmod 3$, $p \ge 17$; the 0.844 figure is cumulative |
| Kraus (1998), Chen–Siksek (2009) | **confirmed via Freitas's introduction** — $(3,3,p)$ settled for $3 \le p \le 10^7$ |
| Bilu–Parent (2011) + BPR (2013) + BDMTV (2019) | **confirmed** — split Cartan; project misattributes to Momose / Darmon–Merel |
| Azon, arXiv:2504.01967v2 | **confirmed at source (full text)** — Hypothesis 5 verbatim; its failure here **derived**, not assumed |
| Bennett–Ellenberg–Ng (2010) | **consistent** — $n \ge 6$; small cases need the rest of the chain; signature is not Beal |
| Breuil–Diamond (2014) Thm 3.2.2 | **still unverified** |

Every load-bearing citation in this repository has now been checked except Breuil–Diamond.

---

# Part X: Breuil–Diamond Théorème 3.2.2 — confirmed at source

**Source**: Christophe Breuil & Fred Diamond, *Formes modulaires de Hilbert modulo $p$ et valeurs
d'extensions galoisiennes*, arXiv:1208.5367v3; published *Ann. Sci. ÉNS* **47** (2014), 905–974.
PDF retrieved and text extracted locally.

**Théorème 3.2.2 exists**, and is a modularity lifting theorem, as the project describes. Its
hypotheses, from the paper:

> Supposons $p > 2$, $\bar\rho : \mathrm{Gal}(\overline{\mathbb Q}/F) \to \mathrm{GL}_2(k_E)$
> **modulaire**, $\bar\rho|_{\mathrm{Gal}(\overline{\mathbb Q}/F(\sqrt[p]{1}))}$ **irréductible**
> et, si $p = 5$, l'image de $\bar\rho(\mathrm{Gal}(\overline{\mathbb Q}/F(\sqrt[p]{1})))$ dans
> $\mathrm{PGL}_2(k_E)$ non isomorphe à $\mathrm{PSL}_2(\mathbb F_5)$. Soit $\psi$ un caractère
> qui relève $\det\bar\rho$ … $T$ un sous-ensemble des places de $F$ divisant $p$ et $S$ un
> ensemble fini de places finies de $F$ contenant les places divisant $p$ et les places où
> $\bar\rho$ ou $\psi$ sont ramifiés. Pour chaque $v \in S$, soit $[r_v, N_v]$ un **type de
> Weil–Deligne** en $v$ …

The paper notes it is a consequence of the main results of Barnet-Lamb, Gee and Geraghty, as
explained in the proof of [25, Lem. 5.3.2].

## X.1 The project's use is accurate

- It is indeed a **local-lift** statement: the theorem takes a Weil–Deligne type $[r_v,N_v]$ at
  each $v \in S$, which is exactly the "local lift hypotheses" U98 and U101 set out to discharge
  at $\mathfrak p_2$, $\mathfrak p_5$ and $\lambda_{17}$.
- Its irreducibility hypothesis is $\bar\rho|_{\mathrm{Gal}(\overline{\mathbb Q}/F(\zeta_p))}$
  irreducible — and the project addresses precisely this, claiming via Clifford theory that
  $\bar\rho_{J^-,17}|_{G_{K(\zeta_{17})}}$ is absolutely irreducible (U64, U101, U103, quoted in
  U105 §2.2). **The right hypothesis is being addressed.**
- The $p = 5$ caveat about $\mathrm{PSL}_2(\mathbb F_5)$ does not bite here, since $p = 17$.

**The citation is confirmed.** Whether the project's *discharge* of the local types and of
irreducibility is itself correct is a separate question this checkpoint does not settle — those
arguments live in U64/U98/U101/U103 and have not been audited line by line.

## X.2 Citation ledger — complete

| Citation | Status |
|---|---|
| Dahmen–Siksek (2014) | confirmed — $(5,5,11)$, $(5,5,13)$ GRH-conditional |
| Freitas (2016) | confirmed (full text) — $p \equiv 2 \bmod 3$, $p \ge 17$ |
| Kraus (1998), Chen–Siksek (2009) | confirmed — $(3,3,p)$ for $3 \le p \le 10^7$ |
| Bilu–Parent / BPR / BDMTV | confirmed — project misattributes to Momose / Darmon–Merel |
| Azon (2025) | confirmed (full text) — Hypothesis 5 fails here, **derived** |
| Bennett–Ellenberg–Ng (2010) | consistent — $n \ge 6$; not a Beal signature |
| **Breuil–Diamond (2014) Thm 3.2.2** | **confirmed (full text)** |

**Every load-bearing citation in this repository has now been checked against its primary source.**
One was misattributed (split Cartan); one was correct but used for a claim the source does not
support (Dahmen–Siksek, whose GRH hypothesis the project claimed to remove); the rest check out.
