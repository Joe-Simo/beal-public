# U17: why the forcing-prime route does not yield infinite descent

Status: verified partial result only. This does not resolve Beal's conjecture.

We continue from U16, whose only surviving structural case is

a = A^5,
b = 16*17^4*B^5,
G(a,b) = C^5,
H(a,b) = 17 D^5,

with gcd(a,b)=1. U16 found several primes q (including q=11) such that any global solution must have q | B.

The natural next question was whether one such forcing prime could be iterated p-adically to force q^2 | B, then q^3 | B, and so on, yielding infinite descent. It cannot.

## Local calculation

Fix a forcing prime q with q not in {5,17}. If q | B, then because b=16*17^4*B^5,

v_q(b) >= 5.

Since gcd(a,b)=1, q does not divide a. Write t=b/a in Z_q. Then v_q(t)>=5.

The homogeneous forms satisfy

G(a,b)/a^16 = 1 - 136 t^2 + 2380 t^4 - 12376 t^6 + 24310 t^8 - 19448 t^10 + 6188 t^12 - 680 t^14 + 17 t^16,

and

H(a,b)/(17 a^16) = 1 - 40 t^2 + 364 t^4 - 1144 t^6 + 1430 t^8 - 728 t^10 + 140 t^12 - 8 t^14 + t^16/17.

Hence both normalized quantities are congruent to 1 modulo q^10.

Because a=A^5, a^16=(A^16)^5 is already a fifth power in Z_q^*. Thus the remaining local requirement is that two principal units congruent to 1 modulo q^10 be fifth powers.

For q != 5, the map u -> u^5 is an automorphism of the principal-unit group 1+q Z_q. Equivalently, for any U congruent to 1 mod q, the polynomial f(x)=x^5-U has a simple root modulo q at x=1, because f(1)=1-U is divisible by q while f'(1)=5 is not divisible by q. Hensel's lemma therefore gives a unique q-adic fifth root in 1+q Z_q.

Consequently, once q | B has been forced, both G/a^16 and H/(17a^16) automatically satisfy the local fifth-power condition q-adically. No stronger divisibility q^2 | B follows from the same local condition, and there is no single-prime infinite descent at q.

This applies in particular to every U16 forcing prime

11,31,41,61,71,101,151,191,211,281,331,431,461,631.

Therefore route (1) proposed at the end of U16 (p-adic lifting/infinite descent at a forcing prime) is closed: the local fifth-power equations become automatically soluble on principal units after the first forced factor enters B.

## Computational note

An attempted larger Wolfram scan for further forcing primes below 20000 failed with an upstream 502 error, so no new computational coverage is claimed from that run.

## Next obligation

The remaining viable directions are global rather than single-prime local: exploit the cyclotomic factorization of G and H, seek a Thue/Thue-Mahler or superelliptic reformulation, or apply a modular method to the final Case-III branch.