"""Update candidates C358-C361 in research/pool/candidates.json."""
import json
from pathlib import Path

POOL_PATH = Path(__file__).resolve().parent.parent / "research" / "pool" / "candidates.json"

def main():
    with open(POOL_PATH, "r") as f:
        data = json.load(f)

    updates = {
        "C358": {
            "status": "PARTIAL_RESULT",
            "failure_reason": None,
            "extracted": ["Kraus sieve eliminates all 4 primes p in [4301, 4400] with p = 1 mod 3; 5 primes with p = 2 mod 3 eliminated by Darmon-Merel."],
        },
        "C359": {
            "status": "BLOCKED",
            "failure_reason": "Arithmetic threefold intersection bounds on (omega)^3 require the conjectural arithmetic Bogomolov-Miyaoka-Yau inequality over Spec Z, which is unproved and equivalent to Vojta / ABC (heuristic laundering, Failure Mode 3).",
            "extracted": ["Higher-dimensional arithmetic intersection theory over Spec Z requires conjectural BMY inequalities to yield height bounds."],
        },
        "C360": {
            "status": "BLOCKED",
            "failure_reason": "Beilinson-Flach Euler system bounds on Selmer groups are scaled by the product of local Tamagawa factors prod_{v in S} c_v(T). For Beal solutions, S = primes(ABC) is unbounded, causing the Tamagawa factor product to diverge exponentially and providing no uniform bound.",
            "extracted": ["Euler systems cannot bound Selmer groups uniformly when the set of bad reduction primes S has unbounded cardinality."],
        },
        "C361": {
            "status": "BLOCKED",
            "failure_reason": "Bhargava's arithmetic invariant theory and coregular representations exist only for degrees <= 5. General Beal signatures have exponents >= 6 where invariant rings are non-coregular, and orbit counts compute average densities rather than universal Diophantine non-existence.",
            "extracted": ["Arithmetic invariant theory is restricted to coregular representations of degree <= 5 and cannot cover general Diophantine exponents."],
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
