# String + / &

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Una texto con + o la escritura Basic compatible &. Convierta los números explícitamente con CStr antes de añadir etiquetas, cantidades o coordenadas.

## Sintaxis exacta

```text
leftText + rightText
leftText & rightText
"label" & CStr(number)
```

## Parámetros

- `leftText` — Texto izquierdo: literal, variable String o resultado de función convertido a texto.
- `rightText` — Texto derecho. CStr(number) convierte un número; CStr(Unit) da texto vacío. Indique espacios, dos puntos y otros separadores.

## Devuelve

String si ambos operandos son String, sin indicador de éxito. Aquí & se normaliza a + y hereda sus reglas: dos números se suman, por lo que 2 & 3 da Integer 5. Mezclar String y número provoca un error. Difiere de la conversión implícita de VB.

## Comportamiento

- Ambos lados se evalúan y unen en orden, de izquierda a derecha en cadenas. Calcule una expresión numérica entre paréntesis y convierta su resultado antes de unirla.
- No se agregan separadores, espacios, comillas ni saltos de línea automáticamente. & dentro de un literal se conserva. El token lógico && sigue siendo AND y no concatena texto.
- CStr formatea números independientemente del idioma del cliente, con punto decimal. Convertir y concatenar no imprime ni envía nada; pase la String resultante a una API después si es necesario.
- Las cadenas son inmutables: unirlas crea un nuevo valor sin modificar las fuentes. Aumentar repetidamente una cadena grande copia su contenido; genere solo la salida necesaria en lugar de reconstruir todo un informe en cada iteración.

## Ejemplos

### 1. Etiquetar una cantidad

```vb
# amount=50 es Integer. CStr(amount) produce "50". "Items: " incluye dos puntos y espacio final. Main devuelve "Items: 50" sin imprimirlo automáticamente.
Option Explicit On
SUB Main()
    VAR amount = 50
    RETURN "Items: " & CStr(amount)
END SUB
```

**Explicación de los parámetros y la ejecución:**

amount=50 es Integer. CStr(amount) produce "50". "Items: " incluye dos puntos y espacio final. Main devuelve "Items: 50" sin imprimirlo automáticamente.

### 2. Función de formato completa

```vb
# Label recibe name="ore", amount=3. Une el nombre, dos puntos explícitos y CStr(amount). La función completa devuelve "ore:3" a Main y puede reutilizarse con otros nombres y cantidades.
Option Explicit On
FUNCTION Label(name, amount)
    RETURN name + ":" + CStr(amount)
END FUNCTION
SUB Main()
    RETURN Label("ore", 3)
END SUB
```

**Explicación de los parámetros y la ejecución:**

Label recibe name="ore", amount=3. Une el nombre, dos puntos explícitos y CStr(amount). La función completa devuelve "ore:3" a Main y puede reutilizarse con otros nombres y cantidades.

### 3. Calcular antes de unir

```vb
# CStr(2+3) calcula 5 y lo convierte en "5". El segundo literal conserva punto y coma, espacios y A&B. Main devuelve "Total: 5; literal: A&B".
Option Explicit On
SUB Main()
    RETURN "Total: " & CStr(2 + 3) & "; literal: A&B"
END SUB
```

**Explicación de los parámetros y la ejecución:**

CStr(2+3) calcula 5 y lo convierte en "5". El segundo literal conserva punto y coma, espacios y A&B. Main devuelve "Total: 5; literal: A&B".

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: ProtectLiteralText / ReplaceConcatenationOutsideLiterals
Runtime/InjectionValue.cs: operator + / explicit operator string
Runtime/InjectionApi.cs: CStr
-->
