# For Each / Next

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

For Each visita gli elementi di un array o di una raccolta nativa enumerabile senza indice numerico. È un’istruzione nel corpo di una procedura o funzione, non una chiamata API.

## Sintassi esatta

```text
For Each item [AS type] In collection
    statements
Next [item]
```

## Parametri

- `item` — item: variabile di iterazione. Riutilizza una variabile locale, un parametro o un campo accessibile; altrimenti crea una variabile locale, anche con Option Explicit On. Non può assegnare a una costante.
- `type` — type: AS type facoltativo, per esempio Integer. Dichiara un iteratore locale e converte ogni elemento. Senza AS una variabile esistente conserva il proprio tipo.
- `collection` — collection: espressione valutata una volta. Sono ammessi array e oggetti nativi enumerabili, non scalari. Gli array annidati forniscono righe; un ciclo interno fornisce celle.
- `statements / NEXT item` — statements / NEXT item: corpo e chiusura. Il nome dopo NEXT è facoltativo ma deve corrispondere all’iteratore. NEXT occupa una riga separata.

## Restituisce

For Each e Next non restituiscono valori. item riceve il valore dell’elemento, non automaticamente indice, ID o quantità nella pila. RETURN nel corpo termina l’intera funzione. Gli esempi restituiscono Integer 12, 105 e 10.

## Comportamento

- La preparazione associa FOR EACH a NEXT prima degli inizializzatori; un abbinamento errato produce SC020. Il motore conserva riferimento e cursore indipendente. Assegnare item non sposta il cursore.
- Gli array vengono letti per indice crescente. Un array vuoto salta il corpo e preserva una variabile esistente senza AS. Elementi non inizializzati e conversioni AS errate producono errori intercettabili.
- Assegnare item non sostituisce l’elemento. Array e oggetti annidati sono riferimenti: modificare una cella di row modifica la riga. Riassegnare collection non cambia il percorso attivo; modifiche ai prossimi elementi dello stesso array sono visibili alla lettura.
- Continue For prosegue il For o For Each più vicino; Exit For lo termina. Errori, RETURN e annullamento rilasciano gli enumeratori nativi. Alcune raccolte vietano modifiche durante l’iterazione; non viene creata una copia automatica.
- L’iteratore rimane visibile nella procedura dopo il ciclo con l’ultimo valore assegnato. Ogni esecuzione ha un cursore indipendente. IDE, completamento, modelli, navigazione, pausa e arresto sono supportati.

## Esempi

### 1. Somma senza indice

```vb
# values[2] contiene tre valori: 2, 4, 6. SumItems riceve l’array; item assume ogni valore. total passa da 0 a 12 e RETURN invia Integer 12 a Main. NEXT item chiude il ciclo.
Option Explicit On
Function SumItems(values)
    Var total = 0
    For Each item In values
        total += item
    Next item
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return SumItems(values)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

values[2] contiene tre valori: 2, 4, 6. SumItems riceve l’array; item assume ogni valore. total passa da 0 a 12 e RETURN invia Integer 12 a Main. NEXT item chiude il ciclo.

### 2. Una valutazione e conversioni

```vb
# SelectItems riceve calls ByRef, lo porta a 1 e restituisce ["2", "3"]. AS Integer converte le stringhe in 2 e 3, total=5. item=100 non cambia sorgente o ordine. Main restituisce calls*100+total, Integer 105.
Option Explicit On
Function SelectItems(ByRef calls)
    calls += 1
    Dim values[1]
    values[0] = "2"
    values[1] = "3"
    Return values
End Function
Sub Main()
    Var calls = 0
    Var total = 0
    For Each item As Integer In SelectItems(calls)
        total += item
        item = 100
    Next
    Return calls * 100 + total
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

SelectItems riceve calls ByRef, lo porta a 1 e restituisce ["2", "3"]. AS Integer converte le stringhe in 2 e 3, total=5. item=100 non cambia sorgente o ordine. Main restituisce calls*100+total, Integer 105.

### 3. Array annidati

```vb
# rows[1][1] contiene due righe di due celle. row riceve il riferimento alla riga; cell riceve 1, 2, 3, 4. Ogni NEXT chiude il proprio ciclo. SumGrid e Main restituiscono Integer 10, senza ricavare automaticamente ID o quantità.
Option Explicit On
Function SumGrid(rows)
    Var total = 0
    For Each row In rows
        For Each cell In row
            total += cell
        Next cell
    Next row
    Return total
End Function
Sub Main()
    Dim rows[1][1]
    rows[0][0] = 1
    rows[0][1] = 2
    rows[1][0] = 3
    rows[1][1] = 4
    Return SumGrid(rows)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

rows[1][1] contiene due righe di due celle. row riceve il riferimento alla riga; cell riceve 1, 2, 3, 4. Ogni NEXT chiude il proprio ciclo. SumGrid e Main restituiscono Integer 10, senza ricavare automaticamente ID o quantità.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: forEach / next
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretForEach / CallSubrutine
Runtime/ForScope.cs: AdvanceEach / Dispose
Runtime/ScriptBindings.cs: VisitForEach / LocalNames
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-each-next-statement
-->
