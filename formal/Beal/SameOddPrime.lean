/-
# Signature `(p, p, r)`, `p` odd: the classical first factorisation step (U145)

`A^p + B^p = (A + B) · S` with `S = Σ A^i (−B)^{p−1−i}`, and `gcd(A + B, S) ∣ p`.
Consequently, for a Beal counterexample of signature `(p, p, r)`, `(A + B) · S = C^r` with the two
factors coprime unless `p` divides both. Unconditional, no external hypotheses.
-/
import Beal.Structure
import Mathlib.Algebra.GeomSum
import Mathlib.NumberTheory.Multiplicity

open Finset

namespace Beal

/-- The cofactor `S` in `A^p + B^p = (A + B) S`. -/
def cofactor (A B : ℤ) (p : ℕ) : ℤ := ∑ i ∈ range p, A ^ i * (-B) ^ (p - 1 - i)

/-- `A^p + B^p = (A + B) · S` for odd `p`. -/
theorem add_pow_eq_mul_cofactor (A B : ℤ) {p : ℕ} (hp : Odd p) :
    A ^ p + B ^ p = (A + B) * cofactor A B p := by
  have h := geom_sum₂_mul A (-B) p
  rw [hp.neg_pow] at h
  unfold cofactor
  rw [mul_comm]; linear_combination -h

