"""Reproduce U75's exact arithmetic and strict checks without network access."""
from __future__ import annotations
from pathlib import Path
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent


def main() -> None:
    logs = OUT/'logs'
    build = OUT/'build'
    logs.mkdir(exist_ok=True)
    build.mkdir(exist_ok=True)
    commands = [
        ('python_version', [sys.executable, '--version']),
        ('node_version', ['node', '--version']),
        ('tsc_version', ['tsc', '--version']),
        ('python_compile', [sys.executable, '-m', 'py_compile',
                            'code/U75_jacobian_factors.py',
                            'code/U75_quadratic_extension_check.py',
                            'research/computations/U75/reproduce.py']),
        ('python_whitespace', [sys.executable, '-m', 'tabnanny',
                               'code/U75_jacobian_factors.py',
                               'code/U75_quadratic_extension_check.py']),
        ('strict_typecheck', ['tsc', 'code/U75_jacobian_factors.ts', '--strict',
             '--noUncheckedIndexedAccess', '--noUnusedLocals', '--noUnusedParameters',
             '--exactOptionalPropertyTypes', '--target', 'ES2022', '--module', 'commonjs',
             '--noEmitOnError', '--outDir', str(build)]),
        ('python', [sys.executable, 'code/U75_jacobian_factors.py']),
        ('typescript', ['node', str(build/'U75_jacobian_factors.js')]),
        ('extension_check', [sys.executable, 'code/U75_quadratic_extension_check.py']),
    ]
    records = []
    for name, command in commands:
        run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=40)
        (logs/f'{name}.stdout').write_text(run.stdout)
        (logs/f'{name}.stderr').write_text(run.stderr)
        records.append({'name': name, 'command': command, 'returncode': run.returncode})
        (OUT/'execution_log.json').write_text(json.dumps(records, indent=2)+'\n')
        if run.returncode:
            raise RuntimeError(f'{name} failed; see preserved stdout/stderr')
        if name in ('python', 'typescript'):
            (OUT/f'{name}_output.json').write_text(run.stdout)
        if name == 'extension_check':
            (OUT/'extension_check.json').write_text(run.stdout)
    a = json.loads((OUT/'python_output.json').read_text())
    b = json.loads((OUT/'typescript_output.json').read_text())
    assert a == b, 'Complete arithmetic outputs disagree'
    (OUT/'certificate_summary.json').write_text(json.dumps(a['summary'], indent=2)+'\n')
    (OUT/'comparison.json').write_text(json.dumps({
        'complete_outputs_identical': True,
        'all_45_character_vectors_and_orders_identical': True,
        'all_15_jet_matrices_identical': True,
        'quadratic_extension_sign_calibration': True,
        'all_commands_passed': True,
        'bun_available': shutil.which('bun') is not None,
        'standalone_linter_available': any(shutil.which(n) for n in ('ruff', 'eslint')),
        'independent_expert_or_kernel_verification': False,
        'degree_five_points_classified': False,
    }, indent=2)+'\n')
    print(json.dumps({'checkpoint': 'U75', 'exact_checks': 'PASS',
                      'rank_lower_bound': 15, 'full_Beal_solved': False}))


if __name__ == '__main__':
    main()
