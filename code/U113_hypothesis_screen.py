"""Jev screen: which checkpoints present a result as unconditional while depending on a
named unproved hypothesis? Narrow noul questions, one request per checkpoint.

Motivated by U110, which rules out 2-torsion "with Cohen-Martinet probability P < 2^-64",
assumes finiteness of Sha for a Cassels-Tate parity argument, and then labels the resulting
rank bounds "100% UNCONDITIONAL (removing the GRH dependency)".

Routing signal only. A hit means READ IT, not that it is wrong.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

CKPT = Path(__file__).resolve().parent.parent / "research" / "checkpoints"

QUESTIONS = {
    "dep_heuristic": jev.noul(
        "Does this checkpoint rely on a probabilistic or statistical heuristic - such as "
        "Cohen-Lenstra, Cohen-Martinet, a random-matrix model, or an argument that some "
        "event is too improbable to occur - as a step in establishing a mathematical claim?",
        true="a probability, density, expected-value or 'too improbable to happen' argument is used to rule out or establish a case, rather than merely to motivate or to guide a search",
        false="no probabilistic reasoning is used for a mathematical step, or probability appears only as commentary on why a search is likely to succeed",
    ),
    "dep_sha": jev.noul(
        "Does this checkpoint assume the finiteness of the Tate-Shafarevich group Sha, or use a "
        "Cassels-Tate parity argument that requires it, in order to pin down a Mordell-Weil rank?",
        true="finiteness of Sha, or a parity consequence of it, is used to determine or bound a rank",
        false="Sha is not used, or is mentioned only as an acknowledged open obstruction that the argument does not rely on",
    ),
    "dep_grh": jev.noul(
        "Does this checkpoint depend on the Generalized Riemann Hypothesis, or on a class-group or "
        "unit-group computation whose certification requires GRH?",
        true="GRH is assumed, or a class number, class group, or unit index is certified only under GRH",
        false="no GRH dependency, or a GRH-free certification is actually carried out and reported",
    ),
    "claims_unconditional": jev.noul(
        "Does this checkpoint apply the words unconditional, 100% closed, definitive, or complete "
        "resolution to a result?",
        true="such closure language is applied to a mathematical result in this checkpoint",
        false="no such closure language is used, or it is used only to describe other people's published theorems",
    ),
    "mismatch": jev.score(
        "Consider the gap between how strongly this checkpoint states its conclusions and what its "
        "arguments actually establish. A checkpoint that assumes an unproved hypothesis and then "
        "calls the result unconditional has a large gap; one that states its dependencies plainly "
        "has none.",
        [
            "level 0: every conclusion is stated with its actual dependencies and no closure language is misapplied",
            "level 1: conclusions are slightly stronger than the arguments, for instance an unstated appeal to another checkpoint",
            "level 2: a result depending on an unproved hypothesis or an unverified external citation is described without that condition",
            "level 3: a result is explicitly called unconditional or 100% closed while the checkpoint itself uses a heuristic, an unproved hypothesis such as finiteness of Sha, or GRH",
        ],
    ),
}


def main() -> int:
    paths = sorted(CKPT.glob("*.md"))
    states = [{"checkpoint": p.name, "excerpt": p.read_text(errors="replace")[:5000]} for p in paths]
    print(f"screening {len(paths)} checkpoints for hidden hypotheses ...", file=sys.stderr)
    resps = jev.ask_many(states, QUESTIONS)
    rows = []
    for p, st, r in zip(paths, states, resps):
        if "error" in r:
            continue
        jev.persist(f"hyp_{p.stem}", st, QUESTIONS, r)
        a = r["answers"]
        rows.append({"file": p.name,
                     "heur": round(a["dep_heuristic"]["noul"], 2),
                     "sha": round(a["dep_sha"]["noul"], 2),
                     "grh": round(a["dep_grh"]["noul"], 2),
                     "uncond": round(a["claims_unconditional"]["noul"], 2),
                     "mismatch": round(a["mismatch"]["score"], 2)})
    rows.sort(key=lambda r: -r["mismatch"])
    print(json.dumps({"state": "HYPOTHESIS_ONLY", "rows": rows}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
