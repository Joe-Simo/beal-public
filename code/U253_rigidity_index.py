"""U253 — EXACT test of the top U252 cell: rigid local systems on P^1 minus {0,1,inf} with local
monodromy of orders (x,y,z). Katz rigidity index for rank n and k=3 punctures:
    rig = (2-k) n^2 + sum_i dim Z(C_i) = -n^2 + sum_i sum_j m_{ij}^2 ,
where at puncture i the local monodromy is semisimple with eigenvalue multiplicities m_{i1},...
It is RIGID iff rig = 2. Exact integer enumeration over all multiplicity partitions."""
from itertools import combinations_with_replacement
def partitions(n, maxp=None):
    if maxp is None: maxp=n
    if n==0: yield ()
    for p in range(min(n,maxp),0,-1):
        for rest in partitions(n-p,p): yield (p,)+rest
print("rank n | rigid multiplicity triples (partitions of n at 0, 1, inf) with rig = 2")
for n in range(1,9):
    parts=list(partitions(n))
    found=[]
    for a in parts:
        for b in parts:
            for c in parts:
                rig=-n*n+sum(x*x for x in a)+sum(x*x for x in b)+sum(x*x for x in c)
                if rig==2: found.append((a,b,c))
    # a local monodromy of ORDER e >= 3 with distinct eigenvalues needs at least ... report the
    # maximum number of distinct eigenvalues available at each puncture
    reg=[f for f in found if all(all(m==1 for m in t) for t in f)]
    print("n=%d : %d rigid triples total; %d with ALL local monodromies regular semisimple"%(n,len(found),len(reg)))
    if reg: print("        regular-semisimple ones:",reg)
print()
print("CONSEQUENCE (exact): if every local monodromy is regular semisimple (n distinct eigenvalues,")
print("which is what 'local monodromy of order x, y, z with x,y,z >= 3 acting with distinct")
print("eigenvalues' gives), then rig = -n^2 + 3n = 2, so n = 1 or n = 2 ONLY.")
for n in range(1,9): print("   n=%d -> rig = %d"%(n,-n*n+3*n))
