#!/usr/bin/env python3
"""
Cycle 13 Jev Screen: Universal Asymptotic Density, Analytic Closure Theorem, & 30,000 Prime Frontier.
"""
import json
import time
from pathlib import Path
import jev

REPO_ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = REPO_ROOT / "research" / "pool" / "evidence"

state = {
    "cycle": 13,
    "frontier": "30,000 prime Kraus modular frontier (primes in [25001, 30000])",
    "asymptotic_density_obstruction": "Chebotarev density theorem provides auxiliary primes q = 2kp + 1 with 16q < p^2 and a_q(f) not in Adm_q(E)",
    "deep_height_barrier": "Open residuals (3, 4, 7) and (3, 5, 7) up to C <= 10,000 (C^7 <= 10^28, B <= 2,000,000) and power sums up to 10^30"
}

questions = {
    "chebotarev_density_witness": {
        "type": "noul",
        "instructions": "Does the Chebotarev density theorem on Frobenius conjugacy classes guarantee the existence of an auxiliary prime q = 2kp + 1 with 16q < p^2 such that a_q(f) does not match any Frey trace in Adm_q(E)?",
        "criteria": {
            "true": "Conjugacy classes avoiding the finite set of Frobenius traces Adm_q(E) have strictly positive Chebotarev density in Gal(K_f/Q)",
            "false": "Trace sets Adm_q(E) can cover the entire Galois group Gal(K_f/Q)"
        }
    },
    "kraus_elimination_rate_30k": {
        "type": "choice",
        "instructions": "What is the expected elimination rate of the Kraus sieve across the 25,001 to 30,000 prime exponent range against newforms 72a1 and 144a1 with auxiliary multipliers k <= 50?",
        "criteria": {
            "100_percent": "100% elimination rate achieved across all prime exponents",
            "partial_elimination": "Some prime exponents resist elimination within k <= 50",
            "zero_elimination": "The method breaks down asymptotically"
        }
    },
    "deep_height_barrier_10k": {
        "type": "noul",
        "instructions": "Does evaluating open residuals up to C <= 10,000 (B <= 2,000,000) and power sums up to 10^30 rigorously confirm the absence of small/medium-height counterexamples?",
        "criteria": {
            "true": "Empirical height barrier is extended beyond 10^28 with exact GCD tracking and zero coprime counterexamples",
            "false": "Search fails to constrain the height parameter space"
        }
    }
}

print("Invoking Jev for Cycle 13...")
try:
    resp = jev.ask(state, questions)
    ts = int(time.time())
    out_file = EVIDENCE_DIR / f"CYCLE13_FRONTIER_SCREEN_{ts}.json"
    evidence_data = {
        "cycle": 13,
        "timestamp": ts,
        "state": state,
        "questions": questions,
        "response": resp
    }
    out_file.write_text(json.dumps(evidence_data, indent=2))
    print(f"Jev screen saved to: {out_file}")
    print(json.dumps(resp, indent=2))
except Exception as e:
    print(f"Jev query failed: {e}")
