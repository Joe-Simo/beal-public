"""U217 — Jev routing: which BLOCKED/PARTIAL candidates are affected by C086 (Z[i] failure is a single trace identity tied to ramified 2)?"""
import json,sys
sys.path.insert(0,'code'); import jev
pool=json.load(open('research/pool/candidates.json')); cs=pool if isinstance(pool,list) else pool.get('candidates',pool)
if isinstance(cs,dict): cs=list(cs.values())
cs=[c for c in cs if c.get('status') in('BLOCKED','PARTIAL_RESULT','PROMISING','ACTIVE')]
FACT="New fact C086: over Z[i], within bases |re|,|im|<=14 and exponents 3..7, the ONLY coprime solution of a^x+b^y=c^z is w^3+conj(w)^3=(1+i)^4 (w=-2+i): a trace identity depending on 2=unit*(1+i)^2."
Q={"unblocks":jev.noul("Does this new fact remove or weaken the specific obstacle that blocks this candidate?",true="weakens the blocker",false="irrelevant to the blocker"),
   "two_adic":jev.noul("Does the candidate's method treat the prime 2 (or the parity of the bases) as a special case?",true="2 is special in it",false="2 not special")}
rs=jev.ask_many([{"fact":FACT,"candidate":c.get('claim','')[:900],"blocker":str(c.get('failure_reason') or c.get('open_obligations') or '')[:500]} for c in cs],Q,concurrency=12)
rows=sorted([(round(r['answers']['unblocks']['noul'],2),round(r['answers']['two_adic']['noul'],2),c['id'],c['claim'][:90]) for c,r in zip(cs,rs) if 'answers' in r],reverse=True)
json.dump({"status":"HYPOTHESIS_ONLY","rows":rows},open('research/pool/evidence/route_after_c086_U217.json','w'),indent=1)
for r in rows[:8]: print(r)
