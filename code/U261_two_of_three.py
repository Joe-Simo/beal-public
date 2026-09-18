"""U261 — sharpest formulation. In a rigid local system of rank n on P^1-{0,1,inf}, how many
punctures can be REGULAR SEMISIMPLE (n distinct eigenvalues, the state that carries a full
exponent)? Exact enumeration over multiplicity partitions."""
def partitions(n,maxp=None):
    if maxp is None: maxp=n
    if n==0: yield ()
    for p in range(min(n,maxp),0,-1):
        for rest in partitions(n-p,p): yield (p,)+rest
print(" n | max # regular-semisimple punctures | when exactly 2 are, the third has k eigenvalues")
for n in range(2,13):
    P=list(partitions(n)); best=0; thirds=set()
    for a in P:
        for b in P:
            for c in P:
                if -n*n+sum(x*x for x in a)+sum(x*x for x in b)+sum(x*x for x in c)!=2: continue
                rs=sum(1 for t in (a,b,c) if len(t)==n)
                best=max(best,rs)
                if rs==2:
                    third=[t for t in (a,b,c) if len(t)!=n]
                    if third: thirds.add(len(third[0]))
    print("%2d | %-33d | %s"%(n,best,sorted(thirds) if thirds else "-"))
print()
print("THEOREM (exact, n = 2..12): a rigid local system of rank n >= 3 has AT MOST TWO")
print("regular-semisimple punctures, and when exactly two are regular semisimple the third has")
print("exactly 2 distinct eigenvalues. Proof of the bound: two regular-semisimple punctures")
print("already use 2n of the 2n+2 eigenvalue budget (C121), leaving at most 2 for the third;")
print("three would need 3n > 2n+2 for n > 2.")
