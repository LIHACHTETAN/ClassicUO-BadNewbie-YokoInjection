from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit('usage: patch_v50_release9_extra.py <project-root>')
root = Path(sys.argv[1]).resolve()
if not (root / 'ClassicUO.sln').is_file():
    raise SystemExit('ClassicUO.sln missing')

def load(rel): return (root/rel).read_text(encoding='utf-8-sig')
def save(rel,text): (root/rel).write_text(text,encoding='utf-8',newline='')
def repl(text,old,new,label,count=1):
    n=text.count(old)
    if n!=count: raise RuntimeError(f'{label}: expected {count}, found {n}')
    return text.replace(old,new)

# 1) One dead-state authority for Dead(id) and FindMobile(dead/alive).
rel='external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs'
s=load(rel)
s=repl(s,
'''                    case "dead": if (bridge.GetHP(id) > 0) return false; break;
                    case "alive": if (bridge.GetHP(id) <= 0) return false; break;''',
'''                    case "dead": if (bridge.IsDead(id) == 0) return false; break;
                    case "alive": if (bridge.IsDead(id) != 0) return false; break;''',
'FindMobile dead/alive')
save(rel,s)

# 2) Manual needs filtered workspace rows + full runtime/workspace context for usage/dependency details.
rel='src/ClassicUO.Client/Game/UI/Gumps/YokoManualGump.cs'
s=load(rel)
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
            _workspaceSymbols = (symbols ?? Array.Empty<YokoApiSymbol>())
                .Where(symbol => symbol != null && !symbol.IsRuntime)
                .ToArray();
            _catalog = null;''',
'''            // Preserve the complete live index for dependency/usage lookup, while
            // exposing only real workspace declarations as Manual workspace rows.
            YokoApiSymbol[] snapshot = symbols as YokoApiSymbol[]
                ?? (symbols ?? Array.Empty<YokoApiSymbol>()).ToArray();
            _workspaceContextSymbols = snapshot;
            _workspaceSymbols = snapshot
                .Where(symbol => symbol != null && !symbol.IsRuntime)
                .ToArray();
            _catalog = null;''','manual dual snapshot')
s=repl(s,
'''        private static YokoApiSymbol[] ResolveManualSymbols(ManualEntry entry)
        {
            IReadOnlyList<YokoApiSymbol> snapshot = _workspaceSymbols;
            if (snapshot == null || snapshot.Count == 0 || !snapshot.Any(symbol => symbol.IsRuntime))
                snapshot = DefaultRuntimeSymbols;''',
'''        private static IReadOnlyList<YokoApiSymbol> ManualSymbolContext()
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
            IReadOnlyList<YokoApiSymbol> snapshot = ManualSymbolContext();''','manual resolve context')
s=repl(s,
'''            IReadOnlyList<YokoApiSymbol> symbols = _workspaceSymbols;
            if (symbols == null || symbols.Count == 0)
                symbols = DefaultRuntimeSymbols;''',
'''            IReadOnlyList<YokoApiSymbol> symbols = ManualSymbolContext();''','manual dependency context')
save(rel,s)

# 3) Verifier follows dual-snapshot invariant.
rel='scripts/VerifyV50Ide.py'; s=load(rel)
s=repl(s,
'''    and '_workspaceSymbols = (symbols ?? Array.Empty<YokoApiSymbol>())' in manual_workspace_update
    and '.Where(symbol => symbol != null && !symbol.IsRuntime)' in manual_workspace_update
    and '.ToArray();' in manual_workspace_update''',
'''    and '_workspaceContextSymbols = snapshot;' in manual_workspace_update
    and '_workspaceSymbols = snapshot' in manual_workspace_update
    and '.Where(symbol => symbol != null && !symbol.IsRuntime)' in manual_workspace_update
    and '.ToArray();' in manual_workspace_update''','verifier dual snapshot')
save(rel,s)

# 4) Remove the empty top-level alias completely; nested archive keeps compatibility copy.
for d in ('Autoload','src/ClassicUO.Client/Autoload'):
    alias=root/d/'Autoload_YokoClassicUO.sc'
    archived=root/d/'Archive'/'Autoload_YokoClassicUO.sc'
    if not archived.is_file() or archived.stat().st_size < 60000:
        raise RuntimeError(f'archived alias missing/incomplete: {d}')
    if alias.exists():
        alias.unlink()

# 5) Direct synchronous Reload must win over a previously queued background worker.
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
            // Direct Reload is an explicit synchronous request. Own the publication
            // gate for its full lifetime so a previously queued worker cannot start
            // later and supersede this newer reload before it publishes.
            lock (_catalogReloadLock)
                Reload(lifecycleEpoch, cancellationToken);
        }''','synchronous Reload ownership')

# 6) Cold chat procedure: resolve/publish just the requested file first, while the
# complete catalogue scan continues/refreshes in the background.
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
                            // A file can appear after an existing scan enumerated its
                            // inputs. Keep a full forced refresh authoritative, but do
                            // not make the requested procedure wait for that refresh.
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
                    RequestProcedureCatalogReload(() => RunChatCommand(originalCommand));
            }, CancellationToken.None,
                TaskCreationOptions.DenyChildAttach, TaskScheduler.Default);
            return true;
        }

        public bool RunChatCommand(string commandLine)
        {'''
s=repl(s,anchor,helper,'cold lookup helper')
s=repl(s,
'''            YokoProcedureInfo procedure = nameIndex < tokens.Length ? FindProcedureByName(tokens[nameIndex]) : null;
            if (procedure == null && !scriptInvocation && !IsProcedureCatalogLoaded())
            {
                RequestProcedureCatalogReload(() => RunChatCommand(command));
                SetStatus("Yoko command queued while Autoload loads in background.");
                return true;
            }
            if (procedure != null)
                return RunProcedure(procedure.Key, tokens.Skip(nameIndex + 1).ToArray());''',
'''            YokoProcedureInfo procedure = nameIndex < tokens.Length ? FindProcedureByName(tokens[nameIndex]) : null;
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
                return RunProcedure(procedure.Key, tokens.Skip(nameIndex + 1).ToArray());''','cold RunChatCommand route')
save(rel,s)

# Extra-patch self audit.
assert 'bridge.IsDead(id) == 0' in load('external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs')
manual=load('src/ClassicUO.Client/Game/UI/Gumps/YokoManualGump.cs')
for token in ('_workspaceContextSymbols = snapshot;', 'ManualSymbolContext()', '!symbol.IsRuntime'):
    assert token in manual
manager=load('src/ClassicUO.Client/Game/Managers/YokoInjectionManager.cs')
for token in ('QueueColdProcedureRun', 'PublishColdProcedureFile', 'lock (_catalogReloadLock)\n                Reload'):
    assert token in manager
for d in ('Autoload','src/ClassicUO.Client/Autoload'):
    assert not (root/d/'Autoload_YokoClassicUO.sc').exists()
    assert (root/d/'Archive'/'Autoload_YokoClassicUO.sc').stat().st_size > 60000
print('v50 Release 9 extra patch verification: PASS')
