# UO.PoisonResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest das Widerstandsfeld des aktuellen Spielers: Gift.

## Genaue Syntax

```text
UO.PoisonResist() -> Integer
```

## Parameter

Keine Parameter.

## Rückgabewert

Integer — vorzeichenbehafteter Statuswert, -32768..32767 im Clientmodell. Negative Werte bleiben erhalten. 0 kann ein echter Wert, ein unbekanntes Feld oder fehlender/zerstörter Player sein; GetResist liefert auch bei unbekannter Auswahl 0. Kein Boolean, ID, Fertigkeitswert oder Höchstwert. 1 bedeutet einen Punkt, keinen Erfolg.

## Verhalten

- Keine Argumente. Die angezeigten Signaturen beachten.
- Liest Player.PoisonResistance im Spielthread, sofern Player vorhanden und nicht zerstört ist; sonst 0. Keine Ausrüstungssuche, Bonusberechnung, Statusanforderung oder Wartezeit. Ein vorhandener Geist ist kein zerstörter Player.
- Elementare Felder kommen in CharacterStatus (0x11), type >= 4. Der Aufruf prüft keine Serverära. Ein kompaktes/älteres Paket ohne diese Felder behält den bisherigen Cache; ein neuer Player beginnt mit 0. Giftwiderstand ist nicht Poisoned; keines dieser Felder ist Resisting Spells.
- CharacterStatus prüft den festen Paketkörper vor Änderungen und wandelt Widerstandswörter in vorzeichenbehaftetes Int16 um. Ein verkürzter Körper verändert keine alten Daten. Der optionale Type-6-Anhang behält sein Verhalten; dessen Widerstandsmaxima werden hier nicht gelesen.
- Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.
- RegisterCharacterGetterAliases ergänzt fehlende parameterlose Funktionen und intrinsische Namen. Bestehende Zweige lesen dasselbe Feld. Namen sind unabhängig von Großschreibung; intrinsische Werte ohne Klammern werden neu gelesen, sofern keine Variable sie verdeckt.

### Interne Funktionen: vom Aufruf zum Ergebnis

Native Schritte des lokalen Lesens. ResistanceAtLeast unten ist eine vollständig definierte BASIC-Hilfsfunktion, keine versteckte API und kein Anlegen von Schutzkleidung.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ergänzt fehlende parameterlose Funktionen und intrinsische Namen. Bestehende Zweige lesen dasselbe Feld. Namen sind unabhängig von Großschreibung; intrinsische Werte ohne Klammern werden neu gelesen, sofern keine Variable sie verdeckt.

`PoisonResist ResistPoison GetPoisonResist GetResistPoison`.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `RegisterCharacterGetterAliases`.

#### 2. Invoke

Liest Player.PoisonResistance im Spielthread, sofern Player vorhanden und nicht zerstört ist; sonst 0. Keine Ausrüstungssuche, Bonusberechnung, Statusanforderung oder Wartezeit. Ein vorhandener Geist ist kein zerstörter Player.

Invoke liest auf dem Spielthread; Warten kann durch Skriptabbruch enden. Kein Paket, Statusabruf, Zielcursor, Ändern des Attributs oder eingebauter Wartezeitraum.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 3. CharacterStatus

CharacterStatus prüft den festen Paketkörper vor Änderungen und wandelt Widerstandswörter in vorzeichenbehaftetes Int16 um. Ein verkürzter Körper verändert keine alten Daten. Der optionale Type-6-Anhang behält sein Verhalten; dessen Widerstandsmaxima werden hier nicht gelesen.

Elementare Felder kommen in CharacterStatus (0x11), type >= 4. Der Aufruf prüft keine Serverära. Ein kompaktes/älteres Paket ohne diese Felder behält den bisherigen Cache; ein neuer Player beginnt mit 0. Giftwiderstand ist nicht Poisoned; keines dieser Felder ist Resisting Spells.

Projektquelle: `src/ClassicUO.Client/Network/PacketHandlers.cs`; Funktion `CharacterStatus`.

#### 4. Clear

World.Clear entfernt Player. Bis Spieler und Daten wieder vorhanden sind, liefern Aufrufe 0. Ein gespeicherter Wert beweist nach Wiederverbindung keine erfüllte Anforderung.

