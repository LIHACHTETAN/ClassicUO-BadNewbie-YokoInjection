# += / -= / *= / /= / &=

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Aggiornare una variabile o elemento di array esistente con +=, -=, *=, /=. Il motore legge il valore, esegue l’operazione e lo riscrive senza valutare due volte la destinazione.

## Sintassi esatta

```text
target += value
target -= value
target *= value
target /= value
target &= value
```

## Parametri

- `target` — target: scalare esistente o elemento items[index], grid[x][y]. Servono elementi inizializzati e indici validi a partire da zero. L’istruzione non dichiara variabili.
- `operator` — += e &= sommano numeri o uniscono due String; -= sottrae; *= moltiplica; /= divide. Il preprocessore trasforma &= in +=, quindi 5 &= 3 memorizza 8. String e numero richiedono CStr esplicito. Scrivi ogni operatore come singolo token.
- `value` — value: espressione valutata una volta dopo destinazione e indici. Il tipo deve essere adatto all’operazione. Convertire i numeri con CStr prima di aggiungerli a String.

## Restituisce

Nessun valore (Unit). È un’istruzione, non un’espressione o flag di successo. Leggere target nella riga seguente per ottenere il valore memorizzato. AS si applica agli scalari: Integer 5 dopo /=2 memorizza Integer 2, mentre una variabile numerica non tipizzata riceve Decimal 2.5.

## Comportamento

- Ogni riferimento all’array viene acquisito prima del suo indice. Gli indici si valutano una volta da sinistra a destra, verificando i limiti prima dell’operando destro. La cella selezionata resta la destinazione anche se una funzione ByRef sostituisce la variabile o una cella genitore.
- Valgono le regole di +, -, *, /: overflow intero su 32 bit, / restituisce Decimal e la divisione flottante per zero può dare Infinity/NaN. Sommare String e numero fallisce. Gli elementi di array non applicano conversioni scalari AS.
- Destinazione non dichiarata, elemento non inizializzato, indice errato, operazione incompatibile, scrittura CONST o conversione fallita generano errori gestibili. La scrittura finale non avviene, ma gli effetti delle funzioni operando già eseguite restano. CONST e AS si verificano alla scrittura scalare, dopo l’eventuale esecuzione a destra.
- Option Explicit controlla i nomi prima dell’esecuzione. Il debugger mantiene la riga originale e i cicli rispettano pausa/arresto. Lettura, calcolo e scrittura non sono sincronizzazione atomica tra procedure concorrenti.

## Esempi

### 1. Tutte le operazioni

```vb
# amount parte da 10. +=2 dà 12, -=3 dà 9, *=4 dà 36, /=2 dà Decimal 18. Main restituisce il valore memorizzato; le assegnazioni stesse non restituiscono nulla.
Option Explicit On
SUB Main()
    VAR amount = 10
    amount += 2
    amount -= 3
    amount *= 4
    amount /= 2
    RETURN amount
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

amount parte da 10. +=2 dà 12, -=3 dà 9, *=4 dà 36, /=2 dà Decimal 18. Main restituisce il valore memorizzato; le assegnazioni stesse non restituiscono nulla.

### 2. Indice valutato una volta

```vb
# NextIndex incrementa calls ricevuto ByRef e restituisce 0. items[0] parte da 5; +=2 lo cambia in 7. Una sola chiamata dà calls=1. Main restituisce items[0]*10+calls=71. La funzione ausiliaria è completa.
Option Explicit On
FUNCTION NextIndex(ByRef calls)
    calls += 1
    RETURN 0
END FUNCTION
SUB Main()
    DIM items[0]
    items[0] = 5
    VAR calls = 0
    items[NextIndex(calls)] += 2
    RETURN items[0] * 10 + calls
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

NextIndex incrementa calls ricevuto ByRef e restituisce 0. items[0] parte da 5; +=2 lo cambia in 7. Una sola chiamata dà calls=1. Main restituisce items[0]*10+calls=71. La funzione ausiliaria è completa.

### 3. Gestire una costante protetta

```vb
# limit è CONST 5. limit+=1 fallisce in scrittura; CATCH salva l’errore in problem e imposta caught=TRUE. limit resta 5. Main restituisce "5:1" con CStr espliciti. Il flag descrive la gestione dell’errore, non il risultato dell’assegnazione. Il testo si costruisce in una variabile: report=CStr(limit), poi report &= ":" e report &= CStr(caught). Ogni &= aggiorna report; Return report restituisce "5:1".
Option Explicit On
SUB Main()
    CONST limit = 5
    VAR caught = FALSE
    TRY
        limit += 1
    CATCH problem
        caught = TRUE
    END TRY
    VAR report = CStr(limit)
    report &= ":"
    report &= CStr(caught)
    RETURN report
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

limit è CONST 5. limit+=1 fallisce in scrittura; CATCH salva l’errore in problem e imposta caught=TRUE. limit resta 5. Main restituisce "5:1" con CStr espliciti. Il flag descrive la gestione dell’errore, non il risultato dell’assegnazione. Il testo si costruisce in una variabile: report=CStr(limit), poi report &= ":" e report &= CStr(caught). Ogni &= aggiorna report; Return report restituisce "5:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: compoundAssignment / compoundOperator
Runtime/BasicSyntaxPreprocessor.cs: ReplaceConcatenationOutsideLiterals
Analysis/InvalidSymbolVisitor.cs: VisitCompoundAssignment / ValidateAssignmentTarget
Runtime/Interpreter.cs: VisitCompoundAssignment
Runtime/SemanticScope.cs: ValidateIndex / SetVar / Coerce
-->
