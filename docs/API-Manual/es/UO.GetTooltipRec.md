# UO.GetTooltipRec

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee las propiedades estructuradas del objeto, con el ID cliloc y los parámetros de sustitución de cada entrada.

## Sintaxis exacta

```text
UO.GetTooltipRec(ObjID:Any) -> Array
```

## Parámetros

- `ObjID` — Serial obligatorio del objeto, no graphic/type ni ID cliloc. Entero, cadena decimal/hex, self, backpack, lasttarget, finditem o nombre AddObject. 0 no selecciona ningún objeto.

## Devuelve

Array<Array>: cada fila contiene [clilocID:Integer, parameters:Array<String>]. rows[i][0] es el ID del mensaje; rows[i][1] contiene sus parámetros. GetArrayLength(rows) cuenta propiedades. Array vacío si no se recibieron entradas o ObjID=0. No son serials de objetos.

## Comportamiento

- Los datos en caché se devuelven inmediatamente. Sin OPL se solicita información y se espera hasta 120 ms; cancelar el procedimiento interrumpe la espera. Una OPL vacía ya conocida se devuelve inmediatamente.
- El array BASIC representa TClilocRec: Count es GetArrayLength(rows), Items son las filas. Se omiten tabulaciones iniciales de transporte; los parámetros internos vacíos conservan su posición. #número sigue siendo una cadena para localizar. Los parámetros ausentes producen un array vacío. Modificar el resultado no cambia la caché.
- https://stealth.od.ua/api/GetTooltipRec/

## Ejemplos

### Listar los ID de propiedades

```vb
# Listar los ID de propiedades
#
# Lee las propiedades estructuradas del objeto, con el ID cliloc y los parámetros de sustitución
# de cada entrada.
#
# Array<Array>: cada fila contiene [clilocID:Integer, parameters:Array<String>]. rows[i][0] es
# el ID del mensaje; rows[i][1] contiene sus parámetros. GetArrayLength(rows) cuenta
# propiedades. Array vacío si no se recibieron entradas o ObjID=0. No son serials de objetos.

SUB Main()
    # ObjID=lasttarget selecciona el objeto. i comienza en 0; row[0] es un ID cliloc. Un array vacío
    # omite el bucle.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        UO.Print('Cliloc: ' + STR(row[0]))
        i = i + 1
    WEND
END SUB
```

**Explicación de los parámetros y la ejecución:**

- ObjID=lasttarget selecciona el objeto. i comienza en 0; row[0] es un ID cliloc. Un array vacío omite el bucle.

### Traducir cada propiedad

```vb
# Traducir cada propiedad
#
# Lee las propiedades estructuradas del objeto, con el ID cliloc y los parámetros de sustitución
# de cada entrada.
#
# Array<Array>: cada fila contiene [clilocID:Integer, parameters:Array<String>]. rows[i][0] es
# el ID del mensaje; rows[i][1] contiene sus parámetros. GetArrayLength(rows) cuenta
# propiedades. Array vacío si no se recibieron entradas o ObjID=0. No son serials de objetos.

SUB Main()
    # GetClilocByID recibe ClilocID=row[0] y Params=row[1], conservando el orden. No pase la fila
    # completa como Params.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR text = UO.GetClilocByID(row[0], row[1])
        UO.Print(text)
        i = i + 1
    WEND
END SUB
```

**Explicación de los parámetros y la ejecución:**

- GetClilocByID recibe ClilocID=row[0] y Params=row[1], conservando el orden. No pase la fila completa como Params.

### Leer un parámetro numérico

```vb
# Leer un parámetro numérico
#
# Lee las propiedades estructuradas del objeto, con el ID cliloc y los parámetros de sustitución
# de cada entrada.
#
# Array<Array>: cada fila contiene [clilocID:Integer, parameters:Array<String>]. rows[i][0] es
# el ID del mensaje; rows[i][1] contiene sus parámetros. GetArrayLength(rows) cuenta
# propiedades. Array vacío si no se recibieron entradas o ObjID=0. No son serials de objetos.

SUB Main()
    # wanted=1060401 es un ejemplo de ID que debe sustituirse. args[0] es String. Compruebe longitud
    # e IsNumeric antes de Val: el parámetro puede ser texto o #cliloc.

    VAR rows = UO.GetTooltipRec('lasttarget')
    VAR wanted = 1060401
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        VAR args = row[1]
        IF row[0] = wanted AND GetArrayLength(args) > 0 THEN
            IF IsNumeric(args[0]) THEN
                UO.Print('Value: ' + STR(Val(args[0])))
            END IF
        END IF
        i = i + 1
    WEND
END SUB
```

**Explicación de los parámetros y la ejecución:**

- wanted=1060401 es un ejemplo de ID que debe sustituirse. args[0] es String. Compruebe longitud e IsNumeric antes de Val: el parámetro puede ser texto o #cliloc.
