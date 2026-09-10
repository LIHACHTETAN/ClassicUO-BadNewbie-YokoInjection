# VAR / DIM

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

VAR y DIM escalar declaran un valor con nombre. La asignación evalúa la expresión y guarda su resultado. Dentro de un procedimiento la declaración es local a esa llamada; fuera de los procedimientos es global al script.

## Sintaxis exacta

```text
VAR name [AS type] [= expression] [, name ...]
DIM name [AS type] [= expression] [, name ...]
name = expression
LET name = expression
SET name = expression
```

## Parámetros

- `name` — Identificador sin comillas: letras, cifras y guiones bajos, empezando por letra o guion bajo. Mantenga la misma escritura y evite palabras clave.
- `type` — AS opcional. Integer/Long/Short/Byte usan la conversión entera con signo de 32 bits del motor; Double/Single/Decimal su número de doble precisión; String texto; Boolean/Bool un valor lógico; Variant/Object conservan la clase del valor. Estos alias no imponen rangos byte/short/long separados de VB.NET.
- `expression` — Inicializador opcional en VAR/DIM; expresión derecha obligatoria al asignar. Se evalúa al ejecutar la línea. AS String sin inicializador empieza con texto vacío; los números tipados y Boolean empiezan en cero. Sin inicializador, VAR sin tipo y VAR AS Variant/Object contienen Unit (ausencia de valor), mientras DIM escalar proporciona 0. Una variable sin tipo puede contener después otra clase de valor.

## Devuelve

Ningún valor. VAR, DIM y la asignación no devuelven resultados. Leer el nombre obtiene el valor guardado. RETURN en los ejemplos devuelve ese valor desde Main, no desde DIM.

## Comportamiento

- Los corchetes de la sintaxis indican partes opcionales; no los escriba alrededor de AS ni del inicializador. DIM de matrices utiliza otra forma.
- LET y SET son formas compatibles de asignación normal. Con Option Explicit On no declaran nombres. AS también se aplica en asignaciones posteriores; una conversión inválida o tipo no admitido causa un error de ejecución.
- Los nombres locales pertenecen a la llamada del procedimiento. Declarar dentro de IF no crea un ámbito de bloque separado. Una rama que no se ejecuta no crea un valor durante la ejecución. Declare antes de la bifurcación si necesitará el valor después.
- Compatibilidad Injection: el procedimiento llamado hereda los valores escalares globales actuales del llamador y sus tipos AS. Reasignar un escalar en el procedimiento llamado no modifica al llamador. Devuelva el nuevo valor o pase un argumento BYREF para actualizarlo. Los valores Array/Object no se clonan en profundidad. Una nueva ejecución principal inicializa de nuevo las globales; una declaración local oculta el nombre en su marco sin sustituir la declaración global.
- El motor evalúa el inicializador, define almacenamiento en el ámbito actual y convierte el tipo. En asignaciones posteriores evalúa primero la parte derecha. Los cálculos son locales; las variables no se guardan automáticamente en un perfil ni archivo JSON.

## Ejemplos

### 1. Actualizar un entero

```vb
# count empieza en 0, recibe 5 y LET suma 2. Main devuelve Integer 7. El primer DIM declara el nombre; las asignaciones posteriores cambian su valor.
Option Explicit On
SUB Main()
    DIM count AS Integer
    count = 5
    LET count = count + 2
    RETURN count
END SUB
```

**Explicación de los parámetros y la ejecución:**

count empieza en 0, recibe 5 y LET suma 2. Main devuelve Integer 7. El primer DIM declara el nombre; las asignaciones posteriores cambian su valor.

### 2. Texto y valor lógico

```vb
# label empieza como String vacía. SET guarda "ore". enabled es Boolean TRUE; la rama IF devuelve String "ore". TRUE sin comillas representa el 1 lógico.
Option Explicit On
SUB Main()
    DIM label AS String
    VAR enabled AS Boolean = TRUE
    SET label = "ore"
    IF enabled = TRUE THEN
        RETURN label
    END IF
    RETURN "disabled"
END SUB
```

**Explicación de los parámetros y la ejecución:**

label empieza como String vacía. SET guarda "ore". enabled es Boolean TRUE; la rama IF devuelve String "ore". TRUE sin comillas representa el 1 lógico.

### 3. Entrada global y cálculo local

```vb
# baseAmount es global y vale 4. extra es local de Calculate y vale 3. Calculate devuelve 7; Main lo guarda en su propio result local y devuelve 7. extra no es una variable local de Main.
Option Explicit On
VAR baseAmount AS Integer = 4
FUNCTION Calculate()
    VAR extra = 3
    RETURN baseAmount + extra
END FUNCTION
SUB Main()
    VAR result = Calculate()
    RETURN result
END SUB
```

**Explicación de los parámetros y la ejecución:**

baseAmount es global y vale 4. extra es local de Calculate y vale 3. Calculate devuelve 7; Main lo guarda en su propio result local y devuelve 7. extra no es una variable local de Main.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim
Runtime/Interpreter.cs: VisitVarDef / VisitAssignment
Runtime/SemanticScope.cs: DefineVar / SetVar / Coerce
-->
