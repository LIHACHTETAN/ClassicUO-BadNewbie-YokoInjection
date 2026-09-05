from __future__ import annotations

from pathlib import Path
import shutil
import sys

if len(sys.argv) != 2:
    raise SystemExit('usage: patch-v50-release9.py <project-root>')

root = Path(sys.argv[1]).resolve()
if not (root / 'ClassicUO.sln').is_file():
    raise SystemExit(f'ClassicUO.sln not found under {root}')


def load(rel: str) -> str:
    return (root / rel).read_text(encoding='utf-8-sig')


def save(rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='')


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise RuntimeError(f'{label}: expected {expected} source site(s), found {count}')
    return text.replace(old, new)


# 1) Compiler compatibility + one authoritative dead-state route.
rel = 'external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs'
s = load(rel)
old_named = 'FindJournalPatternId(bridge.GetJournalText(foundedTextIndex), pattern, equals: false, ignoreCase)'
s = replace_exact(
    s,
    old_named,
    'FindJournalPatternId(bridge.GetJournalText(foundedTextIndex), pattern, false, ignoreCase)',
    'InjectionApiUO non-trailing named arguments',
    2,
)
s = replace_exact(
    s,
    ".Split('|', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);",
    ".Split(new[] { '|' }, StringSplitOptions.RemoveEmptyEntries)\n"
    "                .Select(pattern => pattern.Trim())\n"
    "                .Where(pattern => pattern.Length > 0)\n"
    "                .ToArray();",
    'InjectionApiUO TrimEntries compatibility',
)
s = replace_exact(
    s,
    '                return serial == bridge.Self ? bridge.Dead() : bridge.GetHP(serial) <= 0 ? 1 : 0;',
    '                return serial == bridge.Self ? bridge.Dead() : bridge.IsDead(serial);',
    'InjectionApiUO IsDeadState',
)
s = replace_exact(
    s,
    '                    case "dead": if (bridge.GetHP(id) > 0) return false; break;\n'
    '                    case "alive": if (bridge.GetHP(id) <= 0) return false; break;',
    '                    case "dead": if (bridge.IsDead(id) == 0) return false; break;\n'
    '                    case "alive": if (bridge.IsDead(id) != 0) return false; break;',
    'InjectionApiUO FindMobile dead/alive',
)
s = replace_exact(
    s,
    '            return serial > 0 && bridge.GetHP(serial) <= 0 ? 1 : 0;',
    '            return serial > 0 ? bridge.IsDead(serial) : 0;',
    'InjectionApiUO Dead(id)',
)
save(rel, s)

# 2) InjectionValue: IsSupported() and GetKind() must agree for dynamic delegate parameters.
rel = 'external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs'
s = load(rel)
s = replace_exact(
    s,
    '            if (type.Equals(typeof(string)))',
    '            if (type.Equals(typeof(InjectionValue)))\n'
    '                return InjectionValueKind.Any;\n'
    '            else if (type.Equals(typeof(string)))',
    'InjectionValue Any mapping',
)
s = replace_exact(
    s,
    '            else if (typeof(Array).IsAssignableFrom(type))',
    '            else if (typeof(Array).IsAssignableFrom(type) || typeof(IEnumerable<InjectionValue>).IsAssignableFrom(type))',
    'InjectionValue enumerable mapping',
)
save(rel, s)

# 3) Mixed concrete/Any native signatures need a per-position wildcard fallback.
rel = 'external/InjectionScript/src/InjectionScript/Runtime/NativeSubrutineMetadata.cs'
s = load(rel)
s = replace_exact(
    s,
    '            subrutineDefinition = null;\n            return false;',
    '            // Delegate-backed registrations may mix concrete kinds with InjectionValue (Any).\n'
    '            // Resolve Any as a per-position wildcard and prefer the most specific compatible route.\n'
    '            InjectionValueKind[] actualKinds = argumentValues.Select(item => item.Kind).ToArray();\n'
    '            NativeSubrutineDefinition wildcard = subrutines.Values\n'
    '                .Where(item => item.Name.Equals(name, StringComparison.OrdinalIgnoreCase)\n'
    '                    && item.ArgumentCount == actualKinds.Length\n'
    '                    && item.ParameterKinds.Select((kind, index) =>\n'
    '                        kind == InjectionValueKind.Any || kind == actualKinds[index]).All(match => match))\n'
    '                .OrderBy(item => item.ParameterKinds.Count(kind => kind == InjectionValueKind.Any))\n'
    '                .ThenBy(item => item.GetSignature(), StringComparer.OrdinalIgnoreCase)\n'
    '                .FirstOrDefault();\n'
    '            if (wildcard != null)\n'
    '            {\n'
    '                subrutineDefinition = wildcard;\n'
    '                return true;\n'
    '            }\n\n'
    '            subrutineDefinition = null;\n'
    '            return false;',
    'Native mixed-Any dispatch',
)
save(rel, s)

