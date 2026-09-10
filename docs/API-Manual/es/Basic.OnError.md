# On Error / Resume

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

On Error selecciona cómo tratar errores posteriores en el procedimiento o función actual. Es una instrucción del lenguaje, no una API. Para gestión estructurada y limpieza usa Try/Catch/Finally.

## Sintaxis exacta

```text
On Error GoTo label
On Error Resume Next
On Error GoTo 0
label:
Resume
Resume Next
```

## Parámetros

- `label` — Etiqueta existente del mismo procedimiento, escrita label: en su propia línea. Puede estar antes o después de On Error; no distingue mayúsculas. No es función, cadena ni número de línea. Una etiqueta desconocida produce SC009; el cliente bloquea el script.
- `Resume Next / On Error` — On Error Resume Next continúa automáticamente tras la instrucción fallida sin saltar a una etiqueta. No altera las instrucciones correctas. Se aplica a la llamada actual, no a todos los scripts.
- `0` — On Error GoTo 0 desactiva el modo. Cero es un control especial, no una etiqueta ni resultado Boolean. Otras etiquetas numéricas y GoTo -1 no están admitidos.
- `Resume / Resume Next` — En el manejador, Resume repite la instrucción fallida; Resume Next continúa después. Requieren un fallo registrado y borran su dirección al transferir. No aceptan etiqueta ni plazo como argumento.

## Devuelve

On Error y Resume no devuelven valores. Un error tratado no se convierte en TRUE/FALSE ni repara automáticamente una asignación. Los ejemplos devuelven Integer 5,18,10 explícitos. Los efectos anteriores no se revierten automáticamente.

## Comportamiento

- La preparación resuelve las etiquetas después de leer todo el procedimiento, en ambas direcciones. Se guarda el modo; ante una excepción se considera Try antes de On Error.
- El motor registra la dirección de la instrucción fallida. El modo etiqueta salta al manejador; Resume Next automático pasa la instrucción. Resume reevalúa expresiones y llamadas: corrige primero la causa y considera los efectos repetidos.
- GoTo 0 conserva la dirección del fallo pendiente. El manejador puede desactivarse, reparar y ejecutar Resume. Desactívalo antes de operaciones que puedan fallar para evitar volver a entrar.
- No recupera errores sintácticos ni cancelación. Si un comando solo devuelve 0, FALSE o un estado de fallo sin excepción, On Error no se activa; comprueba su resultado.
- Evita entrar normalmente al manejador con Return o GoTo. Cada procedimiento llamado tiene su modo; un fallo sin tratar puede llegar al llamador. Resume repite entonces la llamada completa, no una línea interna. Sin límite de intentos ni demora automática.

## Ejemplos

### 1. Omitir una asignación fallida

```vb
# values[0] reserva una celda; el índice 5 es inválido. result=1. On Error Resume Next omite la lectura fallida antes de asignar, conservando 1. GoTo 0 desactiva; result+=4 da 5. Main devuelve 5, sin declarar correcta la lectura.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 1
    On Error Resume Next
    result = values[5]
    On Error GoTo 0
    result += 4
    Return result
End Sub
```

**Explicación de los parámetros y la ejecución:**

values[0] reserva una celda; el índice 5 es inválido. result=1. On Error Resume Next omite la lectura fallida antes de asignar, conservando 1. GoTo 0 desactiva; result+=4 da 5. Main devuelve 5, sin declarar correcta la lectura.

### 2. Reparar y reintentar

```vb
# ReadCell guarda 8 en la celda 0 pero index=2. El fallo salta a FixIndex. GoTo 0 desactiva; handled=1, index=0. Resume repite result=values[index] y ahora guarda 8. Return impide entrar normalmente al manejador. Main recibe 18.
Option Explicit On
Function ReadCell()
    Dim values[0]
    values[0] = 8
    Var index = 2
    Var handled = 0
    Var result = 0
    On Error GoTo FixIndex
    result = values[index]
    Return handled * 10 + result
FixIndex:
    On Error GoTo 0
    handled += 1
    index = 0
    Resume
End Function
Sub Main()
    Return ReadCell()
End Sub
```

**Explicación de los parámetros y la ejecución:**

ReadCell guarda 8 en la celda 0 pero index=2. El fallo salta a FixIndex. GoTo 0 desactiva; handled=1, index=0. Resume repite result=values[index] y ahora guarda 8. Return impide entrar normalmente al manejador. Main recibe 18.

### 3. Manejador anterior a su registro

```vb
# GoTo Work omite Failed al entrar normalmente. On Error GoTo Failed instala esa etiqueta anterior. El índice 2 falla antes de cambiar result. El manejador se desactiva, aumenta handled y Resume Next alcanza Return. Resultado 10; las etiquetas no son procedimientos.
Option Explicit On
Sub Main()
    Dim values[0]
    Var result = 0
    Var handled = 0
    GoTo Work
Failed:
    On Error GoTo 0
    handled += 1
    Resume Next
Work:
    On Error GoTo Failed
    result = values[2]
    Return handled * 10 + result
End Sub
```

**Explicación de los parámetros y la ejecución:**

GoTo Work omite Failed al entrar normalmente. On Error GoTo Failed instala esa etiqueta anterior. El índice 2 falla antes de cambiar result. El manejador se desactiva, aumenta handled y Resume Next alcanza Return. Resultado 10; las etiquetas no son procedimientos.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: onError / resume / label
Analysis/InvalidSymbolVisitor.cs: VisitOnError / ValidateLabelReference
Runtime/Instructions/Generator.cs: VisitSubrutine / errorHandlers
Runtime/Instructions/ErrorHandlingInstruction.cs
Runtime/Interpreter.cs: TryHandleStructuredError / TryHandleError / ResumeInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/on-error-statement
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/resume-statement
-->
