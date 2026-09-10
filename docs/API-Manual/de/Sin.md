# Sin

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Berechnet den Sinus.

## Genaue Syntax

```text
Sin(radians:Any) -> Decimal
```

## Parameter

- `radians` — Erforderlich: Integer/Decimal oder Dezimaltext mit Punkt und optionalem Exponenten, etwa "-1.25e2". Sprachunabhängig. Ungültiger/hexadezimaler Text, Unit, Array und Object ergeben 0; numerische Hex-Literale sind bereits Integer. NaN/Infinity sind möglich. Bogenmaß, keine Gradzahl oder Spielrichtung. Endliches Ergebnis in [-1,1]; NaN/Unendlich ergeben NaN.

## Rückgabewert

Decimal — sin(radians). Bogenmaß, keine Gradzahl oder Spielrichtung. Endliches Ergebnis in [-1,1]; NaN/Unendlich ergeben NaN. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

## Verhalten

- Lokale Berechnung auf dem Skriptthread ohne Server, Bewegung, Zielcursor, Warten oder globale Variablenänderungen.
- Decimal ist binäres Double, nicht .NET decimal. Endliche Näherungswerte mit Toleranz vergleichen. NaN/Infinity nicht als Koordinaten oder Mengen verwenden.
- Bogenmaß, keine Gradzahl oder Spielrichtung. Endliches Ergebnis in [-1,1]; NaN/Unendlich ergeben NaN.

### Interne Funktionen: vom Aufruf zum Ergebnis

Tatsächliche Bindungs- und Umwandlungsschritte. Vollständige Helfer zeigen Skriptformeln, ersetzen aber keine Plattformmathematik.

#### 1. Register

Register bindet den BASIC-Namen an eine native Berechnung mit einem Argument und nach Umwandlung an System.Math. Keine versteckten Skripte oder Serverprozeduren.

Decimal — sin(radians). Bogenmaß, keine Gradzahl oder Spielrichtung. Endliches Ergebnis in [-1,1]; NaN/Unendlich ergeben NaN. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

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
# Berechnet den Sinus.
#
# Decimal — sin(radians). Bogenmaß, keine Gradzahl oder Spielrichtung. Endliches Ergebnis in
# [-1,1]; NaN/Unendlich ergeben NaN. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht
# Erfolg/Fehler.

SUB Main()
    # radians = 0; erwartet: 0 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für
    # Print.

    VAR value = Sin(0)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- radians = 0; erwartet: 0 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Anderer Wert über eine Variable

```vb
# Anderer Wert über eine Variable
#
# Berechnet den Sinus.
#
# Decimal — sin(radians). Bogenmaß, keine Gradzahl oder Spielrichtung. Endliches Ergebnis in
# [-1,1]; NaN/Unendlich ergeben NaN. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht
# Erfolg/Fehler.

SUB Main()
    # radians = 1.5707963267948966; erwartet: ~1 (~ bedeutet ungefähr). value hält das Ergebnis;
    # CStr formatiert für Print.

    VAR inputValue = 1.5707963267948966
    VAR value = Sin(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- radians = 1.5707963267948966; erwartet: ~1 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Vollständige Hilfsfunktion

```vb
# Vollständige Hilfsfunktion
#
# Berechnet den Sinus.
#
# Decimal — sin(radians). Bogenmaß, keine Gradzahl oder Spielrichtung. Endliches Ergebnis in
# [-1,1]; NaN/Unendlich ergeben NaN. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht
# Erfolg/Fehler.

# manual-check: scalar-math Sin
SUB Main()
    # degrees in Grad; pi/180 wandelt vor Sin um. SineDegrees(30)≈0.5.

    VAR value = SineDegrees(30)
    UO.Print(CStr(value))
END SUB

SUB SineDegrees(degrees)
    RETURN Sin(degrees*3.141592653589793/180)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- degrees in Grad; pi/180 wandelt vor Sin um. SineDegrees(30)≈0.5.
