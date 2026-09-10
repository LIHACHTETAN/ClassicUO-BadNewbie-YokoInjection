# Abs

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Liefert den Absolutbetrag.

## Genaue Syntax

```text
Abs(value:Any) -> Any
```

## Parameter

- `value` — Erforderlich: Integer/Decimal oder Dezimaltext mit Punkt und optionalem Exponenten, etwa "-1.25e2". Sprachunabhängig. Ungültiger/hexadezimaler Text, Unit, Array und Object ergeben 0; numerische Hex-Literale sind bereits Integer. NaN/Infinity sind möglich. Integer bleibt Integer, außer -2147483648: Decimal 2147483648. Decimal/Text ergeben Decimal. NaN bleibt NaN; beide Unendlichkeiten ergeben +Infinity.

## Rückgabewert

Integer/Decimal — abs(value). Integer bleibt Integer, außer -2147483648: Decimal 2147483648. Decimal/Text ergeben Decimal. NaN bleibt NaN; beide Unendlichkeiten ergeben +Infinity. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

## Verhalten

- Lokale Berechnung auf dem Skriptthread ohne Server, Bewegung, Zielcursor, Warten oder globale Variablenänderungen.
- Decimal ist binäres Double, nicht .NET decimal. Endliche Näherungswerte mit Toleranz vergleichen. NaN/Infinity nicht als Koordinaten oder Mengen verwenden.
- Integer bleibt Integer, außer -2147483648: Decimal 2147483648. Decimal/Text ergeben Decimal. NaN bleibt NaN; beide Unendlichkeiten ergeben +Infinity.

### Interne Funktionen: vom Aufruf zum Ergebnis

Tatsächliche Bindungs- und Umwandlungsschritte. Vollständige Helfer zeigen Skriptformeln, ersetzen aber keine Plattformmathematik.

#### 1. Register

Register bindet den BASIC-Namen an eine native Berechnung mit einem Argument und nach Umwandlung an System.Math. Keine versteckten Skripte oder Serverprozeduren.

Integer/Decimal — abs(value). Integer bleibt Integer, außer -2147483648: Decimal 2147483648. Decimal/Text ergeben Decimal. NaN bleibt NaN; beide Unendlichkeiten ergeben +Infinity. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; Funktion `Register`.

#### 2. BasicDouble

BasicDouble behält Integer/Decimal, liest Text mit invariantem NumberStyles.Float und liefert sonst 0. Abs behandelt gewöhnliche Integer direkt vor dem Double-Fallback.

Erforderlich: Integer/Decimal oder Dezimaltext mit Punkt und optionalem Exponenten, etwa "-1.25e2". Sprachunabhängig. Ungültiger/hexadezimaler Text, Unit, Array und Object ergeben 0; numerische Hex-Literale sind bereits Integer. NaN/Infinity sind möglich.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; Funktion `BasicDouble`.

#### 3. BasicAbs

Integer bleibt Integer, außer -2147483648: Decimal 2147483648. Decimal/Text ergeben Decimal. NaN bleibt NaN; beide Unendlichkeiten ergeben +Infinity.

Integer/Decimal — abs(value). Integer bleibt Integer, außer -2147483648: Decimal 2147483648. Decimal/Text ergeben Decimal. NaN bleibt NaN; beide Unendlichkeiten ergeben +Infinity. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

Projektquelle: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; Funktion `BasicAbs`.

Lokale Berechnung auf dem Skriptthread ohne Server, Bewegung, Zielcursor, Warten oder globale Variablenänderungen.


## Beispiele

### Direkte Berechnung

```vb
# Direkte Berechnung
#
# Liefert den Absolutbetrag.
#
# Integer/Decimal — abs(value). Integer bleibt Integer, außer -2147483648: Decimal 2147483648.
# Decimal/Text ergeben Decimal. NaN bleibt NaN; beide Unendlichkeiten ergeben +Infinity. Zahl,
# keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

SUB Main()
    # value = -12; erwartet: 12 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für
    # Print.

    VAR value = Abs(-12)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value = -12; erwartet: 12 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Anderer Wert über eine Variable

```vb
# Anderer Wert über eine Variable
#
# Liefert den Absolutbetrag.
#
# Integer/Decimal — abs(value). Integer bleibt Integer, außer -2147483648: Decimal 2147483648.
# Decimal/Text ergeben Decimal. NaN bleibt NaN; beide Unendlichkeiten ergeben +Infinity. Zahl,
# keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

SUB Main()
    # value = '-2.5'; erwartet: 2.5 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert
    # für Print.

    VAR inputValue = '-2.5'
    VAR value = Abs(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value = '-2.5'; erwartet: 2.5 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Vollständige Hilfsfunktion

```vb
# Vollständige Hilfsfunktion
#
# Liefert den Absolutbetrag.
#
# Integer/Decimal — abs(value). Integer bleibt Integer, außer -2147483648: Decimal 2147483648.
# Decimal/Text ergeben Decimal. NaN bleibt NaN; beide Unendlichkeiten ergeben +Infinity. Zahl,
# keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

# manual-check: scalar-math Abs
SUB Main()
    # value/target sind Zahlen; tolerance ist erlaubter Abstand >=0. IsWithin liefert Boolean 1/0;
    # negative Toleranz ergibt 0.

    VAR value = IsWithin(12,10,2)
    UO.Print(CStr(value))
END SUB

SUB IsWithin(value,target,tolerance)
    IF tolerance < 0 THEN
        RETURN 0
    END IF
    RETURN Abs(CDbl(value)-CDbl(target)) <= tolerance
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value/target sind Zahlen; tolerance ist erlaubter Abstand >=0. IsWithin liefert Boolean 1/0; negative Toleranz ergibt 0.
