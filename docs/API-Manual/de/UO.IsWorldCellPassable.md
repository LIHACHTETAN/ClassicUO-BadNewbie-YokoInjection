# UO.IsWorldCellPassable

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Prüft einen Übergang zur Nachbarzelle und liefert Begehbarkeit zusammen mit der Höhe.

## Genaue Syntax

```text
UO.IsWorldCellPassable(CurrX:Any, CurrY:Any, CurrZ:Any, DestX:Any, DestY:Any, DestZ:Any, WorldNum:Any) -> Array
```

## Parameter

- `CurrX` — Erforderliche Weltkoordinate X der Startzelle: Ganzzahl 0..65535 innerhalb der geladenen Karte, keine Gump-Koordinate.
- `CurrY` — Erforderliche Weltkoordinate Y der Startzelle: Ganzzahl 0..65535 innerhalb der geladenen Karte, keine Gump-Koordinate.
- `CurrZ` — Erforderliche Starthöhe −128..127, keine Stockwerksnummer. Ungültige Höhen werden abgelehnt, nicht begrenzt.
- `DestX` — Erforderliche Weltkoordinate X der Zielzelle: Ganzzahl 0..65535 innerhalb der geladenen Karte, keine Gump-Koordinate.
- `DestY` — Erforderliche Weltkoordinate Y der Zielzelle: Ganzzahl 0..65535 innerhalb der geladenen Karte, keine Gump-Koordinate.
- `DestZ` — Erforderliche Ersatzhöhe als Eingabe, meist CurrZ. Kein var: Die Variable bleibt unverändert und legt kein Stockwerk fest. Berechnete Höhe aus result[1] lesen. Dieser Bridge liefert stets seine eigene Höhe; das Argument bewahrt die Pascal-Form.
- `WorldNum` — Erforderliche Kartennummer: UO.WorldNum(). Nur aktuelle Karte mit bekannten Abmessungen; andere Karten werden nicht geladen.

## Rückgabewert

Array mit zwei Integer: [0] — Begehbarkeit, 1 = TRUE, 0 = FALSE; [1] — berechnete Z. Nur das erste Element ist logisch; nicht das Array mit TRUE vergleichen. Null/negative Höhen sind gültig; bei [0]=0 beweist die Höhe keine Erreichbarkeit. Abgelehnte Argumente liefern [0, CurrZ].

## Verhalten

- Keine Bewegung, Türöffnung, Zielauswahl oder Netzwerkpakete. Liest vorhandene lokale Geometrie; der Server kann einen späteren Schritt ablehnen. Abfragen sind getrennte Momentaufnahmen.
- Nachbarzelle: X/Y-Abstand höchstens 1. Ferne Ziele, Kartengrenzverletzungen, fehlender Charakter/Karte oder IsDestroyed werden vor der Kollisionsprüfung abgelehnt. Ganze Wege: GetPathArray oder NewMoveXY.
- Gleiche gültige X/Y ergeben [1, CurrZ] ohne Kollisionstest: Kein Schritt nötig. Dies prüft nicht das Verlassen der Zelle. Charakterzustand und Pathfinder-Regeln beeinflussen Nachbarschritte; fehlende geladene Geometrie kann zur Ablehnung führen.

### Interne Funktionen: vom Aufruf zum Ergebnis

Dies sind die tatsächlichen internen C#-Schritte. IsCellOpen ist eine vollständig definierte Hilfsfunktion im Beispiel, kein verborgener integrierter Befehl.

#### 1. ExecuteStealthCompatibility

Liest sieben Integer-Argumente. DestZ wird nur verwendet, wenn ein anderer Bridge keine Höhe liefert. Liefert ein Array ohne Argumentänderung.

Array mit zwei Integer: [0] — Begehbarkeit, 1 = TRUE, 0 = FALSE; [1] — berechnete Z. Nur das erste Element ist logisch; nicht das Array mit TRUE vergleichen. Null/negative Höhen sind gültig; bei [0]=0 beweist die Höhe keine Erreichbarkeit. Abgelehnte Argumente liefern [0, CurrZ].

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `ExecuteStealthCompatibility`.

