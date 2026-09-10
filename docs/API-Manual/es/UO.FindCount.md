# UO.FindCount

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Cuenta objetos encontrados o unidades de una pila mediante su ID.

## Sintaxis exacta

```text
UO.FindCount() -> Integer
UO.FindCount(id:Any) -> Integer
```

## Parámetros

- `id` — Opcional solo para FindCount. Serial de un objeto: Integer, cadena decimal/hexadecimal, lasttarget, lastobject, backpack o nombre AddObject. Usar ID, no graphic/type. Nombre desconocido: 0. self identifica al personaje y aquí da 0. Sin argumento lee el número de objetos encontrados.

## Devuelve

Integer — FindCount() cuenta objetos: una pila cuenta como un item. FindCount(id) lee su Amount actual; los ID desconocidos/eliminados y los personajes devuelven 0. Un objeto no apilable normalmente tiene Amount=1. No devuelve ID, type ni Boolean.

## Comportamiento

- FindType con 1–5 argumentos, FindTypeEx y Count/CountEx/CountGround sustituyen los resultados de este script. Una búsqueda sin coincidencias vacía la instantánea. Guardar los valores necesarios antes de otra búsqueda.
- Estas llamadas no buscan, abren contenedores, mueven objetos ni envían paquetes. Leen datos cargados por el cliente. FindCount(id) no necesita una búsqueda anterior ni modifica sus resultados.
- FindItem/FindCount()/FindFullQuantity son instantáneas de la búsqueda. FindQuantity y FindCount(id) leen la cantidad actual; el objeto puede cambiar o desaparecer después de buscar.

## Ejemplos

### Leer una búsqueda de oro

```vb
# Leer una búsqueda de oro
#
# Cuenta objetos encontrados o unidades de una pila mediante su ID.
#
# Integer — FindCount() cuenta objetos: una pila cuenta como un item. FindCount(id) lee su
# Amount actual; los ID desconocidos/eliminados y los personajes devuelven 0. Un objeto no
# apilable normalmente tiene Amount=1. No devuelve ID, type ni Boolean.

SUB Main()
    # type=0x0EED es oro; color=-1 acepta cualquier color; backpack selecciona el contenido directo
    # con esta forma de FindType. value guarda el resultado; STR lo muestra como texto.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR value = UO.FindCount()
    UO.Print(STR(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- type=0x0EED es oro; color=-1 acepta cualquier color; backpack selecciona el contenido directo con esta forma de FindType. value guarda el resultado; STR lo muestra como texto.

### Comparar objetos, pila y total

```vb
# Comparar objetos, pila y total
#
# Cuenta objetos encontrados o unidades de una pila mediante su ID.
#
# Integer — FindCount() cuenta objetos: una pila cuenta como un item. FindCount(id) lee su
# Amount actual; los ID desconocidos/eliminados y los personajes devuelven 0. Un objeto no
# apilable normalmente tiene Amount=1. No devuelve ID, type ni Boolean.

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
# Cuenta objetos encontrados o unidades de una pila mediante su ID.
#
# Integer — FindCount() cuenta objetos: una pila cuenta como un item. FindCount(id) lee su
# Amount actual; los ID desconocidos/eliminados y los personajes devuelven 0. Un objeto no
# apilable normalmente tiene Amount=1. No devuelve ID, type ni Boolean.

SUB Main()
    # El primer type es oro; 0x0F7A es otro reactivo. El segundo FindType sustituye la instantánea.
    # saved conserva el valor anterior; la última lectura usa el nuevo resultado.

    UO.FindType(0x0EED, -1, 'backpack')
    VAR saved = UO.FindCount()
    UO.FindType(0x0F7A, -1, 'backpack')
    UO.Print(STR(saved))
    UO.Print(STR(UO.FindCount()))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El primer type es oro; 0x0F7A es otro reactivo. El segundo FindType sustituye la instantánea. saved conserva el valor anterior; la última lectura usa el nuevo resultado.

### Leer directamente un objeto por ID

```vb
# Leer directamente un objeto por ID
#
# Cuenta objetos encontrados o unidades de una pila mediante su ID.
#
# Integer — FindCount() cuenta objetos: una pila cuenta como un item. FindCount(id) lee su
# Amount actual; los ID desconocidos/eliminados y los personajes devuelven 0. Un objeto no
# apilable normalmente tiene Amount=1. No devuelve ID, type ni Boolean.

SUB Main()
    # lasttarget debe identificar un objeto ya seleccionado en el juego. No aparece un nuevo cursor.
    # FindCount(id) lee la pila actual, devuelve 0 si falta el objeto y conserva la instantánea de
    # búsqueda.

    VAR id = lasttarget
    VAR amount = UO.FindCount(id)
    UO.Print(STR(amount))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- lasttarget debe identificar un objeto ya seleccionado en el juego. No aparece un nuevo cursor. FindCount(id) lee la pila actual, devuelve 0 si falta el objeto y conserva la instantánea de búsqueda.
