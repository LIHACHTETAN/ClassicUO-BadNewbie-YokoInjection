# UO.Frozen

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Legge il flag di paralisi di un mobile noto al client.

## Sintassi esatta

```text
UO.Frozen() -> Integer
UO.Frozen(value:Any) -> Integer
```

## Parametri

- `value` — Serial/ID facoltativo del mobile: intero, stringa esadecimale, self, lasttarget, altro alias standard o nome AddObject. Non è graphic/type. Senza argomento viene scelto self. Un alias sconosciuto dà 0; non si apre un cursore di selezione.

## Restituisce

Integer Boolean: 1 = TRUE se un mobile caricato ha IsParalyzed; 0 = FALSE se il flag è assente, il mobile è sconosciuto o eliminato, oppure l’oggetto è un item. Non è la durata residua; 0 non garantisce la possibilità di muoversi.

## Comportamento

- Usa Paralyzed per controllare il flag di paralisi. Le varianti Is/Get, GetParalisa, Frozen e GetLocked leggono lo stesso flag.
- La lettura è locale. Non applica né cura la paralisi, non ne attende la fine e non chiede aggiornamenti al server.
- Per questa verifica, value = TRUE, value = 1 e IF value sono equivalenti. TRUE/FALSE si scrivono senza virgolette. Il risultato è un flag, non una quantità o un ID.

## Esempi

### Verificare self con TRUE

```vb
# Verificare self con TRUE
#
# Legge il flag di paralisi di un mobile noto al client.
#
# Integer Boolean: 1 = TRUE se un mobile caricato ha IsParalyzed; 0 = FALSE se il flag è
# assente, il mobile è sconosciuto o eliminato, oppure l’oggetto è un item. Non è la durata
# residua; 0 non garantisce la possibilità di muoversi.

SUB Main()
    # Le parentesi vuote scelgono self. state conserva un’istantanea; TRUE è la costante numerica 1.
    # FALSE non esclude un muro, la stamina esaurita o un altro ostacolo al movimento.

    VAR state = UO.Frozen()
    IF state = TRUE THEN
        UO.Print('Paralysis flag is set')
    ELSE
        UO.Print('Paralysis flag is absent or unavailable')
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Le parentesi vuote scelgono self. state conserva un’istantanea; TRUE è la costante numerica 1.
- FALSE non esclude un muro, la stamina esaurita o un altro ostacolo al movimento.

### Verificare il mobile selezionato

```vb
# Verificare il mobile selezionato
#
# Legge il flag di paralisi di un mobile noto al client.
#
# Integer Boolean: 1 = TRUE se un mobile caricato ha IsParalyzed; 0 = FALSE se il flag è
# assente, il mobile è sconosciuto o eliminato, oppure l’oggetto è un item. Non è la durata
# residua; 0 non garantisce la possibilità di muoversi.

SUB Main()
    # target conserva il serial dell’ultimo bersaglio come stringa esadecimale. IsNpc verifica un
    # mobile caricato, inclusi i giocatori.
    # L’argomento sceglie quel target salvato. Non apre un cursore e non modifica lasttarget.

    VAR target = UO.GetSerial('lasttarget')
    IF UO.IsNpc(target) THEN
        VAR state = UO.Frozen(target)
        UO.Print('Selected mobile paralysis 1/0: ' + STR(state))
    ELSE
        UO.Print('No loaded mobile selected')
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- target conserva il serial dell’ultimo bersaglio come stringa esadecimale. IsNpc verifica un mobile caricato, inclusi i giocatori.
- L’argomento sceglie quel target salvato. Non apre un cursore e non modifica lasttarget.

### Attendere la fine con un limite

```vb
# Attendere la fine con un limite
#
# Legge il flag di paralisi di un mobile noto al client.
#
# Integer Boolean: 1 = TRUE se un mobile caricato ha IsParalyzed; 0 = FALSE se il flag è
# assente, il mobile è sconosciuto o eliminato, oppure l’oggetto è un item. Non è la durata
# residua; 0 non garantisce la possibilità di muoversi.

SUB Main()
    # Al massimo dieci attese di 100 ms. Ogni chiamata senza argomento rilegge self.
    # Dopo il ciclo si verifica separatamente la presenza di self. Si osserva per circa un secondo
    # più l’esecuzione; la guarigione non è garantita.

    VAR attempts = 0
    WHILE UO.Frozen() = TRUE AND attempts < 10
        WAIT(100)
        attempts = attempts + 1
    WEND
    IF UO.IsNpc('self') THEN
        IF UO.Frozen() = FALSE THEN
            UO.Print('Paralysis flag is clear')
        ELSE
            UO.Print('Still paralyzed')
        END IF
    ELSE
        UO.Print('Self is unavailable')
    END IF
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

- Al massimo dieci attese di 100 ms. Ogni chiamata senza argomento rilegge self.
- Dopo il ciclo si verifica separatamente la presenza di self. Si osserva per circa un secondo più l’esecuzione; la guarigione non è garantita.
