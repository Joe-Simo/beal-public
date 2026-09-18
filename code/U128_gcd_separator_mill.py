"""Cycle U128 — the positivity mill aimed at the gcd condition itself.
Model: all A^x+B^y=C^z with bases<=120, exponents 2..15, A!=B, split into COPRIME (gcd(A,B,C)=1) and
NON-COPRIME. Machine-generate Boolean features from ordering/gap/residue atoms only (NO exponent
values, since every coprime model solution has an exponent 2 and that would be a trivial separator),
and look for PERFECT SEPARATORS: features true on every non-coprime solution and false on every
coprime one, or vice versa. A separator provable for exponents>=3 would be Beal itself.
Jev then ranks the survivors; truth is decided by enumeration, proof only by Lean."""
from math import gcd
import itertools, json, sys
sys.path.insert(0,'code'); import jev
P={(n,k):n**k for n in range(1,121) for k in range(2,16)}
inv={}
for (n,k),v in P.items(): inv.setdefault(v,[]).append((n,k))
S=[(A,B,C,x,y,z) for (A,x),va in P.items() for (B,y),vb in P.items() for (C,z) in inv.get(va+vb,[]) if A!=B and min(A,B)>=2]
cop=[s for s in S if gcd(gcd(s[0],s[1]),s[2])==1]; non=[s for s in S if gcd(gcd(s[0],s[1]),s[2])>1]
print("coprime:",len(cop)," non-coprime:",len(non))
F={
 "C<A+B": lambda A,B,C,x,y,z: C<A+B, "C<=max(A,B)": lambda A,B,C,x,y,z: C<=max(A,B), "C<min(A,B)": lambda A,B,C,x,y,z: C<min(A,B),
 "z<=max(x,y)": lambda A,B,C,x,y,z: z<=max(x,y), "z<min(x,y)": lambda A,B,C,x,y,z: z<min(x,y), "z>=max(x,y)": lambda A,B,C,x,y,z: z>=max(x,y),
 "x==y": lambda A,B,C,x,y,z: x==y, "A^x==B^y": lambda A,B,C,x,y,z: A**x==B**y,
 "C^z<=2*max(A^x,B^y)": lambda A,B,C,x,y,z: C**z<=2*max(A**x,B**y),
 "min(A^x,B^y)*4<=C^z": lambda A,B,C,x,y,z: 4*min(A**x,B**y)<=C**z, "min(A^x,B^y)*100<=C^z": lambda A,B,C,x,y,z: 100*min(A**x,B**y)<=C**z,
 "minor<=C^(z-1)": lambda A,B,C,x,y,z: min(A**x,B**y)<=C**(z-1), "minor<=C": lambda A,B,C,x,y,z: min(A**x,B**y)<=C,
 "C|dominant-base": lambda A,B,C,x,y,z: (A if A**x>=B**y else B)%C==0, "C|A or C|B": lambda A,B,C,x,y,z: A%C==0 or B%C==0,
 "A|C or B|C": lambda A,B,C,x,y,z: C%A==0 or C%B==0, "gcd(A,B)>1": lambda A,B,C,x,y,z: gcd(A,B)>1,
 "min base divides other base": lambda A,B,C,x,y,z: max(A,B)%min(A,B)==0,
 "even count==1": lambda A,B,C,x,y,z: sum(t%2==0 for t in (A,B,C))==1, "3|ABC": lambda A,B,C,x,y,z: (A*B*C)%3==0,
 "1/x+1/y+1/z<1": lambda A,B,C,x,y,z: y*z+x*z+x*y < x*y*z,
 "C^z-max(A^x,B^y) < max(A^x,B^y)^(1/2)": lambda A,B,C,x,y,z: (C**z-max(A**x,B**y))**2 < max(A**x,B**y),
}
feats={k:(sum(f(*s) for s in cop),sum(f(*s) for s in non)) for k,f in F.items()}
print(f"{'feature':<42}{'coprime':>9}{'non-cop':>9}")
for k,(a,b) in feats.items(): print(f"{k:<42}{a:>9}{b:>9}")
seps=[k for k,(a,b) in feats.items() if (a==0 and b==len(non)) or (a==len(cop) and b==0)]
print("\nPERFECT single-feature separators:",seps)
# pairs
pairs=[]
for k1,k2 in itertools.combinations(F,2):
    a=sum(F[k1](*s) and F[k2](*s) for s in cop); b=sum(F[k1](*s) and F[k2](*s) for s in non)
    if (a==0 and b>=len(non)//2) or (a>=len(cop)//2 and b==0): pairs.append((k1,k2,a,b))
print("near-separating conjunctions (zero on one side, >=half on the other):",len(pairs))
for p in pairs[:12]: print("  ",p)
Q={"provable_ge3":jev.score("Could this feature be PROVED to hold for every hypothetical Beal counterexample (exponents>=3), from positivity and coprimality?",
   ["level 0: no, it is a small-model artefact","level 1: unlikely","level 2: plausible with real work","level 3: likely a few lines"])}
items=[{"feature":k,"coprime_count":feats[k][0],"noncoprime_count":feats[k][1],"of":[len(cop),len(non)]} for k in F]
rs=jev.ask_many(items,Q,concurrency=12)
rank=[]
for it,r in zip(items,rs):
    if "error" in r: continue
    jev.persist("C044",it,Q,r); rank.append((round(r["answers"]["provable_ge3"]["score"],2),it["feature"]))
rank.sort(reverse=True); print("\nJev provability ranking (HYPOTHESIS_ONLY):"); 
for t in rank[:8]: print(" ",t)
json.dump({"features":feats,"pairs":pairs,"jev":rank},open("research/pool/evidence/gcd_separator_mill.json","w"),indent=1)
