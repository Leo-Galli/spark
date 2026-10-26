#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
EX="${1:-}"
if [[ -z "$EX" ]]; then
  echo "Usage: $0 <exercise-relative-path>" >&2
  exit 2
fi
DIR="$ROOT/$EX"
test -d "$DIR/tests"
cd "$DIR"
for t in tests/*.mjs; do
  node --test "$t"
done
