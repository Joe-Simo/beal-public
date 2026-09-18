"""U203 — independent (pure-Python, no numpy) re-verification of the last 36 triples (7 refined + 29 shadow-killed)."""
import json, time
from math import gcd
T,P=10,360; MODS2=[8,16,32,9,27,25,5,7,11,13,19,31,37,41,61,73,181]
reps0=list(range(3,T))+[T+c for c in range(P)]
def lcm(a,b): return a*b//gcd(a,b)
def primes_upto(n):
    s=[True]*(n+1); s[0]=s[1]=False
    for i in range(2,int(n**.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i in range(n+1) if s[i]]
PR=primes_upto(60000)
def survivors(A,B,C):
    zres={M:{} for M in MODS2}
    for M in MODS2:
        for z in reps0: zres[M].setdefault(pow(C,z,M),set()).add(z)
    out=[]
    for x in reps0:
        for y in reps0:
            cand=None
            for M in MODS2:
                s=zres[M].get((pow(A,x,M)+pow(B,y,M))%M)
                if not s: cand=set(); break
                cand=set(s) if cand is None else cand&s
                if not cand: break
            for z in (cand or ()): out.append((x,y,z))
    return out
def expand(e,P2): return [e] if e<T else [e+P*k for k in range(P2//P)]
def vp(n,p):
    c=0
    while n%p==0: n//=p; c+=1
    return c
def lam(p,k): return (p-1)*p**(k-1) if p>2 else (1 if k==1 else 2 if k==2 else 2**(k-2))
def dead(tr,st):
    A,B,C=tr; bases=tr
    # option list: every prime power p^k, p | some base, k<=T, and P2 = lcm(P, lambda(p^k)); try small ones first
    opts=sorted({(lcm(P,lam(p,k)),p**k) for b in bases for p in PR if p<=b and b%p==0 for k in range(2,T+1) if p**k<10**7})
    for P2,pk in opts:
        n=sum(1 for e in st if e>=T)
        if (P2//P)**n>3_000_000: continue
        qs=[q for q in PR if P2%(q-1)==0 and all(b%q for b in bases)][:300]
        X,Y,Z=expand(st[0],P2),expand(st[1],P2),expand(st[2],P2)
        alive=[(x,y,z) for x in X for y in Y for z in Z]
        for M in [pk]+qs:
            alive=[t for t in alive if (pow(A,t[0],M)+pow(B,t[1],M)-pow(C,t[2],M))%M==0]
            if not alive: return True
    return False
d=json.load(open("research/pool/evidence/joint_sieve_N30.json")); todo=[tuple(t) for t in d["open"]]
t0=time.time(); ok=0; bad=[]
for tr in todo:
    sv=survivors(*tr)
    if all(dead(tr,st) for st in sv): ok+=1
    else: bad.append(tr)
    print(tr,"survivors",len(sv),"->","PROVED" if tr not in bad else "NOT PROVED",flush=True)
print(f"{time.time()-t0:.0f}s: independently proved {ok} of {len(todo)}; not proved: {bad}")
json.dump({"proved":ok,"not_proved":bad},open("research/pool/evidence/independent_shadow_verify_U203.json","w"))
