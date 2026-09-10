# UO.ApiParameterExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Comprueba un valor intrínseco o selector de objeto.

## Sintaxis exacta

```text
UO.ApiParameterExists(name:String) -> Integer
```

## Parámetros

- `name` — String obligatoria: nombre registrado exacto, no expresión de llamada. Ignora mayúsculas y espacios exteriores; no añade UO. Vacío/desconocido devuelve 0. Excluye procedimientos del usuario.

## Devuelve

Integer 1 si existe el registro, si no 0; permite comparar con TRUE/FALSE o 1/0. No confirma objetos, acciones ni permisos del servidor.

## Comportamiento

- No se distingue entre mayúsculas y minúsculas. InjectionApi registra Basic sin prefijo, InjectionApiUO el juego con UO. Una llamada corta antigua produce SC005 con sugerencia UO.; no se ejecuta una sustitución implícita. Los valores de atributos también requieren UO. ApiNameExists, ApiSignatureExists y ApiParameterExists quitan espacios exteriores y comprueban el nombre registrado exacto sin añadir prefijo. Consultan metadatos, no el servidor. No se implementa el operador de reflexión VB.NET GetType(TypeName).

## Ejemplos

### UO.ApiParameterExists — 1

```vb
# UO.ApiParameterExists — 1
#
# Comprueba un valor intrínseco o selector de objeto.
#
# Integer 1 si existe el registro, si no 0; permite comparar con TRUE/FALSE o 1/0. No confirma
# objetos, acciones ni permisos del servidor.

SUB Main()
    # El primer ejemplo comprueba un nombre UO. explícito y devuelve 1. El nombre y la cantidad
    # requerida aparecen en la llamada.

    RETURN UO.ApiParameterExists('UO.GetHP')
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El primer ejemplo comprueba un nombre UO. explícito y devuelve 1. El nombre y la cantidad requerida aparecen en la llamada.

### UO.ApiParameterExists — 2

```vb
# UO.ApiParameterExists — 2
#
# Comprueba un valor intrínseco o selector de objeto.
#
# Integer 1 si existe el registro, si no 0; permite comparar con TRUE/FALSE o 1/0. No confirma
# objetos, acciones ni permisos del servidor.

SUB Main()
    # El segundo comprueba Basic o un selector: Int(value) existe, Int() no; backpack es un
    # selector. Resultado 1 o "1:0" según las llamadas.

    VAR name = 'backpack'
    RETURN UO.ApiParameterExists(name)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El segundo comprueba Basic o un selector: Int(value) existe, Int() no; backpack es un selector. Resultado 1 o "1:0" según las llamadas.

### UO.ApiParameterExists — 3

```vb
# UO.ApiParameterExists — 3
#
# Comprueba un valor intrínseco o selector de objeto.
#
# Integer 1 si existe el registro, si no 0; permite comparar con TRUE/FALSE o 1/0. No confirma
# objetos, acciones ni permisos del servidor.

SUB Main()
    # El tercero define el auxiliar completo y compara una forma corta eliminada o aridad ausente
    # con una válida. name, first, second, count pasan nombres/cantidad sin cambios. Resultado 0
    # para llamadas y "0:1" para valores.

    RETURN CompareNames('GetHP','UO.GetHP')
END SUB

FUNCTION CompareNames(first,second)
    RETURN CStr(UO.ApiParameterExists(first)) + ":" + CStr(UO.ApiParameterExists(second))
END FUNCTION
```

**Explicación de los parámetros y la ejecución:**

- El tercero define el auxiliar completo y compara una forma corta eliminada o aridad ausente con una válida. name, first, second, count pasan nombres/cantidad sin cambios. Resultado 0 para llamadas y "0:1" para valores.
