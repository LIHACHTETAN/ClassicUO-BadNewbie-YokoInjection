# UO.Luck

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee el contador de status del jugador actual: puntos de suerte.

## Sintaxis exacta

```text
UO.Luck() -> Integer
```

## Parámetros

Sin parámetros.

## Devuelve

Integer — puntos de suerte, 0..65535 en el modelo. 0 puede ser real, desconocido o Player ausente/destruido. Cantidad, no Boolean, ID ni type: 1 significa una unidad, no éxito. No enumera objetos ni devuelve un array.

## Comportamiento

- No admite argumentos. Usar las firmas mostradas.
- Lee Player.Luck en el hilo del juego si Player existe y no está destruido; de lo contrario 0. Sin búsqueda de equipo, cálculo de bonos, petición status ni espera. Un fantasma presente no es un Player destruido.
- Luck lee puntos de suerte del servidor, UInt16, desde status type 4. No es porcentaje, número aleatorio ni garantía de botín. No calcula probabilidades ni añade bonos del equipo al leer.
- CharacterStatus valida el cuerpo fijo antes de actualizar. Weight viene del status propio extendido, espacios desde type 3, Luck desde type 4 y WeightMax del servidor desde type 5. Paquetes compactos/antiguos sin contador opcional conservan la caché. Player nuevo empieza en cero; la consulta no demuestra un status reciente.
- RegisterCharacterGetterAliases añade funciones sin argumentos e intrínsecos ausentes. Las ramas existentes leen el mismo campo. Nombres sin distinción de mayúsculas; intrínsecos sin paréntesis se releen salvo variables que los oculten.
- Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.

### Funciones internas: de la llamada al resultado

Etapas nativas de lectura en caché. CanCarry, LuckAtLeast o CanAddFollower es una función BASIC de usuario completa en el ejemplo, no una acción nativa oculta. No modifica inventario ni seguidores.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases añade funciones sin argumentos e intrínsecos ausentes. Las ramas existentes leen el mismo campo. Nombres sin distinción de mayúsculas; intrínsecos sin paréntesis se releen salvo variables que los oculten.

`Luck GetLuck`.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `RegisterCharacterGetterAliases`.

#### 2. Invoke

Lee Player.Luck en el hilo del juego si Player existe y no está destruido; de lo contrario 0. Sin búsqueda de equipo, cálculo de bonos, petición status ni espera. Un fantasma presente no es un Player destruido.

Invoke lee en el hilo del juego; la espera respeta la cancelación del script. Sin paquete, solicitud de status, target, modificación ni retraso incorporado.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 3. CharacterStatus

CharacterStatus valida el cuerpo fijo antes de actualizar. Weight viene del status propio extendido, espacios desde type 3, Luck desde type 4 y WeightMax del servidor desde type 5. Paquetes compactos/antiguos sin contador opcional conservan la caché. Player nuevo empieza en cero; la consulta no demuestra un status reciente.

Luck lee puntos de suerte del servidor, UInt16, desde status type 4. No es porcentaje, número aleatorio ni garantía de botín. No calcula probabilidades ni añade bonos del equipo al leer.

Código del proyecto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; función `CharacterStatus`.

#### 4. Clear

World.Clear elimina Player. Las consultas dan 0 hasta que vuelvan el jugador y sus datos. Un valor guardado no prueba el requisito tras reconectar.

Integer — puntos de suerte, 0..65535 en el modelo. 0 puede ser real, desconocido o Player ausente/destruido. Cantidad, no Boolean, ID ni type: 1 significa una unidad, no éxito. No enumera objetos ni devuelve un array.

Código del proyecto: `src/ClassicUO.Client/Game/World.cs`; función `Clear`.

Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.


## Ejemplos

### Mostrar el contador guardado

```vb
# Mostrar el contador guardado
#
# Lee el contador de status del jugador actual: puntos de suerte.
#
# Integer — puntos de suerte, 0..65535 en el modelo. 0 puede ser real, desconocido o Player
# ausente/destruido. Cantidad, no Boolean, ID ni type: 1 significa una unidad, no éxito. No
# enumera objetos ni devuelve un array.

SUB Main()
    # value guarda una lectura sin argumentos del jugador; CStr la formatea para el diario sin
    # cambiar su significado.

    VAR value = UO.Luck()
    UO.Print('Luck: ' + CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value guarda una lectura sin argumentos del jugador; CStr la formatea para el diario sin cambiar su significado.

### Observar un cambio

```vb
# Observar un cambio
#
# Lee el contador de status del jugador actual: puntos de suerte.
#
# Integer — puntos de suerte, 0..65535 en el modelo. 0 puede ser real, desconocido o Player
# ausente/destruido. Cantidad, no Boolean, ID ni type: 1 significa una unidad, no éxito. No
# enumera objetos ni devuelve un array.

SUB Main()
    # WAIT(500) separa before y after por 500 ms. difference puede ser positiva, cero o negativa;
    # pueden perderse actualizaciones o cambios de personaje intermedios. La espera pertenece al
    # ejemplo.

    VAR before = UO.Luck()
    WAIT(500)
    VAR after = UO.Luck()
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
# Lee el contador de status del jugador actual: puntos de suerte.
#
# Integer — puntos de suerte, 0..65535 en el modelo. 0 puede ser real, desconocido o Player
# ausente/destruido. Cantidad, no Boolean, ID ni type: 1 significa una unidad, no éxito. No
# enumera objetos ni devuelve un array.

SUB Main()
    # LuckAtLeast(minimum) recibe un requisito numérico; 1000 es ejemplo, no límite ni porcentaje.
    # Rechaza Player ausente, lee una vez y devuelve Integer Boolean 1=TRUE o 0=FALSE para value >=
    # minimum. La suerte no es Boolean. Compara la caché, no predice botín.

    IF LuckAtLeast(1000) = TRUE THEN
        UO.Print('Local check passed')
    ELSE
        UO.Print('Local check failed or data unavailable')
    END IF
END SUB

SUB LuckAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.Luck()
    RETURN value >= minimum
END SUB
```

**Explicación de los parámetros y la ejecución:**

- LuckAtLeast(minimum) recibe un requisito numérico; 1000 es ejemplo, no límite ni porcentaje. Rechaza Player ausente, lee una vez y devuelve Integer Boolean 1=TRUE o 0=FALSE para value >= minimum. La suerte no es Boolean. Compara la caché, no predice botín.
