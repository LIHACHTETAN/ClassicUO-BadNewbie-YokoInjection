# VAR / DIM

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

VAR und skalares DIM deklarieren einen benannten Wert. Eine Zuweisung wertet den Ausdruck aus und speichert das Ergebnis. Deklarationen in einer Prozedur sind lokal für den Aufruf, außerhalb der Prozeduren global für das Skript.

## Genaue Syntax

```text
VAR name [AS type] [= expression] [, name ...]
DIM name [AS type] [= expression] [, name ...]
name = expression
LET name = expression
SET name = expression
```

## Parameter

- `name` — Variablenname ohne Anführungszeichen: Buchstaben, Ziffern und Unterstriche, beginnend mit Buchstabe oder Unterstrich. Schreibweise beibehalten und keine Sprachschlüsselwörter verwenden.
- `type` — Optionales AS. Integer/Long/Short/Byte verwenden die vorzeichenbehaftete 32-Bit-Konvertierung der Engine; Double/Single/Decimal deren Zahl doppelter Genauigkeit; String Text; Boolean/Bool einen Wahrheitswert; Variant/Object behalten die Wertart. Diese Aliase erzwingen keine getrennten VB.NET-Bereiche für byte/short/long.
- `expression` — Optionaler Startwert in VAR/DIM; erforderlicher rechter Ausdruck bei Zuweisung. Auswertung beim Ausführen der Zeile. AS String ohne Startwert ergibt leeren Text; typisierte Zahlen und Boolean beginnen mit null. Ohne Startwert enthalten untypisiertes VAR und VAR AS Variant/Object Unit (kein Wert), während skalares DIM 0 setzt. Eine untypisierte Variable kann später eine andere Wertart enthalten.

## Rückgabewert

Kein Wert. VAR, DIM und Zuweisungen liefern kein Ergebnis. Das Lesen des Namens liefert den gespeicherten Wert. RETURN gibt diesen in den Beispielen aus Main zurück, nicht aus DIM.

## Verhalten

- Eckige Klammern in der Syntax kennzeichnen optionale Teile; nicht um AS oder Startwerte schreiben. DIM für Arrays hat eine andere Form.
- LET und SET sind kompatible Formen gewöhnlicher Zuweisung. Mit Option Explicit On deklarieren sie keinen Namen. AS gilt auch für spätere Zuweisungen; unzulässige Konvertierung oder unbekannter Typ erzeugt einen Laufzeitfehler.
- Lokale Namen gehören zum Prozeduraufruf. Eine Deklaration in IF erzeugt keinen eigenen Blockbereich. Ein nicht ausgeführter Zweig erstellt keinen Laufzeitwert. Wird der Wert später benötigt, vor der Verzweigung deklarieren.
- Injection-Kompatibilität: Eine aufgerufene Prozedur erbt die aktuellen globalen Skalarwerte des Aufrufers samt AS-Typen. Eine neue Skalarzuweisung in der aufgerufenen Prozedur ändert den Aufrufer nicht. Dafür den neuen Wert zurückgeben oder ein BYREF-Argument verwenden. Array/Object-Werte werden nicht tief kopiert. Ein neuer Hauptaufruf initialisiert globale Variablen erneut; eine lokale Deklaration verdeckt den Namen im eigenen Rahmen, ohne die globale Deklaration zu ersetzen.
- Die Engine wertet den Startwert aus, definiert Speicher im aktuellen Bereich und konvertiert den Typ. Spätere Zuweisungen werten zuerst die rechte Seite aus. Die Beispiele rechnen lokal; Variablen werden nicht automatisch in Profilen oder JSON-Dateien gespeichert.

## Beispiele

### 1. Eine Ganzzahl ändern

```vb
# count beginnt mit 0, erhält 5, dann addiert LET 2. Main liefert Integer 7. Das erste DIM deklariert den Namen; spätere Zuweisungen ändern den Wert.
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    LET count = count + 2
    RETURN count
END SUB
```

**Erläuterung der Parameter und Ausführung:**

count beginnt mit 0, erhält 5, dann addiert LET 2. Main liefert Integer 7. Das erste DIM deklariert den Namen; spätere Zuweisungen ändern den Wert.

### 2. Text und Wahrheitswert

```vb
# label beginnt als leerer String. SET speichert "ore". enabled ist Boolean TRUE; der IF-Zweig liefert String "ore". TRUE ohne Anführungszeichen bedeutet logisch 1.
Option Explicit On
SUB Main()
    DIM label AS String
    VAR enabled AS Boolean = TRUE
    SET label = "ore"
    IF enabled = TRUE THEN
        RETURN label
    END IF
    RETURN "disabled"
END SUB
```

**Erläuterung der Parameter und Ausführung:**

label beginnt als leerer String. SET speichert "ore". enabled ist Boolean TRUE; der IF-Zweig liefert String "ore". TRUE ohne Anführungszeichen bedeutet logisch 1.

### 3. Globale Eingabe und lokale Berechnung

```vb
# baseAmount ist global und gleich 4. extra ist lokal in Calculate und gleich 3. Calculate liefert 7; Main speichert es im eigenen lokalen result und liefert 7. extra ist keine lokale Variable von Main.
Option Explicit On
VAR baseAmount AS Integer = 4
FUNCTION Calculate()
    VAR extra = 3
    RETURN baseAmount + extra
END FUNCTION
SUB Main()
    VAR result = Calculate()
    RETURN result
END SUB
```

**Erläuterung der Parameter und Ausführung:**

baseAmount ist global und gleich 4. extra ist lokal in Calculate und gleich 3. Calculate liefert 7; Main speichert es im eigenen lokalen result und liefert 7. extra ist keine lokale Variable von Main.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim
Runtime/Interpreter.cs: VisitVarDef / VisitAssignment
Runtime/SemanticScope.cs: DefineVar / SetVar / Coerce
-->
