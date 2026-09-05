param(
    [Parameter(Mandatory = $true)]
    [string]$ClientDirectory,

    [Parameter(Mandatory = $false)]
    [string]$ProjectDirectory = "",

    [Parameter(Mandatory = $false)]
    [int]$MinAliveSeconds = 8
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

if ($MinAliveSeconds -lt 1 -or $MinAliveSeconds -gt 120) {
    throw "MinAliveSeconds must be in range 1..120"
}

$client = [System.IO.Path]::GetFullPath($ClientDirectory)
if (-not (Test-Path -LiteralPath $client -PathType Container)) {
    throw "Client directory does not exist: $client"
}

$required = @(
    'ClassicUO.exe',
    'cuo.dll',
    'SDL3.dll',
    'FNA3D.dll',
    'FAudio.dll',
    'libtheorafile.dll',
    'zlib.dll',
    'Scintilla.dll'
)
$missing = @($required | Where-Object { -not (Test-Path -LiteralPath (Join-Path $client $_) -PathType Leaf) })
if ($missing.Count -gt 0) {
    throw "Client smoke input is incomplete: $($missing -join ', ')"
}

# Never smoke the package staging directory in place. A first run is allowed to create
# settings/profile/log files, and those must not leak into the delivered archive.
$smokeRoot = Join-Path $env:RUNNER_TEMP ("v50-client-smoke-" + [Guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $smokeRoot -Force | Out-Null
Copy-Item -LiteralPath (Join-Path $client '*') -Destination $smokeRoot -Recurse -Force
$exe = Join-Path $smokeRoot 'ClassicUO.exe'

$processes = [System.Collections.Generic.List[System.Diagnostics.Process]]::new()

function Start-SmokeInstance([string]$label) {
    $stdout = Join-Path $smokeRoot ($label + '.stdout.log')
    $stderr = Join-Path $smokeRoot ($label + '.stderr.log')
    $p = Start-Process -FilePath $exe -WorkingDirectory $smokeRoot -PassThru `
        -RedirectStandardOutput $stdout -RedirectStandardError $stderr
    $processes.Add($p)
    Start-Sleep -Seconds 2
    $p.Refresh()
    if ($p.HasExited) {
        $out = if (Test-Path $stdout) { Get-Content -LiteralPath $stdout -Raw -ErrorAction SilentlyContinue } else { '' }
        $err = if (Test-Path $stderr) { Get-Content -LiteralPath $stderr -Raw -ErrorAction SilentlyContinue } else { '' }
        throw "$label exited early with code $($p.ExitCode). STDOUT=[$out] STDERR=[$err]"
    }
    Write-Host "PASS | $label remained alive after initial 2s (pid=$($p.Id))"
    return $p
}

try {
    $first = Start-SmokeInstance 'instance1'
    $second = Start-SmokeInstance 'instance2'

    $deadline = [DateTime]::UtcNow.AddSeconds($MinAliveSeconds)
    while ([DateTime]::UtcNow -lt $deadline) {
        Start-Sleep -Milliseconds 500
        foreach ($item in @($first, $second)) {
            $item.Refresh()
            if ($item.HasExited) {
                throw "ClassicUO.exe pid=$($item.Id) exited during the $MinAliveSeconds-second smoke interval with code $($item.ExitCode)"
            }
        }
    }

    Write-Host "PASS | two ClassicUO.exe instances remained alive for the required smoke interval"
    Write-Host "CLIENT_SMOKE_PASS=1"
}
finally {
    foreach ($p in $processes) {
        try {
            $p.Refresh()
            if (-not $p.HasExited) {
                Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue
                $p.WaitForExit(5000) | Out-Null
            }
        }
        catch {
            Write-Warning "Smoke cleanup could not stop pid=$($p.Id): $($_.Exception.Message)"
        }
        finally {
            $p.Dispose()
        }
    }
    if (Test-Path $smokeRoot) {
        Remove-Item -LiteralPath $smokeRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}
