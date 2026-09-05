#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path

REQUIRED = {
    "ClassicUO.exe",
    "cuo.dll",
    "Scintilla.dll",
    "SDL3.dll",
    "FNA3D.dll",
    "FAudio.dll",
    "libtheorafile.dll",
    "zlib.dll",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def is_built_name(name: str) -> bool:
    return bool(re.match(r"(?i)^client(?:[-_.].*)?built$", name)) or bool(re.match(r"(?i)^client-built(?:[-_.].*)?$", name))


def valid_client_dir(path: Path) -> tuple[bool, list[str]]:
    missing = sorted(name for name in REQUIRED if not (path / name).is_file())
    return not missing, missing


def discover(root: Path) -> list[Path]:
    found: list[Path] = []
    for base in (root, root / "project"):
        if not base.is_dir():
            continue
        for p in base.iterdir():
            if p.is_dir() and p.name.lower() not in {"client", "project"} and is_built_name(p.name):
                ok, _ = valid_client_dir(p)
                if ok:
                    found.append(p.resolve())
    return sorted(set(found), key=lambda p: str(p).casefold())


def choose_candidate(root: Path) -> Path:
    candidates = discover(root)
    if not candidates:
        raise RuntimeError("No fresh built-client directory matching client*-built with required binaries was found")
    if len(candidates) == 1:
        return candidates[0]

    signatures: dict[tuple[tuple[str, str], ...], list[Path]] = {}
    for candidate in candidates:
        signature = tuple(sorted((name, sha256(candidate / name)) for name in REQUIRED))
        signatures.setdefault(signature, []).append(candidate)
    if len(signatures) != 1:
        details = [str(p) for p in candidates]
        raise RuntimeError(f"Ambiguous built-client outputs with different binary hashes: {details}")
    return max(candidates, key=lambda p: p.stat().st_mtime_ns)


def stage(package_root: Path) -> dict[str, object]:
    package_root = package_root.resolve()
    project = package_root / "project"
    baseline = package_root / "client"
    if not (project / "ClassicUO.sln").is_file():
        raise RuntimeError("package root does not contain project/ClassicUO.sln")
    if not baseline.is_dir():
        raise RuntimeError("package root does not contain client/")

    candidate = choose_candidate(package_root)
    ok, missing = valid_client_dir(candidate)
    if not ok:
        raise RuntimeError(f"Built client is incomplete: {missing}")

    baseline_hashes = {name: sha256(baseline / name) for name in REQUIRED if (baseline / name).is_file()}
    built_hashes = {name: sha256(candidate / name) for name in REQUIRED}
    changed = sorted(name for name in REQUIRED if baseline_hashes.get(name) != built_hashes[name])
    if not any(name in changed for name in ("ClassicUO.exe", "cuo.dll")):
        raise RuntimeError("Built-client candidate does not change ClassicUO.exe or cuo.dll versus baseline; refusing possible stale baseline")

    backup = package_root / "client-baseline-rejected"
    if backup.exists():
        shutil.rmtree(backup)
    baseline.rename(backup)
    try:
        shutil.copytree(candidate, baseline)
        ok, missing = valid_client_dir(baseline)
        if not ok:
            raise RuntimeError(f"Staged built client lost required files: {missing}")
    except Exception:
        if baseline.exists():
            shutil.rmtree(baseline)
        backup.rename(baseline)
        raise
    shutil.rmtree(backup)

    # The build output is only an intermediate transport. Keeping it would create a third
    # top-level package root or leave generated binaries under project/.
    if candidate.exists():
        shutil.rmtree(candidate)

    result = {
        "status": "PASS",
        "candidate": str(candidate),
        "changed_required_binaries": changed,
        "classicuo_sha256": built_hashes["ClassicUO.exe"],
        "cuo_sha256": built_hashes["cuo.dll"],
        "temporary_candidate_removed": not candidate.exists(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


def self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="v50-built-client-") as td:
        root = Path(td)
        (root / "project").mkdir()
        (root / "project" / "ClassicUO.sln").write_text("fixture\n", encoding="utf-8")
        baseline = root / "client"
        baseline.mkdir()
        built = root / "client-v50.0.0-built"
        built.mkdir()
        for name in REQUIRED:
            (baseline / name).write_bytes(("old:" + name).encode("ascii"))
            (built / name).write_bytes(("new:" + name).encode("ascii"))
        (built / "Autoload").mkdir()
        (built / "Autoload" / "sample.sc").write_text("SUB Main()\nEND SUB\n", encoding="utf-8")

        result = stage(root)
        assert result["status"] == "PASS"
        assert result["temporary_candidate_removed"] is True
        assert not built.exists()
        assert sorted(p.name for p in root.iterdir()) == ["client", "project"]
        assert (root / "client" / "Autoload" / "sample.sc").is_file()
        assert (root / "client" / "ClassicUO.exe").read_bytes().startswith(b"new:")
        print("PASS fixture | fresh built client replaces baseline and temp output is removed")

    with tempfile.TemporaryDirectory(prefix="v50-stale-client-") as td:
        root = Path(td)
        (root / "project").mkdir()
        (root / "project" / "ClassicUO.sln").write_text("fixture\n", encoding="utf-8")
        baseline = root / "client"
        baseline.mkdir()
        built = root / "client-v50-built"
        built.mkdir()
        for name in REQUIRED:
            data = ("same:" + name).encode("ascii")
            (baseline / name).write_bytes(data)
            (built / name).write_bytes(data)
        try:
            stage(root)
        except RuntimeError as exc:
            assert "stale baseline" in str(exc)
            assert built.exists(), "rejected candidate must not be deleted"
            print("PASS fixture | identical stale baseline rejected without mutation")
        else:
            raise AssertionError("stale baseline candidate was accepted")

    print("BUILT_CLIENT_STAGE_SELFTEST=PASS")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-root", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.package_root is None:
        parser.error("--package-root is required unless --self-test is used")
    stage(args.package_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
