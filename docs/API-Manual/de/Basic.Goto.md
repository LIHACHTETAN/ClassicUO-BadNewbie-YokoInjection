# GoTo / label:

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

GoTo springt zu einer benannten Marke in der aktuellen Prozedur oder Funktion. Eine Marke bezeichnet eine Codestelle, keine aufrufbare Prozedur. Für normalen Kontrollfluss eignen sich If, Schleifen und Return.

## Genaue Syntax

```text
GoTo label
label:
```

## Parameter

- `label` — Bezeichner, der als label: in einer eigenen Zeile derselben Prozedur steht. GoTo label ohne Anführungszeichen, Klammern oder Doppelpunkt nach dem Ziel schreiben. Vorwärts- und Rückwärtssprünge funktionieren ohne Beachtung der Großschreibung. Andere Prozeduren dürfen denselben Markennamen haben. Punkte sind erlaubt, machen daraus aber kein Modulmitglied. Zahlen, berechnete Ausdrücke und Marken anderer Prozeduren werden als Ziele nicht unterstützt.

## Rückgabewert

GoTo und label: liefern keinen Wert, auch kein 1/0 oder TRUE/FALSE. Die Beispiele liefern mit Return aus Main die selbst berechneten Integer -1, 6 und 123.

## Verhalten

- Die Vorbereitung speichert Markenadressen und löst Sprünge nach dem Lesen der gesamten Prozedur auf. Die Ausführung nutzt die fertige Adresse ohne erneute Textsuche. Variablenwerte bleiben erhalten; frühere Aktionen werden nicht rückgängig gemacht.
- Unbekanntes Ziel: SC009, der Client verhindert den Start. Doppelte Marke innerhalb einer Prozedur, auch bei anderer Großschreibung: SC021 vor der Initialisierung. Include behält ursprüngliche Datei und Fehlerzeile. Überzählige Zeichen können Warnungen auslösen; genaue Syntax verwenden.
- Beim Verlassen aktiver Try-Blöcke laufen deren Finally-Blöcke von innen nach außen vor dem Ziel. Ein Sprung innerhalb desselben aktiven Try erhält den Block. Ein Fehler in Finally kann das Erreichen des Ziels verhindern.
- Schleifen und Try/Catch/Finally über ihren normalen Anfang betreten. Ein Sprung in die Mitte stellt übersprungene Initialisierung und Laufzeitkontexte nicht wieder her und ist keine unterstützte Fortsetzung. Für Schleifen Continue oder Exit verwenden.
- Rückwärtssprünge haben weder automatische Versuchszahl noch Zeitlimit oder Wartezeit. Die Abbruchbedingung ausdrücklich ändern. Normaler Ablauf läuft ebenfalls durch Marken; unerwünschte Abschnitte überspringen oder Return verwenden. Fehlerbehandlung wird durch On Error eingerichtet.

## Beispiele

### 1. Vorwärts verzweigen

```vb
# amount=0 wählt NoItems und result=-1; anschließend liefert Finished den Wert -1. Bei amount=4 setzt der normale Pfad 40 und GoTo Finished überspringt NoItems. Beide Marken gehören zu Main und sind keine Aufrufe.
Option Explicit On
Sub Main()
    Var amount = 0
    Var result = 0
    If amount <= 0 Then
        GoTo NoItems
    End If
    result = amount * 10
    GoTo Finished
NoItems:
    result = -1
Finished:
    Return result
End Sub
```

**Erläuterung der Parameter und Ausführung:**

amount=0 wählt NoItems und result=-1; anschließend liefert Finished den Wert -1. Bei amount=4 setzt der normale Pfad 40 und GoTo Finished überspringt NoItems. Beide Marken gehören zu Main und sind keine Aufrufe.

### 2. Begrenzt wiederholen

```vb
# attempt beginnt bei 0 und steigt vor der Prüfung. Again und again bezeichnen dieselbe Marke. Drei Durchgänge addieren 1, 2 und 3; danach ist attempt<3 falsch und Return liefert 6. total wird vor der Marke initialisiert und beim Sprung nicht zurückgesetzt.
Option Explicit On
Sub Main()
    Var attempt = 0
    Var total = 0
Again:
    attempt += 1
    total += attempt
    If attempt < 3 Then
        GoTo again
    End If
    Return total
End Sub
```

**Erläuterung der Parameter und Ausführung:**

attempt beginnt bei 0 und steigt vor der Prüfung. Again und again bezeichnen dieselbe Marke. Drei Durchgänge addieren 1, 2 und 3; danach ist attempt<3 falsch und Return liefert 6. total wird vor der Marke initialisiert und beim Sprung nicht zurückgesetzt.

### 3. Verschachtelte Try verlassen

```vb
# trace wird 1; GoTo Finished überspringt trace=99. Das innere Finally hängt Ziffer 2 an, das äußere Ziffer 3. Erst dann wird Finished erreicht und 123 zurückgegeben. Jeder Finally-Block läuft für diesen Sprung einmal.
Option Explicit On
Sub Main()
    Var trace = 0
    Try
        Try
            trace = trace * 10 + 1
            GoTo Finished
            trace = 99
        Finally
            trace = trace * 10 + 2
        End Try
    Finally
        trace = trace * 10 + 3
    End Try
Finished:
    Return trace
End Sub
```

**Erläuterung der Parameter und Ausführung:**

trace wird 1; GoTo Finished überspringt trace=99. Das innere Finally hängt Ziffer 2 an, das äußere Ziffer 3. Erst dann wird Finished erreicht und 123 zurückgegeben. Jeder Finally-Block läuft für diesen Sprung einmal.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: goto / label / SYMBOL
Analysis/LabelStructureValidator.cs: VisitSubrutine / VisitLabel
Analysis/InvalidSymbolVisitor.cs: VisitGoto / ValidateLabelReference
Runtime/Instructions/Generator.cs: Generate / VisitSubrutine
Runtime/Interpreter.cs: GotoInstruction / Transfer / forScopes disposal
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/goto-statement
-->
