# UO.GetHP

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge la salute attuale dal modello locale.

## Sintassi esatta

```text
UO.GetHP() -> Integer
UO.GetHP(ObjID:Any) -> Any
UO.GetHP(id:Integer) -> Integer
UO.GetHP(id:String) -> Integer
```

## Parametri

- `ObjID` — Oggetto facoltativo nelle forme mostrate: serial numerico/stringa esadecimale, self, lasttarget o nome AddObject registrato. Non è un type. Se omesso, legge self. Un testo sconosciuto causa un errore di conversione in alcune forme; verificare prima il nome.
- `id` — Oggetto facoltativo nelle forme mostrate: serial numerico/stringa esadecimale, self, lasttarget o nome AddObject registrato. Non è un type. Se omesso, legge self. Un testo sconosciuto causa un errore di conversione in alcune forme; verificare prima il nome.

## Restituisce

Integer — valore del campo Hits, non una percentuale né un Boolean. Zero può essere reale o indicare dati assenti. Non dividere per un massimo pari a zero. I valori degli altri mobile possono essere sconosciuti. HP/HitsMax possono rappresentare una scala relativa del server anziché punti esatti. HP=0 non dimostra la morte; usare Dead/IsDead.

## Comportamento

- Non apre status e non richiede aggiornamenti al server. A differenza della richiesta automatica di HP mancanti in Stealth, questo client legge solo dati esistenti. Non modifica caratteristiche né invia pacchetti.
- Ogni risultato è una lettura distinta. Il mondo può cambiare tra Exists e la chiamata successiva; più letture non formano un’istantanea atomica.
- Per un oggetto, World.Get scarta voci assenti o IsDestroyed e produce 0. HP/HitsMax leggono i campi Entity, anche per oggetti con tali campi; Mana/Stamina richiedono Mobile. Senza argomento legge self. Un nome senza argomenti non ha necessariamente una forma con ID: controllare le firme.
- Anche le letture senza argomenti danno 0 per Player assente/distrutto, inclusi Mana/Stamina diretti e i loro massimi, non solo tramite World.Get. Un personaggio morto ancora presente può conservare valori.

### Funzioni interne: dalla chiamata al risultato

Queste sono le vere fasi interne C#. ReadValue è una funzione ausiliaria completamente definita nell’esempio, non un comando integrato nascosto.

#### 1. RegisterCharacterGetterAliases

Alla creazione del runtime, RegisterCharacterGetterAliases registra nomi e forme. Senza argomento usa bridge.Self; con un argomento usa il relativo serial. Le registrazioni esistenti vengono mantenute.

Integer — valore del campo Hits, non una percentuale né un Boolean. Zero può essere reale o indicare dati assenti. Non dividere per un massimo pari a zero. I valori degli altri mobile possono essere sconosciuti. HP/HitsMax possono rappresentare una scala relativa del server anziché punti esatti. HP=0 non dimostra la morte; usare Dead/IsDead.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `RegisterCharacterGetterAliases`.

#### 2. TryGetObject

TryGetObject risolve numeri, stringhe esadecimali e nomi salvati. Il nome AddObject viene risolto a ogni chiamata; nessuna ricerca graphic/type o selezione interattiva.

Oggetto facoltativo nelle forme mostrate: serial numerico/stringa esadecimale, self, lasttarget o nome AddObject registrato. Non è un type. Se omesso, legge self. Un testo sconosciuto causa un errore di conversione in alcune forme; verificare prima il nome.

Sorgente del progetto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; funzione `TryGetObject`.

#### 3. Invoke

Invoke legge nel thread del gioco; un thread di lavoro attende l’elaborazione del gestore. L’annullamento dello script interrompe l’attesa. Nessun ritardo o richiesta di rete aggiuntivi.

Ogni risultato è una lettura distinta. Il mondo può cambiare tra Exists e la chiamata successiva; più letture non formano un’istantanea atomica.

Sorgente del progetto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; funzione `Invoke`.

#### 4. Get

