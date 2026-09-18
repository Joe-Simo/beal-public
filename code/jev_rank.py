"""Standard per-candidate Jev triage for the Beal exploration loop.

Usage:
    python3 code/jev_rank.py                 # rank every ACTIVE candidate in the pool
    python3 code/jev_rank.py C012 C017       # rank named candidates
    python3 code/jev_rank.py --selftest      # one throwaway state, verifies connectivity

One request per candidate, same questions for all, concurrent. Output is a routing
table only: no answer here may set a candidate to PROVED, REFUTED or VERIFIED.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import jev

REPO = Path(__file__).resolve().parent.parent
POOL = REPO / "research" / "pool" / "candidates.json"

CONJECTURE = (
    "Beal's conjecture: if A^x + B^y = C^z with A,B,C,x,y,z positive integers and "
    "x,y,z > 2, then A, B, C share a common prime factor. Equivalently, the "
    "generalized Fermat equation A^x + B^y = C^z has no primitive solutions with "
    "all exponents at least 3. Current project work: modular method / Frey curves, "
    "Kraus sieves over signatures (3,3,p), (2,4,n), (5,5,p), Hilbert modular forms "
    "over real quadratic fields, Chabauty-Coleman on higher-genus quotients, "
    "cyclotomic class-group audits, and Lean 4 formalization of settled signatures."
)

QUESTIONS = {
    "relevance": jev.score(
        "How directly would establishing this research candidate's exact stated claim bear on "
        "Beal's conjecture itself, as opposed to on some peripheral or already-settled case? "
        "Judge the claim as written, not the enthusiasm of its description.",
        [
            "level 0: the claim concerns an unrelated problem, or a case already fully settled in the project, so proving it changes nothing about Beal's conjecture",
            "level 1: the claim touches the modular method in general but resolves no signature or family of exponents appearing in Beal's conjecture",
            "level 2: the claim would settle finitely many additional exponent triples, or one signature for a bounded range of primes",
            "level 3: the claim would settle an entire infinite signature family such as (3,3,p) for all primes p, or (5,5,p) for all p",
            "level 4: the claim would settle all remaining signatures with min exponent at least 3, or otherwise prove Beal's conjecture outright",
        ],
    ),
    "novelty": jev.score(
        "How different is the mathematical mechanism of this candidate from the mechanisms already "
        "present in the existing candidate pool listed in the state? Different wording of the same "
        "Frey-curve-plus-level-lowering argument is not novelty; a different source of finiteness is.",
        [
            "level 0: the same mechanism as an existing pool candidate, differing only in wording or in the numerical range searched",
            "level 1: an existing mechanism applied to a new signature or a new field, with no new structural ingredient",
            "level 2: an existing mechanism combined with one genuinely new ingredient such as a new descent, quotient, or auxiliary curve",
            "level 3: a mechanism not represented in the pool at all, for instance a different cohomological, analytic, or Diophantine-approximation source of finiteness",
        ],
    ),
    "proof_leverage": jev.score(
        "Assume this candidate's exact stated claim is true and available as a black box. How much of "
        "the remaining path to Beal's conjecture then follows by routine or already-completed arguments?",
        [
            "level 0: even granting the claim, no currently open case becomes easier",
            "level 1: granting the claim removes one technical obstruction inside a single ongoing argument",
            "level 2: granting the claim closes one open signature or exponent family by arguments already implemented in the project",
            "level 3: granting the claim reduces all remaining open cases to a finite, explicitly computable check",
            "level 4: granting the claim yields Beal's conjecture immediately",
        ],
    ),
    "failure_similarity": jev.score(
        "How closely does this candidate resemble a route recorded in the state as already REFUTED or "
        "BLOCKED, in the sense that it would run into the same obstruction for the same reason?",
        [
            "level 0: no recorded failed route shares this candidate's obstruction",
            "level 1: a recorded failed route shares surface features but the obstruction that stopped it does not apply here",
            "level 2: a recorded failed route hits an obstruction that plausibly applies here too, though the candidate proposes something that might avoid it",
            "level 3: this candidate would meet exactly the obstruction that already stopped a recorded route, with nothing new offered to avoid it",
        ],
    ),
    "contradiction_risk": jev.score(
        "How likely is this candidate's stated claim to contradict an established published theorem or a "
        "verified computation recorded in this project?",
        [
            "level 0: the claim is consistent with everything established and follows familiar patterns",
            "level 1: the claim is stronger than anything established but no known result rules it out",
            "level 2: the claim implies something that known results make doubtful, such as uniformity where only ineffective finiteness is known",
            "level 3: the claim directly contradicts a published theorem or a verified computation in this project",
        ],
    ),
    "needs_literature_check": jev.noul(
        "Should the next action on this candidate be to verify its claimed external inputs against the "
        "primary published sources, before any further reasoning is invested in it?",
        true="the candidate leans on a cited external theorem, a level-lowering or modularity statement, or a newform or class-number table whose exact hypotheses have not been checked against the primary source",
        false="the candidate's external inputs are already verified against primary sources, or it uses none",
    ),
    "needs_computation_check": jev.noul(
        "Should the next action on this candidate be an exact computation, such as a symbolic derivation, "
        "an exhaustive bounded search, or a class-group or newform calculation in exact arithmetic?",
        true="the candidate rests on a numerical or finite claim that has not been verified in exact arithmetic, or a bounded counterexample search would discriminate it",
        false="the candidate is purely structural, or its computational content has already been verified exactly",
    ),
    "needs_proof_audit": jev.noul(
        "Should the next action on this candidate be an adversarial step-by-step proof audit that re-derives "
        "each step from its stated hypotheses alone and lists every implicit assumption?",
        true="the candidate presents a chain of reasoning whose steps have not been independently re-derived, or whose hypotheses may be used beyond what is stated",
        false="the candidate is a bare conjecture or computation with no reasoning chain yet, or its chain has already been audited",
    ),
    "recommended_action": jev.choice(
        "What single next action should this candidate receive from the research loop right now?",
        {
            "advance": "the candidate is sound so far and the productive next step is more mathematical development along its own line",
            "combine": "the candidate is stalled alone but has an ingredient that fits a specific other pool candidate, and merging them is the productive step",
            "counterexample_search": "the candidate makes a falsifiable claim and a bounded or randomized search could refute it cheaply",
            "exact_computation": "the candidate's next discriminating test is a symbolic or exact-arithmetic computation",
            "formalize": "the candidate's argument is believed complete and small enough to check in Lean 4 or Z3",
            "literature_check": "the candidate's next discriminating test is verifying a cited result against its primary source",
            "park": "the candidate may become useful later but nothing can discriminate it now, so it should be preserved untouched",
            "discard": "the candidate is refuted, duplicated, or has no path forward, and only its extracted lemma or obstruction is worth keeping",
        },
    ),
}


def load_pool() -> list[dict]:
    if not POOL.exists():
        return []
    return json.loads(POOL.read_text())["candidates"]


def rank(candidates: list[dict], pool: list[dict]) -> list[dict]:
    summary = [
        {"id": c["id"], "claim": c["claim"], "method": c.get("method"), "status": c.get("status"),
         "failure_reason": c.get("failure_reason")}
        for c in pool
    ]
    states = [{"conjecture": CONJECTURE, "candidate": c, "existing_pool": summary} for c in candidates]
    responses = jev.ask_many(states, QUESTIONS)
    rows = []
    for cand, state, resp in zip(candidates, states, responses):
        if "error" in resp:
            print(f"  ! {cand['id']}: {resp['error']}", file=sys.stderr)
            rows.append({"id": cand["id"], "error": resp["error"]})
            continue
        jev.persist(cand["id"], state, QUESTIONS, resp)
        a = resp["answers"]
        rows.append({
            "id": cand["id"],
            "state": "HYPOTHESIS_ONLY",
            "relevance": a["relevance"]["score"],
            "novelty": a["novelty"]["score"],
            "proof_leverage": a["proof_leverage"]["score"],
            "failure_similarity": a["failure_similarity"]["score"],
            "contradiction_risk": a["contradiction_risk"]["score"],
            "needs_literature_check": round(a["needs_literature_check"]["noul"], 3),
            "needs_computation_check": round(a["needs_computation_check"]["noul"], 3),
            "needs_proof_audit": round(a["needs_proof_audit"]["noul"], 3),
            "recommended_action": a["recommended_action"]["choice"],
            "action_confidence": round(a["recommended_action"]["confidence"], 3),
        })
    return rows


def selftest() -> int:
    probe = {
        "conjecture": CONJECTURE,
        "candidate": {"id": "SELFTEST", "claim": "2 + 2 = 4", "method": "arithmetic",
                      "status": "ACTIVE"},
        "existing_pool": [],
    }
    q = {"relevance": QUESTIONS["relevance"], "recommended_action": QUESTIONS["recommended_action"]}
    try:
        resp = jev.ask(probe, q)
    except jev.JevUnavailable as e:
        print(f"Jev DEGRADED: {e}", file=sys.stderr)
        return 1
    print(json.dumps(resp, indent=2))
    return 0


def main() -> int:
    args = [a for a in sys.argv[1:]]
    if "--selftest" in args:
        return selftest()
    pool = load_pool()
    if not pool:
        print(f"empty pool: {POOL}", file=sys.stderr)
        return 1
    wanted = set(args)
    cands = [c for c in pool if (c["id"] in wanted) if wanted] or \
            [c for c in pool if c.get("status") in ("ACTIVE", "PROMISING", "PARTIAL_RESULT")]
    rows = rank(cands, pool)
    rows.sort(key=lambda r: (
        -(r.get("relevance", 0) + r.get("proof_leverage", 0) + r.get("novelty", 0)
          - r.get("failure_similarity", 0) - r.get("contradiction_risk", 0))))
    print(json.dumps({"state": "HYPOTHESIS_ONLY", "ranking": rows}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
