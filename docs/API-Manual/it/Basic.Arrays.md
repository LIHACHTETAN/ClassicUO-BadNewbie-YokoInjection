# DIM / REDIM / PRESERVE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: it -->

DIM crea un array dinamico; REDIM ne sostituisce la memoria. PRESERVE copia i valori agli indici comuni. Le dimensioni indicano limiti superiori inclusi, non quantità. Inizializzare gli elementi prima di leggerli.

## Sintassi esatta

```text
DIM name[upper]
DIM name(upper) AS type
DIM grid[xUpper][yUpper]
DIM grid(xUpper, yUpper)
REDIM name[upper]
REDIM PRESERVE name[upper]
name[index] = value
GetArrayLength(name)
```

## Parametri

- `name` — name: variabile array. DIM la dichiara; REDIM sostituisce il valore di una variabile esistente. Accesso con items[i], grid[x][y].
- `upper` — upper: espressione convertita in Integer, valutata una volta da sinistra a destra. DIM items[2] crea tre celle 0..2. -1 crea una dimensione vuota; limiti inferiori e overflow della lunghezza sono errori. La memoria limita le dimensioni pratiche.
- `PRESERVE` — PRESERVE: facoltativo dopo REDIM. Copia ricorsivamente gli indici comuni; ridurre elimina i valori fuori dai nuovi limiti. Senza di esso le celle non sono inizializzate.
- `AS type` — AS type: annotazione DIM accettata senza tipizzare, inizializzare o convertire gli elementi. Sono ammessi valori di tipi diversi.

## Restituisce

DIM e REDIM non restituiscono valori (Unit). items[i] restituisce il valore e il suo tipo effettivo: Integer, Decimal, String, Array o Object. Una cella non inizializzata genera un errore, non 0 o FALSE. GetArrayLength(array) restituisce la lunghezza esterna come Integer; per valori non array restituisce 0.

## Comportamento

- DIM grid(1, 2) equivale a grid[1][2]: due righe di tre celle. Le funzioni nei limiti restano chiamate. Accedere con grid[1][2]; le parentesi tonde in un’espressione indicano una chiamata.
- Assegnazione e ByVal copiano il riferimento, non gli elementi. Gli alias vedono le modifiche comuni. REDIM collega un nuovo array; gli alias conservano quello vecchio. PRESERVE copia le coordinate comuni di array annidati, senza clonare interamente oggetti arbitrari.
- Indici solo da zero. DIM items[2]=5 e inizializzatori REDIM vengono rifiutati con SC014; assegnare le celle separatamente. Indici errati e letture non inizializzate producono errori gestibili.
- Questo dialetto Basic differisce dagli array tipizzati VB.NET per tipi dinamici e PRESERVE multidimensionale. Un booleano memorizzato usa 1/0; un numero qualsiasi o la lunghezza non sono flag di successo.
- RETURN array restituisce il riferimento all’array, che rimane valido dopo la funzione creatrice. Assegnare il risultato non copia gli elementi. Una funzione comune può creare un array per un campo Module. Avvii separati creano array nuovi quando rieseguono DIM.

## Esempi

### 1. Sommare gli elementi

```vb
# Abs(-2) dà limite 2: Main crea 3 celle con 2, 4, 6. Sum riceve il riferimento ByVal, percorre 0..GetArrayLength(items)-1 e restituisce 12. La funzione completa non modifica elementi e accetta array vuoti.
Option Explicit On
FUNCTION Sum(ByVal items)
    VAR total = 0
    VAR i = 0
    FOR i = 0 TO GetArrayLength(items) - 1
        total += items[i]
    NEXT
    RETURN total
END FUNCTION
SUB Main()
    DIM items(Abs(-2))
    items[0] = 2
    items[1] = 4
    items[2] = 6
    RETURN Sum(items)
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

Abs(-2) dà limite 2: Main crea 3 celle con 2, 4, 6. Sum riceve il riferimento ByVal, percorre 0..GetArrayLength(items)-1 e restituisce 12. La funzione completa non modifica elementi e accetta array vuoti.

### 2. Ingrandire conservando

```vb
# values contiene 7 e 8. REDIM PRESERVE values(2) crea 3 celle e copia gli indici 0 e 1. Inizializzare la nuova cella 2 con 9. Main restituisce 7*100+8*10+9=789.
Option Explicit On
SUB Main()
    DIM values[1]
    values[0] = 7
    values[1] = 8
    REDIM PRESERVE values(2)
    values[2] = 9
    RETURN values[0] * 100 + values[1] * 10 + values[2]
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

values contiene 7 e 8. REDIM PRESERVE values(2) crea 3 celle e copia gli indici 0 e 1. Inizializzare la nuova cella 2 con 9. Main restituisce 7*100+8*10+9=789.

### 3. Osservare gli alias

```vb
# grid ha due righe di due celle. alias condivide l’array: alias[0][1]=9 modifica anche grid. PRESERVE espande grid a tre righe conservando 9; alias mantiene due righe. "9:3:2" indica valore, nuova lunghezza esterna e lunghezza del vecchio alias.
Option Explicit On
SUB Main()
    DIM grid[1][1]
    grid[0][1] = 4
    VAR alias = grid
    alias[0][1] = 9
    REDIM PRESERVE grid[2][1]
    RETURN CStr(grid[0][1]) + ":" + CStr(GetArrayLength(grid)) + ":" + CStr(GetArrayLength(alias))
END SUB
```

**Spiegazione dei parametri e dell’esecuzione:**

grid ha due righe di due celle. alias condivide l’array: alias[0][1]=9 modifica anche grid. PRESERVE espande grid a tre righe conservando 9; alias mantiene due righe. "9:3:2" indica valore, nuova lunghezza esterna e lunghezza del vecchio alias.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim / NormalizeArrayDeclarator
Analysis/ArrayDeclarationVisitor.cs: VisitDimDef
Runtime/Interpreter.cs: VisitDimDef / VisitRedim / VisitIndexedSymbol
Runtime/SemanticScope.cs: CreateArray / CopyArray / GetDim / SetDim
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/redim-statement
-->
