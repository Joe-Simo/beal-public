"""U210 — refinement for U209 survivors: expand surviving (x,y) classes from mod L to mod L2 = L*11*13 and test more
primes q = 1 (mod r), (q-1) | L2; plus r-th-power tests modulo p^k for p | AB (the other term vanishes for exponents >= T... here
only when the exponent state is a class, i.e. >= T >= k)."""
import sys, json
g={}; exec(open('code/U209_two_bases_fixed.py').read().split('if __name__')[0],g)
np=g['np']; PR=g['PR']; T=g['T']
def rth_res(M,r): return {pow(t,r,M) for t in range(M)}
def refine(A,B,r,L,F=143):
    L=L*(r if L%r else 1)
    reps=list(range(3,T))+[T+c for c in range(L)]
    alive=np.ones((len(reps),)*2,dtype=bool)
    for q in [q for q in PR if q%r==1 and L%(q-1)==0 and A%q and B%q] if r!=4 else [q for q in PR if q%4==1 and L%(q-1)==0 and A%q and B%q]:
        res=np.zeros(q,dtype=bool); res[[pow(t,r,q) for t in range(q)]]=True
        ax=np.array([pow(A,e,q) for e in reps]); by=np.array([pow(B,e,q) for e in reps])
        alive&=res[(ax[:,None]+by[None,:])%q]
    surv=[(reps[i],reps[j]) for i,j in np.argwhere(alive)]
    if not surv: return []
    L2=L*F
    def ex(e): return [e] if e<T else [e+L*k for k in range(F)]
    pairs=[(x,y) for (x0,y0) in surv for x in ex(x0) for y in ex(y0)]
    qs=[q for q in PR if (q%r==1 if r!=4 else q%4==1) and L2%(q-1)==0 and L%(q-1)!=0 and A%q and B%q][:80]
    for q in qs:
        R=rth_res(q,r)
        pairs=[(x,y) for (x,y) in pairs if (pow(A,x,q)+pow(B,y,q))%q in R]
        if not pairs: return []
    # prime-power moduli of the bases (k<=T so class exponents give 0)
    for b in (A,B):
        for p in [p for p in PR[:20] if b%p==0]:
            for k in (2,3,4,5):
                M=p**k
                if M>20000: continue
                R=rth_res(M,r)
                pairs=[(x,y) for (x,y) in pairs if (pow(A,x,M)+pow(B,y,M))%M in R]
    # collapse back to classes mod L for display
    return sorted({(x if x<T else T+(x-T)%L, y if y<T else T+(y-T)%L) for x,y in pairs})
if __name__=="__main__":
    L=2520; res={}
    for (A,B) in [(2,3),(2,5),(3,5),(2,7),(3,4),(3,7),(5,7),(2,9),(2,11),(3,8),(3,10),(5,6)]:
        line=[]
        for r in (3,4,5,7,11,13):
            s=refine(A,B,r,L)
            res[f"{A},{B},{r}"]=s
            line.append(f"r={r}:{'DEAD' if not s else s[:3]}")
        print((A,B)," ".join(line),flush=True)
    json.dump(res,open("research/pool/evidence/two_bases_fixed_U210.json","w"))
