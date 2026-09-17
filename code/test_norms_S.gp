default(parisize, "512M");
f = x^34 + 2*x^17 - 4;
bnf = bnfinit(f, 1);
rel_pol = x^17 - (2*y - 2);
k_pol = y^2 - y - 1;

h_poly = sum(j=0, 16, (-1)^j * x^(16-j));
pr17 = idealprimedec(bnf.nf, 17);
g17_gen = bnfisprincipal(bnf, pr17[1])[2];
g17_poly = lift(g17_gen);

elements = [x, x+1, h_poly, g17_poly];
names = ["s", "s+1", "h(s)", "g17"];

{
for(i=1, #elements,
  res = polresultant(rel_pol, elements[i], x);
  res_mod = Mod(res, k_pol);
  print(names[i], " norm = ", res_mod);
);
}
