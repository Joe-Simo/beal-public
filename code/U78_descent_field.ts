/** U78 exact checks by trace and multiplication matrices.
 * No class group, dyadic-image basis, global restriction matrix, or rank is computed.
 */
export {};
const check: (ok: boolean, message: string) => asserts ok = (ok, message) => {
  if (!ok) throw new Error(message);
};
const mod = (a: bigint, m: bigint): bigint => ((a%m)+m)%m;
type Vec = readonly bigint[];
function determinant(input: readonly Vec[]): bigint {
  const a=input.map(r=>[...r]),n=a.length;
  check(n>0&&a.every(r=>r.length===n),'Non-square matrix');
  let old=1n,sign=1n;
  for(let k=0;k<n-1;k++) {
    let pivot=k;while(pivot<n&&a[pivot]![k]===0n)pivot++;
    if(pivot===n)return 0n;
    if(pivot!==k){[a[k],a[pivot]]=[a[pivot]!,a[k]!];sign=-sign;}
    const value=a[k]![k]!;
    for(let i=k+1;i<n;i++)for(let j=k+1;j<n;j++) {
      const num=value*a[i]![j]!-a[i]![k]!*a[k]![j]!;
      check(num%old===0n,'Non-exact Bareiss division');a[i]![j]=num/old;
    }
    for(let i=k+1;i<n;i++)a[i]![k]=0n;
    old=value;
  }
  return sign*a[n-1]![n-1]!;
}
function reduceF(input: Vec): bigint[] {
  const c=[...input];while(c.length<34)c.push(0n);
  for(let k=c.length-1;k>=34;k--) {
    c[k-17]=c[k-17]!-2n*c[k]!;c[k-34]=c[k-34]!+4n*c[k]!;
  }
  return c.slice(0,34);
}
function multiplyF(a:Vec,b:Vec):bigint[] {
  const c=Array<bigint>(a.length+b.length-1).fill(0n);
  for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=c[i+j]!+a[i]!*b[j]!;
  return reduceF(c);
}
function powerF(a:Vec,n:number):bigint[] {
  let out=reduceF([1n]),b=reduceF(a);
  while(n>0){if(n%2)out=multiplyF(out,b);b=multiplyF(b,b);n=Math.floor(n/2);}return out;
}
function normF(a:Vec):bigint {
  const cols=Array.from({length:34},(_,i)=>reduceF([...Array<bigint>(i).fill(0n),...a]));
  return determinant(Array.from({length:34},(_,r)=>cols.map(c=>c[r]!)));
}
type Pair = readonly [bigint,bigint];
function mulK(a:Pair,b:Pair):Pair {
  return [a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]];
}
function powK(a:Pair,n:number):Pair {
  let out:Pair=[1n,0n],b=a;
  while(n>0){if(n%2)out=mulK(out,b);b=mulK(b,b);n=Math.floor(n/2);}return out;
}
function normK(a:Pair):bigint{return a[0]**2n+a[0]*a[1]-a[1]**2n;}
function choose(n:number,k:number):bigint {
  let out=1n;for(let j=1;j<=k;j++)out=out*BigInt(n-j+1)/BigInt(j);return out;
}
// Small prime-field polynomials, exact integer arithmetic (p=5 only).
const fm=(a:number):number=>((a%5)+5)%5;
function trim(a:readonly number[]):number[]{const b=a.map(fm);while(b.length&&b[b.length-1]===0)b.pop();return b;}
function rem(a:readonly number[],b:readonly number[]):number[]{
  const c=trim(a);check(b.length>0,'Zero divisor polynomial');
  const inv=[0,1,3,2,4][b[b.length-1]!]!;
  while(c.length>=b.length){const offset=c.length-b.length,k=fm(c[c.length-1]!*inv);
    for(let j=0;j<b.length;j++)c[j+offset]=fm(c[j+offset]!-k*b[j]!);
    while(c.length&&c[c.length-1]===0)c.pop();}
  return c;
}
function mul5(a:readonly number[],b:readonly number[]):number[]{
  if(a.length===0||b.length===0)return [];
  const c=Array<number>(a.length+b.length-1).fill(0);
  for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=fm(c[i+j]!+a[i]!*b[j]!);
  return trim(c);
}
function gcd5(a:readonly number[],b:readonly number[]):number[]{
  let c=trim(a),d=trim(b);while(d.length)[c,d]=[d,rem(c,d)];
  return c.length?c.map(v=>fm(v*[0,1,3,2,4][c[c.length-1]!]!)):[];
}
function modPower5(a:readonly number[],n:number,h:readonly number[]):number[]{
  let out=[1],b=trim(a);while(n>0){if(n%2)out=rem(mul5(out,b),h);b=rem(mul5(b,b),h);n=Math.floor(n/2);}return out;
}
for(const p of [2,17])check(!Array.from({length:p},(_,a)=>a).some(a=>((a*a-a-1)%p+p)%p===0),'Base prime not inert');
const c:Pair=[-2n,2n],a:Pair=[0n,-2n];
const power=powK(a,17),shift:Pair=[power[0]-c[0],power[1]-c[1]];
check(shift.every(v=>v%17n===0n),'Shift not divisible by 17');
const shiftMod=shift.map(v=>Number(mod(v/17n,17n)));
check(shiftMod.join(',')==='11,8'&&mod(normK([11n,8n]),17n)===9n,'Shift not Eisenstein');
for(let j=1;j<17;j++)check(choose(17,j)%17n===0n&&choose(17,j)%289n!==0n,'Binomial valuation');
const h=Array.from({length:17},(_,j)=>j%2===0?1n:-1n);
check(h.reduce((sum,v,j)=>sum+v*(-1n)**BigInt(j),0n)===17n,'h(-1)');
const hp=h.map(v=>fm(Number(v)));let frobenius=[0,1];
for(let n=1;n<=16;n++) {
  frobenius=modPower5(frobenius,5,hp);
  if(n===8){const difference=[...frobenius];while(difference.length<2)difference.push(0);
    difference[1]=fm(difference[1]!-1);check(gcd5(hp,difference).join(',')==='1','Missing irreducibility gcd');}
}
check(frobenius.join(',')==='0,1','Frobenius degree-16 test');
let fivePower=1;for(let i=1;i<=16;i++){fivePower=fivePower*5%17;check((fivePower===1)===(i===16),'Incorrect residue degree');}

