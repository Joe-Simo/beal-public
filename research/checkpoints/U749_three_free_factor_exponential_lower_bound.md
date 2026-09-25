# U749: The 3-free Beal factor must grow exponentially with the exponent

**Date checked:** 2026-09-24

**Status:** necessary bound in the U727 residual branch; it bounds the exponent when the 3-free factor is fixed, but supplies no uniform bound for Beal.

In U727, write the 3-free factor as $c_1=b\delta_E$, with $h=v_3(C)\ge1$, $m=3^h|b|$, and

\[
A_p m^{p-1}<|\delta_E|<B_p m^{p-1},\qquad
A_p=\frac{27^{1/(2p)}}{\sqrt{108}},\quad B_p=2pA_p.
\]

Let $K=|c_1|=|b\delta_E|$. Multiplying the interval by $|b|$ gives

\[
A_p3^{h(p-1)}|b|^p<K<B_p3^{h(p-1)}|b|^p.
\]

Since $h\ge1$ and $|b|\ge1$, every hypothetical solution must satisfy

\[
K>\phi(p):=A_p3^{p-1}=\frac{3^{p-1+3/(2p)}}{\sqrt{108}}.
\]

The function $\phi(p)$ is increasing for $p\ge2$, since the derivative of its logarithm is $\log 3\,(1-3/(2p^2))>0$. Numerically, $\phi(31)\approx2.089\times10^{13}$. Thus, if $K\le\phi(31)$, no prime exponent $p\ge31$ is possible; more generally, any fixed $K$ leaves only finitely many possible $p$.

There is a second finite restriction. If $|\delta_E|=1$, then $U_p=\pm1$, contradicting the primitive-divisor theorem for a regular Lucas pair when $p>30$. Otherwise BHV gives a primitive prime $q\mid U_p=\delta_E^p$, so $q\mid K$. U727 gives $q\equiv1$ or $-1\pmod{6p}$; hence $p\mid(q-1)/6$ or $p\mid(q+1)/6$, in particular $p\le(K+1)/6$.

These statements prove that fixing the 3-free factor bounds the exponent and that $K$ must grow at least exponentially in $p$. The Beal conjecture allows $K$ to grow with the solution, and no global upper bound for $K$ is known. This is a conditional finite-signature reduction, not a Beal proof. The exact interval and primitive-factor classes are recorded in [U727](U727_lucas_factor_order_and_delta_window.md); the BHV source is [Bilu–Hanrot–Voutier](https://doi.org/10.1515/crll.2001.080).
