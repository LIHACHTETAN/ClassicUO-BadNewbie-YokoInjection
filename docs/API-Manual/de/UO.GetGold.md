# UO.GetGold

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest den im Status des aktuellen Spielers gemeldeten Goldbetrag.

## Genaue Syntax

```text
UO.GetGold() -> Any
```

## Parameter

Keine Parameter.

## Rückgabewert

Integer/Decimal — nichtnegativer Betrag 0..4294967295. Bis 2147483647 Integer, darüber Decimal (Double), das jeden UInt32-Wert exakt darstellt. 0 kann auch fehlender/zerstörter Player oder unbekannter Betrag bedeuten. Kein Boolean, ID, Stapelzähler oder Durchsuchen von Rucksack/Bank.

## Verhalten

- Keine Argumente. Liest das von CharacterStatus (0x11) gespeicherte Player.Gold. Der Server bestimmt den Umfang des Zählers. Kein Durchsuchen von Taschen und keine Bankabfrage. Fehlender/zerstörter Player liefert 0; ein vorhandener Geist kann den Statusbetrag behalten.
- ReadGoldValue liest bridge.Gold einmal. Die C#-Bridge behält Int32 und transportiert die UInt32-Bits. unchecked stellt den vorzeichenlosen Betrag wieder her: kleine Werte als Integer, große als Decimal. Das hohe Bit erzeugt keinen negativen Kontostand mehr. Lokal, ohne Pakete.
- Große Beträge als numerisches Ergebnis vergleichen. CInt/CLng konvertieren in 32-Bit-Integer. Große BASIC-Literale mit Dezimalpunkt schreiben, etwa 3000000000.0. Der Betrag kann vor einem Kauf veralten; CanAfford ist eine lokale Prüfung, keine Serverfreigabe.
- Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.

### Interne Funktionen: vom Aufruf zum Ergebnis

Native Schritte zum Lesen des Statuszählers und Erweitern seines vorzeichenlosen Bereichs. CanAfford ist die unten vollständig definierte BASIC-Hilfsfunktion, kein versteckter Kaufbefehl.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases ergänzt fehlende Gold/GetGold-Funktionen und intrinsische Namen. Der UO.Gold-Zweig und sein intrinsischer Wert nutzen dasselbe ReadGoldValue. Nicht verdeckte intrinsische Namen werden jedes Mal neu gelesen.

Integer/Decimal — nichtnegativer Betrag 0..4294967295. Bis 2147483647 Integer, darüber Decimal (Double), das jeden UInt32-Wert exakt darstellt. 0 kann auch fehlender/zerstörter Player oder unbekannter Betrag bedeuten. Kein Boolean, ID, Stapelzähler oder Durchsuchen von Rucksack/Bank.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `RegisterCharacterGetterAliases`.

#### 2. ReadGoldValue

ReadGoldValue liest bridge.Gold einmal. Die C#-Bridge behält Int32 und transportiert die UInt32-Bits. unchecked stellt den vorzeichenlosen Betrag wieder her: kleine Werte als Integer, große als Decimal. Das hohe Bit erzeugt keinen negativen Kontostand mehr. Lokal, ohne Pakete.

Große Beträge als numerisches Ergebnis vergleichen. CInt/CLng konvertieren in 32-Bit-Integer. Große BASIC-Literale mit Dezimalpunkt schreiben, etwa 3000000000.0. Der Betrag kann vor einem Kauf veralten; CanAfford ist eine lokale Prüfung, keine Serverfreigabe.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `ReadGoldValue`.

#### 3. Invoke

Keine Argumente. Liest das von CharacterStatus (0x11) gespeicherte Player.Gold. Der Server bestimmt den Umfang des Zählers. Kein Durchsuchen von Taschen und keine Bankabfrage. Fehlender/zerstörter Player liefert 0; ein vorhandener Geist kann den Statusbetrag behalten.

Invoke liest auf dem Spielthread; Warten kann durch Skriptabbruch enden. Kein Paket, Statusabruf, Zielcursor, Ändern des Attributs oder eingebauter Wartezeitraum.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 4. CharacterStatus

Keine Argumente. Liest das von CharacterStatus (0x11) gespeicherte Player.Gold. Der Server bestimmt den Umfang des Zählers. Kein Durchsuchen von Taschen und keine Bankabfrage. Fehlender/zerstörter Player liefert 0; ein vorhandener Geist kann den Statusbetrag behalten.

Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.

Projektquelle: `src/ClassicUO.Client/Network/PacketHandlers.cs`; Funktion `CharacterStatus`.

#### 5. Clear

