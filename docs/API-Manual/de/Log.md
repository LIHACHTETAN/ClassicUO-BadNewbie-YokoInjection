# Log

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Berechnet den natürlichen Logarithmus.

## Genaue Syntax

```text
Log(number:Any) -> Decimal
```

## Parameter

- `number` — Erforderlich: Integer/Decimal oder Dezimaltext mit Punkt und optionalem Exponenten, etwa "-1.25e2". Sprachunabhängig. Ungültiger/hexadezimaler Text, Unit, Array und Object ergeben 0; numerische Hex-Literale sind bereits Integer. NaN/Infinity sind möglich. Basis e, nicht 10. Log(1)=0, Log(0)=-Infinity; negativ: NaN; +Infinity: Infinity.

## Rückgabewert

Decimal — ln(number). Basis e, nicht 10. Log(1)=0, Log(0)=-Infinity; negativ: NaN; +Infinity: Infinity. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

## Verhalten

- Lokale Berechnung auf dem Skriptthread ohne Server, Bewegung, Zielcursor, Warten oder globale Variablenänderungen.
- Decimal ist binäres Double, nicht .NET decimal. Endliche Näherungswerte mit Toleranz vergleichen. NaN/Infinity nicht als Koordinaten oder Mengen verwenden.
- Basis e, nicht 10. Log(1)=0, Log(0)=-Infinity; negativ: NaN; +Infinity: Infinity.

### Interne Funktionen: vom Aufruf zum Ergebnis

Tatsächliche Bindungs- und Umwandlungsschritte. Vollständige Helfer zeigen Skriptformeln, ersetzen aber keine Plattformmathematik.

#### 1. Register

Register bindet den BASIC-Namen an eine native Berechnung mit einem Argument und nach Umwandlung an System.Math. Keine versteckten Skripte oder Serverprozeduren.

Decimal — ln(number). Basis e, nicht 10. Log(1)=0, Log(0)=-Infinity; negativ: NaN; +Infinity: Infinity. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

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
# Berechnet den natürlichen Logarithmus.
#
# Decimal — ln(number). Basis e, nicht 10. Log(1)=0, Log(0)=-Infinity; negativ: NaN; +Infinity:
# Infinity. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

SUB Main()
    # number = 1; erwartet: 0 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für
    # Print.

    VAR value = Log(1)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- number = 1; erwartet: 0 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Anderer Wert über eine Variable

```vb
# Anderer Wert über eine Variable
#
# Berechnet den natürlichen Logarithmus.
#
# Decimal — ln(number). Basis e, nicht 10. Log(1)=0, Log(0)=-Infinity; negativ: NaN; +Infinity:
# Infinity. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

SUB Main()
    # number = 2.718281828459045; erwartet: ~1 (~ bedeutet ungefähr). value hält das Ergebnis; CStr
    # formatiert für Print.

    VAR inputValue = 2.718281828459045
    VAR value = Log(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- number = 2.718281828459045; erwartet: ~1 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Vollständige Hilfsfunktion

```vb
# Vollständige Hilfsfunktion
#
# Berechnet den natürlichen Logarithmus.
#
# Decimal — ln(number). Basis e, nicht 10. Log(1)=0, Log(0)=-Infinity; negativ: NaN; +Infinity:
# Infinity. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

# manual-check: scalar-math Log
SUB Main()
    # value>0, baseValue>0 und <>1. Log(value)/Log(baseValue); LogBase(100,10)≈2. Ungültig:
    # Ersatzwert 0, zugleich ein möglicher gültiger Logarithmus.

    VAR value = LogBase(100,10)
    UO.Print(CStr(value))
END SUB

SUB LogBase(value,baseValue)
    IF value <= 0 OR baseValue <= 0 OR baseValue = 1 THEN
        RETURN 0
    END IF
    RETURN Log(value)/Log(baseValue)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value>0, baseValue>0 und <>1. Log(value)/Log(baseValue); LogBase(100,10)≈2. Ungültig: Ersatzwert 0, zugleich ein möglicher gültiger Logarithmus.
