# Do / Loop / While / Until / Repeat

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Do prüft vor oder nach dem Rumpf. While wiederholt bei wahr; Until bis wahr. Repeat … Until ist die unterstützte ältere Form mit abschließender Prüfung.

## Genaue Syntax

```text
Do While condition
    statements
Loop
Do Until condition
    statements
Loop
Do
    statements
Loop While condition
Do
    statements
Loop Until condition
Do
    statements
Loop
Repeat
    statements
Until condition
Continue Do
Exit Do
Break
```

## Parameter

- `condition / While / Until` — Numerisches Boolean 0/False oder 1/True. While setzt bei wahr fort, Until beendet bei wahr. Bei jeder Prüfung neu ausgewertet; Text wird nicht als Boolean geparst.
- `position / Repeat` — Nach Do kann die Bedingung den ersten Durchlauf verhindern. Nach Loop oder Until von Repeat findet mindestens ein Durchlauf statt. Nur eine Bedingungsposition ist erlaubt. Do … Loop ohne Bedingung braucht einen ausdrücklichen Ausstieg.
- `statements / exit` — Rumpf. Continue Do erreicht die nächste Prüfung; Exit Do verlässt das nächste Do oder Repeat. Break verlässt die innerste Schleife beliebigen Typs. RETURN beendet die ganze Prozedur/Funktion.

## Rückgabewert

Do, Loop, Repeat, Until und Exit Do haben keinen Rückgabewert. Beispiele geben ausdrücklich Integer 1,33,83 aus Main zurück: kombinierte Zähler, keine booleschen Befehlsergebnisse.

## Verhalten

- Vorbereitung verknüpft Blöcke und prüft Übergänge. Bedingungen an beiden Enden desselben Do ergeben SC020. Die Engine prüft an der gewählten Position und wiederholt nach der While/Until-Regel.
- Continue Do prüft bei nachgestellter Bedingung diese weiterhin; bei vorgestellter kehrt es zum Kopf zurück. Verlassene Finally-Blöcke laufen vor dem Übergang genau einmal.
- Repeat führt zuerst aus: leere Arrays vorher abfangen. Kein implizites Zeitlimit. Beim Warten auf das Spiel Wait und Frist verwenden; Pause/Stopp bleiben aktiv.

## Beispiele

### 1. Vorher oder nachher

```vb
# ready=True erfüllt Until bereits. Do Until ready führt null Durchläufe aus: before=0. Die zweite Schleife prüft nach dem Erhöhen, daher after=1. Main liefert before*10+after=1.
Option Explicit On
Sub Main()
    Var ready = True
    Var before = 0
    Var after = 0
    Do Until ready
        before += 1
    Loop
    Do
        after += 1
    Loop Until ready
    Return before * 10 + after
End Sub
```

**Erläuterung der Parameter und Ausführung:**

ready=True erfüllt Until bereits. Do Until ready führt null Durchläufe aus: before=0. Die zweite Schleife prüft nach dem Erhöhen, daher after=1. Main liefert before*10+after=1.

### 2. Begrenzte Versuche mit Abschluss

```vb
# attempts startet bei 0 und steigt pro Durchlauf. Die ersten zwei Continue Do führen Finally und die Prüfung attempts<4 aus. Beim dritten Versuch führt auch Exit Do Finally aus. attempts=3, cleanup=3 ergeben 33. Lokale Simulation, keine echten Netzwerkwiederholungen.
Option Explicit On
Sub Main()
    Var attempts = 0
    Var cleanup = 0
    Do
        Try
            attempts += 1
            If attempts < 3 Then
                Continue Do
            End If
            Exit Do
        Finally
            cleanup += 1
        End Try
    Loop While attempts < 4
    Return attempts * 10 + cleanup
End Sub
```

**Erläuterung der Parameter und Ausführung:**

attempts startet bei 0 und steigt pro Durchlauf. Die ersten zwei Continue Do führen Finally und die Prüfung attempts<4 aus. Beim dritten Versuch führt auch Exit Do Finally aus. attempts=3, cleanup=3 ergeben 33. Lokale Simulation, keine echten Netzwerkwiederholungen.

### 3. Ältere Schleife bis zum Marker

```vb
# values=[3,5,0] ist nicht leer. Repeat liest, erhöht index und summiert. Until beendet bei null oder Arraygrenze; OrElse überspringt die zweite Prüfung nach einer gefundenen null. total=8 und index=3 ergeben 83.
Option Explicit On
Sub Main()
    Dim values[2]
    values[0] = 3
    values[1] = 5
    values[2] = 0
    Var index = 0
    Var value = 0
    Var total = 0
    Repeat
        value = values[index]
        index += 1
        total += value
    Until (value = 0) OrElse (index >= GetArrayLength(values))
    Return total * 10 + index
End Sub
```

**Erläuterung der Parameter und Ausführung:**

values=[3,5,0] ist nicht leer. Repeat liest, erhöht index und summiert. Until beendet bei null oder Arraygrenze; OrElse überspringt die zweite Prüfung nach einer gefundenen null. total=8 und index=3 ergeben 83.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(DoLoopContext) / VisitStatement(Repeat/Until)
Runtime/Interpreter.cs: LoopConditionInstruction / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/do-loop-statement
-->
