# Int

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Int(value) rundet eine Basic-Zahl in Richtung minus unendlich ab.

## Genaue Syntax

```text
Int(value:Any) -> Integer
```

## Parameter

- `value` — Ein erforderlicher Integer/Decimal-Wert oder Zahlentext mit Dezimalpunkt, unabhängig von der Sprache. Ungültiger Text, Array, Object und Unit werden 0; Eingaben vorher mit IsNumeric prüfen.

## Rückgabewert

Integer: floor(value), etwa 2.9 -> 2 und -2.9 -> -3. Das Ergebnis muss in einen vorzeichenbehafteten Int32 passen; nichtendliche Werte und Bereichsüberschreitungen vermeiden.

## Verhalten

- Lokale Berechnung ohne Spielabfrage. Ein fehlendes Argument ist ein Fehler. Attribute werden durch UO.Int()/UO.Str() gelesen, nicht Int()/Str(). Int verwendet BasicDouble und Math.Floor; Str wählt InternalSubrutines.Str nach dem Typ und formatiert sprachunabhängig.

## Beispiele

### Int — 1

```vb
# Int — 1
#
# Int(value) rundet eine Basic-Zahl in Richtung minus unendlich ab.
#
# Integer: floor(value), etwa 2.9 -> 2 und -2.9 -> -3. Das Ergebnis muss in einen
# vorzeichenbehafteten Int32 passen; nichtendliche Werte und Bereichsüberschreitungen vermeiden.

SUB Main()
    # value=2.9. Abrunden ergibt Integer 2, den Main zurückgibt.

    RETURN Int(2.9)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value=2.9. Abrunden ergibt Integer 2, den Main zurückgibt.

### Int — 2

```vb
# Int — 2
#
# Int(value) rundet eine Basic-Zahl in Richtung minus unendlich ab.
#
# Integer: floor(value), etwa 2.9 -> 2 und -2.9 -> -3. Das Ergebnis muss in einen
# vorzeichenbehafteten Int32 passen; nichtendliche Werte und Bereichsüberschreitungen vermeiden.

SUB Main()
    # value=-2.9. Abrunden ergibt -3; Abschneiden in Richtung null ergäbe -2. Main liefert Integer
    # -3.

    VAR value = -2.9
    RETURN Int(value)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value=-2.9. Abrunden ergibt -3; Abschneiden in Richtung null ergäbe -2. Main liefert Integer -3.

### Int — 3

```vb
# Int — 3
#
# Int(value) rundet eine Basic-Zahl in Richtung minus unendlich ab.
#
# Integer: floor(value), etwa 2.9 -> 2 und -2.9 -> -3. Das Ergebnis muss in einen
# vorzeichenbehafteten Int32 passen; nichtendliche Werte und Bereichsüberschreitungen vermeiden.

SUB Main()
    # WholeUnits erhält total=27, size=5. Bei size<=0 kommt 0 zurück; sonst rundet Int(total/size)
    # die 5.4 ab. Main liefert 5 ganze Einheiten. Hilfsfunktion und beide Parameter sind vollständig
    # definiert.

    RETURN WholeUnits(27,5)
END SUB

SUB WholeUnits(total,size)
    IF size <= 0 THEN
        RETURN 0
    END IF
    RETURN Int(total/size)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- WholeUnits erhält total=27, size=5. Bei size<=0 kommt 0 zurück; sonst rundet Int(total/size) die 5.4 ab. Main liefert 5 ganze Einheiten. Hilfsfunktion und beide Parameter sind vollständig definiert.
