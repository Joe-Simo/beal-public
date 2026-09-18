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
    ("U332: Primary-Source Check of the Instance-Closure Rows",
     ["python3", "code/U332_rows_source_check.py"]),
    ("U328: Positive Controls for the Empty Searches (C156, C081, C045)",
     ["python3", "code/U328_search_controls.py"]),
    ("U323: Counterexample Search Against Every Named Hypothesis Prop",
     ["python3", "code/U323_named_prop_countersearch.py"]),
    ("U320: Assert-Based Regression Guards for the U309-U319 Obstruction Cycle",
     ["python3", "code/U320_regression_checks.py"]),
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
    ("U109: PARI/GP Descent & Chabauty Verification for (2, 3, 8) & (2, 3, 9)", ["/opt/homebrew/bin/gp", "-q", "code/verify_238_239_descent.gp"]),
    ("U109: Signature (2, 3, 7) & (2, 3, 11) Modular Forms & LMFDB Audit", ["python3", "code/U109_signature_2_3_7_and_2_3_11_verification.py"]),
    ("U110: Kraus Sieve Elimination for Signature (3, 3, p) [p in 43..100]", ["python3", "code/U110_kraus_sieve_p43_p100.py"]),
    ("U110: Serre Uniformity & Cartan Bound Certification", ["python3", "code/U110_serre_uniformity_cartan_bounds.py"]),
    ("U110: Real Cyclotomic Class Number & Sahoo P1 Audit (p in 100..200)", ["python3", "code/U110_cyclotomic_p100_p200.py"]),
    ("U110: PARI/GP 3-Adic Coleman & Strassman Zero Bounds on C^-", ["/opt/homebrew/bin/gp", "-q", "code/U110_coleman_strassman_genus8.gp"]),
    ("U110: Frey Conductor 72 & 144 Newform Inventory Audit", ["python3", "code/U110_frey_conductor_72_newform_inventory.py"]),
    ("U110: Signature (2, 3, 11) Higher Prime Trace Rigidity", ["python3", "code/U110_signature_2_3_11_higher_traces.py"]),
    ("U110: Signature (2, 3, 13) Twisted Modular Curve Geometry Audit", ["python3", "code/U110_verify_twisted_modular_curve_geometry.py"]),
    ("U110: PARI/GP Elliptic Chabauty & 2-Descent for (2, 3, 8)", ["/opt/homebrew/bin/gp", "-q", "code/U110_elliptic_chabauty_2_3_8.gp"]),
    ("U110: Linear Forms in Logarithms Bounds & Exponent Envelope", ["python3", "code/U110_linear_forms_logarithms_bounds.py"]),
    ("U110: Signature (2, 4, n) Serre Weight & Modular Verification", ["python3", "code/U110_signature_2_4_n_modular_verification.py"]),
    ("U110: PARI/GP Hilbert Newform Norm 4000 Non-Existence Certificate", ["/opt/homebrew/bin/gp", "-q", "code/U110_hilbert_forms_norm4000.gp"]),
    ("U111: Kraus Sieve Elimination for Signature (3, 3, p) [p in 101..200]", ["python3", "code/U111_kraus_sieve_p101_p200.py"]),
    ("U111: Kraus Sieve Elimination for Signature (3, 3, p) [p in 201..300]", ["python3", "code/U111_kraus_sieve_p201_p300.py"]),
    ("U111: Real Cyclotomic Class Number & Sahoo P1 Audit (p in 200..300)", ["python3", "code/U111_cyclotomic_p200_p300.py"]),
    ("U111: Universal Serre Uniformity & Cartan Elimination for All Signatures", ["python3", "code/U111_general_cartan_elimination.py"]),
    ("U111: Multi-Prime Simultaneous Sieve for Signature (2, 3, 11)", ["python3", "code/U111_signature_2_3_11_simultaneous_sieve.py"]),
    ("U111: Kraus Sieve Elimination for Signature (3, 3, p) [p in 301..400]", ["python3", "code/U111_kraus_sieve_p301_p400.py"]),
    ("U111: Real Cyclotomic Class Number & Sahoo P1 Audit (p in 300..400)", ["python3", "code/U111_cyclotomic_p300_p400.py"]),
    ("U111: Signature (2, 4, n) Full Resolution for all n >= 4", ["python3", "code/U111_signature_2_4_n_lucas_lehmer.py"]),
    ("U111: Universal Borel Subgroup Elimination & Full Galois Surjectivity", ["python3", "code/U111_universal_borel_elimination.py"]),
    ("U111: Frey Conductor 288 & 576 Elimination for p in [17..37]", ["python3", "code/U111_conductor_288_576_audit.py"]),
    ("U111: Formal Immersion Order-16 Obstruction at Infinity for (2, 3, 13)", ["python3", "code/U111_formal_immersion_13.py"]),
    ("U111: Matveev 3-Variable Linear Forms in Logarithms Bounds", ["python3", "code/U111_matveev_3variable_logarithms.py"]),
    ("U111: Modular Curve X_{E_0}(17) Genus 133 & Automorphism Audit", ["python3", "code/U111_automorphism_twisted_17.py"]),
    ("U111: Signature (2, 3, 11) Deep Sieve & Diophantine Search", ["python3", "code/U111_signature_2_3_11_deep_search.py"]),
    ("U111: PARI/GP X_0(17) Selmer & 2-Descent Field of Degree 36", ["/opt/homebrew/bin/gp", "-q", "code/U111_x0_17_selmer_degree36.gp"]),
    ("U111: Modular Curve X_{E_0}(19) Genus 196 & Automorphism Audit", ["python3", "code/U111_automorphism_twisted_19.py"]),
    ("U111: PARI/GP 5-Adic Coleman & Strassman Zero Bounds on C^-", ["/opt/homebrew/bin/gp", "-q", "code/U111_coleman_5adic_genus8.gp"]),
    ("U111: Signature (5, 5, p) Modular Level-Lowering & Hilbert Sieve over Q(sqrt(5))", ["python3", "code/U111_signature_5_5_p_hilbert_sieve.py"]),
    ("U111: Real Cyclotomic Class Number & Sahoo P1 Audit (p in 400..500)", ["python3", "code/U111_cyclotomic_p400_p500.py"]),
    ("U111: Kraus Sieve Elimination for Signature (3, 3, p) [p in 401..500]", ["python3", "code/U111_kraus_sieve_p401_p500.py"]),
    ("U111: PARI/GP Hilbert Forms over Q(sqrt(2)) & Resolution of (4, 4, p)", ["/opt/homebrew/bin/gp", "-q", "code/U111_hilbert_forms_q_sqrt2.gp"]),
    ("U111: Real Cyclotomic Class Number & Sahoo P1 Audit (p in 500..600)", ["python3", "code/U111_cyclotomic_p500_p600.py"]),
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
