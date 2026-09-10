# List

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

List() erzeugt eine geordnete Sammlung mit veränderlicher Länge. Das Ergebnis in einer Variablen speichern: items.Add ist eine Objektmethode, kein globaler Befehl List.Add.

## Genaue Syntax

```text
List() -> Object
List(source:Any) -> Object
```

## Parameter

- `source` — source: ohne Argument entsteht eine leere Sammlung. List akzeptiert Array oder List, Dictionary ein Dictionary. Der äußere Container wird kopiert, verschachtelte Referenzen bleiben gemeinsam.

## Rückgabewert

Der Erzeuger liefert Object:List. Item/Index liest einen Wert; Count zählt Elemente; IndexOf liefert eine Position ab 0 oder -1. Contains/Remove liefern 1=TRUE oder 0=FALSE. Add/Insert/Set/RemoveAt/Clear liefern Unit, ToArray ein neues Array.

## Verhalten

- index / key: List verwendet ganzzahlige numerische Positionen ab 0; Insert akzeptiert auch Count(). Dictionary-Schlüssel sind Text oder endliche Zahlen. Numerische 1 und 1.0 sind ein Schlüssel, Text "1" ein anderer.
- value: initialisierter Basic-Wert, auch Array oder Sammlung. Unit kann nicht gespeichert werden. Gleichheit vergleicht Zahlen, Text unter Beachtung der Großschreibung oder Referenzidentität.
- fallback: Get liefert den Ersatz bei fehlendem Schlüssel ohne Einfügung. Alle Argumente einschließlich fallback-Ausdruck werden vor dem Aufruf ausgewertet.
- Add hängt an, Insert fügt vor der Position ein, Set/Index ersetzt ein vorhandenes Element, Item/Index liest es. Remove löscht den ersten gleichen Wert, RemoveAt eine Position, Clear alle Elemente.
- Contains prüft das Vorkommen, IndexOf findet den ersten Treffer. Negative, gebrochene, textuelle oder ungültige Indizes erzeugen einen abfangbaren Fehler ohne Änderung.
- For Each erhält die Reihenfolge. ToArray erstellt eine flache Momentaufnahme; diese zum Durchlaufen während Änderungen verwenden.
- Änderungen während direktem For Each, auch Set, lösen beim nächsten Schritt einen abfangbaren Fehler aus. Try/Finally wird abgewickelt. Abgelehnte Änderungen bewahren die Daten.
- Aliase und ByVal teilen die Sammlung. Kopien und Momentaufnahmen kopieren nur den äußeren Container. Indiziertes ByRef und zusammengesetzte Zuweisung werten Container/Schlüssel einmal aus; eine neue Variablenzuweisung lenkt die Rückschreibung nicht um.
- Dies sind lokale Skriptdaten. Die Methoden bewegen keine Spielgegenstände und verwenden kein Netzwerk. Ein als Element gespeicherter Stapel belegt eine Position.

## Beispiele

### Liste aufbauen und summieren

```vb
# Liste aufbauen und summieren
#
# List() erzeugt eine geordnete Sammlung mit veränderlicher Länge. Das Ergebnis in einer
# Variablen speichern: items.Add ist eine Objektmethode, kein globaler Befehl List.Add.
#
# Der Erzeuger liefert Object:List. Item/Index liest einen Wert; Count zählt Elemente; IndexOf
# liefert eine Position ab 0 oder -1. Contains/Remove liefern 1=TRUE oder 0=FALSE.
# Add/Insert/Set/RemoveAt/Clear liefern Unit, ToArray ein neues Array.

Option Explicit On
Sub Main()
    # Add ergibt [3,7], Insert(1,5) ergibt [3,5,7], Set(0,2) ergibt [2,5,7]. For Each summiert drei
    # Werte. Main liefert Integer 14.

    Var items = List()
    items.Add(3)
    items.Add(7)
    items.Insert(1, 5)
    items.Set(0, 2)
    Var total = 0
    For Each item In items
        total += item
    Next
    Return total
End Sub
```

**Erläuterung der Parameter und Ausführung:**

- Add ergibt [3,7], Insert(1,5) ergibt [3,5,7], Set(0,2) ergibt [2,5,7]. For Each summiert drei Werte. Main liefert Integer 14.

### Kopien und Momentaufnahme

```vb
# Kopien und Momentaufnahme
#
# List() erzeugt eine geordnete Sammlung mit veränderlicher Länge. Das Ergebnis in einer
# Variablen speichern: items.Add ist eine Objektmethode, kein globaler Befehl List.Add.
#
# Der Erzeuger liefert Object:List. Item/Index liest einen Wert; Count zählt Elemente; IndexOf
# liefert eine Position ab 0 oder -1. Contains/Remove liefern 1=TRUE oder 0=FALSE.
# Add/Insert/Set/RemoveAt/Clear liefern Unit, ToArray ein neues Array.

Option Explicit On
Sub Main()
    # seed=[4,6]. copied und snapshot behalten diese Werte. Das Original wird [9,6]; Remove(6)
    # liefert TRUE=1, RemoveAt(0) leert es, Clear lässt es leer. Main liefert 4*100+6*10+1+0,
    # Integer 461.

    Dim seed[1]
    seed[0] = 4
    seed[1] = 6
    Var items = List(seed)
    Var copied = List(items)
    Var snapshot = items.ToArray()
    items[0] = 9
    Var removed = items.Remove(6)
    items.RemoveAt(0)
    items.Clear()
    Return snapshot[0]*100 + copied[1]*10 + removed + items.Count()
End Sub
```

**Erläuterung der Parameter und Ausführung:**

- seed=[4,6]. copied und snapshot behalten diese Werte. Das Original wird [9,6]; Remove(6) liefert TRUE=1, RemoveAt(0) leert es, Clear lässt es leer. Main liefert 4*100+6*10+1+0, Integer 461.

### Suche und ByRef

```vb
# Suche und ByRef
#
# List() erzeugt eine geordnete Sammlung mit veränderlicher Länge. Das Ergebnis in einer
# Variablen speichern: items.Add ist eine Objektmethode, kein globaler Befehl List.Add.
#
# Der Erzeuger liefert Object:List. Item/Index liest einen Wert; Count zählt Elemente; IndexOf
# liefert eine Position ab 0 oder -1. Contains/Remove liefern 1=TRUE oder 0=FALSE.
# Add/Insert/Set/RemoveAt/Clear liefern Unit, ToArray ein neues Array.

Option Explicit On
Function NextIndex(ByRef calls)
    calls += 1
    Return 0
End Function
Sub Bump(ByRef value)
    value += 1
End Sub
Sub Main()
    # NextIndex läuft einmal: calls=1, Index 0. Bump ändert 5 auf 6. Contains(6)=TRUE, IndexOf(6)=0,
    # Item(0) liefert 6. Main liefert Integer 601.

    Var items = List()
    items.Add(5)
    Var calls = 0
    Bump(items[NextIndex(calls)])
    If items.Contains(6) AndAlso items.IndexOf(6) = 0 Then
        Return items.Item(0)*100 + calls
    End If
    Return -1
End Sub
```

**Erläuterung der Parameter und Ausführung:**

- NextIndex läuft einmal: calls=1, Index 0. Bump ändert 5 auf 6. Contains(6)=TRUE, IndexOf(6)=0, Item(0) liefert 6. Main liefert Integer 601.
