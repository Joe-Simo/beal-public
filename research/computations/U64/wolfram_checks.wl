(* Two separate, stateless evaluations actually executed. *)
Module[{u,v,t,f,g,h,cs,pairs,roots,e},
 f[x_]:=x^5+40 u v x^3+320 u^2 v^2 x+64(8 v^5-u^5);
 g=Expand[f[t-u-2v]];cs=CoefficientList[g,t];
 h=Expand[(g/.t->0)/5-2(u^5+8v^5)];
 pairs=Select[Tuples[Range[0,24],2],Mod[#[[1]]^5+8#[[2]]^5,5]!=0&];
 roots=Select[pairs,Function[ab,AnyTrue[Range[0,24],Function[x,Mod[f[x]/.{u->ab[[1]],v->ab[[2]]},25]==0]]]];
 <|"lower_coefficients_divisible_by_5"->AllTrue[Flatten[CoefficientList[#,{u,v}]&/@Most[cs]],Mod[#,5]==0&],
 "constant_quotient_congruence"->PolynomialMod[h,5],"pairs_mod25"->Length[pairs],
 "pairs_with_root_mod25"->Length[roots],
 "discriminant_identity"->TrueQ[Factor[Discriminant[f[t],t]]==2^24*5^5*(u^5+8v^5)^4],
 "b_Hecke_sum_product"->{Expand[(9-e)+e],PolynomialRemainder[(9-e)e,e^2-9e+19,e]}|>]

Module[{pairs,mul,pow,count,rows,e,poly,vals,a,b,n1,n2,s,prod},
 mul[{x_,y_},{z_,w_},p_,d_]:=Mod[{x z+d y w,x w+y z},p];
 pow[v_,p_,d_]:=Nest[mul[#,v,p,d]&,{1,0},5];
 count[p_]:=Module[{d,els,squares,chi,c1,c2},
 d=SelectFirst[Range[2,p-1],JacobiSymbol[#,p]==-1&];els=Tuples[Range[0,p-1],2];
 squares=Counts[mul[#,#,p,d]&/@els];
 c1=1+Sum[1+JacobiSymbol[Mod[64-x^5,p],p],{x,0,p-1}];
 c2=1+Total[Lookup[squares,{#},0][[1]]&/@(Mod[{64,0}-pow[#,p,d],p]&/@els)];{c1,c2}];
 poly=e^2-9e+19;vals={{11,{9-e,e}},{19,{0,0}},{31,{-e-1,e-10}},{41,{11e-50,-11e+49}}};
 rows=Table[{n1,n2}=count[z[[1]]];s=z[[1]]+1-n1;prod=(s^2-(z[[1]]^2+1-n2))/2-2z[[1]];
 {a,b}=z[[2]];{z[[1]],n1,n2,s,prod,Expand[a+b],PolynomialRemainder[a b,poly,e]}, {z,vals}];
 <|"boundary_q_Nq_Nq2_S_P_HeckeSum_HeckeProduct"->rows,
 "all_boundary_pairs_match"->And@@(#[[4;;5]]==#[[6;;7]]&/@rows)|>]
