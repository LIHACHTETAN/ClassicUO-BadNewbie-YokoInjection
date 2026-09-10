# Wait Until / Timeout

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Wait Until prüft eine Bedingung bis zum Erfolg oder Zeitablauf. Es ist eine Basic-Erweiterung, keine VB.NET-Anweisung. Sie läuft im aktuellen Skript ohne neuen Thread oder weiteren Prozedurstart.

## Genaue Syntax

```text
Wait Until condition Timeout milliseconds
```

## Parameter

- `condition` — condition wird sofort und danach zwischen kurzen Wartephasen ausgewertet. Verwenden Sie Boolean oder einen Vergleich: numerische 0 ist false; andere Werte folgen den If-Regeln. Der String "false" ist kein Boolean false. UO-Aufrufe und eigene Hilfsfunktionen sind möglich; Fehler werden weitergegeben, Seiteneffekte wiederholen sich bei jeder Prüfung.
- `Timeout milliseconds` — Timeout ist erforderlich. milliseconds wird einmal vor der ersten Prüfung ausgewertet und muss Integer 0..2147483647 sein. Negative Werte, Brüche und Strings erzeugen vorher einen Fehler. Null erlaubt nur die sofortige Prüfung. Außerhalb dieser Markierung bleibt timeout ein zulässiger Variablenname.

## Rückgabewert

Die Anweisung liefert keinen Wert. Erfolg setzt das Skript in der nächsten Zeile fort; Zeitablauf erzeugt einen Fehler mit Datei und Zeile. Try/Catch oder On Error können ihn behandeln; sonst scheitert der aktuelle Lauf. Es gibt kein automatisches false. Beispiel 2 erstellt ausdrücklich einen Wrapper mit True/1 oder False/0.

## Verhalten

- Der Interpreter speichert die Dauer und startet eine monotone Stopwatch. Die erste Prüfung erfolgt sofort und darf auch bei Limit 0 erfolgreich sein. Nach false prüft die Schleife Abbruch und Pause, berechnet die Restzeit und wartet höchstens 10 ms vor der nächsten Prüfung. Das vermeidet eine aktive Dauerschleife; die Betriebssystemplanung kann Intervalle verlängern.
- Pause unterbricht die Prüfungen, reale verstrichene Zeit zählt aber zum Limit. Beim Fortsetzen wird ein abgelaufenes Limit vor der nächsten Prüfung gemeldet. Stopp unterbricht das Warten und überspringt Skript-Catch/Finally wie andere Notabbrüche. Ein blockierender Aufruf in condition kann nicht zwangsweise unterbrochen werden: Hilfsfunktionen kurz halten. Eine begonnene Prüfung endet vor der Verarbeitung ihres Ergebnisses oder Fehlers.
- Bedingungsfehler bleiben erhalten und werden nicht als Timeout umgedeutet. Normale Fehler und Timeouts führen die zuständigen Finally-Blöcke aus. Variablen gehören zum aktuellen Aufruf; erneuter Eintritt startet eine neue Frist. End Wait und ein zusätzlicher Intervallparameter existieren nicht. Wait(milliseconds) bleibt eine getrennte Verzögerungsfunktion.

## Beispiele

### 1. Eine Hilfsfunktion mit Zeitbudget prüfen

```vb
# checks beginnt bei 0 und wird von Ready per ByRef bei jeder Prüfung erhöht. required=3 wird ByVal übergeben; budget=5000 erlaubt bis zu fünf Sekunden. Zwei Prüfungen ergeben false, die dritte true; Main liefert Integer 3. Dies zeigt deterministisches Abfragen ohne Server-Simulation; ersetzen Sie die Bedingung durch die benötigte Zustandsprüfung.
Option Explicit On
Function Ready(ByRef checks As Integer, ByVal required As Integer) As Boolean
    checks += 1
    Return checks >= required
End Function

Sub Main()
    Dim checks As Integer = 0
    Const budget = 5000
    Wait Until Ready(checks, 3) Timeout budget
    Return checks
End Sub
```

**Erläuterung der Parameter und Ausführung:**

checks beginnt bei 0 und wird von Ready per ByRef bei jeder Prüfung erhöht. required=3 wird ByVal übergeben; budget=5000 erlaubt bis zu fünf Sekunden. Zwei Prüfungen ergeben false, die dritte true; Main liefert Integer 3. Dies zeigt deterministisches Abfragen ohne Server-Simulation; ersetzen Sie die Bedingung durch die benötigte Zustandsprüfung.

### 2. Einen eigenen Boolean-Wrapper erstellen

```vb
# TryWait erhält ready=False und budget=0. Die sofortige Prüfung scheitert mit Timeout. Catch problem gibt False zurück; Main liefert 0, vergleichbar mit False. ready=True ergäbe 1/True. Der Wrapper fängt alle Ausführungsfehler: problem auswerten, falls Unterscheidung nötig ist. ready ist hier ein Boolean-Wert, kein Callback.
Option Explicit On
Function TryWait(ByVal ready As Boolean, ByVal budget As Integer) As Boolean
    Try
        Wait Until ready Timeout budget
        Return True
    Catch problem
        Return False
    End Try
End Function

Sub Main()
    Dim success = TryWait(False, 0)
    Return success
End Sub
```

**Erläuterung der Parameter und Ausführung:**

TryWait erhält ready=False und budget=0. Die sofortige Prüfung scheitert mit Timeout. Catch problem gibt False zurück; Main liefert 0, vergleichbar mit False. ready=True ergäbe 1/True. Der Wrapper fängt alle Ausführungsfehler: problem auswerten, falls Unterscheidung nötig ist. ready ist hier ein Boolean-Wert, kein Callback.

### 3. Bedingungsfehler erhalten und abschließen

```vb
# CheckStatus mit state=-1 wirft sofort "disconnected". Das 3000-ms-Limit ersetzt diesen Fehler nicht. Catch kopiert problem nach message; Finally setzt finished=True/1. Main liefert "disconnected:1". state=1 wäre sofort erfolgreich, state=0 bliebe bis zum Timeout false. Keine Spielverbindung ist erforderlich.
Option Explicit On
Function CheckStatus(ByVal state As Integer) As Boolean
    If state < 0 Then
        Throw "disconnected"
    End If
    Return state = 1
End Function

Sub Main()
    Dim message = ""
    Dim finished = False
    Try
        Wait Until CheckStatus(-1) Timeout 3000
    Catch problem
        message = problem
    Finally
        finished = True
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

CheckStatus mit state=-1 wirft sofort "disconnected". Das 3000-ms-Limit ersetzt diesen Fehler nicht. Catch kopiert problem nach message; Finally setzt finished=True/1. Main liefert "disconnected:1". state=1 wäre sofort erfolgreich, state=0 bliebe bis zum Timeout false. Keine Spielverbindung ist erforderlich.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: waitUntilStatement / WAIT_UNTIL
Analysis/LoopStructureValidator.cs: VisitWaitUntilStatement
Runtime/Interpreter.cs: VisitWaitUntilStatement / Failure
Runtime/InjectionRuntime.cs: executionCheckpoint / retrieveCancellationToken
-->