# 4) Runtime/manual catalogue is process-global; keep these tests serialized.
rel = 'tests/ClassicUO.UnitTests/Game/Managers/YokoApiSymbolIndexTests.cs'
s = load(rel)
s = replace_exact(
    s,
    '[CollectionDefinition("Yoko completion catalog")]',
    '[CollectionDefinition("Yoko completion catalog", DisableParallelization = true)]',
    'Yoko completion test isolation',
)
save(rel, s)

# 5) Test fixtures must model the same remote dead-state and skill-id contract as the runtime bridge.
rel = 'tests/ClassicUO.UnitTests/Game/Managers/YokoInjectionCompatibilityTests.cs'
s = load(rel)
s = replace_exact(
    s,
    '                    case nameof(IApiBridge.GetHP): return HpValue;\n'
    '                    case nameof(IApiBridge.Dead): return DeadValue;',
    '                    case nameof(IApiBridge.GetHP): return HpValue;\n'
    '                    case nameof(IApiBridge.Dead): return DeadValue;\n'
    '                    case nameof(IApiBridge.IsDead):\n'
    '                        return arguments.Length > 0 && (int)arguments[0] == 0x00001235 ? 1 : 0;',
    'RecordingBridge IsDead fixture',
)
s = replace_exact(
    s,
    '            Assert.Contains(proxy.Calls, c => c.Name == nameof(IApiBridge.UseSkill)\n'
    '                && string.Equals((string)c.Arguments[0], "Tracking", StringComparison.OrdinalIgnoreCase));',
    '            Assert.Contains(proxy.Calls, c => c.Name == nameof(IApiBridge.UseSkill)\n'
    '                && c.Arguments[0] is int skillId && skillId == 39);',
    'WaitingForMenu UseSkill fixture',
)
save(rel, s)

# 6) Generator must consume the actual InjectionScript output produced by the outer solution build.
rel = 'tools/YokoExampleGenerator/YokoExampleGenerator.csproj'
s = load(rel)
s = replace_exact(
    s,
    'bin\\Release\\netstandard2.0\\InjectionScript.dll',
    'bin\\Debug\\netstandard2.0\\InjectionScript.dll',
    'Yoko example generator InjectionScript reference',
)
save(rel, s)

# 7) Regenerate examples from the just-built runtime before the unfiltered unit-test gate.
rel = 'BUILD_V50_WINDOWS.ps1'
s = load(rel)
unit_anchor = '    Invoke-Checked "ClassicUO unit tests" {'
generator_block = (
    '    Invoke-Checked "Restore Yoko example generator" {\n'
    '        dotnet restore tools\\YokoExampleGenerator\\YokoExampleGenerator.csproj --ignore-failed-sources @restorePackageArgs\n'
    '    }\n'
    '    Invoke-Checked "Regenerate Yoko engine examples from current runtime" {\n'
    '        dotnet run --project tools\\YokoExampleGenerator\\YokoExampleGenerator.csproj -c Release --no-restore -- `\n'
    '            src\\ClassicUO.Client\\YokoDocumentation\\Examples `\n'
    '            src\\ClassicUO.Client\\YokoDocumentation\\Manual\\injection-manual-catalog.json `\n'
    '            src\\ClassicUO.Client\\YokoDocumentation\\Manual\\stealth-uo-api-catalog.json\n'
    '    }\n\n'
    + unit_anchor
)
s = replace_exact(s, unit_anchor, generator_block, 'Release 9 example regeneration gate')
save(rel, s)

