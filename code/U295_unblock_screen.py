"""U295 — routing screen over the BLOCKED candidates: does anything established this session
change their blocker? New facts available: the rigidity obstruction (rank <= 2; budget 2n+2;
exponents 3,4,6 over Q; degree phi(lcm)/2; at most two exponents at rank >= 3), the classical
Frey limit (only the pairs (2,3) and (n,n)), the descent scope (needs two EQUAL exponents), the
(3,4,4) chain (FLT3 closes same parity; 3|gcd is empty; survivor = elliptic Chabauty on
y^2=x^3-972), and the two gates."""
import json,sys
sys.path.insert(0,'code'); import jev
pool=json.load(open('research/pool/candidates.json'))
cs=pool if isinstance(pool,list) else pool.get('candidates',pool)
if isinstance(cs,dict): cs=list(cs.values())
blocked=[c for c in cs if c.get('status')=='BLOCKED']
NEW=("Established this session: (1) a rigid local system on P^1-{0,1,inf} that is regular semisimple at all three punctures "
 "has rank <= 2, its eigenvalue budget is 2n+2 against 3n, and at rank >= 3 only TWO punctures can be full — so at most two "
 "exponents fit; (2) rank 2 over Q carries only the exponents 3,4,6, and over a degree-d field needs d >= phi(x)/2, or "
 "phi(lcm(x,y,z))/2 for all three at once; (3) classical Frey models of short Weierstrass shape absorb only the pairs (2,3) "
 "and (n,n); (4) factorisation descent needs two EQUAL exponents, so it never reaches the open core; (5) for (3,4,4): the "
 "same-parity branch is closed by FLT3, the 3|gcd branch is empty, and the survivor is elliptic Chabauty on y^2 = x^3 - 972; "
 "(6) two gates — a condition must fail on some exponent-2 Fermat-Catalan solution, and its proof must use the equation.")
Q={"blocker_changed":jev.noul("Does any of the newly established facts REMOVE or WEAKEN the specific obstacle recorded as this candidate's blocker?",true="blocker weakened",false="blocker untouched"),
   "now_testable":jev.noul("Is there now a concrete exact test, runnable with Python, PARI or Lean at zero budget, that was not available before?",true="newly testable",false="still not testable"),
   "explained":jev.noul("Do the new facts EXPLAIN why this candidate is blocked, even if they do not unblock it?",true="explains the block",false="unrelated")}
rs=jev.ask_many([{"new_facts":NEW,"candidate_id":c['id'],"claim":c.get('claim','')[:800],
                  "blocker":str(c.get('failure_reason') or c.get('obligations') or '')[:500]} for c in blocked],Q,concurrency=12)
rows=[]
for c,r in zip(blocked,rs):
    if 'answers' not in r: continue
    a={k:round(v['noul'],2) for k,v in r['answers'].items()}
    rows.append((round(max(a['blocker_changed'],a['now_testable']),2),a,c['id'],c.get('claim','')[:70]))
rows.sort(key=lambda r:-r[0])
json.dump({"status":"HYPOTHESIS_ONLY","rows":rows},open('research/pool/evidence/unblock_screen_U295.json','w'),indent=1)
print("blocked candidates screened:",len(rows))
for s,a,i,cl in rows[:10]: print(s,i,a,cl)
