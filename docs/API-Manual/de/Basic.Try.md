# Try / Catch / Finally / Throw

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Try behandelt Laufzeitfehler aus seinem Rumpf und aufgerufenen Hilfsfunktionen. Catch übernimmt den Fehler, Finally führt Abschlussarbeiten aus, Throw löst einen Fehler aus oder wirft ihn erneut. Ein API-Ergebnis 0 oder false ist kein Ausnahmefehler und muss ausdrücklich geprüft werden.

## Genaue Syntax

```text
Try
    statements
Catch
    handlerStatements
Finally
    cleanupStatements
End Try
Catch name
Catch name As Exception
Catch name As String
Throw stringExpression
Throw
```

## Parameter

- `Try / statements` — Try benötigt einen Catch-Block, einen Finally-Block oder beide vor End Try. Verschachtelung ist erlaubt. Bei erfolgreichem Rumpf wird Catch übersprungen. Mehrere Catch-Blöcke, When-Filter und Exit Try werden in dieser Teilmenge nicht unterstützt.
- `Catch / name / As type` — Die Catch-Variable ist optional. name erhält den Fehlertext als String. As String beschreibt diese Darstellung; As Exception ist eine Kompatibilitätsschreibweise, kein .NET-Objekt und kein Typfilter. Andere Typen werden abgelehnt. Ein neuer Name wird zur Prozedurlokalen und verdeckt ein gleichnamiges Global. Eine vorhandene lokale Variable wird unter Beachtung von Typ/Const zugewiesen. Soll sie ohne ausgeführten Catch existieren, zuvor als String deklarieren.
- `Finally / End Try` — Finally ist bei vorhandenem Catch optional und darf leer sein. Normaler Abschluss, Fehler, Return, Exit Sub/Function und Schleifen-/GoTo-Sprünge nach außen führen die betroffenen Finally-Blöcke aus. End Try ist erforderlich. Skriptabbruch umgeht absichtlich Catch und Skript-Finally, damit der Notstopp nicht verzögert werden kann.
- `Throw stringExpression` — Throw stringExpression wertet die Nachricht einmal aus und erzeugt einen neuen Skriptfehler. Erforderlich ist String; andere Werte ausdrücklich mit CStr umwandeln. Dies ist eine Basic-Form, nicht Throw New Exception(...) aus VB.NET. Ohne Handler scheitert der aktuelle Skriptlauf, nicht jeder andere Lauf.
- `Throw` — Throw ohne Nachricht ist nur innerhalb von Catch samt verschachtelten Blöcken erlaubt. Es wirft den aktiven Fehler mit ursprünglichem Text, Dateinamen und Zeile erneut. Eine von Catch aufgerufene Hilfsfunktion benötigt dafür einen eigenen Catch.

## Rückgabewert

Try/Catch/Finally und Throw liefern keine ID, Zahl oder Boolean. Catch stellt Nachrichtentext in name bereit; Throw überträgt die Kontrolle statt einen Wert zu liefern. Die Beispiele geben ausdrücklich zwei Strings und Integer 13 aus Main zurück. Aufgerufene APIs behalten ihren eigenen Rückgabevertrag.

## Verhalten

- Die Vorbereitung prüft Blöcke und verbietet GoTo/On Error GoTo in Try, Catch oder Finally. Der Generator speichert Handler- und Abschlussadressen. Jeder Aufruf besitzt eigene aktive Handler. Fehler erreichen den nächsten geeigneten Catch; Fehler im Catch laufen über dessen Finally nach außen. Ohne strukturierten Handler können normale On-Error-Regeln gelten.
- Ausstehende Rückgabe, Fehler oder Sprünge werden während Finally gespeichert. Verschachtelte Abschlüsse laufen von innen nach außen. Ein neuer Fehler in Finally ersetzt den ausstehenden Fehler. Basic erlaubt auch Return oder auswärts gerichtete Sprünge aus Finally, welche die ausstehende Fortsetzung ersetzen; anders als VB.NET. Ein erneutes Throw erhält den ersten Fehlerort, auch aus Hilfsfunktionen.
- Pause/Stopp bleiben aktiv. Try erzeugt weder Threads noch Wiederholungsversuche oder Wartezeiten. Vorbereitete Adressen werden wiederverwendet; normale Bedingungen direkt prüfen, statt Ausnahmen dafür zu verwenden. Notstopp überspringt Skript-Abschlusscode; vom Host verwaltete Ressourcen folgen ihrer eigenen Laufzeitverwaltung.

