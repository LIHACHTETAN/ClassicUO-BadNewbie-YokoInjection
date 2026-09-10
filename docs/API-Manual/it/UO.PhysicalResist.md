# UO.PhysicalResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge il campo di resistenza del giocatore attuale: armatura/resistenza fisica.

## Sintassi esatta

```text
UO.PhysicalResist() -> Integer
```

## Parametri

Nessun parametro.

## Restituisce

Integer — valore status con segno, -32768..32767 nel modello. I negativi vengono conservati. 0 può essere reale, sconosciuto o dovuto a Player assente/distrutto; GetResist restituisce 0 anche per selettori ignoti. Non è Boolean, ID, abilità o limite. 1 indica un punto, non un successo.

## Comportamento

- Nessun argomento. Seguire le firme visualizzate.
- Legge Player.PhysicalResistance nel thread di gioco se Player esiste e non è distrutto; altrimenti 0. Nessuna ricerca nell’equipaggiamento, calcolo bonus, richiesta status o attesa. Un fantasma presente non è un Player distrutto.
- PhysicalResistance è il campo armatura/status del server: indice d’armatura con regole classiche, resistenza fisica con regole basate sulle resistenze. Non converte le regole né calcola la percentuale di danno evitato. Armor e alias fisici leggono lo stesso campo.
- CharacterStatus verifica il corpo fisso prima delle modifiche, poi converte le word in Int16 con segno. Un corpo troncato conserva i dati precedenti. La coda opzionale type 6 mantiene il comportamento esistente; questi getter non ne leggono i massimi di resistenza.
- Ogni chiamata rilegge i dati locali. Le variabili conservano istantanee; letture separate possono vedere aggiornamenti diversi. Un risultato non zero non verifica la connessione; zero può essere un valore o dati assenti.
- RegisterCharacterGetterAliases aggiunge funzioni senza argomenti e nomi intrinseci mancanti. I rami esistenti leggono lo stesso campo. Nomi indipendenti dalle maiuscole; intrinseci senza parentesi riletti salvo variabili che li nascondono.

### Funzioni interne: dalla chiamata al risultato

Passaggi nativi della lettura locale. ResistanceAtLeast sotto è una funzione BASIC utente completa, non un’API nascosta o un comando per indossare protezioni.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases aggiunge funzioni senza argomenti e nomi intrinseci mancanti. I rami esistenti leggono lo stesso campo. Nomi indipendenti dalle maiuscole; intrinseci senza parentesi riletti salvo variabili che li nascondono.

`Armor PhysicalResist ResistPhysical GetArmor GetPhysicalResist GetResistPhysical`.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `RegisterCharacterGetterAliases`.

#### 2. Invoke

Legge Player.PhysicalResistance nel thread di gioco se Player esiste e non è distrutto; altrimenti 0. Nessuna ricerca nell’equipaggiamento, calcolo bonus, richiesta status o attesa. Un fantasma presente non è un Player distrutto.

Invoke legge sul thread del gioco; l’attesa rispetta l’annullamento dello script. Nessun pacchetto, richiesta status, target, modifica o ritardo incorporato.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 3. CharacterStatus

CharacterStatus verifica il corpo fisso prima delle modifiche, poi converte le word in Int16 con segno. Un corpo troncato conserva i dati precedenti. La coda opzionale type 6 mantiene il comportamento esistente; questi getter non ne leggono i massimi di resistenza.

PhysicalResistance è il campo armatura/status del server: indice d’armatura con regole classiche, resistenza fisica con regole basate sulle resistenze. Non converte le regole né calcola la percentuale di danno evitato. Armor e alias fisici leggono lo stesso campo.

Sorgente del progetto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; funzione `CharacterStatus`.

#### 4. Clear

World.Clear rimuove Player. Le letture danno 0 finché giocatore e dati non tornano disponibili. Un valore salvato non prova il requisito dopo una riconnessione.

Integer — valore status con segno, -32768..32767 nel modello. I negativi vengono conservati. 0 può essere reale, sconosciuto o dovuto a Player assente/distrutto; GetResist restituisce 0 anche per selettori ignoti. Non è Boolean, ID, abilità o limite. 1 indica un punto, non un successo.

Sorgente del progetto: `src/ClassicUO.Client/Game/World.cs`; funzione `Clear`.

Ogni chiamata rilegge i dati locali. Le variabili conservano istantanee; letture separate possono vedere aggiornamenti diversi. Un risultato non zero non verifica la connessione; zero può essere un valore o dati assenti.


## Esempi

### Mostrare il valore in cache

```vb
# Mostrare il valore in cache
#
# Legge il campo di resistenza del giocatore attuale: armatura/resistenza fisica.
#
# Integer — valore status con segno, -32768..32767 nel modello. I negativi vengono conservati. 0
# può essere reale, sconosciuto o dovuto a Player assente/distrutto; GetResist restituisce 0
# anche per selettori ignoti. Non è Boolean, ID, abilità o limite. 1 indica un punto, non un
# successo.

SUB Main()
    # value conserva una lettura del giocatore senza argomenti; CStr la formatta per il diario.

    VAR value = UO.PhysicalResist()
    UO.Print('PhysicalResistance: ' + CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value conserva una lettura del giocatore senza argomenti; CStr la formatta per il diario.

### Confrontare due osservazioni

```vb
# Confrontare due osservazioni
#
# Legge il campo di resistenza del giocatore attuale: armatura/resistenza fisica.
#
# Integer — valore status con segno, -32768..32767 nel modello. I negativi vengono conservati. 0
# può essere reale, sconosciuto o dovuto a Player assente/distrutto; GetResist restituisce 0
# anche per selettori ignoti. Non è Boolean, ID, abilità o limite. 1 indica un punto, non un
# successo.

SUB Main()
    # WAIT(500) separa before e after di 500 ms; difference può essere negativa. Si possono perdere
    # aggiornamenti intermedi. L’attesa è dell’esempio.

    VAR before = UO.PhysicalResist()
    WAIT(500)
    VAR after = UO.PhysicalResist()
    VAR difference = after - before
    UO.Print('Resistance change: ' + CStr(difference))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- WAIT(500) separa before e after di 500 ms; difference può essere negativa. Si possono perdere aggiornamenti intermedi. L’attesa è dell’esempio.

### Funzione completa per la resistenza minima

```vb
# Funzione completa per la resistenza minima
#
# Legge il campo di resistenza del giocatore attuale: armatura/resistenza fisica.
#
# Integer — valore status con segno, -32768..32767 nel modello. I negativi vengono conservati. 0
# può essere reale, sconosciuto o dovuto a Player assente/distrutto; GetResist restituisce 0
# anche per selettori ignoti. Non è Boolean, ID, abilità o limite. 1 indica un punto, non un
# successo.

SUB Main()
    # minimum=50 è un requisito d’esempio, non un limite. ResistanceAtLeast rifiuta Player assente,
    # legge una volta e restituisce Integer Boolean 1=TRUE o 0=FALSE per value >= minimum. La
    # resistenza non è Boolean. Definizione completa sotto.

    IF ResistanceAtLeast(50) = TRUE THEN
        UO.Print('Local resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.PhysicalResist()
    RETURN value >= minimum
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- minimum=50 è un requisito d’esempio, non un limite. ResistanceAtLeast rifiuta Player assente, legge una volta e restituisce Integer Boolean 1=TRUE o 0=FALSE per value >= minimum. La resistenza non è Boolean. Definizione completa sotto.
