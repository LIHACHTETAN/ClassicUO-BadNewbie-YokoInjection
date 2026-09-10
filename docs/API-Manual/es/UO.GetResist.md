# UO.GetResist

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee una resistencia del personaje propio mediante un número o nombre.

## Sintaxis exacta

```text
UO.GetResist(resistance:Any) -> Integer
```

## Parámetros

- `resistance` — resistance obligatorio: números 0=physical, 1=fire, 2=cold, 3=poison, 4=energy; nombres physical/phys/armor, fire, cold, poison, energy. Ignora mayúsculas y espacios exteriores. Sin serial, type, hue, cursor ni segundo argumento.

## Devuelve

Integer — valor de status con signo, -32768..32767 en el modelo. Conserva los negativos. 0 puede ser real, desconocido o indicar Player ausente/destruido; GetResist también da 0 con selector desconocido. No es Boolean, ID, habilidad ni límite. 1 significa un punto, no éxito.

## Comportamiento

- Primero distingue el tipo: "1" y "0" son nombres desconocidos y dan 0. Decimal no textual se trunca hacia cero: 1.9 -> fire, -0.9 -> physical. TRUE=1 elige fire, FALSE=0 physical; Array/Unit también pasan a 0. Usar un entero explícito o un nombre válido. No resuelve nombres AddObject.
- GetResistance selecciona un solo getter del bridge; números/nombres desconocidos dan Integer 0 sin lectura. No lee cinco campos atómicamente ni cambia resistencias.
- PhysicalResistance es el campo armadura/status del servidor: índice de armadura con reglas clásicas, resistencia física con reglas de resistencias. No convierte reglas ni calcula el porcentaje de reducción del daño. Armor y alias físicos leen el mismo campo.
- Los campos elementales llegan mediante CharacterStatus (0x11), type >= 4. La consulta no comprueba la era. Un status compacto/antiguo sin estos campos conserva su caché anterior; Player nuevo empieza en 0. Resistencia al veneno no es Poisoned; ningún campo es la habilidad Resisting Spells.
- CharacterStatus valida el cuerpo fijo antes de modificar datos y convierte las palabras de resistencia en Int16 con signo. Un cuerpo truncado conserva los datos. La cola opcional type 6 mantiene su comportamiento; estos getters no leen sus resistencias máximas.
- Invoke lee en el hilo del juego; la espera respeta la cancelación del script. Sin paquete, solicitud de status, target, modificación ni retraso incorporado.
- Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.

### Funciones internas: de la llamada al resultado

Etapas nativas de lectura local. ResistanceAtLeast debajo es una función BASIC de usuario completa, no una API oculta ni una orden para equipar protección.

#### 1. RegisterCharacterGetterAliases

Registra GetResist(resistance) y UO.GetResist(resistance) con un argumento enlazado a GetResistance. No hay intrínseco sin argumento para este selector.

resistance obligatorio: números 0=physical, 1=fire, 2=cold, 3=poison, 4=energy; nombres physical/phys/armor, fire, cold, poison, energy. Ignora mayúsculas y espacios exteriores. Sin serial, type, hue, cursor ni segundo argumento.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `RegisterCharacterGetterAliases`.

#### 2. GetResistance

Primero distingue el tipo: "1" y "0" son nombres desconocidos y dan 0. Decimal no textual se trunca hacia cero: 1.9 -> fire, -0.9 -> physical. TRUE=1 elige fire, FALSE=0 physical; Array/Unit también pasan a 0. Usar un entero explícito o un nombre válido. No resuelve nombres AddObject.

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`. GetResistance selecciona un solo getter del bridge; números/nombres desconocidos dan Integer 0 sin lectura. No lee cinco campos atómicamente ni cambia resistencias.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `GetResistance`.

#### 3. ToInt

ToInt recibe aquí solo un selector no textual. Integer se conserva, Decimal se trunca hacia cero, Array/Unit dan 0. El resultado es un índice, no una resistencia. GetResistance procesa los nombres textuales.

`0: PhysicalResistance; 1: FireResistance; 2: ColdResistance; 3: PoisonResistance; 4: EnergyResistance`.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/NumberConversions.cs`; función `ToInt`.

#### 4. Invoke

Invoke lee el campo Player elegido en la tabla anterior conservando el signo. Player ausente/destruido da 0. No pide status ni espera nuevos datos.

Invoke lee en el hilo del juego; la espera respeta la cancelación del script. Sin paquete, solicitud de status, target, modificación ni retraso incorporado.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 5. CharacterStatus

CharacterStatus valida el cuerpo fijo antes de modificar datos y convierte las palabras de resistencia en Int16 con signo. Un cuerpo truncado conserva los datos. La cola opcional type 6 mantiene su comportamiento; estos getters no leen sus resistencias máximas.

