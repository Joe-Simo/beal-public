(* Executed independently through WolframLanguageEvaluator, 2026-09-15.
   First call deliberately records toric-only Y=1 residues. *)
Module[{z,r,a,v,x,h,cyc,phi,norm,c,rows,mm,pp,units,logs,comb},
 cyc=1+z+z^2+z^3+z^4; phi=1+z+z^4;
 h=r^4+a*r^3+a^2*r^2+a^3*r+a^4;
 norm=Factor[Resultant[h,v*(r^3-a^3),r]];
 rows=Table[With[{q=data[[1]],p=data[[2]],xx=data[[3]],yy=data[[4]]},
 {q,PrimeQ[q],Mod[p^2-p-1,q],
 PowerMod[Mod[5*PowerMod[32,-1,q],q],(q-1)/17,q],PowerMod[p,(q-1)/17,q],
 Mod[PowerMod[xx,10,q]+256*PowerMod[yy,10,q],q],
 PowerMod[Mod[2*PowerMod[xx,5,q],q],(q-1)/17,q]}],
 {data,{{2381,1774,33,1},{17681,1932,788,1},{610301,412274,2504,1}}}];
 mm[u_,w_]:=Mod[Table[Sum[If[i+j==k,u[[i+1]]w[[j+1]],
 If[i+j==k+5,2u[[i+1]]w[[j+1]],0]],{i,0,4},{j,0,4}],{k,0,4}],289];
 pp[u_,e_]:=Module[{base=u,exp=e,out={1,0,0,0,0}},
 While[exp>0,If[OddQ[exp],out=mm[out,base]];
 base=mm[base,base];exp=Quotient[exp,2]];out];
 units={{-1,1,0,0,0},{1,1,0,1,0}};
 logs=Table[Mod[pp[u,17^4-1]-{1,0,0,0,0},289]/17,{u,units}];
 c=Mod[5*PowerMod[32,-1,289],289];
 <|"quartic_norm"->norm,
 "unit_polynomial_remainder"->PolynomialRemainder[phi^2-phi-1,cyc,z],
 "unit_root_formula_remainder"->PolynomialRemainder[(-z)^17*(1+z)-phi,cyc,z],
 "cyclotomic_product"->PolynomialRemainder[Product[1-z^j,{j,1,4}],cyc,z],
 "rational_root_identity"->Cancel[x^17*(5x^8)/(2x^5)^5],
 "quintic_unit_logs"->logs,
 "named_rows_q_prime_phi_poly_c_char_phi_char_toric_gaussian"->rows,
 "c_mod289_and_sixteenth_power"->{c,PowerMod[c,16,289]},
 "field_degree_arithmetic"->{2*16,17^2,2*16*17^2,GCD[17^2,4*(17^4-1)]}|>]

(* Second actual call: scale-retaining joint witnesses and a passing example. *)
Module[{rows,z,poly13,phi,quintic,gaussian,c,unitroot},
 rows=Table[With[{q=data[[1]],p=data[[2]],xx=data[[3]],yy=data[[4]]},
 {q,PrimeQ[q],Mod[PowerMod[xx,10,q]+256*PowerMod[yy,10,q],q],
 PowerMod[Mod[2*PowerMod[xx,5,q],q],(q-1)/17,q],
 PowerMod[Mod[5*PowerMod[32,-1,q],q],(q-1)/17,q],PowerMod[p,(q-1)/17,q]}],
 {data,{{2381,1774,726,22},{17681,1932,9456,12},{610301,412274,25040,10}}}];
 poly13=z^5-2;
 quintic=PolynomialMod[PolynomialRemainder[(1+6*z+3*z^2+7*z^4)^17,poly13,z],13];
 gaussian=PolynomialMod[PolynomialRemainder[(5+z)^17,z^2+1,z],13];
 phi=z; unitroot=PolynomialMod[PolynomialRemainder[z^89,z^2-z-1,z],13];
 c=PowerMod[9,17,13];
 <|"rows_q_prime_toric_gaussian_c_phi"->rows,
 "q13_quintic_root_power"->quintic,"q13_gaussian_root_power"->gaussian,
 "q13_c_root_power"->c,"q13_phi_root"->unitroot,
 "q13_phi_root_power"->PolynomialMod[PolynomialRemainder[unitroot^17,z^2-z-1,z],13],
 "q13_toric_equation"->Mod[6^10+256,13]|>]
