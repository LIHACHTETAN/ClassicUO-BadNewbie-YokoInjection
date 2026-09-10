# For / To / Step / Next / Exit For

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

For wiederholt einen Block über einen einschließlichen Zahlenbereich. Geeignet für Indizes oder eine bekannte Anzahl von Schritten; For Each durchläuft Elementwerte.

## Genaue Syntax

```text
For [VAR] counter = start To limit [Step increment]
    statements
Next [counter]
Continue For
Exit For
Break
```

## Parameter

- `counter / VAR` — Beschreibbare skalare Zählvariable. VAR deklariert sie in der Prozedur, sonst wird eine vorhandene Variable verwendet. Mit Option Explicit On vorher deklarieren oder For Var nutzen. Typ separat angeben: DIM counter AS Integer; AS im numerischen For-Kopf wird nicht unterstützt.
- `start` — Numerischer Startausdruck, einmal ausgewertet und vor limit und increment zugewiesen.
- `limit` — Einschließliche Grenze, beim Eintritt einmal ausgewertet. Positiver Schritt: counter <= limit; negativer: counter >= limit.
- `increment` — Optionaler Zahlenschritt, standardmäßig 1. Negative und gebrochene Schritte sind erlaubt; null erzeugt einen abfangbaren Fehler. Zählertyp und Schritt müssen Fortschritt erlauben.
- `statements / Next / exit` — Rumpf und Next auf getrennten Zeilen. Der optionale Next-Name muss übereinstimmen. Continue For erreicht den nächsten Schritt; Exit For verlässt das nächste For/For Each; Break verlässt die innerste Schleife beliebigen Typs.

## Rückgabewert

For, Next und Exit For liefern keinen Wert. Der Zähler ist eine Zahl, nicht automatisch eine Gegenstands-ID. Nach regulärem Ende behält diese Engine den zuletzt ausgeführten Wert statt eines Werts außerhalb der Grenze. Überspringen behält start, früher Ausstieg den aktuellen Wert. Beispiele liefern Integer 12,28,395.

## Verhalten

- Eintritt: start zuweisen, Grenze und Schritt speichern, null ablehnen, ersten Wert prüfen. Falsche Richtung überspringt den Rumpf; start=limit führt ihn einmal aus.
- Next prüft counter+step und weist nur zu, wenn eine weitere Iteration im Bereich liegt. 1 To 5 Step 3 besucht 1 und 4. Änderungen der ursprünglichen Grenz-/Schrittvariablen ändern die gespeicherten Werte nicht; Änderungen am Zähler beeinflussen den nächsten Schritt.
- Struktur und Next-Name werden vor Ausführung geprüft; Strukturfehler ergeben SC020. Für Verschachtelungen verschiedene Zähler nutzen. Beim Verlassen eines Try läuft Finally. Pause/Stopp bleiben aktiv; keine automatische Wartezeit oder Frist.

## Beispiele

### 1. Arrayzellen summieren

```vb
# values[2] erzeugt Indizes 0,1,2 mit 2,4,6. Sum bekommt das Array ByVal, startet index=0 und speichert length-1=2. Standardschritt 1 besucht drei Zellen; total=12 geht an Main.
Option Explicit On
Function Sum(ByVal items)
    Var total = 0
    For Var index = 0 To GetArrayLength(items) - 1
        total += items[index]
    Next index
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return Sum(values)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

values[2] erzeugt Indizes 0,1,2 mit 2,4,6. Sum bekommt das Array ByVal, startet index=0 und speichert length-1=2. Standardschritt 1 besucht drei Zellen; total=12 geht an Main.

### 2. Vom Ende löschen

```vb
# items enthält -1,3,-2,5. Start Count()-1=3, Grenze 0, Schritt -1. Das Löschen eines negativen Elements verschiebt nur bereits besuchte Indizes; kein ausstehendes Element wird übersprungen. Übrig bleiben 3,5; Count()*10+3+5 liefert 28.
Option Explicit On
Sub Main()
    Var items = List()
    items.Add(-1)
    items.Add(3)
    items.Add(-2)
    items.Add(5)
    For Var index = items.Count() - 1 To 0 Step -1
        If items[index] < 0 Then
            items.RemoveAt(index)
        End If
    Next index
    Return items.Count() * 10 + items[0] + items[1]
End Sub
```

**Erläuterung der Parameter und Ausführung:**

items enthält -1,3,-2,5. Start Count()-1=3, Grenze 0, Schritt -1. Das Löschen eines negativen Elements verschiebt nur bereits besuchte Indizes; kein ausstehendes Element wird übersprungen. Übrig bleiben 3,5; Count()*10+3+5 liefert 28.

### 3. Grenzen und letzter Zähler

```vb
# ReadLimit erhöht calls ByRef und liefert value. Start=1, Grenze=5, Schritt=2 werden je einmal gelesen: calls=3. upper=99 und stride=1 im Rumpf ändern das nicht. Besucht werden 1,3,5; total=9, index bleibt 5. Main liefert 395.
Option Explicit On
Function ReadLimit(ByRef calls, ByVal value)
    calls += 1
    Return value
End Function
Sub Main()
    Var calls = 0
    Var upper = 5
    Var stride = 2
    Var total = 0
    For Var index = ReadLimit(calls, 1) To ReadLimit(calls, upper) Step ReadLimit(calls, stride)
        total += index
        upper = 99
        stride = 1
    Next index
    Return calls * 100 + total * 10 + index
End Sub
```

**Erläuterung der Parameter und Ausführung:**

ReadLimit erhöht calls ByRef und liefert value. Start=1, Grenze=5, Schritt=2 werden je einmal gelesen: calls=3. upper=99 und stride=1 im Rumpf ändern das nicht. Besucht werden 1,3,5; total=9, index bleibt 5. Main liefert 395.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretFor / CallSubrutine
Runtime/ForScope.cs: ContainsCurrent / HasNext
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-next-statement
-->
