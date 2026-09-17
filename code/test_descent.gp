default(parisize, "512M");
f = x^34 + 2*x^17 - 4;
bnf = bnfinit(f, 1);
print("Class number: ", bnf.no);
print("Class group: ", bnf.cyc);
print("Regulator: ", bnf.reg);

rel_pol = x^17 - (2*y - 2);
k_pol = y^2 - y - 1;

{
for(i=1, 17,
  u = lift(bnf.fu[i]);
  res = polresultant(rel_pol, u, x);
  res_mod = Mod(res, k_pol);
  print("u", i, " rel norm = ", res_mod);
);
}
