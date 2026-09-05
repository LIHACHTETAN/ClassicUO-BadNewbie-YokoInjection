from __future__ import annotations
from pathlib import Path
import shutil, sys

if len(sys.argv)!=2:
    raise SystemExit('usage: patch_v50_next.py <project-root>')
root=Path(sys.argv[1]).resolve()
if not (root/'ClassicUO.sln').is_file():
    raise SystemExit('ClassicUO.sln missing')

def load(rel): return (root/rel).read_text(encoding='utf-8-sig')
def save(rel,text): (root/rel).write_text(text,encoding='utf-8',newline='')
def repl(text,old,new,label,count=1):
    n=text.count(old)
    if n!=count: raise RuntimeError(f'{label}: expected {count}, found {n}')
    return text.replace(old,new)

# exact SDK
p=root/'global.json'
import json
j=json.loads(p.read_text(encoding='utf-8-sig')); j.setdefault('sdk',{})['rollForward']='disable'; p.write_text(json.dumps(j,indent=2)+'\n',encoding='utf-8')

# InjectionApiUO compiler + dead semantics
rel='external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs'; s=load(rel)
old="FindJournalPatternId(bridge.GetJournalText(foundedTextIndex), pattern, equals: false, ignoreCase)"
s=repl(s,old,"FindJournalPatternId(bridge.GetJournalText(foundedTextIndex), pattern, false, ignoreCase)",'named args',2)
s=repl(s,".Split('|', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);",
       ".Split(new[] { '|' }, StringSplitOptions.RemoveEmptyEntries)\n                .Select(pattern => pattern.Trim())\n                .Where(pattern => pattern.Length > 0)\n                .ToArray();",'TrimEntries')
s=repl(s,"                return serial == bridge.Self ? bridge.Dead() : bridge.GetHP(serial) <= 0 ? 1 : 0;",
       "                return serial == bridge.Self ? bridge.Dead() : bridge.IsDead(serial);",'IsDeadState')
s=repl(s,'                    case "dead": if (bridge.GetHP(id) > 0) return false; break;\n                    case "alive": if (bridge.GetHP(id) <= 0) return false; break;',
       '                    case "dead": if (bridge.IsDead(id) == 0) return false; break;\n                    case "alive": if (bridge.IsDead(id) != 0) return false; break;', 'FindMobile dead/alive')
s=repl(s,"            return serial > 0 && bridge.GetHP(serial) <= 0 ? 1 : 0;",
       "            return serial > 0 ? bridge.IsDead(serial) : 0;",'Dead(id)')
save(rel,s)

# InjectionValue kind consistency
rel='external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs'; s=load(rel)
s=repl(s,'            if (type.Equals(typeof(string)))',
       '            if (type.Equals(typeof(InjectionValue)))\n                return InjectionValueKind.Any;\n            else if (type.Equals(typeof(string)))','Any kind')
s=repl(s,'            else if (typeof(Array).IsAssignableFrom(type))',
       '            else if (typeof(Array).IsAssignableFrom(type) || typeof(IEnumerable<InjectionValue>).IsAssignableFrom(type))','enumerable array')
save(rel,s)

# mixed Any native dispatch
rel='external/InjectionScript/src/InjectionScript/Runtime/NativeSubrutineMetadata.cs'; s=load(rel)
old='            subrutineDefinition = null;\n            return false;'
new='''            // Delegate-backed registrations may mix concrete kinds with InjectionValue (Any).
            // Resolve Any as a per-position wildcard and prefer the most specific compatible route.
            InjectionValueKind[] actualKinds = argumentValues.Select(item => item.Kind).ToArray();
            NativeSubrutineDefinition wildcard = subrutines.Values
                .Where(item => item.Name.Equals(name, StringComparison.OrdinalIgnoreCase)
                    && item.ArgumentCount == actualKinds.Length
                    && item.ParameterKinds.Select((kind, index) =>
                        kind == InjectionValueKind.Any || kind == actualKinds[index]).All(match => match))
                .OrderBy(item => item.ParameterKinds.Count(kind => kind == InjectionValueKind.Any))
                .FirstOrDefault();
            if (wildcard != null)
            {
                subrutineDefinition = wildcard;
                return true;
            }

            subrutineDefinition = null;
            return false;'''
s=repl(s,old,new,'mixed Any')
save(rel,s)

# Manual: maintain separate filtered workspace rows and full workspace+runtime context.
rel='src/ClassicUO.Client/Game/UI/Gumps/YokoManualGump.cs'; s=load(rel)
s=repl(s,
'''        private static volatile IReadOnlyList<YokoApiSymbol> _workspaceSymbols =
            Array.Empty<YokoApiSymbol>();''',
'''        private static volatile IReadOnlyList<YokoApiSymbol> _workspaceSymbols =
            Array.Empty<YokoApiSymbol>();
        private static volatile IReadOnlyList<YokoApiSymbol> _workspaceContextSymbols =
            Array.Empty<YokoApiSymbol>();''','manual context field')