Integer — vorzeichenbehafteter Statuswert, -32768..32767 im Clientmodell. Negative Werte bleiben erhalten. 0 kann ein echter Wert, ein unbekanntes Feld oder fehlender/zerstörter Player sein; GetResist liefert auch bei unbekannter Auswahl 0. Kein Boolean, ID, Fertigkeitswert oder Höchstwert. 1 bedeutet einen Punkt, keinen Erfolg.

Projektquelle: `src/ClassicUO.Client/Game/World.cs`; Funktion `Clear`.

Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.


## Beispiele

### Cachewert ausgeben

```vb
# Cachewert ausgeben
#
# Liest das Widerstandsfeld des aktuellen Spielers: Gift.
#
# Integer — vorzeichenbehafteter Statuswert, -32768..32767 im Clientmodell. Negative Werte
# bleiben erhalten. 0 kann ein echter Wert, ein unbekanntes Feld oder fehlender/zerstörter
# Player sein; GetResist liefert auch bei unbekannter Auswahl 0. Kein Boolean, ID,
# Fertigkeitswert oder Höchstwert. 1 bedeutet einen Punkt, keinen Erfolg.

SUB Main()
    # value speichert einen parameterlosen Spielerwert; CStr formatiert ihn fürs Journal.

    VAR value = UO.PoisonResist()
    UO.Print('PoisonResistance: ' + CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value speichert einen parameterlosen Spielerwert; CStr formatiert ihn fürs Journal.

### Zwei Beobachtungen vergleichen

```vb
# Zwei Beobachtungen vergleichen
#
# Liest das Widerstandsfeld des aktuellen Spielers: Gift.
#
# Integer — vorzeichenbehafteter Statuswert, -32768..32767 im Clientmodell. Negative Werte
# bleiben erhalten. 0 kann ein echter Wert, ein unbekanntes Feld oder fehlender/zerstörter
# Player sein; GetResist liefert auch bei unbekannter Auswahl 0. Kein Boolean, ID,
# Fertigkeitswert oder Höchstwert. 1 bedeutet einen Punkt, keinen Erfolg.

SUB Main()
    # WAIT(500) trennt before und after um 500 ms; difference kann negativ sein. Zwischenupdates
    # können unbemerkt bleiben. Die Wartezeit gehört zum Beispiel.

    VAR before = UO.PoisonResist()
    WAIT(500)
    VAR after = UO.PoisonResist()
    VAR difference = after - before
    UO.Print('Resistance change: ' + CStr(difference))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- WAIT(500) trennt before und after um 500 ms; difference kann negativ sein. Zwischenupdates können unbemerkt bleiben. Die Wartezeit gehört zum Beispiel.

### Vollständige Mindestwiderstandsprüfung

```vb
# Vollständige Mindestwiderstandsprüfung
#
# Liest das Widerstandsfeld des aktuellen Spielers: Gift.
#
# Integer — vorzeichenbehafteter Statuswert, -32768..32767 im Clientmodell. Negative Werte
# bleiben erhalten. 0 kann ein echter Wert, ein unbekanntes Feld oder fehlender/zerstörter
# Player sein; GetResist liefert auch bei unbekannter Auswahl 0. Kein Boolean, ID,
# Fertigkeitswert oder Höchstwert. 1 bedeutet einen Punkt, keinen Erfolg.

SUB Main()
    # minimum=50 ist eine Beispielanforderung, kein Maximum. ResistanceAtLeast weist fehlenden
    # Player zurück, liest einmal und liefert Integer Boolean 1=TRUE oder 0=FALSE für value >=
    # minimum. Der Widerstand ist kein Boolean. Vollständige Definition unten.

    IF ResistanceAtLeast(50) = TRUE THEN
        UO.Print('Local resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.PoisonResist()
    RETURN value >= minimum
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- minimum=50 ist eine Beispielanforderung, kein Maximum. ResistanceAtLeast weist fehlenden Player zurück, liest einmal und liefert Integer Boolean 1=TRUE oder 0=FALSE für value >= minimum. Der Widerstand ist kein Boolean. Vollständige Definition unten.
