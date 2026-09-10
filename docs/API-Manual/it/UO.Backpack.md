# UO.Backpack

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Restituisce l’ID dello zaino attualmente equipaggiato.

## Sintassi esatta

```text
UO.Backpack() -> Integer
```

## Parametri

Nessun parametro.

## Restituisce

Integer — serial/ID, non graphic/type, layer, quantità o Boolean. 0: nessun oggetto attuale. Conserva tutti i 32 bit; verificare <> 0, non = TRUE o > 0. Il risultato salvato non si aggiorna da solo. Cerca l’item non distrutto sul layer Backpack di Player. Player o zaino assente/distrutto dà 0. Identifica il contenitore, non il contenuto; non crea borse.

## Comportamento

- Nessun argomento. Lettura locale tramite Invoke sul thread del gioco; l’annullamento può interrompere l’attesa di quel thread. Nessun pacchetto, apertura, target o trasferimento.
- Gli intrinseci self/backpack senza parentesi vengono riletti, salvo variabili che li nascondono. Gli alias testuali dipendono dal comando che li riceve. Come destinazione di trasferimento "self" significa zaino, mentre UO.Self() restituisce il personaggio. Per un contenitore usare UO.Backpack().
- World.Clear rimuove Player: le letture seguenti danno 0. Accesso o sostituzione dello zaino possono cambiare ID. Letture separate non sono atomiche. ID diverso da 0 non dimostra connessione, permesso del server o contenuto caricato.

### Funzioni interne: dalla chiamata al risultato

Passaggi reali di lettura dell’oggetto client. IsOwnSerial è la funzione completa dell’esempio, non un’altra API integrata.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility sceglie il ramo senza argomenti e inserisce l’Integer del bridge in InjectionValue. Nessun parametro di uscita Pascal o argomento opzionale aggiuntivo.

Integer — serial/ID, non graphic/type, layer, quantità o Boolean. 0: nessun oggetto attuale. Conserva tutti i 32 bit; verificare <> 0, non = TRUE o > 0. Il risultato salvato non si aggiorna da solo.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `ExecuteStealthCompatibility`.

#### 2. Invoke

Cerca l’item non distrutto sul layer Backpack di Player. Player o zaino assente/distrutto dà 0. Identifica il contenitore, non il contenuto; non crea borse. Invoke legge nel thread del gioco; un thread di lavoro attende l’elaborazione del gestore. L’annullamento dello script interrompe l’attesa. Nessun ritardo o richiesta di rete aggiuntivi.

Integer — serial/ID, non graphic/type, layer, quantità o Boolean. 0: nessun oggetto attuale. Conserva tutti i 32 bit; verificare <> 0, non = TRUE o > 0. Il risultato salvato non si aggiorna da solo. Nessun argomento. Lettura locale tramite Invoke sul thread del gioco; l’annullamento può interrompere l’attesa di quel thread. Nessun pacchetto, apertura, target o trasferimento.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 3. FindItemByLayer

Cerca l’item non distrutto sul layer Backpack di Player. Player o zaino assente/distrutto dà 0. Identifica il contenitore, non il contenuto; non crea borse.

Integer — serial/ID, non graphic/type, layer, quantità o Boolean. 0: nessun oggetto attuale. Conserva tutti i 32 bit; verificare <> 0, non = TRUE o > 0. Il risultato salvato non si aggiorna da solo.

Sorgente del progetto: `src/ClassicUO.Client/Game/GameObjects/Entity.cs`; funzione `FindItemByLayer`.

#### 4. Clear

World.Clear rimuove Player: le letture seguenti danno 0. Accesso o sostituzione dello zaino possono cambiare ID. Letture separate non sono atomiche. ID diverso da 0 non dimostra connessione, permesso del server o contenuto caricato.

World.Clear rimuove Player: le letture seguenti danno 0. Accesso o sostituzione dello zaino possono cambiare ID. Letture separate non sono atomiche. ID diverso da 0 non dimostra connessione, permesso del server o contenuto caricato.

