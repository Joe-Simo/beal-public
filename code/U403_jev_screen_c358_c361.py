"""Jev screen for Candidates C358-C361.
Screening:
- C358: Kraus Sieve for (3, 3, p) on p in [4301, 4400]
- C359: Arakelov-Mumford-Parshin Arithmetic Threefolds & (omega)^3 Height Bounds
- C360: Universal Euler Systems & Beilinson-Flach Elements for Triangle Orbifolds
- C361: Arithmetic Invariant Theory & Bhargava Orbits on Fermat Hypersurfaces
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

CANDIDATES = {
    "C358": {
        "title": "KRAUS SIEVE MODULAR METHOD EXTENSION FOR SIGNATURE (3, 3, p) ON [4301, 4400]",
        "claim": "No non-trivial primitive solutions exist for signature (3, 3, p) for all prime exponents p in [4301, 4400].",
        "method": "Modular method level lowering to conductor 72, Kraus sieve relations at auxiliary primes q = 2kp + 1 with a_q(f) = 0 mod 2.",
        "category": "dead_category_bounded_sieve",
    },
    "C359": {
        "title": "ARAKELOV-MUMFORD-PARSHIN ARITHMETIC THREEFOLDS AND (omega)^3 HEIGHT BOUNDS",
        "claim": "The arithmetic self-intersection of the relative dualizing sheaf (omega)^3 on the arithmetic threefold fibered by triangle orbifolds unconditionally bounds heights of primitive points.",
        "method": "Higher-dimensional Arakelov intersection theory (Parshin, Moret-Bailly) on arithmetic schemes fibered over modular curves.",
        "category": "effective_diophantine_geometry",
    },
    "C360": {
        "title": "UNIVERSAL EULER SYSTEMS AND BEILINSON-FLACH ELEMENTS FOR TRIANGLE ORBIFOLDS",
        "claim": "Beilinson-Flach Euler systems in rank 4 motivic cohomology annihilate the global Selmer group of Frey Galois representations even when S = primes(ABC) is unbounded.",
        "method": "Kato / Kings-Loeffler-Zerbes Euler system machinery applied to products of modular curves parameterizing Beal solutions.",
        "category": "unifying_modular_motivic_geometry",
    },
    "C361": {
        "title": "ARITHMETIC INVARIANT THEORY AND BHARGAVA ORBITS ON FERMAT HYPERSURFACES",
        "claim": "Higher composition laws and integer orbits under coregular group actions bound primitive integral solutions on generalized Fermat hypersurfaces.",
        "method": "Bhargava's geometry-of-numbers techniques and coregular representations applied to binary forms and Fermat invariants.",
        "category": "effective_diophantine_geometry",
    },
}

QUESTIONS = {
    "relevance": jev.score(
        "How directly does this candidate address the general Beal conjecture across arbitrary triples (p, q, r) >= 3?",
        [
            "level 0: Settle only bounded prime exponents or dead category computation with no general leverage.",
            "level 1: Relevant to a single signature family or requires bounded bad reduction.",
            "level 2: Provides structural constraints applicable to infinite families with unbounded exponents.",
            "level 3: Directly attacks the general Beal conjecture for all (p, q, r) >= 3 via uniform Diophantine geometry.",
        ],
    ),
    "fc_blindness": jev.noul(
        "Is this candidate's mathematical mechanism blind to exponent 2 (i.e. does it also hold for Fermat-Catalan identities with exponent 2)?",
        true="The mechanism holds on all Fermat-Catalan identities with exponent 2, hence cannot prove Beal on its own.",
        false="The mechanism strictly exploits the Beal hyperbolic defect -chi >= 1/12 (which fails on Fermat-Catalan) or specific exponent >= 3 geometry.",
    ),
    "dead_category": jev.noul(
        "Does this candidate fall into a known dead category (bounded sieves, modular method one signature at a time, elementary congruences, abc/Baker)?",
        true="Yes, it is in a known dead category incapable of proving the full conjecture.",
        false="No, it explores live directions such as effective Diophantine geometry on orbifolds or unifying motivic objects.",
    ),
    "action": jev.choice(
        "What is the recommended next action for this candidate in the research loop?",
        {
            "exploit_bounded": "Execute exact computation or Kraus sieve verification to advance empirical milestone bounds.",
            "audit_obstruction": "Perform rigorous primary-source mathematical audit to expose fundamental structural obstruction.",
            "refute": "Refute the candidate due to heuristic laundering or geometric impossibility.",
            "pursue_frontier": "Actively develop as the leading mathematical frontier for unconditional Diophantine bounds.",
        },
    ),
}

def main():
    print("Executing Jev screen for C358-C361...")
    cids = list(CANDIDATES.keys())
    states = []
    for cid in cids:
        data = CANDIDATES[cid]
        state = (
            f"Candidate: {cid} - {data['title']}\n"
            f"Claim: {data['claim']}\n"
            f"Method: {data['method']}\n"
            f"Category: {data['category']}\n"
            f"Context: Beal conjecture requires x, y, z >= 3. Fermat-Catalan identities have exponent 2 and defect -chi <= 1/18, while Beal has -chi >= 1/12."
        )
        states.append(state)

    results = jev.ask_many(states, QUESTIONS, concurrency=4)

    evidence_dir = Path(__file__).resolve().parent.parent / "research" / "pool" / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)

    print("\n--- JEV SCREEN RESULTS ---")
    for cid, state, resp in zip(cids, states, results):
        print(f"\nCandidate {cid}:")
        if "error" in resp:
            print(f"  ERROR: {resp['error']}")
            continue
        answers = resp.get("answers", {})
        for qname, qans in answers.items():
            if qans.get("type") == "score":
                print(f"  {qname}: score={qans.get('score')} (conf={qans.get('confidence')})")
            elif qans.get("type") == "noul":
                print(f"  {qname}: value={qans.get('value')} (conf={qans.get('confidence')})")
            elif qans.get("type") == "choice":
                print(f"  {qname}: choice={qans.get('choice')} (conf={qans.get('confidence')})")

        p = jev.persist(cid, state, QUESTIONS, resp)
        print(f"  Persisted evidence to {p.name}")

if __name__ == "__main__":
    main()
