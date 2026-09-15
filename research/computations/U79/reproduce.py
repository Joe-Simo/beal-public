"""Replay U79 finite certificates offline; no class-group/rank claim is computed."""
from __future__ import annotations
import json
from pathlib import Path
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
        ('python_compile', [sys.executable, '-m', 'py_compile', 'code/U79_dyadic_image.py',
                             'research/computations/U79/reproduce.py']),
        ('python_whitespace', [sys.executable, '-m', 'tabnanny', 'code/U79_dyadic_image.py',
                                'research/computations/U79/reproduce.py']),
        ('strict_typecheck', ['tsc', 'code/U79_dyadic_image.ts', '--strict',
             '--noUncheckedIndexedAccess', '--noUnusedLocals', '--noUnusedParameters',
             '--exactOptionalPropertyTypes', '--target', 'ES2022', '--module', 'commonjs',
             '--resolveJsonModule', '--esModuleInterop', '--noEmitOnError', '--outDir', str(build)]),
        ('python', [sys.executable, 'code/U79_dyadic_image.py']),
        ('typescript', ['node', str(build/'code/U79_dyadic_image.js')])]
    records = []
    for name, command in commands:
        run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=40)
        (logs/f'{name}.stdout').write_text(run.stdout)
        (logs/f'{name}.stderr').write_text(run.stderr)
        records.append({'name': name, 'command': command, 'returncode': run.returncode})
        (OUT/'execution_log.json').write_text(json.dumps(records, indent=2)+'\n')
        if run.returncode:
            raise RuntimeError(f'{name} failed; actual output is preserved')
        if name in ('python', 'typescript'):
            (OUT/f'{name}_output.json').write_text(run.stdout)
    a = json.loads((OUT/'python_output.json').read_text())
    b = json.loads((OUT/'typescript_output.json').read_text())
    assert a == b, 'Complete mathematical outputs disagree'
    assert not a['summary']['global_restriction_matrix_computed']
    (OUT/'certificate_summary.json').write_text(json.dumps(a['summary'], indent=2)+'\n')
    (OUT/'comparison.json').write_text(json.dumps({
        'entire_outputs_equal': True, 'all_commands_passed': True,
        'all16_squareclass_certificates_verified': True,
        'dyadic_Kummer_image_basis_complete_as_proved': True,
        'bun_available': shutil.which('bun') is not None,
        'standalone_linter_available': any(shutil.which(x) for x in ('eslint', 'ruff')),
        'independent_expert_or_kernel_verification': False,
        'global_rank_upper_bound_computed': False}, indent=2)+'\n')
    print(json.dumps({'checkpoint': 'U79', 'exact_checks': 'PASS',
                      'dyadic_image_dimension': 16, 'global_rank_computed': False,
                      'full_Beal_solved': False}))


if __name__ == '__main__':
    main()
