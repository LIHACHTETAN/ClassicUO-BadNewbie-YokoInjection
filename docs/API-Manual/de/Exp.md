# Exp

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Potenziert e.

## Genaue Syntax

```text
Exp(power:Any) -> Decimal
```

## Parameter

- `power` — Erforderlich: Integer/Decimal oder Dezimaltext mit Punkt und optionalem Exponenten, etwa "-1.25e2". Sprachunabhängig. Ungültiger/hexadezimaler Text, Unit, Array und Object ergeben 0; numerische Hex-Literale sind bereits Integer. NaN/Infinity sind möglich. Exp(0)=1. Sehr positiv: Infinity; sehr negativ: Unterlauf zu 0. NaN unverändert.

## Rückgabewert

Decimal — e^power. Exp(0)=1. Sehr positiv: Infinity; sehr negativ: Unterlauf zu 0. NaN unverändert. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

## Verhalten

- Lokale Berechnung auf dem Skriptthread ohne Server, Bewegung, Zielcursor, Warten oder globale Variablenänderungen.
- Decimal ist binäres Double, nicht .NET decimal. Endliche Näherungswerte mit Toleranz vergleichen. NaN/Infinity nicht als Koordinaten oder Mengen verwenden.
- Exp(0)=1. Sehr positiv: Infinity; sehr negativ: Unterlauf zu 0. NaN unverändert.

### Interne Funktionen: vom Aufruf zum Ergebnis

Tatsächliche Bindungs- und Umwandlungsschritte. Vollständige Helfer zeigen Skriptformeln, ersetzen aber keine Plattformmathematik.

#### 1. Register

Register bindet den BASIC-Namen an eine native Berechnung mit einem Argument und nach Umwandlung an System.Math. Keine versteckten Skripte oder Serverprozeduren.

Decimal — e^power. Exp(0)=1. Sehr positiv: Infinity; sehr negativ: Unterlauf zu 0. NaN unverändert. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

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
# Potenziert e.
#
# Decimal — e^power. Exp(0)=1. Sehr positiv: Infinity; sehr negativ: Unterlauf zu 0. NaN
# unverändert. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

SUB Main()
    # power = 0; erwartet: 1 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für
    # Print.

    VAR value = Exp(0)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- power = 0; erwartet: 1 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Anderer Wert über eine Variable

```vb
# Anderer Wert über eine Variable
#
# Potenziert e.
#
# Decimal — e^power. Exp(0)=1. Sehr positiv: Infinity; sehr negativ: Unterlauf zu 0. NaN
# unverändert. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

SUB Main()
    # power = 1; erwartet: ~2.718281828459045 (~ bedeutet ungefähr). value hält das Ergebnis; CStr
    # formatiert für Print.

    VAR inputValue = 1
    VAR value = Exp(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- power = 1; erwartet: ~2.718281828459045 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Vollständige Hilfsfunktion

```vb
# Vollständige Hilfsfunktion
#
# Potenziert e.
#
# Decimal — e^power. Exp(0)=1. Sehr positiv: Infinity; sehr negativ: Unterlauf zu 0. NaN
# unverändert. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

# manual-check: scalar-math Exp
SUB Main()
    # value ist der Anfang, rate die stetige Rate je Zeiteinheit, period deren Anzahl.
    # Growth(100,0.05,2)≈110.517; Zahlenbeispiel.

    VAR value = Growth(100,0.05,2)
    UO.Print(CStr(value))
END SUB

SUB Growth(value,rate,period)
    RETURN value*Exp(rate*period)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value ist der Anfang, rate die stetige Rate je Zeiteinheit, period deren Anzahl. Growth(100,0.05,2)≈110.517; Zahlenbeispiel.
