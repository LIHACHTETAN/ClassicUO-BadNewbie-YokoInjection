# UO.GetTooltipRec

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge le proprietà strutturate dell’oggetto, inclusi ID cliloc e parametri di sostituzione di ogni voce.

## Sintassi esatta

```text
UO.GetTooltipRec(ObjID:Any) -> Array
```

## Parametri

- `ObjID` — Serial obbligatorio dell’oggetto, non graphic/type né ID cliloc. Intero, stringa decimale/hex, self, backpack, lasttarget, finditem o nome AddObject. 0 non seleziona alcun oggetto.

## Restituisce

Array<Array>: ogni riga contiene [clilocID:Integer, parameters:Array<String>]. rows[i][0] è l’ID del messaggio; rows[i][1] contiene i parametri. GetArrayLength(rows) conta le proprietà. Array vuoto se non sono arrivate voci o ObjID=0. Non sono serial di oggetti.

## Comportamento

- I dati in cache sono restituiti subito. Senza OPL viene inviata una richiesta con attesa massima di 120 ms; annullare la procedura interrompe l’attesa. Una OPL nota e vuota è restituita subito.
- L’array BASIC rappresenta TClilocRec: Count è GetArrayLength(rows), Items sono le righe. Le tabulazioni iniziali di trasporto sono ignorate; i parametri interni vuoti mantengono la posizione. #numero resta una stringa da localizzare. Parametri mancanti: array vuoto. Modificare il risultato non cambia la cache.
- https://stealth.od.ua/api/GetTooltipRec/

## Esempi

### Elencare gli ID delle proprietà

```vb
# Elencare gli ID delle proprietà
#
# Legge le proprietà strutturate dell’oggetto, inclusi ID cliloc e parametri di sostituzione di
# ogni voce.
#
# Array<Array>: ogni riga contiene [clilocID:Integer, parameters:Array<String>]. rows[i][0] è
# l’ID del messaggio; rows[i][1] contiene i parametri. GetArrayLength(rows) conta le proprietà.
# Array vuoto se non sono arrivate voci o ObjID=0. Non sono serial di oggetti.

SUB Main()
    # ObjID=lasttarget seleziona l’oggetto. i parte da 0; row[0] è un ID cliloc. Con un array vuoto
    # il ciclo non viene eseguito.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        UO.Print('Cliloc: ' + STR(row[0]))
        i = i + 1
    WEND
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- ObjID=lasttarget seleziona l’oggetto. i parte da 0; row[0] è un ID cliloc. Con un array vuoto il ciclo non viene eseguito.

### Tradurre ogni proprietà

```vb
# Tradurre ogni proprietà
#
# Legge le proprietà strutturate dell’oggetto, inclusi ID cliloc e parametri di sostituzione di
# ogni voce.
#
# Array<Array>: ogni riga contiene [clilocID:Integer, parameters:Array<String>]. rows[i][0] è
# l’ID del messaggio; rows[i][1] contiene i parametri. GetArrayLength(rows) conta le proprietà.
# Array vuoto se non sono arrivate voci o ObjID=0. Non sono serial di oggetti.

SUB Main()
    # GetClilocByID riceve ClilocID=row[0] e Params=row[1], mantenendo l’ordine. Non passare
    # l’intera riga come Params.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR text = UO.GetClilocByID(row[0], row[1])
        UO.Print(text)
        i = i + 1
    WEND
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- GetClilocByID riceve ClilocID=row[0] e Params=row[1], mantenendo l’ordine. Non passare l’intera riga come Params.

### Leggere un parametro numerico

```vb
# Leggere un parametro numerico
#
# Legge le proprietà strutturate dell’oggetto, inclusi ID cliloc e parametri di sostituzione di
# ogni voce.
#
# Array<Array>: ogni riga contiene [clilocID:Integer, parameters:Array<String>]. rows[i][0] è
# l’ID del messaggio; rows[i][1] contiene i parametri. GetArrayLength(rows) conta le proprietà.
# Array vuoto se non sono arrivate voci o ObjID=0. Non sono serial di oggetti.

SUB Main()
    # wanted=1060401 è un esempio di ID da sostituire. args[0] è una String. Prima di Val verificare
    # lunghezza e IsNumeric: il parametro può essere testo o #cliloc.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR wanted = 1060401
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR args = row[1]
        IF row[0] = wanted AND GetArrayLength(args) > 0 THEN
            IF IsNumeric(args[0]) THEN
                UO.Print('Value: ' + STR(Val(args[0])))
            END IF
        END IF
        i = i + 1
    WEND
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- wanted=1060401 è un esempio di ID da sostituire. args[0] è una String. Prima di Val verificare lunghezza e IsNumeric: il parametro può essere testo o #cliloc.