# 8) Keep exactly one active full AutoLoad. Preserve the identical historical alias nested, not top-level.
for relative_dir in ('Autoload', 'src/ClassicUO.Client/Autoload'):
    directory = root / relative_dir
    canonical = directory / 'autoload.sc'
    alias = directory / 'Autoload_YokoClassicUO.sc'
    if not canonical.is_file() or not alias.is_file():
        raise RuntimeError(f'Missing AutoLoad source in {relative_dir}')
    if canonical.read_bytes() != alias.read_bytes():
        raise RuntimeError(f'Expected identical AutoLoad aliases in {relative_dir}, but bytes differ')
    legacy = directory / 'Legacy'
    legacy.mkdir(parents=True, exist_ok=True)
    target = legacy / alias.name
    if target.exists():
        target.unlink()
    shutil.move(str(alias), str(target))

# 9) Make synchronous Reload authoritative over constructor warmup, without blocking UI async reloads.
#    Also add a tiny cold fast-path for a procedure stored in <ProcedureName>.sc/.inj/.bas/.txt;
#    this publishes only that file and lets the full catalogue continue in the background.
rel = 'src/ClassicUO.Client/Game/Managers/YokoInjectionManager.cs'
s = load(rel)
s = replace_exact(
    s,
    '        private bool _procedureCatalogLoaded;\n        private bool _catalogReloadInProgress;',
    '        private bool _procedureCatalogLoaded;\n        private int _synchronousReloadInProgress;\n        private bool _catalogReloadInProgress;',
    'Yoko synchronous reload field',
)
s = replace_exact(
    s,
    '        public void Reload()\n'
    '        {\n'
    '            (long lifecycleEpoch, CancellationToken cancellationToken) = CaptureLifecycle();\n'
    '            Reload(lifecycleEpoch, cancellationToken);\n'
    '        }\n\n'
    '        private bool Reload(long lifecycleEpoch, CancellationToken cancellationToken)\n'
    '        {\n'
    '            if (cancellationToken.IsCancellationRequested || !IsLifecycleCurrent(lifecycleEpoch))\n'
    '                return false;\n',
    '        public void Reload()\n'
    '        {\n'
    '            (long lifecycleEpoch, CancellationToken cancellationToken) = CaptureLifecycle();\n'
    '            Interlocked.Exchange(ref _synchronousReloadInProgress, 1);\n'
    '            try\n'
    '            {\n'
    '                Reload(lifecycleEpoch, cancellationToken, authoritative: true);\n'
    '            }\n'
    '            finally\n'
    '            {\n'
    '                Volatile.Write(ref _synchronousReloadInProgress, 0);\n'
    '            }\n'
    '        }\n\n'
    '        private bool Reload(long lifecycleEpoch, CancellationToken cancellationToken,\n'
    '            bool authoritative = false)\n'
    '        {\n'
    '            if (cancellationToken.IsCancellationRequested || !IsLifecycleCurrent(lifecycleEpoch))\n'
    '                return false;\n'
    '            if (!authoritative && Volatile.Read(ref _synchronousReloadInProgress) != 0)\n'
    '                return false;\n',
    'Yoko authoritative synchronous reload',
)
run_anchor = '        public bool RunChatCommand(string commandLine)\n        {\n'
fast_helper = '''        private YokoProcedureInfo TryLoadProcedureFromMatchingFileFast(string procedureName)
        {
            if (string.IsNullOrWhiteSpace(procedureName)
                || !Regex.IsMatch(procedureName, @"^[A-Za-z_][A-Za-z0-9_]*$",
                    RegexOptions.CultureInvariant))
                return null;

            foreach (string extension in ScriptFileExtensions)
            {
                string filePath = Path.Combine(AutoloadPath, procedureName + extension);
                if (!File.Exists(filePath))
                    continue;

                string fullPath = Path.GetFullPath(filePath);
                string source;
                try
                {
                    source = File.ReadAllText(fullPath);
                }
                catch
                {
                    return null;
                }

                IReadOnlyList<YokoProcedureInfo> discovered = DiscoverProcedures(
                    source, fullPath, Path.GetFileName(fullPath));
                YokoProcedureInfo requested = discovered.FirstOrDefault(item =>
                    item.Name.Equals(procedureName, StringComparison.OrdinalIgnoreCase));
                if (requested == null)
                    continue;

                lock (_catalogReloadLock)
                {
                    lock (_proceduresLock)
                    {
                        _procedures.RemoveAll(item => string.Equals(
                            Path.GetFullPath(item.FilePath), fullPath,
                            StringComparison.OrdinalIgnoreCase));
                        _procedures.AddRange(discovered);
                        _procedures = _procedures
                            .OrderBy(item => item.FileName, StringComparer.OrdinalIgnoreCase)
                            .ThenBy(item => item.LineNumber)
                            .ToList();
                        RebuildProcedureLookupLocked();
                        _procedureSourceCache[fullPath] = source;
                        _procedureFileCache[fullPath] = discovered;
                    }
                }

                foreach (YokoProcedureInfo item in discovered)
                {
                    if (!_running.ContainsKey(item.Key))
                    {
                        _procedureStates[item.Key] = item.IsValid
                            ? YokoProcedureState.Ready
                            : YokoProcedureState.Error;
                    }
                }
                Interlocked.Increment(ref _procedureCatalogRevision);
                return requested;
            }

            return null;
        }

'''
s = replace_exact(s, run_anchor, fast_helper + run_anchor, 'Yoko cold procedure fast helper')
s = replace_exact(
    s,
    '            YokoProcedureInfo procedure = nameIndex < tokens.Length ? FindProcedureByName(tokens[nameIndex]) : null;\n'
    '            if (procedure == null && !scriptInvocation && !IsProcedureCatalogLoaded())\n'
    '            {\n'
    '                RequestProcedureCatalogReload(() => RunChatCommand(command));\n'
    '                SetStatus("Yoko command queued while Autoload loads in background.");\n'
    '                return true;\n'
    '            }\n',
    '            YokoProcedureInfo procedure = nameIndex < tokens.Length ? FindProcedureByName(tokens[nameIndex]) : null;\n'
    '            if (procedure == null && !scriptInvocation && !IsProcedureCatalogLoaded()\n'
    '                && nameIndex < tokens.Length)\n'
    '            {\n'
    '                procedure = TryLoadProcedureFromMatchingFileFast(tokens[nameIndex]);\n'
    '            }\n'
    '            if (procedure == null && !scriptInvocation && !IsProcedureCatalogLoaded())\n'
    '            {\n'
    '                RequestProcedureCatalogReload(() => RunChatCommand(command));\n'
    '                SetStatus("Yoko command queued while Autoload loads in background.");\n'
    '                return true;\n'
    '            }\n',
    'Yoko cold command fast path',
)
save(rel, s)

