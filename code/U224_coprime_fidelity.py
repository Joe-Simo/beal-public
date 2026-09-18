"""U224 — Jev screen #2, narrowed to the ONE fidelity question that matters most: does each theorem
assume a coprimality condition STRONGER than Beal's gcd(gcd(A,B),C)=1, or exclude base 1?
Only files flagged >=0.5 on coprime_swap or base_one in U223 are re-screened, question by question,
with the root definition supplied so Jev can compare against it."""
import json,sys
sys.path.insert(0,'code'); import jev
DEF=open('formal/Beal/Conjecture.lean').read()[:6000]
FILES=["Necessary","FourTwoNFive","Residual","SameOddPrime","SixTwoNThree","ClosedFamilies",
       "EvenEvenThree","Structure","GaussianPow","MordellFixedBase","FixedBasesExample","Mihailescu"]
CTX=("Beal's conjecture hypothesis is ONLY gcd(gcd(A,B),C)=1 (a common prime divides all three). "
 "It does NOT give pairwise coprimality as an assumption. Pairwise coprimality is a THEOREM derivable from it "
 "(Beal/Structure.lean: gcd_ab_eq_one etc). So a theorem that ASSUMES Nat.Coprime A B is fine ONLY if it is applied "
 "via that derivation; it is a fidelity defect if a file states a headline 'no Beal counterexample' result whose "
 "hypothesis is pairwise coprimality supplied from nowhere. Bases may equal 1 unless excluded by a cited result.")
Q={"assumes_pairwise":jev.noul("Does a headline theorem in this file take pairwise coprimality (e.g. Nat.Coprime A B) as an INPUT hypothesis rather than deriving it from gcd(gcd(A,B),C)=1?",true="assumes it as input",false="derives it or does not need it"),
 "derivation_present":jev.noul("Does the file (or an explicit call it makes) derive that coprimality from the Beal gcd condition?",true="derivation present",false="no derivation visible"),
 "base_one_excluded":jev.noul("Does a theorem silently require a base >= 2 or > 1 without citing the base-one exclusion result?",true="silently excludes base 1",false="base 1 handled or irrelevant")}
reqs=[{"context":CTX,"beal_definition_file":DEF,"filename":f,"lean_source":open('formal/Beal/%s.lean'%f).read()[:13000]} for f in FILES]
rs=jev.ask_many(reqs,Q,concurrency=12)
rows=[]
for f,r in zip(FILES,rs):
    if 'answers' not in r: print("ERR",f); continue
    a={k:round(v['noul'],2) for k,v in r['answers'].items()}
    rows.append((round(a['assumes_pairwise']*(1-a['derivation_present']),2),a,f))
rows.sort(key=lambda r:-r[0])
json.dump({"status":"HYPOTHESIS_ONLY","rows":rows},open('research/pool/evidence/coprime_fidelity_U224.json','w'),indent=1)
for s,a,f in rows: print(s,f,a)
