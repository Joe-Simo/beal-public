"""Update candidates C350-C353 in research/pool/candidates.json."""
import json
from pathlib import Path

POOL_PATH = Path(__file__).resolve().parent.parent / "research" / "pool" / "candidates.json"

def main():
    with open(POOL_PATH, "r") as f:
        data = json.load(f)

    updates = {
        "C350": {
            "status": "PARTIAL_RESULT",
            "failure_reason": None,
            "extracted": ["Kraus sieve eliminates all 5 primes p in [4101, 4200] with p = 1 mod 3; 4 primes with p = 2 mod 3 eliminated by Darmon-Merel."],
        },
        "C351": {
            "status": "BLOCKED",
            "failure_reason": "Orbifold ramification multiplicities exactly cancel the naive height on stacky curves so h_X(t) = O(1); bounding h(t) requires the unproved Vojta conjecture on Deligne-Mumford stacks (heuristic laundering).",
            "extracted": ["Hyperbolic defect -chi >= 1/12 is not Fermat-Catalan blind (gap 5/84), but converting defect to height bounds requires Vojta/ABC."],
        },
        "C352": {
            "status": "BLOCKED",
            "failure_reason": "Uniform Bogomolov (Dimitrov-Gao-Habegger, Kuhne) applies only to curves of fixed genus g; Fermat curve genus g ~ O(pqr) blows up with exponents, precluding uniform bounds across variable exponents.",
            "extracted": ["Uniform Bogomolov bounds are genus-dependent and cannot bridge to variable-exponent Diophantine families."],
        },
        "C353": {
            "status": "BLOCKED",
            "failure_reason": "Chabauty-Kim condition dim Sel(U_n) < dim U_n(Q_p) fails because the bad reduction set S = primes(ABC) has unbounded cardinality, causing Selmer variety dimension to blow up as O(|S|^n).",
            "extracted": ["Unbounded bad reduction is a fundamental structural obstruction to non-abelian Chabauty on P^1 \\ {0, 1, infty}."],
        },
    }

    for c in data["candidates"]:
        if c["id"] in updates:
            up = updates[c["id"]]
            c["status"] = up["status"]
            c["failure_reason"] = up["failure_reason"]
            c["extracted"] = up["extracted"]
            print(f"Updated {c['id']} -> {c['status']}")

    with open(POOL_PATH, "w") as f:
        json.dump(data, f, indent=2)

    print("Candidates successfully updated.")

if __name__ == "__main__":
    main()
