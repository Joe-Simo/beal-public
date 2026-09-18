"""U232 — COUNTERSEARCH: apply gate 2 (C094) to the machine-checked kernel conditions.
For each condition, test it on GENERIC coprime triples a+b=c whose terms are NOT all perfect powers.
A condition that holds on those uses only the equation + coprimality, not the power structure.
A condition that FAILS on some of them genuinely needs the exponents. Exact integers only."""
from math import gcd
def ipp(n):
    if n<2: return n==1
    for k in range(2,n.bit_length()+1):
        lo,hi=1,1
        while hi**k<=n: hi*=2
        while lo<hi-1:
            m=(lo+hi)//2
            if m**k<=n: lo=m
            else: hi=m
        if lo**k==n: return True
    return False
# generic coprime triples a+b=c, none of a,b,c a perfect power
GEN=[(a,b,a+b) for a in range(2,200) for b in range(a+1,200)
     if gcd(a,b)==1 and not ipp(a) and not ipp(b) and not ipp(a+b)]
# genuine power triples with exponents>=3 do not exist (that is the conjecture); use the
# exponent-2 Fermat-Catalan set as the closest available power triples
FC=[(1,1,2,3,3,2),(2,5,7,2,3,4),(7,3,13,2,2,9),(2,7,17,3,71,2),(3,5,11,4,122,2),
    (33,8,1549034,2,15613,3),(1414,3,2213459,2,65,7),(9262,3,15312283,2,113,7),
    (17,7,76271,3,21063928,2),(43,8,96222,3,30042907,2)]
COND={
 "pairwise coprime (gcd_ab/ac/bc)":       lambda a,b,c: gcd(a,b)==1 and gcd(a,c)==1 and gcd(b,c)==1,
 "no cancellation: c>max(a,b)":           lambda a,b,c: c>max(a,b),
 "size window: c<2*max(a,b)":             lambda a,b,c: c<2*max(a,b),
 "exactly one of a,b,c even":             lambda a,b,c: [a%2,b%2,c%2].count(0)==1,
 "8 | a+b when c even":                   lambda a,b,c: (c%2!=0) or ((a+b)%8==0),
 "c not div by 3 when 3|a and 3|b":       lambda a,b,c: not(a%3==0 and b%3==0) or c%3!=0,
}
print("%-38s %-22s %s"%("kernel condition","holds on GENERIC","holds on Fermat-Catalan"))
for name,f in COND.items():
    g=sum(1 for a,b,c in GEN if f(a,b,c)); G=len(GEN)
    fc=sum(1 for A,x,B,y,C,z in FC if f(A**x,B**y,C**z))
    print("%-38s %6d/%-6d (%5.1f%%)   %d/10"%(name,g,G,100*g/G,fc))
print("\nGATE 2 reading: a condition holding on ~100%% of the %d generic non-power triples uses only"%len(GEN))
print("the equation and coprimality of the VALUES; it carries no perfect-power content.")
