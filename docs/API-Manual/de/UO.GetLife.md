# UO.GetLife

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest die aktuellen Lebenspunkte aus dem lokalen Modell.

## Genaue Syntax

```text
UO.GetLife() -> Integer
```

## Parameter

Keine Parameter.

## Rückgabewert

Integer — Feldwert Hits, kein Prozentsatz und kein Boolean. Null kann ein echter Wert oder fehlende Information sein. Nie durch ein Maximum von null teilen. Werte anderer Mobiles können unbekannt sein. HP/HitsMax können eine relative Serverskala statt exakter Punkte enthalten. HP=0 beweist keinen Tod; dafür Dead/IsDead verwenden.

## Verhalten

- Öffnet keinen status und fordert kein Serverupdate an. Anders als Stealths automatische Anfrage bei fehlenden HP liest dieser Client nur vorhandene Daten. Keine Eigenschaftsänderung oder Paketsendung.
- Jedes Ergebnis ist eine einzelne Abfrage. Zwischen Exists und dem nächsten Aufruf kann sich die Welt ändern; mehrere Abfragen bilden keinen atomaren Schnappschuss.
- Bei Objekten verwirft World.Get fehlende oder IsDestroyed-Einträge und liefert 0. HP/HitsMax lesen Entity-Felder, auch bei Gegenständen mit diesen Feldern; Mana/Stamina erfordern Mobile. Ohne Argument wird self gelesen. Nicht jeder Name ohne Argument hat eine ID-Form: Signaturen prüfen.
- Auch parameterlose Abfragen liefern bei fehlendem/zerstörtem Player 0. Das gilt für direkte Mana/Stamina-Werte und ihre Maxima, nicht nur für World.Get. Ein vorhandener toter Charakter kann weiterhin Werte besitzen.

### Interne Funktionen: vom Aufruf zum Ergebnis

Dies sind die tatsächlichen internen C#-Schritte. ReadValue ist eine vollständig definierte Hilfsfunktion im Beispiel, kein verborgener integrierter Befehl.

#### 1. RegisterCharacterGetterAliases

Beim Erstellen des runtime registriert RegisterCharacterGetterAliases Namen und Formen. Ohne Argument wird bridge.Self gewählt, mit Argument dessen serial. Bestehende Registrierungen bleiben erhalten.

Integer — Feldwert Hits, kein Prozentsatz und kein Boolean. Null kann ein echter Wert oder fehlende Information sein. Nie durch ein Maximum von null teilen. Werte anderer Mobiles können unbekannt sein. HP/HitsMax können eine relative Serverskala statt exakter Punkte enthalten. HP=0 beweist keinen Tod; dafür Dead/IsDead verwenden.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `RegisterCharacterGetterAliases`.

#### 2. Invoke

Invoke liest im Spielthread; ein Arbeitsthread wartet auf die Verarbeitung durch den Manager. Skriptabbruch unterbricht das Warten. Keine zusätzliche Verzögerung oder Netzwerkanfrage.

Jedes Ergebnis ist eine einzelne Abfrage. Zwischen Exists und dem nächsten Aufruf kann sich die Welt ändern; mehrere Abfragen bilden keinen atomaren Schnappschuss.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 3. Get

Bei Objekten verwirft World.Get fehlende oder IsDestroyed-Einträge und liefert 0. HP/HitsMax lesen Entity-Felder, auch bei Gegenständen mit diesen Feldern; Mana/Stamina erfordern Mobile. Ohne Argument wird self gelesen. Nicht jeder Name ohne Argument hat eine ID-Form: Signaturen prüfen.

Integer — Feldwert Hits, kein Prozentsatz und kein Boolean. Null kann ein echter Wert oder fehlende Information sein. Nie durch ein Maximum von null teilen. Werte anderer Mobiles können unbekannt sein. HP/HitsMax können eine relative Serverskala statt exakter Punkte enthalten. HP=0 beweist keinen Tod; dafür Dead/IsDead verwenden.

