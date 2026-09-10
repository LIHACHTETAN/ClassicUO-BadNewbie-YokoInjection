# Dictionary

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Dictionary() erzeugt eine Schlüssel/Wert-Sammlung. Methoden werden am Ergebnisobjekt aufgerufen. Zahlen und Text sind verschiedene Schlüssel; auch "ore" und "Ore" unterscheiden sich.

## Genaue Syntax

```text
Dictionary() -> Object
Dictionary(source:Any) -> Object
```

## Parameter

- `source` — source: ohne Argument entsteht eine leere Sammlung. List akzeptiert Array oder List, Dictionary ein Dictionary. Der äußere Container wird kopiert, verschachtelte Referenzen bleiben gemeinsam.

## Rückgabewert

Der Erzeuger liefert Object:Dictionary. Item/Index/Get liefern einen Wert; Count zählt Schlüssel. ContainsKey/Remove liefern 1=TRUE oder 0=FALSE. Add/Set/Clear liefern Unit, Keys/Values neue Array-Werte. For Each liefert Einträge: Key() den Schlüssel, Value() seinen Wert.

## Verhalten

- index / key: List verwendet ganzzahlige numerische Positionen ab 0; Insert akzeptiert auch Count(). Dictionary-Schlüssel sind Text oder endliche Zahlen. Numerische 1 und 1.0 sind ein Schlüssel, Text "1" ein anderer.
- value: initialisierter Basic-Wert, auch Array oder Sammlung. Unit kann nicht gespeichert werden. Gleichheit vergleicht Zahlen, Text unter Beachtung der Großschreibung oder Referenzidentität.
- fallback: Get liefert den Ersatz bei fehlendem Schlüssel ohne Einfügung. Alle Argumente einschließlich fallback-Ausdruck werden vor dem Aufruf ausgewertet.
- Add lehnt vorhandene Schlüssel ohne Überschreiben ab. Set/Index erzeugt oder ersetzt. Item/Index benötigt einen vorhandenen Schlüssel, Get bietet einen Ersatz. Remove liefert 0 bei fehlendem Schlüssel, Clear leert alles.
- NaN, Unendlichkeit, Arrays, Objekte und Unit sind keine Schlüssel. Die Schlüsselreihenfolge ist nicht festgelegt. Jeder Eintrag behält sein eigenes Paar auch nach weiteren Iterationen.
- Keys/Values erzeugen flache Momentaufnahmen. Keys() beim Löschen/Ersetzen durchlaufen; direktes For Each über das Dictionary liefert Eintragsobjekte.
- Änderungen während direktem For Each, auch Set, lösen beim nächsten Schritt einen abfangbaren Fehler aus. Try/Finally wird abgewickelt. Abgelehnte Änderungen bewahren die Daten.
- Aliase und ByVal teilen die Sammlung. Kopien und Momentaufnahmen kopieren nur den äußeren Container. Indiziertes ByRef und zusammengesetzte Zuweisung werten Container/Schlüssel einmal aus; eine neue Variablenzuweisung lenkt die Rückschreibung nicht um.
- Dies sind lokale Skriptdaten. Die Methoden bewegen keine Spielgegenstände und verwenden kein Netzwerk. Ein als Element gespeicherter Stapel belegt eine Position.

## Beispiele

### Schlüsseltypen und Ersatz

```vb
# Schlüsseltypen und Ersatz
#
# Dictionary() erzeugt eine Schlüssel/Wert-Sammlung. Methoden werden am Ergebnisobjekt
# aufgerufen. Zahlen und Text sind verschiedene Schlüssel; auch "ore" und "Ore" unterscheiden
# sich.
#
# Der Erzeuger liefert Object:Dictionary. Item/Index/Get liefern einen Wert; Count zählt
# Schlüssel. ContainsKey/Remove liefern 1=TRUE oder 0=FALSE. Add/Set/Clear liefern Unit,
# Keys/Values neue Array-Werte. For Each liefert Einträge: Key() den Schlüssel, Value() seinen
# Wert.

Option Explicit On
Sub Main()
    # "ore" wird von 5 auf 8 geändert. Zahlenschlüssel 1 speichert 2, Textschlüssel "1" speichert 3.
    # Get("wood",7) liefert 7 ohne Einfügung. Main liefert 8*100+2*10+3+7, Integer 830.

    Var values = Dictionary()
    values.Add("ore", 5)
    values.Set("ore", 8)
    values[1] = 2
    values["1"] = 3
    Return values.Item("ore")*100 + values[1]*10 + values["1"] + values.Get("wood", 7)
End Sub
```

