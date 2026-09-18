"""U223 — COUNTERSEARCH: Jev statement-fidelity screen over every Lean file (CLAUDE.md lists this as a cheap
Jev decision that was being skipped). Narrow, concrete questions only. HYPOTHESIS_ONLY routing."""
import glob,json,sys
sys.path.insert(0,'code'); import jev
files=sorted(glob.glob('formal/Beal/*.lean'))
CTX=("Beal's conjecture: for POSITIVE integers A,B,C,x,y,z with A^x+B^y=C^z and x,y,z>=3, gcd(gcd(A,B),C)>1. "
 "Known fidelity traps in this repo: silently requiring exponent>=2 instead of >=3; excluding base 1; assuming "
 "A,B,C pairwise coprime when only gcd(gcd(A,B),C)=1 is given; proving a statement about a DIFFERENT equation "
 "(generalized Fermat a x^p+b y^q=c z^r) and calling it Beal; stating a hypothesis as an `axiom` rather than a "
 "named Prop; a theorem whose conclusion is weaker than its docstring claims.")
Q={"exp_range":jev.noul("Does any theorem or definition in this file admit an exponent equal to 2 (or fail to require x,y,z>=3) where the docstring claims a Beal statement?",true="exponent range wrong or unstated",false="exponent range correct"),
 "base_one":jev.noul("Does any statement exclude the base value 1, or assume bases >1 without saying so?",true="excludes base 1",false="base 1 allowed"),
 "coprime_swap":jev.noul("Does any statement assume A,B,C pairwise coprime, or assume gcd(A,B)=1, where the conjecture only gives gcd(gcd(A,B),C)=1?",true="coprimity assumption stronger than Beal",false="coprimity matches"),
 "axiom_used":jev.noul("Does the file declare a Lean `axiom` (as opposed to a `def ... : Prop` named hypothesis)?",true="declares an axiom",false="no axiom"),
 "docstring_gap":jev.noul("Does a docstring or comment claim MORE than the theorem statement below it actually proves (e.g. claims a signature family the theorem does not cover)?",true="docstring overclaims",false="docstring matches")}
reqs=[{"context":CTX,"filename":f,"lean_source":open(f).read()[:14000]} for f in files]
rs=jev.ask_many(reqs,Q,concurrency=12)
rows=[]
for f,r in zip(files,rs):
    if 'answers' not in r: print("ERR",f,r.get('error')); continue
    a={k:round(v['noul'],2) for k,v in r['answers'].items()}
    rows.append((round(max(a.values()),2),a,f))
rows.sort(key=lambda r:-r[0])
json.dump({"status":"HYPOTHESIS_ONLY","rows":rows},open('research/pool/evidence/fidelity_screen_U223.json','w'),indent=1)
for s,a,f in rows:
    flag=[k for k,v in a.items() if v>=0.5]
    print(s,f.split('/')[-1],flag if flag else '')
