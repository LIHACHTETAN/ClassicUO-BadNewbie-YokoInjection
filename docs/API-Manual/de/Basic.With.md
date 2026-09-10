# With / End With

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

With fasst Operationen an einem gespeicherten Objekt zusammen. Ein führender Punkt bezeichnet dessen Mitglied. With UO und With moduleName sind zusätzliche Basic-Formen für ausdrücklich gewählte Namensräume.

## Genaue Syntax

```text
With objectExpression
    .Method(arguments)
    statements
End With
With UO
    .Command(arguments)
End With
With moduleName
    .field = expression
    .Procedure(arguments)
End With
```

## Parameter

- `objectExpression / UO / moduleName` — Erforderlicher Empfänger: ein natives Objekt wie List() oder Dictionary(), eine Objektvariable oder eine Funktion, die ein Objekt liefert. Der Ausdruck wird beim Eintritt genau einmal ausgewertet, auch bei leerem Rumpf. Zahlen, Zeichenfolgen, Arrays und Unit sind hier keine Objektempfänger. Eine lokale Objektvariable hat Vorrang vor einem gleichnamigen Modul.
- `.Method(arguments) / .field` — Objektmethoden benötigen Klammern: .Add(value), .Item(index), .Count(). Parameter und Ergebnisse bleiben unverändert; siehe Basic.List/Basic.Dictionary. Beliebige Objektfelder und Eigenschaften werden hier nicht unterstützt. Bei Modulen sind zugängliche .field und .Procedure(arguments) erlaubt; Private gilt weiterhin. In With UO bedeutet .Command(...) ausdrücklich UO.Command(...). Außerhalb bleiben Spielbefehle mit UO qualifiziert.
- `statements / End With` — Der Rumpf darf leer sein oder Aufrufe, Zuweisungen, Bedingungen und korrekt verschachtelte Blöcke enthalten. End With ist erforderlich. Ein führender Punkt außerhalb des Rumpfs ist ungültig. Andere Objekte bleiben über vollständige Namen erreichbar.

## Rückgabewert

With ist ein Steuerblock ohne eigenen Rückgabewert, keine ID und kein Erfolgs-Boolean. Aufgerufene Methoden behalten ihren Rückgabetyp. Return in den Beispielen liefert ausdrücklich Integer aus Main; 127, 28 und 72 sind Beispielberechnungen.

## Verhalten

- Die Vorbereitung prüft den Block und bindet relative Namen. Beim Eintritt speichert der Interpreter die einmal ausgewertete Objektreferenz im aktuellen Aufruf. Eine spätere Neuzuweisung der Variablen ändert sie nicht. Erneuter Eintritt wertet neu aus; rekursive Aufrufe besitzen getrennte Referenzen.
- Der Kopf eines inneren With wird im äußeren Kontext ausgewertet. Im inneren Rumpf bezeichnet der Punkt das innere Objekt; End With stellt den äußeren Kontext wieder her. Return, Schleifensprünge und GoTo nach außen verlassen die betroffenen Bereiche nach den zugehörigen Finally-Blöcken. Sprünge in einen With-Rumpf werden abgelehnt.
- Ein ungeeigneter Empfänger oder eine unbekannte Methode erzeugt einen Fehler statt false. Catch/On Error kann ihn behandeln. Scheitert der Empfänger, überspringt On Error Resume Next den ganzen Block. With wartet nicht, wiederholt nichts und startet keinen Thread. Pause/Stopp bleiben wirksam. Gebundene Namen werden mit dem vorbereiteten Skript zwischengespeichert; Methodenaufrufe werten den Empfänger nicht erneut aus.

## Beispiele

### 1. Einmalige Auswertung

