# Sqr

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Berechnet die Quadratwurzel.

## Genaue Syntax

```text
Sqr(number:Any) -> Decimal
```

## Parameter

- `number` — Erforderlich: Integer/Decimal oder Dezimaltext mit Punkt und optionalem Exponenten, etwa "-1.25e2". Sprachunabhängig. Ungültiger/hexadezimaler Text, Unit, Array und Object ergeben 0; numerische Hex-Literale sind bereits Integer. NaN/Infinity sind möglich. Eingang >=0: nichtnegative Wurzel. Negativ: NaN; +Infinity: Infinity; NaN unverändert.

## Rückgabewert

Decimal — sqrt(number). Eingang >=0: nichtnegative Wurzel. Negativ: NaN; +Infinity: Infinity; NaN unverändert. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

## Verhalten

- Lokale Berechnung auf dem Skriptthread ohne Server, Bewegung, Zielcursor, Warten oder globale Variablenänderungen.
- Decimal ist binäres Double, nicht .NET decimal. Endliche Näherungswerte mit Toleranz vergleichen. NaN/Infinity nicht als Koordinaten oder Mengen verwenden.
- Eingang >=0: nichtnegative Wurzel. Negativ: NaN; +Infinity: Infinity; NaN unverändert.

### Interne Funktionen: vom Aufruf zum Ergebnis

Tatsächliche Bindungs- und Umwandlungsschritte. Vollständige Helfer zeigen Skriptformeln, ersetzen aber keine Plattformmathematik.

#### 1. Register

Register bindet den BASIC-Namen an eine native Berechnung mit einem Argument und nach Umwandlung an System.Math. Keine versteckten Skripte oder Serverprozeduren.

Decimal — sqrt(number). Eingang >=0: nichtnegative Wurzel. Negativ: NaN; +Infinity: Infinity; NaN unverändert. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

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
# Berechnet die Quadratwurzel.
#
# Decimal — sqrt(number). Eingang >=0: nichtnegative Wurzel. Negativ: NaN; +Infinity: Infinity;
# NaN unverändert. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

SUB Main()
    # number = 25; erwartet: 5 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für
    # Print.

    VAR value = Sqr(25)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- number = 25; erwartet: 5 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Anderer Wert über eine Variable

```vb
# Anderer Wert über eine Variable
#
# Berechnet die Quadratwurzel.
#
# Decimal — sqrt(number). Eingang >=0: nichtnegative Wurzel. Negativ: NaN; +Infinity: Infinity;
# NaN unverändert. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

SUB Main()
    # number = 2; erwartet: ~1.4142135623730951 (~ bedeutet ungefähr). value hält das Ergebnis; CStr
    # formatiert für Print.

    VAR inputValue = 2
    VAR value = Sqr(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- number = 2; erwartet: ~1.4142135623730951 (~ bedeutet ungefähr). value hält das Ergebnis; CStr formatiert für Print.

### Vollständige Hilfsfunktion

```vb
# Vollständige Hilfsfunktion
#
# Berechnet die Quadratwurzel.
#
# Decimal — sqrt(number). Eingang >=0: nichtnegative Wurzel. Negativ: NaN; +Infinity: Infinity;
# NaN unverändert. Zahl, keine ID oder Erfolgsmeldung. 1/0 bedeutet hier nicht Erfolg/Fehler.

# manual-check: scalar-math Sqr
SUB Main()
    # dx/dy sind Koordinatendifferenzen. CDbl verhindert Ganzzahlüberlauf vor sqrt(dx²+dy²).
    # SegmentLength(3,4)=5; euklidische Distanz, keine Route/Kollisionsprüfung.

    VAR value = SegmentLength(3,4)
    UO.Print(CStr(value))
END SUB

SUB SegmentLength(dx,dy)
    VAR x = CDbl(dx)
    VAR y = CDbl(dy)
    RETURN Sqr(x*x+y*y)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- dx/dy sind Koordinatendifferenzen. CDbl verhindert Ganzzahlüberlauf vor sqrt(dx²+dy²). SegmentLength(3,4)=5; euklidische Distanz, keine Route/Kollisionsprüfung.
