# For / To / Step / Next / Exit For

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

For repite un bloque en un intervalo numérico inclusivo. Úsalo para índices o una cantidad conocida de operaciones; For Each recorre valores de elementos.

## Sintaxis exacta

```text
For [VAR] counter = start To limit [Step increment]
    statements
Next [counter]
Continue For
Exit For
Break
```

## Parámetros

- `counter / VAR` — Contador escalar modificable. VAR lo declara en el procedimiento; sin VAR utiliza una variable existente. Con Option Explicit On decláralo antes o usa For Var. Para un tipo explícito escribe DIM counter AS Integer antes del bucle; AS en la cabecera numérica no está admitido.
- `start` — Expresión numérica inicial, evaluada una vez y asignada antes de evaluar limit e increment.
- `limit` — Límite incluido, evaluado una vez al entrar. Paso positivo: counter <= limit; negativo: counter >= limit.
- `increment` — Paso numérico opcional, predeterminado 1. Admite negativos y fracciones; cero causa un error capturable. Tipo y paso deben permitir que el contador avance.
- `statements / Next / exit` — Cuerpo y Next en líneas separadas. El nombre opcional tras Next debe coincidir. Continue For pasa al siguiente paso; Exit For sale del For/For Each más cercano; Break sale del bucle más interno de cualquier tipo.

## Devuelve

For, Next y Exit For no devuelven valores. El contador es un número, no un ID automático. Al terminar normalmente este motor conserva el último valor ejecutado, no uno fuera del intervalo. Un bucle omitido conserva start; una salida anticipada conserva el valor actual. Los ejemplos devuelven Integer 12,28,395.

## Comportamiento

- Entrada: asignar start, guardar límite y paso, rechazar cero, comprobar el primer valor. Una dirección incompatible omite el cuerpo; start=limit lo ejecuta una vez.
- Next comprueba counter+step y lo asigna solo si cabe otra iteración. 1 To 5 Step 3 visita 1 y 4. Cambiar las variables originales del límite/paso no altera los valores guardados; cambiar el contador sí afecta al siguiente paso.
- Estructura y nombre Next se verifican antes de ejecutar; los errores estructurales producen SC020. Usa contadores distintos en bucles anidados. Al salir de Try se ejecuta Finally. Pausa/parada siguen activas; no hay espera ni plazo automático.

## Ejemplos

### 1. Sumar celdas

```vb
# values[2] crea índices 0,1,2 con valores 2,4,6. Sum recibe el array ByVal, empieza en index=0 y guarda length-1=2. El paso implícito 1 visita tres celdas; total=12 vuelve a Main.
Option Explicit On
Function Sum(ByVal items)
    Var total = 0
    For Var index = 0 To GetArrayLength(items) - 1
        total += items[index]
    Next index
    Return total
End Function
Sub Main()
    Dim values[2]
    values[0] = 2
    values[1] = 4
    values[2] = 6
    Return Sum(values)
End Sub
```

**Explicación de los parámetros y la ejecución:**

values[2] crea índices 0,1,2 con valores 2,4,6. Sum recibe el array ByVal, empieza en index=0 y guarda length-1=2. El paso implícito 1 visita tres celdas; total=12 vuelve a Main.

### 2. Borrar desde el final

```vb
# items contiene -1,3,-2,5. Inicio Count()-1=3, límite 0, paso -1. Borrar un valor negativo desplaza solo índices ya visitados y no omite elementos pendientes. Quedan 3 y 5; Count()*10+3+5 devuelve 28.
Option Explicit On
Sub Main()
    Var items = List()
    items.Add(-1)
    items.Add(3)
    items.Add(-2)
    items.Add(5)
    For Var index = items.Count() - 1 To 0 Step -1
        If items[index] < 0 Then
            items.RemoveAt(index)
        End If
    Next index
    Return items.Count() * 10 + items[0] + items[1]
End Sub
```

**Explicación de los parámetros y la ejecución:**

items contiene -1,3,-2,5. Inicio Count()-1=3, límite 0, paso -1. Borrar un valor negativo desplaza solo índices ya visitados y no omite elementos pendientes. Quedan 3 y 5; Count()*10+3+5 devuelve 28.

### 3. Límites guardados y contador final

```vb
# ReadLimit incrementa calls ByRef y devuelve value. Inicio=1, límite=5, paso=2 se evalúan una vez cada uno: calls=3. upper=99 y stride=1 en el cuerpo no los alteran. Visita 1,3,5; total=9, index queda en 5. Main devuelve 395.
Option Explicit On
Function ReadLimit(ByRef calls, ByVal value)
    calls += 1
    Return value
End Function
Sub Main()
    Var calls = 0
    Var upper = 5
    Var stride = 2
    Var total = 0
    For Var index = ReadLimit(calls, 1) To ReadLimit(calls, upper) Step ReadLimit(calls, stride)
        total += index
        upper = 99
        stride = 1
    Next index
    Return calls * 100 + total * 10 + index
End Sub
```

**Explicación de los parámetros y la ejecución:**

ReadLimit incrementa calls ByRef y devuelve value. Inicio=1, límite=5, paso=2 se evalúan una vez cada uno: calls=3. upper=99 y stride=1 en el cuerpo no los alteran. Visita 1,3,5; total=9, index queda en 5. Main devuelve 395.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Interpreter.cs: InterpretFor / CallSubrutine
Runtime/ForScope.cs: ContainsCurrent / HasNext
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-next-statement
-->
