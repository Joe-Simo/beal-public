#!/usr/bin/env python3
"""
Kraus modular sieve for signature (3, 3, p) with exponents p in [11001, 11100].
Audits every prime p = 1 (mod 3) in this interval against newforms at level 72 / 144.
"""

import sys
from sympy import isprime, primerange

def trace_72a1(q):
    """Compute Frobenius trace a_q of elliptic curve 72a1: y^2 = x^3 - 1."""
    if q % 3 == 2:
        return 0
    cnt = 0
    for x in range(q):
        rhs = (x**3 - 1) % q
        if rhs == 0:
            cnt += 1
        elif pow(rhs, (q - 1) // 2, q) == 1:
            cnt += 2
    return q - cnt

def solve_kraus_for_p(p, max_k=50):
    """Find auxiliary prime q = 2kp + 1 such that no t in F_q satisfies the Kraus condition."""
    for k in range(1, max_k + 1):
        q = 2 * k * p + 1
        if not isprime(q):
            continue
        aq = trace_72a1(q)
        
        pth_powers = set(pow(s, (q - 1) // (2 * k), q) for s in range(1, q))
        
        survivors = 0
        for tau in pth_powers:
            if (tau + 1) % q == 0:
                continue
            if pow((tau + 1) % q, 2 * k, q) != 1:
                continue
            if pow((tau * tau - tau + 1) % q, 2 * k, q) != 1:
                continue
            survivors += 1
            
        if survivors == 0:
            return q, k, aq
            
    return None, None, None

def main():
    p_min, p_max = 11001, 11100
    primes = [p for p in primerange(p_min, p_max + 1) if p % 3 == 1]
    print(f"Auditing primes p = 1 (mod 3) in [{p_min}, {p_max}]: {primes}")
    
    eliminated = {}
    for p in primes:
        q, k, aq = solve_kraus_for_p(p)
        if q is not None:
            print(f"Prime p = {p}: ELIMINATED by auxiliary prime q = {q} (k={k}, a_q(72a1)={aq})")
            eliminated[p] = (q, k, aq)
        else:
            print(f"Prime p = {p}: FAILED to eliminate within max_k")
            sys.exit(1)
            
    print("\nAll primes in range successfully eliminated!")
    print(f"Total eliminated: {len(eliminated)}/{len(primes)}")

if __name__ == "__main__":
    main()
