# UO.Gold

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge la quantità d’oro riportata nello status del giocatore attuale.

## Sintassi esatta

```text
UO.Gold() -> Any
```

## Parametri

Nessun parametro.

## Restituisce

Integer/Decimal — importo non negativo 0..4294967295. Fino a 2147483647 è Integer; oltre è Decimal (Double), che rappresenta esattamente tutti gli UInt32. 0 può indicare Player assente/distrutto o importo sconosciuto. Non è Boolean, ID, numero di pile né scansione di zaino/banca.

## Comportamento

- Nessun argomento. Legge Player.Gold memorizzato da CharacterStatus (0x11). Il server decide cosa include il contatore. Non percorre borse né richiede il saldo bancario. Player assente/distrutto dà 0; un fantasma presente può conservare l’importo.
- ReadGoldValue legge bridge.Gold una volta. Il bridge C# conserva Int32 e trasporta i bit UInt32. La conversione unchecked ripristina l’importo senza segno: piccoli valori Integer, grandi Decimal. Il bit alto non rende più negativo il saldo. Conversione locale senza pacchetti.
- Conservare il risultato numerico per confrontare grandi importi. CInt/CLng convertono in Integer a 32 bit. Scrivere i grandi letterali BASIC con un punto, ad esempio 3000000000.0. Il saldo può cambiare prima dell’acquisto; CanAfford è un controllo locale, non un permesso del server.
- Ogni chiamata rilegge i dati locali. Le variabili conservano istantanee; letture separate possono vedere aggiornamenti diversi. Un risultato non zero non verifica la connessione; zero può essere un valore o dati assenti.

### Funzioni interne: dalla chiamata al risultato

Passaggi nativi del contatore status e dell’estensione senza segno. CanAfford è la funzione BASIC utente completa sotto, non un comando d’acquisto nascosto.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases aggiunge Gold/GetGold e intrinseci mancanti. Il ramo UO.Gold e il suo intrinseco usano lo stesso ReadGoldValue. I nomi intrinseci vengono riletti salvo variabili che li nascondano.

Integer/Decimal — importo non negativo 0..4294967295. Fino a 2147483647 è Integer; oltre è Decimal (Double), che rappresenta esattamente tutti gli UInt32. 0 può indicare Player assente/distrutto o importo sconosciuto. Non è Boolean, ID, numero di pile né scansione di zaino/banca.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `RegisterCharacterGetterAliases`.

#### 2. ReadGoldValue

ReadGoldValue legge bridge.Gold una volta. Il bridge C# conserva Int32 e trasporta i bit UInt32. La conversione unchecked ripristina l’importo senza segno: piccoli valori Integer, grandi Decimal. Il bit alto non rende più negativo il saldo. Conversione locale senza pacchetti.

Conservare il risultato numerico per confrontare grandi importi. CInt/CLng convertono in Integer a 32 bit. Scrivere i grandi letterali BASIC con un punto, ad esempio 3000000000.0. Il saldo può cambiare prima dell’acquisto; CanAfford è un controllo locale, non un permesso del server.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `ReadGoldValue`.

#### 3. Invoke

Nessun argomento. Legge Player.Gold memorizzato da CharacterStatus (0x11). Il server decide cosa include il contatore. Non percorre borse né richiede il saldo bancario. Player assente/distrutto dà 0; un fantasma presente può conservare l’importo.

Invoke legge sul thread del gioco; l’attesa rispetta l’annullamento dello script. Nessun pacchetto, richiesta status, target, modifica o ritardo incorporato.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 4. CharacterStatus

Nessun argomento. Legge Player.Gold memorizzato da CharacterStatus (0x11). Il server decide cosa include il contatore. Non percorre borse né richiede il saldo bancario. Player assente/distrutto dà 0; un fantasma presente può conservare l’importo.

Ogni chiamata rilegge i dati locali. Le variabili conservano istantanee; letture separate possono vedere aggiornamenti diversi. Un risultato non zero non verifica la connessione; zero può essere un valore o dati assenti.

Sorgente del progetto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; funzione `CharacterStatus`.

#### 5. Clear

