/* U302 — turn the Mordell-Weil sieve conditions into a SIZE bound. The sieve from tiny primes
   forces 120 | n. Canonical height grows as h(nP) = n^2 * h(P), so the smallest admissible point
   has canonical height at least 120^2 h(P). Convert that into a bound on the naive height of the
   x-coordinate, hence on the size of any solution in this branch. */
default(realprecision, 60);
{
M = ellinit([0, 6912, 0, 15925248, -4076863488]);
P = [1024, 143360];
h = ellheight(M, P);
print("canonical height of the generator P = ", P);
print("  h(P)            = ", h);
print("");
print("  sieve forces 120 | n (from p = 5,7,11,13,19,29), so any admissible n has |n| >= 120.");
print("  h(nP) = n^2 h(P), so h >= 120^2 * h(P) = ", 120^2*h);
print("");
print("  naive height of x(nP) is about 2*h(nP) for this model, so");
print("  log10 |x| is at least about ", 2*120^2*h/log(10));
print("  i.e. x has at least about ", floor(2*120^2*h/log(10)), " decimal digits.");
print("");
print("  sanity: the multiples computed exactly in U298 had these digit counts for x:");
for(n = 1, 8,
  Q = ellmul(M,P,n);
  if(Q != [0], print("    n = ", n, "   digits of numerator(x) = ", #Str(numerator(Q[1])),
                     "   n^2 h(P) = ", n^2*h)));
quit;
}
