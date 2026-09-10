# UO.GetLandTilesArray

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Sucht Landkacheln nach graphic/type in einem Rechteck.

## Genaue Syntax

```text
UO.GetLandTilesArray(Xmin:Any, Ymin:Any, Xmax:Any, Ymax:Any, WorldNum:Any, TileType:Any) -> Any
```

## Parameter

- `Xmin` — Weltkoordinaten zweier eingeschlossener Ecken, 0..65535. Vertauschte Ecken werden normalisiert. Höchstens 1.000.000 Zellen; ungültige Grenzen erzeugen vor dem Kartenlesen einen Skriptfehler.
- `Ymin` — Weltkoordinaten zweier eingeschlossener Ecken, 0..65535. Vertauschte Ecken werden normalisiert. Höchstens 1.000.000 Zellen; ungültige Grenzen erzeugen vor dem Kartenlesen einen Skriptfehler.
- `Xmax` — Weltkoordinaten zweier eingeschlossener Ecken, 0..65535. Vertauschte Ecken werden normalisiert. Höchstens 1.000.000 Zellen; ungültige Grenzen erzeugen vor dem Kartenlesen einen Skriptfehler.
- `Ymax` — Weltkoordinaten zweier eingeschlossener Ecken, 0..65535. Vertauschte Ecken werden normalisiert. Höchstens 1.000.000 Zellen; ungültige Grenzen erzeugen vor dem Kartenlesen einen Skriptfehler.
- `WorldNum` — Karten-/Facettennummer 0..255; UO.WorldNum() verwenden. Eine andere Karte liefert ein leeres Array. Ein Kartenwechsel zwischen Abschnitten verwirft das Teilergebnis.
- `TileType` — Ein Kachel-graphic/type, normalerweise 0..65535, keine serial. 0 sucht genau graphic 0; -1 ist kein Platzhalter. Kein passender Typ: leeres Ergebnis.

## Rückgabewert

Array aus [graphic, X, Y, Z], alle Felder Integer. graphic ist der Landtyp, Z seine Basishöhe. Keine Treffer: leeres Array. Die Anzahl ist GetArrayLength(result). Indizes beginnen bei 0. Kein Boolean, keine serial und kein Pascal record; es gibt keinen siebten Ausgabeparameter.

## Verhalten

- Liest lokale Daten, ohne FindItem/FindCount zu ändern, sich zu bewegen, ein Ziel zu aktivieren oder einen Serverbefehl zu senden.
- Aufsteigendes X, innerhalb jedes X aufsteigendes Y. Datensätze einer Zelle behalten die Reihenfolge des Bridge, nicht Entfernung oder Höhe.
- Bis zu 32 Zellen je Abschnitt mit einem weichen Zeitbudget von etwa 1 ms. Abbruch wird zwischen Abschnitten geprüft. Komplexe Zellen oder kalte Lesezugriffe können länger dauern. Große Bereiche aufteilen; die Welt kann sich währenddessen ändern.

### Interne Funktionen: vom Aufruf zum Ergebnis

Tatsächliche C#-Schritte, keine zusätzlichen UO-Befehle. Die Hilfsprozedur steht vollständig in den Beispielen.

#### 1. ExecuteStealthCompatibility

Nimmt sechs Argumente entgegen; die einfache Form übergibt einen Typ, Ex wandelt Array oder Skalar in Typen um.

Ruft FindPortableTiles im land/static-Modus auf und liefert das Ergebnisarray direkt.

Projektquellcode: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `ExecuteStealthCompatibility`.

#### 2. FindPortableTiles

Prüft Koordinaten, Karte und Fläche mit 64-Bit-Arithmetik; normalisiert Ecken und erstellt ein HashSet der Typen.

Speichert X/Y und plant ScanSlice über ExecutePathQuerySlice. Wait(0) prüft Abbruch zwischen Abschnitten; Kartenwechsel ergibt ein leeres Array.

Projektquellcode: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `FindPortableTiles`.

#### 3. ScanSlice

Bearbeitet höchstens 32 Zellen auf dem Spielthread und speichert nach jeder Zelle den Cursor.

GetLandscapeTile liefert graphic/Z/flags; GetStaticTiles liefert graphic/Z/hue-Tripel. Passende Datensätze werden angefügt, zwischen Abschnitten wird die Kontrolle zurückgegeben.

Projektquellcode: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `ScanSlice`.

#### 4. GetChunk2

Nimmt Blockkoordinaten und Ladeflag an; prüft beide Achsen vor dem linearen Index.

Liefert Chunk oder null; Y außerhalb der Karte wird nicht zur Nachbarspalte. Bereits geladene Blöcke werden wiederverwendet, weitere bei Bedarf gelesen.

