"""U142 — search for a NON-BLIND residue condition: an implication over residues mod M that is TRUE for
every admissible (A,B,C mod M; x,y,z>=3) but FALSE on at least one Fermat-Catalan solution (which has an
exponent 2). Exponent enters only through residues of powers, so a condition is expressed as
  hypothesis on (A,B,C mod M, parity/class of x,y,z)  ==>  conclusion on (A,B,C mod M)."""
from math import gcd
import itertools, json
FC=[(1,2,3,7,3,2),(2,7,3,5,2,4),(7,13,2,3,2,9),(2,17,71,7,3,2),(3,11,122,5,4,2),
    (17,76271,21063928,7,3,2),(1414,2213459,65,3,2,7),(9262,15312283,113,3,2,7),(43,96222,30042907,8,3,2),(33,1549034,15613,8,2,3)]
def admissible(M, xs):
    """all (a,b,c,x,y,z) with a,b,c mod M pairwise-coprime-ish (gcd with M) and x,y,z in xs, a^x+b^y=c^z mod M"""
    out=[]
    for a in range(M):
      for b in range(M):
        if gcd(gcd(a,b),M)>1: continue
        for c in range(M):
          if gcd(gcd(a,c),M)>1 or gcd(gcd(b,c),M)>1: continue
          for x in xs:
            pa=pow(a,x,M)
            for y in xs:
              s=(pa+pow(b,y,M))%M
              for z in xs:
                if pow(c,z,M)==s: out.append((a,b,c,x,y,z))
    return out
found=[]
for M in (16,32,9,27,5,7,13,11):
    xs=list(range(3,3+12))            # exponent classes 3..14 cover residues of powers for these M
    adm=admissible(M,xs)
    # candidate conclusions: residue of one base given parity of exponents and which base is even/divisible
    # Encode as: for each (x mod 4, y mod 4, z mod 4) class and each 'divisibility pattern' of (a,b,c) by the prime of M,
    # the SET of admissible (a,b,c) residues. A FC solution reduced mod M with its exponent classes must lie in that set
    # if the condition is blind. Exponent 2 has class 2 mod 4 -- compare against class 2+4k>=6 (i.e. 6,10,14).
    table={}
    for (a,b,c,x,y,z) in adm:
        table.setdefault((x%4,y%4,z%4),set()).add((a,b,c))
    for s in FC:
        A,B,C,x,y,z=s
        key=(x%4,y%4,z%4)
        r=(A%M,B%M,C%M)
        if key in table and r not in table[key]:
            found.append((M,s,key))
print("non-blind residue conditions found (FC solution outside the exponent>=3 admissible set for its exponent classes mod 4):")
for f in found: print("  M=%d  FC=%s  class=%s"%f)
print("total:",len(found))
json.dump([[f[0],list(f[1]),list(f[2])] for f in found],open("research/pool/evidence/mod16_nonblind_U142.json","w"))
