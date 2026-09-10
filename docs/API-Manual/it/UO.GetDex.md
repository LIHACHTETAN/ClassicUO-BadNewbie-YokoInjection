# UO.GetDex

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge la Destrezza attuale (Dexterity, DEX).

## Sintassi esatta

```text
UO.GetDex() -> Integer
UO.GetDex(ObjID:Any) -> Integer
```

## Parametri

- `ObjID` — ObjID solo nella forma con un argomento: serial intero, stringa decimale/esadecimale 0x, "self", "lasttarget" o nome AddObject. Identifica il personaggio, non graphic/type. Senza argomento legge il giocatore attuale.

## Restituisce

Integer — punti attuali, 0..65535 nel modello; non percentuale, ID, abilità, blocco o Boolean. 0 può indicare anche giocatore assente/distrutto o soggetto non disponibile. Confrontare con una soglia numerica, non = TRUE. Non è il limite né necessariamente il valore base senza modificatori.

## Comportamento

- Forme supportate: () per self, (ObjID) per un soggetto esplicito. Nessun altro argomento opzionale.
- Legge Player.Dexterity se Player esiste e non è distrutto, altrimenti 0. Un personaggio morto presente non è un oggetto distrutto. Nessun calcolo da HP, mana o stamina.
- GetStr/GetInt/GetDex accettano ObjID, ma questi attributi sono memorizzati solo su PlayerMobile: ogni altro serial dà 0, anche per un mobile caricato. Limite rispetto alla descrizione generica Stealth; nessun valore remoto viene inventato.
- Invoke legge sul thread del gioco; l’attesa rispetta l’annullamento dello script. Nessun pacchetto, richiesta status, target, modifica o ritardo incorporato.
- Ogni chiamata rilegge i dati locali. Le variabili conservano istantanee; letture separate possono vedere aggiornamenti diversi. Un risultato non zero non verifica la connessione; zero può essere un valore o dati assenti.
- Nomi equivalenti con e senza UO., senza distinzione tra maiuscole e minuscole: `Dex Dexterity GetDex GetDexterity`.
- Int(value) senza UO. arrotonda un numero BASIC verso il basso; Str(value) lo formatta in testo. Sono operazioni diverse dalle letture UO.Int()/UO.Str(). GetInt(ObjID) non arrotonda un numero.
- ExecuteStealthCompatibility.Arg risolve il nome prima della conversione numerica. Un testo sconosciuto non numerico causa errore, non un target. Decimal viene convertito in Integer, Array/Unit in 0. Usare un serial valido.

### Funzioni interne: dalla chiamata al risultato

Passaggi nativi di lettura. AttributeAtLeast è la funzione BASIC utente completa riportata sotto, non un’API nascosta o una modifica di attributo.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases aggiunge funzioni senza argomenti e nomi intrinseci mancanti. I rami di compatibilità esistenti scelgono il getter; entrambi restituiscono Integer. L’intrinseco viene riletto salvo una variabile che lo nasconda.

Nomi equivalenti con e senza UO., senza distinzione tra maiuscole e minuscole: `Dex Dexterity GetDex GetDexterity`.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `RegisterCharacterGetterAliases`.

#### 2. ExecuteStealthCompatibility

ObjID solo nella forma con un argomento: serial intero, stringa decimale/esadecimale 0x, "self", "lasttarget" o nome AddObject. Identifica il personaggio, non graphic/type. Senza argomento legge il giocatore attuale.

ExecuteStealthCompatibility.Arg risolve il nome prima della conversione numerica. Un testo sconosciuto non numerico causa errore, non un target. Decimal viene convertito in Integer, Array/Unit in 0. Usare un serial valido.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `ExecuteStealthCompatibility`.

#### 3. GetDexterity

GetStr/GetInt/GetDex accettano ObjID, ma questi attributi sono memorizzati solo su PlayerMobile: ogni altro serial dà 0, anche per un mobile caricato. Limite rispetto alla descrizione generica Stealth; nessun valore remoto viene inventato.

Legge Player.Dexterity se Player esiste e non è distrutto, altrimenti 0. Un personaggio morto presente non è un oggetto distrutto. Nessun calcolo da HP, mana o stamina.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `GetDexterity`.

#### 4. Invoke

Legge Player.Dexterity se Player esiste e non è distrutto, altrimenti 0. Un personaggio morto presente non è un oggetto distrutto. Nessun calcolo da HP, mana o stamina. Invoke legge sul thread del gioco; l’attesa rispetta l’annullamento dello script. Nessun pacchetto, richiesta status, target, modifica o ritardo incorporato.

Integer — punti attuali, 0..65535 nel modello; non percentuale, ID, abilità, blocco o Boolean. 0 può indicare anche giocatore assente/distrutto o soggetto non disponibile. Confrontare con una soglia numerica, non = TRUE. Non è il limite né necessariamente il valore base senza modificatori. Ogni chiamata rilegge i dati locali. Le variabili conservano istantanee; letture separate possono vedere aggiornamenti diversi. Un risultato non zero non verifica la connessione; zero può essere un valore o dati assenti.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 5. CharacterStatus

CharacterStatus assegna il campo STR/DEX/INT ricevuto a Player.Dexterity per un pacchetto status personale applicabile. La query legge questa cache senza attendere un nuovo pacchetto.

