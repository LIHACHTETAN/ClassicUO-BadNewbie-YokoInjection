# UO.ApiParameterExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Controlla un valore intrinseco o un selettore oggetto.

## Sintassi esatta

```text
UO.ApiParameterExists(name:String) -> Integer
```

## Parametri

- `name` — String obbligatoria: nome registrato esatto, non espressione di chiamata. Maiuscole e spazi esterni ignorati; UO. non viene aggiunto. Vuoto/sconosciuto: 0. Procedure personali escluse.

## Restituisce

Integer 1 se registrato, altrimenti 0; confrontabile con TRUE/FALSE o 1/0. Non conferma oggetti, azioni o permessi del server.

## Comportamento

- Maiuscole e minuscole sono equivalenti. InjectionApi registra Basic senza prefisso, InjectionApiUO il gioco con UO. Una vecchia chiamata breve produce SC005 e suggerisce UO.; nessuna sostituzione viene eseguita implicitamente. Anche i valori degli attributi richiedono UO. ApiNameExists, ApiSignatureExists e ApiParameterExists eliminano gli spazi esterni e controllano il nome registrato esatto senza aggiungere prefissi. Leggono metadati, non lo stato del server. GetType(TypeName), operatore di riflessione VB.NET, non è implementato.

## Esempi

### UO.ApiParameterExists — 1

```vb
# UO.ApiParameterExists — 1
#
# Controlla un valore intrinseco o un selettore oggetto.
#
# Integer 1 se registrato, altrimenti 0; confrontabile con TRUE/FALSE o 1/0. Non conferma
# oggetti, azioni o permessi del server.

SUB Main()
    # Il primo esempio verifica un nome di gioco UO. esplicito e restituisce 1. Nome e numero di
    # argomenti necessario sono nella chiamata.

    RETURN UO.ApiParameterExists('UO.GetHP')
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Il primo esempio verifica un nome di gioco UO. esplicito e restituisce 1. Nome e numero di argomenti necessario sono nella chiamata.

### UO.ApiParameterExists — 2

```vb
# UO.ApiParameterExists — 2
#
# Controlla un valore intrinseco o un selettore oggetto.
#
# Integer 1 se registrato, altrimenti 0; confrontabile con TRUE/FALSE o 1/0. Non conferma
# oggetti, azioni o permessi del server.

SUB Main()
    # Il secondo verifica Basic o un selettore: Int(value) esiste, Int() no; backpack è un
    # selettore. Risultato 1 o "1:0" secondo le chiamate.

    VAR name = 'backpack'
    RETURN UO.ApiParameterExists(name)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Il secondo verifica Basic o un selettore: Int(value) esiste, Int() no; backpack è un selettore. Risultato 1 o "1:0" secondo le chiamate.

### UO.ApiParameterExists — 3

```vb
# UO.ApiParameterExists — 3
#
# Controlla un valore intrinseco o un selettore oggetto.
#
# Integer 1 se registrato, altrimenti 0; confrontabile con TRUE/FALSE o 1/0. Non conferma
# oggetti, azioni o permessi del server.

SUB Main()
    # Il terzo definisce l’intero helper e confronta una forma breve rimossa o un’arità assente con
    # una forma valida. name, first, second, count passano nomi/numero invariati. Risultato 0 per
    # chiamate, "0:1" per valori.

    RETURN CompareNames('GetHP','UO.GetHP')
END SUB

FUNCTION CompareNames(first,second)
    RETURN CStr(UO.ApiParameterExists(first)) + ":" + CStr(UO.ApiParameterExists(second))
END FUNCTION
```

**Spiegazione dei parametri e dell’esecuzione:**

- Il terzo definisce l’intero helper e confronta una forma breve rimossa o un’arità assente con una forma valida. name, first, second, count passano nomi/numero invariati. Risultato 0 per chiamate, "0:1" per valori.
