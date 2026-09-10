# Include

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Include lädt eine weitere Quelldatei vor Analyse und Ausführung. Funktionen und Variablen werden verfügbar; Prozeduren oder Threads starten dadurch nicht automatisch.

## Genaue Syntax

```text
Include "fileName"
```

## Parameter

- `fileName` — fileName: nicht leerer Dateiname in einfachen oder doppelten Anführungszeichen. Relativer oder absoluter wörtlicher Pfad, keine Variable und kein Ausdruck. Beliebige Erweiterung; Inhalt muss vom Interpreter unterstützter Quelltext sein.

## Rückgabewert

Kein Rückgabewert: Anweisung zur Quellvorbereitung. Include(...) nicht zuweisen und kein ID, TRUE/FALSE oder 1/0 erwarten. Eingebundene Funktionen liefern eigene Werte mit RETURN.

## Verhalten

- Include auf eigener Zeile außerhalb SUB/FUNCTION. Suche neben der einbindenden Datei, danach in deren Include-Unterordner. Verschachtelte Pfade beziehen sich auf die aktuelle Bibliothek. Hauptdatei vor relativen Pfaden speichern.
- Jeder vollständige Pfad wird einmal eingebunden. Zyklus A → B → A ergibt SC016. Pfad-, Zugriffs- und Syntaxfehler verhindern den Start vor globalen Initialisierungen. Diagnose und Debugger behalten Originaldatei und Zeile.
- Zeichenketten und SUB/FUNCTION in derselben Datei schließen. Erneute Deklaration einer globalen Variable oder Konstante erzeugt SC017 vor dem Start.
- Der nächste Start liest geänderte Bibliotheken; vorbereitete oder laufende Skripte behalten ihren Quellstand. Keine Profilübernahme und kein Start anderer Skripte.
- Jede Datei darf Option Explicit vor eigenen Deklarationen setzen, sonst gilt die Hauptdatei. Deklarationen teilen einen Namensraum; Module entstehen nicht automatisch.
- UTF-8 mit BOM-Erkennung. Grenzen: 128 Dateien einschließlich Hauptdatei, 32 Ebenen, 16.777.216 Quellzeichen. Include in Kommentaren oder Zeichenketten lädt nichts.
- Jedes Beispiel hat einen eigenen Ordner. Main.bas und alle gezeigten Dateien mit exakten Namen und Unterordnern speichern. Fertige Gruppen: API Manual/Examples/Basic.Include/1, /2, /3. Main.bas ausführen, Dateien nicht zusammenfügen.

## Beispiele

### 1. Gemeinsame Funktion

```vb
# Main.bas bindet Common.bas ein und ruft Add(4, 7) auf. left und right werden als Werte übergeben; Add liefert die Summe, Main Integer 11. Common.bas startet nicht allein.
Option Explicit On
Include "Common.bas"
SUB Main()
    RETURN Add(4, 7)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Main.bas bindet Common.bas ein und ruft Add(4, 7) auf. left und right werden als Werte übergeben; Add liefert die Summe, Main Integer 11. Common.bas startet nicht allein.

**Common.bas**

```vbnet
Option Explicit On
FUNCTION Add(ByVal left, ByVal right)
    RETURN left + right
END FUNCTION
```

### 2. Verschachtelte Bibliothek

```vb
# Main.bas bindet lib/Route.bas ein, diese Math.bas aus ihrem lib-Ordner. Distance(-3, 5) übergibt dx=-3, dy=5 an Manhattan; Abs entfernt Vorzeichen, Summe Integer 8. Keine Spielfigurbewegung.
Option Explicit On
Include "lib/Route.bas"
SUB Main()
    RETURN Distance(-3, 5)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Main.bas bindet lib/Route.bas ein, diese Math.bas aus ihrem lib-Ordner. Distance(-3, 5) übergibt dx=-3, dy=5 an Manhattan; Abs entfernt Vorzeichen, Summe Integer 8. Keine Spielfigurbewegung.

**lib/Route.bas**

```vbnet
Option Explicit On
Include "Math.bas"
FUNCTION Distance(ByVal dx, ByVal dy)
    RETURN Manhattan(dx, dy)
END FUNCTION
```

**lib/Math.bas**

```vbnet
Option Explicit On
FUNCTION Manhattan(ByVal dx, ByVal dy)
    RETURN Abs(dx) + Abs(dy)
END FUNCTION
```

### 3. Wiederholtes Einbinden

```vb
# Common.bas und ./Common.bas bezeichnen dieselbe Datei: CONST und Funktion werden einmal deklariert. SharedValue=7; GetShared() liefert 7, Main multipliziert mit 2 und liefert Integer 14. Beide Dateien verwenden Option Explicit On.
Option Explicit On
Include "Common.bas"
Include "./Common.bas"
SUB Main()
    RETURN GetShared() * 2
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Common.bas und ./Common.bas bezeichnen dieselbe Datei: CONST und Funktion werden einmal deklariert. SharedValue=7; GetShared() liefert 7, Main multipliziert mit 2 und liefert Integer 14. Beide Dateien verwenden Option Explicit On.

**Common.bas**

```vbnet
Option Explicit On
CONST SharedValue = 7
FUNCTION GetShared()
    RETURN SharedValue
END FUNCTION
```

<!-- implementation references (not callable script procedures):
Parsing/ScriptSourceGraph.cs: Load / Builder.AddInclude / ResolveLine
Runtime/InjectionRuntime.cs: Prepare / Load
Runtime/Interpreter.cs: Location / EvaluateInitializer / CallObserved
Analysis/SanityAnalyzer.cs: Analyze
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: PrepareScriptForExecution
InjectionScript.Lsp/Workspace.cs: UpdateDiagnostic
-->
