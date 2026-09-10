# Public / Private

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Public macht ein Modulmitglied von außen zugänglich. Private erlaubt nur Funktionen, Prozeduren und Initialisierern desselben Moduls den Zugriff. Der Modifikator steht vor der Deklaration, nicht vor dem Aufruf.

## Genaue Syntax

```text
Public declaration
Private declaration
```

## Parameter

- `visibility` — visibility: Public oder Private. Ohne Modifikator sind SUB/FUNCTION im Modul öffentlich und VAR/DIM/CONST privat.
- `declaration` — declaration: SUB/FUNCTION, skalare VAR/DIM oder CONST. Public ist auch für Module und Deklarationen auf Dateiebene möglich. Private ist auf Dateiebene und im Prozedurrumpf unzulässig. Mitgliedsnamen ohne Punkt deklarieren.

## Rückgabewert

Public und Private liefern keinen Wert und ändern weder Feldtyp noch Funktionsergebnis. Normalize(12) liefert per RETURN Integer 10; NextCount() liefert den neuen Zählerstand, nicht TRUE/FALSE.

## Verhalten

- Im Modul gelten kurze und vollständige Namen eigener Mitglieder. Externer Code greift nur auf Public über ModuleName.Member zu. Public erzeugt keinen kurzen globalen Namen.
- Prüfung vor dem Start, auch mit Option Explicit Off: fremdes Private ergibt SC019; ungültige Modul-/Modifikatordeklarationen ergeben SC018 oder Syntaxfehler. Danach laufen keine Initialisierer.
- Eine öffentliche Funktion darf private Helfer aufrufen. Entscheidend ist das Modul der aufrufenden Funktion, nicht ihr externer Auftraggeber. Private Helfer lassen sich nicht einzeln über IDE, Hotkey oder externe Prozedur-API starten.
- Public Const bleibt unveränderlich, Public Var veränderlich. Explizite lokale Variablen verdecken gleichnamige Felder nur in ihrer Prozedur. Private verschlüsselt den Quelltext nicht und verbirgt ihn nicht vor dem Eigentümer.
- Debugger-Kurznamen und Private-Zugriff beziehen sich auf den ausgewählten Aufrufrahmen. Innerhalb des Moduls ist das Feld zugänglich; im externen Aufrufer wird ModuleName.privateField abgewiesen.

## Beispiele

### 1. Öffentliche Funktion mit privatem Helfer

```vb
# value=12 gelangt zu Limits.Normalize und dann Clamp. maximum=10 begrenzt den Wert; beide liefern Integer 10. Main ruft nur Normalize auf. Ein externer Aufruf Limits.Clamp(12) ist verboten.
Option Explicit On
Module Limits
    Private Const maximum = 10
    Private Function Clamp(ByVal value)
        If value > maximum Then
            Return maximum
        End If
        Return value
    End Function
    Public Function Normalize(ByVal value)
        Return Clamp(value)
    End Function
End Module
Sub Main()
    Return Limits.Normalize(12)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

value=12 gelangt zu Limits.Normalize und dann Clamp. maximum=10 begrenzt den Wert; beide liefern Integer 10. Main ruft nur Normalize auf. Ein externer Aufruf Limits.Clamp(12) ist verboten.

### 2. Privates Feld und lokale Variable

```vb
# VAR value=7 ohne Modifikator ist privat in Store. Read liefert Feldwert 7. LocalValue besitzt eine eigene value=9 und ändert das Feld nicht. Main liefert 7*10+9, Integer 79.
Option Explicit On
Module Store
    Var value = 7
    Public Function Read()
        Return value
    End Function
    Public Function LocalValue()
        Var value = 9
        Return value
    End Function
End Module
Sub Main()
    Return Store.Read() * 10 + Store.LocalValue()
End Sub
```

**Erläuterung der Parameter und Ausführung:**

VAR value=7 ohne Modifikator ist privat in Store. Read liefert Feldwert 7. LocalValue besitzt eine eigene value=9 und ändert das Feld nicht. Main liefert 7*10+9, Integer 79.

### 3. Konstante öffentlich, Zähler privat

```vb
# Public Const increment=2 ist als Counter.increment lesbar. Private count beginnt bei 1. NextCount addiert increment, speichert und liefert 3. Main liefert 3*10+2, Integer 32. Externer Zugriff auf Counter.count und Änderungen an increment sind verboten.
Option Explicit On
Module Counter
    Public Const increment = 2
    Private Var count = 1
    Public Function NextCount()
        count += increment
        Return count
    End Function
End Module
Sub Main()
    Var result = Counter.NextCount()
    Return result * 10 + Counter.increment
End Sub
```

**Erläuterung der Parameter und Ausführung:**

Public Const increment=2 ist als Counter.increment lesbar. Private count beginnt bei 1. NextCount addiert increment, speichert und liefert 3. Main liefert 3*10+2, Integer 32. Externer Zugriff auf Counter.count und Änderungen an increment sind verboten.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: visibility / globalVar / globalConst / subrutine
Runtime/ScriptBindings.cs: CheckAccess / CheckDeclaration
Runtime/InjectionRuntime.cs: BlockingLanguageError / CallSubrutineValues
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: DiscoverScopedProcedures / RunProcedure
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/private
-->
