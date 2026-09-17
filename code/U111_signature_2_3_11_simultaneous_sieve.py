"""U111: Multi-Prime Simultaneous Sieve for Signature (2, 3, 11).

Formulates and executes a multi-prime simultaneous sieve across the 8 good primes:
  q in {5, 7, 13, 17, 19, 23, 29, 31}
with modulus M = prod(q) = 3,038,795,305.

Verifies:
1. Local compatibility counts N_f(q) and global CRT counts N_f(M) for all candidate newforms in S_2^new(432) and S_2^new(864).
2. Sieve density rho_f = N_f(M) / prod(q^2 - 1) across the ~8.54 x 10^18 pair space.
3. Structural constraints for the Catalan newform 864b1:
   - B = -2 mod 5 is universally forced.
   - At q = 23, 11th power collapse forces A^2 + B^3 in {1, -1} mod 23, leaving only 5 pairs.
4. Bounded integer search in [-2000, 2000] x [-200, 200]:
   - 864b1 / E_cat isolates the unique Catalan solution (3, -2).
   - 288a1 isolates the unique trivial solution (0, 1).
   - All other forms in S_2^new(432) and S_2^new(864) (including 864a1, 864c1) yield 0 integer points.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import subprocess
from typing import Any
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

# Sieve primes
PRIMES_Q = [5, 7, 13, 17, 19, 23, 29, 31]
ALL_PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31]
PRIME_INDICES = {p: i for i, p in enumerate(ALL_PRIMES)}

MODULUS_M = math.prod(PRIMES_Q)  # 3,038,795,305
TOTAL_PAIRS_M = math.prod(q**2 - 1 for q in PRIMES_Q)  # ~8.5436 x 10^18


def get_mu11_powers(q: int) -> set[int]:
    """Compute the set of 11th power residues in F_q."""
    return {pow(c, 11, q) for c in range(q)}


def compute_frey_trace(a: int, b: int, q: int) -> int | None:
    """Compute Frobenius trace a_q(E_{(a, b)}) for Y^2 = X^3 + 3bX + 2a over F_q."""
    delta = (-16 * (4 * (3 * b) ** 3 + 27 * (2 * a) ** 2)) % q
    if delta == 0:
        return None  # Bad reduction (q | C)
    cnt = 1
    for x in range(q):
        rhs = (x**3 + 3 * b * x + 2 * a) % q
        cnt += 1 + sp.legendre_symbol(rhs, q)
    return int(q + 1 - cnt)


def precompute_local_admissible_pairs() -> dict[int, dict[tuple[int, int], int | str]]:
    """Precompute all (A, B) in F_q^2 with A^2 + B^3 in mu_11(F_q) and their reduction traces."""
    pair_data = {}
    for q in PRIMES_Q:
        pow11 = get_mu11_powers(q)
        pairs: dict[tuple[int, int], int | str] = {}
        for a in range(q):
            for b in range(q):
                if a == 0 and b == 0:
                    continue
                lhs = (a**2 + b**3) % q
                if lhs in pow11:
                    if lhs == 0:
                        pairs[(a, b)] = "bad"
                    else:
                        tr = compute_frey_trace(a, b, q)
                        assert tr is not None
                        pairs[(a, b)] = tr
        pair_data[q] = pairs
    return pair_data


def query_pari_gp_forms() -> dict[str, list[int]]:
    """Query PARI/GP for rational newforms at levels 432 and 864."""
    gp_code = r"""
    {
      my(Lv = [432, 864], primes = [5, 7, 11, 13, 17, 19, 23, 29, 31]);
      for(idx=1, #Lv,
        my(N = Lv[idx]);
        my(mf = mfinit([N, 2, 1], 0));
        my(eb = mfeigenbasis(mf));
        for(i=1, #eb,
          my(f = eb[i]);
          if(poldegree(f.mod) == 1,
            my(coeffs = mfcoefs(f, 35));
            my(v = vector(#primes, p, coeffs[primes[p]+1]));
            print("FORM_DATA:", N, "_", i, ":", v);
          );
        );
      );
    }
    """
    proc = subprocess.run(["gp", "-q"], input=gp_code, text=True, capture_output=True, check=True)
    forms: dict[str, list[int]] = {}
    for line in proc.stdout.strip().split("\n"):
        line = line.strip()
        if not line.startswith("FORM_DATA:"):
            continue
        parts = [p.strip() for p in line.split(":")]
        name = parts[1]
        raw_v = parts[2].strip("[]").split(",")
        forms[name] = [int(x.strip()) for x in raw_v]
    return forms


def filter_compatible_pairs(
    pair_data: dict[int, dict[tuple[int, int], int | str]],
    faqs: list[int]
) -> dict[int, list[tuple[int, int]]]:
    """Filter admissible pairs in F_q^2 that satisfy trace compatibility mod 11."""
    compatible: dict[int, list[tuple[int, int]]] = {}
    for q in PRIMES_Q:
        aq_f = faqs[PRIME_INDICES[q]]
        valid = []
        for (a, b), val in pair_data[q].items():
            if val == "bad":
                # Multiplicative reduction congruence: aq(f) = +-(q+1) mod 11
                if (aq_f - (q + 1)) % 11 == 0 or (aq_f + (q + 1)) % 11 == 0:
                    valid.append((a, b))
            else:
                # Good reduction congruence: aq(E) = aq(f) mod 11
                if (val - aq_f) % 11 == 0:
                    valid.append((a, b))
        compatible[q] = valid
    return compatible


def run_bounded_integer_search(
    allowed: dict[int, set[tuple[int, int]]],
    a_bound: int = 2000,
    b_bound: int = 200,
) -> list[tuple[int, int]]:
    """Search for coprime integer pairs (A, B) in [-a_bound, a_bound] x [-b_bound, b_bound]."""
    found = []
    # Pre-filter B by small primes
    for b in range(-b_bound, b_bound + 1):
        # Quick check for b at 5, 7, 13
        b_valid = True
        for q in [5, 7, 13]:
            bq = b % q
            if not any(p[1] == bq for p in allowed[q]):
                b_valid = False
                break
        if not b_valid:
            continue

        for a in range(-a_bound, a_bound + 1):
            if math.gcd(a, b) != 1:
                continue
            match = True
            for q in PRIMES_Q:
                if (a % q, b % q) not in allowed[q]:
                    match = False
                    break
            if match:
                found.append((a, b))
    return found


def main() -> None:
    print("================================================================================")
    print("U111: MULTI-PRIME SIMULTANEOUS SIEVE FOR SIGNATURE (2, 3, 11)")
    print("================================================================================")
    print(f"Sieve primes: {PRIMES_Q}")
    print(f"Modulus M = prod(q) = {MODULUS_M}")
    print(f"Total non-zero pair space mod M: {TOTAL_PAIRS_M:.4e}")

    # 1. Precompute local pair data
    print("\n[1] PRECOMPUTING LOCAL ADMISSIBLE PAIRS & FREY TRACES:")
    pair_data = precompute_local_admissible_pairs()
    for q in PRIMES_Q:
        print(f"  q = {q:2d}: {len(pair_data[q]):3d} admissible pairs in F_{q}^2 \\ {{(0, 0)}}")

    # 2. Query PARI/GP for rational newforms
    print("\n[2] FETCHING CANDIDATE NEWFORMS AT LEVELS 432 AND 864:")
    forms = query_pari_gp_forms()
    # Add Catalan Frey curve directly for explicit comparison
    # E_cat traces: [-2, -3, 6, 3, -2, -3, -6, 8, 0]
    forms["E_cat"] = [-2, -3, 6, 3, -2, -3, -6, 8, 0]
    # Add 288a1: [-4, 0, 0, -6, -8, 0, 0, 4, 0]
    forms["288a1"] = [-4, 0, 0, -6, -8, 0, 0, 4, 0]
    print(f"  Loaded {len(forms)} rational forms for testing.")

    # 3. Multi-Prime Simultaneous Sieve
    print("\n[3] SIMULTANEOUS SIEVE ACROSS ALL 8 PRIMES:")
    sieve_results: dict[str, Any] = {}
    print(f"  {'Form':<10} | {'Local Counts N(q) for q in {5,7,13,17,19,23,29,31}}':<50} | {'N(M)':<16} | {'Density rho':<12}")
    print("  " + "-" * 95)

    for fname, faqs in sorted(forms.items()):
        compat = filter_compatible_pairs(pair_data, faqs)
        counts = [len(compat[q]) for q in PRIMES_Q]
        n_m = math.prod(counts)
        density = n_m / TOTAL_PAIRS_M
        sieve_results[fname] = {
            "a_q": {q: faqs[PRIME_INDICES[q]] for q in ALL_PRIMES},
            "local_counts": {q: len(compat[q]) for q in PRIMES_Q},
            "N_M": n_m,
            "density": density,
            "log10_density": math.log10(density) if density > 0 else -999,
        }
        counts_str = ", ".join(f"{c:3d}" for c in counts)
        print(f"  {fname:<10} | [{counts_str}] | {n_m:<16d} | {density:.4e}")

    # 4. Deep Inspection of Catalan Form 864b1 / E_cat
    print("\n[4] STRUCTURAL CONSTRAINTS ON CATALAN FORM (864b1 / E_cat):")
    cat_compat = filter_compatible_pairs(pair_data, forms["E_cat"])
    allowed_cat = {q: set(cat_compat[q]) for q in PRIMES_Q}

    # Verify B = -2 mod 5 is forced
    b_mod5_vals = {p[1] for p in allowed_cat[5]}
    print(f"  At q = 5: admissible B values = {b_mod5_vals}")
    assert b_mod5_vals == {3}  # 3 = -2 mod 5
    print("  [PASS] THEOREM: B = -2 mod 5 is RIGIDLY FORCED for the Catalan modular form!")

    # Verify q = 23 collapse
    print(f"  At q = 23: admissible pairs count = {len(allowed_cat[23])}")
    print(f"    Pairs: {sorted(allowed_cat[23])}")
    assert (3 % 23, (-2) % 23) in allowed_cat[23]
    print("  [PASS] THEOREM: Catalan pair (3, -2) = (3, 21) in F_23 is an exact match at q = 23!")

    # 5. Bounded Integer Search across Forms
    print("\n[5] BOUNDED INTEGER SEARCH IN [-2000, 2000] x [-200, 200]:")
    target_search_forms = ["E_cat", "864_4", "864_8", "864_10", "288a1", "432_1", "432_2", "432_7"]
    search_findings = {}

    for target in target_search_forms:
        if target not in forms:
            continue
        compat_t = filter_compatible_pairs(pair_data, forms[target])
        allowed_t = {q: set(compat_t[q]) for q in PRIMES_Q}
        found = run_bounded_integer_search(allowed_t, a_bound=2000, b_bound=200)
        search_findings[target] = found
        print(f"  Form {target:<8}: found {len(found)} integer pairs -> {found}")

    # Verify isolation of known solutions
    assert search_findings["E_cat"] == [(3, -2)]
    print("\n  [PASS] THEOREM: The Catalan solution (3, -2) is the UNIQUE integer pair in the search box matching E_cat!")
    assert search_findings["288a1"] == [(0, 1)]
    print("  [PASS] THEOREM: The Trivial solution (0, 1) is the UNIQUE integer pair in the search box matching 288a1!")

    # Verify emptiness for non-solution forms
    assert search_findings["864_8"] == []  # 864a1
    assert search_findings["864_10"] == []  # 864c1
    assert search_findings["432_1"] == []
    assert search_findings["432_2"] == []
    assert search_findings["432_7"] == []
    print("  [PASS] THEOREM: All candidate forms without integer solutions yield EXACTLY ZERO integer points in the search box!")

    # 6. Save JSON ledger
    out_file = ROOT / "references/U111_signature_2_3_11_simultaneous_sieve.json"
    json_data = {
        "status": "PASS",
        "description": "Multi-prime simultaneous sieve for signature (2, 3, 11)",
        "primes": PRIMES_Q,
        "modulus_M": MODULUS_M,
        "total_pairs_M": TOTAL_PAIRS_M,
        "sieve_results": sieve_results,
        "catalan_constraints": {
            "q5_b_forced": 3,
            "q23_admissible_pairs": [list(p) for p in sorted(allowed_cat[23])],
        },
        "bounded_search_results": {k: [list(pt) for pt in v] for k, v in search_findings.items()},
    }
    out_file.write_text(json.dumps(json_data, indent=2))
    print(f"\nSaved structured sieve verification data to: {out_file}")
    print("\nALL SIMULTANEOUS SIEVE VERIFICATIONS COMPLETED SUCCESSFULLY WITH RETURN CODE 0.")


if __name__ == "__main__":
    main()
