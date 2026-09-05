#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

FORBIDDEN_DIRS = {".git", "bin", "obj", "publish", "__pycache__", ".vs"}
FORBIDDEN_SUFFIXES = {".bak", ".old", ".tmp", ".orig", ".rej", ".pyc", ".pyo"}
REQUIRED_CLIENT_FILES = {
    "ClassicUO.exe",
    "cuo.dll",
    "Scintilla.dll",
    "SDL3.dll",
    "FNA3D.dll",
    "FAudio.dll",
    "libtheorafile.dll",
    "zlib.dll",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def normalized_rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def collect_files(root: Path) -> list[Path]:
    return sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: normalized_rel(p, root).lower())


def validate_staging(root: Path) -> dict[str, object]:
    if not root.is_dir():
        raise RuntimeError(f"Staging root is missing: {root}")
    top = sorted(p.name for p in root.iterdir())
    if top != ["client", "project"]:
        raise RuntimeError(f"Top-level staging entries must be exactly project/ and client/, got: {top}")

    project = root / "project"
    client = root / "client"
    if not (project / "ClassicUO.sln").is_file():
        raise RuntimeError("Missing project/ClassicUO.sln")

    missing_client = sorted(name for name in REQUIRED_CLIENT_FILES if not (client / name).is_file())
    if missing_client:
        raise RuntimeError(f"Missing required client files: {missing_client}")

    forbidden_dirs: list[str] = []
    forbidden_files: list[str] = []
    nested_zips: list[str] = []
    case_map: dict[str, str] = {}
    case_collisions: list[tuple[str, str]] = []

    for p in root.rglob("*"):
        rel = normalized_rel(p, root)
        if p.is_dir() and p.name.lower() in {d.lower() for d in FORBIDDEN_DIRS}:
            forbidden_dirs.append(rel)
        if p.is_file():
            if p.suffix.lower() in FORBIDDEN_SUFFIXES:
                forbidden_files.append(rel)
            if p.suffix.lower() == ".zip":
                nested_zips.append(rel)
            key = rel.casefold()
            prior = case_map.get(key)
            if prior is not None and prior != rel:
                case_collisions.append((prior, rel))
            else:
                case_map[key] = rel

    if forbidden_dirs:
        raise RuntimeError(f"Forbidden build/cache directories in package: {forbidden_dirs[:20]}")
    if forbidden_files:
        raise RuntimeError(f"Forbidden backup/temp files in package: {forbidden_files[:20]}")
    if nested_zips:
        raise RuntimeError(f"Nested ZIP files are not allowed in final project+client package: {nested_zips[:20]}")
    if case_collisions:
        raise RuntimeError(f"Case-insensitive path collisions: {case_collisions[:20]}")

    files = collect_files(root)
    return {
        "file_count": len(files),
        "project_file_count": sum(1 for p in files if normalized_rel(p, root).startswith("project/")),
        "client_file_count": sum(1 for p in files if normalized_rel(p, root).startswith("client/")),
        "total_bytes": sum(p.stat().st_size for p in files),
    }


