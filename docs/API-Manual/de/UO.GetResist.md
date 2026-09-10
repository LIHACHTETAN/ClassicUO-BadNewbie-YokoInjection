# UO.GetResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest einen Widerstand des eigenen Spielers anhand einer Zahl oder eines Namens.

## Genaue Syntax

```text
UO.GetResist(resistance:Any) -> Integer
```

## Parameter

- `resistance` — resistance erforderlich: Zahlen 0=physical, 1=fire, 2=cold, 3=poison, 4=energy; Namen physical/phys/armor, fire, cold, poison, energy. Großschreibung und äußere Leerzeichen werden ignoriert. Kein serial, type, hue, Zielcursor oder zweites Argument.

## Rückgabewert

Integer — vorzeichenbehafteter Statuswert, -32768..32767 im Clientmodell. Negative Werte bleiben erhalten. 0 kann ein echter Wert, ein unbekanntes Feld oder fehlender/zerstörter Player sein; GetResist liefert auch bei unbekannter Auswahl 0. Kein Boolean, ID, Fertigkeitswert oder Höchstwert. 1 bedeutet einen Punkt, keinen Erfolg.

## Verhalten

- Zuerst wird die Wertart geprüft: "1" und "0" sind unbekannte Namen und liefern 0. Nichttextuelle Decimal-Werte werden Richtung null gekürzt: 1.9 -> fire, -0.9 -> physical. TRUE=1 wählt fire, FALSE=0 physical; Array/Unit werden ebenfalls 0. Explizite ganze Zahl oder gültigen Namen verwenden. Keine AddObject-Auflösung.
- GetResistance wählt genau einen Bridge-Getter; unbekannte Zahlen/Namen liefern Integer 0 ohne Feldzugriff. Keine atomare Abfrage aller fünf Werte und keine Änderung des Widerstands.
- PhysicalResistance ist das Rüstungs-/Statusfeld des Servers: unter klassischen Regeln ein Rüstungswert, bei Widerstandsregeln physischer Widerstand. Keine Umrechnung der Regeln oder Berechnung prozentualer Schadensminderung. Armor und physische Aliasnamen lesen dasselbe Feld.
- Elementare Felder kommen in CharacterStatus (0x11), type >= 4. Der Aufruf prüft keine Serverära. Ein kompaktes/älteres Paket ohne diese Felder behält den bisherigen Cache; ein neuer Player beginnt mit 0. Giftwiderstand ist nicht Poisoned; keines dieser Felder ist Resisting Spells.
- CharacterStatus prüft den festen Paketkörper vor Änderungen und wandelt Widerstandswörter in vorzeichenbehaftetes Int16 um. Ein verkürzter Körper verändert keine alten Daten. Der optionale Type-6-Anhang behält sein Verhalten; dessen Widerstandsmaxima werden hier nicht gelesen.
- Invoke liest auf dem Spielthread; Warten kann durch Skriptabbruch enden. Kein Paket, Statusabruf, Zielcursor, Ändern des Attributs oder eingebauter Wartezeitraum.
- Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.

### Interne Funktionen: vom Aufruf zum Ergebnis

Native Schritte des lokalen Lesens. ResistanceAtLeast unten ist eine vollständig definierte BASIC-Hilfsfunktion, keine versteckte API und kein Anlegen von Schutzkleidung.

#### 1. RegisterCharacterGetterAliases

Registriert GetResist(resistance) und UO.GetResist(resistance) mit einem Argument für GetResistance. Für diese Auswahl gibt es keinen parameterlosen intrinsischen Wert.

resistance erforderlich: Zahlen 0=physical, 1=fire, 2=cold, 3=poison, 4=energy; Namen physical/phys/armor, fire, cold, poison, energy. Großschreibung und äußere Leerzeichen werden ignoriert. Kein serial, type, hue, Zielcursor oder zweites Argument.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `RegisterCharacterGetterAliases`.

#### 2. GetResistance

