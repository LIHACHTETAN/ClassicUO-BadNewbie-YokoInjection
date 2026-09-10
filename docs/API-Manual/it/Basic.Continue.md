# Continue For / Do / While

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Continue salta il resto del corpo del ciclo contenitore più vicino del tipo richiesto. Continue For vale per For e For Each, Continue Do per Do/Loop e Repeat/Until, Continue While per While/Wend.

## Sintassi esatta

```text
Continue For
Continue Do
Continue While
```

## Parametri

- `kind` — kind: For, Do o While obbligatorio dopo Continue, senza parentesi. Il ciclo deve contenere l’istruzione nella stessa procedura. Un ciclo interno di altro tipo non intercetta il salto.

## Restituisce

Continue non restituisce valori e non è un’espressione. Non rappresenta TRUE/FALSE né riavvia la procedura. La funzione può eseguire RETURN in seguito; gli esempi restituiscono Integer 10, 3 e 34.

## Comportamento

- For esegue NEXT, applica STEP e confronta il valore successivo con il limite; For Each prende l’elemento successivo. Il ciclo termina quando esaurito. Non ripete inizializzazione o espressione della raccolta.
- Do verifica nuovamente la condizione iniziale, oppure quella finale su Loop. Repeat/Until usa UNTIL. Do/Loop senza condizione continua fino all’uscita o all’arresto. While verifica WHILE. Continue Do non seleziona While/Wend.
- La preparazione risolve l’indirizzo del ciclo richiesto. Se manca produce SC020 prima degli inizializzatori anche senza Option Explicit. Controlla anche NEXT e chiusure. La vecchia forma FOR/NEXT attraverso IF resta supportata.
- Uscire da TRY/CATCH esegue i FINALLY attraversati dall’interno all’esterno, una volta ciascuno. Se tutto il ciclo è dentro TRY, quel FINALLY non viene eseguito a ogni giro. RETURN o un errore in FINALLY sostituisce il salto pendente.
- Continue non attende. Aggiornare la condizione o usare un’attesa appropriata nel polling, altrimenti il ciclo può essere infinito. Pausa e arresto restano attivi. Gli enumeratori nativi abbandonati vengono rilasciati; le esecuzioni restano indipendenti. Exit For/Do/While termina il ciclo.

## Esempi

### 1. Saltare elementi

```vb
# values contiene -2, 4, 0, 6. item<=0 esegue Continue For per -2 e 0, saltando total+=item. Vale anche in For Each. SumPositive e Main restituiscono Integer 10 dalla somma 4+6.
Option Explicit On
Function SumPositive(values)
    Var total = 0
    For Each item In values
        If item <= 0 Then
            Continue For
        End If
        total += item
    Next
    Return total
End Function
Sub Main()
    Dim values[3]
    values[0] = -2
    values[1] = 4
    values[2] = 0
    values[3] = 6
    Return SumPositive(values)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

values contiene -2, 4, 0, 6. item<=0 esegue Continue For per -2 e 0, saltando total+=item. Vale anche in For Each. SumPositive e Main restituiscono Integer 10 dalla somma 4+6.

### 2. Scegliere il ciclo esterno

```vb
# AdvanceTo riceve limit=3, count parte da 0. In While True, count aumenta e Continue Do passa al Do esterno. La condizione viene ricontrollata; count=3 termina il ciclo e restituisce Integer 3.
Option Explicit On
Function AdvanceTo(limit)
    Var count = 0
    Do While count < limit
        While True
            count += 1
            Continue Do
        Wend
    Loop
    Return count
End Function
Sub Main()
    Return AdvanceTo(3)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

AdvanceTo riceve limit=3, count parte da 0. In While True, count aumenta e Continue Do passa al Do esterno. La condizione viene ricontrollata; count=3 termina il ciclo e restituisce Integer 3.

### 3. Pulizia del giro saltato

```vb
# Process riceve limit=3 e skip=2. i assume 1, 2, 3. Il secondo giro salta total+=i, ma Finally aumenta cleanup tre volte. total=4, cleanup=3; RETURN cleanup*10+total restituisce Integer 34.
Option Explicit On
Function Process(limit, skip)
    Var total = 0
    Var cleanup = 0
    For Var i = 1 To limit
        Try
            If i = skip Then
                Continue For
            End If
            total += i
        Finally
            cleanup += 1
        End Try
    Next i
    Return cleanup * 10 + total
End Function
Sub Main()
    Return Process(3, 2)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

Process riceve limit=3 e skip=2. i assume 1, 2, 3. Il secondo giro salta total+=i, ma Finally aumenta cleanup tre volte. total=4, cleanup=3; RETURN cleanup*10+total restituisce Integer 34.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: continueLoop / doLoop
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: AddTransfer / EndBreakScope
Runtime/Interpreter.cs: Transfer / DeferReturn / TryHandleStructuredError
Runtime/ForScope.cs: HasNext / AdvanceEach
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/continue-statement
-->
