# UO.GetStatLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest den lokalen Steigerungsmodus einer Eigenschaft.

## Genaue Syntax

```text
UO.GetStatLockState(statNum:Any) -> Integer
```

## Parameter

- `statNum` — Erforderliche Eigenschaftsnummer: 0 — STR, 1 — DEX, 2 — INT. Weder der aktuelle Wert noch ein ausgeschriebener Name.

## Rückgabewert

Integer: 0 — steigern, 1 — senken, 2 — sperren. Moduscode, nicht true/false. Nummern außerhalb 0..2 liefern −1. Ohne Charakter liefert eine gültige Nummer standardmäßig 0; keine Bestätigung des Serverzustands.

## Verhalten

- Invoke liest vorhandene Daten im Spielthread und sendet keine Netzwerkpakete. Die Fertigkeit wird weder benutzt noch trainiert. Zwei Abfragen sind getrennte Momentaufnahmen.
- Erforderliche Eigenschaftsnummer: 0 — STR, 1 — DEX, 2 — INT. Weder der aktuelle Wert noch ein ausgeschriebener Name.
- ExecuteStealthCompatibility wählt den Zweig. Text liest den Fertigkeitsselektor, Arg numerische Nummern und Modi. Nicht konvertierbare Argumente können einen Konvertierungsfehler auslösen.

### Interne Funktionen: vom Aufruf zum Ergebnis

Dies sind die tatsächlichen internen C#-Schritte. ReadMode ist eine vollständig definierte Hilfsfunktion im Beispiel, kein verborgener integrierter Befehl.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility wählt den Zweig. Text liest den Fertigkeitsselektor, Arg numerische Nummern und Modi. Nicht konvertierbare Argumente können einen Konvertierungsfehler auslösen.

Integer: 0 — steigern, 1 — senken, 2 — sperren. Moduscode, nicht true/false. Nummern außerhalb 0..2 liefern −1. Ohne Charakter liefert eine gültige Nummer standardmäßig 0; keine Bestätigung des Serverzustands.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke liest im Spielthread; ein Arbeitsthread wartet auf die Verarbeitung durch den Manager. Skriptabbruch unterbricht das Warten. Keine zusätzliche Verzögerung oder Netzwerkanfrage.

Invoke liest vorhandene Daten im Spielthread und sendet keine Netzwerkpakete. Die Fertigkeit wird weder benutzt noch trainiert. Zwei Abfragen sind getrennte Momentaufnahmen.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 3. GetStatLockState

GetStatLockState/SetStatLockState wählen StrLock, DexLock oder IntLock anhand 0/1/2. Unbekannte Nummern lesen −1; Schreiben prüft beide Grenzen vor dem Senden.

Integer: 0 — steigern, 1 — senken, 2 — sperren. Moduscode, nicht true/false. Nummern außerhalb 0..2 liefern −1. Ohne Charakter liefert eine gültige Nummer standardmäßig 0; keine Bestätigung des Serverzustands.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `GetStatLockState`.

Invoke liest vorhandene Daten im Spielthread und sendet keine Netzwerkpakete. Die Fertigkeit wird weder benutzt noch trainiert. Zwei Abfragen sind getrennte Momentaufnahmen.


## Beispiele

### Lesen und anzeigen

```vb
# Lesen und anzeigen
#
# Liest den lokalen Steigerungsmodus einer Eigenschaft.
#
# Integer: 0 — steigern, 1 — senken, 2 — sperren. Moduscode, nicht true/false. Nummern außerhalb
# 0..2 liefern −1. Ohne Charakter liefert eine gültige Nummer standardmäßig 0; keine Bestätigung
# des Serverzustands.

SUB Main()
    # Das Beispiel setzt selector und beim Schreiben mode ausdrücklich. Die erste Zeile wählt eine
    # Fertigkeit per Name oder Eigenschaft per Nummer. Print zeigt nur das Ergebnis.

    VAR selector = 0
    VAR mode = UO.GetStatLockState(selector)
    UO.Print(CStr(mode))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Das Beispiel setzt selector und beim Schreiben mode ausdrücklich. Die erste Zeile wählt eine Fertigkeit per Name oder Eigenschaft per Nummer. Print zeigt nur das Ergebnis.

### In Bedingung oder Vergleich verwenden

```vb
# In Bedingung oder Vergleich verwenden
#
# Liest den lokalen Steigerungsmodus einer Eigenschaft.
#
# Integer: 0 — steigern, 1 — senken, 2 — sperren. Moduscode, nicht true/false. Nummern außerhalb
# 0..2 liefern −1. Ohne Charakter liefert eine gültige Nummer standardmäßig 0; keine Bestätigung
# des Serverzustands.

SUB Main()
    # Grenzwert 95.1 und Modi 0/1/2 sind Beispieleinstellungen. Vor Modusänderungen −1 prüfen. Lesen
    # nach dem Schreiben zeigt die lokale Kopie ohne Warten auf den Server.

    VAR mode = UO.GetStatLockState(0)
    IF mode = 2 THEN
        UO.Print("Locked")
    ELSE
        IF mode = -1 THEN
            UO.Print("Unknown selector")
        ELSE
            UO.Print("Mode: " + CStr(mode))
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
# Liest den lokalen Steigerungsmodus einer Eigenschaft.
#
# Integer: 0 — steigern, 1 — senken, 2 — sperren. Moduscode, nicht true/false. Nummern außerhalb
# 0..2 liefern −1. Ohne Charakter liefert eine gültige Nummer standardmäßig 0; keine Bestätigung
# des Serverzustands.

SUB Main()
    # Der vollständige Helfer folgt Main. selector wählt Fertigkeit/Eigenschaft, mode den
    # Schreibmodus. ReadValue/ReadMode liefern die ursprüngliche Zahl; ApplyMode prüft Argumente,
    # handelt und liefert keinen Wert. WAIT(1000) trennt zwei Lesemomentaufnahmen.

    VAR before = ReadMode(0)
    WAIT(1000)
    VAR after = ReadMode(0)
    UO.Print(CStr(before) + " -> " + CStr(after))
END SUB

SUB ReadMode(selector)
    RETURN UO.GetStatLockState(selector)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Der vollständige Helfer folgt Main. selector wählt Fertigkeit/Eigenschaft, mode den Schreibmodus. ReadValue/ReadMode liefern die ursprüngliche Zahl; ApplyMode prüft Argumente, handelt und liefert keinen Wert. WAIT(1000) trennt zwei Lesemomentaufnahmen.
