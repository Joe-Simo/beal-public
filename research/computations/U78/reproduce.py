"""Replay U78 exact certificates offline. External calculator jobs are not rerun."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent


def main() -> None:
    logs=OUT/'logs';build=OUT/'build'
    logs.mkdir(exist_ok=True);build.mkdir(exist_ok=True)
    commands=[
        ('python_version',[sys.executable,'--version']),
        ('node_version',['node','--version']),
        ('tsc_version',['tsc','--version']),
        ('python_compile',[sys.executable,'-m','py_compile','code/U78_descent_field.py',
                           'research/computations/U78/reproduce.py']),
        ('python_whitespace',[sys.executable,'-m','tabnanny','code/U78_descent_field.py',
                              'research/computations/U78/reproduce.py']),
        ('strict_typecheck',['tsc','code/U78_descent_field.ts','--strict','--noUncheckedIndexedAccess',
                            '--noUnusedLocals','--noUnusedParameters','--exactOptionalPropertyTypes',
                            '--target','ES2022','--module','commonjs','--noEmitOnError','--outDir',str(build)]),
        ('python',[sys.executable,'code/U78_descent_field.py']),
        ('typescript',['node',str(build/'U78_descent_field.js')])]
    records=[]
    for name,command in commands:
        result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,timeout=40)
        (logs/f'{name}.stdout').write_text(result.stdout)
        (logs/f'{name}.stderr').write_text(result.stderr)
        records.append({'name':name,'command':command,'returncode':result.returncode})
        (OUT/'execution_log.json').write_text(json.dumps(records,indent=2)+'\n')
        if result.returncode:
            raise RuntimeError(f'{name} failed; see preserved stdout and stderr')
        if name in ('python','typescript'):
            (OUT/f'{name}_output.json').write_text(result.stdout)
    a=json.loads((OUT/'python_output.json').read_text())
    b=json.loads((OUT/'typescript_output.json').read_text())
    assert a==b, 'Complete exact outputs disagree'
    assert not a['summary']['numerical_rank_upper_bound_computed']
    assert not a['summary']['class_group_2_rank_computed']
    assert not a['summary']['restriction_matrix_computed']
    (OUT/'certificate_summary.json').write_text(json.dumps(a['summary'],indent=2)+'\n')
    (OUT/'comparison.json').write_text(json.dumps({
        'complete_mathematical_outputs_identical':True,'all_commands_passed':True,
        'bun_available':shutil.which('bun') is not None,
        'standalone_linter_available':any(shutil.which(n) for n in ('eslint','ruff')),
        'independent_expert_or_kernel_verification':False,
        'numerical_rank_upper_bound_computed':False,'full_Beal_solved':False},indent=2)+'\n')
    print(json.dumps({'checkpoint':'U78','exact_checks':'PASS',
                      'numerical_rank_upper_bound_computed':False,'full_Beal_solved':False}))


if __name__=='__main__':
    main()
