"""U170 — COUNTERSEARCH of the InstanceRows.pss347 hypothesis.
PSS (Poonen-Schaefer-Stoll 2007): the primitive integer solutions of x^2 + y^3 = z^7 are exactly
(+-1,-1,0), (+-1,0,1), +-(0,1,1), (+-3,-2,1), (+-71,-17,2), (+-2213459,1414,65),
(+-15312283,9262,113), (+-21063928,-76271,17).
A Beal counterexample with exponents {3,4,7} in ANY arrangement gives a PSS solution with |x| a perfect
square >= 1, y,z nonzero (signs absorbed: 3 and 7 are odd). Check: identities exact; no such solution."""
from math import isqrt
PSS=[(1,-1,0),(1,0,1),(0,1,1),(3,-2,1),(71,-17,2),(2213459,1414,65),(15312283,9262,113),(21063928,-76271,17)]
for x,y,z in PSS: assert x*x+y**3==z**7,(x,y,z)
print("all 8 PSS identities verified exactly")
bad=[(x,y,z) for x,y,z in PSS if x>0 and isqrt(x)**2==x and y!=0 and z!=0]
print("PSS solutions with |x| a nonzero perfect square and yz != 0:",bad)
# brute-force sanity for every arrangement of {3,4,7} and {3,4,5}, and (3,4,4): no small coprime solutions
from math import gcd
from itertools import permutations
def search(sig,N):
    x,y,z=sig; P={}
    for c in range(1,N+1): P.setdefault(c**z,[]).append(c)
    out=[]
    for a in range(1,N+1):
        for b in range(1,N+1):
            v=a**x+b**y
            if v in P and gcd(a,b)==1: out.append((a,b,P[v][0]))
    return out
for base in [(3,4,7),(3,4,5),(3,4,4)]:
    for sig in sorted(set(permutations(base))):
        r=search(sig,400)
        print(sig,"coprime solutions with bases<=400:",r)
