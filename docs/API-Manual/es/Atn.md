# Atn

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Calcula la arcotangente.

## Sintaxis exacta

```text
Atn(number:Any) -> Decimal
```

## Parámetros

- `number` — Obligatorio: Integer/Decimal o texto decimal con punto y exponente opcional, como "-1.25e2". Independiente del idioma. Texto inválido/hexadecimal, Unit, Array y Object dan 0; los literales hexadecimales numéricos ya son Integer. Posibles NaN/Infinity. Entrada pendiente, salida radianes en [-pi/2,pi/2]. Infinitos dan los extremos; NaN sigue NaN. No es atan2.

## Devuelve

Decimal — atan(number). Entrada pendiente, salida radianes en [-pi/2,pi/2]. Infinitos dan los extremos; NaN sigue NaN. No es atan2. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

## Comportamiento

- Cálculo local en el hilo del script, sin servidor, movimiento, objetivo, espera ni cambios de variables globales.
- Decimal es Double binario, no .NET decimal. Comparar resultados finitos aproximados con tolerancia. No usar NaN/Infinity como coordenadas o cantidades.
- Entrada pendiente, salida radianes en [-pi/2,pi/2]. Infinitos dan los extremos; NaN sigue NaN. No es atan2.

### Funciones internas: de la llamada al resultado

Etapas reales de registro/conversión. Los auxiliares completos muestran fórmulas del script, sin sustituir las matemáticas de la plataforma.

#### 1. Register

Register enlaza el nombre BASIC con un cálculo nativo de un argumento y System.Math tras convertirlo. No ejecuta scripts ocultos ni procedimientos del servidor.

Decimal — atan(number). Entrada pendiente, salida radianes en [-pi/2,pi/2]. Infinitos dan los extremos; NaN sigue NaN. No es atan2. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

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
# Calcula la arcotangente.
#
# Decimal — atan(number). Entrada pendiente, salida radianes en [-pi/2,pi/2]. Infinitos dan los
# extremos; NaN sigue NaN. No es atan2. Número, no ID ni estado de éxito. 1/0 no indican
# éxito/fallo.

SUB Main()
    # number = 0; se espera 0 (~ indica aproximación). value guarda el resultado; CStr formatea para
    # Print.

    VAR value = Atn(0)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- number = 0; se espera 0 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Otro argumento mediante variable

```vb
# Otro argumento mediante variable
#
# Calcula la arcotangente.
#
# Decimal — atan(number). Entrada pendiente, salida radianes en [-pi/2,pi/2]. Infinitos dan los
# extremos; NaN sigue NaN. No es atan2. Número, no ID ni estado de éxito. 1/0 no indican
# éxito/fallo.

SUB Main()
    # number = 1; se espera ~0.7853981633974483 (~ indica aproximación). value guarda el resultado;
    # CStr formatea para Print.

    VAR inputValue = 1
    VAR value = Atn(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- number = 1; se espera ~0.7853981633974483 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Función auxiliar completa

```vb
# Función auxiliar completa
#
# Calcula la arcotangente.
#
# Decimal — atan(number). Entrada pendiente, salida radianes en [-pi/2,pi/2]. Infinitos dan los
# extremos; NaN sigue NaN. No es atan2. Número, no ID ni estado de éxito. 1/0 no indican
# éxito/fallo.

# manual-check: scalar-math Atn
SUB Main()
    # rise/run es la pendiente. run=0 da alternativa 0, no ángulo vertical. SlopeDegrees(1,1)≈45; no
    # distingue todos los cuadrantes.

    VAR value = SlopeDegrees(1,1)
    UO.Print(CStr(value))
END SUB

SUB SlopeDegrees(rise,run)
    IF run = 0 THEN
        RETURN 0
    END IF
    RETURN Atn(CDbl(rise)/CDbl(run))*180/3.141592653589793
END SUB
```

**Explicación de los parámetros y la ejecución:**

- rise/run es la pendiente. run=0 da alternativa 0, no ángulo vertical. SlopeDegrees(1,1)≈45; no distingue todos los cuadrantes.
