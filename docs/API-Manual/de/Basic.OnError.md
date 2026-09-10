# On Error / Resume

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

On Error bestimmt die Behandlung folgender Laufzeitfehler im aktuellen Prozedur- oder Funktionsaufruf. Es ist eine Sprachanweisung, kein API-Aufruf. Für strukturierte Behandlung und Abschluss dient Try/Catch/Finally.

## Genaue Syntax

```text
On Error GoTo label
On Error Resume Next
On Error GoTo 0
label:
Resume
Resume Next
```

## Parameter

- `label` — Vorhandene Marke derselben Prozedur, als label: auf eigener Zeile. Vor oder hinter On Error, ohne Beachtung der Großschreibung. Kein Funktionsname, Textliteral oder Zeilennummer. Unbekannte Marken erzeugen SC009; der Client blockiert das Skript.
- `Resume Next / On Error` — On Error Resume Next setzt automatisch nach der fehlgeschlagenen Anweisung fort, ohne Markensprung. Erfolgreiche Anweisungen bleiben unverändert. Gilt für den aktuellen Aufruf, nicht für alle Skripte.
- `0` — On Error GoTo 0 schaltet den Modus aus. Null ist ein Steuerwert, keine Marke und kein Boolean-Ergebnis. Andere numerische Marken und GoTo -1 sind nicht unterstützt.
- `Resume / Resume Next` — Im Handler wiederholt Resume die fehlgeschlagene Anweisung; Resume Next setzt dahinter fort. Ein gespeicherter Fehler ist erforderlich; seine Adresse wird danach gelöscht. Keine Marke oder Zeitlimit als Argument.

## Rückgabewert

On Error und Resume liefern keinen Wert. Ein behandelter Fehler wird nicht zu TRUE/FALSE und repariert keine Zuweisung automatisch. Beispiele liefern ausdrücklich Integer 5,18,10. Vorherige Seiteneffekte werden nicht automatisch zurückgerollt.

## Verhalten

- Die Vorbereitung löst Marken nach der gesamten Prozedur auf, in beide Richtungen. Zur Laufzeit wird der Modus gespeichert; bei Fehlern kommt strukturierte Try-Behandlung vor On Error.
- Die fehlgeschlagene Anweisungsadresse wird gespeichert. Markenmodus springt zum Handler, automatisches Resume Next dahinter. Resume wertet Ausdrücke und Aufrufe erneut aus: zuerst die Ursache beheben und wiederholte Effekte beachten.
- GoTo 0 löscht die gespeicherte Fehleradresse nicht. Der Handler kann sich deaktivieren, Daten reparieren und Resume ausführen. Vor fehleranfälliger Handler-Arbeit deaktivieren, um Wiedereintritt zu vermeiden.
- Syntaxfehler und Abbruch werden nicht behandelt. Liefert ein Befehl lediglich 0, FALSE oder einen Fehlerstatus ohne Ausnahme, wird On Error nicht aufgerufen; Ergebnis prüfen.
- Normalen Ablauf mit Return oder GoTo vom Handler fernhalten. Aufgerufene Prozeduren haben eigenen Zustand; unbehandelte Fehler können zum Aufrufer gelangen. Resume wiederholt dort den gesamten Aufruf, keine interne Zeile. Keine automatische Versuchszahl oder Wartezeit.
- Erreicht ein Fehler nach der Bereinigung von Try einen äußeren On Error GoTo-Handler, wiederholt Resume den gesamten Try-Block ab dem Kopf. Resume Next und On Error Resume Next setzen bei der ersten Anweisung nach End Try fort. Bereits ausgeführte Aktionen können sich wiederholen; ein abgewickelter Block wird nicht mitten im Rumpf betreten.

## Beispiele

### 1. Eine fehlgeschlagene Zuweisung überspringen

```vb
# values[0] hat eine Zelle; Index 5 ist ungültig. result=1. On Error Resume Next überspringt den Leseversuch vor der Zuweisung, daher bleibt 1. GoTo 0 schaltet aus; result+=4 ergibt 5. Main liefert 5, nicht den Erfolg des Leseversuchs.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 1
    On Error Resume Next
    result = values[5]
    On Error GoTo 0
    result += 4
    Return result
End Sub
```

**Erläuterung der Parameter und Ausführung:**

values[0] hat eine Zelle; Index 5 ist ungültig. result=1. On Error Resume Next überspringt den Leseversuch vor der Zuweisung, daher bleibt 1. GoTo 0 schaltet aus; result+=4 ergibt 5. Main liefert 5, nicht den Erfolg des Leseversuchs.

### 2. Reparieren und wiederholen

```vb
# ReadCell speichert 8 in Zelle 0, startet aber index=2. Der Fehler springt zu FixIndex. GoTo 0 deaktiviert; handled=1, index=0. Resume wiederholt result=values[index] und speichert jetzt 8. Return verhindert den normalen Eintritt in den Handler. Main erhält 18.
Option Explicit On
Function ReadCell()
    Dim values[0]
    values[0] = 8
    Var index = 2
    Var handled = 0
    Var result = 0
    On Error GoTo FixIndex
    result = values[index]
    Return handled * 10 + result
FixIndex:
    On Error GoTo 0
    handled += 1
    index = 0
    Resume
End Function
Sub Main()
    Return ReadCell()
End Sub
```

**Erläuterung der Parameter und Ausführung:**

ReadCell speichert 8 in Zelle 0, startet aber index=2. Der Fehler springt zu FixIndex. GoTo 0 deaktiviert; handled=1, index=0. Resume wiederholt result=values[index] und speichert jetzt 8. Return verhindert den normalen Eintritt in den Handler. Main erhält 18.

### 3. Handler vor seiner Registrierung

```vb
# GoTo Work überspringt Failed beim normalen Eintritt. On Error GoTo Failed aktiviert die frühere Marke. Index 2 scheitert vor Änderung von result. Der Handler deaktiviert sich, erhöht handled und erreicht Return über Resume Next. Ergebnis 10; Marken sind keine Prozeduren.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 0
    Var handled = 0
    GoTo Work
Failed:
    On Error GoTo 0
    handled += 1
    Resume Next
Work:
    On Error GoTo Failed
    result = values[2]
    Return handled * 10 + result
End Sub
```

**Erläuterung der Parameter und Ausführung:**

GoTo Work überspringt Failed beim normalen Eintritt. On Error GoTo Failed aktiviert die frühere Marke. Index 2 scheitert vor Änderung von result. Der Handler deaktiviert sich, erhöht handled und erreicht Return über Resume Next. Ergebnis 10; Marken sind keine Prozeduren.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: onError / resume / label
Analysis/InvalidSymbolVisitor.cs: VisitOnError / ValidateLabelReference
Runtime/Instructions/Generator.cs: VisitSubrutine / errorHandlers
Runtime/Instructions/ErrorHandlingInstruction.cs
Runtime/Interpreter.cs: TryHandleStructuredError / TryHandleError / ResumeInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/on-error-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/resume-statement
-->
