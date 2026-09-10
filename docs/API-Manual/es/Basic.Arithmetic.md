# +, -, *, /, MOD

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Una expresión aritmética calcula un valor: + suma, - resta o cambia el signo, * multiplica, / divide y MOD devuelve el resto entero. Asigne el resultado a una variable o devuélvalo mediante RETURN.

## Sintaxis exacta

```text
left + right
left - right
-right
left * right
left / right
left MOD right
(expression)
```

## Parámetros

- `left` — Operando numérico izquierdo: literal, variable declarada, expresión entre paréntesis o resultado de función. El menos unario no tiene operando izquierdo.
- `right` — Operando numérico derecho. En / es el divisor; en MOD debe seguir siendo distinto de cero tras convertirse a Integer. Por ejemplo, 0.5 se trunca a 0 y provoca un error.
- `operator / precedence` — Prioridad: menos unario; después * / MOD al mismo nivel de izquierda a derecha; finalmente + - binarios de izquierda a derecha. Los paréntesis alteran el orden. No se admite más unario, potencia ^ ni división entera con barra inversa.

## Devuelve

Integer para +, -, * y menos unario con enteros; Decimal si algún operando numérico participante es Decimal. / siempre devuelve Decimal: 5/2=2.5. MOD devuelve Integer. Es un número calculado; el significado de éxito o cantidad depende del script.

## Comportamiento

- MOD convierte ambos operandos a enteros con signo de 32 bits, truncando hacia cero las fracciones representables. El resto conserva el signo del dividendo: -17 MOD 5=-2; -2147483648 MOD -1=0. La combinación de mayúsculas, incluso mOd, no cambia el resultado.
- MOD entre cero genera un error capturable con TRY/CATCH. / realiza división flotante: un numerador no nulo entre cero produce Infinity con signo, y 0/0 produce NaN. Compruebe el divisor si necesita un resultado finito.
- Las operaciones enteras +, -, * y negación conservan los 32 bits bajos al desbordarse; no amplían el tipo automáticamente. Para cálculos grandes convierta antes un operando a Decimal si acepta aproximaciones. La aritmética flotante tiene redondeos binarios.
- Los operadores numéricos ordinarios no interpretan texto automáticamente. String+String concatena, String+Integer falla. Elija una conversión explícita, por ejemplo CDbl. MOD infijo analiza texto entero de forma más estricta que la función BasicMod.
- El evaluador calcula los operandos en el orden de la expresión, selecciona el token del operador y crea una InjectionValue. Las expresiones entre paréntesis terminan primero. Solo hay movimiento, espera o red si un operando llama a una API que los realiza.

## Ejemplos

### 1. Prioridad y paréntesis

```vb
# plain=2+3*4 multiplica primero y vale 14. grouped=(2+3)*4 vale 20. Main devuelve plain*100+grouped=1420 para verificar ambos cálculos.
Option Explicit On
SUB Main()
    VAR plain = 2 + 3 * 4
    VAR grouped = (2 + 3) * 4
    RETURN plain * 100 + grouped
END SUB
```

**Explicación de los parámetros y la ejecución:**

plain=2+3*4 multiplica primero y vale 14. grouped=(2+3)*4 vale 20. Main devuelve plain*100+grouped=1420 para verificar ambos cálculos.

### 2. Lotes completos y objetos restantes

```vb
# DescribeBatches recibe total=27 y size=5. La comprobación rechaza tamaños nulos o negativos. Fix(total/size) convierte 5.4 en 5 lotes completos; total mOd size da 2 objetos restantes. CStr permite devolver el texto "5:2". La función auxiliar está definida por completo.
Option Explicit On
FUNCTION DescribeBatches(total, size)
    IF size <= 0 THEN
        RETURN "invalid"
    END IF
    VAR whole = Fix(total / size)
    VAR remaining = total mOd size
    RETURN CStr(whole) + ":" + CStr(remaining)
END FUNCTION
SUB Main()
    RETURN DescribeBatches(27, 5)
END SUB
```

**Explicación de los parámetros y la ejecución:**

DescribeBatches recibe total=27 y size=5. La comprobación rechaza tamaños nulos o negativos. Fix(total/size) convierte 5.4 en 5 lotes completos; total mOd size da 2 objetos restantes. CStr permite devolver el texto "5:2". La función auxiliar está definida por completo.

### 3. Capturar un divisor inválido

```vb
# 10 MOD 0 genera un error antes de asignar unusedResult. CATCH lo guarda en problem y establece caught=TRUE. Main devuelve 1 como indicador de gestión del error del ejemplo, no como resultado del MOD fallido.
Option Explicit On
SUB Main()
    VAR caught = FALSE
    TRY
        VAR unusedResult = 10 MOD 0
    CATCH problem
        caught = TRUE
    END TRY
    RETURN caught
END SUB
```

**Explicación de los parámetros y la ejecución:**

10 MOD 0 genera un error antes de asignar unusedResult. CATCH lo guarda en problem y establece caught=TRUE. Main devuelve 1 como indicador de gestión del error del ejemplo, no como resultado del MOD fallido.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: signedOperand / additiveOperand / comparativeOperand
Runtime/Interpreter.cs: VisitSignedOperand / VisitAdditiveOperand / VisitComparativeOperand
Runtime/InjectionValue.cs: arithmetic operators
Runtime/NumberConversions.cs: ToInt
-->
