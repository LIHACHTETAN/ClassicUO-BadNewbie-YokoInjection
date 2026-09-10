# Log

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Calcula el logaritmo natural.

## Sintaxis exacta

```text
Log(number:Any) -> Decimal
```

## Parámetros

- `number` — Obligatorio: Integer/Decimal o texto decimal con punto y exponente opcional, como "-1.25e2". Independiente del idioma. Texto inválido/hexadecimal, Unit, Array y Object dan 0; los literales hexadecimales numéricos ya son Integer. Posibles NaN/Infinity. Base e, no 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity: Infinity.

## Devuelve

Decimal — ln(number). Base e, no 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity: Infinity. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

## Comportamiento

- Cálculo local en el hilo del script, sin servidor, movimiento, objetivo, espera ni cambios de variables globales.
- Decimal es Double binario, no .NET decimal. Comparar resultados finitos aproximados con tolerancia. No usar NaN/Infinity como coordenadas o cantidades.
- Base e, no 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity: Infinity.

### Funciones internas: de la llamada al resultado

Etapas reales de registro/conversión. Los auxiliares completos muestran fórmulas del script, sin sustituir las matemáticas de la plataforma.

#### 1. Register

Register enlaza el nombre BASIC con un cálculo nativo de un argumento y System.Math tras convertirlo. No ejecuta scripts ocultos ni procedimientos del servidor.

Decimal — ln(number). Base e, no 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity: Infinity. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

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
# Calcula el logaritmo natural.
#
# Decimal — ln(number). Base e, no 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity:
# Infinity. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # number = 1; se espera 0 (~ indica aproximación). value guarda el resultado; CStr formatea para
    # Print.

    VAR value = Log(1)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- number = 1; se espera 0 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Otro argumento mediante variable

```vb
# Otro argumento mediante variable
#
# Calcula el logaritmo natural.
#
# Decimal — ln(number). Base e, no 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity:
# Infinity. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # number = 2.718281828459045; se espera ~1 (~ indica aproximación). value guarda el resultado;
    # CStr formatea para Print.

    VAR inputValue = 2.718281828459045
    VAR value = Log(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- number = 2.718281828459045; se espera ~1 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Función auxiliar completa

```vb
# Función auxiliar completa
#
# Calcula el logaritmo natural.
#
# Decimal — ln(number). Base e, no 10. Log(1)=0, Log(0)=-Infinity; negativo: NaN; +Infinity:
# Infinity. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

# manual-check: scalar-math Log
SUB Main()
    # value>0, baseValue>0 y <>1. Log(value)/Log(baseValue); LogBase(100,10)≈2. Entrada inválida:
    # alternativa 0, también posible resultado válido.

    VAR value = LogBase(100,10)
    UO.Print(CStr(value))
END SUB

SUB LogBase(value,baseValue)
    IF value <= 0 OR baseValue <= 0 OR baseValue = 1 THEN
        RETURN 0
    END IF
    RETURN Log(value)/Log(baseValue)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value>0, baseValue>0 y <>1. Log(value)/Log(baseValue); LogBase(100,10)≈2. Entrada inválida: alternativa 0, también posible resultado válido.
