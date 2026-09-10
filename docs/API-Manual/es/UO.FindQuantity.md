# UO.FindQuantity

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee la cantidad actual del primer resultado.

## Sintaxis exacta

```text
UO.FindQuantity() -> Any
```

## Parámetros

Sin parámetros.

## Devuelve

Integer — Amount actual del objeto indicado por FindItem(); 1 para un personaje existente, 0 para un objeto ausente/eliminado. No suma otras pilas. Lee el valor al efectuar la llamada.

## Comportamiento

- FindType con 1–5 argumentos, FindTypeEx y Count/CountEx/CountGround sustituyen los resultados de este script. Una búsqueda sin coincidencias vacía la instantánea. Guardar los valores necesarios antes de otra búsqueda.
- Estas llamadas no buscan, abren contenedores, mueven objetos ni envían paquetes. Leen datos cargados por el cliente. FindCount(id) no necesita una búsqueda anterior ni modifica sus resultados.
- FindItem/FindCount()/FindFullQuantity son instantáneas de la búsqueda. FindQuantity y FindCount(id) leen la cantidad actual; el objeto puede cambiar o desaparecer después de buscar.

## Ejemplos

### Leer una búsqueda de oro

```vb
# Leer una búsqueda de oro
#
# Lee la cantidad actual del primer resultado.
#
# Integer — Amount actual del objeto indicado por FindItem(); 1 para un personaje existente, 0
# para un objeto ausente/eliminado. No suma otras pilas. Lee el valor al efectuar la llamada.

SUB Main()
    # type=0x0EED es oro; color=-1 acepta cualquier color; backpack selecciona el contenido directo
    # con esta forma de FindType. value guarda el resultado; STR lo muestra como texto.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindQuantity()
    UO.Print(STR(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- type=0x0EED es oro; color=-1 acepta cualquier color; backpack selecciona el contenido directo con esta forma de FindType. value guarda el resultado; STR lo muestra como texto.

### Comparar objetos, pila y total

```vb
# Comparar objetos, pila y total
#
# Lee la cantidad actual del primer resultado.
#
# Integer — Amount actual del objeto indicado por FindItem(); 1 para un personaje existente, 0
# para un objeto ausente/eliminado. No suma otras pilas. Lee el valor al efectuar la llamada.

SUB Main()
    # Las cuatro lecturas siguen la misma búsqueda. Dos pilas de 50: objetos=2, primera pila=50,
    # total=100. FindItem es el ID único de la primera pila, no su type.

    UO.FindType(0x0EED, -1, 'backpack')
    UO.Print(STR(UO.FindCount()))
    UO.Print(STR(UO.FindQuantity()))
    UO.Print(STR(UO.FindFullQuantity()))
    UO.Print('0x' + Hex(UO.FindItem()))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- Las cuatro lecturas siguen la misma búsqueda. Dos pilas de 50: objetos=2, primera pila=50, total=100. FindItem es el ID único de la primera pila, no su type.

### Guardar un valor antes de buscar otra vez

```vb
# Guardar un valor antes de buscar otra vez
#
# Lee la cantidad actual del primer resultado.
#
# Integer — Amount actual del objeto indicado por FindItem(); 1 para un personaje existente, 0
# para un objeto ausente/eliminado. No suma otras pilas. Lee el valor al efectuar la llamada.

SUB Main()
    # El primer type es oro; 0x0F7A es otro reactivo. El segundo FindType sustituye la instantánea.
    # saved conserva el valor anterior; la última lectura usa el nuevo resultado.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindQuantity()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindQuantity()))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El primer type es oro; 0x0F7A es otro reactivo. El segundo FindType sustituye la instantánea. saved conserva el valor anterior; la última lectura usa el nuevo resultado.
