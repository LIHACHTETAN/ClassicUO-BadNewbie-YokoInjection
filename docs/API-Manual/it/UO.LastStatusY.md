# UO.LastStatusY

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Restituisce la coordinata Y salvata dell’ultimo oggetto con stato accettato.

## Sintassi esatta

```text
UO.LastStatusY() -> Integer
```

## Parametri

Nessun parametro.

## Restituisce

Integer — coordinata Y salvata, non pixel della finestra né Boolean. 0 prima del primo stato o dopo l’azzeramento; zero è anche una coordinata valida. Usare UO.LastStatus() per distinguere un record assente.

## Comportamento

- Nessun parametro. Leggere non invia pacchetti, non apre finestre e non attende risposte. UO.GetStatus(id), RequestStats e UpdateObject richiedono dati; l’invio non cambia LastStatus.
- Un pacchetto 0x11 accettato salva insieme serial e X/Y noti in World, condiviso dagli script. Oggetti sconosciuti/distrutti e pacchetti base incompleti non sostituiscono il record. Uno stato successivo di un altro oggetto può sostituirlo.
- X/Y fotografano Entity alla ricezione, non la posizione attuale. Per i mobile sono celle del mondo; un oggetto dentro un contenitore può avere coordinate del contenuto. Il pacchetto di stato non contiene X/Y. Movimento/rimozione successivi non cambiano il dato; World.Clear lo azzera. GetX/GetY leggono la posizione attuale di un oggetto presente.
- Chiamate separate non sono atomiche: può arrivare un aggiornamento intermedio. Lo stesso serial non dimostra una nuova risposta alla propria richiesta. laststatus senza parentesi è un valore intrinseco dinamico, salvo una variabile omonima; UO.LastStatus() è la funzione registrata.

### Funzioni interne: dalla chiamata al risultato

Queste sono le vere fasi interne C#. ReadSavedStatus è una funzione ausiliaria completamente definita nell’esempio, non un comando integrato nascosto.

#### 1. CharacterStatus

CharacterStatus valida il pacchetto base ed Entity tramite World.Get, aggiorna lo stato e salva serial/X/Y. La posizione viene da Entity, non dal pacchetto.

Integer — coordinata Y salvata, non pixel della finestra né Boolean. 0 prima del primo stato o dopo l’azzeramento; zero è anche una coordinata valida. Usare UO.LastStatus() per distinguere un record assente.

Sorgente del progetto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; funzione `CharacterStatus`.

#### 2. LastStatusY

ExecuteStealthCompatibility restituisce il serial del bridge come Integer. LastStatusX/LastStatusY usano IStatusSnapshotBridge; un vecchio bridge esterno senza questa interfaccia mantiene GetX/GetY.

Integer — coordinata Y salvata, non pixel della finestra né Boolean. 0 prima del primo stato o dopo l’azzeramento; zero è anche una coordinata valida. Usare UO.LastStatus() per distinguere un record assente.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `LastStatusY`.

#### 3. Invoke

Invoke legge World sul thread di gioco rispettando l’annullamento dello script. Non attende il server e non modifica lo stato.

Nessun parametro. Leggere non invia pacchetti, non apre finestre e non attende risposte. UO.GetStatus(id), RequestStats e UpdateObject richiedono dati; l’invio non cambia LastStatus.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 4. Clear

Clear azzera serial e coordinate anche quando conserva gli script in esecuzione.

X/Y fotografano Entity alla ricezione, non la posizione attuale. Per i mobile sono celle del mondo; un oggetto dentro un contenitore può avere coordinate del contenuto. Il pacchetto di stato non contiene X/Y. Movimento/rimozione successivi non cambiano il dato; World.Clear lo azzera. GetX/GetY leggono la posizione attuale di un oggetto presente.

Sorgente del progetto: `src/ClassicUO.Client/Game/World.cs`; funzione `Clear`.

Chiamate separate non sono atomiche: può arrivare un aggiornamento intermedio. Lo stesso serial non dimostra una nuova risposta alla propria richiesta. laststatus senza parentesi è un valore intrinseco dinamico, salvo una variabile omonima; UO.LastStatus() è la funzione registrata.


## Esempi

### Leggere l’ultimo valore

```vb
# Leggere l’ultimo valore
#
# Restituisce la coordinata Y salvata dell’ultimo oggetto con stato accettato.
#
# Integer — coordinata Y salvata, non pixel della finestra né Boolean. 0 prima del primo stato o
# dopo l’azzeramento; zero è anche una coordinata valida. Usare UO.LastStatus() per distinguere
# un record assente.

SUB Main()
    # Una lettura sola. HEX mostra il serial esadecimale; CStr mostra la coordinata numerica. Non
    # seleziona un oggetto.

    VAR value = UO.LastStatusY()
    UO.Print('Saved value: ' + CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Una lettura sola. HEX mostra il serial esadecimale; CStr mostra la coordinata numerica. Non seleziona un oggetto.

### Richiedere lo stato e leggere i dati noti

```vb
# Richiedere lo stato e leggere i dati noti
#
# Restituisce la coordinata Y salvata dell’ultimo oggetto con stato accettato.
#
# Integer — coordinata Y salvata, non pixel della finestra né Boolean. 0 prima del primo stato o
# dopo l’azzeramento; zero è anche una coordinata valida. Usare UO.LastStatus() per distinguere
# un record assente.

SUB Main()
    # subject è il serial di self. 500 è un’attesa di esempio in millisecondi, senza garanzia di
    # risposta. Il record può essere vecchio o riferirsi a un altro oggetto.

    VAR subject = UO.Self()
    IF subject <> 0 THEN
        UO.GetStatus(subject)
        WAIT(500)
        VAR value = UO.LastStatusY()
        UO.Print('Known value: ' + CStr(value))
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- subject è il serial di self. 500 è un’attesa di esempio in millisecondi, senza garanzia di risposta. Il record può essere vecchio o riferirsi a un altro oggetto.

### Funzione completa ReadSavedStatus

```vb
# Funzione completa ReadSavedStatus
#
# Restituisce la coordinata Y salvata dell’ultimo oggetto con stato accettato.
#
# Integer — coordinata Y salvata, non pixel della finestra né Boolean. 0 prima del primo stato o
# dopo l’azzeramento; zero è anche una coordinata valida. Usare UO.LastStatus() per distinguere
# un record assente.

SUB Main()
    # expectedId è il serial salvato in Main. La funzione è definita interamente sotto; -1 indica un
    # record non più selezionato, non il risultato della specifica API. I controlli prima/dopo
    # riducono la mescolanza di oggetti ma non garantiscono atomicità per aggiornamenti dello stesso
    # serial.

    VAR expectedId = UO.LastStatus()
    IF expectedId <> 0 THEN
        VAR value = ReadSavedStatus(expectedId)
        UO.Print('Checked value: ' + CStr(value))
    END IF
END SUB

SUB ReadSavedStatus(expectedId)
    IF expectedId = 0 OR UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    VAR value = UO.LastStatusY()
    IF UO.LastStatus() <> expectedId THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- expectedId è il serial salvato in Main. La funzione è definita interamente sotto; -1 indica un record non più selezionato, non il risultato della specifica API. I controlli prima/dopo riducono la mescolanza di oggetti ma non garantiscono atomicità per aggiornamenti dello stesso serial.
