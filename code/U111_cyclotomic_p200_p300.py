#!/usr/bin/env python3
"""
U111: Real Cyclotomic Class Number and Sahoo Class P_1 Audit for 200 < p < 300
=============================================================================

This script performs the arithmetic and number-theoretic audit of the
maximal real cyclotomic fields K^+ = Q(zeta_p)^+ for all 16 primes in (200, 300).

Target Equation: X^{2l} + Y^{2m} = Z^p, exponents l, m > 10^60.
Sahoo (2025) Class P_1 requires:
  1. 2 is inert in K^+ = Q(zeta_p)^+ (residue degree f^+ = (p-1)/2, splitting index g^+ = 1)
  2. h_p^+ = 1 (or algebraically, 2 does not divide h_p^+)
  3. p != 1 (mod 8) (which is automatically necessary for 2 to be inert)

Literature references for h_p^+:
  - F. J. van der Linden (1982), Math. Comp. 39(160), 693-707 (Odlyzko GRH bounds)
  - R. Schoof (1998, 2003), Math. Comp. 72(242), 913-937 (Tables of h_p^+ up to 10000; OEIS A230869/A230870)
  - J. C. Miller (2014, published Math. Comp. 84(295), 2459-2469; arXiv:1407.2373):
      * Under GRH: h_p^+ = 1 for all p <= 241 except p in {163, 191, 229}
        with h_{163}^+ = 4, h_{191}^+ = 11, h_{229}^+ = 3.
      * For 241 < p < 300: Schoof (2003) Main Table / OEIS A230869/A230870 gives:
        h_{257}^+ = 3, h_{277}^+ = 4, and h_p^+ = 1 for all other p in (200, 300).
"""

import sys
import time
import subprocess
import json

PRIMES = [
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293
]

# Known class numbers from Miller (2014), Schoof (2003), OEIS A230869 / A230870
LITERATURE_CLASS_NUMBERS = {
    211: {"h_plus": 1, "status": "Under GRH", "source": "Miller 2014 (Thm 1.1) / Schoof 2003"},
    223: {"h_plus": 1, "status": "Under GRH", "source": "Miller 2014 (Thm 1.1) / Schoof 2003"},
    227: {"h_plus": 1, "status": "Under GRH", "source": "Miller 2014 (Thm 1.1) / Schoof 2003"},
    229: {"h_plus": 3, "status": "Under GRH", "source": "Miller 2014 (Thm 1.1) / Schoof 2003"},
    233: {"h_plus": 1, "status": "Under GRH", "source": "Miller 2014 (Thm 1.1) / Schoof 2003"},
    239: {"h_plus": 1, "status": "Under GRH", "source": "Miller 2014 (Thm 1.1) / Schoof 2003"},
    241: {"h_plus": 1, "status": "Under GRH", "source": "Miller 2014 (Thm 1.1) / Schoof 2003"},
    251: {"h_plus": 1, "status": "Under GRH", "source": "Schoof 2003 Main Table"},
    257: {"h_plus": 3, "status": "Under GRH", "source": "Schoof 2003 / OEIS A230869 (Fermat prime F_4)"},
    263: {"h_plus": 1, "status": "Under GRH", "source": "Schoof 2003 Main Table"},
    269: {"h_plus": 1, "status": "Under GRH", "source": "Schoof 2003 Main Table"},
    271: {"h_plus": 1, "status": "Under GRH", "source": "Schoof 2003 Main Table"},
    277: {"h_plus": 4, "status": "Under GRH", "source": "Schoof 2003 / OEIS A230869"},
    281: {"h_plus": 1, "status": "Under GRH", "source": "Schoof 2003 Main Table"},
    283: {"h_plus": 1, "status": "Under GRH", "source": "Schoof 2003 Main Table"},
    293: {"h_plus": 1, "status": "Under GRH", "source": "Schoof 2003 Main Table"},
}

def compute_order_mod_p(base, p):
    """Compute multiplicative order of base modulo p."""
    cur = base % p
    order = 1
    while cur != 1:
        cur = (cur * base) % p
        order += 1
    return order

