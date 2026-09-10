# CONST

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

CONST declara un nombre cuya vinculación rechaza la reasignación normal. El valor inicial puede ser un literal o el resultado de una expresión, evaluado al ejecutar la declaración.

## Sintaxis exacta

```text
CONST name [AS type] = expression [, name ...]
```

## Parámetros

- `name` — Nombre de constante sin comillas, distinto en su ámbito. La declaración es global fuera de los procedimientos y local a la llamada dentro de ellos.
- `type` — Tipo AS compatible opcional, con las conversiones de VAR. AS Integer convierte, por ejemplo, al entero con signo de 32 bits del motor. Los corchetes indican partes opcionales; no se escriben alrededor de AS.
- `expression` — Expresión inicial obligatoria: número, texto entre comillas, TRUE/FALSE, cálculo o resultado de una función compatible. Se evalúa una vez por esta ejecución de la declaración, no una vez para siempre.

## Devuelve

Ningún valor. CONST es una declaración, no una función ni una consulta lógica. Leer su nombre obtiene el resultado guardado. Los RETURN de los ejemplos pertenecen a Main o ApplyLimit.

## Comportamiento

- Una asignación normal, LET o SET no puede reemplazar esta vinculación: se produce un error de modificación de constante. TRY/CATCH puede manejarlo. Option Explicit exige declaraciones pero no detecta toda asignación inválida antes de iniciar.
- Una constante global se inicializa al comenzar una nueva ejecución principal y se hereda en los procedimientos llamados con su marca de constante y tipo AS. Las locales se inicializan al ejecutar su declaración. Por tanto, una función inicializadora puede volver a trabajar en otro inicio.
- Se protege la vinculación, no el contenido interno de Array/Object. Otra declaración local puede ocultar un nombre global; una nueva declaración crea otra vinculación. Evite reutilizar nombres de constantes.
- El motor evalúa el inicializador, aplica AS y marca la constante en el ámbito. Las asignaciones normales posteriores comprueban esa marca antes de cambiar el valor. Los ejemplos de literales escalares no realizan acciones de juego.

## Ejemplos

### 1. Calcular con un retraso fijo

```vb
# delay es una constante Integer local igual a 350. Multiplicar por 2 crea la variable separada doubled=700. Main devuelve 700; el ejemplo no espera.
Option Explicit On
SUB Main()
    CONST delay AS Integer = 350
    VAR doubled = delay * 2
    RETURN doubled
END SUB
```

**Explicación de los parámetros y la ejecución:**

delay es una constante Integer local igual a 350. Multiplicar por 2 crea la variable separada doubled=700. Main devuelve 700; el ejemplo no espera.

### 2. Pasar un límite global

```vb
# limit es una constante Integer global igual a 50. ApplyLimit recibe amount=72 y maximum=50 y devuelve la cantidad menor, 50. La función está definida por completo y solo lee sus parámetros.
Option Explicit On
CONST limit AS Integer = 50
FUNCTION ApplyLimit(amount, maximum)
    IF amount > maximum THEN
        RETURN maximum
    END IF
    RETURN amount
END FUNCTION
SUB Main()
    RETURN ApplyLimit(72, limit)
END SUB
```

**Explicación de los parámetros y la ejecución:**

limit es una constante Integer global igual a 50. ApplyLimit recibe amount=72 y maximum=50 y devuelve la cantidad menor, 50. La función está definida por completo y solo lee sus parámetros.

### 3. Manejar una reasignación prohibida

```vb
# limit empieza en 3. Asignar 4 provoca un error sin cambiar la constante. CATCH guarda el error en problem y establece caught=TRUE. Main devuelve 1 lógico; aquí TRUE y 1 son equivalentes.
Option Explicit On
SUB Main()
    CONST limit = 3
    VAR caught = FALSE
    TRY
        limit = 4
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**Explicación de los parámetros y la ejecución:**

limit empieza en 3. Asignar 4 provoca un error sin cambiar la constante. CATCH guarda el error en problem y establece caught=TRUE. Main devuelve 1 lógico; aquí TRUE y 1 son equivalentes.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: constDeclaration / globalConst
Runtime/DefinitionCollector.cs: VisitGlobalConst
Runtime/Interpreter.cs: VisitConstDef
Runtime/SemanticScope.cs: DefineVar / SetVar
-->
