# += / -= / *= / /= / &=

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Actualice una variable o elemento de matriz existente con +=, -=, *=, /=. El motor lee el valor, aplica la operación y lo guarda sin evaluar dos veces el destino.

## Sintaxis exacta

```text
target += value
target -= value
target *= value
target /= value
target &= value
```

## Parámetros

- `target` — target: escalar existente o elemento items[index], grid[x][y]. Los elementos deben estar inicializados y los índices, desde cero, ser válidos. Esta instrucción no declara variables.
- `operator` — += y &= suman números o unen dos String; -= resta; *= multiplica; /= divide. El preprocesador cambia &= por +=, así que 5 &= 3 guarda 8. String y número requieren CStr explícito. Escribe cada operador como un solo token.
- `value` — value: expresión evaluada una vez después del destino y los índices. Su tipo debe servir para la operación. Use CStr para añadir números a String.

## Devuelve

Ningún valor (Unit). Es una instrucción, no una expresión ni indicador de éxito. Lea target en la siguiente línea para obtener el resultado guardado. AS se aplica al escribir escalares: Integer 5 tras /=2 guarda Integer 2; una variable numérica sin tipo recibe Decimal 2.5.

## Comportamiento

- Cada referencia de matriz se captura antes de evaluar su índice. Los índices se ejecutan una vez de izquierda a derecha y se comprueban sus límites antes del operando derecho. La celda seleccionada sigue siendo el destino aunque una función ByRef reemplace la variable o una celda superior.
- Se aplican las reglas de +, -, *, /: desbordamiento entero de 32 bits, / devuelve Decimal y la división flotante entre cero puede dar Infinity/NaN. Mezclar String y número falla. Los elementos de matriz no tienen conversión escalar AS.
- Destino no declarado, elemento no inicializado, índice incorrecto, operación incompatible, escritura CONST o conversión fallida producen errores capturables. La escritura final no sucede, pero no se deshacen efectos previos de funciones operando. CONST y AS se comprueban al escribir el escalar, después de que pueda haberse ejecutado la derecha.
- Option Explicit comprueba nombres antes de ejecutar. El depurador conserva la línea original y los bucles respetan pausa/parada. Leer, calcular y escribir no es sincronización atómica entre procedimientos concurrentes.

## Ejemplos

### 1. Los cuatro operadores

```vb
# amount empieza en 10. +=2 da 12, -=3 da 9, *=4 da 36, /=2 da Decimal 18. Main devuelve el valor guardado; las asignaciones no devuelven valores.
Option Explicit On
SUB Main()
    VAR amount = 10
    amount += 2
    amount -= 3
    amount *= 4
    amount /= 2
    RETURN amount
END SUB
```

**Explicación de los parámetros y la ejecución:**

amount empieza en 10. +=2 da 12, -=3 da 9, *=4 da 36, /=2 da Decimal 18. Main devuelve el valor guardado; las asignaciones no devuelven valores.

### 2. Índice evaluado una vez

```vb
# NextIndex incrementa calls recibido ByRef y devuelve 0. items[0] empieza en 5; +=2 lo cambia a 7. Una llamada deja calls=1. Main devuelve items[0]*10+calls=71. La función auxiliar está completa.
Option Explicit On
FUNCTION NextIndex(ByRef calls)
    calls += 1
    RETURN 0
END FUNCTION
SUB Main()
    DIM items[0]
    items[0] = 5
    VAR calls = 0
    items[NextIndex(calls)] += 2
    RETURN items[0] * 10 + calls
END SUB
```

**Explicación de los parámetros y la ejecución:**

NextIndex incrementa calls recibido ByRef y devuelve 0. items[0] empieza en 5; +=2 lo cambia a 7. Una llamada deja calls=1. Main devuelve items[0]*10+calls=71. La función auxiliar está completa.

### 3. Constante protegida

```vb
# limit es CONST 5. limit+=1 falla al escribir; CATCH guarda el error en problem y pone caught=TRUE. limit sigue siendo 5. Main devuelve "5:1" con CStr explícitos. El indicador describe la gestión del error, no un resultado de asignación. El texto se construye en una variable: report=CStr(limit), luego report &= ":" y report &= CStr(caught). Cada &= actualiza report; Return report devuelve "5:1".
Option Explicit On
SUB Main()
    CONST limit = 5
    VAR caught = FALSE
    TRY
        limit += 1
    CATCH problem
        caught = TRUE
    END TRY
    VAR report = CStr(limit)
    report &= ":"
    report &= CStr(caught)
    RETURN report
END SUB
```

**Explicación de los parámetros y la ejecución:**

limit es CONST 5. limit+=1 falla al escribir; CATCH guarda el error en problem y pone caught=TRUE. limit sigue siendo 5. Main devuelve "5:1" con CStr explícitos. El indicador describe la gestión del error, no un resultado de asignación. El texto se construye en una variable: report=CStr(limit), luego report &= ":" y report &= CStr(caught). Cada &= actualiza report; Return report devuelve "5:1".

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: compoundAssignment / compoundOperator
Runtime/BasicSyntaxPreprocessor.cs: ReplaceConcatenationOutsideLiterals
Analysis/InvalidSymbolVisitor.cs: VisitCompoundAssignment / ValidateAssignmentTarget
Runtime/Interpreter.cs: VisitCompoundAssignment
Runtime/SemanticScope.cs: ValidateIndex / SetVar / Coerce
-->
