#!/usr/bin/env python3
"""
Master Verification Suite: Executes and audits all 14 core mathematical
milestones, test suites, and certificates for the Beal Conjecture Program.

Exit code 0: All milestones pass with 100% verification.
"""

import sys
import os
import subprocess
import time

MILESTONES = [
    ("Section 8 TypeScript Checker Suite", ["bun", "code/test_section8_counterexample_checker.ts"]),
    ("Section 8 Python Checker Suite", ["python3", "code/test_section8_counterexample_checker.py"]),
    ("Section 8 C+GMP Standalone Checker Suite", ["python3", "code/test_check_counterexample_gmp.py"]),
    ("Section 8 C+GMP Shell Test Suite", ["bash", "code/test_check_counterexample_gmp.sh"]),
    ("C+GMP Multi-Threaded Near-Misses Test", ["./code/beal_search_gmp", "--test-near-misses"]),
    ("Python Search Tool & Bridge Test Suite", ["python3", "code/test_beal_search.py"]),
    ("U97: Prime-5 Dihedral Galois Certificate", ["python3", "code/U97_prime5_galois_certificate.py"]),
    ("U99: Modular Newform Inventory Audit (Conductors | 864)", ["python3", "code/U99_newform_inventory_audit.py"]),
    ("U100: Orbit H LMFDB Hecke Elimination at 11", ["python3", "code/U100_orbit_h_hecke_elimination.py"]),
    ("U100: Signature (2, 3, 7) Poonen-Schaefer-Stoll Audit", ["python3", "code/U100_signature_2_3_7_pss_audit.py"]),
    ("U101: Breuil-Diamond Local Lift Bridge Certificate", ["python3", "code/U101_local_lift_bridge_certificate.py"]),
    ("U101: Modularity Lifting & Group-Theoretic Certification", ["python3", "code/U101_modularity_lifting_verification.py"]),
    ("U101: Decic Chabauty Feasibility (p=23, 29, 31)", ["/opt/homebrew/bin/gp", "-q", "code/U101_decic_chabauty_feasibility.gp"]),
    ("U102: Definitive Elimination of CM Orbit b", ["python3", "code/U102_orbit_b_definitive_elimination.py"]),
    ("U102: Rational Point Classification on C^-/k", ["python3", "code/U102_rational_points_analysis.py"]),
    ("U102: Genus-8 Coleman Integration & Annihilating Differentials", ["python3", "code/U102_coleman_integration_genus8.py"]),
    ("U102: Kraus Frey Modularity & Level-Lowering", ["python3", "code/U102_kraus_frey_modularity_verification.py"]),
    ("U102: Q-Curves over Q(i) & Quartic Beal Families Elimination", ["python3", "code/verify_qcurves_modular_forms.py"]),
    ("U103: Galois 17-Torsion Representation & V4 Image", ["python3", "code/U103_galois_representation_17_torsion.py"]),
    ("U103: Higher Decic Coleman Integration (p=19, 23, 29, 31)", ["python3", "code/U103_higher_decic_coleman.py"]),
    ("U103: Kraus Frey Level-576 Elimination for p=13", ["python3", "code/U103_kraus_frey_level576_elimination.py"]),
    ("U104: Kraus Frey Curve Mod-p Irreducibility", ["python3", "code/U104_kraus_frey_curve_mod_p_irreducibility.py"]),
    ("U105: Mod-7 Representation & X_0(14) Absolute Irreducibility", ["python3", "code/U105_mod7_representation_and_x0_14.py"]),
    ("U105: Signature (2, 3, 13) Frey & Modular Curve Analysis", ["python3", "code/explore_signature_2_3_13.py"]),
    ("U106: Algebraic Descent for Signature (3, 3, p)", ["python3", "code/U106_algebraic_descent.py"]),
    ("U106: Algebraic Descent Case II (3 | C) Thue Analysis", ["python3", "code/U106_case2_three_divides_C.py"]),
    ("U106: Kraus Sieve Elimination for Signature (3, 3, p)", ["python3", "code/kraus_sieve_signature_3_3_p.py"]),
    ("U106: Fontaine-Laffaille & Serre Weight Certification", ["python3", "code/U106_fontaine_laffaille_serre_weights.py"]),
    ("U102: PARI/GP Unconditional Class Number Certificate for L_11 & L_13", ["/opt/homebrew/bin/gp", "-q", "code/certify_p11_p13_class_groups.gp"]),
    ("U108: PARI/GP Subfield Decomposition for Split-2 Primes (p=31, 43)", ["/opt/homebrew/bin/gp", "-q", "code/decompose_split2_subfields.gp"]),
    ("U99/U102: PARI/GP Degree-34 Class Number & Regulator Certificate", ["/opt/homebrew/bin/gp", "-q", "code/certify_class_number.gp"]),
    ("U100/U102: PARI/GP 3-Adic Coleman Integration on C^-", ["/opt/homebrew/bin/gp", "-q", "code/coleman_integration_p3.gp"]),
]

def main():
    print("================================================================================")
    print("        BEAL CONJECTURE COMPREHENSIVE REPRODUCIBILITY & AUDIT SUITE             ")
    print("================================================================================")
    total = len(MILESTONES)
    passed = 0
    failures = []
    
    t_start = time.time()
    for idx, (name, cmd) in enumerate(MILESTONES, 1):
        print(f"\n[{idx}/{total}] RUNNING: {name}")
        print(f"       Command: {' '.join(cmd)}")
        t0 = time.time()
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            elapsed = time.time() - t0
            if res.returncode == 0:
                print(f"       STATUS: [PASS] ({elapsed:.2f}s)")
                passed += 1
            else:
                print(f"       STATUS: [FAIL] (return code {res.returncode})")
                print("       STDERR:", res.stderr[:300])
                failures.append((name, res.stderr))
        except Exception as e:
            print(f"       STATUS: [EXCEPTION] {e}")
            failures.append((name, str(e)))

    t_total = time.time() - t_start
    print("\n================================================================================")
    print(f" AUDIT SUMMARY: {passed}/{total} MILESTONES PASSED IN {t_total:.2f}s")
    print("================================================================================")
    
    if failures:
        print("\nFailed Milestones:")
        for name, err in failures:
            print(f"  - {name}: {err[:150]}")
        sys.exit(1)
    else:
        print(f"\nALL {total} AUDIT CERTIFICATES AND TEST SUITES EXECUTED WITH 100% PASS RATE!")
        sys.exit(0)

if __name__ == "__main__":
    main()
