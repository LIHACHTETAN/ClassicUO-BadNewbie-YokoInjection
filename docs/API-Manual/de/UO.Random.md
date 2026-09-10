# UO.Random

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Wählt eine Pseudozufallszahl als ganze Zahl. Random(min,max) schließt beide Grenzen ein; die ältere Form Random(max) schließt die obere Grenze aus.

## Genaue Syntax

```text
UO.Random(max:Integer) -> Integer
UO.Random(min:Integer, max:Integer) -> Integer
```

## Parameter

- `min` — Untere Grenze, nur bei zwei Argumenten. Vorzeichenbehaftete 32-Bit-Ganzzahl von -2147483648 bis 2147483647; muss <= max sein.
- `max` — Zwei Argumente: eingeschlossene obere Grenze, beliebiger Integer. Ein Argument: ausgeschlossene obere Grenze, 0..2147483647. Random(0) liefert 0.

## Rückgabewert

Integer — eine ausgewählte Zahl, kein Wahrheitswert und keine serial. Zwei Argumente: min <= Ergebnis <= max. Ein positives Argument: 0 <= Ergebnis < max. Wiederholungen sind möglich.

## Verhalten

- Keine Form ohne Argument. Gleiche Grenzen liefern genau diesen Wert. Vertauschte Grenzen oder ein einzelnes negatives Argument führen zu einem Skriptfehler; Grenzen werden nicht automatisch getauscht.
- Der gesamte vorzeichenbehaftete 32-Bit-Bereich wird ohne Überlauf von max+1 unterstützt. Für abgestufte Brüche Ganzzahlen teilen: Random(0,100)/100.0.
- Der Generator gehört zur Skriptlaufzeit; gleichzeitige Aufrufe sind synchronisiert. Random hat keinen seed-Parameter und unterscheidet sich von BASIC Rnd. Speichern Sie ein Ergebnis zur Wiederverwendung.
- Der Aufruf arbeitet lokal, wartet nicht, bewegt nichts und sendet keine Pakete. Zufällige Koordinaten müssen geprüft werden; Random(0)=0 macht keinen Index eines leeren Arrays gültig.

## Beispiele

### Einen Würfel werfen

```vb
# Einen Würfel werfen
#
# Wählt eine Pseudozufallszahl als ganze Zahl. Random(min,max) schließt beide Grenzen ein; die
# ältere Form Random(max) schließt die obere Grenze aus.
#
# Integer — eine ausgewählte Zahl, kein Wahrheitswert und keine serial. Zwei Argumente: min <=
# Ergebnis <= max. Ein positives Argument: 0 <= Ergebnis < max. Wiederholungen sind möglich.

SUB Main()
    # min=1 und max=6 schließen alle sechs Werte ein. roll speichert einen Wurf; STR wandelt ihn in
    # Text um. Ein späterer Aufruf kann denselben Wert liefern.

    VAR roll = UO.Random(1, 6)
    UO.Print(STR(roll))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- min=1 und max=6 schließen alle sechs Werte ein. roll speichert einen Wurf; STR wandelt ihn in Text um. Ein späterer Aufruf kann denselben Wert liefern.

### Eine zufällige Zeit warten

```vb
# Eine zufällige Zeit warten
#
# Wählt eine Pseudozufallszahl als ganze Zahl. Random(min,max) schließt beide Grenzen ein; die
# ältere Form Random(max) schließt die obere Grenze aus.
#
# Integer — eine ausgewählte Zahl, kein Wahrheitswert und keine serial. Zwei Argumente: min <=
# Ergebnis <= max. Ein positives Argument: 0 <= Ergebnis < max. Wiederholungen sind möglich.

SUB Main()
    # min=350 und max=700 sind eingeschlossene Grenzen in Millisekunden. Random berechnet delay;
    # UO.Wait(delay) wartet. Beachten Sie die vom Server benötigte Mindestwartezeit.

    VAR delay = UO.Random(350, 700)
    UO.Print(STR(delay))
    UO.Wait(delay)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- min=350 und max=700 sind eingeschlossene Grenzen in Millisekunden. Random berechnet delay; UO.Wait(delay) wartet. Beachten Sie die vom Server benötigte Mindestwartezeit.

### Ältere Indexform und gleiche Grenzen

```vb
# Ältere Indexform und gleiche Grenzen
#
# Wählt eine Pseudozufallszahl als ganze Zahl. Random(min,max) schließt beide Grenzen ein; die
# ältere Form Random(max) schließt die obere Grenze aus.
#
# Integer — eine ausgewählte Zahl, kein Wahrheitswert und keine serial. Zwei Argumente: min <=
# Ergebnis <= max. Ein positives Argument: 0 <= Ergebnis < max. Wiederholungen sind möglich.

SUB Main()
    # Random(10) liefert 0..9, niemals 10. Random(7,7) liefert immer 7. Random(-2,2) kann
    # -2,-1,0,1,2 liefern. Jeder Ausdruck zieht eine eigene Zahl.

    VAR index = UO.Random(10)
    VAR fixedValue = UO.Random(7, 7)
    VAR offset = UO.Random(-2, 2)
    UO.Print(STR(index) + ', ' + STR(fixedValue) + ', ' + STR(offset))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Random(10) liefert 0..9, niemals 10. Random(7,7) liefert immer 7. Random(-2,2) kann -2,-1,0,1,2 liefern. Jeder Ausdruck zieht eine eigene Zahl.
