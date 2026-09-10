# For Each / Next

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

For Each durchläuft die Elemente eines Arrays oder einer aufzählbaren nativen Sammlung ohne numerischen Index. Die Anweisung steht in einer Prozedur oder Funktion und ist kein API-Aufruf.

## Genaue Syntax

```text
For Each item [AS type] In collection
    statements
Next [item]
```

## Parameter

- `item` — item: Laufvariable. Verwendet eine vorhandene lokale Variable, einen Parameter oder ein zugängliches Feld; andernfalls entsteht eine lokale Variable, auch mit Option Explicit On. Konstanten sind nicht beschreibbar.
- `type` — type: optionales AS type, etwa Integer. Deklariert eine lokale Laufvariable und konvertiert jedes Element. Ohne AS behält eine vorhandene Variable ihren Typ.
- `collection` — collection: einmal ausgewerteter Ausdruck. Erlaubt sind Arrays und aufzählbare native Objekte, keine Skalare. Verschachtelte Arrays liefern zunächst Zeilen; eine innere Schleife liefert Zellen.
- `statements / NEXT item` — statements / NEXT item: Rumpf und Abschluss. Der Name nach NEXT ist optional, muss aber zur Laufvariable passen. NEXT steht in einer eigenen Zeile.

## Rückgabewert

For Each und Next liefern keinen Wert. item erhält den Elementwert, nicht automatisch Index, ID oder Stapelmenge. RETURN im Rumpf beendet die gesamte Funktion. Die Beispiele liefern Integer 12, 105 und 10.

## Verhalten

- Die Vorbereitung verknüpft FOR EACH mit NEXT vor jeder Initialisierung. Ein falsches NEXT erzeugt SC020. Die Engine speichert Sammlungsreferenz und eigenen Cursor; eine Zuweisung an item verschiebt diesen nicht.
- Arrays werden nach aufsteigendem Index gelesen. Ein leeres Array überspringt den Rumpf und erhält den Wert einer vorhandenen Variable ohne AS. Uninitialisierte Elemente und ungültige AS-Konvertierungen erzeugen abfangbare Fehler.
- item=... ersetzt kein Arrayelement. Verschachtelte Arrays und Objekte sind Referenzen: Änderungen an row-Zellen ändern die Zeile. Neuzuweisung von collection wechselt nicht die aktive Sammlung; Änderungen späterer Elemente desselben Arrays sind beim Lesen sichtbar.
- Continue For geht beim nächsten For oder For Each weiter, Exit For verlässt ihn. Fehler, RETURN und Abbruch geben native Enumerator-Ressourcen frei. Manche Sammlungen verbieten Änderungen während des Durchlaufs; es wird keine automatische Kopie erstellt.
- Die Laufvariable bleibt in der Prozedur nach der Schleife sichtbar und behält den zuletzt zugewiesenen Wert. Jeder Start besitzt einen eigenen Cursor. IDE-Ergänzung, Vorlagen, Navigation sowie Pause und Stopp werden unterstützt.

## Beispiele

### 1. Summe ohne Index

```vb
# values[2] enthält drei Elemente 2, 4, 6. SumItems erhält das Array und item nacheinander die Zahlen. total steigt von 0 auf 12; RETURN gibt Integer 12 an Main. NEXT item beendet diese Schleife.
Option Explicit On
Function SumItems(values)
    Var total = 0
    For Each item In values
        total += item
    Next item
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return SumItems(values)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

values[2] enthält drei Elemente 2, 4, 6. SumItems erhält das Array und item nacheinander die Zahlen. total steigt von 0 auf 12; RETURN gibt Integer 12 an Main. NEXT item beendet diese Schleife.

### 2. Einmal auswerten, Werte konvertieren

```vb
# SelectItems erhält calls ByRef, setzt es auf 1 und liefert ["2", "3"]. AS Integer wandelt in 2 und 3 um; total=5. item=100 ändert weder Quelle noch Reihenfolge. Main liefert calls*100+total, Integer 105.
Option Explicit On
Function SelectItems(ByRef calls)
    calls += 1
    Dim values[1]
    values[0] = "2"
    values[1] = "3"
    Return values
End Function
Sub Main()
    Var calls = 0
    Var total = 0
    For Each item As Integer In SelectItems(calls)
        total += item
        item = 100
    Next
    Return calls * 100 + total
End Sub
```

**Erläuterung der Parameter und Ausführung:**

SelectItems erhält calls ByRef, setzt es auf 1 und liefert ["2", "3"]. AS Integer wandelt in 2 und 3 um; total=5. item=100 ändert weder Quelle noch Reihenfolge. Main liefert calls*100+total, Integer 105.

### 3. Verschachtelte Arrays

```vb
# rows[1][1] enthält zwei Zeilen mit je zwei Zellen. row erhält eine Zeilenreferenz, cell die Werte 1, 2, 3, 4. Jedes NEXT schließt seine Schleife. SumGrid und Main liefern Integer 10; ID und Menge werden nicht automatisch ermittelt.
Option Explicit On
Function SumGrid(rows)
    Var total = 0
    For Each row In rows
        For Each cell In row
            total += cell
        Next cell
    Next row
    Return total
End Function
Sub Main()
    Dim rows[1][1]
    rows[0][0] = 1
    rows[0][1] = 2
    rows[1][0] = 3
    rows[1][1] = 4
    Return SumGrid(rows)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

rows[1][1] enthält zwei Zeilen mit je zwei Zellen. row erhält eine Zeilenreferenz, cell die Werte 1, 2, 3, 4. Jedes NEXT schließt seine Schleife. SumGrid und Main liefern Integer 10; ID und Menge werden nicht automatisch ermittelt.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: forEach / next
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretForEach / CallSubrutine
Runtime/ForScope.cs: AdvanceEach / Dispose
Runtime/ScriptBindings.cs: VisitForEach / LocalNames
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-each-next-statement
-->
