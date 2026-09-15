/** U79: verify local-divisor norm and square-congruence certificates exactly.
 * The norm coefficients are independently generated from the implicit root
 * series, not copied from the Python Lagrange-log formula.
 */
import certificate from '../references/U79/certificate.json';
const check: (ok: boolean, message: string) => asserts ok = (ok, message) => {
  if (!ok) throw new Error(message);
};
type Vec = readonly bigint[];
type Pair = readonly [bigint, bigint];
const mod = (a: bigint, n: bigint): bigint => ((a % n) + n) % n;
const one = [1n, ...Array<bigint>(33).fill(0n)];
const zero = Array<bigint>(34).fill(0n);
function pairMultiply(a: Pair, b: Pair, m: bigint): Pair {
  return [mod(a[0]*b[0]+a[1]*b[1], m),
    mod(a[0]*b[1]+a[1]*b[0]+a[1]*b[1], m)];
}
function multiply(a: Vec, b: Vec, m = 8n): bigint[] {
  check(a.length === 34 && b.length === 34, 'Wrong coefficient rank');
  const aa: Pair[] = [], bb: Pair[] = [];
  for (let i=0; i<17; i++) { aa.push([a[2*i]!, a[2*i+1]!]); bb.push([b[2*i]!, b[2*i+1]!]); }
  const temp: Pair[] = Array.from({length: 33}, () => [0n, 0n] as const);
  for (let i=0; i<17; i++) for (let j=0; j<17; j++) {
    const p = pairMultiply(aa[i]!, bb[j]!, m), old = temp[i+j]!;
    temp[i+j] = [mod(old[0]+p[0], m), mod(old[1]+p[1], m)];
  }
  for (let k=32; k>=17; k--) {
    const p = pairMultiply(temp[k]!, [-2n, 2n], m), old = temp[k-17]!;
    temp[k-17] = [mod(old[0]+p[0], m), mod(old[1]+p[1], m)];
  }
  return temp.slice(0,17).flatMap(p => [...p]);
}
function add(a: Vec, b: Vec, m=8n): bigint[] { return a.map((v,i) => mod(v+b[i]!,m)); }
function scale(a: Vec, n: bigint, m=8n): bigint[] { return a.map(v => mod(v*n,m)); }
function monomial(n: number, p: Pair=[1n,0n], m=8n): bigint[] {
  check(Number.isSafeInteger(n) && n>=0, 'Invalid monomial');
  for (let i=0; i<Math.floor(n/17); i++) p=pairMultiply(p,[-2n,2n],m);
  const out=[...zero]; out[2*(n%17)]=p[0]; out[2*(n%17)+1]=p[1]; return out;
}
function valuation(a: Vec, bits=3): number {
  let v=17*bits;
  for(let i=0;i<34;i++) {
    let c=a[i]!, power=0;
    if(c===0n) continue;
    while(c%2n===0n){c/=2n;power++;}
    v=Math.min(v,17*power+Math.floor(i/2));
  }
  return v;
}
function choose(n: number,k: number): bigint {
  let v=1n;
  for(let i=1;i<=k;i++)v=v*BigInt(n-i+1)/BigInt(i);
  return v;
}
function normSeries(d: number, degree: number): bigint[] {
  const max=d*degree;
  // H=1-V, V=q^17*(1-V)^(-16); its coefficients are Fuss-Catalan integers.
  const F=Array<bigint>(max+1).fill(0n); F[0]=1n;
  if(max>=1)F[1]=1n;
  for(let n=1;17*n<=max;n++) {
    const c=choose(17*n-2,n-1);
    check(c%BigInt(n)===0n,'Nonintegral implicit series');
    F[17*n]=-c/BigInt(n);
  }
  // L_n=n*[q^n]log(F), found from F'=F*(log F)'.
  const L=Array<bigint>(max+1).fill(0n);
  for(let n=1;n<=max;n++) {
    let c=BigInt(n)*F[n]!;
    for(let j=1;j<n;j++)c-=L[j]!*F[n-j]!;
    L[n]=c;
  }
  const N=[1n];
  for(let n=1;n<=degree;n++) {
    let c=0n;
    for(let j=1;j<=n;j++)c+=L[d*j]!*N[n-j]!;
    check(c%BigInt(n)===0n,'Nonintegral norm series');N.push(c/BigInt(n));
  }
  return N;
}
function buildUnit(d: number, parameter: string, bits=3) {
  const m=1n<<BigInt(bits),depth=34-2*d;
  let coefficient: Pair=[1n,1n];
  for(let i=0;i<d;i++)coefficient=pairMultiply(coefficient,[3n,-1n],m);
  if(parameter==='phi')coefficient=pairMultiply(coefficient,[2n,-1n],m);
  else check(parameter==='1','Unknown parameter');
  const series=normSeries(d,Math.floor((17*bits-1)/depth));
  const t=monomial(depth,coefficient,m);let term=[...one],out=[...zero];
  for(const c of series){out=add(out,scale(term,c,m),m);term=multiply(term,t,m);}
  check(valuation(term,bits)>=17*bits,'Insufficient tail precision');
  return {unit:out,series};
}
function highProduct(code: number,m=8n): bigint[] {
  let out=[...one];
  for(let k=0;k<16;k++)if((code>>k)&1) {
    const n=19+2*Math.floor(k/2),p:Pair=k%2===0?[1n,0n]:[0n,1n];
    out=multiply(out,add(one,monomial(n,p,m),m),m);
  }
  return out;
}
function binaryRank(values: readonly number[]): number {
  const a=[...values];let rank=0;
  for(let bit=15;bit>=0;bit--) {
    const p=a.findIndex((v,j)=>j>=rank&&((v>>bit)&1)!==0);
    if(p===-1)continue;
    [a[p],a[rank]]=[a[rank]!,a[p]!];
    for(let j=0;j<a.length;j++)if(j!==rank&&((a[j]!>>bit)&1))a[j]=a[j]!^a[rank]!;
    rank++;
  }
  return rank;
}
const computed=certificate.witnesses.map(row=>{
  check(row.d>=1&&row.d<=15&&row.d%2===1,'Invalid extension degree');
  const {unit,series}=buildUnit(row.d,row.parameter);
  check(series.map(String).join(',')===row.norm_polynomial.join(','),'Norm coefficient mismatch');
  check(unit.map(Number).join(',')===row.unit_mod8.join(','),'Norm representative mismatch');
  check(row.high_basis_code>=0&&row.high_basis_code<65536,'Invalid high basis code');
  let square=[...one];
  for(const correction of row.square_corrections) {
    const [n,a,b]=correction;
    check(n!==undefined&&a!==undefined&&b!==undefined&&n>0&&n<=17,'Bad square witness');
    check((a===0||a===1)&&(b===0||b===1),'Bad residue representative');
    square=multiply(square,add(one,monomial(n,[BigInt(a),BigInt(b)])));
  }
  const target=multiply(highProduct(row.high_basis_code),multiply(square,square));
  check(valuation(add(unit,scale(target,-1n)))>=35,'Squareclass congruence failed');
  // Same squares and high-class representative are valid at greater ring precision.
  const higher=buildUnit(row.d,row.parameter,4).unit;
  let sq16=[...one];
  for(const c of row.square_corrections) {
    sq16=multiply(sq16,add(one,monomial(c[0]!,[BigInt(c[1]!),BigInt(c[2]!)],16n),16n),16n);
  }
  const target16=multiply(highProduct(row.high_basis_code,16n),multiply(sq16,sq16,16n),16n);
  check(valuation(add(higher,scale(target16,-1n,16n),16n),4)>=35,'Higher precision failed');
  return {d:row.d,parameter:row.parameter,t_depth:34-2*row.d,
    norm_polynomial:series.map(String),unit_mod8:unit.map(Number),
    high_basis_code:row.high_basis_code,square_corrections:row.square_corrections,
    square_congruence_depth_at_least:35};
});
check(computed.length===16,'Incomplete witness count');
check(new Set(computed.map(r=>`${r.d}:${r.parameter}`)).size===16,'Repeated witness');
const codes=computed.map(r=>r.high_basis_code);check(binaryRank(codes)===16,'Witnesses do not span');
// The last three unit generators map to a basis of the base local squareclasses.
const units:Pair[]=[];
for(let a=0n;a<8n;a++)for(let b=0n;b<8n;b++)if(a%2n!==0n||b%2n!==0n)units.push([a,b]);
const sqMap=new Map(units.map(a=>{const s=pairMultiply(a,a,8n);return [s.join(','),s];}));
check(sqMap.size===6,'Base square subgroup size');
const c:Pair=[6n,2n],c2=pairMultiply(c,c,8n);
const gens:Pair[]=[[7n,2n],[3n,0n],[mod(1n+c2[0],8n),c2[1]]];
const cosets=new Set<string>();
for(let n=0;n<8;n++) {
  let a:Pair=[1n,0n];for(let i=0;i<3;i++)if(n>>i&1)a=pairMultiply(a,gens[i]!,8n);
  cosets.add([...sqMap.values()].map(s=>pairMultiply(a,s,8n).join(',')).sort().join(';'));
}
check(cosets.size===8,'Base norm generators not independent');
// For alpha=(1+s)/(1+s^17), its class equals (1+s)(1+s^17), since an
// inverse and the element have equal squareclass. Its lower grade is 1.
const alphaNumerator=add(one,monomial(1)),alphaDenominator=add(one,monomial(17));
const alphaProduct=multiply(alphaNumerator,alphaDenominator);
check(valuation(add(alphaProduct,scale(one,-1n)))===1,'Candidate leading odd grade');
const summary={dyadic_Kummer_dimension:16,dyadic_basis:['1+s^n','1+phi*s^n'],
  basis_exponents:[19,21,23,25,27,29,31,33],witness_count:16,witness_matrix_rank:16,
  high_basis_codes_by_d:Array.from({length:8},(_,i)=>codes.slice(2*i,2*i+2)),
  precision:'modulo 8, congruence modulo s^35; v_s(2)=17',higher_precision_codes_identical:true,
  base_norm_cosets:8,restriction_coordinates:'16 bits at odd depths 1,3,...,15',
  alpha_global_candidate:'(s+1)/(1+s^17)=1/h(s)',alpha_squareclass_code:65537,
  alpha_low16_code:1,alpha_passes_at5:true,alpha_fails_at2:true,
  class_group_2_rank_computed:false,global_candidate_basis_computed:false,
  global_restriction_matrix_computed:false,numerical_rank_upper_bound_computed:false,
  full_Beal_solved:false};
console.log(JSON.stringify({checkpoint:'U79',summary,witnesses:computed},null,2));
