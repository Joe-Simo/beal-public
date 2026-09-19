"""High-throughput Jev screen for Salvage, Pairwise Combination, and Flaw Detection.
Screening:
- Batch 1: Salvage analysis over Checkpoints U300-U308
- Batch 2: Pairwise combination analysis across live/geometric candidates C379-C389
- Batch 3: Three-failure-mode scan across candidates C370-C389
"""
from __future__ import annotations
import itertools
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

REPO = Path(__file__).resolve().parent.parent
CKPT_DIR = REPO / "research" / "checkpoints"
POOL_FILE = REPO / "research" / "pool" / "candidates.json"

# 1. SALVAGE QUESTIONS
SALVAGE_Q = {
    "has_proved_lemma": jev.score(
        "Does this checkpoint contain a genuinely proved, self-contained lemma (exact computation, algebraic identity, or certified sieve)?",
        [
            "level 0: No self-contained proofs; entirely conditional on conjectures or citations.",
            "level 1: Routine verification checks with no independent mathematical lemma.",
            "level 2: Self-contained exact algebraic identity, certified modular traces, or defect bounds.",
            "level 3: Deep self-contained mathematical classification or Lean 4 formalized theorem.",
        ],
    ),
    "reusable_lemma": jev.noul(
        "Does the checkpoint contain an extracted lemma that remains valid and reusable even if Beal remains open?",
        true="Yes, contains reusable algebraic identities, sieve certificates, or obstruction classifications.",
        false="No, entirely tied to speculative headline claims.",
    ),
    "salvage_action": jev.choice(
        "What is the recommended salvage action for this checkpoint?",
        {
            "extract_lemma": "Formally extract the proved lemma into the Lean 4 or Python core library.",
            "maintain_cert": "Maintain as an exact empirical verification milestone certificate.",
            "retire_unconditional": "Retire headline claims while preserving failure analysis.",
            "none": "No substantive content to salvage.",
        },
    ),
}

# 2. COMBINATION QUESTIONS
COMBINE_Q = {
    "compatible": jev.noul(
        "Are these two candidates mathematically compatible, operating on complementary aspects of the conjecture?",
        true="Yes, one provides input to the other or they address complementary signatures/invariants.",
        false="No, they operate in disjoint or contradictory frameworks.",
    ),
    "combination_value": jev.score(
        "What value would combining these two candidate approaches create?",
        [
            "level 0: Zero value; combination fails or is identical to one candidate alone.",
            "level 1: Minor bookkeeping convenience without resolving open obstacles.",
            "level 2: Discharges a specific open obligation in one of the candidates.",
            "level 3: Opens a genuine new attack route avoiding known dead ends.",
        ],
    ),
    "shared_failure": jev.noul(
        "Do both candidates fail due to the same fundamental obstruction (e.g. deformation invariance, Selmer blowup, or heuristic laundering)?",
        true="Yes, both share the same failure mode and combining them provides no new leverage.",
        false="No, they hit independent failure modes, offering structural contrast.",
    ),
}

# 3. FLAW DETECTION QUESTIONS
FLAW_Q = {
    "has_conflation": jev.noul(
        "Does this candidate commit Failure Mode 1 (residual/isogeny conflation, or confounding complex moduli deformation with arithmetic coordinates)?",
        true="Yes, conflates residual/geometric properties with Diophantine point exclusion.",
        false="No, maintains strict distinction between arithmetic coordinates and geometric moduli.",
    ),
    "has_chabauty_field_slip": jev.noul(
        "Does this candidate commit Failure Mode 2 (Chabauty over wrong field, or ignoring unbounded bad reduction blowup)?",
        true="Yes, applies Chabauty rank bounds over base field to higher degree points or ignores Selmer dimension blowup.",
        false="No, correctly accounts for field degrees and Selmer variety growth.",
    ),
    "has_heuristic_laundering": jev.noul(
        "Does this candidate commit Failure Mode 3 (heuristic laundering, treating GRH/ABC/Vojta bounds as unconditional)?",
        true="Yes, relabels conjectural height bounds or heuristics as unconditional results.",
        false="No, strictly relies on exact unconditional arithmetic.",
    ),
}