def write_zip(root: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as zf:
        for path in collect_files(root):
            arcname = normalized_rel(path, root)
            zf.write(path, arcname)


def is_unsafe_zip_name(name: str) -> bool:
    # Always reason about ZIP paths as POSIX paths. Reject Windows absolute/drive forms too.
    raw = name.replace("\\", "/")
    p = PurePosixPath(raw)
    if p.is_absolute():
        return True
    if re.match(r"^[A-Za-z]:/", raw):
        return True
    return any(part == ".." for part in p.parts)


def verify_zip(output: Path) -> dict[str, object]:
    with zipfile.ZipFile(output, "r") as zf:
        bad_crc = zf.testzip()
        if bad_crc is not None:
            raise RuntimeError(f"ZIP CRC/compressed-data failure: {bad_crc}")

        names = [i.filename for i in zf.infolist() if not i.is_dir()]
        unsafe = [name for name in names if is_unsafe_zip_name(name)]
        if unsafe:
            raise RuntimeError(f"Unsafe ZIP paths: {unsafe[:20]}")

        exact_duplicates = sorted({name for name in names if names.count(name) > 1})
        if exact_duplicates:
            raise RuntimeError(f"Duplicate ZIP entry names: {exact_duplicates[:20]}")

        case_map: dict[str, str] = {}
        case_collisions: list[tuple[str, str]] = []
        for name in names:
            key = name.casefold()
            prior = case_map.get(key)
            if prior is not None and prior != name:
                case_collisions.append((prior, name))
            else:
                case_map[key] = name
        if case_collisions:
            raise RuntimeError(f"Case-insensitive ZIP collisions: {case_collisions[:20]}")

        roots = sorted({PurePosixPath(name).parts[0] for name in names if PurePosixPath(name).parts})
        if roots != ["client", "project"]:
            raise RuntimeError(f"ZIP roots must be exactly project/client, got {roots}")

        return {
            "zip_entries": len(zf.infolist()),
            "zip_files": len(names),
            "zip_uncompressed_bytes": sum(i.file_size for i in zf.infolist() if not i.is_dir()),
            "zip_compressed_bytes": sum(i.compress_size for i in zf.infolist() if not i.is_dir()),
        }


def compare_tree(source: Path, extracted: Path) -> dict[str, object]:
    source_files = {normalized_rel(p, source): p for p in collect_files(source)}
    extracted_files = {normalized_rel(p, extracted): p for p in collect_files(extracted)}
    missing = sorted(set(source_files) - set(extracted_files))
    extra = sorted(set(extracted_files) - set(source_files))
    if missing or extra:
        raise RuntimeError(f"Fresh extraction file-list mismatch: missing={missing[:20]} extra={extra[:20]}")

    mismatches: list[str] = []
    for rel in sorted(source_files):
        if sha256_file(source_files[rel]) != sha256_file(extracted_files[rel]):
            mismatches.append(rel)
    if mismatches:
        raise RuntimeError(f"Fresh extraction SHA mismatches: {mismatches[:20]}")

    return {
        "source_files": len(source_files),
        "extracted_files": len(extracted_files),
        "missing": 0,
        "extra": 0,
        "sha_mismatches": 0,
    }


def package(staging: Path, output: Path, report: Path | None, sha_sidecar: Path | None) -> dict[str, object]:
    stage_info = validate_staging(staging)
    write_zip(staging, output)
    zip_info = verify_zip(output)

    with tempfile.TemporaryDirectory(prefix="v50-fresh-extract-") as td:
        fresh = Path(td)
        with zipfile.ZipFile(output, "r") as zf:
            # Safe after verify_zip() rejected traversal/absolute paths.
            zf.extractall(fresh)
        extract_info = compare_tree(staging, fresh)
        # Re-validate the extracted tree independently.
        extracted_stage_info = validate_staging(fresh)

    digest = sha256_file(output)
    result = {
        "status": "PASS",
        "archive": output.name,
        "archive_bytes": output.stat().st_size,
        "sha256": digest,
        **stage_info,
        **zip_info,
        **extract_info,
        "extracted_validation": extracted_stage_info,
    }

    if sha_sidecar is not None:
        sha_sidecar.parent.mkdir(parents=True, exist_ok=True)
        sha_sidecar.write_text(f"{digest}  {output.name}\n", encoding="ascii")
    if report is not None:
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps(result, indent=2, sort_keys=True))
    return result


def self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="v50-package-selftest-") as td:
        base = Path(td)
        stage = base / "stage"
        (stage / "project").mkdir(parents=True)
        (stage / "client").mkdir(parents=True)
        (stage / "project" / "ClassicUO.sln").write_text("fixture\n", encoding="utf-8")
        (stage / "project" / "src.txt").write_text("source\n", encoding="utf-8")
        for name in REQUIRED_CLIENT_FILES:
            (stage / "client" / name).write_bytes((name + "\n").encode("ascii"))

        out = base / "fixture.zip"
        sidecar = base / "fixture.sha256.txt"
        report = base / "fixture.json"
        result = package(stage, out, report, sidecar)
        assert result["status"] == "PASS"
        assert out.is_file() and sidecar.is_file() and report.is_file()
        print("PASS fixture | clean project+client package")

        # Ensure nested ZIP rejection works.
        (stage / "project" / "bad.zip").write_bytes(b"not a real zip")
        try:
            validate_staging(stage)
        except RuntimeError as exc:
            assert "Nested ZIP" in str(exc)
            print("PASS fixture | nested zip rejected")
        else:
            raise AssertionError("nested ZIP was not rejected")
        (stage / "project" / "bad.zip").unlink()

        # Verify traversal detection independently using a malicious ZIP entry.
        malicious = base / "malicious.zip"
        with zipfile.ZipFile(malicious, "w") as zf:
            zf.writestr("../escape.txt", "x")
            zf.writestr("project/ClassicUO.sln", "x")
            zf.writestr("client/ClassicUO.exe", "x")
        try:
            verify_zip(malicious)
        except RuntimeError as exc:
            assert "Unsafe ZIP" in str(exc)
            print("PASS fixture | traversal entry rejected")
        else:
            raise AssertionError("unsafe ZIP traversal was not rejected")

        # Case-insensitive collision must be rejected even if Windows would normally mask it.
        collision = base / "collision.zip"
        with zipfile.ZipFile(collision, "w") as zf:
            zf.writestr("project/ClassicUO.sln", "a")
            zf.writestr("project/CLASSICUO.SLN", "b")
            zf.writestr("client/ClassicUO.exe", "x")
        try:
            verify_zip(collision)
        except RuntimeError as exc:
            assert "Case-insensitive" in str(exc)
            print("PASS fixture | case-insensitive collision rejected")
        else:
            raise AssertionError("case-insensitive collision was not rejected")

    print("PACKAGE_GATE_SELFTEST=PASS")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--staging-root", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--sha-sidecar", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0
    if args.staging_root is None or args.output is None:
        parser.error("--staging-root and --output are required unless --self-test is used")
    package(args.staging_root.resolve(), args.output.resolve(), args.report, args.sha_sidecar)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
