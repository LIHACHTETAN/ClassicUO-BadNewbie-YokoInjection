# Basic / UO.

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

I comandi di gioco usano UO.; Basic e le funzioni personali usano i nomi dichiarati.

## Sintassi esatta

```text
UO.command(arguments)
BasicFunction(arguments)
UserFunction(arguments)
```

## Parametri

- `UO.command` — UO.command(arguments): prefisso obbligatorio del gioco. UO.GetType(id) legge grafica/corpo, non un tipo Basic o CLR.
- `BasicFunction` — BasicFunction(arguments): ad esempio Int(value), Str(value), CInt(value), senza UO.
- `arguments` — self, backpack, ground e Rhand mantengono il significato di argomenti oggetto, filtro o livello; non sono chiamate abbreviate.

## Restituisce

La regola dei nomi non restituisce valori. Int restituisce Integer, Str String; i tre Api*Exists restituiscono Integer 1/0, utilizzabili come TRUE/FALSE.

## Comportamento

- Maiuscole e minuscole sono equivalenti. InjectionApi registra Basic senza prefisso, InjectionApiUO il gioco con UO. Una vecchia chiamata breve produce SC005 e suggerisce UO.; nessuna sostituzione viene eseguita implicitamente. Anche i valori degli attributi richiedono UO. ApiNameExists, ApiSignatureExists e ApiParameterExists eliminano gli spazi esterni e controllano il nome registrato esatto senza aggiungere prefissi. Leggono metadati, non lo stato del server. GetType(TypeName), operatore di riflessione VB.NET, non è implementato.

## Esempi

### 1. 1

```vb
# graphic legge il corpo o 0 senza dati; whole=2. registered controlla UO.GetType con un argomento. Main restituisce "2:1" indipendentemente dalla grafica, senza movimento o trasferimento.
Option Explicit On
Sub Main()
    Var graphic = UO.GetType('self')
    Var whole = Int(2.9)
    Var registered = UO.ApiSignatureExists('UO.GetType', 1)
    Return CStr(whole) + ":" + CStr(registered)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

graphic legge il corpo o 0 senza dati; whole=2. registered controlla UO.GetType con un argomento. Main restituisce "2:1" indipendentemente dalla grafica, senza movimento o trasferimento.

### 2. 2

```vb
# La Function GetType completa riceve value=6 da CInt(6) e restituisce 7. UO.GetType continua a leggere la grafica di gioco. Le due chiamate restano distinte.
Option Explicit On
Function GetType(value)
    Return value + 1
End Function
Sub Main()
    Var localResult = GetType(CInt(6))
    Var graphic = UO.GetType('self')
    Return localResult
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

La Function GetType completa riceve value=6 da CInt(6) e restituisce 7. UO.GetType continua a leggere la grafica di gioco. Le due chiamate restano distinte.

### 3. 3

```vb
# oldCall=0, gameCall=1 e basicCall=1 controllano GetType, UO.GetType(id) e Int(value). argumentName=1 conferma backpack come selettore. Main restituisce "0:1:1:1". Le procedure personali non vengono cercate.
Option Explicit On
Sub Main()
    Var oldCall = UO.ApiSignatureExists('GetType', 1)
    Var gameCall = UO.ApiSignatureExists('UO.GetType', 1)
    Var basicCall = UO.ApiSignatureExists('Int', 1)
    Var argumentName = UO.ApiParameterExists('backpack')
    Return CStr(oldCall) + ":" + CStr(gameCall) + ":" + CStr(basicCall) + ":" + CStr(argumentName)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

oldCall=0, gameCall=1 e basicCall=1 controllano GetType, UO.GetType(id) e Int(value). argumentName=1 conferma backpack come selettore. Main restituisce "0:1:1:1". Le procedure personali non vengono cercate.

<!-- implementation references (not callable script procedures):
Runtime/InjectionApi.cs: Register
Runtime/InjectionApiUO.cs: Register / RegisterCharacterGetterAliases / ApiNameExists / ApiSignatureExists / ApiParameterExists
Analysis/InvalidSymbolVisitor.cs: VisitCall
Runtime/ScriptBindings.cs: Builder.CallName
-->
