#!/usr/bin/env python3
"""Maintainer only: pack solutions-src into AES-256 7z archives."""
from __future__ import annotations
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEVEN = Path(r"C:\Program Files\7-Zip\7z.exe")
if not SEVEN.exists():
    SEVEN = Path("7z")
KEYS = ROOT / ".keys"
SRC = ROOT / "solutions-src"
OUT = ROOT / "solutions"

def main() -> None:
    keys = {}
    for line in KEYS.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        part, key = line.split("=", 1)
        keys[part.strip()] = key.strip()
    OUT.mkdir(exist_ok=True)
    for part_dir in sorted(SRC.glob("part-*")):
        part = part_dir.name  # part-1
        key = keys.get(part)
        if not key:
            raise SystemExit(f"missing key for {part}")
        archive = OUT / f"{part}.7z"
        if archive.exists():
            archive.unlink()
        cmd = [str(SEVEN), "a", "-t7z", "-m0=lzma2", "-mhe=on", f"-p{key}", str(archive), str(part_dir.name)]
        subprocess.check_call(cmd, cwd=part_dir.parent)
        print("wrote", archive)

if __name__ == "__main__":
    main()
