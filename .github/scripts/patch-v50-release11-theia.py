from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit('usage: patch-v50-release11-theia.py <project-root>')

root = Path(sys.argv[1]).resolve()
build = root / 'BUILD_V50_WINDOWS.ps1'
if not build.is_file():
    raise SystemExit(f'BUILD_V50_WINDOWS.ps1 not found under {root}')

text = build.read_text(encoding='utf-8-sig')
old = '''    Invoke-Checked "Publish standalone Eclipse Theia WebView2 host" {
        dotnet publish src\\ClassicUO.TheiaHost\\ClassicUO.TheiaHost.csproj `
            -c Release --no-restore -r win-x64 --self-contained true `
            -p:NuGetAudit=false `
            -p:PublishSingleFile=true -p:IncludeNativeLibrariesForSelfExtract=true `
            -o $TheiaOutput
    }'''
new = '''    Invoke-Checked "Restore standalone Eclipse Theia WebView2 host" {
        dotnet restore src\\ClassicUO.TheiaHost\\ClassicUO.TheiaHost.csproj `
            -r win-x64 -p:NuGetAudit=false
    }
    Invoke-Checked "Publish standalone Eclipse Theia WebView2 host" {
        dotnet publish src\\ClassicUO.TheiaHost\\ClassicUO.TheiaHost.csproj `
            -c Release --no-restore -r win-x64 --self-contained true `
            -p:NuGetAudit=false `
            -p:PublishSingleFile=true -p:IncludeNativeLibrariesForSelfExtract=true `
            -o $TheiaOutput
    }'''
count = text.count(old)
if count != 1:
    raise RuntimeError(f'TheiaHost publish anchor: expected 1 site, found {count}')
text = text.replace(old, new, 1)
build.write_text(text, encoding='utf-8', newline='')
check = build.read_text(encoding='utf-8-sig')
if 'Restore standalone Eclipse Theia WebView2 host' not in check:
    raise RuntimeError('TheiaHost restore gate missing after patch')
if 'dotnet restore src\\ClassicUO.TheiaHost\\ClassicUO.TheiaHost.csproj' not in check:
    raise RuntimeError('TheiaHost project restore command missing after patch')
print('v50 Release 11 TheiaHost restore patch verification: PASS')
