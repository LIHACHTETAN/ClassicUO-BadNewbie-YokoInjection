# String + / &

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: de -->

Text mit + oder der kompatiblen Basic-Schreibweise & verbinden. Zahlen ausdrücklich mit CStr umwandeln, bevor Beschriftungen, Mengen oder Koordinaten daraus entstehen.

## Genaue Syntax

```text
leftText + rightText
leftText & rightText
"label" & CStr(number)
```

## Parameter

- `leftText` — Linker Text: Literal, String-Variable oder in Text umgewandeltes Funktionsergebnis.
- `rightText` — Rechter Text. CStr(number) wandelt Zahlen um; CStr(Unit) ergibt leeren Text. Leerzeichen, Doppelpunkte und andere Trenner selbst angeben.

## Rückgabewert

String, wenn beide Operanden String sind; kein Erfolgsflag. & wird hier zu + normalisiert und übernimmt dessen Regeln: zwei Zahlen werden addiert, also ergibt 2 & 3 Integer 5. String und Zahl zu mischen schlägt fehl. Das unterscheidet sich von impliziter VB-Textumwandlung.

## Verhalten

- Beide Seiten werden in Reihenfolge ausgewertet und verbunden. Ketten laufen von links nach rechts. Numerische Berechnungen einklammern und das Ergebnis vor dem Verbinden umwandeln.
- Trenner, Leerzeichen, Anführungszeichen und Zeilenumbrüche werden nicht automatisch ergänzt. & im String-Literal bleibt ein kaufmännisches Und. Das logische Token && bleibt AND und verbindet keinen Text.
- CStr formatiert Zahlen unabhängig von der Clientsprache mit Dezimalpunkt. Umwandlung und Verkettung drucken oder senden nichts; die entstandene String bei Bedarf anschließend einer API übergeben.
- Strings sind unveränderlich: eine Verkettung erzeugt einen neuen Wert, ohne Quellvariablen zu ändern. Ständiges Vergrößern langer Strings kopiert ihren Inhalt; nur die benötigte Ausgabe erzeugen statt bei jedem Schleifendurchlauf einen ganzen Bericht neu aufzubauen.

## Beispiele

### 1. Anzahl beschriften

```vb
# amount=50 ist Integer. CStr(amount) ergibt "50". "Items: " enthält Doppelpunkt und abschließendes Leerzeichen. Main gibt "Items: 50" ohne automatische Ausgabe zurück.
Option Explicit On
SUB Main()
    VAR amount = 50
    RETURN "Items: " & CStr(amount)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

amount=50 ist Integer. CStr(amount) ergibt "50". "Items: " enthält Doppelpunkt und abschließendes Leerzeichen. Main gibt "Items: 50" ohne automatische Ausgabe zurück.

### 2. Vollständige Formatierfunktion

```vb
# Label erhält name="ore", amount=3. Sie verbindet Name, ausdrücklichen Doppelpunkt und CStr(amount). Die vollständige Funktion gibt "ore:3" an Main zurück und kann andere Namen und Mengen verarbeiten.
Option Explicit On
FUNCTION Label(name, amount)
    RETURN name + ":" + CStr(amount)
END FUNCTION
SUB Main()
    RETURN Label("ore", 3)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

Label erhält name="ore", amount=3. Sie verbindet Name, ausdrücklichen Doppelpunkt und CStr(amount). Die vollständige Funktion gibt "ore:3" an Main zurück und kann andere Namen und Mengen verarbeiten.

### 3. Vorher rechnen

```vb
# CStr(2+3) berechnet zuerst 5 und wandelt es in "5" um. Das zweite Literal behält Semikolon, Leerzeichen und A&B. Main gibt "Total: 5; literal: A&B" zurück.
Option Explicit On
SUB Main()
    RETURN "Total: " & CStr(2 + 3) & "; literal: A&B"
END SUB
```

**Erläuterung der Parameter und Ausführung:**

CStr(2+3) berechnet zuerst 5 und wandelt es in "5" um. Das zweite Literal behält Semikolon, Leerzeichen und A&B. Main gibt "Total: 5; literal: A&B" zurück.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: ProtectLiteralText / ReplaceConcatenationOutsideLiterals
Runtime/InjectionValue.cs: operator + / explicit operator string
Runtime/InjectionApi.cs: CStr
-->