## Beispiele

### 1. Parameter prüfen und Meldung speichern

```vb
# CheckedAmount erhält amount=-2 als Integer mit ByVal. Der negative Wert löst Throw "amount must be non-negative" aus. Catch übernimmt den String in problem und kopiert ihn nach message; As Exception erstellt kein Objekt. Finally setzt finished=1. Main liefert "amount must be non-negative:1". Nichtnegative Werte würden normal zurückkehren und Catch überspringen.
Option Explicit On
Function CheckedAmount(ByVal amount As Integer) As Integer
    If amount < 0 Then
        Throw "amount must be non-negative"
    End If
    Return amount
End Function

Sub Main()
    Dim message=""
    Dim finished=0
    Try
        CheckedAmount(-2)
    Catch problem As Exception
        message=problem
    Finally
        finished=1
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

CheckedAmount erhält amount=-2 als Integer mit ByVal. Der negative Wert löst Throw "amount must be non-negative" aus. Catch übernimmt den String in problem und kopiert ihn nach message; As Exception erstellt kein Objekt. Finally setzt finished=1. Main liefert "amount must be non-negative:1". Nichtnegative Werte würden normal zurückkehren und Catch überspringen.

### 2. Erneut nach außen werfen

```vb
# Das innere Throw erzeugt "missing item". Inneres Catch setzt trace=1; das leere Throw erhält denselben Fehler. Inneres Finally hängt 2 an, äußeres Catch kopiert outerProblem nach message und hängt 3 an, äußeres Finally hängt 4 an. Main liefert "1234:missing item". trace zeigt die Reihenfolge und ist kein Fehlercode.
Option Explicit On
Sub Main()
    Dim trace=0
    Dim message=""
    Try
        Try
            Throw "missing item"
        Catch problem
            trace=1
            Throw
        Finally
            trace=trace*10+2
        End Try
    Catch outerProblem
        message=outerProblem
        trace=trace*10+3
    Finally
        trace=trace*10+4
    End Try
    Return CStr(trace) & ":" & message
End Sub
```

**Erläuterung der Parameter und Ausführung:**

Das innere Throw erzeugt "missing item". Inneres Catch setzt trace=1; das leere Throw erhält denselben Fehler. Inneres Finally hängt 2 an, äußeres Catch kopiert outerProblem nach message und hängt 3 an, äußeres Finally hängt 4 an. Main liefert "1234:missing item". trace zeigt die Reihenfolge und ist kein Fehlercode.

### 3. Jede begonnene Iteration abschließen

```vb
# number nimmt 1, 2 und 3 an. Nur 1 wird zu total addiert: Continue For überspringt 2, Exit For beendet bei 3. Alle drei betretenen Try-Blöcke führen Finally aus, daher finished=3. Main liefert 1*10+3=13. Finally benötigt keinen Fehler; der Schleifensprung wartet auf den Abschluss der Iteration.
Option Explicit On
Sub Main()
    Dim total=0
    Dim finished=0
    For Var number=1 To 3
        Try
            If number=2 Then
                Continue For
            End If
            If number=3 Then
                Exit For
            End If
            total+=number
        Finally
            finished+=1
        End Try
    Next
    Return total*10+finished
End Sub
```

**Erläuterung der Parameter und Ausführung:**

number nimmt 1, 2 und 3 an. Nur 1 wird zu total addiert: Continue For überspringt 2, Exit For beendet bei 3. Alle drei betretenen Try-Blöcke führen Finally aus, daher finished=3. Main liefert 1*10+3=13. Finally benötigt keinen Fehler; der Schleifensprung wartet auf den Abschluss der Iteration.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: tryStatement / catchClause / finallyClause / throwStatement
Analysis/TryStructureValidator.cs: VisitTryStatement / VisitSubrutine / VisitCatchClause / VisitThrowStatement
Runtime/Instructions/Generator.cs: Generate(TryStatementContext)
Runtime/Instructions/TryInstruction.cs: TryInstruction / CatchInstruction / FinallyInstruction / EndTryInstruction
Runtime/Interpreter.cs: CallSubrutine / TryHandleStructuredError / Transfer / DeferReturn / Failure
Runtime/SemanticScope.cs: IsLocal / DefineVar / SetVar
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/try-catch-finally-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/throw-statement
-->
