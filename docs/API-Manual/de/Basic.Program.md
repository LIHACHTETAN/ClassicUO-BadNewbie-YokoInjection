# SUB Main()

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Eine Basic-Datei enthält Prozedur-/Funktionsdefinitionen und optionale globale Deklarationen. Ausführbare Arbeit gehört in eine Prozedur. Diese Beispiele verwenden Main() als Einstieg und sind vollständige Dateien.

## Genaue Syntax

```text
Option Explicit On
SUB Main()
    statement
END SUB
# comment
; comment
REM comment
// comment
' comment
```

## Parameter

- `Main / entry` — Zum Start gewählte Prozedur. Main ist ein üblicher Name, keine automatische Anweisung. SUB Main() deklariert eine Prozedur ohne Argumente. Eine Hilfsfunktion arbeitet erst beim Aufruf.
- `statement` — Eine ausführbare Anweisung pro Zeile innerhalb SUB…END SUB oder FUNCTION…END FUNCTION. Globale VAR/CONST und Option Explicit stehen außerhalb; Option Explicit vor den Deklarationen.
- `comment` — # und ; beginnen außerhalb von Zeichenketten Kommentare, auch nach Code. REM, // und ein Apostroph beginnen ganze Kommentarzeilen nach optionaler Einrückung. Innerhalb von Zeichenketten können diese Zeichen wörtlicher Text sein.

## Rückgabewert

Dateiladen oder eine SUB-Deklaration liefert keinen Wert. RETURN expression liefert den Wert und beendet den Aufruf sofort. Das Blockende oder RETURN ohne Ausdruck ergibt Unit, also keinen Wert.

## Verhalten

- UTF-8 bewahrt lokalisierte Kommentare und Texte. CRLF und LF werden akzeptiert. Einrückung und Leerzeilen verbessern die Lesbarkeit, ersetzen aber nicht END SUB oder END FUNCTION.
- Schlüsselwörter, Prozedur- und Variablennamen ignorieren Groß-/Kleinschreibung: itemCount, ITEMCOUNT und ItemCount bezeichnen dieselbe Bindung. Text behält seine Schreibweise; Schlüssel in UO.SetGlobal("Key", …) sind Daten, keine Bezeichner.
- Einfache Namen beginnen mit ASCII-Buchstaben oder Unterstrich, danach sind Buchstaben, Ziffern und Unterstriche zulässig. Reservierte Wörter und API-Namen vermeiden. UO.Print ist ein qualifizierter Aufruf. Ein Doppelpunkt nach einem Namen definiert eine Sprungmarke, keinen allgemeinen Anweisungstrenner.
- Die Engine normalisiert unterstütztes Basic, analysiert die ganze Datei, sammelt Deklarationen und prüft Namen. Hilfsfunktionen dürfen deshalb unter Main stehen. Laden startet nicht alle Definitionen: Der Start initialisiert die gewählte Prozedur und folgt ihren Aufrufen.
- Die Beispiele berechnen nur Werte. Nach Prüfung der Vorlage die benötigten UO-Aufrufe in den Körper einfügen. Diese Regeln beschreiben die Engine, ohne sämtliche Funktionen anderer Basic-Implementierungen zu versprechen.

## Beispiele

### 1. Kommentare und wörtlicher Text

```vb
# Main definiert note als "ore #1; keep". # und ; in der Zeichenkette bleiben erhalten. Andere Kommentare mit #, REM, // und Apostroph tun nichts. RETURN liefert den ursprünglichen Text.
Option Explicit On
# Complete file
SUB Main()
    REM Full-line comment
    VAR note = "ore #1; keep" # Trailing comment
    // Another full-line comment
    ' Another full-line comment
    RETURN note
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Main definiert note als "ore #1; keep". # und ; in der Zeichenkette bleiben erhalten. Andere Kommentare mit #, REM, // und Apostroph tun nichts. RETURN liefert den ursprünglichen Text.

### 2. Vollständige Hilfsfunktion

```vb
# Main ruft DoubleCount mit amount=7 auf. Die darunter definierte Funktion multipliziert ihren Integer-Parameter mit 2 und liefert 14. Main gibt das Ergebnis weiter. Keine fehlende Include-Datei oder undefinierte Hilfsfunktion nötig.
Option Explicit On
SUB Main()
    RETURN DoubleCount(7)
END SUB
FUNCTION DoubleCount(ByVal amount AS Integer)
    VAR result = amount * 2
    RETURN result
END FUNCTION
```

**Erläuterung der Parameter und Ausführung:**

Main ruft DoubleCount mit amount=7 auf. Die darunter definierte Funktion multipliziert ihren Integer-Parameter mit 2 und liefert 14. Main gibt das Ergebnis weiter. Keine fehlende Include-Datei oder undefinierte Hilfsfunktion nötig.

### 3. Schreibweise der Namen

```vb
# itemCount beginnt mit 3. ITEMCOUNT und itemcount addieren 2 zu derselben Variablen. Gemischt geschriebene Schlüsselwörter funktionieren. Main liefert 5, ohne zusätzliche Variablen anzulegen.
Option Explicit On
sUb Main()
    Var itemCount = 3
    ITEMCOUNT = itemcount + 2
    ReTuRn ItemCount
EnD sUb
```

**Erläuterung der Parameter und Ausführung:**

itemCount beginnt mit 3. ITEMCOUNT und itemcount addieren 2 zu derselben Variablen. Gemischt geschriebene Schlüsselwörter funktionieren. Main liefert 5, ohne zusätzliche Variablen anzulegen.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: file / subrutine / LineComment / SYMBOL
Runtime/BasicSyntaxPreprocessor.cs: Process
Runtime/InjectionRuntime.cs: Prepare / Load / CallSubrutineValues
Runtime/SemanticScope.cs: Scope
https://learn.microsoft.com/en-us/dotnet/visual-basic/reference/language-specification/introduction (comparison of identifier casing only)
-->
