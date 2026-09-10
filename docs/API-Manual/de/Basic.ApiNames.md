# Basic / UO.

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Spielbefehle verwenden UO.; Basic und eigene Funktionen verwenden ihre deklarierten Namen.

## Genaue Syntax

```text
UO.command(arguments)
BasicFunction(arguments)
UserFunction(arguments)
```

## Parameter

- `UO.command` — UO.command(arguments): erforderliches Spielpräfix. UO.GetType(id) liest Grafik/Körper, keinen Basic- oder CLR-Typ.
- `BasicFunction` — BasicFunction(arguments): etwa Int(value), Str(value), CInt(value), ohne UO.
- `arguments` — self, backpack, ground und Rhand behalten ihre Bedeutung als Objekt-, Filter- oder Layerargumente; sie sind keine verkürzten Aufrufe.

## Rückgabewert

Die Namensregel liefert keinen Wert. Int liefert Integer, Str String; die drei Api*Exists liefern Integer 1/0 und erlauben TRUE/FALSE.

## Verhalten

- Groß-/Kleinschreibung ist egal. InjectionApi registriert Basic ohne Präfix, InjectionApiUO das Spiel mit UO. Alte Kurzaufrufe erzeugen SC005 mit UO.-Vorschlag; kein stiller Ersatz wird ausgeführt. Attributwerte benötigen ebenfalls UO. ApiNameExists, ApiSignatureExists und ApiParameterExists entfernen äußere Leerzeichen und prüfen den exakten registrierten Namen ohne Präfixergänzung. Sie lesen Metadaten, keinen Serverzustand. Der VB.NET-Reflexionsoperator GetType(TypeName) fehlt.

## Beispiele

### 1. 1

```vb
# graphic liest den Körper oder 0 ohne Daten; whole=2. registered prüft UO.GetType mit einem Argument. Main liefert unabhängig von der Grafik "2:1", ohne Bewegung oder Transfer.
Option Explicit On
Sub Main()
    Var graphic = UO.GetType('self')
    Var whole = Int(2.9)
    Var registered = UO.ApiSignatureExists('UO.GetType', 1)
    Return CStr(whole) + ":" + CStr(registered)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

graphic liest den Körper oder 0 ohne Daten; whole=2. registered prüft UO.GetType mit einem Argument. Main liefert unabhängig von der Grafik "2:1", ohne Bewegung oder Transfer.

### 2. 2

```vb
# Die vollständig gezeigte Function GetType erhält value=6 aus CInt(6) und liefert 7. UO.GetType liest weiter die Spielgrafik. Beide Namen bleiben getrennt.
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

**Erläuterung der Parameter und Ausführung:**

Die vollständig gezeigte Function GetType erhält value=6 aus CInt(6) und liefert 7. UO.GetType liest weiter die Spielgrafik. Beide Namen bleiben getrennt.

### 3. 3

```vb
# oldCall=0, gameCall=1 und basicCall=1 prüfen GetType, UO.GetType(id) und Int(value). argumentName=1 bestätigt backpack als Argumentselektor. Main liefert "0:1:1:1". Eigene Prozeduren werden dabei nicht gesucht.
Option Explicit On
Sub Main()
    Var oldCall = UO.ApiSignatureExists('GetType', 1)
    Var gameCall = UO.ApiSignatureExists('UO.GetType', 1)
    Var basicCall = UO.ApiSignatureExists('Int', 1)
    Var argumentName = UO.ApiParameterExists('backpack')
    Return CStr(oldCall) + ":" + CStr(gameCall) + ":" + CStr(basicCall) + ":" + CStr(argumentName)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

oldCall=0, gameCall=1 und basicCall=1 prüfen GetType, UO.GetType(id) und Int(value). argumentName=1 bestätigt backpack als Argumentselektor. Main liefert "0:1:1:1". Eigene Prozeduren werden dabei nicht gesucht.

<!-- implementation references (not callable script procedures):
Runtime/InjectionApi.cs: Register
Runtime/InjectionApiUO.cs: Register / RegisterCharacterGetterAliases / ApiNameExists / ApiSignatureExists / ApiParameterExists
Analysis/InvalidSymbolVisitor.cs: VisitCall
Runtime/ScriptBindings.cs: Builder.CallName
-->
