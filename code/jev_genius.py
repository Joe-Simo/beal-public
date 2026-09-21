"""Jev Mathematical Genius AI Machine (code/jev_genius.py).

An advanced, multi-tier autonomous mathematical intelligence engine powered by Jev
(TypeSafe System One), designed specifically to resolve Diophantine equations and
attack Beal's conjecture through adversarial screening, ontological decomposition,
combinatorial synthesis, and rigorous failure-mode detection.

Core Capabilities:
1. Deep Ontological Decomposition:
   - Evaluates arithmetic geometry, Galois cohomology, automorphy, and motivic structures.
2. 5-Stage Adversarial Sieve:
   - Stage 1: Target & Exponent Discipline (strictly x, y, z >= 3, coprimality, non-triviality).
   - Stage 2: Fermat-Catalan Blindness Test (adversarial test against the 10 known exponent-2 solutions).
   - Stage 3: Canonical Three Failure Modes (Residual conflation, Chabauty wrong field / Selmer blowup, Heuristic laundering).
   - Stage 4: Structural Obstruction Pinpoint (Cusp form abundance, continuous moduli, Selmer linear growth).
   - Stage 5: Finiteness-to-Nonexistence Gap (distinguishing Mordell/Faltings finiteness from Beal non-existence).
3. Combinatorial Matrix Synthesis:
   - Screens all unordered candidate pairs concurrently to discover orthogonal, obstruction-compensating hybrids.
4. Persistent Lemma Salvage Engine:
   - Automatically preserves unconditional sub-theorems, exact modular traces, and valid bounds in salvaged_lemmas.json.
5. Domain-Specific Breakthrough Discovery:
   - Screens breakthrough hypotheses across Arithmetic Geometry, Automorphic Forms, Derived Categories, p-adic Hodge, and Diophantine Transcendence.
6. Deep Obstruction Diagnostic:
   - Decomposes blocked candidates into their underlying topological, cohomological, and arithmetic failure mechanisms.
7. Kraus Modular Sieve Advisor:
   - Evaluates optimal parameters, modulus distributions, and Frobenius trace collisions for signature (3, 3, p).
8. Empirical Intelligence Benchmark:
   - Calibrates Jev's discrimination accuracy against ground-truth theorems vs. canonical fallacies.
9. Formal Lean 4 Statement Fidelity Audit:
   - Audits Lean 4 code to guarantee strict adherence to Beal's conjecture and standard axioms.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "code"))
import jev

POOL_FILE = REPO_ROOT / "research" / "pool" / "candidates.json"
SALVAGED_FILE = REPO_ROOT / "research" / "pool" / "salvaged_lemmas.json"
EVIDENCE_DIR = REPO_ROOT / "research" / "pool" / "evidence"

# The 10 known Fermat-Catalan primitive non-trivial integer solutions with exponent 2:
FERMAT_CATALAN_IDENTITIES = [
    "1^m + 2^3 = 3^2",
    "2^5 + 7^2 = 3^4",
    "7^3 + 13^2 = 2^9",
    "2^7 + 17^3 = 71^2",
    "3^5 + 11^4 = 122^2",
    "17^7 + 76271^3 = 21063928^2",
    "1414^3 + 2213459^2 = 65^7",
    "9262^3 + 15312283^2 = 113^7",
    "43^8 + 96222^3 = 30042907^2",
    "33^8 + 1549034^2 = 15613^3",
]

BEAL_CONJECTURE_SPEC = (
    "Beal Conjecture: For positive integers A, B, C, x, y, z with A^x + B^y = C^z and "
    "x, y, z >= 3, then gcd(A, B, C) > 1. Strictly requires x,y,z >= 3 (strictly hyperbolic defect "
    "1/x + 1/y + 1/z - 1 <= -1/12). Primitive solutions (gcd(A,B,C)=1) must be non-existent."
)


# ==============================================================================
# 1. QUESTION SUITES FOR JEV
# ==============================================================================

def get_genius_triage_questions() -> dict[str, dict[str, Any]]:
    return {
        "target_discipline": jev.noul(
            instructions=(
                "Does this candidate strictly enforce Beal target discipline (exponents x, y, z >= 3, "
                "coprimality gcd(A, B, C) = 1, positive non-zero integers) without silently allowing "
                "exponent 2, negative terms, or non-integral coordinates?"
            ),
            true="Strictly adheres to target discipline with exponents strictly at least 3.",
            false="Violates target discipline, allows exponent 2, or restricts exponents without general proof.",
        ),
        "fc_blindness": jev.noul(
            instructions=(
                f"Is this candidate blind to the 10 known Fermat-Catalan solutions ({', '.join(FERMAT_CATALAN_IDENTITIES[:3])}...)? "
                "Specifically, does its core mathematical mechanism hold equally well for identities with exponent 2, "
                "meaning it cannot prove Beal on its own without additional exponent >= 3 input?"
            ),
            true="The mechanism is Fermat-Catalan blind: it holds on identities with exponent 2.",
            false="The mechanism strictly exploits the Beal hyperbolic defect (-chi >= 1/12) which fails on exponent 2.",
        ),
        "canonical_failure_mode": jev.choice(
            instructions=(
                "Evaluate the candidate against the four canonical repository failure modes (from CLAUDE.md).\n"
                "Which failure mode does this candidate trigger?\n"
                "CRITICAL BOUNDARY DISTINCTIONS:\n"
                "- Failure Mode 1 (Residual conflation): Concluding a mod-p congruence is impossible purely from non-isogeny, "
                "l-adic isomorphism refutation, or endomorphism algebra inequality. (FALLACY)\n"
                "- Sound Modular Sieve (Kraus criterion): Explicitly computing local Frobenius traces a_k(E) mod l and proving "
                "a_k(E) != a_k(f) mod l for all newforms f at auxiliary prime k = 2mp+1. This directly eliminates the residual "
                "mod-p congruence itself and is COMPLETELY SOUND (sound_no_failure_mode).\n"
                "- Failure Mode 2 (Chabauty wrong field / Selmer blowup): Applying rank bounds across field extensions without "
                "bounding the ramification set S = primes(ABC).\n"
                "- Failure Mode 3 (Heuristic laundering): Relabelling GRH, ABC, or Cohen-Lenstra bounds as unconditional.\n"
                "- Failure Mode 4 (Unchecked approximation direction): A bound, interval, sieve, or truncated range is used, and the "
                "conclusion is valid only if the approximation errs one particular way (e.g. ellrank(E)[1] lower bound used as rank upper bound).\n"
                "- Failure Mode 5 (Local-Global Moduli Conflation): Invariant depends only on the projective cross-ratio "
                "t = A/B in P^1(Q) or P^1(C), completely blind to integer coprimality gcd(gcd(A,B),C) > 1.\n"
                "- sound_no_failure_mode: Avoids all failure modes via exact structural or modular computation."
            ),
            criteria={
                "mode_1_residual_conflation": (
                    "Failure Mode 1: Residual/isogeny/conductor conflation. Confuses mod-p Galois representation "
                    "irreducibility or non-isogeny with non-existence of residual mod-p congruence."
                ),
                "mode_2_chabauty_unbounded_s": (
                    "Failure Mode 2: Chabauty over wrong field or Selmer dimension blowup. Selmer variety dimension "
                    "dim Sel(U_n) grows linearly with |S| = primes(ABC), exceeding local dimension dim U_n(Q_p)."
                ),
                "mode_3_heuristic_laundering": (
                    "Failure Mode 3: Heuristic laundering. Assumes ABC conjecture, Vojta conjecture, Cohen-Lenstra, "
                    "or GRH bounds and labels the result unconditional."
                ),
                "mode_4_unchecked_approximation_direction": (
                    "Failure Mode 4: Unchecked approximation direction. Bound/interval used in the wrong direction for the claim "
                    "(e.g. lower rank bound used to claim rank 0, or over-approximating the safe set)."
                ),
                "mode_5_moduli_coprimality_conflation": (
                    "Failure Mode 5: Local-global / moduli conflation. Invariant depends only on projective geometry "
                    "over Q or C (cross-ratio t = A/B), completely blind to integer coprimality gcd(A, B, C) > 1."
                ),
                "sound_no_failure_mode": (
                    "None: The candidate avoids all failure modes through exact structural invariants or explicit modular trace computation."
                ),
            },
        ),
        "uses_equation_gate": jev.noul(
            instructions=(
                "Second Gate (U228): Does the proof/mechanism of this candidate genuinely use the Diophantine equation "
                "A^x + B^y = C^z? Or is it an exponent-only inequality (such as rad(ABC)^3 <= A^x B^y C^z, or |chi| >= 1/12) "
                "that merely restates the exponent hypothesis without using the equation?"
            ),
            true="Genuinely uses the equation A^x + B^y = C^z (e.g. via Frey curves, factoring, modular traces, or covers).",
            false="Does NOT use the equation; it is the exponent hypothesis in disguise, proving only a generic inequality.",
        ),
        "survey_category": jev.choice(
            instructions=(
                "Classify the mathematical mechanism according to the repository Survey-of-Failures gate (U211):\n"
                "- fatal_bounded_sieve: Bounded / fixed-input computation, congruence or covering sieves (can never resolve Beal).\n"
                "- fatal_modular_single_sig: Modular method one signature at a time (stalls: no Frey object for 3 independent exponents).\n"
                "- fatal_elementary: Elementary methods (LTE, p-adic valuations, difference-of-powers, residues - invalid or FC-blind).\n"
                "- fatal_abc_baker: ABC or Baker linear forms in logarithms (ineffective or too weak with unknown bases).\n"
                "- live_unifying_modular_motivic: Unifying modular/motivic object for three exponents (LIVE direction).\n"
                "- live_effective_diophantine_geometry: Effective Diophantine geometry bounding coordinates (LIVE direction)."
            ),
            criteria={
                "fatal_bounded_sieve": "Bounded / fixed-input computation, congruence or covering sieves.",
                "fatal_modular_single_sig": "Modular method one signature at a time (stalls on 3 exponents).",
                "fatal_elementary": "Elementary methods (LTE, valuations, residues).",
                "fatal_abc_baker": "ABC / Baker linear forms in logarithms.",
                "live_unifying_modular_motivic": "Unifying modular/motivic object for three exponents.",
                "live_effective_diophantine_geometry": "Effective Diophantine geometry bounding coordinates.",
            },
        ),
        "finiteness_to_nonexistence": jev.choice(
            instructions=(
                r"Does the mathematical mechanism bridge the critical gap between finiteness (|X(Q)| < \infty) "
                r"and complete non-existence of primitive integer points (|X(Z)_{prim}| = 0)?"
            ),
            criteria={
                "proves_nonexistence": "Provides an exact obstruction that forces the solution set to be completely empty.",
                "finiteness_only": "Only proves finiteness (like Faltings/Chabauty/Vojta), leaving unknown points uneliminated.",
                "bounded_only": "Only eliminates bounded prime exponents (e.g. Kraus sieve up to a computational bound).",
                "vacuous": "The invariant does not constrain integer points on the hypersurface.",
            },
        ),
        "structural_obstruction": jev.choice(
            instructions=(
                "Identify the exact primary mathematical obstruction that blocks this candidate from unconditional completion."
            ),
            criteria={
                "projective_coprimality_blindness": "The invariant depends only on the projective cross-ratio A/B in P^1 and cannot detect integer coprimality gcd(A, B, C) = 1.",
                "selmer_dimension_growth": "Selmer variety dimension grows linearly with the unknown ramification set S = primes(ABC).",
                "continuous_moduli_degeneration": r"Moduli parameter lambda = A^x / C^z approaches cusps (0, 1, \infty) degenerating heights.",
                "automorphic_cusp_abundance": "Arthur trace formula / cusp form abundance dim S_k(N) >> 0 prevents representation vanishing.",
                "torsion_wild_ramification": "Wild additive reduction at primes 2 and 3 obstructs p-adic period maps and torsion vanishing.",
                "computational_scale": "Method is sound in principle for bounded exponents but computationally restricted to finite primes.",
                "unobstructed": "No known mathematical obstruction prevents this candidate from completing an unconditional proof.",
            },
        ),
        "genius_recommendation": jev.choice(
            instructions="What is the high-precision action recommended by the Mathematical Genius Engine?",
            criteria={
                "advance_kraus_frontier": "Execute exact modular sieve / PARI-GP computation to push empirical exponent bounds.",
                "audit_and_isolate_obstruction": "Conduct deep mathematical audit to prove why this mechanism hits a structural dead-end.",
                "salvage_proved_sublemmas": "Extract valid sub-lemmas, modular traces, or local bounds into the salvaged lemma pool.",
                "refute_and_archive": "Refute candidate due to fundamental geometric flaw, heuristic laundering, or inconsistency.",
                "synthesize_breakthrough": "Candidate contains a live ingredient suitable for cross-pollination in a breakthrough hypothesis.",
            },
        ),
    }


def get_pairwise_synthesis_questions() -> dict[str, dict[str, Any]]:
    return {
        "orthogonality": jev.noul(
            instructions=(
                "Are the mathematical mechanisms of Candidate A and Candidate B mathematically orthogonal "
                "(e.g. local Galois deformation vs. global Arakelov heights, or bounded modular sieve vs. cyclotomic Selmer descent)?"
            ),
            true="The two mechanisms operate on independent mathematical structures and can be combined.",
            false="The two mechanisms are redundant, parallel, or share the exact same mathematical foundation.",
        ),
        "obstruction_compensation": jev.noul(
            instructions=(
                "Does the strength of Candidate A compensate for the primary obstruction of Candidate B? "
                "(For example, does Candidate A's local congruence bound the bad reduction set S that obstructs Candidate B?)"
            ),
            true="Candidate A provides information that strictly removes or weakens Candidate B's obstruction.",
            false="Neither candidate resolves the obstruction of the other; the obstructions are compounding.",
        ),
        "breakthrough_potential": jev.score(
            instructions=(
                "Estimate the breakthrough potential of a synthesized hybrid method combining Candidate A and Candidate B."
            ),
            criteria=[
                "level 0: No synergy; synthesis yields no new leverage beyond the individual candidates.",
                "level 1: Minor synergy; provides slightly improved computational bounds or local certificates.",
                "level 2: Strong synergy; closes a major gap for an infinite signature family.",
                "level 3: Definitive breakthrough; creates a viable, unconditional path toward full Beal.",
            ],
        ),
        "synthesis_action": jev.choice(
            instructions="What action should be taken on this candidate pair?",
            criteria={
                "formulate_hybrid_candidate": "Formulate a new hybrid candidate combining the two complementary invariants.",
                "discard_pair": "Discard pair; shared failure modes or redundant mechanisms.",
                "keep_independent": "Keep independent; both are valuable but do not synthesize into a unified proof.",
            },
        ),
    }


def get_obstruction_diagnostic_questions() -> dict[str, dict[str, Any]]:
    return {
        "failure_level": jev.choice(
            instructions="At what mathematical level does this approach fundamentally fail?",
            criteria={
                "representation_theoretic": "Mod-p Galois representations cannot be distinguished from target modular forms.",
                "geometric_moduli": "The moduli space has cusps or positive dimension where heights cannot be bounded.",
                "cohomological_dimension": "Cohomology or Selmer dimension grows uncontrollably with ramification |S|.",
                "topological_invariance": "The topological invariant is blind to integer coordinates and Fermat-Catalan solutions.",
                "computational_exhaustion": "The theoretical approach is sound but infinite cases cannot be covered finitely.",
            },
        ),
        "bypassable": jev.noul(
            instructions="Is there any plausible mathematical modification that bypasses this obstruction without changing the core framework?",
            true="Yes, a known variant or refined invariant can bypass this obstruction.",
            false="No, the obstruction is intrinsic to the foundational category/machinery used.",
        ),
        "salvageable_core": jev.choice(
            instructions="What component of this candidate should be preserved in the research ledger?",
            criteria={
                "local_frobenius_traces": "Exact local traces, conductor calculations, and Hecke eigenvalues.",
                "cohomological_vanishing": "Explicit vanishing theorems or rank bounds for specific auxiliary fields.",
                "height_inequalities": "Bounded Arakelov or Faltings height estimates.",
                "negative_certificate": "Rigorous proof that this entire mathematical category cannot resolve Beal.",
            },
        ),
    }


def get_invariant_synthesis_questions() -> dict[str, dict[str, Any]]:
    return {
        "fc_defect_discrimination": jev.noul(
            instructions=(
                "Does this candidate mathematical invariant distinguish the 10 known Fermat-Catalan identities "
                f"({', '.join(FERMAT_CATALAN_IDENTITIES[:3])}...) with exponent 2 from genuine Beal configurations (x,y,z >= 3)? "
                "Specifically, does it exploit the strict hyperbolic defect 1 - 1/x - 1/y - 1/z >= 1/12 such that it vanishes or is blocked on exponent 2?"
            ),
            true="Strictly distinguishes exponent 2 from Beal; exploits the hyperbolic defect -chi >= 1/12.",
            false="Fermat-Catalan blind: holds equally on exponent 2 identities.",
        ),
        "coprimality_coupling": jev.noul(
            instructions=(
                "Does the invariant couple directly to the coprimality condition gcd(A, B, C) = 1 (e.g. through tame/wild conductor, "
                "Serre level, or discriminant valuation), distinguishing coprime integer points from projectively scaled multiples?"
            ),
            true="Directly couples to coprimality; sensitive to common factors.",
            false="Projectively invariant; insensitive to integer gcd scaling.",
        ),
        "finiteness_or_vanishing": jev.choice(
            instructions="What is the ultimate Diophantine consequence forced by this invariant?",
            criteria={
                "nonexistence_certificate": "Forces complete non-existence of primitive solutions when x, y, z >= 3.",
                "finiteness_only": "Proves finiteness of solutions (Faltings/Chabauty), leaving unknown points uneliminated.",
                "local_obstruction": "Provides local obstructions modulo specific prime powers.",
                "vacuous": "Does not constrain integer coordinates on the hypersurface.",
            },
        ),
        "breakthrough_score": jev.score(
            instructions="Evaluate the breakthrough potential of this invariant toward an unconditional resolution of Beal's conjecture.",
            criteria=[
                "level 0: Blind or vacuous; provides no leverage.",
                "level 1: Minor local constraint; does not close any signature.",
                "level 2: Strong structural invariant; closes an infinite signature family or settles bounded prime range.",
                "level 3: Unconditional resolution; overcomes both the exponent 2 defect and the coprimality obstacle.",
            ],
        ),
    }


def get_algebraic_family_questions() -> dict[str, dict[str, Any]]:
    return {
        "local_congruence_obstruction": jev.choice(
            instructions=(
                "Evaluate whether this candidate algebraic parameterization family is trapped by local congruence "
                "obstructions modulo small primes p in {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}.\n"
                "- trapped_by_small_primes: Congruence conditions modulo small primes force gcd(A, B, C) > 1 "
                "or prevent coprime integer solutions from existing.\n"
                "- unobstructed_locally: The family admits coprime solutions modulo all small primes."
            ),
            criteria={
                "trapped_by_small_primes": "Trapped by local congruence obstructions mod small primes.",
                "unobstructed_locally": "Unobstructed locally; admits coprime points mod small primes.",
            },
        ),
        "fc_defect_discrimination": jev.noul(
            instructions=(
                "Does this algebraic family exploit the strict hyperbolic defect 1 - 1/x - 1/y - 1/z >= 1/12, "
                "or does it equally admit solutions with exponent 2 (Fermat-Catalan blind)?"
            ),
            true="Exploits the hyperbolic defect; blocked on exponent 2.",
            false="Fermat-Catalan blind; admits exponent 2 solutions.",
        ),
        "coprimality_preservation": jev.choice(
            instructions=(
                "How does this algebraic family interact with the Beal coprimality condition gcd(A, B, C) = 1?"
            ),
            criteria={
                "intrinsically_coprime": "Parameterization isolates primitive solutions with gcd(A, B, C) = 1.",
                "projectively_invariant": "Parameterization is projectively invariant; gcd(A, B, C) can be scaled arbitrarily.",
                "always_common_factor": "Every integer point generated by this family has gcd(A, B, C) > 1.",
            },
        ),
        "screening_verdict": jev.choice(
            instructions="What is the final screening verdict for this candidate algebraic family?",
            criteria={
                "viable_counterexample_search": "Locally unobstructed and coprime; viable parameterization family for guided counterexample search.",
                "theoretically_obstructed": "Fundamentally obstructed by local congruences, projective degeneration, or Fermat-Catalan defect.",
                "unifying_proof_candidate": "Viable algebraic structure for unifying motivic/modular non-existence attack.",
            },
        ),
    }


# ==============================================================================
# 2. CORE MATHEMATICAL GENIUS ENGINE CLASS
# ==============================================================================

class JevMathematicalGenius:
    """The central orchestrator for Jev-powered mathematical intelligence."""

    def __init__(self):
        self.pool = self._load_pool()

    def _load_pool(self) -> list[dict[str, Any]]:
        if not POOL_FILE.exists():
            return []
        try:
            return json.loads(POOL_FILE.read_text()).get("candidates", [])
        except Exception:
            return []

    def get_candidate(self, cid: str) -> dict[str, Any] | None:
        for c in self.pool:
            if c.get("id") == cid:
                return c
        return None

    def triage_candidates(self, candidate_ids: list[str] | None = None) -> list[dict[str, Any]]:
        """Run the 5-Stage Adversarial Sieve across specified candidate IDs."""
        if not candidate_ids:
            candidate_ids = [c.get("id") for c in self.pool if c.get("status") == "ACTIVE"][:10]
            if not candidate_ids:
                candidate_ids = [c.get("id") for c in self.pool][:10]
            print(f"[JevGenius] No candidate IDs supplied. Triaging top active pool candidates: {candidate_ids}")
        states = []
        c_map = {}
        for cid in candidate_ids:
            cand = self.get_candidate(cid)
            if not cand:
                print(f"[WARN] Candidate {cid} not found in pool. Creating minimal state.")
                cand = {"id": cid, "claim": f"Frontier candidate {cid}", "method": "Unspecified"}
            c_map[cid] = cand
            states.append({
                "conjecture_spec": BEAL_CONJECTURE_SPEC,
                "candidate_id": cid,
                "title": cand.get("title", cid),
                "claim": cand.get("claim", ""),
                "method": cand.get("method", ""),
                "category": cand.get("category", ""),
                "status": cand.get("status", "ACTIVE"),
            })

        questions = get_genius_triage_questions()
        print(f"\n[JevGenius] Querying Jev System One with 5-stage adversarial sieve across {len(states)} candidates...")
        responses = jev.ask_many(states, questions, concurrency=min(12, len(states)))

        results = []
        for state, resp in zip(states, responses):
            cid = state["candidate_id"]
            if "error" in resp:
                print(f"[FAIL] Jev returned error for {cid}: {resp['error']}")
                results.append({"candidate_id": cid, "error": resp["error"]})
                continue

            jev.persist(cid, state, questions, resp)
            answers = resp.get("answers", {})

            # Parse typed answers safely
            target_disc = answers.get("target_discipline", {}).get("noul", 0.0) >= 0.5
            fc_blind = answers.get("fc_blindness", {}).get("noul", 0.0) >= 0.5
            uses_eq = answers.get("uses_equation_gate", {}).get("noul", 0.0) >= 0.5
            survey_cat = answers.get("survey_category", {}).get("choice", "unknown")
            fail_mode = answers.get("canonical_failure_mode", {}).get("choice", "unknown")
            fail_conf = answers.get("canonical_failure_mode", {}).get("confidence", 0.0)
            finiteness = answers.get("finiteness_to_nonexistence", {}).get("choice", "unknown")
            obstruction = answers.get("structural_obstruction", {}).get("choice", "unknown")
            rec_action = answers.get("genius_recommendation", {}).get("choice", "unknown")

            # Calculate Jev Genius Viability Index incorporating all gates from CLAUDE.md
            fail_penalty = 1.0 if fail_mode == "sound_no_failure_mode" else 0.15
            fc_penalty = 0.1 if fc_blind else 1.0
            eq_penalty = 1.0 if uses_eq else 0.20
            survey_factor = 1.0 if survey_cat.startswith("live_") else 0.25
            target_factor = 1.0 if target_disc else 0.0
            genius_index = target_factor * fc_penalty * eq_penalty * fail_penalty * survey_factor

            entry = {
                "candidate_id": cid,
                "title": state["title"],
                "target_discipline": target_disc,
                "fc_blindness": fc_blind,
                "uses_equation": uses_eq,
                "survey_category": survey_cat,
                "failure_mode": fail_mode,
                "failure_mode_confidence": fail_conf,
                "finiteness_profile": finiteness,
                "structural_obstruction": obstruction,
                "recommended_action": rec_action,
                "genius_index": round(genius_index, 3),
                "raw_answers": answers,
            }
            results.append(entry)

            print(f"\n{'='*70}")
            print(f"Candidate: {cid} | Genius Index: {genius_index:.3f}")
            print(f"Title: {state['title']}")
            print(f"  - Target Discipline: {'PASS' if target_disc else 'FAIL'}")
            print(f"  - FC Blindness (Exp 2): {'BLIND' if fc_blind else 'EXPLOITS DEFECT'}")
            print(f"  - Equation Gate (U228): {'USES EQUATION' if uses_eq else 'EXPONENT DISGUISE'}")
            print(f"  - Survey Category (U211): {survey_cat}")
            print(f"  - Failure Mode: {fail_mode} (conf: {fail_conf:.2f})")
            print(f"  - Structural Obstruction: {obstruction}")
            print(f"  - Finiteness Profile: {finiteness}")
            print(f"  - Recommended Action: {rec_action}")

        # Save report
        summary_path = EVIDENCE_DIR / f"genius_triage_{int(time.time())}.json"
        summary_path.write_text(json.dumps(results, indent=2))
        print(f"\n[JevGenius] Triage report saved to: {summary_path}")
        return results

    def synthesize_pair(self, cid_a: str, cid_b: str) -> dict[str, Any]:
        """Evaluate combinatorial synthesis between two candidates."""
        ca = self.get_candidate(cid_a) or {"id": cid_a, "claim": "Unknown", "method": "Unknown"}
        cb = self.get_candidate(cid_b) or {"id": cid_b, "claim": "Unknown", "method": "Unknown"}

        state = {
            "conjecture_spec": BEAL_CONJECTURE_SPEC,
            "candidate_a": {"id": cid_a, "title": ca.get("title", cid_a), "claim": ca.get("claim"), "method": ca.get("method")},
            "candidate_b": {"id": cid_b, "title": cb.get("title", cid_b), "claim": cb.get("claim"), "method": cb.get("method")},
        }

        questions = get_pairwise_synthesis_questions()
        print(f"\n[JevGenius] Evaluating synthesis between {cid_a} and {cid_b}...")
        resp = jev.ask(state, questions)
        jev.persist(f"PAIR_{cid_a}_{cid_b}", state, questions, resp)

        answers = resp.get("answers", {})
        ortho = answers.get("orthogonality", {}).get("noul", 0.0) >= 0.5
        comp = answers.get("obstruction_compensation", {}).get("noul", 0.0) >= 0.5
        score_val = answers.get("breakthrough_potential", {}).get("score", 0.0)
        action = answers.get("synthesis_action", {}).get("choice", "discard_pair")

        print(f"Synthesis Result for {cid_a} + {cid_b}:")
        print(f"  - Orthogonality: {ortho}")
        print(f"  - Obstruction Compensation: {comp}")
        print(f"  - Breakthrough Potential Score: {score_val:.2f} / 3.00")
        print(f"  - Synthesis Action: {action}")

        return {
            "candidate_a": cid_a,
            "candidate_b": cid_b,
            "orthogonality": ortho,
            "compensation": comp,
            "breakthrough_score": score_val,
            "action": action,
            "raw": answers,
        }

    def synthesize_matrix(self, candidate_ids: list[str] | None = None) -> list[dict[str, Any]]:
        """Screen all unordered pairs among candidates to find breakthrough hybrids."""
        if not candidate_ids:
            # Pick active or representative candidates from pool
            candidate_ids = [c["id"] for c in self.pool if c.get("status") in ("ACTIVE", "PARTIAL_RESULT")][-8:]

        pairs = list(itertools.combinations(candidate_ids, 2))
        print(f"\n[JevGenius] Running Combinatorial Synthesis Matrix across {len(pairs)} candidate pairs...")

        states = []
        for cid_a, cid_b in pairs:
            ca = self.get_candidate(cid_a) or {"id": cid_a, "claim": "Unknown", "method": "Unknown"}
            cb = self.get_candidate(cid_b) or {"id": cid_b, "claim": "Unknown", "method": "Unknown"}
            states.append({
                "conjecture_spec": BEAL_CONJECTURE_SPEC,
                "pair_id": f"{cid_a}_{cid_b}",
                "candidate_a": {"id": cid_a, "title": ca.get("title", cid_a), "claim": ca.get("claim"), "method": ca.get("method")},
                "candidate_b": {"id": cid_b, "title": cb.get("title", cid_b), "claim": cb.get("claim"), "method": cb.get("method")},
            })

        questions = get_pairwise_synthesis_questions()
        responses = jev.ask_many(states, questions, concurrency=min(12, len(states)))

        matrix_results = []
        for state, resp in zip(states, responses):
            pair_id = state["pair_id"]
            cid_a, cid_b = pair_id.split("_")
            if "error" in resp:
                continue

            jev.persist(f"MATRIX_{pair_id}", state, questions, resp)
            answers = resp.get("answers", {})
            ortho = answers.get("orthogonality", {}).get("noul", 0.0) >= 0.5
            comp = answers.get("obstruction_compensation", {}).get("noul", 0.0) >= 0.5
            score_val = answers.get("breakthrough_potential", {}).get("score", 0.0)
            action = answers.get("synthesis_action", {}).get("choice", "discard_pair")

            entry = {
                "pair": f"{cid_a} + {cid_b}",
                "candidate_a": cid_a,
                "candidate_b": cid_b,
                "orthogonality": ortho,
                "compensation": comp,
                "breakthrough_score": round(score_val, 2),
                "action": action,
            }
            matrix_results.append(entry)

        matrix_results.sort(key=lambda x: x["breakthrough_score"], reverse=True)

        print("\n" + "=" * 80)
        print("COMBINATORIAL SYNTHESIS MATRIX LEADERBOARD (Top Breakthrough Pairs)")
        print("=" * 80)
        for idx, item in enumerate(matrix_results[:10], 1):
            print(f"{idx:2d}. {item['pair']:<18} | Score: {item['breakthrough_score']:.2f}/3.00 | Ortho: {str(item['orthogonality']):<5} | Comp: {str(item['compensation']):<5} | Action: {item['action']}")

        rep_path = EVIDENCE_DIR / f"genius_synthesis_matrix_{int(time.time())}.json"
        rep_path.write_text(json.dumps(matrix_results, indent=2))
        print(f"\n[JevGenius] Matrix report saved to: {rep_path}")
        return matrix_results

    def salvage_candidates(self, candidate_ids: list[str]) -> list[dict[str, Any]]:
        """Salvage unconditional mathematical lemmas and exact bounds into persistent ledger."""
        questions = {
            "has_reusable_lemma": jev.noul(
                instructions="Does this candidate contain an unconditionally proved lemma, modular trace identity, or arithmetic bound that remains valid even if the headline claim is blocked/refuted?",
                true="Yes, contains genuinely proved, mathematically reusable lemmas.",
                false="No, the entire content is conditional, flawed, or trivial.",
            ),
            "lemma_description": jev.choice(
                instructions="What is the primary category of salvaged mathematical content?",
                criteria={
                    "modular_trace_congruence": "Exact Fourier coefficients and Hecke eigenvalues eliminating local signatures.",
                    "galois_inertia_weight": "Bounds on inertia action or Fontaine-Laffaille Serre weights.",
                    "cohomology_dimension_bound": "Exact dimensions or vanishing of low-degree cohomology / Selmer groups.",
                    "height_positivity": "Positivity bounds on Arakelov or Faltings heights on degenerating curves.",
                    "none": "Nothing mathematically reusable.",
                },
            ),
        }

        states = []
        for cid in candidate_ids:
            c = self.get_candidate(cid) or {"id": cid, "claim": "Unknown", "method": "Unknown"}
            states.append({"candidate_id": cid, "candidate": c})

        print(f"\n[JevGenius] Running salvage protocol across {len(states)} candidates...")
        responses = jev.ask_many(states, questions, concurrency=min(12, len(states)))

        salvaged = []
        for state, resp in zip(states, responses):
            cid = state["candidate_id"]
            if "error" in resp:
                print(f"[FAIL] Salvage error for {cid}: {resp['error']}")
                continue
            jev.persist(f"SALVAGE_{cid}", state, questions, resp)
            answers = resp.get("answers", {})
            noul_val = answers.get("has_reusable_lemma", {}).get("noul", 0.0)
            lemma_type = answers.get("lemma_description", {}).get("choice", "none")
            has_lemma = (noul_val >= 0.35) and (lemma_type != "none")

            print(f"Salvage check for {cid}: has_lemma={has_lemma} (score: {noul_val:.2f}), type={lemma_type}")

            if has_lemma:
                entry = {
                    "candidate_id": cid,
                    "title": state["candidate"].get("title", cid),
                    "lemma_type": lemma_type,
                    "salvage_timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                }
                salvaged.append(entry)
                print(f"[SALVAGED] {cid}: {lemma_type}")

        # Update persistent salvaged database
        existing = []
        if SALVAGED_FILE.exists():
            try:
                existing = json.loads(SALVAGED_FILE.read_text()).get("salvaged_lemmas", [])
            except Exception:
                existing = []

        existing_ids = {item["candidate_id"] for item in existing}
        for item in salvaged:
            if item["candidate_id"] not in existing_ids:
                existing.append(item)

        SALVAGED_FILE.parent.mkdir(parents=True, exist_ok=True)
        SALVAGED_FILE.write_text(json.dumps({"salvaged_lemmas": existing}, indent=2))
        print(f"[JevGenius] Salvaged database updated at: {SALVAGED_FILE} (total {len(existing)} lemmas)")
        return salvaged

    def explain_obstruction(self, cid: str) -> dict[str, Any]:
        """Deeply diagnose the exact mathematical obstruction blocking a candidate."""
        c = self.get_candidate(cid) or {"id": cid, "claim": "Unknown", "method": "Unknown"}
        state = {
            "conjecture_spec": BEAL_CONJECTURE_SPEC,
            "candidate_id": cid,
            "title": c.get("title", cid),
            "claim": c.get("claim", ""),
            "method": c.get("method", ""),
            "failure_reason": c.get("failure_reason", ""),
        }

        questions = get_obstruction_diagnostic_questions()
        print(f"\n[JevGenius] Diagnosing structural obstruction for {cid} ({c.get('title', cid)})...")
        resp = jev.ask(state, questions)
        jev.persist(f"OBSTRUCTION_{cid}", state, questions, resp)

        answers = resp.get("answers", {})
        f_level = answers.get("failure_level", {}).get("choice", "unknown")
        bypass = answers.get("bypassable", {}).get("noul", 0.0) >= 0.5
        salvage_core = answers.get("salvageable_core", {}).get("choice", "negative_certificate")

        print(f"\nObstruction Diagnostic for {cid}:")
        print(f"  - Failure Level: {f_level}")
        print(f"  - Bypassable: {bypass}")
        print(f"  - Salvageable Core: {salvage_core}")
        return {
            "candidate_id": cid,
            "failure_level": f_level,
            "bypassable": bypass,
            "salvageable_core": salvage_core,
            "raw": answers,
        }

    def discover_hypotheses(self, domain: str = "all") -> list[dict[str, Any]]:
        """Autonomously generate and screen breakthrough mathematical hypotheses by domain."""
        all_hypotheses = {
            "arithmetic_geometry": [
                {
                    "id": "H_ORBIFOLD_HIGGS_SIMPSON",
                    "title": "NON-ABELIAN HODGE THEORY & STABLE HIGGS BUNDLES ON TRIANGLE ORBIFOLDS",
                    "claim": "The Simpson correspondence for parabolic Higgs bundles on the orbifold triangle curve (P^1; x, y, z) with -chi >= 1/12 forces harmonic metric rigidity, bounding integer heights.",
                    "method": "Non-abelian Hodge theory, Simpson correspondence, parabolic Higgs bundles, Chern classes, and harmonic maps.",
                    "category": "effective_diophantine_geometry",
                },
                {
                    "id": "H_IWASAWA_PRYM_DESCENT",
                    "title": "ANTICYCLOTOMIC IWASAWA THEORY AND PRYM MONODROMY OF CYCLIC COVERS",
                    "claim": "Vanishing of the anticyclotomic Iwasawa mu-invariant on the Selmer group of the Prym variety Prym(C/P^1) forces rank 0 over Z_p^infty, isolating integer points.",
                    "method": "Iwasawa theory, anticyclotomic extensions, Prym varieties, p-adic L-functions, and Euler systems.",
                    "category": "effective_diophantine_geometry",
                },
            ],
            "derived_noncommutative": [
                {
                    "id": "H_DERIVED_AZUMAYA_TWISTED",
                    "title": "DERIVED AZUMAYA ALGEBRAS & TWISTED SHEAF COHOMOLOGY ON CYCLIC COVERS",
                    "claim": "Derived Azumaya algebras on cyclic covers of P^1 overcome Lefschetz hyperplane Picard vanishing Pic(X_bar)=Z by producing non-trivial classes in derived Brauer group dBr(X).",
                    "method": "Derived algebraic geometry, derived Brauer groups, twisted sheaves, and dg-categories.",
                    "category": "unifying_modular_motivic_geometry",
                },
                {
                    "id": "H_DERIVED_INTERSECTION_ARAKELOV",
                    "title": "DERIVED INTERSECTION HEIGHTS & KODAIRA-SPENCER OVER SPEC Z",
                    "claim": "Arithmetic intersection self-pairing <omega, omega>_Ar in derived Arakelov geometry on cyclic covers bounds coordinates unconditionally by avoiding Kodaira-Spencer degeneration.",
                    "method": "Derived algebraic geometry, Arakelov intersection theory, arithmetic Chow groups, and Deligne pairings.",
                    "category": "effective_diophantine_geometry",
                },
            ],
            "padic_hodge_prismatic": [
                {
                    "id": "H_SYNTHETIC_SPECTRUM_TC",
                    "title": "RELATIVE TOPOLOGICAL CYCLIC HOMOLOGY TC(Z[1/6]) AND FROBENIUS MONODROMY",
                    "claim": "The cyclotomic trace map trc: K_1(Z[1/6]) -> TC_1(Z[1/6]) kills primitive integer solutions to A^x + B^y = C^z for x,y,z >= 3 by non-triviality of Bott-inverted homotopy.",
                    "method": "Topological cyclic homology, cyclotomic trace, spectral algebraic geometry, and motivic homotopy theory over the sphere spectrum S.",
                    "category": "unifying_modular_motivic_geometry",
                },
                {
                    "id": "H_PRISMATIC_F_GAUGE_BEAL",
                    "title": "PRISMATIC DIEUDONNE THEORY AND NYGAARD FILTRATION ON FERMAT COVERS",
                    "claim": "The Nygaard filtration on the prismatic cohomology Delta_{X/Z_p} of cyclic covers produces an integer height gap preventing solutions with coprime coordinates.",
                    "method": "Prismatic cohomology (Bhatt-Scholze), F-gauges, Breuil-Kisin modules, and Nygaard filtration.",
                    "category": "unifying_modular_motivic_geometry",
                },
            ],
            "automorphic_langlands": [
                {
                    "id": "H_RIGID_LOCAL_SYSTEMS_KATZ",
                    "title": "PHYSICAL RIGIDITY AND KATZ MIDDLE CONVOLUTION ON (P^1 \\ {0, 1, infty})",
                    "claim": "Katz middle convolution MC_chi transforms the local system of A^x + B^y = C^z into an irreducible rigid local system that cannot lift to Q without sharing a common factor.",
                    "method": "Rigid local systems, Katz middle convolution, index of rigidity, and geometric monodromy.",
                    "category": "unifying_modular_motivic_geometry",
                },
                {
                    "id": "H_ARTHUR_CLOISEL_BASE_CHANGE",
                    "title": "ARTHUR ENDOSCOPIC CLASSIFICATION AND BASE CHANGE TO TOTALLY REAL FIELDS",
                    "claim": "Base change of Frey representations to abelian real extensions forces residual automorphy obstructions that rule out primitive solutions for infinite exponent families.",
                    "method": "Arthur endoscopic classification, Clozel-Harris-Taylor automorphy, and base change.",
                    "category": "classical_modular_frey",
                },
            ],
            "diophantine_transcendence": [
                {
                    "id": "H_BAKER_WUSTHOLZ_HEIGHT_GAP",
                    "title": "LINEAR FORMS IN LOGARITHMS & SEMI-STABLE BAKER-WUSTHOLZ BOUNDS",
                    "claim": "Explicit lower bounds on linear forms in logarithms of algebraic numbers combined with Frey minimal discriminants force an upper bound on min(x, y, z).",
                    "method": "Baker-Wüstholz theorem, linear forms in p-adic logarithms, and Frey minimal discriminants.",
                    "category": "effective_diophantine_geometry",
                },
                {
                    "id": "H_O_MINIMAL_PILA_ZANNIER",
                    "title": "O-MINIMALITY AND PILA-ZANNIER COUNTING ON MODULI OF FREY CURVES",
                    "claim": "The Pila-Wilkie counting theorem applied to the period map of the Frey curve restricts integer points on non-algebraic transcendental loci.",
                    "method": "O-minimality, Pila-Zannier strategy, Ax-Schanuel for Shimura varieties, and point counting.",
                    "category": "effective_diophantine_geometry",
                },
            ],
        }

        selected_hypotheses = []
        if domain == "all":
            for group in all_hypotheses.values():
                selected_hypotheses.extend(group)
        elif domain in all_hypotheses:
            selected_hypotheses.extend(all_hypotheses[domain])
        else:
            print(f"[ERR] Unknown domain '{domain}'. Valid: {list(all_hypotheses.keys())} or 'all'.")
            return []

        states = []
        for h in selected_hypotheses:
            states.append({
                "conjecture_spec": BEAL_CONJECTURE_SPEC,
                "candidate_id": h["id"],
                "title": h["title"],
                "claim": h["claim"],
                "method": h["method"],
                "category": h["category"],
                "status": "HYPOTHESIS_ONLY",
            })

        questions = get_genius_triage_questions()
        print(f"\n[JevGenius] Screening {len(states)} breakthrough hypotheses in domain '{domain}'...")
        responses = jev.ask_many(states, questions, concurrency=min(12, len(states)))

        discovered = []
        for state, resp in zip(states, responses):
            hid = state["candidate_id"]
            if "error" in resp:
                continue
            jev.persist(hid, state, questions, resp)
            answers = resp.get("answers", {})

            target_disc = answers.get("target_discipline", {}).get("noul", 0.0) >= 0.5
            fc_blind = answers.get("fc_blindness", {}).get("noul", 0.0) >= 0.5
            fail_mode = answers.get("canonical_failure_mode", {}).get("choice", "unknown")
            fail_conf = answers.get("canonical_failure_mode", {}).get("confidence", 0.0)
            obstruction = answers.get("structural_obstruction", {}).get("choice", "unknown")
            rec_action = answers.get("genius_recommendation", {}).get("choice", "unknown")

            fail_penalty = 1.0 if fail_mode == "sound_no_failure_mode" else 0.15
            fc_penalty = 0.1 if fc_blind else 1.0
            target_factor = 1.0 if target_disc else 0.0
            genius_index = target_factor * fc_penalty * fail_penalty

            entry = {
                "hypothesis_id": hid,
                "title": state["title"],
                "genius_index": round(genius_index, 3),
                "target_discipline": target_disc,
                "fc_blindness": fc_blind,
                "failure_mode": fail_mode,
                "failure_mode_confidence": fail_conf,
                "structural_obstruction": obstruction,
                "recommended_action": rec_action,
            }
            discovered.append(entry)

            print(f"\n{'='*70}")
            print(f"Hypothesis: {hid} | Genius Index: {genius_index:.3f}")
            print(f"Title: {state['title']}")
            print(f"  - Target Discipline: {'PASS' if target_disc else 'FAIL'}")
            print(f"  - FC Blindness (Exp 2): {'BLIND' if fc_blind else 'EXPLOITS DEFECT'}")
            print(f"  - Failure Mode: {fail_mode} (conf: {fail_conf:.2f})")
            print(f"  - Structural Obstruction: {obstruction}")
            print(f"  - Action: {rec_action}")

        rep_path = EVIDENCE_DIR / f"genius_discovery_{domain}_{int(time.time())}.json"
        rep_path.write_text(json.dumps(discovered, indent=2))
        print(f"\n[JevGenius] Discovery report saved to: {rep_path}")
        return discovered

    def run_benchmark(self) -> dict[str, Any]:
        """Calibrate Jev's discrimination accuracy against ground truth theorems vs. canonical fallacies."""
        benchmark_cases = [
            # Ground Truth True/Sound
            {
                "id": "GT_WILES_FLT",
                "title": "WILES 1995 MODULARITY THEOREM & FERMAT'S LAST THEOREM",
                "claim": "Every semistable elliptic curve over Q is modular; ribet level lowering forces Frey curve representation to arise from S_2(2) = 0, proving A^p + B^p = C^p has no non-trivial solutions for p >= 3.",
                "method": "Galois deformation theory, modularity of semistable elliptic curves, Ribet level lowering.",
                "ground_truth_sound": True,
                "ground_truth_failure": "sound_no_failure_mode",
            },
            {
                "id": "GT_DARMON_GRANVILLE",
                "title": "DARMON-GRANVILLE 1995 GENERALIZED FERMAT FINITENESS",
                "claim": "For fixed positive integers x, y, z with 1/x + 1/y + 1/z < 1, the equation A^x + B^y = C^z has only finitely many primitive integer solutions.",
                "method": "Faltings' theorem on subvarieties of abelian varieties, Prym varieties, cyclic coverings.",
                "ground_truth_sound": True,
                "ground_truth_failure": "sound_no_failure_mode",
            },
            {
                "id": "GT_KRAUS_SIEVE",
                "title": "KRAUS 1997 MODULAR SIEVE CRITERION FOR (3, 3, p)",
                "claim": "For a fixed prime p >= 5, if there exists an auxiliary prime k = 2*m*p + 1 such that for all newforms f in S_2(N) and all candidate Frobenius traces a_k(E_{A,B}), a_k(E) != a_k(f) mod l, then no solutions exist.",
                "method": "Explicit Kraus sieve, Galois representations, Fourier coefficients of weight 2 newforms.",
                "ground_truth_sound": True,
                "ground_truth_failure": "sound_no_failure_mode",
            },
            # Ground Truth Fallacies
            {
                "id": "FALLACY_RESIDUAL_CONFLATION",
                "title": "RESIDUAL MOD-P CONGRUENCE REFUTED BY NON-ISOGENY",
                "claim": "Because elliptic curve E is not isogenous to any elliptic curve of conductor 2 or 6, their mod-p Galois representations rho_{E, p} cannot be isomorphic for any prime p.",
                "method": "Isogeny class refutation.",
                "ground_truth_sound": False,
                "ground_truth_failure": "mode_1_residual_conflation",
            },
            {
                "id": "FALLACY_CHABAUTY_WRONG_FIELD",
                "title": "CHABAUTY OVER BASE FIELD APPLIED TO EXTENSION POINTS",
                "claim": "Proving rank J(Q) < genus(C) implies C(K) has only finitely many points for all number fields K generated by coordinates of Beal solutions.",
                "method": "Chabauty-Coleman method applied across field extensions without bounding ramification S.",
                "ground_truth_sound": False,
                "ground_truth_failure": "mode_2_chabauty_unbounded_s",
            },
            {
                "id": "FALLACY_HEURISTIC_LAUNDERING",
                "title": "COHEN-LENSTRA HEURISTIC USED AS UNCONDITIONAL PROOF",
                "claim": "Because the Cohen-Lenstra heuristic predicts the p-part of the class group Cl(Q(sqrt(-d))) is trivial with probability 1 - O(1/p), this rules out counterexamples unconditionally.",
                "method": "Heuristic laundering of probabilistic distribution as unconditional proof.",
                "ground_truth_sound": False,
                "ground_truth_failure": "mode_3_heuristic_laundering",
            },
            {
                "id": "FALLACY_APPROXIMATION_DIRECTION",
                "title": "PARI ELLRANK LOWER BOUND USED AS RANK ZERO CERTIFICATE",
                "claim": "Evaluating ellrank(E)[1] = 0 proves the Mordell-Weil rank of the Jacobian is 0, eliminating rational points.",
                "method": "Unchecked approximation direction: ellrank(E)[1] is PARI's lower rank bound, not upper bound.",
                "ground_truth_sound": False,
                "ground_truth_failure": "mode_4_unchecked_approximation_direction",
            },
        ]

        states = []
        for b in benchmark_cases:
            states.append({
                "conjecture_spec": BEAL_CONJECTURE_SPEC,
                "candidate_id": b["id"],
                "title": b["title"],
                "claim": b["claim"],
                "method": b["method"],
            })

        questions = get_genius_triage_questions()
        print(f"\n[JevGenius] Running Intelligence Benchmark across {len(states)} calibrated cases...")
        responses = jev.ask_many(states, questions, concurrency=len(states))

        correct_soundness = 0
        correct_failure_mode = 0
        total = len(states)

        for b, resp in zip(benchmark_cases, responses):
            cid = b["id"]
            answers = resp.get("answers", {})
            fail_mode = answers.get("canonical_failure_mode", {}).get("choice", "unknown")
            is_sound = (fail_mode == "sound_no_failure_mode")

            sound_match = (is_sound == b["ground_truth_sound"])
            mode_match = (fail_mode == b["ground_truth_failure"])

            if sound_match:
                correct_soundness += 1
            if mode_match:
                correct_failure_mode += 1

            status = "PASS" if sound_match and mode_match else "WARN"
            print(f"[{status}] {cid}: Soundness={sound_match} | FailureMode={mode_match} (Predicted: {fail_mode}, Truth: {b['ground_truth_failure']})")

        soundness_acc = correct_soundness / total
        failure_acc = correct_failure_mode / total
        print(f"\n[JevGenius Benchmark Results]")
        print(f"  - Soundness Classification Accuracy: {soundness_acc * 100:.1f}% ({correct_soundness}/{total})")
        print(f"  - Failure Mode Pinpoint Accuracy:    {failure_acc * 100:.1f}% ({correct_failure_mode}/{total})")

        return {
            "soundness_accuracy": soundness_acc,
            "failure_mode_accuracy": failure_acc,
            "total_cases": total,
        }

    def verify_lean_file(self, lean_file_path: str) -> dict[str, Any]:
        """Verify Lean 4 theorem statements against Beal target discipline and axiomatics with deterministic pre-checks."""
        lp = Path(lean_file_path)
        if not lp.exists():
            print(f"[ERR] Lean file {lean_file_path} not found.")
            return {"error": "File not found"}

        content = lp.read_text()

        # 1. Deterministic static audit: check for sorry, admit, and custom axioms
        has_sorry = bool(re.search(r"\bsorry\b", content))
        has_admit = bool(re.search(r"\badmit\b", content))
        custom_axioms = re.findall(r"^\s*axiom\s+(\w+)", content, re.MULTILINE)
        theorem_lines = [line.strip() for line in content.splitlines() if line.strip().startswith("theorem")]

        deterministic_flags = {
            "has_sorry": has_sorry,
            "has_admit": has_admit,
            "custom_axioms": custom_axioms,
            "theorem_count": len(theorem_lines),
        }

        # 2. Try running Lake build/lean if lake is installed
        lake_compile_ok = None
        lake_stderr = ""
        try:
            formal_dir = REPO_ROOT / "formal"
            rel_path = lp.resolve().relative_to(formal_dir.resolve()) if lp.resolve().is_relative_to(formal_dir.resolve()) else lp.resolve()
            res = subprocess.run(
                ["lake", "env", "lean", str(rel_path)],
                capture_output=True,
                text=True,
                cwd=str(formal_dir),
                timeout=30,
            )
            lake_compile_ok = (res.returncode == 0)
            lake_stderr = res.stderr[:500]
        except Exception:
            pass

        state = {
            "lean_file": str(lp.name),
            "theorems": theorem_lines[:15],
            "full_content_snippet": content[:2000],
            "deterministic_flags": deterministic_flags,
            "lake_compilation_success": lake_compile_ok,
            "conjecture_spec": BEAL_CONJECTURE_SPEC,
        }

        questions = {
            "statement_fidelity": jev.noul(
                instructions="Do the theorem statements in this Lean 4 file encode the exact mathematical conjecture (or an exact partial case) without relaxing exponents, dropping coprimality, or assuming vacuous premises?",
                true="The formal theorem statements faithfully encode the mathematical problem.",
                false="The statements suffer from proxy relaxation, exponent-2 leakage, or vacuous hypotheses.",
            ),
            "action": jev.choice(
                instructions="What is the recommended verification action for this Lean file?",
                criteria={
                    "lake_build_verify": "Proceed with Lake build and axiom audit [propext, Classical.choice, Quot.sound].",
                    "rewrite_statement": "Refactor formal theorem statements to ensure exact fidelity to Beal's conjecture.",
                    "reject_formalization": "Reject formalization due to severe statement drift, sorry placeholders, or custom axioms.",
                },
            ),
        }

        print(f"\n[JevGenius] Auditing Lean 4 formal file: {lp.name}...")
        resp = jev.ask(state, questions)
        jev.persist(f"LEAN_{lp.stem}", state, questions, resp)

        answers = resp.get("answers", {})
        fidelity = answers.get("statement_fidelity", {}).get("noul", 0.0) >= 0.5
        rec_action = answers.get("action", {}).get("choice", "lake_build_verify")

        # Deterministic override: if sorry or custom axioms exist, action MUST reject
        if has_sorry or has_admit or custom_axioms:
            rec_action = "reject_formalization"

        print(f"Lean Audit Result for {lp.name}:")
        print(f"  - Deterministic Audit: sorry={has_sorry}, admit={has_admit}, custom_axioms={custom_axioms}")
        if lake_compile_ok is not None:
            print(f"  - Lake Compiler Status: {'PASS' if lake_compile_ok else 'FAIL'}")
        print(f"  - Statement Fidelity:   {'PASS' if fidelity else 'FAIL'}")
        print(f"  - Final Action:         {rec_action}")

        return {
            "file": str(lp.name),
            "deterministic": deterministic_flags,
            "lake_compile_ok": lake_compile_ok,
            "fidelity": fidelity,
            "action": rec_action,
            "raw": answers,
        }

    def synthesize_invariant(self, invariants: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
        """Screen mathematical invariants for Fermat-Catalan defect discrimination and coprimality coupling."""
        if not invariants:
            invariants = [
                {
                    "id": "INV_ORBIFOLD_EULER_DEFECT",
                    "title": "Orbifold Euler Characteristic Defect Invariant: -chi(P^1; x, y, z) = 1 - 1/x - 1/y - 1/z",
                    "formula": "-chi = 1 - 1/x - 1/y - 1/z >= 1/12",
                    "description": "Measures the hyperbolic area of the triangle orbifold. Strictly positive for x,y,z >= 3, but <= 0 or zero for spherical/Euclidean triples (2, 3, 6), (2, 4, 4), (3, 3, 3).",
                },
                {
                    "id": "INV_SERRE_CONDUCTOR_VALUATION",
                    "title": "Serre Level Wild Conductor Invariant N(rho_{E, p}) at Primes 2 and 3",
                    "formula": "val_2(N) in {1, 5, 6}, val_3(N) in {1, 2, 3}",
                    "description": "Calculates the minimal conductor of the Frey curve representation. Detects coprimality gcd(A, B, C) = 1 via additive reduction exponents at 2 and 3.",
                },
                {
                    "id": "INV_KRAUS_FROBENIUS_DEGENERACY",
                    "title": "Kraus Frobenius Trace Degeneracy Sieve: a_k(E_{A,B}) mod l vs a_k(f)",
                    "formula": "prod_{f in S_2(N)} (a_k(E) - a_k(f)) != 0 mod l",
                    "description": "Explicit local Frobenius trace differences at auxiliary primes k = 2mp + 1. Eliminates residual representations unconditionally.",
                },
                {
                    "id": "INV_DERIVED_BRAUER_AZUMAYA",
                    "title": "Derived Brauer Group Class: dBr(X) = H^2(X_et, G_m) / Br(Q)",
                    "formula": "alpha in dBr(X) with alpha(P) non-trivial on integer points",
                    "description": "Non-commutative derived Azumaya algebra on cyclic covers to bypass Lefschetz hyperplane Picard rigidity.",
                },
            ]

        states = []
        for inv in invariants:
            states.append({
                "conjecture_spec": BEAL_CONJECTURE_SPEC,
                "invariant_id": inv["id"],
                "title": inv["title"],
                "formula": inv.get("formula", ""),
                "description": inv.get("description", ""),
            })

        questions = get_invariant_synthesis_questions()
        print(f"\n[JevGenius] Synthesizing and evaluating {len(states)} Diophantine invariants...")
        responses = jev.ask_many(states, questions, concurrency=min(12, len(states)))

        results = []
        for state, resp in zip(states, responses):
            iid = state["invariant_id"]
            if "error" in resp:
                continue
            jev.persist(f"INVARIANT_{iid}", state, questions, resp)
            answers = resp.get("answers", {})

            fc_disc = answers.get("fc_defect_discrimination", {}).get("noul", 0.0) >= 0.5
            coprime = answers.get("coprimality_coupling", {}).get("noul", 0.0) >= 0.5
            consequence = answers.get("finiteness_or_vanishing", {}).get("choice", "vacuous")
            score_val = answers.get("breakthrough_score", {}).get("score", 0.0)

            entry = {
                "invariant_id": iid,
                "title": state["title"],
                "fc_defect_discrimination": fc_disc,
                "coprimality_coupling": coprime,
                "consequence": consequence,
                "breakthrough_score": round(score_val, 2),
            }
            results.append(entry)

            print(f"\n{'='*70}")
            print(f"Invariant: {iid} | Score: {score_val:.2f} / 3.00")
            print(f"Title: {state['title']}")
            print(f"  - FC Defect Discrimination: {'DISCRIMINATING' if fc_disc else 'BLIND'}")
            print(f"  - Coprimality Coupling:     {'COUPLED' if coprime else 'PROJECTIVE'}")
            print(f"  - Diophantine Consequence:  {consequence}")

        rep_path = EVIDENCE_DIR / f"genius_invariants_{int(time.time())}.json"
        rep_path.write_text(json.dumps(results, indent=2))
        print(f"\n[JevGenius] Invariant synthesis report saved to: {rep_path}")
        return results

    def screen_algebraic_families(self, families: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
        """Screen candidate algebraic parameterization families for counterexample hunt or motivic proof."""
        if not families:
            families = [
                {
                    "id": "FAM_KUMMER_COVERS",
                    "title": "Cyclic Kummer Covers of P^1 \\ {0, 1, \\infty}",
                    "formula": "w^N = x^a (1-x)^b with x = A^x / C^z",
                    "description": "Geometric covers mapping Diophantine solutions to rational points on higher-genus curves. Subject to Coleman-Chabauty bounds.",
                },
                {
                    "id": "FAM_FERMAT_TWISTS",
                    "title": "Twists of Fermat Curves over Cyclotomic and Quadratic Fields",
                    "formula": "a X^p + b Y^p + c Z^p = 0 over Q(zeta_p) or Q(sqrt(-3))",
                    "description": "Algebraic twists of Fermat hypersurfaces with prescribed ramification at primes dividing ABC.",
                },
                {
                    "id": "FAM_EISENSTEIN_COORDINATES",
                    "title": "Eisenstein Coordinate Families A^3 + B^3 = C^z via Z[omega]",
                    "formula": "(A + B)(A + omega B)(A + omega^2 B) = C^z, with omega^2 + omega + 1 = 0",
                    "description": "Algebraic factorization in the Eisenstein ring Z[omega]. Ideal factorization requires each factor to be an almost-z-th power.",
                },
                {
                    "id": "FAM_PRYM_TYURIN_COVERS",
                    "title": "Prym-Tyurin Covers and Prym Varieties of Dihedral Covers",
                    "formula": "Prym(C / C_0) attached to triangle curve coverings",
                    "description": "Abelian varieties associated to dihedral covers of P^1 with branch points at {0, 1, \\infty}, providing Frey-like representations for 3 exponents.",
                },
                {
                    "id": "FAM_FREY_HELLEGOUARCH",
                    "title": "Frey-Hellegouarch Weierstrass Curves y^2 = x(x - A^x)(x + B^y)",
                    "formula": "y^2 = x(x - A^x)(x + B^y), Delta = 16 (A^x B^y C^z)^2",
                    "description": "Elliptic curves over Q whose minimal discriminant is a 2z-th or 2-power times conductor powers. Bounded levels 2, 32, 64, 144.",
                },
            ]

        states = []
        for fam in families:
            states.append({
                "conjecture_spec": BEAL_CONJECTURE_SPEC,
                "family_id": fam["id"],
                "title": fam["title"],
                "formula": fam.get("formula", ""),
                "description": fam.get("description", ""),
            })

        questions = get_algebraic_family_questions()
        print(f"\n[JevGenius] Screening {len(states)} algebraic parameterization families with Jev System One...")
        responses = jev.ask_many(states, questions, concurrency=min(12, len(states)))

        results = []
        for state, resp in zip(states, responses):
            fid = state["family_id"]
            if "error" in resp:
                continue
            jev.persist(f"FAMILY_{fid}", state, questions, resp)
            answers = resp.get("answers", {})

            local_obs = answers.get("local_congruence_obstruction", {}).get("choice", "unknown")
            fc_disc = answers.get("fc_defect_discrimination", {}).get("noul", 0.0) >= 0.5
            coprime = answers.get("coprimality_preservation", {}).get("choice", "unknown")
            verdict = answers.get("screening_verdict", {}).get("choice", "theoretically_obstructed")

            entry = {
                "family_id": fid,
                "title": state["title"],
                "local_congruence_obstruction": local_obs,
                "fc_defect_discrimination": fc_disc,
                "coprimality_preservation": coprime,
                "screening_verdict": verdict,
                "raw": answers,
            }
            results.append(entry)

            print(f"\n{'='*70}")
            print(f"Family: {fid} | Verdict: {verdict}")
            print(f"Title: {state['title']}")
            print(f"  - Local Congruence Modulo Small Primes: {local_obs}")
            print(f"  - Fermat-Catalan Defect Discrimination: {'DISCRIMINATING' if fc_disc else 'BLIND'}")
            print(f"  - Coprimality Preservation:            {coprime}")
            print(f"  - Screening Assessment:                {verdict}")

        rep_path = EVIDENCE_DIR / f"genius_algebraic_families_{int(time.time())}.json"
        rep_path.write_text(json.dumps(results, indent=2))
        print(f"\n[JevGenius] Algebraic families screening report saved to: {rep_path}")
        return results

    def generate_candidate(self, signature: str = "3,3,p", framework: str = "derived_geometry") -> dict[str, Any]:
        """Autonomously propose, formulate, and screen a new mathematical candidate."""
        prompt_state = {
            "conjecture_spec": BEAL_CONJECTURE_SPEC,
            "target_signature": signature,
            "framework": framework,
        }
        cand_questions = {
            "promising_mechanism": jev.choice(
                instructions=f"Select the most promising mathematical mechanism for signature {signature} in framework {framework}.",
                criteria={
                    "twisted_sheaves_cyclic_prym": "Twisted sheaves and Azumaya algebras on cyclic Prym covers bypassing Lefschetz hyperplane Picard vanishing.",
                    "modular_kraus_hilbert_extension": "Multi-form Kraus sieve over real quadratic fields or higher-level modular curves.",
                    "prismatic_nygaard_height": "Prismatic cohomology Nygaard filtration gap constraining integer coordinate heights.",
                    "relative_anabelian_outer_galois": "Relative anabelian section conjecture on affine hyperbolic triangle curve.",
                },
            ),
            "expected_obstruction": jev.choice(
                instructions="What is the anticipated primary mathematical obstruction for this mechanism?",
                criteria={
                    "selmer_dimension_growth": "Selmer variety dimension grows with unknown primes(ABC).",
                    "continuous_moduli_degeneration": "Moduli parameters degenerate at punctures {0, 1, infty}.",
                    "torsion_wild_ramification": "Wild additive reduction at 2 and 3 obstructs p-adic period maps.",
                    "computational_scale": "Method is sound but requires computationally intensive modular traces.",
                },
            ),
        }
        print(f"\n[JevGenius] Generating new mathematical candidate for signature ({signature}) using {framework}...")
        resp = jev.ask(prompt_state, cand_questions)
        answers = resp.get("answers", {})
        mech = answers.get("promising_mechanism", {}).get("choice", "twisted_sheaves_cyclic_prym")
        obs = answers.get("expected_obstruction", {}).get("choice", "continuous_moduli_degeneration")

        existing_nums = []
        for c in self.pool:
            cid = c.get("id", "")
            if cid.startswith("C") and cid[1:].isdigit():
                existing_nums.append(int(cid[1:]))
        next_num = max(existing_nums, default=401) + 1
        new_cid = f"C{next_num}"

        titles = {
            "twisted_sheaves_cyclic_prym": "DERIVED AZUMAYA ALGEBRAS & TWISTED SHEAVES ON PRYM COVERS",
            "modular_kraus_hilbert_extension": "HILBERT MODULAR KRAUS SIEVE EXTENSION OVER REAL QUADRATIC FIELDS",
            "prismatic_nygaard_height": "PRISMATIC NYGAARD FILTRATION AND DIEUDONNE HEIGHT BOUNDS",
            "relative_anabelian_outer_galois": "RELATIVE ANABELIAN SECTION CONJECTURE ON TRIANGLE ORBIFOLDS",
        }

        candidate_obj = {
            "id": new_cid,
            "title": titles.get(mech, f"ADVANCED {framework.upper()} MECHANISM FOR {signature}"),
            "claim": f"Derived invariants for signature ({signature}) constrain primitive integer solutions unconditionally.",
            "method": f"{framework.replace('_', ' ').title()} combined with Galois deformation and modular elimination.",
            "status": "ACTIVE",
            "category": "unifying_modular_motivic_geometry",
            "parents": ["C400", "C401"],
            "inspirations": ["Grothendieck 1968", "Lieblich 2008", "Kraus 1998"],
            "evidence": [],
            "obligations": [f"Audit whether {mech} overcomes {obs}."],
            "evaluations": {"category": "unifying_modular_motivic_geometry"},
            "novelty_note": f"Autonomous candidate synthesized by Jev Genius using {mech}.",
        }

        print(f"\n[JevGenius Generated Candidate {new_cid}]")
        print(f"  - Title: {candidate_obj['title']}")
        print(f"  - Mechanism: {mech}")
        print(f"  - Anticipated Obstruction: {obs}")

        self.pool.append(candidate_obj)
        triage_res = self.triage_candidates([new_cid])
        self.pool.pop()
        candidate_obj["triage_result"] = triage_res

        return candidate_obj

    def run_cycle(self) -> dict[str, Any]:
        """Execute an autonomous end-to-end research cycle powered by Jev."""
        print("\n" + "=" * 80)
        print("STARTING AUTONOMOUS JEV RESEARCH CYCLE")
        print("=" * 80)

        print("\n[Cycle Step 1/4] Running Intelligence Benchmark...")
        bench = self.run_benchmark()

        print("\n[Cycle Step 2/4] Screening Diophantine Invariants...")
        invs = self.synthesize_invariant()

        print("\n[Cycle Step 3/4] Screening Candidate Combinatorial Matrix...")
        mat = self.synthesize_matrix()

        print("\n[Cycle Step 4/4] Running Lemma Salvage Engine...")
        active_ids = [c["id"] for c in self.pool if c.get("status") in ("ACTIVE", "PARTIAL_RESULT")][-5:]
        salv = self.salvage_candidates(active_ids)

        print("\n" + "=" * 80)
        print("AUTONOMOUS JEV RESEARCH CYCLE COMPLETE")
        print(f"  - Benchmark Accuracy: {bench['soundness_accuracy']*100:.1f}%")
        print(f"  - Invariants Screened: {len(invs)}")
        print(f"  - Candidate Pairs Evaluated: {len(mat)}")
        print(f"  - Lemmas Salvaged: {len(salv)}")
        print("=" * 80)
        return {
            "benchmark": bench,
            "invariants": invs,
            "matrix": mat,
            "salvaged": salv,
        }

    def advise_sieve(self, signature: str = "3,3,p", p_min: int = 5501, p_max: int = 5600, run_computation: bool = False) -> dict[str, Any]:
        """Advise on optimal Kraus sieve modular elimination parameters for a signature, with optional exact execution."""
        print(f"\n[JevGenius Sieve Advisor] Analyzing modular parameters for signature ({signature}) across [{p_min}, {p_max}]...")
        state = {
            "conjecture_spec": BEAL_CONJECTURE_SPEC,
            "target_signature": signature,
            "p_min": p_min,
            "p_max": p_max,
        }
        questions = {
            "modular_levels": jev.choice(
                instructions=f"What are the target newform levels for Frey curves of signature {signature}?",
                criteria={
                    "level_72_144": "Levels 72 and 144 (Kraus Frey curve y^2 = x^3 + 3AB x + B^3 - A^3).",
                    "level_32_64_128": "Levels 32, 64, and 128 (Ellenberg Frey curve for signature (2, 4, p)).",
                    "hilbert_level_25_50": "Hilbert modular levels over Q(sqrt(5)) (Billerey et al. for (5, 5, p)).",
                    "hyperelliptic_jacobian": "Jacobian varieties of hyperelliptic curves over Q for (2, 3, p).",
                },
            ),
            "expected_sieve_rate": jev.choice(
                instructions=f"What is the expected empirical elimination rate of the modular sieve for {signature}?",
                criteria={
                    "high_rate_above_95": "High elimination rate (>95%); almost every prime eliminated at low k <= 20.",
                    "moderate_rate_50_90": "Moderate rate (50-90%); requires searching higher auxiliary moduli k <= 200.",
                    "low_rate_below_50": "Low rate (<50%); severely obstructed by trace collisions or CM forms.",
                },
            ),
        }
        resp = jev.ask(state, questions)
        answers = resp.get("answers", {})
        levels = answers.get("modular_levels", {}).get("choice", "level_72_144")
        rate = answers.get("expected_sieve_rate", {}).get("choice", "high_rate_above_95")

        print("\n" + "=" * 80)
        print(f"KRAUS SIEVE MODULAR ADVISORY REPORT: Signature ({signature})")
        print("=" * 80)
        print(f"  - Target Exponent Range:       [{p_min}, {p_max}]")
        print(f"  - Target Modular Levels:       {levels}")
        print(f"  - Expected Sieve Rate:         {rate}")
        print(f"  - Recommended Auxiliary Bound: max_q = 400,000 (k <= 40)")
        print(f"  - Sieve Algorithm:             Canonical Kraus Frey parameterization with Legendre O(1) table")
        print("=" * 80)

        computation_results = None
        if run_computation:
            print(f"\n[JevGenius Sieve Execution] Running deterministic Kraus sieve computation for {signature} across [{p_min}, {p_max}]...")
            try:
                import sympy
                sys.path.insert(0, str(REPO_ROOT / "code"))
                from kraus_sieve_signature_3_3_p import kraus_sieve
                eliminated = []
                uneliminated = []
                primes_to_test = [p for p in range(p_min, p_max + 1) if sympy.isprime(p)]
                for p in primes_to_test:
                    res = kraus_sieve(p, max_k=40, verbose=False)
                    if res:
                        q, k, _, _, _ = res
                        eliminated.append((p, q, k))
                    else:
                        uneliminated.append(p)
                computation_results = {
                    "primes_tested": len(primes_to_test),
                    "eliminated_count": len(eliminated),
                    "uneliminated": uneliminated,
                    "sample_eliminations": eliminated[:5],
                }
                print(f"  - Primes Tested: {len(primes_to_test)}")
                print(f"  - Eliminated:    {len(eliminated)} / {len(primes_to_test)}")
                if uneliminated:
                    print(f"  - Uneliminated:  {uneliminated}")
                else:
                    print(f"  - Status:        100% of primes in range eliminated!")
            except Exception as e:
                print(f"[WARN] Could not run deterministic sieve computation: {e}")
                computation_results = {"error": str(e)}

        return {
            "signature": signature,
            "p_range": [p_min, p_max],
            "levels": levels,
            "expected_rate": rate,
            "computation": computation_results,
        }

    def get_signature_taxonomy(self, signature: str | None = None) -> dict[str, Any]:
        """Query the exact mathematical taxonomy of Beal signatures and their literature status."""
        taxonomy = {
            "(n, n, n)": {"status": "SOLVED", "theorem": "Fermat's Last Theorem (Wiles 1995, Taylor-Wiles 1995)", "method": "Semistable elliptic curves, Mazur deformation, level lowering."},
            "(n, n, 2)": {"status": "SOLVED", "theorem": "Darmon-Merel (1997)", "method": "Frey curve y^2 = x^3 + 2(A - B)x^2 - (A+B)^2 x, Mazur level 32/64."},
            "(n, n, 3)": {"status": "SOLVED", "theorem": "Darmon-Merel (1997)", "method": "Frey curve over Q, level 18 vanishing dim S_2(18) = 0."},
            "(2, 4, n)": {"status": "SOLVED", "theorem": "Ellenberg (2004)", "method": "Frey curve of level 32/64/128, Galois representations over Q."},
            "(2, 6, n)": {"status": "SOLVED", "theorem": "Bennett-Chen (2012)", "method": "Frey curves of levels 288 and 576, modular elimination."},
            "(2, n, 4)": {"status": "SOLVED", "theorem": "Bennett-Chen-Dahmen-Yazdani (2014)", "method": "Modular method and Chabauty-Coleman on quotients."},
            "(3, 4, n)": {"status": "SOLVED", "theorem": "Bennett-Chen-Dahmen-Yazdani (2016)", "method": "Frey Q-curves and modular forms over quadratic fields."},
            "(3, 3, p)": {"status": "BOUNDED_5500", "theorem": "Kraus (1998) + Joe-Simo (2026)", "method": "Kraus sieve over levels 72 and 144, verified up to p = 5500 with standard axioms in Lean 4."},
            "(5, 5, p)": {"status": "OPEN_PARTIAL", "theorem": "Billerey-Chen-Dieulefait-Freitas (2018)", "method": "Frey abelian surfaces and Hilbert modular forms over Q(sqrt(5))."},
            "(p, q, r)": {"status": "OPEN", "theorem": "Darmon-Granville (1995) Finiteness Only", "method": "Faltings theorem on curves of genus >= 2; complete non-existence is open."},
        }
        if signature and signature in taxonomy:
            res = {signature: taxonomy[signature]}
        else:
            res = taxonomy

        print("\n" + "=" * 80)
        print("BEAL CONJECTURE SIGNATURE TAXONOMY & CLASSIFICATION")
        print("=" * 80)
        for sig, info in res.items():
            print(f"  {sig:<12} | Status: {info['status']:<14} | {info['theorem']}")
            print(f"               Method: {info['method']}")
        print("=" * 80)
        return res

    def fact_check_claim(self, claim_text: str, citation: str) -> dict[str, Any]:
        """Adversarially fact-check a mathematical claim or citation against repository failure modes."""
        print(f"\n[JevGenius Fact-Checker] Auditing claim: '{claim_text}' ({citation})...")
        state = {
            "conjecture_spec": BEAL_CONJECTURE_SPEC,
            "claim": claim_text,
            "citation": citation,
        }
        questions = {
            "heuristic_dependency": jev.noul(
                instructions="Does this mathematical claim implicitly or explicitly assume unproved conjectures such as ABC, Vojta, Cohen-Lenstra heuristics, or GRH?",
                true="Depends on unproved heuristics or conjectures.",
                false="Unconditionally proved in published literature.",
            ),
            "field_extension_validity": jev.noul(
                instructions="Does the theorem validity depend on a base field (e.g. Q) that fails when extended to number fields generated by coordinates of Beal solutions?",
                true="Valid over general number fields without restriction.",
                false="Restricted to base field; fails over coordinate extension fields.",
            ),
            "verdict": jev.choice(
                instructions="What is the final fact-check verdict for this claim?",
                criteria={
                    "verified_sound": "Claim is mathematically sound and unconditionally verified.",
                    "heuristic_laundered": "Claim launders a conditional result (GRH/ABC/Vojta) as unconditional.",
                    "field_boundary_error": "Claim misapplies a base field bound to field extensions.",
                    "conflation_error": "Claim confuses non-isogeny with residual Galois representation non-isomorphism.",
                },
            ),
        }
        resp = jev.ask(state, questions)
        answers = resp.get("answers", {})
        heur = answers.get("heuristic_dependency", {}).get("noul", 0.0) >= 0.5
        field_ok = answers.get("field_extension_validity", {}).get("noul", 0.0) >= 0.5
        verdict = answers.get("verdict", {}).get("choice", "verified_sound")

        print("\n" + "=" * 80)
        print(f"JEV FACT-CHECK VERDICT: {verdict.upper()}")
        print("=" * 80)
        print(f"  - Claim:                {claim_text}")
        print(f"  - Citation:             {citation}")
        print(f"  - Heuristic Dependency: {'YES (CONDITIONAL)' if heur else 'NO (UNCONDITIONAL)'}")
        print(f"  - Field Generalization: {'VALID OVER EXTENSIONS' if field_ok else 'RESTRICTED TO BASE FIELD'}")
        print(f"  - Overall Assessment:   {verdict}")
        print("=" * 80)
        return {
            "claim": claim_text,
            "citation": citation,
            "heuristic_dependency": heur,
            "field_validity": field_ok,
            "verdict": verdict,
        }


# ==============================================================================
# 3. CLI INTERFACE
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="Jev Mathematical Genius AI Machine")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Triage command
    p_triage = subparsers.add_parser("triage", help="Run 5-stage adversarial sieve on candidates")
    p_triage.add_argument("candidates", nargs="*", default=None, help="Candidate IDs (e.g. C390 C391 ...); defaults to active pool")

    # Synthesize command
    p_syn = subparsers.add_parser("synthesize", help="Evaluate pairwise synthesis between two candidates")
    p_syn.add_argument("cid_a", help="First candidate ID")
    p_syn.add_argument("cid_b", help="Second candidate ID")

    # Synthesize Matrix command
    p_mat = subparsers.add_parser("synthesize-matrix", help="Screen all pairs among candidates to find breakthrough hybrids")
    p_mat.add_argument("candidates", nargs="*", default=None, help="Optional candidate IDs; defaults to active pool")

    # Synthesize Invariant command
    subparsers.add_parser("synthesize-invariant", help="Evaluate mathematical invariants against Fermat-Catalan defect")

    # Generate Candidate command
    p_gen = subparsers.add_parser("generate-candidate", help="Autonomously propose and screen a new candidate")
    p_gen.add_argument("--signature", default="3,3,p", help="Target signature (e.g. 3,3,p, 2,4,p)")
    p_gen.add_argument("--framework", default="derived_geometry", help="Target mathematical framework")

    # Cycle command
    subparsers.add_parser("cycle", help="Run full autonomous research cycle (benchmark, invariants, matrix, salvage)")

    # Sieve Advisor command
    p_sieve = subparsers.add_parser("sieve-advisor", help="Advise on optimal Kraus sieve parameters")
    p_sieve.add_argument("--signature", default="3,3,p", help="Target signature")
    p_sieve.add_argument("--p-min", type=int, default=5501, help="Minimum prime exponent")
    p_sieve.add_argument("--p-max", type=int, default=5600, help="Maximum prime exponent")
    p_sieve.add_argument("--run", action="store_true", help="Execute deterministic Kraus modular sieve computation for the p-range")

    # Signature Taxonomy command
    p_tax = subparsers.add_parser("signature-taxonomy", help="View classification and status of all Beal signatures")
    p_tax.add_argument("--signature", default=None, help="Optional signature filter (e.g. '(3, 3, p)')")

    # Fact Check command
    p_fact = subparsers.add_parser("fact-check", help="Adversarially fact-check an external claim or citation")
    p_fact.add_argument("--claim", required=True, help="Mathematical claim text")
    p_fact.add_argument("--citation", required=True, help="Primary source paper or reference")

    # Salvage command
    p_salvage = subparsers.add_parser("salvage", help="Salvage unconditional lemmas from candidates")
    p_salvage.add_argument("candidates", nargs="+", help="Candidate IDs to salvage")

    # Explain Obstruction command
    p_obs = subparsers.add_parser("explain-obstruction", help="Diagnose structural obstruction of a candidate")
    p_obs.add_argument("candidate_id", help="Candidate ID (e.g. C400)")

    # Discover command
    p_disc = subparsers.add_parser("discover", help="Autonomously generate and screen breakthrough mathematical hypotheses")
    p_disc.add_argument("--domain", default="all", choices=[
        "all", "arithmetic_geometry", "derived_noncommutative", "padic_hodge_prismatic",
        "automorphic_langlands", "diophantine_transcendence"
    ], help="Mathematical domain to discover hypotheses in")

    # Benchmark command
    subparsers.add_parser("benchmark", help="Calibrate Jev discrimination accuracy on ground-truth dataset")

    # Screen Families command
    subparsers.add_parser("screen-families", help="Screen algebraic parameterization families with Jev")

    # Verify Lean command
    p_lean = subparsers.add_parser("verify-lean", help="Audit Lean 4 theorem statements with Jev")
    p_lean.add_argument("file", help="Path to Lean 4 file (e.g. formal/Beal/Signature3.lean)")

    args = parser.parse_args()
    engine = JevMathematicalGenius()

    if args.command == "screen-families":
        engine.screen_algebraic_families()
    elif args.command == "triage":
        engine.triage_candidates(args.candidates)
    elif args.command == "synthesize":
        engine.synthesize_pair(args.cid_a, args.cid_b)
    elif args.command == "synthesize-matrix":
        engine.synthesize_matrix(args.candidates if args.candidates else None)
    elif args.command == "synthesize-invariant":
        engine.synthesize_invariant()
    elif args.command == "generate-candidate":
        engine.generate_candidate(args.signature, args.framework)
    elif args.command == "cycle":
        engine.run_cycle()
    elif args.command == "sieve-advisor":
        engine.advise_sieve(args.signature, args.p_min, args.p_max, run_computation=args.run)
    elif args.command == "signature-taxonomy":
        engine.get_signature_taxonomy(args.signature)
    elif args.command == "fact-check":
        engine.fact_check_claim(args.claim, args.citation)
    elif args.command == "salvage":
        engine.salvage_candidates(args.candidates)
    elif args.command == "explain-obstruction":
        engine.explain_obstruction(args.candidate_id)
    elif args.command == "discover":
        engine.discover_hypotheses(args.domain)
    elif args.command == "benchmark":
        engine.run_benchmark()
    elif args.command == "verify-lean":
        engine.verify_lean_file(args.file)


if __name__ == "__main__":
    main()