/-- `S ≡ p · A^{p−1}` modulo `A + B`. -/
theorem add_dvd_cofactor_sub (A B : ℤ) (p : ℕ) :
    A + B ∣ cofactor A B p - p * A ^ (p - 1) := by
  unfold cofactor
  have : (p : ℤ) * A ^ (p - 1) = ∑ i ∈ range p, A ^ i * A ^ (p - 1 - i) := by
    rw [Finset.sum_congr rfl (fun i hi => by
      rw [← pow_add, Nat.add_sub_cancel' (Nat.le_sub_one_of_lt (Finset.mem_range.mp hi))])]
    simp
  rw [this, ← Finset.sum_sub_distrib]
  refine Finset.dvd_sum fun i _ => ?_
  rw [← mul_sub]
  refine Dvd.dvd.mul_left ?_ _
  have := sub_dvd_pow_sub_pow (-B) A (p - 1 - i)
  have e : -B - A = -(A + B) := by ring
  rw [e, neg_dvd] at this
  exact this

/-- **Key lemma.** For coprime `A, B` and any prime `p`, every common divisor of `A + B` and `S`
divides `p`. -/
theorem gcd_add_cofactor_dvd_prime {A B : ℤ} (hab : IsCoprime A B) {p : ℕ} (hp : p.Prime)
    {g : ℤ} (h1 : g ∣ A + B) (h2 : g ∣ cofactor A B p) : g ∣ (p : ℤ) := by
  have h3 : g ∣ (p : ℤ) * A ^ (p - 1) := by
    have := dvd_sub h2 (h1.trans (add_dvd_cofactor_sub A B p))
    simpa using this
  -- `g` is coprime to `A`: a common prime would divide `B = (A + B) − A`
  have hgA : IsCoprime g A := by
    have hA : IsCoprime A (A + B) := by
      have := hab.add_mul_left_right 1; rw [add_comm]; simpa using this
    exact hA.symm.of_isCoprime_of_dvd_left h1
  exact (hgA.pow_right).dvd_of_dvd_mul_right h3

/-- **Signature `(p, p, r)` structure.** In a Beal counterexample with `x = y = p` prime and
`z = r`, we have `(A + B) · S = C^r` and every common divisor of the two factors divides `p`. -/
theorem ppr_factorisation {A B C p r : ℕ} (hp : p.Prime) (hodd : Odd p)
    (h : IsBealCounterexample A B C p p r) :
    ((A : ℤ) + B) * cofactor A B p = (C : ℤ) ^ r ∧
    ∀ g : ℤ, g ∣ (A : ℤ) + B → g ∣ cofactor A B p → g ∣ (p : ℤ) := by
  have hab : Nat.Coprime A B := gcd_ab_eq_one h
  obtain ⟨_, _, _, _, _, _, _, heq⟩ := h
  refine ⟨?_, fun g h1 h2 => gcd_add_cofactor_dvd_prime (Nat.isCoprime_iff_coprime.mpr hab) hp h1 h2⟩
  rw [← add_pow_eq_mul_cofactor _ _ hodd]
  exact_mod_cast heq

end Beal

namespace Beal

/-- The cofactor over `ℕ`: `(A^p + B^p) / (A + B)`. -/
def cofactorNat (A B p : ℕ) : ℕ := (A ^ p + B ^ p) / (A + B)

theorem cofactorNat_mul {A B p : ℕ} (hodd : Odd p) (hA : 0 < A) :
    (A + B) * cofactorNat A B p = A ^ p + B ^ p := by
  unfold cofactorNat
  refine Nat.mul_div_cancel' ?_
  have h := add_pow_eq_mul_cofactor (A : ℤ) (B : ℤ) hodd
  have hd : ((A : ℤ) + B) ∣ (A : ℤ) ^ p + B ^ p := ⟨_, h⟩
  exact_mod_cast hd

theorem cofactorNat_cast {A B p : ℕ} (hodd : Odd p) (hA : 0 < A) :
    (cofactorNat A B p : ℤ) = cofactor A B p := by
  have h1 := cofactorNat_mul (A := A) (B := B) hodd hA
  have h2 := add_pow_eq_mul_cofactor (A : ℤ) (B : ℤ) hodd
  have hpos : (0 : ℤ) < (A : ℤ) + B := by positivity
  have : ((A : ℤ) + B) * (cofactorNat A B p : ℤ) = ((A : ℤ) + B) * cofactor A B p := by
    rw [← h2]; exact_mod_cast h1
  exact mul_left_cancel₀ hpos.ne' this

/-- **Coprime branch of `(p, p, r)`.** If `p ∤ A + B` then `A + B` and the cofactor are coprime and
both are `r`-th powers. -/
theorem ppr_coprime_branch {A B C p r : ℕ} (hp : p.Prime) (hodd : Odd p)
    (h : IsBealCounterexample A B C p p r) (hnd : ¬ p ∣ A + B) :
    ∃ d e : ℕ, A + B = d ^ r ∧ cofactorNat A B p = e ^ r := by
  have hab : Nat.Coprime A B := gcd_ab_eq_one h
  obtain ⟨hA, hB, hC, _, _, _, _, heq⟩ := h
  have hmul : (A + B) * cofactorNat A B p = C ^ r := by rw [cofactorNat_mul hodd hA]; exact heq
  have hcop : Nat.Coprime (A + B) (cofactorNat A B p) := by
    rw [Nat.coprime_iff_gcd_eq_one, Nat.eq_one_iff_not_exists_prime_dvd]
    rintro q hq hdvd
    have h1 : q ∣ A + B := hdvd.trans (Nat.gcd_dvd_left _ _)
    have h2 : q ∣ cofactorNat A B p := hdvd.trans (Nat.gcd_dvd_right _ _)
    have h1' : (q : ℤ) ∣ (A : ℤ) + B := by exact_mod_cast h1
    have h2' : (q : ℤ) ∣ cofactor A B p := by
      rw [← cofactorNat_cast hodd hA]; exact_mod_cast h2
    have h3 : (q : ℤ) ∣ (p : ℤ) :=
      gcd_add_cofactor_dvd_prime (Nat.isCoprime_iff_coprime.mpr hab) hp h1' h2'
    have h4 : q ∣ p := by exact_mod_cast h3
    have : q = p := (Nat.prime_dvd_prime_iff_eq hq hp).mp h4
    subst this
    exact hnd h1
  have hu : IsUnit (gcd (A + B) (cofactorNat A B p)) := by
    rw [Nat.isUnit_iff]; exact hcop
  obtain ⟨d, hd⟩ := exists_eq_pow_of_mul_eq_pow hu hmul
  have hu' : IsUnit (gcd (cofactorNat A B p) (A + B)) := by
    rw [Nat.isUnit_iff]; exact hcop.symm
  have hmul' : cofactorNat A B p * (A + B) = C ^ r := by rw [mul_comm]; exact hmul
  obtain ⟨e, he⟩ := exists_eq_pow_of_mul_eq_pow hu' hmul'
  exact ⟨d, e, hd, he⟩

end Beal

namespace Beal

/-- **p-adic branch of `(p, p, r)` (Lifting the Exponent).** If `p ∣ A + B` then
`v_p(A + B) + 1 = r · v_p(C)` and the cofactor has `v_p = 1` exactly. -/
theorem ppr_padic_branch {A B C p r : ℕ} (hp : p.Prime) (hodd : Odd p)
    (h : IsBealCounterexample A B C p p r) (hd : p ∣ A + B) :
    padicValNat p (A + B) + 1 = r * padicValNat p C ∧ padicValNat p (cofactorNat A B p) = 1 := by
  haveI := Fact.mk hp
  have hab : Nat.Coprime A B := gcd_ab_eq_one h
  obtain ⟨hA, hB, hC, _, _, _, _, heq⟩ := h
  have hpA : ¬ p ∣ A := by
    intro hpa
    have hpb : p ∣ B := (Nat.dvd_add_right hpa).mp hd
    have := Nat.dvd_gcd hpa hpb
    rw [hab] at this
    exact hp.one_lt.ne' (Nat.dvd_one.mp this)
  have hlte : padicValNat p (A ^ p + B ^ p) = padicValNat p (A + B) + padicValNat p p :=
    padicValNat.pow_add_pow hodd hd hpA hodd
  rw [padicValNat_self, heq, padicValNat.pow _ hC.ne'] at hlte
  refine ⟨hlte.symm, ?_⟩
  have hmul := cofactorNat_mul (A := A) (B := B) hodd hA
  have hS0 : cofactorNat A B p ≠ 0 := by
    intro h0; rw [h0, mul_zero] at hmul
    have : 0 < A ^ p + B ^ p := by positivity
    omega
  have hv : padicValNat p ((A + B) * cofactorNat A B p) =
      padicValNat p (A + B) + padicValNat p (cofactorNat A B p) :=
    padicValNat.mul (by omega) hS0
  rw [hmul, heq, padicValNat.pow _ hC.ne'] at hv
  omega

end Beal

namespace Beal

/-- **Dichotomy for `(p, p, r)`.** Either `p ∤ A + B` and both `A + B`, `S` are `r`-th powers, or
`p ∣ A + B` with `v_p(A + B) + 1 = r · v_p(C)` and `v_p(S) = 1`. -/
theorem ppr_dichotomy {A B C p r : ℕ} (hp : p.Prime) (hodd : Odd p)
    (h : IsBealCounterexample A B C p p r) :
    (¬ p ∣ A + B ∧ ∃ d e : ℕ, A + B = d ^ r ∧ cofactorNat A B p = e ^ r) ∨
    (p ∣ A + B ∧ padicValNat p (A + B) + 1 = r * padicValNat p C ∧
      padicValNat p (cofactorNat A B p) = 1) := by
  by_cases hd : p ∣ A + B
  · exact Or.inr ⟨hd, ppr_padic_branch hp hodd h hd⟩
  · exact Or.inl ⟨hd, ppr_coprime_branch hp hodd h hd⟩

end Beal
