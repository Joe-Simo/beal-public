f1 = -7*x^3+35*x^2-21*x+1; g = x^3-21*x^2+35*x-7;
{
L=[["A+ second quotient  y^2 =  g(x)   (x=1/V^2)", g],["A- second quotient  y^2 = -g(x)", -g],["D- second quotient  y^2 = -7 f1(x) (x=1/U^2)", -7*f1],["C+ second quotient  y^2 =  7 f1(x)", 7*f1]];
for(i=1,4,
  E=ellinit(ellfromeqn(y^2-L[i][2])); r=ellrank(E);
  print(L[i][1]," | cond ",ellglobalred(E)[1]," | tors ",elltors(E)[1..2]," | rank ",r[1..2]," | pts h<=300: ",hyperellratpoints(L[i][2],300)));
}
quit;
