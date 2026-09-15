/** Exact U64 checks, independent of the Python square-multiplicity implementation. */
export {};
type Pair = readonly [bigint, bigint];
type Row = { U: bigint; V: bigint; Np: bigint; Np2: bigint; S: bigint; P: bigint };
type Quadratic = { linear: bigint; constant: bigint };
function ensure(condition: boolean, message: string): asserts condition {
  if (!condition) throw new Error(message);
}
function mod(n: bigint, p: bigint): bigint { return ((n % p) + p) % p; }
function power(n: bigint, e: bigint, p: bigint): bigint {
  ensure(e >= 0n && p > 1n, 'Invalid modular-power domain');
  let base = mod(n, p), k = e, out = 1n;
  while (k !== 0n) {
    if (k % 2n === 1n) out = mod(out * base, p);
    base = mod(base * base, p); k /= 2n;
  }
  return out;
}
function chi(n: bigint, p: bigint): bigint {
  const a = mod(n, p);
  if (a === 0n) return 0n;
  const out = power(a, (p - 1n) / 2n, p);
  ensure(out === 1n || out === p - 1n, 'Invalid quadratic character');
  return out === 1n ? 1n : -1n;
}
function f(x: bigint, u: bigint, v: bigint): bigint {
  return x**5n + 40n*u*v*x**3n + 320n*u*u*v*v*x + 64n*(8n*v**5n-u**5n);
}
function product(a: Pair, b: Pair, field: Quadratic): Pair {
  return [a[0]*b[0]-field.constant*a[1]*b[1],
    a[0]*b[1]+a[1]*b[0]-field.linear*a[1]*b[1]];
}
function tracePair(a: Pair, b: Pair, field: Quadratic): Pair {
  const prod = product(a, b, field);
  ensure(a[1]+b[1] === 0n && prod[1] === 0n, 'Pair is not conjugate');
  return [a[0]+b[0], prod[0]];
}
function fieldNorm(a: Pair, field: Quadratic): bigint {
  return a[0]*a[0]-field.linear*a[0]*a[1]+field.constant*a[1]*a[1];
}
function json(data: unknown): string {
  return JSON.stringify(data, (_key: string, value: unknown) =>
    typeof value === 'bigint' ? value.toString() : value, 2);
}
function sortInts(values: Iterable<bigint>): bigint[] {
  return [...values].sort((a, b) => a < b ? -1 : a > b ? 1 : 0);
}
function allRows(p: bigint): { rows: Row[]; toric: bigint } {
  ensure([11n,19n,31n,41n].includes(p), 'Only the specified prime domain is implemented');
  let d = 2n;
  while (chi(d,p) !== -1n) d++;
  const character = new Map<bigint, bigint>();
  for (let a=0n; a<p; a++) character.set(a, chi(a,p));
  function tableChi(a: bigint): bigint {
    const value = character.get(mod(a,p));
    ensure(value !== undefined, 'Incomplete character table');
    return value;
  }
  const sq = new Set<bigint>(), tw = new Set<bigint>();
  for (let a=0n; a<p; a++) { sq.add(mod(a*a,p)); tw.add(mod(2n*a*a,p)); }
  // Direct binomial expressions over F_p[j], j^2=d; no square enumeration.
  const powers: {x:Pair; cube:Pair; fifth:Pair}[] = [];
  for (let a=0n; a<p; a++) for (let b=0n; b<p; b++) {
    powers.push({x:[a,b],
      cube:[mod(a**3n+3n*d*a*b*b,p),mod(3n*a*a*b+d*b**3n,p)],
      fifth:[mod(a**5n+10n*d*a**3n*b*b+5n*d*d*a*b**4n,p),
             mod(5n*a**4n*b+10n*d*a*a*b**3n+d*d*b**5n,p)]});
  }
  const rows: Row[] = [];
  let toric=0n;
  for (const u of sortInts(sq)) for (const v of sortInts(tw)) {
    if (u === 0n && v === 0n) continue;
    if (mod(u**5n+8n*v**5n,p) === 0n) { toric++; continue; }
    let n1=p+1n, n2=p*p+1n;
    for (let x=0n; x<p; x++) n1 += tableChi(-f(x,u,v));
    const c3=40n*u*v, c1=320n*u*u*v*v, c0=64n*(8n*v**5n-u**5n);
    for (const z of powers) {
      const a=mod(-z.fifth[0]-c3*z.cube[0]-c1*z.x[0]-c0,p);
      const b=mod(-z.fifth[1]-c3*z.cube[1]-c1*z.x[1],p);
      // Chi_(p^2)(a+bj)=Chi_p(a^2-d b^2), including the zero element.
      n2 += tableChi(a*a-d*b*b);
    }
    const s=p+1n-n1, numerator=s*s-(p*p+1n-n2);
    ensure(numerator%2n === 0n, 'Nonintegral Euler coefficient');
    rows.push({U:u,V:v,Np:n1,Np2:n2,S:s,P:numerator/2n-2n*p});
  }
  return {rows,toric};
}
ensure(power(0n,0n,11n) === 1n && chi(0n,11n) === 0n, 'Zero conventions');
ensure(chi(5n,17n) === -1n, 'RM field is not inert at 17');
let pairCount=0n, roots=0n;
for (let u=0n; u<25n; u++) for (let v=0n; v<25n; v++) {
  if (mod(u**5n+8n*v**5n,5n) === 0n) continue;
  pairCount++;
  const c=f(-u-2n*v,u,v);
  ensure(c%5n === 0n && c%25n !== 0n, 'Eisenstein constant valuation');
  ensure(mod(c/5n-2n*(u**5n+8n*v**5n),5n) === 0n, 'Constant quotient');
  for (let x=0n; x<25n; x++) if (mod(f(x,u,v),25n) === 0n) roots++;
}
ensure(pairCount === 500n && roots === 0n, 'Complete mod25 domain');
ensure(f(-7n,1n,3n)%25n === 0n, 'Essential unit hypothesis');
const bfield: Quadratic = {linear:-9n,constant:19n};
const forms: readonly {suffix:string; field:Quadratic; a:Pair; b:Pair}[] = [
  {suffix:'a',field:{linear:1n,constant:-1n},a:[-1n,-1n],b:[0n,1n]},
  {suffix:'b',field:bfield,a:[9n,-1n],b:[0n,1n]},
  {suffix:'c',field:{linear:5n,constant:-5n},a:[-5n,-1n],b:[0n,1n]},
  {suffix:'d',field:{linear:1n,constant:-1n},a:[-1n,-1n],b:[0n,1n]},
  {suffix:'e',field:{linear:11n,constant:29n},a:[-11n,-1n],b:[0n,1n]},
  {suffix:'f',field:{linear:5n,constant:-5n},a:[-5n,-1n],b:[0n,1n]},
  {suffix:'g',field:{linear:1n,constant:-1n},a:[-1n,-1n],b:[0n,1n]},
];
const initial=allRows(11n);
const recovered=forms.map(rec => {
  const [s,p]=tracePair(rec.a,rec.b,rec.field);
  const matches=initial.rows.filter(r => mod(r.S-s,17n)===0n && mod(r.P-p,17n)===0n);
  return {suffix:rec.suffix,sum:s,product:p,compatible_parameter_pairs:matches.length};
});
ensure(recovered.filter(r=>r.compatible_parameter_pairs>0).map(r=>r.suffix).join(',') === 'b',
  'Unexpected recovered form survivor');
