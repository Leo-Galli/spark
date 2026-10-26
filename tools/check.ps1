param(
  [Parameter(Mandatory = $true)][string]$Exercise
)
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$ex = Join-Path $root $Exercise
if (-not (Test-Path $ex)) { throw "Exercise not found: $Exercise" }
$tests = Join-Path $ex "tests"
if (-not (Test-Path $tests)) { throw "No tests/ in $Exercise" }
Push-Location $ex
try {
  Get-ChildItem -Path $tests -Filter *.mjs | ForEach-Object {
    node --test $_.FullName
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
  }
} finally {
  Pop-Location
}
