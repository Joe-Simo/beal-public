#!/usr/bin/env python3
"""
U393: Jev Screen for Live Candidates on Unifying Modular/Motivic Objects & Effective Diophantine Geometry
Evaluates active candidates targeting general exponents (x, y, z) >= 3 against:
1. Target relevance to general Beal conjecture (unifying object for three independent exponents)
2. Susceptibility to Fermat-Catalan blindness (does the mechanism distinguish exponent >= 3 from exponent 2?)
3. Risk of known failure modes:
   - Residual/isogeny/conductor conflation
   - Chabauty over wrong field / higher degree rational points
   - Heuristic laundering (unconditional vs conditional on Vojta/ABC/GRH)
4. Proof leverage and routing recommendation.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
import jev

CANDIDATES_JSON = ROOT / "research" / "pool" / "candidates.json"
EVIDENCE_DIR = ROOT / "research" / "pool" / "evidence"

TARGET_CONJECTURE = (
    "Beal's Conjecture: If A^x + B^y = C^z with A, B, C, x, y, z positive integers and x, y, z >= 3, "
    "then gcd(gcd(A, B), C) > 1. Equivalently, no coprime positive integer solutions exist for min(x,y,z) >= 3. "
    "Dead categories: single-signature Kraus sieves, bounded exponent searches, Baker linear forms, elementary congruences. "
    "Live directions: a unifying modular/motivic object for three independent exponents, and effective Diophantine geometry."
)

LIVE_CANDIDATE_IDS = [
    "C281",  # Darmon rigid local systems
    "C283",  # Jacobian GL_2 decomposition & potential modularity
    "C286",  # Motivic hypergeometric Galois representations
    "C287",  # Corvaja-Zannier arithmetic defect on orbifold surfaces
    "C289",  # Minhyong Kim non-abelian Chabauty on P^1 \ {0, 1, \infty}
    "C290",  # Belyi map branch locus rigidification
    "C291",  # Depth-2 Selmer scheme dimension for P^1 \ {0, 1, \infty}
    "C292",  # Lawrence-Venkatesh method on Frey families over exponent lattice
    "C293",  # Effective Arakelov height bounds on triangle orbifolds
    "C295",  # Universal Serre weight parity obstruction for three odd exponents
]

QUESTIONS = {
    "unifying_power": jev.score(
        "Does this candidate provide a UNIFYING object or mechanism for THREE INDEPENDENT exponents (x, y, z) >= 3, "
        "rather than fixing one or two exponents, or running one signature at a time?",
        [
            "level 0: fixes one or more exponents (e.g. signature (3, 3, p) or (2, 3, p)) or reduces to a single-signature sieve",
            "level 1: handles variable exponents only within a narrow parametrized algebraic family",
            "level 2: constructs a geometric or motivic object genuinely parametrized by arbitrary (x, y, z)",
            "level 3: constructs a universal modular or motivic obstruction that applies simultaneously to all triples (x, y, z) >= 3",
        ],
    ),
    "fc_blindness_risk": jev.noul(
        "Is there a risk that this candidate's mechanism is FERMAT-CATALAN BLIND, meaning that the identical condition "
        "or bound would hold on the ten known primitive Fermat-Catalan solutions with an exponent of 2 (e.g. 1 + 2^3 = 3^2)?",
        true="the mechanism depends only on the hyperbolic defect chi < 0 or topological Euler characteristic, which holds equally for exponent 2, so it cannot distinguish Beal from Fermat-Catalan",
        false="the mechanism specifically exploits that ALL THREE exponents are at least 3 (e.g. chi <= -1/12, or all three inertia actions are of order >= 3)",
    ),
    "unconditional_status": jev.score(
        "Is this candidate genuinely UNCONDITIONAL, as opposed to laundering a dependency on Vojta's conjecture, "
        "the ABC conjecture, GRH, or finiteness of Tate-Shafarevich groups?",
        [
            "level 0: explicitly or implicitly conditional on Vojta, ABC, or an unproved Diophantine conjecture",
            "level 1: depends on standard conjectures in the Langlands program (e.g. potential modularity or Fontaine-Mazur)",
            "level 2: depends only on proved modularity theorems and established p-adic Hodge theory",
            "level 3: completely unconditional and effective, relying solely on established theorems in Diophantine geometry",
        ],
    ),
    "routing_priority": jev.score(
        "What is the routing priority for allocating the next deep reasoning pass to this candidate?",
        [
            "level 0: park or discard; blocked by known failure mode or exponent-2 blindness",
            "level 1: low priority; requires unproved conjectures or lacks effective Diophantine bounds",
            "level 2: medium priority; genuine unifying object with non-trivial open obligations",
            "level 3: highest priority; promising live direction on unifying motivic objects or effective Diophantine geometry",
        ],
    ),
}


def main():
    pool_data = json.loads(CANDIDATES_JSON.read_text())
    candidates_by_id = {c["id"]: c for c in pool_data.get("candidates", [])}

    states = []
    for cid in LIVE_CANDIDATE_IDS:
        c = candidates_by_id.get(cid)
        if not c:
            continue
        state = {
            "id": cid,
            "claim": c.get("claim", ""),
            "method": c.get("method", ""),
            "target": TARGET_CONJECTURE,
        }
        states.append(state)

    print(f"Executing Jev batch screen across {len(states)} live candidates ...", file=sys.stderr)
    responses = jev.ask_many(states, QUESTIONS)

    results = []
    for s, resp in zip(states, responses):
        cid = s["id"]
        res_record = {
            "id": cid,
            "claim": s["claim"],
            "state": "HYPOTHESIS_ONLY",
            "unifying_power": resp.get("unifying_power", {}).get("score", 0),
            "fc_blindness_risk": resp.get("fc_blindness_risk", {}).get("value", True),
            "unconditional_status": resp.get("unconditional_status", {}).get("score", 0),
            "routing_priority": resp.get("routing_priority", {}).get("score", 0),
            "confidence": resp.get("routing_priority", {}).get("confidence", 0),
        }
        results.append(res_record)

        # Save individual evidence
        ev_file = EVIDENCE_DIR / f"live_screen_{cid}_{int(jev.time.time())}.json"
        ev_file.write_text(json.dumps({"state": s, "response": resp}, indent=2))

    # Sort by routing priority descending
    results.sort(key=lambda r: (r["routing_priority"], r["unifying_power"]), reverse=True)

    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
