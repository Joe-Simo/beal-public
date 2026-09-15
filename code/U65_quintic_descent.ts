/** U65 exact checks. The mod-289 audit uses the unsplit degree-five algebra,
 * unlike Python's separate linear/quartic Fermat quotients. */
export {};
type Poly = readonly bigint[];
type SieveRow = { a: bigint; b: bigint; U: bigint; V: bigint; gaussian_witnesses: bigint[][] };
function ensure(condition: boolean, message: string): asserts condition {
  if (!condition) throw new Error(message);
}
const mod = (a: bigint, m: bigint): bigint => ((a % m) + m) % m;
const coefficient = (a: Poly, i: number): bigint => a[i] ?? 0n;
function scalarPower(a: bigint, n: bigint, m: bigint): bigint {
  ensure(n >= 0n && m > 1n, 'Invalid modular power');
  let out = 1n, base = mod(a, m), k = n;
  while (k > 0n) {
    if (k % 2n) out = mod(out * base, m);
    base = mod(base * base, m); k /= 2n;
  }
  return out;
}
function ringProduct(a: Poly, b: Poly, f: Poly, m: bigint | null): bigint[] {
  const degree = f.length - 1;
  ensure(coefficient(f, degree) === 1n && a.length <= degree && b.length <= degree,
    'The quotient polynomial must be monic');
  const result = Array<bigint>(2 * degree - 1).fill(0n);
  for (let i = 0; i < a.length; i++) for (let j = 0; j < b.length; j++)
    result[i+j] = coefficient(result,i+j) + coefficient(a,i)*coefficient(b,j);
  for (let k = result.length-1; k >= degree; k--) {
    const leading = coefficient(result,k);
    for (let j = 0; j < degree; j++)
      result[k-degree+j] = coefficient(result,k-degree+j)-leading*coefficient(f,j);
  }
  return result.slice(0,degree).map(x => m === null ? x : mod(x,m));
}
function ringPower(a: Poly, n: bigint, f: Poly, m: bigint | null): bigint[] {
  ensure(n >= 0n, 'Negative quotient-algebra exponent');
  let out: bigint[] = [1n], base = [...a], k = n;
  while (k > 0n) {
    if (k % 2n) out = ringProduct(out,base,f,m);
    base = ringProduct(base,base,f,m); k /= 2n;
  }
  return Array.from({length:f.length-1},(_,i) => coefficient(out,i));
}
function determinant(input: readonly Poly[]): bigint {
  const a = input.map(r => [...r]); const n = a.length;
  ensure(a.every(r => r.length === n), 'Nonsquare determinant');
  let previous = 1n, sign = 1n;
  for (let k=0; k<n-1; k++) {
    let row=k; while (row<n && coefficient(a[row] ?? [],k)===0n) row++;
    if (row === n) return 0n;
    if (row !== k) { const temp=a[k]; a[k]=a[row]!; a[row]=temp!; sign=-sign; }
    const pivot=coefficient(a[k]!,k);
    for (let i=k+1; i<n; i++) for (let j=k+1; j<n; j++) {
      const numerator=coefficient(a[i]!,j)*pivot-coefficient(a[i]!,k)*coefficient(a[k]!,j);
      ensure(numerator%previous===0n,'Nonexact Bareiss division');
      a[i]![j]=numerator/previous;
    }
    for (let i=k+1; i<n; i++) a[i]![k]=0n;
    previous=pivot;
  }
  return sign*coefficient(a[n-1]!,n-1);
}
const defining: Poly=[-2n,0n,0n,0n,0n,1n];
function fieldNorm(a: Poly): bigint {
  const columns = Array.from({length:5},(_,j) => {
    const basis=Array<bigint>(5).fill(0n); basis[j]=1n;
    return ringProduct(a,basis,defining,null);
  });
  return determinant(Array.from({length:5},(_,i) => columns.map(c => coefficient(c,i))));
}
const generators: Poly[]=[[0n,1n],[1n,1n],[1n,0n,1n],[1n,1n,1n],[1n,0n,0n,1n,-1n]];
const generatorNorms=generators.map(fieldNorm);
ensure(generatorNorms.join(',')==='2,3,5,7,13','Norm generator certificate');
ensure(fieldNorm([2n**60n,1n])===(2n**60n)**5n+2n,'Beyond-safe-integer norm test');
ensure(scalarPower(0n,0n,17n)===1n && mod(-1n,17n)===16n,'Arithmetic boundary conventions');
ensure(ringPower([0n,1n,0n,0n,0n],17n**4n,defining,17n).join(',')==='0,1,0,0,0',
  'Frobenius^4 on the full residue algebra');
