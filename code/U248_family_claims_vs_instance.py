"""U248 — for every FAMILY the milestone layer claims to resolve, test whether simple INSTANCE
CLOSURE (C107) already gives it from held sources. A family closable that way needs none of the
modular machinery; one that is NOT closable that way rests entirely on an unauditable route."""
FAMILIES=[
 ("(2k,4m,n), k>=2,m>=1,n>=4", "verify_qcurves_modular_forms.py"),
 ("(4k,4m,n), k,m>=1,n>=2",    "verify_qcurves_modular_forms.py"),
 ("(4,4,p), p>=3",             "U111_hilbert_forms_q_sqrt2.gp"),
 ("(3,3,p), p<=700",           "U111_kraus_sieve_p601_p700.py"),
 ("(2,4,n), n>=4",             "U110_signature_2_4_n_modular_verification.py"),
 ("(5,5,p), p prime",          "U111_signature_5_5_p_hilbert_sieve.py"),
 ("(p,q,r) general, p,q,r>=3", "U111_general_cartan_elimination.py"),
]
# held no-solution rows (survey Table 1.1 / BCDY Table 1)
HELD=[("(n,n,2), n>=4  Darmon-Merel",   lambda P,Q,R: P==Q>=4 and R==2),
      ("(n,n,3), n>=3",                 lambda P,Q,R: P==Q>=3 and R==3),
      ("(n,n,n), n>=3  Fermat",         lambda P,Q,R: P==Q==R>=3),
      ("(2,4,n), n>=4",                 lambda P,Q,R: P==2 and Q==4 and R>=4),
      ("(4,4,2) Fermat right triangle", lambda P,Q,R: P==4 and Q==4 and R==2),
      ("(3,3,n), n<=1e9",               lambda P,Q,R: P==3 and Q==3 and 3<=R<=10**9),
      ("(4,2n,3), n>=2",                lambda P,Q,R: P==4 and Q%2==0 and Q>=4 and R==3)]
def divisors(n): return [d for d in range(2,n+1) if n%d==0]
from itertools import permutations
def instance_closes(x,y,z):
    for xx,yy,zz in set(permutations((x,y,z))):
        for name,f in HELD:
            for P in divisors(xx):
                for Q in divisors(yy):
                    for R in divisors(zz):
                        if f(P,Q,R): return "%s  [(%d,%d,%d) | (%d,%d,%d)]"%(name,P,Q,R,xx,yy,zz)
    return None
def sample(fam):
    if fam.startswith("(2k,4m,n)"): return [(2*k,4*m,n) for k in (2,3) for m in (1,2) for n in (4,5,7)]
    if fam.startswith("(4k,4m,n)"): return [(4*k,4*m,n) for k in (1,2) for m in (1,2) for n in (2,3,5,7)]
    if fam.startswith("(4,4,p)"):   return [(4,4,p) for p in (3,5,7,11,13)]
    if fam.startswith("(3,3,p)"):   return [(3,3,p) for p in (5,7,11,701)]
    if fam.startswith("(2,4,n)"):   return [(2,4,n) for n in (4,5,7)]
    if fam.startswith("(5,5,p)"):   return [(5,5,p) for p in (7,11,13,19,23)]
    return [(3,5,7),(4,5,7),(3,4,11),(5,7,11)]
for fam,script in FAMILIES:
    S=sample(fam); res=[(t,instance_closes(*t)) for t in S]
    ok=sum(1 for _,r in res if r); print("%-30s %-40s %d/%d members closed by instance closure"%(fam,script,ok,len(res)))
    for t,r in res:
        if r is None: print("      NOT closed by held sources:",t)
