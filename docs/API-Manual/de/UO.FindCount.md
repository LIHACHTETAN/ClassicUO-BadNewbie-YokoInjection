# UO.FindCount

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Zählt Suchobjekte oder liest die Menge eines Stapels anhand seiner ID.

## Genaue Syntax

```text
UO.FindCount() -> Integer
UO.FindCount(id:Any) -> Integer
```

## Parameter

- `id` — Nur bei FindCount optional. serial eines Gegenstands: Integer, dezimale/hexadezimale Zeichenfolge, lasttarget, lastobject, backpack oder AddObject-Name. ID verwenden, keinen graphic/type. Unbekannter Name: 0. self bezeichnet die Figur und ergibt hier 0. Ohne Argument wird die Zahl der Suchobjekte gelesen.

## Rückgabewert

Integer — FindCount() zählt gefundene Objekte: jeder Stapel ist ein item. FindCount(id) liest den aktuellen Amount dieses Gegenstands; unbekannte/gelöschte IDs und Figuren liefern 0. Ein nicht stapelbarer Gegenstand hat normalerweise Amount=1. Kein ID-, type- oder Boolean-Ergebnis.

## Verhalten

- FindType mit 1–5 Argumenten, FindTypeEx und Count/CountEx/CountGround ersetzen die Suchergebnisse dieses Skripts. Eine erfolglose Suche leert den Stand. Benötigte Werte vor der nächsten Suche speichern.
- Diese Aufrufe suchen nicht neu, öffnen keine Behälter, bewegen nichts und senden keine Pakete. Sie lesen geladene Clientdaten. FindCount(id) braucht keine vorherige Suche und verändert deren Ergebnisse nicht.
- FindItem/FindCount()/FindFullQuantity sind gespeicherte Suchstände. FindQuantity und FindCount(id) lesen die aktuelle Menge; ein Objekt kann sich nach der Suche ändern oder verschwinden.

## Beispiele

### Eine Goldsuche auslesen

```vb
# Eine Goldsuche auslesen
#
# Zählt Suchobjekte oder liest die Menge eines Stapels anhand seiner ID.
#
# Integer — FindCount() zählt gefundene Objekte: jeder Stapel ist ein item. FindCount(id) liest
# den aktuellen Amount dieses Gegenstands; unbekannte/gelöschte IDs und Figuren liefern 0. Ein
# nicht stapelbarer Gegenstand hat normalerweise Amount=1. Kein ID-, type- oder
# Boolean-Ergebnis.

SUB Main()
    # type=0x0EED bedeutet Gold; color=-1 erlaubt jede Farbe; backpack wählt in dieser FindType-Form
    # den direkten Rucksackinhalt. value speichert das Ergebnis; STR zeigt es als Text.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindCount()
    UO.Print(STR(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- type=0x0EED bedeutet Gold; color=-1 erlaubt jede Farbe; backpack wählt in dieser FindType-Form den direkten Rucksackinhalt. value speichert das Ergebnis; STR zeigt es als Text.

### Objekte, Stapel und Gesamtmenge vergleichen

```vb
# Objekte, Stapel und Gesamtmenge vergleichen
#
# Zählt Suchobjekte oder liest die Menge eines Stapels anhand seiner ID.
#
# Integer — FindCount() zählt gefundene Objekte: jeder Stapel ist ein item. FindCount(id) liest
# den aktuellen Amount dieses Gegenstands; unbekannte/gelöschte IDs und Figuren liefern 0. Ein
# nicht stapelbarer Gegenstand hat normalerweise Amount=1. Kein ID-, type- oder
# Boolean-Ergebnis.

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
# Zählt Suchobjekte oder liest die Menge eines Stapels anhand seiner ID.
#
# Integer — FindCount() zählt gefundene Objekte: jeder Stapel ist ein item. FindCount(id) liest
# den aktuellen Amount dieses Gegenstands; unbekannte/gelöschte IDs und Figuren liefern 0. Ein
# nicht stapelbarer Gegenstand hat normalerweise Amount=1. Kein ID-, type- oder
# Boolean-Ergebnis.

SUB Main()
    # Der erste type ist Gold; 0x0F7A ist ein anderer Reagenztyp. Das zweite FindType ersetzt den
    # Suchstand. saved behält den früheren Wert; der letzte Aufruf liest das neue Ergebnis.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindCount()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindCount()))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Der erste type ist Gold; 0x0F7A ist ein anderer Reagenztyp. Das zweite FindType ersetzt den Suchstand. saved behält den früheren Wert; der letzte Aufruf liest das neue Ergebnis.

### Einen Gegenstand direkt per ID lesen

```vb
# Einen Gegenstand direkt per ID lesen
#
# Zählt Suchobjekte oder liest die Menge eines Stapels anhand seiner ID.
#
# Integer — FindCount() zählt gefundene Objekte: jeder Stapel ist ein item. FindCount(id) liest
# den aktuellen Amount dieses Gegenstands; unbekannte/gelöschte IDs und Figuren liefern 0. Ein
# nicht stapelbarer Gegenstand hat normalerweise Amount=1. Kein ID-, type- oder
# Boolean-Ergebnis.

SUB Main()
    # lasttarget muss einen bereits im Spiel gewählten Gegenstand bezeichnen. Es erscheint kein
    # neuer Zielcursor. FindCount(id) liest dessen aktuellen Stapel, liefert bei fehlendem Objekt 0
    # und lässt den Suchstand unverändert.

    VAR id = lasttarget
    VAR amount = UO.FindCount(id)
    UO.Print(STR(amount))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- lasttarget muss einen bereits im Spiel gewählten Gegenstand bezeichnen. Es erscheint kein neuer Zielcursor. FindCount(id) liest dessen aktuellen Stapel, liefert bei fehlendem Objekt 0 und lässt den Suchstand unverändert.
