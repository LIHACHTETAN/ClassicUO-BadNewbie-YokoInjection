# UO.GetFollowersMax

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee el contador de status del jugador actual: máximo de espacios de control.

## Sintaxis exacta

```text
UO.GetFollowersMax() -> Integer
```

## Parámetros

Sin parámetros.

## Devuelve

Integer — máximo de espacios de control, 0..255 en el modelo. 0 puede ser real, desconocido o Player ausente/destruido. Cantidad, no Boolean, ID ni type: 1 significa una unidad, no éxito. No enumera objetos ni devuelve un array.

## Comportamiento

- No admite argumentos. Usar las firmas mostradas.
- Lee Player.FollowersMax en el hilo del juego si Player existe y no está destruido; de lo contrario 0. Sin búsqueda de equipo, cálculo de bonos, petición status ni espera. Un fantasma presente no es un Player destruido.
- PetsMax/FollowersMax lee el total permitido por el servidor desde status type 3, no los espacios libres. La ocupación puede superar el límite. Espacio libre: maximum - current, cambiando negativos a 0. No libera, doma ni invoca nada.
- CharacterStatus valida el cuerpo fijo antes de actualizar. Weight viene del status propio extendido, espacios desde type 3, Luck desde type 4 y WeightMax del servidor desde type 5. Paquetes compactos/antiguos sin contador opcional conservan la caché. Player nuevo empieza en cero; la consulta no demuestra un status reciente.
- RegisterCharacterGetterAliases añade funciones sin argumentos e intrínsecos ausentes. Las ramas existentes leen el mismo campo. Nombres sin distinción de mayúsculas; intrínsecos sin paréntesis se releen salvo variables que los oculten.
- Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.

### Funciones internas: de la llamada al resultado

Etapas nativas de lectura en caché. CanCarry, LuckAtLeast o CanAddFollower es una función BASIC de usuario completa en el ejemplo, no una acción nativa oculta. No modifica inventario ni seguidores.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases añade funciones sin argumentos e intrínsecos ausentes. Las ramas existentes leen el mismo campo. Nombres sin distinción de mayúsculas; intrínsecos sin paréntesis se releen salvo variables que los oculten.

`PetsMax FollowersMax GetPetsMax GetFollowersMax`.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `RegisterCharacterGetterAliases`.

#### 2. Invoke

Lee Player.FollowersMax en el hilo del juego si Player existe y no está destruido; de lo contrario 0. Sin búsqueda de equipo, cálculo de bonos, petición status ni espera. Un fantasma presente no es un Player destruido.

Invoke lee en el hilo del juego; la espera respeta la cancelación del script. Sin paquete, solicitud de status, target, modificación ni retraso incorporado.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 3. CharacterStatus

CharacterStatus valida el cuerpo fijo antes de actualizar. Weight viene del status propio extendido, espacios desde type 3, Luck desde type 4 y WeightMax del servidor desde type 5. Paquetes compactos/antiguos sin contador opcional conservan la caché. Player nuevo empieza en cero; la consulta no demuestra un status reciente.

PetsMax/FollowersMax lee el total permitido por el servidor desde status type 3, no los espacios libres. La ocupación puede superar el límite. Espacio libre: maximum - current, cambiando negativos a 0. No libera, doma ni invoca nada.

Código del proyecto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; función `CharacterStatus`.

#### 4. Clear

World.Clear elimina Player. Las consultas dan 0 hasta que vuelvan el jugador y sus datos. Un valor guardado no prueba el requisito tras reconectar.

Integer — máximo de espacios de control, 0..255 en el modelo. 0 puede ser real, desconocido o Player ausente/destruido. Cantidad, no Boolean, ID ni type: 1 significa una unidad, no éxito. No enumera objetos ni devuelve un array.

Código del proyecto: `src/ClassicUO.Client/Game/World.cs`; función `Clear`.

Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.


## Ejemplos

### Mostrar el contador guardado

```vb
# Mostrar el contador guardado
#
# Lee el contador de status del jugador actual: máximo de espacios de control.
#
# Integer — máximo de espacios de control, 0..255 en el modelo. 0 puede ser real, desconocido o
# Player ausente/destruido. Cantidad, no Boolean, ID ni type: 1 significa una unidad, no éxito.
# No enumera objetos ni devuelve un array.

SUB Main()
    # value guarda una lectura sin argumentos del jugador; CStr la formatea para el diario sin
    # cambiar su significado.

    VAR value = UO.GetFollowersMax()
    UO.Print('FollowersMax: ' + CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value guarda una lectura sin argumentos del jugador; CStr la formatea para el diario sin cambiar su significado.

### Observar un cambio

```vb
# Observar un cambio
#
# Lee el contador de status del jugador actual: máximo de espacios de control.
#
# Integer — máximo de espacios de control, 0..255 en el modelo. 0 puede ser real, desconocido o
# Player ausente/destruido. Cantidad, no Boolean, ID ni type: 1 significa una unidad, no éxito.
# No enumera objetos ni devuelve un array.

SUB Main()
    # WAIT(500) separa before y after por 500 ms. difference puede ser positiva, cero o negativa;
    # pueden perderse actualizaciones o cambios de personaje intermedios. La espera pertenece al
    # ejemplo.

    VAR before = UO.GetFollowersMax()
    WAIT(500)
    VAR after = UO.GetFollowersMax()
    VAR difference = after - before
    UO.Print('Counter change: ' + CStr(difference))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- WAIT(500) separa before y after por 500 ms. difference puede ser positiva, cero o negativa; pueden perderse actualizaciones o cambios de personaje intermedios. La espera pertenece al ejemplo.

### Función de decisión completa

```vb
# Función de decisión completa
#
# Lee el contador de status del jugador actual: máximo de espacios de control.
#
# Integer — máximo de espacios de control, 0..255 en el modelo. 0 puede ser real, desconocido o
# Player ausente/destruido. Cantidad, no Boolean, ID ni type: 1 significa una unidad, no éxito.
# No enumera objetos ni devuelve un array.

SUB Main()
    # CanAddFollower(extraSlots) recibe espacios requeridos; 2 puede ser una criatura que ocupa dos
    # espacios. Rechaza entrada negativa, Player ausente o maximum <= 0, lee ocupados/límite y
    # devuelve Integer Boolean 1=TRUE o 0=FALSE para extraSlots <= maximum - current. Sin
    # desbordamiento de suma; superar límite da false incluso con cero. No verifica dueño, habilidad
    # de doma ni permiso del servidor. Puede haber actualizaciones entre lecturas.

    IF CanAddFollower(2) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB CanAddFollower(extraSlots)
    IF extraSlots < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR current = UO.PetsCurrent()
    VAR maximum = UO.GetFollowersMax()
    IF maximum <= 0 THEN
        RETURN FALSE
    END IF
    RETURN extraSlots <= maximum - current
END SUB
```

**Explicación de los parámetros y la ejecución:**

- CanAddFollower(extraSlots) recibe espacios requeridos; 2 puede ser una criatura que ocupa dos espacios. Rechaza entrada negativa, Player ausente o maximum <= 0, lee ocupados/límite y devuelve Integer Boolean 1=TRUE o 0=FALSE para extraSlots <= maximum - current. Sin desbordamiento de suma; superar límite da false incluso con cero. No verifica dueño, habilidad de doma ni permiso del servidor. Puede haber actualizaciones entre lecturas.
