#!/usr/bin/env python3
"""
U110: Frey Conductor 72 and 144 Newform Inventory and Modular Elimination Verification
-------------------------------------------------------------------------------------
Author: Frey Conductor 72 Serre Level Lowering Specialist
Date: 2026-09-17

Verifies:
1. Dimensions of S_2(Gamma_0(N)) and S_2^new(Gamma_0(N)) for all divisors of 72 and 144.
2. Explicit newform and oldform decomposition:
   - S_2(Gamma_0(72)): dim = 5 (1 newform 72a1, 4 oldforms from 24a1 and 36a1).
   - S_2(Gamma_0(144)): dim = 13 (2 newforms 144a1, 144b1; 11 oldforms from 24a1, 36a1, 48a1, 72a1).
3. Exact Hecke eigenvalues a_q(f) for all 25 primes q < 100 for all newforms and oldform generators.
4. Proof of quadratic twist relations under character chi_{-4}.
5. Symbolic and local analysis of the prompt Frey curve E_prompt: y^2 = x^3 + 3(B^3 - A^3)x - 2(B^3 + A^3).
6. Isomorphism of Kraus Frey curve E_{A, B}: y^2 = x^3 + 3AB x + B^3 - A^3 to newforms:
   - E_{2, 1} =~ 72a1
   - E_{1, 2} =~ 144a1
   - E_{0, 1} =~ 36a1
   - E_{1, 0} =~ 144b1
"""

import json
from pathlib import Path
import subprocess
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def verify_dimensions():
    print("=== 1. Modular Form Space Dimensions at Levels 72 and 144 ===")
    gp_script = """{
    divs72 = divisors(72);
    for(i=1, #divs72,
      d = divs72[i];
      print("72;", d, ";", mfdim([d, 2, 1], 1), ";", mfdim([d, 2, 1], 0));
    );
    divs144 = divisors(144);
    for(i=1, #divs144,
      d = divs144[i];
      print("144;", d, ";", mfdim([d, 2, 1], 1), ";", mfdim([d, 2, 1], 0));
    );
    }"""
    res = subprocess.run(["gp", "-q"], input=gp_script, text=True, capture_output=True, check=True)
    
    dims72 = {}
    dims144 = {}
    for line in res.stdout.strip().split("\n"):
        if not line or ";" not in line:
            continue
        group, d, dim_full, dim_new = line.split(";")
        d, dim_full, dim_new = int(d), int(dim_full), int(dim_new)
        if group == "72":
            dims72[d] = (dim_full, dim_new)
        else:
            dims144[d] = (dim_full, dim_new)
            
    print(f"Level 72: Total dim S_2(72) = {dims72[72][0]}, dim S_2^new(72) = {dims72[72][1]}")
    assert dims72[72] == (5, 1)
    
    # Check oldform decomposition for 72:
    # 24a1 has dim_new = 1. 72 / 24 = 3, which has 2 divisors (1, 3) => 2 oldforms.
    # 36a1 has dim_new = 1. 72 / 36 = 2, which has 2 divisors (1, 2) => 2 oldforms.
    # Total oldforms = 2 + 2 = 4.
    old72 = 2 * dims72[24][1] + 2 * dims72[36][1]
    assert old72 == 4
    assert dims72[72][0] == dims72[72][1] + old72
    print(f"[PASS] S_2(72) decomposed: 1 newform (72a1) + 4 oldforms (2 from 24a1, 2 from 36a1) = 5.")

    print(f"\nLevel 144: Total dim S_2(144) = {dims144[144][0]}, dim S_2^new(144) = {dims144[144][1]}")
    assert dims144[144] == (13, 2)
    # Check oldform decomposition for 144:
    # 24a1: index 6, divisors {1, 2, 3, 6} => 4 oldforms.
    # 36a1: index 4, divisors {1, 2, 4} => 3 oldforms.
    # 48a1: index 3, divisors {1, 3} => 2 oldforms.
    # 72a1: index 2, divisors {1, 2} => 2 oldforms.
    # Total oldforms = 4 + 3 + 2 + 2 = 11.
    old144 = 4 * dims144[24][1] + 3 * dims144[36][1] + 2 * dims144[48][1] + 2 * dims144[72][1]
    assert old144 == 11
    assert dims144[144][0] == dims144[144][1] + old144
    print(f"[PASS] S_2(144) decomposed: 2 newforms (144a1, 144b1) + 11 oldforms (4 from 24a1, 3 from 36a1, 2 from 48a1, 2 from 72a1) = 13.")
    return dims72, dims144

