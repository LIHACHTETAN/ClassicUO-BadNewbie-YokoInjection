# Public / Private

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Public espone un membro del modulo al codice esterno. Private limita l’accesso a funzioni, procedure e inizializzatori dello stesso modulo. Il modificatore precede la dichiarazione, non la chiamata.

## Sintassi esatta

```text
Public declaration
Private declaration
```

## Parametri

- `visibility` — visibility: Public o Private. Senza modificatore, SUB/FUNCTION del modulo sono pubblici e VAR/DIM/CONST sono privati.
- `declaration` — declaration: SUB/FUNCTION, VAR/DIM scalare o CONST. Public vale anche per Module e dichiarazioni a livello di file. Private non è ammesso a livello di file o nel corpo di una procedura. Dichiarare nomi senza punto.

## Restituisce

Public e Private non restituiscono valori e non modificano tipi o risultati. Normalize(12) restituisce Integer 10 con RETURN; NextCount() restituisce il nuovo conteggio, non TRUE/FALSE.

## Comportamento

- Dentro Module sono ammessi nomi brevi e qualificati dei propri membri. Il codice esterno accede solo ai Public mediante ModuleName.Member. Public non crea un nome globale breve.
- Gli accessi vengono verificati prima dell’esecuzione anche con Option Explicit Off: Private di un altro modulo produce SC019; dichiarazioni errate di modulo/modificatore producono SC018 o errori sintattici. Gli inizializzatori non partono dopo tali errori.
- Una funzione pubblica può chiamare un aiutante privato: conta il modulo in cui è dichiarata la chiamante. Un aiutante privato non si avvia separatamente dall’IDE, da un tasto rapido o dall’API esterna delle procedure.
- Public Const resta costante e Public Var modificabile. Una variabile locale esplicita nasconde un campo omonimo solo nella propria procedura. Private non cifra il sorgente né lo nasconde al proprietario.
- Il debugger risolve nomi brevi e Private nel contesto del frame selezionato. Il campo è visibile nel modulo; scegliendo il chiamante esterno, ModuleName.privateField viene rifiutato.

## Esempi

### 1. Interfaccia pubblica e aiutante privato

```vb
# value=12 passa a Limits.Normalize, poi Clamp. maximum=10 limita il risultato; entrambi restituiscono Integer 10. Main chiama solo Normalize. La chiamata esterna Limits.Clamp(12) è vietata.
Option Explicit On
Module Limits
    Private Const maximum = 10
    Private Function Clamp(ByVal value)
        If value > maximum Then
            Return maximum
        End If
        Return value
    End Function
    Public Function Normalize(ByVal value)
        Return Clamp(value)
    End Function
End Module
Sub Main()
    Return Limits.Normalize(12)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

value=12 passa a Limits.Normalize, poi Clamp. maximum=10 limita il risultato; entrambi restituiscono Integer 10. Main chiama solo Normalize. La chiamata esterna Limits.Clamp(12) è vietata.

### 2. Campo privato e variabile locale

```vb
# VAR value=7 senza modificatore è privata in Store. Read restituisce il campo 7. LocalValue usa una propria value=9 senza cambiare il campo. Main restituisce 7*10+9, Integer 79.
Option Explicit On
Module Store
    Var value = 7
    Public Function Read()
        Return value
    End Function
    Public Function LocalValue()
        Var value = 9
        Return value
    End Function
End Module
Sub Main()
    Return Store.Read() * 10 + Store.LocalValue()
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

VAR value=7 senza modificatore è privata in Store. Read restituisce il campo 7. LocalValue usa una propria value=9 senza cambiare il campo. Main restituisce 7*10+9, Integer 79.

### 3. Costante pubblica, contatore privato

```vb
# Public Const increment=2 si legge come Counter.increment. Private count parte da 1. NextCount aggiunge increment, salva e restituisce 3. Main restituisce 3*10+2, Integer 32. Accesso esterno a Counter.count e modifica di increment sono vietati.
Option Explicit On
Module Counter
    Public Const increment = 2
    Private Var count = 1
    Public Function NextCount()
        count += increment
        Return count
    End Function
End Module
Sub Main()
    Var result = Counter.NextCount()
    Return result * 10 + Counter.increment
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

Public Const increment=2 si legge come Counter.increment. Private count parte da 1. NextCount aggiunge increment, salva e restituisce 3. Main restituisce 3*10+2, Integer 32. Accesso esterno a Counter.count e modifica di increment sono vietati.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: visibility / globalVar / globalConst / subrutine
Runtime/ScriptBindings.cs: CheckAccess / CheckDeclaration
Runtime/InjectionRuntime.cs: BlockingLanguageError / CallSubrutineValues
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: DiscoverScopedProcedures / RunProcedure
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/private
-->
