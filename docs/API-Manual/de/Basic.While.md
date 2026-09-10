# While / Wend / Exit While / Break

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

While prüft vor jedem Durchlauf und wiederholt bei wahrer Bedingung. Diese Engine schließt mit Wend; die VB.NET-Schreibweise End While wird nicht unterstützt.

## Genaue Syntax

```text
While condition
    statements
Wend
Continue While
Exit While
Break
```

## Parameter

- `condition` — Ausdruck bei jeder Prüfung, einschließlich erster und letzter. Vergleich oder numerisches Boolean verwenden: 0/False beendet, 1/True und andere von null verschiedene Zahlen setzen fort. Text wird nicht als Boolean gelesen.
- `statements` — Anweisungen für Arbeit und Fortschritt der Bedingung. Ist die erste Prüfung falsch, wird der gesamte Rumpf übersprungen.
- `Wend / exit` — Wend springt zur Prüfung. Continue While prüft erneut; Exit While verlässt das nächste While auch über eine innere Schleife anderen Typs. Break verlässt die innerste Schleife beliebigen Typs.

## Rückgabewert

While, Wend, Exit While und Break liefern keinen Wert. RETURN im Rumpf beendet die ganze Prozedur/Funktion. Beispiele liefern Integer 6,1,406. Suchergebnis 1 ist ein Arrayindex, kein Wahrheitswert.

## Verhalten

- Ablauf: prüfen, Rumpf ausführen, zurückspringen. Keine gespeicherte numerische Grenze, kein automatisches Inkrement.
- Fortschritt ausdrücklich programmieren. Beim regelmäßigen Abfragen des Spiels passenden Wait und eine Frist vorsehen: While wartet nicht und hat kein eigenes Zeitlimit. Pause/Stopp bleiben verfügbar.
- Continue und Ausstieg führen Finally der verlassenen Try-Blöcke aus. Kopf, Anweisungen und Wend stehen auf getrennten Zeilen innerhalb einer Prozedur/Funktion.

## Beispiele

### 1. Ziffernsumme

```vb
# DigitSum erhält number=123 ByVal. MOD 10 liest die letzte Ziffer; Fix(number/10) entfernt sie: 123→12→1→0. total=3+2+1=6. Die letzte falsche Prüfung beendet; Main erhält 6. Eingabe 0 hätte ohne Rumpf den Wert 0.
Option Explicit On
Function DigitSum(ByVal number)
    Var total = 0
    While number > 0
        total += number MOD 10
        number = Fix(number / 10)
    Wend
    Return total
End Function
Sub Main()
    Return DigitSum(123)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

DigitSum erhält number=123 ByVal. MOD 10 liest die letzte Ziffer; Fix(number/10) entfernt sie: 123→12→1→0. total=3+2+1=6. Die letzte falsche Prüfung beendet; Main erhält 6. Eingabe 0 hätte ohne Rumpf den Wert 0.

### 2. Ersten Treffer finden

```vb
# FirstAbove bekommt values=[4,7,9], threshold=6. Die Grenzprüfung schützt values[index]. Bei index=1 setzt 7>6 found=1 und Exit While beendet die Suche. Ohne Treffer bleibt -1. Main liefert den bei null beginnenden Index 1.
Option Explicit On
Function FirstAbove(ByVal values, ByVal threshold)
    Var index = 0
    Var found = -1
    While index < GetArrayLength(values)
        If values[index] > threshold Then
            found = index
            Exit While
        End If
        index += 1
    Wend
    Return found
End Function
Sub Main()
    Dim values[2]
    values[0] = 4
    values[1] = 7
    values[2] = 9
    Return FirstAbove(values, 6)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

FirstAbove bekommt values=[4,7,9], threshold=6. Die Grenzprüfung schützt values[index]. Bei index=1 setzt 7>6 found=1 und Exit While beendet die Suche. Ohne Treffer bleibt -1. Main liefert den bei null beginnenden Index 1.

### 3. Prüfungen zählen

```vb
# CanContinue erhält checks ByRef, index und limit=3 ByVal, erhöht checks und liefert index<limit als 1/0. Prüfungen bei 0,1,2,3: vier Aufrufe für drei Durchläufe. total=6; Main liefert 406.
Option Explicit On
Function CanContinue(ByRef checks, ByVal index, ByVal limit)
    checks += 1
    Return index < limit
End Function
Sub Main()
    Var checks = 0
    Var index = 0
    Var total = 0
    While CanContinue(checks, index, 3)
        index += 1
        total += index
    Wend
    Return checks * 100 + total
End Sub
```

**Erläuterung der Parameter und Ausführung:**

CanContinue erhält checks ByRef, index und limit=3 ByVal, erhöht checks und liefert index<limit als 1/0. Prüfungen bei 0,1,2,3: vier Aufrufe für drei Durchläufe. total=6; Main liefert 406.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(WhileContext)
Runtime/Interpreter.cs: WhileInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/while-end-while-statement
-->
