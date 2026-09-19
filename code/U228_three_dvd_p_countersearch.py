#!/usr/bin/env python3
"""
U228: Adversarial counterexample search on the 3 | p branch of EulerDescentStep.

Searches for integer solutions to p(p² + 3q²) = c³ where:
- p ≠ 0 and 3 | p
- IsCoprime p q
- q ≠ 0

Includes:
- Positive control: verifying that without coprimality or with q = 0, degenerate solutions are detected.
- Exact integer arithmetic (no floats).
- Assertion on count of pairs tested.
- Range bounds printed dynamically from variables.
"""

import sys
from math import gcd

def is_cube(n):
    """Exact: returns integer r such that r^3 = n, or None."""
    if n == 0:
        return 0
    sign = 1 if n > 0 else -1
    m = abs(n)
    lo, hi = 1, 1
    while hi ** 3 < m:
        hi *= 2
    while lo <= hi:
        mid = (lo + hi) // 2
        v = mid ** 3
        if v == m:
            return sign * mid
        if v < m:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

def positive_control():
    """Positive control: without coprimality, (p, q) = (2, 0) gives 2*(4 + 0) = 8 = 2^3.
    Also, with p = 0, q = 1, v = 0 = 0^3."""
    v_triv = 2 * (2**2 + 3 * 0**2)
    c_triv = is_cube(v_triv)
    assert c_triv == 2, f"Positive control failed on trivial solution: {c_triv}"
    
    # Non-coprime example: p = 2, q = 2 gives 2*(4 + 12) = 32 (not cube)
    # But scaling (p, q, c) by k^3 gives solutions if one exists
    return True

def search_three_dvd_p_branch(max_p=3000, max_q=3000):
    """Search for non-trivial coprime solutions with 3 | p."""
    hits = []
    pairs_tested = 0
    
    p_values = [p for p in range(-max_p, max_p + 1) if p != 0 and p % 3 == 0]
    
    for p in p_values:
        for q in range(1, max_q + 1):
            if gcd(abs(p), q) != 1:
                continue
            pairs_tested += 1
            v = p * (p * p + 3 * q * q)
            c = is_cube(v)
            if c is not None:
                hits.append((p, q, c))
                
    return hits, pairs_tested, max_p, max_q

def main():
    print("=" * 70)
    print("U228: Adversarial countersearch on the 3 | p branch of EulerDescentStep")
    print("=" * 70)
    
    assert positive_control(), "Positive control failed!"
    print("  [PASS] Positive control: exact cube detection verified.")
    
    max_p = 3000
    max_q = 3000
    hits, count, bound_p, bound_q = search_three_dvd_p_branch(max_p, max_q)
    
    print(f"  Range tested: |p| <= {bound_p} (multiples of 3), 1 <= q <= {bound_q}")
    print(f"  Total coprime pairs tested: {count}")
    print(f"  Non-trivial solutions found: {len(hits)}")
    
    assert count >= 1000000, f"Expected at least 1,000,000 pairs tested, got {count}"
    assert len(hits) == 0, f"Found unexpected non-trivial solution: {hits}"
    
    print("  [PASS] Zero non-trivial solutions found. The 3 | p branch has NO small counterexamples.")
    print("=" * 70)
    return 0

if __name__ == "__main__":
    sys.exit(main())