Projektquellcode: `src/ClassicUO.Client/Game/Map/Map.cs`; Funktion `GetChunk2`.

Liest lokale Daten, ohne FindItem/FindCount zu ändern, sich zu bewegen, ein Ziel zu aktivieren oder einen Serverbefehl zu senden.


## Beispiele

### In Charakternähe suchen

```vb
# In Charakternähe suchen
#
# Sucht Landkacheln nach graphic/type in einem Rechteck.
#
# Array aus [graphic, X, Y, Z], alle Felder Integer. graphic ist der Landtyp, Z seine Basishöhe.
# Keine Treffer: leeres Array. Die Anzahl ist GetArrayLength(result). Indizes beginnen bei 0.
# Kein Boolean, keine serial und kein Pascal record; es gibt keinen siebten Ausgabeparameter.

SUB Main()
    # x/y sind self-Koordinaten, map ist die aktuelle Karte. Das Gebiet umfasst 3×3 Zellen
    # einschließlich Grenzen. Ex nutzt zwei Beispieltypen, die einfache Form einen. Graphics an die
    # eigenen Ressourcen anpassen, keine Objekt-IDs einsetzen.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetLandTilesArray(x, y, x + 2, y + 2, map, 0x0003)
    UO.Print("Records: " + CStr(GetArrayLength(rows)))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- x/y sind self-Koordinaten, map ist die aktuelle Karte. Das Gebiet umfasst 3×3 Zellen einschließlich Grenzen. Ex nutzt zwei Beispieltypen, die einfache Form einen. Graphics an die eigenen Ressourcen anpassen, keine Objekt-IDs einsetzen.

### Vertauschte Ecken und alle Felder

```vb
# Vertauschte Ecken und alle Felder
#
# Sucht Landkacheln nach graphic/type in einem Rechteck.
#
# Array aus [graphic, X, Y, Z], alle Felder Integer. graphic ist der Landtyp, Z seine Basishöhe.
# Keine Treffer: leeres Array. Die Anzahl ist GetArrayLength(result). Indizes beginnen bei 0.
# Kein Boolean, keine serial und kein Pascal record; es gibt keinen siebten Ausgabeparameter.

SUB Main()
    # Das 2×2-Gebiet wird mit absteigenden Ecken angegeben und normalisiert. row ist ein Datensatz.
    # PrintTile ist vollständig definiert und gibt nur Zahlen aus. Bei Land ist hue=0 ein
    # Platzhalterargument; der Landdatensatz besitzt kein hue-Feld.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetLandTilesArray(x + 1, y + 1, x, y, map, 0x0003)
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        PrintTile(row[0], row[1], row[2], row[3], 0)
        i = i + 1
    WEND
END SUB

SUB PrintTile(graphic, x, y, z, hue)
    UO.Print("Type=" + CStr(graphic) + " X=" + CStr(x) + " Y=" + CStr(y))
    UO.Print("Z=" + CStr(z) + " hue=" + CStr(hue))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Das 2×2-Gebiet wird mit absteigenden Ecken angegeben und normalisiert. row ist ein Datensatz. PrintTile ist vollständig definiert und gibt nur Zahlen aus. Bei Land ist hue=0 ein Platzhalterargument; der Landdatensatz besitzt kein hue-Feld.

### Mit begrenzten Versuchen erneut suchen

```vb
# Mit begrenzten Versuchen erneut suchen
#
# Sucht Landkacheln nach graphic/type in einem Rechteck.
#
# Array aus [graphic, X, Y, Z], alle Felder Integer. graphic ist der Landtyp, Z seine Basishöhe.
# Keine Treffer: leeres Array. Die Anzahl ist GetArrayLength(result). Indizes beginnen bei 0.
# Kein Boolean, keine serial und kein Pascal record; es gibt keinen siebten Ausgabeparameter.

SUB Main()
    # Höchstens drei Suchen einer Zelle, dazwischen WAIT(250). Jeder Aufruf erstellt ein neues
    # Ergebnis. Länge 0 bedeutet aktuell keine Treffer, keine dauerhafte Abwesenheit auf dem Server.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR attempt = 0
    WHILE attempt < 3
        VAR rows = UO.GetLandTilesArray(x, y, x, y, map, 0x0003)
        UO.Print("Records: " + CStr(GetArrayLength(rows)))
        attempt = attempt + 1
        WAIT(250)
    WEND
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Höchstens drei Suchen einer Zelle, dazwischen WAIT(250). Jeder Aufruf erstellt ein neues Ergebnis. Länge 0 bedeutet aktuell keine Treffer, keine dauerhafte Abwesenheit auf dem Server.
