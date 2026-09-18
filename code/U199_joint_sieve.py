"""U199 — JOINT covering sieve for the triples not excluded by one modulus (U198).
Exponent states: exact values 3..T-1, then classes mod P for x >= T.  For every modulus M used, a^x mod M depends
only on the state (T >= every p-adic preperiod, lambda(M') | P).  A triple is PROVED to have no solution with
x,y,z >= 3 when the joint set of allowed state-triples becomes empty.  Exact arithmetic (numpy only for booleans)."""
import json, sys, time
import numpy as np
from math import gcd
T,P=10,360
MODS=[8,16,32,9,27,25,5,7,11,13,19,31,37,41,61,73,181]
S=(T-3)+P
def states_res(a,M):
    out=[pow(a,x,M) for x in range(3,T)]
    out+=[pow(a,T+c,M) for c in range(P)]          # representative T+c for class c; valid since period | P beyond T
    return np.array(out,dtype=np.int64)
def check_periodicity(a,M):
    # verify a^(x+P) == a^x mod M for all x >= T (enough to check x in [T, T+P+20))
    return all(pow(a,x+P,M)==pow(a,x,M) for x in range(T,T+60))
def prove(A,B,C):
    allowed=np.ones((S,S,S),dtype=bool)
    for M in MODS:
        assert check_periodicity(A,M) and check_periodicity(B,M) and check_periodicity(C,M)
        rx,ry,rz=states_res(A,M),states_res(B,M),states_res(C,M)
        zmask=np.zeros((M,S),dtype=bool); zmask[rz,np.arange(S)]=True
        sumxy=(rx[:,None]+ry[None,:])%M
        allowed&=zmask[sumxy]
        if not allowed.any(): return M
    return None
d=json.load(open("research/pool/evidence/fixed_three_bases_N30.json"))
fails=[t for t in d["fail"] if t[0]!=1]
print("triples to attack (A>=2):",len(fails)," (A=1 triples:",len(d["fail"])-len(fails),"-> Mihailescu)")
t0=time.time(); done=[]; still=[]
for (A,B,C) in fails:
    if time.time()-t0>520: break
    r=prove(A,B,C)
    (done if r else still).append((A,B,C))
print(f"processed {len(done)+len(still)} of {len(fails)} in {time.time()-t0:.0f}s: PROVED no solution: {len(done)}; still open under this sieve: {len(still)}")
print("still open:",still[:40])
json.dump({"proved":done,"open":still,"T":T,"P":P,"mods":MODS},open("research/pool/evidence/joint_sieve_N30.json","w"))
