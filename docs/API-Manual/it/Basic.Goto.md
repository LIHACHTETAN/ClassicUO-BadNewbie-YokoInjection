# GoTo / label:

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

GoTo trasferisce l’esecuzione a un’etichetta della procedura o funzione corrente. L’etichetta indica una posizione, non una procedura chiamabile. Per il controllo ordinario usa If, cicli e Return.

## Sintassi esatta

```text
GoTo label
label:
```

## Parametri

- `label` — Identificatore dichiarato come label: su una riga propria nella stessa procedura. Scrivi GoTo label senza virgolette, parentesi o due punti dopo la destinazione. Sono possibili salti avanti e indietro, senza distinguere maiuscole. Altre procedure possono riusare il nome. I punti sono ammessi ma non creano membri di modulo. Numeri, espressioni calcolate ed etichette di altre procedure non sono destinazioni supportate.

## Restituisce

GoTo e label: non restituiscono valori, né 1/0 né TRUE/FALSE. Gli esempi restituiscono esplicitamente da Main gli Integer -1, 6 e 123 calcolati dallo script.

## Comportamento

- La preparazione registra gli indirizzi e risolve i salti dopo aver letto tutta la procedura. L’esecuzione usa l’indirizzo risolto senza cercare di nuovo nel testo. Le variabili mantengono i valori e le azioni precedenti non vengono annullate.
- Destinazione sconosciuta: SC009 e avvio bloccato dal client. Nome duplicato nella stessa procedura, anche con maiuscole diverse: SC021 prima dell’inizializzazione. Include conserva file e riga originali. Caratteri superflui possono produrre avvisi; usa la sintassi esatta.
- Uscire da Try attivi esegue i rispettivi Finally dall’interno verso l’esterno prima della destinazione. Un salto nello stesso Try attivo lo mantiene. Un errore in Finally può impedire di raggiungere la destinazione.
- Entra nei cicli e Try/Catch/Finally dal loro inizio normale. Saltare nel mezzo non ricrea inizializzazione o contesti saltati; non è una ripresa supportata. Usa Continue o Exit per i cicli.
- Il salto indietro non impone limiti di tentativi, timeout o attese. Modifica esplicitamente la condizione di uscita. Il flusso normale attraversa anche le etichette: salta le sezioni indesiderate o usa Return. Il gestore degli errori si imposta con On Error.

## Esempi

### 1. Salto in avanti

```vb
# amount=0 sceglie NoItems e result=-1, poi Finished restituisce -1. Con amount=4 il percorso normale assegna 40 e GoTo Finished salta NoItems. Le etichette appartengono a Main e non sono chiamate.
Option Explicit On
Sub Main()
    Var amount = 0
    Var result = 0
    If amount <= 0 Then
        GoTo NoItems
    End If
    result = amount * 10
    GoTo Finished
NoItems:
    result = -1
Finished:
    Return result
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

amount=0 sceglie NoItems e result=-1, poi Finished restituisce -1. Con amount=4 il percorso normale assegna 40 e GoTo Finished salta NoItems. Le etichette appartengono a Main e non sono chiamate.

### 2. Ripetizione limitata

```vb
# attempt parte da 0 e aumenta prima del test. Again e again sono la stessa etichetta. Tre passaggi aggiungono 1, 2, 3; poi attempt<3 è falso e Return dà 6. total è inizializzato prima dell’etichetta e non viene azzerato dal salto.
Option Explicit On
Sub Main()
    Var attempt = 0
    Var total = 0
Again:
    attempt += 1
    total += attempt
    If attempt < 3 Then
        GoTo again
    End If
    Return total
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

attempt parte da 0 e aumenta prima del test. Again e again sono la stessa etichetta. Tre passaggi aggiungono 1, 2, 3; poi attempt<3 è falso e Return dà 6. total è inizializzato prima dell’etichetta e non viene azzerato dal salto.

### 3. Uscire da Try annidati

```vb
# trace diventa 1; GoTo Finished salta trace=99. Il Finally interno aggiunge la cifra 2, quello esterno la cifra 3. Solo dopo viene raggiunto Finished e restituito 123. Ogni Finally viene eseguito una volta per questo salto.
Option Explicit On
Sub Main()
    Var trace = 0
    Try
        Try
            trace = trace * 10 + 1
            GoTo Finished
            trace = 99
        Finally
            trace = trace * 10 + 2
        End Try
    Finally
        trace = trace * 10 + 3
    End Try
Finished:
    Return trace
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

trace diventa 1; GoTo Finished salta trace=99. Il Finally interno aggiunge la cifra 2, quello esterno la cifra 3. Solo dopo viene raggiunto Finished e restituito 123. Ogni Finally viene eseguito una volta per questo salto.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: goto / label / SYMBOL
Analysis/LabelStructureValidator.cs: VisitSubrutine / VisitLabel
Analysis/InvalidSymbolVisitor.cs: VisitGoto / ValidateLabelReference
Runtime/Instructions/Generator.cs: Generate / VisitSubrutine
Runtime/Interpreter.cs: GotoInstruction / Transfer / forScopes disposal
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/goto-statement
-->