const bvalues: readonly {q:bigint; a:Pair; b:Pair}[] = [
  {q:11n,a:[9n,-1n],b:[0n,1n]}, {q:19n,a:[0n,0n],b:[0n,0n]},
  {q:31n,a:[-1n,-1n],b:[-10n,1n]}, {q:41n,a:[-50n,11n],b:[49n,-11n]},
];
const diagnostics=bvalues.map(rec => {
  const {q}=rec, [s,p]=tracePair(rec.a,rec.b,bfield);
  const domain=q===11n ? initial : allRows(q);
  const matches=domain.rows.filter(r => mod(r.S-s,17n)===0n && mod(r.P-p,17n)===0n);
  const boundary=domain.rows.find(r=>r.U===1n && r.V===0n);
  ensure(boundary!==undefined && boundary.S===s && boundary.P===p, 'Boundary mismatch');
  const aSquared=product(rec.a,rec.a,bfield);
  const toricNorm=fieldNorm([aSquared[0]-(q+1n)**2n,aSquared[1]],bfield);
  ensure(mod(toricNorm,17n)!==0n, 'Toric condition unexpectedly matches');
  const ratios=new Set(matches.filter(r=>r.U!==0n).map(r=>mod(r.V*power(r.U,q-2n,q),q)));
  return {prime:q,form_b_sum_product:[s,p],good_pairs:domain.rows.length,
    toric_nonzero_pairs:domain.toric,compatible_good_pairs:matches.length,boundary,
    compatible_V_over_U:sortInts(ratios),compatible_U_zero:matches.filter(r=>r.U===0n).length,
    toric_norm_mod17:mod(toricNorm,17n),rows:domain.rows};
});
console.log(json({checkpoint:'U64',status:'completed',full_Beal_solved:false,
  arithmetic:'TypeScript bigint; direct binomial expansions and norm characters',
  mod25:{parameter_pairs:pairCount,roots},prime11_recovered_forms:recovered,
  unchecked_orbits:['h'],form_b_diagnostics:diagnostics}));