**Erläuterung der Parameter und Ausführung:**

- "ore" wird von 5 auf 8 geändert. Zahlenschlüssel 1 speichert 2, Textschlüssel "1" speichert 3. Get("wood",7) liefert 7 ohne Einfügung. Main liefert 8*100+2*10+3+7, Integer 830.

### Einträge, Momentaufnahmen und Löschen

```vb
# Einträge, Momentaufnahmen und Löschen
#
# Dictionary() erzeugt eine Schlüssel/Wert-Sammlung. Methoden werden am Ergebnisobjekt
# aufgerufen. Zahlen und Text sind verschiedene Schlüssel; auch "ore" und "Ore" unterscheiden
# sich.
#
# Der Erzeuger liefert Object:Dictionary. Item/Index/Get liefern einen Wert; Count zählt
# Schlüssel. ContainsKey/Remove liefern 1=TRUE oder 0=FALSE. Add/Set/Clear liefern Unit,
# Keys/Values neue Array-Werte. For Each liefert Einträge: Key() den Schlüssel, Value() seinen
# Wert.

Option Explicit On
Sub Main()
    # Die Werte ergeben 5. Keys() erlaubt Löschen beim Durchlaufen. copied behält ore=2, snapshot
    # zwei Werte. Nach Clear gilt Count()=0. Main liefert 5*100+2*10+2+0, Integer 522.

    Var values = Dictionary()
    values.Add("ore", 2)
    values.Add("wood", 3)
    Var copied = Dictionary(values)
    Var snapshot = values.Values()
    Var total = 0
    For Each entry In values
        If values.ContainsKey(entry.Key()) Then
            total += entry.Value()
        End If
    Next
    For Each key In values.Keys()
        values.Remove(key)
    Next
    values.Clear()
    Return total*100 + copied["ore"]*10 + GetArrayLength(snapshot) + values.Count()
End Sub
```

**Erläuterung der Parameter und Ausführung:**

- Die Werte ergeben 5. Keys() erlaubt Löschen beim Durchlaufen. copied behält ore=2, snapshot zwei Werte. Nach Clear gilt Count()=0. Main liefert 5*100+2*10+2+0, Integer 522.

### Doppelten Schlüssel abfangen

```vb
# Doppelten Schlüssel abfangen
#
# Dictionary() erzeugt eine Schlüssel/Wert-Sammlung. Methoden werden am Ergebnisobjekt
# aufgerufen. Zahlen und Text sind verschiedene Schlüssel; auch "ore" und "Ore" unterscheiden
# sich.
#
# Der Erzeuger liefert Object:Dictionary. Item/Index/Get liefern einen Wert; Count zählt
# Schlüssel. ContainsKey/Remove liefern 1=TRUE oder 0=FALSE. Add/Set/Clear liefern Unit,
# Keys/Values neue Array-Werte. For Each liefert Einträge: Key() den Schlüssel, Value() seinen
# Wert.

Option Explicit On
Sub Main()
    # Das erste Add speichert ore=4. Das zweite mit 7 erzeugt einen Fehler, Catch setzt caught=1.
    # ore=4 bleibt erhalten. Main liefert 4*10+1, Integer 41.

    Var values = Dictionary()
    values.Add("ore", 4)
    Var caught = 0
    Try
        values.Add("ore", 7)
    Catch problem
        caught = 1
    End Try
    Return values["ore"]*10 + caught
End Sub
```

**Erläuterung der Parameter und Ausführung:**

- Das erste Add speichert ore=4. Das zweite mit 7 erzeugt einen Fehler, Catch setzt caught=1. ore=4 bleibt erhalten. Main liefert 4*10+1, Integer 41.
