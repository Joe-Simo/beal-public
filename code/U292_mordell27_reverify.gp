/* U292 — discharge the C057 obligation: independent confirmation of rank 0 for Y^2 = X^3 + 27,
   by a SECOND method (analytic rank) alongside the 2-descent, plus an isomorphism cross-check. */
default(parisize,"1G");
{
E = ellinit([0,0,0,0,27]);
print("E : Y^2 = X^3 + 27");
print("  conductor      = ", ellglobalred(E)[1]);
print("  torsion        = ", elltors(E));
print("  2-descent rank = ", ellrank(E));
print("  analytic rank  = ", ellanalyticrank(E));
print("  all affine rational points up to height 10^6: ", ellratpoints(E, 1000000));
print("");
print("cross-check by isomorphism to a SECOND curve:");
F = ellinit([0,0,0,0,-432]);   /* Y^2 = X^3 - 432, the x^3+y^3=1 curve */
print("  F : Y^2 = X^3 - 432   conductor ", ellglobalred(F)[1], "  rank ", ellrank(F), "  torsion ", elltors(F));
print("  E isomorphic to F ? ", ellisisom(E,F));
G = ellinit([0,0,0,0,-27]);
print("  G : Y^2 = X^3 - 27    conductor ", ellglobalred(G)[1], "  rank ", ellrank(G), "  torsion ", elltors(G));
print("");
print("  minimal model of E: ", ellminimalmodel(E)[1..5]);
quit;
}
