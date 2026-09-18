"""U233 — EXPLOITATION of the one kernel condition that passes both gates (C097).
Kernel has only 8 | A^x+B^y when C even. The equation gives the strictly stronger
    2^(z*v_2(C)) || A^x + B^y,   in particular 2^z | A^x + B^y.
(a) Jev routing; (b) exact measurement of how much more the strong form prunes."""
import json,sys
from math import gcd
sys.path.insert(0,'code'); import jev
CTX=("Beal repo. Machine-checked kernel currently contains only '8 | A^x+B^y when C is even'. The equation gives "
 "2^(z*v_2(C)) exactly dividing A^x+B^y, hence 2^z | A^x+B^y with z>=3. Gate 1: must fail on some of the ten "
 "exponent-2 Fermat-Catalan solutions. Gate 2: the proof must use the equation A^x+B^y=C^z.")
Q={"strictly_stronger":jev.noul("Is 2^z | A^x+B^y (z>=3, C even) strictly stronger than 8 | A^x+B^y as a constraint on counterexamples?",true="strictly stronger",false="equivalent"),
 "gate2":jev.noul("Does its proof use the equation A^x+B^y=C^z (rather than only the exponent bounds)?",true="uses the equation",false="does not"),
 "new_here":jev.noul("Would this be new to a repo whose kernel currently stops at modulus 8?",true="new here",false="already present")}
rs=jev.ask_many([{"context":CTX,"claim":"2^z divides A^x+B^y whenever C is even"}],Q,concurrency=2)
print("JEV:",{k:round(v['noul'],2) for k,v in rs[0]['answers'].items()})
json.dump({"status":"HYPOTHESIS_ONLY","answers":{k:v['noul'] for k,v in rs[0]['answers'].items()}},
          open('research/pool/evidence/two_adic_U233.json','w'),indent=1)
def ipp(n):
    if n<2: return n==1
    for k in range(2,n.bit_length()+1):
        lo,hi=1,1
        while hi**k<=n: hi*=2
        while lo<hi-1:
            m=(lo+hi)//2
            if m**k<=n: lo=m
            else: hi=m
        if lo**k==n: return True
    return False
GEN=[(a,b,a+b) for a in range(2,300) for b in range(a+1,300)
     if gcd(a,b)==1 and not ipp(a) and not ipp(b) and not ipp(a+b) and (a+b)%2==0]
print("\ngeneric coprime non-power triples with c EVEN:",len(GEN))
for k in (3,4,5,6,7,8):
    n=sum(1 for a,b,c in GEN if (a+b)%(2**k)==0)
    print("  fraction satisfying 2^%d | a+b : %6.2f%%  (kernel uses k=3)"%(k,100*n/len(GEN)))
FC=[(1,1,2,3,3,2),(2,5,7,2,3,4),(7,3,13,2,2,9),(2,7,17,3,71,2),(3,5,11,4,122,2),
    (33,8,1549034,2,15613,3),(1414,3,2213459,2,65,7),(9262,3,15312283,2,113,7),
    (17,7,76271,3,21063928,2),(43,8,96222,3,30042907,2)]
print("\nFermat-Catalan solutions with C even, check 2^z | A^x+B^y:")
for A,x,B,y,C,z in FC:
    if C%2: continue
    a,b,c=A**x,B**y,C**z
    print("  %d^%d+%d^%d=%d^%d  v2(a+b)=%d  z=%d  2^z divides: %s"
          %(A,x,B,y,C,z,(a+b&-(a+b)).bit_length()-1,z,(a+b)%(2**z)==0))
