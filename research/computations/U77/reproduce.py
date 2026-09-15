"""Reproduce U77 certificates offline; does not request a remote rank computation."""
from __future__ import annotations
from pathlib import Path
import json
import shutil
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent

def main() -> None:
    logs=OUT/'logs';logs.mkdir(exist_ok=True)
    build=OUT/'build';build.mkdir(exist_ok=True)
    commands=[
        ('python_version',[sys.executable,'--version']),
        ('node_version',['node','--version']),
        ('tsc_version',['tsc','--version']),
        ('compile',[sys.executable,'-m','py_compile','code/U77_twist_reduction.py',
                    'research/computations/U77/reproduce.py']),
        ('whitespace',[sys.executable,'-m','tabnanny','code/U77_twist_reduction.py',
                       'research/computations/U77/reproduce.py']),
        ('typecheck',['tsc','code/U77_twist_reduction.ts','--strict','--noUncheckedIndexedAccess',
                       '--noUnusedLocals','--noUnusedParameters','--exactOptionalPropertyTypes',
                       '--target','ES2022','--module','commonjs','--noEmitOnError','--outDir',str(build)]),
        ('python',[sys.executable,'code/U77_twist_reduction.py']),
        ('typescript',['node',str(build/'U77_twist_reduction.js')])]
    records=[]
    for name,cmd in commands:
        run=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,timeout=40)
        (logs/f'{name}.stdout').write_text(run.stdout)
        (logs/f'{name}.stderr').write_text(run.stderr)
        records.append({'name':name,'command':cmd,'returncode':run.returncode})
        (OUT/'execution_log.json').write_text(json.dumps(records,indent=2)+'\n')
        if run.returncode:
            raise RuntimeError(f'{name} failed; see preserved logs')
        if name in ('python','typescript'):
            (OUT/f'{name}_output.json').write_text(run.stdout)
    a=json.loads((OUT/'python_output.json').read_text())
    b=json.loads((OUT/'typescript_output.json').read_text())
    assert a==b, 'Complete mathematical outputs differ'
    (OUT/'certificate_summary.json').write_text(json.dumps(a['summary'],indent=2)+'\n')
    (OUT/'comparison.json').write_text(json.dumps({
        'complete_outputs_identical':True,'all_commands_passed':True,
        'three_character_vectors_and_orders_equal':True,'two_complete_orbits_equal':True,
        'bun_available':shutil.which('bun') is not None,
        'standalone_linter_available':any(shutil.which(n) for n in ('ruff','eslint')),
        'rank_upper_bound_computed':False,'independent_expert_or_kernel_verification':False},indent=2)+'\n')
    print(json.dumps({'checkpoint':'U77','exact_checks':'PASS','rank_upper_bound_computed':False,
                      'full_Beal_solved':False}))

if __name__=='__main__':
    main()
