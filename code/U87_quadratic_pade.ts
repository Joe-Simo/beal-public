export {};

type Rat = { n: bigint; d: bigint };
function abs(a: bigint): bigint { return a < 0n ? -a : a; }
function gcd(a: bigint, b: bigint): bigint {
  let x=abs(a), y=abs(b);
  while(y!==0n){ const r=x%y; x=y; y=r; }
  return x;
}
function rat(n: bigint, d: bigint=1n): Rat {
  if(d===0n) throw new Error('zero denominator');
  let nn=n, dd=d;
  if(dd<0n){nn=-nn;dd=-dd;}
  const g=gcd(nn,dd);
  return {n:nn/g,d:dd/g};
}
function add(a:Rat,b:Rat):Rat{return rat(a.n*b.d+b.n*a.d,a.d*b.d);}
function mul(a:Rat,b:Rat):Rat{return rat(a.n*b.n,a.d*b.d);}
function scale(a:Rat,k:bigint):Rat{return rat(a.n*k,a.d);}
function powBig(base:bigint, exp:number):bigint {
  let b=base,e=exp,out=1n;
  while(e>0){if(e&1)out*=b;b*=b;e>>=1;}
  return out;
}

const maxN=49;
const B:Rat[]=[rat(1n)];
for(let k=1;k<=maxN;k++){
  const prev=B[k-1]; if(!prev) throw new Error('missing binomial');
  B.push(mul(prev,rat(BigInt(1-17*(k-1)),BigInt(17*k))));
}
function f(j:number,m:number):Rat {
  const b=B[j+10*m]; if(!b) throw new Error(`missing B ${j+10*m}`);
  return scale(b,powBig(-256n,m));
}
const pairs=[[1,9],[2,8],[3,7],[4,6],[5,5]] as const;
function productSeriesCoefficient(pairIndex:number,n:number):Rat {
  const pair=pairs[pairIndex]; if(!pair) throw new Error('missing pair');
  let out=rat(0n);
  for(let k=0;k<=n;k++) out=add(out,mul(f(pair[0],k),f(pair[1],n-k)));
  return out;
}

const lambda=[
 15798242183726487723872974980213975697091265396056n,
 -249202890961784236021683574474477003603265904312448n,
 1216292797751835710390793468584676049161821798713448n,
 -2877403423806299594932394239043237544733898769276736n,
 1894513509087467786381667797189625338402082189240825n,
] as const;
let lambdaGcd=0n;
for(const x of lambda) lambdaGcd=gcd(lambdaGcd,x);
if(lambdaGcd!==1n) throw new Error('lambda not primitive');

const combo:Rat[]=[];
for(let n=0;n<=4;n++){
  let s=rat(0n);
  for(let j=0;j<5;j++) s=add(s,scale(productSeriesCoefficient(j,n),lambda[j]!));
  combo.push(s);
}
for(let n=0;n<4;n++){
  const c=combo[n]; if(!c || c.n!==0n) throw new Error(`cancellation failed at S^${n}`);
}
const lead=combo[4]; if(!lead || lead.n===0n) throw new Error('S^4 coefficient vanished');
if(lead.n%31n===0n || lead.d%31n===0n) throw new Error('leading coefficient not a 31-adic unit');

const L=lambda.reduce((s,x)=>s+abs(x),0n);
if(L!==6253210863791113815450412054272229911598159926939513n) throw new Error('L mismatch');
const forcedProduct=433992707035920672833426144791n;
const lhs=powBig(forcedProduct,50*17);
const rhs12155=9n*powBig(L,17)*powBig(10n,2*12155);
const rhs12156=9n*powBig(L,17)*powBig(10n,2*12156);
if(!(lhs>rhs12155)) throw new Error('12155 lower bound failed');
if(!(lhs<rhs12156)) throw new Error('12156 threshold check failed');

console.log(JSON.stringify({
  checkpoint:'U87',
  coefficientPairs:pairs,
  lambda:lambda.map(String),
  lambdaL1:String(L),
  cancelledSCoefficients:[0,1,2,3],
  firstNonzeroSCoefficient:4,
  localYOrder:50,
  leadNumeratorDigits:lead.n.toString().replace('-','').length,
  leadDenominatorDigits:lead.d.toString().length,
  lead31AdicUnit:true,
  forcedProduct:String(forcedProduct),
  forcedProductPowerDividingInvariant:50,
  maxBaseStrictlyGreaterThanPowerOf10:12155,
  fullBealSolved:false,
},null,2));
