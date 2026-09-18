/* U283 — the palindromic involution. p(u) = u^6 p(1/u), so the genus-4 curve w^3 = p(u) has the
   involution u -> 1/u, w -> w/u^2. Setting z = u + 1/u and W = w/u gives
      W^3 = p(u)/u^3 = z^3 + 114 z^2 - 708 z + 1208,
   a PLANE CUBIC, hence a curve of GENUS 1. Compute it and its rank. */
default(parisize,"1G");
{
print("quotient curve:  W^3 = z^3 + 114*z^2 - 708*z + 1208");
print("  genus of y^3 = f(x) with deg f = 3, gcd(3,3)=3 : ((3-1)(3-1)-(3-1))/2 = 1  -> elliptic");
print("");
E = ellfromeqn(y^3 - (x^3 + 114*x^2 - 708*x + 1208));
print("  Weierstrass model from ellfromeqn: ", E);
Em = ellinit(E);
print("  minimal model : ", ellminimalmodel(Em));
Emin = ellminimalmodel(Em);
print("  conductor     : ", ellglobalred(Emin)[1]);
print("  j-invariant   : ", Emin.j);
print("  torsion       : ", elltors(Emin));
print("  analytic rank : ", ellanalyticrank(Emin));
print("  2-descent rank bound : ", ellrank(Emin));
print("");
print("  integral points (if rank 0 this is everything affine): ", ellratpoints(Emin, 10000));
quit;
}
