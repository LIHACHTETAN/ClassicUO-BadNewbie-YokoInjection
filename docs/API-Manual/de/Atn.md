# Atn

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Berechnet den Arkustangens.

## Genaue Syntax

```text
Atn(number:Any) -> Decimal
```

## Parameter

- `number` — Erforderlich: Integer/Decimal oder Dezimaltext mit Punkt und optionalem Exponenten, etwa "-1.25e2". Sprachunabhängig. Ungültiger/hexadezimaler Text, Unit, Array und Object ergeben 0; numerische Hex-Literale sind bereits Integer. NaN/Infinity sind möglich. Eingang Steigung, Ausgang Bogenmaß [-pi/2,pi/2]. Unendlichkeiten geben die Grenzen; NaN bleibt NaN. Kein atan2.

## Rückgabewert

Decimal — atan(number). Eingang Steigung, Ausgang Bogenmaß [-pi/2,pi/2]. Unendlichkeiten geben die Grenzen; NaN bleibt NaN. Kein atan2. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

## Verhalten

- Lokale Berechnung auf dem Skriptthread ohne Server, Bewegung, Zielcursor, Warten oder globale Variablenänderungen.
- Decimal ist binäres Double, nicht .NET decimal. Endliche Näherungswerte mit Toleranz vergleichen. NaN/Infinity nicht als Koordinaten oder Mengen verwenden.
- Eingang Steigung, Ausgang Bogenmaß [-pi/2,pi/2]. Unendlichkeiten geben die Grenzen; NaN bleibt NaN. Kein atan2.

### Interne Funktionen: vom Aufruf zum Ergebnis

Tatsächliche Bindungs- und Umwandlungsschritte. Vollständige Helfer zeigen Skriptformeln, ersetzen aber keine Plattformmathematik.

#### 1. Register

Register bindet den BASIC-Namen an eine native Berechnung mit einem Argument und nach Umwandlung an System.Math. Keine versteckten Skripte oder Serverprozeduren.

Decimal — atan(number). Eingang Steigung, Ausgang Bogenmaß [-pi/2,pi/2]. Unendlichkeiten geben die Grenzen; NaN bleibt NaN. Kein atan2. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; Funktion `Register`.

#### 2. BasicDouble

BasicDouble behält Integer/Decimal, liest Text mit invariantem NumberStyles.Float und liefert sonst 0. Abs behandelt gewöhnliche Integer direkt vor dem Double-Fallback.

Erforderlich: Integer/Decimal oder Dezimaltext mit Punkt und optionalem Exponenten, etwa "-1.25e2". Sprachunabhängig. Ungültiger/hexadezimaler Text, Unit, Array und Object ergeben 0; numerische Hex-Literale sind bereits Integer. NaN/Infinity sind möglich.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; Funktion `BasicDouble`.

Lokale Berechnung auf dem Skriptthread ohne Server, Bewegung, Zielcursor, Warten oder globale Variablenänderungen.


## Beispiele

### Direkte Berechnung

```vb
# Direkte Berechnung
#
# Berechnet den Arkustangens.
#
# Decimal — atan(number). Eingang Steigung, Ausgang Bogenmaß [-pi/2,pi/2]. Unendlichkeiten geben
# die Grenzen; NaN bleibt NaN. Kein atan2. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier
# nicht Erfolg/Fehler.

SUB Main()
    # number = 0; erwartet: 0 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für
    # Print.

    VAR value = Atn(0)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- number = 0; erwartet: 0 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Anderer Wert über eine Variable

```vb
# Anderer Wert über eine Variable
#
# Berechnet den Arkustangens.
#
# Decimal — atan(number). Eingang Steigung, Ausgang Bogenmaß [-pi/2,pi/2]. Unendlichkeiten geben
# die Grenzen; NaN bleibt NaN. Kein atan2. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier
# nicht Erfolg/Fehler.

SUB Main()
    # number = 1; erwartet: ~0.7853981633974483 (~ bedeutet ungefähr). value hält das Ergebnis; CStr
    # formatiert für Print.

    VAR inputValue = 1
    VAR value = Atn(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- number = 1; erwartet: ~0.7853981633974483 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Vollständige Hilfsfunktion

```vb
# Vollständige Hilfsfunktion
#
# Berechnet den Arkustangens.
#
# Decimal — atan(number). Eingang Steigung, Ausgang Bogenmaß [-pi/2,pi/2]. Unendlichkeiten geben
# die Grenzen; NaN bleibt NaN. Kein atan2. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier
# nicht Erfolg/Fehler.

# manual-check: scalar-math Atn
SUB Main()
    # rise/run ist die Steigung. run=0 gibt Ersatzwert 0, keinen senkrechten Winkel.
    # SlopeDegrees(1,1)≈45; unterscheidet nicht alle Quadranten.

    VAR value = SlopeDegrees(1,1)
    UO.Print(CStr(value))
END SUB

SUB SlopeDegrees(rise,run)
    IF run = 0 THEN
        RETURN 0
    END IF
    RETURN Atn(CDbl(rise)/CDbl(run))*180/3.141592653589793
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- rise/run ist die Steigung. run=0 gibt Ersatzwert 0, keinen senkrechten Winkel. SlopeDegrees(1,1)≈45; unterscheidet nicht alle Quadranten.
