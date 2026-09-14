# U19: the quadratic-field unit classes collapse to one pair

Status: verified partial result only. This does not resolve Beal's conjecture.

Continue from U18. We had

P_g/sqrt(17) = eta^j * gamma^5,
P_h/sqrt(17) = eta^k * delta^5,

where eta=4+sqrt(17) is a fundamental unit and j,k are each in {0,1,2,3,4}.

U16 already proved that every global Case-III solution satisfies 101 | B. Since

b=16*17^4*B^5,

we have b == 0 (mod 101). An independent exact Wolfram residue enumeration for q=101 was rerun. It found 20 Case-III residue pairs, and every one has b==0 mod 101.

The prime 101 splits in Q(sqrt(17)), with square roots of 17 modulo 101 equal to 44 and 57. At either prime above 101, eta=4+sqrt(17) has nontrivial class modulo fifth powers. Exact checks give

for sqrt(17)=44: eta=48 and eta^20=87 mod 101,
for sqrt(17)=57: eta=61 and eta^20=36 mod 101.

Since neither value is 1, eta is not a fifth power modulo either prime above 101. Its image therefore generates the order-5 quotient of F_101^* by fifth powers.

Now reduce the U18 equations modulo a prime above 101. Because b==0,

P_g/sqrt(17) == -(4+sqrt(17))*a^8 = -eta*a^8,

and

P_h/sqrt(17) == (4-sqrt(17))*a^8 = -eta^(-1)*a^8.

But a=A^5, so a^8=(A^8)^5 is already a fifth power. Also -1=(-1)^5 is a fifth power. Hence

eta^(1-j) must be a fifth power,
eta^(-1-k) must be a fifth power.

Because eta has exact nontrivial order 5 in the quotient modulo fifth powers, this forces

j == 1 (mod 5),
k == -1 == 4 (mod 5).

Thus all 25 possible unit-class pairs collapse to the single pair

P_g/sqrt(17) = eta * gamma^5,
P_h/sqrt(17) = eta^4 * delta^5.

This is a strict global strengthening of U18.

A convenient simplification of the first equation is

(P_g/sqrt(17))/eta = gamma^5,

whose left side expands exactly to

-a^8 + 4(17+3sqrt(17))a^6b^2 - 2(51+2sqrt(17))a^4b^4 + 4(17-3sqrt(17))a^2b^6 + (-17+4sqrt(17))b^8.

The second equation can similarly be normalized by eta^4.

Next obligation: write gamma and delta in the integral basis of O_K, expand their fifth powers, and compare the sqrt(17)-coefficients. Because the unit ambiguity is now gone, this produces fixed Diophantine systems rather than a family of unit twists.