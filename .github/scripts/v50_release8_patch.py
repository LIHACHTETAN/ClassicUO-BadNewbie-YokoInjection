from __future__ import annotations
from pathlib import Path
import collections
import json
import re
import shutil
import sys

if len(sys.argv) != 2:
    raise SystemExit('usage: v50_release8_patch.py <project-root>')
root = Path(sys.argv[1]).resolve()
if not (root / 'ClassicUO.sln').is_file():
    raise SystemExit(f'ClassicUO.sln not found under {root}')


def load(rel: str) -> str:
    return (root / rel).read_text(encoding='utf-8-sig')


def save(rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected exactly 1 site, found {count}')
    return text.replace(old, new, 1)

# Exact SDK resolution for the release runner.
global_path = root / 'global.json'
global_json = json.loads(global_path.read_text(encoding='utf-8-sig'))
global_json.setdefault('sdk', {})['rollForward'] = 'disable'
global_path.write_text(json.dumps(global_json, indent=2) + '\n', encoding='utf-8')

# InjectionValue: IsSupported and GetKind must agree for pass-through runtime values.
rel = 'external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs'
s = load(rel)
old = '''        public static InjectionValueKind GetKind(Type type)\n        {\n            if (type.Equals(typeof(string)))\n                return InjectionValueKind.String;\n            else if (type.Equals(typeof(int)))\n                return InjectionValueKind.Integer;\n            else if (type.Equals(typeof(void)))\n                return InjectionValueKind.Unit;\n            else if (type.Equals(typeof(double)))\n                return InjectionValueKind.Decimal;\n            else if (typeof(Array).IsAssignableFrom(type))\n                return InjectionValueKind.Array;\n            else if (typeof(InjectionObject).IsAssignableFrom(type))\n                return InjectionValueKind.Object;\n\n            throw new NotSupportedException($"Unsupported type {type.Name}.");\n        }'''
new = '''        public static InjectionValueKind GetKind(Type type)\n        {\n            if (type.Equals(typeof(InjectionValue)))\n                return InjectionValueKind.Any;\n            else if (type.Equals(typeof(string)))\n                return InjectionValueKind.String;\n            else if (type.Equals(typeof(int)))\n                return InjectionValueKind.Integer;\n            else if (type.Equals(typeof(void)))\n                return InjectionValueKind.Unit;\n            else if (type.Equals(typeof(double)))\n                return InjectionValueKind.Decimal;\n            else if (typeof(Array).IsAssignableFrom(type) || typeof(IEnumerable<InjectionValue>).IsAssignableFrom(type))\n                return InjectionValueKind.Array;\n            else if (typeof(InjectionObject).IsAssignableFrom(type))\n                return InjectionValueKind.Object;\n\n            throw new NotSupportedException($"Unsupported type {type.Name}.");\n        }'''
s = replace_once(s, old, new, 'InjectionValue.GetKind')
save(rel, s)

# Native dispatch: Any is a per-position wildcard, not only an all-Any signature.
rel = 'external/InjectionScript/src/InjectionScript/Runtime/NativeSubrutineMetadata.cs'
s = load(rel)
old = '''        public bool TryGet(string name, IEnumerable<InjectionValue> argumentValues, out NativeSubrutineDefinition subrutineDefinition)\n        {\n            var key = NativeSubrutineDefinition.GetSignature(name, argumentValues);\n            if (subrutines.TryGetValue(key, out var value))\n            {\n                subrutineDefinition = value;\n                return true;\n            }\n\n            key = NativeSubrutineDefinition.GetAnySignature(name, argumentValues);\n            if (subrutines.TryGetValue(key, out value))\n            {\n                subrutineDefinition = value;\n                return true;\n            }\n\n            subrutineDefinition = null;\n            return false;\n        }'''
new = '''        public bool TryGet(string name, IEnumerable<InjectionValue> argumentValues, out NativeSubrutineDefinition subrutineDefinition)\n        {\n            InjectionValue[] arguments = argumentValues as InjectionValue[]\n                ?? (argumentValues ?? Enumerable.Empty<InjectionValue>()).ToArray();\n            var key = NativeSubrutineDefinition.GetSignature(name, arguments);\n            if (subrutines.TryGetValue(key, out var value))\n            {\n                subrutineDefinition = value;\n                return true;\n            }\n\n            // Any is a per-parameter wildcard. Exact signatures win first; then\n            // choose the compatible registration with the most concrete slots.\n            InjectionValueKind[] actualKinds = arguments.Select(argument => argument.Kind).ToArray();\n            NativeSubrutineDefinition compatible = subrutines.Values\n                .Where(candidate => candidate.Name.Equals(name, StringComparison.OrdinalIgnoreCase)\n                    && candidate.ArgumentCount == actualKinds.Length)\n                .Where(candidate => candidate.ParameterKinds.Select((kind, index) =>\n                        kind == InjectionValueKind.Any || kind == actualKinds[index]).All(match => match))\n                .OrderByDescending(candidate => candidate.ParameterKinds.Count(kind => kind != InjectionValueKind.Any))\n                .ThenBy(candidate => candidate.GetSignature(), StringComparer.OrdinalIgnoreCase)\n                .FirstOrDefault();\n            if (compatible != null)\n            {\n                subrutineDefinition = compatible;\n                return true;\n            }\n\n            subrutineDefinition = null;\n            return false;\n        }'''
s = replace_once(s, old, new, 'NativeSubrutineMetadata.TryGet')
save(rel, s)

# Runtime compatibility and behavior corrections.
rel = 'external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs'
s = load(rel)
old_named = 'FindJournalPatternId(bridge.GetJournalText(foundedTextIndex), pattern, equals: false, ignoreCase)'
if s.count(old_named) != 2:
    raise RuntimeError(f'InjectionApiUO named-argument sites: expected 2, found {s.count(old_named)}')
s = s.replace(old_named, 'FindJournalPatternId(bridge.GetJournalText(foundedTextIndex), pattern, false, ignoreCase)')
old_split = ".Split('|', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);"
new_split = ".Split(new[] { '|' }, StringSplitOptions.RemoveEmptyEntries)\n                .Select(pattern => pattern.Trim())\n                .Where(pattern => pattern.Length > 0)\n                .ToArray();"
s = replace_once(s, old_split, new_split, 'InjectionApiUO TrimEntries')
s = replace_once(s,
'''                return serial == bridge.Self ? bridge.Dead() : bridge.GetHP(serial) <= 0 ? 1 : 0;''',
'''                return serial == bridge.Self ? bridge.Dead() : bridge.IsDead(serial);''',
'IsDeadState')
s = replace_once(s,
'''                    case "dead": if (bridge.GetHP(id) > 0) return false; break;\n                    case "alive": if (bridge.GetHP(id) <= 0) return false; break;''',
'''                    case "dead": if (bridge.IsDead(id) == 0) return false; break;\n                    case "alive": if (bridge.IsDead(id) != 0) return false; break;''',
'FindMobile dead/alive')
s = replace_once(s,
'''            return serial > 0 && bridge.GetHP(serial) <= 0 ? 1 : 0;''',
'''            return serial > 0 ? bridge.IsDead(serial) : 0;''',
'UO.Dead remote state')
s = replace_once(s,
'''                if (ConvertSkillName(value).HasValue)\n                {\n                    UseSkillCore(value);\n                    return;\n                }''',
'''                if (ConvertSkillName(value).HasValue)\n                {\n                    bridge.UseSkill(value);\n                    return;\n                }''',
'TriggerWaitAction skill name')
save(rel, s)

# Preserve the original skill name through the bridge for WaitingForMenu/Journal triggers.
rel = 'external/InjectionScript/src/InjectionScript/Runtime/IApiBridge.cs'
s = load(rel)
s = replace_once(s, '        int UseSkill(int skillId);',
'''        int UseSkill(int skillId);\n        int UseSkill(string skillName);''', 'IApiBridge.UseSkill(string)')
save(rel, s)

rel = 'src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs'
s = load(rel)
old = '''        public int UseSkill(int skillId)\n        {\n            if (skillId <= 0 || IsOnline() == 0)\n                return 0;\n            Invoke(() => GameActions.UseSkill(skillId - 1));\n            return 1;\n        }'''
new = old + '''\n        public int UseSkill(string skillName) => Invoke(() =>\n        {\n            if (IsOnline() == 0)\n                return 0;\n            Skill skill = FindSkillUnsafe(skillName);\n            if (skill == null)\n                return 0;\n            GameActions.UseSkill(skill.Index);\n            return 1;\n        });'''
s = replace_once(s, old, new, 'ClassicUOInjectionApiBridge.UseSkill(string)')
save(rel, s)

# The completion/manual catalogue is process-global. Its tests must not race World instances
# from other xUnit collections that publish their own catalogue snapshots.
rel = 'tests/ClassicUO.UnitTests/Game/Managers/YokoApiSymbolIndexTests.cs'
s = load(rel)
s = replace_once(s, '[CollectionDefinition("Yoko completion catalog")]',
                 '[CollectionDefinition("Yoko completion catalog", DisableParallelization = true)]',
                 'completion catalogue test isolation')
save(rel, s)

# The explicit remote mobile used by Dead()/FindMobile(dead) must actually be dead in the bridge mock.
rel = 'tests/ClassicUO.UnitTests/Game/Managers/YokoInjectionCompatibilityTests.cs'
s = load(rel)
s = replace_once(s,
'''                    case nameof(IApiBridge.GetHP): return HpValue;\n                    case nameof(IApiBridge.Dead): return DeadValue;''',
'''                    case nameof(IApiBridge.GetHP): return HpValue;\n                    case nameof(IApiBridge.Dead): return DeadValue;\n                    case nameof(IApiBridge.IsDead): return (int)arguments[0] == 0x00001235 ? 1 : 0;''',
'remote dead mobile mock')
save(rel, s)

# Keep the latest alias for reference but remove it from the active top-level AutoLoad catalogue.
for base in ('src/ClassicUO.Client/Autoload', 'Autoload'):
    src = root / base / 'Autoload_YokoClassicUO.sc'
    if src.is_file():
        dst = root / base / 'Legacy' / src.name
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            dst.unlink()
        shutil.move(str(src), str(dst))

# Runtime inventory now exposes two previously omitted exact arities. Keep generated examples,
# README, index and manifest synchronized before the source-verification gate hashes the tree.
examples = root / 'src/ClassicUO.Client/YokoDocumentation/Examples'
manifest_path = examples / 'MANIFEST.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
manifest['exactSignatures'] = 1336
for entry in manifest['files']:
    if entry.get('Name') == 'UO.InJournal':
        entry['Arities'] = [1, 2]
    elif entry.get('Name') == 'UO.InJournalBetweenTimes':
        entry['Arities'] = [2, 3, 4]
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

path = examples / 'Commands/08_UI_Chat_And_Journal/UO_InJournal.sc'
s = path.read_text(encoding='utf-8-sig')
s = replace_once(s, '# Registered arities: 1', '# Registered arities: 1 | 2', 'InJournal example header')
marker = '# Main is intentionally safe: choose one of the procedures above in the IDE.\n'
block = '''# Variant 1: direct call of UO.InJournal/2\nSUB UO_InJournal_A2_Direct()\n    UO.InJournal('example', 0)\nEND SUB\n\n# Variant 2: the same call with named variables that are easy to replace\nSUB UO_InJournal_A2_Variables()\n    VAR arg1 = 'example' # pattern\n    VAR arg2 = 0 # maxLinesOrIgnoreCase\n    UO.InJournal(arg1, arg2)\nEND SUB\n\n# Variant 3: capture and display the returned value\nSUB UO_InJournal_A2_Result()\n    VAR resultValue = UO.InJournal('example', 0)\n    UO.Print('Result: ' + CStr(resultValue))\nEND SUB\n\n'''
s = replace_once(s, marker, block + marker, 'InJournal arity-2 example')
path.write_text(s, encoding='utf-8', newline='')

path = examples / 'Commands/08_UI_Chat_And_Journal/UO_InJournalBetweenTimes.sc'
s = path.read_text(encoding='utf-8-sig')
s = replace_once(s, '# Registered arities: 3 | 4', '# Registered arities: 2 | 3 | 4', 'InJournalBetweenTimes example header')
marker = '# Variant 1: direct call of UO.InJournalBetweenTimes/3\n'
block = '''# Variant 1: direct call of UO.InJournalBetweenTimes/2\nSUB UO_InJournalBetweenTimes_A2_Direct()\n    UO.InJournalBetweenTimes('example', 0)\nEND SUB\n\n# Variant 2: the same call with named variables that are easy to replace\nSUB UO_InJournalBetweenTimes_A2_Variables()\n    VAR arg1 = 'example' # pattern\n    VAR arg2 = 0 # start_time\n    UO.InJournalBetweenTimes(arg1, arg2)\nEND SUB\n\n# Variant 3: capture and display the returned value\nSUB UO_InJournalBetweenTimes_A2_Result()\n    VAR resultValue = UO.InJournalBetweenTimes('example', 0)\n    UO.Print('Result: ' + CStr(resultValue))\nEND SUB\n\n'''
s = replace_once(s, marker, block + marker, 'InJournalBetweenTimes arity-2 example')
path.write_text(s, encoding='utf-8', newline='')

readme = examples / 'README_RU.md'
s = readme.read_text(encoding='utf-8-sig')
if '1334 точных перегрузок' not in s:
    raise RuntimeError('README_RU exact-signature count anchor not found')
readme.write_text(s.replace('1334 точных перегрузок', '1336 точных перегрузок', 1), encoding='utf-8', newline='')

index = examples / 'INDEX.csv'
lines = []
seen_index = set()
for line in index.read_text(encoding='utf-8-sig').splitlines():
    if '"UO.InJournal"' in line:
        line, count = re.subn(r'"1"(?=,)', '"1|2"', line, count=1)
        if count != 1:
            raise RuntimeError('INDEX UO.InJournal arity anchor not found')
        seen_index.add('InJournal')
    if '"UO.InJournalBetweenTimes"' in line:
        line, count = re.subn(r'"3\|4"(?=,)', '"2|3|4"', line, count=1)
        if count != 1:
            raise RuntimeError('INDEX UO.InJournalBetweenTimes arity anchor not found')
        seen_index.add('InJournalBetweenTimes')
    lines.append(line)
if seen_index != {'InJournal', 'InJournalBetweenTimes'}:
    raise RuntimeError(f'INDEX rows not patched: {seen_index}')
index.write_text('\r\n'.join(lines) + '\r\n', encoding='utf-8', newline='')

# Patch self-audit: no duplicate procedure/function names across the active top-level AutoLoad files.
active = root / 'src/ClassicUO.Client/Autoload'
seen = collections.defaultdict(list)
for script in active.glob('*.sc'):
    text = script.read_text(encoding='utf-8-sig')
    for match in re.finditer(r'(?im)^\s*(?:sub|function)\s+([A-Za-z_][A-Za-z0-9_]*)', text):
        seen[match.group(1).lower()].append(script.name)
duplicates = {name: files for name, files in seen.items() if len(files) > 1}
if duplicates:
    sample = list(duplicates.items())[:10]
    raise RuntimeError(f'active AutoLoad duplicate declarations remain: {sample}')
if manifest['exactSignatures'] != 1336:
    raise RuntimeError('example manifest exactSignatures is not 1336')
print(f'v50 Release 8 source patch PASS; active AutoLoad files={len(list(active.glob("*.sc")))} declarations={sum(len(v) for v in seen.values())}; manifest exactSignatures=1336')