const e1: Poly=[-1n,1n,0n,0n,0n], e2: Poly=[1n,1n,0n,1n,0n];
ensure(fieldNorm(e1)===1n && fieldNorm(e2)===1n,'Unit norms');
// This is an identity certificate, not an integer-height search: both sides
// have degree at most 10 in each variable, and 11 distinct values are used.
for (let u=-5n;u<=5n;u++) for (let v=-5n;v<=5n;v++) {
  const root: Poly=[0n,2n*u,0n,0n,-2n*v];
  const powers=Array.from({length:5},(_,j)=>ringPower(root,BigInt(j),defining,null));
  const matrix=Array.from({length:5},(_,i)=>powers.map(c=>coefficient(c,i)));
  ensure(determinant(matrix)===1024n*(u**5n+8n*v**5n)**2n,'Index identity grid');
  ensure(fieldNorm([u,0n,0n,v,0n])===u**5n+8n*v**5n,'Norm identity grid');
}
// Both q=11 Hecke entries satisfy this same quadratic, in the quartic Hecke field.
const h: Poly=[241n,190n,-13n,-10n,1n];
const numerator: Poly=[120n,18n,15n,-2n];
const nSquared=ringProduct(numerator,numerator,h,null);
ensure(nSquared.every((x,i)=>x-455n*coefficient(numerator,i)+(i===0?5n*91n**2n:0n)===0n),
  'Hecke quadratic identity');
// Complete exact common-root test in F_17[j], j^2=3. All quadratics here
// split over this field; the field itself is checked by scalar nonresiduosity.
ensure(scalarPower(3n,8n,17n)===16n,'Quadratic extension definition');
const quadratic: Poly=[-3n,0n,1n];
const freyPairs: readonly (readonly [bigint,bigint])[]=[[-3n,-9n],[1n,-1n],[9n,19n]];
const common=Array<number>(3).fill(0); let hRoots=0;
for (let x=0n;x<17n;x++) for (let y=0n;y<17n;y++) {
  const a:Poly=[x,y], square=ringProduct(a,a,quadratic,17n);
  const isH=mod(coefficient(square,0)-5n*x+5n,17n)===0n &&
    mod(coefficient(square,1)-5n*y,17n)===0n;
  if (!isH) continue; hRoots++;
  freyPairs.forEach(([s,p],j)=>{
    if (mod(coefficient(square,0)-s*x+p,17n)===0n &&
        mod(coefficient(square,1)-s*y,17n)===0n) common[j]=(common[j] ?? 0)+1;
  });
}
ensure(hRoots===2 && common.every(c=>c===0),'h must be excluded at every embedding');
const unitCharacters = [
  {p:103n,root:17n,generator:64n}, {p:137n,root:9n,generator:119n},
].map(({p,root,generator})=>{
  ensure(scalarPower(root,5n,p)===2n && scalarPower(generator,17n,p)===1n && generator!==1n,
    'Character definitions');
  const log=new Map<bigint,bigint>();
  for (let i=0n;i<17n;i++) log.set(scalarPower(generator,i,p),i);
  ensure(log.size===17,'Incomplete character image');
  const values=[scalarPower(root-1n,(p-1n)/17n,p),scalarPower(root**3n+root+1n,(p-1n)/17n,p)];
  const logs=values.map(v=>{const a=log.get(v);ensure(a!==undefined,'No discrete log');return a;});
  return {p,root,generator,values,logs};
});
const first=unitCharacters[0]!.logs,second=unitCharacters[1]!.logs;
ensure(mod(coefficient(first,0)*coefficient(second,1)-coefficient(first,1)*coefficient(second,0),17n)===4n,
  'Unit-basis determinant');

