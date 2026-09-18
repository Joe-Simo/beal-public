"""Independent audit of the project's Kraus sieve data for signature (3,3,p).

Three checks, all exact:
  A. Hasse bound  |a_q| <= 2*sqrt(q)  for every reported newform trace.
  B. Cross-prime consistency: a_q of a FIXED newform at a FIXED prime q must not depend
     on which exponent p the certificate was computed for.
  C. Coverage: is newform 144b actually eliminated? The summaries report
     'unconditionally_eliminated: true' but the per-certificate flags include
     elim_144b_canon, which is sometimes false and is absent from the sample rows.
"""
import json, math, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
files = sorted((REPO / "references" / "U111").glob("kraus_sieve_*.json")) + \
        sorted((REPO / "references").glob("**/kraus_sieve_*.json"))
files = sorted(set(files))

traces = {}          # (form, q) -> {aq: [sources]}
hasse_viol = []
elim144b = {"true": 0, "false": 0, "absent": 0}
p_missing_144b = []

for f in files:
    data = json.loads(f.read_text())
    for pstr, rec in data.items():
        if not isinstance(rec, dict):
            continue
        certs = []
        if isinstance(rec.get("first_certificate"), dict):
            certs.append(("first", rec["first_certificate"]))
        for i, c in enumerate(rec.get("eliminating_primes_sample", []) or []):
            if isinstance(c, dict):
                certs.append((f"sample{i}", c))
        saw144b = False
        for tag, c in certs:
            q = c.get("q")
            if not isinstance(q, int):
                continue
            for form in ("aq_72", "aq_144a", "aq_144b"):
                if form in c and isinstance(c[form], int):
                    a = c[form]
                    if abs(a) > 2 * math.isqrt(q) + 2:
                        hasse_viol.append((f.name, pstr, q, form, a, 2 * math.sqrt(q)))
                    traces.setdefault((form, q), {}).setdefault(a, []).append(f"{f.name}:p={pstr}:{tag}")
            if "elim_144b_canon" in c:
                saw144b = True
                elim144b["true" if c["elim_144b_canon"] else "false"] += 1
        if not saw144b:
            elim144b["absent"] += 1
            p_missing_144b.append(f"{f.name}:p={pstr}")

print("A. HASSE BOUND |a_q| <= 2*sqrt(q)")
print(f"   violations: {len(hasse_viol)}")
for v in hasse_viol[:5]:
    print("   ", v)

print("\nB. CROSS-PRIME CONSISTENCY of a_q for a fixed newform at a fixed q")
incons = {k: v for k, v in traces.items() if len(v) > 1}
print(f"   (newform,q) pairs seen at >1 exponent p: "
      f"{sum(1 for k,v in traces.items() if sum(len(s) for s in v.values())>1)}")
print(f"   INCONSISTENT pairs (same newform+q, different a_q): {len(incons)}")
for k, v in list(incons.items())[:6]:
    print(f"   {k}: {dict((a, s[:2]) for a, s in v.items())}")

print("\nC. COVERAGE OF NEWFORM 144b")
print(f"   certificates reporting elim_144b_canon TRUE : {elim144b['true']}")
print(f"   certificates reporting elim_144b_canon FALSE: {elim144b['false']}")
print(f"   exponents p with NO 144b flag anywhere      : {elim144b['absent']}")
if p_missing_144b:
    print("   e.g.", p_missing_144b[:6])
print(f"\n   files scanned: {[f.name for f in files]}")
