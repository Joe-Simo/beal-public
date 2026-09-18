# U113: Corrected Coverage Ledger (post-audit, 2026-09-17)

Supersedes the coverage ledgers in U105 §4 and related checkpoints, which record as
"100% Closed" several families whose supporting arguments did not survive audit
([U113 audit](U113_orbit_b_elimination_audit.md)).

**Beal's conjecture is not solved.** Nothing below claims otherwise.

## Legend

- **PROVED (ours, verified)** — established here and independently re-verified by exact computation.
- **CITED, UNVERIFIED** — rests on an external theorem not yet checked against its primary source.
- **CONDITIONAL** — depends on an unproved hypothesis (GRH, finiteness of Sha, Cohen–Lenstra).
- **OPEN** — not established.
- **WITHDRAWN** — previously recorded as closed; the supporting argument failed audit.

## Ledger

| Family / claim | Previously recorded | Post-audit status | Basis |
|---|---|---|---|
| Counterexample checker (all six conditions, exact) | validated | **PROVED (ours, verified)** | Independent re-implementation agrees on every required vector *and* on the discriminating reason; True-branch reachability proven by mutating only the exponent gate; exact at 121 digits |
| No counterexample with $A,B \le 160{,}000$, $x,y,z \in \{3,\dots,19\}$ prime | 100% closed | **PROVED (ours), low leverage** | Exhaustive GMP search; bounds where a counterexample can live, proves nothing about the conjecture |
| $\operatorname{disc}(f) = 2^{24}5^5Z^{68}$; good reduction at $q \mid Y$ | — | **PROVED (ours, verified)** | Symbolic + 5 exact specialisations (U113 Part I) |
| Orbit $b \sim \operatorname{Jac}(C_0)_{/K}$ | proved | **PROVED (ours, verified)** | Point counting: $(S,P) = (9,19), (-11,29), (-1,-151)$ at $q=11,31,41$; $a_{\mathfrak q}=0$ for $q\not\equiv1\bmod5$ |
| Orbit $b$ **eliminated** (U97, U102) | "definitive, unconditional" | **WITHDRAWN** | All three U97 strategies and all four U102 arguments fail; Strategy 3 refuted by computation (U113 Parts I–II) |
| $X^{10}+256Y^{10}=Z^{17}$ (Orientation B) | closed by two pathways | **WITHDRAWN → OPEN** | Pathway 1 = the withdrawn orbit-$b$ argument; Pathway 2 bounds $C^-(k)$ while solutions give points of degree 10 over $k$ (U113 Part III) |
| All-even branch, $17 \mid t$ | 100% closed | **WITHDRAWN → OPEN** | Depends entirely on Orientation B; additionally states $r,s\ge5$ while the ledger drops that hypothesis |
| All-even branch, $x$ or $y \in \{4,6,8\}$ | implicitly closed | **OPEN** | Never covered by U105 Thm 1.1 ($r,s \ge 5$); no reduction proved |
| $x^5+y^5=z^{11}$, $x^5+y^5=z^{13}$ | "100% unconditionally resolved" | **CONDITIONAL (GRH)** — *source confirmed* | Dahmen–Siksek prove these **assuming GRH** (Acta Arith. 164 (2014) 65–100, confirmed at source). The claimed removal uses GRH-conditional Bach bounds + Cohen–Martinet heuristics — circular (U113 Parts IV, VI) |
| $\operatorname{rank}J^-(k) \le 2 < g=8$ (U99) | unconditional | **CONDITIONAL (GRH + Cohen–Martinet)**, and over the wrong field | $h(F)=1$ not certified: Minkowski bound $5.67\times10^{19}$, `bnfcertify` fails (U113 Parts III–IV) |
| $(5,5,p)$, $p=17$ | partially resolved | **CONDITIONAL (finiteness of Sha)** | Cassels–Tate parity step assumes Sha finite; U110 concedes rank 2 defeats one-generator Chabauty |
| $(3,3,p)$, $p \le 700$, $p \equiv 1 \bmod 3$ | 100% eliminated | **CITATION-VERIFIED**, sieve data sound | 0 Hasse violations, 0 inconsistencies over 88 repeated traces. 144b1 is handled outside the sieve by a split-Cartan argument; the supporting theorem is real (Bilu–Parent 2011 + BPR 2013; $p=13$ by BDMTV 2019) and its hypotheses hold for all 44 exponents. Project misattributes it to Momose/Darmon–Merel (U113 Parts V–VI) |
| $(3,3,p)$, $p \equiv 2 \bmod 3$ | closed (Freitas 2016) | **CITED, UNVERIFIED** | Not checked against primary source |
| $(3,3,p)$, **all** $p$ | — | **OPEN** | No uniformity in $p$; the sieve is per-prime |
| $(2,4,n)$, $n \ge 4$ | 100% closed | **CITED, UNVERIFIED** | Euler/Bruin/Ellenberg/Bennett–Ellenberg–Ng not checked against primary sources |
| $(10,10,19)$ | 100% closed | **CITATION-VERIFIED** | $(5,5,19)$ is one of Dahmen–Siksek's **unconditional** cases (confirmed at source). U105 Thm 1.2 step 5 ("positivity forces $A=B=1$") is still a non sequitur, though the conclusion survives |
| Mixed-signature part of Beal | — | **OPEN**, no mechanism in the pool | The bulk of the conjecture |

