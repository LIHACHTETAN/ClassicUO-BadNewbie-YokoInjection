# Sqr

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Calcula la raíz cuadrada.

## Sintaxis exacta

```text
Sqr(number:Any) -> Decimal
```

## Parámetros

- `number` — Obligatorio: Integer/Decimal o texto decimal con punto y exponente opcional, como "-1.25e2". Independiente del idioma. Texto inválido/hexadecimal, Unit, Array y Object dan 0; los literales hexadecimales numéricos ya son Integer. Posibles NaN/Infinity. Entrada >=0: raíz no negativa. Negativo: NaN; +Infinity: Infinity; NaN sin cambio.

## Devuelve

Decimal — sqrt(number). Entrada >=0: raíz no negativa. Negativo: NaN; +Infinity: Infinity; NaN sin cambio. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

## Comportamiento

- Cálculo local en el hilo del script, sin servidor, movimiento, objetivo, espera ni cambios de variables globales.
- Decimal es Double binario, no .NET decimal. Comparar resultados finitos aproximados con tolerancia. No usar NaN/Infinity como coordenadas o cantidades.
- Entrada >=0: raíz no negativa. Negativo: NaN; +Infinity: Infinity; NaN sin cambio.

### Funciones internas: de la llamada al resultado

Etapas reales de registro/conversión. Los auxiliares completos muestran fórmulas del script, sin sustituir las matemáticas de la plataforma.

#### 1. Register

Register enlaza el nombre BASIC con un cálculo nativo de un argumento y System.Math tras convertirlo. No ejecuta scripts ocultos ni procedimientos del servidor.

Decimal — sqrt(number). Entrada >=0: raíz no negativa. Negativo: NaN; +Infinity: Infinity; NaN sin cambio. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

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
# Calcula la raíz cuadrada.
#
# Decimal — sqrt(number). Entrada >=0: raíz no negativa. Negativo: NaN; +Infinity: Infinity; NaN
# sin cambio. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # number = 25; se espera 5 (~ indica aproximación). value guarda el resultado; CStr formatea
    # para Print.

    VAR value = Sqr(25)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- number = 25; se espera 5 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Otro argumento mediante variable

```vb
# Otro argumento mediante variable
#
# Calcula la raíz cuadrada.
#
# Decimal — sqrt(number). Entrada >=0: raíz no negativa. Negativo: NaN; +Infinity: Infinity; NaN
# sin cambio. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # number = 2; se espera ~1.4142135623730951 (~ indica aproximación). value guarda el resultado;
    # CStr formatea para Print.

    VAR inputValue = 2
    VAR value = Sqr(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- number = 2; se espera ~1.4142135623730951 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Función auxiliar completa

```vb
# Función auxiliar completa
#
# Calcula la raíz cuadrada.
#
# Decimal — sqrt(number). Entrada >=0: raíz no negativa. Negativo: NaN; +Infinity: Infinity; NaN
# sin cambio. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

# manual-check: scalar-math Sqr
SUB Main()
    # dx/dy son diferencias. CDbl evita desbordamiento entero antes de sqrt(dx²+dy²).
    # SegmentLength(3,4)=5; distancia euclidiana, no ruta/colisión.

    VAR value = SegmentLength(3,4)
    UO.Print(CStr(value))
END SUB

SUB SegmentLength(dx,dy)
    VAR x = CDbl(dx)
    VAR y = CDbl(dy)
    RETURN Sqr(x*x+y*y)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- dx/dy son diferencias. CDbl evita desbordamiento entero antes de sqrt(dx²+dy²). SegmentLength(3,4)=5; distancia euclidiana, no ruta/colisión.
