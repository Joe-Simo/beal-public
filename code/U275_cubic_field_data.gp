/* U275 — arithmetic data for the fields of C146: the pure cubic Q(3^(1/3)) and the sextic
   defined by p(X) = X^6+114X^5-705X^4+1436X^3-705X^2+114X+1, plus the cubic resolvent. */
default(parisize,"512M");
{
print("== pure cubic field Q(3^(1/3)) ==");
K = bnfinit(x^3 - 3, 1);
print("  disc          = ", K.disc);
print("  class number  = ", K.no);
print("  units rank    = ", #K.fu);
print("  fundamental u = ", K.fu);
print("  regulator     = ", K.reg);
print("");
print("== cubic resolvent  Z^3 + 114 Z^2 - 708 Z + 1208 ==");
R = bnfinit(x^3 + 114*x^2 - 708*x + 1208, 1);
print("  disc          = ", R.disc);
print("  class number  = ", R.no);
print("  units rank    = ", #R.fu);
print("  isomorphic to Q(3^(1/3))? ", nfisisom(K, R) != 0);
print("");
print("== sextic  X^6+114X^5-705X^4+1436X^3-705X^2+114X+1 ==");
S = nfinit(x^6 + 114*x^5 - 705*x^4 + 1436*x^3 - 705*x^2 + 114*x + 1);
print("  disc          = ", S.disc);
print("  signature     = ", S.sign);
print("  Galois group  = ", polgalois(x^6 + 114*x^5 - 705*x^4 + 1436*x^3 - 705*x^2 + 114*x + 1));
print("");
print("== Thue feasibility ==");
T = thueinit(x^6 + 114*x^5 - 705*x^4 + 1436*x^3 - 705*x^2 + 114*x + 1, 1);
print("  thueinit succeeded; W(a,b) = 1 solutions: ", thue(T, 1));
print("  W(a,b) = 8  solutions: ", thue(T, 8));
print("  W(a,b) = 27 solutions: ", thue(T, 27));
print("  W(a,b) = 64 solutions: ", thue(T, 64));
quit;
}
