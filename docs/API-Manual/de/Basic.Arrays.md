# DIM / REDIM / PRESERVE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

DIM erstellt ein dynamisches Array; REDIM ersetzt dessen Speicher. PRESERVE kopiert Werte an gemeinsamen Indizes. Dimensionen nennen inklusive Obergrenzen, keine Elementzahlen. Elemente vor dem Lesen initialisieren.

## Genaue Syntax

```text
DIM name[upper]
DIM name(upper) AS type
DIM grid[xUpper][yUpper]
DIM grid(xUpper, yUpper)
REDIM name[upper]
REDIM PRESERVE name[upper]
name[index] = value
GetArrayLength(name)
```

## Parameter

- `name` — name: Arrayvariable. DIM deklariert sie; REDIM ersetzt den Wert einer bestehenden Bindung. Zugriff mit items[i], grid[x][y].
- `upper` — upper: einmal von links nach rechts ausgewerteter, in Integer umgewandelter Ausdruck. DIM items[2] erstellt drei Plätze 0..2. -1 erzeugt eine leere Dimension; kleinere Grenzen und Längenüberlauf sind Fehler. Praktisch begrenzt der Speicher die Größe.
- `PRESERVE` — PRESERVE: optional nach REDIM. Kopiert gemeinsame Indizes rekursiv; Verkleinern verwirft außerhalb liegende Werte. Ohne PRESERVE sind neue Plätze nicht initialisiert.
- `AS type` — AS type: akzeptierte DIM-Annotation ohne Typbindung, Initialisierung oder Umwandlung der Elemente. Unterschiedliche Wertarten sind möglich.

## Rückgabewert

DIM und REDIM liefern keinen Wert (Unit). items[i] liefert den gespeicherten Wert mit tatsächlicher Art Integer, Decimal, String, Array oder Object. Uninitialisiertes Lesen löst einen Fehler aus, nicht 0 oder FALSE. GetArrayLength(array) liefert die äußere Länge als Integer; bei Nicht-Arrays 0.

## Verhalten

- DIM grid(1, 2) entspricht grid[1][2], zwei Zeilen mit je drei Plätzen. Funktionsaufrufe in Grenzen bleiben erhalten. Zugriff erfolgt mit grid[1][2]; runde Klammern im Ausdruck bedeuten einen Funktionsaufruf.
- Zuweisung und ByVal kopieren die Referenz, nicht die Elemente. Aliase sehen Änderungen gemeinsamer Plätze. REDIM bindet ein neues Array, alte Aliase behalten das bisherige. PRESERVE kopiert gemeinsame Koordinaten verschachtelter Arrays, klont aber keine beliebigen Objekte vollständig.
- Indizes beginnen bei null. DIM items[2]=5 und REDIM-Initialisierer werden mit SC014 abgelehnt; Elemente separat zuweisen. Ungültige Indizes und uninitialisierte Zugriffe sind abfangbare Fehler.
- Dieser Basic-Dialekt unterscheidet sich durch dynamische Elementarten und mehrdimensionales PRESERVE von VB.NET. Gespeicherte boolesche Werte verwenden 1/0; beliebige Zahlen oder Längen sind keine Erfolgsflags.
- RETURN array gibt die Array-Referenz zurück; der Speicher bleibt nach dem Funktionsende erhalten. Eine Zuweisung kopiert keine Elemente. Eine Hilfsfunktion kann so ein Array für ein Module-Feld erstellen. Separate Skriptläufe erzeugen beim erneuten DIM neue Arrays.

## Beispiele

### 1. Elemente summieren

```vb
# Abs(-2) liefert Obergrenze 2: Main erstellt 3 Plätze mit 2, 4, 6. Sum erhält die Referenz ByVal, läuft über 0..GetArrayLength(items)-1 und liefert 12. Der vollständige Helfer ändert nichts und akzeptiert leere Arrays.
Option Explicit On
FUNCTION Sum(ByVal items)
    VAR total = 0
    VAR i = 0
    FOR i = 0 TO GetArrayLength(items) - 1
        total += items[i]
    NEXT
    RETURN total
END FUNCTION
SUB Main()
    DIM items(Abs(-2))
    items[0] = 2
    items[1] = 4
    items[2] = 6
    RETURN Sum(items)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Abs(-2) liefert Obergrenze 2: Main erstellt 3 Plätze mit 2, 4, 6. Sum erhält die Referenz ByVal, läuft über 0..GetArrayLength(items)-1 und liefert 12. Der vollständige Helfer ändert nichts und akzeptiert leere Arrays.

### 2. Vergrößern und bewahren

```vb
# values enthält 7 und 8. REDIM PRESERVE values(2) erstellt 3 Plätze und kopiert Indizes 0 und 1. Den neuen Platz 2 mit 9 initialisieren. Main liefert 7*100+8*10+9=789.
Option Explicit On
SUB Main()
    DIM values[1]
    values[0] = 7
    values[1] = 8
    REDIM PRESERVE values(2)
    values[2] = 9
    RETURN values[0] * 100 + values[1] * 10 + values[2]
END SUB
```

**Erläuterung der Parameter und Ausführung:**

values enthält 7 und 8. REDIM PRESERVE values(2) erstellt 3 Plätze und kopiert Indizes 0 und 1. Den neuen Platz 2 mit 9 initialisieren. Main liefert 7*100+8*10+9=789.

### 3. Aliase beobachten

```vb
# grid hat zwei Zeilen mit zwei Plätzen. alias teilt das Array: alias[0][1]=9 ändert auch grid. PRESERVE vergrößert grid auf drei Zeilen und erhält 9; alias bleibt bei zwei Zeilen. "9:3:2" bedeutet Wert, neue äußere Länge und Länge des alten Alias.
Option Explicit On
SUB Main()
    DIM grid[1][1]
    grid[0][1] = 4
    VAR alias = grid
    alias[0][1] = 9
    REDIM PRESERVE grid[2][1]
    RETURN CStr(grid[0][1]) + ":" + CStr(GetArrayLength(grid)) + ":" + CStr(GetArrayLength(alias))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

grid hat zwei Zeilen mit zwei Plätzen. alias teilt das Array: alias[0][1]=9 ändert auch grid. PRESERVE vergrößert grid auf drei Zeilen und erhält 9; alias bleibt bei zwei Zeilen. "9:3:2" bedeutet Wert, neue äußere Länge und Länge des alten Alias.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim / NormalizeArrayDeclarator
Analysis/ArrayDeclarationVisitor.cs: VisitDimDef
Runtime/Interpreter.cs: VisitDimDef / VisitRedim / VisitIndexedSymbol
Runtime/SemanticScope.cs: CreateArray / CopyArray / GetDim / SetDim
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/redim-statement
-->
