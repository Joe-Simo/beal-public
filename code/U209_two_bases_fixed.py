"""U209 — TWO BASES FIXED, C FREE: is A^x + B^y (x,y>=3) ever a perfect r-th power?  (r = 4 or an odd prime <= R)
If not for every r <= R and r = 4, then for these (A,B) there is no Beal counterexample A^x+B^y=C^z with ANY C and any z
having a prime factor <= R or divisible by 4.  Covering sieve over (x,y) states: exact 3..T-1 plus classes mod L.
A pair survives modulus q (q prime, q = 1 mod r, (q-1) | L) only if A^x+B^y is an r-th power residue mod q (0 allowed).
Sound: a genuine r-th power is an r-th power residue modulo every prime."""
import sys, json, numpy as np
from math import gcd
T=8
def primes_upto(n):
    s=bytearray([1])*(n+1); s[0:2]=b"\0\0"
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
PR=primes_upto(200000)
def run(A,B,r,L):
    reps=list(range(3,T))+[T+c for c in range(L)]
    S=len(reps)
    alive=np.ones((S,S),dtype=bool)
    qs=[q for q in PR if q%r==1 and L%(q-1)==0 and A%q and B%q] if r!=4 else [q for q in PR if q%4==1 and L%(q-1)==0 and A%q and B%q]
    used=0
    for q in qs:
        res=np.zeros(q,dtype=bool); res[[pow(t,r,q) for t in range(q)]]=True
        ax=np.array([pow(A,e,q) for e in reps]); by=np.array([pow(B,e,q) for e in reps])
        alive&=res[(ax[:,None]+by[None,:])%q]; used+=1
        if not alive.any(): return 0,used,[]
    idx=np.argwhere(alive)
    return int(alive.sum()),used,[(reps[i],reps[j]) for i,j in idx[:6]]
if __name__=="__main__":
    L=int(sys.argv[1]) if len(sys.argv)>1 else 2520
    for (A,B) in [(2,3),(2,5),(3,5),(2,7),(3,4),(3,7),(5,7)]:
        out=[]
        for r in (3,4,5,7):
            n,used,ex=run(A,B,r,L*(r if L%r else 1))
            out.append(f"r={r}: {'DEAD' if n==0 else str(n)+' classes left '+str(ex[:3])} ({used} primes)")
        print((A,B)," | ".join(out),flush=True)
