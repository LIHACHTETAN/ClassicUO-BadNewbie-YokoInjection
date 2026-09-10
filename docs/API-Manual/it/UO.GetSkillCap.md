# UO.GetSkillCap

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge il limite dell’abilità ricevuto dal server.

## Sintassi esatta

```text
UO.GetSkillCap(SkillName:Any) -> Decimal
```

## Parametri

- `SkillName` — Abilità obbligatoria: nome dei dati client, come "Mining" o "Animal Lore", oppure indice decimale 0..Skills.Length−1 come numero o stringa. Ignora maiuscole/minuscole, elimina spazi esterni e sostituisce _ con uno spazio. Non è un ID oggetto né un indice da 1. Una stringa numerica indica sempre un indice.

## Restituisce

Decimal (Double) — punti abilità in decimi, per esempio 95,1 invece di 951. Il campo CapFixed viene diviso direttamente per 10 in Double. Zero indica abilità nulla o personaggio/abilità assente. Non Boolean. Le vecchie SkillVal/BaseVal usano una scala diversa; non confondere le famiglie.

## Comportamento

- Invoke legge dati esistenti sul thread del gioco senza pacchetti di rete. Non usa né allena l’abilità. Due letture sono istantanee separate.
- Abilità obbligatoria: nome dei dati client, come "Mining" o "Animal Lore", oppure indice decimale 0..Skills.Length−1 come numero o stringa. Ignora maiuscole/minuscole, elimina spazi esterni e sostituisce _ con uno spazio. Non è un ID oggetto né un indice da 1. Una stringa numerica indica sempre un indice.
- ExecuteStealthCompatibility sceglie il ramo. Text legge il selettore abilità; Arg legge numeri e modalità. Un argomento non convertibile può causare un errore di conversione.

### Funzioni interne: dalla chiamata al risultato

Queste sono le vere fasi interne C#. ReadValue è una funzione ausiliaria completamente definita nell’esempio, non un comando integrato nascosto.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility sceglie il ramo. Text legge il selettore abilità; Arg legge numeri e modalità. Un argomento non convertibile può causare un errore di conversione.

Decimal (Double) — punti abilità in decimi, per esempio 95,1 invece di 951. Il campo CapFixed viene diviso direttamente per 10 in Double. Zero indica abilità nulla o personaggio/abilità assente. Non Boolean. Le vecchie SkillVal/BaseVal usano una scala diversa; non confondere le famiglie.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke legge nel thread del gioco; un thread di lavoro attende l’elaborazione del gestore. L’annullamento dello script interrompe l’attesa. Nessun ritardo o richiesta di rete aggiuntivi.

Invoke legge dati esistenti sul thread del gioco senza pacchetti di rete. Non usa né allena l’abilità. Due letture sono istantanee separate.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 3. FindSkillUnsafe

FindSkillUnsafe verifica prima l’indice decimale e i limiti; altrimenti normalizza il nome e confronta esattamente Skill.Name ignorando maiuscole/minuscole. Un nome sconosciuto produce null; non apre il bersaglio.

Abilità sconosciuta o personaggio assente restituisce −1.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `FindSkillUnsafe`.

#### 4. GetSkillValue

GetSkillValue sceglie BaseFixed, ValueFixed o CapFixed e divide i decimi interi per 10d, senza arrotondamento intermedio in Single.

Decimal (Double) — punti abilità in decimi, per esempio 95,1 invece di 951. Il campo CapFixed viene diviso direttamente per 10 in Double. Zero indica abilità nulla o personaggio/abilità assente. Non Boolean. Le vecchie SkillVal/BaseVal usano una scala diversa; non confondere le famiglie.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `GetSkillValue`.

Invoke legge dati esistenti sul thread del gioco senza pacchetti di rete. Non usa né allena l’abilità. Due letture sono istantanee separate.


## Esempi

### Leggere e mostrare

```vb
# Leggere e mostrare
#
# Legge il limite dell’abilità ricevuto dal server.
#
# Decimal (Double) — punti abilità in decimi, per esempio 95,1 invece di 951. Il campo CapFixed
# viene diviso direttamente per 10 in Double. Zero indica abilità nulla o personaggio/abilità
# assente. Non Boolean. Le vecchie SkillVal/BaseVal usano una scala diversa; non confondere le
# famiglie.

SUB Main()
    # L’esempio imposta selector e, in scrittura, mode. La prima riga sceglie l’abilità per nome o
    # l’attributo per numero. Print mostra soltanto il risultato.

    VAR selector = 'Mining'
    VAR value = UO.GetSkillCap(selector)
    UO.Print(CStr(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- L’esempio imposta selector e, in scrittura, mode. La prima riga sceglie l’abilità per nome o l’attributo per numero. Print mostra soltanto il risultato.

### Usare in una condizione o confronto

```vb
# Usare in una condizione o confronto
#
# Legge il limite dell’abilità ricevuto dal server.
#
# Decimal (Double) — punti abilità in decimi, per esempio 95,1 invece di 951. Il campo CapFixed
# viene diviso direttamente per 10 in Double. Zero indica abilità nulla o personaggio/abilità
# assente. Non Boolean. Le vecchie SkillVal/BaseVal usano una scala diversa; non confondere le
# famiglie.

SUB Main()
    # Soglia 95.1 e modalità 0/1/2 sono impostazioni di esempio. Verificare −1 prima di modificare
    # la modalità. La lettura dopo la scrittura mostra la copia locale senza attendere il server.

    IF UO.GetSkillLockState('Mining') >= 0 THEN
        VAR value = UO.GetSkillCap('Mining')
        IF value >= 95.1 THEN
            UO.Print('Value >= 95.1: ' + CStr(value))
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
# Legge il limite dell’abilità ricevuto dal server.
#
# Decimal (Double) — punti abilità in decimi, per esempio 95,1 invece di 951. Il campo CapFixed
# viene diviso direttamente per 10 in Double. Zero indica abilità nulla o personaggio/abilità
# assente. Non Boolean. Le vecchie SkillVal/BaseVal usano una scala diversa; non confondere le
# famiglie.

SUB Main()
    # La funzione completa segue Main. selector sceglie abilità/attributo; mode indica la modalità.
    # ReadValue/ReadMode restituiscono il numero originale; ApplyMode verifica gli argomenti, agisce
    # e non restituisce valori. WAIT(1000) separa due letture.

    VAR before = ReadValue('Animal_Lore')
    WAIT(1000)
    VAR after = ReadValue('Animal Lore')
    UO.Print(CStr(after - before))
END SUB

SUB ReadValue(selector)
    RETURN UO.GetSkillCap(selector)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- La funzione completa segue Main. selector sceglie abilità/attributo; mode indica la modalità. ReadValue/ReadMode restituiscono il numero originale; ApplyMode verifica gli argomenti, agisce e non restituisce valori. WAIT(1000) separa due letture.
