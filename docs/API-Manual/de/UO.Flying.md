# UO.Flying

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Prüft, ob ein Mobile fliegt.

## Genaue Syntax

```text
UO.Flying() -> Integer
UO.Flying(id:Any) -> Integer
```

## Parameter

- `id` — Optionales Objekt in den gezeigten Formen: numerischer serial, Hex-Zeichenfolge, self, lasttarget oder registrierter AddObject-Name. Kein type. Ohne Argument wird self gelesen. Unbekannter Text verursacht in manchen Formen einen Konvertierungsfehler; den Namen vorher prüfen.

## Rückgabewert

Integer Boolean: 1 = TRUE, 0 = FALSE. Zahlen oder logische Konstanten ohne Anführungszeichen sind vergleichbar. 1 bedeutet IsFlying beim Mobile; sonst oder ohne Mobile 0. Die Höhe Z allein bedeutet keinen Flug.

Logisches Ergebnis: 1 = TRUE, 0 = FALSE. Nach VAR result = Befehl(...) sind IF result = TRUE THEN und IF result = 1 THEN gleichwertig; entsprechend IF result = FALSE THEN und IF result = 0 THEN. TRUE/FALSE ohne Anführungszeichen. Einmal aufrufen und speichern: Ein weiterer Aufruf kann die Aktion wiederholen oder einen geänderten Zustand lesen.

## Verhalten

- Liest das lokale Modell: kein target, keine status-Anforderung, Flagänderung oder Paketsendung. Ein zerstörtes Objekt gilt schon vor dem Entfernen seines Wörterbucheintrags als fehlend.
- Jedes Ergebnis ist eine einzelne Abfrage. Zwischen Exists und dem nächsten Aufruf kann sich die Welt ändern; mehrere Abfragen bilden keinen atomaren Schnappschuss.
- Poisoned/Flying beachten die Protokollversion: Vor 7.0.0.0 bedeutet Bit 0x04 Gift; ab 7.0.0.0 Flug, während Gift getrennt gespeichert wird. Flug wird nicht aus Z berechnet.

### Interne Funktionen: vom Aufruf zum Ergebnis

Dies sind die tatsächlichen internen C#-Schritte. ReadState ist eine vollständig definierte Hilfsfunktion im Beispiel, kein verborgener integrierter Befehl.

#### 1. RegisterCharacterGetterAliases

Beim Erstellen des runtime registriert RegisterCharacterGetterAliases Namen und Formen. Ohne Argument wird bridge.Self gewählt, mit Argument dessen serial. Bestehende Registrierungen bleiben erhalten.

1 bedeutet IsFlying beim Mobile; sonst oder ohne Mobile 0. Die Höhe Z allein bedeutet keinen Flug.

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

World.Get löst den serial auf und liefert bei IsDestroyed null; danach wird das Mobile-Flag gelesen. Alive prüft Exists und das Fehlen von IsDead; Gegenstände sind erlaubt. Dead für self liest Player.IsDead.

1 bedeutet IsFlying beim Mobile; sonst oder ohne Mobile 0. Die Höhe Z allein bedeutet keinen Flug.

Projektquelle: `src/ClassicUO.Client/Game/World.cs`; Funktion `Get`.

Liest das lokale Modell: kein target, keine status-Anforderung, Flagänderung oder Paketsendung. Ein zerstörtes Objekt gilt schon vor dem Entfernen seines Wörterbucheintrags als fehlend.


## Beispiele

### Eigenen Zustand prüfen

