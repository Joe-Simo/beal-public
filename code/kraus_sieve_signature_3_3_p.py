#!/usr/bin/env python3
"""
Kraus Sieve Verification for Generalized Fermat Equation A^3 + B^3 = C^p
Signature: (3, 3, p)
Target Newform: 72a1 (y^2 = x^3 + 6x - 7)

This script performs the Kraus sieve modular elimination algorithm for prime
exponents p >= 5, searching for auxiliary primes q = 2kp + 1 (q does not divide 72)
that eliminate the persistent level-72 newform obstruction 72a1.
"""

import sys
import sympy

def trace_weierstrass(a4, a6, q):
    """
    Computes the trace of Frobenius a_q for the elliptic curve:
        E: y^2 = x^3 + a4*x + a6
    over the finite field F_q.
    Formula: a_q = - sum_{x in F_q} ( (x^3 + a4*x + a6) / q )
    """
    s = 0
    for x in range(q):
        rhs = (x**3 + a4 * x + a6) % q
        s += int(sympy.legendre_symbol(rhs, q))
    return -s

def kraus_sieve(p, max_k=50, verbose=True):
    """
    Executes the Kraus sieve for exponent p against the newform 72a1.
    Returns:
        (q, k, aq_72, aq_72_mod, admissible_traces) if eliminated,
        else None if no eliminating prime found within max_k.
    """
    a4_72 = 6
    a6_72 = -7
    
    if verbose:
        print("=" * 78)
        print(f"  KRAUS SIEVE MODULAR ELIMINATION AUDIT FOR EXPONENT p = {p}")
        print("=" * 78)
        print(f"Target Curve: 72a1  y^2 = x^3 + 6x - 7 (Conductor 72, j = 2048/3)")
        print(f"Algebraic Factorization: A^3 + B^3 = (A+B)(A^2 - AB + B^2) = C^p")
        print("-" * 78)
        
    for k in range(1, max_k + 1):
        q = 2 * k * p + 1
        n = 2 * k
        if not sympy.isprime(q) or 72 % q == 0:
            continue
            
        aq_72 = int(trace_weierstrass(a4_72, a6_72, q))
        aq_72_mod = aq_72 % p
        
        # Check multiplicative reduction condition at q | C:
        # If q | C, then F has multiplicative reduction at q,
        # so a_q(72a1) must satisfy a_q(72a1) = +- (q + 1) mod p.
        # Since q = 2kp + 1, q + 1 = 2 mod p, -(q+1) = -2 mod p.
        pm_qplus1 = {(q + 1) % p, (-(q + 1)) % p}
        q_can_divide_C = (aq_72_mod in pm_qplus1)
        
        # Subgroup of p-th powers in F_q^*
        # |Up| = (q - 1) / p = 2k
        Up = set(pow(x, p, q) for x in range(1, q))
        
        admissible_traces = set()
        
        # 1. Multiplicative reduction contribution (q | C):
        if q_can_divide_C:
            admissible_traces.update(pm_qplus1)
            
        # 2. Boundary contribution (q | B):
        # When q | B, A^3 = C^p. Since gcd(3, p) = 1, A is a p-th power in F_q^*.
        # The Frey curve specializes to y^2 = x^3 - A^3 over F_q.
        # Its trace over F_q is (+- a_q(y^2 = x^3 - 1)):
        aq_inf = int(trace_weierstrass(0, -1, q))
        admissible_traces.add(aq_inf % p)
        admissible_traces.add((-aq_inf) % p)
        
        # 3. Good reduction contribution (q does not divide BC):
        # Set t = A/B mod q in F_q \ {-1}.
        # By coprimality and algebraic descent:
        # Subcase 3.1: 3 does not divide C:
        #   A + B and A^2 - AB + B^2 are both coprime p-th powers.
        #   Dividing by B: t + 1 in Up and t^2 - t + 1 in Up.
        # Subcase 3.2: 3 divides C:
        #   v_3(C) >= 1. The 3-valuations distribute as (p-1, 1) or (1, p-1).
        #   (t + 1)/3^(p-1) in Up and (t^2 - t + 1)/3 in Up, OR
        #   (t + 1)/3 in Up and (t^2 - t + 1)/3^(p-1) in Up.
        valid_t = set()
        inv3 = pow(3, -1, q)
        inv3_p1 = pow(pow(3, p - 1, q), -1, q)
        
        for t in range(q):
            if (t + 1) % q == 0:
                continue # t = -1 corresponds to q | C
                
            f1 = (t + 1) % q
            f2 = (t**2 - t + 1) % q
            
            # Subcase 3.1
            if f1 in Up and f2 in Up:
                valid_t.add(t)
                continue
                
            # Subcase 3.2
            if ((f1 * inv3_p1) % q in Up) and ((f2 * inv3) % q in Up):
                valid_t.add(t)
                continue
            if ((f1 * inv3) % q in Up) and ((f2 * inv3_p1) % q in Up):
                valid_t.add(t)
                continue
                
        for t in valid_t:
            a4 = (3 * t) % q
            a6 = (1 - pow(t, 3, q)) % q
            aq_t = int(trace_weierstrass(a4, a6, q))
            admissible_traces.add(aq_t % p)
            admissible_traces.add((-aq_t) % p)
            
        is_eliminated = (aq_72_mod not in admissible_traces)
        
        if verbose:
            tag = "===> ELIMINATED! <===" if is_eliminated else "survives"
            print(f"k={k:2d} (n={n:2d}) | q={q:5d} | aq(72a1)={aq_72:3d} = {aq_72_mod:2d} mod {p} | "
                  f"q|C: {str(q_can_divide_C):5s} | |valid_t|={len(valid_t):2d} | "
                  f"|Admissible|={len(admissible_traces):2d}/{p} | {tag}")
            if is_eliminated:
                print("-" * 78)
                print(f"  CERTIFICATE FOR p = {p}:")
                print(f"  Auxiliary Prime q = {q} (k = {k}, n = {n})")
                print(f"  a_{q}(72a1) = {aq_72} = {aq_72_mod} (mod {p})")
                print(f"  q | C possible: {q_can_divide_C} (pm 2 mod {p} = {sorted(pm_qplus1)})")
                print(f"  Admissible traces mod {p}: {sorted(admissible_traces)}")
                print(f"  Target trace {aq_72_mod} NOT IN Admissible traces!")
                print(f"  CONCLUSION: Newform 72a1 is completely eliminated for p = {p} at q = {q}!")
                print("=" * 78 + "\n")
                return q, k, aq_72, aq_72_mod, admissible_traces
                
    if verbose:
        print(f"No eliminating prime found for p = {p} with k <= {max_k}.\n")
    return None

def main():
    test_primes = [5, 7, 11, 13, 19, 31, 37]
    results = {}
    for p in test_primes:
        res = kraus_sieve(p, max_k=50, verbose=True)
        results[p] = res
        
    print("\n" + "#" * 78)
    print("  SUMMARY MASTER TABLE OF KRAUS SIEVE VERIFICATIONS")
    print("#" * 78)
    print(f"{'p':4s} | {'q':6s} | {'k':3s} | {'n=2k':5s} | {'aq(72a1)':9s} | {'aq mod p':9s} | {'|Admissible|':12s} | {'Eliminated?':12s}")
    print("-" * 78)
    for p in test_primes:
        res = results[p]
        if res is not None:
            q, k, aq_72, aq_72_mod, admissible = res
            print(f"{p:4d} | {q:6d} | {k:3d} | {2*k:5d} | {aq_72:9d} | {aq_72_mod:9d} | {len(admissible):2d}/{p:<8d} | YES (q={q})")
        else:
            print(f"{p:4d} | {'--':6s} | {'--':3s} | {'--':5s} | {'--':9s} | {'--':9s} | {'--':12s} | NOT in range")
    print("#" * 78)

if __name__ == "__main__":
    main()
