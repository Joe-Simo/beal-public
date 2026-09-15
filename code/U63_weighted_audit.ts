/** U63: independent exact finite checks using bigint and quadratic characters. */
export {};
type Pair = readonly [bigint, bigint];
type Row = { U: bigint; V: bigint; N11: bigint; N121: bigint;
  N11_negative_twist: bigint; S: bigint; P: bigint; D: bigint };
type HistogramRow = [bigint, bigint, bigint, bigint];
function requireTrue(condition: boolean, message: string): asserts condition {
  if (!condition) throw new Error(message);
}
function mod(n: bigint, p: bigint): bigint { return ((n % p) + p) % p; }
function power(n: bigint, e: bigint, p: bigint): bigint {
  requireTrue(e >= 0n && p > 0n, 'Invalid modular-power arguments');
  let out = 1n, base = mod(n, p), k = e;
  while (k > 0n) {
    if (k % 2n !== 0n) out = mod(out * base, p);
    base = mod(base * base, p);
    k /= 2n;
  }
  return out;
}
function chi(n: bigint, p: bigint): bigint {
  const reduced = mod(n, p);
  if (reduced === 0n) return 0n;
  const symbol = power(reduced, (p - 1n) / 2n, p);
  requireTrue(symbol === 1n || symbol === p - 1n, 'Non-prime input or character error');
  return symbol === 1n ? 1n : -1n;
}
function f(x: bigint, u: bigint, v: bigint): bigint {
  return x**5n + 40n*u*v*x**3n + 320n*u*u*v*v*x + 64n*(8n*v**5n-u**5n);
}
// Direct real/imaginary binomial expressions, rather than Python's pair multiplication.
function coefficients(x: bigint, y: bigint, u: bigint, v: bigint): Pair {
  const a = x**5n-10n*x**3n*y*y+5n*x*y**4n
    +40n*u*v*(x**3n-3n*x*y*y)+320n*u*u*v*v*x+64n*(8n*v**5n-u**5n);
  const b = 5n*x**4n*y-10n*x*x*y**3n+y**5n
    +40n*u*v*(3n*x*x*y-y**3n)+320n*u*u*v*v*y;
  return [a, b];
}
function histogram(rows: readonly Row[], sign: bigint): HistogramRow[] {
  const counts = new Map<string, HistogramRow>();
  for (const r of rows) {
    const s = sign*r.S, key = `${s},${r.P},${r.D}`;
    const old = counts.get(key);
    if (old) old[3] += 1n;
    else counts.set(key, [s, r.P, r.D, 1n]);
  }
  return [...counts.values()].sort((a,b) => a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0);
}
function json(data: unknown): string {
  return JSON.stringify(data, (_key: string, value: unknown) =>
    typeof value === 'bigint' ? value.toString() : value, 2);
}
const q = 11n;
requireTrue(chi(-1n,q) === -1n, 'i^2+1 must be irreducible');
requireTrue(chi(5n,17n) === -1n, 'Inert RM coefficient field at 17');
requireTrue(power(0n,0n,q) === 1n && chi(0n,q) === 0n, 'Zero conventions');
const squares = new Set<bigint>(), twiceSquares = new Set<bigint>();
for (let a=0n; a<q; a++) { squares.add(mod(a*a,q)); twiceSquares.add(mod(2n*a*a,q)); }
const rows: Row[] = [];
for (let u=0n; u<q; u++) for (let v=0n; v<q; v++) {
  if (u === 0n && v === 0n) continue;
  requireTrue(mod(u**5n+8n*v**5n,q) !== 0n, 'Unexpected toric case in F11');
  let n1=q+1n, n1Twist=q+1n, n2=q*q+1n;
  for (let x=0n; x<q; x++) {
    n1 += chi(f(x,u,v),q); n1Twist += chi(-f(x,u,v),q);
    for (let y=0n; y<q; y++) {
      const [a,b] = coefficients(x,y,u,v);
      // The quadratic character over F_(q^2) is the F_q character of the norm.
      n2 += chi(a*a+b*b,q);
    }
  }
  requireTrue(n1+n1Twist === 2n*(q+1n), 'Quadratic twist sum identity');
  const s=q+1n-n1, numerator=s*s-(q*q+1n-n2);
  requireTrue(numerator % 2n === 0n, 'Nonintegral Euler coefficient');
  const p=numerator/2n-2n*q;
  rows.push({U:u,V:v,N11:n1,N121:n2,N11_negative_twist:n1Twist,S:s,P:p,D:s*s-4n*p});
}
const structured = rows.filter(r => squares.has(r.U) && twiceSquares.has(r.V));
requireTrue(rows.length === 120 && structured.length === 35, 'Complete domains');
const expected: HistogramRow[] = [[-9n,19n,5n,5n],[-1n,-1n,5n,5n],[3n,-9n,45n,25n]];
requireTrue(json(histogram(structured,1n)) === json(expected), 'Square-structured trace inventory');
const witness=rows.find(r => r.U === 0n && r.V === 2n);
requireTrue(witness !== undefined && witness.N11 === 13n && witness.N121 === 163n
  && witness.S === -1n && witness.P === -1n, 'Counterexample to U41 nonmatching claim');
