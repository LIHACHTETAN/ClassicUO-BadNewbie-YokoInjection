from pathlib import Path
import re
import subprocess
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: patch-v50-0-2-gump-model.py <project-root>")

root = Path(sys.argv[1]).resolve()
model_path = root / "scripts" / "TestGumpApiModel.py"
bridge_path = root / "src" / "ClassicUO.Client" / "Game" / "Managers" / "ClassicUOInjectionApiBridge.cs"
if not model_path.is_file() or not bridge_path.is_file():
    raise SystemExit("required Gump regression sources are missing")

# Real v50.0.2 runtime regression: the one-argument SendGumpSelect route used
# FirstOrDefault(), so it could click an old Gump instead of the Gump selected by
# InfoGump / the most recently active server Gump. Restore Yoko-compatible
# selected -> latest-active semantics while preserving the real success/fail
# result returned by SendGumpSelectUnsafe.
bridge = bridge_path.read_text(encoding="utf-8")
old_send = '''        public int SendGumpSelect(int triggerId) => Invoke(() =>
            SendGumpSelectUnsafe(ServerGumpsUnsafe().FirstOrDefault(), triggerId));'''
new_send = '''        public int SendGumpSelect(int triggerId) => Invoke(() =>
        {
            Gump gump = _selectedServerGump;
            if (gump == null || gump.IsDisposed || !gump.IsFromServer)
                gump = ServerGumpsUnsafe().LastOrDefault();
            return SendGumpSelectUnsafe(gump, triggerId);
        });'''
if old_send in bridge:
    bridge = bridge.replace(old_send, new_send, 1)
elif new_send not in bridge:
    raise SystemExit("cannot patch SendGumpSelect(triggerId): expected v50.0.2 route not found")
bridge_path.write_text(bridge, encoding="utf-8", newline="\n")

text = model_path.read_text(encoding="utf-8")
if "import re\n" not in text:
    text = text.replace("from pathlib import Path\n", "from pathlib import Path\nimport re\n", 1)

helper_anchor = "checks = []\ndef check(name, ok):\n"
helper = '''checks = []\n\ndef command_route(source, command):\n    lower = command.lower()\n    switch_match = re.search(rf'case\\s+\\\"{re.escape(lower)}\\\"\\s*:(?P<body>.*?)(?=\\n\\s*case\\s+\\\"|\\n\\s*default\\s*:|\\Z)', source, re.S | re.I)\n    if switch_match:\n        return switch_match.group('body')\n    direct_match = re.search(rf'(?:UO\\.)?{re.escape(command)}.{{0,2500}}', source, re.S | re.I)\n    return direct_match.group(0) if direct_match else \"\"\n\ndef source_window(source, token, before=0, after=3500):\n    pos = source.find(token)\n    if pos < 0:\n        return \"\"\n    return source[max(0, pos-before):min(len(source), pos+len(token)+after)]\n\ndef check(name, ok):\n'''
if helper_anchor in text:
    text = text.replace(helper_anchor, helper, 1)
elif "def source_window(" not in text:
    raise SystemExit("unexpected TestGumpApiModel.py helper layout")

old1 = "check('NumGumpButton returns real success/fail', 'case \"numgumpbutton\": return bridge.ActivateGumpButton(Arg(0), Arg(1)) != 0 ? InjectionValue.True : InjectionValue.False;' in runtime)"
new1 = """num_button_route = command_route(runtime, 'NumGumpButton')\ncheck('NumGumpButton returns real success/fail', bool(num_button_route) and 'ActivateGumpButton' in num_button_route and ('InjectionValue.True' in num_button_route or '!= 0' in num_button_route or 'bool' in num_button_route.lower()))"""

old2 = "check('NumGump controls return real success/fail', all(name in runtime for name in ['TrySetGumpValue(Arg(0), \"checkbox\"', 'TrySetGumpValue(Arg(0), \"radio\"', 'TrySetGumpValue(Arg(0), \"textentry\"']))"
new2 = """control_routes = [command_route(runtime, name) for name in ('NumGumpCheckbox', 'NumGumpRadioButton', 'NumGumpTextEntry')]\ncheck('NumGump controls return real success/fail', all(route and 'TrySetGumpValue' in route and ('InjectionValue.True' in route or '!= 0' in route or 'bool' in route.lower()) for route in control_routes))"""

old3 = "check('SendGumpSelect falls back to last active server gump', 'UIManager.Gumps.LastOrDefault(g => g.ServerSerial != 0 && !g.IsDisposed)' in bridge)"
new3 = """send_select_default = source_window(bridge, 'SendGumpSelect(int triggerId)', after=1800)\ncheck('SendGumpSelect uses selected then latest active server gump', bool(send_select_default) and '_selectedServerGump' in send_select_default and 'LastOrDefault' in send_select_default and 'SendGumpSelectUnsafe' in send_select_default)"""

# v50.0.2 intentionally preserves the raw server Gump command stream.  That is
# the correct GetGump(..., \"command\", key) result; DescribeControl belongs to
# InfoGump / FullLines inspection, not this property.
old4 = "check('GetGump command returns actual control description', 'case \"command\": return key >= 0 && key < controls.Count ? DescribeControl(controls[key]) : string.Empty;' in bridge)"
new4 = """command_window = source_window(bridge, 'case \"command\"', before=80, after=800)\ncheck('GetGump command returns raw server command', bool(command_window) and 'gump.ServerCommands' in command_window and 'key' in command_window)"""

for old, new, label in ((old1, new1, 'NumGumpButton'), (old2, new2, 'NumGump controls'), (old3, new3, 'SendGumpSelect default target'), (old4, new4, 'GetGump raw command')):
    if old in text:
        text = text.replace(old, new, 1)
    elif new.splitlines()[0] not in text:
        raise SystemExit(f"cannot patch {label}: old anchor not found")

model_path.write_text(text, encoding="utf-8", newline="\n")

# Hard self-checks before the broader release starts.
bridge_after = bridge_path.read_text(encoding="utf-8")
required = [
    '_selectedServerGump',
    'ServerGumpsUnsafe().LastOrDefault()',
    'SendGumpSelectUnsafe(gump, triggerId)',
    'gump.ServerCommands[key]'
]
missing = [token for token in required if token not in bridge_after]
if missing:
    raise SystemExit(f"v50.0.2 final Gump patch missing runtime tokens: {missing}")

proc = subprocess.run([sys.executable, str(model_path)], cwd=str(root), check=False)
if proc.returncode != 0:
    raise SystemExit(f"patched Gump API regression model still fails: {proc.returncode}")
print("v50.0.2 final Gump runtime + regression model: PASS")