s=repl(s,
'''            // Keep the exact snapshot supplied by the live manager. Manual,
            // Inspector, completion and Autoload must all observe one revision.
            _workspaceSymbols = symbols as YokoApiSymbol[]
                ?? (symbols ?? Array.Empty<YokoApiSymbol>()).ToArray();
            _catalog = null;''',
'''            // Preserve the complete live index for dependency/usage lookup, while
            // exposing only real workspace declarations as Manual workspace rows.
            YokoApiSymbol[] snapshot = symbols as YokoApiSymbol[]
                ?? (symbols ?? Array.Empty<YokoApiSymbol>()).ToArray();
            _workspaceContextSymbols = snapshot;
            _workspaceSymbols = snapshot
                .Where(symbol => symbol != null && !symbol.IsRuntime)
                .ToArray();
            _catalog = null;''','manual update')
anchor='''        private static YokoApiSymbol[] ResolveManualSymbols(ManualEntry entry)
        {
            IReadOnlyList<YokoApiSymbol> snapshot = _workspaceSymbols;
            if (snapshot == null || snapshot.Count == 0 || !snapshot.Any(symbol => symbol.IsRuntime))
                snapshot = DefaultRuntimeSymbols;'''
replacement='''        private static IReadOnlyList<YokoApiSymbol> ManualSymbolContext()
        {
            IReadOnlyList<YokoApiSymbol> snapshot = _workspaceContextSymbols;
            if (snapshot == null || snapshot.Count == 0)
                return DefaultRuntimeSymbols;
            if (snapshot.Any(symbol => symbol != null && symbol.IsRuntime))
                return snapshot;
            return snapshot.Concat(DefaultRuntimeSymbols).ToArray();
        }

        private static YokoApiSymbol[] ResolveManualSymbols(ManualEntry entry)
        {
            IReadOnlyList<YokoApiSymbol> snapshot = ManualSymbolContext();'''
s=repl(s,anchor,replacement,'manual resolve context')
s=repl(s,
'''            IReadOnlyList<YokoApiSymbol> symbols = _workspaceSymbols;
            if (symbols == null || symbols.Count == 0)
                symbols = DefaultRuntimeSymbols;''',
'''            IReadOnlyList<YokoApiSymbol> symbols = ManualSymbolContext();''','manual dependency context')
save(rel,s)

# deterministic verifier follows dual snapshot invariant
rel='scripts/VerifyV50Ide.py'; s=load(rel)
s=repl(s,
'''    and '_workspaceSymbols = symbols as YokoApiSymbol[]' in manual_workspace_update
    and '?? (symbols ?? Array.Empty<YokoApiSymbol>()).ToArray();' in manual_workspace_update''',
'''    and '_workspaceContextSymbols = snapshot;' in manual_workspace_update
    and '_workspaceSymbols = snapshot' in manual_workspace_update
    and '.Where(symbol => symbol != null && !symbol.IsRuntime)' in manual_workspace_update
    and '.ToArray();' in manual_workspace_update''','verifier manual invariant')
save(rel,s)

# completion singleton isolation test
rel='tests/ClassicUO.UnitTests/Game/Managers/YokoApiSymbolIndexTests.cs'; s=load(rel)
s=repl(s,'[CollectionDefinition("Yoko completion catalog")]',
       '[CollectionDefinition("Yoko completion catalog", DisableParallelization = true)]','collection isolation')
save(rel,s)

# runtime test fixtures for real IsDead and UseSkill(int)
rel='tests/ClassicUO.UnitTests/Game/Managers/YokoInjectionCompatibilityTests.cs'; s=load(rel)
s=repl(s,
'''                    case nameof(IApiBridge.GetHP): return HpValue;
                    case nameof(IApiBridge.Dead): return DeadValue;''',
'''                    case nameof(IApiBridge.GetHP): return HpValue;
                    case nameof(IApiBridge.Dead): return DeadValue;
                    case nameof(IApiBridge.IsDead):
                        return arguments.Length > 0 && (int)arguments[0] == 0x00001235 ? 1 : 0;''','IsDead fixture')
s=repl(s,
'''            Assert.Contains(proxy.Calls, c => c.Name == nameof(IApiBridge.UseSkill)
                && string.Equals((string)c.Arguments[0], "Tracking", StringComparison.OrdinalIgnoreCase));''',
'''            Assert.Contains(proxy.Calls, c => c.Name == nameof(IApiBridge.UseSkill)
                && c.Arguments[0] is int skillId && skillId == 39);''','UseSkill fixture')
save(rel,s)

