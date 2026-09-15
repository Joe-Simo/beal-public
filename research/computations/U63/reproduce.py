"""Run the bounded U63 certificates without changing historical outputs."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'research/computations/U63'
BUILD = OUT / 'build'
BUILD.mkdir(exist_ok=True)
records: list[dict[str, object]] = []


def run(command: list[str], stdout_file: str | None = None) -> None:
    start = time.monotonic()
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True,
                            check=False, timeout=40)
    entry: dict[str, object] = {'command': command, 'cwd': str(ROOT),
                              'exit_code': result.returncode,
                              'elapsed_seconds': time.monotonic()-start,
                              'stderr': result.stderr}
    if stdout_file:
        (OUT / stdout_file).write_text(result.stdout)
        entry['stdout_file'] = stdout_file
        entry['stdout_sha256'] = hashlib.sha256(result.stdout.encode()).hexdigest()
    else:
        entry['stdout'] = result.stdout
    records.append(entry)
    if result.returncode != 0:
        (OUT/'execution_log.json').write_text(json.dumps(records,indent=2)+'\n')
        raise RuntimeError(f'Command failed: {command!r}: {result.stderr}')


run([sys.executable,'--version'])
run(['node','--version'])
run(['tsc','--version'])
run([sys.executable,'-c','import sympy; print(sympy.__version__)'])
run([sys.executable,'-m','py_compile','code/U63_weighted_audit.py',
     'research/computations/U63/reproduce.py'])
run([sys.executable,'-m','tabnanny','code/U63_weighted_audit.py'])
run(['tsc','--target','ES2022','--module','commonjs','--strict',
     '--noUncheckedIndexedAccess','--noUnusedLocals','--noUnusedParameters',
     '--outDir',str(BUILD),'code/U63_weighted_audit.ts','code/U60_audit.ts'])
run([sys.executable,'code/U63_weighted_audit.py'],'python_output.json')
run(['node',str(BUILD/'U63_weighted_audit.js')],'typescript_output.json')
run(['node',str(BUILD/'U60_audit.js')],'U60_checker_replay.json')


def normalize(value: object) -> object:
    if isinstance(value,dict):
        return {k:normalize(v) for k,v in value.items()}
    if isinstance(value,list):
        return [normalize(v) for v in value]
    if isinstance(value,str) and value.lstrip('-').isdigit():
        return int(value)
    return value


p = json.loads((OUT/'python_output.json').read_text())
t = normalize(json.loads((OUT/'typescript_output.json').read_text()))
# This harness is not a substitute for reading the two mathematical implementations.
fields=['all_pairs','structured_pairs','rows','all_trace_distribution','structured_plus_f',
        'structured_minus_f','U41_nonmatching_counterexample','correct_form_a_sum_product',
        'form_a_excluded_after_repair_in_square_domain']
for field in fields:
    assert p['prime11'][field] == t['prime11'][field], field
for field in ['square_residues','pairs','tested_x_per_pair','subdomain_5_divides_V_pairs']:
    assert p['mod125'][field] == t['mod125'][field], field
assert len(p['mod125']['root_triples']) == t['mod125']['root_count'] == 0
assert [','.join(map(str,a)) for a in p['mod4_quadratic_squares']] == t['mod4_quadratic_squares']
for field in ['negative_twist_model_identity','infinity_smoothness_identity',
              'inertia_cyclotomic_identity','discriminant_identity']:
    assert p[field] is True

summary = dict(p)
summary['prime11'] = {k:v for k,v in p['prime11'].items() if k != 'rows'}
summary['arithmetic'] = 'Exact Python, TypeScript bigint, and recorded Wolfram checks'
summary['comparison'] = {'all_120_rows_equal':True,'mod125_equal':True,
                         'mod4_equal':True,'no_mathematical_output_mismatch':True}
summary['source_hashes'] = {path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
    for path in ['code/U63_weighted_audit.py','code/U63_weighted_audit.ts',
                 'code/U60_audit.ts','research/computations/U63/wolfram_checks.wl']}
summary['mathematical_status'] = {'U41_weighted_elimination':'invalidated',
    'local_model_and_conductor':'written self-reviewed proof; not kernel checked',
    'U62':'unchanged written self-reviewed status; not re-certified here',
    'weighted_equation_solved':False,'independent_expert_review':False,
    'proof_assistant_verification':False}
(OUT/'certificate_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'execution_log.json').write_text(json.dumps({
    'completed_utc':datetime.now(timezone.utc).isoformat(),'commands':records,
    'comparison':'All shared exact outputs agree after converting decimal strings to integers.',
    'tools_present':{name:shutil.which(name) for name in ['bun','lean','sage','magma','ruff','tsc','node']},
    'lint_qualification':'No repository lint command found. Strict unused-variable/type checks and Python compilation/tabnanny ran; tabnanny is not a full style linter.'},indent=2)+'\n')
print('Completed: all finite comparisons and focused checker replay passed.')
