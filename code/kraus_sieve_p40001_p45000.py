#!/usr/bin/env python3
"""
Kraus Sieve Modular Elimination Frontier: Exponent Range p in [40001, 45000]
Signature: (3, 3, p)
Target Newforms:
  - Level 72:  72a1  (y^2 = x^3 + 6x - 7)
  - Level 144: 144a1 (y^2 = x^3 + 6x + 7, quadratic twist by -4)

High-performance launcher executing the native C/OpenMP engine code/kraus_sieve_c.
"""
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "research" / "pool" / "evidence" / "kraus_sieve_p40001_p45000.json"
BINARY = REPO_ROOT / "code" / "kraus_sieve_c"

if __name__ == "__main__":
    if not BINARY.exists():
        subprocess.run(["gcc", "-O3", "-fopenmp", str(REPO_ROOT / "code" / "kraus_sieve_c.c"), "-o", str(BINARY)], check=True)
    res = subprocess.run([str(BINARY), "40001", "45000", str(OUTPUT_FILE)])
    sys.exit(res.returncode)