#### 2. CheckWorldStep

Invoke prüft Charakter, Karte, Abmessungen, Koordinaten, Höhe und Nachbarschaft vor der Subtraktion; wählt die Richtung. Verlangt nach CanWalkForQuery exakte Ziel-X/Y.

Array mit zwei Integer: [0] — Begehbarkeit, 1 = TRUE, 0 = FALSE; [1] — berechnete Z. Nur das erste Element ist logisch; nicht das Array mit TRUE vergleichen. Null/negative Höhen sind gültig; bei [0]=0 beweist die Höhe keine Erreichbarkeit. Abgelehnte Argumente liefern [0, CurrZ].

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `CheckWorldStep`.

#### 3. CanWalkForQuery

Entfernt vorübergehend das Sperrzellenprädikat eines fremden Wegs, stellt es in finally wieder her und ruft CanWalk ohne Wegstart auf.

Keine Bewegung, Türöffnung, Zielauswahl oder Netzwerkpakete. Liest vorhandene lokale Geometrie; der Server kann einen späteren Schritt ablehnen. Abfragen sind getrennte Momentaufnahmen.

Projektquelle: `src/ClassicUO.Client/Game/Pathfinder.cs`; Funktion `CanWalkForQuery`.

#### 4. CanWalk

Prüft Hauptschritt und diagonale Seiten. Liefert bool und ändert ref-Koordinaten nur bei einem angenommenen Schritt.

Kollisionsfunktionen lesen geladene Geometrie und Charakterzustand. Ein seitlicher Diagonalersatz bedeutet nicht, dass die angefragte Zelle erreicht wurde.

Projektquelle: `src/ClassicUO.Client/Game/Pathfinder.cs`; Funktion `CanWalk`.

#### 5. CalculateNewZ

Erhält Ziel-X/Y, Start-Z per ref und Richtung. Wählt Oberfläche und Freiraum gemäß Charakterzustand; bool bezeichnet Begehbarkeit, z die Höhe.

Kollisionsfunktionen lesen geladene Geometrie und Charakterzustand. Ein seitlicher Diagonalersatz bedeutet nicht, dass die angefragte Zelle erreicht wurde.

Projektquelle: `src/ClassicUO.Client/Game/Pathfinder.cs`; Funktion `CalculateNewZ`.

#### 6. CalculateMinMaxZ

Erhält neue Zelle, aktuelle Z, Richtung und Modus. Berechnet über CreateItemList ref minZ/maxZ anhand der Startgeometrie.

Kollisionsfunktionen lesen geladene Geometrie und Charakterzustand. Ein seitlicher Diagonalersatz bedeutet nicht, dass die angefragte Zelle erreicht wurde.

Projektquelle: `src/ClassicUO.Client/Game/Pathfinder.cs`; Funktion `CalculateMinMaxZ`.

#### 7. CreateItemList

Erhält Liste, X/Y und Modus. Sammelt geladene Objekte und Kollisionsregeln; bool bezeichnet vorhandene Geometrie. Map.GetTile nutzt load=false ohne neue Blöcke zu lesen.

Kollisionsfunktionen lesen geladene Geometrie und Charakterzustand. Ein seitlicher Diagonalersatz bedeutet nicht, dass die angefragte Zelle erreicht wurde.

Projektquelle: `src/ClassicUO.Client/Game/Pathfinder.cs`; Funktion `CreateItemList`.

Keine Bewegung, Türöffnung, Zielauswahl oder Netzwerkpakete. Liest vorhandene lokale Geometrie; der Server kann einen späteren Schritt ablehnen. Abfragen sind getrennte Momentaufnahmen.


## Beispiele

### Östliche Zelle prüfen