// Compute the basis discriminant independently from the Newton-trace Gram matrix.
const traces=Array<bigint>(67).fill(0n);traces[0]=34n;
for(let n=1;n<=66;n++) {
  let value=0n;
  if(n>17)value-=2n*traces[n-17]!;else if(n===17)value-=34n;
  if(n>34)value+=4n*traces[n-34]!;else if(n===34)value+=136n;
  traces[n]=value;
}
const basis2=Array.from({length:34},(_,j)=>{
  const v=Array<bigint>(34).fill(0n);if(j<17)v[j]=2n;else {v[j-17]=2n;v[j]=1n;}return v;});
const gram=basis2.map(left=>basis2.map(right=>{
  let t=0n;for(let i=0;i<34;i++)for(let j=0;j<34;j++)t+=left[i]!*right[j]!*traces[i+j]!;return t;}));
const gramDisc=determinant(gram);check(gramDisc%2n**68n===0n,'Basis scaling not exact');
const fieldDisc=gramDisc/2n**68n;
check(fieldDisc===2n**32n*5n**17n*17n**34n,'Field basis discriminant');
const index=2n**34n/determinant(basis2);
check(index===2n**17n,'Equation order index');
const normValues=[normF([0n,1n]),normF([1n,1n]),normF(h)];
check(normValues.join(',')===[-4n,-5n,5n**16n].join(','),'Principal generator norms');
check(normK(c)===-4n&&normK([-1n,2n])===-5n,'Relative constants');
const pi=Array<bigint>(18).fill(0n);pi[0]=1n;pi[17]=1n;
check(normF(pi)===(-5n)**17n,'Norm of sqrt5');
const numerator=Array<bigint>(33).fill(0n);numerator[15]=2n;numerator[32]=1n;
const rp=powerF(numerator,17);
const rootRhs=Array<bigint>(34).fill(0n);rootRhs[0]=4n**18n;rootRhs[17]=4n**17n;
check(rp.every((v,i)=>8n*v===rootRhs[i]),'Root equation');
const s17=Array<bigint>(18).fill(0n);s17[17]=1n;
const recovered=multiplyF(s17,powerF(numerator,8));
check(recovered.every((v,i)=>v===(i===1?4n**8n:0n)),'Recover s from root');
const delta:Pair=[3n,-1n],bb:Pair=[2n,1n],phSquared:Pair=[1n,1n];
check(mulK(delta,phSquared).join(',')===bb.join(','),'Curve coefficient identity');
// Scaling x=A*u,y=A^8*v makes y^2=x^17+A^16*B monic.
const aa:Pair=[-12n,4n];check(normK(aa)===80n&&normK(bb)===5n,'Model discriminant coefficient norms');
const modelDiscNorm=17n**34n*normK(aa)**256n*normK(bb)**16n;
check(modelDiscNorm===2n**1024n*5n**272n*17n**34n,'Good-prime inventory');
const kernel5:number[][]=[],image5:number[][]=[];
for(let n=0;n<16;n++){
  const row=[(n>>3)&1,(n>>2)&1,(n>>1)&1,n&1];
  if(row[0]===0&&(row[1]!+row[3]!)%2===0){kernel5.push(row);if((row[1]!+row[2]!)%2===0)image5.push(row);}}