World.Clear entfernt Player. Bis Spieler und Daten wieder vorhanden sind, liefern Aufrufe 0. Ein gespeicherter Wert beweist nach Wiederverbindung keine erfüllte Anforderung.

Integer/Decimal — nichtnegativer Betrag 0..4294967295. Bis 2147483647 Integer, darüber Decimal (Double), das jeden UInt32-Wert exakt darstellt. 0 kann auch fehlender/zerstörter Player oder unbekannter Betrag bedeuten. Kein Boolean, ID, Stapelzähler oder Durchsuchen von Rucksack/Bank.

Projektquelle: `src/ClassicUO.Client/Game/World.cs`; Funktion `Clear`.

Jeder Aufruf liest neu. Variablen speichern Momentaufnahmen; getrennte Aufrufe können verschiedene Serverupdates sehen. Ein Wert ungleich 0 prüft keine Verbindung; 0 kann ein Wert oder fehlende Daten sein.


## Beispiele

### Gemeldeten Betrag ausgeben

```vb
# Gemeldeten Betrag ausgeben
#
# Liest den im Status des aktuellen Spielers gemeldeten Goldbetrag.
#
# Integer/Decimal — nichtnegativer Betrag 0..4294967295. Bis 2147483647 Integer, darüber Decimal
# (Double), das jeden UInt32-Wert exakt darstellt. 0 kann auch fehlender/zerstörter Player oder
# unbekannter Betrag bedeuten. Kein Boolean, ID, Stapelzähler oder Durchsuchen von
# Rucksack/Bank.

SUB Main()
    # amount speichert einen Aufruf; CStr formatiert fürs Journal. Gold wird weder gesucht noch
    # bewegt oder ausgegeben.

    VAR amount = UO.GetGold()
    UO.Print('Status gold: ' + CStr(amount))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- amount speichert einen Aufruf; CStr formatiert fürs Journal. Gold wird weder gesucht noch bewegt oder ausgegeben.

### Vollständiges CanAfford mit großem Preis

```vb
# Vollständiges CanAfford mit großem Preis
#
# Liest den im Status des aktuellen Spielers gemeldeten Goldbetrag.
#
# Integer/Decimal — nichtnegativer Betrag 0..4294967295. Bis 2147483647 Integer, darüber Decimal
# (Double), das jeden UInt32-Wert exakt darstellt. 0 kann auch fehlender/zerstörter Player oder
# unbekannter Betrag bedeuten. Kein Boolean, ID, Stapelzähler oder Durchsuchen von
# Rucksack/Bank.

SUB Main()
    # price=3000000000.0 ist ein Beispielpreis. CanAfford(price) weist negativen Preis oder
    # fehlenden Player zurück, liest einmal und liefert für amount >= price Integer Boolean 1=TRUE
    # oder 0=FALSE. Der Betrag selbst ist kein Boolean. Vollständige Definition unten.

    VAR price = 3000000000.0
    IF CanAfford(price) = TRUE THEN
        UO.Print('Local balance is sufficient')
    ELSE
        UO.Print('Local check failed')
    END IF
END SUB

SUB CanAfford(price)
    IF price < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR amount = UO.GetGold()
    RETURN amount >= price
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- price=3000000000.0 ist ein Beispielpreis. CanAfford(price) weist negativen Preis oder fehlenden Player zurück, liest einmal und liefert für amount >= price Integer Boolean 1=TRUE oder 0=FALSE. Der Betrag selbst ist kein Boolean. Vollständige Definition unten.

### Änderung des Betrags beobachten

```vb
# Änderung des Betrags beobachten
#
# Liest den im Status des aktuellen Spielers gemeldeten Goldbetrag.
#
# Integer/Decimal — nichtnegativer Betrag 0..4294967295. Bis 2147483647 Integer, darüber Decimal
# (Double), das jeden UInt32-Wert exakt darstellt. 0 kann auch fehlender/zerstörter Player oder
# unbekannter Betrag bedeuten. Kein Boolean, ID, Stapelzähler oder Durchsuchen von
# Rucksack/Bank.

SUB Main()
    # before/after werden durch WAIT(500) Millisekunden getrennt. difference=after-before kann bei
    # sinkendem Betrag negativ sein; das ist kein vorzeichenloser Überlauf. Zwischenupdates oder
    # Charakterwechsel können unbemerkt bleiben.

    VAR before = UO.GetGold()
    WAIT(500)
    VAR after = UO.GetGold()
    VAR difference = after - before
    UO.Print('Balance change: ' + CStr(difference))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- before/after werden durch WAIT(500) Millisekunden getrennt. difference=after-before kann bei sinkendem Betrag negativ sein; das ist kein vorzeichenloser Überlauf. Zwischenupdates oder Charakterwechsel können unbemerkt bleiben.