```vb
# Östliche Zelle prüfen
#
# Prüft einen Übergang zur Nachbarzelle und liefert Begehbarkeit zusammen mit der Höhe.
#
# Array mit zwei Integer: [0] — Begehbarkeit, 1 = TRUE, 0 = FALSE; [1] — berechnete Z. Nur das
# erste Element ist logisch; nicht das Array mit TRUE vergleichen. Null/negative Höhen sind
# gültig; bei [0]=0 beweist die Höhe keine Erreichbarkeit. Abgelehnte Argumente liefern [0,
# CurrZ].

SUB Main()
    # x/y/z sind der Start, x+1/y der Nachbar; sechstes Argument Ersatz-Z, letztes aktuelle Karte.
    # result[0] vor result[1] prüfen.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR result = UO.IsWorldCellPassable(x,y,z,x+1,y,z,UO.WorldNum())
    IF result[0] = TRUE THEN
        UO.Print('Passable, Z=' + CStr(result[1]))
    ELSE
        UO.Print('Blocked')
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- x/y/z sind der Start, x+1/y der Nachbar; sechstes Argument Ersatz-Z, letztes aktuelle Karte. result[0] vor result[1] prüfen.

### Z ohne Änderung des Arguments lesen

```vb
# Z ohne Änderung des Arguments lesen
#
# Prüft einen Übergang zur Nachbarzelle und liefert Begehbarkeit zusammen mit der Höhe.
#
# Array mit zwei Integer: [0] — Begehbarkeit, 1 = TRUE, 0 = FALSE; [1] — berechnete Z. Nur das
# erste Element ist logisch; nicht das Array mit TRUE vergleichen. Null/negative Höhen sind
# gültig; bei [0]=0 beweist die Höhe keine Erreichbarkeit. Abgelehnte Argumente liefern [0,
# CurrZ].

SUB Main()
    # proposedZ bleibt 0. targetZ stammt aus result[1], nicht aus dem Argument. Bei Ablehnung wird
    # keine Höhe abgeleitet.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR proposedZ = 0
    VAR result = UO.IsWorldCellPassable(x,y,z,x,y+1,proposedZ,UO.WorldNum())
    IF result[0] = 1 THEN
        VAR targetZ = result[1]
        UO.Print('Input=' + CStr(proposedZ) + '; result=' + CStr(targetZ))
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- proposedZ bleibt 0. targetZ stammt aus result[1], nicht aus dem Argument. Bei Ablehnung wird keine Höhe abgeleitet.

### Vollständige IsCellOpen-Funktion

```vb
# Vollständige IsCellOpen-Funktion
#
# Prüft einen Übergang zur Nachbarzelle und liefert Begehbarkeit zusammen mit der Höhe.
#
# Array mit zwei Integer: [0] — Begehbarkeit, 1 = TRUE, 0 = FALSE; [1] — berechnete Z. Nur das
# erste Element ist logisch; nicht das Array mit TRUE vergleichen. Null/negative Höhen sind
# gültig; bei [0]=0 beweist die Höhe keine Erreichbarkeit. Abgelehnte Argumente liefern [0,
# CurrZ].

SUB Main()
    # Vollständiger Helfer nach Main: Start-X/Y/Z, Ziel-X/Y und Karte. Ergänzt das sechste Argument
    # und liefert nur Integer 1/0, kein Array. IsCellOpen darf mit TRUE verglichen werden. Keine
    # Bewegung.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR openCell = IsCellOpen(x,y,UO.GetZ(),x+1,y+1,UO.WorldNum())
    IF openCell = TRUE THEN
        UO.Print('Diagonal cell is locally passable')
    END IF
END SUB

SUB IsCellOpen(x,y,z,toX,toY,map)
    VAR cellResult = UO.IsWorldCellPassable(x,y,z,toX,toY,z,map)
    IF GetArrayLength(cellResult) <> 2 THEN
        RETURN 0
    END IF
    RETURN cellResult[0]
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Vollständiger Helfer nach Main: Start-X/Y/Z, Ziel-X/Y und Karte. Ergänzt das sechste Argument und liefert nur Integer 1/0, kein Array. IsCellOpen darf mit TRUE verglichen werden. Keine Bewegung.
