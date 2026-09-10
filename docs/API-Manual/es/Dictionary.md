# Dictionary

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Dictionary() crea una colección clave → valor. Use los métodos del objeto devuelto. Las claves numéricas y textuales son distintas; "ore" y "Ore" también difieren.

## Sintaxis exacta

```text
Dictionary() -> Object
Dictionary(source:Any) -> Object
```

## Parámetros

- `source` — source: omitirlo crea una colección vacía. List acepta una matriz o List; Dictionary acepta Dictionary. Se copia el contenedor exterior y se comparten referencias anidadas.

## Devuelve

El constructor devuelve Object:Dictionary. Item/índice/Get devuelven valores; Count cuenta claves. ContainsKey/Remove devuelven 1=TRUE o 0=FALSE. Add/Set/Clear devuelven Unit; Keys/Values, nuevos Array. For Each entrega entradas: Key() devuelve la clave, Value() su valor.

## Comportamiento

- index / key: posiciones List numéricas enteras desde 0; Insert también admite Count(). Dictionary admite texto o números finitos. Los números 1 y 1.0 identifican una clave; el texto "1", otra.
- value: valor Basic inicializado, incluida matriz o colección. Unit no se puede almacenar. Igualdad numérica, texto sensible a mayúsculas o identidad de referencias.
- fallback: Get devuelve este valor si falta la clave, sin insertarla. Todos los argumentos, incluida la expresión fallback, se evalúan antes de llamar.
- Add rechaza una clave existente sin sobrescribir. Set/índice crea o reemplaza; Item/índice exige una clave existente, Get ofrece un valor alternativo. Remove devuelve 0 si falta; Clear vacía todo.
- NaN, infinito, matrices, objetos y Unit no son claves válidas. El orden no está garantizado. Cada entrada conserva su pareja incluso al avanzar a otras iteraciones.
- Keys/Values crean copias superficiales. Recorra Keys() para eliminar/reemplazar; For Each directo sobre el diccionario produce objetos de entrada.
- Modificar durante For Each directo, incluso con Set, produce un error capturable en el siguiente paso. Try/Finally se desenrolla correctamente. Los cambios rechazados conservan los datos.
- Los alias y ByVal comparten la colección. Las copias duplican solo el contenedor exterior. ByRef indexado y la asignación compuesta evalúan contenedor/clave una vez; reemplazar la variable no redirige la escritura.
- Son datos locales del script: los métodos no mueven objetos del juego ni usan la red. Una pila guardada como elemento ocupa una posición.

## Ejemplos

### Tipos de claves y valor alternativo

```vb
# Tipos de claves y valor alternativo
#
# Dictionary() crea una colección clave → valor. Use los métodos del objeto devuelto. Las claves
# numéricas y textuales son distintas; "ore" y "Ore" también difieren.
#
# El constructor devuelve Object:Dictionary. Item/índice/Get devuelven valores; Count cuenta
# claves. ContainsKey/Remove devuelven 1=TRUE o 0=FALSE. Add/Set/Clear devuelven Unit;
# Keys/Values, nuevos Array. For Each entrega entradas: Key() devuelve la clave, Value() su
# valor.

Option Explicit On
Sub Main()
    # "ore" cambia de 5 a 8. La clave numérica 1 guarda 2, el texto "1" guarda 3. Get("wood",7)
    # devuelve 7 sin inserción. Main devuelve 8*100+2*10+3+7, Integer 830.

    Var values = Dictionary()
    values.Add("ore", 5)
    values.Set("ore", 8)
    values[1] = 2
    values["1"] = 3
    Return values.Item("ore")*100 + values[1]*10 + values["1"] + values.Get("wood", 7)
End Sub
```

**Explicación de los parámetros y la ejecución:**

- "ore" cambia de 5 a 8. La clave numérica 1 guarda 2, el texto "1" guarda 3. Get("wood",7) devuelve 7 sin inserción. Main devuelve 8*100+2*10+3+7, Integer 830.

### Entradas, copias y eliminación

```vb
# Entradas, copias y eliminación
#
# Dictionary() crea una colección clave → valor. Use los métodos del objeto devuelto. Las claves
# numéricas y textuales son distintas; "ore" y "Ore" también difieren.
#
# El constructor devuelve Object:Dictionary. Item/índice/Get devuelven valores; Count cuenta
# claves. ContainsKey/Remove devuelven 1=TRUE o 0=FALSE. Add/Set/Clear devuelven Unit;
# Keys/Values, nuevos Array. For Each entrega entradas: Key() devuelve la clave, Value() su
# valor.

Option Explicit On
Sub Main()
    # Los valores suman 5. Keys() permite eliminar durante el recorrido. copied conserva ore=2 y
    # snapshot dos valores. Tras Clear, Count()=0. Main devuelve 5*100+2*10+2+0, Integer 522.

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

**Explicación de los parámetros y la ejecución:**

- Los valores suman 5. Keys() permite eliminar durante el recorrido. copied conserva ore=2 y snapshot dos valores. Tras Clear, Count()=0. Main devuelve 5*100+2*10+2+0, Integer 522.

### Gestionar claves duplicadas

```vb
# Gestionar claves duplicadas
#
# Dictionary() crea una colección clave → valor. Use los métodos del objeto devuelto. Las claves
# numéricas y textuales son distintas; "ore" y "Ore" también difieren.
#
# El constructor devuelve Object:Dictionary. Item/índice/Get devuelven valores; Count cuenta
# claves. ContainsKey/Remove devuelven 1=TRUE o 0=FALSE. Add/Set/Clear devuelven Unit;
# Keys/Values, nuevos Array. For Each entrega entradas: Key() devuelve la clave, Value() su
# valor.

Option Explicit On
Sub Main()
    # El primer Add guarda ore=4. El segundo con 7 genera un error; Catch pone caught=1. ore=4 se
    # conserva. Main devuelve 4*10+1, Integer 41.

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

**Explicación de los parámetros y la ejecución:**

- El primer Add guarda ore=4. El segundo con 7 genera un error; Catch pone caught=1. ore=4 se conserva. Main devuelve 4*10+1, Integer 41.
