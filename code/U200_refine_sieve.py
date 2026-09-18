"""U200 — refinement for the triples surviving U199: add prime-power moduli p^k for the primes p dividing a base
(these separate 'x >= 3' from genuine small-exponent solutions, which the coprime moduli can never do), and extra
coprime moduli, by expanding surviving exponent states to a larger period only where needed."""
import json, numpy as np, itertools, time
from math import gcd
T,P=10,360
MODS=[8,16,32,9,27,25,5,7,11,13,19,31,37,41,61,73,181]
S=(T-3)+P
def lcm(a,b): return a*b//gcd(a,b)
def states_res(a,M):
    return np.array([pow(a,x,M) for x in range(3,T)]+[pow(a,T+c,M) for c in range(P)],dtype=np.int64)
def survivors(A,B,C):
    allowed=np.ones((S,S,S),dtype=bool)
    for M in MODS:
        rx,ry,rz=states_res(A,M),states_res(B,M),states_res(C,M)
        zmask=np.zeros((M,S),dtype=bool); zmask[rz,np.arange(S)]=True
        allowed&=zmask[(rx[:,None]+ry[None,:])%M]
    return np.argwhere(allowed)
def period(a,M):
    # eventual period of a^x mod M for x>=T
    v=pow(a,T,M); k=1; w=(v*a)%M
    while w!=v:
        w=(w*a)%M; k+=1
        if k>2*M: raise ValueError("not purely periodic from T: choose k <= T")
    return k
def expand(state,Q):
    # state -> list of (is_exact, value) describing x: exact x, or class (x mod Q', x>=T) refined to period Q (multiple of P)
    if state<T-3: return [("e",state+3)]
    c=state-(T-3)                       # x = T + c (mod P), x>=T
    return [("c",(T+c+P*k)) for k in range(Q//P)]   # representatives T+c+P*k, distinct mod Q
def refine(A,B,C,surv,extra):
    surv=[tuple(int(v) for v in s) for s in surv]
    for M in extra:
        Qa,Qb,Qc=lcm(P,period(A,M)),lcm(P,period(B,M)),lcm(P,period(C,M))
        if (Qa//P)*(Qb//P)*(Qc//P)>6000: continue
        new=[]
        for (sx,sy,sz) in surv:
            ok=False
            for ex in expand(sx,Qa):
                for ey in expand(sy,Qb):
                    for ez in expand(sz,Qc):
                        if (pow(A,ex[1],M)+pow(B,ey[1],M)-pow(C,ez[1],M))%M==0: ok=True; break
                    if ok: break
                if ok: break
            if ok: new.append((sx,sy,sz))
        surv=new
        if not surv: return M,0
    return None,len(surv)
d=json.load(open("research/pool/evidence/joint_sieve_N30.json"))
res={}
t0=time.time()
for (A,B,C) in d["open"]:
    surv=survivors(A,B,C)
    primes=sorted({p for n in (A,B,C) for p in range(2,n+1) if n%p==0 and all(p%q for q in range(2,p))})
    extra=[p**k for p in primes for k in range(3,T+1) if p**k<200000]+[17,29,43,97,109,113,127,241]
    M,left=refine(A,B,C,surv,extra)
    res[(A,B,C)]=(len(surv),M,left)
    print((A,B,C),"survivors after U199:",flush=True) if False else print((A,B,C),"survivors after U199:",len(surv),"->","PROVED by adding",M if M else f"NOT closed, {left} states left")
print(f"{time.time()-t0:.0f}s; proved {sum(1 for v in res.values() if v[1])} of {len(res)}")
json.dump({str(k):v for k,v in res.items()},open("research/pool/evidence/refine_sieve_N30.json","w"))
