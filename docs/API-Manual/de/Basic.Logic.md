# NOT / AND / OR / XOR

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

NOT kehrt eine Bedingung um. AND verlangt beide, OR mindestens eine, XOR genau eine. && entspricht AND, || entspricht OR. Groß-/Kleinschreibung ist bei Schlüsselwörtern egal.

## Genaue Syntax

```text
NOT (condition)
left AND right
left && right
left OR right
left || right
left XOR right
```

## Parameter

- `left` — Linke binäre Bedingung. AND/OR verlangen Integer oder Decimal: null ist falsch, jede andere Zahl wahr.
- `right` — Rechte Bedingung, bei AND/OR ebenfalls numerisch. Beide Operanden werden ausgewertet; links falsch bei AND oder wahr bei OR überspringt diesen Ausdruck nicht.
- `NOT / grouping` — Bei NOT die gesamte umzukehrende Bedingung einklammern. Kombinationen aus AND, OR und XOR ausdrücklich mit Klammern gruppieren.

## Rückgabewert

Integer 1 (TRUE) oder Integer 0 (FALSE). Logische Operationen, keine Bitoperationen: 2 AND 4 liefert 1 und keine Bitmaske. Rückgabeflags mit =TRUE oder =1, =FALSE oder =0 prüfen.

## Verhalten

- AND, OR und XOR sind in dieser Engine gleichrangig und werden von links nach rechts ausgewertet: TRUE OR FALSE AND FALSE ergibt 0; TRUE OR (FALSE AND FALSE) ergibt 1. Diese Kompatibilitätsregel beim Übertragen von VB beachten.
- NOT(condition) wertet die Bedingung aus und kehrt sie um. Am Vergleichsanfang bedeutet NOT 1=2 dasselbe wie NOT(1=2). (NOT value) schreiben, wenn der umgekehrte Wert selbst Vergleichsoperand sein soll.
- AND/OR lehnen String, Array, Object und Unit ab. Das bisherige NOT und XOR prüft hingegen Gleichheit mit der numerischen Null: "0", leerer Text, Arrays, Objekte und Unit gelten als ungleich null. Dafür klare numerische Bedingungen festlegen; CBool hat eigene Umwandlungsregeln.
- Jeder rechte Ausdruck läuft, einschließlich Funktionen, Wartevorgängen und Fehlern. Klammern ändern nur die Gruppierung. Verschachtelte IF-Anweisungen verwenden, wenn ein späterer Ausdruck nur nach einer erfüllten Bedingung ausgeführt werden darf.

## Beispiele

### 1. Benannte Flags kombinieren

```vb
# ready=TRUE und blocked=FALSE. NOT(blocked) liefert 1, also wird canRun=1. ready XOR blocked ist wahr, weil genau ein Flag wahr ist. Main gibt canRun*10+exclusive=11 zurück.
Option Explicit On
SUB Main()
    VAR ready = TRUE
    VAR blocked = FALSE
    VAR canRun = ready AND (NOT blocked)
    VAR exclusive = ready XOR blocked
    RETURN canRun * 10 + exclusive
END SUB
```

**Erläuterung der Parameter und Ausführung:**

ready=TRUE und blocked=FALSE. NOT(blocked) liefert 1, also wird canRun=1. ready XOR blocked ist wahr, weil genau ein Flag wahr ist. Main gibt canRun*10+exclusive=11 zurück.

### 2. Beide Aufrufe beobachten

```vb
# Mark erhöht seinen ByRef-Parameter counter und gibt TRUE zurück. Main beginnt bei counter=0. FALSE AND Mark(counter) ruft Mark trotzdem auf; TRUE OR Mark(counter) ruft es erneut auf. Die Bedingungen ergeben 0 und 1, Main liefert counter=2. Mark ist vollständig angegeben.
Option Explicit On
FUNCTION Mark(ByRef counter)
    counter = counter + 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR counter = 0
    VAR first = FALSE AND Mark(counter)
    VAR second = TRUE OR Mark(counter)
    RETURN counter
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Mark erhöht seinen ByRef-Parameter counter und gibt TRUE zurück. Main beginnt bei counter=0. FALSE AND Mark(counter) ruft Mark trotzdem auf; TRUE OR Mark(counter) ruft es erneut auf. Die Bedingungen ergeben 0 und 1, Main liefert counter=2. Mark ist vollständig angegeben.

### 3. Gruppierung festlegen

```vb
# legacy berechnet TRUE OR FALSE, dann AND FALSE und ergibt 0. grouped berechnet zuerst FALSE AND FALSE in Klammern, dann OR mit TRUE und ergibt 1. Main liefert legacy*10+grouped=1.
Option Explicit On
SUB Main()
    VAR legacy = TRUE OR FALSE AND FALSE
    VAR grouped = TRUE OR (FALSE AND FALSE)
    RETURN legacy * 10 + grouped
END SUB
```

**Erläuterung der Parameter und Ausführung:**

legacy berechnet TRUE OR FALSE, dann AND FALSE und ergibt 0. grouped berechnet zuerst FALSE AND FALSE in Klammern, dann OR mit TRUE und ergibt 1. Main liefert legacy*10+grouped=1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: expression / logicalOperand / signedOperand
Runtime/Interpreter.cs: VisitExpression / VisitLogicalOperand / VisitSignedOperand
Runtime/InjectionValue.cs: operator & / operator | / Equals
-->
