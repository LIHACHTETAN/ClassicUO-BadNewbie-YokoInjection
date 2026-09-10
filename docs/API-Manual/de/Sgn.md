# Sgn

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liefert das Vorzeichen.

## Genaue Syntax

```text
Sgn(value:Any) -> Integer
```

## Parameter

- `value` — Erforderlich: Integer/Decimal oder Dezimaltext mit Punkt und optionalem Exponenten, etwa "-1.25e2". Sprachunabhängig. Ungültiger/hexadezimaler Text, Unit, Array und Object ergeben 0; numerische Hex-Literale sind bereits Integer. NaN/Infinity sind möglich. -1 negativ, 0 null, +1 positiv. NaN verursacht einen Mathematikfehler; Unendlichkeiten liefern ihr Vorzeichen.

## Rückgabewert

Integer — sign(value). -1 negativ, 0 null, +1 positiv. NaN verursacht einen Mathematikfehler; Unendlichkeiten liefern ihr Vorzeichen. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

## Verhalten

- Lokale Berechnung auf dem Skriptthread ohne Server, Bewegung, Zielcursor, Warten oder globale Variablenänderungen.
- Decimal ist binäres Double, nicht .NET decimal. Endliche Näherungswerte mit Toleranz vergleichen. NaN/Infinity nicht als Koordinaten oder Mengen verwenden.
- -1 negativ, 0 null, +1 positiv. NaN verursacht einen Mathematikfehler; Unendlichkeiten liefern ihr Vorzeichen.

### Interne Funktionen: vom Aufruf zum Ergebnis

Tatsächliche Bindungs- und Umwandlungsschritte. Vollständige Helfer zeigen Skriptformeln, ersetzen aber keine Plattformmathematik.

#### 1. Register

Register bindet den BASIC-Namen an eine native Berechnung mit einem Argument und nach Umwandlung an System.Math. Keine versteckten Skripte oder Serverprozeduren.

Integer — sign(value). -1 negativ, 0 null, +1 positiv. NaN verursacht einen Mathematikfehler; Unendlichkeiten liefern ihr Vorzeichen. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; Funktion `Register`.

#### 2. BasicDouble

BasicDouble behält Integer/Decimal, liest Text mit invariantem NumberStyles.Float und liefert sonst 0. Abs behandelt gewöhnliche Integer direkt vor dem Double-Fallback.

Erforderlich: Integer/Decimal oder Dezimaltext mit Punkt und optionalem Exponenten, etwa "-1.25e2". Sprachunabhängig. Ungültiger/hexadezimaler Text, Unit, Array und Object ergeben 0; numerische Hex-Literale sind bereits Integer. NaN/Infinity sind möglich.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; Funktion `BasicDouble`.

#### 3. BasicSgn

-1 negativ, 0 null, +1 positiv. NaN verursacht einen Mathematikfehler; Unendlichkeiten liefern ihr Vorzeichen.

Integer — sign(value). -1 negativ, 0 null, +1 positiv. NaN verursacht einen Mathematikfehler; Unendlichkeiten liefern ihr Vorzeichen. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; Funktion `BasicSgn`.

Lokale Berechnung auf dem Skriptthread ohne Server, Bewegung, Zielcursor, Warten oder globale Variablenänderungen.


## Beispiele

### Direkte Berechnung

```vb
# Direkte Berechnung
#
# Liefert das Vorzeichen.
#
# Integer — sign(value). -1 negativ, 0 null, +1 positiv. NaN verursacht einen Mathematikfehler;
# Unendlichkeiten liefern ihr Vorzeichen. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier
# nicht Erfolg/Fehler.

SUB Main()
    # value = -8; erwartet: -1 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für
    # Print.

    VAR value = Sgn(-8)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value = -8; erwartet: -1 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Anderer Wert über eine Variable

```vb
# Anderer Wert über eine Variable
#
# Liefert das Vorzeichen.
#
# Integer — sign(value). -1 negativ, 0 null, +1 positiv. NaN verursacht einen Mathematikfehler;
# Unendlichkeiten liefern ihr Vorzeichen. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier
# nicht Erfolg/Fehler.

SUB Main()
    # value = 10-10; erwartet: 0 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für
    # Print.

    VAR inputValue = 10-10
    VAR value = Sgn(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value = 10-10; erwartet: 0 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Vollständige Hilfsfunktion

```vb
# Vollständige Hilfsfunktion
#
# Liefert das Vorzeichen.
#
# Integer — sign(value). -1 negativ, 0 null, +1 positiv. NaN verursacht einen Mathematikfehler;
# Unendlichkeiten liefern ihr Vorzeichen. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier
# nicht Erfolg/Fehler.

# manual-check: scalar-math Sgn
SUB Main()
    # current/destination liegen auf einer Achse. StepToward liefert -1/0/1, keine Achtwegerichtung
    # und keine Bewegung.

    VAR value = StepToward(12,10)
    UO.Print(CStr(value))
END SUB

SUB StepToward(current,destination)
    RETURN Sgn(CDbl(destination)-CDbl(current))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- current/destination liegen auf einer Achse. StepToward liefert -1/0/1, keine Achtwegerichtung und keine Bewegung.
