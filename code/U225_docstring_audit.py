"""U225 — Jev screen #3: docstring/comment OVERCLAIM audit on the seven files flagged in U223.
One narrow question per artifact: does a docstring assert a family/signature/unconditionality that the
theorem below it does not deliver? Each hit is then verified by reading the theorem statement."""
import json,sys
sys.path.insert(0,'code'); import jev
FILES=["AlgebraicIdentities","KnownSolutions","Taxonomy","TaxonomyExtensions","FermatCatalan","GaussianObstruction","Signature3","ClosedFamilies","MordellFixedBase","FixedBasesExample"]
CTX=("Beal repo. Recurring defect: a docstring says a theorem closes a SIGNATURE FAMILY or is UNCONDITIONAL, "
 "while the theorem below takes named hypotheses (published theorems stated as Props) or covers a strictly "
 "smaller family. A theorem that takes a named hypothesis is CONDITIONAL and its docstring must say so. "
 "A file-level header that says 'no sorry, no custom axioms' is a factual claim about the build.")
Q={"family_overclaim":jev.noul("Does a docstring name a signature or family (e.g. '(p,4,4)', 'all r', 'every prime p') that the theorem statement directly below it does NOT actually quantify over?",true="docstring names a bigger family",false="docstring matches the statement"),
 "conditional_unmarked":jev.noul("Does a docstring present a result as unconditional/closed while the theorem takes a named-hypothesis argument (a Prop standing for a published theorem)?",true="conditional but presented as closed",false="conditionality is stated"),
 "header_build_claim":jev.noul("Does the file header assert 'no sorry, no custom axioms' or similar about itself?",true="asserts a build property",false="no such assertion")}
reqs=[{"context":CTX,"filename":f,"lean_source":open('formal/Beal/%s.lean'%f).read()[:15000]} for f in FILES]
rs=jev.ask_many(reqs,Q,concurrency=10)
rows=[]
for f,r in zip(FILES,rs):
    if 'answers' not in r: print("ERR",f); continue
    a={k:round(v['noul'],2) for k,v in r['answers'].items()}
    rows.append((round(max(a['family_overclaim'],a['conditional_unmarked']),2),a,f))
rows.sort(key=lambda r:-r[0])
json.dump({"status":"HYPOTHESIS_ONLY","rows":rows},open('research/pool/evidence/docstring_audit_U225.json','w'),indent=1)
for s,a,f in rows: print(s,f,a)
