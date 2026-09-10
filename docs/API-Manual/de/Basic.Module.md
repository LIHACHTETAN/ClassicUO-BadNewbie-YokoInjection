# Module / End Module

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Module fasst Funktionen, Prozeduren, VAR/DIM und CONST unter einem Namen zusammen. Von außen gelten Tools.Sum oder Counter.count; im eigenen Modul sind kurze Mitgliedsnamen möglich.

## Genaue Syntax

```text
Module moduleName
    members
End Module
moduleName.member(arguments)
moduleName.field
```

## Parameter

- `moduleName` — moduleName: einfacher Bezeichner ohne Unterscheidung der Großschreibung, etwa Tools. UO ist reserviert. Doppelte Modulnamen und verschachtelte Module sind unzulässig.
- `members` — members: SUB/FUNCTION, skalare VAR/DIM, CONST, Include und eine gültige Option-Explicit-Direktive. Felder können Array- oder Objektwerte enthalten. DIM[...] direkt im Modul wird nicht unterstützt; Array per Funktion erstellen und in VAR speichern.
- `member / arguments` — member / arguments: Mitgliedsname und Funktionsargumente. Tools.Sum(2, 3) übergibt left=2 und right=3. Counter.count als Feld benötigt keine Klammern.

## Rückgabewert

Module selbst liefert keinen Wert und ist kein Aufruf Module(...). Tools.Sum(...) liefert den RETURN-Wert der Funktion, ein Feld seinen gespeicherten Wert. Vergleiche liefern Integer 1/0 entsprechend TRUE/FALSE in Bedingungen und Vergleichen. Eine beliebige Zahl, ID oder Menge ist nicht automatisch ein boolesches Ergebnis.

## Verhalten

- Module auf Dateiebene mit End Module abschließen. Include kann ein Modul oder seine Mitglieder laden; Fehler behalten Originaldatei und Zeile. Option Explicit gilt für die physische Datei.
- Die Vorbereitung erfasst vollständige Namen, bindet kurze Verweise an das aktuelle Modul und prüft Zugriffe vor dem Start. Explizite lokale Parameter, VAR, CONST oder DIM verdecken gleichnamige Felder. Sonst wird zuerst im Modul, dann unter normalen globalen Variablen gesucht.
- Felder werden zu Beginn jedes einzelnen Laufs in Deklarationsreihenfolge initialisiert. Verschachtelte Aufrufe dieses Laufs teilen Änderungen. Ein neuer Lauf beginnt neu; parallele Skripte teilen keinen Modulzustand. Keine Speicherung auf Datenträger.
- Funktionen/Prozeduren sind standardmäßig Public, Felder/Konstanten Private. Private benötigt Module. Siehe Public / Private.
- Die IDE zeigt vollständige Prozedurnamen. Öffentliche Prozeduren ohne Pflichtargumente lassen sich aus der Liste starten; private Helfer bleiben intern. Ergänzung, Navigation und Variablenanzeige beachten das aktuelle Modul.

## Beispiele

### 1. Gleiche Namen in verschiedenen Modulen

```vb
# Tools.Sum addiert left=2 und right=3 zu 5. Other.Sum multipliziert sie zu 6. Vollständige Namen unterscheiden die Funktionen; Main liefert Integer 11.
Option Explicit On
Module Tools
    Public Function Sum(ByVal left, ByVal right)
        Return left + right
    End Function
End Module
Module Other
    Public Function Sum(ByVal left, ByVal right)
        Return left * right
    End Function
End Module
Sub Main()
    Return Tools.Sum(2, 3) + Other.Sum(2, 3)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

Tools.Sum addiert left=2 und right=3 zu 5. Other.Sum multipliziert sie zu 6. Vollständige Namen unterscheiden die Funktionen; Main liefert Integer 11.

### 2. Geteiltes Feld eines Laufs

```vb
# count beginnt bei 0. Jeder Increment-Aufruf erhöht dasselbe Feld um 1; zwei Aufrufe ergeben before=2. Read sieht Counter.count=5. Main liefert 2*10+5, Integer 25. Der nächste Lauf beginnt wieder bei 0.
Option Explicit On
Module Counter
    Public Var count As Integer = 0
    Public Sub Increment()
        count += 1
    End Sub
    Public Function Read()
        Return count
    End Function
End Module
Sub Main()
    Counter.Increment()
    Counter.Increment()
    Var before = Counter.Read()
    Counter.count = 5
    Return before * 10 + Counter.Read()
End Sub
```

**Erläuterung der Parameter und Ausführung:**

count beginnt bei 0. Jeder Increment-Aufruf erhöht dasselbe Feld um 1; zwei Aufrufe ergeben before=2. Read sieht Counter.count=5. Main liefert 2*10+5, Integer 25. Der nächste Lauf beginnt wieder bei 0.

### 3. Boolesches Ergebnis

```vb
# maximum=4 ist in Limits verfügbar. Allowed(3) liefert Integer 1, Allowed(7) Integer 0. accepted=TRUE und rejected=FALSE prüfen diese Werte. Bei Erfolg liefert Main Integer 10.
Option Explicit On
Module Limits
    Private Const maximum = 4
    Public Function Allowed(ByVal amount)
        Return amount <= maximum
    End Function
End Module
Sub Main()
    Var accepted = Limits.Allowed(3)
    Var rejected = Limits.Allowed(7)
    If accepted = TRUE AndAlso rejected = FALSE Then
        Return 10
    End If
    Return 0
End Sub
```

**Erläuterung der Parameter und Ausführung:**

maximum=4 ist in Limits verfügbar. Allowed(3) liefert Integer 1, Allowed(7) Integer 0. accepted=TRUE und rejected=FALSE prüfen diese Werte. Bei Erfolg liefert Main Integer 10.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: moduleDeclaration / moduleSection
Runtime/DeclarationScope.cs: Qualify / IsPrivate
Runtime/ScriptBindings.cs: Builder.Variable / CallName
Runtime/SemanticScope.cs: Scope / DefineGlobalVariables
Runtime/Interpreter.cs: EvaluateBoundExpression / CallSubrutine
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/module-statement
-->
