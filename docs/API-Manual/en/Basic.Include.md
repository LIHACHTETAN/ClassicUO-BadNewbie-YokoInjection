# Include

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Include loads another source file before parsing and execution. Its shared functions and variables become available to the main script; it does not automatically start a procedure or thread.

## Exact syntax

```text
Include "fileName"
```

## Parameters

- `fileName` — fileName: a nonempty single- or double-quoted file name. Relative and absolute paths are accepted. This is a literal path, not a variable or expression. Any extension is allowed; the content must be source text supported by this engine.

## Returns

No return value: Include is a source preparation directive. Do not assign Include(...), or expect an ID, TRUE/FALSE or 1/0 from it. Included functions return their own values through RETURN.

## Behavior

- Write Include on its own line outside SUB/FUNCTION. Search order: beside the including file, then its Include subfolder. Nested paths are relative to the current library, not the main script. Save the main file before using relative paths.
- Each full path is included once per preparation. A cycle A → B → A produces SC016. Path, access and syntax errors prevent execution before global initialization. Diagnostics and debugger locations retain the original file and line.
- Close string literals and SUB/FUNCTION in the same file that opens them. Redeclaring a global variable or constant produces SC017 before execution.
- The next launch reads changed library content; an already prepared or running script keeps its code snapshot. Shared source does not copy profile settings or launch other scripts.
- Each file may set Option Explicit before its own declarations; absent that directive it inherits the main file setting. Declarations share the same namespace; equal function names do not create a module automatically.
- Files use UTF-8 with BOM recognition. Limits per preparation: 128 files including the main file, 32 nesting levels, 16,777,216 source characters. Include text inside comments or strings does not load files.
- Each example below has its own folder. Save Main.bas and every displayed file using the exact names and subfolders. Ready-to-run sets are in API Manual/Examples/Basic.Include/1, /2 and /3. Run Main.bas rather than concatenating all the files.

## Examples

### 1. Shared function

```vb
# Main.bas includes Common.bas and calls Add(4, 7). left and right are passed by value; Add returns their sum and Main returns Integer 11. Common.bas does not start by itself.
Option Explicit On
Include "Common.bas"
SUB Main()
    RETURN Add(4, 7)
END SUB
```

**Parameter and execution notes:**

Main.bas includes Common.bas and calls Add(4, 7). left and right are passed by value; Add returns their sum and Main returns Integer 11. Common.bas does not start by itself.

**Common.bas**

```vbnet
Option Explicit On
FUNCTION Add(ByVal left, ByVal right)
    RETURN left + right
END FUNCTION
```

### 2. Nested library

```vb
# Main.bas includes lib/Route.bas, which includes Math.bas from its own lib folder. Distance(-3, 5) passes dx=-3 and dy=5 to Manhattan; Abs removes the signs and the sum is Integer 8. This arithmetic example does not move the character.
Option Explicit On
Include "lib/Route.bas"
SUB Main()
    RETURN Distance(-3, 5)
END SUB
```

**Parameter and execution notes:**

Main.bas includes lib/Route.bas, which includes Math.bas from its own lib folder. Distance(-3, 5) passes dx=-3 and dy=5 to Manhattan; Abs removes the signs and the sum is Integer 8. This arithmetic example does not move the character.

**lib/Route.bas**

```vbnet
Option Explicit On
Include "Math.bas"
FUNCTION Distance(ByVal dx, ByVal dy)
    RETURN Manhattan(dx, dy)
END FUNCTION
```

**lib/Math.bas**

```vbnet
Option Explicit On
FUNCTION Manhattan(ByVal dx, ByVal dy)
    RETURN Abs(dx) + Abs(dy)
END FUNCTION
```

### 3. Repeated inclusion

```vb
# Common.bas and ./Common.bas identify one file, so its CONST and function are declared once. SharedValue=7; GetShared() returns 7 and Main multiplies it by 2, returning Integer 14. Both files use Option Explicit On.
Option Explicit On
Include "Common.bas"
Include "./Common.bas"
SUB Main()
    RETURN GetShared() * 2
END SUB
```

**Parameter and execution notes:**

Common.bas and ./Common.bas identify one file, so its CONST and function are declared once. SharedValue=7; GetShared() returns 7 and Main multiplies it by 2, returning Integer 14. Both files use Option Explicit On.

**Common.bas**

```vbnet
Option Explicit On
CONST SharedValue = 7
FUNCTION GetShared()
    RETURN SharedValue
END FUNCTION
```

<!-- implementation references (not callable script procedures):
Parsing/ScriptSourceGraph.cs: Load / Builder.AddInclude / ResolveLine
Runtime/InjectionRuntime.cs: Prepare / Load
Runtime/Interpreter.cs: Location / EvaluateInitializer / CallObserved
Analysis/SanityAnalyzer.cs: Analyze
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: PrepareScriptForExecution
InjectionScript.Lsp/Workspace.cs: UpdateDiagnostic
-->
