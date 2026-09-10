# UO.Followers

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest den Statuszähler des aktuellen Spielers: belegte Kontrollplätze für Begleiter.

## Genaue Syntax

```text
UO.Followers() -> Integer
```

## Parameter

Keine Parameter.

## Rückgabewert

Integer — belegte Kontrollplätze für Begleiter, 0..255 im Modell. 0 kann echt, unbekannt oder fehlender/zerstörter Player sein. Menge, kein Boolean, ID oder type: 1 bedeutet eine Einheit, keinen Erfolg. Keine Objektsuche und kein Array.

## Verhalten

- Keine Argumente. Die angezeigten Signaturen beachten.
- Liest Player.Followers im Spielthread, sofern Player vorhanden und nicht zerstört ist; sonst 0. Keine Ausrüstungssuche, Bonusberechnung, Statusanforderung oder Wartezeit. Ein vorhandener Geist ist kein zerstörter Player.
- PetsCurrent/Followers liest belegte Kontrollplätze aus eigenem Status type >= 3. Ein Tier kann mehrere Plätze belegen; Regeln für beschworene/gezähmte Wesen legt der Server fest. Keine Anzahl sichtbarer Mobiles, Tier-IDs oder naher Tiere.
- CharacterStatus prüft den festen Körper vor Änderungen. Weight stammt aus eigenem erweitertem Status, Plätze ab Typ 3, Luck ab Typ 4, Server-WeightMax ab Typ 5. Kompakte/alte Pakete ohne optionalen Zähler behalten den Cache. Ein neuer Player startet bei null; kein Nachweis frischer Daten.
- RegisterCharacterGetterAliases ergänzt fehlende parameterlose Funktionen und intrinsische Namen. Bestehende Zweige lesen dasselbe Feld. Namen sind unabhängig von Großschreibung; intrinsische Werte ohne Klammern werden neu gelesen, sofern keine Variable sie verdeckt.
- Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.

### Interne Funktionen: vom Aufruf zum Ergebnis

Native Schritte des Cachelesens. CanCarry, LuckAtLeast oder CanAddFollower im Beispiel ist eine vollständige BASIC-Hilfsfunktion, keine versteckte native Aktion. Inventar und Begleiter bleiben unverändert.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ergänzt fehlende parameterlose Funktionen und intrinsische Namen. Bestehende Zweige lesen dasselbe Feld. Namen sind unabhängig von Großschreibung; intrinsische Werte ohne Klammern werden neu gelesen, sofern keine Variable sie verdeckt.

`PetsCurrent Followers GetPetsCurrent GetFollowers`.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `RegisterCharacterGetterAliases`.

#### 2. Invoke

Liest Player.Followers im Spielthread, sofern Player vorhanden und nicht zerstört ist; sonst 0. Keine Ausrüstungssuche, Bonusberechnung, Statusanforderung oder Wartezeit. Ein vorhandener Geist ist kein zerstörter Player.

Invoke liest auf dem Spielthread; Warten kann durch Skriptabbruch enden. Kein Paket, Statusabruf, Zielcursor, Ändern des Attributs oder eingebauter Wartezeitraum.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 3. CharacterStatus

CharacterStatus prüft den festen Körper vor Änderungen. Weight stammt aus eigenem erweitertem Status, Plätze ab Typ 3, Luck ab Typ 4, Server-WeightMax ab Typ 5. Kompakte/alte Pakete ohne optionalen Zähler behalten den Cache. Ein neuer Player startet bei null; kein Nachweis frischer Daten.

PetsCurrent/Followers liest belegte Kontrollplätze aus eigenem Status type >= 3. Ein Tier kann mehrere Plätze belegen; Regeln für beschworene/gezähmte Wesen legt der Server fest. Keine Anzahl sichtbarer Mobiles, Tier-IDs oder naher Tiere.

Projektquelle: `src/ClassicUO.Client/Network/PacketHandlers.cs`; Funktion `CharacterStatus`.

#### 4. Clear

World.Clear entfernt Player. Bis Spieler und Daten wieder vorhanden sind, liefern Aufrufe 0. Ein gespeicherter Wert beweist nach Wiederverbindung keine erfüllte Anforderung.

