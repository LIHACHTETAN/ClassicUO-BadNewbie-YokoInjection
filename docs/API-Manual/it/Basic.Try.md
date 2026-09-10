# Try / Catch / Finally / Throw

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Try gestisce gli errori di esecuzione del proprio corpo e delle funzioni chiamate. Catch riceve l’errore, Finally completa l’operazione e Throw crea o rilancia un errore. Un risultato API 0 o false va controllato esplicitamente: non attiva automaticamente Catch.

## Sintassi esatta

```text
Try
    statements
Catch
    handlerStatements
Finally
    cleanupStatements
End Try
Catch name
Catch name As Exception
Catch name As String
Throw stringExpression
Throw
```

## Parametri

- `Try / statements` — Try richiede un Catch, un Finally o entrambi prima di End Try. I blocchi possono essere annidati. Se il corpo riesce, Catch viene saltato. Questo sottoinsieme non implementa più Catch, filtri When o Exit Try.
- `Catch / name / As type` — La variabile Catch è facoltativa. name riceve il messaggio come String. As String indica questa rappresentazione; As Exception è una forma di compatibilità, non un oggetto .NET o filtro di tipo. Altri tipi sono rifiutati. Un nuovo nome diventa locale alla procedura e nasconde una globale omonima. Una locale esistente riceve un’assegnazione rispettando tipo/Const. Dichiarare uno String prima di Try se serve anche senza eseguire Catch.
- `Finally / End Try` — Finally è facoltativo se esiste Catch e può avere corpo vuoto. Completamento normale, errori, Return, Exit Sub/Function e trasferimenti di ciclo/GoTo verso l’esterno eseguono i Finally interessati. End Try è obbligatorio. L’annullamento evita intenzionalmente Catch e il Finally dello script per non ritardare l’arresto di emergenza.
- `Throw stringExpression` — Throw stringExpression valuta il messaggio una volta e genera un nuovo errore di script. Serve String; convertire esplicitamente altri valori con CStr. È una forma Basic, non Throw New Exception(...) di VB.NET. Senza gestore fallisce l’esecuzione corrente, non tutti gli altri script.
- `Throw` — Throw senza messaggio è valido solo dentro Catch, inclusi i blocchi annidati. Rilancia l’errore attivo mantenendo testo, file e riga originali. Una funzione chiamata da Catch necessita di un proprio Catch per questa forma.

## Restituisce

Try/Catch/Finally e Throw non restituiscono ID, numeri o Boolean. Catch espone il messaggio in name; Throw trasferisce il controllo invece di restituire un valore. Gli esempi restituiscono esplicitamente due String e Integer 13 da Main. Le API chiamate conservano il proprio contratto di ritorno.

## Comportamento

- La preparazione verifica i blocchi e vieta GoTo/On Error GoTo dentro Try, Catch o Finally. Il generatore conserva gli indirizzi di gestione e finalizzazione. Ogni chiamata ha i propri gestori attivi; l’errore raggiunge il Catch idoneo più vicino. Un errore in Catch passa attraverso il suo Finally a un gestore esterno. In assenza di gestione strutturata possono intervenire le normali regole On Error.
- Ritorno, errore o salto in sospeso sono conservati durante Finally. La finalizzazione annidata procede dall’interno verso l’esterno. Un nuovo errore in Finally sostituisce quello in sospeso. Basic permette anche Return e salti uscenti da Finally, sostituendo la continuazione in sospeso: è diverso da VB.NET. Il rilancio conserva la prima posizione dell’errore, anche da funzioni chiamate.
- Pausa/arresto rimangono attivi. Try non crea thread, tentativi ripetuti o attese. Gli indirizzi preparati vengono riutilizzati; controllare direttamente le condizioni normali anziché usare eccezioni. L’arresto di emergenza salta la finalizzazione dello script; le risorse gestite dall’host seguono la propria durata di vita nel motore.

## Esempi

### 1. Convalidare il parametro e salvare il messaggio