## Formal verification

| Claim | Post-audit status | Basis |
|---|---|---|
| **Exponent reduction**: a counterexample implies one with all exponents in $\{4\} \cup \{\text{odd primes}\}$ | — | **PROVED (Lean-kernel verified)** — `#print axioms` reports only `[propext, Classical.choice, Quot.sound]`; no `sorry`, no custom axioms |
| **All signatures with $4 \mid x$, $4 \mid y$, $z$ even** (non-diagonal; subsumes diagonal $(n,n,n)$, $4\mid n$) | Signature4.lean: `sorry` | **PROVED (Lean-kernel verified), unconditional** — via mathlib `not_fermat_42` / `fermatLastTheoremFour`; standard axioms only; no coprimality needed |
| **Pairwise coprimality of the bases**; **no counterexample with $A = B$** | used tacitly, never proved | **PROVED (Lean-kernel verified)** — standard axioms only (U113 Part III) |
| **All signatures with $3 \mid x$, $3 \mid y$, $3 \mid z$** (non-diagonal; includes the Fermat cubic $(3,3,3)$) | `flt_3` axiom | **PROVED (Lean-kernel verified), unconditional** — via mathlib `fermatLastTheoremThree` (`FLT/Three.lean:757`); standard axioms only. *Correction: an earlier entry here wrongly said mathlib lacks FLT3.* |

| Claim | Post-audit status | Basis |
|---|---|---|
| "(2,3,8) Lean 4 formalized", "Lean 4 + mathlib verification" | **NOT VERIFIED** | No `lake`/`lean`/`elan` on this machine; **no file in `formal/` has ever been compiled**. 7 `sorry`s and 9 custom `axiom`s, 5 of which assert the substantive theorems. Countersearch over 227,994 pairs found no inconsistency witness, so the axiom set is not shown unsound — but it is unverified trust, not proof (U113 Part VII) |

## Standing obligations

1. Two primary sources have now been checked (U113 Part VI): Dahmen–Siksek (2014) and the
   split-Cartan chain Bilu–Parent (2011) + BPR (2013) + BDMTV (2019). Both confirmed, both
   against abstracts and bibliographic records rather than full text. Still unchecked and
   load-bearing: **Freitas (2016)** for $(3,3,p)$ with $p \equiv 2 \bmod 3$; the $(2,4,n)$
   chain (Euler, Bruin, Ellenberg, Bennett–Ellenberg–Ng); Breuil–Diamond (2014) Thm 3.2.2;
   Azon (arXiv:2504.01967v2) Thm 5.23.
2. Every Chabauty/rank claim must state the field its points are rational over, after the
   Part III failure mode.
3. No result may be relabelled unconditional on the strength of a heuristic or a GRH-conditional
   bound (Part IV).

## Obstruction results (U115–U117)

| result | status |
|---|---|
| **Beal is FALSE over `ℤ[i]`** — so no proof can rest on unique factorisation alone | **PROVED (Lean-kernel verified)**, `[propext]` alone |
| **abc gives finiteness only, ineffectively** — cannot resolve Beal, nor can IUT | literature-verified (U115) |
| **Azon's Hypothesis 5 fails for every reduction of the all-even branch** by either route | derived here, exact computation (U114 VI–VIII, U116) |
| min exponent 3 "largely inaccessible through current techniques" | Darmon-program survey (U114 II) |
| Beal ⟺ "2 is an obligatory exponent" in the hyperbolic regime | **PROVED (Lean-kernel verified)** for the ten known solutions (U117) |

## Relation to the literature (U114)

Every family verified above is a **special case of a known theorem** — $(p,p,p)$ for all $p\ge3$ is
Wiles–Taylor; $(p,p,2)$ for $p\ge5$ is Darmon–Merel. These are **formalisation** contributions,
valuable because mathlib lacks full FLT, $(p,p,2)$, $(p,p,3)$ and $(2,4,r)$ — never new mathematics.

## What is genuinely established by this project

An exact verified counterexample checker; an exhaustive search to $1.6\times10^5$ with zero
counterexamples; a verified discriminant identity; a verified identification of orbit $b$; a
sound and internally consistent body of Kraus sieve data for 44 exponents; and a large amount of
correctly executed machinery whose *conclusions* were overstated. The conjecture itself, and every
infinite family bearing on it, remains open.

## Addendum (Part VI): a warning about the non-split Cartan case

The **non-split** Cartan case of Serre's uniformity problem is **open in general**. Any future
route running a Cartan-image argument at primes where the relevant Cartan is non-split — for
$\mathbb{Q}(\sqrt{-3})$ that means $p \equiv 2 \bmod 3$ — will meet an open problem rather than a
citable theorem. The $(3,3,p)$ route escapes this only because those primes are handled by a
different mechanism (Freitas 2016), which remains unverified.
