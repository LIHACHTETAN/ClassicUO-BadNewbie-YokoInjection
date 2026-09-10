# For Each / Next

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

For Each recorre los elementos de un array o colección nativa enumerable sin índice numérico. Es una instrucción dentro de un procedimiento o función, no una llamada API.

## Sintaxis exacta

```text
For Each item [AS type] In collection
    statements
Next [item]
```

## Parámetros

- `item` — item: variable de iteración. Reutiliza una variable local, parámetro o campo accesible; si no existe crea una local, incluso con Option Explicit On. No permite escribir en constantes.
- `type` — type: AS type opcional, por ejemplo Integer. Declara un iterador local y convierte cada elemento. Sin AS una variable existente conserva su tipo.
- `collection` — collection: expresión evaluada una sola vez. Admite arrays y objetos nativos enumerables, no escalares. Los arrays anidados proporcionan filas; un bucle interno obtiene sus celdas.
- `statements / NEXT item` — statements / NEXT item: cuerpo y cierre. El nombre tras NEXT es opcional pero debe coincidir con el iterador. NEXT ocupa una línea propia.

## Devuelve

For Each y Next no devuelven valores. item recibe el valor del elemento, no automáticamente índice, ID ni cantidad de una pila. RETURN dentro del cuerpo termina toda la función. Los ejemplos devuelven Integer 12, 105 y 10.

## Comportamiento

- La preparación empareja FOR EACH y NEXT antes de los inicializadores; una discordancia genera SC020. El motor guarda referencia y cursor independiente. Cambiar item no mueve el cursor.
- Los arrays se leen por índices crecientes. Un array vacío omite el cuerpo y conserva el valor de una variable existente sin AS. Elementos sin inicializar y conversiones AS inválidas generan errores capturables.
- Asignar item no reemplaza el elemento. Arrays y objetos anidados son referencias: modificar una celda de row modifica la fila. Reasignar collection no sustituye el recorrido activo; los cambios de elementos posteriores del mismo array se observan al leerlos.
- Continue For avanza el For o For Each más próximo; Exit For sale de él. Error, RETURN y cancelación liberan enumeradores nativos. Algunas colecciones impiden modificaciones durante el recorrido; no se crea una copia automática.
- El iterador sigue visible en el procedimiento después del bucle con su último valor. Cada ejecución tiene su cursor. IDE ofrece autocompletado, plantillas y navegación; pausa y parada siguen disponibles.

## Ejemplos

### 1. Suma sin índice

```vb
# values[2] contiene tres valores: 2, 4, 6. SumItems recibe el array e item cada número. total pasa de 0 a 12; RETURN entrega Integer 12 a Main. NEXT item cierra ese recorrido.
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

**Explicación de los parámetros y la ejecución:**

values[2] contiene tres valores: 2, 4, 6. SumItems recibe el array e item cada número. total pasa de 0 a 12; RETURN entrega Integer 12 a Main. NEXT item cierra ese recorrido.

### 2. Una evaluación y conversión

```vb
# SelectItems recibe calls ByRef y lo cambia a 1; devuelve ["2", "3"]. AS Integer convierte a 2 y 3, total=5. item=100 no cambia origen ni orden. Main devuelve calls*100+total, Integer 105.
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

**Explicación de los parámetros y la ejecución:**

SelectItems recibe calls ByRef y lo cambia a 1; devuelve ["2", "3"]. AS Integer convierte a 2 y 3, total=5. item=100 no cambia origen ni orden. Main devuelve calls*100+total, Integer 105.

### 3. Arrays anidados

```vb
# rows[1][1] contiene dos filas con dos celdas. row recibe una referencia de fila y cell los valores 1, 2, 3, 4. Cada NEXT cierra su bucle. SumGrid y Main devuelven Integer 10; no se deducen ID ni cantidad.
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

**Explicación de los parámetros y la ejecución:**

rows[1][1] contiene dos filas con dos celdas. row recibe una referencia de fila y cell los valores 1, 2, 3, 4. Cada NEXT cierra su bucle. SumGrid y Main devuelven Integer 10; no se deducen ID ni cantidad.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: forEach / next
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretForEach / CallSubrutine
Runtime/ForScope.cs: AdvanceEach / Dispose
Runtime/ScriptBindings.cs: VisitForEach / LocalNames
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-each-next-statement
-->
