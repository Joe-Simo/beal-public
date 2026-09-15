Module[{q=409, gp, rootsI, rootsW, i0, inv2, inv2i, pairs, rows},
 gp=Union[PowerMod[Range[0,q-1],17,q]];
 rootsI=Select[Range[0,q-1],Mod[#^2+1,q]==0&];
 rootsW=Select[Range[0,q-1],Mod[#^2-#-1,q]==0&];
 i0=First[rootsI]; inv2=PowerMod[2,-1,q]; inv2i=PowerMod[2*i0,-1,q];
 pairs=DeleteCases[Flatten[Table[{Mod[(a+b)*inv2,q],Mod[(a-b)*inv2i,q]},
   {a,gp},{b,gp}],1],{0,0}];
 rows=Table[With[{kept=Select[pairs,Function[z,And@@Table[
   MemberQ[gp,Mod[(z[[1]]^4+30*z[[1]]^2*z[[2]]^2+z[[2]]^4
     -16*z[[1]]^2*z[[2]]^2*w)*PowerMod[PowerMod[w,k,q],-1,q],q]],
   {w,rootsW}]]]},
   {k,Length[kept],Count[kept,{m_,n_}/;Mod[m*n,q]==0],
    Count[kept,{m_,n_}/;Mod[m*m+n*n,q]==0]}],{k,{0,15}}];
 <|"q"->q,"roots_i"->rootsI,"roots_omega"->rootsW,
   "scalar_17th_power_values_including_zero"->gp,
   "nonzero_Gaussian_outputs"->Length[pairs],
   "zero_norm_outputs_included"->Count[pairs,{m_,n_}/;Mod[m*m+n*n,q]==0],
   "rows_k_survivors_axes_zeroNorm"->rows|>]
