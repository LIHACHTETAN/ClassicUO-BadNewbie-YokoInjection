from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: manual-v50-0-2-gate-fix.py <project-root>")

root = Path(sys.argv[1]).resolve()
project_manual = root / "src/ClassicUO.Client/YokoDocumentation/Manual/COMPLETE_RUNTIME_API_MANUAL.md"
text = project_manual.read_text(encoding="utf-8-sig")

replacements = [
    (
        "`Hide()` opens Target; `Hide(serial)` acts immediately.",
        "`UO.Hide()` opens a normal object Target; `Hide(serial)` acts immediately.",
    ),
    (
        "Uses `IsFromServer`, not `GumpID != 0`, so a real server Gump with GumpID 0 is valid.",
        "The Yoko Gump Inspector uses `IsFromServer`, not `GumpID != 0`, so a real server Gump with GumpID 0 is valid.",
    ),
    (
        "actual controls and ButtonID values",
        "actual controls and **ButtonID** values",
    ),
]

for old, new in replacements:
    if old not in text:
        raise SystemExit(f"required Manual source phrase missing: {old}")
    text = text.replace(old, new, 1)

project_manual.write_text(text, encoding="utf-8", newline="")
client_manual = root.parent / "client/YokoDocumentation/Manual/COMPLETE_RUNTIME_API_MANUAL.md"
client_manual.parent.mkdir(parents=True, exist_ok=True)
client_manual.write_text(text, encoding="utf-8", newline="")

assert "`UO.Hide()` opens a normal object Target" in text
assert "Yoko Gump Inspector" in text
assert "**ButtonID**" in text
print("v50.0.2 exact Manual gate wording applied and synchronized")
