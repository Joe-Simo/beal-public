"""U244 — SYSTEMATIC instance closure. A Beal signature (x,y,z), all exponents >=3, is an instance of a
SOLVED signature (P,Q,R) when, for some permutation, P|x, Q|y, R|z: then a^x=(a^(x/P))^P etc.
If (P,Q,R) has NO primitive solutions, (x,y,z) is closed outright. If it has a finite solution LIST,
the list must be checked for entries whose coordinates are the required perfect powers.
Solved rows are taken ONLY from survey arXiv:2412.11933 Table 1.1 (held in references/U130/)."""
from itertools import permutations, combinations_with_replacement
def primes(n): return [p for p in range(3,n+1) if all(p%d for d in range(2,int(p**.5)+1))]
RED=sorted(set([4]+primes(40)))

# solved (P,Q,R) families from survey Table 1.1, as predicates on an ORDERED triple
NO_SOL=[   # families with NO non-trivial primitive solutions
 ("(n,n,2), n>=5",      lambda P,Q,R: P==Q>=5 and R==2),
 ("(n,n,3), n>=3",      lambda P,Q,R: P==Q>=3 and R==3),
 ("(n,n,n), n>=3",      lambda P,Q,R: P==Q==R>=3),
 ("(2,4,n), n>=5",      lambda P,Q,R: P==2 and Q==4 and R>=5),
 ("(2,6,n), n>=3",      lambda P,Q,R: P==2 and Q==6 and R>=3),
 ("(3,3,n), n<=1e9",    lambda P,Q,R: P==3 and Q==3 and 3<=R<=10**9),
 ("(3,3,2n), n>=2",     lambda P,Q,R: P==3 and Q==3 and R%2==0 and R>=4),
 ("(3,6,n), n>=3",      lambda P,Q,R: P==3 and Q==6 and R>=3),
 ("(4,2n,3), n>=2",     lambda P,Q,R: P==4 and Q%2==0 and Q>=4 and R==3),
 ("(2,2n,3), n<=1e7",   lambda P,Q,R: P==2 and Q%2==0 and 3<=Q//2<=10**7 and R==3),
 ("(2n,2n,5), n>=2",    lambda P,Q,R: P==Q and P%2==0 and P>=4 and R==5),
 ("(3,4,5)",            lambda P,Q,R: (P,Q,R)==(3,4,5)),
 ("(5,5,7)/(5,5,19)/(7,7,5)", lambda P,Q,R: (P,Q,R) in {(5,5,7),(5,5,19),(7,7,5)}),
]
FINITE_LIST=[("(2,3,7) PSS", (2,3,7))]   # complete but non-empty solution list -> needs a value check
def closes(x,y,z):
    for P,Q,R in permutations((x,y,z)):
        pass
    for xx,yy,zz in set(permutations((x,y,z))):
        for name,f in NO_SOL:
            # find divisors P|xx, Q|yy, R|zz with the family predicate
            for P in [d for d in range(2,xx+1) if xx%d==0]:
                for Q in [d for d in range(2,yy+1) if yy%d==0]:
                    for R in [d for d in range(2,zz+1) if zz%d==0]:
                        if f(P,Q,R): return "%s via (%d,%d,%d)|(%d,%d,%d)"%(name,P,Q,R,xx,yy,zz)
    return None
def finite_instance(x,y,z):
    out=[]
    for xx,yy,zz in set(permutations((x,y,z))):
        for name,(P,Q,R) in FINITE_LIST:
            if xx%P==0 and yy%Q==0 and zz%R==0: out.append("%s as (%d,%d,%d)"%(name,xx,yy,zz))
    return out
openset=[]; closed_by=[]; needs_check=[]
for t in combinations_with_replacement(RED,3):
    if 1/t[0]+1/t[1]+1/t[2]>=1: continue
    c=closes(*t)
    if c: closed_by.append((t,c)); continue
    fi=finite_instance(*t)
    if fi: needs_check.append((t,fi)); continue
    openset.append(t)
print("reduced hyperbolic signatures with exponents in {4} u odd primes <= 37")
print("  closed by a NO-SOLUTION instance :",len(closed_by))
print("  reduce to a FINITE-LIST instance :",len(needs_check))
print("  still open                        :",len(openset))
print("\nsmallest closed-by-instance (first 8):")
for t,c in closed_by[:8]: print("   ",t,"<-",c)
print("\nfinite-list instances needing a value check:")
for t,fi in needs_check[:10]: print("   ",t,"<-",fi)
print("\nsmallest still open (first 12):",openset[:12])
