"""U228 — Jev routing on WHY C092 is non-blind, plus exact verification of the proposed mechanism.
Proposed lemma: for squarefree pairwise-coprime A,B,C (>1), rad(ABC)=ABC, so
    rad(ABC)^3 <= A^x B^y C^z  <=>  A^3 B^3 C^3 <= A^x B^y C^z,
which holds whenever x,y,z>=3 and can FAIL as soon as an exponent drops below 3. That is the exact
mechanism behind the four Fermat-Catalan violations."""
import json,sys
from math import gcd
sys.path.insert(0,'code'); import jev
CTX=("Beal repo. C092 (machine-checked): rad(ABC)^3 <= A^x B^y C^z for every Beal counterexample. It FAILS on 4 of the "
 "10 Fermat-Catalan solutions, so it is not exponent-2-blind. Question: is the mechanism simply that rad(ABC)=ABC when "
 "the bases are squarefree, reducing the inequality to A^3 B^3 C^3 <= A^x B^y C^z, i.e. to the exponent hypothesis itself?")
Q={"mechanism_is_exponents":jev.noul("If the mechanism reduces to A^3B^3C^3 <= A^xB^yC^z, is the condition then merely the exponent hypothesis x,y,z>=3 restated (like |chi|>=1/12), rather than independent arithmetic content?",true="merely the exponent hypothesis restated",false="independent content"),
 "worth_formalising":jev.noul("Is an explicit iff-characterisation of when the condition fails worth adding to the Lean development as documentation of the blindness mechanism?",true="worth it",false="not worth it")}
rs=jev.ask_many([{"context":CTX,"question":"mechanism behind the non-blindness of rad(ABC)^3 <= abc"}],Q,concurrency=2)
print("JEV:",{k:round(v['noul'],2) for k,v in rs[0]['answers'].items()})
json.dump({"status":"HYPOTHESIS_ONLY","answers":{k:v['noul'] for k,v in rs[0]['answers'].items()}},open('research/pool/evidence/blindness_mechanism_U228.json','w'),indent=1)
def rad(n):
    r,d=1,2
    while d*d<=n:
        if n%d==0:
            r*=d
            while n%d==0: n//=d
        d+=1
    return r*(n if n>1 else 1)
FC=[(1,1,2,3,3,2),(2,5,7,2,3,4),(7,3,13,2,2,9),(2,7,17,3,71,2),(3,5,11,4,122,2),
    (33,8,1549034,2,15613,3),(1414,3,2213459,2,65,7),(9262,3,15312283,2,113,7),
    (17,7,76271,3,21063928,2),(43,8,96222,3,30042907,2)]
print("\nExact: for each FC solution, is rad(ABC)=ABC (squarefree), and does the cube test fail?")
for A,x,B,y,C,z in FC:
    a,b,c=A**x,B**y,C**z; R=rad(A*B*C); sf = (R==A*B*C)
    fails = not (R**3 <= a*b*c)
    minexp=min(x,y,z)
    print("  %-34s squarefree_product=%-5s min_exp=%d  cube_test_fails=%s"%("%d^%d+%d^%d=%d^%d"%(A,x,B,y,C,z),sf,minexp,fails))
print("\nExact: the iff for squarefree pairwise-coprime bases, brute force over small cases")
bad=0; tested=0
for A in range(2,25):
  for B in range(2,25):
    for C in range(2,25):
      if rad(A)!=A or rad(B)!=B or rad(C)!=C: continue
      if gcd(A,B)!=1 or gcd(A,C)!=1 or gcd(B,C)!=1: continue
      for x in range(1,7):
        for y in range(1,7):
          for z in range(1,7):
            tested+=1
            lhs = rad(A*B*C)**3 <= A**x*B**y*C**z
            rhs = A**3*B**3*C**3 <= A**x*B**y*C**z
            if lhs!=rhs: bad+=1
print("  iff holds on all %d squarefree pairwise-coprime cases: %s (mismatches %d)"%(tested,bad==0,bad))
