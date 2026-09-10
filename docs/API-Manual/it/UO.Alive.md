# UO.Alive

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Controlla la presenza di un oggetto senza stato di morte.

## Sintassi esatta

```text
UO.Alive() -> Integer
UO.Alive(value:Any) -> Integer
```

## Parametri

- `value` — Oggetto facoltativo nelle forme mostrate: serial numerico/stringa esadecimale, self, lasttarget o nome AddObject registrato. Non è un type. Se omesso, legge self. Un testo sconosciuto causa un errore di conversione in alcune forme; verificare prima il nome.

## Restituisce

Integer Boolean: 1 = TRUE, 0 = FALSE. Confrontabile con numeri o costanti logiche senza virgolette. 1 indica un serial positivo esistente non marcato morto. Anche un oggetto presente restituisce 1: non è un filtro per mobile. Oggetti morti o assenti restituiscono 0.

Risultato logico: 1 = TRUE, 0 = FALSE. Dopo VAR result = comando(...), usare IF result = TRUE THEN o IF result = 1 THEN; per il risultato negativo, IF result = FALSE THEN o IF result = 0 THEN. TRUE/FALSE senza virgolette. Chiamare una sola volta e salvare il risultato: un nuovo richiamo può ripetere l’azione o leggere uno stato cambiato.

## Comportamento

- Legge il modello locale: nessun target, richiesta di status, modifica di flag o invio di pacchetti. Un oggetto distrutto è assente anche prima della rimozione dal dizionario.
- Ogni risultato è una lettura distinta. Il mondo può cambiare tra Exists e la chiamata successiva; più letture non formano un’istantanea atomica.

### Funzioni interne: dalla chiamata al risultato

Queste sono le vere fasi interne C#. ReadState è una funzione ausiliaria completamente definita nell’esempio, non un comando integrato nascosto.

#### 1. RegisterCharacterGetterAliases

Alla creazione del runtime, RegisterCharacterGetterAliases registra nomi e forme. Senza argomento usa bridge.Self; con un argomento usa il relativo serial. Le registrazioni esistenti vengono mantenute.

1 indica un serial positivo esistente non marcato morto. Anche un oggetto presente restituisce 1: non è un filtro per mobile. Oggetti morti o assenti restituiscono 0.

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

World.Get risolve il serial e restituisce null per IsDestroyed; poi legge il flag Mobile. Alive controlla Exists e l’assenza di IsDead; gli oggetti sono ammessi. Dead per self legge Player.IsDead.

1 indica un serial positivo esistente non marcato morto. Anche un oggetto presente restituisce 1: non è un filtro per mobile. Oggetti morti o assenti restituiscono 0.

Sorgente del progetto: `src/ClassicUO.Client/Game/World.cs`; funzione `Get`.

Legge il modello locale: nessun target, richiesta di status, modifica di flag o invio di pacchetti. Un oggetto distrutto è assente anche prima della rimozione dal dizionario.


## Esempi

### Controllare il proprio stato

```vb
# Controllare il proprio stato
#
# Controlla la presenza di un oggetto senza stato di morte.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE. Confrontabile con numeri o costanti logiche senza
# virgolette. 1 indica un serial positivo esistente non marcato morto. Anche un oggetto presente
# restituisce 1: non è un filtro per mobile. Oggetti morti o assenti restituiscono 0.
#
# Risultato logico: 1 = TRUE, 0 = FALSE. Dopo VAR result = comando(...), usare IF result = TRUE
# THEN o IF result = 1 THEN; per il risultato negativo, IF result = FALSE THEN o IF result = 0
# THEN. TRUE/FALSE senza virgolette. Chiamare una sola volta e salvare il risultato: un nuovo
# richiamo può ripetere l’azione o leggere uno stato cambiato.

SUB Main()
    # Le parentesi vuote leggono self. active conserva un risultato; TRUE e FALSE selezionano i due
    # rami. Print mostra soltanto un messaggio di esempio.

    VAR active = UO.Alive()
    IF active = TRUE THEN
        UO.Print('State is active')
    ELSE
        UO.Print('State is inactive or unavailable')
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Le parentesi vuote leggono self. active conserva un risultato; TRUE e FALSE selezionano i due rami. Print mostra soltanto un messaggio di esempio.

### Oggetto selezionato e funzione ReadState completa

```vb
# Oggetto selezionato e funzione ReadState completa
#
# Controlla la presenza di un oggetto senza stato di morte.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE. Confrontabile con numeri o costanti logiche senza
# virgolette. 1 indica un serial positivo esistente non marcato morto. Anche un oggetto presente
# restituisce 1: non è un filtro per mobile. Oggetti morti o assenti restituiscono 0.
#
# Risultato logico: 1 = TRUE, 0 = FALSE. Dopo VAR result = comando(...), usare IF result = TRUE
# THEN o IF result = 1 THEN; per il risultato negativo, IF result = FALSE THEN o IF result = 0
# THEN. TRUE/FALSE senza virgolette. Chiamare una sola volta e salvare il risultato: un nuovo
# richiamo può ripetere l’azione o leggere uno stato cambiato.

SUB Main()
    # lasttarget è l’oggetto selezionato in precedenza. Exists ne verifica la presenza. obj è
    # l’unico parametro di ReadState; la funzione restituisce il risultato invariato. La definizione
    # completa è inclusa nel codice copiato.

    IF UO.Exists('lasttarget') THEN
        VAR observed = ReadState('lasttarget')
        UO.Print('State 1/0: ' + CStr(observed))
    END IF
END SUB

SUB ReadState(obj)
    RETURN UO.Alive(obj)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- lasttarget è l’oggetto selezionato in precedenza. Exists ne verifica la presenza. obj è l’unico parametro di ReadState; la funzione restituisce il risultato invariato. La definizione completa è inclusa nel codice copiato.

### Rilevare un cambiamento in mezzo secondo

```vb
# Rilevare un cambiamento in mezzo secondo
#
# Controlla la presenza di un oggetto senza stato di morte.
#
# Integer Boolean: 1 = TRUE, 0 = FALSE. Confrontabile con numeri o costanti logiche senza
# virgolette. 1 indica un serial positivo esistente non marcato morto. Anche un oggetto presente
# restituisce 1: non è un filtro per mobile. Oggetti morti o assenti restituiscono 0.
#
# Risultato logico: 1 = TRUE, 0 = FALSE. Dopo VAR result = comando(...), usare IF result = TRUE
# THEN o IF result = 1 THEN; per il risultato negativo, IF result = FALSE THEN o IF result = 0
# THEN. TRUE/FALSE senza virgolette. Chiamare una sola volta e salvare il risultato: un nuovo
# richiamo può ripetere l’azione o leggere uno stato cambiato.

SUB Main()
    # Entrambe le chiamate senza argomenti leggono self; WAIT(500) significa 500 millisecondi. Si
    # confrontano due istantanee e si possono perdere cambiamenti intermedi. Nessuna attesa
    # infinita.

    VAR before = UO.Alive()
    WAIT(500)
    VAR after = UO.Alive()
    IF before <> after THEN
        UO.Print('State changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Entrambe le chiamate senza argomenti leggono self; WAIT(500) significa 500 millisecondi. Si confrontano due istantanee e si possono perdere cambiamenti intermedi. Nessuna attesa infinita.
