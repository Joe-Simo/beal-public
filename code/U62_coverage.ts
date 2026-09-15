/** Full-scale residue certificates for U62; not a proof of the full Beal conjecture. */
type Pair = readonly [bigint, bigint];
type Relation = readonly [bigint, bigint];
const gaussian: Relation = [-1n, 0n];
const golden: Relation = [1n, 1n];
function requireTrue(ok: boolean, message: string): asserts ok {
  if (!ok) throw new Error(message);
}
function mod(a: bigint, q: bigint): bigint { return ((a % q) + q) % q; }
function times(x: Pair, y: Pair, relation: Relation, q: bigint): Pair {
  return [mod(x[0]*y[0]+relation[0]*x[1]*y[1],q),
    mod(x[0]*y[1]+x[1]*y[0]+relation[1]*x[1]*y[1],q)];
}
function power(x: Pair, n: bigint, relation: Relation, q: bigint): Pair {
  requireTrue(n>=0n, "Negative exponent");
  let out: Pair=[1n,0n], base=x, e=n;
  while(e>0n) {
    if(e%2n===1n) out=times(out,base,relation,q);
    base=times(base,base,relation,q); e/=2n;
  }
  return out;
}
function scalarPower(a: bigint, n: bigint, q: bigint): bigint {
  return power([a,0n],n,golden,q)[0];
}
function key(x: Pair): string { return `${x[0]},${x[1]}`; }
function h(x: Pair,q: bigint): Pair {
  const [m,n]=x;
  return [mod(m**4n+30n*m*m*n*n+n**4n,q),mod(-16n*m*m*n*n,q)];
}
function norm(x: Pair,relation: Relation,q: bigint): bigint {
  return mod(x[0]*x[0]+relation[1]*x[0]*x[1]-relation[0]*x[1]*x[1],q);
}
function allImages(q: bigint,relation: Relation): Pair[] {
  const image=new Map<string,Pair>();
  for(let a=0n;a<q;a++) for(let b=0n;b<q;b++) {
    const value=power([a,b],17n,relation,q); image.set(key(value),value);
  }
  return [...image.values()];
}
function roots(q: bigint,relation: Relation): bigint[] {
  const result: bigint[]=[];
  for(let t=0n;t<q;t++) if(mod(t*t-relation[1]*t-relation[0],q)===0n) result.push(t);
  return result;
}
function splitImages(q: bigint,relation: Relation): Pair[] {
  const rs=roots(q,relation), root0=rs[0], root1=rs[1];
  requireTrue(rs.length===2 && root0!==undefined && root1!==undefined,"Expected split algebra");
  const inverse=scalarPower(mod(root0-root1,q),q-2n,q);
  requireTrue(mod(inverse*(root0-root1),q)===1n,"Exact inverse check");
  const scalarSet=new Set<bigint>();
  for(let a=0n;a<q;a++) scalarSet.add(scalarPower(a,17n,q));
  const out: Pair[]=[];
  for(const x0 of scalarSet) for(const x1 of scalarSet) {
    const b=mod((x0-x1)*inverse,q), a=mod(x0-b*root0,q);
    requireTrue(mod(a+b*root1,q)===x1,"Split reconstruction");
    out.push([a,b]);
  }
  return out;
}
function sieve(q: bigint,classes: readonly number[]) {
  const fullGaussian=q===409n?splitImages(q,gaussian):allImages(q,gaussian);
  const alpha=q===409n?splitImages(q,golden):allImages(q,golden);
  const gi=fullGaussian.filter(([a,b])=>a!==0n||b!==0n);
  const rows=classes.map(k=>{
    const unit=power([0n,1n],BigInt(k),golden,q);
    const targets=new Set(alpha.map(a=>key(times(unit,a,golden,q))));
    const kept=gi.filter(z=>targets.has(key(h(z,q))));
    return {k,compatible_count:kept.length,
      axis_count:kept.filter(([m,n])=>mod(m*n,q)===0n).length,
      diagonal_count:kept.filter(([m,n])=>mod((m-n)*(m+n),q)===0n).length,
      zero_norm_gaussian_survivors:kept.filter(z=>norm(z,gaussian,q)===0n).length};
  });
  return {q:q.toString(),nonzero_gaussian_image_size:gi.length,quadratic_image_size:alpha.length,
    nonzero_zero_norm_gaussian_images:gi.filter(z=>norm(z,gaussian,q)===0n).length,rows};
}
const first=sieve(67n,Array.from({length:17},(_,i)=>i));
const second=sieve(409n,[0,15]);
requireTrue(JSON.stringify(first.rows.filter(x=>x.compatible_count).map(x=>[x.k,x.compatible_count,x.axis_count,x.diagonal_count]))===JSON.stringify([[0,132,132,0],[15,132,0,132]]),"q67 full unit classification");
requireTrue(JSON.stringify(second.rows.map(x=>[x.k,x.compatible_count,x.axis_count]))===JSON.stringify([[0,48,48],[15,0,0]]),"q409 full unit classification");
requireTrue(second.nonzero_gaussian_image_size===624 && second.quadratic_image_size===625,"All split outputs including zero divisors");
requireTrue(second.nonzero_zero_norm_gaussian_images===48,"Zero norm outputs were retained");
console.log(JSON.stringify({status:"completed",arithmetic:"TypeScript bigint",unit_sieves:[first,second],full_Beal_solved:false},null,2));
