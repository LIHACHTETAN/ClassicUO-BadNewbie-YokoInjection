param(
    [Parameter(Mandatory = $true)]
    [string]$Project
)

$ErrorActionPreference = 'Stop'

function Replace-ExactText {
    param(
        [Parameter(Mandatory = $true)][string]$Text,
        [Parameter(Mandatory = $true)][string]$Old,
        [Parameter(Mandatory = $true)][string]$New,
        [Parameter(Mandatory = $true)][string]$Label,
        [int]$Expected = 1
    )

    $count = ([regex]::Matches($Text, [regex]::Escape($Old))).Count
    if ($count -ne $Expected) {
        throw "$Label: expected $Expected source site(s), found $count"
    }
    return $Text.Replace($Old, $New)
}

# C# compatibility fixes discovered by the full Windows compiler.
$api = Join-Path $Project 'external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs'
$text = Get-Content $api -Raw
$oldNamed = 'FindJournalPatternId(bridge.GetJournalText(foundedTextIndex), pattern, equals: false, ignoreCase)'
$newNamed = 'FindJournalPatternId(bridge.GetJournalText(foundedTextIndex), pattern, false, ignoreCase)'
$text = Replace-ExactText $text $oldNamed $newNamed 'InjectionApiUO non-trailing named arguments' 2
$oldSplit = ".Split('|', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);"
$newSplit = ".Split(new[] { '|' }, StringSplitOptions.RemoveEmptyEntries)`r`n                .Select(pattern => pattern.Trim())`r`n                .Where(pattern => pattern.Length > 0)`r`n                .ToArray();"
$text = Replace-ExactText $text $oldSplit $newSplit 'InjectionApiUO TrimEntries compatibility'

# Dead(id) must use the bridge's real dead-state route instead of inferring death from HP.
$oldDeadState = '                return serial == bridge.Self ? bridge.Dead() : bridge.GetHP(serial) <= 0 ? 1 : 0;'
$newDeadState = '                return serial == bridge.Self ? bridge.Dead() : bridge.IsDead(serial);'
$text = Replace-ExactText $text $oldDeadState $newDeadState 'InjectionApiUO IsDeadState'
$oldDeadCall = '            return serial > 0 && bridge.GetHP(serial) <= 0 ? 1 : 0;'
$newDeadCall = '            return serial > 0 ? bridge.IsDead(serial) : 0;'
$text = Replace-ExactText $text $oldDeadCall $newDeadCall 'InjectionApiUO Dead(id)'
Set-Content $api -Value $text -Encoding utf8
Write-Host 'InjectionApiUO compiler/dead-state patch: PASS'

# Keep IsSupported() and GetKind() consistent for delegate-backed dynamic arguments.
$iv = Join-Path $Project 'external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs'
$ivText = Get-Content $iv -Raw
$oldKind = '            if (type.Equals(typeof(string)))'
$newKind = "            if (type.Equals(typeof(InjectionValue)))`r`n                return InjectionValueKind.Any;`r`n            else if (type.Equals(typeof(string)))"
$ivText = Replace-ExactText $ivText $oldKind $newKind 'InjectionValue Any mapping'
$oldArray = '            else if (typeof(Array).IsAssignableFrom(type))'
$newArray = '            else if (typeof(Array).IsAssignableFrom(type) || typeof(IEnumerable<InjectionValue>).IsAssignableFrom(type))'
$ivText = Replace-ExactText $ivText $oldArray $newArray 'InjectionValue enumerable mapping'
Set-Content $iv -Value $ivText -Encoding utf8
Write-Host 'InjectionValue runtime kind mapping patch: PASS'

# Exact + all-Any dispatch is insufficient for signatures that mix concrete kinds and Any.
$metadata = Join-Path $Project 'external/InjectionScript/src/InjectionScript/Runtime/NativeSubrutineMetadata.cs'
$metadataText = Get-Content $metadata -Raw
$oldDispatchEnd = "            subrutineDefinition = null;`r`n            return false;"
$newDispatchEnd = @"
            // Delegate-backed registrations may mix concrete kinds with InjectionValue (Any).
            // Resolve Any as a per-position wildcard and prefer the most specific compatible route.
            InjectionValueKind[] actualKinds = argumentValues.Select(item => item.Kind).ToArray();
            NativeSubrutineDefinition wildcard = subrutines.Values
                .Where(item => item.Name.Equals(name, StringComparison.OrdinalIgnoreCase)
                    && item.ArgumentCount == actualKinds.Length
                    && item.ParameterKinds.Select((kind, index) =>
                        kind == InjectionValueKind.Any || kind == actualKinds[index]).All(match => match))
                .OrderBy(item => item.ParameterKinds.Count(kind => kind == InjectionValueKind.Any))
                .FirstOrDefault();
            if (wildcard != null)
            {
                subrutineDefinition = wildcard;
                return true;
            }

            subrutineDefinition = null;
            return false;
