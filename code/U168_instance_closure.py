"""U168 — systematic 'instance of a closed lower signature' check (lesson of U167).
Our equation: T1 + T2 - T3 = 0 with exponents (x,y,z), all >=3, reduced to {4} U odd primes.
A literature row (a,b,c) means R1^a + R2^b - R3^c = 0 has NO coprime nonzero INTEGER solutions.
(x,y,z) is an instance of the row if some bijection of our terms onto row slots has: row exponent | our
exponent, and -- up to a global sign -- every term whose sign differs from its slot sits on an ODD row
exponent (the sign is absorbed into the base).  Rows that are 'solved with solutions' are listed apart."""
import itertools, json
# SOURCE COVERAGE (U336, pool C192): of the 17 rows below, 14 have their primary source held in
# references/U130/ and located by code/U332_rows_source_check.py. Three do not:
#   (2,6,n) Bennett-Chen   -- never fires on a reduced signature; inert, and its source is not held
#   (2,n,6)                -- CORRECTION (U337, pool C193): this row IS sourced. It appears verbatim
#                             in BCDY Theorem 1, which is held as references/U130/bcdy.txt. My U336
#                             audit listed it as unsourced; that was wrong, and the error is kept
#                             here rather than silently deleted.
#   (13,13,5) arXiv:2510.12092 -- FIRES, and is the ONLY load-bearing row without a held source.
# So only ONE row is both load-bearing and unsourced, not two as U336 first said.
# It closes exactly 2 of the 74 closed signatures, (13,13,5) and (5,13,13); removing it leaves 72
# and reverts those two to OPEN. The (3,4,4) row rests on the survey rather than on Cohen's book,
# which is also not held -- but that row is now superseded by the machine-checked
# Beal.three_four_four_same_parity plus the Euler gap (pool C168, C172, C177).
#
# ---------------------------------------------------------------------------------------------
# UNSTATED DEPENDENCY, found by the U332/U333 primary-source check and recorded here (pool C189).
#
# The sources these rows cite close only the NON-TRIVIAL solutions. Darmon-Merel says so in as
# many words: "a solution is called trivial if xyz = 0 or +-1". So a row taken from them does NOT
# by itself dispose of a Beal case with a base equal to 1 -- and the target discipline for this
# project forbids silently excluding a base of 1.
#
# That case is genuinely covered, but ELSEWHERE and by a different theorem: 1 + B^y = C^z with
# y, z >= 3 is Catalan's equation, closed by Mihailescu. In this repository that lives in
# formal/Beal/Mihailescu.lean (beal_base_a_ne_one, beal_base_b_ne_one,
# beal_counterexample_base_ne_one, beal_counterexample_bases_ge_two), all of them taking the named
# hypothesis MihailescuTheorem.
#
# So every "closed" verdict below carries the implicit rider: closed for bases >= 2 by the cited
# row, and for a base of 1 by Mihailescu. Neither half may be dropped.
# ---------------------------------------------------------------------------------------------
NOSOL = {  # rows with NO coprime nonzero integer solutions (BCDY 2015 Tables 1-2; survey 2412.11933 Table 1.1)
 "(n,n,n) Wiles": lambda a,b,c: a==b==c and a>=3,
 "(n,n,2) DM/Poonen n>=4": lambda a,b,c: a==b and a>=4 and c==2,
 "(n,n,3) DM/Poonen n>=3": lambda a,b,c: a==b and a>=3 and c==3,
 "(2,4,n) BEN n>=4": lambda a,b,c: a==2 and b==4 and c>=4,
 "(2,6,n) Bennett-Chen n>=3": lambda a,b,c: a==2 and b==6 and c>=3,
 "(2,n,4) n>=4": lambda a,b,c: a==2 and c==4 and b>=4,
 "(2,n,6) n>=3": lambda a,b,c: a==2 and c==6 and b>=3,
 "(3,3,2n) BCDY n>=2": lambda a,b,c: a==3 and b==3 and c%2==0 and c>=4,
 "(3,6,n) BCDY n>=2": lambda a,b,c: a==3 and b==6 and c>=2,
 "(4,2n,3) BCDY n>=2": lambda a,b,c: a==4 and b%2==0 and b>=4 and c==3,
 "(2n,2n,5) Bennett n>=2": lambda a,b,c: a==b and a%2==0 and a>=4 and c==5,
 "(3,4,5) Siksek-Stoll": lambda a,b,c: (a,b,c)==(3,4,5),
 "(5,5,7),(5,5,19),(7,7,5) Dahmen-Siksek": lambda a,b,c: (a,b,c) in {(5,5,7),(5,5,19),(7,7,5)},
 "(13,13,5) arXiv:2510.12092 [SOURCE NOT HELD in references/U130 -- see pool C192]": lambda a,b,c: (a,b,c)==(13,13,5),
 "(3,3,n) 3<=n<=10^9": lambda a,b,c: a==3 and b==3 and 3<=c<=10**9,
 "(3,4,4) Cohen GTM240 Prop 14.6.6 (+ rank-0 re-derivation U168)": lambda a,b,c: (a,b,c)==(3,4,4),
 "(2,3,7) PSS: no solution with a square x (checked against the full list)": lambda a,b,c: (a,b,c)==(4,3,7),
}
def divisors(n): return [d for d in range(2,n+1) if n%d==0]
def instance(sig):
    ours=[(sig[0],+1),(sig[1],+1),(sig[2],-1)]
    for perm in itertools.permutations(range(3)):
        for da in divisors(ours[perm[0]][0]):
          for db in divisors(ours[perm[1]][0]):
            for dc in divisors(ours[perm[2]][0]):
                row=(da,db,dc); slots=(+1,+1,-1)
                for name,f in NOSOL.items():
                    if not f(*row): continue
                    for g in (+1,-1):
                        ok=all(ours[perm[i]][1]*g==slots[i] or row[i]%2==1 for i in range(3))
                        if ok: return name,row,perm
    return None
