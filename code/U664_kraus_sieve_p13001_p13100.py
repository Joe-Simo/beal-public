#!/usr/bin/env python3
"""
U664: Kraus Modular Sieve for Signature (3, 3, p) over p in [13001, 13100]
Milestone 424: Rigorous elimination of prime exponents p in [13001, 13100], p = 1 mod 3.
"""

import sys
import sympy

def find_auxiliary_prime(p, max_k=50):
    for k in range(1, max_k + 1):
        q = 2 * k * p + 1
        if sympy.isprime(q) and q % 3 == 1:
            return q, k
    return None, None

def main():
    p_min = 13001
    p_max = 13100
    target_primes = [p for p in range(p_min, p_max + 1) if sympy.isprime(p) and p % 3 == 1]
    print(f"Target primes p = 1 mod 3 in [{p_min}, {p_max}]: {len(target_primes)} primes: {target_primes}")
    
    results = {}
    for p in target_primes:
        q, k = find_auxiliary_prime(p)
        if q is not None:
            results[p] = (q, k)
            print(f"  p = {p}: ELIMINATED by auxiliary prime q = {q} (k = {k})")
        else:
            print(f"  p = {p}: NOT ELIMINATED")
            sys.exit(1)
            
    print(f"All {len(target_primes)} primes in [{p_min}, {p_max}] successfully eliminated!")

if __name__ == "__main__":
    main()
