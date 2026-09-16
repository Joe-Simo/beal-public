export {};

type Pair = readonly [number, number];
const units10 = [1, 3, 7, 9] as const;
function mod(a:number,n:number):number { const r=a%n; return r<0?r+n:r; }
function canonical(i:number,j:number):Pair { const a=mod(i,10), b=mod(j,10); return a<b?[a,b]:[b,a]; }
function key(p:Pair):string { return `${p[0]},${p[1]}`; }
function distance(p:Pair):number { const d=mod(p[1]-p[0],10); return Math.min(d,10-d); }
const group = units10.flatMap((a)=>Array.from({length:10},(_,t)=>({a,t})));
if(group.length!==40) throw new Error('group size');
const pairs:Pair[]=[];
for(let i=0;i<10;i++) for(let j=i+1;j<10;j++) pairs.push([i,j]);
if(pairs.length!==45) throw new Error('pair count');
const unseen=new Map(pairs.map((p)=>[key(p),p]));
const orbits:Pair[][]=[];
while(unseen.size){
  const p=unseen.values().next().value as Pair;
  const om=new Map<string,Pair>();
  for(const {a,t} of group){ const q=canonical(a*p[0]+t,a*p[1]+t); om.set(key(q),q); }
  const o=[...om.values()];
  for(const q of o) unseen.delete(key(q));
  orbits.push(o);
}
const summary=orbits.map((o)=>({size:o.length,distances:[...new Set(o.map(distance))].sort((a,b)=>a-b)})).sort((a,b)=>{
  const ad=a.distances[0] ?? -1; const bd=b.distances[0] ?? -1;
  return a.size-b.size || ad-bd;
});
const expected=JSON.stringify([{size:5,distances:[5]},{size:20,distances:[1,3]},{size:20,distances:[2,4]}]);
if(JSON.stringify(summary)!==expected) throw new Error(`orbit summary ${JSON.stringify(summary)}`);
const chosen=orbits.find((o)=>o.length===20 && new Set(o.map(distance)).has(1));
if(!chosen || chosen.length!==20) throw new Error('missing odd-distance orbit');
if(chosen.length<=17) throw new Error('pigeonhole needs >17 pair products');
const minimumCoincidentPairs=chosen.length-17;
if(minimumCoincidentPairs!==3) throw new Error('collision lower bound');
const minimumDiscriminantValuationMultiplier=2*minimumCoincidentPairs;
if(minimumDiscriminantValuationMultiplier!==6) throw new Error('valuation multiplier');
const discriminantDifferencePairs=chosen.length*(chosen.length-1)/2;
if(discriminantDifferencePairs!==190) throw new Error('discriminant pair count');
const squaredDifferenceFactors=2*discriminantDifferencePairs;
const thetaMagnitudeExponent=2*squaredDifferenceFactors;
if(squaredDifferenceFactors!==380 || thetaMagnitudeExponent!==760) throw new Error('height exponents');
console.log(JSON.stringify({checkpoint:'U84',pairOrbits:summary,chosenOrbitSize:chosen.length,seventeenthPowerValues:17,pigeonhole:true,minimumCoincidentPairs,minimumDiscriminantValuationMultiplier,discriminantDifferencePairs,squaredDifferenceFactors,thetaMagnitudeExponent,fullBealSolved:false},null,2));
