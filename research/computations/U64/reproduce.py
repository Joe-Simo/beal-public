"""Replay the bounded U64 certificates and compare every mathematical row."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT/'research/computations/U64'
BUILD = OUT/'build'


def canonical(value: object) -> object:
    if isinstance(value, dict):
        return {k: canonical(v) for k, v in value.items()}
    if isinstance(value, list):
        return [canonical(v) for v in value]
    if isinstance(value, int) and not isinstance(value, bool):
        return str(value)
    return value


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    BUILD.mkdir(exist_ok=True)
    records: list[dict[str, object]] = []
    commands = [
        ([sys.executable, 'code/U64_weighted_local.py'], 'python_output.json'),
        (['tsc', '--target', 'ES2022', '--module', 'commonjs', '--strict',
          '--noUncheckedIndexedAccess', '--noUnusedLocals', '--noUnusedParameters',
          '--outDir', str(BUILD), 'code/U64_weighted_local.ts'], 'typecheck.txt'),
        (['node', str(BUILD/'U64_weighted_local.js')], 'typescript_output.json'),
        ([sys.executable, '-m', 'py_compile', 'code/U64_weighted_local.py',
          'research/computations/U64/reproduce.py'], 'compile.txt'),
        ([sys.executable, '-m', 'tabnanny', 'code/U64_weighted_local.py'], 'tabnanny.txt'),
    ]
    for command, filename in commands:
        start = time.monotonic()
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=40)
        (OUT/filename).write_text(result.stdout)
        records.append({'command': command, 'cwd': str(ROOT), 'returncode': result.returncode,
                        'stdout_file': filename, 'stderr': result.stderr,
                        'elapsed_seconds': time.monotonic()-start})
        if result.returncode:
            (OUT/'execution_log.json').write_text(json.dumps({'status':'failed','commands':records},indent=2))
            raise RuntimeError(f'Command failed: {command!r}: {result.stderr}')
    p = json.loads((OUT/'python_output.json').read_text())
    t = json.loads((OUT/'typescript_output.json').read_text())
    for key in ['prime11_recovered_forms', 'form_b_diagnostics', 'unchecked_orbits']:
        if canonical(p[key]) != canonical(t[key]):
            raise AssertionError(f'Mathematical output mismatch: {key}')
    assert t['mod25'] == {'parameter_pairs':'500','roots':'0'}
    assert p['eisenstein']['mod25_parameter_pairs'] == 500
    assert p['eisenstein']['roots_mod25'] == []
    comparison = {'status':'passed',
        'arithmetic_rows_compared':sum(len(x['rows']) for x in p['form_b_diagnostics']),
        'comparisons':['all seven recovered prime11 forms', 'every bounded row at 11,19,31,41',
                       'boundary fibers and ratio sets', 'toric norm residues', 'mod25 root domain'],
        'normalization':'JSON decimal bigint strings matched to exact Python integers; no floating conversion'}
    (OUT/'comparison.json').write_text(json.dumps(comparison,indent=2)+'\n')
    summary = {k:v for k,v in p.items() if k!='form_b_diagnostics'}
    summary['form_b_diagnostics'] = [{k:v for k,v in r.items() if k!='rows'}
                                      for r in p['form_b_diagnostics']]
    summary['row_comparison'] = comparison
    summary['scope'] = 'No global weighted-equation exclusion; h unverified; full Beal unresolved'
    (OUT/'certificate_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    source_files = ['code/U64_weighted_local.py', 'code/U64_weighted_local.ts',
                    'references/U64/hecke_records.json', 'references/U64/sources.json',
                    'research/computations/U64/reproduce.py',
                    'research/computations/U64/wolfram_checks.wl',
                    'research/computations/U64/wolfram_output.txt']
    versions = {'python':platform.python_version(),
                'node':subprocess.check_output(['node','--version'],text=True).strip(),
                'typescript':subprocess.check_output(['tsc','--version'],text=True).strip()}
    import sympy
    versions['sympy'] = sympy.__version__
    log = {'status':'completed', 'finished_UTC':datetime.now(timezone.utc).isoformat(),
           'versions':versions, 'commands':records,
           'capabilities':{name:shutil.which(name) for name in ['bun','ruff','eslint','lean','magma','sage','gp']},
           'source_sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in source_files},
           'verification':'Exact bounded computations and self-review, not independent expert or kernel certification'}
    (OUT/'execution_log.json').write_text(json.dumps(log,indent=2)+'\n')
    print(json.dumps({'status':'completed','rows_compared':comparison['arithmetic_rows_compared'],
                      'recovered_form_survivors':['b'],'unchecked_orbits':['h']},indent=2))


if __name__ == '__main__':
    main()
