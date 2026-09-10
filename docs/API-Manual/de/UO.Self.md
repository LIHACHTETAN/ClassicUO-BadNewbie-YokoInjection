# UO.Self

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liefert die ID des aktuellen Charakters.

## Genaue Syntax

```text
UO.Self() -> Integer
```

## Parameter

Keine Parameter.

## Rückgabewert

Integer — Serial/ID, kein Graphic/Type, Layer, Zähler oder Boolean. 0: kein aktuelles Objekt. Alle 32 Bits bleiben erhalten; <> 0 statt = TRUE oder > 0 prüfen. Ein gespeichertes Ergebnis aktualisiert sich nicht selbst. Liest World.Player.Serial; fehlender/zerstörter Player liefert 0. Tod ist keine Zerstörung: ein vorhandener Geist behält die Spieler-ID.

## Verhalten

- Keine Argumente. Lokales Lesen über Invoke auf dem Spielthread; Skriptabbruch kann das Warten darauf beenden. Kein Paket, Öffnen eines Containers, Zielauswahl oder Itemtransfer.
- self/backpack ohne Klammern werden neu gelesen, sofern keine Skriptvariable sie verdeckt. Textaliasnamen werden von der empfangenden Funktion ausgewertet. Beim Transferziel bedeutet "self" Rucksack; UO.Self() liefert dagegen die Spieler-Serial. Für eine Container-ID UO.Backpack() verwenden.
- World.Clear entfernt Player; danach liefern Aufrufe 0. Anmeldung oder Austausch des Rucksacks kann die ID ändern. Einzelne Lesevorgänge bilden keinen atomaren Snapshot. Eine ID ungleich 0 beweist weder Verbindung, Servererlaubnis noch geladenen Inhalt.

### Interne Funktionen: vom Aufruf zum Ergebnis

Tatsächliche Schritte zum Lesen des Clientobjekts. IsOwnSerial ist die vollständig gezeigte Skriptfunktion, keine weitere eingebaute API.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility wählt den Zweig ohne Argumente und verpackt den Bridge-Integer als InjectionValue. Kein Pascal-Ausgabeparameter und kein weiteres optionales Argument.

Integer — Serial/ID, kein Graphic/Type, Layer, Zähler oder Boolean. 0: kein aktuelles Objekt. Alle 32 Bits bleiben erhalten; <> 0 statt = TRUE oder > 0 prüfen. Ein gespeichertes Ergebnis aktualisiert sich nicht selbst.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `ExecuteStealthCompatibility`.

#### 2. Invoke

Liest World.Player.Serial; fehlender/zerstörter Player liefert 0. Tod ist keine Zerstörung: ein vorhandener Geist behält die Spieler-ID. Invoke liest im Spielthread; ein Arbeitsthread wartet auf die Verarbeitung durch den Manager. Skriptabbruch unterbricht das Warten. Keine zusätzliche Verzögerung oder Netzwerkanfrage.

Integer — Serial/ID, kein Graphic/Type, Layer, Zähler oder Boolean. 0: kein aktuelles Objekt. Alle 32 Bits bleiben erhalten; <> 0 statt = TRUE oder > 0 prüfen. Ein gespeichertes Ergebnis aktualisiert sich nicht selbst. Keine Argumente. Lokales Lesen über Invoke auf dem Spielthread; Skriptabbruch kann das Warten darauf beenden. Kein Paket, Öffnen eines Containers, Zielauswahl oder Itemtransfer.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 3. Clear

World.Clear entfernt Player; danach liefern Aufrufe 0. Anmeldung oder Austausch des Rucksacks kann die ID ändern. Einzelne Lesevorgänge bilden keinen atomaren Snapshot. Eine ID ungleich 0 beweist weder Verbindung, Servererlaubnis noch geladenen Inhalt.

World.Clear entfernt Player; danach liefern Aufrufe 0. Anmeldung oder Austausch des Rucksacks kann die ID ändern. Einzelne Lesevorgänge bilden keinen atomaren Snapshot. Eine ID ungleich 0 beweist weder Verbindung, Servererlaubnis noch geladenen Inhalt.

Projektquelle: `src/ClassicUO.Client/Game/World.cs`; Funktion `Clear`.

