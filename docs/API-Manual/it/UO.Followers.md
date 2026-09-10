# UO.Followers

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge il contatore status del giocatore attuale: slot di controllo occupati.

## Sintassi esatta

```text
UO.Followers() -> Integer
```

## Parametri

Nessun parametro.

## Restituisce

Integer — slot di controllo occupati, 0..255 nel modello. 0 può essere reale, sconosciuto o Player assente/distrutto. Quantità, non Boolean, ID o type: 1 significa un’unità, non successo. Nessuna ricerca oggetti o array restituito.

## Comportamento

- Nessun argomento. Seguire le firme visualizzate.
- Legge Player.Followers nel thread di gioco se Player esiste e non è distrutto; altrimenti 0. Nessuna ricerca nell’equipaggiamento, calcolo bonus, richiesta status o attesa. Un fantasma presente non è un Player distrutto.
- PetsCurrent/Followers legge gli slot occupati dallo status proprio type >= 3. Un animale può usare più slot; il server definisce le regole per creature evocate/addomesticate. Non conta mobile visibili, non elenca ID e non conta animali vicini.
- CharacterStatus verifica il corpo fisso prima degli aggiornamenti. Weight è nello status proprio esteso, slot dal type 3, Luck dal type 4, WeightMax server dal type 5. Pacchetti compatti/vecchi senza un contatore opzionale conservano la cache. Player nuovo parte da zero; nessuna prova di status fresco.
- RegisterCharacterGetterAliases aggiunge funzioni senza argomenti e nomi intrinseci mancanti. I rami esistenti leggono lo stesso campo. Nomi indipendenti dalle maiuscole; intrinseci senza parentesi riletti salvo variabili che li nascondono.
- Ogni chiamata rilegge i dati locali. Le variabili conservano istantanee; letture separate possono vedere aggiornamenti diversi. Un risultato non zero non verifica la connessione; zero può essere un valore o dati assenti.

### Funzioni interne: dalla chiamata al risultato

Passaggi nativi della lettura cache. CanCarry, LuckAtLeast o CanAddFollower nell’esempio è una funzione BASIC utente completa, non un’azione nativa nascosta. Non modifica inventario o seguaci.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases aggiunge funzioni senza argomenti e nomi intrinseci mancanti. I rami esistenti leggono lo stesso campo. Nomi indipendenti dalle maiuscole; intrinseci senza parentesi riletti salvo variabili che li nascondono.

`PetsCurrent Followers GetPetsCurrent GetFollowers`.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `RegisterCharacterGetterAliases`.

#### 2. Invoke

Legge Player.Followers nel thread di gioco se Player esiste e non è distrutto; altrimenti 0. Nessuna ricerca nell’equipaggiamento, calcolo bonus, richiesta status o attesa. Un fantasma presente non è un Player distrutto.

Invoke legge sul thread del gioco; l’attesa rispetta l’annullamento dello script. Nessun pacchetto, richiesta status, target, modifica o ritardo incorporato.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 3. CharacterStatus

CharacterStatus verifica il corpo fisso prima degli aggiornamenti. Weight è nello status proprio esteso, slot dal type 3, Luck dal type 4, WeightMax server dal type 5. Pacchetti compatti/vecchi senza un contatore opzionale conservano la cache. Player nuovo parte da zero; nessuna prova di status fresco.

PetsCurrent/Followers legge gli slot occupati dallo status proprio type >= 3. Un animale può usare più slot; il server definisce le regole per creature evocate/addomesticate. Non conta mobile visibili, non elenca ID e non conta animali vicini.

Sorgente del progetto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; funzione `CharacterStatus`.

#### 4. Clear

World.Clear rimuove Player. Le letture danno 0 finché giocatore e dati non tornano disponibili. Un valore salvato non prova il requisito dopo una riconnessione.

