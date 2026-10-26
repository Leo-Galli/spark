#!/usr/bin/env python3
"""Fail CI if book prose, secrets, or broken exercise contracts appear."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_NAMES = {
    ".keys",
    "solutions-src",
    "manuscript",
    "spark-print-latest.pdf",
    "spark-print-latest.epub",
    "spark-print-latest.docx",
}
EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F6FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FAFF"
    "\u2600-\u27BF"
    "]"
)
AI_ATTR_RE = re.compile(
    r"Co-authored-by:\s*(Claude|Codebuff|Cursor|ChatGPT|Copilot|GPT-|Anthropic)",
    re.I,
)
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+|\n+")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9\s]", " ", text.lower())).strip()


def iter_text_files(*, for_prose: bool = False):
    skip_dirs = {
        ".git",
        "node_modules",
        "unlocked",
        "__pycache__",
        "solutions",
        "solutions-src",
    }
    # Shared listings moved from the book (Phase D2) are expected duplicates.
    if for_prose:
        skip_dirs |= {"templates", "running-example", "worksheets", "project-ideas"}
    skip_names = {
        "manuscript-fingerprints.txt",
        "guard_no_book_text.py",
        "exercise-map.json",
        "commit-msg",
    }
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(part in skip_dirs for part in p.parts):
            continue
        if p.name in skip_names:
            continue
        if p.suffix.lower() in {".7z", ".png", ".jpg", ".pdf", ".woff", ".woff2", ".txt"}:
            continue
        if p.name == "_scaffold_f1.py":
            continue
        yield p

def structure_only() -> int:
    required = [
        "README.md",
        "LICENSE",
        "NOTICE.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "CODE_OF_CONDUCT.md",
        ".gitignore",
        ".gitattributes",
        ".editorconfig",
        ".github/workflows/ci.yml",
        "templates/README.md",
        "worksheets/README.md",
        "project-ideas/ideas.csv",
        "running-example/package.json",
        "tools/check.ps1",
        "tools/check.sh",
        "tools/unlock.ps1",
        "tools/unlock.sh",
        "tools/build_solutions.py",
        "tools/guard_no_book_text.py",
        "tools/exercise-map.json",
        "tools/manuscript-fingerprints.txt",
        "tools/commit-msg",
    ]
    missing = [r for r in required if not (ROOT / r).exists()]
    for n in range(1, 7):
        if not (ROOT / f"solutions/part-{n}.7z").exists():
            missing.append(f"solutions/part-{n}.7z")
    if missing:
        print("STRUCTURE FAIL:", *missing, sep="\n  ")
        return 1
    print("STRUCTURE OK")
    return 0


def tracked_forbidden() -> list[str]:
    errors = []
    try:
        r = subprocess.run(
            ["git", "ls-files"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return errors
    for line in r.stdout.splitlines():
        name = Path(line).name
        if name in {".keys"} or line.startswith("solutions-src/") or "/solutions-src/" in line:
            errors.append(f"tracked forbidden path: {line}")
        if name in FORBIDDEN_NAMES and name not in {".keys", "solutions-src"}:
            errors.append(f"tracked forbidden path: {line}")
        if line.endswith((".pdf", ".epub", ".docx")) and not line.startswith("running-example/"):
            errors.append(f"tracked book output: {line}")
    return errors


def load_fingerprints() -> set[str]:
    path = ROOT / "tools" / "manuscript-fingerprints.txt"
    if not path.exists():
        return set()
    return {ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()}


def prose_matches(fingerprints: set[str]) -> list[str]:
    if not fingerprints:
        return ["missing tools/manuscript-fingerprints.txt"]
    hits = []
    for p in iter_text_files(for_prose=True):
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for sentence in SENTENCE_SPLIT.split(text):
            n = normalize(sentence)
            words = n.split()
            if len(words) < 12:
                continue
            digest = hashlib.sha256(n.encode()).hexdigest()
            if digest in fingerprints:
                hits.append(f"manuscript sentence match in {p.relative_to(ROOT)}")
                break
    return hits


def guard() -> int:
    errors = []
    for p in ROOT.rglob("*"):
        name = p.name
        if name.endswith((".pdf", ".epub", ".docx")) and "running-example" not in p.parts:
            if p.is_file():
                errors.append(f"book output file: {p.relative_to(ROOT)}")
        if name == "manuscript" and p.is_dir():
            errors.append(f"manuscript tree present: {p.relative_to(ROOT)}")
    for p in ROOT.glob("unlocked/**/*"):
        if p.is_file():
            errors.append(f"unlocked plaintext present: {p.relative_to(ROOT)}")
    errors.extend(tracked_forbidden())
    errors.extend(prose_matches(load_fingerprints()))
    if errors:
        print("GUARD FAIL:")
        print("\n".join(errors))
        return 1
    print("GUARD OK")
    return 0


def starters_fail() -> int:
    bad = []
    for tests in ROOT.glob("part-*/**/tests/*.mjs"):
        ex = tests.parents[1]
        rel = ex.relative_to(ROOT).as_posix()
        r = subprocess.run(
            ["node", "--test", str(tests)],
            cwd=ex,
            capture_output=True,
            text=True,
        )
        if r.returncode == 0:
            bad.append(rel)
    if bad:
        print("STARTERS unexpectedly pass:")
        print("\n".join(bad))
        return 1
    print("STARTERS FAIL AS EXPECTED")
    return 0


def solutions_pass() -> int:
    src = ROOT / "solutions-src"
    if not src.exists():
        print("SOLUTIONS PASS SKIP: solutions-src missing (maintainer tree required)")
        return 1
    bad = []
    for tests in ROOT.glob("part-*/**/tests/*.mjs"):
        ex = tests.parents[1]
        # part-N-slug/chapter/ex-NN -> chapter/ex under solutions-src/part-N
        parts = ex.relative_to(ROOT).parts
        part_slug = parts[0]
        part_num = part_slug.split("-")[1]
        chapter = parts[1]
        exercise = parts[2]
        sol_starter = src / f"part-{part_num}" / chapter / exercise / "starter"
        if not sol_starter.exists():
            bad.append(f"missing solution starter: {sol_starter.relative_to(ROOT)}")
            continue
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            shutil.copytree(ex, tmp_path / "ex")
            dest_starter = tmp_path / "ex" / "starter"
            if dest_starter.exists():
                shutil.rmtree(dest_starter)
            shutil.copytree(sol_starter, dest_starter)
            test_files = sorted((tmp_path / "ex" / "tests").glob("*.mjs"))
            if not test_files:
                bad.append(f"no tests: {ex.relative_to(ROOT).as_posix()}")
                continue
            r = subprocess.run(
                ["node", "--test", *[str(t) for t in test_files]],
                cwd=tmp_path / "ex",
                capture_output=True,
                text=True,
            )
            if r.returncode != 0:
                bad.append(ex.relative_to(ROOT).as_posix())
                detail = (r.stderr or r.stdout or "").strip()
                if detail:
                    bad.append(detail[:400])
    if bad:
        print("SOLUTIONS unexpectedly fail:")
        print("\n".join(bad))
        return 1
    print("SOLUTIONS PASS")
    return 0


def seven_zip() -> Path:
    candidates = [
        Path(r"C:\Program Files\7-Zip\7z.exe"),
        Path("7z"),
        Path("/usr/bin/7z"),
    ]
    for c in candidates:
        if c.exists() or shutil.which(str(c)):
            return c
    raise FileNotFoundError("7z not found")


def load_keys() -> dict[str, str]:
    keys_path = ROOT / ".keys"
    if not keys_path.exists():
        raise FileNotFoundError(".keys missing")
    keys = {}
    for line in keys_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        part, key = line.split("=", 1)
        keys[part.strip()] = key.strip()
    return keys


def archives_unlock() -> int:
    try:
        seven = seven_zip()
        keys = load_keys()
    except FileNotFoundError as e:
        print(f"ARCHIVES FAIL: {e}")
        return 1
    errors = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        for n in range(1, 7):
            part = f"part-{n}"
            archive = ROOT / "solutions" / f"{part}.7z"
            key = keys.get(part)
            if not key:
                errors.append(f"missing key for {part}")
                continue
            if not archive.exists():
                errors.append(f"missing archive {archive.name}")
                continue
            out = tmp_path / part
            out.mkdir()
            r = subprocess.run(
                [str(seven), "x", f"-p{key}", f"-o{out}", str(archive), "-y"],
                capture_output=True,
                text=True,
            )
            if r.returncode != 0:
                errors.append(f"unlock failed for {part}: {r.stderr.strip()[:200]}")
                continue
            if not any(out.rglob("*")):
                errors.append(f"empty extract for {part}")
    if errors:
        print("ARCHIVES FAIL:")
        print("\n".join(errors))
        return 1
    print("ARCHIVES UNLOCK OK")
    return 0


def exercise_map() -> int:
    map_path = ROOT / "tools" / "exercise-map.json"
    if not map_path.exists():
        print("MAP FAIL: missing tools/exercise-map.json")
        return 1
    data = json.loads(map_path.read_text(encoding="utf-8"))
    exercises = data.get("exercises", [])
    errors = []
    seen_repo = set()
    seen_ch = set()
    disk = {
        p.parents[1].relative_to(ROOT).as_posix()
        for p in ROOT.glob("part-*/**/tests/*.mjs")
    }
    for row in exercises:
        repo_path = row.get("repo_path", "")
        chapter_file = row.get("chapter_file", "")
        if not repo_path or not chapter_file:
            errors.append(f"incomplete row: {row}")
            continue
        if repo_path in seen_repo:
            errors.append(f"duplicate repo_path: {repo_path}")
        seen_repo.add(repo_path)
        if chapter_file in seen_ch:
            errors.append(f"duplicate chapter_file: {chapter_file}")
        seen_ch.add(chapter_file)
        if repo_path not in disk:
            errors.append(f"map path missing on disk: {repo_path}")
        if not (ROOT / repo_path / "README.md").exists():
            errors.append(f"missing README: {repo_path}")
    for path in sorted(disk):
        if path not in seen_repo:
            errors.append(f"disk exercise not in map: {path}")
    if len(exercises) != 25:
        errors.append(f"expected 25 exercises, found {len(exercises)}")
    if errors:
        print("MAP FAIL:")
        print("\n".join(errors))
        return 1
    print("MAP OK (25 two-way)")
    return 0


def meta_scan() -> int:
    errors = []
    for p in iter_text_files():
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if EMOJI_RE.search(text):
            errors.append(f"emoji in {p.relative_to(ROOT)}")
        if AI_ATTR_RE.search(text):
            errors.append(f"AI attribution in {p.relative_to(ROOT)}")
    # git log must not contain AI co-author lines
    try:
        r = subprocess.run(
            ["git", "log", "--all", "--format=%B"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        if AI_ATTR_RE.search(r.stdout):
            errors.append("AI attribution in git log")
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    hook = ROOT / "tools" / "commit-msg"
    installed = ROOT / ".git" / "hooks" / "commit-msg"
    if not hook.exists():
        errors.append("missing tools/commit-msg hook source")
    elif ROOT.joinpath(".git").exists() and not installed.exists():
        errors.append("commit-msg hook not installed at .git/hooks/commit-msg")
    if errors:
        print("META FAIL:")
        print("\n".join(errors))
        return 1
    print("META OK")
    return 0


def ci_yaml() -> int:
    path = ROOT / ".github" / "workflows" / "ci.yml"
    if not path.exists():
        print("CI YAML FAIL: missing")
        return 1
    text = path.read_text(encoding="utf-8")
    required = [
        "guard_no_book_text.py --structure-only",
        "guard_no_book_text.py",
        "--starters-fail",
        "--meta-scan",
        "--exercise-map",
    ]
    missing = [r for r in required if r not in text]
    if missing:
        print("CI YAML FAIL: missing steps:", *missing, sep="\n  ")
        return 1
    try:
        import yaml  # type: ignore

        yaml.safe_load(text)
    except ImportError:
        # structural checks above are enough when PyYAML is absent
        pass
    except Exception as e:
        print(f"CI YAML FAIL: parse error: {e}")
        return 1
    print("CI YAML OK")
    return 0


def clean_status() -> int:
    try:
        r = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"STATUS FAIL: {e}")
        return 1
    if r.stdout.strip():
        print("STATUS FAIL: working tree not clean")
        print(r.stdout)
        return 1
    print("STATUS CLEAN")
    return 0


def all_gates() -> int:
    steps = [
        ("structure", structure_only),
        ("guard", guard),
        ("starters", starters_fail),
        ("solutions", solutions_pass),
        ("archives", archives_unlock),
        ("map", exercise_map),
        ("meta", meta_scan),
        ("ci-yaml", ci_yaml),
        ("status", clean_status),
    ]
    failed = []
    for name, fn in steps:
        code = fn()
        if code != 0:
            failed.append(name)
    if failed:
        print("F2 FAIL:", ", ".join(failed))
        return 1
    print("F2 ALL GATES PASS")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--structure-only", action="store_true")
    ap.add_argument("--starters-fail", action="store_true")
    ap.add_argument("--solutions-pass", action="store_true")
    ap.add_argument("--archives-unlock", action="store_true")
    ap.add_argument("--exercise-map", action="store_true")
    ap.add_argument("--meta-scan", action="store_true")
    ap.add_argument("--ci-yaml", action="store_true")
    ap.add_argument("--clean-status", action="store_true")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    if args.structure_only:
        return structure_only()
    if args.starters_fail:
        return starters_fail()
    if args.solutions_pass:
        return solutions_pass()
    if args.archives_unlock:
        return archives_unlock()
    if args.exercise_map:
        return exercise_map()
    if args.meta_scan:
        return meta_scan()
    if args.ci_yaml:
        return ci_yaml()
    if args.clean_status:
        return clean_status()
    if args.all:
        return all_gates()
    return guard()


if __name__ == "__main__":
    sys.exit(main())