Integer — belegte Kontrollplätze für Begleiter, 0..255 im Modell. 0 kann echt, unbekannt oder fehlender/zerstörter Player sein. Menge, kein Boolean, ID oder type: 1 bedeutet eine Einheit, keinen Erfolg. Keine Objektsuche und kein Array.

Projektquelle: `src/ClassicUO.Client/Game/World.cs`; Funktion `Clear`.

Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.


## Beispiele

### Gespeicherten Zähler anzeigen

```vb
# Gespeicherten Zähler anzeigen
#
# Liest den Statuszähler des aktuellen Spielers: belegte Kontrollplätze für Begleiter.
#
# Integer — belegte Kontrollplätze für Begleiter, 0..255 im Modell. 0 kann echt, unbekannt oder
# fehlender/zerstörter Player sein. Menge, kein Boolean, ID oder type: 1 bedeutet eine Einheit,
# keinen Erfolg. Keine Objektsuche und kein Array.

SUB Main()
    # value speichert einen parameterlosen Spielerwert; CStr formatiert ihn fürs Journal ohne
    # Bedeutungsänderung.

    VAR value = UO.Followers()
    UO.Print('Followers: ' + CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value speichert einen parameterlosen Spielerwert; CStr formatiert ihn fürs Journal ohne Bedeutungsänderung.

### Änderung beobachten

```vb
# Änderung beobachten
#
# Liest den Statuszähler des aktuellen Spielers: belegte Kontrollplätze für Begleiter.
#
# Integer — belegte Kontrollplätze für Begleiter, 0..255 im Modell. 0 kann echt, unbekannt oder
# fehlender/zerstörter Player sein. Menge, kein Boolean, ID oder type: 1 bedeutet eine Einheit,
# keinen Erfolg. Keine Objektsuche und kein Array.

SUB Main()
    # WAIT(500) trennt before und after um 500 ms. difference kann positiv, null oder negativ sein;
    # Zwischenupdates oder Charakterwechsel können entgehen. Die Wartezeit gehört zum Beispiel.

    VAR before = UO.Followers()
    WAIT(500)
    VAR after = UO.Followers()
    VAR difference = after - before
    UO.Print('Counter change: ' + CStr(difference))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- WAIT(500) trennt before und after um 500 ms. difference kann positiv, null oder negativ sein; Zwischenupdates oder Charakterwechsel können entgehen. Die Wartezeit gehört zum Beispiel.

### Vollständige Entscheidungsfunktion

```vb
# Vollständige Entscheidungsfunktion
#
# Liest den Statuszähler des aktuellen Spielers: belegte Kontrollplätze für Begleiter.
#
# Integer — belegte Kontrollplätze für Begleiter, 0..255 im Modell. 0 kann echt, unbekannt oder
# fehlender/zerstörter Player sein. Menge, kein Boolean, ID oder type: 1 bedeutet eine Einheit,
# keinen Erfolg. Keine Objektsuche und kein Array.

SUB Main()
    # CanAddFollower(extraSlots) nimmt benötigte Kontrollplätze; 2 kann ein einziges Wesen mit zwei
    # Plätzen meinen. Weist negative Eingabe, fehlenden Player oder maximum <= 0 zurück, liest
    # Belegung/Grenze und liefert Integer Boolean 1=TRUE oder 0=FALSE für extraSlots <= maximum -
    # current. Kein Additionsüberlauf; Überschreitung ergibt auch bei null false. Prüft weder
    # Eigentümer, Zähmskill noch Serverfreigabe. Zwischenwerte können aktualisiert werden.

    IF CanAddFollower(2) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB CanAddFollower(extraSlots)
    IF extraSlots < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR current = UO.Followers()
    VAR maximum = UO.PetsMax()
    IF maximum <= 0 THEN
        RETURN FALSE
    END IF
    RETURN extraSlots <= maximum - current
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- CanAddFollower(extraSlots) nimmt benötigte Kontrollplätze; 2 kann ein einziges Wesen mit zwei Plätzen meinen. Weist negative Eingabe, fehlenden Player oder maximum <= 0 zurück, liest Belegung/Grenze und liefert Integer Boolean 1=TRUE oder 0=FALSE für extraSlots <= maximum - current. Kein Additionsüberlauf; Überschreitung ergibt auch bei null false. Prüft weder Eigentümer, Zähmskill noch Serverfreigabe. Zwischenwerte können aktualisiert werden.
