"""Two Jev batches the loop has been neglecting.

BATCH 1 - COMBINATION: every unordered pair of pool candidates (C(n,2) requests). The brief
lists "whether two approaches are promising to combine" as a Jev decision; it had never been used.

BATCH 2 - SALVAGE: every checkpoint, asked whether it contains a result that is genuinely
unconditionally proved and reusable as a lemma elsewhere -- the inverse of the flaw screens,
which only looked for what is broken.
"""
from __future__ import annotations
import itertools, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

REPO = Path(__file__).resolve().parent.parent
POOL = json.loads((REPO / "research" / "pool" / "candidates.json").read_text())["candidates"]
CKPT = REPO / "research" / "checkpoints"

CONJ = ("Beal: A^x + B^y = C^z with x,y,z >= 3 and gcd(gcd(A,B),C) = 1 has no solutions. "
        "Audit has shown three recurring failure modes in this project: conflating a residual "
        "mod-p congruence with an isogeny or l-adic statement; using a Chabauty rank bound over "
        "a base field to conclude about points of higher degree; and relabelling a GRH-conditional "
        "or heuristic result as unconditional.")

COMBINE_Q = {
    "compatible": jev.noul(
        "Are these two research candidates mathematically COMPATIBLE, in the sense that the "
        "objects, fields, exponents and equations they concern are the same or are related by a "
        "reduction that the project has already proved?",
        true="they concern the same equation, signature, curve or field, or one supplies an input the other consumes",
        false="they concern unrelated equations, signatures or methods, so no joint statement could be formed without inventing a new reduction",
    ),
    "combination_value": jev.score(
        "If these two candidates were combined into a single line of attack, how much would the "
        "combination accomplish beyond what the better of the two accomplishes alone?",
        [
            "level 0: nothing; the combination is just the stronger candidate restated, or they are incompatible",
            "level 1: the combination tidies bookkeeping but resolves no obligation that either one leaves open",
            "level 2: one candidate discharges a specific open obligation recorded in the other",
            "level 3: the combination closes a case or an infinite family that neither one closes alone",
        ],
    ),
    "shared_failure": jev.noul(
        "Would these two candidates FAIL FOR THE SAME REASON, so that combining them adds no "
        "diversity of failure mechanism and a single obstruction would defeat both?",
        true="both depend on the same blocked step, the same unverified citation, or the same one of the three recorded failure modes",
        false="they would fail for different reasons, so each provides genuine independent information",
    ),
}

SALVAGE_Q = {
    "has_proved_result": jev.score(
        "Does this checkpoint contain at least one result that is genuinely and unconditionally "
        "PROVED within it - an exact computation, an explicit algebraic identity, or a complete "
        "derivation - as opposed to a result that depends on an external citation, on another "
        "checkpoint, on GRH, on finiteness of Sha, or on a probabilistic heuristic?",
        [
            "level 0: every substantive claim depends on an external citation, another checkpoint, or an unproved hypothesis",
            "level 1: it contains only routine computations whose correctness is clear but which carry no mathematical content on their own",
            "level 2: it contains a self-contained exact computation or algebraic identity that would be reusable if verified",
            "level 3: it contains a complete self-contained derivation of a non-trivial statement, proved within the checkpoint itself",
        ],
    ),
    "reusable_elsewhere": jev.noul(
        "Would the self-contained part of this checkpoint remain valid and useful even if the "
        "checkpoint's headline conclusion were withdrawn?",
        true="it establishes an identity, a valuation profile, a conductor computation, a class-group fact or a point count that stands on its own",
        false="everything in it is downstream of the headline claim and falls with it",
    ),
}


def main() -> int:
    which = sys.argv[1] if len(sys.argv) > 1 else "both"
    if which in ("both", "combine"):
        pairs = list(itertools.combinations(POOL, 2))
        states = [{"conjecture": CONJ, "candidate_A": a, "candidate_B": b} for a, b in pairs]
        print(f"BATCH 1: {len(states)} candidate pairs ...", file=sys.stderr)
        resps = jev.ask_many(states, COMBINE_Q, concurrency=12)
        rows = []
        for (a, b), st, r in zip(pairs, states, resps):
            if "error" in r:
                continue
            jev.persist(f"combine_{a['id']}_{b['id']}", st, COMBINE_Q, r)
            an = r["answers"]
            rows.append({"pair": f"{a['id']}+{b['id']}",
                         "compat": round(an["compatible"]["noul"], 2),
                         "value": round(an["combination_value"]["score"], 2),
                         "shared_fail": round(an["shared_failure"]["noul"], 2)})
        rows.sort(key=lambda r: -(r["value"] + r["compat"] - r["shared_fail"]))
        print(json.dumps({"state": "HYPOTHESIS_ONLY", "combinations": rows[:15]}, indent=2))

    if which in ("both", "salvage"):
        paths = sorted(CKPT.glob("*.md"))
        states = [{"checkpoint": p.name, "excerpt": p.read_text(errors="replace")[:5000]}
                  for p in paths]
        print(f"BATCH 2: {len(states)} checkpoints ...", file=sys.stderr)
        resps = jev.ask_many(states, SALVAGE_Q, concurrency=12)
        rows = []
        for p, st, r in zip(paths, states, resps):
            if "error" in r:
                continue
            jev.persist(f"salvage_{p.stem}", st, SALVAGE_Q, r)
            an = r["answers"]
            rows.append({"file": p.name,
                         "proved": round(an["has_proved_result"]["score"], 2),
                         "reusable": round(an["reusable_elsewhere"]["noul"], 2)})
        rows.sort(key=lambda r: -(r["proved"] + r["reusable"]))
        print(json.dumps({"state": "HYPOTHESIS_ONLY", "salvage_top": rows[:20]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
