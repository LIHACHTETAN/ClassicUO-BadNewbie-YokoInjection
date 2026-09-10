# SUB Main()

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Un archivo Basic contiene definiciones de procedimientos/funciones y declaraciones globales opcionales. Las acciones ejecutables van dentro de un procedimiento. Estos ejemplos son archivos completos con Main() como entrada.

## Sintaxis exacta

```text
Option Explicit On
SUB Main()
    statement
END SUB
# comment
; comment
REM comment
// comment
' comment
```

## Parámetros

- `Main / entry` — Procedimiento elegido para iniciar. Main es un nombre convencional, no una instrucción automática. SUB Main() declara un procedimiento sin argumentos. Una función auxiliar solo trabaja cuando se llama.
- `statement` — Una instrucción ejecutable por línea dentro de SUB…END SUB o FUNCTION…END FUNCTION. VAR/CONST globales y Option Explicit van fuera; Option Explicit precede a las declaraciones.
- `comment` — # y ; abren comentarios fuera de las cadenas, incluso después del código. REM, // y un apóstrofo abren líneas completas de comentario tras la sangría opcional. Dentro de una cadena pueden conservarse como texto.

## Devuelve

Cargar el archivo o declarar SUB no devuelve valores. RETURN expression devuelve el valor y termina inmediatamente la llamada. Alcanzar el final del cuerpo o usar RETURN solo produce Unit, sin valor.

## Comportamiento

- Guarde en UTF-8 para conservar comentarios y cadenas localizados. Se admiten CRLF y LF. Sangrías y líneas vacías mejoran la lectura sin sustituir END SUB ni END FUNCTION.
- Palabras clave, procedimientos y variables ignoran mayúsculas: itemCount, ITEMCOUNT e ItemCount son la misma asociación. El texto conserva su escritura; las claves de UO.SetGlobal("Key", …) son datos, no identificadores.
- Un nombre simple empieza con letra ASCII o guion bajo, seguido de letras, dígitos o guiones bajos. Evite palabras reservadas y nombres API. UO.Print es una llamada cualificada. Los dos puntos tras un nombre definen una etiqueta, no un separador general de instrucciones.
- El motor normaliza el Basic admitido, analiza todo el archivo, reúne declaraciones y comprueba nombres. Una función auxiliar puede estar debajo de Main. Cargar no inicia todas las definiciones: iniciar prepara el procedimiento elegido y sigue sus llamadas.
- Los ejemplos solo calculan valores. Tras verificar la plantilla, introduzca dentro las llamadas UO necesarias. Son reglas de este motor, sin prometer todas las capacidades de otras implementaciones Basic.

## Ejemplos

### 1. Comentarios y texto literal

```vb
# Main declara note con "ore #1; keep". # y ; dentro de la cadena se conservan. Los demás comentarios #, REM, // y apóstrofo no hacen nada. RETURN devuelve el texto original.
Option Explicit On
# Complete file
SUB Main()
    REM Full-line comment
    VAR note = "ore #1; keep" # Trailing comment
    // Another full-line comment
    ' Another full-line comment
    RETURN note
END SUB
```

**Explicación de los parámetros y la ejecución:**

Main declara note con "ore #1; keep". # y ; dentro de la cadena se conservan. Los demás comentarios #, REM, // y apóstrofo no hacen nada. RETURN devuelve el texto original.

### 2. Función auxiliar completa

```vb
# Main llama a DoubleCount con amount=7. Definida debajo, la función multiplica su parámetro Integer por 2 y devuelve 14. Main transmite ese resultado. No hacen falta archivos Include ausentes ni funciones sin declarar.
Option Explicit On
SUB Main()
    RETURN DoubleCount(7)
END SUB
FUNCTION DoubleCount(ByVal amount AS Integer)
    VAR result = amount * 2
    RETURN result
END FUNCTION
```

**Explicación de los parámetros y la ejecución:**

Main llama a DoubleCount con amount=7. Definida debajo, la función multiplica su parámetro Integer por 2 y devuelve 14. Main transmite ese resultado. No hacen falta archivos Include ausentes ni funciones sin declarar.

### 3. Mayúsculas en identificadores

```vb
# itemCount empieza en 3; ITEMCOUNT e itemcount suman 2 a la misma variable. Se aceptan palabras clave con mayúsculas mezcladas. Main devuelve 5 sin crear variables adicionales.
Option Explicit On
sUb Main()
    Var itemCount = 3
    ITEMCOUNT = itemcount + 2
    ReTuRn ItemCount
EnD sUb
```

**Explicación de los parámetros y la ejecución:**

itemCount empieza en 3; ITEMCOUNT e itemcount suman 2 a la misma variable. Se aceptan palabras clave con mayúsculas mezcladas. Main devuelve 5 sin crear variables adicionales.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: file / subrutine / LineComment / SYMBOL
Runtime/BasicSyntaxPreprocessor.cs: Process
Runtime/InjectionRuntime.cs: Prepare / Load / CallSubrutineValues
Runtime/SemanticScope.cs: Scope
https://learn.microsoft.com/en-us/dotnet/visual-basic/reference/language-specification/introduction (comparison of identifier casing only)
-->
