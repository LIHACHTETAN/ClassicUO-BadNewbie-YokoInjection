# UO.GetMaxMana

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest das maximale Mana aus dem lokalen Modell.

## Genaue Syntax

```text
UO.GetMaxMana() -> Integer
UO.GetMaxMana(ObjID:Any) -> Any
```

## Parameter

- `ObjID` — Optionales Objekt in den gezeigten Formen: numerischer serial, Hex-Zeichenfolge, self, lasttarget oder registrierter AddObject-Name. Kein type. Ohne Argument wird self gelesen. Unbekannter Text verursacht in manchen Formen einen Konvertierungsfehler; den Namen vorher prüfen.

## Rückgabewert

Integer — Feldwert ManaMax, kein Prozentsatz und kein Boolean. Null kann ein echter Wert oder fehlende Information sein. Nie durch ein Maximum von null teilen. Werte anderer Mobiles können unbekannt sein. HP/HitsMax können eine relative Serverskala statt exakter Punkte enthalten. HP=0 beweist keinen Tod; dafür Dead/IsDead verwenden.

## Verhalten

- Öffnet keinen status und fordert kein Serverupdate an. Anders als Stealths automatische Anfrage bei fehlenden HP liest dieser Client nur vorhandene Daten. Keine Eigenschaftsänderung oder Paketsendung.
- Jedes Ergebnis ist eine einzelne Abfrage. Zwischen Exists und dem nächsten Aufruf kann sich die Welt ändern; mehrere Abfragen bilden keinen atomaren Schnappschuss.
- Bei Objekten verwirft World.Get fehlende oder IsDestroyed-Einträge und liefert 0. HP/HitsMax lesen Entity-Felder, auch bei Gegenständen mit diesen Feldern; Mana/Stamina erfordern Mobile. Ohne Argument wird self gelesen. Nicht jeder Name ohne Argument hat eine ID-Form: Signaturen prüfen.
- Auch parameterlose Abfragen liefern bei fehlendem/zerstörtem Player 0. Das gilt für direkte Mana/Stamina-Werte und ihre Maxima, nicht nur für World.Get. Ein vorhandener toter Charakter kann weiterhin Werte besitzen.

### Interne Funktionen: vom Aufruf zum Ergebnis

Dies sind die tatsächlichen internen C#-Schritte. ReadValue ist eine vollständig definierte Hilfsfunktion im Beispiel, kein verborgener integrierter Befehl.

#### 1. RegisterCharacterGetterAliases

Beim Erstellen des runtime registriert RegisterCharacterGetterAliases Namen und Formen. Ohne Argument wird bridge.Self gewählt, mit Argument dessen serial. Bestehende Registrierungen bleiben erhalten.

Integer — Feldwert ManaMax, kein Prozentsatz und kein Boolean. Null kann ein echter Wert oder fehlende Information sein. Nie durch ein Maximum von null teilen. Werte anderer Mobiles können unbekannt sein. HP/HitsMax können eine relative Serverskala statt exakter Punkte enthalten. HP=0 beweist keinen Tod; dafür Dead/IsDead verwenden.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `RegisterCharacterGetterAliases`.

#### 2. TryGetObject

TryGetObject löst Zahlen, Hex-Zeichenfolgen und gespeicherte Namen auf. AddObject-Namen werden bei jedem Aufruf neu aufgelöst; keine Suche nach graphic/type und keine interaktive Auswahl.

Optionales Objekt in den gezeigten Formen: numerischer serial, Hex-Zeichenfolge, self, lasttarget oder registrierter AddObject-Name. Kein type. Ohne Argument wird self gelesen. Unbekannter Text verursacht in manchen Formen einen Konvertierungsfehler; den Namen vorher prüfen.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `TryGetObject`.

#### 3. Invoke

Invoke liest im Spielthread; ein Arbeitsthread wartet auf die Verarbeitung durch den Manager. Skriptabbruch unterbricht das Warten. Keine zusätzliche Verzögerung oder Netzwerkanfrage.

Jedes Ergebnis ist eine einzelne Abfrage. Zwischen Exists und dem nächsten Aufruf kann sich die Welt ändern; mehrere Abfragen bilden keinen atomaren Schnappschuss.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 4. Get

Bei Objekten verwirft World.Get fehlende oder IsDestroyed-Einträge und liefert 0. HP/HitsMax lesen Entity-Felder, auch bei Gegenständen mit diesen Feldern; Mana/Stamina erfordern Mobile. Ohne Argument wird self gelesen. Nicht jeder Name ohne Argument hat eine ID-Form: Signaturen prüfen.

