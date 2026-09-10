# CONST

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

CONST deklariert einen Namen, dessen Bindung gewöhnliche Neuzuweisungen ablehnt. Der Startwert kann ein Literal oder Ausdrucksergebnis sein und wird bei Ausführung der Deklaration berechnet.

## Genaue Syntax

```text
CONST name [AS type] = expression [, name ...]
```

## Parameter

- `name` — Konstantenname ohne Anführungszeichen, eindeutig im eigenen Bereich. Außerhalb von Prozeduren ist die Deklaration global, innerhalb lokal für den Aufruf.
- `type` — Optionaler unterstützter AS-Typ mit denselben Konvertierungen wie VAR. AS Integer erzeugt etwa die vorzeichenbehaftete 32-Bit-Ganzzahl der Engine. Eckige Klammern markieren optionale Syntax und werden nicht um AS geschrieben.
- `expression` — Erforderlicher Startausdruck: Zahl, Text in Anführungszeichen, TRUE/FALSE, Berechnung oder Ergebnis einer unterstützten Funktion. Einmal pro Ausführung dieser Deklaration berechnet, nicht einmal für immer.

## Rückgabewert

Kein Wert. CONST ist eine Deklaration, keine Funktion oder Wahrheitsabfrage. Das Lesen des Namens liefert den gespeicherten Startwert. RETURN in den Beispielen gehört zu Main oder ApplyLimit.

## Verhalten

- Gewöhnliche Zuweisung, LET und SET können diese Bindung nicht ersetzen; es entsteht ein Konstantenfehler. TRY/CATCH kann ihn behandeln. Option Explicit verlangt Deklarationen, erkennt aber nicht jede ungültige Zuweisung schon vor dem Start.
- Globale Konstanten werden bei einem neuen Hauptaufruf initialisiert und mit Konstantenkennzeichen und AS-Typ an aufgerufene Prozeduren vererbt. Lokale Konstanten initialisieren bei ihrer Deklaration. Initialisierungsfunktionen können beim nächsten Start erneut arbeiten.
- Geschützt wird die Bindung, nicht der innere Inhalt von Array/Object. Eine separate lokale Deklaration kann einen globalen Namen verdecken; eine andere Deklaration erstellt eine neue Bindung. Konstantennamen zur Klarheit nicht wiederverwenden.
- Die Engine berechnet den Startausdruck, konvertiert AS und markiert die Konstante im Bereich. Spätere gewöhnliche Zuweisungen prüfen das Kennzeichen vor einer Änderung. Skalare Literalbeispiele führen keine Spielaktion aus.

## Beispiele

### 1. Feste Verzögerung berechnen

```vb
# delay ist eine lokale Integer-Konstante mit Wert 350. Multiplikation mit 2 erzeugt die separate Variable doubled=700. Main liefert 700; das Beispiel wartet nicht.
Option Explicit On
SUB Main()
    CONST delay AS Integer = 350
    VAR doubled = delay * 2
    RETURN doubled
END SUB
```

**Erläuterung der Parameter und Ausführung:**

delay ist eine lokale Integer-Konstante mit Wert 350. Multiplikation mit 2 erzeugt die separate Variable doubled=700. Main liefert 700; das Beispiel wartet nicht.

### 2. Globale Grenze übergeben

```vb
# limit ist eine globale Integer-Konstante mit Wert 50. ApplyLimit erhält amount=72 und maximum=50 und liefert die kleinere Menge 50. Die Funktion ist vollständig definiert und liest ihre Parameter nur.
Option Explicit On
CONST limit AS Integer = 50
FUNCTION ApplyLimit(amount, maximum)
    IF amount > maximum THEN
        RETURN maximum
    END IF
    RETURN amount
END FUNCTION
SUB Main()
    RETURN ApplyLimit(72, limit)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

limit ist eine globale Integer-Konstante mit Wert 50. ApplyLimit erhält amount=72 und maximum=50 und liefert die kleinere Menge 50. Die Funktion ist vollständig definiert und liest ihre Parameter nur.

### 3. Unzulässige Zuweisung behandeln

```vb
# limit beginnt mit 3. Die Zuweisung von 4 erzeugt einen Fehler und ändert die Konstante nicht. CATCH speichert den Fehler in problem und setzt caught=TRUE. Main liefert logisch 1; TRUE und 1 sind hier gleichwertig.
Option Explicit On
SUB Main()
    CONST limit = 3
    VAR caught = FALSE
    TRY
        limit = 4
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**Erläuterung der Parameter und Ausführung:**

limit beginnt mit 3. Die Zuweisung von 4 erzeugt einen Fehler und ändert die Konstante nicht. CATCH speichert den Fehler in problem und setzt caught=TRUE. Main liefert logisch 1; TRUE und 1 sind hier gleichwertig.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: constDeclaration / globalConst
Runtime/DefinitionCollector.cs: VisitGlobalConst
Runtime/Interpreter.cs: VisitConstDef
Runtime/SemanticScope.cs: DefineVar / SetVar
-->