PhysicalResistance es el campo armadura/status del servidor: índice de armadura con reglas clásicas, resistencia física con reglas de resistencias. No convierte reglas ni calcula el porcentaje de reducción del daño. Armor y alias físicos leen el mismo campo. Los campos elementales llegan mediante CharacterStatus (0x11), type >= 4. La consulta no comprueba la era. Un status compacto/antiguo sin estos campos conserva su caché anterior; Player nuevo empieza en 0. Resistencia al veneno no es Poisoned; ningún campo es la habilidad Resisting Spells.

Código del proyecto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; función `CharacterStatus`.

#### 6. Clear

World.Clear elimina Player. Las consultas dan 0 hasta que vuelvan el jugador y sus datos. Un valor guardado no prueba el requisito tras reconectar.

Integer — valor de status con signo, -32768..32767 en el modelo. Conserva los negativos. 0 puede ser real, desconocido o indicar Player ausente/destruido; GetResist también da 0 con selector desconocido. No es Boolean, ID, habilidad ni límite. 1 significa un punto, no éxito.

Código del proyecto: `src/ClassicUO.Client/Game/World.cs`; función `Clear`.

Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.


## Ejemplos

### Elegir un nombre con mayúsculas mixtas

```vb
# Elegir un nombre con mayúsculas mixtas
#
# Lee una resistencia del personaje propio mediante un número o nombre.
#
# Integer — valor de status con signo, -32768..32767 en el modelo. Conserva los negativos. 0
# puede ser real, desconocido o indicar Player ausente/destruido; GetResist también da 0 con
# selector desconocido. No es Boolean, ID, habilidad ni límite. 1 significa un punto, no éxito.

SUB Main()
    # resistance=" FiRe " elige fuego ignorando mayúsculas y espacios exteriores. value conserva el
    # signo; no abre cursor.

    VAR value = UO.GetResist(' FiRe ')
    UO.Print('Fire resistance: ' + CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- resistance=" FiRe " elige fuego ignorando mayúsculas y espacios exteriores. value conserva el signo; no abre cursor.

### Comparar selectores numéricos y textuales

```vb
# Comparar selectores numéricos y textuales
#
# Lee una resistencia del personaje propio mediante un número o nombre.
#
# Integer — valor de status con signo, -32768..32767 en el modelo. Conserva los negativos. 0
# puede ser real, desconocido o indicar Player ausente/destruido; GetResist también da 0 con
# selector desconocido. No es Boolean, ID, habilidad ni límite. 1 significa un punto, no éxito.

SUB Main()
    # 2 elige frío, "poison" veneno. No son serials. Comparar dos instantáneas produce Boolean; la
    # resistencia al veneno no indica envenenamiento.

    VAR cold = UO.GetResist(2)
    VAR poison = UO.GetResist('poison')
    IF cold < poison THEN
        UO.Print('Cold resistance is lower')
    ELSE
        UO.Print('Cold resistance is equal or higher')
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- 2 elige frío, "poison" veneno. No son serials. Comparar dos instantáneas produce Boolean; la resistencia al veneno no indica envenenamiento.

### Función completa de resistencia mínima

```vb
# Función completa de resistencia mínima
#
# Lee una resistencia del personaje propio mediante un número o nombre.
#
# Integer — valor de status con signo, -32768..32767 en el modelo. Conserva los negativos. 0
# puede ser real, desconocido o indicar Player ausente/destruido; GetResist también da 0 con
# selector desconocido. No es Boolean, ID, habilidad ni límite. 1 significa un punto, no éxito.

SUB Main()
    # minimum=50 es un requisito de ejemplo, no un límite. ResistanceAtLeast rechaza Player ausente,
    # lee una vez y devuelve Integer Boolean 1=TRUE o 0=FALSE según value >= minimum. La resistencia
    # no es Boolean. Definición completa debajo.
    # selector pasa sin cambios a GetResist; el ejemplo usa "fire". La función comprueba Player,
    # pero no cualquier selector ni la actualidad del status. Usar un selector de la lista.

    IF ResistanceAtLeast('fire', 50) = TRUE THEN
        UO.Print('Local fire resistance requirement met')
    ELSE
        UO.Print('Requirement not met or no player')
    END IF
END SUB

SUB ResistanceAtLeast(selector, minimum)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR value = UO.GetResist(selector)
    RETURN value >= minimum
END SUB
```

**Explicación de los parámetros y la ejecución:**

- minimum=50 es un requisito de ejemplo, no un límite. ResistanceAtLeast rechaza Player ausente, lee una vez y devuelve Integer Boolean 1=TRUE o 0=FALSE según value >= minimum. La resistencia no es Boolean. Definición completa debajo.
- selector pasa sin cambios a GetResist; el ejemplo usa "fire". La función comprueba Player, pero no cualquier selector ni la actualidad del status. Usar un selector de la lista.