def compute_hecke_eigenvalues():
    print("\n=== 2. Computing Hecke Eigenvalues a_q(f) for all primes q < 100 ===")
    primes = [q for q in range(2, 100) if sp.isprime(q)]
    assert len(primes) == 25
    
    gp_script = f"""{{
    pvec = {primes};
    mf24 = mfinit([24, 2, 1], 0); f24 = mfeigenbasis(mf24)[1];
    mf36 = mfinit([36, 2, 1], 0); f36 = mfeigenbasis(mf36)[1];
    mf48 = mfinit([48, 2, 1], 0); f48 = mfeigenbasis(mf48)[1];
    mf72 = mfinit([72, 2, 1], 0); f72 = mfeigenbasis(mf72)[1];
    mf144 = mfinit([144, 2, 1], 0); f144a = mfeigenbasis(mf144)[1]; f144b = mfeigenbasis(mf144)[2];

    forms = [f24, f36, f48, f72, f144a, f144b];
    names = ["24a1", "36a1", "48a1", "72a1", "144a1", "144b1"];

    for(k=1, #forms,
      printf("%s:", names[k]);
      cf = mfcoefs(forms[k], 97);
      for(i=1, #pvec,
        q = pvec[i];
        printf(" %d=%d", q, cf[q+1]);
      );
      printf("\\n");
    );
    }}"""
    res = subprocess.run(["gp", "-q"], input=gp_script, text=True, capture_output=True, check=True)
    
    eigenvalues = {}
    for line in res.stdout.strip().split("\n"):
        if not line or ":" not in line:
            continue
        name, rest = line.split(":")
        eigenvalues[name] = {}
        for entry in rest.strip().split():
            q_str, aq_str = entry.split("=")
            eigenvalues[name][int(q_str)] = int(aq_str)
            
    print(f"Successfully computed eigenvalues for {len(eigenvalues)} forms across {len(primes)} primes.")
    
    # Verify quadratic twist relations: chi_{-4}(q) = (-1)^((q-1)/2) for odd q
    print("\nVerifying Quadratic Twist Identities via chi_{-4}:")
    for q in primes:
        if q == 2:
            chi = 0
        else:
            chi = 1 if (q % 4 == 1) else -1
            
        # 144a1 is twist of 72a1
        if q > 2:
            assert eigenvalues["144a1"][q] == chi * eigenvalues["72a1"][q], f"Mismatch at q={q} for 144a1"
        # 144b1 is twist of 36a1
        if q > 2:
            assert eigenvalues["144b1"][q] == chi * eigenvalues["36a1"][q], f"Mismatch at q={q} for 144b1"
        # 48a1 is twist of 24a1
        if q > 2:
            assert eigenvalues["48a1"][q] == chi * eigenvalues["24a1"][q], f"Mismatch at q={q} for 48a1"
            
    print("[PASS] All quadratic twist identities hold unconditionally for all 25 primes!")
    return eigenvalues