check(kernel5.length===4&&image5.length===2&&image5[1]!.join(',')==='0,1,1,1','Local Kummer line');
check((17%5)**2%5===4,'Derivative nonsquare character');
const localDimensions=[{p:2,degree:2,fs:[17]},{p:5,degree:2,fs:[1,16]},{p:17,degree:2,fs:[17]}].map(row=>{
  const torsion=row.fs.length-1,im=torsion+(row.p===2?8*row.degree:0);
  return {prime:row.p,base_local_degree:row.degree,relative_factor_degrees:row.fs,
    J_local_2torsion_dimension:torsion,norm_kernel_dimension:2*im,Kummer_image_dimension:im,quotient_dimension:im};});
check(localDimensions.reduce((sum,r)=>sum+r.quotient_dimension,0)===17,'Restriction dimension');
check((2+16-1)+4+1-((2-1)+3+1)===17,'Global dimension constant');
const summary={defining_polynomial:'s^34+2*s^17-4',signature:[2,16],
  integral_basis:'s^j, phi*s^j, 0<=j<=16; phi=(s^17+2)/2',
  polynomial_discriminant_factorization:{'2':66,'5':17,'17':34},
  field_discriminant_factorization:{'2':32,'5':17,'17':34},field_discriminant:fieldDisc.toString(),
  equation_order_index:Number(index),shift_constant_coefficients:shift.map(Number),shift_divided_by17_mod17:shiftMod,
  shift_quotient_norm_mod17:9,norms_s_splus1_h:normValues.map(String),
  primes_above_S:[{p:2,absolute_e:17,absolute_f:2,ideal_norm:'4',principal_generator:'s'},
    {p:5,absolute_e:2,absolute_f:1,ideal_norm:'5',principal_generator:'s+1'},
    {p:5,absolute_e:2,absolute_f:16,ideal_norm:(5n**16n).toString(),principal_generator:'h(s)'},
    {p:17,absolute_e:17,absolute_f:2,ideal_norm:'289',class_order_divides:17}],
  monic_model_discriminant_norm_factors:{'2':1024,'5':272,'17':34},
  local5_norm_kernel:kernel5,local5_Kummer_image:image5,local_dimensions:localDimensions,
  real_local_norm_kernel_dimensions:[0,0],global_candidate_dimension:'17+d, d=dim_F2 Cl(F)[2]',
  restriction_target_dimension:17,Selmer_dimension_formula:'17+d-rank(Psi)',
  class_group_2_rank_computed:false,dyadic_image_basis_computed:false,restriction_matrix_computed:false,
  numerical_rank_upper_bound_computed:false,full_Beal_solved:false};
console.log(JSON.stringify({checkpoint:'U78',summary},null,2));
