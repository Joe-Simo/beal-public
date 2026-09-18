/* U278 — the general homogeneous case F(u,v) = w^3 (C148 gap (i)). Standard descent: in
   K = Q[x]/(p(x)), the ideal (u - theta*v) is a cube times an ideal supported on the
   discriminant, so with the class number and units in hand the equation splits into finitely
   many Thue-type equations over K. Compute that data. */
default(parisize,"2G");
{
p = x^6 + 114*x^5 - 705*x^4 + 1436*x^3 - 705*x^2 + 114*x + 1;
print("sextic p(x) = ", p);
K = bnfinit(p, 1);
print("  field discriminant = ", K.disc, "   factored: ", factor(K.disc));
print("  class number h     = ", K.no);
print("  class group        = ", K.cyc);
print("  signature          = ", K.sign);
print("  unit rank          = ", #K.fu);
print("  regulator          = ", K.reg);
print("");
print("  h mod 3 = ", K.no % 3, "   (if 3 does not divide h, the cube-of-an-ideal step is clean)");
print("");
print("  torsion units      = ", K.tu);
print("  fundamental units  = ", K.fu);
quit;
}
