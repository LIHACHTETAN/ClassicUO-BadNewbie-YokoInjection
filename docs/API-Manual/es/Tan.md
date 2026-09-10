# Tan

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Calcula la tangente.

## Sintaxis exacta

```text
Tan(radians:Any) -> Decimal
```

## Parámetros

- `radians` — Obligatorio: Integer/Decimal o texto decimal con punto y exponente opcional, como "-1.25e2". Independiente del idioma. Texto inválido/hexadecimal, Unit, Array y Object dan 0; los literales hexadecimales numéricos ya son Integer. Posibles NaN/Infinity. Radianes. Resultado ilimitado, enorme e inestable cerca de pi/2+k*pi. NaN/infinito dan NaN.

## Devuelve

Decimal — tan(radians). Radianes. Resultado ilimitado, enorme e inestable cerca de pi/2+k*pi. NaN/infinito dan NaN. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

## Comportamiento

- Cálculo local en el hilo del script, sin servidor, movimiento, objetivo, espera ni cambios de variables globales.
- Decimal es Double binario, no .NET decimal. Comparar resultados finitos aproximados con tolerancia. No usar NaN/Infinity como coordenadas o cantidades.
- Radianes. Resultado ilimitado, enorme e inestable cerca de pi/2+k*pi. NaN/infinito dan NaN.

### Funciones internas: de la llamada al resultado

Etapas reales de registro/conversión. Los auxiliares completos muestran fórmulas del script, sin sustituir las matemáticas de la plataforma.

#### 1. Register

Register enlaza el nombre BASIC con un cálculo nativo de un argumento y System.Math tras convertirlo. No ejecuta scripts ocultos ni procedimientos del servidor.

Decimal — tan(radians). Radianes. Resultado ilimitado, enorme e inestable cerca de pi/2+k*pi. NaN/infinito dan NaN. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

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
# Calcula la tangente.
#
# Decimal — tan(radians). Radianes. Resultado ilimitado, enorme e inestable cerca de pi/2+k*pi.
# NaN/infinito dan NaN. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # radians = 0; se espera 0 (~ indica aproximación). value guarda el resultado; CStr formatea
    # para Print.

    VAR value = Tan(0)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- radians = 0; se espera 0 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Otro argumento mediante variable

```vb
# Otro argumento mediante variable
#
# Calcula la tangente.
#
# Decimal — tan(radians). Radianes. Resultado ilimitado, enorme e inestable cerca de pi/2+k*pi.
# NaN/infinito dan NaN. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # radians = 0.7853981633974483; se espera ~1 (~ indica aproximación). value guarda el resultado;
    # CStr formatea para Print.

    VAR inputValue = 0.7853981633974483
    VAR value = Tan(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- radians = 0.7853981633974483; se espera ~1 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Función auxiliar completa

```vb
# Función auxiliar completa
#
# Calcula la tangente.
#
# Decimal — tan(radians). Radianes. Resultado ilimitado, enorme e inestable cerca de pi/2+k*pi.
# NaN/infinito dan NaN. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

# manual-check: scalar-math Tan
SUB Main()
    # degrees en grados; pi/180 convierte antes de Tan. TangentDegrees(45)≈1; evitar singularidades.

    VAR value = TangentDegrees(45)
    UO.Print(CStr(value))
END SUB

SUB TangentDegrees(degrees)
    RETURN Tan(degrees*3.141592653589793/180)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- degrees en grados; pi/180 convierte antes de Tan. TangentDegrees(45)≈1; evitar singularidades.
