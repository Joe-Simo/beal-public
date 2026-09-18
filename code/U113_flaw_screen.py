"""Jev screen: which checkpoints likely carry the two failure modes found in U113?

FM1 (residual/isogeny conflation): refuting isogeny, Faltings Hom=0, End^0 dimension
    clash, or l-adic non-isomorphism, and concluding a RESIDUAL mod-p congruence is
    impossible. Strictly weaker statement refuted than the one claimed.
FM2 (Chabauty over the wrong field): a rank < genus bound over a base field used to
    conclude something about solutions whose coordinates have higher degree.

One request per checkpoint, same questions, concurrency 12. Routing signal only:
a high score here does NOT mean the checkpoint is wrong, it means audit it next.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

REPO = Path(__file__).resolve().parent.parent
CKPT = REPO / "research" / "checkpoints"

QUESTIONS = {
    "fm1_residual_isogeny": jev.score(
        "Does this checkpoint argue that two objects are NOT isogenous, or that their l-adic "
        "Tate modules or endomorphism algebras differ, and then conclude from that alone that a "
        "RESIDUAL mod-p Galois representation congruence is impossible? Refuting isogeny or an "
        "l-adic isomorphism is strictly stronger than refuting a mod-p congruence, so that "
        "inference is invalid. Judge only whether this pattern is present.",
        [
            "level 0: the checkpoint makes no claim about isogenies, endomorphism algebras or Galois representation congruences at all",
            "level 1: it discusses Galois representations but keeps residual mod-p statements and l-adic or isogeny statements clearly separate",
            "level 2: it mentions both an isogeny or endomorphism argument and a residual congruence, and the relationship between them is not made explicit",
            "level 3: it explicitly refutes an isogeny, an l-adic isomorphism, or matching endomorphism algebras, and concludes from that a residual mod-p congruence cannot hold",
        ],
    ),
    "fm2_chabauty_wrong_field": jev.score(
        "Does this checkpoint apply Chabauty-Coleman, a Mordell-Weil rank bound, or a Selmer rank "
        "bound over one field, and then draw a conclusion about Diophantine solutions whose "
        "coordinates actually generate a strictly larger field? A bound on the rational points over "
        "a base field says nothing about points of higher degree. Judge only whether this pattern is present.",
        [
            "level 0: the checkpoint uses no rank bound, Chabauty, Coleman integration or Selmer computation",
            "level 1: it uses a rank or Chabauty bound and the solutions it concludes about are rational over the same field the bound was proved over",
            "level 2: it uses a rank or Chabauty bound and the field of definition of the relevant points is not clearly identified",
            "level 3: it uses a rank or Chabauty bound over one field while the solutions demonstrably generate a larger field, and concludes about the solutions anyway",
        ],
    ),
    "overclaimed_language": jev.noul(
        "Does this checkpoint describe a result as unconditional, definitive, 100% closed, or "
        "completely resolved, while the argument supporting it depends on a step whose hypotheses "
        "are not verified within the checkpoint itself?",
        true="it uses words such as unconditional, definitive, 100% closed, or complete resolution for a result that leans on an external theorem, another checkpoint, or a step whose hypotheses are not checked there",
        false="its claims are stated with their actual dependencies and conditions, or it makes no strong closure claim",
    ),
    "audit_priority": jev.choice(
        "Given the two known failure modes described in the other material, what should be done "
        "with this checkpoint next?",
        {
            "audit_now": "it very likely contains one of the two failure modes and a load-bearing claim depends on it",
            "audit_later": "it may contain a failure mode but nothing currently load-bearing depends on it",
            "verify_computation": "its main risk is an unchecked numerical or finite computation rather than a logical failure mode",
            "verify_literature": "its main risk is an external citation used outside its actual hypotheses",
            "no_action": "it is a search log, a ledger, or otherwise carries no argument that could exhibit these failure modes",
        },
    ),
}

CONTEXT = {
    "conjecture": "Beal: A^x + B^y = C^z with x,y,z >= 3 and gcd(A,B,C)=1 has no solutions.",
    "failure_mode_1": "U113 found that U97 and U102 both refute isogeny / l-adic isomorphism / "
                      "endomorphism-algebra equality and conclude a residual mod-17 congruence is "
                      "impossible. That inference is invalid: non-isogenous abelian varieties routinely "
                      "share a residual mod-p representation (verified exactly with curves having "
                      "rational 5-torsion, a_p = p+1 mod 5 while a_p differ over Z).",
    "failure_mode_2": "U113 found that U105 uses rank_Z J^-(k) <= 2 < g = 8 over k = Q(sqrt5) to bound "
                      "C^-(k), while solutions give points of degree 10 over k (minimal polynomial "
                      "x^10 + 256). The bound is silent about those points.",
}


def summarize(path: Path, limit: int = 5000) -> dict:
    text = path.read_text(errors="replace")
    head = text[:limit]
    return {"filename": path.name, "excerpt": head,
            "length_chars": len(text)}


def main() -> int:
    paths = sorted(CKPT.glob("*.md"))
    if len(sys.argv) > 1:
        paths = [p for p in paths if any(a in p.name for a in sys.argv[1:])]
    states = [{**CONTEXT, "checkpoint": summarize(p)} for p in paths]
    print(f"screening {len(paths)} checkpoints via Jev ...", file=sys.stderr)
    responses = jev.ask_many(states, QUESTIONS)
    rows = []
    for p, st, resp in zip(paths, states, responses):
        if "error" in resp:
            print(f"  ! {p.name}: {resp['error']}", file=sys.stderr)
            continue
        jev.persist(f"screen_{p.stem}", st, QUESTIONS, resp)
        a = resp["answers"]
        rows.append({
            "file": p.name,
            "fm1": round(a["fm1_residual_isogeny"]["score"], 2),
            "fm2": round(a["fm2_chabauty_wrong_field"]["score"], 2),
            "overclaim": round(a["overclaimed_language"]["noul"], 2),
            "action": a["audit_priority"]["choice"],
            "conf": round(a["audit_priority"]["confidence"], 2),
        })
    rows.sort(key=lambda r: -(max(r["fm1"], r["fm2"]) + r["overclaim"]))
    print(json.dumps({"state": "HYPOTHESIS_ONLY", "screen": rows}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
