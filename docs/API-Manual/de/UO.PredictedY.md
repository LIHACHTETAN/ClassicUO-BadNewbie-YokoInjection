# UO.PredictedY

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest den vorhergesagten Wert für Y-Koordinate nach den bereits eingereihten Spielerschritten.

## Genaue Syntax

```text
UO.PredictedY() -> Integer
```

## Parameter

Keine Parameter.

## Rückgabewert

Integer Y in Kartenfeldern. 0 ist eine gültige Koordinate oder bedeutet fehlenden Spieler.

## Verhalten

- Nur die angezeigte UO-Funktion ohne Argumente. Keine target-, serial-, type-, Ziel-, Distanz- oder timeout-Parameter. Zahl, kein Boolean, ID oder tile-Datensatz: 1 bedeutet keine Ankunft.
- GetEndPosition liest X/Y/Z/Richtung des letzten bereits eingereihten Mobile.Step. Bei leerer Warteschlange wird die aktuelle Position/Richtung gelesen. O(1)-Zugriff ohne Schrittentnahme, Bewegung, Paket, Wegberechnung oder Warten auf Ankunft.
- X/Y sind Welt-/Kartenkoordinaten, keine Pixel eines Container-Gumps. Z ist Höhe, keine Etage. Ein einzelner Bestandteil, kein Array und nicht das endgültige Wegziel.
- Lokale Vorhersage, keine bestätigte Ankunft. Neue/beendete/abgewiesene Schritte, geleerte Warteschlange oder Teleport können sie ändern. Einzelabfragen sind nicht atomar; gleiches X beweist weder Y/Z noch Serverannahme.
- Invoke liest im Spielthread; ein Arbeitsthread wartet auf die Verarbeitung durch den Manager. Skriptabbruch unterbricht das Warten. Keine zusätzliche Verzögerung oder Netzwerkanfrage.
- Externe IApiBridge ohne IPredictedMovementBridge verwenden weiterhin aktuelle Position/Richtung als Rückfall. Classic UO implementiert die Warteschlangenschnittstelle.

### Interne Funktionen: vom Aufruf zum Ergebnis

Tatsächliche native Leseschritte. PredictionEquals ist eine vollständig definierte BASIC-Hilfsfunktion, kein interner Befehl oder Bewegungsablauf.

#### 1. ExecuteStealthCompatibility

Die native Funktion ruft ReadPredictedCoordinate auf und wählt eine IPredictedMovementBridge-Eigenschaft. Kein NewMoveXY und keine neue Wegsuche.

Nur die angezeigte UO-Funktion ohne Argumente. Keine target-, serial-, type-, Ziel-, Distanz- oder timeout-Parameter. Zahl, kein Boolean, ID oder tile-Datensatz: 1 bedeutet keine Ankunft.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `ExecuteStealthCompatibility`.

#### 2. ReadPredictedCoordinate

Die native Funktion ruft ReadPredictedCoordinate auf und wählt eine IPredictedMovementBridge-Eigenschaft. Kein NewMoveXY und keine neue Wegsuche.

Externe IApiBridge ohne IPredictedMovementBridge verwenden weiterhin aktuelle Position/Richtung als Rückfall. Classic UO implementiert die Warteschlangenschnittstelle.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `ReadPredictedCoordinate`.

#### 3. Invoke

Invoke liest im Spielthread; ein Arbeitsthread wartet auf die Verarbeitung durch den Manager. Skriptabbruch unterbricht das Warten. Keine zusätzliche Verzögerung oder Netzwerkanfrage.

Integer Y in Kartenfeldern. 0 ist eine gültige Koordinate oder bedeutet fehlenden Spieler.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 4. ReadPredictedPosition

ReadPredictedPosition liefert bei fehlendem/zerstörtem Player 0; sonst wird GetEndPosition aufgerufen und ein Bestandteil gewählt.

GetEndPosition liest X/Y/Z/Richtung des letzten bereits eingereihten Mobile.Step. Bei leerer Warteschlange wird die aktuelle Position/Richtung gelesen. O(1)-Zugriff ohne Schrittentnahme, Bewegung, Paket, Wegberechnung oder Warten auf Ankunft.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `ReadPredictedPosition`.

#### 5. GetEndPosition

