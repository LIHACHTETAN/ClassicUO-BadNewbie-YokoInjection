# UO.GetParalyzed

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest das dem Client bekannte Lähmungsmerkmal eines Mobiles.

## Genaue Syntax

```text
UO.GetParalyzed() -> Integer
UO.GetParalyzed(value:Any) -> Integer
```

## Parameter

- `value` — Optionale Serial/ID des Mobiles: Ganzzahl, Hex-Zeichenkette, self, lasttarget, anderer Standardalias oder AddObject-Name. Kein graphic/type. Ohne Argument wird self gewählt. Ein unbekannter Alias ergibt 0; es erscheint kein Zielcursor.

## Rückgabewert

Integer Boolean: 1 = TRUE, wenn ein geladenes Mobile IsParalyzed hat; 0 = FALSE, wenn das Merkmal fehlt, das Mobile unbekannt oder gelöscht ist oder das Objekt ein Gegenstand ist. Keine Restdauer; 0 garantiert keine freie Bewegung.

## Verhalten

- Paralyzed prüft das Lähmungsmerkmal. Die Is/Get-Varianten, GetParalisa, Frozen und GetLocked lesen dasselbe Merkmal.
- Die Abfrage liest lokale Daten. Sie verursacht oder heilt keine Lähmung, wartet nicht auf deren Ende und fordert keine Aktualisierung vom Server an.
- Für diese Prüfung sind value = TRUE, value = 1 und IF value gleichwertig. TRUE/FALSE stehen ohne Anführungszeichen. Das Ergebnis ist ein Merkmal, keine Menge oder ID.

## Beispiele

### Self mit TRUE prüfen

```vb
# Self mit TRUE prüfen
#
# Liest das dem Client bekannte Lähmungsmerkmal eines Mobiles.
#
# Integer Boolean: 1 = TRUE, wenn ein geladenes Mobile IsParalyzed hat; 0 = FALSE, wenn das
# Merkmal fehlt, das Mobile unbekannt oder gelöscht ist oder das Objekt ein Gegenstand ist.
# Keine Restdauer; 0 garantiert keine freie Bewegung.

SUB Main()
    # Leere Klammern wählen self. state speichert eine Momentaufnahme; TRUE ist die numerische
    # Konstante 1.
    # FALSE schließt eine Wand, fehlende Ausdauer oder andere Bewegungshindernisse nicht aus.

    VAR state = UO.GetParalyzed()
    IF state = TRUE THEN
        UO.Print('Paralysis flag is set')
    ELSE
        UO.Print('Paralysis flag is absent or unavailable')
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Leere Klammern wählen self. state speichert eine Momentaufnahme; TRUE ist die numerische Konstante 1.
- FALSE schließt eine Wand, fehlende Ausdauer oder andere Bewegungshindernisse nicht aus.

### Das ausgewählte Mobile prüfen

```vb
# Das ausgewählte Mobile prüfen
#
# Liest das dem Client bekannte Lähmungsmerkmal eines Mobiles.
#
# Integer Boolean: 1 = TRUE, wenn ein geladenes Mobile IsParalyzed hat; 0 = FALSE, wenn das
# Merkmal fehlt, das Mobile unbekannt oder gelöscht ist oder das Objekt ein Gegenstand ist.
# Keine Restdauer; 0 garantiert keine freie Bewegung.

SUB Main()
    # target speichert die Serial des letzten Ziels als Hex-Zeichenkette. IsNpc prüft ein geladenes
    # Mobile, einschließlich Spielern.
    # Das Argument wählt genau dieses gespeicherte target. Es öffnet keinen Cursor und ändert
    # lasttarget nicht.

    VAR target = UO.GetSerial('lasttarget')
    IF UO.IsNpc(target) THEN
        VAR state = UO.GetParalyzed(target)
        UO.Print('Selected mobile paralysis 1/0: ' + STR(state))
    ELSE
        UO.Print('No loaded mobile selected')
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- target speichert die Serial des letzten Ziels als Hex-Zeichenkette. IsNpc prüft ein geladenes Mobile, einschließlich Spielern.
- Das Argument wählt genau dieses gespeicherte target. Es öffnet keinen Cursor und ändert lasttarget nicht.

### Mit einer Grenze auf das Ende warten

```vb
# Mit einer Grenze auf das Ende warten
#
# Liest das dem Client bekannte Lähmungsmerkmal eines Mobiles.
#
# Integer Boolean: 1 = TRUE, wenn ein geladenes Mobile IsParalyzed hat; 0 = FALSE, wenn das
# Merkmal fehlt, das Mobile unbekannt oder gelöscht ist oder das Objekt ein Gegenstand ist.
# Keine Restdauer; 0 garantiert keine freie Bewegung.

SUB Main()
    # Höchstens zehn Wartezeiten von 100 ms. Jeder Aufruf ohne Argument liest self erneut.
    # Nach der Schleife wird self separat auf Verfügbarkeit geprüft. Beobachtung für etwa eine
    # Sekunde plus Ausführungszeit; keine garantierte Heilung.

    VAR attempts = 0
    WHILE UO.GetParalyzed() = TRUE AND attempts < 10
        WAIT(100)
        attempts = attempts + 1
    WEND
    IF UO.IsNpc('self') THEN
        IF UO.GetParalyzed() = FALSE THEN
            UO.Print('Paralysis flag is clear')
        ELSE
            UO.Print('Still paralyzed')
        END IF
    ELSE
        UO.Print('Self is unavailable')
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Höchstens zehn Wartezeiten von 100 ms. Jeder Aufruf ohne Argument liest self erneut.
- Nach der Schleife wird self separat auf Verfügbarkeit geprüft. Beobachtung für etwa eine Sekunde plus Ausführungszeit; keine garantierte Heilung.
