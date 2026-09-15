"""Replay U65's exact local certificates without a network or paid runtime."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent


def normalized(value: object) -> object:
    if isinstance(value, bool) or value is None:
        return value
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        return [normalized(v) for v in value]
    if isinstance(value, dict):
        return {str(k): normalized(v) for k, v in value.items()}
    return value


def main() -> None:
    tsc, node = shutil.which('tsc'), shutil.which('node')
    if tsc is None or node is None:
        raise RuntimeError('This replay requires the TypeScript compiler and Node.js')
    OUT.mkdir(parents=True, exist_ok=True)
    build = OUT / 'build'
    log: dict[str, object] = {
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'full_Beal_solved': False,
        'scope': 'U65 finite certificate and polynomial-identity replay; not formal proof verification',
        'commands': [],
        'capabilities': {name: shutil.which(name) for name in
                         ['tsc', 'node', 'bun', 'ruff', 'eslint', 'lean', 'lake', 'sage', 'magma']},
    }
    commands = log['commands']
    assert isinstance(commands, list)

    def run(args: list[str], destination: str | None = None) -> None:
        result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=45, check=False)
        record = {'command': args, 'cwd': str(ROOT), 'returncode': result.returncode,
                  'stderr': result.stderr}
        if destination:
            path = OUT / destination
            path.write_text(result.stdout)
            record['stdout_file'] = str(path.relative_to(ROOT))
            record['stdout_sha256'] = hashlib.sha256(result.stdout.encode()).hexdigest()
        else:
            record['stdout'] = result.stdout
        commands.append(record)
        (OUT / 'execution_log.json').write_text(json.dumps(log, indent=2))
        if result.returncode:
            raise RuntimeError(f'Failed: {args!r}\n{result.stderr}')

    run([sys.executable, '--version'])
    run([tsc, '--version'])
    run([node, '--version'])
    run([sys.executable, '-c', 'import sympy; print(sympy.__version__)'])
    run([sys.executable, '-m', 'py_compile', 'code/U65_quintic_descent.py',
         'research/computations/U65/reproduce.py'])
    run([sys.executable, '-m', 'tabnanny', 'code/U65_quintic_descent.py'])
    run([tsc, '--strict', '--noUncheckedIndexedAccess', '--noUnusedLocals', '--noUnusedParameters',
         '--target', 'ES2022', '--module', 'commonjs', '--outDir', str(build),
         'code/U65_quintic_descent.ts'])
    run([sys.executable, 'code/U65_quintic_descent.py'], 'python_output.json')
    run([node, str(build / 'U65_quintic_descent.js')], 'typescript_output.json')
    py = json.loads((OUT / 'python_output.json').read_text())
    ts = json.loads((OUT / 'typescript_output.json').read_text())
    assert normalized(py['sieve']['rows']) == normalized(ts['sieve']['rows'])
    for key in ['modulus', 'square_parameter_pairs', 'norm_17th_power_pairs',
                'two_component_pairs', 'gaussian_parameter_pairs', 'gaussian_root_pairs']:
        assert normalized(py['sieve'][key]) == normalized(ts['sieve'][key]), key
    assert normalized(py['unit_basis_characters']) == normalized(ts['unit_basis_characters'])
    assert normalized(py['quintic_field']['generator_norms']) == normalized(ts['generator_norms'])
    assert ts['h_roots_mod17_squared'] == 2
    assert ts['common_roots_with_Frey_quadratics'] == [0, 0, 0]
    comparison = {'status': 'all compared mathematical values agree',
                  'full_Beal_solved': False,
                  'full_rows_compared': 24, 'square_root_witness_pairs_compared': 544,
                  'different_methods': ['Python split linear/quartic Fermat quotients and split Gaussian test',
                                        'TypeScript unsplit degree-five Frobenius equation and unsplit Gaussian test'],
                  'not_established': ['global Diophantine impossibility', 'independent expert verification',
                                      'proof-assistant verification', 'newspace completeness']}
    (OUT / 'comparison.json').write_text(json.dumps(comparison, indent=2))
    log['completed_utc'] = datetime.now(timezone.utc).isoformat()
    log['status'] = 'completed'
    log['lint_note'] = 'No configured standalone linter found; strict/no-unused TypeScript, py_compile and tabnanny executed.'
    log['comparison'] = comparison
    (OUT / 'execution_log.json').write_text(json.dumps(log, indent=2))
    print(json.dumps(comparison, indent=2))


if __name__ == '__main__':
    main()
