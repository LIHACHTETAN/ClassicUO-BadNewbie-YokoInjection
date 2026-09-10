# AndAlso / OrElse

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

AndAlso y OrElse combinan condiciones omitiendo el operando derecho innecesario. AndAlso lo omite si la izquierda es falsa; OrElse si es verdadera. Úselos para proteger accesos a matrices y evitar llamadas.

## Sintaxis exacta

```text
left AndAlso right
left OrElse right
(conditionA OrElse conditionB) AndAlso conditionC
```

## Parámetros

- `left` — left: expresión evaluada primero y una vez. Cero Integer o Decimal es falso; cualquier número distinto de cero es verdadero.
- `right` — right: expresión evaluada una vez solo cuando es necesaria. Las lecturas, llamadas y efectos omitidos no ocurren. Un operando evaluado debe ser numérico; convierta texto explícitamente con CBool.

## Devuelve

Integer 1 (TRUE) o 0 (FALSE), no el operando original. result=1 equivale a result=TRUE; result=0 a result=FALSE. Aquí verdadero es 1, no el -1 numérico de VB.NET. Un conteo corriente sigue siendo un conteo; esta operación produce un booleano.

## Comportamiento

- Las comparaciones pertenecen a los operandos. AndAlso tiene prioridad sobre OrElse; operadores iguales se asocian de izquierda a derecha. Los paréntesis cambian la agrupación. Option Explicit también comprueba las expresiones omitidas.
- Por compatibilidad, las secuencias AND/OR/XOR mantienen su agrupación inmediata de izquierda a derecha dentro de un operando, antes de AndAlso/OrElse. TRUE OR FALSE AndAlso FALSE da FALSE; TRUE OrElse FALSE AND FALSE da TRUE. Use paréntesis al mezclarlos. AND, OR, && y || evalúan ambos lados.
- El motor evalúa la izquierda, comprueba su verdad numérica y devuelve un booleano o evalúa la derecha necesaria. Los errores necesarios llegan a CATCH; FINALLY y pausa/parada siguen funcionando. Omitir una llamada también omite sus acciones.

## Ejemplos

### 1. Proteger el primer elemento

```vb
# FirstEquals recibe items y expected. GetArrayLength(items)>0 evita leer items[0] en matrices vacías. Main pasa [42] y una matriz vacía, obtiene 1 y 0 y devuelve 10. La función completa no modifica la matriz.
Option Explicit On
FUNCTION FirstEquals(ByVal items, expected)
    RETURN (GetArrayLength(items) > 0) AndAlso (items[0] = expected)
END FUNCTION
SUB Main()
    DIM items[0], empty[-1]
    items[0] = 42
    VAR present = FirstEquals(items, 42)
    VAR missing = FirstEquals(empty, 42)
    RETURN present * 10 + missing
END SUB
```

**Explicación de los parámetros y la ejecución:**

FirstEquals recibe items y expected. GetArrayLength(items)>0 evita leer items[0] en matrices vacías. Main pasa [42] y una matriz vacía, obtiene 1 y 0 y devuelve 10. La función completa no modifica la matriz.

### 2. Una llamada alternativa

```vb
# Probe incrementa calls ByRef y devuelve TRUE. TRUE OrElse Probe(calls) omite la llamada; FALSE OrElse Probe(calls) la ejecuta una vez. Ambas condiciones dan 1 y Main devuelve el número de llamadas: 1.
Option Explicit On
FUNCTION Probe(ByRef calls)
    calls += 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR cached = TRUE OrElse Probe(calls)
    VAR fallback = FALSE OrElse Probe(calls)
    RETURN calls
END SUB
```

**Explicación de los parámetros y la ejecución:**

Probe incrementa calls ByRef y devuelve TRUE. TRUE OrElse Probe(calls) omite la llamada; FALSE OrElse Probe(calls) la ejecuta una vez. Ambas condiciones dan 1 y Main devuelve el número de llamadas: 1.

### 3. División protegida y prioridad

```vb
# AverageExceeds(total, count, limit) divide solo cuando count>0. (25,0,10) da 0; (25,2,10) da 1 porque 12.5>10. TRUE OrElse FALSE AndAlso FALSE da 1 omitiendo el grupo AndAlso. Main devuelve "0:1:1".
Option Explicit On
FUNCTION AverageExceeds(total, count, limit)
    RETURN (count > 0) AndAlso (total / count > limit)
END FUNCTION
SUB Main()
    VAR empty = AverageExceeds(25, 0, 10)
    VAR accepted = AverageExceeds(25, 2, 10)
    VAR priority = TRUE OrElse FALSE AndAlso FALSE
    RETURN CStr(empty) + ":" + CStr(accepted) + ":" + CStr(priority)
END SUB
```

**Explicación de los parámetros y la ejecución:**

AverageExceeds(total, count, limit) divide solo cuando count>0. (25,0,10) da 0; (25,2,10) da 1 porque 12.5>10. TRUE OrElse FALSE AndAlso FALSE da 1 omitiendo el grupo AndAlso. Main devuelve "0:1:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: logicalOperator / ANDALSO / ORELSE
Runtime/Interpreter.cs: VisitExpression / EvaluateAndAlsoGroup / EvaluateEagerLogicalGroup / NumericTruth
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/andalso-operator
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/operators/orelse-operator
-->
