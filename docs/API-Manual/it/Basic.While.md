# While / Wend / Exit While / Break

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

While controlla prima di ogni passaggio e ripete quando la condizione è vera. Questo motore chiude con Wend; End While di VB.NET non è supportato.

## Sintassi esatta

```text
While condition
    statements
Wend
Continue While
Exit While
Break
```

## Parametri

- `condition` — Espressione rivalutata a ogni controllo, compresi primo e ultimo. Usa confronti o Boolean numerici: 0/False termina, 1/True e altri numeri non nulli continuano. Il testo non è interpretato come Boolean.
- `statements` — Istruzioni che svolgono il lavoro e fanno avanzare la condizione. Se il primo controllo è falso, tutto il corpo viene saltato.
- `Wend / exit` — Wend torna al controllo. Continue While lo ripete; Exit While esce dal While più vicino anche attraverso un ciclo interno di altro tipo. Break esce dal ciclo più interno di qualsiasi tipo.

## Restituisce

While, Wend, Exit While e Break non restituiscono valori. RETURN nel corpo termina tutta la procedura/funzione. Esempi: Integer 6,1,406. Il risultato di ricerca 1 è un indice, non un indicatore Boolean.

## Comportamento

- Sequenza: controllo, corpo, ritorno al controllo. Nessun limite numerico memorizzato e nessun incremento automatico.
- Programma esplicitamente l’avanzamento. Per interrogare periodicamente il gioco aggiungi un Wait adeguato e una scadenza: While non attende e non scade da solo. Pausa e arresto rimangono disponibili.
- Continue e uscita eseguono i Finally dei Try abbandonati. Intestazione, istruzioni e Wend su righe separate dentro una procedura o funzione.

## Esempi

### 1. Somma delle cifre

```vb
# DigitSum riceve number=123 ByVal. MOD 10 legge l’ultima cifra, Fix(number/10) la rimuove: 123→12→1→0. total=3+2+1=6. Il controllo finale falso esce; Main riceve 6. Con 0 il corpo non parte e il risultato è 0.
Option Explicit On
Function DigitSum(ByVal number)
    Var total = 0
    While number > 0
        total += number MOD 10
        number = Fix(number / 10)
    Wend
    Return total
End Function
Sub Main()
    Return DigitSum(123)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

DigitSum riceve number=123 ByVal. MOD 10 legge l’ultima cifra, Fix(number/10) la rimuove: 123→12→1→0. total=3+2+1=6. Il controllo finale falso esce; Main riceve 6. Con 0 il corpo non parte e il risultato è 0.

### 2. Primo elemento corrispondente

```vb
# FirstAbove riceve values=[4,7,9], threshold=6. Il limite protegge values[index]. All’indice 1, 7>6 assegna found=1 e Exit While interrompe. Senza corrispondenze resta -1. Main restituisce l’indice a base zero 1.
Option Explicit On
Function FirstAbove(ByVal values, ByVal threshold)
    Var index = 0
    Var found = -1
    While index < GetArrayLength(values)
        If values[index] > threshold Then
            found = index
            Exit While
        End If
        index += 1
    Wend
    Return found
End Function
Sub Main()
    Dim values[2]
    values[0] = 4
    values[1] = 7
    values[2] = 9
    Return FirstAbove(values, 6)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

FirstAbove riceve values=[4,7,9], threshold=6. Il limite protegge values[index]. All’indice 1, 7>6 assegna found=1 e Exit While interrompe. Senza corrispondenze resta -1. Main restituisce l’indice a base zero 1.

### 3. Contare i controlli

```vb
# CanContinue riceve checks ByRef, index e limit=3 ByVal, incrementa checks e restituisce index<limit come 1/0. Controlli agli indici 0,1,2,3: quattro chiamate per tre passaggi. total=6; Main restituisce 406.
Option Explicit On
Function CanContinue(ByRef checks, ByVal index, ByVal limit)
    checks += 1
    Return index < limit
End Function
Sub Main()
    Var checks = 0
    Var index = 0
    Var total = 0
    While CanContinue(checks, index, 3)
        index += 1
        total += index
    Wend
    Return checks * 100 + total
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

CanContinue riceve checks ByRef, index e limit=3 ByVal, incrementa checks e restituisce index<limit come 1/0. Controlli agli indici 0,1,2,3: quattro chiamate per tre passaggi. total=6; Main restituisce 406.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(WhileContext)
Runtime/Interpreter.cs: WhileInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/while-end-while-statement
-->
