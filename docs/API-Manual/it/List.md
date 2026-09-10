# List

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: it -->

List() crea una raccolta ordinata di lunghezza variabile. Salvare l’oggetto in una variabile: items.Add è un metodo, non un comando globale List.Add.

## Sintassi esatta

```text
List() -> Object
List(source:Any) -> Object
```

## Parametri

- `source` — source: omesso crea una raccolta vuota. List accetta array o List; Dictionary accetta Dictionary. Si copia il contenitore esterno, condividendo i riferimenti annidati.

## Restituisce

Il costruttore restituisce Object:List. Item/indice legge un valore; Count conta gli elementi; IndexOf restituisce una posizione da 0 o -1. Contains/Remove restituiscono 1=TRUE o 0=FALSE. Add/Insert/Set/RemoveAt/Clear restituiscono Unit; ToArray, un nuovo Array.

## Comportamento

- index / key: posizioni List numeriche intere da 0; Insert accetta anche Count(). Le chiavi Dictionary sono testo o numeri finiti. I numeri 1 e 1.0 identificano una chiave; il testo "1" un’altra.
- value: valore Basic inizializzato, anche array o raccolta. Unit non può essere memorizzato. Uguaglianza numerica, testo sensibile alle maiuscole o identità dei riferimenti.
- fallback: Get restituisce questo valore per una chiave assente, senza inserirla. Tutti gli argomenti, inclusa l’espressione fallback, si valutano prima della chiamata.
- Add aggiunge in coda; Insert inserisce prima della posizione; Set/indice sostituisce un elemento esistente; Item/indice lo legge. Remove elimina il primo valore uguale, RemoveAt una posizione, Clear tutto.
- Contains verifica la presenza, IndexOf trova la prima corrispondenza. Indici negativi, frazionari, testuali o fuori intervallo producono un errore intercettabile senza modifiche.
- For Each mantiene l’ordine. ToArray crea una copia superficiale da scorrere quando si modifica la lista originale.
- Modificare durante For Each diretto, anche con Set, genera un errore intercettabile al passo successivo. Try/Finally si conclude correttamente. Le modifiche rifiutate conservano i dati.
- Alias e ByVal condividono la raccolta. Copie e istantanee duplicano solo il contenitore esterno. ByRef indicizzato e assegnazione composta valutano contenitore/chiave una volta; sostituire la variabile non reindirizza la scrittura.
- Sono dati locali dello script: i metodi non spostano oggetti di gioco né usano la rete. Una pila memorizzata come elemento occupa una posizione.

## Esempi

### Creare e sommare una lista

```vb
# Creare e sommare una lista
#
# List() crea una raccolta ordinata di lunghezza variabile. Salvare l’oggetto in una variabile:
# items.Add è un metodo, non un comando globale List.Add.
#
# Il costruttore restituisce Object:List. Item/indice legge un valore; Count conta gli elementi;
# IndexOf restituisce una posizione da 0 o -1. Contains/Remove restituiscono 1=TRUE o 0=FALSE.
# Add/Insert/Set/RemoveAt/Clear restituiscono Unit; ToArray, un nuovo Array.

Option Explicit On
Sub Main()
    # Add produce [3,7]; Insert(1,5), [3,5,7]; Set(0,2), [2,5,7]. For Each somma tre valori. Main
    # restituisce Integer 14.

    Var items = List()
    items.Add(3)
    items.Add(7)
    items.Insert(1, 5)
    items.Set(0, 2)
    Var total = 0
    For Each item In items
        total += item
    Next
    Return total
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

- Add produce [3,7]; Insert(1,5), [3,5,7]; Set(0,2), [2,5,7]. For Each somma tre valori. Main restituisce Integer 14.

### Copie indipendenti

```vb
# Copie indipendenti
#
# List() crea una raccolta ordinata di lunghezza variabile. Salvare l’oggetto in una variabile:
# items.Add è un metodo, non un comando globale List.Add.
#
# Il costruttore restituisce Object:List. Item/indice legge un valore; Count conta gli elementi;
# IndexOf restituisce una posizione da 0 o -1. Contains/Remove restituiscono 1=TRUE o 0=FALSE.
# Add/Insert/Set/RemoveAt/Clear restituiscono Unit; ToArray, un nuovo Array.

Option Explicit On
Sub Main()
    # seed=[4,6]. copied e snapshot conservano questi valori. L’originale diventa [9,6]; Remove(6)
    # restituisce TRUE=1, RemoveAt(0) lo svuota, Clear lo lascia vuoto. Main restituisce
    # 4*100+6*10+1+0, Integer 461.

    Dim seed[1]
    seed[0] = 4
    seed[1] = 6
    Var items = List(seed)
    Var copied = List(items)
    Var snapshot = items.ToArray()
    items[0] = 9
    Var removed = items.Remove(6)
    items.RemoveAt(0)
    items.Clear()
    Return snapshot[0]*100 + copied[1]*10 + removed + items.Count()
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

- seed=[4,6]. copied e snapshot conservano questi valori. L’originale diventa [9,6]; Remove(6) restituisce TRUE=1, RemoveAt(0) lo svuota, Clear lo lascia vuoto. Main restituisce 4*100+6*10+1+0, Integer 461.

### Ricerca e ByRef

```vb
# Ricerca e ByRef
#
# List() crea una raccolta ordinata di lunghezza variabile. Salvare l’oggetto in una variabile:
# items.Add è un metodo, non un comando globale List.Add.
#
# Il costruttore restituisce Object:List. Item/indice legge un valore; Count conta gli elementi;
# IndexOf restituisce una posizione da 0 o -1. Contains/Remove restituiscono 1=TRUE o 0=FALSE.
# Add/Insert/Set/RemoveAt/Clear restituiscono Unit; ToArray, un nuovo Array.

Option Explicit On
Function NextIndex(ByRef calls)
    calls += 1
    Return 0
End Function
Sub Bump(ByRef value)
    value += 1
End Sub
Sub Main()
    # NextIndex viene eseguito una volta: calls=1, indice 0. Bump cambia 5 in 6. Contains(6)=TRUE,
    # IndexOf(6)=0, Item(0) restituisce 6. Main restituisce Integer 601.

    Var items = List()
    items.Add(5)
    Var calls = 0
    Bump(items[NextIndex(calls)])
    If items.Contains(6) AndAlso items.IndexOf(6) = 0 Then
        Return items.Item(0)*100 + calls
    End If
    Return -1
End Sub
```

**Spiegazione dei parametri e dell’esecuzione:**

- NextIndex viene eseguito una volta: calls=1, indice 0. Bump cambia 5 in 6. Contains(6)=TRUE, IndexOf(6)=0, Item(0) restituisce 6. Main restituisce Integer 601.
