"""Run the U69 exact certificates and focused code-quality checks offline."""
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
    ('typescript_version', ['tsc', '--version']),
    ('python_compile', [sys.executable, '-m', 'py_compile', 'code/U69_joint_support.py', str(__file__)]),
    ('python_whitespace', [sys.executable, '-m', 'tabnanny', 'code/U69_joint_support.py', str(__file__)]),
    ('strict_typecheck', ['tsc', 'code/U69_joint_support.ts', '--strict', '--noUnusedLocals',
                         '--noUnusedParameters', '--noUncheckedIndexedAccess',
                         '--exactOptionalPropertyTypes', '--target', 'ES2022', '--module',
                         'commonjs', '--noEmitOnError', '--outDir', str(BUILD)]),
    ('python', [sys.executable, 'code/U69_joint_support.py']),
    ('typescript', ['node', str(BUILD/'U69_joint_support.js')]),
]
records = []
for label, command in commands:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=40)
    (LOG/f'{label}.stdout').write_text(result.stdout)
    (LOG/f'{label}.stderr').write_text(result.stderr)
    records.append({'label': label, 'command': command, 'exit_code': result.returncode})
    (OUT/'execution_log.json').write_text(json.dumps(records, indent=2)+'\n')
    if result.returncode:
        raise RuntimeError(f'{label} failed; inspect retained stdout/stderr')
    if label in ('python', 'typescript'):
        (OUT/f'{label}_output.json').write_text(result.stdout)
py = json.loads((OUT/'python_output.json').read_text())['summary']
ts = json.loads((OUT/'typescript_output.json').read_text())['summary']
assert py == ts, 'Distinct certificate implementations disagree'
(OUT/'certificate_summary.json').write_text(json.dumps(py, indent=2)+'\n')
(OUT/'comparison.json').write_text(json.dumps({
    'all_shared_mathematical_fields_equal': True,
    'all_recorded_commands_passed': True,
    'bun_available': shutil.which('bun') is not None,
    'standalone_linter_available': any(shutil.which(x) for x in ('ruff', 'eslint')),
    'formal_or_independent_expert_verification': False,
    'full_Beal_solved': False,
}, indent=2)+'\n')
print('U69: all shared certificates agree; full Beal remains unresolved.')
