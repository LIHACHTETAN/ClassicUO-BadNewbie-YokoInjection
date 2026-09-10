# +, -, *, /, MOD

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Ein arithmetischer Ausdruck berechnet einen Wert: + addiert, - subtrahiert oder kehrt das Vorzeichen um, * multipliziert, / dividiert, MOD liefert den ganzzahligen Rest. Den Wert einer Variablen zuweisen oder mit RETURN zurückgeben.

## Genaue Syntax

```text
left + right
left - right
-right
left * right
left / right
left MOD right
(expression)
```

## Parameter

- `left` — Linker numerischer Operand: Literal, deklarierte Variable, geklammerter Ausdruck oder Funktionsergebnis. Beim unären Minus entfällt er.
- `right` — Rechter numerischer Operand. Bei / der Divisor; bei MOD muss er nach der Umwandlung in Integer ungleich null bleiben. Beispielsweise wird 0.5 zu 0 abgeschnitten und verursacht einen Fehler.
- `operator / precedence` — Reihenfolge: unäres Minus, dann * / MOD gleichrangig von links nach rechts, dann binäres + - von links nach rechts. Klammern ändern die Reihenfolge. Unäres Plus, Potenz ^ und Ganzzahldivision mit umgekehrtem Schrägstrich werden nicht unterstützt.

## Rückgabewert

Integer bei ganzzahligem +, -, * und unärem Minus; Decimal, wenn ein beteiligter numerischer Operand Decimal ist. / liefert immer Decimal: 5/2=2.5. MOD liefert Integer. Erst der Skriptkontext macht aus der Zahl einen Erfolgsindikator oder eine Objektanzahl.

## Verhalten

- MOD wandelt beide Operanden in vorzeichenbehaftete 32-Bit-Ganzzahlen um und schneidet darstellbare Bruchteile gegen null ab. Der Rest hat das Vorzeichen des Dividenden: -17 MOD 5=-2; -2147483648 MOD -1=0. Auch mOd funktioniert unabhängig von der Schreibweise.
- MOD durch null löst einen mit TRY/CATCH abfangbaren Fehler aus. / verwendet Gleitkommadivision: eine von null verschiedene Zahl durch null ergibt vorzeichenbehaftetes Infinity, 0/0 ergibt NaN. Für ein endliches Ergebnis den Divisor vorher prüfen.
- Ganzzahliges +, -, * und Negieren laufen bei Überlauf innerhalb von 32 Bit um; der Typ wird nicht automatisch vergrößert. Vor großen Rechnungen einen Operanden in Decimal umwandeln, falls Näherungswerte ausreichen. Gleitkommazahlen unterliegen binären Rundungsfehlern.
- Normale Zahlenoperatoren lesen Text nicht automatisch als Zahl. String+String verbindet Text, String+Integer schlägt fehl. Beispielsweise CDbl ausdrücklich verwenden. Der infixe MOD-Operator wandelt Ganzzahltext strenger um als die separate Funktion BasicMod.
- Der Interpreter wertet Operanden in Ausdrucksreihenfolge aus, wählt das Operator-Token und erstellt eine InjectionValue. Geklammerte Ausdrücke werden zuerst abgeschlossen. Bewegung, Warten und Netzwerkzugriffe entstehen nur, wenn ein Operand eine entsprechende API aufruft.

## Beispiele

### 1. Rangfolge und Klammern

```vb
# plain=2+3*4 multipliziert zuerst und ergibt 14. grouped=(2+3)*4 ergibt 20. Main gibt plain*100+grouped=1420 zurück, um beide Rechnungen zu prüfen.
Option Explicit On
SUB Main()
    VAR plain = 2 + 3 * 4
    VAR grouped = (2 + 3) * 4
    RETURN plain * 100 + grouped
END SUB
```

**Erläuterung der Parameter und Ausführung:**

plain=2+3*4 multipliziert zuerst und ergibt 14. grouped=(2+3)*4 ergibt 20. Main gibt plain*100+grouped=1420 zurück, um beide Rechnungen zu prüfen.

### 2. Vollständige Gruppen und Rest

```vb
# DescribeBatches erhält total=27 und size=5. Die Prüfung verwirft Gruppengrößen kleiner oder gleich null. Fix(total/size) macht aus 5.4 fünf vollständige Gruppen; total mOd size ergibt zwei übrige Objekte. CStr ermöglicht die Textausgabe "5:2". Die Hilfsfunktion ist vollständig angegeben.
Option Explicit On
FUNCTION DescribeBatches(total, size)
    IF size <= 0 THEN
        RETURN "invalid"
    END IF
    VAR whole = Fix(total / size)
    VAR remaining = total mOd size
    RETURN CStr(whole) + ":" + CStr(remaining)
END FUNCTION
SUB Main()
    RETURN DescribeBatches(27, 5)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

DescribeBatches erhält total=27 und size=5. Die Prüfung verwirft Gruppengrößen kleiner oder gleich null. Fix(total/size) macht aus 5.4 fünf vollständige Gruppen; total mOd size ergibt zwei übrige Objekte. CStr ermöglicht die Textausgabe "5:2". Die Hilfsfunktion ist vollständig angegeben.

### 3. Ungültigen Divisor abfangen

```vb
# 10 MOD 0 scheitert vor der Zuweisung an unusedResult. CATCH speichert den Fehler in problem und setzt caught=TRUE. Main liefert 1 als Fehlerbehandlungsindikator dieses Beispiels, nicht als Ergebnis des fehlgeschlagenen MOD.
Option Explicit On
SUB Main()
    VAR caught = FALSE
    TRY
        VAR unusedResult = 10 MOD 0
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**Erläuterung der Parameter und Ausführung:**

10 MOD 0 scheitert vor der Zuweisung an unusedResult. CATCH speichert den Fehler in problem und setzt caught=TRUE. Main liefert 1 als Fehlerbehandlungsindikator dieses Beispiels, nicht als Ergebnis des fehlgeschlagenen MOD.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: signedOperand / additiveOperand / comparativeOperand
Runtime/Interpreter.cs: VisitSignedOperand / VisitAdditiveOperand / VisitComparativeOperand
Runtime/InjectionValue.cs: arithmetic operators
Runtime/NumberConversions.cs: ToInt
-->
