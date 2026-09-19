"""Register Candidates C350-C353 in the research pool."""
import json
from pathlib import Path

POOL_PATH = Path(__file__).resolve().parent.parent / "research" / "pool" / "candidates.json"

def main():
    with open(POOL_PATH, "r") as f:
        data = json.load(f)

    existing_ids = {c["id"] for c in data["candidates"]}

    new_candidates = [
        {
            "id": "C350",
            "title": "KRAUS SIEVE MODULAR METHOD EXTENSION FOR SIGNATURE (3, 3, p) ON [4101, 4200]",
            "claim": "No non-trivial primitive solutions exist for signature (3, 3, p) for all prime exponents p in [4101, 4200].",
            "method": "Modular method level lowering to conductor 72, Kraus sieve relations at auxiliary primes q = 2kp + 1 with a_q(f) = 0 mod 2.",
            "status": "ACTIVE",
            "parents": ["C347"],
            "inspirations": ["Kraus 1998", "Darmon-Merel 1997"],
            "evidence": ["screen_C350_cycle250.json"],
            "obligations": ["Compute Kraus certificates for all primes in [4101, 4200] and verify with PARI/GP"],
            "evaluations": {"category": "dead_category_bounded_sieve"},
            "failure_reason": None,
            "novelty_note": "Direct continuation of bounded empirical verification frontier to exponent 4200.",
            "extracted": []
        },
        {
            "id": "C351",
            "title": "STACKY CURVES AND MUMFORD-ARAKELOV ORBIFOLD HEIGHT BOUNDS (-chi >= 1/12)",
            "claim": "The hyperbolic defect -chi >= 1/12 on the Deligne-Mumford stack X(p, q, r) yields an unconditional upper bound on the Faltings height h_Fal(E_{A,B,C}) independent of Vojta's conjecture.",
            "method": "Arakelov intersection theory on stacky curves, evaluating the canonical orbifold bundle and Mumford's metric relation to bound arithmetic heights.",
            "status": "ACTIVE",
            "parents": ["C293", "C348"],
            "inspirations": ["Mumford 1977", "Edixhoven 1997", "Bruin 2004"],
            "evidence": ["screen_C351_cycle250.json"],
            "obligations": ["Audit whether stacky Arakelov height bounds can be made independent of unproved Vojta/ABC inequalities."],
            "evaluations": {"category": "effective_diophantine_geometry"},
            "failure_reason": None,
            "novelty_note": "Exploits the genuine defect gap -chi >= 1/12 that separates Beal from Fermat-Catalan.",
            "extracted": []
        },
        {
            "id": "C352",
            "title": "UNIFORM BOGOMOLOV ON MODULAR AND SHIMURA JACOBIANS",
            "claim": "Uniform Bogomolov bounds on curves embedded in their Jacobians yield a finite bound on primitive points for hyperbolic signatures (p, q, r).",
            "method": "Dimitrov-Gao-Habegger / Kuhne uniform Bogomolov theorem applied to modular or Shimura curves parameterizing Frey representations.",
            "status": "ACTIVE",
            "parents": ["C336", "C345"],
            "inspirations": ["Dimitrov-Gao-Habegger 2021", "Kuhne 2021"],
            "evidence": ["screen_C352_cycle250.json"],
            "obligations": ["Audit whether uniform Bogomolov applies to variable-exponent Frey families or only fixed genus curves."],
            "evaluations": {"category": "effective_diophantine_geometry"},
            "failure_reason": None,
            "novelty_note": "First application of modern uniform Bogomolov / uniform Mordell-Lang bounds to the Beal pool.",
            "extracted": []
        },
        {
            "id": "C353",
            "title": "MOTIVIC FUNDAMENTAL GROUPS AND NON-ABELIAN CHABAUTY-KIM OVER UNBOUNDED S",
            "claim": "Higher-depth Selmer varieties of pi_1^et(P^1 \\ {0, 1, infty}) can bound integral points even when S = primes(ABC) has unbounded cardinality.",
            "method": "Kim's non-abelian Chabauty program applied to the punctured projective line with varying bad reduction sets S.",
            "status": "ACTIVE",
            "parents": ["C289", "C291"],
            "inspirations": ["Minhyong Kim 2005", "Ellenberg-Hast 2017"],
            "evidence": ["screen_C353_cycle250.json"],
            "obligations": ["Determine whether dim Sel(U_n) < dim U_n(Q_p) can ever hold when |S| is arbitrarily large."],
            "evaluations": {"category": "unifying_modular_motivic_geometry"},
            "failure_reason": None,
            "novelty_note": "Explores higher depth unipotent fundamental group representations to overcome rank/defect bottlenecks.",
            "extracted": []
        }
    ]

    added = 0
    for cand in new_candidates:
        if cand["id"] not in existing_ids:
            data["candidates"].append(cand)
            added += 1
            print(f"Added {cand['id']}: {cand['title']}")
        else:
            print(f"Skipped {cand['id']} (already exists)")

    with open(POOL_PATH, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Successfully registered {added} new candidates. Total candidates: {len(data['candidates'])}.")

if __name__ == "__main__":
    main()
