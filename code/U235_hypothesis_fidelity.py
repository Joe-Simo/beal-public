"""U235 — primary-source fidelity screen on every NAMED HYPOTHESIS. For each Lean `def ... : Prop`
that stands for a published theorem, ask whether the Lean statement is STRONGER than what the cited
paper proves (the dangerous direction: a too-strong hypothesis silently assumes the conjecture)."""
import re,json,sys,glob
sys.path.insert(0,'code'); import jev
SRC={"BennettSkinnerThree":"bennett_skinner","BCDYFourTwoNThree":"bcdy","BCDYThreeThreeTwoN":"bcdy",
 "DarmonMerelNN2":"darmon_merel","DarmonMerelNN2Int":"darmon_merel","DarmonMerelNN3":"darmon_merel",
 "DahmenSiksek":"dahmen_siksek","BEN24n":"ben2010","BruinClassification238":"survey",
 "FreitasTheoremMod3":"survey","KrausEvenCLevel18Newform":"survey","MihailescuTheorem":"survey",
 "Mordell27":"mordell27_pari_output","Quartic400g2":"four_2n_five_pari_output","Quartic400b2":"four_2n_five_pari_output",
 "FLTHyp":"survey"}
def grab(name):
    for f in glob.glob('formal/Beal/*.lean'):
        s=open(f).read()
        m=re.search(r'(/--.*?-/\s*)?def %s : Prop :=(.*?)(?=\n\n|\ndef |\ntheorem |\nlemma )'%name, s, re.S)
        if m: return (m.group(1) or '')+ 'def %s : Prop :=%s'%(name,m.group(2))
    return None
CTX=("Beal repo. Each Lean `def ... : Prop` below stands for a PUBLISHED theorem and is passed as an explicit "
 "hypothesis, never asserted. DANGER: if the Lean Prop is STRONGER than what the cited paper actually proves, the "
 "conditional results built on it are worthless (they would assume part of Beal). Judge the Lean statement against "
 "the supplied primary-source extract.")
Q={"stronger_than_source":jev.noul("Is the Lean Prop STRONGER than the theorem in the supplied source extract (wider exponent range, weaker coprimality hypothesis, more coefficients, or an unproved uniformity in a parameter)?",true="Lean Prop is stronger",false="matches or is weaker"),
 "source_present":jev.noul("Does the supplied extract actually contain the cited theorem?",true="theorem present in extract",false="not found in extract"),
 "assumes_beal":jev.noul("Would assuming this Prop directly give a Beal counterexample-free family that the paper does NOT claim?",true="over-assumes",false="no")}
reqs=[];names=[]
for n,src in SRC.items():
    lean=grab(n)
    if not lean: print("SKIP (not found)",n); continue
    try: txt=open('references/U130/%s.txt'%src).read()
    except FileNotFoundError: txt="(no extract saved)"
    names.append(n); reqs.append({"context":CTX,"hypothesis_name":n,"lean_statement":lean[:2500],"source_extract":txt[:16000]})
rs=jev.ask_many(reqs,Q,concurrency=8)
rows=[]
for n,r in zip(names,rs):
    if 'answers' not in r: print("ERR",n); continue
    a={k:round(v['noul'],2) for k,v in r['answers'].items()}
    rows.append((round(max(a['stronger_than_source'],a['assumes_beal']),2),a,n))
rows.sort(key=lambda r:-r[0])
json.dump({"status":"HYPOTHESIS_ONLY","rows":rows},open('research/pool/evidence/hypothesis_fidelity_U235.json','w'),indent=1)
for s,a,n in rows: print(s,n,a)
