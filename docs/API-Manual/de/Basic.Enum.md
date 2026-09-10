# Enum / End Enum

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Enum fasst benannte Integer-Konstanten für Skriptzustände zusammen. Die Deklaration steht auf Datei- oder Module-Ebene, außerhalb von Sub/Function. Unterstützt wird eine Teilmenge von VB.NET, kein .NET-Enum-Objekt.

## Genaue Syntax

```text
[Public | Private] Enum name [As Integer]
    member [= constantExpression]
    ...
End Enum
Dim state As name = name.member
ModuleName.name.member
```

## Parameter

- `Public / Private` — Public ist der Standard, auch im Module. Private ist nur im Module zulässig und verbirgt Typ und Mitglieder vor anderen Modulen und der Dateiebene.
- `name` — Ein einfacher Name ohne Punkte, etwa Mode; Großschreibung ist unerheblich. UO und eingebaute Typnamen sind reserviert. Der vollständige Name darf keinen Enum-, Module- oder globalen Variablennamen wiederholen.
- `As Integer` — Optional; nur vorzeichenbehafteter 32-Bit-Integer, -2147483648..2147483647. Andere Basistypen werden abgelehnt. As Mode bei Variablen, Parametern oder Function-Ergebnissen verwendet normale Integer-Speicherung und Konvertierung; Werte müssen nicht in der Mitgliederliste stehen. Ohne Initialisierung gilt 0.
- `member` — Ein einfacher Mitgliedsname je Zeile, mindestens einer. Doppelte Namen sowie True und False sind unzulässig. Ohne Ausdruck beginnt die Reihe bei 0 und erhöht den vorherigen Wert um 1. Verschiedene Namen dürfen denselben Wert haben.
- `constantExpression` — Optionaler konstanter Ausdruck: dezimale/0x-Ganzzahlen, Klammern, unäres Minus, + - * / Mod, frühere Mitglieder und bereits deklarierte numerische Const. Endwerte müssen ganze Zahlen im Bereich sein; Zwischenquotienten dürfen Brüche sein. Referenzierte Const müssen ebenfalls Integer ergeben, untypisiert oder As Integer/Long/Short/Byte. Keine Aufrufe, Variablen, Strings, Vergleiche oder Arrayzugriffe. Vorwärtsverweise, Zyklen und Abhängigkeiten über 128 Ebenen werden abgelehnt.
- `name.member` — Zugriff mit Mode.Ready, außerhalb des Moduls mit Tools.Mode.Ready. In Tools genügt Mode.Ready; With Mode erlaubt .Ready. Zuweisung, += und ByRef-Rückschreiben dürfen die Konstanten nicht ändern. Enum ist keine aufrufbare Funktion.

## Rückgabewert

Die Deklaration liefert keinen Wert und braucht keine Aufrufklammern. Ein Mitglied liefert Integer, etwa Mode.Working = 3, keinen automatischen Erfolgsstatus. state = Mode.Finished ist dagegen ein Boolean-Vergleich: 1/True oder 0/False, beide Schreibweisen sind möglich. Der Zustandswert 0 kann Idle statt Fehler bedeuten.

## Verhalten

- EnumCatalog berechnet bei der Vorbereitung frühere Konstanten ohne Skript/API-Ausführung, vergibt automatische Werte und prüft Namen, Zugriff und Grenzen. SC026 blockiert den Start auch ohne Option Explicit. Syntaxfehler verhindern ebenfalls die Ausführung; unvollständige Eingaben liefern Diagnosen.
- DefinitionCollector installiert konstante Mitglieder vor globalen Initialisierern und Optional-Standardwerten; diese dürfen später deklarierte Enums verwenden. Innerhalb eines Enum gelten weiterhin nur frühere Konstanten. Vorbereitete Skripte speichern den Katalog, ein neues Skript ersetzt ihn.
- ScriptBindings löst Modulnamen und Private einmal auf. Ausführung liest Konstanten ohne Neuberechnung in Schleifen oder Reflection. As Mode wird Integer; der Debugger kann Integer anzeigen. Include darf Enums liefern. Keine Flags-Attribute, System.Enum-Methoden, impliziten Mitgliedimporte oder automatische Mitgliederliste.

## Beispiele

### 1. Zustände benennen

