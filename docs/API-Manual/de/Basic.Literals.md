# 123 / 0x0EED / "text" / TRUE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Ein Literal schreibt einen Wert direkt in den Code. Zahlen und zitierte Texte brauchen keine Deklaration. TRUE/FALSE sind vordefinierte logische Werte. Eine zitierte Zahl bleibt bis zur Konvertierung Text.

## Genaue Syntax

```text
123
-2147483648
0x0EED
0xFFFFFFFF
2.5
"text"
'text'
TRUE
FALSE
```

## Parameter

- `integer / hexadecimal` — Dezimaler Integer von -2147483648 bis 2147483647 oder 0x mit Hexziffern 0–9/A–F. Kleines x verwenden. Hexliterale repräsentieren 32 Bits: 0xFFFFFFFF ist Integer -1, keine positive 64-Bit-Zahl.
- `floating` — Gleitkommazahl mit Ziffern vor und nach dem Punkt, etwa 2.5 oder -0.25. 0.5 statt .5 schreiben. Komma, Exponentenschreibweise 1e3 und Zahlensuffixe sind in dieser Grammatik nicht unterstützt.
- `text` — Text zwischen passenden einfachen oder doppelten Anführungszeichen. Für ein enthaltenes Zitat die andere Form oder Chr(34)/Chr(39) verwenden. Rückstrich-Escapes und verdoppelte Anführungszeichen werden nicht interpretiert. Beispieltext auf einer physischen Zeile halten.
- `TRUE / FALSE` — TRUE ist Integer 1, FALSE Integer 0. Diese Namen nicht neu deklarieren. Es sind Werte statt Aufrufe: TRUE, nicht TRUE().

## Rückgabewert

Ganz-/Hexzahl ergibt Integer; eine Zahl mit Punkt ergibt Decimal, einen binären Gleitkommawert; zitierter Text ergibt String. TRUE/FALSE ergeben Integer 1/0. Eine Wertauswertung löst keine Spielaktion aus und deklariert keine Variable.

## Verhalten

- Das Zeichen in -5 ist eine unäre Operation. -2147483648 wird als kleinster Integer behandelt, ohne zuerst den positiven Betrag speichern zu müssen. Ganze Zahlen außerhalb des Bereichs scheitern; größere Näherungswerte benötigen passende Gleitkommazahlen.
- Text behält Zeichen und Schreibweise. "350" ist nicht die Zahl 350, "false" nicht FALSE. # und ; sind innerhalb von Anführungszeichen Text, außerhalb Kommentare. Konvertierungen stehen unter AS und den Funktionskarten.
- Die Engine erkennt das Token, liest Zahlen kulturunabhängig oder entfernt die äußeren Anführungszeichen. Die IDE-Sprache ändert den Dezimaltrenner im Quelltext nicht.
- Serial, Grafiktyp und Koordinate können alle Zahlen sein. Das Literal bestimmt ihre Bedeutung nicht; entscheidend ist der Parametervertrag des API-Aufrufs.

## Beispiele

### 1. Hextyp und Ganzzahlgrenze

```vb
# itemType=0x0EED ist 3821. lowest=-2147483648 entspricht dem vorzeichenbehafteten Bitmuster 0x80000000. Main liefert deshalb itemType=3821. Es findet keine Gegenstandssuche statt.
Option Explicit On
SUB Main()
    VAR itemType = 0x0EED
    VAR lowest = -2147483648
    IF lowest = 0x80000000 THEN
        RETURN itemType
    END IF
    RETURN 0
END SUB
```

**Erläuterung der Parameter und Ausführung:**

itemType=0x0EED ist 3821. lowest=-2147483648 entspricht dem vorzeichenbehafteten Bitmuster 0x80000000. Main liefert deshalb itemType=3821. Es findet keine Gegenstandssuche statt.

### 2. Beide Zitatarten

```vb
# owner="O'Brien" enthält ein Apostroph. instruction steht in einfachen Anführungszeichen und enthält doppelte. owner, " | " und instruction ergeben O'Brien | say "go", ohne Rückstrich-Escapes im Skript.
Option Explicit On
SUB Main()
    VAR owner = "O'Brien"
    VAR instruction = 'say "go"'
    RETURN owner + " | " + instruction
END SUB
```

**Erläuterung der Parameter und Ausführung:**

owner="O'Brien" enthält ein Apostroph. instruction steht in einfachen Anführungszeichen und enthält doppelte. owner, " | " und instruction ergeben O'Brien | say "go", ohne Rückstrich-Escapes im Skript.

### 3. Logische Werte als Zahlen

```vb
# enabled=TRUE speichert 1, stopped=FALSE speichert 0. Die Rechnung ergibt 1*10+0=10. Main liefert ein Zahlenergebnis, nicht das kanonische TRUE.
Option Explicit On
SUB Main()
    VAR enabled = TRUE
    VAR stopped = FALSE
    RETURN enabled * 10 + stopped
END SUB
```

**Erläuterung der Parameter und Ausführung:**

enabled=TRUE speichert 1, stopped=FALSE speichert 0. Die Rechnung ergibt 1*10+0=10. Main liefert ein Zahlenergebnis, nicht das kanonische TRUE.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: number / literal / HEX_NUMBER / DEC_NUMBER
Runtime/Interpreter.cs: VisitNumber / VisitLiteral / VisitSignedOperand
Runtime/InjectionApiUO.cs: TRUE / FALSE intrinsic values
-->