Zuerst wird die Wertart geprüft: "1" und "0" sind unbekannte Namen und liefern 0. Nichttextuelle Decimal-Werte werden Richtung null gekürzt: 1.9 -> fire, -0.9 -> physical. TRUE=1 wählt fire, FALSE=0 physical; Array/Unit werden ebenfalls 0. Explizite ganze Zahl oder gültigen Namen verwenden. Keine AddObject-Auflösung.

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`. GetResistance wählt genau einen Bridge-Getter; unbekannte Zahlen/Namen liefern Integer 0 ohne Feldzugriff. Keine atomare Abfrage aller fünf Werte und keine Änderung des Widerstands.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `GetResistance`.

#### 3. ToInt

ToInt erhält hier nur nichttextuelle Selektoren. Integer bleibt, Decimal wird Richtung null gekürzt, Array/Unit ergeben 0. Das Ergebnis ist ein Auswahlindex, kein Widerstand. Textnamen behandelt GetResistance.

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/NumberConversions.cs`; Funktion `ToInt`.

#### 4. Invoke

Invoke liest das oben zugeordnete Player-Feld mit Vorzeichen. Fehlender/zerstörter Player ergibt 0. Keine Statusanforderung oder Wartezeit auf neue Daten.

Invoke liest auf dem Spielthread; Warten kann durch Skriptabbruch enden. Kein Paket, Statusabruf, Zielcursor, Ändern des Attributs oder eingebauter Wartezeitraum.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 5. CharacterStatus

CharacterStatus prüft den festen Paketkörper vor Änderungen und wandelt Widerstandswörter in vorzeichenbehaftetes Int16 um. Ein verkürzter Körper verändert keine alten Daten. Der optionale Type-6-Anhang behält sein Verhalten; dessen Widerstandsmaxima werden hier nicht gelesen.

PhysicalResistance ist das Rüstungs-/Statusfeld des Servers: unter klassischen Regeln ein Rüstungswert, bei Widerstandsregeln physischer Widerstand. Keine Umrechnung der Regeln oder Berechnung prozentualer Schadensminderung. Armor und physische Aliasnamen lesen dasselbe Feld. Elementare Felder kommen in CharacterStatus (0x11), type >= 4. Der Aufruf prüft keine Serverära. Ein kompaktes/älteres Paket ohne diese Felder behält den bisherigen Cache; ein neuer Player beginnt mit 0. Giftwiderstand ist nicht Poisoned; keines dieser Felder ist Resisting Spells.

Projektquelle: `src/ClassicUO.Client/Network/PacketHandlers.cs`; Funktion `CharacterStatus`.

#### 6. Clear

World.Clear entfernt Player. Bis Spieler und Daten wieder vorhanden sind, liefern Aufrufe 0. Ein gespeicherter Wert beweist nach Wiederverbindung keine erfüllte Anforderung.

Integer — vorzeichenbehafteter Statuswert, -32768..32767 im Clientmodell. Negative Werte bleiben erhalten. 0 kann ein echter Wert, ein unbekanntes Feld oder fehlender/zerstörter Player sein; GetResist liefert auch bei unbekannter Auswahl 0. Kein Boolean, ID, Fertigkeitswert oder Höchstwert. 1 bedeutet einen Punkt, keinen Erfolg.

Projektquelle: `src/ClassicUO.Client/Game/World.cs`; Funktion `Clear`.

Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.


## Beispiele

### Namen mit gemischter Großschreibung wählen

