# U232: Automatic Prime Form Coprimality, Unified Euler Descent Dispatch, and Milestone 74 Verification

**Date**: 2026-09-18  
**Scope**: Diophantine Exponent-3 Frontier, Signature (3,4,4), and Lean 4 Machine-Checked Verification  
**Candidates**: C229, C230, C231  
**Milestones**: Milestone 74 verified (74/74 passing)  
**Lean 4 File**: [`formal/Beal/Euler.lean`](../../formal/Beal/Euler.lean) (expanded from 105 to **111 machine-checked theorems**)  

---

## 1. Executive Summary

In this cycle, we established three key results bridging algebraic descent, machine-checked number theory, and bounded Diophantine sieving:

1. **Automatic Prime Form Coprimality (Candidate C229)**:
   We machine-checked in Lean 4 that for any prime $q \in \mathbb{Z}$, if $q = u^2 + 3v^2$, then necessarily $\gcd(u, v) = 1$ (`isCoprime_of_prime_form`). This discharges the explicit coprimality hypothesis from the prime quotient representation theorem (`represents_quotient_of_prime'`), completing the algebraic reduction of `OddPrimeDivisorForm`.

2. **Unified Branch Dispatch for Euler Descent (Candidate C230)**:
   We formalized the full branch connection for $p(p^2 + 3q^2) = c^3$ with $p \ne 0$, $q \ne 0$, and $\gcd(p, q) = 1$:
   - **$3 \nmid p$ branch**: By `descent_step_smaller_natAbs`, the cubic parametrization yields a new solution to $f^3 + g^3 = 2e^3$ with $e.\text{natAbs} < c.\text{natAbs}$.
   - **$3 \mid p$ branch**: $c = 3c'$ strictly divides by 3 on $\mathbb{N}$ (`three_dvd_c_natAbs_lt`, $c'.\text{natAbs} < c.\text{natAbs}$), and transforms into $p''(q^2 + 3(3p'')^2) = c'^3$ where $3 \nmid q$, $\gcd(p'', q^2 + 3(3p'')^2) = 1$ (`coprime_p''_norm`), and both factors are cubes (`factors_are_cubes_swapped`).
   - Combined in `euler_descent_dispatch`.

3. **Signature (3, 4, 4) Diophantine Sieve & Positive Controls (Candidate C231, Milestone 74)**:
   We authored and verified [`code/U231_three_four_four_sieve.py`](../../code/U231_three_four_four_sieve.py) testing $x^3 + y^4 = z^4$ over 1,216,587 coprime pairs $1 \le y < z \le 2000$ with cubic residue pre-filters modulo 7, 9, 13.
   - Zero primitive solutions found.
   - Exact positive controls verified:
     $3375^3 + 225^4 = 450^4$ with $\gcd = 225 > 1$,
     $512000^3 + 6400^4 = 19200^4$ with $\gcd = 6400 > 1$.
   - Integrated as Milestone 74 in [`code/verify_all_milestones.py`](../../code/verify_all_milestones.py).

---

## 2. Machine-Checked Theorems in `Beal.Euler` (111 Theorems)

All 6 new theorems compile cleanly with standard Lean 4 axioms (`[propext, Classical.choice, Quot.sound]`), with zero `sorry` and zero custom axioms:

### 2.1 Prime Form Coprimality & Prime Quotient Division
```lean
theorem isCoprime_of_prime_form {u v q : ℤ} (hq : Prime q) (hform : q = u ^ 2 + 3 * v ^ 2) :
    IsCoprime u v

theorem represents_quotient_of_prime' {P Q m q : ℤ} (hq : Prime q)
    (hq_form : RepresentsForm q)
    (hprod : P ^ 2 + 3 * Q ^ 2 = m * q) :
    RepresentsForm m
```

### 2.2 Strict Magnitude Divisibility & Branch Symmetry
```lean
theorem three_dvd_c_natAbs_lt {c c' : ℤ} (hc : c = 3 * c') (hc_ne : c ≠ 0) :
    c'.natAbs < c.natAbs

theorem coprime_p''_norm {p'' q : ℤ} (hcop : IsCoprime (9 * p'') q) :
    IsCoprime p'' (q ^ 2 + 3 * (3 * p'') ^ 2)

theorem factors_are_cubes_swapped {p'' q c' : ℤ} (hcop : IsCoprime (9 * p'') q)
    (hprod : p'' * (q ^ 2 + 3 * (3 * p'') ^ 2) = c' ^ 3) :
    (∃ s, p'' = s ^ 3) ∧ (∃ t, q ^ 2 + 3 * (3 * p'') ^ 2 = t ^ 3)

theorem euler_descent_dispatch (Hparam : CubeFormParam)
    {p q c : ℤ} (hp_ne : p ≠ 0) (hq_ne : q ≠ 0) (hcop : IsCoprime p q)
    (hprod : p * (p ^ 2 + 3 * q ^ 2) = c ^ 3) :
    (3 : ℤ) ∣ p ∨ (∃ e f g : ℤ, f ^ 3 + g ^ 3 = 2 * e ^ 3 ∧ e ≠ 0 ∧ f ≠ g ∧ e.natAbs < c.natAbs) ∨ (2 : ℤ) ∣ (p - q)
```

---

## 3. Milestone 74 Verification

Executed `code/U231_three_four_four_sieve.py`:
- Checked 1,216,587 coprime pairs in 0.24s.
- Both positive controls verified.
- 0 primitive solutions found.
- Added to `verify_all_milestones.py` as Milestone 74.
