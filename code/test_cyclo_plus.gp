default(parisize, "1024M");
default(realprecision, 19);

poly_plus(p) = {
  my(x='x, y='y, P=polcyclo(p, x));
  my(R = polresultant(P, x^2 - y*x + 1, x));
  my(F = factor(R));
  return(subst(F[1, 1], y, x));
};

{
forprime(p=3, 43,
  pol = poly_plus(p);
  t0 = gettime();
  bnf = bnfinit(pol, 1);
  t = gettime() - t0;
  print(Strprintf("p=%2d, deg=%2d: h^+=%d, cyc=%s, reg=%g (time=%d ms)", 
        p, poldegree(pol), bnf.no, Str(bnf.cyc), 1.0*bnf.reg, t));
);
}
quit;
