"""Cycle U127 — COUNTERSEARCH via the ring where Beal FAILS.
Helenius: (-2+i)^3 + (-2-i)^3 = (1+i)^4 in Z[i], bases pairwise coprime (norms 5,5,2).
Every constraint we have proved over Z is tested here through its norm analogue. A constraint
whose norm analogue FAILS on this identity is one that any proof of Beal must draw from the
ordering/positivity of Z, not from ring structure alone. Exact Gaussian arithmetic only."""
import sys; sys.path.insert(0,'code'); import jev
def mul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def pw(a,k):
    r=(1,0)
    for _ in range(k): r=mul(r,a)
    return r
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def N(a): return a[0]*a[0]+a[1]*a[1]
A,B,C=(-2,1),(-2,-1),(1,1); x,y,z=3,3,4
lhs=add(pw(A,x),pw(B,y)); rhs=pw(C,z)
print("A^x =",pw(A,x)," B^y =",pw(B,y)," sum =",lhs," C^z =",rhs," equal:",lhs==rhs)
print("norms: N(A^x)=",N(pw(A,x))," N(B^y)=",N(pw(B,y))," N(C^z)=",N(rhs))
tests={
 "no_cancellation  N(C^z) <= 2*max(N(A^x),N(B^y))": N(rhs)<=2*max(N(pw(A,x)),N(pw(B,y))),
 "no_cancellation  N(C^z) >  max(N(A^x),N(B^y))  (sum exceeds each summand)": N(rhs)>max(N(pw(A,x)),N(pw(B,y))),
 "C smallest (by norm) => z > max(x,y)": (not (N(C)<N(A) and N(C)<N(B))) or z>max(x,y),
 "dominant dichotomy: N(B^y)<=N(A^x) => (z<=x iff N(A)<N(C))": (not N(pw(B,y))<=N(pw(A,x))) or ((z<=x)==(N(A)<N(C))),
 "exactly one base 'even' (divisible by 1+i)": sum(1 for t in (A,B,C) if N(t)%2==0)==1,
 "not both x,y even when C even": (N(C)%2) or not (x%2==0 and y%2==0),
}
for k,v in tests.items(): print(f"{'HOLDS ' if v else 'FAILS '} {k}")
CTX="Helenius identity in Z[i] refutes the Beal statement there. Norm analogues of the verified Z-constraints were tested exactly."
Q={"essential":jev.noul("Is the FAILING constraint (no-cancellation: the sum must exceed each summand) the ingredient any proof of Beal over Z must essentially use, beyond ring structure?",true="yes, ordering is essential",false="no, a ring-theoretic proof could avoid it")}
r=jev.ask({"context":CTX,"failing":[k for k,v in tests.items() if not v],"holding":[k for k,v in tests.items() if v]},Q)
jev.persist("C043",{"context":CTX},Q,r); print("Jev (HYPOTHESIS_ONLY):",r.get("answers"))
