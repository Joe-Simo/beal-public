\\ exponent-4 side at z=7: A^2 = u*P7(u,v), P7 = u^6-21u^4v^2+35u^2v^4-7v^6, gcd(u,P7) | 7
\\ 7 not| u: u=+-s^2, P7=+-t^2, V=v/s^2, X=V^2:  T^2 = +-(1-21X+35X^2-7X^3)
\\ 7 | u  : P7 = +-7 t^2, U=u/v, X=U^2:          +-7 T^2 = X^3-21X^2+35X-7  <=> (7T)^2 = +-7(X^3-21X^2+35X-7)
f1 = -7*x^3+35*x^2-21*x+1; f2 = -f1; f3 = 7*(x^3-21*x^2+35*x-7); f4 = -f3;
{
L=[["Ea: T^2= f(X)   (7-free,+)",f1],["Eb: T^2=-f(X)   (7-free,-)",f2],["Ec: T^2= 7g(X)  (7|u,+)",f3],["Ed: T^2=-7g(X)  (7|u,-)",f4]];
for(i=1,4,
  E=ellinit(ellfromeqn(y^2-L[i][2]));
  r=ellrank(E);
  print(L[i][1]," | cond ",ellglobalred(E)[1]," | tors ",elltors(E)[1..2]," | rank bounds ",r[1..2]," | pts on cubic model h<=200: ",hyperellratpoints(L[i][2],200)));
}
quit;
