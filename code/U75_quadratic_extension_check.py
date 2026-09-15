"""Direct F_(1021^2) curve count calibrating the Jacobi-sum sign.

Integer arrays only: reduction after each operation bounds all intermediate
products by 2*q^3, far below signed-int64 capacity. This is one finite check,
not a count of rational points over the number field.
"""
from __future__ import annotations
import json
import numpy as np


def main() -> None:
    q, zeta = 1021, 802
    d = (1 + zeta) % q
    nonsquare = next(a for a in range(2, q) if pow(a, (q - 1)//2, q) == q - 1)
    assert 2*q**3 < 2**63
    a, b = np.indices((q, q), dtype=np.int64)
    x, y = np.ones_like(a), np.zeros_like(a)
    base_a, base_b, exponent = a, b, 17
    while exponent:
        if exponent & 1:
            x, y = ((x*base_a + nonsquare*y*base_b) % q,
                    (x*base_b + y*base_a) % q)
        base_a, base_b = ((base_a*base_a + nonsquare*base_b*base_b) % q,
                          2*base_a*base_b % q)
        exponent //= 2
    # C_1 is birational to v^2=d^2-4*u^17. There is one point at infinity.
    fa, fb = (d*d - 4*x) % q, -4*y % q
    norm_values = (fa*fa - nonsquare*fb*fb) % q
    character = np.array([0] + [1 if pow(t, (q-1)//2, q) == 1 else -1
                                for t in range(1, q)], dtype=np.int64)
    point_count = int(q*q + 1 + np.sum(character[norm_values], dtype=np.int64))
    # Reconstruct S_1 independently from a short order-17 character table.
    generator = 10
    character_log: dict[int, int] = {}
    v = 1
    for k in range(q-1):
        character_log[v] = k % 17
        v = v*generator % q
    assert len(character_log) == q - 1
    counts = [0]*17
    for t in range(1, q):
        if t != d:
            counts[(character_log[t]+character_log[(d-t) % q]) % 17] += 1
    square = [0]*17
    for i, u in enumerate(counts):
        for j, v in enumerate(counts):
            square[(i+j) % 17] += u*v
    trace_square = 16*square[0] - sum(square[1:])
    predicted = q*q + 1 - trace_square
    assert point_count == predicted
    print(json.dumps({'checkpoint': 'U75', 'curve': 'C_1', 'q': q,
                      'extension_degree': 2, 'nonsquare': nonsquare,
                      'affine_inputs_counted': q*q, 'curve_points': point_count,
                      'jacobi_prediction': predicted, 'agreement': True,
                      'arithmetic': 'integer-only numpy arrays; int64 bound checked',
                      'full_Beal_solved': False}, indent=2))


if __name__ == '__main__':
    main()
