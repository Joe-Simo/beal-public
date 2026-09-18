"""U227 — (a) Jev screen on the SHARPENED radical bound; (b) exact integer verification.
Claim: for coprime A^x+B^y=C^z, from A^x<c, B^y<c, C^z=c and rad(abc)<=ABC:
    rad(A*B*C)^(x*y*z) <= c^(y*z + x*z + x*y),   c = C^z.
Equivalently quality q = log c / log rad >= 1/S with S = 1/x+1/y+1/z.
Blindness: evaluate on the ten Fermat-Catalan solutions."""
import json,sys
from math import gcd,log
sys.path.insert(0,'code'); import jev
CTX=("Beal. Known: rad(abc)^3 <= abc unconditionally (formalised, C092), but the implied abc-quality bound tends to 1 "
 "and is vacuous (C088). Sharpened form uses c alone: rad(ABC)^(xyz) <= c^(yz+xz+xy), i.e. quality >= 1/(1/x+1/y+1/z). "
 "For (3,3,3) this gives quality >= 1 (vacuous, and FLT3 closes it anyway); for (3,5,7) it gives quality >= 105/71 = 1.479.")
Q={"standard":jev.noul("Is the bound quality >= 1/(1/x+1/y+1/z) for generalized Fermat equations already standard in the literature (e.g. stated in abc/Fermat-Catalan surveys)?",true="standard",false="not standard"),
 "vacuous":jev.noul("Is a lower bound of 1.479 on abc-quality vacuous, given that abc triples of quality up to 1.6299 are KNOWN to exist?",true="vacuous",false="informative"),
 "lean":jev.noul("Can rad(A*B*C)^(x*y*z) <= (C^z)^(y*z+x*z+x*y) be stated and proved in Lean 4 over natural numbers with existing mathlib API?",true="Lean-ready",false="not Lean-ready")}
rs=jev.ask_many([{"context":CTX,"claim":"quality >= 1/(1/x+1/y+1/z) for every coprime solution of A^x+B^y=C^z"}],Q,concurrency=2)
print("JEV:",{k:round(v['noul'],2) for k,v in rs[0]['answers'].items()})
json.dump({"status":"HYPOTHESIS_ONLY","answers":{k:v['noul'] for k,v in rs[0]['answers'].items()}},open('research/pool/evidence/sharp_radical_U227.json','w'),indent=1)
# ---- exact verification, integers only ----
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
print("\nSharpened bound rad(ABC)^(xyz) <= c^(yz+xz+xy) on the ten Fermat-Catalan solutions:")
fails=0
for A,x,B,y,C,z in FC:
    a,b,c=A**x,B**y,C**z
    assert a+b==c
    R=rad(A*B*C); e=x*y*z; f=y*z+x*z+x*y
    ok = R**e <= c**f
    if not ok: fails+=1
    print("  A=%d^%d B=%d^%d C=%d^%d  S=1/x+1/y+1/z=%.4f  q=%.4f  holds:%s"%(A,x,B,y,C,z,1/x+1/y+1/z,log(c)/log(R),ok))
print("  violations:",fails,"of 10")
print("\nExact check of the derivation on random coprime power triples with all exponents>=3 (none expected to exist):")
print("  identity check (A^x)^(yz)*(B^y)^(xz)*(C^z)^(xy) = (ABC)^(xyz):",
      all((A**x)**(y*z)*(B**y)**(x*z)*(C**z)**(x*y)==(A*B*C)**(x*y*z)
          for A in range(1,7) for B in range(1,7) for C in range(1,7) for x in (3,4,5) for y in (3,5) for z in (3,4)))
print("\nquality floor 1/S for small signatures with x,y,z>=3:")
for sig in [(3,3,3),(3,3,4),(3,4,5),(3,5,7),(4,5,7),(3,3,5),(5,5,5)]:
    S=sum(1/e for e in sig); print("  ",sig,"q >= %.4f"%(1/S))
