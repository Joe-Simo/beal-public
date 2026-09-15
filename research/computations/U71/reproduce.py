"""Run the U71 exact verifiers and quality checks without network access."""
from pathlib import Path
import json, subprocess, sys, shutil
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
LOG=OUT/'logs';LOG.mkdir(exist_ok=True)
BUILD=OUT/'build';BUILD.mkdir(exist_ok=True)
commands=[
 ('python_version',[sys.executable,'--version']),
 ('node_version',['node','--version']),
 ('tsc_version',['tsc','--version']),
 ('compile',[sys.executable,'-m','py_compile','code/U71_common_root.py','research/computations/U71/reproduce.py']),
 ('whitespace',[sys.executable,'-m','tabnanny','code/U71_common_root.py']),
 ('strict_typecheck',['tsc','code/U71_common_root.ts','--strict','--noUncheckedIndexedAccess','--noUnusedLocals','--noUnusedParameters','--exactOptionalPropertyTypes','--target','ES2022','--module','commonjs','--resolveJsonModule','--esModuleInterop','--noEmitOnError','--outDir',str(BUILD)]),
 ('python',[sys.executable,'code/U71_common_root.py']),
 ('typescript',['node',str(BUILD/'code/U71_common_root.js')])]
records=[]
for name,command in commands:
 run=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,timeout=40)
 (LOG/f'{name}.stdout').write_text(run.stdout);(LOG/f'{name}.stderr').write_text(run.stderr)
 records.append({'name':name,'command':command,'returncode':run.returncode})
 (OUT/'execution_log.json').write_text(json.dumps(records,indent=2)+'\n')
 if run.returncode:raise RuntimeError(f'{name} failed; see stored output')
 if name in ('python','typescript'):(OUT/f'{name}_output.json').write_text(run.stdout)
a=json.loads((OUT/'python_output.json').read_text());b=json.loads((OUT/'typescript_output.json').read_text())
assert a['summary']==b['summary']
assert list(map(str,a['local_17_root']))==b['local_17_root']
(OUT/'certificate_summary.json').write_text(json.dumps(a['summary'],indent=2)+'\n')
(OUT/'comparison.json').write_text(json.dumps({'all_shared_fields_equal':True,'local_17_root_equal':True,'all_commands_pass':True,'standalone_linter_available':any(shutil.which(n) for n in ['ruff','eslint']),'bun_available':shutil.which('bun') is not None,'independent_expert_or_kernel_verification':False},indent=2)+'\n')
print(json.dumps({'checkpoint':'U71','arithmetic_checks':'PASS','full_Beal_solved':False}))
