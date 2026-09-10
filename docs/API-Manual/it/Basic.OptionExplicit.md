# Option Explicit

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Richiede la dichiarazione delle variabili prima di eseguire lo script. È una direttiva di file del linguaggio Basic di questo motore, non un comando UO o una chiamata di funzione.

## Sintassi esatta

```text
Option Explicit
Option Explicit On
Option Explicit Off
```

## Parametri

- `On / Off` — On attiva il controllo rigoroso; Off lo disattiva. Senza una parola dopo Explicit si intende On. In assenza della direttiva resta la modalità precedente non rigorosa. Non aggiungere parentesi o virgolette.

## Restituisce

Nessun valore. La direttiva non è un’espressione e non restituisce TRUE/FALSE, un numero o un ID. I RETURN negli esempi appartengono a Main o Enough, non a Option Explicit.

## Comportamento

- Scrivere la direttiva una sola volta, prima di variabili, costanti e procedure. Può essere preceduta da righe vuote e commenti. Una direttiva ripetuta o tardiva produce SC013, anche passando successivamente a Off.
- Con On, leggere o assegnare una variabile non dichiarata produce SC006 con la posizione nel sorgente. Si controllano anche nomi di array, contatori FOR e oggetti destinatari di metodi. VAR/DIM/CONST, parametri e variabili CATCH con nome dichiarano nomi. FOR VAR dichiara il contatore.
- Dichiarare le variabili locali prima dell’uso. Una variabile locale di una procedura non dichiara un nome in un’altra. Le dichiarazioni globali sono accessibili alle procedure. Il controllo dei nomi non dimostra l’inizializzazione in tutti i rami.
- Il parser legge l’intero file; l’analizzatore risolve le dichiarazioni; un errore rigoroso blocca l’esecuzione prima del primo comando. Un ricaricamento applica l’opzione del nuovo file indipendentemente dal precedente. Off può ancora produrre avvisi; leggere un valore inesistente può fallire durante l’esecuzione.
- La direttiva da sola non esegue azioni di gioco né invia pacchetti. Non implica compatibilità completa con VB.NET e non controlla l’esistenza di un bersaglio.

## Esempi

### 1. Dichiarare prima di assegnare

```vb
# On attiva il controllo. DIM dichiara count come Integer; assegnare 5 è valido. Main restituisce 5. Sostituire count con coutn non dichiarato blocca l’avvio con SC006.
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    RETURN count
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

On attiva il controllo. DIM dichiara count come Integer; assegnare 5 è valido. Main restituisce 5. Sostituire count con coutn non dichiarato blocca l’avvio con SC006.

### 2. Parametro e costante globale

```vb
# La direttiva senza modalità significa On. minimum è la costante globale 3. amount è un parametro dichiarato in Enough e una variabile locale distinta in Main. Enough confronta 5 >= 3 e restituisce TRUE, numericamente 1.
Option Explicit
CONST minimum = 3
FUNCTION Enough(amount)
    RETURN amount >= minimum
END FUNCTION
SUB Main()
    VAR amount = 5
    RETURN Enough(amount)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

La direttiva senza modalità significa On. minimum è la costante globale 3. amount è un parametro dichiarato in Enough e una variabile locale distinta in Main. Enough confronta 5 >= 3 e restituisce TRUE, numericamente 1.

### 3. Eseguire uno script precedente

```vb
# Off permette di creare legacyCounter con un’assegnazione senza DIM. Main restituisce 7. Questo esempio di compatibilità può ancora mostrare un avviso; dichiarare la variabile e usare On per il controllo rigoroso.
Option Explicit Off
SUB Main()
    legacyCounter = 7
    RETURN legacyCounter
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

Off permette di creare legacyCounter con un’assegnazione senza DIM. Main restituisce 7. Questo esempio di compatibilità può ancora mostrare un avviso; dichiarare la variabile e usare On per il controllo rigoroso.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: optionExplicit
Analysis/SanityAnalyzer.cs
Analysis/InvalidSymbolVisitor.cs
Runtime/InjectionRuntime.cs
-->
