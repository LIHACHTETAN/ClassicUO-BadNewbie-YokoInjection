# str

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Str(value) formatta uno scalare Basic come testo.

## Sintassi esatta

```text
str(value:Decimal) -> String
str(value:Integer) -> String
str(value:String) -> String
```

## Parametri

- `value` — Un Integer, Decimal o String obbligatorio. Il tipo effettivo seleziona l’overload. Array, Object e Unit non hanno un overload Str corrispondente.

## Restituisce

String: testo numerico indipendente dalla lingua o String originale invariata. Nessuno spazio iniziale per numeri positivi e nessun parametro di precisione.

## Comportamento

- Calcolo locale senza interrogare il gioco. Omettere l’argomento è un errore. Gli attributi si leggono con UO.Int()/UO.Str(), non Int()/Str(). Int usa BasicDouble e Math.Floor; Str seleziona InternalSubrutines.Str per tipo e formatta indipendentemente dalla lingua.

## Esempi

### Str — 1

```vb
# Str — 1
#
# Str(value) formatta uno scalare Basic come testo.
#
# String: testo numerico indipendente dalla lingua o String originale invariata. Nessuno spazio
# iniziale per numeri positivi e nessun parametro di precisione.

SUB Main()
    # value=42 è Integer. Str produce "42" senza spazio iniziale; Main restituisce quella String.

    RETURN Str(42)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value=42 è Integer. Str produce "42" senza spazio iniziale; Main restituisce quella String.

### Str — 2

```vb
# Str — 2
#
# Str(value) formatta uno scalare Basic come testo.
#
# String: testo numerico indipendente dalla lingua o String originale invariata. Nessuno spazio
# iniziale per numeri positivi e nessun parametro di precisione.

SUB Main()
    # amount=-12.5 è Decimal. Str salva "-12.5" in text con il punto per tutte le lingue. Main
    # restituisce text; amount resta numerico.

    VAR amount = -12.5
    VAR text = Str(amount)
    RETURN text
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- amount=-12.5 è Decimal. Str salva "-12.5" in text con il punto per tutte le lingue. Main restituisce text; amount resta numerico.

### Str — 3

```vb
# Str — 3
#
# Str(value) formatta uno scalare Basic come testo.
#
# String: testo numerico indipendente dalla lingua o String originale invariata. Nessuno spazio
# iniziale per numeri positivi e nessun parametro di precisione.

SUB Main()
    # ItemLabel riceve name="ore", count=3. Str(name) conserva il nome e Str(count) produce "3". La
    # funzione unisce i testi con " x"; Main restituisce "ore x3".

    RETURN ItemLabel("ore",3)
END SUB

SUB ItemLabel(name,count)
    RETURN Str(name) + " x" + Str(count)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- ItemLabel riceve name="ore", count=3. Str(name) conserva il nome e Str(count) produce "3". La funzione unisce i testi con " x"; Main restituisce "ore x3".
