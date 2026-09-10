# UO.FireResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee el campo de resistencia del jugador actual: fuego.

## Sintaxis exacta

```text
UO.FireResist() -> Integer
```

## Parámetros

Sin parámetros.

## Devuelve

Integer — valor de status con signo, -32768..32767 en el modelo. Conserva los negativos. 0 puede ser real, desconocido o indicar Player ausente/destruido; GetResist también da 0 con selector desconocido. No es Boolean, ID, habilidad ni límite. 1 significa un punto, no éxito.

## Comportamiento

- No admite argumentos. Usar las firmas mostradas.
- Lee Player.FireResistance en el hilo del juego si Player existe y no está destruido; de lo contrario 0. Sin búsqueda de equipo, cálculo de bonos, petición status ni espera. Un fantasma presente no es un Player destruido.
- Los campos elementales llegan mediante CharacterStatus (0x11), type >= 4. La consulta no comprueba la era. Un status compacto/antiguo sin estos campos conserva su caché anterior; Player nuevo empieza en 0. Resistencia al veneno no es Poisoned; ningún campo es la habilidad Resisting Spells.
- CharacterStatus valida el cuerpo fijo antes de modificar datos y convierte las palabras de resistencia en Int16 con signo. Un cuerpo truncado conserva los datos. La cola opcional type 6 mantiene su comportamiento; estos getters no leen sus resistencias máximas.
- Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.
- RegisterCharacterGetterAliases añade funciones sin argumentos e intrínsecos ausentes. Las ramas existentes leen el mismo campo. Nombres sin distinción de mayúsculas; intrínsecos sin paréntesis se releen salvo variables que los oculten.

### Funciones internas: de la llamada al resultado

Etapas nativas de lectura local. ResistanceAtLeast debajo es una función BASIC de usuario completa, no una API oculta ni una orden para equipar protección.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases añade funciones sin argumentos e intrínsecos ausentes. Las ramas existentes leen el mismo campo. Nombres sin distinción de mayúsculas; intrínsecos sin paréntesis se releen salvo variables que los oculten.

`FireResist ResistFire GetFireResist GetResistFire`.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `RegisterCharacterGetterAliases`.

#### 2. Invoke

Lee Player.FireResistance en el hilo del juego si Player existe y no está destruido; de lo contrario 0. Sin búsqueda de equipo, cálculo de bonos, petición status ni espera. Un fantasma presente no es un Player destruido.

Invoke lee en el hilo del juego; la espera respeta la cancelación del script. Sin paquete, solicitud de status, target, modificación ni retraso incorporado.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 3. CharacterStatus

CharacterStatus valida el cuerpo fijo antes de modificar datos y convierte las palabras de resistencia en Int16 con signo. Un cuerpo truncado conserva los datos. La cola opcional type 6 mantiene su comportamiento; estos getters no leen sus resistencias máximas.

Los campos elementales llegan mediante CharacterStatus (0x11), type >= 4. La consulta no comprueba la era. Un status compacto/antiguo sin estos campos conserva su caché anterior; Player nuevo empieza en 0. Resistencia al veneno no es Poisoned; ningún campo es la habilidad Resisting Spells.

Código del proyecto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; función `CharacterStatus`.

#### 4. Clear

World.Clear elimina Player. Las consultas dan 0 hasta que vuelvan el jugador y sus datos. Un valor guardado no prueba el requisito tras reconectar.

Integer — valor de status con signo, -32768..32767 en el modelo. Conserva los negativos. 0 puede ser real, desconocido o indicar Player ausente/destruido; GetResist también da 0 con selector desconocido. No es Boolean, ID, habilidad ni límite. 1 significa un punto, no éxito.

Código del proyecto: `src/ClassicUO.Client/Game/World.cs`; función `Clear`.

Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.


## Ejemplos

### Mostrar el valor en caché

```vb
# Mostrar el valor en caché
#
# Lee el campo de resistencia del jugador actual: fuego.
#
# Integer — valor de status con signo, -32768..32767 en el modelo. Conserva los negativos. 0
# puede ser real, desconocido o indicar Player ausente/destruido; GetResist también da 0 con
# selector desconocido. No es Boolean, ID, habilidad ni límite. 1 significa un punto, no éxito.

SUB Main()
    # value conserva una lectura sin argumentos del jugador; CStr la formatea para el diario.

    VAR value = UO.FireResist()
    UO.Print('FireResistance: ' + CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value conserva una lectura sin argumentos del jugador; CStr la formatea para el diario.

### Comparar dos observaciones

```vb
# Comparar dos observaciones
#
# Lee el campo de resistencia del jugador actual: fuego.
#
# Integer — valor de status con signo, -32768..32767 en el modelo. Conserva los negativos. 0
# puede ser real, desconocido o indicar Player ausente/destruido; GetResist también da 0 con
# selector desconocido. No es Boolean, ID, habilidad ni límite. 1 significa un punto, no éxito.

SUB Main()
    # WAIT(500) separa before y after por 500 ms; difference puede ser negativa. Pueden perderse
    # actualizaciones intermedias. La espera pertenece al ejemplo.

    VAR before = UO.FireResist()
    WAIT(500)
    VAR after = UO.FireResist()
    VAR difference = after - before
    UO.Print('Resistance change: ' + CStr(difference))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- WAIT(500) separa before y after por 500 ms; difference puede ser negativa. Pueden perderse actualizaciones intermedias. La espera pertenece al ejemplo.

### Función completa de resistencia mínima

```vb
# Función completa de resistencia mínima
#
# Lee el campo de resistencia del jugador actual: fuego.
#
# Integer — valor de status con signo, -32768..32767 en el modelo. Conserva los negativos. 0
# puede ser real, desconocido o indicar Player ausente/destruido; GetResist también da 0 con
# selector desconocido. No es Boolean, ID, habilidad ni límite. 1 significa un punto, no éxito.

SUB Main()
    # minimum=50 es un requisito de ejemplo, no un límite. ResistanceAtLeast rechaza Player ausente,
    # lee una vez y devuelve Integer Boolean 1=TRUE o 0=FALSE según value >= minimum. La resistencia
    # no es Boolean. Definición completa debajo.

    IF ResistanceAtLeast(50) = TRUE THEN
        UO.Print('Local resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.FireResist()
    RETURN value >= minimum
END SUB
```

**Explicación de los parámetros y la ejecución:**

- minimum=50 es un requisito de ejemplo, no un límite. ResistanceAtLeast rechaza Player ausente, lee una vez y devuelve Integer Boolean 1=TRUE o 0=FALSE según value >= minimum. La resistencia no es Boolean. Definición completa debajo.
