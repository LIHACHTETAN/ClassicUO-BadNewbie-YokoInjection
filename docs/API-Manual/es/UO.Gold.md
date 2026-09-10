# UO.Gold

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee la cantidad de oro indicada en el status del jugador actual.

## Sintaxis exacta

```text
UO.Gold() -> Any
```

## Parámetros

Sin parámetros.

## Devuelve

Integer/Decimal — cantidad no negativa 0..4294967295. Hasta 2147483647 es Integer; por encima es Decimal (Double), que representa exactamente todos los UInt32. 0 también puede indicar Player ausente/destruido o cantidad desconocida. No es Boolean, ID, número de pilas ni búsqueda en mochila/banco.

## Comportamiento

- Sin argumentos. Lee Player.Gold almacenado por CharacterStatus (0x11). El servidor decide qué oro incluye. No recorre bolsas ni consulta la cuenta bancaria. Player ausente/destruido da 0; un fantasma presente puede conservar la cantidad.
- ReadGoldValue lee bridge.Gold una vez. El bridge C# mantiene Int32 y transporta los bits UInt32. La conversión unchecked recupera la cantidad sin signo: pequeña como Integer, grande como Decimal. El bit alto ya no produce saldo negativo. Conversión local sin paquetes.
- Conservar el resultado numérico al comparar grandes cantidades. CInt/CLng convierten a Integer de 32 bits. Escribir un literal BASIC grande con punto, por ejemplo 3000000000.0. El saldo puede cambiar antes de comprar; CanAfford es una comprobación local, no permiso del servidor.
- Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.

### Funciones internas: de la llamada al resultado

Etapas nativas para leer el contador status y ampliar su rango sin signo. CanAfford es la función BASIC de usuario completa abajo, no una orden oculta de compra.

#### 1. RegisterCharacterGetterAliases

RegisterCharacterGetterAliases añade Gold/GetGold e intrínsecos ausentes. La rama UO.Gold y su intrínseco usan el mismo ReadGoldValue. Los nombres intrínsecos se releen salvo que una variable los oculte.

Integer/Decimal — cantidad no negativa 0..4294967295. Hasta 2147483647 es Integer; por encima es Decimal (Double), que representa exactamente todos los UInt32. 0 también puede indicar Player ausente/destruido o cantidad desconocida. No es Boolean, ID, número de pilas ni búsqueda en mochila/banco.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `RegisterCharacterGetterAliases`.

#### 2. ReadGoldValue

ReadGoldValue lee bridge.Gold una vez. El bridge C# mantiene Int32 y transporta los bits UInt32. La conversión unchecked recupera la cantidad sin signo: pequeña como Integer, grande como Decimal. El bit alto ya no produce saldo negativo. Conversión local sin paquetes.

Conservar el resultado numérico al comparar grandes cantidades. CInt/CLng convierten a Integer de 32 bits. Escribir un literal BASIC grande con punto, por ejemplo 3000000000.0. El saldo puede cambiar antes de comprar; CanAfford es una comprobación local, no permiso del servidor.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `ReadGoldValue`.

#### 3. Invoke

Sin argumentos. Lee Player.Gold almacenado por CharacterStatus (0x11). El servidor decide qué oro incluye. No recorre bolsas ni consulta la cuenta bancaria. Player ausente/destruido da 0; un fantasma presente puede conservar la cantidad.

Invoke lee en el hilo del juego; la espera respeta la cancelación del script. Sin paquete, solicitud de status, target, modificación ni retraso incorporado.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 4. CharacterStatus

Sin argumentos. Lee Player.Gold almacenado por CharacterStatus (0x11). El servidor decide qué oro incluye. No recorre bolsas ni consulta la cuenta bancaria. Player ausente/destruido da 0; un fantasma presente puede conservar la cantidad.

Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.

Código del proyecto: `src/ClassicUO.Client/Network/PacketHandlers.cs`; función `CharacterStatus`.

#### 5. Clear

World.Clear elimina Player. Las consultas dan 0 hasta que vuelvan el jugador y sus datos. Un valor guardado no prueba el requisito tras reconectar.

