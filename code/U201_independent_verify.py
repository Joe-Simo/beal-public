"""U201 — INDEPENDENT re-implementation (different code path: no numpy, no precomputed tail sets).
Part 1: every single-modulus exclusion is re-derived from scratch by brute force over explicit exponent ranges
        3 .. 3+L-1 where L = (preperiod + period) of the three residue sequences, computed by direct iteration.
Part 2: joint-sieve exclusions re-checked pair-by-pair with Python sets (time-boxed)."""
import json, time
from math import gcd
def cycle_len(a,M):
    # length after which a^x (x>=3) repeats: smallest L with a^(3+L) == a^(3+t) for some t<L ; return bound t+period
    seen={}; v=pow(a,3,M); i=0
    while v not in seen: seen[v]=i; v=(v*a)%M; i+=1
    return i            # all distinct residues appear within the first i exponents (3..3+i-1)
def single_ok(A,B,C,M):
    La,Lb,Lc=cycle_len(A,M),cycle_len(B,M),cycle_len(C,M)
    rc={pow(C,z,M) for z in range(3,3+Lc)}
    for x in range(3,3+La):
        ax=pow(A,x,M)
        for y in range(3,3+Lb):
            if (ax+pow(B,y,M))%M in rc: return False
    return True
MODS1=[8,9,16,27,32,64,5,7,11,13,17,19,25,29,31,37,41,43,49,61,73,81,97,101,109,113,121,125,127,151,181,193,211,241,257,
      63,65,91,117,133,171,217,247,259,273,341,511,513,585,657,703,1001,1729,2047,4095,4097,8191]
d=json.load(open("research/pool/evidence/fixed_three_bases_N30.json"))
fail=set(map(tuple,d["fail"]))
N=d["N"]; t0=time.time(); ver=0; mism=[]
for A in range(1,N+1):
  for B in range(A+1,N+1):
    if gcd(A,B)!=1: continue
    for C in range(2,N+1):
      if gcd(A,C)!=1 or gcd(B,C)!=1 or (A,B,C) in fail: continue
      if any(single_ok(A,B,C,M) for M in MODS1 if cycle_len(A,M)*cycle_len(B,M)<=20000): ver+=1
      else: mism.append((A,B,C))
print(f"Part 1: single-modulus exclusions re-verified independently: {ver} of {d['excluded']}; mismatches: {mism[:5]} ({len(mism)})  [{time.time()-t0:.0f}s]")
# Part 2 (time-boxed)
T,P=10,360; MODS2=[8,16,32,9,27,25,5,7,11,13,19,31,37,41,61,73,181]
reps=list(range(3,T))+[T+c for c in range(P)]
j=json.load(open("research/pool/evidence/joint_sieve_N30.json")); proved=[tuple(t) for t in j["proved"]]
t1=time.time(); ok2=0; bad2=[]
for (A,B,C) in proved:
    if time.time()-t1>420: break
    zres={M:{} for M in MODS2}
    for M in MODS2:
        for z in reps: zres[M].setdefault(pow(C,z,M),set()).add(z)
    alive=False
    for x in reps:
        for y in reps:
            cand=None
            for M in MODS2:
                s=zres[M].get((pow(A,x,M)+pow(B,y,M))%M)
                if not s: cand=set(); break
                cand = set(s) if cand is None else cand & s
                if not cand: break
            if cand: alive=True; break
        if alive: break
    if alive: bad2.append((A,B,C))
    else: ok2+=1
print(f"Part 2: joint-sieve exclusions re-verified independently: {ok2} (of {len(proved)}; time-boxed); mismatches: {bad2}")
json.dump({"part1_verified":ver,"part1_mismatch":mism,"part2_verified":ok2,"part2_mismatch":bad2},open("research/pool/evidence/independent_verify_U201.json","w"))
