{
f = x^34 + 2*x^17 - 4;
c = 0;
forprime(p=3, 500,
  if(p==5 || p==17, next);
  F = factormod(f, p);
  degs = vector(matsize(F)[1], i, poldegree(F[i,1]));
  degs = vecsort(degs);
  print("p=", p, " (mod 85=", p%85, "): ", degs);
  c++;
  if(c > 20, break);
);
quit;
}
