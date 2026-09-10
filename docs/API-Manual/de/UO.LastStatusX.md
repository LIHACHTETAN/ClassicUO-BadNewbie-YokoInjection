# UO.LastStatusX

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liefert die gespeicherte X-Koordinate des zuletzt angenommenen Statusobjekts.

## Genaue Syntax

```text
UO.LastStatusX() -> Integer
```

## Parameter

Keine Parameter.

## Rückgabewert

Integer — gespeicherte X-Koordinate, kein Fensterpixel und kein Boolean. Vor dem ersten Status oder nach dem Leeren 0; auch eine echte Koordinate darf 0 sein. Fehlende Daten mit UO.LastStatus() unterscheiden.

## Verhalten

- Keine Parameter. Lesen sendet keine Pakete, öffnet kein Fenster und wartet auf keine Antwort. UO.GetStatus(id), RequestStats und UpdateObject fordern Daten an; das Senden verändert LastStatus nicht.
- Ein angenommener 0x11-Paketstatus speichert Serial und bekannte X/Y gemeinsam in World für alle Skripte. Unbekannte/zerstörte Objekte und unvollständige Basispakete ersetzen den Eintrag nicht. Spätere Statuspakete anderer Objekte können ihn ersetzen.
- X/Y stammen von Entity beim Empfang, nicht von der aktuellen Position. Bei Mobiles sind es Weltzellen; Gegenstände in Behältern können Inhaltskoordinaten besitzen. Das Statuspaket enthält selbst keine X/Y. Spätere Bewegung/Entfernung ändert den gespeicherten Stand nicht; World.Clear setzt ihn zurück. GetX/GetY lesen die aktuelle Position vorhandener Objekte.
- Getrennte Aufrufe sind nicht atomar; dazwischen kann ein Update eintreffen. Dieselbe Serial beweist keine frische Antwort auf die eigene Anfrage. laststatus ohne Klammern ist ein dynamischer eingebauter Wert, sofern keine Skriptvariable ihn verdeckt; UO.LastStatus() ist die registrierte Funktion.

### Interne Funktionen: vom Aufruf zum Ergebnis

Dies sind die tatsächlichen internen C#-Schritte. ReadSavedStatus ist eine vollständig definierte Hilfsfunktion im Beispiel, kein verborgener integrierter Befehl.

#### 1. CharacterStatus

CharacterStatus prüft das Basispaket und Entity über World.Get, aktualisiert Statusfelder und speichert Serial/X/Y. Die Position kommt von Entity, nicht aus dem Statuspaket.

Integer — gespeicherte X-Koordinate, kein Fensterpixel und kein Boolean. Vor dem ersten Status oder nach dem Leeren 0; auch eine echte Koordinate darf 0 sein. Fehlende Daten mit UO.LastStatus() unterscheiden.

Projektquelle: `src/ClassicUO.Client/Network/PacketHandlers.cs`; Funktion `CharacterStatus`.

#### 2. LastStatusX

ExecuteStealthCompatibility liefert die Bridge-Serial als Integer. LastStatusX/LastStatusY verwenden IStatusSnapshotBridge; eine ältere externe Bridge ohne diese Schnittstelle behält GetX/GetY bei.

Integer — gespeicherte X-Koordinate, kein Fensterpixel und kein Boolean. Vor dem ersten Status oder nach dem Leeren 0; auch eine echte Koordinate darf 0 sein. Fehlende Daten mit UO.LastStatus() unterscheiden.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `LastStatusX`.

#### 3. Invoke

Invoke liest World auf dem Spielthread unter Beachtung des Skriptabbruchs. Kein Warten auf Netzwerkantworten und keine Statusänderung.

Keine Parameter. Lesen sendet keine Pakete, öffnet kein Fenster und wartet auf keine Antwort. UO.GetStatus(id), RequestStats und UpdateObject fordern Daten an; das Senden verändert LastStatus nicht.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 4. Clear

Clear setzt Serial und beide Koordinaten auf 0, auch beim Erhalt laufender Skripte.

X/Y stammen von Entity beim Empfang, nicht von der aktuellen Position. Bei Mobiles sind es Weltzellen; Gegenstände in Behältern können Inhaltskoordinaten besitzen. Das Statuspaket enthält selbst keine X/Y. Spätere Bewegung/Entfernung ändert den gespeicherten Stand nicht; World.Clear setzt ihn zurück. GetX/GetY lesen die aktuelle Position vorhandener Objekte.

