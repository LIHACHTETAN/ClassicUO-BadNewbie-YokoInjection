# Select Case / Case / Exit Select

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Select Case wählt einen Zweig, indem ein gespeicherter Wert der Reihe nach mit Alternativen verglichen wird. Geeignet für Gegenstandskategorien, Skriptmodi und Zahlenbereiche. Die Basic-Anweisung braucht kein UO.; Spielaufrufe in Ausdrücken behalten UO.

## Genaue Syntax

```text
Select Case expression
    Case value1, value2
        statements
        Exit Select
    Case from To to
        statements
    Case Is >= value
        statements
    Case Else
        statements
End Select
```

## Parameter

- `expression` — Pflichtausdruck: Variable, Literal oder Funktionsaufruf. Wird bei jedem Eintritt genau einmal ausgewertet, auch bei leerem Block oder ausschließlich Case Else.
- `value / from / to` — Case erlaubt einen Wert oder durch Kommas getrennte Ausdrücke. from To to schließt beide Grenzen ein. Ein umgekehrter Bereich trifft nicht zu. Die obere Grenze wird nur nach erfolgreicher unterer Prüfung ausgewertet. Kommas innerhalb von Funktionsargumenten trennen keine Alternativen.
- `Is comparison value` — Vergleiche mit =, <>, <, <=, > oder >=. Is ist optional: Case Is >= 5 und Case >= 5 sind gleichwertig. Es gelten die Wertvergleiche der Engine, keine Objekttypprüfung.
- `Case Else` — Optionaler Ersatzfall, wenn zuvor kein Case passt. Darf nur einmal und zuletzt stehen. Ohne ihn geht es bei fehlender Übereinstimmung nach End Select weiter.
- `Exit Select` — Verlässt den nächstliegenden umgebenden Select Case bis hinter dessen End Select. Beendet weder äußere Schleife noch Prozedur. Außerhalb eines Select Case entsteht ein Ladefehler.

## Rückgabewert

Select Case, Case, End Select und Exit Select liefern keinen Wert und werden nicht mit TRUE oder 1 verglichen. Die Beispielfunktionen geben String oder Integer ausdrücklich mit Return zurück. TRUE ist numerisch 1 und FALSE 0; Case True passt zu 1, nicht zu jeder Zahl ungleich null.

## Verhalten

- Die Vorbereitung erzeugt SelectInstruction, geordnete CaseInstruction-Prüfungen und aufgelöste Sprünge. Die Auswahl wird privat im aktuellen Funktionsaufruf gespeichert, ohne künstliche lokale Variable. Rekursion und verschachtelte Blöcke haben unabhängige Werte; jeder erneute Eintritt ersetzt den alten Wert.
- CaseMatches prüft von links nach rechts bis zum ersten Treffer. Der gewählte Rumpf läuft einmal, ein Sprung überspringt die übrigen Zweige. Änderungen innerhalb eines Case lesen die Auswahl nicht erneut ein. Bereits erfolgte Nebenwirkungen bleiben bestehen.
- Zahlen und Zeichenfolgen verwenden normale Engine-Vergleiche; Zeichenfolgen beachten Großschreibung. Option Compare Text und automatische VB.NET-Konvertierung sind nicht implementiert. Zahl und Text bei Bedarf ausdrücklich umwandeln.
- End Select ist erforderlich. Kein ausführbarer Code vor dem ersten Case; For und Next dürfen nicht auf verschiedene Zweige verteilt werden. Fehlerhafte Blöcke verhindern das Laden. Über Select Case eintreten, nicht mit GoTo in die Mitte.
- Fehler gehen an die aktuelle Fehlerbehandlung. On Error Resume Next überspringt eine fehlgeschlagene Auswahl ganz, bei einem fehlerhaften Case geht es zum nächsten. Resume wiederholt die betroffene Anweisung. Exit Select führt verlassene aktive Finally-Blöcke aus. Pause und Stopp bleiben zwischen Anweisungen wirksam; keine Wartezeit oder Zeitgrenze wird ergänzt.

