# UO.Backpack

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Devuelve el ID de la mochila equipada actualmente.

## Sintaxis exacta

```text
UO.Backpack() -> Integer
```

## Parámetros

Sin parámetros.

## Devuelve

Integer — serial/ID, no graphic/type, capa, cantidad ni Boolean. 0: no hay objeto actual. Conserva los 32 bits; comprueba <> 0, no = TRUE o > 0. Un resultado guardado no se actualiza solo. Busca el item no destruido en la capa Backpack de Player. Player o mochila ausente/destruido da 0. Identifica el contenedor, no su contenido; no crea bolsas.

## Comportamiento

- Sin argumentos. Lectura local mediante Invoke en el hilo del juego; cancelar puede interrumpir la espera del hilo. No envía paquetes, abre contenedores, activa target ni mueve items.
- Los intrínsecos self/backpack sin paréntesis se leen de nuevo salvo que una variable los oculte. Los alias de texto dependen del comando receptor. Como destino de transferencia, "self" significa mochila; UO.Self() devuelve el personaje. Para un contenedor usa UO.Backpack().
- World.Clear elimina Player; las siguientes lecturas dan 0. Entrar al mundo o sustituir la mochila puede cambiar el ID. Las lecturas separadas no son atómicas. Un ID no nulo no prueba conexión, permiso del servidor o contenido cargado.

### Funciones internas: de la llamada al resultado

Etapas reales de lectura del objeto del cliente. IsOwnSerial es la función completa del ejemplo, no otra API integrada.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility selecciona la rama sin argumentos y envuelve el Integer del bridge en InjectionValue. Sin parámetro de salida Pascal ni argumento opcional adicional.

Integer — serial/ID, no graphic/type, capa, cantidad ni Boolean. 0: no hay objeto actual. Conserva los 32 bits; comprueba <> 0, no = TRUE o > 0. Un resultado guardado no se actualiza solo.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `ExecuteStealthCompatibility`.

#### 2. Invoke

Busca el item no destruido en la capa Backpack de Player. Player o mochila ausente/destruido da 0. Identifica el contenedor, no su contenido; no crea bolsas. Invoke lee en el hilo del juego; un hilo de trabajo espera el procesamiento del gestor. Cancelar el script interrumpe esa espera. No añade demoras ni consultas de red.

Integer — serial/ID, no graphic/type, capa, cantidad ni Boolean. 0: no hay objeto actual. Conserva los 32 bits; comprueba <> 0, no = TRUE o > 0. Un resultado guardado no se actualiza solo. Sin argumentos. Lectura local mediante Invoke en el hilo del juego; cancelar puede interrumpir la espera del hilo. No envía paquetes, abre contenedores, activa target ni mueve items.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 3. FindItemByLayer

Busca el item no destruido en la capa Backpack de Player. Player o mochila ausente/destruido da 0. Identifica el contenedor, no su contenido; no crea bolsas.

Integer — serial/ID, no graphic/type, capa, cantidad ni Boolean. 0: no hay objeto actual. Conserva los 32 bits; comprueba <> 0, no = TRUE o > 0. Un resultado guardado no se actualiza solo.

Código del proyecto: `src/ClassicUO.Client/Game/GameObjects/Entity.cs`; función `FindItemByLayer`.

#### 4. Clear

World.Clear elimina Player; las siguientes lecturas dan 0. Entrar al mundo o sustituir la mochila puede cambiar el ID. Las lecturas separadas no son atómicas. Un ID no nulo no prueba conexión, permiso del servidor o contenido cargado.

World.Clear elimina Player; las siguientes lecturas dan 0. Entrar al mundo o sustituir la mochila puede cambiar el ID. Las lecturas separadas no son atómicas. Un ID no nulo no prueba conexión, permiso del servidor o contenido cargado.

Código del proyecto: `src/ClassicUO.Client/Game/World.cs`; función `Clear`.

World.Clear elimina Player; las siguientes lecturas dan 0. Entrar al mundo o sustituir la mochila puede cambiar el ID. Las lecturas separadas no son atómicas. Un ID no nulo no prueba conexión, permiso del servidor o contenido cargado.


## Ejemplos

### Leer y mostrar el ID

```vb
# Leer y mostrar el ID
#
# Devuelve el ID de la mochila equipada actualmente.
#
# Integer — serial/ID, no graphic/type, capa, cantidad ni Boolean. 0: no hay objeto actual.
# Conserva los 32 bits; comprueba <> 0, no = TRUE o > 0. Un resultado guardado no se actualiza
# solo. Busca el item no destruido en la capa Backpack de Player. Player o mochila
# ausente/destruido da 0. Identifica el contenedor, no su contenido; no crea bolsas.

SUB Main()
    # id guarda un resultado; HEX formatea el serial para el diario. No selecciona ni usa el objeto.

    VAR id = UO.Backpack()
    UO.Print('ID: ' + HEX(id))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- id guarda un resultado; HEX formatea el serial para el diario. No selecciona ni usa el objeto.

### Detectar un cambio de ID

```vb
# Detectar un cambio de ID
#
# Devuelve el ID de la mochila equipada actualmente.
#
# Integer — serial/ID, no graphic/type, capa, cantidad ni Boolean. 0: no hay objeto actual.
# Conserva los 32 bits; comprueba <> 0, no = TRUE o > 0. Un resultado guardado no se actualiza
# solo. Busca el item no destruido en la capa Backpack de Player. Player o mochila
# ausente/destruido da 0. Identifica el contenedor, no su contenido; no crea bolsas.

SUB Main()
    # before/after se leen con 250 ms de diferencia. WAIT pertenece al ejemplo. La igualdad final
    # puede ocultar cambios intermedios.

    VAR before = UO.Backpack()
    WAIT(250)
    VAR after = UO.Backpack()
    IF before <> after THEN
        UO.Print('ID changed: ' + HEX(after))
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- before/after se leen con 250 ms de diferencia. WAIT pertenece al ejemplo. La igualdad final puede ocultar cambios intermedios.

### Función IsOwnSerial completa

```vb
# Función IsOwnSerial completa
#
# Devuelve el ID de la mochila equipada actualmente.
#
# Integer — serial/ID, no graphic/type, capa, cantidad ni Boolean. 0: no hay objeto actual.
# Conserva los 32 bits; comprueba <> 0, no = TRUE o > 0. Un resultado guardado no se actualiza
# solo. Busca el item no destruido en la capa Backpack de Player. Player o mochila
# ausente/destruido da 0. Identifica el contenedor, no su contenido; no crea bolsas.

SUB Main()
    # candidate es el ID LastTarget guardado. IsOwnSerial(candidate) recibe un serial y devuelve
    # Integer Boolean: 1=TRUE para el ID propio actual no nulo; de lo contrario 0=FALSE. Definición
    # completa, sin cambiar target.

    VAR candidate = UO.LastTarget()
    IF IsOwnSerial(candidate) = TRUE THEN
        UO.Print('Own object selected')
    ELSE
        UO.Print('Different object or no own object')
    END IF
END SUB

SUB IsOwnSerial(candidate)
    VAR current = UO.Backpack()
    RETURN current <> 0 AND current = candidate
END SUB
```

**Explicación de los parámetros y la ejecución:**

- candidate es el ID LastTarget guardado. IsOwnSerial(candidate) recibe un serial y devuelve Integer Boolean: 1=TRUE para el ID propio actual no nulo; de lo contrario 0=FALSE. Definición completa, sin cambiar target.
