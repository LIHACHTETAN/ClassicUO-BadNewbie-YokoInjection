# UO.SetStatState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Richiede una modifica alla modalità di crescita dell’attributo.

## Sintassi esatta

```text
UO.SetStatState(statNum:Any, statState:Any) -> Unit
```

## Parametri

- `statNum` — Numero obbligatorio dell’attributo: 0 — STR, 1 — DEX, 2 — INT. Non il valore attuale né il nome testuale.
- `statState` — Modalità obbligatoria: 0 — aumento, 1 — diminuzione, 2 — bloccato. Tre codici, non Boolean; true/false non descrivono tutte le modalità.

## Restituisce

Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del server.

## Comportamento

- Una richiesta valida invia un pacchetto tramite GameActions e cambia subito la modalità locale. Restano valide le regole del server; la crescita non è garantita. Abilità sconosciute, indici/modalità non validi e personaggio assente sono ignorati senza pacchetto.
- Numero obbligatorio dell’attributo: 0 — STR, 1 — DEX, 2 — INT. Non il valore attuale né il nome testuale.
- ExecuteStealthCompatibility sceglie il ramo. Text legge il selettore abilità; Arg legge numeri e modalità. Un argomento non convertibile può causare un errore di conversione.

### Funzioni interne: dalla chiamata al risultato

Queste sono le vere fasi interne C#. ApplyMode è una funzione ausiliaria completamente definita nell’esempio, non un comando integrato nascosto.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility sceglie il ramo. Text legge il selettore abilità; Arg legge numeri e modalità. Un argomento non convertibile può causare un errore di conversione.

Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del server.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke legge nel thread del gioco; un thread di lavoro attende l’elaborazione del gestore. L’annullamento dello script interrompe l’attesa. Nessun ritardo o richiesta di rete aggiuntivi.

Una richiesta valida invia un pacchetto tramite GameActions e cambia subito la modalità locale. Restano valide le regole del server; la crescita non è garantita. Abilità sconosciute, indici/modalità non validi e personaggio assente sono ignorati senza pacchetto.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 3. SetStatLockState

GetStatLockState/SetStatLockState scelgono StrLock, DexLock o IntLock tramite 0/1/2. Un numero sconosciuto legge −1; la scrittura verifica entrambi i limiti prima dell’invio.

Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del server.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `SetStatLockState`.

#### 4. ChangeStatLock

Una richiesta valida invia un pacchetto tramite GameActions e cambia subito la modalità locale. Restano valide le regole del server; la crescita non è garantita. Abilità sconosciute, indici/modalità non validi e personaggio assente sono ignorati senza pacchetto.

Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del server.

Sorgente del progetto: `src/ClassicUO.Client/Game/GameActions.cs`; funzione `ChangeStatLock`.

Una richiesta valida invia un pacchetto tramite GameActions e cambia subito la modalità locale. Restano valide le regole del server; la crescita non è garantita. Abilità sconosciute, indici/modalità non validi e personaggio assente sono ignorati senza pacchetto.


## Esempi

### Leggere e mostrare

```vb
# Leggere e mostrare
#
# Richiede una modifica alla modalità di crescita dell’attributo.
#
# Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né
# confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del
# server.

SUB Main()
    # L’esempio imposta selector e, in scrittura, mode. La prima riga sceglie l’abilità per nome o
    # l’attributo per numero. Print mostra soltanto il risultato.

    VAR selector = 0
    VAR mode = 2
    UO.SetStatState(selector, mode)
    UO.Print(CStr(UO.GetStatLockState(selector)))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- L’esempio imposta selector e, in scrittura, mode. La prima riga sceglie l’abilità per nome o l’attributo per numero. Print mostra soltanto il risultato.

### Usare in una condizione o confronto

```vb
# Usare in una condizione o confronto
#
# Richiede una modifica alla modalità di crescita dell’attributo.
#
# Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né
# confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del
# server.

SUB Main()
    # Soglia 95.1 e modalità 0/1/2 sono impostazioni di esempio. Verificare −1 prima di modificare
    # la modalità. La lettura dopo la scrittura mostra la copia locale senza attendere il server.

    VAR selector = 0
    VAR before = UO.GetStatLockState(selector)
    IF before >= 0 AND before <= 2 THEN
        UO.SetStatState(selector, 0)
        UO.Print(CStr(UO.GetStatLockState(selector)))
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Soglia 95.1 e modalità 0/1/2 sono impostazioni di esempio. Verificare −1 prima di modificare la modalità. La lettura dopo la scrittura mostra la copia locale senza attendere il server.

### Funzione ausiliaria completa

```vb
# Funzione ausiliaria completa
#
# Richiede una modifica alla modalità di crescita dell’attributo.
#
# Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né
# confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del
# server.

SUB Main()
    # La funzione completa segue Main. selector sceglie abilità/attributo; mode indica la modalità.
    # ReadValue/ReadMode restituiscono il numero originale; ApplyMode verifica gli argomenti, agisce
    # e non restituisce valori. WAIT(1000) separa due letture.

    ApplyMode(0, 2)
END SUB

SUB ApplyMode(selector, mode)
    IF mode < 0 OR mode > 2 THEN
        RETURN
    END IF
    IF UO.GetStatLockState(selector) < 0 THEN
        RETURN
    END IF
    UO.SetStatState(selector, mode)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- La funzione completa segue Main. selector sceglie abilità/attributo; mode indica la modalità. ReadValue/ReadMode restituiscono il numero originale; ApplyMode verifica gli argomenti, agisce e non restituisce valori. WAIT(1000) separa due letture.