Sorgente del progetto: `src/ClassicUO.Client/Game/World.cs`; funzione `Clear`.

World.Clear rimuove Player: le letture seguenti danno 0. Accesso o sostituzione dello zaino possono cambiare ID. Letture separate non sono atomiche. ID diverso da 0 non dimostra connessione, permesso del server o contenuto caricato.


## Esempi

### Leggere e mostrare l’ID

```vb
# Leggere e mostrare l’ID
#
# Restituisce l’ID dello zaino attualmente equipaggiato.
#
# Integer — serial/ID, non graphic/type, layer, quantità o Boolean. 0: nessun oggetto attuale.
# Conserva tutti i 32 bit; verificare <> 0, non = TRUE o > 0. Il risultato salvato non si
# aggiorna da solo. Cerca l’item non distrutto sul layer Backpack di Player. Player o zaino
# assente/distrutto dà 0. Identifica il contenitore, non il contenuto; non crea borse.

SUB Main()
    # id conserva un risultato; HEX formatta il serial nel diario. Nessun oggetto viene scelto o
    # usato.

    VAR id = UO.Backpack()
    UO.Print('ID: ' + HEX(id))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- id conserva un risultato; HEX formatta il serial nel diario. Nessun oggetto viene scelto o usato.

### Rilevare un cambio di ID

```vb
# Rilevare un cambio di ID
#
# Restituisce l’ID dello zaino attualmente equipaggiato.
#
# Integer — serial/ID, non graphic/type, layer, quantità o Boolean. 0: nessun oggetto attuale.
# Conserva tutti i 32 bit; verificare <> 0, non = TRUE o > 0. Il risultato salvato non si
# aggiorna da solo. Cerca l’item non distrutto sul layer Backpack di Player. Player o zaino
# assente/distrutto dà 0. Identifica il contenitore, non il contenuto; non crea borse.

SUB Main()
    # before/after sono letti a 250 ms di distanza. WAIT è solo nell’esempio. Valori finali uguali
    # possono nascondere cambiamenti intermedi.

    VAR before = UO.Backpack()
    WAIT(250)
    VAR after = UO.Backpack()
    IF before <> after THEN
        UO.Print('ID changed: ' + HEX(after))
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- before/after sono letti a 250 ms di distanza. WAIT è solo nell’esempio. Valori finali uguali possono nascondere cambiamenti intermedi.

### Funzione IsOwnSerial completa

```vb
# Funzione IsOwnSerial completa
#
# Restituisce l’ID dello zaino attualmente equipaggiato.
#
# Integer — serial/ID, non graphic/type, layer, quantità o Boolean. 0: nessun oggetto attuale.
# Conserva tutti i 32 bit; verificare <> 0, non = TRUE o > 0. Il risultato salvato non si
# aggiorna da solo. Cerca l’item non distrutto sul layer Backpack di Player. Player o zaino
# assente/distrutto dà 0. Identifica il contenitore, non il contenuto; non crea borse.

SUB Main()
    # candidate è l’ID LastTarget salvato. IsOwnSerial(candidate) prende un serial e restituisce
    # Integer Boolean: 1=TRUE per l’ID proprio attuale diverso da 0, altrimenti 0=FALSE. Funzione
    # completa, senza cambiare target.

    VAR candidate = UO.LastTarget()
    IF IsOwnSerial(candidate) = TRUE THEN
        UO.Print('Own object selected')
    ELSE
        UO.Print('Different object or no own object')
    END IF
END SUB

SUB IsOwnSerial(candidate)
    VAR current = UO.Backpack()
    RETURN current <> 0 AND current = candidate
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- candidate è l’ID LastTarget salvato. IsOwnSerial(candidate) prende un serial e restituisce Integer Boolean: 1=TRUE per l’ID proprio attuale diverso da 0, altrimenti 0=FALSE. Funzione completa, senza cambiare target.