Integer — Feldwert ManaMax, kein Prozentsatz und kein Boolean. Null kann ein echter Wert oder fehlende Information sein. Nie durch ein Maximum von null teilen. Werte anderer Mobiles können unbekannt sein. HP/HitsMax können eine relative Serverskala statt exakter Punkte enthalten. HP=0 beweist keinen Tod; dafür Dead/IsDead verwenden.

Projektquelle: `src/ClassicUO.Client/Game/World.cs`; Funktion `Get`.

Öffnet keinen status und fordert kein Serverupdate an. Anders als Stealths automatische Anfrage bei fehlenden HP liest dieser Client nur vorhandene Daten. Keine Eigenschaftsänderung oder Paketsendung.


## Beispiele

### Eigenen Charakterwert anzeigen

```vb
# Eigenen Charakterwert anzeigen
#
# Liest das maximale Mana aus dem lokalen Modell.
#
# Integer — Feldwert ManaMax, kein Prozentsatz und kein Boolean. Null kann ein echter Wert oder
# fehlende Information sein. Nie durch ein Maximum von null teilen. Werte anderer Mobiles können
# unbekannt sein. HP/HitsMax können eine relative Serverskala statt exakter Punkte enthalten.
# HP=0 beweist keinen Tod; dafür Dead/IsDead verwenden.

SUB Main()
    # Der Aufruf ohne Argument liest self. value speichert eine Zahl; STR wandelt sie nur für die
    # Meldung um.

    VAR value = UO.GetMaxMana()
    UO.Print('GetMaxMana: ' + STR(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Der Aufruf ohne Argument liest self. value speichert eine Zahl; STR wandelt sie nur für die Meldung um.

### Wert in Bedingung oder Berechnung verwenden

```vb
# Wert in Bedingung oder Berechnung verwenden
#
# Liest das maximale Mana aus dem lokalen Modell.
#
# Integer — Feldwert ManaMax, kein Prozentsatz und kein Boolean. Null kann ein echter Wert oder
# fehlende Information sein. Nie durch ein Maximum von null teilen. Werte anderer Mobiles können
# unbekannt sein. HP/HitsMax können eine relative Serverskala statt exakter Punkte enthalten.
# HP=0 beweist keinen Tod; dafür Dead/IsDead verwenden.

SUB Main()
    # Das Beispiel nutzt einen Grenzwert oder eine Berechnung für dieses Feld. Zahlen sind
    # Beispieleinstellungen, keine Servergrenzen. Vor einer Division wird geprüft, ob das Maximum
    # positiv ist.

    VAR value = UO.GetMaxMana()
    IF value > 0 THEN
        UO.Print('Mana percent: ' + STR(UO.Mana() * 100 / value))
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Das Beispiel nutzt einen Grenzwert oder eine Berechnung für dieses Feld. Zahlen sind Beispieleinstellungen, keine Servergrenzen. Vor einer Division wird geprüft, ob das Maximum positiv ist.

### Vollständige ReadValue-Hilfsfunktion

```vb
# Vollständige ReadValue-Hilfsfunktion
#
# Liest das maximale Mana aus dem lokalen Modell.
#
# Integer — Feldwert ManaMax, kein Prozentsatz und kein Boolean. Null kann ein echter Wert oder
# fehlende Information sein. Nie durch ein Maximum von null teilen. Werte anderer Mobiles können
# unbekannt sein. HP/HitsMax können eine relative Serverskala statt exakter Punkte enthalten.
# HP=0 beweist keinen Tod; dafür Dead/IsDead verwenden.

SUB Main()
    # lasttarget ist das zuvor ausgewählte Objekt; Exists prüft dessen Vorhandensein. obj ist der
    # einzige ReadValue-Parameter. Die vollständig definierte Funktion liefert die Zahl unverändert.

    IF UO.Exists('lasttarget') THEN
        VAR value = ReadValue('lasttarget')
        UO.Print('Selected value: ' + CStr(value))
    END IF
END SUB

SUB ReadValue(obj)
    RETURN UO.GetMaxMana(obj)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- lasttarget ist das zuvor ausgewählte Objekt; Exists prüft dessen Vorhandensein. obj ist der einzige ReadValue-Parameter. Die vollständig definierte Funktion liefert die Zahl unverändert.