Projektquelle: `src/ClassicUO.Client/Game/World.cs`; Funktion `Clear`.

Getrennte Aufrufe sind nicht atomar; dazwischen kann ein Update eintreffen. Dieselbe Serial beweist keine frische Antwort auf die eigene Anfrage. laststatus ohne Klammern ist ein dynamischer eingebauter Wert, sofern keine Skriptvariable ihn verdeckt; UO.LastStatus() ist die registrierte Funktion.


## Beispiele

### Letzten Wert lesen

```vb
# Letzten Wert lesen
#
# Liefert die gespeicherte X-Koordinate des zuletzt angenommenen Statusobjekts.
#
# Integer — gespeicherte X-Koordinate, kein Fensterpixel und kein Boolean. Vor dem ersten Status
# oder nach dem Leeren 0; auch eine echte Koordinate darf 0 sein. Fehlende Daten mit
# UO.LastStatus() unterscheiden.

SUB Main()
    # Einmal lesen. HEX zeigt Serials hexadezimal, CStr zeigt eine numerische Koordinate. Es wird
    # kein Objekt ausgewählt.

    VAR value = UO.LastStatusX()
    UO.Print('Saved value: ' + CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Einmal lesen. HEX zeigt Serials hexadezimal, CStr zeigt eine numerische Koordinate. Es wird kein Objekt ausgewählt.

### Status anfordern und bekannte Daten lesen

```vb
# Status anfordern und bekannte Daten lesen
#
# Liefert die gespeicherte X-Koordinate des zuletzt angenommenen Statusobjekts.
#
# Integer — gespeicherte X-Koordinate, kein Fensterpixel und kein Boolean. Vor dem ersten Status
# oder nach dem Leeren 0; auch eine echte Koordinate darf 0 sein. Fehlende Daten mit
# UO.LastStatus() unterscheiden.

SUB Main()
    # subject ist die Serial von self. 500 Millisekunden sind eine Beispielpause, keine
    # Antwortgarantie. Der angezeigte Stand kann alt sein oder ein anderes Objekt betreffen.

    VAR subject = UO.Self()
    IF subject <> 0 THEN
        UO.GetStatus(subject)
        WAIT(500)
        VAR value = UO.LastStatusX()
        UO.Print('Known value: ' + CStr(value))
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- subject ist die Serial von self. 500 Millisekunden sind eine Beispielpause, keine Antwortgarantie. Der angezeigte Stand kann alt sein oder ein anderes Objekt betreffen.

### Vollständige Hilfsfunktion ReadSavedStatus

```vb
# Vollständige Hilfsfunktion ReadSavedStatus
#
# Liefert die gespeicherte X-Koordinate des zuletzt angenommenen Statusobjekts.
#
# Integer — gespeicherte X-Koordinate, kein Fensterpixel und kein Boolean. Vor dem ersten Status
# oder nach dem Leeren 0; auch eine echte Koordinate darf 0 sein. Fehlende Daten mit
# UO.LastStatus() unterscheiden.

SUB Main()
    # expectedId ist die in Main gespeicherte Serial. Die Hilfsfunktion steht vollständig unten; -1
    # bedeutet einen nicht mehr ausgewählten Eintrag und ist kein Rückgabecode der eigentlichen
    # Funktion. Vorher-/Nachher-Prüfungen verringern Vermischungen, garantieren aber keine
    # Atomarität bei Updates derselben Serial.

    VAR expectedId = UO.LastStatus()
    IF expectedId <> 0 THEN
        VAR value = ReadSavedStatus(expectedId)
        UO.Print('Checked value: ' + CStr(value))
    END IF
END SUB

SUB ReadSavedStatus(expectedId)
    IF expectedId = 0 OR UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    VAR value = UO.LastStatusX()
    IF UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- expectedId ist die in Main gespeicherte Serial. Die Hilfsfunktion steht vollständig unten; -1 bedeutet einen nicht mehr ausgewählten Eintrag und ist kein Rückgabecode der eigentlichen Funktion. Vorher-/Nachher-Prüfungen verringern Vermischungen, garantieren aber keine Atomarität bei Updates derselben Serial.
