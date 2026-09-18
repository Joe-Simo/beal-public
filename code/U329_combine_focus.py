"""Jev pairwise-combination screen, restricted to the live obstruction line.

`code/U113_combine_and_salvage.py` runs every unordered pair of the pool, which is now
C(183,2) = 16,653 requests.  This driver reuses its exact questions on a focused set: the
candidates produced by the U309-U328 obstruction cycle together with the older structural ones
they bear on.  91 pairs instead of 16,653.

NOVEL COMBINATION is the loop mechanism this cycle is exercising: not "is candidate X right" but
"does candidate X discharge an obligation recorded in candidate Y".  Every result is a routing
signal stored HYPOTHESIS_ONLY; a high score means read the pair next, never that the combination
works.
"""
from __future__ import annotations
import itertools, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev
from U113_combine_and_salvage import COMBINE_Q, CONJ  # exact same questions, no restatement

REPO = Path(__file__).resolve().parent.parent
POOL = json.loads((REPO / "research" / "pool" / "candidates.json").read_text())["candidates"]

# the obstruction line built this session, plus the older structural candidates it bears on
FOCUS = [
    "C169",  # rigidity permits three distinct orders (refuted the U258 headline)
    "C170",  # rank >= phi(m) over Q
    "C171",  # automorphy is the surviving obstruction (later corrected)
    "C172",  # opposite parity needs no Chabauty, reduces to Euler
    "C174",  # the object is never regular
    "C175",  # regularity obstruction does not need rigidity
    "C176",  # the base-field escape is cheap, so C174/C175 are about Q only
    "C177",  # Euler reduced to its descent step (carried the U322 flaw)
    "C179",  # first steps of the descent machine-checked
    "C180",  # the square-target shortcut is refuted
    "C083",  # no Frey object for three independent exponents
    "C128",  # two exponents can be related, the third cannot
    "C157",  # the factorisation descent needs gcd(y,z) > 1
    "C015",  # the Lean development and its fidelity obligation
]


def main() -> int:
    by_id = {c["id"]: c for c in POOL}
    missing = [i for i in FOCUS if i not in by_id]
    if missing:
        print(f"missing candidates: {missing}", file=sys.stderr)
    chosen = [by_id[i] for i in FOCUS if i in by_id]
    pairs = list(itertools.combinations(chosen, 2))
    states = [{"conjecture": CONJ, "candidate_A": a, "candidate_B": b} for a, b in pairs]
    print(f"screening {len(pairs)} focused pairs via Jev ...", file=sys.stderr)
    try:
        resps = jev.ask_many(states, COMBINE_Q, concurrency=12)
    except Exception as e:  # noqa: BLE001
        print(f"JEV UNREACHABLE: {e}. Degradation logged; reason over the pool instead.",
              file=sys.stderr)
        return 2
    rows = []
    for (a, b), st, r in zip(pairs, states, resps):
        if "error" in r:
            print(f"  ! {a['id']}+{b['id']}: {r['error']}", file=sys.stderr)
            continue
        jev.persist(f"combine_focus_{a['id']}_{b['id']}", st, COMBINE_Q, r)
        an = r["answers"]
        rows.append({
            "pair": f"{a['id']}+{b['id']}",
            "compat": round(an["compatible"]["noul"], 2),
            "value": round(an["combination_value"]["score"], 2),
            "shared_fail": round(an["shared_failure"]["noul"], 2),
        })
    rows.sort(key=lambda r: -(r["value"] + r["compat"] - r["shared_fail"]))
    print(json.dumps({
        "state": "HYPOTHESIS_ONLY",
        "note": "routing only; a high score means read this pair next, never that the combination works",
        "pairs_screened": len(rows),
        "top": rows[:12],
        "bottom": rows[-5:],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
