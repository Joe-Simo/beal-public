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
function p(j:number,n:number):Rat {
  let out=rat(0n);
  for(let k=0;k<=n;k++) out=add(out,mul(f(j,k),f(9-j,n-k)));
  return out;
}

const lambda=[
 -391297461914300582187021086407205172878178454196n,
 -45543393576002299013194949131204923972748847296580n,
 263003783011157522723347342656612893143239370625476n,
 -515316029541067322730336733534880098514360212425548n,
 298239740356053050930242237285506272580149235212283n,
] as const;
let lambdaGcd=0n;
for(const x of lambda) lambdaGcd=gcd(lambdaGcd,x);
if(lambdaGcd!==1n) throw new Error('lambda not primitive');

const combo:Rat[]=[];
for(let n=0;n<=4;n++){
  let s=rat(0n);
  for(let j=0;j<5;j++) s=add(s,scale(p(j,n),lambda[j]!));
  combo.push(s);
}
for(let n=0;n<4;n++){
  const c=combo[n]; if(!c || c.n!==0n) throw new Error(`cancellation failed at S^${n}`);
}
const lead=combo[4]; if(!lead || lead.n===0n) throw new Error('S^4 coefficient vanished');
if(lead.n%31n===0n || lead.d%31n===0n) throw new Error('leading coefficient not a 31-adic unit');

const L=lambda.reduce((s,x)=>s+abs(x),0n);
if(L!==1122494243946194495979308283694611393383375844014083n) throw new Error('L mismatch');
const forcedProduct=433992707035920672833426144791n;
const lhs=powBig(forcedProduct,49*17);
const rhs11909=9n*powBig(L,17)*powBig(10n,2*11909);
const rhs11910=9n*powBig(L,17)*powBig(10n,2*11910);
if(!(lhs>rhs11909)) throw new Error('11909 lower bound failed');
if(!(lhs<rhs11910)) throw new Error('11910 threshold check failed');

console.log(JSON.stringify({
  checkpoint:'U87',
  lambda:lambda.map(String),
  lambdaL1:String(L),
  cancelledSCoefficients:[0,1,2,3],
  firstNonzeroSCoefficient:4,
  localYOrder:49,
  leadNumeratorDigits:lead.n.toString().replace('-','').length,
  leadDenominatorDigits:lead.d.toString().length,
  lead31AdicUnit:true,
  forcedProduct:String(forcedProduct),
  forcedProductPowerDividingInvariant:49,
  maxBaseStrictlyGreaterThanPowerOf10:11909,
  fullBealSolved:false,
},null,2));
