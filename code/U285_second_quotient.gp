/* U285 — the branch needs u = a^2 and v = b^2, so z = (a^4+b^4)/(a^2 b^2) = g + 1/g with
   g = (a/b)^2 a SQUARE. Writing g = h^2 gives z = h^2 + 1/h^2 = y^2 - 2 with y = h + 1/h.
   Substituting into W^3 = q(z) gives W^3 = Y^3 + 108 Y^2 - 1152 Y + 3072 with Y = y^2.
   That is a second plane cubic — another elliptic curve. Compute its rank. */
default(parisize,"1G");
{
print("second quotient:  W^3 = Y^3 + 108 Y^2 - 1152 Y + 3072,  with Y = y^2 required a square");
E2 = ellfromeqn(w^3 - (x^3 + 108*x^2 - 1152*x + 3072));
print("  Weierstrass: ", E2);
F = ellminimalmodel(ellinit(E2));
print("  minimal model coefficients: ", F[1..5]);
print("  conductor  : ", ellglobalred(F)[1]);
print("  j-invariant: ", F.j);
print("  torsion    : ", elltors(F));
print("  analytic rank: ", ellanalyticrank(F));
print("  2-descent  : ", ellrank(F));
print("  small rational points: ", ellratpoints(F, 10000));
quit;
}
