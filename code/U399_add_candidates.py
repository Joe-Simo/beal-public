"""Register Candidates C354-C357 in the research pool."""
import json
from pathlib import Path

POOL_PATH = Path(__file__).resolve().parent.parent / "research" / "pool" / "candidates.json"

def main():
    with open(POOL_PATH, "r") as f:
        data = json.load(f)

    existing_ids = {c["id"] for c in data["candidates"]}

    new_candidates = [
        {
            "id": "C354",
            "title": "KRAUS SIEVE MODULAR METHOD EXTENSION FOR SIGNATURE (3, 3, p) ON [4201, 4300]",
            "claim": "No non-trivial primitive solutions exist for signature (3, 3, p) for all prime exponents p in [4201, 4300].",
            "method": "Modular method level lowering to conductor 72, Kraus sieve relations at auxiliary primes q = 2kp + 1 with a_q(f) = 0 mod 2.",
            "status": "ACTIVE",
            "parents": ["C350"],
            "inspirations": ["Kraus 1998", "Darmon-Merel 1997"],
            "evidence": ["screen_C354_cycle251.json"],
            "obligations": ["Compute Kraus certificates for all primes in [4201, 4300] and verify with PARI/GP"],
            "evaluations": {"category": "dead_category_bounded_sieve"},
            "failure_reason": None,
            "novelty_note": "Direct continuation of bounded empirical verification frontier to exponent 4300.",
            "extracted": []
        },
        {
            "id": "C355",
            "title": "CHEREDNIK-DRINFELD P-ADIC UNIFORMIZATION AND SHIMURA PERIOD MAPPINGS",
            "claim": "p-adic uniformization of Shimura curves by Mumford curves constrains integral points on triangle orbifolds via non-archimedean period mappings.",
            "method": "Cherednik-Drinfeld theorem and rigid analytic geometry applied to p-adic uniformized quotients parameterizing Frey representations.",
            "status": "ACTIVE",
            "parents": ["C336", "C345"],
            "inspirations": ["Cherednik 1976", "Drinfeld 1976", "Boutot-Carayol 1991"],
            "evidence": ["screen_C355_cycle251.json"],
            "obligations": ["Audit whether p-adic uniformization periods can detect global integer coprimality across all primes."],
            "evaluations": {"category": "effective_diophantine_geometry"},
            "failure_reason": None,
            "novelty_note": "First investigation of non-archimedean uniformization on Shimura curves for Frey curves.",
            "extracted": []
        },
        {
            "id": "C356",
            "title": "LAWRENCE-VENKATESH METHOD AND VARIATIONS OF HODGE STRUCTURES ACROSS EXPONENTS",
            "claim": "The Lawrence-Venkatesh method of variations of Galois representations and p-adic period maps bounds primitive solutions across all (p, q, r) >= 3.",
            "method": "Lawrence-Venkatesh strategy applied to families of abelian varieties or hypersurfaces associated to generalized Fermat equations.",
            "status": "ACTIVE",
            "parents": ["C351", "C353"],
            "inspirations": ["Lawrence-Venkatesh 2020"],
            "evidence": ["screen_C356_cycle251.json"],
            "obligations": ["Audit whether Lawrence-Venkatesh applies to variable families of schemes or requires a fixed base scheme with fixed Hodge numbers."],
            "evaluations": {"category": "unifying_modular_motivic_geometry"},
            "failure_reason": None,
            "novelty_note": "Direct test of the celebrated Lawrence-Venkatesh method against variable exponent Diophantine equations.",
            "extracted": []
        },
        {
            "id": "C357",
            "title": "RELATIVE GALOIS DEFORMATIONS AND MULTI-EXPONENT FONTAINE-MAZUR MODULARITY",
            "claim": "Relative deformation rings over universal exponent moduli force mod-p Frey representations to arise from a finite set of fixed-weight modular forms.",
            "method": "Universal deformation rings parameterizing Galois representations with varying wild ramification exponents.",
            "status": "ACTIVE",
            "parents": ["C339", "C348"],
            "inspirations": ["Mazur 1989", "Fontaine-Mazur 1995", "Kisin 2009"],
            "evidence": ["screen_C357_cycle251.json"],
            "obligations": ["Determine whether Fontaine-Mazur modularity can constrain representations when the Hodge-Tate weights depend on variable exponents."],
            "evaluations": {"category": "unifying_modular_motivic_geometry"},
            "failure_reason": None,
            "novelty_note": "Explores relative deformation rings parameterized by varying exponent tuples.",
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
