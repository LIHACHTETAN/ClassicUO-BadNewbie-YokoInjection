# Wait Until / Timeout

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

Wait Until verifica una condizione fino al successo o alla scadenza. È un’estensione Basic, non un’istruzione VB.NET. Lavora nello script corrente senza creare thread o avviare altre procedure.

## Sintassi esatta

```text
Wait Until condition Timeout milliseconds
```

## Parametri

- `condition` — condition viene valutata subito e poi tra brevi attese. Usare Boolean o un confronto: il numero 0 significa false, gli altri valori seguono If. Il testo "false" non è Boolean false. Sono possibili chiamate UO e funzioni proprie; gli errori si propagano e gli effetti si ripetono a ogni verifica.
- `Timeout milliseconds` — Timeout è obbligatorio. milliseconds viene valutato una volta prima della condizione: Integer 0..2147483647. Numeri negativi, frazioni e Strings generano prima un errore. Zero permette solo la verifica immediata. Altrove timeout rimane un nome di variabile valido.

## Restituisce

L’istruzione non restituisce valori. Il successo continua alla riga seguente; la scadenza genera un errore con file e riga, gestibile da Try/Catch o On Error. Altrimenti fallisce l’esecuzione corrente. Nessun false automatico: l’esempio 2 crea una funzione che restituisce True/1 o False/0.

## Comportamento

- Il motore memorizza la durata e avvia uno Stopwatch monotono. La prima verifica immediata può riuscire anche con limite zero. Dopo false il ciclo controlla annullamento e pausa, calcola il residuo e attende al massimo 10 ms prima della prossima verifica. Non è un ciclo attivo continuo; la pianificazione del sistema può allungare l’intervallo.
- La pausa sospende le verifiche ma il tempo reale conta nel limite. Alla ripresa una scadenza viene segnalata prima di verificare ancora. Stop interrompe l’attesa e salta Catch/Finally dello script come gli altri arresti d’emergenza. Non può interrompere forzatamente una chiamata bloccata dentro condition: usare funzioni brevi. Una verifica iniziata termina prima di elaborarne risultato o errore.
- Un errore della condizione non diventa timeout. Errori normali e scadenze eseguono i Finally applicabili. Le variabili appartengono alla chiamata corrente; un nuovo ingresso riavvia il limite. Non esistono End Wait o un parametro aggiuntivo di intervallo. Wait(milliseconds) resta una funzione separata di ritardo.

## Esempi

### 1. Controllare una funzione entro un limite

```vb
# checks parte da 0; Ready lo riceve ByRef e incrementa a ogni verifica. required=3 è ByVal e budget=5000 concede cinque secondi. Due verifiche restituiscono false, la terza true; Main restituisce Integer 3. È un esempio deterministico, non un server simulato: sostituire la condizione con lo stato reale desiderato.
Option Explicit On
Function Ready(ByRef checks As Integer, ByVal required As Integer) As Boolean
    checks += 1
    Return checks >= required
End Function

Sub Main()
    Dim checks As Integer = 0
    Const budget = 5000
    Wait Until Ready(checks, 3) Timeout budget
    Return checks
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

checks parte da 0; Ready lo riceve ByRef e incrementa a ogni verifica. required=3 è ByVal e budget=5000 concede cinque secondi. Due verifiche restituiscono false, la terza true; Main restituisce Integer 3. È un esempio deterministico, non un server simulato: sostituire la condizione con lo stato reale desiderato.

### 2. Restituire Boolean da una propria funzione

```vb
# TryWait riceve ready=False e budget=0. Il test immediato fallisce con timeout. Catch problem restituisce False; Main restituisce 0, confrontabile con False. ready=True darebbe 1/True. La funzione cattura tutti gli errori: esaminare problem per distinguerli. ready è un valore Boolean, non un callback.
Option Explicit On
Function TryWait(ByVal ready As Boolean, ByVal budget As Integer) As Boolean
    Try
        Wait Until ready Timeout budget
        Return True
    Catch problem
        Return False
    End Try
End Function

Sub Main()
    Dim success = TryWait(False, 0)
    Return success
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

TryWait riceve ready=False e budget=0. Il test immediato fallisce con timeout. Catch problem restituisce False; Main restituisce 0, confrontabile con False. ready=True darebbe 1/True. La funzione cattura tutti gli errori: esaminare problem per distinguerli. ready è un valore Boolean, non un callback.

### 3. Conservare l’errore e finalizzare

```vb
# CheckStatus con state=-1 genera subito "disconnected". Il limite di 3000 ms non sostituisce l’errore. Catch copia problem in message; Finally imposta finished=True/1. Main restituisce "disconnected:1". state=1 riuscirebbe subito, state=0 resterebbe false fino alla scadenza. Non serve una connessione al gioco.
Option Explicit On
Function CheckStatus(ByVal state As Integer) As Boolean
    If state < 0 Then
        Throw "disconnected"
    End If
    Return state = 1
End Function

Sub Main()
    Dim message = ""
    Dim finished = False
    Try
        Wait Until CheckStatus(-1) Timeout 3000
    Catch problem
        message = problem
    Finally
        finished = True
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

CheckStatus con state=-1 genera subito "disconnected". Il limite di 3000 ms non sostituisce l’errore. Catch copia problem in message; Finally imposta finished=True/1. Main restituisce "disconnected:1". state=1 riuscirebbe subito, state=0 resterebbe false fino alla scadenza. Non serve una connessione al gioco.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: waitUntilStatement / WAIT_UNTIL
Analysis/LoopStructureValidator.cs: VisitWaitUntilStatement
Runtime/Interpreter.cs: VisitWaitUntilStatement / Failure
Runtime/InjectionRuntime.cs: executionCheckpoint / retrieveCancellationToken
-->