World.Clear rimuove Player. Le letture danno 0 finché giocatore e dati non tornano disponibili. Un valore salvato non prova il requisito dopo una riconnessione.

Integer/Decimal — importo non negativo 0..4294967295. Fino a 2147483647 è Integer; oltre è Decimal (Double), che rappresenta esattamente tutti gli UInt32. 0 può indicare Player assente/distrutto o importo sconosciuto. Non è Boolean, ID, numero di pile né scansione di zaino/banca.

Sorgente del progetto: `src/ClassicUO.Client/Game/World.cs`; funzione `Clear`.

Ogni chiamata rilegge i dati locali. Le variabili conservano istantanee; letture separate possono vedere aggiornamenti diversi. Un risultato non zero non verifica la connessione; zero può essere un valore o dati assenti.


## Esempi

### Mostrare l’importo ricevuto

```vb
# Mostrare l’importo ricevuto
#
# Legge la quantità d’oro riportata nello status del giocatore attuale.
#
# Integer/Decimal — importo non negativo 0..4294967295. Fino a 2147483647 è Integer; oltre è
# Decimal (Double), che rappresenta esattamente tutti gli UInt32. 0 può indicare Player
# assente/distrutto o importo sconosciuto. Non è Boolean, ID, numero di pile né scansione di
# zaino/banca.

SUB Main()
    # amount conserva una query; CStr formatta per il diario. Non cerca, sposta o spende oro.

    VAR amount = UO.Gold()
    UO.Print('Status gold: ' + CStr(amount))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- amount conserva una query; CStr formatta per il diario. Non cerca, sposta o spende oro.

### CanAfford completo con prezzo elevato

```vb
# CanAfford completo con prezzo elevato
#
# Legge la quantità d’oro riportata nello status del giocatore attuale.
#
# Integer/Decimal — importo non negativo 0..4294967295. Fino a 2147483647 è Integer; oltre è
# Decimal (Double), che rappresenta esattamente tutti gli UInt32. 0 può indicare Player
# assente/distrutto o importo sconosciuto. Non è Boolean, ID, numero di pile né scansione di
# zaino/banca.

SUB Main()
    # price=3000000000.0 è un prezzo d’esempio. CanAfford(price) rifiuta prezzo negativo o Player
    # assente, legge una volta e restituisce Integer Boolean 1=TRUE o 0=FALSE per amount >= price.
    # L’importo non è Boolean. Funzione completa sotto.

    VAR price = 3000000000.0
    IF CanAfford(price) = TRUE THEN
        UO.Print('Local balance is sufficient')
    ELSE
        UO.Print('Local check failed')
    END IF
END SUB

SUB CanAfford(price)
    IF price < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR amount = UO.Gold()
    RETURN amount >= price
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- price=3000000000.0 è un prezzo d’esempio. CanAfford(price) rifiuta prezzo negativo o Player assente, legge una volta e restituisce Integer Boolean 1=TRUE o 0=FALSE per amount >= price. L’importo non è Boolean. Funzione completa sotto.

### Osservare la variazione del saldo

```vb
# Osservare la variazione del saldo
#
# Legge la quantità d’oro riportata nello status del giocatore attuale.
#
# Integer/Decimal — importo non negativo 0..4294967295. Fino a 2147483647 è Integer; oltre è
# Decimal (Double), che rappresenta esattamente tutti gli UInt32. 0 può indicare Player
# assente/distrutto o importo sconosciuto. Non è Boolean, ID, numero di pile né scansione di
# zaino/banca.

SUB Main()
    # before/after sono separati da WAIT(500) millisecondi. difference=after-before può essere
    # negativo quando il saldo diminuisce; non è l’overflow senza segno corretto. Aggiornamenti o
    # cambi di personaggio intermedi possono sfuggire.

    VAR before = UO.Gold()
    WAIT(500)
    VAR after = UO.Gold()
    VAR difference = after - before
    UO.Print('Balance change: ' + CStr(difference))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- before/after sono separati da WAIT(500) millisecondi. difference=after-before può essere negativo quando il saldo diminuisce; non è l’overflow senza segno corretto. Aggiornamenti o cambi di personaggio intermedi possono sfuggire.
