#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Method:
    name: str
    body: str
    full_text: str


def strip_comments_and_strings(text: str) -> str:
    out: list[str] = []
    i = 0
    n = len(text)
    state = "code"
    while i < n:
        c = text[i]
        nxt = text[i + 1] if i + 1 < n else ""
        if state == "code":
            if c == "/" and nxt == "/":
                out.extend("  ")
                i += 2
                state = "line_comment"
            elif c == "/" and nxt == "*":
                out.extend("  ")
                i += 2
                state = "block_comment"
            elif c == '"':
                out.append('"')
                i += 1
                state = "string"
            elif c == "'":
                out.append("'")
                i += 1
                state = "char"
            else:
                out.append(c)
                i += 1
        elif state == "line_comment":
            if c == "\n":
                out.append("\n")
                state = "code"
            else:
                out.append(" ")
            i += 1
        elif state == "block_comment":
            if c == "*" and nxt == "/":
                out.extend("  ")
                i += 2
                state = "code"
            else:
                out.append("\n" if c == "\n" else " ")
                i += 1
        elif state == "string":
            if c == "\\":
                out.extend("  ")
                i += 2
            elif c == '"':
                out.append('"')
                i += 1
                state = "code"
            else:
                out.append("\n" if c == "\n" else " ")
                i += 1
        elif state == "char":
            if c == "\\":
                out.extend("  ")
                i += 2
            elif c == "'":
                out.append("'")
                i += 1
                state = "code"
            else:
                out.append("\n" if c == "\n" else " ")
                i += 1
    return "".join(out)


def find_matching_brace(text: str, open_index: int) -> int:
    depth = 0
    stripped = strip_comments_and_strings(text)
    for idx in range(open_index, len(stripped)):
        c = stripped[idx]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return idx
    raise ValueError(f"Unbalanced method block starting at index {open_index}")


def extract_methods(text: str) -> dict[str, Method]:
    # Good enough for ProfileManager-style methods; attributes and generic return types are tolerated.
    header_re = re.compile(
        r"(?m)^\s*(?:(?:public|private|internal|protected|static|async|sealed|virtual|override|new|unsafe)\s+)+"
        r"[\w<>,?\[\].:]+\s+(?P<name>[A-Za-z_]\w*)\s*\([^;{}]*\)\s*\{"
    )
    methods: dict[str, Method] = {}
    for match in header_re.finditer(text):
        name = match.group("name")
        open_index = text.find("{", match.start(), match.end())
        close_index = find_matching_brace(text, open_index)
        full = text[match.start(): close_index + 1]
        body = text[open_index + 1: close_index]
        methods[name] = Method(name=name, body=body, full_text=full)
    return methods


def reachable_from(methods: dict[str, Method], root: str) -> set[str]:
    if root not in methods:
        raise ValueError(f"Method {root}() was not found")
    names = set(methods)
    reached: set[str] = set()
    pending = [root]
    while pending:
        name = pending.pop()
        if name in reached:
            continue
        reached.add(name)
        code = strip_comments_and_strings(methods[name].body)
        for candidate in names:
            if candidate != name and re.search(rf"\b{re.escape(candidate)}\s*\(", code):
                pending.append(candidate)
    return reached