# Self-audit before expensive Windows compilation.
api = load('external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs')
if old_named in api or 'StringSplitOptions.TrimEntries' in api:
    raise RuntimeError('compiler compatibility patch verification failed')
if 'case "dead": if (bridge.IsDead(id) == 0)' not in api or api.count('bridge.IsDead(serial)') < 2:
    raise RuntimeError('dead-state patch verification failed')
iv = load('external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs')
if 'return InjectionValueKind.Any;' not in iv or 'typeof(IEnumerable<InjectionValue>).IsAssignableFrom(type)' not in iv:
    raise RuntimeError('InjectionValue mapping verification failed')
metadata = load('external/InjectionScript/src/InjectionScript/Runtime/NativeSubrutineMetadata.cs')
if 'per-position wildcard' not in metadata:
    raise RuntimeError('mixed Any dispatch verification failed')
manager = load('src/ClassicUO.Client/Game/Managers/YokoInjectionManager.cs')
for marker in ('_synchronousReloadInProgress', 'authoritative: true', 'TryLoadProcedureFromMatchingFileFast'):
    if marker not in manager:
        raise RuntimeError(f'Yoko manager patch verification failed: {marker}')
manual = load('src/ClassicUO.Client/Game/UI/Gumps/YokoManualGump.cs')
if '_workspaceSymbols = symbols as YokoApiSymbol[]' not in manual:
    raise RuntimeError('Manual must retain full live workspace/runtime snapshot')
if '.Where(symbol => symbol != null && !symbol.IsRuntime)' in manual:
    raise RuntimeError('Release 8 over-filtered Manual snapshot remains')
build = load('BUILD_V50_WINDOWS.ps1')
if 'Regenerate Yoko engine examples from current runtime' not in build:
    raise RuntimeError('Release 9 example regeneration gate missing')
for relative_dir in ('Autoload', 'src/ClassicUO.Client/Autoload'):
    directory = root / relative_dir
    if (directory / 'Autoload_YokoClassicUO.sc').exists():
        raise RuntimeError(f'duplicate active AutoLoad alias remains: {relative_dir}')
    archived = directory / 'Legacy/Autoload_YokoClassicUO.sc'
    if not archived.is_file() or archived.stat().st_size < 60000:
        raise RuntimeError(f'archived AutoLoad alias missing/incomplete: {relative_dir}')

print('v50 Release 9 source patch verification: PASS')