```vb
# Idle=0 und Queued=1 entstehen automatisch. Working=10 setzt die Folge neu, Finished=11. state As TaskState erhält 10. Main liefert String "0:1:10:11"; CStr formatiert die Zahlen. Namen können an eigene Zustände angepasst werden, die Deklaration startet nichts.
Option Explicit On
Enum TaskState As Integer
    Idle
    Queued
    Working = 10
    Finished
End Enum

Sub Main()
    Dim state As TaskState = TaskState.Working
    Return CStr(TaskState.Idle) & ":" & CStr(TaskState.Queued) & ":" & CStr(state) & ":" & CStr(TaskState.Finished)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

Idle=0 und Queued=1 entstehen automatisch. Working=10 setzt die Folge neu, Finished=11. state As TaskState erhält 10. Main liefert String "0:1:10:11"; CStr formatiert die Zahlen. Namen können an eigene Zustände angepasst werden, die Deklaration startet nichts.

### 2. Modulzustand verbergen

```vb
# Controller.Mode ist nur intern sichtbar. NextMode erhält distance ByVal As Integer, ohne das Aufrufargument zu ändern. distance<=1 wählt Arrived=5, sonst Walking=4; state beginnt bei 0. Main übergibt 3 und 1, erhält 4 und 5 und liefert Integer 45. Dies bewegt keinen Charakter; distance ist eine Beispieleingabe. Außen ist Controller.NextMode erlaubt, Controller.Mode.Arrived nicht.
Option Explicit On
Module Controller
    Private Enum Mode
        Idle
        Walking = 4
        Arrived
    End Enum

    Public Function NextMode(ByVal distance As Integer) As Integer
        Dim state As Mode
        If distance <= 1 Then
            state = Mode.Arrived
        Else
            state = Mode.Walking
        End If
        Return state
    End Function
End Module

Sub Main()
    Dim farState = Controller.NextMode(3)
    Dim nearState = Controller.NextMode(1)
    Return farState * 10 + nearState
End Sub
```

**Erläuterung der Parameter und Ausführung:**

Controller.Mode ist nur intern sichtbar. NextMode erhält distance ByVal As Integer, ohne das Aufrufargument zu ändern. distance<=1 wählt Arrived=5, sonst Walking=4; state beginnt bei 0. Main übergibt 3 und 1, erhält 4 und 5 und liefert Integer 45. Dies bewegt keinen Charakter; distance ist eine Beispieleingabe. Außen ist Controller.NextMode erlaubt, Controller.Mode.Arrived nicht.

### 3. Zustand wechseln und Boolean liefern

```vb
# Die frühere Integer-Const FirstState=2 ergibt Idle=2, Working=3, Finished=4. Advance verändert state in Main per ByRef; With Mode kürzt Namen ab, Select Case wählt den Übergang. Zwei Aufrufe ergeben 2→3→4. IsFinal erhält eine ByVal-Kopie und vergleicht mit Finished: Main liefert 1/True, nach nur einem Übergang wäre es 0/False. Ein weiterer Advance wirft "No next state"; Enum-Konstanten bleiben unverändert.
Option Explicit On
Const FirstState As Integer = 2
Enum Mode
    Idle = FirstState
    Working = Idle + 1
    Finished
End Enum

Sub Advance(ByRef state As Mode)
    With Mode
        Select Case state
            Case .Idle
                state = .Working
            Case .Working
                state = .Finished
            Case Else
                Throw "No next state"
        End Select
    End With
End Sub

Function IsFinal(ByVal state As Mode) As Boolean
    Return state = Mode.Finished
End Function

Sub Main()
    Dim state As Mode = Mode.Idle
    Advance(state)
    Advance(state)
    Return IsFinal(state)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

Die frühere Integer-Const FirstState=2 ergibt Idle=2, Working=3, Finished=4. Advance verändert state in Main per ByRef; With Mode kürzt Namen ab, Select Case wählt den Übergang. Zwei Aufrufe ergeben 2→3→4. IsFinal erhält eine ByVal-Kopie und vergleicht mit Finished: Main liefert 1/True, nach nur einem Übergang wäre es 0/False. Ein weiterer Advance wirft "No next state"; Enum-Konstanten bleiben unverändert.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: enumDeclaration / enumMember
Runtime/EnumCatalog.cs: Build / Observe / Reference / Evaluate
Runtime/DefinitionCollector.cs: VisitFile / VisitEnumDeclaration
Runtime/ScriptBindings.cs: Variable / VisitTypeClause / VisitWithStatement
Runtime/SemanticScope.cs: DefineGlobalVariables / SetVar
Runtime/Metadata.cs: NormalizeType
-->
