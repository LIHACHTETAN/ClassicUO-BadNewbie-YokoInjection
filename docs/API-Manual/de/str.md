# str

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Str(value) formatiert einen skalaren Basic-Wert als Text.

## Genaue Syntax

```text
str(value:Decimal) -> String
str(value:Integer) -> String
str(value:String) -> String
```

## Parameter

- `value` — Ein erforderlicher Integer-, Decimal- oder String-Wert. Der tatsächliche Typ bestimmt die Überladung. Für Array, Object und Unit gibt es keine passende Str-Überladung.

## Rückgabewert

String: sprachunabhängiger Zahlentext oder unveränderte Eingabe-String. Positive Zahlen erhalten kein führendes Leerzeichen. Kein Genauigkeitsparameter.

## Verhalten

- Lokale Berechnung ohne Spielabfrage. Ein fehlendes Argument ist ein Fehler. Attribute werden durch UO.Int()/UO.Str() gelesen, nicht Int()/Str(). Int verwendet BasicDouble und Math.Floor; Str wählt InternalSubrutines.Str nach dem Typ und formatiert sprachunabhängig.

## Beispiele

### Str — 1

```vb
# Str — 1
#
# Str(value) formatiert einen skalaren Basic-Wert als Text.
#
# String: sprachunabhängiger Zahlentext oder unveränderte Eingabe-String. Positive Zahlen
# erhalten kein führendes Leerzeichen. Kein Genauigkeitsparameter.

SUB Main()
    # value=42 ist Integer. Str liefert "42" ohne führendes Leerzeichen; Main gibt diese String
    # zurück.

    RETURN Str(42)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value=42 ist Integer. Str liefert "42" ohne führendes Leerzeichen; Main gibt diese String zurück.

### Str — 2

```vb
# Str — 2
#
# Str(value) formatiert einen skalaren Basic-Wert als Text.
#
# String: sprachunabhängiger Zahlentext oder unveränderte Eingabe-String. Positive Zahlen
# erhalten kein führendes Leerzeichen. Kein Genauigkeitsparameter.

SUB Main()
    # amount=-12.5 ist Decimal. Str speichert "-12.5" mit Dezimalpunkt in text, unabhängig von der
    # Sprache. Main gibt text zurück; amount bleibt numerisch.

    VAR amount = -12.5
    VAR text = Str(amount)
    RETURN text
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- amount=-12.5 ist Decimal. Str speichert "-12.5" mit Dezimalpunkt in text, unabhängig von der Sprache. Main gibt text zurück; amount bleibt numerisch.

### Str — 3

```vb
# Str — 3
#
# Str(value) formatiert einen skalaren Basic-Wert als Text.
#
# String: sprachunabhängiger Zahlentext oder unveränderte Eingabe-String. Positive Zahlen
# erhalten kein führendes Leerzeichen. Kein Genauigkeitsparameter.

SUB Main()
    # ItemLabel erhält name="ore", count=3. Str(name) erhält den Namen, Str(count) liefert "3". Die
    # Funktion verbindet beide Texte mit " x"; Main liefert "ore x3".

    RETURN ItemLabel("ore",3)
END SUB

SUB ItemLabel(name,count)
    RETURN Str(name) + " x" + Str(count)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- ItemLabel erhält name="ore", count=3. Str(name) erhält den Namen, Str(count) liefert "3". Die Funktion verbindet beide Texte mit " x"; Main liefert "ore x3".
