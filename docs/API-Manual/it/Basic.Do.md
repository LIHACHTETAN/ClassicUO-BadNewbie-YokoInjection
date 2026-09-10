# Do / Loop / While / Until / Repeat

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Do controlla prima o dopo il corpo. While ripete se vero; Until fino al vero. Repeat … Until è la forma storica supportata con controllo finale.

## Sintassi esatta

```text
Do While condition
    statements
Loop
Do Until condition
    statements
Loop
Do
    statements
Loop While condition
Do
    statements
Loop Until condition
Do
    statements
Loop
Repeat
    statements
Until condition
Continue Do
Exit Do
Break
```

## Parametri

- `condition / While / Until` — Espressione Boolean numerica 0/False o 1/True. While continua se vera, Until esce se vera. Rivalutata a ogni controllo; il testo non è convertito in Boolean.
- `position / Repeat` — Dopo Do la condizione può evitare il primo passaggio. Dopo Loop o Until di Repeat avviene almeno un passaggio. È ammessa una sola posizione della condizione. Do … Loop senza condizione richiede un’uscita esplicita.
- `statements / exit` — Corpo. Continue Do raggiunge il prossimo controllo; Exit Do esce dal Do o Repeat più vicino. Break esce dal ciclo più interno di qualsiasi tipo. RETURN termina tutta la procedura/funzione.

## Restituisce

Do, Loop, Repeat, Until ed Exit Do non restituiscono valori. Gli esempi restituiscono esplicitamente Integer 1,33,83 da Main: contatori combinati, non risultati Boolean di comandi.

## Comportamento

- La preparazione associa i blocchi e verifica i trasferimenti. Condizioni a entrambe le estremità dello stesso Do producono SC020. Il motore verifica nella posizione scelta e ripete secondo While/Until.
- Continue Do verifica comunque la condizione finale, se presente; con condizione iniziale ritorna all’intestazione. I Finally abbandonati vengono eseguiti esattamente una volta prima del trasferimento.
- Repeat esegue prima: verifica gli array vuoti prima dell’ingresso. Nessun timeout implicito. Per attendere il gioco usa Wait e una scadenza; pausa/arresto rimangono attivi.

## Esempi

### 1. Prima o dopo

```vb
# ready=True soddisfa già Until. Do Until ready esegue zero passaggi: before=0. Il secondo ciclo controlla dopo l’incremento, quindi after=1. Main restituisce before*10+after=1.
Option Explicit On
Sub Main()
    Var ready = True
    Var before = 0
    Var after = 0
    Do Until ready
        before += 1
    Loop
    Do
        after += 1
    Loop Until ready
    Return before * 10 + after
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

ready=True soddisfa già Until. Do Until ready esegue zero passaggi: before=0. Il secondo ciclo controlla dopo l’incremento, quindi after=1. Main restituisce before*10+after=1.

### 2. Tentativi limitati con pulizia

```vb
# attempts parte da 0 e aumenta a ogni passaggio. I primi due Continue Do eseguono Finally e il controllo attempts<4. Al terzo tentativo anche Exit Do esegue Finally. attempts=3, cleanup=3 danno 33. È una simulazione locale, non tentativi di rete reali.
Option Explicit On
Sub Main()
    Var attempts = 0
    Var cleanup = 0
    Do
        Try
            attempts += 1
            If attempts < 3 Then
                Continue Do
            End If
            Exit Do
        Finally
            cleanup += 1
        End Try
    Loop While attempts < 4
    Return attempts * 10 + cleanup
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

attempts parte da 0 e aumenta a ogni passaggio. I primi due Continue Do eseguono Finally e il controllo attempts<4. Al terzo tentativo anche Exit Do esegue Finally. attempts=3, cleanup=3 danno 33. È una simulazione locale, non tentativi di rete reali.

### 3. Ciclo storico con sentinella

```vb
# values=[3,5,0] non è vuoto. Repeat legge, incrementa index e somma. Until termina a zero o al limite dell’array; OrElse salta il secondo controllo quando trova zero. total=8 e index=3 producono 83.
Option Explicit On
Sub Main()
    Dim values[2]
    values[0] = 3
    values[1] = 5
    values[2] = 0
    Var index = 0
    Var value = 0
    Var total = 0
    Repeat
        value = values[index]
        index += 1
        total += value
    Until (value = 0) OrElse (index >= GetArrayLength(values))
    Return total * 10 + index
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

values=[3,5,0] non è vuoto. Repeat legge, incrementa index e somma. Until termina a zero o al limite dell’array; OrElse salta il secondo controllo quando trova zero. total=8 e index=3 producono 83.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(DoLoopContext) / VisitStatement(Repeat/Until)
Runtime/Interpreter.cs: LoopConditionInstruction / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/do-loop-statement
-->
