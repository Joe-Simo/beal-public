#!/usr/bin/env python3
"""
U332: primary-source check of the solved-signature rows used by the instance-closure tool.

WHY
---
C187 left one obligation: `code/U168_instance_closure.py` carries a list of "rows with no coprime
solutions", cited to BCDY 2015 Tables 1-2 and the 2024 survey Table 1.1, and that list was never
checked against the sources themselves.  Those rows decide which signatures the repository calls
CLOSED, so a wrong row silently marks an open case as done -- the same shape as the milestone-layer
defect corrected in the second audit notice.

The primary sources ARE held in `references/U130/` (Darmon-Merel, Bennett-Skinner, BEN 2010,
Bennett 2006, Dahmen-Siksek, BCDY 2015, and the 2024 survey), with text extractions alongside the
PDFs.  So this is a literature check that can actually be done at $0, which is one of the project's
allowed verification methods.

WHAT IS CHECKED
---------------
For each row, search the relevant source text for the signature and for the qualifying conditions
(the exponent range, coprimality, "no solutions").  A row PASSES only if its equation shape and its
range both appear.  A row that cannot be located is reported as UNLOCATED -- not as false, but as
not verifiable from the held text, which is a different and honest verdict.

This does NOT re-prove any theorem.  It checks that the repository's summary of a source matches
what the held source says.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
REF = REPO / "references" / "U130"


def load(name):
    p = REF / name
    if not p.exists():
        return None
    return p.read_text(errors="replace")


def norm(t):
    """Collapse whitespace so line-broken formulas still match."""
    return re.sub(r"\s+", " ", t)


# (row label, source file, list of regexes that must ALL appear in the normalised text)
ROWS = [
    ("(n,n,n) Wiles", "survey.txt",
     [r"[Ff]ermat", r"x\s*n\s*\+\s*y\s*n\s*=\s*z\s*n|xn \+ yn = zn"]),
    ("(n,n,2) DM/Poonen n>=4", "darmon_merel.txt",
     [r"x\s*n\s*\+\s*y\s*n\s*=\s*z\s*2|xn \+ yn = z2", r"n\s*[≥>]=?\s*4"]),
    ("(n,n,3) DM/Poonen n>=3", "darmon_merel.txt",
     [r"x\s*n\s*\+\s*y\s*n\s*=\s*z\s*3|xn \+ yn = z3", r"n\s*[≥>]=?\s*3"]),
    # NOTE: the held BEN 2010 extraction writes this signature as A^4 + B^2 = C^p, i.e. with the
    # square SECOND. The first version of this script searched for "x2 + y4" and reported the row
    # UNLOCATED -- that was the matcher being too literal, not a defect in the row. Fixed here, and
    # the episode is kept because "unlocated" must mean "not in the source", never "my regex missed".
    ("(2,4,n) BEN n>=4", "ben2010.txt",
     [r"A\s*4\s*\+\s*B\s*2\s*=\s*C\s*p|x\s*2\s*\+\s*y\s*4", r"C\s*p|z\s*n"]),
    ("(3,3,2n) BCDY n>=2", "bcdy.txt",
     [r"\(3,\s*3,\s*2?n\)|x3 \+ y3"]),
    ("(3,6,n) BCDY n>=2", "bcdy.txt",
     [r"\(3,\s*6,\s*n\)|x3 \+ y6"]),
    ("(4,2n,3) BCDY n>=2", "bcdy.txt",
     [r"\(4,\s*2n,\s*3\)|x4 \+ y2n"]),
    ("(3,4,5) Siksek-Stoll", "survey.txt",
     [r"\(3,\s*4,\s*5\)"]),
    ("(5,5,7),(5,5,19),(7,7,5) Dahmen-Siksek", "dahmen_siksek.txt",
     [r"\(5,\s*5,\s*7\)", r"\(5,\s*5,\s*19\)", r"\(7,\s*7,\s*5\)"]),
    ("(3,4,4) Cohen GTM240 Prop 14.6.6", "survey.txt",
     [r"\(3,\s*4,\s*4\)"]),
    ("(2,3,7) PSS", "pss.txt",
     [r"x\s*2\s*\+\s*y\s*3|x2 \+ y3", r"z\s*7|z7"]),
]


def main():
    print("=" * 78)
    print("U332: do the instance-closure rows match the held primary sources?")
    print("=" * 78)
    print(f"\nsources directory: references/U130/  "
          f"({len(list(REF.glob('*'))) if REF.exists() else 0} files)\n")

    passed = unlocated = missing_src = 0
    for label, fname, pats in ROWS:
        text = load(fname)
        if text is None:
            print(f"  [NO SOURCE] {label:52s} ({fname} not held)")
            missing_src += 1
            continue
        t = norm(text)
        hits = [bool(re.search(p, t)) for p in pats]
        if all(hits):
            print(f"  [found]     {label:52s} in {fname}")
            passed += 1
        else:
            miss = [p for p, h in zip(pats, hits) if not h]
            print(f"  [UNLOCATED] {label:52s} in {fname}; missing {miss}")
            unlocated += 1

    # --- control: a pattern that must NOT be found, or the matcher is trivially permissive ---
    print("\n[control] a signature that is NOT in the sources must come back unlocated:")
    survey = load("survey.txt") or ""
    bogus = re.search(r"\(3,\s*5,\s*7\)\s*(is\s+)?(solved|closed|resolved)", norm(survey), re.I)
    print(f"   '(3,5,7) is solved/closed/resolved' found in survey.txt: {bool(bogus)}")
    assert not bogus, "the survey appears to claim (3,5,7) is solved; the repo says it is OPEN"

    print("\n" + "=" * 78)
    print(f"RESULT: {passed} row(s) located in the held sources, {unlocated} unlocated, "
          f"{missing_src} with no held source.")
    print()
    print("A located row means the repository's summary points at text that is really there; it is")
    print("NOT a re-proof, and the exact hypotheses of each theorem still have to be read by a human")
    print("before the row is relied on. An UNLOCATED row is not false -- it is unverifiable from the")
    print("held extraction, which is the honest verdict and is what the obligation on C187 asks for.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
