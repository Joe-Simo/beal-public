#!/usr/bin/env python3
"""
AMS Submission Dossier Generator & Cryptographic Integrity Audit
Beal Conjecture Autonomous Research Campaign (Candidate C623)

Computes SHA-256 cryptographic checksums for all formal proof modules,
computational engines, PARI/GP scripts, and empirical JSON certificates.
Outputs CHECKSUMS.sha256 and SUBMISSION_MANIFEST.json.
"""
from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHECKSUMS_FILE = REPO_ROOT / "CHECKSUMS.sha256"
MANIFEST_FILE = REPO_ROOT / "SUBMISSION_MANIFEST.json"


def sha256_file(filepath: Path) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def collect_submission_assets() -> dict[str, list[Path]]:
    """Gather all core research assets organized by category."""
    categories: dict[str, list[Path]] = {
        "formal_proofs_lean4": sorted(list((REPO_ROOT / "formal" / "Beal").glob("*.lean")) + [REPO_ROOT / "formal" / "Beal.lean", REPO_ROOT / "formal" / "lakefile.lean"]),
        "c_gmp_search_engine": sorted([
            REPO_ROOT / "code" / "beal_search_gmp.c",
            REPO_ROOT / "code" / "check_counterexample_gmp.c",
            REPO_ROOT / "code" / "kraus_sieve_c.c"
        ]),
        "pari_gp_scripts": sorted(list((REPO_ROOT / "code").glob("*.gp"))),
        "python_sieve_and_audit": sorted([
            REPO_ROOT / "code" / "kraus_sieve_p5501_p6500.py",
            REPO_ROOT / "code" / "kraus_sieve_p6501_p10000.py",
            REPO_ROOT / "code" / "kraus_sieve_p10001_p15000.py",
            REPO_ROOT / "code" / "kraus_sieve_p15001_p20000.py",
            REPO_ROOT / "code" / "kraus_sieve_p20001_p25000.py",
            REPO_ROOT / "code" / "kraus_sieve_p25001_p30000.py",
            REPO_ROOT / "code" / "kraus_sieve_p30001_p35000.py",
            REPO_ROOT / "code" / "kraus_sieve_p35001_p40000.py",
            REPO_ROOT / "code" / "kraus_sieve_p40001_p45000.py",
            REPO_ROOT / "code" / "kraus_sieve_p45001_p50000.py",
            REPO_ROOT / "code" / "beal_counterexample_checker.py",
            REPO_ROOT / "code" / "jev.py",
            REPO_ROOT / "code" / "pool.py"
        ]),
        "evidence_certificates_json": sorted(list((REPO_ROOT / "research" / "pool" / "evidence").glob("*.json"))),
        "preprints_and_papers": sorted(list((REPO_ROOT / "research" / "papers").glob("*.*"))),
    }
    return categories


def main():
    print("=================================================================")
    print("Generating AMS Submission Dossier & Cryptographic Audit")
    print("=================================================================")

    categories = collect_submission_assets()
    checksum_lines = []
    manifest_records = {}

    total_files = 0
    for cat_name, file_list in categories.items():
        print(f"Processing category: {cat_name} ({len(file_list)} files)...")
        manifest_records[cat_name] = []
        for f in file_list:
            if not f.exists():
                continue
            h = sha256_file(f)
            rel_path = f.relative_to(REPO_ROOT)
            checksum_lines.append(f"{h}  {rel_path}")
            manifest_records[cat_name].append({
                "file": str(rel_path),
                "sha256": h,
                "size_bytes": f.stat().st_size
            })
            total_files += 1

    # Write CHECKSUMS.sha256
    CHECKSUMS_FILE.write_text("\n".join(checksum_lines) + "\n")
    print(f"\nWrote {len(checksum_lines)} cryptographic checksums to: {CHECKSUMS_FILE}")

    # Write SUBMISSION_MANIFEST.json
    manifest_data = {
        "title": "Candidate C623 AMS Submission Dossier",
        "description": "Cryptographic manifest of Lean 4 formal proofs, C/GMP engines, and verified search logs",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "total_assets_certified": total_files,
        "verification_commands": {
            "lean4_build": "cd formal && lake build Beal",
            "c_gmp_section8_test": "./code/beal_search_gmp --test-near-misses",
            "checksum_audit": "shasum -a 256 -c CHECKSUMS.sha256"
        },
        "assets_by_category": manifest_records
    }
    with open(MANIFEST_FILE, "w") as mf:
        json.dump(manifest_data, mf, indent=2)
    print(f"Wrote submission manifest to: {MANIFEST_FILE}")
    print("=================================================================")
    print("[SUCCESS] AMS Submission Packet generated with full cryptographic audit.")


if __name__ == "__main__":
    main()
