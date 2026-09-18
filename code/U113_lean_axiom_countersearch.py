"""COUNTERSEARCH against the custom axioms in formal/Beal/.

Target: axiom kraus_even_c_level18_newform
  hypotheses: A,B,C > 0, p >= 3, gcd(A,B) = 1, A^3 + B^3 = C^p, C even
  conclusion: cuspFormsDimGamma0 18 2 >= 1

dim S_2(Gamma_0(18)) = 0, because X_0(18) has genus 0. So ANY witness satisfying the
hypotheses makes the Lean development INCONSISTENT (False becomes provable, and every
'theorem' in it becomes vacuous).

Structure: A,B must both be odd (C even => A^3+B^3 even; gcd(A,B)=1 forbids both even).
Then A^3+B^3 = (A+B)(A^2-AB+B^2) with the second factor ODD, so every factor of 2 in C^p
comes from A+B, requiring v_2(A+B) >= 3 for p >= 3. Exact integer arithmetic only.
"""
from math import gcd

LIMIT = 3000
found = []
checked = 0

def exact_root(n: int, p: int) -> int | None:
    """Exact integer p-th root of n, or None. Pure integer arithmetic."""
    if n < 1:
        return None
    lo, hi = 1, 1 << ((n.bit_length() + p - 1) // p + 1)
    while lo <= hi:
        mid = (lo + hi) // 2
        v = mid ** p
        if v == n:
            return mid
        if v < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


for A in range(1, LIMIT + 1, 2):          # A odd
    for B in range(A, LIMIT + 1, 2):      # B odd, B >= A wlog by symmetry
        if gcd(A, B) != 1:
            continue
        S = A ** 3 + B ** 3
        # every factor of 2 comes from A+B; need 2^3 | S for C even, p >= 3
        if S % 8 != 0:
            continue
        checked += 1
        p = 3
        while 2 ** p <= S:
            C = exact_root(S, p)
            if C is not None and C % 2 == 0 and C > 0:
                found.append((A, B, C, p))
            p += 1

print(f"searched all odd coprime pairs 1 <= A <= B <= {LIMIT}")
print(f"pairs surviving the 8 | A^3+B^3 necessary condition: {checked}")
print(f"witnesses making the Lean development inconsistent: {len(found)}")
for w in found:
    print("  *** WITNESS ***", w)
if not found:
    print("\nNo witness in this range. The axiom's hypotheses are vacuous here, so the")
    print("development is not shown inconsistent -- but note the axiom ASSERTS the very")
    print("level-lowering step whose conclusion (no such solution) is what is being proved.")
    print("It is an unverified trusted input, not a theorem, and it is doing real work.")

# Sanity: the parallel odd-C statement must NOT be vacuous, or the search is miscoded.
ex = [(A, B) for A in range(1, 60, 2) for B in range(A, 60, 2)
      if gcd(A, B) == 1 and (A ** 3 + B ** 3) % 8 == 0]
print(f"\nself-check: odd coprime pairs with 8 | A^3+B^3 below 60: {len(ex)} e.g. {ex[:5]}")
print("(non-empty, so the 8 | S filter is not silently rejecting everything)")
