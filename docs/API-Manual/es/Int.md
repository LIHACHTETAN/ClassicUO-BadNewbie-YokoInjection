# Int

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Int(value) redondea un número Basic hacia menos infinito.

## Sintaxis exacta

```text
Int(value:Any) -> Integer
```

## Parámetros

- `value` — Un Integer/Decimal o texto numérico obligatorio. El separador es el punto en cualquier idioma. Texto inválido, Array, Object y Unit se convierten en 0; comprueba las entradas con IsNumeric.

## Devuelve

Integer: floor(value), por ejemplo 2.9 -> 2, -2.9 -> -3. El resultado debe caber en Int32 con signo; evita valores no finitos y fuera de rango.

## Comportamiento

- Cálculo local sin consultas al juego. Omitir el argumento es un error. Los atributos usan UO.Int()/UO.Str(), no Int()/Str(). Int usa BasicDouble y Math.Floor; Str selecciona InternalSubrutines.Str por tipo y formatea independientemente del idioma.

## Ejemplos

### Int — 1

```vb
# Int — 1
#
# Int(value) redondea un número Basic hacia menos infinito.
#
# Integer: floor(value), por ejemplo 2.9 -> 2, -2.9 -> -3. El resultado debe caber en Int32 con
# signo; evita valores no finitos y fuera de rango.

SUB Main()
    # value=2.9. Redondear hacia abajo produce Integer 2, que devuelve Main.

    RETURN Int(2.9)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value=2.9. Redondear hacia abajo produce Integer 2, que devuelve Main.

### Int — 2

```vb
# Int — 2
#
# Int(value) redondea un número Basic hacia menos infinito.
#
# Integer: floor(value), por ejemplo 2.9 -> 2, -2.9 -> -3. El resultado debe caber en Int32 con
# signo; evita valores no finitos y fuera de rango.

SUB Main()
    # value=-2.9. Redondear hacia abajo da -3; truncar hacia cero daría -2. Main devuelve Integer
    # -3.

    VAR value = -2.9
    RETURN Int(value)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value=-2.9. Redondear hacia abajo da -3; truncar hacia cero daría -2. Main devuelve Integer -3.

### Int — 3

```vb
# Int — 3
#
# Int(value) redondea un número Basic hacia menos infinito.
#
# Integer: floor(value), por ejemplo 2.9 -> 2, -2.9 -> -3. El resultado debe caber en Int32 con
# signo; evita valores no finitos y fuera de rango.

SUB Main()
    # WholeUnits recibe total=27 y size=5. size<=0 devuelve 0; en otro caso Int(total/size) redondea
    # 5.4 hacia abajo. Main devuelve 5 unidades completas. Se define la función y sus dos
    # parámetros.

    RETURN WholeUnits(27,5)
END SUB

SUB WholeUnits(total,size)
    IF size <= 0 THEN
        RETURN 0
    END IF
    RETURN Int(total/size)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- WholeUnits recibe total=27 y size=5. size<=0 devuelve 0; en otro caso Int(total/size) redondea 5.4 hacia abajo. Main devuelve 5 unidades completas. Se define la función y sus dos parámetros.
