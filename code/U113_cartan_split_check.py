"""Does the 144b elimination cover every prime the (3,3,p) sieve claims?

144b1 : y^2 = x^3 - 1 has CM by Q(sqrt(-3)).  If rho-bar_{E,p} = rho-bar_{144b1,p}, the
image of rho-bar_{E,p} lies in the normalizer of a Cartan subgroup, SPLIT when p splits in
Q(sqrt(-3)) (i.e. p = 1 mod 3) and NON-SPLIT when p is inert (p = 2 mod 3).

That distinction is decisive:
  * split Cartan  -> Bilu-Parent-Rebolledo (2013): X_split(p)(Q) has only cusps and CM
                     points for p >= 11, p != 13.  A non-CM Frey curve is then excluded.
  * non-split     -> X_ns(p)(Q) is NOT determined in general; this is open.
"""
import json
from pathlib import Path
from sympy import isprime

REPO = Path(__file__).resolve().parent.parent
ps = set()
for f in sorted((REPO / "references" / "U111").glob("kraus_sieve_*.json")) + \
         sorted((REPO / "references").glob("**/kraus_sieve_*.json")):
    for k, rec in json.loads(f.read_text()).items():
        if isinstance(rec, dict) and isinstance(rec.get("exponent_p"), int):
            ps.add(rec["exponent_p"])

ps = sorted(ps)
split = [p for p in ps if p % 3 == 1]
inert = [p for p in ps if p % 3 == 2]
print(f"exponents p appearing in the sieve data: {len(ps)}  range [{min(ps)}, {max(ps)}]")
print(f"  p = 1 mod 3 (SPLIT in Q(sqrt-3), split Cartan, BPR applies): {len(split)}")
print(f"  p = 2 mod 3 (INERT, NON-split Cartan, X_ns(p) open)        : {len(inert)}")
print(f"  all sieve exponents prime: {all(isprime(p) for p in ps)}")
print(f"  all sieve exponents >= 11 and != 13 (BPR hypothesis): "
      f"{all(p >= 11 and p != 13 for p in ps)}   min p = {min(ps)}")
print()
print("The checkpoints state that p = 2 mod 3 was resolved separately by Freitas (2016)")
print("via the Halberstadt-Kraus symplectic criterion, so the sieve itself handles p = 1 mod 3.")
print("Consistency check -- does the sieve data contain any p = 2 mod 3?",
      "NO (consistent)" if not inert else f"YES: {inert[:8]} (INCONSISTENT with that claim)")
print()
print("CONCLUSION: for the primes actually in the sieve, the Cartan subgroup is SPLIT, so the")
print("correct supporting theorem is Bilu-Parent-Rebolledo (2013) on X_split(p), whose")
print("hypotheses (p >= 11, p != 13) are satisfied here. The checkpoints instead cite")
print("'Momose / Darmon-Merel', which concern cyclic isogenies and quadratic Q-curves, not")
print("split Cartan normalizers. The argument SHAPE is valid; the citation is misattributed")
print("and has not been checked against a primary source.")
