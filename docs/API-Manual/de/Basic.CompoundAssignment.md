# += / -= / *= / /= / &=

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Vorhandene Variablen oder Arrayelemente mit +=, -=, *=, /= ändern. Die Engine liest den Wert, rechnet und schreibt zurück, ohne das Ziel zweimal auszuwerten.

## Genaue Syntax

```text
target += value
target -= value
target *= value
target /= value
target &= value
```

## Parameter

- `target` — target: vorhandener Skalar oder Element items[index], grid[x][y]. Elemente müssen initialisiert und nullbasierte Indizes gültig sein. Dies deklariert keine Variable.
- `operator` — += und &= addieren Zahlen oder verbinden zwei String-Werte; -= subtrahiert; *= multipliziert; /= dividiert. Der Präprozessor ersetzt &= durch +=, daher speichert 5 &= 3 den Wert 8. String und Zahl benötigen ausdrückliches CStr. Jeden Operator als ein Token schreiben.
- `value` — value: einmal nach Ziel und Indizes ausgewerteter Ausdruck. Seine Wertart muss zur Operation passen. Zahlen vor dem Anhängen an String mit CStr umwandeln.

## Rückgabewert

Kein Wert (Unit). Eine Anweisung, kein Ausdruck oder Erfolgsflag. Das gespeicherte Ergebnis anschließend aus target lesen. AS gilt beim skalaren Zurückschreiben: Integer 5 speichert nach /=2 Integer 2, eine untypisierte Zahl erhält Decimal 2.5.

## Verhalten

- Jede Arrayreferenz wird vor ihrem Index erfasst. Indizes laufen einmal von links nach rechts; Grenzen werden vor dem rechten Operanden geprüft. Die erfasste Zelle bleibt das Ziel, auch wenn eine ByRef-Funktion die Arrayvariable oder übergeordnete Zelle ersetzt.
- Es gelten die Regeln von +, -, *, /: Ganzzahlüberlauf innerhalb von 32 Bit; / liefert Decimal und bei Gleitkommadivision durch null eventuell Infinity/NaN. String mit Zahl zu addieren schlägt fehl. Arrayelemente haben keine skalare AS-Umwandlung.
- Nicht deklariertes Ziel, uninitialisiertes Element, falscher Index, ungeeignete Operation, CONST-Schreiben oder fehlgeschlagene Umwandlung lösen abfangbare Fehler aus. Die abschließende Speicherung entfällt; bereits ausgeführte Operandeneffekte werden nicht zurückgerollt. CONST und AS werden beim skalaren Schreiben nach dem rechten Ausdruck geprüft.
- Option Explicit prüft Namen vor dem Start. Debugger verwenden die Quellzeile, Schleifen beachten Pause/Stopp. Lesen, Rechnen und Schreiben sind keine atomare Synchronisierung paralleler Prozeduren.

## Beispiele

### 1. Alle vier Operationen

```vb
# amount beginnt bei 10. +=2 ergibt 12, -=3 ergibt 9, *=4 ergibt 36, /=2 ergibt Decimal 18. Main liefert den gespeicherten Wert; die Zuweisungen selbst geben nichts zurück.
Option Explicit On
SUB Main()
    VAR amount = 10
    amount += 2
    amount -= 3
    amount *= 4
    amount /= 2
    RETURN amount
END SUB
```

**Erläuterung der Parameter und Ausführung:**

amount beginnt bei 10. +=2 ergibt 12, -=3 ergibt 9, *=4 ergibt 36, /=2 ergibt Decimal 18. Main liefert den gespeicherten Wert; die Zuweisungen selbst geben nichts zurück.

### 2. Index nur einmal auswerten

```vb
# NextIndex erhöht den ByRef-Parameter calls und liefert 0. items[0] beginnt bei 5; +=2 ändert es auf 7. Ein Aufruf bedeutet calls=1. Main liefert items[0]*10+calls=71. Die Hilfsfunktion ist vollständig angegeben.
Option Explicit On
FUNCTION NextIndex(ByRef calls)
    calls += 1
    RETURN 0
END FUNCTION
SUB Main()
    DIM items[0]
    items[0] = 5
    VAR calls = 0
    items[NextIndex(calls)] += 2
    RETURN items[0] * 10 + calls
END SUB
```

**Erläuterung der Parameter und Ausführung:**

NextIndex erhöht den ByRef-Parameter calls und liefert 0. items[0] beginnt bei 5; +=2 ändert es auf 7. Ein Aufruf bedeutet calls=1. Main liefert items[0]*10+calls=71. Die Hilfsfunktion ist vollständig angegeben.

### 3. Konstantenschutz behandeln

```vb
# limit ist CONST 5. limit+=1 scheitert beim Schreiben; CATCH speichert den Fehler in problem und setzt caught=TRUE. limit bleibt 5. Main liefert "5:1" mit ausdrücklichem CStr. Das Flag beschreibt die Fehlerbehandlung, nicht das Ergebnis der Zuweisung. Die Ausgabe entsteht in einer Variablen: report=CStr(limit), dann report &= ":" und report &= CStr(caught). Jedes &= aktualisiert report; Return report liefert "5:1".
Option Explicit On
SUB Main()
    CONST limit = 5
    VAR caught = FALSE
    TRY
        limit += 1
    CATCH problem
        caught = TRUE
    END TRY
    VAR report = CStr(limit)
    report &= ":"
    report &= CStr(caught)
    RETURN report
END SUB
```

**Erläuterung der Parameter und Ausführung:**

limit ist CONST 5. limit+=1 scheitert beim Schreiben; CATCH speichert den Fehler in problem und setzt caught=TRUE. limit bleibt 5. Main liefert "5:1" mit ausdrücklichem CStr. Das Flag beschreibt die Fehlerbehandlung, nicht das Ergebnis der Zuweisung. Die Ausgabe entsteht in einer Variablen: report=CStr(limit), dann report &= ":" und report &= CStr(caught). Jedes &= aktualisiert report; Return report liefert "5:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: compoundAssignment / compoundOperator
Runtime/BasicSyntaxPreprocessor.cs: ReplaceConcatenationOutsideLiterals
Analysis/InvalidSymbolVisitor.cs: VisitCompoundAssignment / ValidateAssignmentTarget
Runtime/Interpreter.cs: VisitCompoundAssignment
Runtime/SemanticScope.cs: ValidateIndex / SetVar / Coerce
-->
