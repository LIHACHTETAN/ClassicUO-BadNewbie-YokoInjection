# 123 / 0x0EED / "text" / TRUE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Un literal escribe un valor directamente en el código. Números y textos entre comillas no requieren declaraciones. TRUE/FALSE son valores lógicos predefinidos. Un número entre comillas sigue siendo texto hasta convertirlo.

## Sintaxis exacta

```text
123
-2147483648
0x0EED
0xFFFFFFFF
2.5
"text"
'text'
TRUE
FALSE
```

## Parámetros

- `integer / hexadecimal` — Integer decimal de -2147483648 a 2147483647, o 0x con dígitos hexadecimales 0–9/A–F. Use x minúscula. El literal representa 32 bits: 0xFFFFFFFF es Integer -1, no un positivo de 64 bits.
- `floating` — Flotante con dígitos antes y después del punto: 2.5 o -0.25. Escriba 0.5 en vez de .5. La coma, el exponente 1e3 y los sufijos numéricos no están admitidos por esta gramática.
- `text` — Texto entre comillas simples o dobles coincidentes. Para incluir una comilla use la otra forma o Chr(34)/Chr(39). No se interpretan escapes con barra inversa ni comillas duplicadas. Mantenga la cadena de ejemplo en una línea física.
- `TRUE / FALSE` — TRUE es Integer 1 y FALSE es Integer 0. No vuelva a declarar estos nombres. Son valores, no llamadas: TRUE, no TRUE().

## Devuelve

Un entero/hexadecimal da Integer; un número con punto da Decimal, flotante binario; un texto entre comillas da String. TRUE/FALSE dan Integer 1/0. Evaluar un valor no realiza acciones de juego ni declara variables.

## Comportamiento

- El signo de -5 es una operación unaria. -2147483648 se trata como mínimo entero sin tener que almacenar antes su magnitud positiva. Los enteros fuera de rango fallan; valores aproximados mayores necesitan flotantes adecuados.
- El texto conserva caracteres y mayúsculas. "350" no es el número 350, "false" no es FALSE. # y ; son texto dentro de comillas y comentarios fuera. Las conversiones se explican en AS y en las fichas de funciones.
- El motor reconoce el token, interpreta números con cultura invariable o elimina las comillas exteriores. Cambiar el idioma del IDE no cambia el separador decimal del código.
- Serial, tipo gráfico y coordenada pueden ser numéricos. El literal no define su significado: lo hace el contrato del parámetro de la API llamada.

## Ejemplos

### 1. Tipo hexadecimal y límite entero

```vb
# itemType=0x0EED equivale a 3821. lowest=-2147483648 coincide con el patrón con signo 0x80000000. Main devuelve itemType=3821. No se busca ningún objeto.
Option Explicit On
SUB Main()
    VAR itemType = 0x0EED
    VAR lowest = -2147483648
    IF lowest = 0x80000000 THEN
        RETURN itemType
    END IF
    RETURN 0
END SUB
```

**Explicación de los parámetros y la ejecución:**

itemType=0x0EED equivale a 3821. lowest=-2147483648 coincide con el patrón con signo 0x80000000. Main devuelve itemType=3821. No se busca ningún objeto.

### 2. Ambos tipos de comillas

```vb
# owner="O'Brien" contiene un apóstrofo. instruction usa comillas simples alrededor de texto con dobles. Unir owner, " | " e instruction devuelve O'Brien | say "go", sin escapes con barra inversa en el script.
Option Explicit On
SUB Main()
    VAR owner = "O'Brien"
    VAR instruction = 'say "go"'
    RETURN owner + " | " + instruction
END SUB
```

**Explicación de los parámetros y la ejecución:**

owner="O'Brien" contiene un apóstrofo. instruction usa comillas simples alrededor de texto con dobles. Unir owner, " | " e instruction devuelve O'Brien | say "go", sin escapes con barra inversa en el script.

### 3. Valores lógicos numéricos

```vb
# enabled=TRUE guarda 1 y stopped=FALSE guarda 0. El cálculo da 1*10+0=10. Main devuelve un resultado numérico, no el TRUE canónico.
Option Explicit On
SUB Main()
    VAR enabled = TRUE
    VAR stopped = FALSE
    RETURN enabled * 10 + stopped
END SUB
```

**Explicación de los parámetros y la ejecución:**

enabled=TRUE guarda 1 y stopped=FALSE guarda 0. El cálculo da 1*10+0=10. Main devuelve un resultado numérico, no el TRUE canónico.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: number / literal / HEX_NUMBER / DEC_NUMBER
Runtime/Interpreter.cs: VisitNumber / VisitLiteral / VisitSignedOperand
Runtime/InjectionApiUO.cs: TRUE / FALSE intrinsic values
-->
