# AndAlso / OrElse

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

AndAlso und OrElse verbinden Bedingungen und überspringen unnötige rechte Operanden. AndAlso überspringt bei falscher linker Seite, OrElse bei wahrer. Damit lassen sich Arrayzugriffe absichern und Aufrufe vermeiden.

## Genaue Syntax

```text
left AndAlso right
left OrElse right
(conditionA OrElse conditionB) AndAlso conditionC
```

## Parameter

- `left` — left: zuerst einmal ausgewerteter Ausdruck. Integer- oder Decimal-Null ist falsch, jede andere Zahl wahr.
- `right` — right: nur bei Bedarf einmal ausgewerteter Ausdruck. Übersprungene Zugriffe, Aufrufe und Nebenwirkungen finden nicht statt. Ausgewertete Operanden müssen numerisch sein; Text ausdrücklich mit CBool umwandeln.

## Rückgabewert

Integer 1 (TRUE) oder 0 (FALSE), nicht der ursprüngliche Operand. result=1 und result=TRUE sowie result=0 und result=FALSE sind gleichwertig. Wahr entspricht hier 1, nicht dem numerischen -1 von VB.NET. Eine gewöhnliche Anzahl bleibt eine Anzahl; diese Operation liefert einen Wahrheitswert.

## Verhalten

- Vergleiche gehören zu den Operanden. AndAlso bindet stärker als OrElse; gleiche Operatoren laufen von links nach rechts. Klammern ändern die Gruppierung. Übersprungener Code wird weiterhin geparst und von Option Explicit geprüft.
- Zusammenhängende AND/OR/XOR bleiben aus Kompatibilitätsgründen eager und linksassoziativ innerhalb eines Operanden, vor AndAlso/OrElse. TRUE OR FALSE AndAlso FALSE ergibt FALSE; TRUE OrElse FALSE AND FALSE ergibt TRUE. Mischungen einklammern. AND, OR, && und || werten beide Seiten aus.
- Die Engine wertet links aus, prüft numerische Wahrheit und liefert einen booleschen Wert oder wertet rechts aus. Fehler erforderlicher Operanden erreichen CATCH; FINALLY und Pause/Stopp bleiben wirksam. Übersprungene Aufrufe führen auch ihre Aktionen nicht aus.

## Beispiele

### 1. Erstes Element absichern

```vb
# FirstEquals erhält items und expected. GetArrayLength(items)>0 verhindert bei leeren Arrays das Lesen von items[0]. Main übergibt [42] und ein leeres Array, erhält 1 und 0 und liefert 10. Die vollständige Hilfsfunktion verändert nichts.
Option Explicit On
FUNCTION FirstEquals(ByVal items, expected)
    RETURN (GetArrayLength(items) > 0) AndAlso (items[0] = expected)
END FUNCTION
SUB Main()
    DIM items[0], empty[-1]
    items[0] = 42
    VAR present = FirstEquals(items, 42)
    VAR missing = FirstEquals(empty, 42)
    RETURN present * 10 + missing
END SUB
```

**Erläuterung der Parameter und Ausführung:**

FirstEquals erhält items und expected. GetArrayLength(items)>0 verhindert bei leeren Arrays das Lesen von items[0]. Main übergibt [42] und ein leeres Array, erhält 1 und 0 und liefert 10. Die vollständige Hilfsfunktion verändert nichts.

### 2. Ersatzaufruf einmal ausführen

```vb
# Probe erhöht calls ByRef und liefert TRUE. TRUE OrElse Probe(calls) überspringt den Aufruf; FALSE OrElse Probe(calls) führt ihn einmal aus. Beide Bedingungen liefern 1, Main liefert die Aufrufzahl 1.
Option Explicit On
FUNCTION Probe(ByRef calls)
    calls += 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR cached = TRUE OrElse Probe(calls)
    VAR fallback = FALSE OrElse Probe(calls)
    RETURN calls
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Probe erhöht calls ByRef und liefert TRUE. TRUE OrElse Probe(calls) überspringt den Aufruf; FALSE OrElse Probe(calls) führt ihn einmal aus. Beide Bedingungen liefern 1, Main liefert die Aufrufzahl 1.

### 3. Division und Vorrang

```vb
# AverageExceeds(total, count, limit) dividiert nur bei count>0. (25,0,10) ergibt 0; (25,2,10) ergibt 1, weil 12.5>10. TRUE OrElse FALSE AndAlso FALSE ergibt 1 und überspringt die AndAlso-Gruppe. Main liefert "0:1:1".
Option Explicit On
FUNCTION AverageExceeds(total, count, limit)
    RETURN (count > 0) AndAlso (total / count > limit)
END FUNCTION
SUB Main()
    VAR empty = AverageExceeds(25, 0, 10)
    VAR accepted = AverageExceeds(25, 2, 10)
    VAR priority = TRUE OrElse FALSE AndAlso FALSE
    RETURN CStr(empty) + ":" + CStr(accepted) + ":" + CStr(priority)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

AverageExceeds(total, count, limit) dividiert nur bei count>0. (25,0,10) ergibt 0; (25,2,10) ergibt 1, weil 12.5>10. TRUE OrElse FALSE AndAlso FALSE ergibt 1 und überspringt die AndAlso-Gruppe. Main liefert "0:1:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: logicalOperator / ANDALSO / ORELSE
Runtime/Interpreter.cs: VisitExpression / EvaluateAndAlsoGroup / EvaluateEagerLogicalGroup / NumericTruth
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/andalso-operator
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/orelse-operator
-->
