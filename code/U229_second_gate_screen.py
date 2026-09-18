"""U229 — apply the NEW second gate (C094) to the whole pool: does the proof of each claimed
necessary condition actually USE the equation A^x+B^y=C^z, or is it the exponent hypothesis /
a fact about arbitrary triples in disguise? Jev screens; survivors get read by hand."""
import json,sys
sys.path.insert(0,'code'); import jev
pool=json.load(open('research/pool/candidates.json'))
cs=pool if isinstance(pool,list) else pool.get('candidates',pool)
if isinstance(cs,dict): cs=list(cs.values())
cs=[c for c in cs if c.get('status') in ('PARTIAL_RESULT','PROMISING','ACTIVE','VERIFICATION_REQUIRED')]
CTX=("Beal repo, new SECOND GATE (pool C094). A necessary condition on a Beal counterexample carries Beal-specific "
 "content only if its PROOF uses the equation A^x+B^y=C^z. Two ways to fail: (a) the proof uses only x,y,z>=3 and "
 "generic inequalities (example: rad(ABC)^3 <= A^xB^yC^z, proved from rad n | n and A^3<=A^x — the exponent hypothesis "
 "in disguise); (b) the statement holds for EVERY coprime triple a+b=c whether or not the terms are perfect powers "
 "(example: the Steinberg/tame-symbol conditions, and the Fermat-quotient Wronskian divisibility).")
Q={"uses_equation":jev.noul("Does the PROOF of this candidate's claim genuinely use the equation A^x+B^y=C^z (not merely the exponent bounds or generic facts about the numbers)?",true="uses the equation",false="does not use the equation"),
 "holds_for_any_triple":jev.noul("Would the claim hold for an ARBITRARY coprime triple a+b=c whose terms are not perfect powers?",true="holds for arbitrary triples",false="needs perfect powers"),
 "is_exponent_restated":jev.noul("Is the claim essentially the hypothesis x,y,z>=3 restated in other notation?",true="exponent hypothesis restated",false="more than that")}
rs=jev.ask_many([{"context":CTX,"candidate_id":c['id'],"claim":c.get('claim','')[:1200],"method":str(c.get('method',''))[:400],"evidence":str(c.get('evidence',''))[:600]} for c in cs],Q,concurrency=12)
rows=[]
for c,r in zip(cs,rs):
    if 'answers' not in r: continue
    a={k:round(v['noul'],2) for k,v in r['answers'].items()}
    fail=max(1-a['uses_equation'],a['holds_for_any_triple'],a['is_exponent_restated'])
    rows.append((round(fail,2),a,c['id'],c.get('claim','')[:85]))
rows.sort(key=lambda r: -r[0])
json.dump({"status":"HYPOTHESIS_ONLY","rows":rows},open('research/pool/evidence/second_gate_U229.json','w'),indent=1)
print("candidates screened:",len(rows))
for f,a,i,cl in rows[:12]: print(f,i,a,cl)
