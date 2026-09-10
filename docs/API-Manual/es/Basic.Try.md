# Try / Catch / Finally / Throw

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Try trata errores de ejecución de su cuerpo y de las funciones llamadas. Catch recibe el error, Finally finaliza la operación y Throw crea o relanza un error. Un resultado API 0 o false debe comprobarse explícitamente: no activa Catch por sí solo.

## Sintaxis exacta

```text
Try
    statements
Catch
    handlerStatements
Finally
    cleanupStatements
End Try
Catch name
Catch name As Exception
Catch name As String
Throw stringExpression
Throw
```

## Parámetros

- `Try / statements` — Try necesita un Catch, un Finally o ambos antes de End Try. Los bloques pueden anidarse. Si el cuerpo termina correctamente se omite Catch. Este subconjunto no implementa varios Catch, filtros When ni Exit Try.
- `Catch / name / As type` — La variable de Catch es opcional. name recibe el mensaje como String. As String indica esta representación; As Exception es una escritura compatible, no un objeto .NET ni un filtro de tipo. Se rechazan otros tipos. Un nombre nuevo es local a la rutina y oculta una global homónima. Una local existente recibe una asignación respetando tipo/Const. Declare un String antes de Try si debe existir aunque Catch no se ejecute.
- `Finally / End Try` — Finally es opcional cuando existe Catch y puede tener un cuerpo vacío. La finalización normal, errores, Return, Exit Sub/Function y transferencias de bucle/GoTo hacia fuera ejecutan los Finally pertinentes. End Try es obligatorio. La cancelación omite deliberadamente Catch y el Finally del script para impedir que se retrase la parada de emergencia.
- `Throw stringExpression` — Throw stringExpression evalúa una vez el mensaje y crea un error nuevo. Requiere String; convierta otros valores explícitamente con CStr. Es una forma Basic, no Throw New Exception(...) de VB.NET. Sin controlador falla la ejecución actual, no todos los demás scripts.
- `Throw` — Throw sin mensaje solo se permite dentro de Catch, incluidos sus bloques anidados. Relanza el error activo conservando texto, archivo y línea originales. Una función llamada desde Catch necesita su propio Catch para esta forma.

## Devuelve

Try/Catch/Finally y Throw no devuelven ID, número ni Boolean. Catch expone el mensaje mediante name; Throw transfiere el control en vez de devolver un valor. Los ejemplos devuelven explícitamente dos Strings e Integer 13 desde Main. Las API llamadas conservan sus contratos de retorno.

## Comportamiento

- La preparación valida los bloques y prohíbe GoTo/On Error GoTo hacia el interior de Try, Catch o Finally. El generador guarda las direcciones del controlador y la finalización. Cada llamada tiene sus controladores activos; el error llega al Catch válido más cercano. Un error en Catch pasa por su Finally hacia un controlador externo. Sin un controlador estructurado pueden aplicarse las reglas normales de On Error.
- El retorno, error o salto pendiente se conserva durante Finally. La finalización anidada va desde dentro hacia fuera. Un error nuevo en Finally sustituye al pendiente. Basic también permite Return y saltos salientes desde Finally, que sustituyen la continuación pendiente; esto difiere de VB.NET. Relanzar conserva la primera ubicación del error, incluso de funciones llamadas.
- Pausa/parada siguen activas. Try no crea hilos, reintentos ni esperas. Las direcciones preparadas se reutilizan; compruebe directamente las condiciones normales en vez de usar excepciones. La parada de emergencia omite la finalización del script; los recursos del host mantienen sus propias reglas de liberación en el motor.

## Ejemplos

### 1. Validar un parámetro y guardar el mensaje

```vb
# CheckedAmount recibe amount=-2 como Integer por ByVal. El valor negativo provoca Throw "amount must be non-negative". Catch recibe ese String en problem y lo copia a message; As Exception no crea un objeto. Finally establece finished=1. Main devuelve "amount must be non-negative:1". Un valor no negativo retornaría normalmente sin Catch.
Option Explicit On
Function CheckedAmount(ByVal amount As Integer) As Integer
    If amount < 0 Then
        Throw "amount must be non-negative"
    End If
    Return amount
End Function

Sub Main()
    Dim message=""
    Dim finished=0
    Try
        CheckedAmount(-2)
    Catch problem As Exception
        message=problem
    Finally
        finished=1
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**Explicación de los parámetros y la ejecución:**

CheckedAmount recibe amount=-2 como Integer por ByVal. El valor negativo provoca Throw "amount must be non-negative". Catch recibe ese String en problem y lo copia a message; As Exception no crea un objeto. Finally establece finished=1. Main devuelve "amount must be non-negative:1". Un valor no negativo retornaría normalmente sin Catch.

### 2. Relanzar hacia fuera

```vb
# El Throw interno crea "missing item". Catch interno establece trace=1; Throw sin mensaje conserva el mismo error. Finally interno añade 2, Catch externo copia outerProblem a message y añade 3, Finally externo añade 4. Main devuelve "1234:missing item". trace representa el orden de ejecución, no un código de error.
Option Explicit On
Sub Main()
    Dim trace=0
    Dim message=""
    Try
        Try
            Throw "missing item"
        Catch problem
            trace=1
            Throw
        Finally
            trace=trace*10+2
        End Try
    Catch outerProblem
        message=outerProblem
        trace=trace*10+3
    Finally
        trace=trace*10+4
    End Try
    Return CStr(trace) & ":" & message
End Sub
```

**Explicación de los parámetros y la ejecución:**

El Throw interno crea "missing item". Catch interno establece trace=1; Throw sin mensaje conserva el mismo error. Finally interno añade 2, Catch externo copia outerProblem a message y añade 3, Finally externo añade 4. Main devuelve "1234:missing item". trace representa el orden de ejecución, no un código de error.

### 3. Finalizar cada iteración iniciada

```vb
# number toma 1, 2 y 3. Solo 1 se añade a total: Continue For omite 2, Exit For termina en 3. Los tres Try iniciados ejecutan Finally, por lo que finished=3. Main devuelve 1*10+3=13. Finally no requiere un error; el salto del bucle espera a que termine la finalización de la iteración.
Option Explicit On
Sub Main()
    Dim total=0
    Dim finished=0
    For Var number=1 To 3
        Try
            If number=2 Then
                Continue For
            End If
            If number=3 Then
                Exit For
            End If
            total+=number
        Finally
            finished+=1
        End Try
    Next
    Return total*10+finished
End Sub
```

**Explicación de los parámetros y la ejecución:**

number toma 1, 2 y 3. Solo 1 se añade a total: Continue For omite 2, Exit For termina en 3. Los tres Try iniciados ejecutan Finally, por lo que finished=3. Main devuelve 1*10+3=13. Finally no requiere un error; el salto del bucle espera a que termine la finalización de la iteración.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: tryStatement / catchClause / finallyClause / throwStatement
Analysis/TryStructureValidator.cs: VisitTryStatement / VisitSubrutine / VisitCatchClause / VisitThrowStatement
Runtime/Instructions/Generator.cs: Generate(TryStatementContext)
Runtime/Instructions/TryInstruction.cs: TryInstruction / CatchInstruction / FinallyInstruction / EndTryInstruction
Runtime/Interpreter.cs: CallSubrutine / TryHandleStructuredError / Transfer / DeferReturn / Failure
Runtime/SemanticScope.cs: IsLocal / DefineVar / SetVar
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/try-catch-finally-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/throw-statement
-->
