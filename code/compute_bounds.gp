{
n = 34;
r1 = 2;
r2 = 16;
d = 2^32 * 5^17 * 17^34;
sqrtd = sqrt(1.0 * d);

\\ Minkowski bound
M = (factorial(n) / (n^n)) * ((4/Pi)^r2) * sqrtd;
print("Minkowski bound M_F = ", M);
print("log10(M_F) = ", log(M)/log(10));

\\ Bach bound (Bach 1990: 12 * log(d)^2 under GRH)
log_d = log(1.0 * d);
B_bach = 12 * (log_d)^2;
print("log(|disc|) = ", log_d);
print("Bach bound (12*log(disc)^2) = ", B_bach);

\\ Zimmert bound / PARI bound
\\ Let's inspect what bound PARI uses in bnfinit
f = x^34 + 2*x^17 - 4;
bnf = bnfinit(f, 1);
\\ In bnf structure, what is the bound used?
\\ Let's check bnf components
print("bnf[1] (nf) disc: ", bnf[1].disc);
print("bnf class number: ", bnf.no);
print("bnf regulator: ", bnf.reg);
}
quit;
