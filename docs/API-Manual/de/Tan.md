# Tan

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Berechnet den Tangens.

## Genaue Syntax

```text
Tan(radians:Any) -> Decimal
```

## Parameter

- `radians` — Erforderlich: Integer/Decimal oder Dezimaltext mit Punkt und optionalem Exponenten, etwa "-1.25e2". Sprachunabhängig. Ungültiger/hexadezimaler Text, Unit, Array und Object ergeben 0; numerische Hex-Literale sind bereits Integer. NaN/Infinity sind möglich. Bogenmaß. Unbegrenzter, nahe pi/2+k*pi großer instabiler Wert. NaN/Unendlich ergeben NaN.

## Rückgabewert

Decimal — tan(radians). Bogenmaß. Unbegrenzter, nahe pi/2+k*pi großer instabiler Wert. NaN/Unendlich ergeben NaN. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

## Verhalten

- Lokale Berechnung auf dem Skriptthread ohne Server, Bewegung, Zielcursor, Warten oder globale Variablenänderungen.
- Decimal ist binäres Double, nicht .NET decimal. Endliche Näherungswerte mit Toleranz vergleichen. NaN/Infinity nicht als Koordinaten oder Mengen verwenden.
- Bogenmaß. Unbegrenzter, nahe pi/2+k*pi großer instabiler Wert. NaN/Unendlich ergeben NaN.

### Interne Funktionen: vom Aufruf zum Ergebnis

Tatsächliche Bindungs- und Umwandlungsschritte. Vollständige Helfer zeigen Skriptformeln, ersetzen aber keine Plattformmathematik.

#### 1. Register

Register bindet den BASIC-Namen an eine native Berechnung mit einem Argument und nach Umwandlung an System.Math. Keine versteckten Skripte oder Serverprozeduren.

Decimal — tan(radians). Bogenmaß. Unbegrenzter, nahe pi/2+k*pi großer instabiler Wert. NaN/Unendlich ergeben NaN. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

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
# Berechnet den Tangens.
#
# Decimal — tan(radians). Bogenmaß. Unbegrenzter, nahe pi/2+k*pi großer instabiler Wert.
# NaN/Unendlich ergeben NaN. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht
# Erfolg/Fehler.

SUB Main()
    # radians = 0; erwartet: 0 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für
    # Print.

    VAR value = Tan(0)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- radians = 0; erwartet: 0 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Anderer Wert über eine Variable

```vb
# Anderer Wert über eine Variable
#
# Berechnet den Tangens.
#
# Decimal — tan(radians). Bogenmaß. Unbegrenzter, nahe pi/2+k*pi großer instabiler Wert.
# NaN/Unendlich ergeben NaN. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht
# Erfolg/Fehler.

SUB Main()
    # radians = 0.7853981633974483; erwartet: ~1 (~ bedeutet ungefähr). value hält das Ergebnis;
    # CStr formatiert für Print.

    VAR inputValue = 0.7853981633974483
    VAR value = Tan(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- radians = 0.7853981633974483; erwartet: ~1 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Vollständige Hilfsfunktion

```vb
# Vollständige Hilfsfunktion
#
# Berechnet den Tangens.
#
# Decimal — tan(radians). Bogenmaß. Unbegrenzter, nahe pi/2+k*pi großer instabiler Wert.
# NaN/Unendlich ergeben NaN. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht
# Erfolg/Fehler.

# manual-check: scalar-math Tan
SUB Main()
    # degrees in Grad; pi/180 wandelt vor Tan um. TangentDegrees(45)≈1; Singularitäten vermeiden.

    VAR value = TangentDegrees(45)
    UO.Print(CStr(value))
END SUB

SUB TangentDegrees(degrees)
    RETURN Tan(degrees*3.141592653589793/180)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- degrees in Grad; pi/180 wandelt vor Tan um. TangentDegrees(45)≈1; Singularitäten vermeiden.
