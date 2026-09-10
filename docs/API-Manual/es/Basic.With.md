# With / End With

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

With agrupa operaciones sobre un mismo objeto guardado. El punto inicial selecciona un miembro de ese objeto. With UO y With moduleName son extensiones de Basic para indicar explícitamente un espacio de nombres.

## Sintaxis exacta

```text
With objectExpression
    .Method(arguments)
    statements
End With
With UO
    .Command(arguments)
End With
With moduleName
    .field = expression
    .Procedure(arguments)
End With
```

## Parámetros

- `objectExpression / UO / moduleName` — Receptor obligatorio: objeto nativo List(), Dictionary(), variable que contiene uno o función que devuelve uno. La expresión se evalúa una sola vez al entrar, incluso con el cuerpo vacío. Números, cadenas, matrices y Unit no son receptores de objeto en este motor. Una variable local de objeto tiene prioridad sobre un módulo homónimo.
- `.Method(arguments) / .field` — Use métodos con paréntesis: .Add(value), .Item(index), .Count(). Sus parámetros y resultados no cambian; consulte Basic.List/Basic.Dictionary. Aquí no se admiten campos ni propiedades arbitrarios de objetos. Un módulo permite .field y .Procedure(arguments) accesibles; Private sigue vigente. En With UO, .Command(...) significa UO.Command(...). Fuera del bloque los comandos del juego siguen requiriendo UO.
- `statements / End With` — El cuerpo puede estar vacío o contener llamadas, asignaciones, condiciones y bloques correctamente anidados. End With es obligatorio. Un punto inicial fuera del cuerpo es inválido. Los demás objetos siguen accesibles mediante su nombre completo.

## Devuelve

With es un bloque de control sin retorno propio: no devuelve ID, Boolean ni estado de éxito. Cada método conserva su contrato de retorno. Los Return de los ejemplos devuelven explícitamente Integer desde Main; 127, 28 y 72 son cálculos de demostración.

## Comportamiento

- La preparación valida el bloque y vincula los nombres relativos. Al entrar, el intérprete guarda la referencia obtenida de la expresión en la llamada actual. Reasignar la variable original no cambia esa referencia. Volver a entrar por la cabecera evalúa de nuevo; las llamadas recursivas guardan referencias independientes.
- La cabecera de un With interno se evalúa en el contexto externo. En su cuerpo el punto corresponde al objeto interno; End With restaura el contexto externo. Return, los saltos de bucle y GoTo hacia fuera liberan los ámbitos abandonados después de los Finally pertinentes. Saltar al interior del cuerpo está prohibido.
- Un receptor incorrecto o un método desconocido produce un error, no false. Catch/On Error puede tratarlo. Si falla el receptor, On Error Resume Next omite el bloque completo. With no repite, no espera ni crea un hilo. Las comprobaciones de pausa/parada siguen activas. Los nombres vinculados se almacenan con el script preparado; el receptor no se reevalúa en cada método.

## Ejemplos

### 1. Una sola evaluación

```vb
# Choose recibe values por ByVal y calls por ByRef, incrementa calls a 1 y devuelve la lista original. Ambos .Add añaden 2 y 7 a esa lista guardada, aunque values recibe una lista nueva entre las llamadas. Item usa los índices 0 y 1. Main devuelve 1*100+2*10+7=127.
Option Explicit On
Function Choose(ByVal values, ByRef calls) As Object
    calls += 1
    Return values
End Function

Sub Main()
    Dim calls=0
    Dim values=List()
    Dim original=values
    With Choose(values, calls)
        .Add(2)
        values=List()
        .Add(7)
    End With
    Return calls*100+original.Item(0)*10+original.Item(1)
End Sub
```

**Explicación de los parámetros y la ejecución:**

Choose recibe values por ByVal y calls por ByRef, incrementa calls a 1 y devuelve la lista original. Ambos .Add añaden 2 y 7 a esa lista guardada, aunque values recibe una lista nueva entre las llamadas. Item usa los índices 0 y 1. Main devuelve 1*100+2*10+7=127.

### 2. Objetos anidados y finalización

```vb
# groups guarda child con la clave de texto "child". .Item("child") obtiene el objeto del diccionario externo. Dentro, .Add(2) y .Add(7) en Finally modifican la lista. Tras End With, .Set("result",8) vuelve a actuar sobre el diccionario. Count() devuelve 2 e Item("result") devuelve 8; Main da 28.
Option Explicit On
Sub Main()
    Dim groups=Dictionary()
    Dim child=List()
    groups.Set("child", child)
    With groups
        With .Item("child")
            Try
                .Add(2)
            Finally
                .Add(7)
            End Try
        End With
        .Set("result", 8)
    End With
    Return child.Count()*10+groups.Item("result")
End Sub
```

**Explicación de los parámetros y la ejecución:**

groups guarda child con la clave de texto "child". .Item("child") obtiene el objeto del diccionario externo. Dentro, .Add(2) y .Add(7) en Finally modifican la lista. Tras End With, .Set("result",8) vuelve a actuar sobre el diccionario. Count() devuelve 2 e Item("result") devuelve 8; Main da 28.

### 3. Módulo y espacio UO

```vb
# With Tools califica .total, .AddAmount y .CountItems. total comienza en 4 y AddAmount recibe amount=3 por ByVal, dando 7. CountItems recibe una matriz de dos elementos y llama a UO.GetArrayLength(values) mediante With UO, obteniendo 2. Main calcula 7*10+2=72. Las reglas de acceso del módulo siguen vigentes.
Option Explicit On
Module Tools
    Public Var total=0
    Public Sub AddAmount(ByVal amount)
        total += amount
    End Sub
    Public Function CountItems(ByVal values) As Integer
        With UO
            Return .GetArrayLength(values)
        End With
    End Function
End Module

Sub Main()
    Dim values[1]
    With Tools
        .total=4
        .AddAmount(3)
        Return .total*10+.CountItems(values)
    End With
End Sub
```

**Explicación de los parámetros y la ejecución:**

With Tools califica .total, .AddAmount y .CountItems. total comienza en 4 y AddAmount recibe amount=3 por ByVal, dando 7. CountItems recibe una matriz de dos elementos y llama a UO.GetArrayLength(values) mediante With UO, obteniendo 2. Main calcula 7*10+2=72. Las reglas de acceso del módulo siguen vigentes.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: withStatement / SYMBOL
Analysis/WithStructureValidator.cs: VisitWithStatement / VisitSubrutine / VisitTerminal
Runtime/ScriptBindings.cs: Builder.VisitWithStatement / Variable / CallName
Runtime/Instructions/Generator.cs: WithInstruction generation
Runtime/Instructions/WithInstruction.cs: CaptureName / StartAddress / EndAddress
Runtime/Interpreter.cs: CallSubrutine / TryGetObjectSubrutine / ResumeNextAddress
Runtime/ObjectTypes/NativeObjectTypeInference.cs: ResolveWithReceiver / Scope.VisitWithStatement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/with-end-with-statement
-->
