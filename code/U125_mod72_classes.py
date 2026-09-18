"""Cycle U125 — NOVEL COMBINATION of the mod-8 and mod-9 results: the mod-72 sieve by exponent class.
Question: is there an exponent class (x,y,z mod 6) for which NO residue triple (A,B,C mod 72) with
pairwise coprime bases satisfies A^x+B^y=C^z mod 72?  Such a class would be an infinite family of
signatures excluded outright.  n^k mod 72 depends only on n mod 72 and on k for k>=3 (period 6 in k
for units; non-units stabilise by k=3)."""
from math import gcd
M=72
def pw(n,k): return pow(n,k,M)
def coprime_pair(a,b): return gcd(gcd(a,b),M)==1 or gcd(a,b)==1
res={}
for x in range(3,9):        # exponents 3..8 cover every class mod 6 with k>=3
  for y in range(3,9):
    for z in range(3,9):
      cnt=0
      for A in range(M):
        for B in range(M):
          if gcd(gcd(A,B),M)!=1: continue           # 2 or 3 dividing both A and B
          lhs=(pw(A,x)+pw(B,y))%M
          for C in range(M):
            if gcd(gcd(A,C),M)!=1 or gcd(gcd(B,C),M)!=1: continue
            if pw(C,z)==lhs: cnt+=1
      res[(x,y,z)]=cnt
empty=[k for k,v in res.items() if v==0]
print("exponent classes (x,y,z in 3..8):",len(res))
print("classes with ZERO admissible residue triples mod 72:",empty)
tot=M**3
print("min/max admissible per class:",min(res.values()),max(res.values()),"of",tot)
import json; json.dump({str(k):v for k,v in res.items()},open("research/pool/evidence/mod72_class_counts.json","w"),indent=1)
# density summary by (x%2,y%2,z%2,x%3,y%3,z%3)
print("\nlowest 8 classes:")
for k,v in sorted(res.items(),key=lambda t:t[1])[:8]: print(k,v)
