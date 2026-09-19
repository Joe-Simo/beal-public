"""Jev screen for Candidates C394-C397 and Cyclotomic Chabauty Frontier.

Screening:
- C394: Kraus Sieve for (3, 3, p) on p in [5201, 5300]
- C395: Non-Abelian Chabauty over Cyclotomic Base Fields K = Q(zeta_m)
- C396: Relative Anabelian Geometry of P^1 \ {0, 1, \infty} over Spec Z
- C397: Arithmetic Chow Groups & Hyperkähler Periods of Fermat Hypersurfaces
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

CANDIDATES = {
    "C394": {
        "title": "KRAUS SIEVE MODULAR METHOD EXTENSION FOR SIGNATURE (3, 3, p) ON [5201, 5300]",
        "claim": "No non-trivial primitive solutions exist for signature (3, 3, p) for all prime exponents p in [5201, 5300].",
        "method": "Modular method level lowering to conductor 72, Kraus sieve relations at auxiliary primes q = 2kp + 1 with a_q(f) = 0 mod 2.",
        "category": "dead_category_bounded_sieve",
    },
    "C395": {
        "title": "CYCLOTOMIC NON-ABELIAN CHABAUTY-KIM OVER K = Q(zeta_m)",
        "claim": "Descent of unipotent Selmer variety Sel(U_n)(K) under Gal(K/Q) forces dim Sel(U_n)(K)^{Gal} < dim U_n(K_p)^{Gal} even for unbounded S = primes(ABC).",
        "method": "Non-abelian Chabauty-Kim, cyclotomic base change, Galois invariant Selmer varieties, Chabauty-Coleman integration.",
        "category": "effective_diophantine_geometry",
    },
    "C396": {
        "title": "RELATIVE ANABELIAN GEOMETRY OF P^1 \ {0, 1, infty} OVER SPEC Z",
        "claim": "Section conjecture and outer Galois representation into Out(pi_1^{et}(P^1 \ {0,1,infty})) isolate rational points with three-point ramification.",
        "method": "Anabelian geometry (Grothendieck, Mochizuki, Stix), étale fundamental groups, section conjecture.",
        "category": "unifying_modular_motivic_geometry",
    },
    "C397": {
        "title": "HYPERKÄHLER PERIOD MAPS AND ARITHMETIC CHOW GROUPS OF FERMAT HYPERSURFACES",
        "claim": "The Beauville-Bogomolov quadratic form on the primitive cohomology of hyperkähler varieties associated to Fermat covers bounds integer coordinates.",
        "method": "Arithmetic Chow groups, Deligne-Beilinson cohomology, hyperkähler period domains, Arakelov heights.",
        "category": "effective_diophantine_geometry",
    },
}

QUESTIONS = {
    "relevance": jev.score(
        "How directly does this candidate address the general Beal conjecture across arbitrary triples (p, q, r) >= 3?",
        [
            "level 0: Settles only bounded prime exponents or dead category computation with no general leverage.",
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
    "failure_mode_risk": jev.choice(
        "Which known repository failure mode poses the highest structural risk to this candidate?",
        {
            "failure_mode_1": "Failure Mode 1: Residual/isogeny/conductor conflation in modular representations.",
            "failure_mode_2": "Failure Mode 2: Chabauty over wrong field or unbounded bad reduction blowup dim Sel > dim U.",
            "failure_mode_3": "Failure Mode 3: Heuristic laundering (assuming ABC, Vojta, or Cohen-Lenstra unconditionally).",
            "none": "None of the above recurring failure modes apply directly.",
        },
    ),
}


def run_screen() -> None:
    print("Executing Jev screen for C394-C397...")
    states = [
        {"candidate_id": cid, **data}
        for cid, data in CANDIDATES.items()
    ]
    responses = jev.ask_many(states, QUESTIONS, concurrency=4)

    for state, resp in zip(states, responses):
        cid = state["candidate_id"]
        print(f"\n==================== Candidate {cid} ====================")
        print(f"Title: {state['title']}")
        if "error" in resp:
            print(f"ERROR: {resp['error']}")
            continue

        jev.persist(cid, state, QUESTIONS, resp)
        answers = resp.get("answers", {})
        for qname, ans in answers.items():
            print(f"  [{qname}]: value={ans.get('value')} (conf={ans.get('confidence', 0):.2f})")

    # Persist summary
    summary_path = Path("research/pool/evidence/U443_jev_screen_c394_c397_summary.json")
    with open(summary_path, "w") as f:
        json.dump([{"candidate": s, "response": r} for s, r in zip(states, responses)], f, indent=2)
    print(f"\nSaved Jev screen summary to {summary_path}")


if __name__ == "__main__":
    run_screen()
