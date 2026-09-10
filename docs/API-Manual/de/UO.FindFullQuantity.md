# UO.FindFullQuantity

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest die bei der letzten Suche gespeicherte Gesamtmenge.

## Genaue Syntax

```text
UO.FindFullQuantity() -> Any
```

## Parameter

Keine Parameter.

## Rückgabewert

Integer — Summe von max(1, Amount) der gefundenen Gegenstände, plus 1 je gefundener Figur. Keine Treffer: 0. Zwei Stapel mit je 50 ergeben 100; FindCount() ergibt 2. Die Summe stammt vom Suchzeitpunkt.

## Verhalten

- FindType mit 1–5 Argumenten, FindTypeEx und Count/CountEx/CountGround ersetzen die Suchergebnisse dieses Skripts. Eine erfolglose Suche leert den Stand. Benötigte Werte vor der nächsten Suche speichern.
- Diese Aufrufe suchen nicht neu, öffnen keine Behälter, bewegen nichts und senden keine Pakete. Sie lesen geladene Clientdaten. FindCount(id) braucht keine vorherige Suche und verändert deren Ergebnisse nicht.
- FindItem/FindCount()/FindFullQuantity sind gespeicherte Suchstände. FindQuantity und FindCount(id) lesen die aktuelle Menge; ein Objekt kann sich nach der Suche ändern oder verschwinden.

## Beispiele

### Eine Goldsuche auslesen

```vb
# Eine Goldsuche auslesen
#
# Liest die bei der letzten Suche gespeicherte Gesamtmenge.
#
# Integer — Summe von max(1, Amount) der gefundenen Gegenstände, plus 1 je gefundener Figur.
# Keine Treffer: 0. Zwei Stapel mit je 50 ergeben 100; FindCount() ergibt 2. Die Summe stammt
# vom Suchzeitpunkt.

SUB Main()
    # type=0x0EED bedeutet Gold; color=-1 erlaubt jede Farbe; backpack wählt in dieser FindType-Form
    # den direkten Rucksackinhalt. value speichert das Ergebnis; STR zeigt es als Text.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindFullQuantity()
    UO.Print(STR(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- type=0x0EED bedeutet Gold; color=-1 erlaubt jede Farbe; backpack wählt in dieser FindType-Form den direkten Rucksackinhalt. value speichert das Ergebnis; STR zeigt es als Text.

### Objekte, Stapel und Gesamtmenge vergleichen

```vb
# Objekte, Stapel und Gesamtmenge vergleichen
#
# Liest die bei der letzten Suche gespeicherte Gesamtmenge.
#
# Integer — Summe von max(1, Amount) der gefundenen Gegenstände, plus 1 je gefundener Figur.
# Keine Treffer: 0. Zwei Stapel mit je 50 ergeben 100; FindCount() ergibt 2. Die Summe stammt
# vom Suchzeitpunkt.

SUB Main()
    # Alle vier Werte gehören zur selben Suche. Zwei Stapel mit je 50: Objekte=2, erster Stapel=50,
    # Gesamtmenge=100. FindItem ist die eindeutige ID des ersten Stapels, nicht sein type.

    UO.FindType(0x0EED, -1, 'backpack')
    UO.Print(STR(UO.FindCount()))
    UO.Print(STR(UO.FindQuantity()))
    UO.Print(STR(UO.FindFullQuantity()))
    UO.Print('0x' + Hex(UO.FindItem()))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Alle vier Werte gehören zur selben Suche. Zwei Stapel mit je 50: Objekte=2, erster Stapel=50, Gesamtmenge=100. FindItem ist die eindeutige ID des ersten Stapels, nicht sein type.

### Einen Wert vor der nächsten Suche sichern

```vb
# Einen Wert vor der nächsten Suche sichern
#
# Liest die bei der letzten Suche gespeicherte Gesamtmenge.
#
# Integer — Summe von max(1, Amount) der gefundenen Gegenstände, plus 1 je gefundener Figur.
# Keine Treffer: 0. Zwei Stapel mit je 50 ergeben 100; FindCount() ergibt 2. Die Summe stammt
# vom Suchzeitpunkt.

SUB Main()
    # Der erste type ist Gold; 0x0F7A ist ein anderer Reagenztyp. Das zweite FindType ersetzt den
    # Suchstand. saved behält den früheren Wert; der letzte Aufruf liest das neue Ergebnis.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindFullQuantity()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindFullQuantity()))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Der erste type ist Gold; 0x0F7A ist ein anderer Reagenztyp. Das zweite FindType ersetzt den Suchstand. saved behält den früheren Wert; der letzte Aufruf liest das neue Ergebnis.
