"""Replay U67 exact checks and compare all shared finite outputs."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'research/computations/U67'
LOGS = OUT / 'logs'
LOGS.mkdir(parents=True, exist_ok=True)
commands = [
    ('python_version', [sys.executable, '--version']),
    ('node_version', ['node', '--version']),
    ('tsc_version', ['tsc', '--version']),
    ('python_compile', [sys.executable, '-m', 'py_compile', 'code/U67_kummer.py', 'research/computations/U67/reproduce.py']),
    ('python_whitespace', [sys.executable, '-m', 'tabnanny', 'code/U67_kummer.py']),
    ('strict_typecheck', ['tsc', 'code/U67_kummer.ts', '--strict', '--noUncheckedIndexedAccess', '--noUnusedLocals', '--noUnusedParameters', '--noEmitOnError', '--target', 'ES2022', '--module', 'commonjs', '--outDir', 'research/computations/U67/build']),
    ('python', [sys.executable, 'code/U67_kummer.py']),
    ('typescript', ['node', 'research/computations/U67/build/U67_kummer.js']),
]
log = []
for name, args in commands:
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=40)
    (LOGS / (name + '.stdout')).write_text(result.stdout)
    (LOGS / (name + '.stderr')).write_text(result.stderr)
    log.append({'name': name, 'command': args, 'exit_code': result.returncode})
    (OUT / 'execution_log.json').write_text(json.dumps(log, indent=2) + '\n')
    if result.returncode:
        raise RuntimeError(f'{name} failed; consult saved logs')
    if name in ('python', 'typescript'):
        (OUT / (name + '_output.json')).write_text(result.stdout)


def normalized(obj):
    if isinstance(obj, bool) or obj is None:
        return obj
    if isinstance(obj, int):
        return str(obj)
    if isinstance(obj, list):
        return [normalized(v) for v in obj]
    if isinstance(obj, dict):
        return {k: normalized(v) for k, v in obj.items()}
    return obj


p = json.loads((OUT / 'python_output.json').read_text())
t = json.loads((OUT / 'typescript_output.json').read_text())
# The two programs choose fifth roots differently. zeta is not an asserted
# common output; phi, characters, every toric root, and witnesses are compared.
p['named_residue_tests'] = [{k: v for k, v in row.items() if k != 'zeta'} for row in p['named_residue_tests']]
for key in ['named_residue_tests', 'toric_equivalence', 'c_at_17_squared', 'surviving_local_witness']:
    assert normalized(p[key]) == normalized(t[key]), key
summary = {
    'all_named_residue_values_match': True,
    'all_toric_equivalence_counts_match': True,
    'all_toric_root_lists_match': True,
    'all_gaussian_witnesses_match': True,
    'c_mod_289_check_matches': True,
    'full_Beal_solved': False,
    'surviving_local_witness': p['surviving_local_witness'],
    'new_equivalence_domains': p['toric_equivalence'],
    'upstream_rebuild_summary': {k: v for k, v in p['upstream_rebuild'].items() if k != 'rows'},
    'formal_or_expert_verification': False,
    'standalone_linter': 'Not installed; strict tsc, Python compilation and tabnanny ran.'
}
(OUT / 'certificate_summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