const p=17n,m=289n,q4=17n**4n;
function quotientLog(a: Poly): bigint[] {
  return ringPower(a,q4-1n,defining,m).map((v,i)=>{
    const difference=mod(v-(i===0?1n:0n),m);
    ensure(difference%p===0n,'A unit failed the residue Frobenius test');
    return difference/p;
  });
}
const l1=quotientLog(e1),l2=quotientLog(e2);
function unitClass(gamma: Poly): readonly [bigint,bigint] | null {
  const gq=ringPower(gamma,q4,defining,m);
  const target=gq.map((v,i)=>{
    const diff=mod(v-coefficient(gamma,i),m);
    ensure(diff%p===0n,'Frobenius^4 is not the identity in the residue algebra');
    return diff/p;
  });
  const c1=ringProduct(gamma,l1,defining,p),c2=ringProduct(gamma,l2,defining,p);
  for (let i=0;i<5;i++) for (let j=i+1;j<5;j++) {
    const det=mod(coefficient(c1,i)*coefficient(c2,j)-coefficient(c1,j)*coefficient(c2,i),p);
    if (det===0n) continue;
    const inv=scalarPower(det,p-2n,p);
    const a=mod((coefficient(target,i)*coefficient(c2,j)-coefficient(target,j)*coefficient(c2,i))*inv,p);
    const b=mod((coefficient(c1,i)*coefficient(target,j)-coefficient(c1,j)*coefficient(target,i))*inv,p);
    return target.every((v,k)=>mod(a*coefficient(c1,k)+b*coefficient(c2,k)-v,p)===0n)?[a,b]:null;
  }
  throw new Error('Unexpected rank loss; the primitive domain must not be pruned');
}
const rootsX=new Map<bigint,bigint[]>(),rootsY=new Map<bigint,bigint[]>(),scalarImages=new Set<bigint>();
for (let x=0n;x<m;x++) {
  const u=mod(x*x,m),v=mod(2n*x*x,m);
  rootsX.set(u,[...(rootsX.get(u)??[]),x]); rootsY.set(v,[...(rootsY.get(v)??[]),x]);
  scalarImages.add(scalarPower(x,p,m));
}
ensure(rootsX.size===137 && rootsY.size===137 && scalarImages.size===17,'Full square/power domains');
const sorted=(values:Iterable<bigint>):bigint[]=>[...values].sort((a,b)=>a<b?-1:a>b?1:0);
let normCount=0n,gaussianCount=0n;
const sieveRows:SieveRow[]=[];
const gaussian:Poly=[1n,0n,1n];
for (const u of sorted(rootsX.keys())) for (const v of sorted(rootsY.keys())) {
  if (u%p===0n && v%p===0n) continue;
  if (!scalarImages.has(mod(u**5n+8n*v**5n,m))) continue;
  normCount++;
  const ab=unitClass([u,0n,0n,v,0n]); if (ab===null) continue;
  const witnesses:bigint[][]=[];
  for (const x of rootsX.get(u)??[]) for (const y of rootsY.get(v)??[]) {
    const g:Poly=[scalarPower(x,5n,m),mod(16n*scalarPower(y,5n,m),m)];
    const gp=ringPower(g,p,gaussian,m);
    if (gp.every((value,i)=>value===coefficient(g,i))) witnesses.push([x,y]);
  }
  gaussianCount+=BigInt(witnesses.length);
  sieveRows.push({a:ab[0],b:ab[1],U:u,V:v,gaussian_witnesses:witnesses});
}
const before=[...new Set(sieveRows.map(r=>`${r.a},${r.b}`))].sort();
const after=[...new Set(sieveRows.filter(r=>r.gaussian_witnesses.length>0).map(r=>`${r.a},${r.b}`))].sort();
ensure(normCount===1104n && sieveRows.length===24,'Unsplit-algebra count');
ensure(before.join(';')==='0,0;0,14' && after.join(';')==='0,0','Unit ambiguity not eliminated');
ensure(gaussianCount===544n && sieveRows.filter(r=>r.gaussian_witnesses.length>0).length===16,
  'Gaussian enumeration');
ensure(sieveRows.filter(r=>r.gaussian_witnesses.length>0).every(r=>(r.U===0n)!==(r.V===0n)),
  'The surviving residues must be on exactly one axis');
console.log(JSON.stringify({checkpoint:'U65',status:'completed',full_Beal_solved:false,
  h_roots_mod17_squared:hRoots,common_roots_with_Frey_quadratics:common,
  generator_norms:generatorNorms,polynomial_identity_grid:{degree_bound_each_variable:10,grid_size:121},
  unit_basis_characters:unitCharacters,unsplit_unit_logs:[l1,l2],
  sieve:{modulus:m,square_parameter_pairs:18768,norm_17th_power_pairs:normCount,
    two_component_pairs:sieveRows.length,classes_before_gaussian:before,classes_after_gaussian:after,
    gaussian_parameter_pairs:16,gaussian_root_pairs:gaussianCount,rows:sieveRows}},
  (_key:string,value:unknown)=>typeof value==='bigint'?value.toString():value,2));
