"""U141 — COUNTERSEARCH: test every kernel-verified necessary condition on the ten Fermat-Catalan
solutions (each has an exponent 2, so they are NOT Beal counterexamples). A condition that FAILS on one
of them is a condition whose proof uses 'exponent >= 3' essentially -- those are the ones that carry the
Beal-specific content. A condition that HOLDS on all ten is a condition that cannot, by itself,
distinguish Beal from the exponent-2 world.  Jev is asked first to predict which fail (HYPOTHESIS_ONLY),
and the exact test decides."""
import sys, json; sys.path.insert(0,'code'); import jev
from math import gcd
FC=[(1,2,3,7,3,2),(2,7,3,5,2,4),(7,13,2,3,2,9),(2,17,71,7,3,2),(3,11,122,5,4,2),
    (17,76271,21063928,7,3,2),(1414,2213459,65,3,2,7),(9262,15312283,113,3,2,7),(43,96222,30042907,8,3,2),(33,1549034,15613,8,2,3)]
for s in FC: assert s[0]**s[3]+s[1]**s[4]==s[2]**s[5] and gcd(gcd(s[0],s[1]),s[2])==1, s
def cond(A,B,C,x,y,z):
    E=[t%2==0 for t in (A,B,C)]
    return {
     "exactly_one_even": sum(E)==1,
     "pairwise_coprime": gcd(A,B)==1 and gcd(A,C)==1 and gcd(B,C)==1,
     "A_ne_B": A!=B,
     "no_cancellation": A**x<C**z and B**y<C**z and C**z<=2*max(A**x,B**y),
     "C_even=>not_both_xy_even": not(C%2==0) or not(x%2==0 and y%2==0),
     "C_even,x_even,y_odd=>B=7mod8": not(C%2==0 and x%2==0 and y%2==1) or B%8==7,
     "C_even,x,y_odd=>8|A+B": not(C%2==0 and x%2==1 and y%2==1) or (A+B)%8==0,
     "A_even,y,z_odd=>B=C mod8": not(A%2==0 and y%2==1 and z%2==1) or B%8==C%8,
     "A_even,y_odd,z_even=>B=1mod8": not(A%2==0 and y%2==1 and z%2==0) or B%8==1,
     "C_largest=>z<=max(x,y)": not(A<C and B<C) or z<=max(x,y),
     "C_smallest=>z>max(x,y)": not(C<A and C<B) or z>max(x,y),
     "C<=B=>y<z": not(C<=B) or y<z,
     "dominant_dichotomy": not(B**y<=A**x) or ((z<=x)==(A<C)),
     "3|x,3|y,3∤ABC=>C^z=2,7mod9": not(x%3==0 and y%3==0 and A%3 and B%3 and C%3) or pow(C,z,9) in (2,7),
     "curvature_|chi|>=1/12 (12(qr+pr+pq)<=11pqr)": 12*(y*z+x*z+x*y)<=11*x*y*z,
    }
names=list(cond(*FC[0]).keys())
Q={"fails":jev.noul("Will this necessary condition (proved for exponents>=3) FAIL on at least one of the ten Fermat-Catalan solutions, which each contain an exponent 2?",true="fails on some",false="holds on all ten")}
rs=jev.ask_many([{"condition":n,"note":"Fermat-Catalan solutions have an exponent 2; Beal requires all exponents >=3"} for n in names],Q,concurrency=12)
pred={n:round(r["answers"]["fails"]["noul"],2) for n,r in zip(names,rs)}
for n,r in zip(names,rs): jev.persist("countersearch_"+str(names.index(n)),{"condition":n},Q,r)
print(f"{'condition':<48}{'jev P(fail)':>12}  exact: fails on")
res={}
for n in names:
    fails=[s for s in FC if not cond(*s)[n]]
    res[n]=[s for s in fails]
    print(f"{n:<48}{pred[n]:>12}  {[f'{s[0]}^{s[3]}+{s[1]}^{s[4]}={s[2]}^{s[5]}' for s in fails] if fails else 'HOLDS on all 10'}")
json.dump({"jev":pred,"exact":{k:[list(s) for s in v] for k,v in res.items()}},open("research/pool/evidence/countersearch_fc_U141.json","w"),indent=1)
