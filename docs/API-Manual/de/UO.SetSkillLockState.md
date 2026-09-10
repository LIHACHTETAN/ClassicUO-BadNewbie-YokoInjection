# UO.SetSkillLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Fordert einen anderen Steigerungsmodus für die Fertigkeit an.

## Genaue Syntax

```text
UO.SetSkillLockState(SkillName:Any, skillState:Any) -> Unit
```

## Parameter

- `SkillName` — Erforderliche Fertigkeit: Name aus den Clientdaten, etwa "Mining" oder "Animal Lore", oder Dezimalindex 0..Skills.Length−1 als Zahl oder Zeichenfolge. Groß-/Kleinschreibung wird ignoriert, äußere Leerzeichen entfernt und _ durch ein Leerzeichen ersetzt. Keine Gegenstands-ID und kein bei 1 beginnender Index. Numerische Zeichenfolgen sind immer Indizes.
- `skillState` — Erforderlicher Modus: 0 — steigern, 1 — senken, 2 — sperren. Drei Codes, kein Boolean; true/false bilden nicht alle Modi ab.

## Rückgabewert

Unit — kein Rückgabewert. Nicht als Erfolg/Fehler behandeln oder mit true vergleichen. Nachfolgendes Lesen zeigt das lokale Modell, keine Serverbestätigung.

## Verhalten

- Eine gültige Anforderung sendet ein Paket über GameActions und ändert sofort den lokalen Modus. Serverregeln gelten weiterhin; eine Steigerung ist nicht garantiert. Unbekannte Fertigkeiten, ungültige Indizes/Modi und fehlende Charaktere werden ohne Paket ignoriert.
- Erforderliche Fertigkeit: Name aus den Clientdaten, etwa "Mining" oder "Animal Lore", oder Dezimalindex 0..Skills.Length−1 als Zahl oder Zeichenfolge. Groß-/Kleinschreibung wird ignoriert, äußere Leerzeichen entfernt und _ durch ein Leerzeichen ersetzt. Keine Gegenstands-ID und kein bei 1 beginnender Index. Numerische Zeichenfolgen sind immer Indizes.
- ExecuteStealthCompatibility wählt den Zweig. Text liest den Fertigkeitsselektor, Arg numerische Nummern und Modi. Nicht konvertierbare Argumente können einen Konvertierungsfehler auslösen.

### Interne Funktionen: vom Aufruf zum Ergebnis

Dies sind die tatsächlichen internen C#-Schritte. ApplyMode ist eine vollständig definierte Hilfsfunktion im Beispiel, kein verborgener integrierter Befehl.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility wählt den Zweig. Text liest den Fertigkeitsselektor, Arg numerische Nummern und Modi. Nicht konvertierbare Argumente können einen Konvertierungsfehler auslösen.

Unit — kein Rückgabewert. Nicht als Erfolg/Fehler behandeln oder mit true vergleichen. Nachfolgendes Lesen zeigt das lokale Modell, keine Serverbestätigung.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke liest im Spielthread; ein Arbeitsthread wartet auf die Verarbeitung durch den Manager. Skriptabbruch unterbricht das Warten. Keine zusätzliche Verzögerung oder Netzwerkanfrage.

Eine gültige Anforderung sendet ein Paket über GameActions und ändert sofort den lokalen Modus. Serverregeln gelten weiterhin; eine Steigerung ist nicht garantiert. Unbekannte Fertigkeiten, ungültige Indizes/Modi und fehlende Charaktere werden ohne Paket ignoriert.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 3. FindSkillUnsafe

FindSkillUnsafe prüft zuerst den Dezimalindex und seine Grenzen; andernfalls normalisiert es den Namen und vergleicht Skill.Name exakt ohne Groß-/Kleinschreibung. Unbekannte Namen ergeben null; kein Zielcursor wird geöffnet.

Unbekannte Fertigkeit oder fehlender Charakter liefert −1.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `FindSkillUnsafe`.

#### 4. SetSkillLockState

Eine gültige Anforderung sendet ein Paket über GameActions und ändert sofort den lokalen Modus. Serverregeln gelten weiterhin; eine Steigerung ist nicht garantiert. Unbekannte Fertigkeiten, ungültige Indizes/Modi und fehlende Charaktere werden ohne Paket ignoriert.

Unit — kein Rückgabewert. Nicht als Erfolg/Fehler behandeln oder mit true vergleichen. Nachfolgendes Lesen zeigt das lokale Modell, keine Serverbestätigung.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `SetSkillLockState`.

#### 5. ChangeSkillLockStatus

