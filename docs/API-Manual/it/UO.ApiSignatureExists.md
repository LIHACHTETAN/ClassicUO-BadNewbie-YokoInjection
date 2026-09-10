# UO.ApiSignatureExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Controlla un nome nativo e il numero di argomenti.

## Sintassi esatta

```text
UO.ApiSignatureExists(name:String, argumentCount:Integer) -> Integer
```

## Parametri

- `name` — String obbligatoria: nome registrato esatto, non espressione di chiamata. Maiuscole e spazi esterni ignorati; UO. non viene aggiunto. Vuoto/sconosciuto: 0. Procedure personali escluse.
- `argumentCount` — Integer obbligatorio: totale degli argomenti posizionali, compresi gli opzionali espliciti. Quantità negativa/non supportata: 0. I tipi non vengono verificati.

## Restituisce

Integer 1 se registrato, altrimenti 0; confrontabile con TRUE/FALSE o 1/0. Non conferma oggetti, azioni o permessi del server.

## Comportamento

- Maiuscole e minuscole sono equivalenti. InjectionApi registra Basic senza prefisso, InjectionApiUO il gioco con UO. Una vecchia chiamata breve produce SC005 e suggerisce UO.; nessuna sostituzione viene eseguita implicitamente. Anche i valori degli attributi richiedono UO. ApiNameExists, ApiSignatureExists e ApiParameterExists eliminano gli spazi esterni e controllano il nome registrato esatto senza aggiungere prefissi. Leggono metadati, non lo stato del server. GetType(TypeName), operatore di riflessione VB.NET, non è implementato.

## Esempi

### UO.ApiSignatureExists — 1

```vb
# UO.ApiSignatureExists — 1
#
# Controlla un nome nativo e il numero di argomenti.
#
# Integer 1 se registrato, altrimenti 0; confrontabile con TRUE/FALSE o 1/0. Non conferma
# oggetti, azioni o permessi del server.

SUB Main()
    # Il primo esempio verifica un nome di gioco UO. esplicito e restituisce 1. Nome e numero di
    # argomenti necessario sono nella chiamata.

    RETURN UO.ApiSignatureExists('UO.GetType',1)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Il primo esempio verifica un nome di gioco UO. esplicito e restituisce 1. Nome e numero di argomenti necessario sono nella chiamata.

### UO.ApiSignatureExists — 2

```vb
# UO.ApiSignatureExists — 2
#
# Controlla un nome nativo e il numero di argomenti.
#
# Integer 1 se registrato, altrimenti 0; confrontabile con TRUE/FALSE o 1/0. Non conferma
# oggetti, azioni o permessi del server.

SUB Main()
    # Il secondo verifica Basic o un selettore: Int(value) esiste, Int() no; backpack è un
    # selettore. Risultato 1 o "1:0" secondo le chiamate.

    RETURN CStr(UO.ApiSignatureExists('Int',1)) + ':' + CStr(UO.ApiSignatureExists('Int',0))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Il secondo verifica Basic o un selettore: Int(value) esiste, Int() no; backpack è un selettore. Risultato 1 o "1:0" secondo le chiamate.

### UO.ApiSignatureExists — 3

```vb
# UO.ApiSignatureExists — 3
#
# Controlla un nome nativo e il numero di argomenti.
#
# Integer 1 se registrato, altrimenti 0; confrontabile con TRUE/FALSE o 1/0. Non conferma
# oggetti, azioni o permessi del server.

SUB Main()
    # Il terzo definisce l’intero helper e confronta una forma breve rimossa o un’arità assente con
    # una forma valida. name, first, second, count passano nomi/numero invariati. Risultato 0 per
    # chiamate, "0:1" per valori.

    RETURN CheckForm('UO.GetType',0)
END SUB

FUNCTION CheckForm(name,count)
    RETURN UO.ApiSignatureExists(name,count)
END FUNCTION
```

**Spiegazione dei parametri e dell’esecuzione:**

- Il terzo definisce l’intero helper e confronta una forma breve rimossa o un’arità assente con una forma valida. name, first, second, count passano nomi/numero invariati. Risultato 0 per chiamate, "0:1" per valori.
