"""Jev screen: which pool candidates carry the U322 failure mode?

FM (vacuous / degenerate hypothesis): a candidate states a named Prop, a reduction, or a
"remaining gap" whose hypotheses admit a degenerate instance -- a zero, a unit, an empty range, a
trivial solution -- that makes the statement FALSE as written, or makes a downstream implication
vacuously true.  This really happened here: `EulerDescentStep` was recorded as the residual gap of
the (3,4,4) chain and was false, with `p = 0, q = 1, c = 0`.  Lean could not notice, because an
implication from a false hypothesis still type-checks and everything downstream still compiles.

Reasoning found the mode; Jev finds the instances.  One request per candidate, same questions,
concurrency 12.  Routing signal ONLY: a high score does not mean the candidate is wrong, it means
read it next.  Every result is stored HYPOTHESIS_ONLY and never sets a status.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

REPO = Path(__file__).resolve().parent.parent
POOL = REPO / "research" / "pool" / "candidates.json"

QUESTIONS = {
    "degenerate_instance": jev.score(
        "Does this candidate state a claim, a named Prop, or a reduction whose hypotheses allow a "
        "DEGENERATE instance -- a zero value, a unit, a base equal to 1, an empty index range, or a "
        "trivial solution -- that would make the statement false as written? Judge only whether such "
        "an instance is admitted by the stated hypotheses, not whether the intended mathematics is "
        "correct.",
        [
            "level 0: the candidate states no universally quantified claim at all, or every variable is explicitly bounded away from degenerate values",
            "level 1: it states a quantified claim and the hypotheses visibly exclude zero, units and trivial cases",
            "level 2: it states a quantified claim and whether degenerate values are excluded cannot be determined from the text",
            "level 3: the hypotheses as written admit a zero, a unit, a base of 1, or an empty range under which the claim is false",
        ],
    ),
    "vacuous_downstream": jev.score(
        "Does this candidate record a conclusion that DEPENDS on an assumed statement, such that if "
        "the assumed statement were false the conclusion would be vacuously true rather than wrong? "
        "The danger is a chain that still compiles and still looks green while carrying no content.",
        [
            "level 0: the candidate's conclusion is proved outright with no assumed statement",
            "level 1: it depends on an assumed statement and explicitly says so, naming it",
            "level 2: it depends on an assumed statement but the dependency is not clearly flagged",
            "level 3: it presents a conclusion as established while the assumed statement it rests on is itself unverified and not named",
        ],
    ),
    "search_is_vacuous": jev.noul(
        "Does this candidate report a finite or bounded search that found NOTHING, without any "
        "control demonstrating the search would have found something had it been there?",
        true="it reports an empty search result with no positive control, no witness, and no demonstration that the search space was non-empty",
        false="it reports no search, or it reports one together with a control, a witness, or an explicit non-vacuity check",
    ),
    "next_action": jev.choice(
        "Given the failure mode described, what should be done with this candidate next?",
        {
            "countersearch_now": "its stated hypotheses plausibly admit a degenerate counterexample and something load-bearing depends on it",
            "add_control": "its evidence is an empty search that needs a non-vacuity control before it can be relied on",
            "restate_hypotheses": "its claim is probably true but stated too loosely to be provable as written",
            "no_action": "it is a log, a refuted entry, or otherwise carries no claim that could exhibit this mode",
        },
    ),
}

CONTEXT = {
    "conjecture": "Beal: A^x + B^y = C^z with x,y,z >= 3 and gcd(A,B,C) = 1 has no solutions.",
    "failure_mode": "U322: the Prop `EulerDescentStep`, recorded one cycle earlier as the residual gap "
                    "of the (3,4,4) chain, was FALSE as stated -- `IsCoprime p q -> p*(p^2+3q^2) = c^3 "
                    "-> q = 0` is refuted by p = 0, q = 1, c = 0, since IsCoprime 0 1 holds in Z and "
                    "0*(0+3) = 0^3. The Lean build stayed green throughout, because an implication "
                    "from a false hypothesis is still a theorem and everything downstream compiles. "
                    "The fix was to add p != 0, which the reduction does supply.",
    "second_mode": "A bounded search that finds nothing proves nothing unless a control shows the "
                   "searcher can find a positive instance. U317/U318 and U323 each carry such a "
                   "control; earlier candidates may not.",
}


def summarize(c: dict, limit: int = 4000) -> dict:
    keep = {k: c.get(k) for k in
            ("id", "status", "claim", "method", "evidence", "obligations", "failure_reason")}
    text = json.dumps(keep, indent=1)[:limit]
    return {"candidate": text}


def main() -> int:
    data = json.loads(POOL.read_text())
    cands = data["candidates"] if isinstance(data, dict) and "candidates" in data else data
    if len(sys.argv) > 1:
        wanted = set(sys.argv[1:])
        cands = [c for c in cands if c.get("id") in wanted]
    cands = [c for c in cands if c.get("status") not in ("DUPLICATE",)]
    states = [{**CONTEXT, **summarize(c)} for c in cands]
    print(f"screening {len(cands)} candidates via Jev ...", file=sys.stderr)
    try:
        responses = jev.ask_many(states, QUESTIONS)
    except Exception as e:                       # noqa: BLE001
        print(f"JEV UNREACHABLE: {e}. Degradation logged; reason over the pool instead.",
              file=sys.stderr)
        return 2
    rows = []
    for c, st, resp in zip(cands, states, responses):
        if "error" in resp:
            print(f"  ! {c.get('id')}: {resp['error']}", file=sys.stderr)
            continue
        jev.persist(f"vacuity_{c.get('id')}", st, QUESTIONS, resp)
        a = resp["answers"]
        rows.append({
            "id": c.get("id"),
            "status": c.get("status"),
            "degenerate": round(a["degenerate_instance"]["score"], 2),
            "vacuous_downstream": round(a["vacuous_downstream"]["score"], 2),
            "empty_search": round(a["search_is_vacuous"]["noul"], 2),
            "action": a["next_action"]["choice"],
            "conf": round(a["next_action"]["confidence"], 2),
        })
    rows.sort(key=lambda r: -(r["degenerate"] + r["vacuous_downstream"] + r["empty_search"]))
    print(json.dumps({"state": "HYPOTHESIS_ONLY",
                      "note": "routing signal only; a high score means read it next, never that it is wrong",
                      "screen": rows}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
