"""Reproduce the U68 finite certificates and quality checks without network access."""
from __future__ import annotations
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
LOG = OUT / 'logs'
LOG.mkdir(exist_ok=True)
BUILD = OUT / 'build'
BUILD.mkdir(exist_ok=True)
commands = [
    ('python_version', [sys.executable, '--version']),
    ('node_version', ['node', '--version']),
    ('tsc_version', ['tsc', '--version']),
    ('python_compile', [sys.executable, '-m', 'py_compile', 'code/U68_coefficient_height.py']),
    ('python_whitespace', [sys.executable, '-m', 'tabnanny', 'code/U68_coefficient_height.py']),
    ('strict_typecheck', ['tsc', 'code/U68_coefficient_height.ts', '--target', 'ES2022',
                         '--module', 'commonjs', '--strict', '--noUnusedLocals',
                         '--noUnusedParameters', '--noUncheckedIndexedAccess',
                         '--exactOptionalPropertyTypes', '--noEmitOnError',
                         '--outDir', str(BUILD)]),
    ('python', [sys.executable, 'code/U68_coefficient_height.py']),
    ('typescript', ['node', str(BUILD/'U68_coefficient_height.js')]),
]
records = []
for name, command in commands:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=40)
    (LOG/f'{name}.stdout').write_text(result.stdout)
    (LOG/f'{name}.stderr').write_text(result.stderr)
    records.append({'name': name, 'command': command, 'exit_code': result.returncode})
    (OUT/'execution_log.json').write_text(json.dumps(records, indent=2)+'\n')
    if result.returncode:
        raise RuntimeError(f'{name} failed: see preserved stdout/stderr')
    if name in ('python', 'typescript'):
        (OUT/f'{name}_output.json').write_text(result.stdout)
a = json.loads((OUT/'python_output.json').read_text())['summary']
b = json.loads((OUT/'typescript_output.json').read_text())['summary']
assert a == b, 'Independent mathematical certificates disagree'
(OUT/'certificate_summary.json').write_text(json.dumps(a, indent=2)+'\n')
(OUT/'comparison.json').write_text(json.dumps({
    'all_shared_fields_equal': True,
    'all_commands_completed': True,
    'python_domain': 'all projective A:B classes at each listed prime',
    'typescript_domain': 'all fifth-power image pairs at each listed prime',
    'bun_available': shutil.which('bun') is not None,
    'standalone_linter_available': any(shutil.which(x) for x in ('eslint', 'ruff')),
    'independent_expert_or_kernel_verification': False,
}, indent=2)+'\n')
print(json.dumps({'result': 'all finite checks agree', 'bound_digits': a['lower_bound_digits'],
                  'full_Beal_solved': False}, indent=2))
