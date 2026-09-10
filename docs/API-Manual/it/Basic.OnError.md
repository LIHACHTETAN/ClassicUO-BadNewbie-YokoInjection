# On Error / Resume

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

On Error sceglie come gestire gli errori successivi nella procedura o funzione corrente. È un’istruzione del linguaggio, non un’API. Per gestione strutturata e pulizia usa Try/Catch/Finally.

## Sintassi esatta

```text
On Error GoTo label
On Error Resume Next
On Error GoTo 0
label:
Resume
Resume Next
```

## Parametri

- `label` — Etichetta esistente nella stessa procedura, scritta label: su una riga propria. Può precedere o seguire On Error, senza distinzione di maiuscole. Non è funzione, stringa o numero di riga. Un’etichetta sconosciuta dà SC009; il client blocca lo script.
- `Resume Next / On Error` — On Error Resume Next continua automaticamente dopo l’istruzione fallita senza etichetta. Le istruzioni riuscite non cambiano. Vale nell’invocazione corrente, non per tutti gli script.
- `0` — On Error GoTo 0 disattiva il modo. Zero è un valore di controllo speciale, non etichetta o risultato Boolean. Altre etichette numeriche e GoTo -1 non sono supportate.
- `Resume / Resume Next` — Nel gestore Resume ripete l’istruzione fallita; Resume Next prosegue dopo. Richiedono un errore registrato e ne cancellano l’indirizzo dopo il trasferimento. Nessun argomento etichetta o timeout.

## Restituisce

On Error e Resume non restituiscono valori. Un errore gestito non diventa TRUE/FALSE e non ripara l’assegnazione. Gli esempi restituiscono esplicitamente Integer 5,18,10. Nessun annullamento automatico degli effetti precedenti.

## Comportamento

- La preparazione risolve le etichette dopo tutta la procedura, in entrambe le direzioni. Il modo è memorizzato; in caso di eccezione Try viene considerato prima di On Error.
- Il motore conserva l’indirizzo dell’istruzione fallita. Il modo etichetta salta al gestore; Resume Next automatico salta l’istruzione. Resume rivaluta espressioni e chiamate: correggi prima la causa e considera gli effetti ripetuti.
- GoTo 0 non cancella l’indirizzo in attesa. Il gestore può disattivarsi, riparare e poi Resume. Disattivalo prima delle operazioni che potrebbero fallire per evitare il rientro.
- Errori sintattici e annullamento non vengono recuperati. Restituire 0, FALSE o uno stato negativo senza eccezione non richiama On Error: controlla il risultato del comando.
- Evita l’ingresso normale nel gestore con Return o GoTo. Ogni procedura chiamata ha il proprio modo; errori non gestiti possono risalire al chiamante. Resume ripete allora l’intera chiamata, non una riga interna. Nessun limite di tentativi o ritardo automatico.
- Se un errore esce da Try dopo la pulizia e raggiunge un gestore esterno On Error GoTo, Resume ripete l’intero Try dall’intestazione. Resume Next e On Error Resume Next continuano dalla prima istruzione dopo End Try. Le azioni già eseguite possono ripetersi; non si rientra a metà del corpo terminato.

## Esempi

### 1. Saltare un’assegnazione fallita

```vb
# values[0] alloca una cella; l’indice 5 è errato. result=1. On Error Resume Next salta la lettura fallita prima dell’assegnazione, lasciando 1. GoTo 0 disattiva; result+=4 dà 5. Main restituisce 5 senza considerare riuscita la lettura.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 1
    On Error Resume Next
    result = values[5]
    On Error GoTo 0
    result += 4
    Return result
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

values[0] alloca una cella; l’indice 5 è errato. result=1. On Error Resume Next salta la lettura fallita prima dell’assegnazione, lasciando 1. GoTo 0 disattiva; result+=4 dà 5. Main restituisce 5 senza considerare riuscita la lettura.

### 2. Riparare e riprovare

```vb
# ReadCell memorizza 8 nella cella 0 ma index=2. L’errore salta a FixIndex. GoTo 0 disattiva; handled=1, index=0. Resume ripete result=values[index], ora con 8. Return impedisce l’ingresso normale nel gestore. Main riceve 18.
Option Explicit On
Function ReadCell()
    Dim values[0]
    values[0] = 8
    Var index = 2
    Var handled = 0
    Var result = 0
    On Error GoTo FixIndex
    result = values[index]
    Return handled * 10 + result
FixIndex:
    On Error GoTo 0
    handled += 1
    index = 0
    Resume
End Function
Sub Main()
    Return ReadCell()
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

ReadCell memorizza 8 nella cella 0 ma index=2. L’errore salta a FixIndex. GoTo 0 disattiva; handled=1, index=0. Resume ripete result=values[index], ora con 8. Return impedisce l’ingresso normale nel gestore. Main riceve 18.

### 3. Gestore prima della registrazione

```vb
# GoTo Work salta Failed all’ingresso normale. On Error GoTo Failed installa quell’etichetta precedente. L’indice 2 fallisce prima di modificare result. Il gestore si disattiva, incrementa handled e con Resume Next raggiunge Return. Risultato 10; le etichette non sono procedure.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 0
    Var handled = 0
    GoTo Work
Failed:
    On Error GoTo 0
    handled += 1
    Resume Next
Work:
    On Error GoTo Failed
    result = values[2]
    Return handled * 10 + result
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

GoTo Work salta Failed all’ingresso normale. On Error GoTo Failed installa quell’etichetta precedente. L’indice 2 fallisce prima di modificare result. Il gestore si disattiva, incrementa handled e con Resume Next raggiunge Return. Risultato 10; le etichette non sono procedure.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: onError / resume / label
Analysis/InvalidSymbolVisitor.cs: VisitOnError / ValidateLabelReference
Runtime/Instructions/Generator.cs: VisitSubrutine / errorHandlers
Runtime/Instructions/ErrorHandlingInstruction.cs
Runtime/Interpreter.cs: TryHandleStructuredError / TryHandleError / ResumeInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/on-error-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/resume-statement
-->
