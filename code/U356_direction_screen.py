"""Jev screen: which pool candidates use an approximation whose DIRECTION is not checked?

FM (unchecked approximation direction): a candidate relies on a bound, an interval, a sieve, a
superset or a subset, and the conclusion is only valid if the approximation errs one particular
way -- but the candidate does not say which way it errs.

This mode produced both an error and a save on this project within two cycles:

  * ERROR (C206): `ellrank(E)[1]` is the LOWER bound of PARI's rank interval. Using it to conclude
    `rank = 0` is unsound; a lower bound of 0 says nothing. The correct index is `[2]`, the upper
    bound.
  * SAVE (C208): C079 flags a torsion point when `denominator(x) > 1`, which is a strict SUPERSET
    of the Beal-relevant points `denominator(x) = n^j`. It can over-flag but never miss, and
    over-flagging is the safe direction for a closure claim. Confirmed with an explicit
    over-flagging witness.

Reasoning found the mode; Jev finds the instances. One request per candidate, same questions,
concurrency 12. Every result is a routing signal stored HYPOTHESIS_ONLY: a high score means read
this next, never that the candidate is wrong.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

REPO = Path(__file__).resolve().parent.parent
POOL = REPO / "research" / "pool" / "candidates.json"

QUESTIONS = {
    "uses_approximation": jev.noul(
        "Does this candidate rely on a quantity that is an APPROXIMATION rather than an exact "
        "value -- a rank interval, an upper or lower bound, a sieve that removes some cases, a "
        "superset or subset of the objects of interest, or a finite range standing in for an "
        "infinite one?",
        true="its conclusion depends on a bound, an interval endpoint, a sieve, a superset or subset, or a truncated range",
        false="every quantity it uses is exact, or it is a log or a ledger with no quantitative claim",
    ),
    "direction_unstated": jev.score(
        "If the candidate uses an approximation, does it SAY WHICH WAY the approximation errs and "
        "why that direction makes the conclusion safe? Judge only whether the direction is stated, "
        "not whether the mathematics is right.",
        [
            "level 0: it uses no approximation, so the question does not arise",
            "level 1: it uses one and explicitly states the direction and why that direction is safe",
            "level 2: it uses one and the direction is implied but never stated",
            "level 3: it uses one, the conclusion depends on the direction, and the direction is neither stated nor implied",
        ],
    ),
    "conservative_or_optimistic": jev.choice(
        "If the direction can be inferred at all, which way does the approximation err?",
        {
            "conservative": "it over-approximates the danger -- it may flag or keep too much, so it cannot miss a case the conclusion needs excluded",
            "optimistic": "it under-approximates -- it may exclude or discard a case that the conclusion needs, so a miss is possible",
            "cannot_tell": "the text does not allow the direction to be determined",
            "not_applicable": "no approximation is used",
        },
    ),
    "next_action": jev.choice(
        "What should be done with this candidate next, given the failure mode?",
        {
            "check_direction_now": "its conclusion plausibly depends on an unstated direction and something load-bearing rests on it",
            "state_direction": "the direction is probably fine but is not written down, so it should be recorded",
            "no_action": "it uses no approximation, or the direction is already stated",
        },
    ),
}

CONTEXT = {
    "conjecture": "Beal: A^x + B^y = C^z with x,y,z >= 3 and gcd(gcd(A,B),C) = 1 has no solutions.",
    "failure_mode": "Unchecked approximation direction. C206: ellrank(E)[1] is PARI's LOWER rank "
                    "bound; using it to conclude rank = 0 is unsound, the upper bound [2] is the "
                    "sound index. C208: C079 flags denominator(x) > 1, a strict superset of the "
                    "Beal-relevant denominator(x) = n^j, so it over-flags but never misses -- the "
                    "safe direction for a closure claim, confirmed with an over-flagging witness.",
    "rule": "For a CLOSURE claim the safe direction is to over-approximate the set of dangerous "
            "cases. For an EXISTENCE claim it is the opposite. A candidate that does not say which "
            "way its approximation errs cannot be relied on either way.",
}


def summarize(c: dict, limit: int = 4000) -> dict:
    keep = {k: c.get(k) for k in
            ("id", "status", "claim", "method", "evidence", "obligations", "failure_reason")}
    return {"candidate": json.dumps(keep, indent=1)[:limit]}


def main() -> int:
    data = json.loads(POOL.read_text())
    cands = data["candidates"] if isinstance(data, dict) and "candidates" in data else data
    if len(sys.argv) > 1:
        wanted = set(sys.argv[1:])
        cands = [c for c in cands if c.get("id") in wanted]
    cands = [c for c in cands if c.get("status") != "DUPLICATE"]
    states = [{**CONTEXT, **summarize(c)} for c in cands]
    print(f"screening {len(cands)} candidates via Jev ...", file=sys.stderr)
    try:
        responses = jev.ask_many(states, QUESTIONS)
    except Exception as e:  # noqa: BLE001
        print(f"JEV UNREACHABLE: {e}. Degradation logged; reason over the pool instead.",
              file=sys.stderr)
        return 2
    rows = []
    for c, st, resp in zip(cands, states, responses):
        if "error" in resp:
            print(f"  ! {c.get('id')}: {resp['error']}", file=sys.stderr)
            continue
        jev.persist(f"direction_{c.get('id')}", st, QUESTIONS, resp)
        a = resp["answers"]
        rows.append({
            "id": c.get("id"),
            "status": c.get("status"),
            "uses_approx": round(a["uses_approximation"]["noul"], 2),
            "unstated": round(a["direction_unstated"]["score"], 2),
            "errs": a["conservative_or_optimistic"]["choice"],
            "errs_conf": round(a["conservative_or_optimistic"]["confidence"], 2),
            "action": a["next_action"]["choice"],
            "conf": round(a["next_action"]["confidence"], 2),
        })
    rows.sort(key=lambda r: -(r["unstated"] + r["uses_approx"]))
    print(json.dumps({
        "state": "HYPOTHESIS_ONLY",
        "note": "routing only; a high score means read this next, never that it is wrong",
        "screened": len(rows),
        "top": rows[:15],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
