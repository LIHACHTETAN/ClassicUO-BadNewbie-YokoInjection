# UO.LastTarget

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liest die Serial des zuletzt gespeicherten Objektziels.

## Genaue Syntax

```text
UO.LastTarget() -> Integer
```

## Parameter

Keine Parameter.

## Rückgabewert

Integer — Serial/ID, kein Type oder Boolean. 0: kein Objektziel; Boden/Statik haben ebenfalls Serial 0 trotz gespeicherter Koordinaten. Alle 32 Bits bleiben erhalten. Auf <> 0 prüfen, nicht > 0 oder = TRUE.

## Verhalten

- Keine Parameter, Zielauswahl, Cursoröffnung, Angriffe oder Pakete. LastTarget ist nicht LastAttack oder LastStatus. Gewöhnliche self-Auswahl ersetzt das Ziel nicht; explizites ClientMarkChar kann es ändern.
- SetEntity speichert bekannte Entity.X/Y, bei Behälterinhalten eventuell interne Koordinaten. SetLand/SetStatic speichern Weltzellen. Spätere Bewegung/Entfernung ändert nichts. GetX/GetY(serial) liefern die aktuelle Position.
- Clear und World.Clear setzen auch bei erhaltenen Skripten zurück. Eine explizit zugewiesene unbekannte Serial erhält X/Y=0 statt alter Koordinaten. Dies garantiert keine Existenz auf dem Server.
- Getrennte Lesezugriffe sind nicht atomar. LastTile behält bei Objektzielen die Protokollkoordinaten 65535; bei Boden/Statik lesen LastTile(1)/(2) X/Y. lasttarget ohne Klammern ist dynamisch, sofern keine Variable es verdeckt.
- World.Clear ruft ClearWorldState auf: aktiver Cursor/Callback, Ziel und Wiederholungspaket werden gelöscht. Ein normales Reset behält die Historie. Natives TargetLast sendet nur bei aktivem Servercursor ein gespeichertes Paket; ohne Historie oder bei lokalem Callback bleiben Cursor und Netzwerk unverändert. Ein aktiver Client-Callback erhält einmal null als Abbruch: ClientTargetResponsePresent wird 1 bei leerer Antwort. Eine abgeschlossene Auswahl wird nicht erneut benachrichtigt.

### Interne Funktionen: vom Aufruf zum Ergebnis

Dies sind die tatsächlichen internen C#-Schritte. ReadTargetValue ist eine vollständig definierte Hilfsfunktion im Beispiel, kein verborgener integrierter Befehl.

#### 1. SetEntity

SetEntity speichert Serial und X/Y über World.Get. Fehlende/zerstörte Entity ergibt X/Y=0; Protokollsentinels bleiben erhalten.

SetEntity speichert bekannte Entity.X/Y, bei Behälterinhalten eventuell interne Koordinaten. SetLand/SetStatic speichern Weltzellen. Spätere Bewegung/Entfernung ändert nichts. GetX/GetY(serial) liefern die aktuelle Position.

Projektquelle: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; Funktion `SetEntity`.

#### 2. SetLand

SetLand/SetStatic speichern X/Y/Z mit Serial 0. SavedX/SavedY sind von gesendeten Feldern getrennt.

Integer — Serial/ID, kein Type oder Boolean. 0: kein Objektziel; Boden/Statik haben ebenfalls Serial 0 trotz gespeicherter Koordinaten. Alle 32 Bits bleiben erhalten. Auf <> 0 prüfen, nicht > 0 oder = TRUE.

Projektquelle: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; Funktion `SetLand`.

#### 3. SetStatic

SetLand/SetStatic speichern X/Y/Z mit Serial 0. SavedX/SavedY sind von gesendeten Feldern getrennt.