```vb
# Namen mit gemischter Großschreibung wählen
#
# Liest einen Widerstand des eigenen Spielers anhand einer Zahl oder eines Namens.
#
# Integer — vorzeichenbehafteter Statuswert, -32768..32767 im Clientmodell. Negative Werte
# bleiben erhalten. 0 kann ein echter Wert, ein unbekanntes Feld oder fehlender/zerstörter
# Player sein; GetResist liefert auch bei unbekannter Auswahl 0. Kein Boolean, ID,
# Fertigkeitswert oder Höchstwert. 1 bedeutet einen Punkt, keinen Erfolg.

SUB Main()
    # resistance=" FiRe " wählt Feuer nach Entfernen äußerer Leerzeichen, ohne Beachtung der
    # Großschreibung. value bleibt vorzeichenbehaftet; kein Zielcursor.

    VAR value = UO.GetResist(' FiRe ')
    UO.Print('Fire resistance: ' + CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- resistance=" FiRe " wählt Feuer nach Entfernen äußerer Leerzeichen, ohne Beachtung der Großschreibung. value bleibt vorzeichenbehaftet; kein Zielcursor.

### Zahl und Namen vergleichen

```vb
# Zahl und Namen vergleichen
#
# Liest einen Widerstand des eigenen Spielers anhand einer Zahl oder eines Namens.
#
# Integer — vorzeichenbehafteter Statuswert, -32768..32767 im Clientmodell. Negative Werte
# bleiben erhalten. 0 kann ein echter Wert, ein unbekanntes Feld oder fehlender/zerstörter
# Player sein; GetResist liefert auch bei unbekannter Auswahl 0. Kein Boolean, ID,
# Fertigkeitswert oder Höchstwert. 1 bedeutet einen Punkt, keinen Erfolg.

SUB Main()
    # 2 wählt Kälte, "poison" Gift. Keine serials. Der Vergleich zweier Momentaufnahmen ergibt
    # Boolean; Giftwiderstand ist kein Vergiftungsflag.

    VAR cold = UO.GetResist(2)
    VAR poison = UO.GetResist('poison')
    IF cold < poison THEN
        UO.Print('Cold resistance is lower')
    ELSE
        UO.Print('Cold resistance is equal or higher')
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- 2 wählt Kälte, "poison" Gift. Keine serials. Der Vergleich zweier Momentaufnahmen ergibt Boolean; Giftwiderstand ist kein Vergiftungsflag.

### Vollständige Mindestwiderstandsprüfung

```vb
# Vollständige Mindestwiderstandsprüfung
#
# Liest einen Widerstand des eigenen Spielers anhand einer Zahl oder eines Namens.
#
# Integer — vorzeichenbehafteter Statuswert, -32768..32767 im Clientmodell. Negative Werte
# bleiben erhalten. 0 kann ein echter Wert, ein unbekanntes Feld oder fehlender/zerstörter
# Player sein; GetResist liefert auch bei unbekannter Auswahl 0. Kein Boolean, ID,
# Fertigkeitswert oder Höchstwert. 1 bedeutet einen Punkt, keinen Erfolg.

SUB Main()
    # minimum=50 ist eine Beispielanforderung, kein Maximum. ResistanceAtLeast weist fehlenden
    # Player zurück, liest einmal und liefert Integer Boolean 1=TRUE oder 0=FALSE für value >=
    # minimum. Der Widerstand ist kein Boolean. Vollständige Definition unten.
    # selector wird unverändert an GetResist übergeben; das Beispiel nutzt "fire". Die Funktion
    # prüft Player, aber keine beliebige Auswahl und keine Aktualität. Einen oben aufgeführten
    # Selektor verwenden.

    IF ResistanceAtLeast('fire', 50) = TRUE THEN
        UO.Print('Local fire resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(selector, minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetResist(selector)
    RETURN value >= minimum
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- minimum=50 ist eine Beispielanforderung, kein Maximum. ResistanceAtLeast weist fehlenden Player zurück, liest einmal und liefert Integer Boolean 1=TRUE oder 0=FALSE für value >= minimum. Der Widerstand ist kein Boolean. Vollständige Definition unten.
- selector wird unverändert an GetResist übergeben; das Beispiel nutzt "fire". Die Funktion prüft Player, aber keine beliebige Auswahl und keine Aktualität. Einen oben aufgeführten Selektor verwenden.
