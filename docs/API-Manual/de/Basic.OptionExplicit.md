# Option Explicit

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Verlangt Variablendeklarationen vor der Skriptausführung. Dies ist eine Dateidirektive der Basic-Sprache dieser Engine, kein UO-Befehl und kein Funktionsaufruf.

## Genaue Syntax

```text
Option Explicit
Option Explicit On
Option Explicit Off
```

## Parameter

- `On / Off` — On aktiviert die strenge Deklarationsprüfung; Off deaktiviert sie. Ohne Wort nach Explicit gilt On. Ohne Direktive bleibt der bisherige nicht strenge Modus erhalten. Keine Klammern oder Anführungszeichen verwenden.

## Rückgabewert

Kein Wert. Die Direktive ist kein Ausdruck und liefert weder TRUE/FALSE noch eine Zahl oder ID. RETURN in den Beispielen gehört zu Main oder Enough, nicht zu Option Explicit.

## Verhalten

- Die Direktive einmal vor Variablen, Konstanten und Prozeduren schreiben. Leerzeilen und Kommentare dürfen davor stehen. Eine wiederholte oder verspätete Direktive erzeugt SC013, auch beim späteren Wechsel zu Off.
- Mit On erzeugt das Lesen oder Zuweisen einer nicht deklarierten Variablen SC006 mit Quellposition. Arraynamen, FOR-Zähler und Empfänger von Methodenaufrufen werden ebenfalls geprüft. VAR/DIM/CONST, Parameter und benannte CATCH-Variablen deklarieren Namen. FOR VAR deklariert den Zähler.
- Lokale Variablen vor ihrer Verwendung deklarieren. Eine lokale Variable einer Prozedur deklariert keinen Namen in einer anderen. Globale Deklarationen sind in Prozeduren verfügbar. Die Namensprüfung beweist keine Initialisierung in sämtlichen Zweigen.
- Der Parser liest die ganze Datei; die Analyse löst Deklarationen auf; strenge Fehler verhindern die Ausführung vor dem ersten Befehl. Beim Neuladen gilt die Option der neuen Datei unabhängig vom vorherigen Skript. Off kann weiterhin Warnungen erzeugen; das Lesen eines noch nicht vorhandenen Werts kann zur Laufzeit scheitern.
- Die Direktive allein führt keine Spielaktion aus und sendet keine Pakete. Sie bedeutet weder vollständige VB.NET-Kompatibilität noch eine Prüfung, ob ein Spielziel existiert.

## Beispiele

### 1. Vor der Zuweisung deklarieren

```vb
# On aktiviert die Prüfung. DIM deklariert count als Integer; die Zuweisung von 5 gelingt. Main liefert 5. Das nicht deklarierte coutn statt count verhindert den Start mit SC006.
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    RETURN count
END SUB
```

**Erläuterung der Parameter und Ausführung:**

On aktiviert die Prüfung. DIM deklariert count als Integer; die Zuweisung von 5 gelingt. Main liefert 5. Das nicht deklarierte coutn statt count verhindert den Start mit SC006.

### 2. Parameter und globale Konstante

```vb
# Die Direktive ohne Modus bedeutet On. minimum ist die globale Konstante 3. amount ist ein deklarierter Parameter in Enough und eine separate lokale Variable in Main. Enough vergleicht 5 >= 3 und liefert TRUE, numerisch 1.
Option Explicit
CONST minimum = 3
FUNCTION Enough(amount)
    RETURN amount >= minimum
END FUNCTION
SUB Main()
    VAR amount = 5
    RETURN Enough(amount)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Die Direktive ohne Modus bedeutet On. minimum ist die globale Konstante 3. amount ist ein deklarierter Parameter in Enough und eine separate lokale Variable in Main. Enough vergleicht 5 >= 3 und liefert TRUE, numerisch 1.

### 3. Ein älteres Skript ausführen

```vb
# Off erlaubt die Erstellung von legacyCounter durch Zuweisung ohne DIM. Main liefert 7. Dieses Kompatibilitätsbeispiel kann weiter eine Warnung anzeigen; für die strenge Prüfung die Variable deklarieren und On verwenden.
Option Explicit Off
SUB Main()
    legacyCounter = 7
    RETURN legacyCounter
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Off erlaubt die Erstellung von legacyCounter durch Zuweisung ohne DIM. Main liefert 7. Dieses Kompatibilitätsbeispiel kann weiter eine Warnung anzeigen; für die strenge Prüfung die Variable deklarieren und On verwenden.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: optionExplicit
Analysis/SanityAnalyzer.cs
Analysis/InvalidSymbolVisitor.cs
Runtime/InjectionRuntime.cs
-->
