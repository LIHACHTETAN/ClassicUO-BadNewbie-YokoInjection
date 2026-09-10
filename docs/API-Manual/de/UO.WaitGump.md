# UO.WaitGump

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Registriert eine geordnete Folge einmaliger Schaltflächenantworten. Das Skript läuft sofort weiter; ein fehlendes Fenster blockiert es nicht für 30 Sekunden.

## Genaue Syntax

```text
UO.WaitGump(Value:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any) -> Unit
UO.WaitGump(trigger1:Any, trigger2:Any, trigger3:Any, trigger4:Any, trigger5:Any, trigger6:Any, trigger7:Any, trigger8:Any, trigger9:Any, trigger10:Any, trigger11:Any, trigger12:Any, trigger13:Any, trigger14:Any, trigger15:Any, trigger16:Any) -> Unit
UO.WaitGump(triggerId:Integer) -> Unit
UO.WaitGump(triggerId:String) -> Unit
```

## Parameter

- `triggerId` — Integer ButtonID oder numerischer String. Ein String kann eine durch | oder Kommas getrennte Folge enthalten. Formen mit 2..16 Parametern erlauben auch Arrays und verschachtelte Folgen. Alle IDs werden vorab ausgewertet. Eine leere Folge, mehr als 256 ausstehende Client-Schaltflächen oder mehr als 32 Verschachtelungsebenen verursachen einen Fehler ohne Teilregistrierung.
- `Value` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger1` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger2` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger3` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger4` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger5` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger6` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger7` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger8` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger9` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger10` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger11` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger12` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger13` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger14` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger15` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.
- `trigger16` — Folgenelement: Integer ButtonID, numerischer String, durch |/Kommas getrennter String oder Array dieser Elemente. Von links nach rechts nach den Regeln und Grenzen von triggerId. Value benennt den einzelnen Any-Parameter, der ebenfalls Arrays akzeptiert.

## Rückgabewert

Unit — kein Rückgabewert: weder Erfolg noch neuer Wert noch Serverbestätigung.

## Verhalten

- Benötigt eine echte Activate-Schaltfläche mit passender ButtonID; Seitenwechsel und unpassende Fenster werden übersprungen. Spätere IDs überholen die erste ausstehende ID nicht. Pro Layoutempfang höchstens eine Antwort je Fenster. Ein neues Layout darf dasselbe Fensterobjekt wiederverwenden.
- Ein weiterer WaitGump desselben Skripts ergänzt dessen ausstehende Folge. Kein GumpID-Filter: für genaue Auswahl NumGumpButton oder SendGumpSelect verwenden. ButtonID=0 benötigt eine echte Activate-Schaltfläche mit ID 0 und schließt nicht beliebige Fenster.
- Normales Prozedurende erhält ausstehende Aktionen. Abbruch des Besitzers oder Terminate mit seinem Namen entfernt sie; TerminateAll entfernt alle, auch die beendeter Prozeduren. Ein Weltwechsel leert die Warteschlange. Keine Speicherung im Profil.

## Beispiele

### Eine Antwort

```vb
# Eine Antwort
#
# Registriert eine geordnete Folge einmaliger Schaltflächenantworten. Das Skript läuft sofort
# weiter; ein fehlendes Fenster blockiert es nicht für 30 Sekunden.
#
# Unit — kein Rückgabewert: weder Erfolg noch neuer Wert noch Serverbestätigung.

SUB Main()
    # 100 ist die Antwort-ButtonID. WaitGump registriert sie vor UseObject. Das Weiterlaufen des
    # Skripts beweist keine Serverbestätigung.

    UO.WaitGump(100)
    UO.UseObject('0x40001234')
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- 100 ist die Antwort-ButtonID. WaitGump registriert sie vor UseObject. Das Weiterlaufen des Skripts beweist keine Serverbestätigung.

### Mehrere Schritte

```vb
# Mehrere Schritte
#
# Registriert eine geordnete Folge einmaliger Schaltflächenantworten. Das Skript läuft sofort
# weiter; ein fehlendes Fenster blockiert es nicht für 30 Sekunden.
#
# Unit — kein Rückgabewert: weder Erfolg noch neuer Wert noch Serverbestätigung.

SUB Main()
    # 7, 22 und 1 sind ButtonIDs aufeinanderfolgender Formulare und werden in dieser Reihenfolge
    # geprüft. Die Parameteranzahl ist keine Wartezeit; registriert wird die gesamte Folge.

    UO.WaitGump(7,22,1)
    UO.UseObject('0x40001234')
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- 7, 22 und 1 sind ButtonIDs aufeinanderfolgender Formulare und werden in dieser Reihenfolge geprüft. Die Parameteranzahl ist keine Wartezeit; registriert wird die gesamte Folge.

### Wartende Aktionen abbrechen

```vb
# Wartende Aktionen abbrechen
#
# Registriert eine geordnete Folge einmaliger Schaltflächenantworten. Das Skript läuft sofort
# weiter; ein fehlendes Fenster blockiert es nicht für 30 Sekunden.
#
# Unit — kein Rückgabewert: weder Erfolg noch neuer Wert noch Serverbestätigung.

SUB Main()
    # 7|22|1 beschreibt dieselbe Folge. TerminateAll entfernt anschließend alle ausstehenden
    # Gump-Aktionen und stoppt alle Prozeduren; die Wirkung ist global.

    UO.WaitGump('7|22|1')
    UO.TerminateAll()
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- 7|22|1 beschreibt dieselbe Folge. TerminateAll entfernt anschließend alle ausstehenden Gump-Aktionen und stoppt alle Prozeduren; die Wirkung ist global.