# example generator references actual InjectionScript Debug output
rel='tools/YokoExampleGenerator/YokoExampleGenerator.csproj'; s=load(rel)
s=repl(s,'bin\\Release\\netstandard2.0\\InjectionScript.dll','bin\\Debug\\netstandard2.0\\InjectionScript.dll','generator ref')
save(rel,s)

# build regenerates examples before unit tests
rel='BUILD_V50_WINDOWS.ps1'; s=load(rel)
unit='    Invoke-Checked "ClassicUO unit tests" {'
block='''    Invoke-Checked "Restore Yoko example generator" {
        dotnet restore tools\\YokoExampleGenerator\\YokoExampleGenerator.csproj --ignore-failed-sources @restorePackageArgs
    }
    Invoke-Checked "Regenerate Yoko engine examples from current runtime" {
        dotnet run --project tools\\YokoExampleGenerator\\YokoExampleGenerator.csproj -c Release --no-restore -- `
            src\\ClassicUO.Client\\YokoDocumentation\\Examples `
            src\\ClassicUO.Client\\YokoDocumentation\\Manual\\injection-manual-catalog.json `
            src\\ClassicUO.Client\\YokoDocumentation\\Manual\\stealth-uo-api-catalog.json
    }

'''+unit
s=repl(s,unit,block,'generator build gate')
save(rel,s)

# One active top-level AutoLoad; preserve alias only in nested Archive.
for d in ('Autoload','src/ClassicUO.Client/Autoload'):
    directory=root/d; canonical=directory/'autoload.sc'; alias=directory/'Autoload_YokoClassicUO.sc'
    if not canonical.is_file() or not alias.is_file(): raise RuntimeError(f'missing autoload files {d}')
    if canonical.read_bytes()!=alias.read_bytes(): raise RuntimeError(f'autoload aliases differ {d}')
    archive=directory/'Archive'; archive.mkdir(parents=True,exist_ok=True)
    shutil.copy2(alias,archive/alias.name); alias.unlink()

# Manager: synchronous Reload must win over an already-scheduled background reload.
rel='src/ClassicUO.Client/Game/Managers/YokoInjectionManager.cs'; s=load(rel)
s=repl(s,
'''        public void Reload()
        {
            (long lifecycleEpoch, CancellationToken cancellationToken) = CaptureLifecycle();
            Reload(lifecycleEpoch, cancellationToken);
        }''',
'''        public void Reload()
        {
            (long lifecycleEpoch, CancellationToken cancellationToken) = CaptureLifecycle();
            // Direct Reload is an explicit synchronous request (used by tests and
            // internal maintenance). Hold the publication gate for its lifetime so
            // a previously queued background worker cannot start later and supersede
            // this newer request before it publishes.
            lock (_catalogReloadLock)
                Reload(lifecycleEpoch, cancellationToken);
        }''','synchronous Reload ownership')

anchor='''        public bool RunChatCommand(string commandLine)
        {'''