```vb
# Choose erhält values mit ByVal und calls mit ByRef, erhöht calls auf 1 und liefert die ursprüngliche Liste. Beide .Add-Aufrufe fügen 2 und 7 in diese Liste ein, obwohl values dazwischen eine neue Liste erhält. Item verwendet die Indizes 0 und 1. Main liefert 1*100+2*10+7=127.
Option Explicit On
Function Choose(ByVal values, ByRef calls) As Object
    calls += 1
    Return values
End Function

Sub Main()
    Dim calls=0
    Dim values=List()
    Dim original=values
    With Choose(values, calls)
        .Add(2)
        values=List()
        .Add(7)
    End With
    Return calls*100+original.Item(0)*10+original.Item(1)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

Choose erhält values mit ByVal und calls mit ByRef, erhöht calls auf 1 und liefert die ursprüngliche Liste. Beide .Add-Aufrufe fügen 2 und 7 in diese Liste ein, obwohl values dazwischen eine neue Liste erhält. Item verwendet die Indizes 0 und 1. Main liefert 1*100+2*10+7=127.

### 2. Verschachtelung und Abschluss

```vb
# groups speichert child unter dem Textschlüssel "child". .Item("child") liest das Objekt aus dem äußeren Dictionary. Innen verändern .Add(2) und Finally mit .Add(7) die Liste. Nach End With wirkt .Set("result",8) wieder auf das Dictionary. Count() liefert 2, Item("result") liefert 8; Main ergibt 28.
Option Explicit On
Sub Main()
    Dim groups=Dictionary()
    Dim child=List()
    groups.Set("child", child)
    With groups
        With .Item("child")
            Try
                .Add(2)
            Finally
                .Add(7)
            End Try
        End With
        .Set("result", 8)
    End With
    Return child.Count()*10+groups.Item("result")
End Sub
```

**Erläuterung der Parameter und Ausführung:**

groups speichert child unter dem Textschlüssel "child". .Item("child") liest das Objekt aus dem äußeren Dictionary. Innen verändern .Add(2) und Finally mit .Add(7) die Liste. Nach End With wirkt .Set("result",8) wieder auf das Dictionary. Count() liefert 2, Item("result") liefert 8; Main ergibt 28.

### 3. Modul und UO

```vb
# With Tools qualifiziert .total, .AddAmount und .CountItems. total beginnt bei 4; amount=3 kommt über ByVal hinzu, also 7. CountItems erhält ein Array mit zwei Elementen und ruft über With UO die Funktion UO.GetArrayLength(values) auf: Ergebnis 2. Main liefert 7*10+2=72. Die Zugriffsregeln des Moduls gelten weiterhin.
Option Explicit On
Module Tools
    Public Var total=0
    Public Sub AddAmount(ByVal amount)
        total += amount
    End Sub
    Public Function CountItems(ByVal values) As Integer
        With UO
            Return .GetArrayLength(values)
        End With
    End Function
End Module

Sub Main()
    Dim values[1]
    With Tools
        .total=4
        .AddAmount(3)
        Return .total*10+.CountItems(values)
    End With
End Sub
```

**Erläuterung der Parameter und Ausführung:**

With Tools qualifiziert .total, .AddAmount und .CountItems. total beginnt bei 4; amount=3 kommt über ByVal hinzu, also 7. CountItems erhält ein Array mit zwei Elementen und ruft über With UO die Funktion UO.GetArrayLength(values) auf: Ergebnis 2. Main liefert 7*10+2=72. Die Zugriffsregeln des Moduls gelten weiterhin.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: withStatement / SYMBOL
Analysis/WithStructureValidator.cs: VisitWithStatement / VisitSubrutine / VisitTerminal
Runtime/ScriptBindings.cs: Builder.VisitWithStatement / Variable / CallName
Runtime/Instructions/Generator.cs: WithInstruction generation
Runtime/Instructions/WithInstruction.cs: CaptureName / StartAddress / EndAddress
Runtime/Interpreter.cs: CallSubrutine / TryGetObjectSubrutine / ResumeNextAddress
Runtime/ObjectTypes/NativeObjectTypeInference.cs: ResolveWithReceiver / Scope.VisitWithStatement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/with-end-with-statement
-->
