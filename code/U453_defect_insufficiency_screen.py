"""U453: Jev Screen for Hyperbolic Defect Insufficiency & Fermat-Catalan Blindness.

Failure Mode:
Argues that positive hyperbolic defect -chi = 1 - 1/x - 1/y - 1/z > 0 (negative orbifold
Euler characteristic) implies non-existence of primitive integer solutions.
Flaw: Signatures (2, 3, 7), (2, 3, 8), (2, 3, 9), (2, 4, 5) all have -chi > 0 AND have
primitive non-trivial integer solutions (the 10 Fermat-Catalan identities).
Any argument using only -chi > 0 without explicitly utilizing min(x, y, z) >= 3
cannot prove non-existence of solutions.

One request per candidate, identical questions, concurrent jev.ask_many.
Results stored as HYPOTHESIS_ONLY routing signals.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys
import time

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "code"))
import jev

POOL_FILE = REPO / "research" / "pool" / "candidates.json"
OUTPUT_FILE = REPO / "research" / "pool" / "evidence" / f"screen_defect_insufficiency_{int(time.time())}.json"

FC_WITNESSES = [
    "7^3 + 13^2 = 2^9 (signature (3, 2, 9), -chi = 1/18 > 0)",
    "1^6 + 2^3 = 3^2 (signature (6, 3, 2), -chi = 1/6 > 0)",
    "2^5 + 7^2 = 3^4 (signature (5, 2, 4), -chi = 1/20 > 0)",
    "1414^3 + 2213459^2 = 65^7 (signature (3, 2, 7), -chi = 1/42 > 0)",
]

QUESTIONS = {
    "hyperbolic_defect_reliance": jev.score(
        instructions=(
            "Does this candidate argue that the positive hyperbolic defect -chi = 1 - 1/x - 1/y - 1/z > 0 "
            "(or negative Euler characteristic / hyperbolic area of the triangle curve) forces integer points to be empty?",
        ),
        criteria=[
            "level 0: Does not use hyperbolic defect, Euler characteristic, or triangle curvature at all.",
            "level 1: Mentions hyperbolic defect only as background context, relying on modular forms or other tools.",
            "level 2: Uses hyperbolic defect as a necessary condition for finiteness, but does not claim non-existence from it alone.",
            "level 3: Directly claims that -chi > 0 forces non-existence of solutions, or derives contradiction from -chi > 0 alone.",
        ],
    ),
    "fc_blindness_vulnerability": jev.noul(
        instructions=(
            f"Would the mathematical mechanism of this candidate hold equally for the known Fermat-Catalan identities with exponent 2 ({FC_WITNESSES[0]}, {FC_WITNESSES[1]})? "
            "Specifically, does the argument fail to use the condition min(x, y, z) >= 3 in a way that breaks down on exponent 2?"
        ),
        true="The mechanism holds on exponent 2 identities; it is vulnerable to Fermat-Catalan blindness.",
        false="The mechanism strictly breaks down or produces a contradiction when one exponent is 2.",
    ),
    "action_routing": jev.choice(
        instructions="What routing action should be taken on this candidate?",
        criteria={
            "refute_defect_insufficiency": "Candidate relies on defect insufficiency; mark BLOCKED with Fermat-Catalan counterexample.",
            "audit_exponent_separation": "Candidate may separate exponent 2 from >= 3; audit whether min(x,y,z)>=3 is genuinely used.",
            "sound_independent": "Candidate does not rely on hyperbolic defect; mechanism is independent.",
        },
    ),
}


def main():
    if not POOL_FILE.exists():
        print(f"[ERR] Pool file {POOL_FILE} not found.")
        return 1

    pool_data = json.loads(POOL_FILE.read_text()).get("candidates", [])
    # Screen structural / geometric candidates
    candidates = [
        c for c in pool_data
        if c.get("category") in ("effective_diophantine_geometry", "unifying_modular_motivic_geometry")
    ][-15:]

    print(f"[U453] Screening {len(candidates)} geometric/motivic candidates for Hyperbolic Defect Insufficiency...")

    states = []
    for c in candidates:
        states.append({
            "candidate_id": c["id"],
            "title": c.get("title", c["id"]),
            "claim": c.get("claim", ""),
            "method": c.get("method", ""),
            "category": c.get("category", ""),
            "fc_witnesses": FC_WITNESSES,
        })

    responses = jev.ask_many(states, QUESTIONS, concurrency=min(12, len(states)))

    results = []
    print("\n" + "=" * 80)
    print("HYPERBOLIC DEFECT INSUFFICIENCY & FC-BLINDNESS SCREEN RESULTS")
    print("=" * 80)

    flagged_count = 0
    for state, resp in zip(states, responses):
        cid = state["candidate_id"]
        if "error" in resp:
            print(f"[FAIL] {cid}: {resp['error']}")
            continue

        jev.persist(f"SCREEN_DEFECT_{cid}", state, QUESTIONS, resp)
        answers = resp.get("answers", {})

        score_val = answers.get("hyperbolic_defect_reliance", {}).get("score", 0.0)
        fc_vuln = answers.get("fc_blindness_vulnerability", {}).get("noul", 0.0) >= 0.5
        routing = answers.get("action_routing", {}).get("choice", "sound_independent")

        is_flagged = (score_val >= 2.0 and fc_vuln)
        if is_flagged:
            flagged_count += 1

        status_str = "FLAGGED (DEFECT BLIND)" if is_flagged else "PASS / INDEPENDENT"
        print(f"[{status_str}] {cid:<6} | Defect Score: {score_val:.2f}/3.00 | FC-Blind: {str(fc_vuln):<5} | Action: {routing}")
        print(f"         Title: {state['title'][:65]}")

        results.append({
            "candidate_id": cid,
            "title": state["title"],
            "defect_score": score_val,
            "fc_blind": fc_vuln,
            "action": routing,
            "flagged": is_flagged,
        })

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(results, indent=2))
    print("\n" + "=" * 80)
    print(f"Screen complete: {flagged_count}/{len(candidates)} candidates flagged for defect insufficiency.")
    print(f"Evidence saved to: {OUTPUT_FILE}")
    print("=" * 80)
    return 0


if __name__ == "__main__":
    sys.exit(main())
