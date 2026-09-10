# UO.ApiParameterExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Prüft einen intrinsischen Wert oder Objektselektor.

## Genaue Syntax

```text
UO.ApiParameterExists(name:String) -> Integer
```

## Parameter

- `name` — Erforderlicher String: exakter registrierter Name, kein Aufrufausdruck. Großschreibung und äußere Leerzeichen egal; UO. wird nicht ergänzt. Leer/unbekannt ergibt 0. Eigene Prozeduren zählen nicht.

## Rückgabewert

Integer 1 bei vorhandener Registrierung, sonst 0; vergleichbar mit TRUE/FALSE oder 1/0. Keine Bestätigung eines Objekts, Aktionserfolgs oder einer Servererlaubnis.

## Verhalten

- Groß-/Kleinschreibung ist egal. InjectionApi registriert Basic ohne Präfix, InjectionApiUO das Spiel mit UO. Alte Kurzaufrufe erzeugen SC005 mit UO.-Vorschlag; kein stiller Ersatz wird ausgeführt. Attributwerte benötigen ebenfalls UO. ApiNameExists, ApiSignatureExists und ApiParameterExists entfernen äußere Leerzeichen und prüfen den exakten registrierten Namen ohne Präfixergänzung. Sie lesen Metadaten, keinen Serverzustand. Der VB.NET-Reflexionsoperator GetType(TypeName) fehlt.

## Beispiele

### UO.ApiParameterExists — 1

```vb
# UO.ApiParameterExists — 1
#
# Prüft einen intrinsischen Wert oder Objektselektor.
#
# Integer 1 bei vorhandener Registrierung, sonst 0; vergleichbar mit TRUE/FALSE oder 1/0. Keine
# Bestätigung eines Objekts, Aktionserfolgs oder einer Servererlaubnis.

SUB Main()
    # Beispiel 1 prüft einen expliziten UO.-Spielnamen und liefert 1. Name und gegebenenfalls
    # Argumentanzahl stehen im Aufruf.

    RETURN UO.ApiParameterExists('UO.GetHP')
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Beispiel 1 prüft einen expliziten UO.-Spielnamen und liefert 1. Name und gegebenenfalls Argumentanzahl stehen im Aufruf.

### UO.ApiParameterExists — 2

```vb
# UO.ApiParameterExists — 2
#
# Prüft einen intrinsischen Wert oder Objektselektor.
#
# Integer 1 bei vorhandener Registrierung, sonst 0; vergleichbar mit TRUE/FALSE oder 1/0. Keine
# Bestätigung eines Objekts, Aktionserfolgs oder einer Servererlaubnis.

SUB Main()
    # Beispiel 2 prüft Basic oder einen Selektor: Int(value) existiert, Int() nicht; backpack ist
    # ein Selektor. Ergebnis 1 oder "1:0" entsprechend den Aufrufen.

    VAR name = 'backpack'
    RETURN UO.ApiParameterExists(name)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Beispiel 2 prüft Basic oder einen Selektor: Int(value) existiert, Int() nicht; backpack ist ein Selektor. Ergebnis 1 oder "1:0" entsprechend den Aufrufen.

### UO.ApiParameterExists — 3

```vb
# UO.ApiParameterExists — 3
#
# Prüft einen intrinsischen Wert oder Objektselektor.
#
# Integer 1 bei vorhandener Registrierung, sonst 0; vergleichbar mit TRUE/FALSE oder 1/0. Keine
# Bestätigung eines Objekts, Aktionserfolgs oder einer Servererlaubnis.

SUB Main()
    # Beispiel 3 definiert den gesamten Helfer und vergleicht eine entfernte Kurzform oder
    # unbekannte Arity mit einer gültigen Form. name, first, second, count reichen Namen/Anzahl
    # unverändert weiter. Ergebnis 0 für Aufrufe, "0:1" für Werte.

    RETURN CompareNames('GetHP','UO.GetHP')
END SUB

FUNCTION CompareNames(first,second)
    RETURN CStr(UO.ApiParameterExists(first)) + ":" + CStr(UO.ApiParameterExists(second))
END FUNCTION
```

**Erläuterung der Parameter und Ausführung:**

- Beispiel 3 definiert den gesamten Helfer und vergleicht eine entfernte Kurzform oder unbekannte Arity mit einer gültigen Form. name, first, second, count reichen Namen/Anzahl unverändert weiter. Ergebnis 0 für Aufrufe, "0:1" für Werte.
