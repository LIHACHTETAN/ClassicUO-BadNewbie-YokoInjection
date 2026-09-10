# Fix

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Entfernt den Nachkommateil in Richtung null.

## Genaue Syntax

```text
Fix(value:Any) -> Integer
```

## Parameter

- `value` — Erforderlich: Integer/Decimal oder Dezimaltext mit Punkt und optionalem Exponenten, etwa "-1.25e2". Sprachunabhängig. Ungültiger/hexadezimaler Text, Unit, Array und Object ergeben 0; numerische Hex-Literale sind bereits Integer. NaN/Infinity sind möglich. Endlicher Eingang, abgeschnittenes Ergebnis in -2147483648..2147483647. -2.9 wird -2, anders als floor=-3. Außerhalb/NaN/Infinity sind ungültig.

## Rückgabewert

Integer — truncate(value). Endlicher Eingang, abgeschnittenes Ergebnis in -2147483648..2147483647. -2.9 wird -2, anders als floor=-3. Außerhalb/NaN/Infinity sind ungültig. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

## Verhalten

- Lokale Berechnung auf dem Skriptthread ohne Server, Bewegung, Zielcursor, Warten oder globale Variablenänderungen.
- Decimal ist binäres Double, nicht .NET decimal. Endliche Näherungswerte mit Toleranz vergleichen. NaN/Infinity nicht als Koordinaten oder Mengen verwenden.
- Endlicher Eingang, abgeschnittenes Ergebnis in -2147483648..2147483647. -2.9 wird -2, anders als floor=-3. Außerhalb/NaN/Infinity sind ungültig.

### Interne Funktionen: vom Aufruf zum Ergebnis

Tatsächliche Bindungs- und Umwandlungsschritte. Vollständige Helfer zeigen Skriptformeln, ersetzen aber keine Plattformmathematik.

#### 1. Register

Register bindet den BASIC-Namen an eine native Berechnung mit einem Argument und nach Umwandlung an System.Math. Keine versteckten Skripte oder Serverprozeduren.

Integer — truncate(value). Endlicher Eingang, abgeschnittenes Ergebnis in -2147483648..2147483647. -2.9 wird -2, anders als floor=-3. Außerhalb/NaN/Infinity sind ungültig. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

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
# Entfernt den Nachkommateil in Richtung null.
#
# Integer — truncate(value). Endlicher Eingang, abgeschnittenes Ergebnis in
# -2147483648..2147483647. -2.9 wird -2, anders als floor=-3. Außerhalb/NaN/Infinity sind
# ungültig. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

SUB Main()
    # value = 2.9; erwartet: 2 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für
    # Print.

    VAR value = Fix(2.9)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value = 2.9; erwartet: 2 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Anderer Wert über eine Variable

```vb
# Anderer Wert über eine Variable
#
# Entfernt den Nachkommateil in Richtung null.
#
# Integer — truncate(value). Endlicher Eingang, abgeschnittenes Ergebnis in
# -2147483648..2147483647. -2.9 wird -2, anders als floor=-3. Außerhalb/NaN/Infinity sind
# ungültig. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

SUB Main()
    # value = -2.9; erwartet: -2 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für
    # Print.

    VAR inputValue = -2.9
    VAR value = Fix(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- value = -2.9; erwartet: -2 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Vollständige Hilfsfunktion

```vb
# Vollständige Hilfsfunktion
#
# Entfernt den Nachkommateil in Richtung null.
#
# Integer — truncate(value). Endlicher Eingang, abgeschnittenes Ergebnis in
# -2147483648..2147483647. -2.9 wird -2, anders als floor=-3. Außerhalb/NaN/Infinity sind
# ungültig. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

# manual-check: scalar-math Fix
SUB Main()
    # total>=0, size>0: volle Chargen; 27/5 ergibt 5. Ungültig: Ersatzwert 0, auch ohne volle Charge
    # möglich. Quotient muss in Integer passen.

    VAR value = WholeBatches(27,5)
    UO.Print(CStr(value))
END SUB

SUB WholeBatches(total,size)
    IF total < 0 OR size <= 0 THEN
        RETURN 0
    END IF
    RETURN Fix(CDbl(total)/CDbl(size))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- total>=0, size>0: volle Chargen; 27/5 ergibt 5. Ungültig: Ersatzwert 0, auch ohne volle Charge möglich. Quotient muss in Integer passen.
