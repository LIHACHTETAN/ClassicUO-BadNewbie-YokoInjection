# Exp

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Eleva e a una potencia.

## Sintaxis exacta

```text
Exp(power:Any) -> Decimal
```

## Parámetros

- `power` — Obligatorio: Integer/Decimal o texto decimal con punto y exponente opcional, como "-1.25e2". Independiente del idioma. Texto inválido/hexadecimal, Unit, Array y Object dan 0; los literales hexadecimales numéricos ya son Integer. Posibles NaN/Infinity. Exp(0)=1. Muy positivo: Infinity; muy negativo: subdesbordamiento a 0. NaN sin cambio.

## Devuelve

Decimal — e^power. Exp(0)=1. Muy positivo: Infinity; muy negativo: subdesbordamiento a 0. NaN sin cambio. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

## Comportamiento

- Cálculo local en el hilo del script, sin servidor, movimiento, objetivo, espera ni cambios de variables globales.
- Decimal es Double binario, no .NET decimal. Comparar resultados finitos aproximados con tolerancia. No usar NaN/Infinity como coordenadas o cantidades.
- Exp(0)=1. Muy positivo: Infinity; muy negativo: subdesbordamiento a 0. NaN sin cambio.

### Funciones internas: de la llamada al resultado

Etapas reales de registro/conversión. Los auxiliares completos muestran fórmulas del script, sin sustituir las matemáticas de la plataforma.

#### 1. Register

Register enlaza el nombre BASIC con un cálculo nativo de un argumento y System.Math tras convertirlo. No ejecuta scripts ocultos ni procedimientos del servidor.

Decimal — e^power. Exp(0)=1. Muy positivo: Infinity; muy negativo: subdesbordamiento a 0. NaN sin cambio. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

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
# Eleva e a una potencia.
#
# Decimal — e^power. Exp(0)=1. Muy positivo: Infinity; muy negativo: subdesbordamiento a 0. NaN
# sin cambio. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # power = 0; se espera 1 (~ indica aproximación). value guarda el resultado; CStr formatea para
    # Print.

    VAR value = Exp(0)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- power = 0; se espera 1 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Otro argumento mediante variable

```vb
# Otro argumento mediante variable
#
# Eleva e a una potencia.
#
# Decimal — e^power. Exp(0)=1. Muy positivo: Infinity; muy negativo: subdesbordamiento a 0. NaN
# sin cambio. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # power = 1; se espera ~2.718281828459045 (~ indica aproximación). value guarda el resultado;
    # CStr formatea para Print.

    VAR inputValue = 1
    VAR value = Exp(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- power = 1; se espera ~2.718281828459045 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Función auxiliar completa

```vb
# Función auxiliar completa
#
# Eleva e a una potencia.
#
# Decimal — e^power. Exp(0)=1. Muy positivo: Infinity; muy negativo: subdesbordamiento a 0. NaN
# sin cambio. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

# manual-check: scalar-math Exp
SUB Main()
    # value inicial, rate tasa continua por unidad y period duración en esas unidades.
    # Growth(100,0.05,2)≈110.517; ejemplo numérico.

    VAR value = Growth(100,0.05,2)
    UO.Print(CStr(value))
END SUB

SUB Growth(value,rate,period)
    RETURN value*Exp(rate*period)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value inicial, rate tasa continua por unidad y period duración en esas unidades. Growth(100,0.05,2)≈110.517; ejemplo numérico.
