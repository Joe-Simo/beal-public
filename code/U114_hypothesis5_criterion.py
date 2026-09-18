"""A criterion for Azon's Hypothesis 5 in terms of the COEFFICIENTS alone.

From U114 Part VI, for signature (r,r,p) and odd q:
    nu_q = 2p v_q(c) + 2 v_q(C) - v_q(AB) - r v_q(ab).

Azon Definition 3.11: A,B,C pairwise coprime and FREE OF r-TH POWERS.
Azon Lemma 3.12: A a^r, B b^r, C c^p are pairwise coprime.

CASE ANALYSIS over primes q not dividing 2r.
  q | AB:  say q | A. By Lemma 3.12, q divides neither B b^r nor C c^p, so v_q(b)=v_q(C)=v_q(c)=0.
           nu_q = -v_q(AB) - r v_q(a) < 0                                    -> (i) holds
           nu_q = -v_q(AB) mod r, and 1 <= v_q(AB) <= r-1 by r-th-power-freeness
                                                                             -> (ii) holds
  q | ab, q not | AB:  nu_q = -r v_q(ab) = 0 mod r                           -> (ii) FAILS
  q | c or q | C:      nu_q = 2p v_q(c) + 2 v_q(C) > 0                       -> (i) FAILS
  otherwise:           nu_q = 0                                              -> (i) FAILS

Therefore:
    HYPOTHESIS 5 HOLDS  <=>  AB has a prime factor q with q not dividing 2r
                             and ord*(q mod r) even.
This depends ONLY on the coefficients A, B and the exponent r -- not on the putative solution.
"""
from sympy import factorint, n_order, isprime


def hypothesis5_holds(A: int, B: int, r: int):
    """Returns (bool, witnesses, reason). Criterion derived above."""
    AB = abs(A * B)
    if AB in (0, 1):
        return False, [], f"AB = {AB} has no prime factors"
    witnesses = []
    for q, e in factorint(AB).items():
        if (2 * r) % q == 0:
            continue                      # q | 2r is excluded by Hypothesis 5
        if e % r == 0:
            continue                      # cannot happen if AB is r-th-power-free, but check
        if n_order(q, r) % 2 == 0:        # ord*(q mod r) even
            witnesses.append((q, e, n_order(q, r)))
    if witnesses:
        return True, witnesses, "witness prime(s) found in AB"
    return False, [], f"no prime factor of AB={AB} is coprime to 2r={2*r} with even order mod {r}"


CASES = [
    ("Orientation B (the project's main object): U^5 + 8V^5 = Z^17", 1, 8, 1, 5, 17),
    ("Orientation A: X^10 + Y^10 = 2Z^17  ->  (X^2)^5 + (Y^2)^5 = 2Z^17", 1, 1, 2, 5, 17),
]
print("=== The two orientations this project reduced the all-even case to ===\n")
for label, A, B, C, r, p in CASES:
    ok, w, why = hypothesis5_holds(A, B, r)
    print(f"{label}\n  A={A} B={B} C={C} r={r} p={p}  AB={A*B}")
    print(f"  Hypothesis 5: {'HOLDS' if ok else 'FAILS'}  --  {why}\n")

print("=== Which coefficient pairs WOULD satisfy it, for r = 5? ===")
print("(need a prime q | AB with q not in {2,5} and ord*(q mod 5) even, i.e. q != 1 mod 5)\n")
good, bad = [], []
for B in range(2, 40):
    ok, w, _ = hypothesis5_holds(1, B, 5)
    (good if ok else bad).append(B)
print("  B values (with A=1) that SATISFY Hypothesis 5:", good[:18])
print("  B values that FAIL:                          ", bad)
print()
print("  note: B = 8, 16, 32 fail because they are powers of 2, and 2 | 2r = 10.")
print("        B = 11, 31 fail because 11 = 31 = 1 mod 5, so ord*(q mod 5) = 1, odd.")
for B in [3, 7, 8, 11, 16]:
    ok, w, why = hypothesis5_holds(1, B, 5)
    print(f"    B={B:<3} {'HOLDS' if ok else 'FAILS':<6} {w if w else why}")
