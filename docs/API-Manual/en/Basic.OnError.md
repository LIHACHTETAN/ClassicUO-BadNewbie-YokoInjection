# On Error / Resume

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

On Error selects how subsequent runtime errors are handled in the current procedure or function. It is a language statement, not a callable API. For structured recovery and cleanup, use Try/Catch/Finally.

## Exact syntax

```text
On Error GoTo label
On Error Resume Next
On Error GoTo 0
label:
Resume
Resume Next
```

## Parameters

- `label` — An existing label in the same procedure, written as label: on its own line. It may precede or follow On Error; matching ignores case. It is not a function name, quoted text or a source line number. An unknown label produces diagnostic SC009; the client blocks that script.
- `Resume Next / On Error` — On Error Resume Next selects automatic continuation after a failing instruction, without jumping to a label. Normal successful instructions are unaffected. Scope is the current procedure call, not all running scripts.
- `0` — On Error GoTo 0 disables the selected mode. Zero is this special control value, not a label and not a Boolean result. Other numeric labels and GoTo -1 are not supported forms.
- `Resume / Resume Next` — Inside a handler, Resume retries the failed instruction; Resume Next continues after it. They require a recorded runtime failure and clear that recorded address when used. Neither takes a label or timeout in this engine.

## Returns

On Error and Resume do not return a value. A handled failure does not become TRUE/FALSE or repair the failed assignment automatically. The examples explicitly return Integer 5, 18 and 10. There is no implicit rollback of earlier side effects.

## Behavior

- Preparation resolves labels within each procedure after reading its complete body, so both label directions work. Execution stores the selected mode; when an instruction throws, structured Try handling is considered first, then On Error.
- The engine records the failed instruction address. Label mode jumps to the handler; automatic Resume Next advances past that instruction. Resume re-evaluates the failed instruction, including expressions and calls: fix the cause first and consider repeated side effects.
- On Error GoTo 0 does not erase the pending failed address; a handler can disable itself before repairing data and then Resume. Disable before fallible handler work to prevent re-entry into the same handler.
- Parse errors and cancellation are not recovered by this statement. A command returning 0, FALSE or another failure status without throwing does not invoke it: inspect that command’s result.
- Use Return or a deliberate GoTo to keep normal flow out of handler labels. A callee gets its own handler state. An unhandled callee error can reach the caller, where retrying repeats the call instruction, not an inner callee line. There is no automatic retry limit or delay.
- If an error leaves a Try block after cleanup and reaches an external On Error GoTo handler, Resume retries the whole Try from its header. Resume Next continues with the first statement after End Try. On Error Resume Next has the same continuation. Completed actions may repeat when retrying; it does not jump back into an unwound body.

## Examples

### 1. Skip one failed assignment

```vb
# values[0] allocates one cell; index 5 is invalid. result starts at 1. On Error Resume Next skips the failed read before assignment, so result stays 1. GoTo 0 disables handling, then result+=4 gives 5. Main returns 5; this does not declare the failed read successful.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 1
    On Error Resume Next
    result = values[5]
    On Error GoTo 0
    result += 4
    Return result
End Sub
```

**Parameter and execution notes:**

values[0] allocates one cell; index 5 is invalid. result starts at 1. On Error Resume Next skips the failed read before assignment, so result stays 1. GoTo 0 disables handling, then result+=4 gives 5. Main returns 5; this does not declare the failed read successful.

### 2. Repair and retry

```vb
# ReadCell stores 8 in cell 0 but starts index=2. The invalid read jumps to FixIndex. GoTo 0 disables further handling; handled becomes 1 and index becomes 0. Resume repeats result=values[index], now storing 8. Return prevents falling through to the handler. Main receives 1*10+8=18.
Option Explicit On
Function ReadCell()
    Dim values[0]
    values[0] = 8
    Var index = 2
    Var handled = 0
    Var result = 0
    On Error GoTo FixIndex
    result = values[index]
    Return handled * 10 + result
FixIndex:
    On Error GoTo 0
    handled += 1
    index = 0
    Resume
End Function
Sub Main()
    Return ReadCell()
End Sub
```

**Parameter and execution notes:**

ReadCell stores 8 in cell 0 but starts index=2. The invalid read jumps to FixIndex. GoTo 0 disables further handling; handled becomes 1 and index becomes 0. Resume repeats result=values[index], now storing 8. Return prevents falling through to the handler. Main receives 1*10+8=18.

### 3. Handler above its registration

```vb
# The initial GoTo Work skips Failed during normal entry. On Error GoTo Failed then installs that earlier label. Reading index 2 fails before result changes. The handler disables itself, increments handled and uses Resume Next to reach Return. Main returns 1*10+0=10. Labels are not separate procedures.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 0
    Var handled = 0
    GoTo Work
Failed:
    On Error GoTo 0
    handled += 1
    Resume Next
Work:
    On Error GoTo Failed
    result = values[2]
    Return handled * 10 + result
End Sub
```

**Parameter and execution notes:**

The initial GoTo Work skips Failed during normal entry. On Error GoTo Failed then installs that earlier label. Reading index 2 fails before result changes. The handler disables itself, increments handled and uses Resume Next to reach Return. Main returns 1*10+0=10. Labels are not separate procedures.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: onError / resume / label
Analysis/InvalidSymbolVisitor.cs: VisitOnError / ValidateLabelReference
Runtime/Instructions/Generator.cs: VisitSubrutine / errorHandlers
Runtime/Instructions/ErrorHandlingInstruction.cs
Runtime/Interpreter.cs: TryHandleStructuredError / TryHandleError / ResumeInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/on-error-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/resume-statement
-->
