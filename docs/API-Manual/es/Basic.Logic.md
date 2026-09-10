# NOT / AND / OR / XOR

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

NOT invierte una condición. AND exige ambas, OR al menos una, XOR exactamente una. && equivale a AND y || a OR. Las palabras clave no distinguen mayúsculas.

## Sintaxis exacta

```text
NOT (condition)
left AND right
left && right
left OR right
left || right
left XOR right
```

## Parámetros

- `left` — Condición binaria izquierda. AND/OR requieren Integer o Decimal: cero es falso, cualquier otro número es verdadero.
- `right` — Condición derecha, también numérica para AND/OR. Se evalúan ambos operandos: un AND izquierdo falso o un OR izquierdo verdadero no omite esta expresión.
- `NOT / grouping` — Con NOT encierre toda la condición que desea invertir entre paréntesis. Agrupe explícitamente las combinaciones de AND, OR y XOR.

## Devuelve

Integer 1 (TRUE) o Integer 0 (FALSE). Son operaciones lógicas, no de bits: 2 AND 4 devuelve 1, no una máscara. Compruebe el indicador devuelto con =TRUE o =1, =FALSE o =0.

## Comportamiento

- AND, OR y XOR tienen la misma prioridad y van de izquierda a derecha en este motor: TRUE OR FALSE AND FALSE da 0; TRUE OR (FALSE AND FALSE) da 1. Tenga en cuenta esta regla heredada al adaptar VB.
- NOT(condition) evalúa e invierte la condición. Al principio de una comparación, NOT 1=2 significa NOT(1=2). Escriba (NOT value) si el valor invertido debe ser un operando de comparación.
- AND/OR rechazan String, Array, Object y Unit. Los NOT y XOR heredados comprueban igualdad con el cero numérico: "0", texto vacío, matrices, objetos y Unit se consideran no nulos. Defina condiciones numéricas explícitas; CBool tiene sus propias conversiones.
- Toda expresión derecha se ejecuta, incluidas funciones, esperas y errores. Los paréntesis cambian la agrupación, no esta evaluación obligatoria. Use IF anidados si una expresión posterior solo debe ejecutarse tras una condición cumplida.

## Ejemplos

### 1. Combinar indicadores

```vb
# ready=TRUE y blocked=FALSE. NOT(blocked) da 1, por lo que canRun vale 1. ready XOR blocked es verdadero porque solo un indicador es verdadero. Main devuelve canRun*10+exclusive=11.
Option Explicit On
SUB Main()
    VAR ready = TRUE
    VAR blocked = FALSE
    VAR canRun = ready AND (NOT blocked)
    VAR exclusive = ready XOR blocked
    RETURN canRun * 10 + exclusive
END SUB
```

**Explicación de los parámetros y la ejecución:**

ready=TRUE y blocked=FALSE. NOT(blocked) da 1, por lo que canRun vale 1. ready XOR blocked es verdadero porque solo un indicador es verdadero. Main devuelve canRun*10+exclusive=11.

### 2. Observar ambas llamadas

```vb
# Mark incrementa counter recibido ByRef y devuelve TRUE. Main comienza con counter=0. FALSE AND Mark(counter) llama a Mark de todas formas; TRUE OR Mark(counter) lo llama otra vez. Las condiciones dan 0 y 1, pero Main devuelve counter=2. Mark está definida por completo.
Option Explicit On
FUNCTION Mark(ByRef counter)
    counter = counter + 1
    RETURN TRUE
END FUNCTION
SUB Main()
    VAR counter = 0
    VAR first = FALSE AND Mark(counter)
    VAR second = TRUE OR Mark(counter)
    RETURN counter
END SUB
```

**Explicación de los parámetros y la ejecución:**

Mark incrementa counter recibido ByRef y devuelve TRUE. Main comienza con counter=0. FALSE AND Mark(counter) llama a Mark de todas formas; TRUE OR Mark(counter) lo llama otra vez. Las condiciones dan 0 y 1, pero Main devuelve counter=2. Mark está definida por completo.

### 3. Agrupar explícitamente

```vb
# legacy calcula TRUE OR FALSE y después AND FALSE, dando 0. grouped calcula primero FALSE AND FALSE entre paréntesis y después OR con TRUE, dando 1. Main devuelve legacy*10+grouped=1.
Option Explicit On
SUB Main()
    VAR legacy = TRUE OR FALSE AND FALSE
    VAR grouped = TRUE OR (FALSE AND FALSE)
    RETURN legacy * 10 + grouped
END SUB
```

**Explicación de los parámetros y la ejecución:**

legacy calcula TRUE OR FALSE y después AND FALSE, dando 0. grouped calcula primero FALSE AND FALSE entre paréntesis y después OR con TRUE, dando 1. Main devuelve legacy*10+grouped=1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: expression / logicalOperand / signedOperand
Runtime/Interpreter.cs: VisitExpression / VisitLogicalOperand / VisitSignedOperand
Runtime/InjectionValue.cs: operator & / operator | / Equals
-->
