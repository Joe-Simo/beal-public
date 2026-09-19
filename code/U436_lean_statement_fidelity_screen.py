"""U436: High-throughput Jev Statement Fidelity Screen over every Lean 4 file.
Screens for target-discipline fidelity traps:
- Exponent range: does any theorem or definition admit exponent < 3?
- Base 1: does any statement exclude base 1 without justification?
- Coprimality: does any statement silently assume pairwise coprimality when triple gcd = 1 is given?
- Axioms: does any file introduce custom axioms rather than standard axioms or named Props?
- Docstring gaps: does any docstring overclaim relative to the formal theorem statement?
"""
from __future__ import annotations
import glob
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

REPO = Path(__file__).resolve().parent.parent
LEAN_DIR = REPO / "formal" / "Beal"
EVIDENCE_DIR = REPO / "research" / "pool" / "evidence"

CTX = (
    "Beal's conjecture: for POSITIVE integers A, B, C, x, y, z with A^x + B^y = C^z and x, y, z >= 3, "
    "gcd(gcd(A, B), C) > 1. Known fidelity traps in this repo: silently requiring exponent >= 2 instead of >= 3; "
    "excluding base 1; assuming A, B, C pairwise coprime when only gcd(gcd(A, B), C) = 1 is given; proving a statement "
    "about a DIFFERENT equation (generalized Fermat a x^p + b y^q = c z^r) and calling it Beal; stating a hypothesis as an "
    "`axiom` rather than a `def ... : Prop` named hypothesis; a theorem whose conclusion is weaker than its docstring claims."
)

QUESTIONS = {
    "exp_range": jev.noul(
        "Does any theorem or definition in this file admit an exponent equal to 2 (or fail to require x,y,z>=3) where the docstring claims a Beal statement?",
        true="exponent range wrong or unstated",
        false="exponent range correct",
    ),
    "base_one": jev.noul(
        "Does any statement exclude the base value 1, or assume bases >1 without saying so?",
        true="excludes base 1",
        false="base 1 allowed",
    ),
    "coprime_swap": jev.noul(
        "Does any statement assume A,B,C pairwise coprime, or assume gcd(A,B)=1, where the conjecture only gives gcd(gcd(A,B),C)=1?",
        true="coprimity assumption stronger than Beal",
        false="coprimity matches",
    ),
    "axiom_used": jev.noul(
        "Does the file declare a Lean `axiom` (as opposed to a `def ... : Prop` named hypothesis)?",
        true="declares an axiom",
        false="no axiom",
    ),
    "docstring_gap": jev.noul(
        "Does a docstring or comment claim MORE than the theorem statement below it actually proves?",
        true="docstring overclaims",
        false="docstring matches",
    ),
}

def main():
    print("================================================================================")
    print("      U436: JEV STATEMENT FIDELITY SCREEN OVER ALL LEAN 4 FORMAL PROOFS         ")
    print("================================================================================")
    files = sorted(list(LEAN_DIR.glob("*.lean")))
    states = []
    names = []
    for f in files:
        names.append(f.name)
        content = f.read_text()[:12000]
        state = f"File: {f.name}\nContext: {CTX}\nLean Source Code Excerpt:\n{content}"
        states.append(state)

    results = jev.ask_many(states, QUESTIONS, concurrency=12)
    rows = []
    for name, state, resp in zip(names, states, results):
        if "error" in resp:
            print(f"[{name}] ERROR: {resp['error']}")
            continue
        ans = resp.get("answers", {})
        scores = {}
        for qname, qans in ans.items():
            val = qans.get("value")
            conf = qans.get("confidence")
            scores[qname] = val
        print(f"[{name:25s}] exp_range: {scores.get('exp_range')} | base_1: {scores.get('base_one')} | coprime: {scores.get('coprime_swap')} | axiom: {scores.get('axiom_used')} | doc_gap: {scores.get('docstring_gap')}")
        jev.persist(f"fidelity_{name}", state, QUESTIONS, resp)
        rows.append({"file": name, "scores": scores})

    out_file = EVIDENCE_DIR / "U436_fidelity_screen_summary.json"
    with open(out_file, "w") as f:
        json.dump({"status": "HYPOTHESIS_ONLY", "rows": rows}, f, indent=2)
    print("================================================================================")
    print(f"Fidelity screen completed across {len(files)} Lean files and saved to {out_file.name}!")
    print("================================================================================")

if __name__ == "__main__":
    main()
