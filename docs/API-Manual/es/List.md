# List

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

List() crea una colección ordenada de longitud variable. Guarde el objeto en una variable: items.Add es un método, no un comando global List.Add.

## Sintaxis exacta

```text
List() -> Object
List(source:Any) -> Object
```

## Parámetros

- `source` — source: omitirlo crea una colección vacía. List acepta una matriz o List; Dictionary acepta Dictionary. Se copia el contenedor exterior y se comparten referencias anidadas.

## Devuelve

El constructor devuelve Object:List. Item/índice lee un valor; Count cuenta elementos; IndexOf da una posición desde 0 o -1. Contains/Remove devuelven 1=TRUE o 0=FALSE. Add/Insert/Set/RemoveAt/Clear devuelven Unit; ToArray, un nuevo Array.

## Comportamiento

- index / key: posiciones List numéricas enteras desde 0; Insert también admite Count(). Dictionary admite texto o números finitos. Los números 1 y 1.0 identifican una clave; el texto "1", otra.
- value: valor Basic inicializado, incluida matriz o colección. Unit no se puede almacenar. Igualdad numérica, texto sensible a mayúsculas o identidad de referencias.
- fallback: Get devuelve este valor si falta la clave, sin insertarla. Todos los argumentos, incluida la expresión fallback, se evalúan antes de llamar.
- Add añade al final; Insert inserta antes de la posición; Set/índice reemplaza un elemento existente; Item/índice lo lee. Remove elimina el primer valor igual, RemoveAt una posición, Clear todos.
- Contains comprueba pertenencia e IndexOf encuentra la primera coincidencia. Los índices negativos, fraccionarios, textuales o fuera de rango producen un error capturable sin cambios.
- For Each conserva el orden. ToArray crea una copia superficial para recorrer mientras cambia la lista original.
- Modificar durante For Each directo, incluso con Set, produce un error capturable en el siguiente paso. Try/Finally se desenrolla correctamente. Los cambios rechazados conservan los datos.
- Los alias y ByVal comparten la colección. Las copias duplican solo el contenedor exterior. ByRef indexado y la asignación compuesta evalúan contenedor/clave una vez; reemplazar la variable no redirige la escritura.
- Son datos locales del script: los métodos no mueven objetos del juego ni usan la red. Una pila guardada como elemento ocupa una posición.

## Ejemplos

### Crear y sumar una lista

```vb
# Crear y sumar una lista
#
# List() crea una colección ordenada de longitud variable. Guarde el objeto en una variable:
# items.Add es un método, no un comando global List.Add.
#
# El constructor devuelve Object:List. Item/índice lee un valor; Count cuenta elementos; IndexOf
# da una posición desde 0 o -1. Contains/Remove devuelven 1=TRUE o 0=FALSE.
# Add/Insert/Set/RemoveAt/Clear devuelven Unit; ToArray, un nuevo Array.

Option Explicit On
Sub Main()
    # Add produce [3,7]; Insert(1,5), [3,5,7]; Set(0,2), [2,5,7]. For Each suma tres valores. Main
    # devuelve Integer 14.

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

**Explicación de los parámetros y la ejecución:**

- Add produce [3,7]; Insert(1,5), [3,5,7]; Set(0,2), [2,5,7]. For Each suma tres valores. Main devuelve Integer 14.

### Copias independientes

```vb
# Copias independientes
#
# List() crea una colección ordenada de longitud variable. Guarde el objeto en una variable:
# items.Add es un método, no un comando global List.Add.
#
# El constructor devuelve Object:List. Item/índice lee un valor; Count cuenta elementos; IndexOf
# da una posición desde 0 o -1. Contains/Remove devuelven 1=TRUE o 0=FALSE.
# Add/Insert/Set/RemoveAt/Clear devuelven Unit; ToArray, un nuevo Array.

Option Explicit On
Sub Main()
    # seed=[4,6]. copied y snapshot mantienen esos valores. El original pasa a [9,6]; Remove(6)
    # devuelve TRUE=1, RemoveAt(0) lo vacía y Clear lo mantiene vacío. Main devuelve 4*100+6*10+1+0,
    # Integer 461.

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

**Explicación de los parámetros y la ejecución:**

- seed=[4,6]. copied y snapshot mantienen esos valores. El original pasa a [9,6]; Remove(6) devuelve TRUE=1, RemoveAt(0) lo vacía y Clear lo mantiene vacío. Main devuelve 4*100+6*10+1+0, Integer 461.

### Búsqueda y ByRef

```vb
# Búsqueda y ByRef
#
# List() crea una colección ordenada de longitud variable. Guarde el objeto en una variable:
# items.Add es un método, no un comando global List.Add.
#
# El constructor devuelve Object:List. Item/índice lee un valor; Count cuenta elementos; IndexOf
# da una posición desde 0 o -1. Contains/Remove devuelven 1=TRUE o 0=FALSE.
# Add/Insert/Set/RemoveAt/Clear devuelven Unit; ToArray, un nuevo Array.

Option Explicit On
Function NextIndex(ByRef calls)
    calls += 1
    Return 0
End Function
Sub Bump(ByRef value)
    value += 1
End Sub
Sub Main()
    # NextIndex se ejecuta una vez: calls=1, índice 0. Bump cambia 5 a 6. Contains(6)=TRUE,
    # IndexOf(6)=0, Item(0) devuelve 6. Main devuelve Integer 601.

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

**Explicación de los parámetros y la ejecución:**

- NextIndex se ejecuta una vez: calls=1, índice 0. Bump cambia 5 a 6. Contains(6)=TRUE, IndexOf(6)=0, Item(0) devuelve 6. Main devuelve Integer 601.
