# UO.FindItem

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge il serial del primo oggetto dell’ultima ricerca.

## Sintassi esatta

```text
UO.FindItem() -> Any
```

## Parametri

Nessun parametro.

## Restituisce

Integer — serial/ID del primo oggetto, oppure 0 senza risultati. Non è graphic/type. A differenza di FindType, restituisce un numero e non una stringa esadecimale.

## Comportamento

- FindType con 1–5 argomenti, FindTypeEx e Count/CountEx/CountGround sostituiscono i risultati di questo script. Una ricerca senza corrispondenze svuota l’istantanea. Salvare i valori utili prima di una nuova ricerca.
- Queste chiamate non avviano ricerche, non aprono contenitori, non spostano oggetti e non inviano pacchetti. Usano i dati caricati dal client. FindCount(id) non richiede una ricerca precedente e non ne modifica i risultati.
- FindItem/FindCount()/FindFullQuantity sono istantanee della ricerca. FindQuantity e FindCount(id) leggono la quantità attuale; l’oggetto può cambiare o sparire dopo la ricerca.

## Esempi

### Leggere una ricerca d’oro

```vb
# Leggere una ricerca d’oro
#
# Legge il serial del primo oggetto dell’ultima ricerca.
#
# Integer — serial/ID del primo oggetto, oppure 0 senza risultati. Non è graphic/type. A
# differenza di FindType, restituisce un numero e non una stringa esadecimale.

SUB Main()
    # type=0x0EED è oro; color=-1 accetta ogni colore; backpack seleziona il contenuto diretto in
    # questa forma di FindType. value conserva il risultato; STR lo mostra come testo.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindItem()
    UO.Print(STR(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- type=0x0EED è oro; color=-1 accetta ogni colore; backpack seleziona il contenuto diretto in questa forma di FindType. value conserva il risultato; STR lo mostra come testo.

### Confrontare oggetti, pila e totale

```vb
# Confrontare oggetti, pila e totale
#
# Legge il serial del primo oggetto dell’ultima ricerca.
#
# Integer — serial/ID del primo oggetto, oppure 0 senza risultati. Non è graphic/type. A
# differenza di FindType, restituisce un numero e non una stringa esadecimale.

SUB Main()
    # Le quattro letture seguono la stessa ricerca. Due pile da 50: oggetti=2, prima pila=50,
    # totale=100. FindItem è l’ID univoco della prima pila, non il suo type.

    UO.FindType(0x0EED, -1, 'backpack')
    UO.Print(STR(UO.FindCount()))
    UO.Print(STR(UO.FindQuantity()))
    UO.Print(STR(UO.FindFullQuantity()))
    UO.Print('0x' + Hex(UO.FindItem()))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Le quattro letture seguono la stessa ricerca. Due pile da 50: oggetti=2, prima pila=50, totale=100. FindItem è l’ID univoco della prima pila, non il suo type.

### Conservare un valore prima di cercare

```vb
# Conservare un valore prima di cercare
#
# Legge il serial del primo oggetto dell’ultima ricerca.
#
# Integer — serial/ID del primo oggetto, oppure 0 senza risultati. Non è graphic/type. A
# differenza di FindType, restituisce un numero e non una stringa esadecimale.

SUB Main()
    # Il primo type è oro; 0x0F7A è un altro reagente. Il secondo FindType sostituisce l’istantanea.
    # saved conserva il valore precedente; l’ultima lettura usa il nuovo risultato.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindItem()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindItem()))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Il primo type è oro; 0x0F7A è un altro reagente. Il secondo FindType sostituisce l’istantanea. saved conserva il valore precedente; l’ultima lettura usa il nuovo risultato.