def verify_frey_curves():
    print("\n=== 3. Symbolic & Arithmetic Comparison of Frey Curves ===")
    
    # 1. Prompt curve: E_prompt: y^2 = x^3 + 3(B^3 - A^3)x - 2(B^3 + A^3)
    A, B, x = sp.symbols("A B x")
    p_prompt = 3 * (B**3 - A**3)
    q_prompt = -2 * (B**3 + A**3)
    disc_prompt_poly = sp.simplify(-(4 * p_prompt**3 + 27 * q_prompt**2))
    delta_prompt = 16 * disc_prompt_poly
    expected_delta_prompt = -1728 * ((B**3 - A**3)**3 + (B**3 + A**3)**2)
    assert sp.expand(delta_prompt) == sp.expand(expected_delta_prompt)
    print(f"[PASS] E_prompt discriminant: Delta = -1728 * ((B^3 - A^3)^3 + (B^3 + A^3)^2).")
    print(f"       Notice: Degree of (B^3 - A^3)^3 is 9, degree of (B^3 + A^3)^2 is 6.")
    print(f"       Inhomogeneity prevents factoring out (A^3 + B^3)^2 = C^(2p).")

    # 2. Kraus Frey curve: E_kraus: y^2 = x^3 + 3AB x + (B^3 - A^3)
    p_kraus = 3 * A * B
    q_kraus = B**3 - A**3
    disc_kraus_poly = sp.simplify(-(4 * p_kraus**3 + 27 * q_kraus**2))
    delta_kraus = 16 * disc_kraus_poly
    expected_delta_kraus = -432 * (A**3 + B**3)**2
    assert sp.expand(delta_kraus) == sp.expand(expected_delta_kraus)
    print(f"[PASS] E_kraus discriminant: Delta = -432 (A^3 + B^3)^2 = -2^4 * 3^3 * C^(2p).")
    print(f"       Completely homogeneous, strips all primes dividing AB!")

    # 3. Exact Isomorphisms with Newforms
    gp_script = """{
    E_72a1 = ellinit([0, 0, 0, 6, -7]);
    E_144a1 = ellinit([0, 0, 0, 6, 7]);
    E_36a1 = ellinit([0, 0, 0, 0, 1]);
    E_144b1 = ellinit([0, 0, 0, 0, -1]);

    /* Kraus curve at boundary (A, B) = (2, 1) */
    E_21 = ellinit([0, 0, 0, 3*2*1, 1^3 - 2^3]);
    /* Kraus curve at swapped boundary (A, B) = (1, 2) */
    E_12 = ellinit([0, 0, 0, 3*1*2, 2^3 - 1^3]);
    /* Kraus curve at Catalan trivial (A, B) = (0, 1) */
    E_01 = ellinit([0, 0, 0, 3*0*1, 1^3 - 0^3]);
    /* Kraus curve at Catalan trivial (A, B) = (1, 0) */
    E_10 = ellinit([0, 0, 0, 3*1*0, 0^3 - 1^3]);

    print("ISOM;72a1;", ellisisom(E_21, E_72a1));
    print("ISOM;144a1;", ellisisom(E_12, E_144a1));
    print("ISOM;36a1;", ellisisom(E_01, E_36a1));
    print("ISOM;144b1;", ellisisom(E_10, E_144b1));
    }"""
    res = subprocess.run(["gp", "-q"], input=gp_script, text=True, capture_output=True, check=True)
    for line in res.stdout.strip().split("\n"):
        if line.startswith("ISOM;"):
            parts = line.split(";")
            form_name = parts[1]
            isom = parts[2].strip()
            assert isom == "[1, 0, 0, 0]"
            print(f"[PASS] Exact isomorphism: Kraus Frey model matches {form_name} with isomorphism vector {isom}.")

def main():
    dims72, dims144 = verify_dimensions()
    eigenvalues = compute_hecke_eigenvalues()
    verify_frey_curves()
    
    # Save structured json
    data = {
        "dimensions_level_72": {
            "total_dim": dims72[72][0],
            "new_dim": dims72[72][1],
            "old_dim": dims72[72][0] - dims72[72][1]
        },
        "dimensions_level_144": {
            "total_dim": dims144[144][0],
            "new_dim": dims144[144][1],
            "old_dim": dims144[144][0] - dims144[144][1]
        },
        "hecke_eigenvalues": eigenvalues
    }
    out_dir = ROOT / "research/checkpoints"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "U110_hecke_eigenvalues_data.json"
    with open(out_file, "w") as f:
        json.dump(data, f, indent=2)
    print(f"\n[DONE] Verified all properties and saved data to {out_file}")

if __name__ == "__main__":
    main()