Integer — Serial/ID, kein Type oder Boolean. 0: kein Objektziel; Boden/Statik haben ebenfalls Serial 0 trotz gespeicherter Koordinaten. Alle 32 Bits bleiben erhalten. Auf <> 0 prüfen, nicht > 0 oder = TRUE.

Projektquelle: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; Funktion `SetStatic`.

#### 4. ExecuteStealthCompatibility

LastTargetX/LastTargetY lesen ITargetSnapshotBridge; ältere externe Bridges behalten GetX/GetY. Invoke liest mit Abbruchunterstützung auf dem Spielthread.

Integer — Serial/ID, kein Type oder Boolean. 0: kein Objektziel; Boden/Statik haben ebenfalls Serial 0 trotz gespeicherter Koordinaten. Alle 32 Bits bleiben erhalten. Auf <> 0 prüfen, nicht > 0 oder = TRUE.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; Funktion `ExecuteStealthCompatibility`.

#### 5. Invoke

LastTargetX/LastTargetY lesen ITargetSnapshotBridge; ältere externe Bridges behalten GetX/GetY. Invoke liest mit Abbruchunterstützung auf dem Spielthread.

Keine Parameter, Zielauswahl, Cursoröffnung, Angriffe oder Pakete. LastTarget ist nicht LastAttack oder LastStatus. Gewöhnliche self-Auswahl ersetzt das Ziel nicht; explizites ClientMarkChar kann es ändern.

Projektquelle: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; Funktion `Invoke`.

#### 6. Clear

Clear löscht Serial und gespeicherte Koordinaten; World.Clear ruft es beim Bereinigen auf.

Clear und World.Clear setzen auch bei erhaltenen Skripten zurück. Eine explizit zugewiesene unbekannte Serial erhält X/Y=0 statt alter Koordinaten. Dies garantiert keine Existenz auf dem Server.

Projektquelle: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; Funktion `Clear`.

#### 7. ClearWorldState

World.Clear ruft ClearWorldState auf: aktiver Cursor/Callback, Ziel und Wiederholungspaket werden gelöscht. Ein normales Reset behält die Historie. Natives TargetLast sendet nur bei aktivem Servercursor ein gespeichertes Paket; ohne Historie oder bei lokalem Callback bleiben Cursor und Netzwerk unverändert. Ein aktiver Client-Callback erhält einmal null als Abbruch: ClientTargetResponsePresent wird 1 bei leerer Antwort. Eine abgeschlossene Auswahl wird nicht erneut benachrichtigt.

World.Clear ruft ClearWorldState auf: aktiver Cursor/Callback, Ziel und Wiederholungspaket werden gelöscht. Ein normales Reset behält die Historie. Natives TargetLast sendet nur bei aktivem Servercursor ein gespeichertes Paket; ohne Historie oder bei lokalem Callback bleiben Cursor und Netzwerk unverändert. Ein aktiver Client-Callback erhält einmal null als Abbruch: ClientTargetResponsePresent wird 1 bei leerer Antwort. Eine abgeschlossene Auswahl wird nicht erneut benachrichtigt.

Projektquelle: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; Funktion `ClearWorldState`.

#### 8. TargetLast

World.Clear ruft ClearWorldState auf: aktiver Cursor/Callback, Ziel und Wiederholungspaket werden gelöscht. Ein normales Reset behält die Historie. Natives TargetLast sendet nur bei aktivem Servercursor ein gespeichertes Paket; ohne Historie oder bei lokalem Callback bleiben Cursor und Netzwerk unverändert. Ein aktiver Client-Callback erhält einmal null als Abbruch: ClientTargetResponsePresent wird 1 bei leerer Antwort. Eine abgeschlossene Auswahl wird nicht erneut benachrichtigt.

