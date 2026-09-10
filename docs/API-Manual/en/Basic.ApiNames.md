# Basic / UO.

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

Game commands use UO.; Basic constructs, built-in functions and your own functions use their declared names.

## Exact syntax

```text
UO.command(arguments)
BasicFunction(arguments)
UserFunction(arguments)
```

## Parameters

- `UO.command` — UO.command(arguments): required prefix for a game API call. UO.GetType(id) reads a graphic/body, not a Basic or CLR type.
- `BasicFunction` — BasicFunction(arguments): for example Int(value), Str(value), CInt(value). Do not add UO. to a Basic function.
- `arguments` — Object/filter/layer arguments such as self, backpack, ground and Rhand keep their meaning. A name passed as an argument is not a callable game alias.

## Returns

Naming itself returns nothing. Each called function defines its own result: Int returns an Integer, Str a String; the three Api*Exists checks return Integer 1/0, usable as TRUE/FALSE.

## Behavior

- Names are case-insensitive. InjectionApi registers the bare Basic library; InjectionApiUO registers game calls with UO. The analyzer reports SC005 for a removed short call and suggests a registered UO. replacement. No fallback executes that old call. Character getter values also require UO. ApiNameExists, ApiSignatureExists and ApiParameterExists trim surrounding spaces and check the exact registered name without adding a prefix. They inspect metadata, not server state. The engine does not implement the VB.NET reflection operator GetType(TypeName).

## Examples

### 1. 1

```vb
# graphic reads the current character body (0 if unavailable); whole=Int(2.9) is 2. registered checks the one-argument UO.GetType signature. Main returns "2:1" independently of the character graphic. No movement or item transfer occurs.
Option Explicit On
Sub Main()
    Var graphic = UO.GetType('self')
    Var whole = Int(2.9)
    Var registered = UO.ApiSignatureExists('UO.GetType', 1)
    Return CStr(whole) + ":" + CStr(registered)
End Sub
```

**Parameter and execution notes:**

graphic reads the current character body (0 if unavailable); whole=Int(2.9) is 2. registered checks the one-argument UO.GetType signature. Main returns "2:1" independently of the character graphic. No movement or item transfer occurs.

### 2. 2

```vb
# The fully defined user Function GetType receives value=6 from CInt(6) and returns 7. UO.GetType still reads the game graphic. The bare user function and qualified game command do not intercept each other.
Option Explicit On
Function GetType(value)
    Return value + 1
End Function
Sub Main()
    Var localResult = GetType(CInt(6))
    Var graphic = UO.GetType('self')
    Return localResult
End Sub
```

**Parameter and execution notes:**

The fully defined user Function GetType receives value=6 from CInt(6) and returns 7. UO.GetType still reads the game graphic. The bare user function and qualified game command do not intercept each other.

### 3. 3

```vb
# oldCall=0 because GetType is not a registered native call. gameCall=1 and basicCall=1 verify UO.GetType(id) and Int(value). argumentName=1 shows backpack remains an argument selector. Main returns "0:1:1:1". These checks do not search for user procedures.
Option Explicit On
Sub Main()
    Var oldCall = UO.ApiSignatureExists('GetType', 1)
    Var gameCall = UO.ApiSignatureExists('UO.GetType', 1)
    Var basicCall = UO.ApiSignatureExists('Int', 1)
    Var argumentName = UO.ApiParameterExists('backpack')
    Return CStr(oldCall) + ":" + CStr(gameCall) + ":" + CStr(basicCall) + ":" + CStr(argumentName)
End Sub
```

**Parameter and execution notes:**

oldCall=0 because GetType is not a registered native call. gameCall=1 and basicCall=1 verify UO.GetType(id) and Int(value). argumentName=1 shows backpack remains an argument selector. Main returns "0:1:1:1". These checks do not search for user procedures.

<!-- implementation references (not callable script procedures):
Runtime/InjectionApi.cs: Register
Runtime/InjectionApiUO.cs: Register / RegisterCharacterGetterAliases / ApiNameExists / ApiSignatureExists / ApiParameterExists
Analysis/InvalidSymbolVisitor.cs: VisitCall
Runtime/ScriptBindings.cs: Builder.CallName
-->
