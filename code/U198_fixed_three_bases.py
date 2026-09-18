"""U198 — FIXED THREE BASES, ALL EXPONENTS: for pairwise-coprime (A,B,C), find a modulus M with
   {A^x : x>=3} + {B^y : y>=3}  disjoint from  {C^z : z>=3}   (mod M).
That is a PROOF (full covering of the exponent cycles) that A^x+B^y=C^z has no solution with x,y,z>=3 for
these bases -- for every signature at once, including (3,5,7).  Exact integer arithmetic only.
Named hypothesis H: every pairwise-coprime triple with 2 <= A < B, bases <= N is excluded by some M in MODS."""
from math import gcd
import json, sys
N=int(sys.argv[1]) if len(sys.argv)>1 else 30
MODS=[8,9,16,27,32,64,5,7,11,13,17,19,25,29,31,37,41,43,49,61,73,81,97,101,109,113,121,125,127,151,181,193,211,241,257,
      63,65,91,117,133,171,217,247,259,273,341,511,513,585,657,703,1001,1729,2047,4095,4097,8191]
def tail_set(a,M):
    # residues of a^x mod M for all x >= 3 (the sequence is eventually periodic; iterate until repeat)
    seen=set(); v=pow(a,3,M)
    while v not in seen:
        seen.add(v); v=(v*a)%M
    return seen
R={M:{a:tail_set(a,M) for a in range(1,N+1)} for M in MODS}
def excluded(A,B,C):
    for M in MODS:
        ra,rb,rc=R[M][A],R[M][B],R[M][C]
        if len(ra)*len(rb)>20000: continue
        if not any(((x+y)%M) in rc for x in ra for y in rb): return M
    return None
tot=0; ok=0; fail=[]; used={}
for A in range(1,N+1):
  for B in range(A+1,N+1):
    if gcd(A,B)!=1: continue
    for C in range(2,N+1):
      if gcd(A,C)!=1 or gcd(B,C)!=1: continue
      tot+=1
      M=excluded(A,B,C)
      if M: ok+=1; used[M]=used.get(M,0)+1
      else: fail.append((A,B,C))
print(f"bases <= {N}: pairwise-coprime triples (A<B): {tot}; excluded by a single modulus: {ok}; NOT excluded: {len(fail)}")
print("most useful moduli:",sorted(used.items(),key=lambda t:-t[1])[:10])
print("first unexcluded triples:",fail[:30])
json.dump({"N":N,"total":tot,"excluded":ok,"fail":fail,"used":used},open(f"research/pool/evidence/fixed_three_bases_N{N}.json","w"))