## Beispiele

### 1. Mengen einordnen

```vb
# DescribeAmount erhält amount ByVal. Case 0 liefert empty; 1 To 4 enthält 1 und 4; Is >= 5 liefert large. Negative Werte gelangen zu Case Else. Main ruft mit -1, 0, 4 und 5 auf und verbindet zu negative:empty:small:large. Die Wörter sind skripteigene Ergebnisse.
Option Explicit On
Function DescribeAmount(ByVal amount)
    Select Case amount
        Case 0
            Return "empty"
        Case 1 To 4
            Return "small"
        Case Is >= 5
            Return "large"
        Case Else
            Return "negative"
    End Select
End Function

Sub Main()
    Return DescribeAmount(-1) & ":" & DescribeAmount(0) & ":" & DescribeAmount(4) & ":" & DescribeAmount(5)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

DescribeAmount erhält amount ByVal. Case 0 liefert empty; 1 To 4 enthält 1 und 4; Is >= 5 liefert large. Negative Werte gelangen zu Case Else. Main ruft mit -1, 0, 4 und 5 auf und verbindet zu negative:empty:small:large. Die Wörter sind skripteigene Ergebnisse.

### 2. Aufrufe beobachten

```vb
# ReadMode erhöht reads ByRef und liefert einmal 2. Candidate erhöht checks und liefert value. Kandidat 1 passt nicht, 2 passt und 3 wird übersprungen. selected wird 7; Main liefert 1*100+2*10+7=127 ohne Spielzugriff.
Option Explicit On
Function ReadMode(ByRef reads)
    reads += 1
    Return 2
End Function

Function Candidate(ByRef checks, ByVal value)
    checks += 1
    Return value
End Function

Sub Main()
    Dim reads = 0
    Dim checks = 0
    Dim selected = 0
    Select Case ReadMode(reads)
        Case Candidate(checks, 1)
            selected = -1
        Case Candidate(checks, 2), Candidate(checks, 3)
            selected = 7
        Case Else
            selected = -9
    End Select
    Return reads * 100 + checks * 10 + selected
End Sub
```

**Erläuterung der Parameter und Ausführung:**

ReadMode erhöht reads ByRef und liefert einmal 2. Candidate erhöht checks und liefert value. Kandidat 1 passt nicht, 2 passt und 3 wird übersprungen. selected wird 7; Main liefert 1*100+2*10+7=127 ohne Spielzugriff.

### 3. Verschachtelten Block verlassen

```vb
# route enthält harvest, der erste Zweig setzt trace=1. Der innere Case 2 führt Exit Select aus und überspringt trace=99; Finally hängt 2 an. Der äußere Zweig hängt 3 an: Ergebnis 123. Sein Case Else entfällt. Eine andere Zeichenfolge in route ergibt -1.
Option Explicit On
Sub Main()
    Dim route = "harvest"
    Dim trace = 0
    Select Case route
        Case "harvest", "loot"
            trace = 1
            Select Case 2
                Case 2
                    Try
                        Exit Select
                        trace = 99
                    Finally
                        trace = trace * 10 + 2
                    End Try
            End Select
            trace = trace * 10 + 3
        Case Else
            trace = -1
    End Select
    Return trace
End Sub
```

**Erläuterung der Parameter und Ausführung:**

route enthält harvest, der erste Zweig setzt trace=1. Der innere Case 2 führt Exit Select aus und überspringt trace=99; Finally hängt 2 an. Der äußere Zweig hängt 3 an: Ergebnis 123. Sein Case Else entfällt. Eine andere Zeichenfolge in route ergibt -1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: selectStatement / caseClause / caseTest / exitSelect
Analysis/LoopStructureValidator.cs: VisitSelectStatement / VisitExitSelect / VisitCodeBlock
Runtime/Instructions/Generator.cs: Generate(SelectStatementContext)
Runtime/Instructions/SelectInstruction.cs: SelectInstruction / CaseInstruction
Runtime/Interpreter.cs: CaseMatches / ResumeNextAddress / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/select-case-statement
-->
