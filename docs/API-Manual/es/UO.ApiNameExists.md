# UO.ApiNameExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Comprueba un nombre nativo invocable.

## Sintaxis exacta

```text
UO.ApiNameExists(name:String) -> Integer
```

## Parámetros

- `name` — String obligatoria: nombre registrado exacto, no expresión de llamada. Ignora mayúsculas y espacios exteriores; no añade UO. Vacío/desconocido devuelve 0. Excluye procedimientos del usuario.

## Devuelve

Integer 1 si existe el registro, si no 0; permite comparar con TRUE/FALSE o 1/0. No confirma objetos, acciones ni permisos del servidor.

## Comportamiento

- No se distingue entre mayúsculas y minúsculas. InjectionApi registra Basic sin prefijo, InjectionApiUO el juego con UO. Una llamada corta antigua produce SC005 con sugerencia UO.; no se ejecuta una sustitución implícita. Los valores de atributos también requieren UO. ApiNameExists, ApiSignatureExists y ApiParameterExists quitan espacios exteriores y comprueban el nombre registrado exacto sin añadir prefijo. Consultan metadatos, no el servidor. No se implementa el operador de reflexión VB.NET GetType(TypeName).

## Ejemplos

### UO.ApiNameExists — 1

```vb
# UO.ApiNameExists — 1
#
# Comprueba un nombre nativo invocable.
#
# Integer 1 si existe el registro, si no 0; permite comparar con TRUE/FALSE o 1/0. No confirma
# objetos, acciones ni permisos del servidor.

SUB Main()
    # El primer ejemplo comprueba un nombre UO. explícito y devuelve 1. El nombre y la cantidad
    # requerida aparecen en la llamada.

    RETURN UO.ApiNameExists('UO.GetType')
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El primer ejemplo comprueba un nombre UO. explícito y devuelve 1. El nombre y la cantidad requerida aparecen en la llamada.

### UO.ApiNameExists — 2

```vb
# UO.ApiNameExists — 2
#
# Comprueba un nombre nativo invocable.
#
# Integer 1 si existe el registro, si no 0; permite comparar con TRUE/FALSE o 1/0. No confirma
# objetos, acciones ni permisos del servidor.

SUB Main()
    # El segundo comprueba Basic o un selector: Int(value) existe, Int() no; backpack es un
    # selector. Resultado 1 o "1:0" según las llamadas.

    VAR name = 'CInt'
    RETURN UO.ApiNameExists(name)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El segundo comprueba Basic o un selector: Int(value) existe, Int() no; backpack es un selector. Resultado 1 o "1:0" según las llamadas.

### UO.ApiNameExists — 3

```vb
# UO.ApiNameExists — 3
#
# Comprueba un nombre nativo invocable.
#
# Integer 1 si existe el registro, si no 0; permite comparar con TRUE/FALSE o 1/0. No confirma
# objetos, acciones ni permisos del servidor.

SUB Main()
    # El tercero define el auxiliar completo y compara una forma corta eliminada o aridad ausente
    # con una válida. name, first, second, count pasan nombres/cantidad sin cambios. Resultado 0
    # para llamadas y "0:1" para valores.

    RETURN HasBoth('GetType','UO.GetType')
END SUB

FUNCTION HasBoth(first,second)
    RETURN UO.ApiNameExists(first) AndAlso UO.ApiNameExists(second)
END FUNCTION
```

**Explicación de los parámetros y la ejecución:**

- El tercero define el auxiliar completo y compara una forma corta eliminada o aridad ausente con una válida. name, first, second, count pasan nombres/cantidad sin cambios. Resultado 0 para llamadas y "0:1" para valores.
