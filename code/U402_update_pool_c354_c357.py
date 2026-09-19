"""Update candidates C354-C357 in research/pool/candidates.json."""
import json
from pathlib import Path

POOL_PATH = Path(__file__).resolve().parent.parent / "research" / "pool" / "candidates.json"

def main():
    with open(POOL_PATH, "r") as f:
        data = json.load(f)

    updates = {
        "C354": {
            "status": "PARTIAL_RESULT",
            "failure_reason": None,
            "extracted": ["Kraus sieve eliminates all 7 primes p in [4201, 4300] with p = 1 mod 3; 9 primes with p = 2 mod 3 eliminated by Darmon-Merel."],
        },
        "C355": {
            "status": "BLOCKED",
            "failure_reason": "Cherednik-Drinfeld p-adic uniformization parameters and Mumford period lattices on Shimura curves depend projectively on j(E) in Q_p, invariant under scaling (A, B, C) |-> (dA, dB, dC) and blind to global integer coprimality gcd(A, B, C) > 1.",
            "extracted": ["p-adic uniformization periods on Shimura curves are scale invariant and cannot detect integer divisibility across all primes."],
        },
        "C356": {
            "status": "BLOCKED",
            "failure_reason": "Lawrence-Venkatesh method strictly requires a fixed family with fixed Hodge numbers and a fixed bad reduction set S; for Beal, genus g ~ O(pqr) diverges with exponents and S = primes(ABC) has unbounded cardinality, destroying Faltings' Galois finiteness.",
            "extracted": ["Lawrence-Venkatesh requires fixed Hodge numbers and bounded ramification; it cannot bridge across variable exponents or unbounded bad reduction."],
        },
        "C357": {
            "status": "BLOCKED",
            "failure_reason": "Relative Galois deformation functors over variable exponent bases fail to be representable because wild ramification indices and inertia Hodge-Tate weights vary with exponents, and tangent space dimension dim H^1(G_{Q,S}, ad rho) ~ O(|S|) blows up without bound.",
            "extracted": ["Representability of universal deformation rings breaks down under variable wild ramification and unbounded bad reduction."],
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
