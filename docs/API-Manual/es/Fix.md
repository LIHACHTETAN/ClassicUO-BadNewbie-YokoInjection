# Fix

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Trunca la fracción hacia cero.

## Sintaxis exacta

```text
Fix(value:Any) -> Integer
```

## Parámetros

- `value` — Obligatorio: Integer/Decimal o texto decimal con punto y exponente opcional, como "-1.25e2". Independiente del idioma. Texto inválido/hexadecimal, Unit, Array y Object dan 0; los literales hexadecimales numéricos ya son Integer. Posibles NaN/Infinity. Entrada finita, resultado truncado en -2147483648..2147483647. -2.9 da -2, no floor=-3. Fuera de rango/NaN/Infinity no son válidos.

## Devuelve

Integer — truncate(value). Entrada finita, resultado truncado en -2147483648..2147483647. -2.9 da -2, no floor=-3. Fuera de rango/NaN/Infinity no son válidos. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

## Comportamiento

- Cálculo local en el hilo del script, sin servidor, movimiento, objetivo, espera ni cambios de variables globales.
- Decimal es Double binario, no .NET decimal. Comparar resultados finitos aproximados con tolerancia. No usar NaN/Infinity como coordenadas o cantidades.
- Entrada finita, resultado truncado en -2147483648..2147483647. -2.9 da -2, no floor=-3. Fuera de rango/NaN/Infinity no son válidos.

### Funciones internas: de la llamada al resultado

Etapas reales de registro/conversión. Los auxiliares completos muestran fórmulas del script, sin sustituir las matemáticas de la plataforma.

#### 1. Register

Register enlaza el nombre BASIC con un cálculo nativo de un argumento y System.Math tras convertirlo. No ejecuta scripts ocultos ni procedimientos del servidor.

Integer — truncate(value). Entrada finita, resultado truncado en -2147483648..2147483647. -2.9 da -2, no floor=-3. Fuera de rango/NaN/Infinity no son válidos. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; función `Register`.

#### 2. BasicDouble

BasicDouble conserva Integer/Decimal, interpreta texto con NumberStyles.Float invariable y devuelve 0 para lo demás. Abs trata Integer ordinarios antes de usar Double.

Obligatorio: Integer/Decimal o texto decimal con punto y exponente opcional, como "-1.25e2". Independiente del idioma. Texto inválido/hexadecimal, Unit, Array y Object dan 0; los literales hexadecimales numéricos ya son Integer. Posibles NaN/Infinity.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; función `BasicDouble`.

Cálculo local en el hilo del script, sin servidor, movimiento, objetivo, espera ni cambios de variables globales.


## Ejemplos

### Cálculo directo

```vb
# Cálculo directo
#
# Trunca la fracción hacia cero.
#
# Integer — truncate(value). Entrada finita, resultado truncado en -2147483648..2147483647. -2.9
# da -2, no floor=-3. Fuera de rango/NaN/Infinity no son válidos. Número, no ID ni estado de
# éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # value = 2.9; se espera 2 (~ indica aproximación). value guarda el resultado; CStr formatea
    # para Print.

    VAR value = Fix(2.9)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value = 2.9; se espera 2 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Otro argumento mediante variable

```vb
# Otro argumento mediante variable
#
# Trunca la fracción hacia cero.
#
# Integer — truncate(value). Entrada finita, resultado truncado en -2147483648..2147483647. -2.9
# da -2, no floor=-3. Fuera de rango/NaN/Infinity no son válidos. Número, no ID ni estado de
# éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # value = -2.9; se espera -2 (~ indica aproximación). value guarda el resultado; CStr formatea
    # para Print.

    VAR inputValue = -2.9
    VAR value = Fix(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value = -2.9; se espera -2 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Función auxiliar completa

```vb
# Función auxiliar completa
#
# Trunca la fracción hacia cero.
#
# Integer — truncate(value). Entrada finita, resultado truncado en -2147483648..2147483647. -2.9
# da -2, no floor=-3. Fuera de rango/NaN/Infinity no son válidos. Número, no ID ni estado de
# éxito. 1/0 no indican éxito/fallo.

# manual-check: scalar-math Fix
SUB Main()
    # total>=0 y size>0: lotes completos; 27/5 da 5. Entrada inválida: alternativa 0, también válida
    # sin lote. Cociente dentro de Integer.

    VAR value = WholeBatches(27,5)
    UO.Print(CStr(value))
END SUB

SUB WholeBatches(total,size)
    IF total < 0 OR size <= 0 THEN
        RETURN 0
    END IF
    RETURN Fix(CDbl(total)/CDbl(size))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- total>=0 y size>0: lotes completos; 27/5 da 5. Entrada inválida: alternativa 0, también válida sin lote. Cociente dentro de Integer.
