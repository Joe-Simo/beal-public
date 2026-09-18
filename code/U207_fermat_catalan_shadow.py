"""U207 — the one triple the N=80 pipeline left open: (2,17,71), which shadows the Fermat-Catalan identity 2^7+17^3=71^2.
Only z=2 is below 3, so separate with 71^3:  for z>=3, 71^z = 0 (mod 71^3), hence 2^x + 17^y = 0 (mod 71^3).
Dict-based 2-D sieve over x,y classes mod P2 = lcm(360, lambda(71^3)); then primes q with (q-1) | P2, requiring for each
surviving (x,y) that SOME z in its class matches (a necessary condition, so every elimination is sound)."""
from math import gcd
T,P=10,360
k={}; exec(open('code/U202_shadow_kill.py').read().split("d=json.load(open(\"research/pool/evidence/refine_sieve_N30.json\"))")[0],k)
ns=k['ns']; PR=k['PR']
A,B,C=2,17,71; M=71**3; lam=70*71*71
P2=P*lam//gcd(P,lam)
def expand(st): return [st+3] if st<T-3 else [T+(st-(T-3))+P*j for j in range(P2//P)]
sv=[tuple(int(v) for v in s) for s in ns['survivors'](A,B,C)]
print("survivor states:",[(("="+str(a+3)) if a<T-3 else "≡"+str((T+a-(T-3))%P) ,("="+str(b+3)) if b<T-3 else "≡"+str((T+b-(T-3))%P),("="+str(c+3)) if c<T-3 else "≡"+str((T+c-(T-3))%P)) for a,b,c in sv])
qs=[q for q in PR if P2%(q-1)==0 and q not in (2,17,71)][:120]
allok=True
for st in sv:
    if st[2]<T-3:
        print(st,"z is an exact exponent >= 3 -> not a shadow; needs separate treatment"); allok=False; continue
    X,Y,Z=expand(st[0]),expand(st[1]),expand(st[2])
    table={}
    for x in X: table.setdefault(pow(A,x,M),[]).append(x)
    pairs=[(x,y) for y in Y for x in table.get((-pow(B,y,M))%M,[])]
    n0=len(pairs)
    for q in qs:
        zset={pow(C,z,q) for z in Z[:q]}            # residues of 71^z over the class (period | q-1 <= q)
        pairs=[(x,y) for (x,y) in pairs if (pow(A,x,q)+pow(B,y,q))%q in zset]
        if not pairs: break
    n1=len(pairs)
    if pairs:
        # joint 3-D stage on the few surviving pairs: keep z explicitly
        trip=[(x,y,z) for (x,y) in pairs for z in Z]
        for Mq in [2**10,17**3,17**4]+qs+[q for q in PR if P2%(q-1)==0 and q not in (2,17,71)][120:400]:
            trip=[t for t in trip if (pow(A,t[0],Mq)+pow(B,t[1],Mq)-pow(C,t[2],Mq))%Mq==0]
            if not trip: break
        pairs=trip
    print(st,"pairs after 71^3:",n0,"-> after per-prime filter:",n1,"-> after joint 3-D:",len(pairs),"(killed)" if not pairs else "(SURVIVES)")
    allok&= not pairs
print("ALL STATES KILLED:",allok)