Integer — slot di controllo occupati, 0..255 nel modello. 0 può essere reale, sconosciuto o Player assente/distrutto. Quantità, non Boolean, ID o type: 1 significa un’unità, non successo. Nessuna ricerca oggetti o array restituito.

Sorgente del progetto: `src/ClassicUO.Client/Game/World.cs`; funzione `Clear`.

Ogni chiamata rilegge i dati locali. Le variabili conservano istantanee; letture separate possono vedere aggiornamenti diversi. Un risultato non zero non verifica la connessione; zero può essere un valore o dati assenti.


## Esempi

### Mostrare il contatore in cache

```vb
# Mostrare il contatore in cache
#
# Legge il contatore status del giocatore attuale: slot di controllo occupati.
#
# Integer — slot di controllo occupati, 0..255 nel modello. 0 può essere reale, sconosciuto o
# Player assente/distrutto. Quantità, non Boolean, ID o type: 1 significa un’unità, non
# successo. Nessuna ricerca oggetti o array restituito.

SUB Main()
    # value conserva una lettura senza argomenti del giocatore; CStr la formatta per il diario senza
    # cambiarne il senso.

    VAR value = UO.Followers()
    UO.Print('Followers: ' + CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value conserva una lettura senza argomenti del giocatore; CStr la formatta per il diario senza cambiarne il senso.

### Osservare una variazione

```vb
# Osservare una variazione
#
# Legge il contatore status del giocatore attuale: slot di controllo occupati.
#
# Integer — slot di controllo occupati, 0..255 nel modello. 0 può essere reale, sconosciuto o
# Player assente/distrutto. Quantità, non Boolean, ID o type: 1 significa un’unità, non
# successo. Nessuna ricerca oggetti o array restituito.

SUB Main()
    # WAIT(500) separa before e after di 500 ms. difference può essere positiva, zero o negativa;
    # aggiornamenti e cambi di personaggio intermedi possono sfuggire. L’attesa è dell’esempio.

    VAR before = UO.Followers()
    WAIT(500)
    VAR after = UO.Followers()
    VAR difference = after - before
    UO.Print('Counter change: ' + CStr(difference))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- WAIT(500) separa before e after di 500 ms. difference può essere positiva, zero o negativa; aggiornamenti e cambi di personaggio intermedi possono sfuggire. L’attesa è dell’esempio.

### Funzione decisionale completa

```vb
# Funzione decisionale completa
#
# Legge il contatore status del giocatore attuale: slot di controllo occupati.
#
# Integer — slot di controllo occupati, 0..255 nel modello. 0 può essere reale, sconosciuto o
# Player assente/distrutto. Quantità, non Boolean, ID o type: 1 significa un’unità, non
# successo. Nessuna ricerca oggetti o array restituito.

SUB Main()
    # CanAddFollower(extraSlots) riceve slot richiesti; 2 può significare una sola creatura da due
    # slot. Rifiuta input negativo, Player assente o maximum <= 0, legge occupazione/limite e
    # restituisce Integer Boolean 1=TRUE o 0=FALSE per extraSlots <= maximum - current. Nessun
    # overflow di somma; oltre limite dà false anche per zero. Non verifica proprietario, abilità di
    # addomesticamento o permesso server. Possibili aggiornamenti fra letture.

    IF CanAddFollower(2) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB CanAddFollower(extraSlots)
    IF extraSlots < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR current = UO.Followers()
    VAR maximum = UO.PetsMax()
    IF maximum <= 0 THEN
        RETURN FALSE
    END IF
    RETURN extraSlots <= maximum - current
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- CanAddFollower(extraSlots) riceve slot richiesti; 2 può significare una sola creatura da due slot. Rifiuta input negativo, Player assente o maximum <= 0, legge occupazione/limite e restituisce Integer Boolean 1=TRUE o 0=FALSE per extraSlots <= maximum - current. Nessun overflow di somma; oltre limite dà false anche per zero. Non verifica proprietario, abilità di addomesticamento o permesso server. Possibili aggiornamenti fra letture.
