# U115: Alternative approaches to Beal — abc, IUT, and what they would and would not give

**Why this checkpoint exists**: U114 surveyed the *modular-method* literature. It did not survey
alternative theories. This does. Checked at abstract/encyclopaedic level; full texts not read.

---

## 1. The abc conjecture does NOT prove Beal

This is the single most important correction in this checkpoint, and it cuts against a common
informal claim.

- The abc conjecture implies the **Fermat–Catalan conjecture**: the set of solutions to
  $x^p+y^q=z^r$ with $1/p+1/q+1/r<1$ is **finite**.
- For Beal, that means: **abc implies at most finitely many counterexamples to Beal.**
  It does **not** imply there are none.

Beal asserts there are **zero** primitive solutions with $\min(x,y,z)\ge3$. Finiteness is strictly
weaker. Worse, the finiteness is **ineffective** — the same ineffectivity U114 §3 recorded for
Darmon–Granville — so it does not even reduce Beal to a finite, checkable list.

**Consequence for this project**: a proof of abc would not settle Beal. Any future route here that
routes through abc should be recorded as giving finiteness only, never resolution. Some secondary
sources state loosely that abc "would imply the Beal conjecture"; the careful statement is the
finiteness one, and the two must not be conflated.

## 2. Inter-universal Teichmüller theory (Mochizuki) — contested, and formalisation is ongoing

Status as of 2026:

- Mochizuki maintains a report on the situation surrounding IUT (October 2026). Kirti Joshi
  argues the abc conjecture "stands established" by the methods of Mochizuki's papers together
  with his own, and that the Scholze–Stix objections are dismantled (arXiv:2505.10568).
- **Project LANA** (announced March 2026; ZEN University, Utrecht, Alberta) is formalising
  anabelian geometry and attempting to verify IUT **in Lean**. Its interim report states that the
  argument from **Theorem 3.11 to Corollary 3.12 is "unformalizable" as written**, and the project
  explicitly **suspends judgment** on whether IUT proves abc, while not excluding a gap.

**Consequence for this project**: the status of abc is contested and unresolved. And even on the
most favourable outcome, §1 applies — abc gives finiteness, not resolution. So IUT is not a route
to Beal from here under any scenario.

There is a second-order point worth noting: the leading effort to settle a major Diophantine
conjecture is now itself a **Lean formalisation project**, and its central finding so far is that a
key step is *unformalizable as written*. That is the same category of finding this audit reached
about this repository's own arguments, at a vastly greater scale.

## 3. Terminology

Beal's conjecture is also the **Tijdeman–Zagier conjecture** (R. Tijdeman and D. Zagier). Searching
the literature under only one name will miss results. The **Fermat–Catalan conjecture**
(Darmon–Granville) is the finiteness statement, a strictly weaker relative.

## 4. What this closes off

| route | verdict |
|---|---|
| abc conjecture | gives **finiteness only**, and ineffectively — cannot resolve Beal |
| IUT / Mochizuki | contested; formalisation suspended on an unformalizable step; and §1 applies regardless |
| Darmon's program | min exponent 3 "largely inaccessible" (U114 Part II) |
| modular method on the all-even branch | structurally blocked (U114 Parts VI–VIII) |

Every major route this project could plausibly reach is now documented as either closed, blocked,
or insufficient-in-principle. That is a negative result, and it is worth having explicitly.

---

## 5. Elementary approaches: none valid, and the failure mode is one this project already names

No valid elementary proof of Beal exists. Claimed elementary proofs circulate (preprints.org,
ResearchGate, arXiv preprints such as "A Constructive Proof of Beal's Conjecture" and "Proof of the
Tijdeman–Zagier Conjecture via Slope Irrationality and Term Coprimality); none has passed peer
review or been accepted by the community.

A documented failure mode in that literature: **multiplying the equation through by a common factor
in a way that "does not comply with laws of exponents."** That is precisely item 5 of this
project's own target discipline — *"divide bases by a common factor without checking the effect of
unequal exponents"*. The discipline list is, in effect, a catalogue of how elementary attempts die,
and it is worth keeping for exactly that reason.

## 6. Computational verification — a stronger bound than this project's

The literature reports verification of the Tijdeman–Zagier (Beal) conjecture for
**$\min(n,m,k) \le 113$**, and searches over bases reportedly to **$2^{100}$**.

Compare this project: an exhaustive base search to $1.6\times10^5$ with exponents in
$\{3,\dots,19\}$, and $(3,3,p)$ certified to $p \le 700$. Both are far behind. As U114 Part IV
already established for $(3,3,p)$ — where Chen–Siksek reached $p \le 10^7$ in 2009 — **extending
this project's computations is not research, it is re-derivation of weaker results.**

## 7. Closing summary of routes

| route | verdict | source |
|---|---|---|
| modular method, all-even branch | structurally blocked: Azon Hypothesis 5 cannot hold for any Pythagorean-shape reduction | U114 VI–VIII (derived here) |
| Darmon's program | min exponent 3 "largely inaccessible through current techniques" | U114 II |
| abc conjecture | **finiteness only, ineffective** — cannot resolve Beal | U115 §1 |
| inter-universal Teichmüller theory | contested; Lean formalisation suspended on an unformalizable step; and §1 applies regardless | U115 §2 |
| elementary arguments | no valid proof; failure mode is the project's own discipline item 5 | U115 §5 |
| extending computation | far behind the literature ($\min \le 113$; bases to $2^{100}$; $(3,3,p)$ to $10^7$) | U115 §6, U114 IV |

**Every route reachable from this project is documented as closed, blocked, insufficient in
principle, or already superseded.** That is a negative result, and stating it plainly is more
useful than continuing to generate increments that imply otherwise.

---

## 8. Prize status verified (2026-09-17)

An outstanding obligation from the project brief: verify the current official problem and prize
status. Checked via search results and AMS-indexed pages; the AMS rules page itself returned
**HTTP 403** to automated fetching, so this is at search/secondary level, not a direct read.

| item | finding |
|---|---|
| amount | **US $1,000,000**, donated to the AMS by D. Andrew Beal |
| custodian | held by the **American Mathematical Society** until awarded |
| announced | *Notices of the AMS*, December 1997 |
| what wins it | **either** a proof **or** a counterexample |
| publication requirement | must be **published in a refereed and respected mathematics publication** |
| waiting period | **two years** after publication before the Beal Prize Committee decides whether the solution merits detailed evaluation |
| verification | AMS and BPC then choose **two outside experts** to verify |
| awarded to date | **never** — the prize remains unawarded |

### Consequences for this project

1. **Four milestones are distinct and must never be conflated**: (a) a mathematical resolution,
   (b) publication in a refereed venue, (c) two-year waiting period plus expert verification,
   (d) the award itself. This project's status headings already separate solved / verified /
   awarded; this confirms the separation is the right one and matches the actual procedure.
2. The prize requires **refereed publication** — not a preprint, not a repository, not a
   machine-checked file. Formal verification in Lean would be strong supporting evidence but does
   not substitute for the published, refereed article the rules name.
3. Nothing in this project approaches the threshold, and no submission is contemplated. The brief
   requires explicit approval before any external contact or prize claim; none is sought.