def pari_factor_mod2(p, d):
    """
    Use PARI/GP to factor the minimal polynomial of Q(zeta_p)^+ modulo 2.
    Returns list of degrees of irreducible factors.
    """
    gp_code = f"P = polsubcyclo({p}, {d}); F = factormod(P, 2); print([poldegree(F[k,1]) | k <- [1..matsize(F)[1]]]);"
    try:
        res = subprocess.run(
            ["gp", "-q", "-s", "512000000"],
            input=gp_code,
            capture_output=True,
            text=True,
            timeout=15
        )
        if res.returncode == 0 and res.stdout.strip():
            out = res.stdout.strip().replace(";", "")
            return eval(out)
    except Exception as e:
        pass
    return None

def analyze_prime(p):
    """
    Perform complete algebraic analysis of prime p in Q(zeta_p)^+.
    """
    d = (p - 1) // 2
    pmod8 = p % 8
    ord2 = compute_order_mod_p(2, p)
    
    # Check if -1 is in <2 mod p>
    has_neg1 = (ord2 % 2 == 0 and pow(2, ord2 // 2, p) == p - 1)
    
    # Residue degree in K^+
    f_plus = ord2 // 2 if has_neg1 else ord2
    g_plus = d // f_plus
    is_inert = (g_plus == 1)
    
    # PARI verification
    t0 = time.time()
    pari_factors = pari_factor_mod2(p, d)
    t_pari = time.time() - t0
    
    # Literature class number
    lit = LITERATURE_CLASS_NUMBERS.get(p, {"h_plus": None, "status": "Unknown", "source": "N/A"})
    h_plus = lit["h_plus"]
    h_status = lit["status"]
    h_source = lit["source"]
    
    h_is_one = (h_plus == 1)
    two_div_h = (h_plus % 2 == 0) if h_plus is not None else False
    
    # Classification category
    if is_inert:
        if h_plus == 1:
            classification = "Class P_1 (GRH ELIM)"
        elif two_div_h:
            classification = f"Non-P_1: Even h^+ ({h_plus})"
        else:
            classification = f"Non-P_1: Odd h^+ > 1 ({h_plus})"
    else:
        if pmod8 == 1:
            classification = "Non-P_1: p = 1 mod 8"
        else:
            classification = f"Non-P_1: Split-2 (g^+={g_plus})"
            
    return {
        "p": p,
        "pmod8": pmod8,
        "d": d,
        "ord2": ord2,
        "has_neg1": has_neg1,
        "f_plus": f_plus,
        "g_plus": g_plus,
        "is_inert": is_inert,
        "pari_factors": pari_factors,
        "t_pari": t_pari,
        "h_plus": h_plus,
        "h_status": h_status,
        "h_source": h_source,
        "h_is_one": h_is_one,
        "two_div_h": two_div_h,
        "classification": classification
    }

def main():
    print("=" * 115)
    print("  U111: REAL CYCLOTOMIC CLASS NUMBER AUDIT AND SAHOO CLASS P_1 CLASSIFICATION (200 < p < 300)")
    print("=" * 115)
    print(f"{'p':<4} | {'p%8':<4} | {'d':<3} | {'ord2':<4} | {'-1 in <2>':<9} | {'f+':<3} | {'g+':<3} | {'Inert?':<6} | {'PARI Factors':<16} | {'h+':<3} | {'h+ Cert':<11} | {'Classification':<22}")
    print("-" * 115)
    
    results = []
    p1_grh = []
    non_p1_split2 = []
    non_p1_mod8 = []
    non_p1_class_num = []
    
    for p in PRIMES:
        res = analyze_prime(p)
        results.append(res)
        
        cls = res["classification"]
        if "GRH ELIM" in cls:
            p1_grh.append(p)
        elif "p = 1 mod 8" in cls:
            non_p1_mod8.append(p)
        elif "Split-2" in cls:
            non_p1_split2.append(p)
        elif "h^+" in cls:
            non_p1_class_num.append(p)
            
        pari_str = str(res["pari_factors"]) if res["pari_factors"] else "N/A"
        if len(pari_str) > 16:
            pari_str = f"[{res['pari_factors'][0]}x{len(res['pari_factors'])}]"
            
        print(f"{res['p']:<4d} | {res['pmod8']:<4d} | {res['d']:<3d} | {res['ord2']:<4d} | "
              f"{'YES' if res['has_neg1'] else 'NO':<9s} | {res['f_plus']:<3d} | {res['g_plus']:<3d} | "
              f"{'YES' if res['is_inert'] else 'NO':<6s} | {pari_str:<16s} | "
              f"{res['h_plus']:<3d} | {res['h_status']:<11s} | {res['classification']:<22s}")
        
    print("=" * 115)
    print("\n--- SUMMARY OF AUDIT RESULTS (200 < p < 300) ---")
    print(f"Total primes audited: {len(PRIMES)}")
    print(f"Primes where 2 is inert in Q(zeta_p)^+ (g^+ = 1): {len(p1_grh) + len(non_p1_class_num)} / {len(PRIMES)} ({(len(p1_grh) + len(non_p1_class_num))/len(PRIMES)*100:.1f}%)")
    print(f"  - Inert primes: {sorted(p1_grh + non_p1_class_num)}")
    print(f"Primes where 2 splits in Q(zeta_p)^+ (g^+ >= 2): {len(non_p1_mod8) + len(non_p1_split2)} / {len(PRIMES)} ({(len(non_p1_mod8) + len(non_p1_split2))/len(PRIMES)*100:.1f}%)")
    print(f"  - Split primes: {sorted(non_p1_mod8 + non_p1_split2)}")
    
    print("\n--- CLASS P_1 ASYMPTOTIC ELIMINATION (Sahoo 2025: X^{{2l}} + Y^{{2m}} = Z^p) ---")
    print(f"Class P_1 (Strict h_p^+ = 1, Asymptotically Eliminated under GRH): {len(p1_grh)} / {len(PRIMES)} ({len(p1_grh)/len(PRIMES)*100:.1f}%)")
    print(f"  - Certified Primes in Class P_1 (under GRH): {p1_grh}")
    
    print("\n--- NON-P_1 EXCLUSIONS & FAILURE MECHANISMS ---")
    print(f"1. Quadratic Field Splitting (p = 1 mod 8, 2 splits in Q(sqrt(p))): {len(non_p1_mod8)} primes: {non_p1_mod8}")
    print(f"2. Cyclotomic Splitting (p != 1 mod 8, ord_p(2) small): {len(non_p1_split2)} primes: {non_p1_split2}")
    print(f"3. Note on Non-Trivial Class Numbers in (200, 300):")
    print(f"   * p = 229: h_{{229}}^+ = 3 (already split-2: g^+ = 3, ord = 76)")
    print(f"   * p = 257: h_{{257}}^+ = 3 (already split-2: g^+ = 16, ord = 16, Fermat prime F_4)")
    print(f"   * p = 277: h_{{277}}^+ = 4 (already split-2: g^+ = 3, ord = 92)")
    print(f"   -> Remarkably, NO prime with 2 inert has h_p^+ > 1 in this interval!")
    
    # Cumulative stats across [19, 300)
    print("\n--- CUMULATIVE SUMMARY FOR 19 <= p < 300 ---")
    # Previous ranges:
    # [19, 100): 18 primes, 12 P_1 (19, 23, 29*, 37, 47, 53, 59, 61, 67, 71, 79, 83)
    # [100, 200): 21 primes, 12 P_1 (101, 103, 107, 131, 139, 149, 167, 173, 179, 181, 197, 199)
    # [200, 300): 16 primes, 7 P_1 (211, 227, 239, 263, 269, 271, 293)
    total_primes = 18 + 21 + 16
    total_p1 = 12 + 12 + len(p1_grh)
    print(f"Total primes audited in [19, 300): {total_primes}")
    print(f"Total Class P_1 primes in [19, 300): {total_p1} / {total_primes} ({total_p1/total_primes*100:.1f}%)")
    
    # Save output json
    json_path = "research/checkpoints/U111_real_cyclotomic_audit_p200_p300.json"
    try:
        with open(json_path, "w") as f:
            json.dump({
                "checkpoint": "U111",
                "primes_audited": len(PRIMES),
                "p1_grh": p1_grh,
                "non_p1_mod8": non_p1_mod8,
                "non_p1_split2": non_p1_split2,
                "non_trivial_hplus_primes": [229, 257, 277],
                "cumulative_19_300": {
                    "total_primes": total_primes,
                    "total_p1": total_p1,
                    "percentage": round(total_p1 / total_primes * 100, 1)
                },
                "details": results
            }, f, indent=2)
        print(f"\n[+] Audit data successfully exported to {json_path}")
    except Exception as e:
        print(f"[-] Could not export JSON: {e}")

if __name__ == "__main__":
    main()
