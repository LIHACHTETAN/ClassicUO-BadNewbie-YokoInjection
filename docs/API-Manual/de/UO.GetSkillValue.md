# UO.GetSkillValue

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest den Basiswert der Fertigkeit ohne Modifikatoren.

## Genaue Syntax

```text
UO.GetSkillValue(SkillName:Any) -> Decimal
```

## Parameter

- `SkillName` — Erforderliche Fertigkeit: Name aus den Clientdaten, etwa "Mining" oder "Animal Lore", oder Dezimalindex 0..Skills.Length−1 als Zahl oder Zeichenfolge. Groß-/Kleinschreibung wird ignoriert, äußere Leerzeichen entfernt und _ durch ein Leerzeichen ersetzt. Keine Gegenstands-ID und kein bei 1 beginnender Index. Numerische Zeichenfolgen sind immer Indizes.

## Rückgabewert

Decimal (Double) — Fertigkeitspunkte in Zehnteln, etwa 95,1 statt 951. Feld BaseFixed wird direkt als Double durch 10 geteilt. Null bedeutet Nullwert oder fehlenden Charakter/fehlende Fertigkeit. Kein Boolean. Alte SkillVal/BaseVal nutzen eine andere Skala; Familien nicht vermischen.

## Verhalten

- Invoke liest vorhandene Daten im Spielthread und sendet keine Netzwerkpakete. Die Fertigkeit wird weder benutzt noch trainiert. Zwei Abfragen sind getrennte Momentaufnahmen.
- Erforderliche Fertigkeit: Name aus den Clientdaten, etwa "Mining" oder "Animal Lore", oder Dezimalindex 0..Skills.Length−1 als Zahl oder Zeichenfolge. Groß-/Kleinschreibung wird ignoriert, äußere Leerzeichen entfernt und _ durch ein Leerzeichen ersetzt. Keine Gegenstands-ID und kein bei 1 beginnender Index. Numerische Zeichenfolgen sind immer Indizes.
- ExecuteStealthCompatibility wählt den Zweig. Text liest den Fertigkeitsselektor, Arg numerische Nummern und Modi. Nicht konvertierbare Argumente können einen Konvertierungsfehler auslösen.

### Interne Funktionen: vom Aufruf zum Ergebnis

Dies sind die tatsächlichen internen C#-Schritte. ReadValue ist eine vollständig definierte Hilfsfunktion im Beispiel, kein verborgener integrierter Befehl.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility wählt den Zweig. Text liest den Fertigkeitsselektor, Arg numerische Nummern und Modi. Nicht konvertierbare Argumente können einen Konvertierungsfehler auslösen.

Decimal (Double) — Fertigkeitspunkte in Zehnteln, etwa 95,1 statt 951. Feld BaseFixed wird direkt als Double durch 10 geteilt. Null bedeutet Nullwert oder fehlenden Charakter/fehlende Fertigkeit. Kein Boolean. Alte SkillVal/BaseVal nutzen eine andere Skala; Familien nicht vermischen.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke liest im Spielthread; ein Arbeitsthread wartet auf die Verarbeitung durch den Manager. Skriptabbruch unterbricht das Warten. Keine zusätzliche Verzögerung oder Netzwerkanfrage.

Invoke liest vorhandene Daten im Spielthread und sendet keine Netzwerkpakete. Die Fertigkeit wird weder benutzt noch trainiert. Zwei Abfragen sind getrennte Momentaufnahmen.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 3. FindSkillUnsafe

FindSkillUnsafe prüft zuerst den Dezimalindex und seine Grenzen; andernfalls normalisiert es den Namen und vergleicht Skill.Name exakt ohne Groß-/Kleinschreibung. Unbekannte Namen ergeben null; kein Zielcursor wird geöffnet.

Unbekannte Fertigkeit oder fehlender Charakter liefert −1.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `FindSkillUnsafe`.

#### 4. GetSkillValue

GetSkillValue wählt BaseFixed, ValueFixed oder CapFixed und teilt die ganzzahligen Zehntel durch 10d, ohne zwischenzeitliche Single-Rundung.

Decimal (Double) — Fertigkeitspunkte in Zehnteln, etwa 95,1 statt 951. Feld BaseFixed wird direkt als Double durch 10 geteilt. Null bedeutet Nullwert oder fehlenden Charakter/fehlende Fertigkeit. Kein Boolean. Alte SkillVal/BaseVal nutzen eine andere Skala; Familien nicht vermischen.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `GetSkillValue`.

