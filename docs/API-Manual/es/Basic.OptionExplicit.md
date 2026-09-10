# Option Explicit

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Exige declarar las variables antes de ejecutar el script. Es una directiva de archivo del lenguaje Basic de este motor, no un comando UO ni una llamada de función.

## Sintaxis exacta

```text
Option Explicit
Option Explicit On
Option Explicit Off
```

## Parámetros

- `On / Off` — On activa la comprobación estricta; Off la desactiva. Sin palabra después de Explicit se entiende On. Sin directiva se conserva el modo anterior no estricto. No añada paréntesis ni comillas.

## Devuelve

Ningún valor. La directiva no es una expresión y no devuelve TRUE/FALSE, un número ni un ID. Los RETURN de los ejemplos pertenecen a Main o Enough, no a Option Explicit.

## Comportamiento

- Escriba la directiva una vez, antes de variables, constantes y procedimientos. Puede haber comentarios y líneas vacías delante. Una directiva repetida o tardía produce SC013, incluso al cambiar después a Off.
- Con On, leer o asignar una variable no declarada produce SC006 con su posición en el código. También se comprueban nombres de matrices, contadores FOR y objetos receptores de métodos. VAR/DIM/CONST, parámetros y variables CATCH con nombre declaran nombres. FOR VAR declara su contador.
- Declare las variables locales antes de usarlas. Una variable local de un procedimiento no declara ese nombre en otro. Las declaraciones globales están disponibles para los procedimientos. Esto comprueba nombres, no demuestra inicialización en todas las ramas.
- El analizador sintáctico lee todo el archivo; el análisis resuelve declaraciones; un error estricto impide ejecutar el primer comando. Al recargar se aplica la opción del nuevo archivo independientemente del anterior. Off puede seguir mostrando advertencias; leer un valor inexistente puede fallar durante la ejecución.
- La directiva sola no realiza acciones de juego ni envía paquetes. No implica compatibilidad completa con VB.NET ni comprueba que exista un objetivo.

## Ejemplos

### 1. Declarar antes de asignar

```vb
# On activa la comprobación. DIM declara count como Integer; asignar 5 es válido. Main devuelve 5. Sustituir count por coutn sin declarar impide iniciar con SC006.
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    RETURN count
END SUB
```

**Explicación de los parámetros y la ejecución:**

On activa la comprobación. DIM declara count como Integer; asignar 5 es válido. Main devuelve 5. Sustituir count por coutn sin declarar impide iniciar con SC006.

### 2. Parámetro y constante global

```vb
# La directiva sin modo significa On. minimum es la constante global 3. amount es un parámetro declarado en Enough y una variable local distinta en Main. Enough compara 5 >= 3 y devuelve TRUE, numéricamente 1.
Option Explicit
CONST minimum = 3
FUNCTION Enough(amount)
    RETURN amount >= minimum
END FUNCTION
SUB Main()
    VAR amount = 5
    RETURN Enough(amount)
END SUB
```

**Explicación de los parámetros y la ejecución:**

La directiva sin modo significa On. minimum es la constante global 3. amount es un parámetro declarado en Enough y una variable local distinta en Main. Enough compara 5 >= 3 y devuelve TRUE, numéricamente 1.

### 3. Ejecutar un script antiguo

```vb
# Off permite crear legacyCounter mediante asignación sin DIM. Main devuelve 7. Este ejemplo de compatibilidad puede mostrar una advertencia; declare la variable y use On para la comprobación estricta.
Option Explicit Off
SUB Main()
    legacyCounter = 7
    RETURN legacyCounter
END SUB
```

**Explicación de los parámetros y la ejecución:**

Off permite crear legacyCounter mediante asignación sin DIM. Main devuelve 7. Este ejemplo de compatibilidad puede mostrar una advertencia; declare la variable y use On para la comprobación estricta.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: optionExplicit
Analysis/SanityAnalyzer.cs
Analysis/InvalidSymbolVisitor.cs
Runtime/InjectionRuntime.cs
-->
