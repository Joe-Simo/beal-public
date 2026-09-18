"""U204 — full pipeline for bases <= N.  Named hypothesis H_N: 'single modulus + joint sieve + shadow separation decides every
pairwise-coprime triple (A<B) with bases <= N'.  Exact arithmetic; every elimination sound (see C080)."""
import sys, json, time, numpy as np
from math import gcd
N=int(sys.argv[1]); t0=time.time()
g={}; exec(open('code/U198_fixed_three_bases.py').read().split("tot=0; ok=0")[0].replace("N=int(sys.argv[1]) if len(sys.argv)>1 else 30",f"N={N}"),g)
k={}; exec(open('code/U202_shadow_kill.py').read().split("d=json.load(open(\"research/pool/evidence/refine_sieve_N30.json\"))")[0],k)
ns=k['ns']; T=k['T']
u={}; exec(open('code/U205_two_stage_kill.py').read().split("for tr in [(3,47,2)")[0],u)   # two_stage fallback
stats={"single":0,"joint":0,"shadow":0,"mihailescu":0,"open":[]}; tot=0
for A in range(1,N+1):
  for B in range(A+1,N+1):
    if gcd(A,B)!=1: continue
    for C in range(2,N+1):
      if gcd(A,C)!=1 or gcd(B,C)!=1: continue
      tot+=1
      if g['excluded'](A,B,C): stats["single"]+=1; continue
      if A==1: stats["mihailescu"]+=1; continue
      surv=ns['survivors'](A,B,C)
      if len(surv)==0: stats["joint"]+=1; continue
      ok,msg=k['kill']((A,B,C),[tuple(int(v) for v in s) for s in surv])
      if ok: stats["shadow"]+=1
      else:
          sts=[tuple(int(v) for v in s_) for s_ in surv]
          if all(u['kill_state']((A,B,C),st_)[0] for st_ in sts): stats["two_stage"]=stats.get("two_stage",0)+1
          else: stats["open"].append([A,B,C,msg])
      if time.time()-t0>3400: break
print(f"N={N}: triples {tot}; single {stats['single']}; joint {stats['joint']}; shadow-separated {stats['shadow']}; two-stage {stats.get('two_stage',0)}; A=1 (Mihailescu) {stats['mihailescu']}; OPEN {len(stats['open'])}  [{time.time()-t0:.0f}s]")
print("open:",stats["open"][:20])
json.dump(stats,open(f"research/pool/evidence/pipeline_N{N}.json","w"))