"@
$newDispatchEnd = $newDispatchEnd.TrimEnd("`r", "`n")
$metadataText = Replace-ExactText $metadataText $oldDispatchEnd $newDispatchEnd 'Native mixed-Any dispatch'
Set-Content $metadata -Value $metadataText -Encoding utf8
Write-Host 'Native mixed-Any dispatch patch: PASS'

# Workspace Manual data must not be polluted by authoritative runtime symbols.
$manual = Join-Path $Project 'src/ClassicUO.Client/Game/UI/Gumps/YokoManualGump.cs'
$manualText = Get-Content $manual -Raw
$oldWorkspace = "            _workspaceSymbols = symbols as YokoApiSymbol[]`r`n                ?? (symbols ?? Array.Empty<YokoApiSymbol>()).ToArray();"
$newWorkspace = "            _workspaceSymbols = (symbols ?? Array.Empty<YokoApiSymbol>())`r`n                .Where(symbol => symbol != null && !symbol.IsRuntime)`r`n                .ToArray();"
$manualText = Replace-ExactText $manualText $oldWorkspace $newWorkspace 'Yoko Manual workspace/runtime separation'
Set-Content $manual -Value $manualText -Encoding utf8
Write-Host 'Yoko Manual workspace symbol separation: PASS'

# The completion catalog is a process-wide singleton; serialize this test collection.
$symbolTests = Join-Path $Project 'tests/ClassicUO.UnitTests/Game/Managers/YokoApiSymbolIndexTests.cs'
$symbolText = Get-Content $symbolTests -Raw
$symbolText = Replace-ExactText $symbolText '[CollectionDefinition("Yoko completion catalog")]' '[CollectionDefinition("Yoko completion catalog", DisableParallelization = true)]' 'Yoko completion test isolation'
Set-Content $symbolTests -Value $symbolText -Encoding utf8
Write-Host 'Yoko completion singleton test isolation: PASS'

# Update fixtures to the current bridge contract: Dead(id) uses IsDead; UseSkill receives a skill ID.
$compatTests = Join-Path $Project 'tests/ClassicUO.UnitTests/Game/Managers/YokoInjectionCompatibilityTests.cs'
$compatText = Get-Content $compatTests -Raw
$oldProxy = "                    case nameof(IApiBridge.GetHP): return HpValue;`r`n                    case nameof(IApiBridge.Dead): return DeadValue;"
$newProxy = "                    case nameof(IApiBridge.GetHP): return HpValue;`r`n                    case nameof(IApiBridge.Dead): return DeadValue;`r`n                    case nameof(IApiBridge.IsDead):`r`n                        return arguments.Length > 0 && (int)arguments[0] == 0x00001235 ? 1 : 0;"
$compatText = Replace-ExactText $compatText $oldProxy $newProxy 'RecordingBridge IsDead fixture'
$oldSkill = "            Assert.Contains(proxy.Calls, c => c.Name == nameof(IApiBridge.UseSkill)`r`n                && string.Equals((string)c.Arguments[0], \"Tracking\", StringComparison.OrdinalIgnoreCase));"
$newSkill = "            Assert.Contains(proxy.Calls, c => c.Name == nameof(IApiBridge.UseSkill)`r`n                && c.Arguments[0] is int skillId && skillId == 39);"
$compatText = Replace-ExactText $compatText $oldSkill $newSkill 'WaitingForMenu UseSkill fixture'
Set-Content $compatTests -Value $compatText -Encoding utf8
Write-Host 'Injection compatibility fixture patch: PASS'

# The solution maps InjectionScript to its Debug netstandard2.0 output even in the outer Release build.
$generatorProject = Join-Path $Project 'tools/YokoExampleGenerator/YokoExampleGenerator.csproj'
$generatorText = Get-Content $generatorProject -Raw
$generatorText = Replace-ExactText $generatorText 'bin\Release\netstandard2.0\InjectionScript.dll' 'bin\Debug\netstandard2.0\InjectionScript.dll' 'Yoko example generator InjectionScript reference'
Set-Content $generatorProject -Value $generatorText -Encoding utf8

