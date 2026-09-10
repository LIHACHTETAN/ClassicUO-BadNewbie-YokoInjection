# UO.SkillLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Richiede una modifica alla modalità di crescita dell’abilità.

## Sintassi esatta

```text
UO.SkillLockState(SkillName:Any, skillState:Any) -> Unit
```

## Parametri

- `SkillName` — Abilità obbligatoria: nome dei dati client, come "Mining" o "Animal Lore", oppure indice decimale 0..Skills.Length−1 come numero o stringa. Ignora maiuscole/minuscole, elimina spazi esterni e sostituisce _ con uno spazio. Non è un ID oggetto né un indice da 1. Una stringa numerica indica sempre un indice.
- `skillState` — Modalità obbligatoria: 0 — aumento, 1 — diminuzione, 2 — bloccato. Tre codici, non Boolean; true/false non descrivono tutte le modalità.

## Restituisce

Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del server.

## Comportamento

- Una richiesta valida invia un pacchetto tramite GameActions e cambia subito la modalità locale. Restano valide le regole del server; la crescita non è garantita. Abilità sconosciute, indici/modalità non validi e personaggio assente sono ignorati senza pacchetto.
- Abilità obbligatoria: nome dei dati client, come "Mining" o "Animal Lore", oppure indice decimale 0..Skills.Length−1 come numero o stringa. Ignora maiuscole/minuscole, elimina spazi esterni e sostituisce _ con uno spazio. Non è un ID oggetto né un indice da 1. Una stringa numerica indica sempre un indice.
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

#### 3. FindSkillUnsafe

FindSkillUnsafe verifica prima l’indice decimale e i limiti; altrimenti normalizza il nome e confronta esattamente Skill.Name ignorando maiuscole/minuscole. Un nome sconosciuto produce null; non apre il bersaglio.

Abilità sconosciuta o personaggio assente restituisce −1.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `FindSkillUnsafe`.

#### 4. SetSkillLockState

Una richiesta valida invia un pacchetto tramite GameActions e cambia subito la modalità locale. Restano valide le regole del server; la crescita non è garantita. Abilità sconosciute, indici/modalità non validi e personaggio assente sono ignorati senza pacchetto.

Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del server.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `SetSkillLockState`.

#### 5. ChangeSkillLockStatus

Una richiesta valida invia un pacchetto tramite GameActions e cambia subito la modalità locale. Restano valide le regole del server; la crescita non è garantita. Abilità sconosciute, indici/modalità non validi e personaggio assente sono ignorati senza pacchetto.

Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del server.

Sorgente del progetto: `src/ClassicUO.Client/Game/GameActions.cs`; funzione `ChangeSkillLockStatus`.

Una richiesta valida invia un pacchetto tramite GameActions e cambia subito la modalità locale. Restano valide le regole del server; la crescita non è garantita. Abilità sconosciute, indici/modalità non validi e personaggio assente sono ignorati senza pacchetto.


## Esempi

### Leggere e mostrare

```vb
# Leggere e mostrare
#
# Richiede una modifica alla modalità di crescita dell’abilità.
#
# Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né
# confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del
# server.

SUB Main()
    # L’esempio imposta selector e, in scrittura, mode. La prima riga sceglie l’abilità per nome o
    # l’attributo per numero. Print mostra soltanto il risultato.

    VAR selector = 'Mining'
    VAR mode = 2
    UO.SkillLockState(selector, mode)
    UO.Print(CStr(UO.GetSkillLockState(selector)))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- L’esempio imposta selector e, in scrittura, mode. La prima riga sceglie l’abilità per nome o l’attributo per numero. Print mostra soltanto il risultato.

### Usare in una condizione o confronto

```vb
# Usare in una condizione o confronto
#
# Richiede una modifica alla modalità di crescita dell’abilità.
#
# Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né
# confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del
# server.

SUB Main()
    # Soglia 95.1 e modalità 0/1/2 sono impostazioni di esempio. Verificare −1 prima di modificare
    # la modalità. La lettura dopo la scrittura mostra la copia locale senza attendere il server.

    VAR selector = 'Mining'
    VAR before = UO.GetSkillLockState(selector)
    IF before >= 0 AND before <= 2 THEN
        UO.SkillLockState(selector, 0)
        UO.Print(CStr(UO.GetSkillLockState(selector)))
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Soglia 95.1 e modalità 0/1/2 sono impostazioni di esempio. Verificare −1 prima di modificare la modalità. La lettura dopo la scrittura mostra la copia locale senza attendere il server.

### Funzione ausiliaria completa

```vb
# Funzione ausiliaria completa
#
# Richiede una modifica alla modalità di crescita dell’abilità.
#
# Unit — nessun valore restituito. Non interpretare il risultato come successo/errore né
# confrontarlo con true. La lettura successiva mostra il modello locale, non una conferma del
# server.

SUB Main()
    # La funzione completa segue Main. selector sceglie abilità/attributo; mode indica la modalità.
    # ReadValue/ReadMode restituiscono il numero originale; ApplyMode verifica gli argomenti, agisce
    # e non restituisce valori. WAIT(1000) separa due letture.

    ApplyMode('Mining', 2)
END SUB

SUB ApplyMode(selector, mode)
    IF mode < 0 OR mode > 2 THEN
        RETURN
    END IF
    IF UO.GetSkillLockState(selector) < 0 THEN
        RETURN
    END IF
    UO.SkillLockState(selector, mode)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- La funzione completa segue Main. selector sceglie abilità/attributo; mode indica la modalità. ReadValue/ReadMode restituiscono il numero originale; ApplyMode verifica gli argomenti, agisce e non restituisce valori. WAIT(1000) separa due letture.