helper='''        private void PublishColdProcedureFile(string filePath, string source,
            IReadOnlyList<YokoProcedureInfo> procedures)
        {
            if (procedures == null || procedures.Count == 0)
                return;
            string fullPath = Path.GetFullPath(filePath);
            lock (_proceduresLock)
            {
                _procedures.RemoveAll(procedure => string.Equals(
                    Path.GetFullPath(procedure.FilePath), fullPath,
                    StringComparison.OrdinalIgnoreCase));
                _procedures.AddRange(procedures);
                _procedures = _procedures
                    .OrderBy(procedure => procedure.FileName, StringComparer.OrdinalIgnoreCase)
                    .ThenBy(procedure => procedure.LineNumber)
                    .ToList();
                RebuildProcedureLookupLocked();
                _procedureSourceCache[fullPath] = source;
                _procedureFileCache[fullPath] = procedures;
            }
            foreach (YokoProcedureInfo procedure in procedures)
                if (!_running.ContainsKey(procedure.Key))
                    _procedureStates[procedure.Key] = procedure.IsValid
                        ? YokoProcedureState.Ready : YokoProcedureState.Error;
            Interlocked.Increment(ref _procedureCatalogRevision);
            UpdateValidationProblems(fullPath, procedures);
        }

        private bool QueueColdProcedureRun(string procedureName, string[] arguments,
            string originalCommand)
        {
            string requested = (procedureName ?? string.Empty).Trim();
            if (requested.Length == 0)
                return false;

            (long lifecycleEpoch, CancellationToken cancellationToken) = CaptureLifecycle();
            if (cancellationToken.IsCancellationRequested)
                return false;
            string[] copiedArguments = arguments?.ToArray() ?? Array.Empty<string>();

            Task.Factory.StartNew(() =>
            {
                try
                {
                    string[] files = Directory.EnumerateFiles(AutoloadPath, "*",
                            SearchOption.TopDirectoryOnly)
                        .Where(file => AutoloadExtensions.Contains(Path.GetExtension(file)))
                        .OrderBy(file => file, StringComparer.OrdinalIgnoreCase)
                        .ToArray();
                    string declarationPattern = @"(?im)^\\s*(?:SUB|FUNCTION)\\s+"
                        + Regex.Escape(requested) + @"(?:\\s*\\(|\\s|$)";
                    foreach (string file in files)
                    {
                        if (cancellationToken.IsCancellationRequested
                            || !IsLifecycleCurrent(lifecycleEpoch))
                            return;
                        string source = File.ReadAllText(file);
                        if (!Regex.IsMatch(source, declarationPattern,
                                RegexOptions.CultureInvariant))
                            continue;
                        IReadOnlyList<YokoProcedureInfo> procedures = DiscoverProcedures(
                            source, Path.GetFullPath(file),
                            Path.GetRelativePath(AutoloadPath, file));
                        YokoProcedureInfo match = procedures.FirstOrDefault(procedure =>
                            procedure.Name.Equals(requested, StringComparison.OrdinalIgnoreCase));
                        if (match == null)
                            continue;

                        EnqueueMainThreadAction(() =>
                        {
                            if (cancellationToken.IsCancellationRequested
                                || !IsLifecycleCurrent(lifecycleEpoch))
                                return;
                            PublishColdProcedureFile(file, source, procedures);
                            RunProcedure(match, copiedArguments, false);
                            // Keep the complete catalogue authoritative. If the file
                            // appeared after the current scan enumerated its inputs,
                            // force one full follow-up scan without delaying this run.
                            RequestProcedureCatalogReload(force: true);
                        });
                        return;
                    }
                }
                catch (Exception ex)
                {
                    if (IsLifecycleCurrent(lifecycleEpoch))
                        SetStatus("Cold AutoLoad lookup failed: " + ex.Message);
                }

                if (!cancellationToken.IsCancellationRequested
                    && IsLifecycleCurrent(lifecycleEpoch))
                {
                    RequestProcedureCatalogReload(
                        () => RunChatCommand(originalCommand));
                }
            }, CancellationToken.None,
                TaskCreationOptions.DenyChildAttach, TaskScheduler.Default);
            return true;
        }

        public bool RunChatCommand(string commandLine)
        {'''
s=repl(s,anchor,helper,'cold lookup helper')
old='''            YokoProcedureInfo procedure = nameIndex < tokens.Length ? FindProcedureByName(tokens[nameIndex]) : null;
            if (procedure == null && !scriptInvocation && !IsProcedureCatalogLoaded())
            {
                RequestProcedureCatalogReload(() => RunChatCommand(command));
                SetStatus("Yoko command queued while Autoload loads in background.");
                return true;
            }
            if (procedure != null)
                return RunProcedure(procedure.Key, tokens.Skip(nameIndex + 1).ToArray());'''
new='''            YokoProcedureInfo procedure = nameIndex < tokens.Length ? FindProcedureByName(tokens[nameIndex]) : null;
            if (procedure == null && !scriptInvocation && !IsProcedureCatalogLoaded())
            {
                string requestedProcedure = nameIndex < tokens.Length ? tokens[nameIndex] : string.Empty;
                if (QueueColdProcedureRun(requestedProcedure,
                        tokens.Skip(nameIndex + 1).ToArray(), command))
                {
                    SetStatus("Yoko command queued while the requested AutoLoad procedure resolves.");
                    return true;
                }
                RequestProcedureCatalogReload(() => RunChatCommand(command));
                SetStatus("Yoko command queued while Autoload loads in background.");
                return true;
            }
            if (procedure != null)
                return RunProcedure(procedure.Key, tokens.Skip(nameIndex + 1).ToArray());'''
s=repl(s,old,new,'RunChatCommand cold path')
save(rel,s)

# self-audit
assert 'bridge.IsDead(id) == 0' in load('external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs')
manual=load('src/ClassicUO.Client/Game/UI/Gumps/YokoManualGump.cs')
for x in ('_workspaceContextSymbols = snapshot;','ManualSymbolContext()','!symbol.IsRuntime'): assert x in manual
mgr=load('src/ClassicUO.Client/Game/Managers/YokoInjectionManager.cs')
for x in ('QueueColdProcedureRun','PublishColdProcedureFile','lock (_catalogReloadLock)\n                Reload'): assert x in mgr
for d in ('Autoload','src/ClassicUO.Client/Autoload'):
    directory=root/d
    assert not (directory/'Autoload_YokoClassicUO.sc').exists()
    assert (directory/'Archive/Autoload_YokoClassicUO.sc').stat().st_size>60000
print('NEXT PATCH PASS')
