"""Replay U72's exact arithmetic and repository-equivalent quality checks."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
LOG = OUT/'logs'
BUILD = OUT/'build'
LOG.mkdir(exist_ok=True)
BUILD.mkdir(exist_ok=True)
commands = [
    ('python_version', [sys.executable, '--version']),
    ('node_version', ['node', '--version']),
    ('tsc_version', ['tsc', '--version']),
    ('python_compile', [sys.executable, '-m', 'py_compile', 'code/U72_full_support.py',
                        'research/computations/U72/reproduce.py']),
    ('python_whitespace', [sys.executable, '-m', 'tabnanny', 'code/U72_full_support.py']),
    ('strict_typecheck', ['tsc', 'code/U72_full_support.ts', '--target', 'ES2022',
                         '--module', 'commonjs', '--strict', '--noUncheckedIndexedAccess',
                         '--noUnusedLocals', '--noUnusedParameters',
                         '--exactOptionalPropertyTypes', '--noEmitOnError',
                         '--outDir', str(BUILD)]),
    ('python', [sys.executable, 'code/U72_full_support.py']),
    ('typescript', ['node', str(BUILD/'U72_full_support.js')]),
]
records = []
for name, command in commands:
    started = datetime.now(timezone.utc).isoformat()
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=40)
    (LOG/f'{name}.stdout').write_text(result.stdout)
    (LOG/f'{name}.stderr').write_text(result.stderr)
    records.append({'name':name, 'command':command, 'started_utc':started,
                    'returncode':result.returncode})
    (OUT/'execution_log.json').write_text(json.dumps(records, indent=2)+'\n')
    if result.returncode:
        raise RuntimeError(f'{name} failed: inspect preserved stdout/stderr')
    if name in ('python','typescript'):
        (OUT/f'{name}_output.json').write_text(result.stdout)
a = json.loads((OUT/'python_output.json').read_text())
b = json.loads((OUT/'typescript_output.json').read_text())
keys = ('summary','examples17','examples_good','examples2')
assert all(a[key] == b[key] for key in keys), 'Arithmetic disagreement'
(OUT/'certificate_summary.json').write_text(json.dumps(a['summary'], indent=2)+'\n')
(OUT/'comparison.json').write_text(json.dumps({
    'shared_blocks_equal':list(keys), 'all_commands_pass':True,
    'forcing_domains':'Python: projective pairs; TypeScript: all fifth-power image pairs',
    'independent_local_methods':'Python binomial series; TypeScript digit lifts',
    'bun_available':shutil.which('bun') is not None,
    'standalone_linter_available':any(shutil.which(x) for x in ('ruff','eslint')),
    'independent_expert_or_kernel_verification':False,
}, indent=2)+'\n')
print(json.dumps({'checkpoint':'U72','all_checks':'PASS',
                  'base_bound_exponent':a['summary']['base_bound_decimal_exponent'],
                  'full_Beal_solved':False}))
