export {};

type Cycles = number[];
const units10 = [1, 3, 7, 9] as const;
function mod(a: number, n: number): number { const r=a%n; return r<0?r+n:r; }
function cycleLengths(a:number,t:number):Cycles {
  const seen=Array<boolean>(10).fill(false); const out:number[]=[];
  for(let s=0;s<10;s++){ if(seen[s]) continue; let j=s,n=0; while(!seen[j]){seen[j]=true;n++;j=mod(a*j+t,10);} out.push(n); }
  return out.sort((u,v)=>u-v);
}
const cycles:Cycles[]=[];
for(const a of units10) for(let t=0;t<10;t++) cycles.push(cycleLengths(a,t));
if(cycles.length!==40) throw new Error('group size');
function key(c:Cycles):string{return c.join(',');}
const hist=new Map<string,number>(); for(const c of cycles) hist.set(key(c),(hist.get(key(c))??0)+1);
const expected=new Map<string,number>([
['1,1,1,1,1,1,1,1,1,1',1],['10',4],['5,5',4],['2,2,2,2,2',6],['1,1,4,4',10],['2,4,4',10],['1,1,2,2,2,2',5]
]);
for(const [k,v] of expected) if(hist.get(k)!==v) throw new Error(`hist ${k}`);
function cleanCount(r:number):number{return cycles.filter(c=>c.every(d=>d%r!==0)).length;}
const cleanOrders=[1,2,4,8,16] as const;
const clean = new Map<number,number>(cleanOrders.map(r=>[r,cleanCount(r)] as const));
for (const [r,n] of [[1,0],[2,5],[4,20],[8,40],[16,40]] as const) if(clean.get(r)!==n) throw new Error(`clean ${r}`);
const c10=hist.get('10')??0, c55=hist.get('5,5')??0;
function cc(r:number):number { const n=clean.get(r); if(n===undefined) throw new Error(`missing ${r}`); return n; }
// Strong: all U81-clean classes plus the order-1/cycle-10 class.
const strongNumerator=(cc(1)+c10)+cc(2)+2*cc(4)+4*cc(8)+8*cc(16);
// Semi: the disjoint order-1/(5,5) and order-2/(10) classes.
const semiNumerator=c55+c10;
const denominator=16*40;
if(strongNumerator!==529 || semiNumerator!==8 || denominator!==640) throw new Error('density numerators');
if(denominator-strongNumerator-semiNumerator!==103) throw new Error('remainder');
console.log(JSON.stringify({checkpoint:'U82',cycleTypes:Object.fromEntries([...hist.entries()].sort()),cleanCounts:Object.fromEntries(clean),strongDensity:'529/640',semiDensity:'1/80',controlledUnionDensity:'537/640',uncontrolledDensity:'103/640',fullBealSolved:false},null,2));
