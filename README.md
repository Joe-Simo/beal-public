# Beal Conjecture Research

Private working repository for a rigorous attempt to resolve the Beal conjecture.

## Status

**The Beal conjecture is not solved.** This repository contains verified partial results, failed routes, computational certificates, literature checkpoints, and open proof obligations.

## Repository structure

- `research/checkpoints/` — durable research-state snapshots and coverage records.
- `research/gaussian-descent/` — U15–U25, the Gaussian/quadratic-field descent route for the surviving `X^10 + 256Y^10 = Z^17` branch.
- `research/modular-method/` — Hilbert modular-form work, including the sigma-conjugation lemma and U26.
- `research/README.md` — current research index and conventions.

Future reproducible code should go under `code/`, formal proofs under `formal/`, and source/citation records under `references/` when those artifacts exist. Empty directories are intentionally not created.

## Mathematical target

For positive integers `A, B, C, x, y, z` satisfying

`A^x + B^y = C^z`, with `x,y,z >= 3`,

the Beal conjecture asserts that `gcd(A,B,C) > 1`.

A complete resolution requires either an unconditional proof of this full statement or an exact counterexample satisfying all hypotheses. No partial generalized-Fermat result in this repository is presented as a complete resolution.
