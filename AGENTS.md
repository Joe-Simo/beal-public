# Beal Conjecture Research — Working Instructions

**Beal's conjecture is not solved.** Treat every "unconditional" / "100% closed" / "definitive"
claim in `research/checkpoints/` as unverified until audited. The root `README.md` is more
accurate than the individual checkpoints.

## HARD RULE: every research cycle STARTS with a Jev call

Not "consider using Jev" — **the first tool call of every cycle is a Jev batch.** If you are
about to read, audit, compare, or choose between more than two things, you are already late:
write the screen first. This rule exists because the loop drifted away from Jev twice and the
user had to intervene three times.

Jev decisions that are cheap and were being skipped:
- **pairwise combination** — every unordered pair of pool candidates, asking compatibility,
  combination value, and *shared failure mode* (`code/U113_combine_and_salvage.py`).
- **salvage** — the inverse of a flaw screen: which artifacts contain something genuinely proved
  and reusable even if their headline claim is withdrawn.
- **statement fidelity** — for formal files, does the statement encode the ACTUAL conjecture.
- **routing** — which candidate gets the next expensive reasoning pass.

## Use Jev aggressively — this is the main efficiency lever

Jev is almost free, fast, and limited. AI reasoning is expensive, slow, and good.
**Jev screens breadth; reasoning handles the narrow survivors.** Do not audit artifacts serially
when a screen would do.

- Before any serial pass over many artifacts (checkpoints, candidates, lemmas, citations, code),
  write a Jev screen instead: narrow questions, one request per artifact, `jev.ask_many` at
  concurrency ~12. Patterns: [`code/U113_flaw_screen.py`](code/U113_flaw_screen.py),
  [`code/U113_hypothesis_screen.py`](code/U113_hypothesis_screen.py).
- **When reasoning finds a failure mode, immediately turn it into a Jev screen** to find every
  other instance. Reasoning finds the mode; Jev finds the instances. This is how U113 went from
  two hand-audited checkpoints to a ranked list over all 144.
- Good questions are narrow and concrete — "does this use a probabilistic heuristic to rule out a
  case?" — never "is this correct?". Criteria must be concrete situations, not adjectives.
- One candidate per request; same questions across candidates; compare scores across responses.
- Every Jev result is a routing signal stored `HYPOTHESIS_ONLY`. It never sets a candidate to
  PROVED, REFUTED or VERIFIED. A hit means "read this next", not "this is wrong".
- `confidence` is distribution concentration, not correctness. On this project, action confidence
  below ~0.5 means no signal; the two known-dead routes scored 0.92–0.93.
- If Jev is unreachable, reason over the pool and continue; log the degradation.

## Files

| Path | Role |
|---|---|
| `code/jev.py` | Stdlib-only Jev client (no `requests`). Key from `$TYPESAFE_API_KEY` or gitignored `.env.local`. Never print or commit the key. |
| `code/jev_rank.py` | Standard 9-question per-candidate triage of the pool. |
| `code/pool.py` | Research population CRUD. `list` / `add` / `set` / `show`. |
| `research/pool/candidates.json` | The candidate pool. Setting REFUTED/DUPLICATE requires a `failure_reason` in the same call. |
| `research/pool/evidence/` | Raw Jev request + answers per candidate, for reconstructing the exploration tree. |

## Known recurring failure modes in this repo

Check every new claim against these three. All were found by audit in
[`U113`](research/checkpoints/U113_orbit_b_elimination_audit.md).

1. **Residual/isogeny conflation.** Refuting an isogeny, an $\ell$-adic isomorphism, or equality
   of endomorphism algebras, then concluding a *residual* mod-$p$ congruence is impossible.
   Invalid — non-isogenous abelian varieties routinely share a residual representation. If this
   inference worked, the modular method would need no elimination step at all.
2. **Chabauty over the wrong field.** A rank $<$ genus bound proved over a base field, then used
   to conclude something about solutions whose coordinates generate a larger field.
3. **Heuristic laundering.** Cohen–Lenstra/Cohen–Martinet probabilities, or GRH-conditional Bach
   bounds, used to "remove" a GRH dependency, with the result relabelled unconditional. A
   GRH-conditional result may be used *if labelled as such*; it may not be relabelled.

## Standing discipline

- Exact integer arithmetic for anything affecting validity. No floating point where exactness
  matters. Large integers as decimal strings.
- Never silently allow exponent 2, non-positive or non-integer values, exclude a base of 1,
  reorder terms, or restrict the exponent range without proving the restriction covers every case.
- Do not extend a finite search unless the new range tests a named hypothesis.
- Preserve failures with their `failure_reason` and extracted lemmas; never overwrite them.

## Fermat–Catalan blindness test (U141)

Every elementary necessary condition must be evaluated on the ten Fermat–Catalan solutions
(`code/U141_countersearch_fc.py`). Those identities have an exponent 2, so any condition that holds on
all ten is *exponent-2-blind*: it constrains the shape of a counterexample but cannot help prove Beal
on its own. 14 of the first 15 kernel conditions were blind; only |χ| ≥ 1/12 was not (and it is just
"exponents ≥ 3" restated). Do not add another blind condition to the pool without saying so.