```vb
# Eigenen Zustand prüfen
#
# Prüft, ob ein Mobile fliegt.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE. Zahlen oder logische Konstanten ohne Anführungszeichen
# sind vergleichbar. 1 bedeutet IsFlying beim Mobile; sonst oder ohne Mobile 0. Die Höhe Z
# allein bedeutet keinen Flug.
#
# Logisches Ergebnis: 1 = TRUE, 0 = FALSE. Nach VAR result = Befehl(...) sind IF result = TRUE
# THEN und IF result = 1 THEN gleichwertig; entsprechend IF result = FALSE THEN und IF result =
# 0 THEN. TRUE/FALSE ohne Anführungszeichen. Einmal aufrufen und speichern: Ein weiterer Aufruf
# kann die Aktion wiederholen oder einen geänderten Zustand lesen.

SUB Main()
    # Leere Klammern lesen self. active speichert ein Ergebnis; TRUE und FALSE wählen die Zweige.
    # Print zeigt nur eine Beispielmeldung.

    VAR active = UO.Flying()
    IF active = TRUE THEN
        UO.Print('State is active')
    ELSE
        UO.Print('State is inactive or unavailable')
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Leere Klammern lesen self. active speichert ein Ergebnis; TRUE und FALSE wählen die Zweige. Print zeigt nur eine Beispielmeldung.

### Gewähltes Objekt und vollständige ReadState-Funktion

```vb
# Gewähltes Objekt und vollständige ReadState-Funktion
#
# Prüft, ob ein Mobile fliegt.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE. Zahlen oder logische Konstanten ohne Anführungszeichen
# sind vergleichbar. 1 bedeutet IsFlying beim Mobile; sonst oder ohne Mobile 0. Die Höhe Z
# allein bedeutet keinen Flug.
#
# Logisches Ergebnis: 1 = TRUE, 0 = FALSE. Nach VAR result = Befehl(...) sind IF result = TRUE
# THEN und IF result = 1 THEN gleichwertig; entsprechend IF result = FALSE THEN und IF result =
# 0 THEN. TRUE/FALSE ohne Anführungszeichen. Einmal aufrufen und speichern: Ein weiterer Aufruf
# kann die Aktion wiederholen oder einen geänderten Zustand lesen.

SUB Main()
    # lasttarget ist das zuvor gewählte Objekt. Exists prüft sein Vorhandensein. obj ist der einzige
    # ReadState-Parameter; die Funktion liefert das Befehlsresultat unverändert. Die vollständige
    # Definition wird mitkopiert.

    IF UO.Exists('lasttarget') THEN
        VAR observed = ReadState('lasttarget')
        UO.Print('State 1/0: ' + CStr(observed))
    END IF
END SUB

SUB ReadState(obj)
    RETURN UO.Flying(obj)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- lasttarget ist das zuvor gewählte Objekt. Exists prüft sein Vorhandensein. obj ist der einzige ReadState-Parameter; die Funktion liefert das Befehlsresultat unverändert. Die vollständige Definition wird mitkopiert.

### Änderung innerhalb einer halben Sekunde erkennen

```vb
# Änderung innerhalb einer halben Sekunde erkennen
#
# Prüft, ob ein Mobile fliegt.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE. Zahlen oder logische Konstanten ohne Anführungszeichen
# sind vergleichbar. 1 bedeutet IsFlying beim Mobile; sonst oder ohne Mobile 0. Die Höhe Z
# allein bedeutet keinen Flug.
#
# Logisches Ergebnis: 1 = TRUE, 0 = FALSE. Nach VAR result = Befehl(...) sind IF result = TRUE
# THEN und IF result = 1 THEN gleichwertig; entsprechend IF result = FALSE THEN und IF result =
# 0 THEN. TRUE/FALSE ohne Anführungszeichen. Einmal aufrufen und speichern: Ein weiterer Aufruf
# kann die Aktion wiederholen oder einen geänderten Zustand lesen.

SUB Main()
    # Beide Aufrufe ohne Argument lesen self; WAIT(500) bedeutet 500 Millisekunden. Zwei
    # Schnappschüsse werden verglichen; Zwischenänderungen können unbemerkt bleiben. Keine
    # Endlosschleife.

    VAR before = UO.Flying()
    WAIT(500)
    VAR after = UO.Flying()
    IF before <> after THEN
        UO.Print('State changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Beide Aufrufe ohne Argument lesen self; WAIT(500) bedeutet 500 Millisekunden. Zwei Schnappschüsse werden verglichen; Zwischenänderungen können unbemerkt bleiben. Keine Endlosschleife.