Invoke legge sul thread del gioco; l’attesa rispetta l’annullamento dello script. Nessun pacchetto, richiesta status, target, modifica o ritardo incorporato.

Sorgente del progetto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; funzione `CharacterStatus`.

#### 6. Clear

World.Clear rimuove Player. Le letture danno 0 finché giocatore e dati non tornano disponibili. Un valore salvato non prova il requisito dopo una riconnessione.

Integer — punti attuali, 0..65535 nel modello; non percentuale, ID, abilità, blocco o Boolean. 0 può indicare anche giocatore assente/distrutto o soggetto non disponibile. Confrontare con una soglia numerica, non = TRUE. Non è il limite né necessariamente il valore base senza modificatori.

Sorgente del progetto: `src/ClassicUO.Client/Game/World.cs`; funzione `Clear`.

World.Clear rimuove Player. Le letture danno 0 finché giocatore e dati non tornano disponibili. Un valore salvato non prova il requisito dopo una riconnessione.


## Esempi

### Mostrare i punti

```vb
# Mostrare i punti
#
# Legge la Destrezza attuale (Dexterity, DEX).
#
# Integer — punti attuali, 0..65535 nel modello; non percentuale, ID, abilità, blocco o Boolean.
# 0 può indicare anche giocatore assente/distrutto o soggetto non disponibile. Confrontare con
# una soglia numerica, non = TRUE. Non è il limite né necessariamente il valore base senza
# modificatori.

SUB Main()
    # value conserva il numero; CStr lo formatta per il diario. Nessun argomento né azione del
    # personaggio.

    VAR value = UO.GetDex()
    UO.Print('Dexterity: ' + CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- value conserva il numero; CStr lo formatta per il diario. Nessun argomento né azione del personaggio.

### Confrontare due osservazioni

```vb
# Confrontare due osservazioni
#
# Legge la Destrezza attuale (Dexterity, DEX).
#
# Integer — punti attuali, 0..65535 nel modello; non percentuale, ID, abilità, blocco o Boolean.
# 0 può indicare anche giocatore assente/distrutto o soggetto non disponibile. Confrontare con
# una soglia numerica, non = TRUE. Non è il limite né necessariamente il valore base senza
# modificatori.

SUB Main()
    # before/after distano 1000 ms; WAIT è nell’esempio. change=after-before può essere positivo,
    # zero o negativo; da solo non distingue tutti gli aggiornamenti intermedi o una disconnessione.

    VAR before = UO.GetDex()
    WAIT(1000)
    VAR after = UO.GetDex()
    VAR change = after - before
    UO.Print('Change: ' + CStr(change))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- before/after distano 1000 ms; WAIT è nell’esempio. change=after-before può essere positivo, zero o negativo; da solo non distingue tutti gli aggiornamenti intermedi o una disconnessione.

### Funzione completa per il requisito

```vb
# Funzione completa per il requisito
#
# Legge la Destrezza attuale (Dexterity, DEX).
#
# Integer — punti attuali, 0..65535 nel modello; non percentuale, ID, abilità, blocco o Boolean.
# 0 può indicare anche giocatore assente/distrutto o soggetto non disponibile. Confrontare con
# una soglia numerica, non = TRUE. Non è il limite né necessariamente il valore base senza
# modificatori.

SUB Main()
    # minimum=80 è un requisito d’esempio. AttributeAtLeast(minimum) rifiuta il giocatore assente,
    # legge una volta e restituisce Integer Boolean 1=TRUE o 0=FALSE per >= minimum. Il confronto è
    # logico, non l’attributo.

    IF AttributeAtLeast(80) = TRUE THEN
        UO.Print('Requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB AttributeAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetDex()
    RETURN value >= minimum
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- minimum=80 è un requisito d’esempio. AttributeAtLeast(minimum) rifiuta il giocatore assente, legge una volta e restituisce Integer Boolean 1=TRUE o 0=FALSE per >= minimum. Il confronto è logico, non l’attributo.

### Scegliere tramite serial e nome

```vb
# Scegliere tramite serial e nome
#
# Legge la Destrezza attuale (Dexterity, DEX).
#
# Integer — punti attuali, 0..65535 nel modello; non percentuale, ID, abilità, blocco o Boolean.
# 0 può indicare anche giocatore assente/distrutto o soggetto non disponibile. Confrontare con
# una soglia numerica, non = TRUE. Non è il limite né necessariamente il valore base senza
# modificatori.

SUB Main()
    # id proviene da UO.Self(), non è type. AddObject salva statSubject senza target perché riceve
    # il secondo argomento. Le due chiamate scelgono lo stesso soggetto, ma le letture non sono
    # atomiche.

    VAR id = UO.Self()
    IF id <> 0 THEN
        UO.AddObject('statSubject', id)
        VAR direct = UO.GetDex(id)
        VAR byName = UO.GetDex('statSubject')
        UO.Print('Direct: ' + CStr(direct) + '; alias: ' + CStr(byName))
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- id proviene da UO.Self(), non è type. AddObject salva statSubject senza target perché riceve il secondo argomento. Le due chiamate scelgono lo stesso soggetto, ma le letture non sono atomiche.
