# With / End With

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

With raggruppa operazioni sullo stesso oggetto acquisito. Il punto iniziale seleziona un membro di tale oggetto. With UO e With moduleName sono estensioni Basic per indicare esplicitamente uno spazio dei nomi.

## Sintassi esatta

```text
With objectExpression
    .Method(arguments)
    statements
End With
With UO
    .Command(arguments)
End With
With moduleName
    .field = expression
    .Procedure(arguments)
End With
```

## Parametri

- `objectExpression / UO / moduleName` — Destinatario obbligatorio: oggetto nativo List(), Dictionary(), variabile che contiene un oggetto o funzione che lo restituisce. L’espressione viene valutata una sola volta all’ingresso, anche con corpo vuoto. Numeri, stringhe, array e Unit non sono destinatari oggetto in questo motore. Una variabile locale oggetto ha precedenza su un modulo omonimo.
- `.Method(arguments) / .field` — Usare metodi con parentesi: .Add(value), .Item(index), .Count(). Parametri e risultati non cambiano; vedere Basic.List/Basic.Dictionary. Campi e proprietà arbitrari degli oggetti non sono supportati qui. Un modulo permette .field e .Procedure(arguments) accessibili; Private resta valido. In With UO, .Command(...) significa UO.Command(...); altrove i comandi di gioco richiedono ancora UO.
- `statements / End With` — Il corpo può essere vuoto o contenere chiamate, assegnazioni, condizioni e blocchi correttamente annidati. End With è obbligatorio. Un punto iniziale fuori dal corpo è un errore. Gli altri oggetti restano accessibili con il nome completo.

## Restituisce

With è un blocco di controllo senza risultato proprio: non restituisce ID, Boolean o stato di successo. Ogni metodo mantiene il suo contratto di ritorno. Nei tre esempi Return restituisce esplicitamente un Integer da Main; 127, 28 e 72 sono calcoli dimostrativi.

## Comportamento

- La preparazione convalida il blocco e associa i nomi relativi. All’ingresso l’interprete salva il riferimento ottenuto dall’espressione nella chiamata corrente. Riassegnare la variabile originale non cambia tale riferimento. Un nuovo ingresso rivaluta l’espressione; le chiamate ricorsive hanno riferimenti separati.
- L’intestazione del With interno usa il contesto esterno. Nel corpo il punto indica l’oggetto interno; End With ripristina il contesto esterno. Return, i trasferimenti dei cicli e GoTo verso l’esterno eliminano gli ambiti lasciati dopo i Finally applicabili. Saltare dentro il corpo di With è vietato.
- Un destinatario non valido o un metodo sconosciuto genera un errore, non false. Catch/On Error può gestirlo. Se fallisce il destinatario, On Error Resume Next salta l’intero blocco. With non ripete, non attende e non avvia thread. Pausa/arresto restano attivi. I nomi associati sono conservati con lo script preparato; il destinatario non viene rivalutato per ogni metodo.

## Esempi

### 1. Una sola valutazione

```vb
# Choose riceve values tramite ByVal e calls tramite ByRef, incrementa calls a 1 e restituisce la lista originale. Entrambi gli .Add inseriscono 2 e 7 nella lista acquisita, anche se values riceve una nuova lista tra le chiamate. Item usa gli indici 0 e 1. Main restituisce 1*100+2*10+7=127.
Option Explicit On
Function Choose(ByVal values, ByRef calls) As Object
    calls += 1
    Return values
End Function

Sub Main()
    Dim calls=0
    Dim values=List()
    Dim original=values
    With Choose(values, calls)
        .Add(2)
        values=List()
        .Add(7)
    End With
    Return calls*100+original.Item(0)*10+original.Item(1)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

Choose riceve values tramite ByVal e calls tramite ByRef, incrementa calls a 1 e restituisce la lista originale. Entrambi gli .Add inseriscono 2 e 7 nella lista acquisita, anche se values riceve una nuova lista tra le chiamate. Item usa gli indici 0 e 1. Main restituisce 1*100+2*10+7=127.

### 2. Annidamento e finalizzazione

```vb
# groups associa la chiave testuale "child" alla lista child. .Item("child") legge l’oggetto dal dizionario esterno. All’interno .Add(2) e .Add(7) nel Finally modificano la lista. Dopo End With, .Set("result",8) opera nuovamente sul dizionario. Count() restituisce 2, Item("result") restituisce 8: Main dà 28.
Option Explicit On
Sub Main()
    Dim groups=Dictionary()
    Dim child=List()
    groups.Set("child", child)
    With groups
        With .Item("child")
            Try
                .Add(2)
            Finally
                .Add(7)
            End Try
        End With
        .Set("result", 8)
    End With
    Return child.Count()*10+groups.Item("result")
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

groups associa la chiave testuale "child" alla lista child. .Item("child") legge l’oggetto dal dizionario esterno. All’interno .Add(2) e .Add(7) nel Finally modificano la lista. Dopo End With, .Set("result",8) opera nuovamente sul dizionario. Count() restituisce 2, Item("result") restituisce 8: Main dà 28.

### 3. Modulo e spazio UO

```vb
# With Tools qualifica .total, .AddAmount e .CountItems. total parte da 4; AddAmount riceve amount=3 tramite ByVal e porta total a 7. CountItems riceve un array di due elementi e chiama UO.GetArrayLength(values) tramite With UO, ottenendo 2. Main calcola 7*10+2=72. Le regole di accesso del modulo restano valide.
Option Explicit On
Module Tools
    Public Var total=0
    Public Sub AddAmount(ByVal amount)
        total += amount
    End Sub
    Public Function CountItems(ByVal values) As Integer
        With UO
            Return .GetArrayLength(values)
        End With
    End Function
End Module

Sub Main()
    Dim values[1]
    With Tools
        .total=4
        .AddAmount(3)
        Return .total*10+.CountItems(values)
    End With
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

With Tools qualifica .total, .AddAmount e .CountItems. total parte da 4; AddAmount riceve amount=3 tramite ByVal e porta total a 7. CountItems riceve un array di due elementi e chiama UO.GetArrayLength(values) tramite With UO, ottenendo 2. Main calcola 7*10+2=72. Le regole di accesso del modulo restano valide.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: withStatement / SYMBOL
Analysis/WithStructureValidator.cs: VisitWithStatement / VisitSubrutine / VisitTerminal
Runtime/ScriptBindings.cs: Builder.VisitWithStatement / Variable / CallName
Runtime/Instructions/Generator.cs: WithInstruction generation
Runtime/Instructions/WithInstruction.cs: CaptureName / StartAddress / EndAddress
Runtime/Interpreter.cs: CallSubrutine / TryGetObjectSubrutine / ResumeNextAddress
Runtime/ObjectTypes/NativeObjectTypeInference.cs: ResolveWithReceiver / Scope.VisitWithStatement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/with-end-with-statement
-->
