"""U205 — two-stage shadow separation for states where the period factor is large:
stage 1: modulus p^k (p | one base b): the b-term is 0 for exponents >= T, so the congruence involves only the other two
         exponents -> 2-D sieve over classes mod P2 = lcm(360, lambda(p^k));
stage 2: for the surviving 2-D pairs, run the 3-D sieve with primes q, (q-1) | P2."""
import json
from math import gcd
T,P=10,360
k={}; exec(open('code/U202_shadow_kill.py').read().split("d=json.load(open(\"research/pool/evidence/refine_sieve_N30.json\"))")[0],k)
ns=k['ns']; PR=k['PR']; lcm=k['lcm']; vp=k['vp']; lam=k['carmichael_pk']
def expand(st,P2): return [st+3] if st<T-3 else [T+(st-(T-3))+P*j for j in range(P2//P)]
def kill_state(tr,st):
    bases=tr
    for coord in range(3):
        if st[coord]<T-3: continue
        b=bases[coord]
        for p in [q for q in PR if q<=b and b%q==0]:
            for c in (1,2):
                kk=c*vp(b,p)+1; M=p**kk; P2=lcm(P,lam(p,kk))
                if P2//P>2500: continue
                o=[i for i in range(3) if i!=coord]
                E=[expand(st[i],P2) for i in o]
                sign=[1,1,-1]
                pairs=[(e0,e1) for e0 in E[0] for e1 in E[1] if (sign[o[0]]*pow(bases[o[0]],e0,M)+sign[o[1]]*pow(bases[o[1]],e1,M))%M==0]
                if not pairs: return True,M
                if len(pairs)*(P2//P)>3_000_000: continue
                qs=[q for q in PR if P2%(q-1)==0 and all(bb%q for bb in bases)][:200]
                Ec=expand(st[coord],P2)
                alive=[(e0,e1,ec) for (e0,e1) in pairs for ec in Ec]
                for q in qs:
                    def val(e0,e1,ec):
                        ex=[0,0,0]; ex[o[0]]=e0; ex[o[1]]=e1; ex[coord]=ec
                        return (pow(bases[0],ex[0],q)+pow(bases[1],ex[1],q)-pow(bases[2],ex[2],q))%q
                    alive=[t for t in alive if val(*t)==0]
                    if not alive: return True,(M,q)
    return False,None
for tr in [(3,47,2),(41,47,12)]:
    sv=[tuple(int(v) for v in s) for s in ns['survivors'](*tr)]
    res=[kill_state(tr,st) for st in sv]
    print(tr,"states:",len(sv),"all killed:",all(r[0] for r in res),[r[1] for r in res])
