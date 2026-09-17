#!/usr/bin/env python3
"""
U110: Real Cyclotomic Class Number and Sahoo Class P_1 Audit for 100 < p < 200
=============================================================================

This script performs the complete arithmetic and number-theoretic audit of
the maximal real cyclotomic fields K^+ = Q(zeta_p)^+ for all 21 primes
in the interval (100, 200).

Target Equation: X^{2l} + Y^{2m} = Z^p, exponents l, m > 10^60.
Sahoo (2025) Class P_1 requires:
  1. 2 is inert in K^+ = Q(zeta_p)^+ (residue degree f^+ = (p-1)/2, splitting index g^+ = 1)
  2. h_p^+ = 1 (or algebraically, 2 does not divide h_p^+)
  3. p != 1 (mod 8) (which is automatically necessary for 2 to be inert)

Literature references for h_p^+:
  - F. J. van der Linden (1982), Math. Comp. 39(160), 693-707 (GRH for p < 163, h_{163}^+ = 4)
  - R. Schoof (1998, 2003), Math. Comp. 72(242), 913-937 (Tables of h_p^+ up to 10000)
  - J. C. Miller (2014, published Math. Comp. 84(295), 2459-2469; arXiv:1407.2373):
      * Unconditional: h_p^+ = 1 for all p <= 151
      * Under GRH: h_p^+ = 1 for all p <= 241 except p in {163, 191, 229}
        with h_{163}^+ = 4, h_{191}^+ = 11, h_{229}^+ = 3.
"""

import sys
import time
import subprocess
import json

PRIMES = [
    101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
    151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
]

