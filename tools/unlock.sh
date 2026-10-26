#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PART="${1:-}"
KEY="${2:-}"
if [[ -z "$PART" || -z "$KEY" ]]; then
  echo "Usage: $0 <part-number> '<four word key>'" >&2
  exit 2
fi
ARCHIVE="$ROOT/solutions/part-$PART.7z"
OUT="$ROOT/unlocked/part-$PART"
mkdir -p "$OUT"
7z x "-p${KEY}" "-o${OUT}" "$ARCHIVE" -y
echo "Extracted to $OUT"
