"""U254 — EXPLOITATION of C120. For every RIGID triple of local multiplicity partitions on
P^1-{0,1,inf}, count the DISTINCT EIGENVALUES available at each puncture (= number of parts).
That number is the entire budget of exponent information the object can carry at that puncture:
a local monodromy of order x contributes at most (number of parts) of the x-th roots of unity.
Exact enumeration; no heuristics."""
def partitions(n,maxp=None):
    if maxp is None: maxp=n
    if n==0: yield ()
    for p in range(min(n,maxp),0,-1):
        for rest in partitions(n-p,p): yield (p,)+rest
print("n  | rigid triples | max eigenvalue budget (parts) at the three punctures | example")
for n in range(1,10):
    parts=list(partitions(n)); best=None; cnt=0; budgets=set()
    for a in parts:
        for b in parts:
            for c in parts:
                if -n*n+sum(x*x for x in a)+sum(x*x for x in b)+sum(x*x for x in c)==2:
                    cnt+=1; t=(len(a),len(b),len(c)); budgets.add(tuple(sorted(t)))
                    if best is None or sum(t)>sum(best[1]): best=((a,b,c),t)
    mx=max(budgets,key=sum) if budgets else None
    print("%-2d | %-13d | %-18s | %s"%(n,cnt,mx,best[0] if best else None))
print()
print("Reading: at a puncture with k distinct eigenvalues the local monodromy of order x can only")
print("use k of the x-th roots of unity. For k = 2 the object distinguishes at most 'some primitive")
print("x-th root vs 1', which is the classical rank-2 hypergeometric situation. A rigid object of")
print("rank n >= 3 must have SOME puncture with fewer parts than n, i.e. a repeated eigenvalue.")
print()
print("Exact check of the key inequality: for a rigid triple, sum of parts-counts vs 3n")
for n in range(2,10):
    parts=list(partitions(n)); tot=[]
    for a in parts:
        for b in parts:
            for c in parts:
                if -n*n+sum(x*x for x in a)+sum(x*x for x in b)+sum(x*x for x in c)==2:
                    tot.append(len(a)+len(b)+len(c))
    if tot: print("   n=%d : max total distinct eigenvalues = %d  (regular semisimple would need %d)"%(n,max(tot),3*n))
