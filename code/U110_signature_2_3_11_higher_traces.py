"""U110: Higher Trace Rigidity and Modular Analysis for Signature (2, 3, 11).

Exact arithmetic computation and verification of:
1. Kraus Frey curve Frobenius traces a_q(E_{(A, B)}) over F_q for (A, B) in F_q^2 with A^2 + B^3 in mu_{11}(F_q).
2. Extension of the Integer Trace Rigidity Theorem to good primes q in {7, 13, 17, 19, 23}.
3. Criteria for non-divisibility of C by q based on bad multiplicative reduction residues +- (q + 1) mod 11.
4. Complete classification and comparison against candidate newforms in S_2^new(432) and S_2^new(864).
5. Quadratic twist partition of S_2^new(864) into 3 families represented by 864a1, 864b1, 864c1.
6. Verification of the permanent modular barrier: Catalan and trivial solutions.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import subprocess
from typing import Any
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

# Primes of interest
PRIMES_Q = [5, 7, 13, 17, 19, 23]
ALL_PRIMES = [5, 7, 11, 13, 17, 19, 23]
PRIME_INDICES = {p: i for i, p in enumerate(ALL_PRIMES)}

# Reference elliptic curve Weierstrass models
CURVES_REF = {
    "27a1": [0, 0, 1, 0, -7],
    "54a1": [1, -1, 0, 12, 8],
    "96a1": [0, 1, 0, -2, 0],
    "288a1": [0, 0, 0, 3, 0],
    "864a1": [0, 0, 0, -3, 6],
    "864b1": [0, 0, 0, -24, 48],
    "864c1": [0, 0, 0, 24, -16],
    "E_cat": [0, 0, 0, -6, 6],
}


def compute_elliptic_curve_ap(coeffs: list[int], p: int) -> int:
    """Compute Frobenius trace a_p of elliptic curve from Weierstrass coefficients."""
    a1, a2, a3, a4, a6 = coeffs
    cnt = 1
    for x in range(p):
        disc = (4 * (x**3 + a2 * x**2 + a4 * x + a6) + (a1 * x + a3) ** 2) % p
        cnt += 1 + sp.legendre_symbol(disc, p)
    return int(p + 1 - cnt)


def compute_frey_curve_ap(a: int, b: int, q: int) -> int | None:
    """Compute Frobenius trace of Kraus Frey curve Y^2 = X^3 + 3bX + 2a at prime q."""
    delta = (-16 * (4 * (3 * b) ** 3 + 27 * (2 * a) ** 2)) % q
    if delta == 0:
        return None  # Singular / bad reduction
    cnt = 1
    for x in range(q):
        rhs = (x**3 + 3 * b * x + 2 * a) % q
        cnt += 1 + sp.legendre_symbol(rhs, q)
    return int(q + 1 - cnt)


def get_mu11_powers(q: int) -> set[int]:
    """Compute the set of 11th power residues in F_q."""
    return {pow(c, 11, q) for c in range(q)}


def compute_admissible_frey_traces(q: int) -> dict[str, Any]:
    """Compute admissible traces a_q(E) over F_q for A^2 + B^3 = C^11 mod q."""
    pow11 = get_mu11_powers(q)
    total_pairs = 0
    good_pairs = 0
    bad_pairs = 0
    trace_counts: dict[int, int] = {}
    pairs_by_trace: dict[int, list[tuple[int, int]]] = {}

    for a in range(q):
        for b in range(q):
            if a == 0 and b == 0:
                continue
            lhs = (a**2 + b**3) % q
            if lhs in pow11:
                total_pairs += 1
                if lhs == 0:
                    bad_pairs += 1
                else:
                    good_pairs += 1
                    t = compute_frey_curve_ap(a, b, q)
                    assert t is not None
                    trace_counts[t] = trace_counts.get(t, 0) + 1
                    pairs_by_trace.setdefault(t, []).append((a, b))

    max_hasse = math.floor(2 * math.sqrt(q))
    hasse_interval = list(range(-max_hasse, max_hasse + 1))
    bad_residues_mod11 = {(q + 1) % 11, (-(q + 1)) % 11}
    bad_integers_in_hasse = [x for x in hasse_interval if (x % 11) in bad_residues_mod11]

    # Rigid values: integers in Hasse interval with unique representative mod 11
    rigid_values = [
        t for t in hasse_interval
        if len([x for x in hasse_interval if (x - t) % 11 == 0]) == 1
    ]

    return {
        "q": q,
        "max_hasse": max_hasse,
        "hasse_interval": hasse_interval,
        "pow11_count": len(pow11),
        "pow11_elements": sorted(pow11),
        "total_admissible_pairs": total_pairs,
        "good_reduction_pairs": good_pairs,
        "bad_reduction_pairs": bad_pairs,
        "distinct_good_traces": sorted(trace_counts.keys()),
        "trace_frequencies": dict(sorted(trace_counts.items())),
        "bad_residues_mod11": sorted(bad_residues_mod11),
        "bad_integers_in_hasse": bad_integers_in_hasse,
        "rigid_values_hasse": rigid_values,
        "rigid_interval": [min(rigid_values), max(rigid_values)] if rigid_values else [],
    }


def query_pari_gp_newforms() -> dict[int, list[dict[str, Any]]]:
    """Extract all newforms at levels 432 and 864 with Hecke eigenvalues."""
    gp_code = r"""
    {
      my(Lv = [432, 864], primes = [5, 7, 11, 13, 17, 19, 23]);
      for(idx=1, #Lv,
        my(N = Lv[idx]);
        my(mf = mfinit([N, 2, 1], 0));
        my(eb = mfeigenbasis(mf));
        print("LEVEL_HEADER:", N, ":", #eb);
        for(i=1, #eb,
          my(f = eb[i]);
          my(deg = poldegree(f.mod));
          my(coeffs = mfcoefs(f, 25));
          my(v = vector(#primes, p, coeffs[primes[p]+1]));
          print("FORM_DATA:", N, ":", i, ":", deg, ":", f.mod, ":", v);
        );
      );
    }
    """
    proc = subprocess.run(["gp", "-q"], input=gp_code, text=True, capture_output=True, check=True)
    lines = proc.stdout.strip().split("\n")

    results: dict[int, list[dict[str, Any]]] = {432: [], 864: []}
    for line in lines:
        line = line.strip()
        if not line.startswith("FORM_DATA:"):
            continue
        parts = [p.strip() for p in line.split(":")]
        N = int(parts[1])
        form_idx = int(parts[2])
        deg = int(parts[3])
        poly = parts[4]
        aqs_raw = parts[5]

        # Parse vector
        if deg == 1:
            aqs_clean = aqs_raw.strip("[]").split(",")
            aqs = [int(x.strip()) for x in aqs_clean]
        else:
            aqs = aqs_raw  # Keep raw string for non-rational

        results[N].append({
            "index": form_idx,
            "degree": deg,
            "poly": poly,
            "a_q": aqs,
        })
    return results


def analyze_form_rigidity(
    name: str,
    level: int,
    aqs: list[int],
    admissible_data: dict[int, dict[str, Any]]
) -> dict[str, Any]:
    """Analyze non-divisibility and exact trace rigidity for a rational newform."""
    non_div_primes: list[int] = []
    exact_rigid_traces: dict[int, int] = {}
    ambiguous_traces: dict[int, list[int]] = {}

    for q in PRIMES_Q:
        idx = PRIME_INDICES[q]
        aq = aqs[idx]
        adm = admissible_data[q]

        # Non-divisibility check: if a_q(f) is NOT in bad integers in Hasse
        if aq not in adm["bad_integers_in_hasse"]:
            non_div_primes.append(q)
            # Check if trace is in rigid interval
            if aq in adm["rigid_values_hasse"]:
                exact_rigid_traces[q] = aq
            else:
                # Find the two possible values in Hasse interval congruent to aq mod 11
                candidates = [
                    x for x in adm["hasse_interval"]
                    if (x - aq) % 11 == 0
                ]
                ambiguous_traces[q] = candidates
        else:
            # Multiplicative reduction is possible
            pass

    return {
        "name": name,
        "level": level,
        "a_q": {q: aqs[PRIME_INDICES[q]] for q in ALL_PRIMES},
        "non_div_primes": non_div_primes,
        "exact_rigid_traces": exact_rigid_traces,
        "ambiguous_traces": ambiguous_traces,
    }


def verify_twist_families(level_864_forms: list[dict[str, Any]]) -> dict[str, Any]:
    """Verify the partition of rational newforms at level 864 into 3 quadratic twist families."""
    rational_forms = [f for f in level_864_forms if f["degree"] == 1]
    assert len(rational_forms) == 12, f"Expected 12 rational forms, found {len(rational_forms)}"

    fund_discs = [1, -4, -3, 12]  # Twists preserving level 864
    families: dict[str, list[int]] = {
        "Family_864b1 (Catalan twist)": [],
        "Family_864c1": [],
        "Family_864a1": [],
    }

    # Representatives:
    # Form 4 is 864b1: [2, -3, -6, -3, -2, 3, -6]
    # Form 10 is 864c1: [-2, 1, -2, 1, -6, -5, 6]
    # Form 8 is 864a1: [-1, -3, 3, 0, 4, -6, -6]
    rep_forms = {
        "Family_864b1 (Catalan twist)": 4,
        "Family_864c1": 10,
        "Family_864a1": 8,
    }

    form_dict = {f["index"]: f["a_q"] for f in rational_forms}

    for fam_name, rep_idx in rep_forms.items():
        rep_aqs = form_dict[rep_idx]
        for f in rational_forms:
            # Check if f is a twist of rep_aqs by D in fund_discs
            for D in fund_discs:
                twisted = [
                    int(sp.kronecker_symbol(D, p)) * rep_aqs[PRIME_INDICES[p]]
                    for p in ALL_PRIMES
                ]
                if twisted == f["a_q"]:
                    families[fam_name].append(f["index"])
                    break

    for fam_name, members in families.items():
        assert len(members) == 4, f"{fam_name} should have 4 members, got {len(members)}"

    # Check total partition
    all_members = set().union(*families.values())
    assert len(all_members) == 12

    return {
        "twist_discriminants": fund_discs,
        "families": families,
    }


def main() -> None:
    print("================================================================================")
    print("U110: HIGHER TRACE RIGIDITY AND MODULAR ANALYSIS FOR SIGNATURE (2, 3, 11)")
    print("================================================================================")

    # 1. Compute admissible Frey curve traces over F_q
    print("\n[1] ADMISSIBLE FREY CURVE TRACES OVER F_q FOR A^2 + B^3 = C^11 mod q:")
    admissible_data: dict[int, dict[str, Any]] = {}
    for q in PRIMES_Q:
        adm = compute_admissible_frey_traces(q)
        admissible_data[q] = adm
        print(f"\n--- Prime q = {q} ---")
        print(f"  Hasse interval: [-{adm['max_hasse']}, {adm['max_hasse']}], length = {len(adm['hasse_interval'])}")
        print(f"  11th power residues in F_{q}: {adm['pow11_count']} values -> {adm['pow11_elements']}")
        print(f"  Admissible pairs (A, B) in F_{q}^2 \\ {{(0, 0)}}: total = {adm['total_admissible_pairs']}")
        print(f"    - Good reduction pairs (A^2 + B^3 != 0): {adm['good_reduction_pairs']}")
        print(f"    - Bad reduction pairs  (A^2 + B^3 == 0): {adm['bad_reduction_pairs']}")
        print(f"  Distinct good traces a_{q}(E): {adm['distinct_good_traces']}")
        print(f"  Multiplicative reduction residues mod 11: +-({q}+1) mod 11 = {adm['bad_residues_mod11']}")
        print(f"  Bad reduction integers in Hasse interval: {adm['bad_integers_in_hasse']}")
        print(f"  Exact integer rigidity interval: {adm['rigid_interval']}")

    # Check structural theorem for q = 23
    assert admissible_data[23]["pow11_count"] == 3  # {0, 1, 22}
    assert admissible_data[23]["total_admissible_pairs"] == 68
    print("\n  [PASS] At q = 23, gcd(11, 22) = 11 forces C^11 in {0, 1, 22}, collapsing admissible pairs to 68 / 528 (87% prune)!")

    # 2. Extract Newforms at Levels 432 and 864 via PARI/GP
    print("\n[2] PARI/GP NEWSPACE DECOMPOSITION AT LEVELS 432 AND 864:")
    gp_forms = query_pari_gp_newforms()
    print(f"  Level 432: {len(gp_forms[432])} eigenforms (all rational, deg = 1)")
    print(f"  Level 864: {len(gp_forms[864])} eigenforms (12 rational, 2 quadratic)")

    # 3. Analyze Rational Newforms at Level 432
    print("\n[3] TRACE RIGIDITY & NON-DIVISIBILITY AT LEVEL 432:")
    level_432_analysis = []
    for f in gp_forms[432]:
        res = analyze_form_rigidity(f"432_{f['index']}", 432, f["a_q"], admissible_data)
        level_432_analysis.append(res)
        print(f"  Form 432_{f['index']}: a_q = {list(res['a_q'].values())}")
        print(f"    -> q nmid C for q in {res['non_div_primes']}")
        print(f"    -> Exact rigid traces a_q(E) = a_q(f) over Z: {res['exact_rigid_traces']}")
        if res["ambiguous_traces"]:
            print(f"    -> Ambiguous traces mod 11: {res['ambiguous_traces']}")

    # 4. Analyze Rational Newforms at Level 864
    print("\n[4] TRACE RIGIDITY & NON-DIVISIBILITY AT LEVEL 864:")
    level_864_analysis = []
    for f in gp_forms[864]:
        if f["degree"] == 1:
            res = analyze_form_rigidity(f"864_{f['index']}", 864, f["a_q"], admissible_data)
            level_864_analysis.append(res)
            print(f"  Form 864_{f['index']}: a_q = {list(res['a_q'].values())}")
            print(f"    -> q nmid C for q in {res['non_div_primes']}")
            print(f"    -> Exact rigid traces a_q(E) = a_q(f) over Z: {res['exact_rigid_traces']}")
            if res["ambiguous_traces"]:
                print(f"    -> Ambiguous traces mod 11: {res['ambiguous_traces']}")

    # 5. Core FNS Candidate Curves
    print("\n[5] ANALYSIS OF CORE FREITAS--NASKRECKI--STOLL (2020) CANDIDATES:")
    fns_curves_data = {}
    for name, coeffs in CURVES_REF.items():
        aqs = [compute_elliptic_curve_ap(coeffs, p) for p in ALL_PRIMES]
        res = analyze_form_rigidity(name, -1, aqs, admissible_data)
        fns_curves_data[name] = res
        print(f"  Candidate {name:8s}: a_q = {list(res['a_q'].values())}")
        print(f"    -> q nmid C for q in {res['non_div_primes']}")
        print(f"    -> Exact rigid traces a_q(E) = a_q(f) over Z: {res['exact_rigid_traces']}")
        if res["ambiguous_traces"]:
            print(f"    -> Ambiguous traces mod 11: {res['ambiguous_traces']}")

    # Specific theorem assertions for 864c1, 864a1, 864b1
    assert fns_curves_data["864c1"]["non_div_primes"] == [5, 7, 13, 17, 19, 23]
    print("\n  [PASS] THEOREM: For candidate 864c1, q does NOT divide C for ALL q in {5, 7, 13, 17, 19, 23}!")
    assert fns_curves_data["864c1"]["exact_rigid_traces"] == {5: -2, 7: 1, 13: 1}
    print("  [PASS] THEOREM: For candidate 864c1, exact integer rigidity holds at 5, 7, and 13:")
    print("         a_5(E) = -2, a_7(E) = 1, a_13(E) = 1 on the nose over Z!")

    assert fns_curves_data["864a1"]["non_div_primes"] == [5, 13, 19, 23]
    print("\n  [PASS] THEOREM: For candidate 864a1, q does NOT divide C for q in {5, 13, 19, 23}!")
    assert fns_curves_data["864a1"]["exact_rigid_traces"] == {5: -1, 13: 0}
    print("  [PASS] THEOREM: For candidate 864a1, exact integer rigidity holds at 5 and 13:")
    print("         a_5(E) = -1, a_13(E) = 0 on the nose over Z!")

    assert fns_curves_data["864b1"]["non_div_primes"] == [5, 17, 19, 23]
    print("\n  [PASS] THEOREM: For candidate 864b1 (Catalan twist), q does NOT divide C for q in {5, 17, 19, 23}!")
    assert fns_curves_data["864b1"]["exact_rigid_traces"] == {5: 2, 17: -2}
    print("  [PASS] THEOREM: For candidate 864b1, exact integer rigidity holds at 5 and 17:")
    print("         a_5(E) = 2, a_17(E) = -2 on the nose over Z!")

    # 6. Quadratic Twist Verification
    print("\n[6] QUADRATIC TWIST PARTITION OF S_2^new(864):")
    twist_data = verify_twist_families(gp_forms[864])
    for fam_name, members in twist_data["families"].items():
        print(f"  {fam_name}: Forms {members}")
    print("  [PASS] The 12 rational newforms at level 864 partition exactly into 3 twist families.")

    # 7. Catalan and Trivial Solution Verification
    print("\n[7] PERMANENT MODULAR BARRIER (CATALAN & TRIVIAL SOLUTIONS):")
    cat_aqs = [compute_frey_curve_ap(3, -2, p) for p in ALL_PRIMES]
    assert cat_aqs == [-2, -3, 6, 3, -2, -3, -6]
    print(f"  Catalan Frey curve E_{(3, -2)}: a_q = {cat_aqs}")
    twist2_cat = [
        int(sp.kronecker_symbol(8, p)) * cat_aqs[i]
        for i, p in enumerate(ALL_PRIMES)
    ]
    expected_864b = [2, -3, -6, -3, -2, 3, -6]
    assert twist2_cat == expected_864b
    print("  [PASS] 864b1 is the exact quadratic twist by 2 of the Catalan Frey curve E_{(3, -2)}!")

    # Trivial solution (0, 1) -> 288a1
    t01_aqs = [compute_frey_curve_ap(0, 1, p) for p in ALL_PRIMES]
    assert t01_aqs == [-4, 0, 0, -6, -8, 0, 0]
    print(f"  Trivial solution Frey curve E_{(0, 1)}: a_q = {t01_aqs} (identically 288a1, CM by Q(i))")

    # 8. Save structured results to JSON
    out_file = ROOT / "references/U110_signature_2_3_11_higher_traces.json"
    json_payload = {
        "status": "PASS",
        "description": "Trace analysis extension to q in {7, 13, 17, 19, 23} for signature (2, 3, 11)",
        "admissible_data": {
            q: {
                "max_hasse": adm["max_hasse"],
                "good_pairs": adm["good_reduction_pairs"],
                "bad_pairs": adm["bad_reduction_pairs"],
                "total_pairs": adm["total_admissible_pairs"],
                "bad_integers": adm["bad_integers_in_hasse"],
                "rigid_interval": adm["rigid_interval"],
                "frequencies": adm["trace_frequencies"],
            }
            for q, adm in admissible_data.items()
        },
        "level_432_analysis": level_432_analysis,
        "level_864_analysis": level_864_analysis,
        "fns_candidates": fns_curves_data,
        "twist_partition_864": twist_data,
    }
    out_file.write_text(json.dumps(json_payload, indent=2))
    print(f"\nSaved structured verification data to: {out_file}")
    print("\nALL VERIFICATIONS COMPLETED SUCCESSFULLY WITH RETURN CODE 0.")


if __name__ == "__main__":
    main()
