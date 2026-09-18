"""U246 — Jev overclaim screen across the milestone scripts, using the defect pattern found in C110:
a script computes something TRUE but narrow, and its title/commit message asserts something much wider.
Narrow questions only. Top hits get read by hand."""
import re,json,sys,os
sys.path.insert(0,'code'); import jev
src=open('code/verify_all_milestones.py').read()
ms=re.findall(r'\("([^"]+)",\s*\[([^\]]+)\]\)', src)
items=[]
for title,cmd in ms:
    m=re.search(r'"(code/[^"]+)"', cmd)
    if not m: continue
    p=m.group(1)
    if not os.path.exists(p): continue
    items.append((title,p,open(p).read()))
CTX=("Beal repo milestone audit. Known defect pattern (pool C110): a script proves a TRUE but NARROW fact "
 "(e.g. Cartan normalizer orders are prime to p, checked for four primes) while its TITLE asserts something far "
 "wider (\"Universal Serre surjectivity for all signatures\"). Other known traps in this repo: refuting an isogeny "
 "and concluding a RESIDUAL mod-p congruence is impossible; a rank<genus Chabauty bound proved over the wrong field; "
 "Cohen-Lenstra or GRH-conditional bounds relabelled unconditional; and asserting a Frey curve for three INDEPENDENT "
 "exponents, an object that does not exist.")
Q={"title_wider":jev.noul("Does the milestone TITLE assert something strictly wider than what the script actually computes (more primes, all signatures, unconditional, proved rather than checked)?",true="title is wider",false="title matches"),
 "finite_sample":jev.noul("Does the script check a FINITE sample of primes or cases and phrase the conclusion as universal?",true="finite sample, universal wording",false="no such gap"),
 "known_trap":jev.noul("Does it use one of the four named traps: residual/isogeny conflation, Chabauty over the wrong field, heuristic or GRH laundering, or a Frey curve for three independent exponents?",true="uses a named trap",false="no named trap")}
reqs=[{"context":CTX,"milestone_title":t,"script_path":p,"script_source":s[:12000]} for t,p,s in items]
rs=jev.ask_many(reqs,Q,concurrency=12)
rows=[]
for (t,p,_),r in zip(items,rs):
    if 'answers' not in r: continue
    a={k:round(v['noul'],2) for k,v in r['answers'].items()}
    rows.append((round(max(a.values()),2),a,t[:70],p))
rows.sort(key=lambda r:-r[0])
json.dump({"status":"HYPOTHESIS_ONLY","rows":rows},open('research/pool/evidence/milestone_overclaim_U246.json','w'),indent=1)
print("milestones screened:",len(rows))
for s,a,t,p in rows[:12]: print(s,a,"|",t)
