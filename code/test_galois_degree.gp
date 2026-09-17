{
f = x^34 + 2*x^17 - 4;
\\ Let's find primes that split completely in Q(sqrt(5), zeta_17)
\\ p = 1 mod 17, and (5/p) = 1, i.e. p = 1, 4 mod 5
\\ So p = 1 mod 85 or p = ? mod 85
\\ 1 mod 17: 103 mod 5 = 3 (no); 137 mod 5 = 2 (no); 239 mod 5 = 4 (yes, 239 = 1 mod 17, 239 = 4 mod 5)
\\ Let's test primes p = 1 mod 17 with (5/p) = 1:
forprime(p=100, 2000,
  if(p % 17 == 1 && kronecker(5, p) == 1,
    F = factormod(f, p);
    degs = vector(matsize(F)[1], i, poldegree(F[i,1]));
    degs = vecsort(degs);
    print("p=", p, " (1 mod 17, (5/p)=1): ", degs);
  );
);
quit;
}
