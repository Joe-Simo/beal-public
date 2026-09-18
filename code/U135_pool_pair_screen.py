"""Jev pairwise NOVEL COMBINATION screen over the whole pool (all unordered pairs)."""
import json, sys, itertools
sys.path.insert(0,'code'); import jev
db=json.load(open('research/pool/candidates.json'))['candidates']
live=[c for c in db if c['status'] not in ('DUPLICATE',)]
Q={"combine":jev.score("Would combining these two candidates produce a genuinely NEW attack (not a reword of either)?",
   ["level 0: no, unrelated or redundant","level 1: marginal","level 2: a concrete new lemma or test could be written","level 3: the combination could close an infinite family"]),
   "shared_failure":jev.noul("Do they share the SAME failure mode (so combining cannot help)?",true="same obstruction",false="different mechanisms")}
pairs=list(itertools.combinations(live,2))
states=[{"A":{"id":a['id'],"status":a['status'],"claim":a['claim'][:350]},"B":{"id":b['id'],"status":b['status'],"claim":b['claim'][:350]}} for a,b in pairs]
rs=jev.ask_many(states,Q,concurrency=12)
rows=[]
for (a,b),st,r in zip(pairs,states,rs):
    if "error" in r: continue
    jev.persist(f"pair_{a['id']}_{b['id']}",st,Q,r); x=r["answers"]
    rows.append((round(x["combine"]["score"],2),round(1-x["shared_failure"]["noul"],2),a['id'],b['id']))
rows.sort(key=lambda t:-t[0]*t[1])
json.dump(rows,open('research/pool/evidence/pair_screen_U150.json','w'),indent=1)
print(f"{len(rows)} pairs screened; top 15 by combine x distinct-mechanism:")
for t in rows[:15]: print(t)