def run_salvage_screen():
    print("\n--- BATCH 1: SALVAGE SCREEN OVER CHECKPOINTS U300-U308 ---")
    ckpt_files = sorted([f for f in CKPT_DIR.glob("U30*.md")])
    states = []
    names = []
    for f in ckpt_files:
        content = f.read_text()[:1500]  # First 1500 chars
        names.append(f.stem)
        states.append(f"Checkpoint: {f.name}\n\nContent excerpt:\n{content}")

    results = jev.ask_many(states, SALVAGE_Q, concurrency=8)
    for name, state, resp in zip(names, states, results):
        ans = resp.get("answers", {})
        score = ans.get("has_proved_lemma", {}).get("score")
        reusable = ans.get("reusable_lemma", {}).get("value")
        action = ans.get("salvage_action", {}).get("choice")
        print(f"[{name}] ProvedScore: {score} | Reusable: {reusable} | Action: {action}")
        jev.persist(f"salvage_{name}", state, SALVAGE_Q, resp)

def run_pairwise_screen():
    print("\n--- BATCH 2: PAIRWISE COMBINATION SCREEN (C379-C389) ---")
    with open(POOL_FILE) as f:
        pool = json.load(f)["candidates"]
    cands = {c["id"]: c for c in pool if c["id"] in ["C379", "C380", "C381", "C383", "C384", "C385", "C387", "C388", "C389"]}
    cids = sorted(cands.keys())
    pairs = list(itertools.combinations(cids, 2))
    
    states = []
    pair_labels = []
    for c1, c2 in pairs:
        label = f"{c1}+{c2}"
        pair_labels.append(label)
        s1 = cands[c1]
        s2 = cands[c2]
        state = (
            f"Candidate 1 ({c1}): {s1.get('title')}\nClaim 1: {s1.get('claim')}\nMethod 1: {s1.get('method')}\n\n"
            f"Candidate 2 ({c2}): {s2.get('title')}\nClaim 2: {s2.get('claim')}\nMethod 2: {s2.get('method')}\n"
        )
        states.append(state)

    results = jev.ask_many(states, COMBINE_Q, concurrency=12)
    for label, state, resp in zip(pair_labels, states, results):
        ans = resp.get("answers", {})
        compat = ans.get("compatible", {}).get("value")
        val = ans.get("combination_value", {}).get("score")
        shared = ans.get("shared_failure", {}).get("value")
        print(f"[{label}] Compatible: {compat} | ValueScore: {val} | SharedFailure: {shared}")
        jev.persist(f"combine_{label}", state, COMBINE_Q, resp)

def run_flaw_screen():
    print("\n--- BATCH 3: THREE-FAILURE-MODE SCREEN (C370-C389) ---")
    with open(POOL_FILE) as f:
        pool = json.load(f)["candidates"]
    target_ids = [f"C{i}" for i in range(370, 390)]
    cands = [c for c in pool if c["id"] in target_ids]
    
    states = []
    cids = []
    for c in cands:
        cid = c["id"]
        cids.append(cid)
        state = f"Candidate: {cid} - {c.get('title')}\nClaim: {c.get('claim')}\nMethod: {c.get('method')}\nStatus: {c.get('status')}\nFailureReason: {c.get('failure_reason')}"
        states.append(state)

    results = jev.ask_many(states, FLAW_Q, concurrency=12)
    for cid, state, resp in zip(cids, states, results):
        ans = resp.get("answers", {})
        conf = ans.get("has_conflation", {}).get("value")
        chab = ans.get("has_chabauty_field_slip", {}).get("value")
        laund = ans.get("has_heuristic_laundering", {}).get("value")
        print(f"[{cid}] Conflation: {conf} | ChabautySlip: {chab} | Laundering: {laund}")
        jev.persist(f"flaw_{cid}", state, FLAW_Q, resp)

def main():
    print("================================================================================")
    print("      U435: COMPREHENSIVE HIGH-THROUGHPUT JEV SCREEN (SALVAGE + COMBINE + FLAW) ")
    print("================================================================================")
    run_salvage_screen()
    run_pairwise_screen()
    run_flaw_screen()
    print("================================================================================")
    print("ALL JEV SCREEN BATCHES COMPLETED AND PERSISTED TO research/pool/evidence/ !")
    print("================================================================================")

if __name__ == "__main__":
    main()
