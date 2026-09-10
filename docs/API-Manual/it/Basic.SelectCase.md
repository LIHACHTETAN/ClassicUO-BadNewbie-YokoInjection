# Select Case / Case / Exit Select

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Select Case sceglie un ramo confrontando un valore memorizzato con alternative ordinate. È utile per categorie di oggetti, modalità e intervalli numerici. È un’istruzione Basic senza UO.; le chiamate di gioco nelle espressioni richiedono UO.

## Sintassi esatta

```text
Select Case expression
    Case value1, value2
        statements
        Exit Select
    Case from To to
        statements
    Case Is >= value
        statements
    Case Else
        statements
End Select
```

## Parametri

- `expression` — Espressione obbligatoria: variabile, letterale o chiamata di funzione. Viene valutata esattamente una volta a ogni ingresso, anche con blocco vuoto o solo Case Else.
- `value / from / to` — Case accetta un valore o espressioni separate da virgole. from To to include entrambi gli estremi; un intervallo invertito non corrisponde. L’estremo superiore viene valutato solo se il confronto inferiore riesce. Le virgole negli argomenti di una funzione non separano alternative.
- `Is comparison value` — Confronti =, <>, <, <=, > o >=. Is è facoltativo: Case Is >= 5 equivale a Case >= 5. Sono confronti di valori del motore, non controlli del tipo di oggetto.
- `Case Else` — Ramo facoltativo usato se nessun Case precedente corrisponde. Deve essere unico e ultimo. Senza di esso, la mancata corrispondenza prosegue dopo End Select.
- `Exit Select` — Esce dal Select Case contenitore più vicino, dopo il suo End Select. Non termina il ciclo esterno o la procedura. Fuori da Select Case causa un errore di caricamento.

## Restituisce

Select Case, Case, End Select ed Exit Select non restituiscono valori e non si confrontano con TRUE o 1. Le funzioni di esempio restituiscono esplicitamente String o Integer con Return. TRUE è il numero 1, FALSE è 0: Case True corrisponde a 1, non a qualsiasi numero diverso da zero.

## Comportamento

- La preparazione crea SelectInstruction, controlli CaseInstruction ordinati e salti risolti. Il valore è privato della chiamata corrente, senza variabile locale artificiale. Ricorsione e blocchi annidati mantengono valori indipendenti; ogni nuovo ingresso sostituisce il precedente.
- CaseMatches verifica da sinistra a destra fino alla prima corrispondenza. Il ramo scelto viene eseguito una volta, poi un salto ignora gli altri. Le modifiche in un Case non rileggono la selezione; gli effetti già prodotti non vengono annullati.
- Numeri e stringhe usano i confronti ordinari del motore; le stringhe distinguono maiuscole. Option Compare Text e conversioni automatiche VB.NET non sono implementati. Converti esplicitamente quando confronti numeri e testo.
- End Select è obbligatorio. Niente codice eseguibile prima del primo Case o For/Next diviso tra rami. Blocchi malformati impediscono il caricamento. Entra tramite Select Case, non con GoTo nel mezzo.
- Gli errori passano al gestore corrente. On Error Resume Next salta l’intera selezione se fallisce l’espressione; un Case errato passa al successivo. Resume ritenta l’istruzione. Exit Select esegue i Finally attivi da cui esce. Pausa e arresto vengono controllati tra istruzioni; non sono aggiunti attese o timeout.

## Esempi

### 1. Classificare quantità

```vb
# DescribeAmount riceve amount ByVal. Case 0 restituisce empty, 1 To 4 include 1 e 4, Is >= 5 restituisce large. I negativi raggiungono Case Else. Main chiama con -1, 0, 4, 5 e unisce negative:empty:small:large. Sono risultati definiti dallo script.
Option Explicit On
Function DescribeAmount(ByVal amount)
    Select Case amount
        Case 0
            Return "empty"
        Case 1 To 4
            Return "small"
        Case Is >= 5
            Return "large"
        Case Else
            Return "negative"
    End Select
End Function

Sub Main()
    Return DescribeAmount(-1) & ":" & DescribeAmount(0) & ":" & DescribeAmount(4) & ":" & DescribeAmount(5)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

DescribeAmount riceve amount ByVal. Case 0 restituisce empty, 1 To 4 include 1 e 4, Is >= 5 restituisce large. I negativi raggiungono Case Else. Main chiama con -1, 0, 4, 5 e unisce negative:empty:small:large. Sono risultati definiti dallo script.

### 2. Osservare le chiamate

```vb
# ReadMode incrementa reads ByRef e restituisce 2 una volta. Candidate incrementa checks e restituisce value. Il candidato 1 fallisce, 2 corrisponde e 3 viene saltato. selected diventa 7 e Main restituisce 1*100+2*10+7=127 senza accesso al gioco.
Option Explicit On
Function ReadMode(ByRef reads)
    reads += 1
    Return 2
End Function

Function Candidate(ByRef checks, ByVal value)
    checks += 1
    Return value
End Function

Sub Main()
    Dim reads = 0
    Dim checks = 0
    Dim selected = 0
    Select Case ReadMode(reads)
        Case Candidate(checks, 1)
            selected = -1
        Case Candidate(checks, 2), Candidate(checks, 3)
            selected = 7
        Case Else
            selected = -9
    End Select
    Return reads * 100 + checks * 10 + selected
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

ReadMode incrementa reads ByRef e restituisce 2 una volta. Candidate incrementa checks e restituisce value. Il candidato 1 fallisce, 2 corrisponde e 3 viene saltato. selected diventa 7 e Main restituisce 1*100+2*10+7=127 senza accesso al gioco.

### 3. Uscire da un blocco annidato

```vb
# route contiene harvest; il primo ramo imposta trace=1. Il Case 2 interno esegue Exit Select, salta trace=99 e Finally aggiunge 2. Il ramo esterno aggiunge 3: risultato 123. Il suo Case Else viene saltato. Un’altra stringa in route restituisce -1.
Option Explicit On
Sub Main()
    Dim route = "harvest"
    Dim trace = 0
    Select Case route
        Case "harvest", "loot"
            trace = 1
            Select Case 2
                Case 2
                    Try
                        Exit Select
                        trace = 99
                    Finally
                        trace = trace * 10 + 2
                    End Try
            End Select
            trace = trace * 10 + 3
        Case Else
            trace = -1
    End Select
    Return trace
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

route contiene harvest; il primo ramo imposta trace=1. Il Case 2 interno esegue Exit Select, salta trace=99 e Finally aggiunge 2. Il ramo esterno aggiunge 3: risultato 123. Il suo Case Else viene saltato. Un’altra stringa in route restituisce -1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: selectStatement / caseClause / caseTest / exitSelect
Analysis/LoopStructureValidator.cs: VisitSelectStatement / VisitExitSelect / VisitCodeBlock
Runtime/Instructions/Generator.cs: Generate(SelectStatementContext)
Runtime/Instructions/SelectInstruction.cs: SelectInstruction / CaseInstruction
Runtime/Interpreter.cs: CaseMatches / ResumeNextAddress / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/select-case-statement
-->