Per un oggetto, World.Get scarta voci assenti o IsDestroyed e produce 0. HP/HitsMax leggono i campi Entity, anche per oggetti con tali campi; Mana/Stamina richiedono Mobile. Senza argomento legge self. Un nome senza argomenti non ha necessariamente una forma con ID: controllare le firme.

Integer — valore del campo Hits, non una percentuale né un Boolean. Zero può essere reale o indicare dati assenti. Non dividere per un massimo pari a zero. I valori degli altri mobile possono essere sconosciuti. HP/HitsMax possono rappresentare una scala relativa del server anziché punti esatti. HP=0 non dimostra la morte; usare Dead/IsDead.

Sorgente del progetto: `src/ClassicUO.Client/Game/World.cs`; funzione `Get`.

Non apre status e non richiede aggiornamenti al server. A differenza della richiesta automatica di HP mancanti in Stealth, questo client legge solo dati esistenti. Non modifica caratteristiche né invia pacchetti.


## Esempi

### Mostrare il valore del personaggio

```vb
# Mostrare il valore del personaggio
#
# Legge la salute attuale dal modello locale.
#
# Integer — valore del campo Hits, non una percentuale né un Boolean. Zero può essere reale o
# indicare dati assenti. Non dividere per un massimo pari a zero. I valori degli altri mobile
# possono essere sconosciuti. HP/HitsMax possono rappresentare una scala relativa del server
# anziché punti esatti. HP=0 non dimostra la morte; usare Dead/IsDead.

SUB Main()
    # La chiamata senza argomenti legge self. value conserva un numero; STR lo converte solo per il
    # messaggio.

    VAR value = UO.GetHP()
    UO.Print('GetHP: ' + STR(value))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- La chiamata senza argomenti legge self. value conserva un numero; STR lo converte solo per il messaggio.

### Usare il valore in una condizione o un calcolo

```vb
# Usare il valore in una condizione o un calcolo
#
# Legge la salute attuale dal modello locale.
#
# Integer — valore del campo Hits, non una percentuale né un Boolean. Zero può essere reale o
# indicare dati assenti. Non dividere per un massimo pari a zero. I valori degli altri mobile
# possono essere sconosciuti. HP/HitsMax possono rappresentare una scala relativa del server
# anziché punti esatti. HP=0 non dimostra la morte; usare Dead/IsDead.

SUB Main()
    # L’esempio applica una soglia o un calcolo per questo campo. I numeri sono impostazioni di
    # esempio, non limiti del server. Prima della divisione si verifica che il massimo sia positivo.

    VAR value = UO.GetHP()
    VAR maximum = UO.GetMaxHP()
    IF maximum > 0 AND value * 100 / maximum < 50 THEN
        UO.Print('Health below half of the known maximum')
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- L’esempio applica una soglia o un calcolo per questo campo. I numeri sono impostazioni di esempio, non limiti del server. Prima della divisione si verifica che il massimo sia positivo.

### Funzione ausiliaria ReadValue completa

```vb
# Funzione ausiliaria ReadValue completa
#
# Legge la salute attuale dal modello locale.
#
# Integer — valore del campo Hits, non una percentuale né un Boolean. Zero può essere reale o
# indicare dati assenti. Non dividere per un massimo pari a zero. I valori degli altri mobile
# possono essere sconosciuti. HP/HitsMax possono rappresentare una scala relativa del server
# anziché punti esatti. HP=0 non dimostra la morte; usare Dead/IsDead.

SUB Main()
    # lasttarget è l’oggetto selezionato in precedenza; Exists ne verifica la presenza. obj è
    # l’unico parametro di ReadValue. La funzione completamente definita restituisce il numero
    # invariato.

    IF UO.Exists('lasttarget') THEN
        VAR value = ReadValue('lasttarget')
        UO.Print('Selected value: ' + CStr(value))
    END IF
END SUB

SUB ReadValue(obj)
    RETURN UO.GetHP(obj)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- lasttarget è l’oggetto selezionato in precedenza; Exists ne verifica la presenza. obj è l’unico parametro di ReadValue. La funzione completamente definita restituisce il numero invariato.
