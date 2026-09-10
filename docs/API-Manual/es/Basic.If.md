# IF / ELSEIF / ELSE / END IF

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

IF elige como máximo una rama: IF, después ELSEIF hasta la primera condición verdadera; en su defecto ELSE, si existe. Normalmente continúa después de END IF.

## Sintaxis exacta

```text
IF condition THEN
    statements
END IF
IF condition THEN
    statements
ELSEIF elseifCondition THEN
    statements
ELSE
    statements
END IF
```

## Parámetros

- `condition` — condition: expresión comprobada una vez al entrar. Cero numérico es falso, los demás números verdaderos. Prefiera comparaciones explícitas o resultados booleanos API.
- `elseifCondition` — elseifCondition: condición adicional opcional; se evalúa solo si todas las anteriores son falsas. Escriba ELSEIF como una palabra.
- `statements / ELSE` — statements / ELSE: instrucciones en líneas siguientes. ELSE es opcional, sin condición, único y final. THEN y END IF son obligatorios; use bloques multilínea.

## Devuelve

Ningún valor (Unit). IF es una instrucción, no una función. Una condición o RETURN elegido puede producir un valor. Los booleanos 1/0 admiten compararse con TRUE/FALSE; IF count acepta cualquier número no nulo, IF count=TRUE solo 1.

## Comportamiento

- El compilador genera saltos condicionales y de salida. Falso pasa a la siguiente condición o ELSE; una rama elegida omite las alternativas restantes. Cada IF anidado tiene su ELSE. RETURN sale de la rutina ejecutando los FINALLY que la rodean.
- Por compatibilidad, IF compara con cero numérico sin convertir todos los tipos mediante CBool. Texto "0", texto vacío, matrices, objetos y Unit eligen la rama verdadera. Convierta texto explícitamente o compare la propiedad deseada. AndAlso/OrElse requieren números.
- Las declaraciones en ramas omitidas no crean variables durante la ejecución. Inicialice resultados comunes antes de IF. Option Explicit comprueba nombres, no asignaciones por todos los caminos. Varios ELSE se rechazan antes de ejecutar con SC015, incluso sin Option Explicit.

## Ejemplos

### 1. Cuatro casos

```vb
# Classify(value) comprueba <0, =0, <10, después ELSE. -2, 0, 7, 20 dan negative, zero, small, large. Main devuelve "negative:zero:small:large"; cada llamada ejecuta un solo RETURN.
Option Explicit On
FUNCTION Classify(value)
    IF value < 0 THEN
        RETURN "negative"
    ELSEIF value = 0 THEN
        RETURN "zero"
    ELSEIF value < 10 THEN
        RETURN "small"
    ELSE
        RETURN "large"
    END IF
END FUNCTION
SUB Main()
    RETURN Classify(-2) + ":" + Classify(0) + ":" + Classify(7) + ":" + Classify(20)
END SUB
```

**Explicación de los parámetros y la ejecución:**

Classify(value) comprueba <0, =0, <10, después ELSE. -2, 0, 7, 20 dan negative, zero, small, large. Main devuelve "negative:zero:small:large"; cada llamada ejecuta un solo RETURN.

### 2. Decisiones anidadas

```vb
# Action(enabled, amount) comprueba enabled y después amount>0 para elegir work o idle. El ELSE exterior da disabled. (TRUE,5), (TRUE,0), (FALSE,5) producen "work:idle:disabled". Cada END IF cierra su bloque.
Option Explicit On
FUNCTION Action(enabled, amount)
    IF enabled THEN
        IF amount > 0 THEN
            RETURN "work"
        ELSE
            RETURN "idle"
        END IF
    ELSE
        RETURN "disabled"
    END IF
END FUNCTION
SUB Main()
    RETURN Action(TRUE, 5) + ":" + Action(TRUE, 0) + ":" + Action(FALSE, 5)
END SUB
```

**Explicación de los parámetros y la ejecución:**

Action(enabled, amount) comprueba enabled y después amount>0 para elegir work o idle. El ELSE exterior da disabled. (TRUE,5), (TRUE,0), (FALSE,5) producen "work:idle:disabled". Cada END IF cierra su bloque.

### 3. Orden de condiciones

```vb
# Check(calls,value) incrementa calls ByRef y devuelve value. La primera condición es falsa, la segunda verdadera; tercera y ELSE se omiten. result=7, calls=2; Main devuelve calls*10+result=27. Se incluyen todas las funciones auxiliares.
Option Explicit On
FUNCTION Check(ByRef calls, ByVal value)
    calls += 1
    RETURN value
END FUNCTION
SUB Main()
    VAR calls = 0
    VAR result = 0
    IF Check(calls, FALSE) THEN
        result = 5
    ELSEIF Check(calls, TRUE) THEN
        result = 7
    ELSEIF Check(calls, TRUE) THEN
        result = 9
    ELSE
        result = 8
    END IF
    RETURN calls * 10 + result
END SUB
```

**Explicación de los parámetros y la ejecución:**

Check(calls,value) incrementa calls ByRef y devuelve value. La primera condición es falsa, la segunda verdadera; tercera y ELSE se omiten. result=7, calls=2; Main devuelve calls*10+result=27. Se incluyen todas las funciones auxiliares.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: if / elseif / else
Runtime/Instructions/Generator.cs: Generate(IfContext)
Runtime/Interpreter.cs: CallSubrutine / IfInstruction / CreateArgumentWriter
Analysis/MisplacedStatementsVisitor.cs: VisitIf
Runtime/InjectionRuntime.cs: BlockingLanguageError
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/if-then-else-statement
-->
