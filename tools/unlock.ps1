param(
  [Parameter(Mandatory = $true)][int]$Part,
  [Parameter(Mandatory = $true)][string]$Key
)
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$archive = Join-Path $root "solutions/part-$Part.7z"
if (-not (Test-Path $archive)) { throw "Missing $archive" }
$out = Join-Path $root "unlocked/part-$Part"
New-Item -ItemType Directory -Force -Path $out | Out-Null
$seven = "C:\Program Files\7-Zip\7z.exe"
if (-not (Test-Path $seven)) { $seven = "7z" }
& $seven x "-p$Key" "-o$out" $archive -y
if ($LASTEXITCODE -ne 0) { throw "Unlock failed" }
Write-Host "Extracted to $out"
