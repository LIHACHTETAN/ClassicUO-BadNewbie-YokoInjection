from __future__ import annotations

from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: patch-v50-release9-post.py <project-root>")

root = Path(sys.argv[1]).resolve()
if not (root / "ClassicUO.sln").is_file():
    raise SystemExit(f"ClassicUO.sln not found under {root}")


def load(rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8-sig")


def save(rel: str, text: str) -> None:
    (root / rel).write_text(text, encoding="utf-8", newline="")


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise RuntimeError(f"{label}: expected {expected} site(s), found {count}")
    return text.replace(old, new)


# 1. FindMobile(dead/alive) must use the same explicit dead-state bridge as UO.Dead(id).
rel = "external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs"
s = load(rel)
s = replace_exact(
    s,
    '                    case "dead": if (bridge.GetHP(id) > 0) return false; break;\n'
    '                    case "alive": if (bridge.GetHP(id) <= 0) return false; break;',
    '                    case "dead": if (bridge.IsDead(id) == 0) return false; break;\n'
    '                    case "alive": if (bridge.IsDead(id) != 0) return false; break;',
    "FindMobile dead/alive state source",
)
save(rel, s)

# 2. Keep the complete runtime+workspace snapshot for dependency/usage resolution.
# Runtime symbols are excluded only from the workspace-only Manual section.
rel = "src/ClassicUO.Client/Game/UI/Gumps/YokoManualGump.cs"
s = load(rel)
s = replace_exact(
    s,
    "            _workspaceSymbols = (symbols ?? Array.Empty<YokoApiSymbol>())\n"
    "                .Where(symbol => symbol != null && !symbol.IsRuntime)\n"
    "                .ToArray();",
    "            _workspaceSymbols = symbols as YokoApiSymbol[]\n"
    "                ?? (symbols ?? Array.Empty<YokoApiSymbol>()).ToArray();",
    "restore complete Manual snapshot",
)
s = replace_exact(
    s,
    "                         .Where(value => value.IsAutoload\n"
    "                             && value.Kind is YokoApiSymbolKind.Procedure or YokoApiSymbolKind.Function)",
    "                         .Where(value => !value.IsRuntime && value.IsAutoload\n"
    "                             && value.Kind is YokoApiSymbolKind.Procedure or YokoApiSymbolKind.Function)",
    "workspace Manual section runtime filter",
)
save(rel, s)

# Restore the deterministic verifier to the complete-snapshot contract.
rel = "scripts/VerifyV50Ide.py"
s = load(rel)
s = replace_exact(
    s,
    "    and '_workspaceSymbols = (symbols ?? Array.Empty<YokoApiSymbol>())' in manual_workspace_update\n"
    "    and '.Where(symbol => symbol != null && !symbol.IsRuntime)' in manual_workspace_update\n"
    "    and '.ToArray();' in manual_workspace_update",
    "    and '_workspaceSymbols = symbols as YokoApiSymbol[]' in manual_workspace_update\n"
    "    and '?? (symbols ?? Array.Empty<YokoApiSymbol>()).ToArray();' in manual_workspace_update",
    "VerifyV50Ide complete Manual snapshot",
)
save(rel, s)

# 3. A compatibility alias must not remain as an empty top-level .sc file: every
# top-level .sc file is an active script and must contain at least one procedure.
for relative_dir in ("Autoload", "src/ClassicUO.Client/Autoload"):
    directory = root / relative_dir
    alias = directory / "Autoload_YokoClassicUO.sc"
    archive = directory / "Archive" / "Autoload_YokoClassicUO.sc"
    if not archive.is_file() or archive.stat().st_size < 60000:
        raise RuntimeError(f"Archived AutoLoad alias missing/incomplete in {relative_dir}")
    if alias.exists():
        if alias.stat().st_size > 1024:
            raise RuntimeError(f"Unexpected full top-level AutoLoad alias remains in {relative_dir}")
        alias.unlink()

# 4. Cold command execution must not wait for full Manual/symbol indexing.
# Discover/publish the requested top-level file immediately, run it, and let the
# complete catalogue rebuild independently in the background.
rel = "src/ClassicUO.Client/Game/Managers/YokoInjectionManager.cs"
s = load(rel)
s = replace_exact(
    s,
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
                procedure = nameIndex < tokens.Length
                    ? TryPublishColdProcedure(tokens[nameIndex])
                    : null;
                if (procedure != null)
                {
                    // The requested procedure is runnable immediately. Build the complete
                    // Autoload/symbol/Manual catalogue independently in the background.
                    RequestProcedureCatalogReload();
                    return RunProcedure(procedure, tokens.Skip(nameIndex + 1).ToArray());
                }

                RequestProcedureCatalogReload(() => RunChatCommand(command));
                SetStatus("Yoko command queued while Autoload loads in background.");
                return true;
            }
            if (procedure != null)
                return RunProcedure(procedure.Key, tokens.Skip(nameIndex + 1).ToArray());''',
    "cold command execution route",
)
anchor = '''        internal YokoProcedureInfo FindProcedureByName(string name)
        {
            lock (_proceduresLock)
            {
                return _procedures.FirstOrDefault(p => p.Name.Equals(name, StringComparison.OrdinalIgnoreCase));
            }
        }
'''
helper = anchor + '''
        private YokoProcedureInfo TryPublishColdProcedure(string name)
        {
            string requested = name?.Trim();
            if (string.IsNullOrWhiteSpace(requested))
                return null;

            try
            {
                Directory.CreateDirectory(AutoloadPath);
                string[] files = Directory.EnumerateFiles(AutoloadPath, "*", SearchOption.TopDirectoryOnly)
                    .Where(file => AutoloadExtensions.Contains(Path.GetExtension(file)))
                    .OrderBy(file => Path.GetFileNameWithoutExtension(file)
                        .Equals(requested, StringComparison.OrdinalIgnoreCase) ? 0 : 1)
                    .ThenBy(file => file, StringComparer.OrdinalIgnoreCase)
                    .ToArray();

                foreach (string file in files)
                {
                    string source = File.ReadAllText(file);
                    if (source.IndexOf(requested, StringComparison.OrdinalIgnoreCase) < 0)
                        continue;

                    string fullPath = Path.GetFullPath(file);
                    IReadOnlyList<YokoProcedureInfo> procedures = DiscoverProcedures(source, fullPath,
                        Path.GetRelativePath(AutoloadPath, fullPath));
                    YokoProcedureInfo[] matches = procedures
                        .Where(item => item.Name.Equals(requested, StringComparison.OrdinalIgnoreCase))
                        .ToArray();
                    if (matches.Length != 1)
                        continue;

                    YokoProcedureInfo match = matches[0];
                    lock (_proceduresLock)
                    {
                        if (!_procedures.Any(item => item.Key.Equals(match.Key,
                                StringComparison.OrdinalIgnoreCase)))
                        {
                            var published = _procedures.ToList();
                            published.Add(match);
                            _procedures = published;
                            RebuildProcedureLookupLocked();
                        }
                    }
                    _procedureStates[match.Key] = match.IsValid
                        ? YokoProcedureState.Ready
                        : YokoProcedureState.Error;
                    return match;
                }
            }
            catch (Exception ex)
            {
                SetBackgroundStatus("Cold AutoLoad lookup: " + ex.Message);
            }

            return null;
        }
'''
s = replace_exact(s, anchor, helper, "cold procedure publish helper")
save(rel, s)

# Self-audit.
api = load("external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs")
if 'case "dead": if (bridge.IsDead(id) == 0)' not in api:
    raise RuntimeError("FindMobile dead-state patch verification failed")
manual = load("src/ClassicUO.Client/Game/UI/Gumps/YokoManualGump.cs")
if "_workspaceSymbols = symbols as YokoApiSymbol[]" not in manual:
    raise RuntimeError("Complete Manual snapshot verification failed")
if ".Where(value => !value.IsRuntime && value.IsAutoload" not in manual:
    raise RuntimeError("Workspace Manual section filter verification failed")
manager = load("src/ClassicUO.Client/Game/Managers/YokoInjectionManager.cs")
if "TryPublishColdProcedure" not in manager:
    raise RuntimeError("Cold procedure route verification failed")
for relative_dir in ("Autoload", "src/ClassicUO.Client/Autoload"):
    if (root / relative_dir / "Autoload_YokoClassicUO.sc").exists():
        raise RuntimeError(f"Top-level AutoLoad alias remains in {relative_dir}")

print("v50 Release 9 residual patch verification: PASS")