Projektquelle: `src/ClassicUO.Client/Game/World.cs`; Funktion `Get`.

Öffnet keinen status und fordert kein Serverupdate an. Anders als Stealths automatische Anfrage bei fehlenden HP liest dieser Client nur vorhandene Daten. Keine Eigenschaftsänderung oder Paketsendung.


## Beispiele

### Eigenen Charakterwert anzeigen

```vb
# Eigenen Charakterwert anzeigen
#
# Liest die aktuellen Lebenspunkte aus dem lokalen Modell.
#
# Integer — Feldwert Hits, kein Prozentsatz und kein Boolean. Null kann ein echter Wert oder
# fehlende Information sein. Nie durch ein Maximum von null teilen. Werte anderer Mobiles können
# unbekannt sein. HP/HitsMax können eine relative Serverskala statt exakter Punkte enthalten.
# HP=0 beweist keinen Tod; dafür Dead/IsDead verwenden.

SUB Main()
    # Der Aufruf ohne Argument liest self. value speichert eine Zahl; STR wandelt sie nur für die
    # Meldung um.

    VAR value = UO.GetLife()
    UO.Print('GetLife: ' + STR(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Der Aufruf ohne Argument liest self. value speichert eine Zahl; STR wandelt sie nur für die Meldung um.

### Wert in Bedingung oder Berechnung verwenden

```vb
# Wert in Bedingung oder Berechnung verwenden
#
# Liest die aktuellen Lebenspunkte aus dem lokalen Modell.
#
# Integer — Feldwert Hits, kein Prozentsatz und kein Boolean. Null kann ein echter Wert oder
# fehlende Information sein. Nie durch ein Maximum von null teilen. Werte anderer Mobiles können
# unbekannt sein. HP/HitsMax können eine relative Serverskala statt exakter Punkte enthalten.
# HP=0 beweist keinen Tod; dafür Dead/IsDead verwenden.

SUB Main()
    # Das Beispiel nutzt einen Grenzwert oder eine Berechnung für dieses Feld. Zahlen sind
    # Beispieleinstellungen, keine Servergrenzen. Vor einer Division wird geprüft, ob das Maximum
    # positiv ist.

    VAR value = UO.GetLife()
    VAR maximum = UO.GetMaxHP()
    IF maximum > 0 AND value * 100 / maximum < 50 THEN
        UO.Print('Health below half of the known maximum')
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Das Beispiel nutzt einen Grenzwert oder eine Berechnung für dieses Feld. Zahlen sind Beispieleinstellungen, keine Servergrenzen. Vor einer Division wird geprüft, ob das Maximum positiv ist.

### Vollständige ReadValue-Hilfsfunktion

```vb
# Vollständige ReadValue-Hilfsfunktion
#
# Liest die aktuellen Lebenspunkte aus dem lokalen Modell.
#
# Integer — Feldwert Hits, kein Prozentsatz und kein Boolean. Null kann ein echter Wert oder
# fehlende Information sein. Nie durch ein Maximum von null teilen. Werte anderer Mobiles können
# unbekannt sein. HP/HitsMax können eine relative Serverskala statt exakter Punkte enthalten.
# HP=0 beweist keinen Tod; dafür Dead/IsDead verwenden.

SUB Main()
    # Dieser Name hat keine ID-Form. ReadValue ohne Parameter liest self; WAIT(1000) trennt zwei
    # Aufrufe. Der Vergleich zweier Schnappschüsse kann Zwischenänderungen übersehen.

    VAR before = ReadValue()
    WAIT(1000)
    VAR after = ReadValue()
    UO.Print('Before: ' + CStr(before) + '; after: ' + CStr(after))
END SUB

SUB ReadValue()
    RETURN UO.GetLife()
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Dieser Name hat keine ID-Form. ReadValue ohne Parameter liest self; WAIT(1000) trennt zwei Aufrufe. Der Vergleich zweier Schnappschüsse kann Zwischenänderungen übersehen.
