# UO.PredictedDirection

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge il valore previsto di direzione dopo i passi già accodati del giocatore.

## Sintassi esatta

```text
UO.PredictedDirection() -> Integer
```

## Parametri

Nessun parametro.

## Restituisce

Integer direzione 0..7 senza bit di corsa. 0 indica nord o giocatore assente.

## Comportamento

- Solo la funzione UO senza argomenti indicata nella sintassi. Nessun target, serial, type, destinazione, distanza o timeout. Numero, non Boolean, ID o record tile: 1 non significa arrivo.
- GetEndPosition legge X/Y/Z/direzione dell’ultimo Mobile.Step già accodato. Con coda vuota legge posizione/direzione attuale. Lettura O(1) senza rimuovere passi, muoversi, inviare pacchetti, calcolare percorsi o attendere l’arrivo.
- Direzioni del mondo: 0 nord, 1 nord-est, 2 est, 3 sud-est, 4 sud, 5 sud-ovest, 6 ovest, 7 nord-ovest. Schermo isometrico. Direction.Mask elimina il flag corsa; non restituisce velocità.
- Previsione locale, non arrivo confermato. Passi nuovi/completati/rifiutati, svuotamento coda o teletrasporto possono cambiarla. Letture separate non atomiche; X uguale non prova Y/Z o accettazione del server.
- Invoke legge nel thread del gioco; un thread di lavoro attende l’elaborazione del gestore. L’annullamento dello script interrompe l’attesa. Nessun ritardo o richiesta di rete aggiuntivi.
- Le IApiBridge esterne senza IPredictedMovementBridge mantengono il ripiego su posizione/direzione attuale. Classic UO implementa l’interfaccia che considera la coda.

### Funzioni interne: dalla chiamata al risultato

Passaggi nativi effettivi. PredictionEquals è una funzione BASIC utente completamente definita, non un comando interno o una procedura di movimento.

#### 1. ExecuteStealthCompatibility

La funzione nativa chiama ReadPredictedCoordinate e seleziona la proprietà IPredictedMovementBridge. Nessun NewMoveXY o avvio del calcolo del percorso.

Solo la funzione UO senza argomenti indicata nella sintassi. Nessun target, serial, type, destinazione, distanza o timeout. Numero, non Boolean, ID o record tile: 1 non significa arrivo.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `ExecuteStealthCompatibility`.

#### 2. ReadPredictedCoordinate

La funzione nativa chiama ReadPredictedCoordinate e seleziona la proprietà IPredictedMovementBridge. Nessun NewMoveXY o avvio del calcolo del percorso.

Le IApiBridge esterne senza IPredictedMovementBridge mantengono il ripiego su posizione/direzione attuale. Classic UO implementa l’interfaccia che considera la coda.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `ReadPredictedCoordinate`.

#### 3. Invoke

Invoke legge nel thread del gioco; un thread di lavoro attende l’elaborazione del gestore. L’annullamento dello script interrompe l’attesa. Nessun ritardo o richiesta di rete aggiuntivi.

Integer direzione 0..7 senza bit di corsa. 0 indica nord o giocatore assente.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 4. ReadPredictedPosition

ReadPredictedPosition restituisce 0 se Player è assente/distrutto; altrimenti chiama GetEndPosition e sceglie un componente.

GetEndPosition legge X/Y/Z/direzione dell’ultimo Mobile.Step già accodato. Con coda vuota legge posizione/direzione attuale. Lettura O(1) senza rimuovere passi, muoversi, inviare pacchetti, calcolare percorsi o attendere l’arrivo.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `ReadPredictedPosition`.

#### 5. GetEndPosition

GetEndPosition legge X/Y/Z/direzione dell’ultimo Mobile.Step già accodato. Con coda vuota legge posizione/direzione attuale. Lettura O(1) senza rimuovere passi, muoversi, inviare pacchetti, calcolare percorsi o attendere l’arrivo.

Direzioni del mondo: 0 nord, 1 nord-est, 2 est, 3 sud-est, 4 sud, 5 sud-ovest, 6 ovest, 7 nord-ovest. Schermo isometrico. Direction.Mask elimina il flag corsa; non restituisce velocità.

Sorgente del progetto: `src/ClassicUO.Client/Game/GameObjects/Mobile.cs`; funzione `GetEndPosition`.

#### 6. InjectionValue

Integer direzione 0..7 senza bit di corsa. 0 indica nord o giocatore assente.

Previsione locale, non arrivo confermato. Passi nuovi/completati/rifiutati, svuotamento coda o teletrasporto possono cambiarla. Letture separate non atomiche; X uguale non prova Y/Z o accettazione del server.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs`; funzione `InjectionValue`.

PredictionEquals(expected) riceve una coordinata/altezza/direzione numerica, rifiuta il giocatore assente e confronta un componente previsto. Restituisce Integer Boolean 1=TRUE o 0=FALSE. Non attende né garantisce l’arrivo.


## Esempi

### Leggere un componente

```vb
# Leggere un componente
#
# Legge il valore previsto di direzione dopo i passi già accodati del giocatore.
#
# Integer direzione 0..7 senza bit di corsa. 0 indica nord o giocatore assente.

SUB Main()
    # predicted salva una chiamata senza argomenti; CStr formatta il numero per il diario.

    VAR predicted = UO.PredictedDirection()
    UO.Print('Predicted: ' + CStr(predicted))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- predicted salva una chiamata senza argomenti; CStr formatta il numero per il diario.

### Osservare un cambiamento

```vb
# Osservare un cambiamento
#
# Legge il valore previsto di direzione dopo i passi già accodati del giocatore.
#
# Integer direzione 0..7 senza bit di corsa. 0 indica nord o giocatore assente.

SUB Main()
    # WAIT(100) sospende questo esempio per 100 ms. before/after possono essere uguali malgrado
    # movimento intermedio; queste letture non avviano movimento.

    VAR before = UO.PredictedDirection()
    WAIT(100)
    VAR after = UO.PredictedDirection()
    IF before <> after THEN
        UO.Print('Prediction changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- WAIT(100) sospende questo esempio per 100 ms. before/after possono essere uguali malgrado movimento intermedio; queste letture non avviano movimento.

### Funzione di confronto completa

```vb
# Funzione di confronto completa
#
# Legge il valore previsto di direzione dopo i passi già accodati del giocatore.
#
# Integer direzione 0..7 senza bit di corsa. 0 indica nord o giocatore assente.

SUB Main()
    # expected è una coordinata/altezza/direzione di esempio, non un argomento nativo.
    # PredictionEquals verifica UO.Self(), legge una volta e restituisce 1=TRUE se uguale,
    # altrimenti 0=FALSE. Codice completo sotto Main. Un componente uguale non equivale all’arrivo.

    IF PredictionEquals(4) = TRUE THEN
        UO.Print('Queued endpoint matches this component')
    ELSE
        UO.Print('Different component or no player')
    END IF
END SUB

SUB PredictionEquals(expected)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR predicted = UO.PredictedDirection()
    RETURN predicted = expected
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- expected è una coordinata/altezza/direzione di esempio, non un argomento nativo. PredictionEquals verifica UO.Self(), legge una volta e restituisce 1=TRUE se uguale, altrimenti 0=FALSE. Codice completo sotto Main. Un componente uguale non equivale all’arrivo.
