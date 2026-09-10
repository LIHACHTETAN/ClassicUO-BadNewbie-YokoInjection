# UO.GetIntelligence

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest die aktuelle Intelligenz (INT).

## Genaue Syntax

```text
UO.GetIntelligence() -> Integer
```

## Parameter

Keine Parameter.

## Rückgabewert

Integer — aktuelle Attributpunkte, im Modell 0..65535; kein Prozentsatz, ID, Fertigkeitswert, Sperrmodus oder Boolean. 0 kann auch fehlender/zerstörter Spieler oder unbekanntes Subjekt bedeuten. Mit einer Zahl vergleichen, nicht = TRUE. Weder Attributgrenze noch garantiert unveränderter Basiswert.

## Verhalten

- Keine Argumente. Die angezeigten Signaturen beachten.
- Liest Player.Intelligence, wenn Player vorhanden und nicht zerstört ist, sonst 0. Ein vorhandener toter Charakter ist kein zerstörtes Objekt. Keine Ableitung aus HP, Mana oder Ausdauer.
- GetStr/GetInt/GetDex nehmen ObjID an; diese Attribute liegen jedoch nur in PlayerMobile. Jede fremde Serial liefert 0, auch bei geladenem Mobile. Einschränkung gegenüber der allgemeinen Stealth-Beschreibung; fremde Werte werden nicht erfunden.
- Invoke liest auf dem Spielthread; Warten kann durch Skriptabbruch enden. Kein Paket, Statusabruf, Zielcursor, Ändern des Attributs oder eingebauter Wartezeitraum.
- Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.
- Gleichwertige Namen mit oder ohne UO., unabhängig von Groß-/Kleinschreibung: `Int Intelligence GetInt GetIntelligence`.
- Int(value) ohne UO. rundet eine BASIC-Zahl ab; Str(value) formatiert Text. Diese Operationen unterscheiden sich von den Attributlesern UO.Int()/UO.Str(). GetInt(ObjID) rundet keine Zahl.

### Interne Funktionen: vom Aufruf zum Ergebnis

Native Leseschritte. AttributeAtLeast ist die unten vollständig definierte BASIC-Hilfsfunktion, keine versteckte API oder Attributänderung.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ergänzt fehlende parameterlose Funktionen und intrinsische Namen. Vorhandene Kompatibilitätszweige wählen ihren Getter; beide Wege liefern Integer. Ein intrinsischer Name wird neu gelesen, sofern keine Variable ihn verdeckt.

Gleichwertige Namen mit oder ohne UO., unabhängig von Groß-/Kleinschreibung: `Int Intelligence GetInt GetIntelligence`.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `RegisterCharacterGetterAliases`.

#### 2. Invoke

Liest Player.Intelligence, wenn Player vorhanden und nicht zerstört ist, sonst 0. Ein vorhandener toter Charakter ist kein zerstörtes Objekt. Keine Ableitung aus HP, Mana oder Ausdauer. Invoke liest auf dem Spielthread; Warten kann durch Skriptabbruch enden. Kein Paket, Statusabruf, Zielcursor, Ändern des Attributs oder eingebauter Wartezeitraum.

Integer — aktuelle Attributpunkte, im Modell 0..65535; kein Prozentsatz, ID, Fertigkeitswert, Sperrmodus oder Boolean. 0 kann auch fehlender/zerstörter Spieler oder unbekanntes Subjekt bedeuten. Mit einer Zahl vergleichen, nicht = TRUE. Weder Attributgrenze noch garantiert unveränderter Basiswert. Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 3. CharacterStatus

CharacterStatus schreibt das empfangene STR/DEX/INT-Feld nach Player.Intelligence, wenn ein passendes Statuspaket für den eigenen Spieler eintrifft. Die Abfrage liest den Cache ohne auf ein neues Paket zu warten.

Invoke liest auf dem Spielthread; Warten kann durch Skriptabbruch enden. Kein Paket, Statusabruf, Zielcursor, Ändern des Attributs oder eingebauter Wartezeitraum.

Projektquelle: `src/ClassicUO.Client/Network/PacketHandlers.cs`; Funktion `CharacterStatus`.

#### 4. Clear

World.Clear entfernt Player. Bis Spieler und Daten wieder vorhanden sind, liefern Aufrufe 0. Ein gespeicherter Wert beweist nach Wiederverbindung keine erfüllte Anforderung.

