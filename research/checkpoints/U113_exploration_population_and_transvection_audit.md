# Checkpoint U113: Exploration Population Initialization and Refutation of the Universal Transvection Route

**Date:** 2026-09-17  
**Status:** Verified correction to one research route; Beal's conjecture remains unresolved.  
**Base inspected:** `82d81be1b5d5c28b0964857e0855d3b802bb4cd8`  
**Population:** `research/exploration/population.json`

## 1. Exact target

For positive integers (A,B,C,x,y,z) with (x,y,zge 3) and
[
A^x+B^y=C^z,
]
prove (gcd(A,B,C)>1), or exhibit an exact primitive counterexample.

Nothing in this checkpoint proves or disproves the full conjecture.

## 2. Route audited

Recent U110-U111 artifacts claimed a universal mechanism:

1. choose a solution-variable prime (q) of multiplicative reduction for a Frey curve;
2. assert that inertia on (E[p]) contains a transvection of order (p);
3. use the fact that Cartan normalizers have order prime to (p);
4. conclude that Cartan images are impossible, then combine this with Borel/exceptional-image exclusions to claim universal surjectivity.

The group-order implication in step 3 is correct **if** an order-(p) transvection is actually present. The universal passage from step 1 to step 2 is false as stated.

## 3. Decisive local criterion

The Tate-curve argument requires the valuation condition on the **minimal discriminant**. A convenient checked source is:

Pierre Charollois, “Generalized Fermat equations (d'après Halberstadt–Kraus),” in *Clay Mathematics Proceedings* **8** (2009), pp. 92–94, available at  
https://www.claymath.org/library/proceedings/cmip08c.pdf

At Proposition 3.1 the hypothesis is explicitly that (p
mid v_q(Delta)). In the Tate-curve proof, if (e=v_q(Delta)), the (p)-division representation over the maximal unramified local extension is trivial exactly when (pmid e). Thus the order-(p) unipotent element used by the U110-U111 route is not available merely from multiplicative reduction.

## 4. Direct contradiction with the U110-U111 use

For the repository's displayed signature-((2,3,p)) Frey model,
[
Delta=-1728,C^p.
]

At any prime (qmid C) with (q
otin{2,3}),
[
v_q(Delta)=p,v_q(C),
]
so
[
pmid v_q(Delta).
]

Therefore the exact primes used in the claimed “solution-variable transvection” argument do **not** satisfy the local hypothesis needed to force the order-(p) transvection.

A separate Wolfram exact-arithmetic check evaluated
[
v_q!left(-1728(q^2)^pight)
]
for (pin{5,7,11,17}) and (qin{5,7,11,13}). Every result was (2p), hence (0mod p). This is only a sanity check; the symbolic valuation identity above is the proof of the arithmetic point.

## 5. Consequence

The following claims are **not established** by the U110-U111 transvection argument:

- “Cartan normalizers are eliminated for every Beal Frey curve.”
- “Every Beal Frey representation is surjective for all sufficiently large prime exponents.”
- Any downstream result whose only irreducibility/surjectivity input is that universal transvection assertion.

This correction does **not** invalidate signature-specific irreducibility or modularity theorems proved by other arguments. Those must be checked individually from their actual sources.

## 6. Reusable obstruction extracted from the failure

A corrected local lemma has the form:

> Let (E/K) have multiplicative reduction at a prime (q
mid p), and let (Delta_{min}) be its minimal discriminant. If (p
mid v_q(Delta_{min})), then the Tate-curve inertia image on (E[p]) contains a nontrivial unipotent element of order (p); consequently the image cannot lie in a split or non-split Cartan normalizer.

Future uses must verify all of:
1. the model is minimal or (v_q(Delta_{min})) is known;
2. the reduction at (q) is multiplicative;
3. (q
mid p);
4. (p
mid v_q(Delta_{min})).

## 7. Evolved candidate

Candidate `C113-02` keeps the valid group-theoretic component and replaces the invalid universal local step:

- for each concrete Frey family, derive the minimal discriminant at every fixed bad prime and every solution-variable prime;
- search for a prime of multiplicative reduction whose minimal-discriminant valuation is nonzero modulo the representation prime;
- only then use transvection-Cartan incompatibility.

The first discriminating family should be ((2,3,p)), because the (qmid C), (q
otin{2,3}) primes are now known **not** to supply the desired transvection; any repaired route must come from the fixed primes (2,3), from a different Frey model, or from a different irreducibility argument.

## 8. Other population priorities

- `C113-03` — **VERIFICATION_REQUIRED**: adversarially audit the claimed U105 closure of
  [
  X^{10}+256Y^{10}=Z^{17},
  ]
  beginning with the asserted map from integer solutions to (k)-rational points and the “degree-10 obstruction.”
- `C113-04` — **PARTIAL_RESULT**: retain the bounded exact search through the U112 domain, but do not enlarge it blindly.
- `C113-05` — **ACTIVE**: restart from local congruence/valuation structure for unresolved mixed signatures.

## 9. Tool/capability record

- GitHub: connected and writable; repository confirmed private.
- Mathbox: research-program, research-attempt, literature-check, computation-audit, proof-audit, and research-state instructions are available.
- Wolfram: exact evaluator available and used for the valuation sanity check.
- Consensus: unavailable for new searches in this run because the connected account's monthly search quota is exhausted; no additional spending was authorized or used.
- Jev/Typesafe: no callable Jev plugin was exposed in this session. No result in this checkpoint is attributed to Jev. The population file uses the requested narrow routing schema transparently as a temporary surrogate.
- No `.mathbox` ledger was found in the repository; the existing checkpoint/research-index structure is retained rather than creating parallel bookkeeping infrastructure.

## 10. Official-status check

Checked 2026-09-17. The current UNT Beal page still states the conjecture and displays the $1,000,000 prize as held by the AMS. Direct retrieval of the current AMS prize and rules endpoints returned HTTP 403 in this environment, so this checkpoint does not claim a fresh verification of all AMS procedural details or any award decision.

## 11. Next exact action

Audit `C113-03`: reconstruct the U105 weighted-equation map and determine whether a putative integer solution must actually produce a (k)-rational point on the stated genus-8 curve. A degree-(10) field-of-definition statement cannot itself exclude the solution if the construction naturally lands over that extension rather than over (k).
