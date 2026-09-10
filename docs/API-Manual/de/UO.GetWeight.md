# UO.GetWeight

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest den Statuszähler des aktuellen Spielers: aktuelles Gewicht in Stones.

## Genaue Syntax

```text
UO.GetWeight() -> Integer
```

## Parameter

Keine Parameter.

## Rückgabewert

Integer — aktuelles Gewicht in Stones, 0..65535 im Modell. 0 kann echt, unbekannt oder fehlender/zerstörter Player sein. Menge, kein Boolean, ID oder type: 1 bedeutet eine Einheit, keinen Erfolg. Keine Objektsuche und kein Array.

## Verhalten

- Keine Argumente. Die angezeigten Signaturen beachten.
- Liest Player.Weight im Spielthread, sofern Player vorhanden und nicht zerstört ist; sonst 0. Keine Ausrüstungssuche, Bonusberechnung, Statusanforderung oder Wartezeit. Ein vorhandener Geist ist kein zerstörter Player.
- Weight liest das vom Server gemeldete Gesamtgewicht in Stones. Welche Körper-, Ausrüstungs- und Taschengewichte eingeschlossen sind, bestimmt der Shard. Keine Containersuche, Gewichtssumme oder Aktualisierung geschlossener Taschen. Weder Weight eines einzelnen Gegenstands noch Itemanzahl.
- CharacterStatus prüft den festen Körper vor Änderungen. Weight stammt aus eigenem erweitertem Status, Plätze ab Typ 3, Luck ab Typ 4, Server-WeightMax ab Typ 5. Kompakte/alte Pakete ohne optionalen Zähler behalten den Cache. Ein neuer Player startet bei null; kein Nachweis frischer Daten.
- RegisterCharacterGetterAliases ergänzt fehlende parameterlose Funktionen und intrinsische Namen. Bestehende Zweige lesen dasselbe Feld. Namen sind unabhängig von Großschreibung; intrinsische Werte ohne Klammern werden neu gelesen, sofern keine Variable sie verdeckt.
- Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.

### Interne Funktionen: vom Aufruf zum Ergebnis

Native Schritte des Cachelesens. CanCarry, LuckAtLeast oder CanAddFollower im Beispiel ist eine vollständige BASIC-Hilfsfunktion, keine versteckte native Aktion. Inventar und Begleiter bleiben unverändert.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ergänzt fehlende parameterlose Funktionen und intrinsische Namen. Bestehende Zweige lesen dasselbe Feld. Namen sind unabhängig von Großschreibung; intrinsische Werte ohne Klammern werden neu gelesen, sofern keine Variable sie verdeckt.

`Weight GetWeight`.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `RegisterCharacterGetterAliases`.

#### 2. Invoke

Liest Player.Weight im Spielthread, sofern Player vorhanden und nicht zerstört ist; sonst 0. Keine Ausrüstungssuche, Bonusberechnung, Statusanforderung oder Wartezeit. Ein vorhandener Geist ist kein zerstörter Player.

Invoke liest auf dem Spielthread; Warten kann durch Skriptabbruch enden. Kein Paket, Statusabruf, Zielcursor, Ändern des Attributs oder eingebauter Wartezeitraum.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 3. CharacterStatus

CharacterStatus prüft den festen Körper vor Änderungen. Weight stammt aus eigenem erweitertem Status, Plätze ab Typ 3, Luck ab Typ 4, Server-WeightMax ab Typ 5. Kompakte/alte Pakete ohne optionalen Zähler behalten den Cache. Ein neuer Player startet bei null; kein Nachweis frischer Daten.

Weight liest das vom Server gemeldete Gesamtgewicht in Stones. Welche Körper-, Ausrüstungs- und Taschengewichte eingeschlossen sind, bestimmt der Shard. Keine Containersuche, Gewichtssumme oder Aktualisierung geschlossener Taschen. Weder Weight eines einzelnen Gegenstands noch Itemanzahl.

Projektquelle: `src/ClassicUO.Client/Network/PacketHandlers.cs`; Funktion `CharacterStatus`.

#### 4. Clear

