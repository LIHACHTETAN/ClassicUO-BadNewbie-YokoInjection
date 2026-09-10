# UO.GetSkillLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge la modalità locale di crescita dell’abilità.

## Sintassi esatta

```text
UO.GetSkillLockState(SkillName:Any) -> Integer
```

## Parametri

- `SkillName` — Abilità obbligatoria: nome dei dati client, come "Mining" o "Animal Lore", oppure indice decimale 0..Skills.Length−1 come numero o stringa. Ignora maiuscole/minuscole, elimina spazi esterni e sostituisce _ con uno spazio. Non è un ID oggetto né un indice da 1. Una stringa numerica indica sempre un indice.

## Restituisce

Integer: 0 — aumento, 1 — diminuzione, 2 — bloccato. Codice di modalità, non true/false. Abilità sconosciuta o personaggio assente restituisce −1.

## Comportamento

- Invoke legge dati esistenti sul thread del gioco senza pacchetti di rete. Non usa né allena l’abilità. Due letture sono istantanee separate.
- Abilità obbligatoria: nome dei dati client, come "Mining" o "Animal Lore", oppure indice decimale 0..Skills.Length−1 come numero o stringa. Ignora maiuscole/minuscole, elimina spazi esterni e sostituisce _ con uno spazio. Non è un ID oggetto né un indice da 1. Una stringa numerica indica sempre un indice.
- ExecuteStealthCompatibility sceglie il ramo. Text legge il selettore abilità; Arg legge numeri e modalità. Un argomento non convertibile può causare un errore di conversione.

### Funzioni interne: dalla chiamata al risultato

Queste sono le vere fasi interne C#. ReadMode è una funzione ausiliaria completamente definita nell’esempio, non un comando integrato nascosto.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility sceglie il ramo. Text legge il selettore abilità; Arg legge numeri e modalità. Un argomento non convertibile può causare un errore di conversione.

Integer: 0 — aumento, 1 — diminuzione, 2 — bloccato. Codice di modalità, non true/false. Abilità sconosciuta o personaggio assente restituisce −1.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke legge nel thread del gioco; un thread di lavoro attende l’elaborazione del gestore. L’annullamento dello script interrompe l’attesa. Nessun ritardo o richiesta di rete aggiuntivi.

Invoke legge dati esistenti sul thread del gioco senza pacchetti di rete. Non usa né allena l’abilità. Due letture sono istantanee separate.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 3. FindSkillUnsafe

FindSkillUnsafe verifica prima l’indice decimale e i limiti; altrimenti normalizza il nome e confronta esattamente Skill.Name ignorando maiuscole/minuscole. Un nome sconosciuto produce null; non apre il bersaglio.

Abilità sconosciuta o personaggio assente restituisce −1.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `FindSkillUnsafe`.

#### 4. GetSkillLockState

Legge la modalità locale di crescita dell’abilità.

Integer: 0 — aumento, 1 — diminuzione, 2 — bloccato. Codice di modalità, non true/false. Abilità sconosciuta o personaggio assente restituisce −1.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `GetSkillLockState`.

Invoke legge dati esistenti sul thread del gioco senza pacchetti di rete. Non usa né allena l’abilità. Due letture sono istantanee separate.


## Esempi

### Leggere e mostrare

```vb
# Leggere e mostrare
#
# Legge la modalità locale di crescita dell’abilità.
#
# Integer: 0 — aumento, 1 — diminuzione, 2 — bloccato. Codice di modalità, non true/false.
# Abilità sconosciuta o personaggio assente restituisce −1.

SUB Main()
    # L’esempio imposta selector e, in scrittura, mode. La prima riga sceglie l’abilità per nome o
    # l’attributo per numero. Print mostra soltanto il risultato.

    VAR selector = 'Mining'
    VAR mode = UO.GetSkillLockState(selector)
    UO.Print(CStr(mode))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- L’esempio imposta selector e, in scrittura, mode. La prima riga sceglie l’abilità per nome o l’attributo per numero. Print mostra soltanto il risultato.

### Usare in una condizione o confronto

```vb
# Usare in una condizione o confronto
#
# Legge la modalità locale di crescita dell’abilità.
#
# Integer: 0 — aumento, 1 — diminuzione, 2 — bloccato. Codice di modalità, non true/false.
# Abilità sconosciuta o personaggio assente restituisce −1.

SUB Main()
    # Soglia 95.1 e modalità 0/1/2 sono impostazioni di esempio. Verificare −1 prima di modificare
    # la modalità. La lettura dopo la scrittura mostra la copia locale senza attendere il server.

    VAR mode = UO.GetSkillLockState('Mining')
    IF mode = 2 THEN
        UO.Print("Locked")
    ELSE
        IF mode = -1 THEN
            UO.Print("Unknown selector")
        ELSE
            UO.Print("Mode: " + CStr(mode))
        END IF
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Soglia 95.1 e modalità 0/1/2 sono impostazioni di esempio. Verificare −1 prima di modificare la modalità. La lettura dopo la scrittura mostra la copia locale senza attendere il server.

### Funzione ausiliaria completa

```vb
# Funzione ausiliaria completa
#
# Legge la modalità locale di crescita dell’abilità.
#
# Integer: 0 — aumento, 1 — diminuzione, 2 — bloccato. Codice di modalità, non true/false.
# Abilità sconosciuta o personaggio assente restituisce −1.

SUB Main()
    # La funzione completa segue Main. selector sceglie abilità/attributo; mode indica la modalità.
    # ReadValue/ReadMode restituiscono il numero originale; ApplyMode verifica gli argomenti, agisce
    # e non restituisce valori. WAIT(1000) separa due letture.

    VAR before = ReadMode('Mining')
    WAIT(1000)
    VAR after = ReadMode('Mining')
    UO.Print(CStr(before) + " -> " + CStr(after))
END SUB

SUB ReadMode(selector)
    RETURN UO.GetSkillLockState(selector)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- La funzione completa segue Main. selector sceglie abilità/attributo; mode indica la modalità. ReadValue/ReadMode restituiscono il numero originale; ApplyMode verifica gli argomenti, agisce e non restituisce valori. WAIT(1000) separa due letture.
