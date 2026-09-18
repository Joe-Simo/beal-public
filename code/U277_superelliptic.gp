/* U277 — the C147 branch as a superelliptic equation. F(u,v) = w^3 with F the sextic;
   dehomogenised it is the curve w^3 = p(u), p of degree 6 with distinct roots. */
default(parisize,"512M");
{
p = x^6 + 114*x^5 - 705*x^4 + 1436*x^3 - 705*x^2 + 114*x + 1;
print("p(x) = ", p);
print("squarefree (distinct roots)? ", poldisc(p) != 0, "   disc = ", factor(poldisc(p)));
print("number of distinct roots    = ", poldegree(p));
print("");
print("curve  w^3 = p(u):  genus by Riemann-Hurwitz for y^n = f(x), deg f = d, g = gcd(n,d):");
n = 3; d = 6; g = gcd(n,d);
print("  n = ", n, ", d = ", d, ", gcd = ", g);
print("  genus = ((n-1)(d-1) - (g-1))/2 = ", ((n-1)*(d-1) - (g-1))/2);
print("");
print("Integral points on y^3 = f(x) with f squarefree of degree >= 3 are FINITE and EFFECTIVELY");
print("bounded (Baker; LeVeque). So this branch is a finite, effective computation in principle.");
print("");
print("small integral points on w^3 = p(u), |u| <= 20000, by direct test:");
cnt = 0;
for(u = -20000, 20000,
  val = subst(p, x, u);
  if(val > 0,
     c = sqrtnint(val, 3);
     if(c^3 == val, print("   u = ", u, "  w = ", c); cnt++)));
print("  integral points found: ", cnt);
quit;
}
