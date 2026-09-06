from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: patch-v50-0-2-build-manual.py <BUILD_V50_WINDOWS.ps1>")

path = Path(sys.argv[1]).resolve()
text = path.read_text(encoding="utf-8-sig")

patterns = [
    (
        "                & $python.Source -3 scripts\\GenerateCompleteApiManual.py\n",
        "                & $python.Source -3 scripts\\GenerateCompleteApiManual.py\n"
        "                if ($LASTEXITCODE -ne 0) { throw 'GenerateCompleteApiManual.py failed' }\n"
        "                & $python.Source -3 scripts\\ApplyV5002ManualPatch.py $ProjectRoot\n"
        "                if ($LASTEXITCODE -ne 0) { throw 'ApplyV5002ManualPatch.py failed' }\n",
    ),
    (
        "                & $python.Source scripts\\GenerateCompleteApiManual.py\n",
        "                & $python.Source scripts\\GenerateCompleteApiManual.py\n"
        "                if ($LASTEXITCODE -ne 0) { throw 'GenerateCompleteApiManual.py failed' }\n"
        "                & $python.Source scripts\\ApplyV5002ManualPatch.py $ProjectRoot\n"
        "                if ($LASTEXITCODE -ne 0) { throw 'ApplyV5002ManualPatch.py failed' }\n",
    ),
]

changed = 0
for old, new in patterns:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected exactly one occurrence of {old!r}, found {count}")
    text = text.replace(old, new, 1)
    changed += 1

path.write_text(text, encoding="utf-8", newline="")
print(f"BUILD_V50_WINDOWS Manual integration patched: {changed}/2")
