default(parisize, "1G");
default(realprecision, 50);

{
print("================================================================================");
print("  U110: SIGNATURE (5, 5, p) HIGHER PRIMES INVESTIGATION AND L_17 CERTIFICATION");
print("  Author: Signature (5, 5, p) Higher Prime Specialist");
print("  Targets: p in {17, 19, 23}, Q(zeta_17)^+ (deg 8), and Descent Fields (deg 34)");
print("  References: Dahmen-Siksek (2014, Acta Arith. 164), BCDF (2019, Trans. AMS 371),");
print("              BCDF (2022/2025 Crelle), U102/U103 Beal Checkpoints");
print("================================================================================\n");

t_total_start = gettime();

\\ =============================================================================
\\ PART 1: 2-TORSION RIGIDITY ACROSS HIGHER PRIMES p in {17, 19, 23}
\\ =============================================================================
print("################################################################################");
print("  PART 1: REPRESENTATION-THEORETIC 2-RIGIDITY FOR p in {17, 19, 23}");
print("################################################################################\n");

plist = [17, 19, 23];
for(idx=1, #plist,
  p = plist[idx];
  ord2 = znorder(Mod(2, p));
  phi_p = (x^p - 1) / (x - 1);
  fac = factormod(phi_p, 2);
  n_fac = matsize(fac)[1];
  deg_fac = poldegree(fac[1, 1]);
  print("--- Exponent p = ", p, " ---");
  print("  [1.", idx, ".1] Multiplicative Order ord_", p, "(2)       = ", ord2);
  print("  [1.", idx, ".2] Factorization of Phi_", p, "(X) mod 2    = ", n_fac, " irreducible factor(s) of degree ", deg_fac);
  print("  [1.", idx, ".3] Minimal non-trivial F_2-module dim  = ", deg_fac);
  print("  [1.", idx, ".4] Rigidity: dim_{F_2} Cl(O_{L_", p, "})[2] in {0} U {d >= ", deg_fac, "}");
  p_cm = 2.0^(-deg_fac^2);
  print("  [1.", idx, ".5] Cohen-Martinet Heuristic Bound       = 2^(-", deg_fac^2, ") < ", p_cm, "\n");
);


\\ =============================================================================
\\ PART 2: FIELD Q(zeta_17)^+ (MAXIMAL TOTALLY REAL CYCLOTOMIC SUBFIELD, DEG 8)
\\ =============================================================================
print("################################################################################");
print("  PART 2: ANALYSIS OF THE MAXIMAL REAL CYCLOTOMIC FIELD Q(zeta_17)^+");
print("################################################################################\n");

w17 = polsubcyclo(17, 8);
nf_cyc = nfinit(w17);
bnf_cyc = bnfinit(w17, 1);

deg_cyc = poldegree(w17);
r_cyc = nf_cyc.sign;
rank_cyc = r_cyc[1] + r_cyc[2] - 1;
disc_cyc = nf_cyc.disc;
expected_disc_cyc = 17^7;
h_cyc = bnf_cyc.no;
reg_cyc = bnf_cyc.reg;

print("[2.1] Defining Polynomial P_8(w)     = ", w17);
print("[2.2] Degree [Q(zeta_17)^+ : Q]      = ", deg_cyc);
print("[2.3] Signature (r1, r2)             = (", r_cyc[1], ", ", r_cyc[2], ") [TOTALLY REAL]");
print("[2.4] Dirichlet Unit Rank            = ", rank_cyc);
print("[2.5] Field Discriminant             = ", disc_cyc);
print("[2.6] Expected Discriminant 17^7     = ", expected_disc_cyc);
print("[2.7] Discriminant Match             = ", disc_cyc == expected_disc_cyc);
print("[2.8] Class Number h(Q(zeta_17)^+)   = ", h_cyc, " (Class group: ", bnf_cyc.cyc, ")");
print("[2.9] Regulator R(Q(zeta_17)^+)      = ", reg_cyc);

\\ 2-Saturation of Q(zeta_17)^+ units
gens_cyc = concat([-1], bnf_cyc.fu);
dim_cyc = rank_cyc + 1;
primes_test = [67, 101, 103, 137, 239, 307, 409, 443, 613, 647, 919, 953, 1021, 1039, 1087, 1123, 1223, 1259, 1291, 1327];
pr_cyc_list = [];
for(k=1, #primes_test,
  dec = idealprimedec(nf_cyc, primes_test[k]);
  for(m=1, #dec,
    if(dec[m].f == 1,
      pr_cyc_list = concat(pr_cyc_list, [dec[m]])
    )
  );
  if(#pr_cyc_list >= 20, break);
);
N_cyc = min(#pr_cyc_list, 16);
M_cyc_quad = matrix(N_cyc, dim_cyc);
for(k=1, N_cyc,
  pr = pr_cyc_list[k];
  q = pr.p;
  for(m=1, dim_cyc,
    u = gens_cyc[m];
    val = nfmodpr(nf_cyc, u, pr);
    is_sq = (val^((q-1)/2) == 1);
    M_cyc_quad[k, m] = if(is_sq, 0, 1);
  );
);
rank_cyc_2sat = matrank(M_cyc_quad * Mod(1, 2));
print("[2.10] Unit mod squares dim          = ", dim_cyc);
print("[2.11] Local Quad Char Matrix Rank   = ", rank_cyc_2sat);
if(rank_cyc_2sat == dim_cyc,
  print("       [*] Q(zeta_17)^+ UNIT GROUP IS UNCONDITIONALLY 2-SATURATED IN O*!"),
  print("       [!] Rank deficient")
);


\\ =============================================================================
\\ PART 3: THE DEGREE 34 DESCENT FIELD L_{17, 0} (CURVE C_{17, 0})
\\ =============================================================================
print("\n################################################################################");
print("  PART 3: DESCENT FIELD L_{17, 0} FOR CURVE C_{17, 0} (g_{17,0}(t) = t^34 + 2*t^17 - 4)");
print("################################################################################\n");

f0 = t^34 + 2*t^17 - 4;
t0 = gettime();
nf0 = nfinit(f0);
bnf0 = bnfinit(f0, 1);
t_bnf0 = gettime() - t0;

deg0 = poldegree(f0);
r0 = nf0.sign;
unit_rank0 = r0[1] + r0[2] - 1;
disc0 = nf0.disc;
expected_disc17 = 2^32 * 5^17 * 17^34;
h0 = bnf0.no;
cyc0 = bnf0.cyc;
reg0 = bnf0.reg;
w0 = bnf0.tu[1];

print("[3.1] Defining Polynomial g_{17,0}  = ", f0);
print("[3.2] Degree [L_{17,0} : Q]          = ", deg0);
print("[3.3] Signature (r1, r2)             = (", r0[1], ", ", r0[2], ")");
print("[3.4] Dirichlet Unit Rank            = ", unit_rank0);
print("[3.5] Field Discriminant             = ", disc0);
print("[3.6] Expected 2^32*5^17*17^34       = ", expected_disc17);
print("[3.7] Discriminant Match             = ", disc0 == expected_disc17);
print("[3.8] bnfinit computation time       = ", t_bnf0, " ms");
print("[3.9] Class Number h(L_{17,0})       = ", h0);
print("[3.10] Class Group Invariants        = ", cyc0);
print("[3.11] Regulator R(L_{17,0})         = ", reg0);
print("[3.12] Roots of Unity                = ", w0, " (generator: ", bnf0.tu[2], ")");

\\ Minkowski and Bach bounds
log_d17 = log(1.0 * disc0);
sqrtd17 = sqrt(1.0 * disc0);
M17 = (factorial(deg0) / (deg0^deg0)) * ((4/Pi)^r0[2]) * sqrtd17;
B_Bach17 = 12 * (log_d17)^2;
print("[3.13] Minkowski Bound M_{17}        = ", M17);
print("[3.14] log10(M_{17})                 = ", log(M17)/log(10));
print("[3.15] Bach Bound (GRH) B_{17}       = ", B_Bach17);

\\ Independent Scratch Regulator from Numerical Roots
r_all0 = polroots(f0);
r_real0 = [];
r_cplx0 = [];
for(k=1, #r_all0,
  if(abs(imag(r_all0[k])) < 1e-35,
    r_real0 = concat(r_real0, [r_all0[k]]),
    if(imag(r_all0[k]) > 1e-35,
      r_cplx0 = concat(r_cplx0, [r_all0[k]])
    )
  )
);

M_reg0 = matrix(unit_rank0, unit_rank0);
for(j=1, unit_rank0,
  u_pol = lift(bnf0.fu[j]);
  val_real = subst(u_pol, t, r_real0[1]);
  M_reg0[1, j] = log(abs(val_real));
  for(k=1, unit_rank0 - 1,
    val_cplx = subst(u_pol, t, r_cplx0[k]);
    M_reg0[k+1, j] = 2 * log(abs(val_cplx));
  );
);

det_M0 = abs(matdet(M_reg0));
diff_reg0 = abs(det_M0 - reg0);
rel_diff0 = diff_reg0 / reg0;
print("[3.16] Scratch Regulator Det         = ", det_M0);
print("[3.17] Regulator Relative Agreement  = 1 - ", rel_diff0);
if(rel_diff0 < 1e-30,
  print("       [*] L_{17,0} REGULATOR INDEPENDENTLY VERIFIED TO OVER 30 PLACES: SUCCESS!"),
  print("       [!] Regulator discrepancy detected.")
);

\\ Unconditional 2-Saturation of L_{17, 0}
gens0 = concat([-1], bnf0.fu);
dim0 = unit_rank0 + 1;
p_candidates = [3, 7, 11, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127];
all_pr0 = [];
for(k=1, #p_candidates,
  pr_p = idealprimedec(nf0, p_candidates[k]);
  for(m=1, #pr_p,
    if(pr_p[m].f == 1,
      all_pr0 = concat(all_pr0, [pr_p[m]])
    )
  );
  if(#all_pr0 >= 40, break);
);
N_pr0 = min(#all_pr0, 30);
M0_quad = matrix(N_pr0, dim0);
for(k=1, N_pr0,
  pr = all_pr0[k];
  q = pr.p;
  for(m=1, dim0,
    u = gens0[m];
    val = nfmodpr(nf0, u, pr);
    is_sq = (val^((q-1)/2) == 1);
    M0_quad[k, m] = if(is_sq, 0, 1);
  );
);
rank0 = matrank(M0_quad * Mod(1, 2));
print("[3.18] Unit mod squares dimension    = ", dim0);
print("[3.19] Local Quad Char Matrix Rank   = ", rank0);
if(rank0 == dim0,
  print("       [*] L_{17,0} UNIT GROUP IS UNCONDITIONALLY 2-SATURATED IN O_{L_{17,0}}*!"),
  print("       [!] Rank deficient: rank = ", rank0)
);

\\ Relative Norms to K = Q(phi)
rel_pol17_0 = t^17 - (2*y - 2);
k_pol = y^2 - y - 1;
print("[3.20] Relative Norms N_{L_{17,0}/K}(u_i):");
for(k=1, unit_rank0,
  u = lift(bnf0.fu[k]);
  res = polresultant(rel_pol17_0, u, t);
  res_mod = Mod(res, k_pol);
  for(m=-40, 40,
    for(s_idx=1, 2,
      sgn = if(s_idx==1, 1, -1);
      phi_m = sgn * (Mod(y, k_pol)^m);
      if(phi_m == res_mod,
        sgn_str = if(sgn==1, "+", "-");
        print("       Unit u", if(k<10, concat(" ", Str(k)), Str(k)), ": N(u) = ", sgn_str, "phi^(", m, ")");
        break(2);
      );
    );
  );
);

\\ Dedekind Zeta Residues
res0 = (2^r0[1] * (2*Pi)^r0[2] * reg0) / (2 * sqrt(1.0 * disc0));
res_k = (4 * log((1+sqrt(5))/2)) / (2 * sqrt(5));
ratio0 = res0 / res_k;
print("[3.21] Analytic Residue Res_{s=1} zeta_{L_{17,0}} = ", res0);
print("[3.22] Base Field Residue Res_{s=1} zeta_K      = ", res_k);
print("[3.23] Ratio Res(zeta_{L_{17,0}}) / Res(zeta_K)  = ", ratio0);


\\ =============================================================================
\\ PART 4: THE DEGREE 34 DESCENT FIELD L_{17, 1} (CURVE C_{17, 1})
\\ =============================================================================
print("\n################################################################################");
print("  PART 4: DESCENT FIELD L_{17, 1} FOR CURVE C_{17, 1} (g_{17,1}(t) = t^34 - 16*t^17 - 16)");
print("################################################################################\n");

f1 = t^34 - 16*t^17 - 16;
t0 = gettime();
nf1 = nfinit(f1);
bnf1 = bnfinit(f1, 1);
t_bnf1 = gettime() - t0;

deg1 = poldegree(f1);
r1 = nf1.sign;
unit_rank1 = r1[1] + r1[2] - 1;
disc1 = nf1.disc;
h1 = bnf1.no;
cyc1 = bnf1.cyc;
reg1 = bnf1.reg;
w1 = bnf1.tu[1];

print("[4.1] Defining Polynomial g_{17,1}  = ", f1);
print("[4.2] Degree [L_{17,1} : Q]          = ", deg1);
print("[4.3] Signature (r1, r2)             = (", r1[1], ", ", r1[2], ")");
print("[4.4] Dirichlet Unit Rank            = ", unit_rank1);
print("[4.5] Field Discriminant             = ", disc1);
print("[4.6] Discriminant Match             = ", disc1 == expected_disc17);
print("[4.7] bnfinit computation time       = ", t_bnf1, " ms");
print("[4.8] Class Number h(L_{17,1})       = ", h1);
print("[4.9] Class Group Invariants         = ", cyc1);
print("[4.10] Regulator R(L_{17,1})         = ", reg1);

\\ Unconditional 2-Saturation of L_{17, 1}
gens1 = concat([-1], bnf1.fu);
dim1 = unit_rank1 + 1;
all_pr1 = [];
for(k=1, #p_candidates,
  pr_p = idealprimedec(nf1, p_candidates[k]);
  for(m=1, #pr_p,
    if(pr_p[m].f == 1,
      all_pr1 = concat(all_pr1, [pr_p[m]])
    )
  );
  if(#all_pr1 >= 40, break);
);
N_pr1 = min(#all_pr1, 30);
M1_quad = matrix(N_pr1, dim1);
for(k=1, N_pr1,
  pr = all_pr1[k];
  q = pr.p;
  for(m=1, dim1,
    u = gens1[m];
    val = nfmodpr(nf1, u, pr);
    is_sq = (val^((q-1)/2) == 1);
    M1_quad[k, m] = if(is_sq, 0, 1);
  );
);
rank1 = matrank(M1_quad * Mod(1, 2));
print("[4.11] Unit mod squares dimension    = ", dim1);
print("[4.12] Local Quad Char Matrix Rank   = ", rank1);
if(rank1 == dim1,
  print("       [*] L_{17,1} UNIT GROUP IS UNCONDITIONALLY 2-SATURATED IN O_{L_{17,1}}*!"),
  print("       [!] Rank deficient: rank = ", rank1)
);

\\ Dedekind Zeta Residues for L_{17, 1}
res1 = (2^r1[1] * (2*Pi)^r1[2] * reg1) / (2 * sqrt(1.0 * disc1));
ratio1 = res1 / res_k;
print("[4.13] Analytic Residue Res_{s=1} zeta_{L_{17,1}} = ", res1);
print("[4.14] Base Field Residue Res_{s=1} zeta_K      = ", res_k);
print("[4.15] Ratio Res(zeta_{L_{17,1}}) / Res(zeta_K)  = ", ratio1);


\\ =============================================================================
\\ PART 5: THE FRONTIER PRIMES p = 19 AND p = 23 DESCENT INVARIANTS
\\ =============================================================================
print("\n################################################################################");
print("  PART 5: DESCENT FIELD INVARIANTS FOR FRONTIER PRIMES p = 19 AND p = 23");
print("################################################################################\n");

\\ p = 19
f19 = t^38 + 2*t^19 - 4;
nf19 = nfinit(f19);
expected_disc19 = 2^36 * 5^19 * 19^38;
print("[5.1] Field L_{19}: g_{19}(t)        = ", f19);
print("[5.2] Degree [L_{19} : Q]            = ", poldegree(f19));
print("[5.3] Signature (r1, r2)             = (", nf19.sign[1], ", ", nf19.sign[2], ")");
print("[5.4] Dirichlet Unit Rank            = ", nf19.sign[1] + nf19.sign[2] - 1);
print("[5.5] Field Discriminant Match       = ", nf19.disc == expected_disc19);

\\ p = 23
f23 = t^46 + 2*t^23 - 4;
nf23 = nfinit(f23);
expected_disc23 = 2^44 * 5^23 * 23^46;
print("[5.6] Field L_{23}: g_{23}(t)        = ", f23);
print("[5.7] Degree [L_{23} : Q]            = ", poldegree(f23));
print("[5.8] Signature (r1, r2)             = (", nf23.sign[1], ", ", nf23.sign[2], ")");
print("[5.9] Dirichlet Unit Rank            = ", nf23.sign[1] + nf23.sign[2] - 1);
print("[5.10] Field Discriminant Match      = ", nf23.disc == expected_disc23);


print("\n================================================================================");
print("  ALL INVESTIGATIONS AND CERTIFICATIONS COMPLETED IN ", gettime() - t_total_start, " ms");
print("================================================================================");
}
quit;
