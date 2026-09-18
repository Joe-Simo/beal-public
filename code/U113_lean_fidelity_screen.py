"""Jev screen over the Lean files: does each formal statement faithfully encode the
ORIGINAL Beal statement, and how much of its content is axiom rather than proof?

A compiling file that proves the wrong statement is worthless, so statement fidelity is
the thing to screen for. Narrow questions, one request per Lean file.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

FORMAL = Path(__file__).resolve().parent.parent / "formal"

TARGET = ("Beal: for positive integers A,B,C,x,y,z with A^x + B^y = C^z and x,y,z >= 3, "
          "the bases A,B,C share a common prime factor, i.e. gcd(gcd(A,B),C) > 1. "
          "A counterexample needs: all six positive integers, all three exponents at least 3, "
          "exact equality, and gcd(gcd(A,B),C) = 1. Bases equal to 1 are allowed. "
          "Exponent 2 is NOT allowed. The condition is on the BASES, not the exponents.")

QUESTIONS = {
    "fidelity": jev.score(
        "Does this Lean file's formal definition of a Beal counterexample, or of the statement it "
        "proves, faithfully encode the original conjecture as described in the target statement? "
        "Check in particular: all six values positive integers; all three exponents at least 3 and "
        "not 2; the common-factor condition placed on the BASES rather than the exponents; a base "
        "equal to 1 not excluded; the equality exact.",
        [
            "level 0: the file states no Beal-specific statement, for example it is a helper or arithmetic file",
            "level 1: it states a Beal-related statement that DEVIATES from the target, for example allowing exponent 2, excluding base 1, or putting the gcd condition on the exponents",
            "level 2: it states a Beal-related statement that appears faithful but restricts to a sub-case without saying so in the statement itself",
            "level 3: it states a Beal-related statement that matches the target exactly, or a clearly labelled sub-case of it",
        ],
    ),
    "axiom_load": jev.score(
        "How much of this file's mathematical content is asserted as a custom axiom or left as "
        "sorry, rather than proved from mathlib?",
        [
            "level 0: no axiom and no sorry; everything is proved or is a definition",
            "level 1: contains sorry or axioms only for elementary facts that a standard library would already provide",
            "level 2: contains a small number of axioms asserting named external theorems, clearly labelled as such",
            "level 3: the file's substantive conclusions rest on custom axioms that assert precisely what would otherwise need proving",
        ],
    ),
    "vacuous_risk": jev.noul(
        "Is there a risk that a theorem in this file is VACUOUS or trivially true - for instance "
        "because its hypotheses can never be satisfied, because it is derived from an axiom that "
        "already asserts the conclusion, or because the quantifiers make it say less than intended?",
        true="a theorem here is derived almost immediately from an axiom asserting the same thing, or has hypotheses that may be unsatisfiable, so that proving it establishes nothing new",
        false="the theorems here have genuine content derived from definitions and library lemmas",
    ),
}


def main() -> int:
    paths = sorted(FORMAL.rglob("*.lean"))
    states = [{"target_statement": TARGET, "file": p.name,
               "source": p.read_text(errors="replace")[:6000]} for p in paths]
    print(f"screening {len(paths)} Lean files ...", file=sys.stderr)
    resps = jev.ask_many(states, QUESTIONS)
    rows = []
    for p, st, r in zip(paths, states, resps):
        if "error" in r:
            print(f"  ! {p.name}: {r['error']}", file=sys.stderr)
            continue
        jev.persist(f"lean_{p.stem}", st, QUESTIONS, r)
        a = r["answers"]
        rows.append({"file": p.name,
                     "fidelity": round(a["fidelity"]["score"], 2),
                     "axiom_load": round(a["axiom_load"]["score"], 2),
                     "vacuous_risk": round(a["vacuous_risk"]["noul"], 2)})
    rows.sort(key=lambda r: (r["fidelity"], -r["axiom_load"]))
    print(json.dumps({"state": "HYPOTHESIS_ONLY", "rows": rows}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
