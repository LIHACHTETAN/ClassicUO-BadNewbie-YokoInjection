# UO.GumpAutoCheckBox

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Setzt einen Wert einmalig im ersten passenden Steuerelement eines Server-Gumps. Fehlt es, bleibt die Aktion ausstehend.

## Genaue Syntax

```text
UO.GumpAutoCheckBox(CheckBoxID:Any, Value:Any) -> Unit
```

## Parameter

- `CheckBoxID` — Integer — genaue ID des betreffenden Steuerelementtyps. Kein Index, keine GumpID und keine Fenster-Serial. 0 ist eine gewöhnliche ID und wählt nicht ersatzweise das erste Element.
- `Value` — Integer — 1 einschalten, 0 ausschalten. Andere Zahlen ungleich null schalten ebenfalls ein; 0/1 verwenden. Eine gewählte Optionsschaltfläche hebt die Auswahl ihrer Geschwister derselben Gruppe auf.

## Rückgabewert

Unit — kein Rückgabewert: weder Erfolg noch neuer Wert noch Serverbestätigung.

## Verhalten

- Prüft bestehende Fenster in aktueller Oberflächenreihenfolge, danach empfangene oder neu aufgebaute Serverlayouts. Der erste passende Typ mit passender ID verbraucht die Aktion. Für ein bestimmtes Fenster NumGump* mit Index verwenden.
- Ausstehende Felder werden vor automatischen Schaltflächenantworten gesetzt. Ein erneuter Aufruf mit gleichem Typ und gleicher ID im selben Skript ersetzt einen noch ausstehenden Wert. Höchstens 1024 ausstehende Felder im Client; Überschreitung verursacht einen Skriptfehler.
- Normales Prozedurende erhält ausstehende Aktionen. Abbruch des Besitzers oder Terminate mit seinem Namen entfernt sie; TerminateAll entfernt alle, auch die beendeter Prozeduren. Ein Weltwechsel leert die Warteschlange. Keine Speicherung im Profil.

## Beispiele

### Offenes Element ausfüllen

```vb
# Offenes Element ausfüllen
#
# Setzt einen Wert einmalig im ersten passenden Steuerelement eines Server-Gumps. Fehlt es,
# bleibt die Aktion ausstehend.
#
# Unit — kein Rückgabewert: weder Erfolg noch neuer Wert noch Serverbestätigung.

SUB Main()
    # 33 ist eine Beispiel-ID; durch die tatsächliche ID aus InfoGump ersetzen. Der zweite Parameter
    # ist der Wert. Fehlt das Element, bleibt die Aktion ausstehend.

    UO.GumpAutoCheckBox(33, 1)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- 33 ist eine Beispiel-ID; durch die tatsächliche ID aus InfoGump ersetzen. Der zweite Parameter ist der Wert. Fehlt das Element, bleibt die Aktion ausstehend.

### Vor dem Öffnen ausfüllen

```vb
# Vor dem Öffnen ausfüllen
#
# Setzt einen Wert einmalig im ersten passenden Steuerelement eines Server-Gumps. Fehlt es,
# bleibt die Aktion ausstehend.
#
# Unit — kein Rückgabewert: weder Erfolg noch neuer Wert noch Serverbestätigung.

SUB Main()
    # 33 ist die Element-ID, 100 eine Beispiel-ButtonID zur Bestätigung und 0x40001234 die Serial
    # des Objekts, das das Formular öffnet. Alle drei anpassen. Das Feld wird vor der Antwort
    # gesetzt, auch bei späterem Fenstereingang.

    UO.GumpAutoCheckBox(33, 1)
    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- 33 ist die Element-ID, 100 eine Beispiel-ButtonID zur Bestätigung und 0x40001234 die Serial des Objekts, das das Formular öffnet. Alle drei anpassen. Das Feld wird vor der Antwort gesetzt, auch bei späterem Fenstereingang.

### Ausstehenden Wert ersetzen

```vb
# Ausstehenden Wert ersetzen
#
# Setzt einen Wert einmalig im ersten passenden Steuerelement eines Server-Gumps. Fehlt es,
# bleibt die Aktion ausstehend.
#
# Unit — kein Rückgabewert: weder Erfolg noch neuer Wert noch Serverbestätigung.

SUB Main()
    # Beide Aufrufe verwenden ID 33. Vor dem Eintreffen des Elements gilt der letzte Wert. Bei
    # offenem Fenster werden beide Änderungen sofort in Aufrufreihenfolge ausgeführt.

    UO.GumpAutoCheckBox(33, 1)
    UO.GumpAutoCheckBox(33, 0)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Beide Aufrufe verwenden ID 33. Vor dem Eintreffen des Elements gilt der letzte Wert. Bei offenem Fenster werden beide Änderungen sofort in Aufrufreihenfolge ausgeführt.
