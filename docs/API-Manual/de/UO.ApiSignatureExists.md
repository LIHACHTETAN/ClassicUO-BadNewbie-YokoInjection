# UO.ApiSignatureExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: de -->

Prüft einen nativen Namen mit einer Argumentanzahl.

## Genaue Syntax

```text
UO.ApiSignatureExists(name:String, argumentCount:Integer) -> Integer
```

## Parameter

- `name` — Erforderlicher String: exakter registrierter Name, kein Aufrufausdruck. Großschreibung und äußere Leerzeichen egal; UO. wird nicht ergänzt. Leer/unbekannt ergibt 0. Eigene Prozeduren zählen nicht.
- `argumentCount` — Erforderlicher Integer: gesamte Anzahl positionsgebundener Argumente einschließlich expliziter optionaler Werte. Negativ/nicht unterstützt ergibt 0. Werttypen werden nicht geprüft.

## Rückgabewert

Integer 1 bei vorhandener Registrierung, sonst 0; vergleichbar mit TRUE/FALSE oder 1/0. Keine Bestätigung eines Objekts, Aktionserfolgs oder einer Servererlaubnis.

## Verhalten

- Groß-/Kleinschreibung ist egal. InjectionApi registriert Basic ohne Präfix, InjectionApiUO das Spiel mit UO. Alte Kurzaufrufe erzeugen SC005 mit UO.-Vorschlag; kein stiller Ersatz wird ausgeführt. Attributwerte benötigen ebenfalls UO. ApiNameExists, ApiSignatureExists und ApiParameterExists entfernen äußere Leerzeichen und prüfen den exakten registrierten Namen ohne Präfixergänzung. Sie lesen Metadaten, keinen Serverzustand. Der VB.NET-Reflexionsoperator GetType(TypeName) fehlt.

## Beispiele

### UO.ApiSignatureExists — 1

```vb
# UO.ApiSignatureExists — 1
#
# Prüft einen nativen Namen mit einer Argumentanzahl.
#
# Integer 1 bei vorhandener Registrierung, sonst 0; vergleichbar mit TRUE/FALSE oder 1/0. Keine
# Bestätigung eines Objekts, Aktionserfolgs oder einer Servererlaubnis.

SUB Main()
    # Beispiel 1 prüft einen expliziten UO.-Spielnamen und liefert 1. Name und gegebenenfalls
    # Argumentanzahl stehen im Aufruf.

    RETURN UO.ApiSignatureExists('UO.GetType',1)
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Beispiel 1 prüft einen expliziten UO.-Spielnamen und liefert 1. Name und gegebenenfalls Argumentanzahl stehen im Aufruf.

### UO.ApiSignatureExists — 2

```vb
# UO.ApiSignatureExists — 2
#
# Prüft einen nativen Namen mit einer Argumentanzahl.
#
# Integer 1 bei vorhandener Registrierung, sonst 0; vergleichbar mit TRUE/FALSE oder 1/0. Keine
# Bestätigung eines Objekts, Aktionserfolgs oder einer Servererlaubnis.

SUB Main()
    # Beispiel 2 prüft Basic oder einen Selektor: Int(value) existiert, Int() nicht; backpack ist
    # ein Selektor. Ergebnis 1 oder "1:0" entsprechend den Aufrufen.

    RETURN CStr(UO.ApiSignatureExists('Int',1)) + ':' + CStr(UO.ApiSignatureExists('Int',0))
END SUB
```

**Erläuterung der Parameter und Ausführung:**

- Beispiel 2 prüft Basic oder einen Selektor: Int(value) existiert, Int() nicht; backpack ist ein Selektor. Ergebnis 1 oder "1:0" entsprechend den Aufrufen.

### UO.ApiSignatureExists — 3

```vb
# UO.ApiSignatureExists — 3
#
# Prüft einen nativen Namen mit einer Argumentanzahl.
#
# Integer 1 bei vorhandener Registrierung, sonst 0; vergleichbar mit TRUE/FALSE oder 1/0. Keine
# Bestätigung eines Objekts, Aktionserfolgs oder einer Servererlaubnis.

SUB Main()
    # Beispiel 3 definiert den gesamten Helfer und vergleicht eine entfernte Kurzform oder
    # unbekannte Arity mit einer gültigen Form. name, first, second, count reichen Namen/Anzahl
    # unverändert weiter. Ergebnis 0 für Aufrufe, "0:1" für Werte.

    RETURN CheckForm('UO.GetType',0)
END SUB

FUNCTION CheckForm(name,count)
    RETURN UO.ApiSignatureExists(name,count)
END FUNCTION
```

**Erläuterung der Parameter und Ausführung:**

- Beispiel 3 definiert den gesamten Helfer und vergleicht eine entfernte Kurzform oder unbekannte Arity mit einer gültigen Form. name, first, second, count reichen Namen/Anzahl unverändert weiter. Ergebnis 0 für Aufrufe, "0:1" für Werte.