Invoke liest vorhandene Daten im Spielthread und sendet keine Netzwerkpakete. Die Fertigkeit wird weder benutzt noch trainiert. Zwei Abfragen sind getrennte Momentaufnahmen.


## Beispiele

### Lesen und anzeigen

```vb
# Lesen und anzeigen
#
# Liest den Basiswert der Fertigkeit ohne Modifikatoren.
#
# Decimal (Double) — Fertigkeitspunkte in Zehnteln, etwa 95,1 statt 951. Feld BaseFixed wird
# direkt als Double durch 10 geteilt. Null bedeutet Nullwert oder fehlenden Charakter/fehlende
# Fertigkeit. Kein Boolean. Alte SkillVal/BaseVal nutzen eine andere Skala; Familien nicht
# vermischen.

SUB Main()
    # Das Beispiel setzt selector und beim Schreiben mode ausdrücklich. Die erste Zeile wählt eine
    # Fertigkeit per Name oder Eigenschaft per Nummer. Print zeigt nur das Ergebnis.

    VAR selector = 'Mining'
    VAR value = UO.GetSkillValue(selector)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Das Beispiel setzt selector und beim Schreiben mode ausdrücklich. Die erste Zeile wählt eine Fertigkeit per Name oder Eigenschaft per Nummer. Print zeigt nur das Ergebnis.

### In Bedingung oder Vergleich verwenden

```vb
# In Bedingung oder Vergleich verwenden
#
# Liest den Basiswert der Fertigkeit ohne Modifikatoren.
#
# Decimal (Double) — Fertigkeitspunkte in Zehnteln, etwa 95,1 statt 951. Feld BaseFixed wird
# direkt als Double durch 10 geteilt. Null bedeutet Nullwert oder fehlenden Charakter/fehlende
# Fertigkeit. Kein Boolean. Alte SkillVal/BaseVal nutzen eine andere Skala; Familien nicht
# vermischen.

SUB Main()
    # Grenzwert 95.1 und Modi 0/1/2 sind Beispieleinstellungen. Vor Modusänderungen −1 prüfen. Lesen
    # nach dem Schreiben zeigt die lokale Kopie ohne Warten auf den Server.

    IF UO.GetSkillLockState('Mining') >= 0 THEN
        VAR value = UO.GetSkillValue('Mining')
        IF value >= 95.1 THEN
            UO.Print('Value >= 95.1: ' + CStr(value))
        END IF
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Grenzwert 95.1 und Modi 0/1/2 sind Beispieleinstellungen. Vor Modusänderungen −1 prüfen. Lesen nach dem Schreiben zeigt die lokale Kopie ohne Warten auf den Server.

### Vollständige Hilfsfunktion

```vb
# Vollständige Hilfsfunktion
#
# Liest den Basiswert der Fertigkeit ohne Modifikatoren.
#
# Decimal (Double) — Fertigkeitspunkte in Zehnteln, etwa 95,1 statt 951. Feld BaseFixed wird
# direkt als Double durch 10 geteilt. Null bedeutet Nullwert oder fehlenden Charakter/fehlende
# Fertigkeit. Kein Boolean. Alte SkillVal/BaseVal nutzen eine andere Skala; Familien nicht
# vermischen.

SUB Main()
    # Der vollständige Helfer folgt Main. selector wählt Fertigkeit/Eigenschaft, mode den
    # Schreibmodus. ReadValue/ReadMode liefern die ursprüngliche Zahl; ApplyMode prüft Argumente,
    # handelt und liefert keinen Wert. WAIT(1000) trennt zwei Lesemomentaufnahmen.

    VAR before = ReadValue('Animal_Lore')
    WAIT(1000)
    VAR after = ReadValue('Animal Lore')
    UO.Print(CStr(after - before))
END SUB

SUB ReadValue(selector)
    RETURN UO.GetSkillValue(selector)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Der vollständige Helfer folgt Main. selector wählt Fertigkeit/Eigenschaft, mode den Schreibmodus. ReadValue/ReadMode liefern die ursprüngliche Zahl; ApplyMode prüft Argumente, handelt und liefert keinen Wert. WAIT(1000) trennt zwei Lesemomentaufnahmen.
