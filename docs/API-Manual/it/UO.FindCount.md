# UO.FindCount

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Conta gli oggetti trovati oppure le unità di una pila tramite ID.

## Sintassi esatta

```text
UO.FindCount() -> Integer
UO.FindCount(id:Any) -> Integer
```

## Parametri

- `id` — Facoltativo solo per FindCount. Serial di un oggetto: Integer, stringa decimale/esadecimale, lasttarget, lastobject, backpack o nome AddObject. Usare un ID, non graphic/type. Nome sconosciuto: 0. self indica il personaggio e qui dà 0. Senza argomento legge il numero di oggetti trovati.

## Restituisce

Integer — FindCount() conta gli oggetti: una pila conta come un item. FindCount(id) legge il suo Amount attuale; ID sconosciuti/eliminati e personaggi restituiscono 0. Un oggetto non impilabile ha normalmente Amount=1. Non restituisce ID, type o Boolean.

## Comportamento

- FindType con 1–5 argomenti, FindTypeEx e Count/CountEx/CountGround sostituiscono i risultati di questo script. Una ricerca senza corrispondenze svuota l’istantanea. Salvare i valori utili prima di una nuova ricerca.
- Queste chiamate non avviano ricerche, non aprono contenitori, non spostano oggetti e non inviano pacchetti. Usano i dati caricati dal client. FindCount(id) non richiede una ricerca precedente e non ne modifica i risultati.
- FindItem/FindCount()/FindFullQuantity sono istantanee della ricerca. FindQuantity e FindCount(id) leggono la quantità attuale; l’oggetto può cambiare o sparire dopo la ricerca.

## Esempi

### Leggere una ricerca d’oro

```vb
# Leggere una ricerca d’oro
#
# Conta gli oggetti trovati oppure le unità di una pila tramite ID.
#
# Integer — FindCount() conta gli oggetti: una pila conta come un item. FindCount(id) legge il
# suo Amount attuale; ID sconosciuti/eliminati e personaggi restituiscono 0. Un oggetto non
# impilabile ha normalmente Amount=1. Non restituisce ID, type o Boolean.

SUB Main()
    # type=0x0EED è oro; color=-1 accetta ogni colore; backpack seleziona il contenuto diretto in
    # questa forma di FindType. value conserva il risultato; STR lo mostra come testo.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindCount()
    UO.Print(STR(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- type=0x0EED è oro; color=-1 accetta ogni colore; backpack seleziona il contenuto diretto in questa forma di FindType. value conserva il risultato; STR lo mostra come testo.

### Confrontare oggetti, pila e totale

```vb
# Confrontare oggetti, pila e totale
#
# Conta gli oggetti trovati oppure le unità di una pila tramite ID.
#
# Integer — FindCount() conta gli oggetti: una pila conta come un item. FindCount(id) legge il
# suo Amount attuale; ID sconosciuti/eliminati e personaggi restituiscono 0. Un oggetto non
# impilabile ha normalmente Amount=1. Non restituisce ID, type o Boolean.

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
# Conta gli oggetti trovati oppure le unità di una pila tramite ID.
#
# Integer — FindCount() conta gli oggetti: una pila conta come un item. FindCount(id) legge il
# suo Amount attuale; ID sconosciuti/eliminati e personaggi restituiscono 0. Un oggetto non
# impilabile ha normalmente Amount=1. Non restituisce ID, type o Boolean.

SUB Main()
    # Il primo type è oro; 0x0F7A è un altro reagente. Il secondo FindType sostituisce l’istantanea.
    # saved conserva il valore precedente; l’ultima lettura usa il nuovo risultato.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindCount()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindCount()))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Il primo type è oro; 0x0F7A è un altro reagente. Il secondo FindType sostituisce l’istantanea. saved conserva il valore precedente; l’ultima lettura usa il nuovo risultato.

### Leggere direttamente un ID

```vb
# Leggere direttamente un ID
#
# Conta gli oggetti trovati oppure le unità di una pila tramite ID.
#
# Integer — FindCount() conta gli oggetti: una pila conta come un item. FindCount(id) legge il
# suo Amount attuale; ID sconosciuti/eliminati e personaggi restituiscono 0. Un oggetto non
# impilabile ha normalmente Amount=1. Non restituisce ID, type o Boolean.

SUB Main()
    # lasttarget deve indicare un oggetto già selezionato nel gioco. Non appare un nuovo cursore.
    # FindCount(id) legge la pila attuale, restituisce 0 se l’oggetto è assente e conserva
    # l’istantanea della ricerca.

    VAR id = lasttarget
    VAR amount = UO.FindCount(id)
    UO.Print(STR(amount))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- lasttarget deve indicare un oggetto già selezionato nel gioco. Non appare un nuovo cursore. FindCount(id) legge la pila attuale, restituisce 0 se l’oggetto è assente e conserva l’istantanea della ricerca.