# Regenerate engine examples from the just-built runtime before the full unit-test gate.
$buildScript = Join-Path $Project 'BUILD_V50_WINDOWS.ps1'
$buildText = Get-Content $buildScript -Raw
$unitAnchor = '    Invoke-Checked "ClassicUO unit tests" {'
$generatorBlock = @"
    Invoke-Checked "Restore Yoko example generator" {
        dotnet restore tools\YokoExampleGenerator\YokoExampleGenerator.csproj --ignore-failed-sources @restorePackageArgs
    }
    Invoke-Checked "Regenerate Yoko engine examples from current runtime" {
        dotnet run --project tools\YokoExampleGenerator\YokoExampleGenerator.csproj -c Release --no-restore -- ``
            src\ClassicUO.Client\YokoDocumentation\Examples ``
            src\ClassicUO.Client\YokoDocumentation\Manual\injection-manual-catalog.json ``
            src\ClassicUO.Client\YokoDocumentation\Manual\stealth-uo-api-catalog.json
    }

$unitAnchor
"@
$generatorBlock = $generatorBlock.TrimEnd("`r", "`n")
$buildText = Replace-ExactText $buildText $unitAnchor $generatorBlock 'Yoko example regeneration build gate'
Set-Content $buildScript -Value $buildText -Encoding utf8
Write-Host 'Current-runtime Yoko example regeneration gate: PASS'

# Remove the duplicate active AutoLoad alias without losing it: nested folders are intentionally not auto-scanned.
$marker = @'
# v50 compatibility marker
# Canonical active AutoLoad: autoload.sc
# Full historical alias preserved in Archive/Autoload_YokoClassicUO.sc
'@
foreach ($relativeDir in @('Autoload', 'src/ClassicUO.Client/Autoload')) {
    $directory = Join-Path $Project $relativeDir
    $canonical = Join-Path $directory 'autoload.sc'
    $alias = Join-Path $directory 'Autoload_YokoClassicUO.sc'
    if (-not (Test-Path $canonical) -or -not (Test-Path $alias)) {
        throw "Missing AutoLoad source in $relativeDir"
    }
    $canonicalHash = (Get-FileHash $canonical -Algorithm SHA256).Hash
    $aliasHash = (Get-FileHash $alias -Algorithm SHA256).Hash
    if ($canonicalHash -ne $aliasHash) {
        throw "Expected duplicate active AutoLoad sources in $relativeDir, but hashes differ"
    }
    $archive = Join-Path $directory 'Archive'
    New-Item -ItemType Directory -Path $archive -Force | Out-Null
    Copy-Item $alias (Join-Path $archive 'Autoload_YokoClassicUO.sc') -Force
    Set-Content $alias -Value $marker -Encoding utf8
}
Write-Host 'Duplicate active AutoLoad cleanup/archive: PASS'

# Patch assertions: fail before compilation if any intended invariant is absent.
$apiCheck = Get-Content $api -Raw
if ($apiCheck.Contains($oldNamed) -or $apiCheck.Contains('StringSplitOptions.TrimEntries')) { throw 'Compiler compatibility patch verification failed' }
if (([regex]::Matches($apiCheck, [regex]::Escape('bridge.IsDead(serial)'))).Count -lt 2) { throw 'Dead-state patch verification failed' }
$ivCheck = Get-Content $iv -Raw
if (-not $ivCheck.Contains('return InjectionValueKind.Any;') -or -not $ivCheck.Contains('typeof(IEnumerable<InjectionValue>).IsAssignableFrom(type)')) { throw 'InjectionValue patch verification failed' }
$metadataCheck = Get-Content $metadata -Raw
if (-not $metadataCheck.Contains('per-position wildcard')) { throw 'Mixed-Any dispatch patch verification failed' }
$manualCheck = Get-Content $manual -Raw
if (-not $manualCheck.Contains('!symbol.IsRuntime')) { throw 'Workspace symbol patch verification failed' }
$symbolCheck = Get-Content $symbolTests -Raw
if (-not $symbolCheck.Contains('DisableParallelization = true')) { throw 'Completion test isolation patch verification failed' }
$compatCheck = Get-Content $compatTests -Raw
if (-not $compatCheck.Contains('case nameof(IApiBridge.IsDead)') -or -not $compatCheck.Contains('skillId == 39')) { throw 'Compatibility fixture patch verification failed' }
$buildCheck = Get-Content $buildScript -Raw
if (-not $buildCheck.Contains('Regenerate Yoko engine examples from current runtime')) { throw 'Example regeneration gate verification failed' }
foreach ($relativeDir in @('Autoload', 'src/ClassicUO.Client/Autoload')) {
    $directory = Join-Path $Project $relativeDir
    if ((Get-Item (Join-Path $directory 'Autoload_YokoClassicUO.sc')).Length -gt 1024) { throw "Duplicate active AutoLoad alias remains in $relativeDir" }
    if ((Get-Item (Join-Path $directory 'Archive/Autoload_YokoClassicUO.sc')).Length -lt 60000) { throw "Archived AutoLoad alias is incomplete in $relativeDir" }
}

Write-Host 'v50 Release 8 source patch verification: PASS'
