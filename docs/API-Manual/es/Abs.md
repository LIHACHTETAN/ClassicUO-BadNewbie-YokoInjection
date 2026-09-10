# Abs

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Devuelve el valor absoluto.

## Sintaxis exacta

```text
Abs(value:Any) -> Any
```

## Parámetros

- `value` — Obligatorio: Integer/Decimal o texto decimal con punto y exponente opcional, como "-1.25e2". Independiente del idioma. Texto inválido/hexadecimal, Unit, Array y Object dan 0; los literales hexadecimales numéricos ya son Integer. Posibles NaN/Infinity. Integer conserva tipo salvo -2147483648: Decimal 2147483648. Decimal/texto dan Decimal. NaN sigue NaN; ambos infinitos dan +Infinity.

## Devuelve

Integer/Decimal — abs(value). Integer conserva tipo salvo -2147483648: Decimal 2147483648. Decimal/texto dan Decimal. NaN sigue NaN; ambos infinitos dan +Infinity. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

## Comportamiento

- Cálculo local en el hilo del script, sin servidor, movimiento, objetivo, espera ni cambios de variables globales.
- Decimal es Double binario, no .NET decimal. Comparar resultados finitos aproximados con tolerancia. No usar NaN/Infinity como coordenadas o cantidades.
- Integer conserva tipo salvo -2147483648: Decimal 2147483648. Decimal/texto dan Decimal. NaN sigue NaN; ambos infinitos dan +Infinity.

### Funciones internas: de la llamada al resultado

Etapas reales de registro/conversión. Los auxiliares completos muestran fórmulas del script, sin sustituir las matemáticas de la plataforma.

#### 1. Register

Register enlaza el nombre BASIC con un cálculo nativo de un argumento y System.Math tras convertirlo. No ejecuta scripts ocultos ni procedimientos del servidor.

Integer/Decimal — abs(value). Integer conserva tipo salvo -2147483648: Decimal 2147483648. Decimal/texto dan Decimal. NaN sigue NaN; ambos infinitos dan +Infinity. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; función `Register`.

#### 2. BasicDouble

BasicDouble conserva Integer/Decimal, interpreta texto con NumberStyles.Float invariable y devuelve 0 para lo demás. Abs trata Integer ordinarios antes de usar Double.

Obligatorio: Integer/Decimal o texto decimal con punto y exponente opcional, como "-1.25e2". Independiente del idioma. Texto inválido/hexadecimal, Unit, Array y Object dan 0; los literales hexadecimales numéricos ya son Integer. Posibles NaN/Infinity.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; función `BasicDouble`.

#### 3. BasicAbs

Integer conserva tipo salvo -2147483648: Decimal 2147483648. Decimal/texto dan Decimal. NaN sigue NaN; ambos infinitos dan +Infinity.

Integer/Decimal — abs(value). Integer conserva tipo salvo -2147483648: Decimal 2147483648. Decimal/texto dan Decimal. NaN sigue NaN; ambos infinitos dan +Infinity. Número, no ID ni estado de éxito. 1/0 no indican éxito/fallo.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApi.cs`; función `BasicAbs`.

Cálculo local en el hilo del script, sin servidor, movimiento, objetivo, espera ni cambios de variables globales.


## Ejemplos

### Cálculo directo

```vb
# Cálculo directo
#
# Devuelve el valor absoluto.
#
# Integer/Decimal — abs(value). Integer conserva tipo salvo -2147483648: Decimal 2147483648.
# Decimal/texto dan Decimal. NaN sigue NaN; ambos infinitos dan +Infinity. Número, no ID ni
# estado de éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # value = -12; se espera 12 (~ indica aproximación). value guarda el resultado; CStr formatea
    # para Print.

    VAR value = Abs(-12)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value = -12; se espera 12 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Otro argumento mediante variable

```vb
# Otro argumento mediante variable
#
# Devuelve el valor absoluto.
#
# Integer/Decimal — abs(value). Integer conserva tipo salvo -2147483648: Decimal 2147483648.
# Decimal/texto dan Decimal. NaN sigue NaN; ambos infinitos dan +Infinity. Número, no ID ni
# estado de éxito. 1/0 no indican éxito/fallo.

SUB Main()
    # value = '-2.5'; se espera 2.5 (~ indica aproximación). value guarda el resultado; CStr
    # formatea para Print.

    VAR inputValue = '-2.5'
    VAR value = Abs(inputValue)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value = '-2.5'; se espera 2.5 (~ indica aproximación). value guarda el resultado; CStr formatea para Print.

### Función auxiliar completa

```vb
# Función auxiliar completa
#
# Devuelve el valor absoluto.
#
# Integer/Decimal — abs(value). Integer conserva tipo salvo -2147483648: Decimal 2147483648.
# Decimal/texto dan Decimal. NaN sigue NaN; ambos infinitos dan +Infinity. Número, no ID ni
# estado de éxito. 1/0 no indican éxito/fallo.

# manual-check: scalar-math Abs
SUB Main()
    # value/target son números; tolerance es desviación permitida >=0. IsWithin da Boolean 1/0;
    # tolerancia negativa: 0.

    VAR value = IsWithin(12,10,2)
    UO.Print(CStr(value))
END SUB

SUB IsWithin(value,target,tolerance)
    IF tolerance < 0 THEN
        RETURN 0
    END IF
    RETURN Abs(CDbl(value)-CDbl(target)) <= tolerance
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value/target son números; tolerance es desviación permitida >=0. IsWithin da Boolean 1/0; tolerancia negativa: 0.