Integer/Decimal — cantidad no negativa 0..4294967295. Hasta 2147483647 es Integer; por encima es Decimal (Double), que representa exactamente todos los UInt32. 0 también puede indicar Player ausente/destruido o cantidad desconocida. No es Boolean, ID, número de pilas ni búsqueda en mochila/banco.

Código del proyecto: `src/ClassicUO.Client/Game/World.cs`; función `Clear`.

Cada llamada vuelve a leer datos locales. Las variables guardan instantáneas; llamadas separadas pueden ver distintas actualizaciones. Un valor no cero no prueba conexión; cero puede ser un valor o datos ausentes.


## Ejemplos

### Mostrar la cantidad recibida

```vb
# Mostrar la cantidad recibida
#
# Lee la cantidad de oro indicada en el status del jugador actual.
#
# Integer/Decimal — cantidad no negativa 0..4294967295. Hasta 2147483647 es Integer; por encima
# es Decimal (Double), que representa exactamente todos los UInt32. 0 también puede indicar
# Player ausente/destruido o cantidad desconocida. No es Boolean, ID, número de pilas ni
# búsqueda en mochila/banco.

SUB Main()
    # amount guarda una consulta; CStr la formatea para el diario. No busca, mueve ni gasta oro.

    VAR amount = UO.Gold()
    UO.Print('Status gold: ' + CStr(amount))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- amount guarda una consulta; CStr la formatea para el diario. No busca, mueve ni gasta oro.

### CanAfford completo con precio grande

```vb
# CanAfford completo con precio grande
#
# Lee la cantidad de oro indicada en el status del jugador actual.
#
# Integer/Decimal — cantidad no negativa 0..4294967295. Hasta 2147483647 es Integer; por encima
# es Decimal (Double), que representa exactamente todos los UInt32. 0 también puede indicar
# Player ausente/destruido o cantidad desconocida. No es Boolean, ID, número de pilas ni
# búsqueda en mochila/banco.

SUB Main()
    # price=3000000000.0 es un precio de ejemplo. CanAfford(price) rechaza precio negativo o Player
    # ausente, lee una vez y devuelve Integer Boolean 1=TRUE o 0=FALSE para amount >= price. La
    # cantidad no es Boolean. La función se define por completo abajo.

    VAR price = 3000000000.0
    IF CanAfford(price) = TRUE THEN
        UO.Print('Local balance is sufficient')
    ELSE
        UO.Print('Local check failed')
    END IF
END SUB

SUB CanAfford(price)
    IF price < 0 OR UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR amount = UO.Gold()
    RETURN amount >= price
END SUB
```

**Explicación de los parámetros y la ejecución:**

- price=3000000000.0 es un precio de ejemplo. CanAfford(price) rechaza precio negativo o Player ausente, lee una vez y devuelve Integer Boolean 1=TRUE o 0=FALSE para amount >= price. La cantidad no es Boolean. La función se define por completo abajo.

### Observar un cambio de saldo

```vb
# Observar un cambio de saldo
#
# Lee la cantidad de oro indicada en el status del jugador actual.
#
# Integer/Decimal — cantidad no negativa 0..4294967295. Hasta 2147483647 es Integer; por encima
# es Decimal (Double), que representa exactamente todos los UInt32. 0 también puede indicar
# Player ausente/destruido o cantidad desconocida. No es Boolean, ID, número de pilas ni
# búsqueda en mochila/banco.

SUB Main()
    # before/after están separados por WAIT(500) milisegundos. difference=after-before puede ser
    # negativo al bajar el saldo; no es el desbordamiento sin signo corregido. Pueden pasar
    # inadvertidos cambios intermedios o de personaje.

    VAR before = UO.Gold()
    WAIT(500)
    VAR after = UO.Gold()
    VAR difference = after - before
    UO.Print('Balance change: ' + CStr(difference))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- before/after están separados por WAIT(500) milisegundos. difference=after-before puede ser negativo al bajar el saldo; no es el desbordamiento sin signo corregido. Pueden pasar inadvertidos cambios intermedios o de personaje.
