# Enum / End Enum

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Enum raggruppa costanti Integer con nomi per gli stati dello script. Dichiararlo nel file o in Module, fuori da Sub/Function. È un sottoinsieme di VB.NET, senza creare oggetti .NET Enum.

## Sintassi esatta

```text
[Public | Private] Enum name [As Integer]
    member [= constantExpression]
    ...
End Enum
Dim state As name = name.member
ModuleName.name.member
```

## Parametri

- `Public / Private` — Public è predefinito, anche in Module. Private è consentito solo in Module e nasconde tipo e membri agli altri moduli e al file.
- `name` — Nome semplice senza punti, come Mode; maiuscole e minuscole equivalenti. UO e tipi incorporati sono riservati. Il nome completo non può duplicare Enum, Module o variabili globali.
- `As Integer` — Facoltativo; solo Integer con segno a 32 bit, -2147483648..2147483647. Altri tipi base sono rifiutati. As Mode per variabile, parametro o risultato Function usa memoria e conversione Integer; non limita i valori ai membri elencati. Senza inizializzazione vale 0.
- `member` — Un nome semplice per riga, almeno un membro. Duplicati, True e False vietati. Senza espressione si parte da 0, poi si aggiunge 1 al valore precedente. Nomi diversi possono avere lo stesso valore.
- `constantExpression` — Espressione costante facoltativa: interi decimali/0x, parentesi, meno unario, + - * / Mod, membri precedenti e Const numeriche già dichiarate. Risultato finale intero nell’intervallo; divisioni intermedie anche frazionarie. Una Const usata deve produrre Integer, senza tipo o As Integer/Long/Short/Byte. Niente chiamate, variabili, String, confronti o letture di array. Riferimenti futuri, cicli e dipendenze oltre 128 livelli sono rifiutati.
- `name.member` — Leggere Mode.Ready o, fuori dal modulo, Tools.Mode.Ready. Dentro Tools basta Mode.Ready; With Mode consente .Ready. Assegnazioni, += e scrittura di ritorno ByRef non possono modificare costanti. Enum non è una funzione.

## Restituisce

La dichiarazione non restituisce valori e non richiede parentesi di chiamata. Un membro restituisce Integer, ad esempio Mode.Working = 3: è uno stato, non un successo automatico. Il confronto state = Mode.Finished restituisce 1/True o 0/False, utilizzabili in entrambe le forme. Lo stato 0 può significare Idle, non errore.

## Comportamento

- EnumCatalog prepara i valori precedenti senza eseguire script/API, assegna quelli automatici e verifica nomi, accesso e limiti. SC026 blocca l’avvio anche senza Option Explicit. Anche gli errori sintattici bloccano; il testo incompleto nell’editor produce diagnosi.
- DefinitionCollector inserisce i membri costanti prima degli inizializzatori globali e dei valori Optional: questi possono usare Enum dichiarati più avanti. Dentro Enum servono sempre costanti precedenti. Il catalogo resta nello script preparato e viene sostituito caricando un altro script.
- ScriptBindings risolve una volta nomi di modulo e Private. L’esecuzione legge costanti senza ricalcoli nei cicli o reflection. As Mode diventa Integer, che può apparire nel debugger. Include può fornire la dichiarazione. Nessun attributo Flags, metodo System.Enum, importazione implicita o elenco automatico dei membri.

## Esempi

### 1. Dare nomi agli stati

```vb
# Idle=0 e Queued=1 sono automatici. Working=10 cambia la sequenza, Finished=11. state As TaskState riceve 10. Main restituisce String "0:1:10:11"; CStr converte i numeri. Adattare i nomi al proprio script; la dichiarazione non avvia procedure.
Option Explicit On
Enum TaskState As Integer
    Idle
    Queued
    Working = 10
    Finished
End Enum

Sub Main()
    Dim state As TaskState = TaskState.Working
    Return CStr(TaskState.Idle) & ":" & CStr(TaskState.Queued) & ":" & CStr(state) & ":" & CStr(TaskState.Finished)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

Idle=0 e Queued=1 sono automatici. Working=10 cambia la sequenza, Finished=11. state As TaskState riceve 10. Main restituisce String "0:1:10:11"; CStr converte i numeri. Adattare i nomi al proprio script; la dichiarazione non avvia procedure.

### 2. Nascondere lo stato del modulo

```vb
# Controller.Mode è interno. NextMode riceve distance ByVal As Integer senza modificare l’argomento chiamante. distance<=1 sceglie Arrived=5, altrimenti Walking=4; state parte da 0. Main passa 3 e 1, riceve 4 e 5 e restituisce Integer 45. Nessun movimento: distance è un input dimostrativo. Fuori è accessibile Controller.NextMode, non Controller.Mode.Arrived.
Option Explicit On
Module Controller
    Private Enum Mode
        Idle
        Walking = 4
        Arrived
    End Enum

    Public Function NextMode(ByVal distance As Integer) As Integer
        Dim state As Mode
        If distance <= 1 Then
            state = Mode.Arrived
        Else
            state = Mode.Walking
        End If
        Return state
    End Function
End Module

Sub Main()
    Dim farState = Controller.NextMode(3)
    Dim nearState = Controller.NextMode(1)
    Return farState * 10 + nearState
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

Controller.Mode è interno. NextMode riceve distance ByVal As Integer senza modificare l’argomento chiamante. distance<=1 sceglie Arrived=5, altrimenti Walking=4; state parte da 0. Main passa 3 e 1, riceve 4 e 5 e restituisce Integer 45. Nessun movimento: distance è un input dimostrativo. Fuori è accessibile Controller.NextMode, non Controller.Mode.Arrived.

### 3. Cambiare stato e restituire Boolean

```vb
# La precedente Const Integer FirstState=2 produce Idle=2, Working=3, Finished=4. Advance riceve state ByRef e modifica la variabile di Main; With Mode abbrevia i nomi, Select Case sceglie il passaggio. Due chiamate danno 2→3→4. IsFinal riceve una copia ByVal e confronta Finished: Main restituisce 1/True; dopo un solo passaggio sarebbe 0/False. Un altro Advance genera "No next state". Le costanti restano immutate.
Option Explicit On
Const FirstState As Integer = 2
Enum Mode
    Idle = FirstState
    Working = Idle + 1
    Finished
End Enum

Sub Advance(ByRef state As Mode)
    With Mode
        Select Case state
            Case .Idle
                state = .Working
            Case .Working
                state = .Finished
            Case Else
                Throw "No next state"
        End Select
    End With
End Sub

Function IsFinal(ByVal state As Mode) As Boolean
    Return state = Mode.Finished
End Function

Sub Main()
    Dim state As Mode = Mode.Idle
    Advance(state)
    Advance(state)
    Return IsFinal(state)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

La precedente Const Integer FirstState=2 produce Idle=2, Working=3, Finished=4. Advance riceve state ByRef e modifica la variabile di Main; With Mode abbrevia i nomi, Select Case sceglie il passaggio. Due chiamate danno 2→3→4. IsFinal riceve una copia ByVal e confronta Finished: Main restituisce 1/True; dopo un solo passaggio sarebbe 0/False. Un altro Advance genera "No next state". Le costanti restano immutate.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: enumDeclaration / enumMember
Runtime/EnumCatalog.cs: Build / Observe / Reference / Evaluate
Runtime/DefinitionCollector.cs: VisitFile / VisitEnumDeclaration
Runtime/ScriptBindings.cs: Variable / VisitTypeClause / VisitWithStatement
Runtime/SemanticScope.cs: DefineGlobalVariables / SetVar
Runtime/Metadata.cs: NormalizeType
-->
