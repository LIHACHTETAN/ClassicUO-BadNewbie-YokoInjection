# Sgn

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Devuelve el signo.

## Sintaxis exacta

```text
Sgn(value:Any) -> Integer
```

## Parámetros

- `value` — Obligatorio: Integer/Decimal o texto decimal con punto y exponente opcional, como "-1.25e2". Independiente del idioma. Texto inválido/hexadecimal, Unit, Array y Object dan 0; los literales hexadecimales numéricos ya son Integer. Posibles NaN/Infinity. -1 negativo, 0 cero, +1 positivo. NaN causa error matemático; los infinitos dan su signo.

## Devuelve

Integer — sign(value). -1 negativo, 0 cero, +1 positivo. NaN causa error matemático; los infinitos dan su signo. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

## Comportamiento

- Cálculo local en el hilo del script, sin servidor, movimiento, objetivo, espera ni cambios de variables globales.
- Decimal es Double binario, no .NET decimal. Comparar resultados finitos aproximados con tolerancia. No usar NaN/Infinity como coordenadas o cantidades.
- -1 negativo, 0 cero, +1 positivo. NaN causa error matemático; los infinitos dan su signo.

### Funciones internas: de la llamada al resultado

Etapas reales de registro/conversión. Los auxiliares completos muestran fórmulas del script, sin sustituir las matemáticas de la plataforma.

#### 1. Register

Register enlaza el nombre BASIC con un cálculo nativo de un argumento y System.Math tras convertirlo. No ejecuta scripts ocultos ni procedimientos del servidor.

Integer — sign(value). -1 negativo, 0 cero, +1 positivo. NaN causa error matemático; los infinitos dan su signo. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; función `Register`.

#### 2. BasicDouble

BasicDouble conserva Integer/Decimal, interpreta texto con NumberStyles.Float invariable y devuelve 0 para lo demás. Abs trata Integer ordinarios antes de usar Double.

Obligatorio: Integer/Decimal o texto decimal con punto y exponente opcional, como "-1.25e2". Independiente del idioma. Texto inválido/hexadecimal, Unit, Array y Object dan 0; los literales hexadecimales numéricos ya son Integer. Posibles NaN/Infinity.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; función `BasicDouble`.

#### 3. BasicSgn

-1 negativo, 0 cero, +1 positivo. NaN causa error matemático; los infinitos dan su signo.

Integer — sign(value). -1 negativo, 0 cero, +1 positivo. NaN causa error matemático; los infinitos dan su signo. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; función `BasicSgn`.

Cálculo local en el hilo del script, sin servidor, movimiento, objetivo, espera ni cambios de variables globales.


## Ejemplos

### Cálculo directo

```vb
# Cálculo directo
#
# Devuelve el signo.
#
# Integer — sign(value). -1 negativo, 0 cero, +1 positivo. NaN causa error matemático; los
# infinitos dan su signo. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # value = -8; se espera -1 (~ indica aproximación). value guarda el resultado; CStr formatea
    # para Print.

    VAR value = Sgn(-8)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value = -8; se espera -1 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Otro argumento mediante variable

```vb
# Otro argumento mediante variable
#
# Devuelve el signo.
#
# Integer — sign(value). -1 negativo, 0 cero, +1 positivo. NaN causa error matemático; los
# infinitos dan su signo. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # value = 10-10; se espera 0 (~ indica aproximación). value guarda el resultado; CStr formatea
    # para Print.

    VAR inputValue = 10-10
    VAR value = Sgn(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value = 10-10; se espera 0 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Función auxiliar completa

```vb
# Función auxiliar completa
#
# Devuelve el signo.
#
# Integer — sign(value). -1 negativo, 0 cero, +1 positivo. NaN causa error matemático; los
# infinitos dan su signo. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

# manual-check: scalar-math Sgn
SUB Main()
    # current/destination en un eje. StepToward da -1/0/1, no ocho direcciones ni movimiento.

    VAR value = StepToward(12,10)
    UO.Print(CStr(value))
END SUB

SUB StepToward(current,destination)
    RETURN Sgn(CDbl(destination)-CDbl(current))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- current/destination en un eje. StepToward da -1/0/1, no ocho direcciones ni movimiento.
