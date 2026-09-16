export {};

const units10 = [1, 3, 7, 9] as const;
const orders17 = [1, 2, 4, 8, 16] as const;

function mod(a:number,n:number):number { const r=a%n; return r<0?r+n:r; }
function powMod(base:number, exponent:number, modulus:number):number {
  let b=mod(base,modulus), e=exponent, out=1;
  while(e>0){ if((e&1)!==0) out=(out*b)%modulus; b=(b*b)%modulus; e>>=1; }
  return out;
}
function order17(h:number):number {
  for(const r of orders17) if(powMod(h,r,17)===1) return r;
  throw new Error(`no order for ${h}`);
}
function cycles(a:number,t:number):number[] {
  const seen=Array<boolean>(10).fill(false); const out:number[]=[];
  for(let s=0;s<10;s++){
    if(seen[s]) continue;
    let j=s,n=0;
    while(!seen[j]){ seen[j]=true; n++; j=mod(a*j+t,10); }
    out.push(n);
  }
  return out.sort((x,y)=>x-y);
}
function clean(cs:number[],r:number):boolean { return cs.every((d)=>d%r!==0); }
function ckey(cs:number[]):string { return cs.join(','); }

const counts=new Map<string,number>([['strong',0],['semi',0],['weak',0],['uncontrolled',0]]);
for(const a of units10) for(let t=0;t<10;t++){
  const cs=cycles(a,t);
  for(let h=1;h<17;h++){
    const r=order17(h);
    const strong=clean(cs,r)||(r===1&&ckey(cs)==='10');
    const semi=!strong&&((r===1&&ckey(cs)==='5,5')||(r===2&&ckey(cs)==='10'));
    const weak=!strong&&!semi&&r===1&&(t&1)===1;
    const k=strong?'strong':semi?'semi':weak?'weak':'uncontrolled';
    counts.set(k,(counts.get(k)??0)+1);
  }
}
for(const [k,v] of [['strong',529],['semi',8],['weak',16],['uncontrolled',87]] as const){
  if(counts.get(k)!==v) throw new Error(`count ${k}`);
}

// c^10=-256.  c^3 is the canonical local 17th-root twist for q|X because
// (c^3)^17 = c^51 = (-256)^5 c.
if(mod(3*17,10)!==1) throw new Error('c^3 exponent');
// Multiplying by c^7 clears that denominator globally: 7*17+1 = 120 is divisible by 10.
if(mod(7*17+1,10)!==0) throw new Error('c^7 normalization');

// For delta in span{c^3,c^8}, the c^4 and c^9 coefficients have first possible
// perturbation indices min(9,4)=4.  If the c^8 term vanishes, coefficient c^8
// has no n=0 contribution and begins at n>=1.
const semiFirstIndices={a4:Math.min(mod(3-4,10),mod(8-4,10)),a9:Math.min(mod(3-9,10),mod(8-9,10))};
if(semiFirstIndices.a4!==4||semiFirstIndices.a9!==4) throw new Error('semi first indices');
const weakFirstIndexA8=1;

const orderedRatios=10*9;
const bins=17;
const low=Math.floor(orderedRatios/bins), highBins=orderedRatios%bins;
const collisions=highBins*((low+1)*low/2)+(bins-highBins)*(low*(low-1)/2);
if(collisions!==195) throw new Error('ratio collisions');
const valuationMultiplier=2*collisions;
if(valuationMultiplier!==390) throw new Error('ratio multiplier');

console.log(JSON.stringify({checkpoint:'U86',categoryCounts:Object.fromEntries(counts),c3RootIdentityExponent:51,c7ClearingExponent:120,semiFirstIndices,weakFirstIndexA8,orderedRatios,minimumRatioCollisions:collisions,valuationMultiplier,fullBealSolved:false},null,2));