Integer — aktuelle Attributpunkte, im Modell 0..65535; kein Prozentsatz, ID, Fertigkeitswert, Sperrmodus oder Boolean. 0 kann auch fehlender/zerstörter Spieler oder unbekanntes Subjekt bedeuten. Mit einer Zahl vergleichen, nicht = TRUE. Weder Attributgrenze noch garantiert unveränderter Basiswert.

Projektquelle: `src/ClassicUO.Client/Game/World.cs`; Funktion `Clear`.

World.Clear entfernt Player. Bis Spieler und Daten wieder vorhanden sind, liefern Aufrufe 0. Ein gespeicherter Wert beweist nach Wiederverbindung keine erfüllte Anforderung.


## Beispiele

### Punkte ausgeben

```vb
# Punkte ausgeben
#
# Liest die aktuelle Intelligenz (INT).
#
# Integer — aktuelle Attributpunkte, im Modell 0..65535; kein Prozentsatz, ID, Fertigkeitswert,
# Sperrmodus oder Boolean. 0 kann auch fehlender/zerstörter Spieler oder unbekanntes Subjekt
# bedeuten. Mit einer Zahl vergleichen, nicht = TRUE. Weder Attributgrenze noch garantiert
# unveränderter Basiswert.

SUB Main()
    # value speichert die Zahl; CStr formatiert sie fürs Journal. Keine Argumente oder
    # Charakteraktion.

    VAR value = UO.GetIntelligence()
    UO.Print('Intelligence: ' + CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value speichert die Zahl; CStr formatiert sie fürs Journal. Keine Argumente oder Charakteraktion.

### Zwei Beobachtungen vergleichen

```vb
# Zwei Beobachtungen vergleichen
#
# Liest die aktuelle Intelligenz (INT).
#
# Integer — aktuelle Attributpunkte, im Modell 0..65535; kein Prozentsatz, ID, Fertigkeitswert,
# Sperrmodus oder Boolean. 0 kann auch fehlender/zerstörter Spieler oder unbekanntes Subjekt
# bedeuten. Mit einer Zahl vergleichen, nicht = TRUE. Weder Attributgrenze noch garantiert
# unveränderter Basiswert.

SUB Main()
    # before/after liegen 1000 ms auseinander; WAIT gehört zum Beispiel. change=after-before kann
    # positiv, null oder negativ sein. Zwischenstände und Verbindungsabbrüche sind damit allein
    # nicht unterscheidbar.

    VAR before = UO.GetIntelligence()
    WAIT(1000)
    VAR after = UO.GetIntelligence()
    VAR change = after - before
    UO.Print('Change: ' + CStr(change))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- before/after liegen 1000 ms auseinander; WAIT gehört zum Beispiel. change=after-before kann positiv, null oder negativ sein. Zwischenstände und Verbindungsabbrüche sind damit allein nicht unterscheidbar.

### Vollständige Anforderungsprüfung

```vb
# Vollständige Anforderungsprüfung
#
# Liest die aktuelle Intelligenz (INT).
#
# Integer — aktuelle Attributpunkte, im Modell 0..65535; kein Prozentsatz, ID, Fertigkeitswert,
# Sperrmodus oder Boolean. 0 kann auch fehlender/zerstörter Spieler oder unbekanntes Subjekt
# bedeuten. Mit einer Zahl vergleichen, nicht = TRUE. Weder Attributgrenze noch garantiert
# unveränderter Basiswert.

SUB Main()
    # minimum=80 ist eine Beispielanforderung. AttributeAtLeast(minimum) weist fehlenden Spieler
    # zurück, liest einmal und liefert für >= minimum Integer Boolean 1=TRUE oder 0=FALSE. Der
    # Vergleich ist logisch, das Attribut nicht.

    IF AttributeAtLeast(80) = TRUE THEN
        UO.Print('Requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB AttributeAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetIntelligence()
    RETURN value >= minimum
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- minimum=80 ist eine Beispielanforderung. AttributeAtLeast(minimum) weist fehlenden Spieler zurück, liest einmal und liefert für >= minimum Integer Boolean 1=TRUE oder 0=FALSE. Der Vergleich ist logisch, das Attribut nicht.