requireTrue(mod(256n-power(5n,17n,q),q) === 0n, 'Original weighted congruence at witness');
requireTrue(histogram(structured,-1n).every(r => mod(r[0]+1n,17n) !== 0n),
  'Repaired-twist rational trace must exclude form a in this domain');
// In the e^2+e-1 algebra, e*(-e-1)=-1, and the sum is -1.
function mulEigen(x: Pair,y: Pair): Pair {
  return [mod(x[0]*y[0]+x[1]*y[1],17n),mod(x[0]*y[1]+x[1]*y[0]-x[1]*y[1],17n)];
}
requireTrue(json(mulEigen([0n,1n],[-1n,-1n])) === json([16n,0n]), 'Hecke pair product');

const sq125=new Set<bigint>(), twice125=new Set<bigint>();
for (let x=0n; x<125n; x++) { sq125.add(mod(x*x,125n)); twice125.add(mod(2n*x*x,125n)); }
let pairs125=0n, roots125=0n, vDiv5=0n;
for (const u of sq125) for (const v of twice125) {
  if (mod(u**5n+8n*v**5n,5n) === 0n) continue;
  pairs125++; if (v%5n === 0n) vDiv5++;
  for (let x=0n; x<125n; x++) if (mod(f(x,u,v),125n) === 0n) roots125++;
}
requireTrue(sq125.size === 53 && twice125.size === 53 && pairs125 === 1550n
  && roots125 === 0n && vDiv5 === 150n, 'Complete mod125 root test');
const squareClasses=new Set<string>();
for (let a=0n; a<4n; a++) for (let b=0n; b<4n; b++) {
  squareClasses.add(`${mod(a*a+b*b,4n)},${mod(2n*a*b+b*b,4n)}`);
}
requireTrue([...squareClasses].sort().join(';') === '0,0;1,0;1,1;2,3', 'Quadratic ring squares');
requireTrue(!squareClasses.has('3,0'), 'Normalized constant is not a square mod4');
console.log(json({checkpoint:'U63',status:'completed',arithmetic:'TypeScript bigint',full_Beal_solved:false,
  prime11:{all_pairs:rows.length,structured_pairs:structured.length,rows,
    all_trace_distribution:histogram(rows,1n),structured_plus_f:histogram(structured,1n),
    structured_minus_f:histogram(structured,-1n),U41_nonmatching_counterexample:witness,
    correct_form_a_sum_product:[-1n,-1n],form_a_excluded_after_repair_in_square_domain:true},
  mod125:{square_residues:sq125.size,pairs:pairs125,tested_x_per_pair:125n,
    root_count:roots125,subdomain_5_divides_V_pairs:vDiv5},
  mod4_quadratic_squares:[...squareClasses].sort()}));
