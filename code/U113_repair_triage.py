"""Jev triage: which broken Lean modules are worth repairing, and in what order?"""
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

FORMAL = Path(__file__).resolve().parent.parent / "formal"
BROKEN = ["CounterexampleChecker", "KnownSolutions", "SquarefreeCore", "Taxonomy",
          "TaxonomyExtensions", "Signature3", "Signature4", "Signature238", "Mihailescu"]

CONTEXT = ("Beal project. Already kernel-verified and axiom-free: Beal.Conjecture (the statement), "
           "Beal.AlgebraicIdentities, Beal.ExponentReduction (exponent reduction + the diagonal "
           "family (n,n,n) with 4|n via mathlib fermatLastTheoremFour), Beal.Structure (pairwise "
           "coprimality of the bases, no counterexample with A=B). mathlib v4.14.0 provides "
           "fermatLastTheoremFour but NOT a complete FLT for exponent 3, and provides NO "
           "Catalan/Mihailescu theorem. Custom axioms are not acceptable in a verified chain.")

Q = {
    "repair_value": jev.score(
        "If this module were repaired so that it compiles with no sorry and no custom axioms, how "
        "much genuine mathematical content would the project gain?",
        [
            "level 0: nothing; its content is already covered by an existing verified module, or it only restates definitions",
            "level 1: convenience definitions or a taxonomy with no theorem of independent value",
            "level 2: a self-contained elementary theorem or an executable checker with real content",
            "level 3: it would close a signature or an infinite family of Beal signatures",
        ],
    ),
    "repairable_without_axioms": jev.noul(
        "Can this module plausibly be repaired to compile with NO custom axioms and NO sorry, using "
        "only mathlib as it actually exists - noting that mathlib has FLT for exponent 4 but not for "
        "exponent 3, and has no Catalan/Mihailescu theorem?",
        true="its content is elementary or depends only on results mathlib actually contains",
        false="its substance depends on a deep theorem mathlib does not contain, such as FLT3, Mihailescu, or a modular-method elimination, so it would need a custom axiom",
    ),
    "statement_risk": jev.noul(
        "Is there a risk that this module's THEOREM STATEMENTS misencode the Beal conjecture - for "
        "example allowing exponent 2, excluding a base of 1, or putting the coprimality condition on "
        "the exponents rather than the bases - so that repairing it would certify the wrong thing?",
        true="its statements look like they may deviate from the exact conjecture, or it restricts to a sub-case without saying so",
        false="its statements appear to encode the conjecture or a clearly labelled sub-case faithfully",
    ),
}


def main() -> int:
    states = []
    for m in BROKEN:
        p = FORMAL / "Beal" / f"{m}.lean"
        err = subprocess.run(
            ["lake", "build", f"Beal.{m}"], cwd=FORMAL, capture_output=True, text=True,
            env={**__import__("os").environ,
                 "PATH": str(Path.home() / ".elan/bin") + ":" + __import__("os").environ["PATH"]},
            timeout=100)
        errs = "\n".join(l for l in (err.stdout + err.stderr).splitlines()
                         if l.startswith("error:"))[:1500]
        states.append({"context": CONTEXT, "module": m,
                       "source": p.read_text(errors="replace")[:5000],
                       "compiler_errors": errs})
    resps = jev.ask_many(states, Q, concurrency=9)
    rows = []
    for m, st, r in zip(BROKEN, states, resps):
        if "error" in r:
            print(f"! {m}: {r['error']}", file=sys.stderr); continue
        jev.persist(f"repair_{m}", st, Q, r)
        a = r["answers"]
        rows.append({"module": m, "value": round(a["repair_value"]["score"], 2),
                     "repairable": round(a["repairable_without_axioms"]["noul"], 2),
                     "stmt_risk": round(a["statement_risk"]["noul"], 2)})
    rows.sort(key=lambda r: -(r["value"] * r["repairable"]))
    print(f"{'value':>6}{'repair':>8}{'risk':>6}  module")
    for r in rows:
        print(f"{r['value']:>6}{r['repairable']:>8}{r['stmt_risk']:>6}  {r['module']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