```vb
# CheckedAmount riceve amount=-2 come Integer tramite ByVal. Il valore negativo genera Throw "amount must be non-negative". Catch riceve lo String in problem e lo copia in message; As Exception non crea un oggetto. Finally imposta finished=1. Main restituisce "amount must be non-negative:1". Un valore non negativo tornerebbe normalmente senza Catch.
Option Explicit On
Function CheckedAmount(ByVal amount As Integer) As Integer
    If amount < 0 Then
        Throw "amount must be non-negative"
    End If
    Return amount
End Function

Sub Main()
    Dim message=""
    Dim finished=0
    Try
        CheckedAmount(-2)
    Catch problem As Exception
        message=problem
    Finally
        finished=1
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

CheckedAmount riceve amount=-2 come Integer tramite ByVal. Il valore negativo genera Throw "amount must be non-negative". Catch riceve lo String in problem e lo copia in message; As Exception non crea un oggetto. Finally imposta finished=1. Main restituisce "amount must be non-negative:1". Un valore non negativo tornerebbe normalmente senza Catch.

### 2. Rilanciare verso l’esterno

```vb
# Il Throw interno genera "missing item". Catch interno imposta trace=1; Throw senza messaggio mantiene lo stesso errore. Finally interno aggiunge 2, Catch esterno copia outerProblem in message e aggiunge 3, Finally esterno aggiunge 4. Main restituisce "1234:missing item". trace rappresenta l’ordine di esecuzione, non un codice di errore.
Option Explicit On
Sub Main()
    Dim trace=0
    Dim message=""
    Try
        Try
            Throw "missing item"
        Catch problem
            trace=1
            Throw
        Finally
            trace=trace*10+2
        End Try
    Catch outerProblem
        message=outerProblem
        trace=trace*10+3
    Finally
        trace=trace*10+4
    End Try
    Return CStr(trace) & ":" & message
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

Il Throw interno genera "missing item". Catch interno imposta trace=1; Throw senza messaggio mantiene lo stesso errore. Finally interno aggiunge 2, Catch esterno copia outerProblem in message e aggiunge 3, Finally esterno aggiunge 4. Main restituisce "1234:missing item". trace rappresenta l’ordine di esecuzione, non un codice di errore.

### 3. Finalizzare ogni iterazione iniziata

```vb
# number assume 1, 2 e 3. Solo 1 viene aggiunto a total: Continue For salta 2, Exit For termina a 3. Tutti i tre Try iniziati eseguono Finally, quindi finished=3. Main restituisce 1*10+3=13. Finally non richiede un errore; il trasferimento del ciclo attende la finalizzazione dell’iterazione.
Option Explicit On
Sub Main()
    Dim total=0
    Dim finished=0
    For Var number=1 To 3
        Try
            If number=2 Then
                Continue For
            End If
            If number=3 Then
                Exit For
            End If
            total+=number
        Finally
            finished+=1
        End Try
    Next
    Return total*10+finished
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

number assume 1, 2 e 3. Solo 1 viene aggiunto a total: Continue For salta 2, Exit For termina a 3. Tutti i tre Try iniziati eseguono Finally, quindi finished=3. Main restituisce 1*10+3=13. Finally non richiede un errore; il trasferimento del ciclo attende la finalizzazione dell’iterazione.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: tryStatement / catchClause / finallyClause / throwStatement
Analysis/TryStructureValidator.cs: VisitTryStatement / VisitSubrutine / VisitCatchClause / VisitThrowStatement
Runtime/Instructions/Generator.cs: Generate(TryStatementContext)
Runtime/Instructions/TryInstruction.cs: TryInstruction / CatchInstruction / FinallyInstruction / EndTryInstruction
Runtime/Interpreter.cs: CallSubrutine / TryHandleStructuredError / Transfer / DeferReturn / Failure
Runtime/SemanticScope.cs: IsLocal / DefineVar / SetVar
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/try-catch-finally-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/throw-statement
-->
