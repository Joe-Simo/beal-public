# U116: The coefficient obstruction is complete — both reduction routes are closed

**Verification code**: [`code/U116_alleven_factorization_routes.py`](../../code/U116_alleven_factorization_routes.py)

U114 Part VIII closed the **Pythagorean** route to reducing the all-even Beal branch to Azon's
$(r,r,p)$ shape. This checkpoint closes the second, independent route — **direct factorisation** —
and with it the last thread this session identified as open.

---

## 1. The direct factorisation route

$$A^{2r} \;=\; C^{2t} - B^{2s} \;=\; (C^t - B^s)(C^t + B^s).$$

Let $d = \gcd(C^t - B^s,\ C^t + B^s)$. Then $d \mid 2C^t$ and $d \mid 2B^s$, and
$\gcd(B,C) = 1$ (kernel-verified as `gcd_bc_eq_one`), so $d \mid 2$.

**Case 1, $A$ odd.** $A^{2r}$ is odd, so both factors are odd and $d = 1$. Being coprime with
product a $2r$-th power, each is itself a $2r$-th power:
$$C^t - B^s = u^{2r},\quad C^t + B^s = v^{2r} \;\Longrightarrow\; 2C^t = u^{2r} + v^{2r},$$
verified symbolically for $r = 5, 7$. Coefficients $(A,B,C) = (1,1,2)$, so $AB = 1$.

**Case 2, $A$ even.** Then $B$ and $C$ are both odd (they cannot both be even, by coprimality),
both factors are even, $d = 2$, and exactly one of them is divisible by 4 — their sum is $2C^t$
with $C^t$ odd. Splitting the $2r$-th power accordingly:
$$C^t - B^s = 2u^{2r},\quad C^t + B^s = 2^{2r-1}v^{2r} \;\Longrightarrow\;
C^t = u^{2r} + 2^{2r-2}\,v^{2r},$$
verified symbolically. Coefficients $(A,B,C) = (1,\,2^{2r-2},\,1)$, so $AB = 2^{2r-2}$.

## 2. This re-derives the project's own equation, independently

For $r = 5$, Case 2 gives
$$C^t = u^{10} + 256\,v^{10},$$
which is **exactly this project's weighted equation** $X^{10} + 256Y^{10} = Z^{17}$.

Two things follow. First, the derivation above independently reproduces the reduction the project
arrived at through U42–U47, which is good evidence that both are correct. Second — and this is the
point — **the coefficient 256 is forced, not chosen**: it is $2^{2r-2}$ with $r = 5$. The project
did not pick an unlucky orientation. It picked the only one its case admits.

## 3. The obstruction is therefore complete

| route | case | coefficients | $AB$ | Hypothesis 5 |
|---|---|---|---|---|
| Pythagorean, odd leg | — | $(1,1,2)$ | $1$ | fails |
| direct factorisation | $A$ odd | $(1,1,2)$ | $1$ | fails |
| direct factorisation | $A$ even, $r=5$ | $(1,256,1)$ | $2^8$ | fails |
| direct factorisation | $A$ even, $r=7$ | $(1,4096,1)$ | $2^{12}$ | fails |
| project orientation B | — | $(1,8,1)$ | $2^3$ | fails |

**Both independent reduction routes force $AB \in \{1\} \cup \{2^k\}$.** The reason is the same in
each: the only ambiguity in splitting coprime factors of a difference of powers is the factor 2
coming from parity. No other prime can enter the coefficients, because the two factors are coprime
away from 2.

Azon's Hypothesis 5 requires a prime factor of $AB$ **not dividing $2r$**, and $2 \mid 2r$ for
every $r$. So:

$$\textbf{Hypothesis 5 fails for every }(r,r,p)\textbf{-reduction of the all-even branch reachable by either route.}$$

## 4. Status of the last open thread

C013 asked whether a reduction with suitable coefficients exists. Within these two routes,
**no**. The thread is closed, and C013 stays BLOCKED on a now-complete basis rather than a partial one.

## 5. Limits — stated precisely

- This covers the two routes by which the all-even branch is naturally reduced to the $(r,r,p)$
  shape. A reduction introducing coefficients by some *other* device is not covered, and I do not
  claim none exists.
- It says nothing about branches other than all-even, and nothing about Beal as a whole.
- The Case 2 split assumes the standard $2$-adic bookkeeping for a difference of odd powers; the
  symbolic check confirms the resulting identity but not the exhaustiveness of that bookkeeping.
- The whole argument is mine, derived from locally extracted PDF text of arXiv:2504.01967v2, and
  has not been checked by the author or a referee. **Recorded as an open obligation.**