GetEndPosition liest X/Y/Z/Richtung des letzten bereits eingereihten Mobile.Step. Bei leerer Warteschlange wird die aktuelle Position/Richtung gelesen. O(1)-Zugriff ohne Schrittentnahme, Bewegung, Paket, Wegberechnung oder Warten auf Ankunft.

X/Y sind Welt-/Kartenkoordinaten, keine Pixel eines Container-Gumps. Z ist Höhe, keine Etage. Ein einzelner Bestandteil, kein Array und nicht das endgültige Wegziel.

Projektquelle: `src/ClassicUO.Client/Game/GameObjects/Mobile.cs`; Funktion `GetEndPosition`.

#### 6. InjectionValue

Integer Y in Kartenfeldern. 0 ist eine gültige Koordinate oder bedeutet fehlenden Spieler.

Lokale Vorhersage, keine bestätigte Ankunft. Neue/beendete/abgewiesene Schritte, geleerte Warteschlange oder Teleport können sie ändern. Einzelabfragen sind nicht atomar; gleiches X beweist weder Y/Z noch Serverannahme.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs`; Funktion `InjectionValue`.

PredictionEquals(expected) nimmt eine numerische Koordinate/Höhe/Richtung, weist fehlenden Spieler zurück und vergleicht einen vorhergesagten Bestandteil. Integer Boolean 1=TRUE oder 0=FALSE. Wartet nicht auf Ankunft und garantiert sie nicht.


## Beispiele

### Einen Bestandteil lesen

```vb
# Einen Bestandteil lesen
#
# Liest den vorhergesagten Wert für Y-Koordinate nach den bereits eingereihten Spielerschritten.
#
# Integer Y in Kartenfeldern. 0 ist eine gültige Koordinate oder bedeutet fehlenden Spieler.

SUB Main()
    # predicted speichert einen argumentlosen Aufruf; CStr formatiert die Zahl fürs Journal.

    VAR predicted = UO.PredictedY()
    UO.Print('Predicted: ' + CStr(predicted))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- predicted speichert einen argumentlosen Aufruf; CStr formatiert die Zahl fürs Journal.

### Änderung beobachten

```vb
# Änderung beobachten
#
# Liest den vorhergesagten Wert für Y-Koordinate nach den bereits eingereihten Spielerschritten.
#
# Integer Y in Kartenfeldern. 0 ist eine gültige Koordinate oder bedeutet fehlenden Spieler.

SUB Main()
    # WAIT(100) pausiert dieses Beispiel 100 ms. before/after können trotz Zwischenbewegung gleich
    # sein; die Abfragen starten keine Bewegung.

    VAR before = UO.PredictedY()
    WAIT(100)
    VAR after = UO.PredictedY()
    IF before <> after THEN
        UO.Print('Prediction changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- WAIT(100) pausiert dieses Beispiel 100 ms. before/after können trotz Zwischenbewegung gleich sein; die Abfragen starten keine Bewegung.

### Vollständige Vergleichsfunktion

```vb
# Vollständige Vergleichsfunktion
#
# Liest den vorhergesagten Wert für Y-Koordinate nach den bereits eingereihten Spielerschritten.
#
# Integer Y in Kartenfeldern. 0 ist eine gültige Koordinate oder bedeutet fehlenden Spieler.

SUB Main()
    # expected ist eine Beispielkoordinate/-höhe/-richtung, kein Argument des nativen Befehls.
    # PredictionEquals prüft UO.Self(), liest einmal und liefert bei Gleichheit 1=TRUE, sonst
    # 0=FALSE. Vollständige Definition unter Main. Ein passender Bestandteil beweist keine Ankunft.

    IF PredictionEquals(1690) = TRUE THEN
        UO.Print('Queued endpoint matches this component')
    ELSE
        UO.Print('Different component or no player')
    END IF
END SUB

SUB PredictionEquals(expected)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR predicted = UO.PredictedY()
    RETURN predicted = expected
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- expected ist eine Beispielkoordinate/-höhe/-richtung, kein Argument des nativen Befehls. PredictionEquals prüft UO.Self(), liest einmal und liefert bei Gleichheit 1=TRUE, sonst 0=FALSE. Vollständige Definition unter Main. Ein passender Bestandteil beweist keine Ankunft.
