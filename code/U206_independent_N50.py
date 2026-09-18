"""U206 — independent pure-Python pipeline for bases <= N (no numpy, own option search); compares with U204 totals."""
import sys, json, time
from math import gcd
N=int(sys.argv[1]); t0=time.time()
a={}; exec(open('code/U201_independent_verify.py').read().split("d=json.load")[0],a)       # cycle_len, single_ok, MODS1
b={}; exec(open('code/U203_independent_shadow_verify.py').read().split("d=json.load")[0],b) # survivors, dead
MODS1=a['MODS1']; single_ok=a['single_ok']; cyc=a['cycle_len']
st={"single":0,"joint":0,"shadow":0,"A1":0,"open":[]}
for A in range(1,N+1):
  for B in range(A+1,N+1):
    if gcd(A,B)!=1: continue
    for C in range(2,N+1):
      if gcd(A,C)!=1 or gcd(B,C)!=1: continue
      if any(single_ok(A,B,C,M) for M in MODS1 if cyc(A,M)*cyc(B,M)<=20000): st["single"]+=1; continue
      if A==1: st["A1"]+=1; continue
      sv=b['survivors'](A,B,C)
      if not sv: st["joint"]+=1; continue
      if all(b['dead']((A,B,C),s) for s in sv): st["shadow"]+=1
      else: st["open"].append((A,B,C))
print(f"INDEPENDENT N={N}: single {st['single']}; joint {st['joint']}; shadow {st['shadow']}; A=1 {st['A1']}; open {st['open']}  [{time.time()-t0:.0f}s]")
json.dump(st,open(f"research/pool/evidence/independent_pipeline_N{N}.json","w"))
