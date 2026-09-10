# IF / ELSEIF / ELSE / END IF

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

IF sceglie al massimo un ramo: IF, poi ELSEIF fino al primo risultato vero; altrimenti ELSE, se presente. Normalmente si prosegue dopo END IF.

## Sintassi esatta

```text
IF condition THEN
    statements
END IF
IF condition THEN
    statements
ELSEIF elseifCondition THEN
    statements
ELSE
    statements
END IF
```

## Parametri

- `condition` — condition: espressione verificata una volta all’ingresso. Zero numerico è falso, gli altri numeri veri. Preferire confronti espliciti o risultati booleani API.
- `elseifCondition` — elseifCondition: condizione aggiuntiva facoltativa, valutata solo se tutte le precedenti sono false. Scrivere ELSEIF come parola unica.
- `statements / ELSE` — statements / ELSE: istruzioni sulle righe successive. ELSE è facoltativo, senza condizione, unico e finale. THEN e END IF sono obbligatori; usare blocchi multilinea.

## Restituisce

Nessun valore (Unit). IF è un’istruzione, non una funzione. Una condizione o RETURN del ramo scelto può produrre un valore. I booleani 1/0 si confrontano con TRUE/FALSE; IF count accetta ogni numero non nullo, IF count=TRUE solo 1.

## Comportamento

- Il compilatore crea salti condizionali e di uscita. Falso salta alla prossima condizione o ELSE; il ramo scelto salta le alternative. Ogni IF annidato ha il proprio ELSE. RETURN esce dalla procedura eseguendo i FINALLY esterni.
- Per compatibilità IF confronta con zero numerico senza convertire ogni tipo tramite CBool. Testo "0", testo vuoto, array, oggetti e Unit scelgono il ramo vero. Convertire esplicitamente il testo o confrontare la proprietà desiderata. AndAlso/OrElse richiedono numeri.
- Dichiarazioni nei rami saltati non creano variabili durante l’esecuzione. Inizializzare i risultati condivisi prima di IF. Option Explicit controlla nomi, non assegnazioni su ogni percorso. Più ELSE sono rifiutati prima dell’avvio con SC015, anche senza Option Explicit.

## Esempi

### 1. Quattro casi

```vb
# Classify(value) verifica <0, =0, <10, poi ELSE. -2, 0, 7, 20 danno negative, zero, small, large. Main restituisce "negative:zero:small:large"; ogni chiamata esegue un solo RETURN.
Option Explicit On
FUNCTION Classify(value)
    IF value < 0 THEN
        RETURN "negative"
    ELSEIF value = 0 THEN
        RETURN "zero"
    ELSEIF value < 10 THEN
        RETURN "small"
    ELSE
        RETURN "large"
    END IF
END FUNCTION
SUB Main()
    RETURN Classify(-2) + ":" + Classify(0) + ":" + Classify(7) + ":" + Classify(20)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

Classify(value) verifica <0, =0, <10, poi ELSE. -2, 0, 7, 20 danno negative, zero, small, large. Main restituisce "negative:zero:small:large"; ogni chiamata esegue un solo RETURN.

### 2. Decisioni annidate

```vb
# Action(enabled, amount) controlla enabled e poi amount>0 per scegliere work o idle. L’ELSE esterno dà disabled. (TRUE,5), (TRUE,0), (FALSE,5) producono "work:idle:disabled". Ogni END IF chiude il suo blocco.
Option Explicit On
FUNCTION Action(enabled, amount)
    IF enabled THEN
        IF amount > 0 THEN
            RETURN "work"
        ELSE
            RETURN "idle"
        END IF
    ELSE
        RETURN "disabled"
    END IF
END FUNCTION
SUB Main()
    RETURN Action(TRUE, 5) + ":" + Action(TRUE, 0) + ":" + Action(FALSE, 5)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

Action(enabled, amount) controlla enabled e poi amount>0 per scegliere work o idle. L’ELSE esterno dà disabled. (TRUE,5), (TRUE,0), (FALSE,5) producono "work:idle:disabled". Ogni END IF chiude il suo blocco.

### 3. Ordine delle condizioni

```vb
# Check(calls,value) incrementa calls ByRef e restituisce value. Prima condizione falsa, seconda vera; terza ed ELSE sono saltati. result=7, calls=2; Main restituisce calls*10+result=27. Tutte le funzioni ausiliarie sono incluse.
Option Explicit On
FUNCTION Check(ByRef calls, ByVal value)
    calls += 1
    RETURN value
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR result = 0
    IF Check(calls, FALSE) THEN
        result = 5
    ELSEIF Check(calls, TRUE) THEN
        result = 7
    ELSEIF Check(calls, TRUE) THEN
        result = 9
    ELSE
        result = 8
    END IF
    RETURN calls * 10 + result
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

Check(calls,value) incrementa calls ByRef e restituisce value. Prima condizione falsa, seconda vera; terza ed ELSE sono saltati. result=7, calls=2; Main restituisce calls*10+result=27. Tutte le funzioni ausiliarie sono incluse.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: if / elseif / else
Runtime/Instructions/Generator.cs: Generate(IfContext)
Runtime/Interpreter.cs: CallSubrutine / IfInstruction / CreateArgumentWriter
Analysis/MisplacedStatementsVisitor.cs: VisitIf
Runtime/InjectionRuntime.cs: BlockingLanguageError
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/if-then-else-statement
-->
