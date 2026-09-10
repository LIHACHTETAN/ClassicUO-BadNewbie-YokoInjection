# UO.ApiSignatureExists

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Comprueba un nombre nativo con una cantidad de argumentos.

## Sintaxis exacta

```text
UO.ApiSignatureExists(name:String, argumentCount:Integer) -> Integer
```

## Parámetros

- `name` — String obligatoria: nombre registrado exacto, no expresión de llamada. Ignora mayúsculas y espacios exteriores; no añade UO. Vacío/desconocido devuelve 0. Excluye procedimientos del usuario.
- `argumentCount` — Integer obligatorio: número total de argumentos posicionales, incluidos los opcionales explícitos. Negativo/no admitido devuelve 0. No comprueba tipos de valores.

## Devuelve

Integer 1 si existe el registro, si no 0; permite comparar con TRUE/FALSE o 1/0. No confirma objetos, acciones ni permisos del servidor.

## Comportamiento

- No se distingue entre mayúsculas y minúsculas. InjectionApi registra Basic sin prefijo, InjectionApiUO el juego con UO. Una llamada corta antigua produce SC005 con sugerencia UO.; no se ejecuta una sustitución implícita. Los valores de atributos también requieren UO. ApiNameExists, ApiSignatureExists y ApiParameterExists quitan espacios exteriores y comprueban el nombre registrado exacto sin añadir prefijo. Consultan metadatos, no el servidor. No se implementa el operador de reflexión VB.NET GetType(TypeName).

## Ejemplos

### UO.ApiSignatureExists — 1

```vb
# UO.ApiSignatureExists — 1
#
# Comprueba un nombre nativo con una cantidad de argumentos.
#
# Integer 1 si existe el registro, si no 0; permite comparar con TRUE/FALSE o 1/0. No confirma
# objetos, acciones ni permisos del servidor.

SUB Main()
    # El primer ejemplo comprueba un nombre UO. explícito y devuelve 1. El nombre y la cantidad
    # requerida aparecen en la llamada.

    RETURN UO.ApiSignatureExists('UO.GetType',1)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El primer ejemplo comprueba un nombre UO. explícito y devuelve 1. El nombre y la cantidad requerida aparecen en la llamada.

### UO.ApiSignatureExists — 2

```vb
# UO.ApiSignatureExists — 2
#
# Comprueba un nombre nativo con una cantidad de argumentos.
#
# Integer 1 si existe el registro, si no 0; permite comparar con TRUE/FALSE o 1/0. No confirma
# objetos, acciones ni permisos del servidor.

SUB Main()
    # El segundo comprueba Basic o un selector: Int(value) existe, Int() no; backpack es un
    # selector. Resultado 1 o "1:0" según las llamadas.

    RETURN CStr(UO.ApiSignatureExists('Int',1)) + ':' + CStr(UO.ApiSignatureExists('Int',0))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El segundo comprueba Basic o un selector: Int(value) existe, Int() no; backpack es un selector. Resultado 1 o "1:0" según las llamadas.

### UO.ApiSignatureExists — 3

```vb
# UO.ApiSignatureExists — 3
#
# Comprueba un nombre nativo con una cantidad de argumentos.
#
# Integer 1 si existe el registro, si no 0; permite comparar con TRUE/FALSE o 1/0. No confirma
# objetos, acciones ni permisos del servidor.

SUB Main()
    # El tercero define el auxiliar completo y compara una forma corta eliminada o aridad ausente
    # con una válida. name, first, second, count pasan nombres/cantidad sin cambios. Resultado 0
    # para llamadas y "0:1" para valores.

    RETURN CheckForm('UO.GetType',0)
END SUB

FUNCTION CheckForm(name,count)
    RETURN UO.ApiSignatureExists(name,count)
END FUNCTION
```

**Explicación de los parámetros y la ejecución:**

- El tercero define el auxiliar completo y compara una forma corta eliminada o aridad ausente con una válida. name, first, second, count pasan nombres/cantidad sin cambios. Resultado 0 para llamadas y "0:1" para valores.
