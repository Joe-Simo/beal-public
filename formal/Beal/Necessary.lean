/-
# Necessary conditions on a Beal counterexample — consolidated and kernel-verified

Everything this project has verified about a *hypothetical* counterexample, assembled into one
theorem.  This is the "explicit account of what is proved" in machine-checked form.

No `sorry`, no custom axioms: every component depends only on
`[propext, Classical.choice, Quot.sound]`.
-/
import Beal.Structure
import Beal.Mihailescu
import Beal.Radical

namespace Beal

/-- **Consolidated necessary conditions.**
If `(A,B,C,x,y,z)` is a Beal counterexample then all of the following hold.  Any search for a
counterexample may assume them; any claimed counterexample violating one is refuted outright. -/
theorem necessary_conditions {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    -- the three bases are pairwise coprime
    Nat.gcd A B = 1 ∧ Nat.gcd A C = 1 ∧ Nat.gcd B C = 1 ∧
    -- the first two bases are distinct
    A ≠ B ∧
    -- the exponents are not all divisible by 3
    ¬ (3 ∣ x ∧ 3 ∣ y ∧ 3 ∣ z) ∧
    -- x and y are not both divisible by 4 with z even
    ¬ (4 ∣ x ∧ 4 ∣ y ∧ 2 ∣ z) ∧
    -- 3 and 4 do not divide the gcd of the exponents
    ¬ (3 ∣ Nat.gcd x (Nat.gcd y z)) ∧ ¬ (4 ∣ Nat.gcd x (Nat.gcd y z)) := by
  refine ⟨gcd_ab_eq_one h, gcd_ac_eq_one h, gcd_bc_eq_one h, ?_, ?_, ?_, ?_, ?_⟩
  · rintro rfl
    exact not_eq_bases h
  · rintro ⟨h3x, h3y, h3z⟩
    exact no_counterexample_of_three_dvd_all h3x h3y h3z h
  · rintro ⟨h4x, h4y, h2z⟩
    exact no_counterexample_of_four_four_even h4x h4y h2z h
  · intro hd
    exact no_counterexample_of_three_or_four_dvd_gcd (Or.inl hd) h
  · intro hd
    exact no_counterexample_of_three_or_four_dvd_gcd (Or.inr hd) h

/-- **The exponent reduction is available alongside the necessary conditions.**
If a counterexample exists at all, one exists with every exponent in `{4} ∪ {odd primes}`
*and* satisfying all the necessary conditions above. -/
theorem reduced_counterexample_satisfies_necessary
    {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    ∃ A' B' C' x' y' z' : ℕ,
      IsBealCounterexample A' B' C' x' y' z' ∧
      Reduced x' ∧ Reduced y' ∧ Reduced z' ∧
      Nat.gcd A' B' = 1 ∧ Nat.gcd A' C' = 1 ∧ Nat.gcd B' C' = 1 ∧ A' ≠ B' := by
  obtain ⟨A', B', C', x', y', z', hce, hx, hy, hz⟩ := reduction h
  obtain ⟨g1, g2, g3, hne, _, _, _, _⟩ := necessary_conditions hce
  exact ⟨A', B', C', x', y', z', hce, hx, hy, hz, g1, g2, g3, hne⟩



/-! ## Tier 2: conditions that require an external theorem

The conditions above are unconditional. The one below additionally needs Mihailescu's theorem
(Catalan), which mathlib does not contain and which this project carries as the clearly-labelled
named hypothesis `MihailescuTheorem`. It is stated separately so that the hypothesis list
distinguishes the two tiers: a reader can see exactly which constraints are free and which are
bought. No Lean `axiom` is used.
-/

section Tier2
open Beal

/-- **Necessary conditions, including those bought with an external theorem.**
Everything in `necessary_conditions`, plus: all three bases are at least 2 — i.e. no base equals
1 — which follows from Mihailescu's theorem via `beal_counterexample_bases_ge_two`.

This theorem takes `MihailescuTheorem` as an explicit hypothesis; `necessary_conditions` does
not. That difference is the point, and `#print axioms` on both reports only the standard
`[propext, Classical.choice, Quot.sound]`. -/
theorem necessary_conditions_with_catalan (hM : MihailescuTheorem) {A B C x y z : ℕ}
    (h : IsBealCounterexample A B C x y z) :
    (Nat.gcd A B = 1 ∧ Nat.gcd A C = 1 ∧ Nat.gcd B C = 1 ∧ A ≠ B) ∧
    (2 ≤ A ∧ 2 ≤ B ∧ 2 ≤ C) := by
  obtain ⟨g1, g2, g3, hne, _, _, _, _⟩ := necessary_conditions h
  exact ⟨⟨g1, g2, g3, hne⟩, beal_counterexample_bases_ge_two hM A B C x y z h⟩

end Tier2



/-! ## Where the ordering of `ℤ` enters: no cancellation

Beal is **false** over `ℤ[i]` (see `Beal/GaussianObstruction.lean`), and `ℤ[i]` is a PID.  So no
proof can rest on unique factorisation; something special to `ℤ` is needed.  This section isolates
what: **positivity forbids cancellation**, which pins `C^z` into a dyadic window around the larger
of the two summands.  Over `ℤ[i]` the analogous statement fails badly — the Helenius identity has
summands of norm `125` each and a sum of norm `16`.
-/

section NoCancellation

/-- **No cancellation.**  In any Beal counterexample, `C^z` strictly exceeds each summand and is
at most twice the larger one.

The upper bound is `≤`, not `<`: if `A^x = B^y` then `C^z = 2 B^y` exactly.  (That case cannot
actually occur — coprimality forces `A = B = 1`, excluded by `not_eq_bases` — but the inequality
above is the one that holds without invoking it.) -/
theorem no_cancellation {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    A ^ x < C ^ z ∧ B ^ y < C ^ z ∧ C ^ z ≤ 2 * max (A ^ x) (B ^ y) := by
  obtain ⟨hA, hB, hC, hx, hy, hz, _, heq⟩ := h
  have hAx : 0 < A ^ x := Nat.pos_pow_of_pos _ hA
  have hBy : 0 < B ^ y := Nat.pos_pow_of_pos _ hB
  refine ⟨?_, ?_, ?_⟩
  · rw [← heq]; exact Nat.lt_add_of_pos_right hBy
  · rw [← heq]; exact Nat.lt_add_of_pos_left hAx
  · rw [← heq, two_mul]
    exact Nat.add_le_add (le_max_left _ _) (le_max_right _ _)

/-- The same bound, with the larger summand named: `B^y < C^z ≤ 2 B^y`.
A proof of Beal cannot be purely formal — an argument that never compares sizes would apply
verbatim over `ℤ[i]`, where the statement is **false**.  This is the kind of step that has no
analogue there. -/
theorem no_cancellation_of_le {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z)
    (hle : A ^ x ≤ B ^ y) : B ^ y < C ^ z ∧ C ^ z ≤ 2 * B ^ y := by
  obtain ⟨h1, h2, h3⟩ := no_cancellation h
  rw [max_eq_right hle] at h3
  exact ⟨h2, h3⟩

end NoCancellation

end Beal

/-! ## Tier 0+: the full unconditional account (U234, pool C099)

`necessary_conditions` above is the *coprimality and exponent-divisibility* tier.  This section
adds every other unconditional, machine-checked constraint the project has, so that a single
theorem is the explicit account of what is proved about an arbitrary counterexample.

Each entry is tagged with the two gates:
* **G1** = fails on at least one of the ten exponent-2 Fermat–Catalan solutions;
* **G2** = its proof uses the equation `A^x + B^y = C^z`.

| constraint | G1 | G2 |
|---|---|---|
| pairwise coprimality, `A ≠ B`, exponent divisibility | no | yes |
| `C^z > max(A^x,B^y)` and `C^z < 2·max(A^x,B^y)` | no | yes |
| `rad(ABC)^3 ≤ A^x B^y C^z` | **yes** | no |
| `rad(ABC)^(xyz) ≤ (C^z)^(yz+xz+xy)` | no | no |
| `d ∣ C → d^z ∣ A^x + B^y` | no | **yes** |

No single known constraint passes both gates and lies outside a survey-dead category.  That is the
honest summary of the unconditional position. -/

namespace Beal
section FullAccount

/-- **The complete unconditional account.**  Everything this project proves, without hypotheses,
about an arbitrary Beal counterexample, in one statement. -/
theorem full_unconditional_account {A B C x y z : ℕ} (h : IsBealCounterexample A B C x y z) :
    -- tier 1: coprimality and exponent divisibility
    (Nat.gcd A B = 1 ∧ Nat.gcd A C = 1 ∧ Nat.gcd B C = 1 ∧ A ≠ B) ∧
    (¬ (3 ∣ x ∧ 3 ∣ y ∧ 3 ∣ z) ∧ ¬ (4 ∣ x ∧ 4 ∣ y ∧ 2 ∣ z)) ∧
    -- tier 2: the archimedean window (positivity forbids cancellation)
    (A ^ x < C ^ z ∧ B ^ y < C ^ z) ∧
    -- tier 3: radical bounds
    ((rad (A * B * C)) ^ 3 ≤ A ^ x * B ^ y * C ^ z ∧
     (rad (A * B * C)) ^ (x * y * z) ≤ (C ^ z) ^ (y * z + x * z + x * y)) ∧
    -- tier 4: every divisor of C contributes its z-th power to the sum
    (∀ d : ℕ, d ∣ C → d ^ z ∣ A ^ x + B ^ y) := by
  obtain ⟨g1, g2, g3, hne, h3, h4, -, -⟩ := necessary_conditions h
  refine ⟨⟨g1, g2, g3, hne⟩, ⟨h3, h4⟩, ?_, ⟨radical_cube_le h, radical_pow_le h⟩,
    fun d hd => pow_dvd_add_of_dvd_C h hd⟩
  obtain ⟨hA, hB, -, -, -, -, -, heq⟩ := h
  have ha : 1 ≤ A ^ x := Nat.one_le_pow _ _ hA
  have hb : 1 ≤ B ^ y := Nat.one_le_pow _ _ hB
  omega

end FullAccount

end Beal