# Known class numbers from Miller (2014), Schoof (2003), van der Linden (1982)
# Miller 2014: Unconditional for p <= 151; under GRH for 151 < p <= 241.
LITERATURE_CLASS_NUMBERS = {
    101: {"h_plus": 1, "status": "Unconditional", "source": "Miller 2014 (Thm 1.1)"},
    103: {"h_plus": 1, "status": "Unconditional", "source": "Miller 2014 (Thm 1.1)"},
    107: {"h_plus": 1, "status": "Unconditional", "source": "Miller 2014 (Thm 1.1)"},
    109: {"h_plus": 1, "status": "Unconditional", "source": "Miller 2014 (Thm 1.1)"},
    113: {"h_plus": 1, "status": "Unconditional", "source": "Miller 2014 (Thm 1.1)"},
    127: {"h_plus": 1, "status": "Unconditional", "source": "Miller 2014 (Thm 1.1)"},
    131: {"h_plus": 1, "status": "Unconditional", "source": "Miller 2014 (Thm 1.1)"},
    137: {"h_plus": 1, "status": "Unconditional", "source": "Miller 2014 (Thm 1.1)"},
    139: {"h_plus": 1, "status": "Unconditional", "source": "Miller 2014 (Thm 1.1)"},
    149: {"h_plus": 1, "status": "Unconditional", "source": "Miller 2014 (Thm 1.1)"},
    151: {"h_plus": 1, "status": "Unconditional", "source": "Miller 2014 (Thm 1.1)"},
    157: {"h_plus": 1, "status": "Under GRH",     "source": "van der Linden 1982 / Miller 2014"},
    163: {"h_plus": 4, "status": "Under GRH",     "source": "van der Linden 1982 / Miller 2014 (Thm 1.1)"},
    167: {"h_plus": 1, "status": "Under GRH",     "source": "Schoof 2003 / Miller 2014 (Thm 1.1)"},
    173: {"h_plus": 1, "status": "Under GRH",     "source": "Miller 2014 (Thm 1.1)"},
    179: {"h_plus": 1, "status": "Under GRH",     "source": "Miller 2014 (Thm 1.1)"},
    181: {"h_plus": 1, "status": "Under GRH",     "source": "Miller 2014 (Thm 1.1)"},
    191: {"h_plus": 11,"status": "Under GRH",     "source": "Schoof 2003 / Miller 2014 (Thm 1.1)"},
    193: {"h_plus": 1, "status": "Under GRH",     "source": "Miller 2014 (Thm 1.1)"},
    197: {"h_plus": 1, "status": "Under GRH",     "source": "Miller 2014 (Thm 1.1)"},
    199: {"h_plus": 1, "status": "Under GRH",     "source": "Miller 2014 (Thm 1.1)"},
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
            ["gp", "-q", "-s", "256000000"],
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
    # In a cyclic group of order ord2, -1 is in <2> iff ord2 is even and 2^(ord2/2) = -1 mod p
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
            if h_status == "Unconditional":
                classification = "Class P_1 (UNCOND ELIM)"
            else:
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
    print("  U110: REAL CYCLOTOMIC CLASS NUMBER AUDIT AND SAHOO CLASS P_1 CLASSIFICATION (100 < p < 200)")
    print("=" * 115)
    print(f"{'p':<4} | {'p%8':<4} | {'d':<3} | {'ord2':<4} | {'-1 in <2>':<9} | {'f+':<3} | {'g+':<3} | {'Inert?':<6} | {'PARI Factors':<16} | {'h+':<3} | {'h+ Cert':<13} | {'Classification':<22}")
    print("-" * 115)
    
    results = []
    p1_uncond = []
    p1_grh = []
    non_p1_split2 = []
    non_p1_mod8 = []
    non_p1_class_num = []
    
    for p in PRIMES:
        res = analyze_prime(p)
        results.append(res)
        
        # Classification tracking
        cls = res["classification"]
        if "UNCOND ELIM" in cls:
            p1_uncond.append(p)
        elif "GRH ELIM" in cls:
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
              f"{res['h_plus']:<3d} | {res['h_status']:<13s} | {res['classification']:<22s}")
        
    print("=" * 115)
    print("\n--- SUMMARY OF AUDIT RESULTS (100 < p < 200) ---")
    print(f"Total primes audited: {len(PRIMES)}")
    print(f"Primes where 2 is inert in Q(zeta_p)^+ (g^+ = 1): {len(p1_uncond) + len(p1_grh) + len(non_p1_class_num)} / {len(PRIMES)} ({(len(p1_uncond) + len(p1_grh) + len(non_p1_class_num))/len(PRIMES)*100:.1f}%)")
    print(f"  - Inert primes: {sorted(p1_uncond + p1_grh + non_p1_class_num)}")
    print(f"Primes where 2 splits in Q(zeta_p)^+ (g^+ >= 2): {len(non_p1_mod8) + len(non_p1_split2)} / {len(PRIMES)} ({(len(non_p1_mod8) + len(non_p1_split2))/len(PRIMES)*100:.1f}%)")
    print(f"  - Split primes: {sorted(non_p1_mod8 + non_p1_split2)}")
    
    print("\n--- CLASS P_1 ASYMPTOTIC ELIMINATION (Sahoo 2025: X^{{2l}} + Y^{{2m}} = Z^p) ---")
    print(f"Class P_1 (Strict h_p^+ = 1, Asymptotically Eliminated): {len(p1_uncond) + len(p1_grh)} / {len(PRIMES)} ({(len(p1_uncond) + len(p1_grh))/len(PRIMES)*100:.1f}%)")
    print(f"  - Unconditional (p <= 151, Miller 2014): {len(p1_uncond)} primes: {p1_uncond}")
    print(f"  - Under GRH (p > 151, Miller 2014 / Schoof 2003): {len(p1_grh)} primes: {p1_grh}")
    
    print("\n--- NON-P_1 EXCLUSIONS & FAILURE MECHANISMS ---")
    print(f"1. Class Number Obstructions (2 inert, but h_p^+ != 1): {len(non_p1_class_num)} primes: {non_p1_class_num}")
    for p in non_p1_class_num:
        print(f"   * p = {p}: h_{{{p}}}^+ = {LITERATURE_CLASS_NUMBERS[p]['h_plus']} ({'EVEN, 2 | h+' if LITERATURE_CLASS_NUMBERS[p]['h_plus']%2==0 else 'ODD, 2 \u2224 h+'}), Source: {LITERATURE_CLASS_NUMBERS[p]['source']}")
    print(f"2. Quadratic Field Splitting (p = 1 mod 8, 2 splits in Q(sqrt(p))): {len(non_p1_mod8)} primes: {non_p1_mod8}")
    print(f"3. Cyclotomic Splitting (p != 1 mod 8, ord_p(2) small): {len(non_p1_split2)} primes: {non_p1_split2}")
    
    # Save output json
    json_path = "research/checkpoints/U110_real_cyclotomic_audit_p100_p200.json"
    try:
        with open(json_path, "w") as f:
            json.dump({
                "checkpoint": "U110",
                "primes_audited": len(PRIMES),
                "p1_unconditional": p1_uncond,
                "p1_grh": p1_grh,
                "non_p1_class_number_anomaly": non_p1_class_num,
                "non_p1_mod8": non_p1_mod8,
                "non_p1_split2": non_p1_split2,
                "details": results
            }, f, indent=2)
        print(f"\n[+] Audit data successfully exported to {json_path}")
    except Exception as e:
        print(f"[-] Could not export JSON: {e}")

if __name__ == "__main__":
    main()