World.Clear entfernt Player. Bis Spieler und Daten wieder vorhanden sind, liefern Aufrufe 0. Ein gespeicherter Wert beweist nach Wiederverbindung keine erfüllte Anforderung.

Integer — aktuelles Gewicht in Stones, 0..65535 im Modell. 0 kann echt, unbekannt oder fehlender/zerstörter Player sein. Menge, kein Boolean, ID oder type: 1 bedeutet eine Einheit, keinen Erfolg. Keine Objektsuche und kein Array.

Projektquelle: `src/ClassicUO.Client/Game/World.cs`; Funktion `Clear`.

Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.


## Beispiele

### Gespeicherten Zähler anzeigen

```vb
# Gespeicherten Zähler anzeigen
#
# Liest den Statuszähler des aktuellen Spielers: aktuelles Gewicht in Stones.
#
# Integer — aktuelles Gewicht in Stones, 0..65535 im Modell. 0 kann echt, unbekannt oder
# fehlender/zerstörter Player sein. Menge, kein Boolean, ID oder type: 1 bedeutet eine Einheit,
# keinen Erfolg. Keine Objektsuche und kein Array.

SUB Main()
    # value speichert einen parameterlosen Spielerwert; CStr formatiert ihn fürs Journal ohne
    # Bedeutungsänderung.

    VAR value = UO.GetWeight()
    UO.Print('Weight: ' + CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value speichert einen parameterlosen Spielerwert; CStr formatiert ihn fürs Journal ohne Bedeutungsänderung.

### Änderung beobachten

```vb
# Änderung beobachten
#
# Liest den Statuszähler des aktuellen Spielers: aktuelles Gewicht in Stones.
#
# Integer — aktuelles Gewicht in Stones, 0..65535 im Modell. 0 kann echt, unbekannt oder
# fehlender/zerstörter Player sein. Menge, kein Boolean, ID oder type: 1 bedeutet eine Einheit,
# keinen Erfolg. Keine Objektsuche und kein Array.

SUB Main()
    # WAIT(500) trennt before und after um 500 ms. difference kann positiv, null oder negativ sein;
    # Zwischenupdates oder Charakterwechsel können entgehen. Die Wartezeit gehört zum Beispiel.

    VAR before = UO.GetWeight()
    WAIT(500)
    VAR after = UO.GetWeight()
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
# Liest den Statuszähler des aktuellen Spielers: aktuelles Gewicht in Stones.
#
# Integer — aktuelles Gewicht in Stones, 0..65535 im Modell. 0 kann echt, unbekannt oder
# fehlender/zerstörter Player sein. Menge, kein Boolean, ID oder type: 1 bedeutet eine Einheit,
# keinen Erfolg. Keine Objektsuche und kein Array.

SUB Main()
    # CanCarry(extra) nimmt zusätzliches Gewicht in Stones; 10 ist ein Beispiel, keine Stapelanzahl.
    # Negatives extra, fehlender Player oder maximum <= 0 werden abgewiesen. Liest aktuell/Maximum
    # und liefert Integer Boolean 1=TRUE oder 0=FALSE für extra <= maximum - current. Subtraktion
    # vermeidet Überlauf von current + extra. Überlast ergibt auch bei extra=0 false. Lokale
    # Schätzung, keine Serverfreigabe; nicht atomare Lesezugriffe, Gewicht 0 kann unbekannt sein.

    IF CanCarry(10) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB CanCarry(extra)
    IF extra < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR current = UO.GetWeight()
    VAR maximum = UO.MaxWeight()
    IF maximum <= 0 THEN
        RETURN FALSE
    END IF
    RETURN extra <= maximum - current
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- CanCarry(extra) nimmt zusätzliches Gewicht in Stones; 10 ist ein Beispiel, keine Stapelanzahl. Negatives extra, fehlender Player oder maximum <= 0 werden abgewiesen. Liest aktuell/Maximum und liefert Integer Boolean 1=TRUE oder 0=FALSE für extra <= maximum - current. Subtraktion vermeidet Überlauf von current + extra. Überlast ergibt auch bei extra=0 false. Lokale Schätzung, keine Serverfreigabe; nicht atomare Lesezugriffe, Gewicht 0 kann unbekannt sein.
