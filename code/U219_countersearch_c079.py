"""U219 — COUNTERSEARCH of my own lemma C079: for each (n,e) marked OK, brute-force A^3+B^3=n^r, r=3j+e, j>=1, n^r<=10^21,
gcd(A,n)=1, A,B>0.  Any hit refutes C079. Exact integers. Also a positive control: 1^3+2^3=3^2 (j=0) must be found when j=0 allowed."""
from math import gcd
def icbrt(m):
    x=round(m**(1/3))
    while x**3>m: x-=1
    while (x+1)**3<=m: x+=1
    return x
ok=[tuple(map(int,l.split()[1:3])) for l in open('references/U130/fixed_base_333.txt') if l.startswith('OK')]
def sols(N,n):
    out=[]; a=1
    while 2*a**3<=N:
        b3=N-a**3; b=icbrt(b3)
        if b**3==b3 and gcd(a,n)==1: out.append((a,b))
        a+=1
    return out
assert sols(9,3)==[(1,2)]           # positive control
hits=0; tested=0
for n,e in ok:
    j=1
    while n**(3*j+e)<=10**15:
        N=n**(3*j+e); tested+=1
        s=sols(N,n)
        if s: hits+=1; print("HIT",n,3*j+e,s)
        j+=1
print("OK pairs",len(ok),"targets tested",tested,"hits",hits)
