from __future__ import annotations

from pathlib import Path
import shutil
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: patch-v50-release8.py <project-root>")

root = Path(sys.argv[1]).resolve()
if not (root / "ClassicUO.sln").is_file():
    raise SystemExit(f"ClassicUO.sln not found under {root}")


def load(rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8-sig")


def save(rel: str, text: str) -> None:
    path = root / rel
    path.write_text(text, encoding="utf-8", newline="")


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise RuntimeError(f"{label}: expected {expected} source site(s), found {count}")
    return text.replace(old, new)


# Compiler compatibility + dead-state semantics.
rel = "external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs"
s = load(rel)
old_named = "FindJournalPatternId(bridge.GetJournalText(foundedTextIndex), pattern, equals: false, ignoreCase)"
s = replace_exact(
    s,
    old_named,
    "FindJournalPatternId(bridge.GetJournalText(foundedTextIndex), pattern, false, ignoreCase)",
    "InjectionApiUO non-trailing named arguments",
    2,
)
s = replace_exact(
    s,
    ".Split('|', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);",
    ".Split(new[] { '|' }, StringSplitOptions.RemoveEmptyEntries)\n"
    "                .Select(pattern => pattern.Trim())\n"
    "                .Where(pattern => pattern.Length > 0)\n"
    "                .ToArray();",
    "InjectionApiUO TrimEntries compatibility",
)
s = replace_exact(
    s,
    "                return serial == bridge.Self ? bridge.Dead() : bridge.GetHP(serial) <= 0 ? 1 : 0;",
    "                return serial == bridge.Self ? bridge.Dead() : bridge.IsDead(serial);",
    "InjectionApiUO IsDeadState",
)
s = replace_exact(
    s,
    "            return serial > 0 && bridge.GetHP(serial) <= 0 ? 1 : 0;",
    "            return serial > 0 ? bridge.IsDead(serial) : 0;",
    "InjectionApiUO Dead(id)",
)
save(rel, s)

# InjectionValue: IsSupported() and GetKind() must agree.
rel = "external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs"
s = load(rel)
s = replace_exact(
    s,
    "            if (type.Equals(typeof(string)))",
    "            if (type.Equals(typeof(InjectionValue)))\n"
    "                return InjectionValueKind.Any;\n"
    "            else if (type.Equals(typeof(string)))",
    "InjectionValue Any mapping",
)
s = replace_exact(
    s,
    "            else if (typeof(Array).IsAssignableFrom(type))",
    "            else if (typeof(Array).IsAssignableFrom(type) || typeof(IEnumerable<InjectionValue>).IsAssignableFrom(type))",
    "InjectionValue enumerable mapping",
)
save(rel, s)

# Mixed concrete/Any native signatures need per-position wildcard dispatch.
rel = "external/InjectionScript/src/InjectionScript/Runtime/NativeSubrutineMetadata.cs"
s = load(rel)
s = replace_exact(
    s,
    "            subrutineDefinition = null;\n            return false;",
    "            // Delegate-backed registrations may mix concrete kinds with InjectionValue (Any).\n"
    "            // Resolve Any as a per-position wildcard and prefer the most specific compatible route.\n"
    "            InjectionValueKind[] actualKinds = argumentValues.Select(item => item.Kind).ToArray();\n"
    "            NativeSubrutineDefinition wildcard = subrutines.Values\n"
    "                .Where(item => item.Name.Equals(name, StringComparison.OrdinalIgnoreCase)\n"
    "                    && item.ArgumentCount == actualKinds.Length\n"
    "                    && item.ParameterKinds.Select((kind, index) =>\n"
    "                        kind == InjectionValueKind.Any || kind == actualKinds[index]).All(match => match))\n"
    "                .OrderBy(item => item.ParameterKinds.Count(kind => kind == InjectionValueKind.Any))\n"
    "                .FirstOrDefault();\n"
    "            if (wildcard != null)\n"
    "            {\n"
    "                subrutineDefinition = wildcard;\n"
    "                return true;\n"
    "            }\n\n"
    "            subrutineDefinition = null;\n"
    "            return false;",
    "Native mixed-Any dispatch",
)
save(rel, s)

# Manual workspace section must contain only workspace symbols, never runtime API rows.
rel = "src/ClassicUO.Client/Game/UI/Gumps/YokoManualGump.cs"
s = load(rel)
s = replace_exact(
    s,
    "            _workspaceSymbols = symbols as YokoApiSymbol[]\n"
    "                ?? (symbols ?? Array.Empty<YokoApiSymbol>()).ToArray();",
    "            _workspaceSymbols = (symbols ?? Array.Empty<YokoApiSymbol>())\n"
    "                .Where(symbol => symbol != null && !symbol.IsRuntime)\n"
    "                .ToArray();",
    "Yoko Manual workspace/runtime separation",
)
save(rel, s)

# The completion catalog is process-global; this test collection must not race other World instances.
rel = "tests/ClassicUO.UnitTests/Game/Managers/YokoApiSymbolIndexTests.cs"
s = load(rel)
s = replace_exact(
    s,
    '[CollectionDefinition("Yoko completion catalog")]',
    '[CollectionDefinition("Yoko completion catalog", DisableParallelization = true)]',
    "Yoko completion test isolation",
)
save(rel, s)

# Update test fixtures to the current bridge contract.
rel = "tests/ClassicUO.UnitTests/Game/Managers/YokoInjectionCompatibilityTests.cs"
s = load(rel)
s = replace_exact(
    s,
    "                    case nameof(IApiBridge.GetHP): return HpValue;\n"
    "                    case nameof(IApiBridge.Dead): return DeadValue;",
    "                    case nameof(IApiBridge.GetHP): return HpValue;\n"
    "                    case nameof(IApiBridge.Dead): return DeadValue;\n"
    "                    case nameof(IApiBridge.IsDead):\n"
    "                        return arguments.Length > 0 && (int)arguments[0] == 0x00001235 ? 1 : 0;",
    "RecordingBridge IsDead fixture",
)
s = replace_exact(
    s,
    "            Assert.Contains(proxy.Calls, c => c.Name == nameof(IApiBridge.UseSkill)\n"
    "                && string.Equals((string)c.Arguments[0], \"Tracking\", StringComparison.OrdinalIgnoreCase));",
    "            Assert.Contains(proxy.Calls, c => c.Name == nameof(IApiBridge.UseSkill)\n"
    "                && c.Arguments[0] is int skillId && skillId == 39);",
    "WaitingForMenu UseSkill fixture",
)
save(rel, s)

# Generator must consume the actual InjectionScript output produced by the outer solution build.
rel = "tools/YokoExampleGenerator/YokoExampleGenerator.csproj"
s = load(rel)
s = replace_exact(
    s,
    "bin\\Release\\netstandard2.0\\InjectionScript.dll",
    "bin\\Debug\\netstandard2.0\\InjectionScript.dll",
    "Yoko example generator InjectionScript reference",
)
save(rel, s)

# Regenerate Examples/MANIFEST from the just-built runtime before running unit tests.
rel = "BUILD_V50_WINDOWS.ps1"
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
s = replace_exact(s, unit_anchor, generator_block, "Yoko example regeneration build gate")
save(rel, s)

# Keep only one active full AutoLoad. Preserve the identical alias under a nested archive,
# which is intentionally excluded by the top-directory-only runnable catalogue.
marker = (
    "# v50 compatibility marker\n"
    "# Canonical active AutoLoad: autoload.sc\n"
    "# Full historical alias preserved in Archive/Autoload_YokoClassicUO.sc\n"
)
for relative_dir in ("Autoload", "src/ClassicUO.Client/Autoload"):
    directory = root / relative_dir
    canonical = directory / "autoload.sc"
    alias = directory / "Autoload_YokoClassicUO.sc"
    if not canonical.is_file() or not alias.is_file():
        raise RuntimeError(f"Missing AutoLoad source in {relative_dir}")
    if canonical.read_bytes() != alias.read_bytes():
        raise RuntimeError(f"Expected duplicate active AutoLoad sources in {relative_dir}, but bytes differ")
    archive = directory / "Archive"
    archive.mkdir(parents=True, exist_ok=True)
    shutil.copy2(alias, archive / alias.name)
    alias.write_text(marker, encoding="utf-8", newline="")

# Patch self-audit.
api_check = load("external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs")
if old_named in api_check or "StringSplitOptions.TrimEntries" in api_check:
    raise RuntimeError("Compiler compatibility patch verification failed")
if api_check.count("bridge.IsDead(serial)") < 2:
    raise RuntimeError("Dead-state patch verification failed")
iv_check = load("external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs")
if "return InjectionValueKind.Any;" not in iv_check or "typeof(IEnumerable<InjectionValue>).IsAssignableFrom(type)" not in iv_check:
    raise RuntimeError("InjectionValue patch verification failed")
metadata_check = load("external/InjectionScript/src/InjectionScript/Runtime/NativeSubrutineMetadata.cs")
if "per-position wildcard" not in metadata_check:
    raise RuntimeError("Mixed-Any dispatch patch verification failed")
manual_check = load("src/ClassicUO.Client/Game/UI/Gumps/YokoManualGump.cs")
if "!symbol.IsRuntime" not in manual_check:
    raise RuntimeError("Workspace symbol patch verification failed")
symbol_check = load("tests/ClassicUO.UnitTests/Game/Managers/YokoApiSymbolIndexTests.cs")
if "DisableParallelization = true" not in symbol_check:
    raise RuntimeError("Completion test isolation patch verification failed")
compat_check = load("tests/ClassicUO.UnitTests/Game/Managers/YokoInjectionCompatibilityTests.cs")
if "case nameof(IApiBridge.IsDead)" not in compat_check or "skillId == 39" not in compat_check:
    raise RuntimeError("Compatibility fixture patch verification failed")
build_check = load("BUILD_V50_WINDOWS.ps1")
if "Regenerate Yoko engine examples from current runtime" not in build_check:
    raise RuntimeError("Example regeneration gate verification failed")
for relative_dir in ("Autoload", "src/ClassicUO.Client/Autoload"):
    directory = root / relative_dir
    if (directory / "Autoload_YokoClassicUO.sc").stat().st_size > 1024:
        raise RuntimeError(f"Duplicate active AutoLoad alias remains in {relative_dir}")
    if (directory / "Archive/Autoload_YokoClassicUO.sc").stat().st_size < 60000:
        raise RuntimeError(f"Archived AutoLoad alias is incomplete in {relative_dir}")

print("v50 Release 8 source patch verification: PASS")
