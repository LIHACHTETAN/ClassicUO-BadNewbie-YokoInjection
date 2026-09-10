# Dictionary

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

Dictionary() crea una raccolta chiave → valore. Usare i metodi dell’oggetto restituito. Chiavi numeriche e testuali sono distinte; anche "ore" e "Ore" differiscono.

## Sintassi esatta

```text
Dictionary() -> Object
Dictionary(source:Any) -> Object
```

## Parametri

- `source` — source: omesso crea una raccolta vuota. List accetta array o List; Dictionary accetta Dictionary. Si copia il contenitore esterno, condividendo i riferimenti annidati.

## Restituisce

Il costruttore restituisce Object:Dictionary. Item/indice/Get restituiscono valori; Count conta le chiavi. ContainsKey/Remove restituiscono 1=TRUE o 0=FALSE. Add/Set/Clear restituiscono Unit; Keys/Values, nuovi Array. For Each produce voci: Key() restituisce la chiave e Value() il valore.

## Comportamento

- index / key: posizioni List numeriche intere da 0; Insert accetta anche Count(). Le chiavi Dictionary sono testo o numeri finiti. I numeri 1 e 1.0 identificano una chiave; il testo "1" un’altra.
- value: valore Basic inizializzato, anche array o raccolta. Unit non può essere memorizzato. Uguaglianza numerica, testo sensibile alle maiuscole o identità dei riferimenti.
- fallback: Get restituisce questo valore per una chiave assente, senza inserirla. Tutti gli argomenti, inclusa l’espressione fallback, si valutano prima della chiamata.
- Add rifiuta una chiave esistente senza sovrascrivere. Set/indice crea o sostituisce; Item/indice richiede la chiave, Get offre un valore di riserva. Remove restituisce 0 se assente, Clear svuota tutto.
- NaN, infinito, array, oggetti e Unit non sono chiavi valide. L’ordine non è garantito. Ogni voce conserva la propria coppia anche passando all’iterazione successiva.
- Keys/Values creano copie superficiali. Scorrere Keys() per eliminare/sostituire; For Each sul dizionario produce oggetti voce.
- Modificare durante For Each diretto, anche con Set, genera un errore intercettabile al passo successivo. Try/Finally si conclude correttamente. Le modifiche rifiutate conservano i dati.
- Alias e ByVal condividono la raccolta. Copie e istantanee duplicano solo il contenitore esterno. ByRef indicizzato e assegnazione composta valutano contenitore/chiave una volta; sostituire la variabile non reindirizza la scrittura.
- Sono dati locali dello script: i metodi non spostano oggetti di gioco né usano la rete. Una pila memorizzata come elemento occupa una posizione.

## Esempi

### Tipi delle chiavi e riserva

```vb
# Tipi delle chiavi e riserva
#
# Dictionary() crea una raccolta chiave → valore. Usare i metodi dell’oggetto restituito. Chiavi
# numeriche e testuali sono distinte; anche "ore" e "Ore" differiscono.
#
# Il costruttore restituisce Object:Dictionary. Item/indice/Get restituiscono valori; Count
# conta le chiavi. ContainsKey/Remove restituiscono 1=TRUE o 0=FALSE. Add/Set/Clear
# restituiscono Unit; Keys/Values, nuovi Array. For Each produce voci: Key() restituisce la
# chiave e Value() il valore.

Option Explicit On
Sub Main()
    # "ore" passa da 5 a 8. La chiave numerica 1 contiene 2, il testo "1" contiene 3. Get("wood",7)
    # restituisce 7 senza inserimento. Main restituisce 8*100+2*10+3+7, Integer 830.

    Var values = Dictionary()
    values.Add("ore", 5)
    values.Set("ore", 8)
    values[1] = 2
    values["1"] = 3
    Return values.Item("ore")*100 + values[1]*10 + values["1"] + values.Get("wood", 7)
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

- "ore" passa da 5 a 8. La chiave numerica 1 contiene 2, il testo "1" contiene 3. Get("wood",7) restituisce 7 senza inserimento. Main restituisce 8*100+2*10+3+7, Integer 830.

### Voci, copie ed eliminazione

```vb
# Voci, copie ed eliminazione
#
# Dictionary() crea una raccolta chiave → valore. Usare i metodi dell’oggetto restituito. Chiavi
# numeriche e testuali sono distinte; anche "ore" e "Ore" differiscono.
#
# Il costruttore restituisce Object:Dictionary. Item/indice/Get restituiscono valori; Count
# conta le chiavi. ContainsKey/Remove restituiscono 1=TRUE o 0=FALSE. Add/Set/Clear
# restituiscono Unit; Keys/Values, nuovi Array. For Each produce voci: Key() restituisce la
# chiave e Value() il valore.

Option Explicit On
Sub Main()
    # I valori sommano a 5. Keys() permette di eliminare durante lo scorrimento. copied conserva
    # ore=2, snapshot due valori. Dopo Clear Count()=0. Main restituisce 5*100+2*10+2+0, Integer
    # 522.

    Var values = Dictionary()
    values.Add("ore", 2)
    values.Add("wood", 3)
    Var copied = Dictionary(values)
    Var snapshot = values.Values()
    Var total = 0
    For Each entry In values
        If values.ContainsKey(entry.Key()) Then
            total += entry.Value()
        End If
    Next
    For Each key In values.Keys()
        values.Remove(key)
    Next
    values.Clear()
    Return total*100 + copied["ore"]*10 + GetArrayLength(snapshot) + values.Count()
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

- I valori sommano a 5. Keys() permette di eliminare durante lo scorrimento. copied conserva ore=2, snapshot due valori. Dopo Clear Count()=0. Main restituisce 5*100+2*10+2+0, Integer 522.

### Gestire una chiave duplicata

```vb
# Gestire una chiave duplicata
#
# Dictionary() crea una raccolta chiave → valore. Usare i metodi dell’oggetto restituito. Chiavi
# numeriche e testuali sono distinte; anche "ore" e "Ore" differiscono.
#
# Il costruttore restituisce Object:Dictionary. Item/indice/Get restituiscono valori; Count
# conta le chiavi. ContainsKey/Remove restituiscono 1=TRUE o 0=FALSE. Add/Set/Clear
# restituiscono Unit; Keys/Values, nuovi Array. For Each produce voci: Key() restituisce la
# chiave e Value() il valore.

Option Explicit On
Sub Main()
    # Il primo Add memorizza ore=4. Il secondo con 7 genera un errore; Catch imposta caught=1. ore=4
    # rimane. Main restituisce 4*10+1, Integer 41.

    Var values = Dictionary()
    values.Add("ore", 4)
    Var caught = 0
    Try
        values.Add("ore", 7)
    Catch problem
        caught = 1
    End Try
    Return values["ore"]*10 + caught
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

- Il primo Add memorizza ore=4. Il secondo con 7 genera un errore; Catch imposta caught=1. ore=4 rimane. Main restituisce 4*10+1, Integer 41.
