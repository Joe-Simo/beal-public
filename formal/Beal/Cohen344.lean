/-
# `(3,4,4)` from Euler instead of from a citation (U316, pool C173)

`ClosedFamilies.lean` carries the hypothesis `cohen344 : NoCoprimeSol 3 4 4`, sourced to
Cohen, *Number Theory Volume II* (GTM 240), Prop. 14.6.6.  That book is not held in
`references/`, so the hypothesis was unauditable at $0 — the only such hypothesis of
`final_residual`.

This file removes the citation.  `cohen344_of_euler` derives `NoCoprimeSol 3 4 4` from a single
named classical theorem, **Euler's** `a³ + b³ = 2c³`, by splitting on the parity of `b` and `c`
(they cannot both be even, being coprime):

* `b, c` both odd — closed **outright**, no hypothesis: `three_four_four_same_parity`.
* opposite parity — `opposite_parity_reduction` turns the branch into Euler's equation, and
  `a = b` there forces `C − B = C + B`, hence `B = 0`, excluded.

`EulerCubicTwo` is stated, **not proved**.  It is not in mathlib (`Mathlib/NumberTheory/FLT/`
contains only `Basic`, `Four`, `MasonStothers`, `Three`, and a grep for the statement finds
nothing), and this project has not formalised it.  So this is an **audit improvement, not a new
theorem**: an unverifiable book reference becomes a named 1770 result plus a machine-checked
derivation, with the one remaining gap explicit in the type.

No `sorry`, no custom `axiom`s; mathlib only.
-/
import Beal.ThreeFourFour
import Beal.ClosedFamilies
namespace Beal

/-- **Euler's theorem on `a³ + b³ = 2c³`** (Euler, *Vollständige Anleitung zur Algebra*, 1770;
see also Dickson, *History of the Theory of Numbers* II, ch. XXI).  Stated, not proved: it is not
in mathlib, and this project has not formalised it.  Every use is flagged. -/
def EulerCubicTwo : Prop :=
  ∀ a b c : ℕ, 0 < a → 0 < b → 0 < c → Nat.Coprime a b → a ^ 3 + b ^ 3 = 2 * c ^ 3 → a = b

/-- `(3,4,4)` has no coprime solution, **given** Euler's theorem.  This replaces the unauditable
citation `cohen344` (Cohen, GTM 240, Prop. 14.6.6) by a named classical theorem plus a
machine-checked derivation: the same-parity branch is proved outright here, and the
opposite-parity branch is reduced to Euler. -/
theorem cohen344_of_euler (hE : EulerCubicTwo) : NoCoprimeSol 3 4 4 := by
  intro a b c ha hb hc hab heq
  -- b and c are coprime
  have hbc : Nat.Coprime b c := by
    rw [Nat.coprime_iff_gcd_eq_one, Nat.eq_one_iff_not_exists_prime_dvd]
    rintro p hp hdvd
    have hpb : p ∣ b := hdvd.trans (Nat.gcd_dvd_left b c)
    have hpc : p ∣ c := hdvd.trans (Nat.gcd_dvd_right b c)
    have hpa : p ∣ a := by
      refine hp.dvd_of_dvd_pow (n := 3) ?_
      have : a ^ 3 = c ^ 4 - b ^ 4 := by omega
      rw [this]
      exact Nat.dvd_sub' (dvd_pow hpc (by norm_num)) (dvd_pow hpb (by norm_num))
    have : p ∣ Nat.gcd a b := Nat.dvd_gcd hpa hpb
    rw [hab] at this
    exact hp.one_lt.ne' (Nat.dvd_one.mp this)
  -- b < c
  have hlt : b < c := by
    by_contra hcon
    have : c ^ 4 ≤ b ^ 4 := Nat.pow_le_pow_left (by omega) 4
    have : 0 < a ^ 3 := Nat.pos_pow_of_pos 3 ha
    omega
  rcases Nat.even_or_odd b with hbe | hbo
  · -- b even, so c is odd (coprime), opposite parity
    have hco : Odd c := by
      rcases Nat.even_or_odd c with hce | hco
      · exfalso
        obtain ⟨k, hk⟩ := hbe; obtain ⟨l, hl⟩ := hce
        have : 2 ∣ Nat.gcd b c := Nat.dvd_gcd ⟨k, by omega⟩ ⟨l, by omega⟩
        rw [hbc] at this; omega
      · exact hco
    obtain ⟨m, n, r, hm, hn, hr, hmn, hu, hv, hcube⟩ :=
      opposite_parity_reduction ha hb hlt hbc (Or.inr ⟨hbe, hco⟩) heq
    have hmn2 : Nat.Coprime (m ^ 2) (n ^ 2) := Nat.Coprime.pow _ _ hmn
    have := hE (m ^ 2) (n ^ 2) r (by positivity) (by positivity) hr hmn2 hcube
    have hmn' : m = n := by nlinarith [this]
    rw [hmn'] at hu
    omega
  · rcases Nat.even_or_odd c with hce | hco
    · -- b odd, c even: opposite parity again
      obtain ⟨m, n, r, hm, hn, hr, hmn, hu, hv, hcube⟩ :=
        opposite_parity_reduction ha hb hlt hbc (Or.inl ⟨hbo, hce⟩) heq
      have hmn2 : Nat.Coprime (m ^ 2) (n ^ 2) := Nat.Coprime.pow _ _ hmn
      have := hE (m ^ 2) (n ^ 2) r (by positivity) (by positivity) hr hmn2 hcube
      have hmn' : m = n := by nlinarith [this]
      rw [hmn'] at hu
      omega
    · -- both odd: closed unconditionally
      exact three_four_four_same_parity ha hbo hco hlt hbc heq

/-- Assembling `InstanceRows` with the `cohen344` field supplied by `cohen344_of_euler` instead of
by Cohen's book.  The other three fields are unchanged and still cited; this records exactly which
one of the four the audit has improved. -/
theorem instanceRows_of_euler (hE : EulerCubicTwo)
    (hpss : NoCoprimeSol 3 4 7 ∧ NoCoprimeSol 3 7 4 ∧ NoCoprimeSol 4 7 3)
    (hss : NoCoprimeSol 3 4 5 ∧ NoCoprimeSol 3 5 4 ∧ NoCoprimeSol 4 5 3)
    (hp44 : ∀ p, 5 ≤ p → NoCoprimeSol p 4 4) : InstanceRows :=
  { pss347 := hpss, ss345 := hss, cohen344 := cohen344_of_euler hE, p44 := hp44 }

end Beal
