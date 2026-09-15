# Beal Conjecture Research

Private working repository for a rigorous attempt to resolve the Beal conjecture.

## Status

**The Beal conjecture is not solved.** This repository contains partial arguments, failed routes, computational certificates, literature checkpoints, and open proof obligations; historical “verified” labels are not independent certification.

**Latest checkpoint: [U60 — audit and modulo-289 reduction](research/checkpoints/U60_audit_and_mod289_reduction.md).**

U60 corrects the invalid square-residue normalization in U57/U58, recovers U57's 103-divisibility conclusion with a complete residue check, and corrects U59's projective-kernel and q^2-precision statements. Do not reuse U58's restricted root lists as complete pruning rules.

A new algebraic certificate eliminates B=-b^2 in the explicitly stated auxiliary simultaneous system, leaving B=-17b^2 with 17|b. Compatible local solutions persist at all powers of the five primes examined. The next global target is the explicit genus-three quotient in U60; no rational-point classification or complete Beal solution is claimed.

## Repository structure

- `research/checkpoints/` — durable research-state snapshots and coverage records.
- `research/gaussian-descent/` — U15–U25, the Gaussian/quadratic-field descent route for the surviving `X^10 + 256Y^10 = Z^17` branch.
- `research/modular-method/` — Hilbert modular-form work, including the sigma-conjugation lemma and U26.
- `research/README.md` — historical research index and conventions; read the latest checkpoint above first.
- `code/U60_audit.ts` and `code/U60_symbolic.py` — executable exact checks.
- `research/computations/U60_*` — full outputs, Wolfram expressions and verification records.

Formal proofs should go under `formal/` and source records under `references/` when those artifacts exist. Empty directories are intentionally not created.

## Mathematical target

For positive integers `A, B, C, x, y, z` satisfying

`A^x + B^y = C^z`, with `x,y,z >= 3`,

the Beal conjecture asserts that `gcd(A,B,C) > 1`.

A complete resolution requires either an unconditional proof of this full statement or an exact counterexample satisfying all hypotheses. No partial generalized-Fermat result in this repository is presented as a complete resolution.
