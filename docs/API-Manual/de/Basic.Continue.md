# Continue For / Do / While

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Continue überspringt den restlichen Rumpf der nächsten umgebenden Schleife des angegebenen Typs. Continue For gilt für For und For Each, Continue Do für Do/Loop und Repeat/Until, Continue While für While/Wend.

## Genaue Syntax

```text
Continue For
Continue Do
Continue While
```

## Parameter

- `kind` — kind: For, Do oder While ist nach Continue erforderlich, ohne Klammern. Die passende Schleife muss die Anweisung in derselben Prozedur umgeben. Eine innere Schleife anderen Typs fängt den Sprung nicht ab.

## Rückgabewert

Continue liefert keinen Wert und ist kein Ausdruck. Es bedeutet weder TRUE/FALSE noch einen Neustart der Prozedur. Die Funktion kann später RETURN ausführen; die Beispiele liefern Integer 10, 3 und 34.

## Verhalten

- For führt NEXT aus, berücksichtigt STEP und prüft den nächsten Wert gegen die Grenze; For Each liest das nächste Element. Nach dem letzten Element endet die Schleife. Initialisierung und Sammlungsausdruck werden nicht wiederholt.
- Do prüft eine Anfangsbedingung am Anfang, eine Loop-Bedingung am Ende. Repeat/Until verwendet UNTIL. Bedingungsloses Do/Loop läuft bis Exit oder Stopp. While prüft WHILE erneut. Continue Do wählt kein While/Wend.
- Die Vorbereitung bestimmt die Adresse der nächsten passenden Schleife. Fehlt sie, tritt SC020 vor Initialisierern auf, auch ohne Option Explicit. NEXT-Namen und Abschlüsse werden geprüft. Die alte FOR/NEXT-Form über eine IF-Grenze bleibt erhalten.
- Beim Verlassen von TRY/CATCH werden überquerte FINALLY-Blöcke einmal von innen nach außen ausgeführt. Liegt die gesamte Schleife in TRY, läuft dessen FINALLY nicht bei jeder Iteration. RETURN oder ein Fehler in FINALLY ersetzt den ausstehenden Sprung.
- Continue wartet nicht. Ändern Sie die Bedingung oder verwenden Sie beim Abfragen eine passende Wartefunktion, sonst droht eine Endlosschleife. Pause und Stopp bleiben aktiv. Verlassene native Enumeratoren werden freigegeben; Ausführungen bleiben unabhängig. Exit For/Do/While verlässt die Schleife.

## Beispiele

### 1. Elemente überspringen

```vb
# values enthält -2, 4, 0, 6. item<=0 löst für -2 und 0 Continue For aus; total+=item entfällt für diese Werte. Die Form gilt auch in For Each. SumPositive und Main liefern Integer 10 aus 4+6.
Option Explicit On
Function SumPositive(values)
    Var total = 0
    For Each item In values
        If item <= 0 Then
            Continue For
        End If
        total += item
    Next
    Return total
End Function
Sub Main()
    Dim values[3]
    values[0] = -2
    values[1] = 4
    values[2] = 0
    values[3] = 6
    Return SumPositive(values)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

values enthält -2, 4, 0, 6. item<=0 löst für -2 und 0 Continue For aus; total+=item entfällt für diese Werte. Die Form gilt auch in For Each. SumPositive und Main liefern Integer 10 aus 4+6.

### 2. Äußere Schleife nach Typ wählen

```vb
# AdvanceTo erhält limit=3, count beginnt mit 0. In While True steigt count und Continue Do springt zum äußeren Do. Die Bedingung wird erneut geprüft; count=3 beendet die Schleife und liefert Integer 3.
Option Explicit On
Function AdvanceTo(limit)
    Var count = 0
    Do While count < limit
        While True
            count += 1
            Continue Do
        Wend
    Loop
    Return count
End Function
Sub Main()
    Return AdvanceTo(3)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

AdvanceTo erhält limit=3, count beginnt mit 0. In While True steigt count und Continue Do springt zum äußeren Do. Die Bedingung wird erneut geprüft; count=3 beendet die Schleife und liefert Integer 3.

### 3. Aufräumen beim Überspringen

```vb
# Process erhält limit=3 und skip=2. i durchläuft 1, 2, 3. Die zweite Iteration überspringt total+=i, Finally erhöht cleanup jedoch dreimal. total=4, cleanup=3; RETURN cleanup*10+total liefert Integer 34.
Option Explicit On
Function Process(limit, skip)
    Var total = 0
    Var cleanup = 0
    For Var i = 1 To limit
        Try
            If i = skip Then
                Continue For
            End If
            total += i
        Finally
            cleanup += 1
        End Try
    Next i
    Return cleanup * 10 + total
End Function
Sub Main()
    Return Process(3, 2)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

Process erhält limit=3 und skip=2. i durchläuft 1, 2, 3. Die zweite Iteration überspringt total+=i, Finally erhöht cleanup jedoch dreimal. total=4, cleanup=3; RETURN cleanup*10+total liefert Integer 34.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: continueLoop / doLoop
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: AddTransfer / EndBreakScope
Runtime/Interpreter.cs: Transfer / DeferReturn / TryHandleStructuredError
Runtime/ForScope.cs: HasNext / AdvanceEach
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/continue-statement
-->
