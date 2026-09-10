# CONST

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

CONST dichiara un nome la cui associazione rifiuta la normale riassegnazione. Il valore iniziale può essere un letterale o il risultato di un’espressione, valutato all’esecuzione della dichiarazione.

## Sintassi esatta

```text
CONST name [AS type] = expression [, name ...]
```

## Parametri

- `name` — Nome della costante senza virgolette, distinto nel proprio ambito. La dichiarazione è globale fuori dalle procedure e locale alla chiamata al loro interno.
- `type` — Tipo AS supportato facoltativo, con le conversioni di VAR. AS Integer converte per esempio nell’intero con segno a 32 bit del motore. Le parentesi quadre indicano parti facoltative e non si scrivono intorno ad AS.
- `expression` — Espressione iniziale obbligatoria: numero, testo tra virgolette, TRUE/FALSE, calcolo o risultato di una funzione supportata. Viene valutata una volta per questa esecuzione della dichiarazione, non una volta per sempre.

## Restituisce

Nessun valore. CONST è una dichiarazione, non una funzione o una domanda logica. Leggere il nome fornisce il risultato conservato. I RETURN degli esempi appartengono a Main o ApplyLimit.

## Comportamento

- Assegnazione normale, LET e SET non possono sostituire questa associazione: si produce un errore di modifica della costante. TRY/CATCH può gestirlo. Option Explicit richiede dichiarazioni ma non rileva ogni assegnazione errata prima dell’avvio.
- Una costante globale si inizializza a una nuova esecuzione principale e viene ereditata dalle procedure chiamate con il flag di costante e il tipo AS. Le costanti locali si inizializzano alla dichiarazione. Una funzione inizializzatrice può quindi lavorare nuovamente all’avvio successivo.
- La protezione riguarda l’associazione, non il contenuto interno di Array/Object. Una dichiarazione locale distinta può nascondere un nome globale; un’altra dichiarazione crea una nuova associazione. Evitare di riutilizzare nomi di costanti.
- Il motore valuta l’inizializzatore, applica AS e registra il flag nell’ambito. Le assegnazioni normali successive controllano quel flag prima di modificare il valore. Gli esempi di letterali scalari non eseguono azioni di gioco.

## Esempi

### 1. Calcolo con un ritardo fisso

```vb
# delay è una costante Integer locale pari a 350. Moltiplicare per 2 crea la variabile distinta doubled=700. Main restituisce 700; l’esempio non attende.
Option Explicit On
SUB Main()
    CONST delay AS Integer = 350
    VAR doubled = delay * 2
    RETURN doubled
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

delay è una costante Integer locale pari a 350. Moltiplicare per 2 crea la variabile distinta doubled=700. Main restituisce 700; l’esempio non attende.

### 2. Passare un limite globale

```vb
# limit è una costante Integer globale pari a 50. ApplyLimit riceve amount=72 e maximum=50 e restituisce la quantità minore, 50. La funzione è definita interamente e legge soltanto i parametri.
Option Explicit On
CONST limit AS Integer = 50
FUNCTION ApplyLimit(amount, maximum)
    IF amount > maximum THEN
        RETURN maximum
    END IF
    RETURN amount
END FUNCTION
SUB Main()
    RETURN ApplyLimit(72, limit)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

limit è una costante Integer globale pari a 50. ApplyLimit riceve amount=72 e maximum=50 e restituisce la quantità minore, 50. La funzione è definita interamente e legge soltanto i parametri.

### 3. Gestire una riassegnazione vietata

```vb
# limit parte da 3. Assegnare 4 causa un errore senza modificare la costante. CATCH conserva l’errore in problem e imposta caught=TRUE. Main restituisce 1 logico; qui TRUE e 1 sono equivalenti.
Option Explicit On
SUB Main()
    CONST limit = 3
    VAR caught = FALSE
    TRY
        limit = 4
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

limit parte da 3. Assegnare 4 causa un errore senza modificare la costante. CATCH conserva l’errore in problem e imposta caught=TRUE. Main restituisce 1 logico; qui TRUE e 1 sono equivalenti.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: constDeclaration / globalConst
Runtime/DefinitionCollector.cs: VisitGlobalConst
Runtime/Interpreter.cs: VisitConstDef
Runtime/SemanticScope.cs: DefineVar / SetVar
-->
