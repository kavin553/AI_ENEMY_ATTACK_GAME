import os
import sys
import py_compile
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "run_outputs"
EXCLUDE_DIRS = {"venv", "__pycache__", "run_outputs"}
OUT.mkdir(exist_ok=True)

results = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    # prune excluded dirs
    dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
    for fname in filenames:
        if not fname.endswith('.py'):
            continue
        path = Path(dirpath) / fname
        if path.resolve() == Path(__file__).resolve():
            continue
        rel = path.relative_to(ROOT)
        out_file = OUT / (str(rel).replace(os.sep, '_') + '.txt')

        # Syntax check
        try:
            py_compile.compile(str(path), doraise=True)
            compile_ok = True
            compile_err = ''
        except py_compile.PyCompileError as e:
            compile_ok = False
            compile_err = str(e)

        if not compile_ok:
            with open(out_file, 'w', encoding='utf-8') as fo:
                fo.write('COMPILE_ERROR:\n')
                fo.write(compile_err)
            results.append((str(rel), False, 'compile_error', compile_err))
            print(f"[COMPILE ERROR] {rel}")
            continue

        # Execute with timeout
        try:
            proc = subprocess.run([sys.executable, str(path)], capture_output=True, text=True, timeout=10)
            ok = proc.returncode == 0
            stdout = proc.stdout
            stderr = proc.stderr
            returncode = proc.returncode
        except subprocess.TimeoutExpired:
            ok = False
            stdout = ''
            stderr = 'Timeout after 10s'
            returncode = 'timeout'
        except Exception as e:
            ok = False
            stdout = ''
            stderr = f'Exception: {e}'
            returncode = 'exception'

        with open(out_file, 'w', encoding='utf-8') as fo:
            fo.write(f'FILE: {rel}\nRETURN_CODE: {returncode}\n\nSTDOUT:\n')
            fo.write(stdout or '')
            fo.write('\n\nSTDERR:\n')
            fo.write(stderr or '')

        status = 'ok' if ok else 'error'
        results.append((str(rel), ok, status, stderr))
        print(f"[{status.upper()}] {rel} (out -> {out_file.name})")

# Summary
print('\n=== Summary ===')
for fname, ok, status, info in results:
    print(f"- {fname}: {status}{' — ' + info if info else ''}")

print(f"\nOutputs saved to: {OUT}")
print('Done.')
