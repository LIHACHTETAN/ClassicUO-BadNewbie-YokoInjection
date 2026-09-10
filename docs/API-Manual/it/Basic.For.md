# For / To / Step / Next / Exit For

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

For ripete un blocco lungo un intervallo numerico inclusivo. Serve per indici o un numero noto di operazioni; For Each visita i valori degli elementi.

## Sintassi esatta

```text
For [VAR] counter = start To limit [Step increment]
    statements
Next [counter]
Continue For
Exit For
Break
```

## Parametri

- `counter / VAR` — Contatore scalare modificabile. VAR lo dichiara nella procedura; altrimenti usa una variabile esistente. Con Option Explicit On dichiaralo prima o usa For Var. Per un tipo esplicito scrivi DIM counter AS Integer prima del ciclo: AS nell’intestazione numerica non è supportato.
- `start` — Espressione numerica iniziale, valutata una volta e assegnata prima di limit e increment.
- `limit` — Estremo incluso, valutato una volta all’ingresso. Passo positivo: counter <= limit; negativo: counter >= limit.
- `increment` — Passo numerico facoltativo, predefinito 1. Ammessi valori negativi e frazionari; zero causa un errore intercettabile. Tipo e passo devono permettere l’avanzamento.
- `statements / Next / exit` — Corpo e Next su righe separate. Il nome facoltativo dopo Next deve corrispondere. Continue For passa al prossimo passo; Exit For esce dal For/For Each più vicino; Break esce dal ciclo più interno di qualsiasi tipo.

## Restituisce

For, Next ed Exit For non restituiscono valori. Il contatore è un numero, non automaticamente un ID. Alla fine normale il motore conserva l’ultimo valore eseguito, non un valore oltre il limite. Un ciclo saltato conserva start; un’uscita anticipata il valore corrente. Gli esempi restituiscono Integer 12,28,395.

## Comportamento

- Ingresso: assegnare start, memorizzare limite e passo, rifiutare zero, controllare il primo valore. Una direzione incompatibile salta il corpo; start=limit lo esegue una volta.
- Next controlla counter+step e lo assegna solo se resta nell’intervallo. 1 To 5 Step 3 visita 1 e 4. Cambiare le variabili originali del limite/passo non cambia i valori memorizzati; cambiare il contatore influenza il passo successivo.
- Struttura e nome Next vengono verificati prima dell’esecuzione; errori strutturali danno SC020. Usa contatori diversi nei cicli annidati. Uscire da Try esegue Finally. Pausa/arresto restano attivi; nessun ritardo o timeout automatico.

## Esempi

### 1. Sommare le celle

```vb
# values[2] crea gli indici 0,1,2 con valori 2,4,6. Sum riceve l’array ByVal, parte da index=0 e memorizza length-1=2. Il passo implicito 1 visita tre celle; total=12 ritorna a Main.
Option Explicit On
Function Sum(ByVal items)
    Var total = 0
    For Var index = 0 To GetArrayLength(items) - 1
        total += items[index]
    Next index
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return Sum(values)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

values[2] crea gli indici 0,1,2 con valori 2,4,6. Sum riceve l’array ByVal, parte da index=0 e memorizza length-1=2. Il passo implicito 1 visita tre celle; total=12 ritorna a Main.

### 2. Eliminare dalla fine

```vb
# items contiene -1,3,-2,5. Inizio Count()-1=3, limite 0, passo -1. Eliminare un valore negativo sposta solo indici già visitati, senza saltare elementi ancora da leggere. Restano 3 e 5; Count()*10+3+5 restituisce 28.
Option Explicit On
Sub Main()
    Var items = List()
    items.Add(-1)
    items.Add(3)
    items.Add(-2)
    items.Add(5)
    For Var index = items.Count() - 1 To 0 Step -1
        If items[index] < 0 Then
            items.RemoveAt(index)
        End If
    Next index
    Return items.Count() * 10 + items[0] + items[1]
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

items contiene -1,3,-2,5. Inizio Count()-1=3, limite 0, passo -1. Eliminare un valore negativo sposta solo indici già visitati, senza saltare elementi ancora da leggere. Restano 3 e 5; Count()*10+3+5 restituisce 28.

### 3. Limiti memorizzati e contatore finale

```vb
# ReadLimit incrementa calls ByRef e restituisce value. Inizio=1, limite=5, passo=2 sono valutati una volta ciascuno: calls=3. upper=99 e stride=1 nel corpo non li cambiano. Visite 1,3,5; total=9, index resta 5. Main restituisce 395.
Option Explicit On
Function ReadLimit(ByRef calls, ByVal value)
    calls += 1
    Return value
End Function
Sub Main()
    Var calls = 0
    Var upper = 5
    Var stride = 2
    Var total = 0
    For Var index = ReadLimit(calls, 1) To ReadLimit(calls, upper) Step ReadLimit(calls, stride)
        total += index
        upper = 99
        stride = 1
    Next index
    Return calls * 100 + total * 10 + index
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

ReadLimit incrementa calls ByRef e restituisce value. Inizio=1, limite=5, passo=2 sono valutati una volta ciascuno: calls=3. upper=99 e stride=1 nel corpo non li cambiano. Visite 1,3,5; total=9, index resta 5. Main restituisce 395.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretFor / CallSubrutine
Runtime/ForScope.cs: ContainsCurrent / HasNext
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-next-statement
-->
