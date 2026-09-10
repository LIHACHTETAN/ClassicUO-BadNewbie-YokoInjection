# str

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Str(value) formatea un escalar Basic como texto.

## Sintaxis exacta

```text
str(value:Decimal) -> String
str(value:Integer) -> String
str(value:String) -> String
```

## Parámetros

- `value` — Un Integer, Decimal o String obligatorio. El tipo real selecciona la sobrecarga. Array, Object y Unit no tienen una sobrecarga Str compatible.

## Devuelve

String: texto numérico independiente del idioma o String original sin cambios. Los positivos no llevan espacio inicial. No hay parámetro de precisión.

## Comportamiento

- Cálculo local sin consultas al juego. Omitir el argumento es un error. Los atributos usan UO.Int()/UO.Str(), no Int()/Str(). Int usa BasicDouble y Math.Floor; Str selecciona InternalSubrutines.Str por tipo y formatea independientemente del idioma.

## Ejemplos

### Str — 1

```vb
# Str — 1
#
# Str(value) formatea un escalar Basic como texto.
#
# String: texto numérico independiente del idioma o String original sin cambios. Los positivos
# no llevan espacio inicial. No hay parámetro de precisión.

SUB Main()
    # value=42 es Integer. Str produce "42" sin espacio inicial; Main devuelve esa String.

    RETURN Str(42)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value=42 es Integer. Str produce "42" sin espacio inicial; Main devuelve esa String.

### Str — 2

```vb
# Str — 2
#
# Str(value) formatea un escalar Basic como texto.
#
# String: texto numérico independiente del idioma o String original sin cambios. Los positivos
# no llevan espacio inicial. No hay parámetro de precisión.

SUB Main()
    # amount=-12.5 es Decimal. Str guarda "-12.5" en text con punto para todos los idiomas. Main
    # devuelve text; amount sigue siendo numérico.

    VAR amount = -12.5
    VAR text = Str(amount)
    RETURN text
END SUB
```

**Explicación de los parámetros y la ejecución:**

- amount=-12.5 es Decimal. Str guarda "-12.5" en text con punto para todos los idiomas. Main devuelve text; amount sigue siendo numérico.

### Str — 3

```vb
# Str — 3
#
# Str(value) formatea un escalar Basic como texto.
#
# String: texto numérico independiente del idioma o String original sin cambios. Los positivos
# no llevan espacio inicial. No hay parámetro de precisión.

SUB Main()
    # ItemLabel recibe name="ore", count=3. Str(name) mantiene el nombre y Str(count) produce "3".
    # La función une los textos con " x"; Main devuelve "ore x3".

    RETURN ItemLabel("ore",3)
END SUB

SUB ItemLabel(name,count)
    RETURN Str(name) + " x" + Str(count)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- ItemLabel recibe name="ore", count=3. Str(name) mantiene el nombre y Str(count) produce "3". La función une los textos con " x"; Main devuelve "ore x3".