def check_profile_manager(path: Path) -> list[str]:
    raw = path.read_text(encoding="utf-8-sig")
    methods = extract_methods(raw)
    reachable = reachable_from(methods, "Load")
    live = "\n".join(methods[name].full_text for name in sorted(reachable))
    live_code = strip_comments_and_strings(live)

    failures: list[str] = []

    # String literals are intentionally checked on raw reachable text as well.
    forbidden = [
        (r"(?i)(?:^|[^A-Za-z0-9_])v2(?:[^A-Za-z0-9_]|$)", "legacy v2 token reachable from Load"),
        (r"(?i)default\.json", "default.json reachable from fresh Load"),
        (r"\bNewFromDefault\s*\(", "NewFromDefault() reachable from fresh Load"),
        (r"\bFile\s*\.\s*Copy\s*\(", "File.Copy reachable from fresh Load"),
        (r"\bDirectory\s*\.\s*(?:Move|CreateDirectory|GetFiles|GetDirectories)\s*\([^)]*(?:legacy|v2)", "legacy directory migration reachable from Load"),
        (r"(?i)\b(?:migrate|migration|legacy)\w*\s*\(", "migration/legacy helper reachable from Load"),
    ]
    for pattern, message in forbidden:
        target = live if "v2" in message or "default.json" in message else live_code
        if re.search(pattern, target):
            failures.append(message)

    load = methods["Load"].full_text
    if not re.search(r"\bservername\b", load, flags=re.IGNORECASE):
        failures.append("Load() does not use the connected server/shard name")
    if not re.search(r"\busername\b", load, flags=re.IGNORECASE):
        failures.append("Load() does not use the account/user name")
    if not re.search(r"\bcharactername\b", load, flags=re.IGNORECASE):
        failures.append("Load() does not use the character name")

    # A cache miss must create a fresh Profile object in the reachable load path.
    # This deliberately accepts a dedicated helper so long as it is reachable and does not hit forbidden migration/default routes.
    if not re.search(r"\bnew\s+Profile\s*\(", live_code):
        failures.append("fresh Load path never creates new Profile()")

    return failures


def run_fixture(name: str, source: str, expected_ok: bool) -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "ProfileManager.cs"
        p.write_text(source, encoding="utf-8")
        failures = check_profile_manager(p)
        ok = not failures
        if ok != expected_ok:
            raise AssertionError(f"fixture {name!r}: expected ok={expected_ok}, got failures={failures}")
        print(f"PASS fixture | {name}")


def self_test() -> None:
    common = """
internal static class ProfileManager
{
    static Profile LoadJson(string p) => null;
    static Profile NewFromDefault() => new Profile();
"""
    good = common + """
    public static void Load(string servername, string username, string charactername)
    {
        string path = MakePath(username, servername, charactername);
        CurrentProfile = LoadJson(path) ?? CreateFresh();
    }
    private static Profile CreateFresh() { return new Profile(); }
    private static string MakePath(string username, string servername, string charactername) => username + servername + charactername;
    static Profile CurrentProfile;
}
"""
    run_fixture("clean fresh profile", good, True)

    bad_v2 = common + """
    public static void Load(string servername, string username, string charactername)
    {
        string path = MakePath(username, servername, charactername);
        CurrentProfile = LoadJson(path) ?? MigrateLegacy();
    }
    private static Profile MigrateLegacy() { string old = \"v2\"; return new Profile(); }
    private static string MakePath(string username, string servername, string charactername) => username + servername + charactername;
    static Profile CurrentProfile;
}
"""
    run_fixture("reject v2 migration", bad_v2, False)

    bad_default = common + """
    public static void Load(string servername, string username, string charactername)
    {
        string path = MakePath(username, servername, charactername);
        CurrentProfile = LoadJson(path) ?? NewFromDefault();
    }
    private static string MakePath(string username, string servername, string charactername) => username + servername + charactername;
    static Profile CurrentProfile;
}
"""
    run_fixture("reject default fallback", bad_default, False)

    bad_copy = common + """
    public static void Load(string servername, string username, string charactername)
    {
        string path = MakePath(username, servername, charactername);
        CurrentProfile = LoadJson(path) ?? CopyOld(path);
    }
    private static Profile CopyOld(string path) { File.Copy(\"old\", path); return new Profile(); }
    private static string MakePath(string username, string servername, string charactername) => username + servername + charactername;
    static Profile CurrentProfile;
}
"""
    run_fixture("reject copy migration", bad_copy, False)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("profile_manager", nargs="?", help="Path to ProfileManager.cs")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("FRESH_PROFILE_GATE_SELFTEST=PASS")
        return 0

    if not args.profile_manager:
        parser.error("profile_manager is required unless --self-test is used")
    path = Path(args.profile_manager)
    if not path.is_file():
        print(f"FAIL | missing file: {path}", file=sys.stderr)
        return 2
    failures = check_profile_manager(path)
    if failures:
        for failure in failures:
            print("FAIL | " + failure)
        return 1
    print("PASS | fresh profile Load() has no reachable v2/default/migration/copy fallback")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
