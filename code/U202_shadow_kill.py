"""U202 — kill the shadow states of U200. A surviving class c in {1,2} (mod 360, exponent >= 10) on base b shadows a true
identity with exponent c < 3. For p | b, modulo p^k with k = c*v_p(b)+1 the term b^e (e>=3) is 0 but b^c is not, so the
true identity is separated -- provided the other two exponents are pinned modulo the orders mod p^k, which needs primes q
with (q-1) | P2 = lcm(360, lambda(p^k)).  Joint sieve over refined classes mod P2 (exact, numpy booleans)."""
import json, numpy as np, time
from math import gcd
T,P=10,360
ns={}; exec(open('code/U200_refine_sieve.py').read().split("d=json.load")[0].replace("        if not surv: return M,0\n    return None,len(surv)","        if not surv: return M,[]\n    return None,surv"),ns)
def lcm(a,b): return a*b//gcd(a,b)
def vp(n,p):
    c=0
    while n%p==0: n//=p; c+=1
    return c
def carmichael_pk(p,k): return (p-1)*p**(k-1) if p>2 else (1 if k==1 else 2 if k==2 else 2**(k-2))
def primes_upto(n):
    s=bytearray([1])*(n+1); s[0:2]=b"\0\0"
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
PR=primes_upto(60000)
def reps(state,P2):
    if state<T-3: return np.array([state+3],dtype=object)
    c=state-(T-3)
    return np.array([T+c+P*k for k in range(P2//P)],dtype=object)
def kill(tr,states):
    A,B,C=tr; bases=(A,B,C)
    for st in states:
        options=[]
        for coord,s_ in enumerate(st):
            if s_>=T-3:
                b=bases[coord]
                for p in [q for q in PR if q<=b and b%q==0]:
                    for c in (1,2):
                        k=c*vp(b,p)+1
                        if k<=T: options.append((lcm(P,carmichael_pk(p,k)),p**k))
        options.sort()
        done=False; note="no option"
        for P2,pk in options:
            nclass=sum(1 for s_ in st if s_>=T-3)
            if (P2//P)**nclass>4e7: note=f"period factor {P2//P} too large"; continue
            qs=[q for q in PR if (P2%(q-1)==0) and all(b%q for b in bases)][:300]
            R=[reps(s_,P2) for s_ in st]
            alive=np.ones((len(R[0]),len(R[1]),len(R[2])),dtype=bool)
            for M in [pk]+qs:
                rx=np.array([pow(A,int(e),M) for e in R[0]]); ry=np.array([pow(B,int(e),M) for e in R[1]]); rz=np.array([pow(C,int(e),M) for e in R[2]])
                alive&=((rx[:,None,None]+ry[None,:,None]-rz[None,None,:])%M==0)
                if not alive.any(): break
            if not alive.any(): done=True; break
            note=f"state {st} survives with P2={P2} ({int(alive.sum())} refined classes)"
        if not done: return False,note
    return True,"all shadow states killed"
d=json.load(open("research/pool/evidence/refine_sieve_N30.json"))
opened=[eval(k) for k,v in d.items() if not v[1]]
res={}; t0=time.time()
for tr in opened:
    A,B,C=tr; surv=ns['survivors'](A,B,C)
    primes=sorted({p for n in tr for p in range(2,n+1) if n%p==0 and all(p%q for q in range(2,p))})
    extra=[p**k for p in primes for k in range(3,T+1) if p**k<200000]+[17,29,43,97,109,113,127,241]
    M,left=ns['refine'](A,B,C,surv,extra)
    ok,msg=kill(tr,left); res[str(tr)]=[ok,msg]; print(tr,ok,msg,flush=True)
print(f"{time.time()-t0:.0f}s: killed {sum(1 for v in res.values() if v[0])} of {len(res)}")
json.dump(res,open("research/pool/evidence/shadow_kill_U202.json","w"),indent=1)