World.Clear ruft ClearWorldState auf: aktiver Cursor/Callback, Ziel und Wiederholungspaket werden gelöscht. Ein normales Reset behält die Historie. Natives TargetLast sendet nur bei aktivem Servercursor ein gespeichertes Paket; ohne Historie oder bei lokalem Callback bleiben Cursor und Netzwerk unverändert. Ein aktiver Client-Callback erhält einmal null als Abbruch: ClientTargetResponsePresent wird 1 bei leerer Antwort. Eine abgeschlossene Auswahl wird nicht erneut benachrichtigt.

Projektquelle: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; Funktion `TargetLast`.

Getrennte Lesezugriffe sind nicht atomar. LastTile behält bei Objektzielen die Protokollkoordinaten 65535; bei Boden/Statik lesen LastTile(1)/(2) X/Y. lasttarget ohne Klammern ist dynamisch, sofern keine Variable es verdeckt.


## Beispiele

### Gespeicherten Wert lesen

```vb
# Gespeicherten Wert lesen
#
# Liest die Serial des zuletzt gespeicherten Objektziels.
#
# Integer — Serial/ID, kein Type oder Boolean. 0: kein Objektziel; Boden/Statik haben ebenfalls
# Serial 0 trotz gespeicherter Koordinaten. Alle 32 Bits bleiben erhalten. Auf <> 0 prüfen,
# nicht > 0 oder = TRUE.

SUB Main()
    # value enthält das Ergebnis; HEX zeigt die ID, CStr die Koordinate. Keine Auswahl.

    VAR value = UO.LastTarget()
    UO.Print('Saved value: ' + HEX(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value enthält das Ergebnis; HEX zeigt die ID, CStr die Koordinate. Keine Auswahl.

### Gespeicherte und aktuelle Position vergleichen

```vb
# Gespeicherte und aktuelle Position vergleichen
#
# Liest die Serial des zuletzt gespeicherten Objektziels.
#
# Integer — Serial/ID, kein Type oder Boolean. 0: kein Objektziel; Boden/Statik haben ebenfalls
# Serial 0 trotz gespeicherter Koordinaten. Alle 32 Bits bleiben erhalten. Auf <> 0 prüfen,
# nicht > 0 oder = TRUE.

SUB Main()
    # id ist die gespeicherte Serial. Exists prüft vor GetX/GetY; die Positionen können abweichen.
    # Eine Null-ID beweist keine Punktauswahl.

    VAR id = UO.LastTarget()
    VAR x = UO.LastTargetX()
    VAR y = UO.LastTargetY()
    UO.Print('Saved XY: ' + CStr(x) + ',' + CStr(y))
    IF id <> 0 AND UO.Exists(id) THEN
        UO.Print('Live XY: ' + CStr(UO.GetX(id)) + ',' + CStr(UO.GetY(id)))
    END IF
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- id ist die gespeicherte Serial. Exists prüft vor GetX/GetY; die Positionen können abweichen. Eine Null-ID beweist keine Punktauswahl.

### Vollständige Hilfsfunktion ReadTargetValue

```vb
# Vollständige Hilfsfunktion ReadTargetValue
#
# Liest die Serial des zuletzt gespeicherten Objektziels.
#
# Integer — Serial/ID, kein Type oder Boolean. 0: kein Objektziel; Boden/Statik haben ebenfalls
# Serial 0 trotz gespeicherter Koordinaten. Alle 32 Bits bleiben erhalten. Auf <> 0 prüfen,
# nicht > 0 oder = TRUE.

SUB Main()
    # minimum/maximum konfigurieren den Helferfilter, nicht die API. -1 ist dessen eigenes
    # Bereichssignal. Die ID-Variante behält jede nichtleere Serial samt höchstem Bit.

    VAR value = ReadTargetValue()
    UO.Print('Checked value: ' + CStr(value))
END SUB

SUB ReadTargetValue()
    VAR value = UO.LastTarget()
    IF value = 0 THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- minimum/maximum konfigurieren den Helferfilter, nicht die API. -1 ist dessen eigenes Bereichssignal. Die ID-Variante behält jede nichtleere Serial samt höchstem Bit.