Eine gültige Anforderung sendet ein Paket über GameActions und ändert sofort den lokalen Modus. Serverregeln gelten weiterhin; eine Steigerung ist nicht garantiert. Unbekannte Fertigkeiten, ungültige Indizes/Modi und fehlende Charaktere werden ohne Paket ignoriert.

Unit — kein Rückgabewert. Nicht als Erfolg/Fehler behandeln oder mit true vergleichen. Nachfolgendes Lesen zeigt das lokale Modell, keine Serverbestätigung.

Projektquelle: `src/ClassicUO.Client/Game/GameActions.cs`; Funktion `ChangeSkillLockStatus`.

Eine gültige Anforderung sendet ein Paket über GameActions und ändert sofort den lokalen Modus. Serverregeln gelten weiterhin; eine Steigerung ist nicht garantiert. Unbekannte Fertigkeiten, ungültige Indizes/Modi und fehlende Charaktere werden ohne Paket ignoriert.


## Beispiele

### Lesen und anzeigen

```vb
# Lesen und anzeigen
#
# Fordert einen anderen Steigerungsmodus für die Fertigkeit an.
#
# Unit — kein Rückgabewert. Nicht als Erfolg/Fehler behandeln oder mit true vergleichen.
# Nachfolgendes Lesen zeigt das lokale Modell, keine Serverbestätigung.

SUB Main()
    # Das Beispiel setzt selector und beim Schreiben mode ausdrücklich. Die erste Zeile wählt eine
    # Fertigkeit per Name oder Eigenschaft per Nummer. Print zeigt nur das Ergebnis.

    VAR selector = 'Mining'
    VAR mode = 2
    UO.SetSkillLockState(selector, mode)
    UO.Print(CStr(UO.GetSkillLockState(selector)))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Das Beispiel setzt selector und beim Schreiben mode ausdrücklich. Die erste Zeile wählt eine Fertigkeit per Name oder Eigenschaft per Nummer. Print zeigt nur das Ergebnis.

### In Bedingung oder Vergleich verwenden

```vb
# In Bedingung oder Vergleich verwenden
#
# Fordert einen anderen Steigerungsmodus für die Fertigkeit an.
#
# Unit — kein Rückgabewert. Nicht als Erfolg/Fehler behandeln oder mit true vergleichen.
# Nachfolgendes Lesen zeigt das lokale Modell, keine Serverbestätigung.

SUB Main()
    # Grenzwert 95.1 und Modi 0/1/2 sind Beispieleinstellungen. Vor Modusänderungen −1 prüfen. Lesen
    # nach dem Schreiben zeigt die lokale Kopie ohne Warten auf den Server.

    VAR selector = 'Mining'
    VAR before = UO.GetSkillLockState(selector)
    IF before >= 0 AND before <= 2 THEN
        UO.SetSkillLockState(selector, 0)
        UO.Print(CStr(UO.GetSkillLockState(selector)))
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Grenzwert 95.1 und Modi 0/1/2 sind Beispieleinstellungen. Vor Modusänderungen −1 prüfen. Lesen nach dem Schreiben zeigt die lokale Kopie ohne Warten auf den Server.

### Vollständige Hilfsfunktion

```vb
# Vollständige Hilfsfunktion
#
# Fordert einen anderen Steigerungsmodus für die Fertigkeit an.
#
# Unit — kein Rückgabewert. Nicht als Erfolg/Fehler behandeln oder mit true vergleichen.
# Nachfolgendes Lesen zeigt das lokale Modell, keine Serverbestätigung.

SUB Main()
    # Der vollständige Helfer folgt Main. selector wählt Fertigkeit/Eigenschaft, mode den
    # Schreibmodus. ReadValue/ReadMode liefern die ursprüngliche Zahl; ApplyMode prüft Argumente,
    # handelt und liefert keinen Wert. WAIT(1000) trennt zwei Lesemomentaufnahmen.

    ApplyMode('Mining', 2)
END SUB

SUB ApplyMode(selector, mode)
    IF mode < 0 OR mode > 2 THEN
        RETURN
    END IF
    IF UO.GetSkillLockState(selector) < 0 THEN
        RETURN
    END IF
    UO.SetSkillLockState(selector, mode)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Der vollständige Helfer folgt Main. selector wählt Fertigkeit/Eigenschaft, mode den Schreibmodus. ReadValue/ReadMode liefern die ursprüngliche Zahl; ApplyMode prüft Argumente, handelt und liefert keinen Wert. WAIT(1000) trennt zwei Lesemomentaufnahmen.