World.Clear entfernt Player; danach liefern Aufrufe 0. Anmeldung oder Austausch des Rucksacks kann die ID ändern. Einzelne Lesevorgänge bilden keinen atomaren Snapshot. Eine ID ungleich 0 beweist weder Verbindung, Servererlaubnis noch geladenen Inhalt.


## Beispiele

### ID lesen und ausgeben

```vb
# ID lesen und ausgeben
#
# Liefert die ID des aktuellen Charakters.
#
# Integer — Serial/ID, kein Graphic/Type, Layer, Zähler oder Boolean. 0: kein aktuelles Objekt.
# Alle 32 Bits bleiben erhalten; <> 0 statt = TRUE oder > 0 prüfen. Ein gespeichertes Ergebnis
# aktualisiert sich nicht selbst. Liest World.Player.Serial; fehlender/zerstörter Player liefert
# 0. Tod ist keine Zerstörung: ein vorhandener Geist behält die Spieler-ID.

SUB Main()
    # id speichert einen Aufruf; HEX formatiert die Serial für das Journal. Kein Objekt wird
    # ausgewählt oder benutzt.

    VAR id = UO.Self()
    UO.Print('ID: ' + HEX(id))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- id speichert einen Aufruf; HEX formatiert die Serial für das Journal. Kein Objekt wird ausgewählt oder benutzt.

### Änderung der ID erkennen

```vb
# Änderung der ID erkennen
#
# Liefert die ID des aktuellen Charakters.
#
# Integer — Serial/ID, kein Graphic/Type, Layer, Zähler oder Boolean. 0: kein aktuelles Objekt.
# Alle 32 Bits bleiben erhalten; <> 0 statt = TRUE oder > 0 prüfen. Ein gespeichertes Ergebnis
# aktualisiert sich nicht selbst. Liest World.Player.Serial; fehlender/zerstörter Player liefert
# 0. Tod ist keine Zerstörung: ein vorhandener Geist behält die Spieler-ID.

SUB Main()
    # before/after werden im Abstand von 250 ms gelesen. WAIT gehört nur zum Beispiel. Gleiche
    # Endwerte schließen zwischenzeitliche Änderungen nicht aus.

    VAR before = UO.Self()
    WAIT(250)
    VAR after = UO.Self()
    IF before <> after THEN
        UO.Print('ID changed: ' + HEX(after))
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- before/after werden im Abstand von 250 ms gelesen. WAIT gehört nur zum Beispiel. Gleiche Endwerte schließen zwischenzeitliche Änderungen nicht aus.

### Vollständige Funktion IsOwnSerial

```vb
# Vollständige Funktion IsOwnSerial
#
# Liefert die ID des aktuellen Charakters.
#
# Integer — Serial/ID, kein Graphic/Type, Layer, Zähler oder Boolean. 0: kein aktuelles Objekt.
# Alle 32 Bits bleiben erhalten; <> 0 statt = TRUE oder > 0 prüfen. Ein gespeichertes Ergebnis
# aktualisiert sich nicht selbst. Liest World.Player.Serial; fehlender/zerstörter Player liefert
# 0. Tod ist keine Zerstörung: ein vorhandener Geist behält die Spieler-ID.

SUB Main()
    # candidate ist die gespeicherte LastTarget-ID. IsOwnSerial(candidate) erwartet eine Serial und
    # liefert Integer Boolean: 1=TRUE für die aktuelle eigene ID ungleich 0, sonst 0=FALSE. Die
    # vollständige Funktion ändert kein Ziel.

    VAR candidate = UO.LastTarget()
    IF IsOwnSerial(candidate) = TRUE THEN
        UO.Print('Own object selected')
    ELSE
        UO.Print('Different object or no own object')
    END IF
END SUB

SUB IsOwnSerial(candidate)
    VAR current = UO.Self()
    RETURN current <> 0 AND current = candidate
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- candidate ist die gespeicherte LastTarget-ID. IsOwnSerial(candidate) erwartet eine Serial und liefert Integer Boolean: 1=TRUE für die aktuelle eigene ID ungleich 0, sonst 0=FALSE. Die vollständige Funktion ändert kein Ziel.