P=[3,4,5,7,11,13,17,19]
open_,closed=[],{}
for sig in itertools.product(P,repeat=3):
    if sig[0]>sig[1]: continue            # A,B symmetric
    r=instance(sig)
    if r: closed[sig]=r[0]
    else: open_.append(sig)
print("reduced signatures tested:",len(closed)+len(open_)," closed by instance:",len(closed)," open:",len(open_))
from collections import Counter
print(Counter(closed.values()).most_common())
print("OPEN containing a 4:",[s for s in open_ if 4 in s][:40])
print("OPEN all odd, smallest:",[s for s in open_ if 4 not in s][:25])
# --- CONSERVATIVE COUNT (U338, pool C194) -------------------------------------------------
# One row is load-bearing and has no held primary source: (13,13,5), arXiv:2510.12092. At $0 the
# paper cannot be fetched, so the honest thing is to report BOTH counts every run and let the
# reader choose which to rely on, rather than quietly using the larger one.
UNSOURCED = [k for k in NOSOL if "SOURCE NOT HELD" in k]
cons_closed = {k: v for k, v in closed.items() if v not in UNSOURCED}
reverted = sorted(set(closed) - set(cons_closed))
print(f"CONSERVATIVE (dropping rows with no held source {UNSOURCED}): "
      f"closed {len(cons_closed)}, open {len(open_) + len(reverted)}")
print(f"  signatures that revert to OPEN: {reverted}")
assert len(reverted) == 2, f"expected exactly 2 reverting signatures, got {reverted}"

json.dump({"closed":{str(k):v for k,v in closed.items()},"open":open_,
           "conservative_closed":{str(k):v for k,v in cons_closed.items()},
           "reverted_without_unsourced_rows":[str(k) for k in reverted]},
          open("research/pool/evidence/instance_closure_U168.json","w"))
