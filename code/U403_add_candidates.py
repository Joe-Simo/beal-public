"""Register Candidates C358-C361 in the research pool."""
import json
from pathlib import Path

POOL_PATH = Path(__file__).resolve().parent.parent / "research" / "pool" / "candidates.json"

def main():
    with open(POOL_PATH, "r") as f:
        data = json.load(f)

    existing_ids = {c["id"] for c in data["candidates"]}

    new_candidates = [
        {
            "id": "C358",
            "title": "KRAUS SIEVE MODULAR METHOD EXTENSION FOR SIGNATURE (3, 3, p) ON [4301, 4400]",
            "claim": "No non-trivial primitive solutions exist for signature (3, 3, p) for all prime exponents p in [4301, 4400].",
            "method": "Modular method level lowering to conductor 72, Kraus sieve relations at auxiliary primes q = 2kp + 1 with a_q(f) = 0 mod 2.",
            "status": "ACTIVE",
            "parents": ["C354"],
            "inspirations": ["Kraus 1998", "Darmon-Merel 1997"],
            "evidence": ["screen_C358_cycle252.json"],
            "obligations": ["Compute Kraus certificates for all primes in [4301, 4400] and verify with PARI/GP"],
            "evaluations": {"category": "dead_category_bounded_sieve"},
            "failure_reason": None,
            "novelty_note": "Direct continuation of bounded empirical verification frontier to exponent 4400.",
            "extracted": []
        },
        {
            "id": "C359",
            "title": "ARAKELOV-MUMFORD-PARSHIN ARITHMETIC THREEFOLDS AND (omega)^3 HEIGHT BOUNDS",
            "claim": "The arithmetic self-intersection of the relative dualizing sheaf (omega)^3 on the arithmetic threefold fibered by triangle orbifolds unconditionally bounds heights of primitive points.",
            "method": "Higher-dimensional Arakelov intersection theory (Parshin, Moret-Bailly) on arithmetic schemes fibered over modular curves.",
            "status": "ACTIVE",
            "parents": ["C351", "C355"],
            "inspirations": ["Parshin 1988", "Moret-Bailly 1989", "Gillet-Soule 1992"],
            "evidence": ["screen_C359_cycle252.json"],
            "obligations": ["Audit whether higher arithmetic intersection numbers depend on Vojta/Bogomolov or are scale invariant."],
            "evaluations": {"category": "effective_diophantine_geometry"},
            "failure_reason": None,
            "novelty_note": "First investigation of arithmetic threefold intersection theory in the Beal candidate pool.",
            "extracted": []
        },
        {
            "id": "C360",
            "title": "UNIVERSAL EULER SYSTEMS AND BEILINSON-FLACH ELEMENTS FOR TRIANGLE ORBIFOLDS",
            "claim": "Beilinson-Flach Euler systems in rank 4 motivic cohomology annihilate the global Selmer group of Frey Galois representations even when S = primes(ABC) is unbounded.",
            "method": "Kato / Kings-Loeffler-Zerbes Euler system machinery applied to products of modular curves parameterizing Beal solutions.",
            "status": "ACTIVE",
            "parents": ["C353", "C356"],
            "inspirations": ["Kato 2004", "Kings-Loeffler-Zerbes 2017"],
            "evidence": ["screen_C360_cycle252.json"],
            "obligations": ["Determine whether Euler system bounding holds when the set of bad reduction primes is unbounded."],
            "evaluations": {"category": "unifying_modular_motivic_geometry"},
            "failure_reason": None,
            "novelty_note": "First application of modern Euler systems (Beilinson-Flach elements) to the Beal exploration pool.",
            "extracted": []
        },
        {
            "id": "C361",
            "title": "ARITHMETIC INVARIANT THEORY AND BHARGAVA ORBITS ON FERMAT HYPERSURFACES",
            "claim": "Higher composition laws and integer orbits under coregular group actions bound primitive integral solutions on generalized Fermat hypersurfaces.",
            "method": "Bhargava's geometry-of-numbers techniques and coregular representations applied to binary forms and Fermat invariants.",
            "status": "ACTIVE",
            "parents": ["C348", "C352"],
            "inspirations": ["Bhargava 2004", "Bhargava-Shankar 2015"],
            "evidence": ["screen_C361_cycle252.json"],
            "obligations": ["Audit whether coregular orbit counts can constrain solutions when exponents exceed 3, 4, 5."],
            "evaluations": {"category": "effective_diophantine_geometry"},
            "failure_reason": None,
            "novelty_note": "Explores Bhargava's arithmetic invariant theory and geometry-of-numbers orbits.",
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
