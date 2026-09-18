"""U245 — EXPLOITATION of C105. For signature (3,3,z) under KrausProp7 we are always in the p-adic
branch, so with C = 3^w * u * v, 3 not dividing u*v:
    A+B = 3^(zw-1) * u^z ,    A^2-AB+B^2 = 3 * v^z .
Writing S=A+B, P=AB:  S^2 - 3P = 3 v^z, so P = (S^2 - 3 v^z)/3, and A,B are the roots of
T^2 - S T + P, which are POSITIVE INTEGERS iff S^2-4P is a perfect square and 0 < P <= S^2/4.
This is an EXACT finite test for each (z,w,u). Exact integer arithmetic only.
CATEGORY: bounded computation / elementary descent — survey-dead. Reported as structure, not progress."""
from math import isqrt
def iroot(n,k):
    if n<0: return -1
    lo,hi=0,1
    while hi**k<=n: hi*=2
    while lo<hi-1:
        m=(lo+hi)//2
        if m**k<=n: lo=m
        else: hi=m
    return lo
tot=0; sols=[]
print("z   w   u   v-candidates in the forced window   integer (A,B) found")
for z in (5,7,11,13):
    for w in (1,2):
        for u in (1,2,4,5):
            if u%3==0: continue
            S=3**(z*w-1)*u**z
            # 1 <= P <= S^2/4  and  3 v^z = S^2 - 3P  =>  v^z in [(S^2-3*floor(S^2/4))/3, (S^2-3)/3]
            lo=(S*S-3*(S*S//4)+2)//3
            hi=(S*S-3)//3
            vlo=iroot(max(lo-1,0),z)+1; vhi=iroot(hi,z)
            cands=[v for v in range(max(vlo,1),vhi+1) if v%3]
            found=[]
            for v in cands:
                num=S*S-3*v**z
                if num<=0 or num%3: continue
                P=num//3
                if P<1: continue
                D=S*S-4*P
                if D<0: continue
                r=isqrt(D)
                if r*r!=D: continue
                A=(S+r)//2; B=(S-r)//2
                if A>0 and B>0 and (S+r)%2==0 and A**3+B**3==(3**w*u*v)**z: found.append((A,B,v))
            tot+=len(cands)
            print("%-3d %-3d %-3d %-34s %s"%(z,w,u,"%d cands (v in [%d,%d])"%(len(cands),vlo,vhi),found if found else "none"))
            sols+=found
print("\ntotal v-candidates examined:",tot,"  solutions found:",len(sols))
print("Consistency control — the descent must REPRODUCE a known identity when the hypotheses are dropped.")
print("  1^3+2^3=9=3^2 has z=2 (excluded here: z>=3), S=3, and 3 | C: S=3=3^(2*1-1)*1^2 with w=1,u=1 -> v^2=(9-3*P)/3 with P=2 gives v^2=1, v=1, C=3*1*1=3. Check:",1**3+2**3==3**2)
