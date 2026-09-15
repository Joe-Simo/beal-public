/** U67: distinct exact quotient-ring and residue checks. Not a full proof checker. */
type Poly = readonly bigint[];
const assert: (condition: boolean, message: string) => asserts condition = (condition, message) => {
  if (!condition) throw new Error(message);
};
const mod = (a: bigint, n: bigint): bigint => ((a % n) + n) % n;
function power(a: bigint, e: bigint, n: bigint): bigint {
  assert(e >= 0n && n > 1n, 'Power domain');
  let out = 1n;
  a = mod(a, n);
  while (e > 0n) {
    if ((e & 1n) !== 0n) out = out * a % n;
    a = a * a % n;
    e >>= 1n;
  }
  return out;
}
function inverse(a: bigint, n: bigint): bigint {
  let r = n; let s = mod(a, n); let t = 0n; let u = 1n;
  while (s !== 0n) {
    const q = r / s;
    [r, s] = [s, r - q * s];
    [t, u] = [u, t - q * u];
  }
  assert(r === 1n, 'Nonunit inverse');
  return mod(t, n);
}
function prime(n: bigint): boolean {
  if (n < 2n) return false;
  for (let d = 2n; d * d <= n; d++) if (n % d === 0n) return false;
  return true;
}
function reduce(a: Poly, f: Poly): bigint[] {
  const out = [...a]; const degree = f.length - 1;
  assert(f[degree] === 1n, 'Monic polynomial required');
  while (out.length < degree) out.push(0n);
  for (let k = out.length - 1; k >= degree; k--) {
    const leading = out[k]!;
    for (let j = 0; j < degree; j++) out[k - degree + j] = out[k - degree + j]! - leading * f[j]!;
  }
  return out.slice(0, degree);
}
function multiply(a: Poly, b: Poly, f: Poly): bigint[] {
  const out: bigint[] = Array.from({length: a.length + b.length - 1}, () => 0n);
  for (let i = 0; i < a.length; i++) for (let j = 0; j < b.length; j++) out[i+j] = out[i+j]! + a[i]! * b[j]!;
  return reduce(out, f);
}
function polynomialPower(a: Poly, e: number, f: Poly): bigint[] {
  assert(Number.isSafeInteger(e) && e >= 0, 'Exponent domain');
  let out = reduce([1n], f);
  // Successive products deliberately differ from Python's binary exponentiation.
  for (let k = 0; k < e; k++) out = multiply(out, a, f);
  return out;
}
function determinant(matrix: readonly Poly[]): bigint {
  const a = matrix.map(row => [...row]); const size = a.length;
  assert(a.every(row => row.length === size), 'Square matrix required');
  let denominator = 1n; let sign = 1n;
  for (let k = 0; k < size - 1; k++) {
    if (a[k]![k] === 0n) {
      const pivot = a.findIndex((row, i) => i > k && row[k] !== 0n);
      if (pivot === -1) return 0n;
      [a[k], a[pivot]] = [a[pivot]!, a[k]!]; sign = -sign;
    }
    const pivot = a[k]![k]!;
    for (let i = k+1; i < size; i++) for (let j = k+1; j < size; j++) {
      const numerator = a[i]![j]! * pivot - a[i]![k]! * a[k]![j]!;
      assert(numerator % denominator === 0n, 'Nonexact determinant division');
      a[i]![j] = numerator / denominator;
    }
    for (let i = k+1; i < size; i++) a[i]![k] = 0n;
    denominator = pivot;
  }
  return sign * a[size-1]![size-1]!;
}
function normTest(a: bigint): bigint {
  const h = [a**4n, a**3n, a*a, a, 1n];
  const columns: bigint[][] = [];
  for (let j = 0; j < 4; j++) {
    const basis = Array.from({length: 4}, (_, i) => i === j ? 1n : 0n);
    columns.push(multiply([-(a**3n), 0n, 0n, 1n], basis, h));
  }
  const matrix = Array.from({length: 4}, (_, i) => columns.map(col => col[i]!));
  return determinant(matrix);
}
function symbolicChecks(): object {
  const f = [1n, 1n, 1n, 1n, 1n]; const z = [0n, 1n, 0n, 0n];
  const phi = reduce([1n, 1n, 0n, 0n, 1n], f);
  const square = multiply(phi, phi, f);
  assert(square.every((v,i) => v-phi[i]!-(i === 0 ? 1n : 0n) === 0n), 'phi relation');
  const root = multiply(polynomialPower([0n,-1n,0n,0n],17,f), [1n,1n],f);
  assert(root.every((v,i) => v === phi[i]), 'cyclotomic root formula');
  let product = reduce([1n], f);
  for (let j = 1; j <= 4; j++) {
    const zj = polynomialPower(z,j,f).map((v,i) => (i === 0 ? 1n : 0n)-v);
    product = multiply(product,zj,f);
  }
  assert(product[0] === 5n && product.slice(1).every(v => v === 0n), 'cyclotomic product');
  const normRows: string[][] = [];
  for (let a = -6n; a <= 6n; a++) {
    const value = normTest(a); assert(value === 5n*a**12n, 'degree-12 norm interpolation');
    normRows.push([a.toString(), value.toString()]);
  }
  const big = 2n**60n+1n;
  assert(normTest(big) === 5n*big**12n, 'large integer exactness');
  return {cyclotomic_product: '5', root_of_phi_formula: true,
    quartic_norm_grid: normRows, norm_polynomial_degree_bound: 12,
    scalar_V_homogeneous_degree: 4, large_integer_check: true};
}
function rootsOfUnity(p: bigint): bigint {
  assert((p-1n)%5n === 0n, 'Split cyclotomic prime required');
  for (let a = 2n; a < p; a++) {
    const z = power(a,(p-1n)/5n,p);
    if (z !== 1n) return z;
  }
  throw new Error('No primitive fifth root found');
}
function toricRatios(p: bigint, z: bigint): bigint[] {
  let first: bigint | null = null;
  for (let x = 1n; x < p; x++) if ((power(x,10n,p)+256n)%p === 0n) { first = x; break; }
  if (first === null) return [];
  const mu = mod(-z,p); const result: bigint[] = [];
  for (let j = 0n; j < 10n; j++) result.push(first*power(mu,j,p)%p);
  assert(new Set(result).size === 10, 'Distinct tenth roots');
  assert(result.every(x => (power(x,10n,p)+256n)%p === 0n), 'Toric roots');
  return result.sort((a,b) => a < b ? -1 : a > b ? 1 : 0);
}
function namedTests(): object[] {
  return [2381n,17681n,610301n].map(p => {
    assert(prime(p) && p%340n === 1n,'Named prime');
    const z = rootsOfUnity(p);
    let sqrt = 0n;
    while (sqrt*sqrt%p !== 5n) { sqrt++; assert(sqrt < p,'sqrt5 not found'); }
    const phi = (1n+sqrt)*inverse(2n,p)%p; const c = 5n*inverse(32n,p)%p;
    const cc = power(c,(p-1n)/17n,p); const pc = power(phi,(p-1n)/17n,p);
    const ratios = toricRatios(p,z); assert(ratios.length === 10,'Toric witness exists');
    let y = 1n;
    while (power(2n*power(ratios[0]!*y%p,5n,p)%p,(p-1n)/17n,p) !== 1n) y++;
    return {q:p, phi, c, c_character:cc, phi_character:pc,
      c_passes:cc === 1n, phi_passes:pc === 1n,
      toric_X_roots_for_Y_1:ratios, gaussian_toric_witness:[ratios[0]!*y%p,y]};
  });
}
function equivalenceTests(): object[] {
  return [241n,2381n,17681n].map(p => {
    assert(prime(p) && p%20n === 1n,'Split prime');
    const z = rootsOfUnity(p); const ratios = toricRatios(p,z);
    let rr = 1n;
    while (power(rr,5n,p) !== 2n) { rr++; assert(rr < p, 'rho root not found'); }
    const rhos = Array.from({length:5}, (_,j) => rr*power(z,BigInt(j),p)%p);
    const image = new Set<bigint>();
    for (let j=0n;j<p;j++) image.add(power(j,17n,p));
    const phi = mod(1n+z+inverse(z,p),p);
    const constant = image.has(5n*inverse(32n,p)%p) && image.has(phi);
    let total = 0; let gaussian = 0; let joint = 0;
    for (const ratio of ratios) for(let y=1n;y<p;y++) {
      const x = ratio*y%p; total++;
      // At the toric fiber the two split Gaussian values are 0 and 2X^5.
      if (!image.has(2n*power(x,5n,p)%p)) continue;
      gaussian++;
      const unitPower = rhos.every(r => image.has((x*x+2n*power(r,3n,p)*y*y)%p));
      assert(unitPower === constant,'New toric equivalence failed');
      if (unitPower) joint++;
    }
    assert(total > 0 && gaussian > 0,'Nonvacuous check required');
    return {q:p,toric_pairs:total,gaussian_pairs:gaussian,joint_pairs:joint,constant_tests:constant};
  });
}
function survivingLocalWitness(): object {
  const beta = [1n,6n,3n,0n,7n];
  const quintic = polynomialPower(beta,17,[-2n,0n,0n,0n,0n,1n]).map(v => mod(v,13n));
  const gaussian = polynomialPower([5n,1n],17,[1n,0n,1n]).map(v => mod(v,13n));
  const phi = polynomialPower([3n,5n],17,[-1n,-1n,1n]).map(v => mod(v,13n));
  assert(quintic.every((v,i) => v === [10n,0n,0n,2n,0n][i]), 'q13 quintic witness');
  assert(gaussian[0] === 2n && gaussian[1] === 3n, 'q13 Gaussian witness');
  assert(phi[0] === 0n && phi[1] === 1n, 'q13 phi witness');
  assert((6n**10n+256n)%13n === 0n && power(9n,17n,13n) === 3n, 'q13 toric/c witness');
  return {q:13, X_Y_Z_residues:[6,1,0], beta, beta_power:quintic,
    gaussian_root:[5,1], gaussian_power:gaussian, c_root:9, c_root_power:3,
    phi_root:[3,5], phi_root_power:phi};
}
const c289=5n*inverse(32n,289n)%289n;
assert(power(c289,16n,289n) === 256n,'17-adic consistency');
console.log(JSON.stringify({checkpoint:'U67',full_Beal_solved:false,
  symbolic:symbolicChecks(),named_residue_tests:namedTests(),toric_equivalence:equivalenceTests(),
  surviving_local_witness:survivingLocalWitness(),
  c_at_17_squared:{modulus:289,c:c289,c_to_16:power(c289,16n,289n)}},
  (_key: string,value: unknown) => typeof value === 'bigint' ? value.toString() : value,2));
