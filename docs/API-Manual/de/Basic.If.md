# IF / ELSEIF / ELSE / END IF

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

IF wählt höchstens einen Zweig: zuerst IF, dann ELSEIF bis zum ersten wahren Ergebnis, sonst das optionale ELSE. Danach geht es normalerweise nach END IF weiter.

## Genaue Syntax

```text
IF condition THEN
    statements
END IF
IF condition THEN
    statements
ELSEIF elseifCondition THEN
    statements
ELSE
    statements
END IF
```

## Parameter

- `condition` — condition: beim Eintritt einmal geprüfter Ausdruck. Numerische Null ist falsch, andere Zahlen wahr. Explizite Vergleiche oder boolesche API-Ergebnisse bevorzugen.
- `elseifCondition` — elseifCondition: optionale weitere Bedingung, nur nach falschen vorherigen Bedingungen ausgewertet. ELSEIF als ein Wort schreiben.
- `statements / ELSE` — statements / ELSE: Anweisungen auf Folgezeilen. ELSE ist optional, bedingungslos, einmalig und zuletzt. THEN und END IF sind Pflicht; mehrzeilige Blöcke verwenden.

## Rückgabewert

Kein Wert (Unit). IF ist eine Kontrollanweisung, keine Funktion. Bedingungen oder ausgewählte RETURN können Werte liefern. Boolesche 1/0 lassen sich mit TRUE/FALSE vergleichen; IF count akzeptiert jede Zahl außer null, IF count=TRUE nur 1.

## Verhalten

- Der Compiler erzeugt Bedingungs- und Ausgangssprünge. Falsch springt zur nächsten Bedingung oder ELSE; gewählte Zweige überspringen den Rest. Verschachtelte IF haben eigene ELSE. RETURN verlässt die Prozedur unter Ausführung umgebender FINALLY.
- Aus Kompatibilitätsgründen vergleicht IF mit numerischer Null statt alle Arten mit CBool umzuwandeln. Text "0", leerer Text, Arrays, Objekte und Unit wählen daher den wahren Zweig. Text ausdrücklich konvertieren oder Eigenschaften vergleichen. AndAlso/OrElse benötigen numerische Operanden.
- Deklarationen übersprungener Zweige erzeugen keine Laufzeitvariablen. Gemeinsame Ergebnisse vor IF initialisieren. Option Explicit prüft Namen, nicht Zuweisungen auf allen Wegen. Mehrere ELSE werden vor dem Start mit SC015 abgelehnt, auch ohne Option Explicit.

## Beispiele

### 1. Vier Fälle

```vb
# Classify(value) prüft <0, =0, <10, dann ELSE. -2, 0, 7, 20 liefern negative, zero, small, large. Main liefert "negative:zero:small:large"; jeder Aufruf führt ein RETURN aus.
Option Explicit On
FUNCTION Classify(value)
    IF value < 0 THEN
        RETURN "negative"
    ELSEIF value = 0 THEN
        RETURN "zero"
    ELSEIF value < 10 THEN
        RETURN "small"
    ELSE
        RETURN "large"
    END IF
END FUNCTION
SUB Main()
    RETURN Classify(-2) + ":" + Classify(0) + ":" + Classify(7) + ":" + Classify(20)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Classify(value) prüft <0, =0, <10, dann ELSE. -2, 0, 7, 20 liefern negative, zero, small, large. Main liefert "negative:zero:small:large"; jeder Aufruf führt ein RETURN aus.

### 2. Verschachtelte Entscheidungen

```vb
# Action(enabled, amount) prüft enabled, dann amount>0 für work oder idle. Das äußere ELSE liefert disabled. (TRUE,5), (TRUE,0), (FALSE,5) ergeben "work:idle:disabled". Jedes END IF schließt seinen Block.
Option Explicit On
FUNCTION Action(enabled, amount)
    IF enabled THEN
        IF amount > 0 THEN
            RETURN "work"
        ELSE
            RETURN "idle"
        END IF
    ELSE
        RETURN "disabled"
    END IF
END FUNCTION
SUB Main()
    RETURN Action(TRUE, 5) + ":" + Action(TRUE, 0) + ":" + Action(FALSE, 5)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Action(enabled, amount) prüft enabled, dann amount>0 für work oder idle. Das äußere ELSE liefert disabled. (TRUE,5), (TRUE,0), (FALSE,5) ergeben "work:idle:disabled". Jedes END IF schließt seinen Block.

### 3. Bedingungsreihenfolge

```vb
# Check(calls,value) erhöht calls ByRef und liefert value. Erste Bedingung falsch, zweite wahr; dritte und ELSE entfallen. result=7, calls=2, Main liefert calls*10+result=27. Alle Helfer sind enthalten.
Option Explicit On
FUNCTION Check(ByRef calls, ByVal value)
    calls += 1
    RETURN value
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR result = 0
    IF Check(calls, FALSE) THEN
        result = 5
    ELSEIF Check(calls, TRUE) THEN
        result = 7
    ELSEIF Check(calls, TRUE) THEN
        result = 9
    ELSE
        result = 8
    END IF
    RETURN calls * 10 + result
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Check(calls,value) erhöht calls ByRef und liefert value. Erste Bedingung falsch, zweite wahr; dritte und ELSE entfallen. result=7, calls=2, Main liefert calls*10+result=27. Alle Helfer sind enthalten.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: if / elseif / else
Runtime/Instructions/Generator.cs: Generate(IfContext)
Runtime/Interpreter.cs: CallSubrutine / IfInstruction / CreateArgumentWriter
Analysis/MisplacedStatementsVisitor.cs: VisitIf
Runtime/InjectionRuntime.cs: BlockingLanguageError
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/if-then-else-statement
-->
