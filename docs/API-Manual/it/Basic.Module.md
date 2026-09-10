# Module / End Module

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Module raggruppa funzioni, procedure, VAR/DIM e CONST sotto un nome. Dall’esterno si usano Tools.Sum o Counter.count; nel modulo corrente sono ammessi nomi brevi.

## Sintassi esatta

```text
Module moduleName
    members
End Module
moduleName.member(arguments)
moduleName.field
```

## Parametri

- `moduleName` — moduleName: identificatore semplice senza distinzione maiuscole/minuscole, ad esempio Tools. UO è riservato. Nomi duplicati e moduli annidati non sono ammessi.
- `members` — members: SUB/FUNCTION, VAR/DIM scalari, CONST, Include e una direttiva Option Explicit valida. Un campo può contenere array o oggetti. DIM[...] direttamente nel modulo non è supportato; creare l’array con una funzione e salvarlo in VAR.
- `member / arguments` — member / arguments: nome del membro e argomenti della funzione. Tools.Sum(2, 3) passa left=2 e right=3. Il campo Counter.count si legge senza parentesi.

## Restituisce

Module non restituisce un valore e non si chiama come Module(...). Tools.Sum(...) restituisce il RETURN della funzione; un campo fornisce il valore memorizzato. I confronti restituiscono Integer 1/0, equivalenti a TRUE/FALSE in condizioni e confronti. Un numero, ID o conteggio generico non è automaticamente un risultato booleano.

## Comportamento

- Dichiarare Module a livello di file e chiudere con End Module. Include può caricare un modulo o i suoi membri; gli errori conservano file e riga originali. Option Explicit appartiene al file fisico.
- La preparazione raccoglie i nomi qualificati, associa quelli brevi al modulo corrente e verifica gli accessi prima dell’esecuzione. Un parametro, VAR, CONST o DIM locale esplicito nasconde un campo omonimo. Altrimenti si cerca il campo del modulo e poi la variabile globale tradizionale.
- I campi si inizializzano nell’ordine delle dichiarazioni a ogni nuovo avvio. Le chiamate annidate dello stesso avvio condividono le modifiche. Un altro avvio riparte da zero; gli script concorrenti non condividono lo stato del modulo. Non viene salvato su disco.
- Funzioni/procedure sono Public per impostazione predefinita; campi/costanti sono Private. Private richiede Module. Vedere Public / Private.
- L’IDE mostra i nomi qualificati. Le procedure pubbliche senza argomenti obbligatori si avviano dall’elenco; gli aiutanti privati restano interni. Completamento, navigazione e variabili rispettano il modulo corrente.

## Esempi

### 1. Nomi uguali in moduli diversi

```vb
# Tools.Sum somma left=2 e right=3 restituendo 5; Other.Sum li moltiplica restituendo 6. I nomi qualificati distinguono le funzioni. Main restituisce Integer 11.
Option Explicit On
Module Tools
    Public Function Sum(ByVal left, ByVal right)
        Return left + right
    End Function
End Module
Module Other
    Public Function Sum(ByVal left, ByVal right)
        Return left * right
    End Function
End Module
Sub Main()
    Return Tools.Sum(2, 3) + Other.Sum(2, 3)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

Tools.Sum somma left=2 e right=3 restituendo 5; Other.Sum li moltiplica restituendo 6. I nomi qualificati distinguono le funzioni. Main restituisce Integer 11.

### 2. Campo condiviso in un avvio

```vb
# count inizia da 0. Ogni Increment aggiunge 1 allo stesso campo; dopo due chiamate before=2. Read vede Counter.count=5. Main restituisce 2*10+5, Integer 25. Un nuovo avvio riparte da 0.
Option Explicit On
Module Counter
    Public Var count As Integer = 0
    Public Sub Increment()
        count += 1
    End Sub
    Public Function Read()
        Return count
    End Function
End Module
Sub Main()
    Counter.Increment()
    Counter.Increment()
    Var before = Counter.Read()
    Counter.count = 5
    Return before * 10 + Counter.Read()
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

count inizia da 0. Ogni Increment aggiunge 1 allo stesso campo; dopo due chiamate before=2. Read vede Counter.count=5. Main restituisce 2*10+5, Integer 25. Un nuovo avvio riparte da 0.

### 3. Risultato booleano

```vb
# maximum=4 è disponibile dentro Limits. Allowed(3) restituisce Integer 1; Allowed(7) Integer 0. accepted=TRUE e rejected=FALSE verificano i risultati. Main restituisce Integer 10 se entrambi sono corretti.
Option Explicit On
Module Limits
    Private Const maximum = 4
    Public Function Allowed(ByVal amount)
        Return amount <= maximum
    End Function
End Module
Sub Main()
    Var accepted = Limits.Allowed(3)
    Var rejected = Limits.Allowed(7)
    If accepted = TRUE AndAlso rejected = FALSE Then
        Return 10
    End If
    Return 0
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

maximum=4 è disponibile dentro Limits. Allowed(3) restituisce Integer 1; Allowed(7) Integer 0. accepted=TRUE e rejected=FALSE verificano i risultati. Main restituisce Integer 10 se entrambi sono corretti.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: moduleDeclaration / moduleSection
Runtime/DeclarationScope.cs: Qualify / IsPrivate
Runtime/ScriptBindings.cs: Builder.Variable / CallName
Runtime/SemanticScope.cs: Scope / DefineGlobalVariables
Runtime/Interpreter.cs: EvaluateBoundExpression / CallSubrutine
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/module-statement
-->
