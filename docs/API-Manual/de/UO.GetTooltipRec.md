# UO.GetTooltipRec

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest strukturierte Objekteigenschaften mit Cliloc-ID und Ersetzungsparametern jedes Eintrags.

## Genaue Syntax

```text
UO.GetTooltipRec(ObjID:Any) -> Array
```

## Parameter

- `ObjID` — Erforderliche Objekt-Serial, keine Graphic/Type- oder Cliloc-ID. Ganzzahl, Dezimal-/Hex-String, self, backpack, lasttarget, finditem oder AddObject-Name. 0 wählt kein Objekt.

## Rückgabewert

Array<Array>: Jede Zeile enthält [clilocID:Integer, parameters:Array<String>]. rows[i][0] ist die Meldungs-ID; rows[i][1] enthält die Parameter. GetArrayLength(rows) zählt Eigenschaften. Ein leeres Array bedeutet keine empfangenen Einträge oder ObjID=0. Die IDs sind keine Objekt-Serials.

## Verhalten

- Cache-Daten werden sofort geliefert. Ohne OPL wird eine Anfrage gesendet und bis zu 120 ms gewartet; ein Prozedurabbruch beendet das Warten. Eine bekannte leere OPL wird sofort zurückgegeben.
- Das BASIC-Array bildet TClilocRec ab: Count entspricht GetArrayLength(rows), Items den Zeilen. Führende Transport-Tabulatoren entfallen; leere innere Parameter behalten ihre Position. #Zahl bleibt zur Lokalisierung ein String. Fehlende Parameter ergeben ein leeres Array. Änderungen am Ergebnis verändern den Cache nicht.
- https://stealth.od.ua/api/GetTooltipRec/

## Beispiele

### Eigenschafts-IDs auflisten

```vb
# Eigenschafts-IDs auflisten
#
# Liest strukturierte Objekteigenschaften mit Cliloc-ID und Ersetzungsparametern jedes Eintrags.
#
# Array<Array>: Jede Zeile enthält [clilocID:Integer, parameters:Array<String>]. rows[i][0] ist
# die Meldungs-ID; rows[i][1] enthält die Parameter. GetArrayLength(rows) zählt Eigenschaften.
# Ein leeres Array bedeutet keine empfangenen Einträge oder ObjID=0. Die IDs sind keine
# Objekt-Serials.

SUB Main()
    # ObjID=lasttarget wählt das Objekt. i beginnt bei 0; row[0] ist eine Cliloc-ID. Bei leerem
    # Array läuft die Schleife nicht.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        UO.Print('Cliloc: ' + STR(row[0]))
        i = i + 1
    WEND
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- ObjID=lasttarget wählt das Objekt. i beginnt bei 0; row[0] ist eine Cliloc-ID. Bei leerem Array läuft die Schleife nicht.

### Jede Eigenschaft übersetzen

```vb
# Jede Eigenschaft übersetzen
#
# Liest strukturierte Objekteigenschaften mit Cliloc-ID und Ersetzungsparametern jedes Eintrags.
#
# Array<Array>: Jede Zeile enthält [clilocID:Integer, parameters:Array<String>]. rows[i][0] ist
# die Meldungs-ID; rows[i][1] enthält die Parameter. GetArrayLength(rows) zählt Eigenschaften.
# Ein leeres Array bedeutet keine empfangenen Einträge oder ObjID=0. Die IDs sind keine
# Objekt-Serials.

SUB Main()
    # GetClilocByID erhält ClilocID=row[0] und Params=row[1] in unveränderter Reihenfolge. Nicht die
    # ganze Zeile als Params übergeben.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR text = UO.GetClilocByID(row[0], row[1])
        UO.Print(text)
        i = i + 1
    WEND
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- GetClilocByID erhält ClilocID=row[0] und Params=row[1] in unveränderter Reihenfolge. Nicht die ganze Zeile als Params übergeben.

### Numerischen Parameter lesen

```vb
# Numerischen Parameter lesen
#
# Liest strukturierte Objekteigenschaften mit Cliloc-ID und Ersetzungsparametern jedes Eintrags.
#
# Array<Array>: Jede Zeile enthält [clilocID:Integer, parameters:Array<String>]. rows[i][0] ist
# die Meldungs-ID; rows[i][1] enthält die Parameter. GetArrayLength(rows) zählt Eigenschaften.
# Ein leeres Array bedeutet keine empfangenen Einträge oder ObjID=0. Die IDs sind keine
# Objekt-Serials.

SUB Main()
    # wanted=1060401 ist eine beispielhafte Eigenschafts-ID und muss angepasst werden. args[0] ist
    # ein String. Vor Val Länge und IsNumeric prüfen: Ein Parameter kann Text oder #cliloc
    # enthalten.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR wanted = 1060401
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR args = row[1]
        IF row[0] = wanted AND GetArrayLength(args) > 0 THEN
            IF IsNumeric(args[0]) THEN
                UO.Print('Value: ' + STR(Val(args[0])))
            END IF
        END IF
        i = i + 1
    WEND
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- wanted=1060401 ist eine beispielhafte Eigenschafts-ID und muss angepasst werden. args[0] ist ein String. Vor Val Länge und IsNumeric prüfen: Ein Parameter kann Text oder #cliloc enthalten.
