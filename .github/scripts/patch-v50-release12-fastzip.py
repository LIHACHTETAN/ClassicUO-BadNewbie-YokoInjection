from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit('usage: patch-v50-release12-fastzip.py <project-root>')

root = Path(sys.argv[1]).resolve()
build = root / 'BUILD_V50_WINDOWS.ps1'
if not build.is_file():
    raise SystemExit(f'BUILD_V50_WINDOWS.ps1 not found under {root}')

text = build.read_text(encoding='utf-8-sig')
old = '''    Invoke-Checked "Create v50.0.0 Windows x64 archive" {
        Compress-Archive -Path (Join-Path $OutputDirectory "*") -DestinationPath $ArchivePath -CompressionLevel Optimal -Force
    }'''
new = '''    Invoke-Checked "Create v50.0.0 Windows x64 archive" {
        $tar = (Get-Command tar.exe -ErrorAction Stop).Source
        & $tar -a -cf $ArchivePath -C $OutputDirectory .
        if ($LASTEXITCODE -ne 0) {
            throw "tar.exe failed to create client ZIP with exit code $LASTEXITCODE"
        }
    }'''
count = text.count(old)
if count != 1:
    raise RuntimeError(f'Internal client ZIP anchor: expected 1 site, found {count}')
text = text.replace(old, new, 1)
build.write_text(text, encoding='utf-8', newline='')

check = build.read_text(encoding='utf-8-sig')
if 'Compress-Archive -Path (Join-Path $OutputDirectory "*")' in check:
    raise RuntimeError('Slow internal Compress-Archive route remains after Release 12 patch')
if '& $tar -a -cf $ArchivePath -C $OutputDirectory .' not in check:
    raise RuntimeError('Fast tar.exe internal ZIP route missing after Release 12 patch')
for required in (
    'Expand-Archive -Path $ArchivePath',
    'Archive missing files',
    'Archive content hash mismatch',
    'Native dependency/export probe on extracted archive',
    'Client process startup smoke test on extracted archive',
):
    if required not in check:
        raise RuntimeError(f'Existing archive verification invariant missing: {required}')

print('v50 Release 12 fast ZIP patch verification: PASS')
