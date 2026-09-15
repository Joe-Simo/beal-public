"""Replay U73 finite checks and quality gates; no network or hidden point search."""
from __future__ import annotations

import json
from pathlib import Path
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
    ('python_compile', [sys.executable, '-m', 'py_compile', 'code/U73_genus_eight.py',
                        'research/computations/U73/reproduce.py']),
    ('python_whitespace', [sys.executable, '-m', 'tabnanny', 'code/U73_genus_eight.py']),
    ('strict_typecheck', ['tsc', 'code/U73_genus_eight.ts', '--target', 'ES2022',
                          '--module', 'commonjs', '--strict', '--noUnusedLocals',
                          '--noUnusedParameters', '--noUncheckedIndexedAccess',
                          '--exactOptionalPropertyTypes', '--noEmitOnError', '--outDir', str(BUILD)]),
    ('python', [sys.executable, 'code/U73_genus_eight.py']),
    ('typescript', ['node', str(BUILD/'U73_genus_eight.js')]),
]
records = []
for name, command in commands:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=40)
    (LOG/f'{name}.stdout').write_text(result.stdout)
    (LOG/f'{name}.stderr').write_text(result.stderr)
    records.append({'name': name, 'command': command, 'returncode': result.returncode})
    (OUT/'execution_log.json').write_text(json.dumps(records, indent=2)+'\n')
    if result.returncode:
        raise RuntimeError(f'{name} failed; consult stored output')
    if name in ('python', 'typescript'):
        (OUT/f'{name}_output.json').write_text(result.stdout)
a = json.loads((OUT/'python_output.json').read_text())
b = json.loads((OUT/'typescript_output.json').read_text())
assert a == b, 'Exact outputs disagree'
(OUT/'certificate_summary.json').write_text(json.dumps(a['summary'], indent=2)+'\n')
(OUT/'comparison.json').write_text(json.dumps({
    'entire_mathematical_outputs_equal': True,
    'local_vectors_compared': len(a['local_examples']),
    'all_commands_pass': True,
    'bun_available': shutil.which('bun') is not None,
    'standalone_linter_available': any(shutil.which(x) for x in ('ruff', 'eslint')),
    'independent_expert_or_kernel_verification': False,
    'global_point_classification_performed': False,
}, indent=2)+'\n')
print(json.dumps({'checkpoint': 'U73', 'exact_checks': 'PASS', 'full_Beal_solved': False}))
