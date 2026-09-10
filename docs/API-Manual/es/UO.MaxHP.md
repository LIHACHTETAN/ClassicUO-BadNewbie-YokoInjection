# UO.MaxHP

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee la salud máxima del modelo local.

## Sintaxis exacta

```text
UO.MaxHP() -> Integer
```

## Parámetros

Sin parámetros.

## Devuelve

Integer — valor del campo HitsMax, no un porcentaje ni un Boolean. Cero puede ser un valor real o datos ausentes. Nunca divida entre un máximo de cero. Los valores de otros mobile pueden ser desconocidos. HP/HitsMax pueden contener una escala relativa del servidor en lugar de puntos exactos. HP=0 no demuestra la muerte; utilice Dead/IsDead.

## Comportamiento

- No abre status ni solicita actualizaciones al servidor. A diferencia de la petición automática de HP ausentes de Stealth, este cliente solo lee datos existentes. No modifica atributos ni envía paquetes.
- Cada resultado es una lectura independiente. El mundo puede cambiar entre Exists y la siguiente llamada; varias consultas no forman una instantánea atómica.
- Para objetos, World.Get rechaza entradas ausentes o IsDestroyed y produce 0. HP/HitsMax leen Entity, incluidos objetos con esos campos; Mana/Stamina requieren Mobile. Sin argumento lee self. Un nombre sin argumentos no siempre tiene una forma con ID: compruebe las firmas.
- Las lecturas sin argumentos también dan 0 si Player está ausente o destruido, incluidos Mana/Stamina directos y sus máximos, no solo mediante World.Get. Un personaje muerto todavía presente puede conservar valores.

### Funciones internas: de la llamada al resultado

Estas son las etapas internas reales de C#. ReadValue es una función auxiliar completamente definida en el ejemplo, no un comando integrado oculto.

#### 1. RegisterCharacterGetterAliases

Al crear el runtime, RegisterCharacterGetterAliases registra nombres y formas. Sin argumento utiliza bridge.Self; con un argumento utiliza su serial. Se conservan los registros existentes.

Integer — valor del campo HitsMax, no un porcentaje ni un Boolean. Cero puede ser un valor real o datos ausentes. Nunca divida entre un máximo de cero. Los valores de otros mobile pueden ser desconocidos. HP/HitsMax pueden contener una escala relativa del servidor en lugar de puntos exactos. HP=0 no demuestra la muerte; utilice Dead/IsDead.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `RegisterCharacterGetterAliases`.

#### 2. Invoke

Invoke lee en el hilo del juego; un hilo de trabajo espera el procesamiento del gestor. Cancelar el script interrumpe esa espera. No añade demoras ni consultas de red.

Cada resultado es una lectura independiente. El mundo puede cambiar entre Exists y la siguiente llamada; varias consultas no forman una instantánea atómica.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 3. Get

Para objetos, World.Get rechaza entradas ausentes o IsDestroyed y produce 0. HP/HitsMax leen Entity, incluidos objetos con esos campos; Mana/Stamina requieren Mobile. Sin argumento lee self. Un nombre sin argumentos no siempre tiene una forma con ID: compruebe las firmas.

Integer — valor del campo HitsMax, no un porcentaje ni un Boolean. Cero puede ser un valor real o datos ausentes. Nunca divida entre un máximo de cero. Los valores de otros mobile pueden ser desconocidos. HP/HitsMax pueden contener una escala relativa del servidor en lugar de puntos exactos. HP=0 no demuestra la muerte; utilice Dead/IsDead.

Código del proyecto: `src/ClassicUO.Client/Game/World.cs`; función `Get`.

No abre status ni solicita actualizaciones al servidor. A diferencia de la petición automática de HP ausentes de Stealth, este cliente solo lee datos existentes. No modifica atributos ni envía paquetes.


## Ejemplos

### Mostrar el valor del personaje

```vb
# Mostrar el valor del personaje
#
# Lee la salud máxima del modelo local.
#
# Integer — valor del campo HitsMax, no un porcentaje ni un Boolean. Cero puede ser un valor
# real o datos ausentes. Nunca divida entre un máximo de cero. Los valores de otros mobile
# pueden ser desconocidos. HP/HitsMax pueden contener una escala relativa del servidor en lugar
# de puntos exactos. HP=0 no demuestra la muerte; utilice Dead/IsDead.

SUB Main()
    # La llamada sin argumentos lee self. value guarda un número; STR lo convierte solo para el
    # mensaje.

    VAR value = UO.MaxHP()
    UO.Print('MaxHP: ' + STR(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- La llamada sin argumentos lee self. value guarda un número; STR lo convierte solo para el mensaje.

### Usar el valor en una condición o cálculo

```vb
# Usar el valor en una condición o cálculo
#
# Lee la salud máxima del modelo local.
#
# Integer — valor del campo HitsMax, no un porcentaje ni un Boolean. Cero puede ser un valor
# real o datos ausentes. Nunca divida entre un máximo de cero. Los valores de otros mobile
# pueden ser desconocidos. HP/HitsMax pueden contener una escala relativa del servidor en lugar
# de puntos exactos. HP=0 no demuestra la muerte; utilice Dead/IsDead.

SUB Main()
    # El ejemplo aplica un umbral o cálculo para este campo. Los números son ajustes de ejemplo, no
    # límites del servidor. Antes de dividir, se comprueba que el máximo sea positivo.

    VAR value = UO.MaxHP()
    IF value > 0 THEN
        UO.Print('Known HP percent: ' + STR(UO.GetHP() * 100 / value))
    ELSE
        UO.Print('HP maximum unavailable')
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El ejemplo aplica un umbral o cálculo para este campo. Los números son ajustes de ejemplo, no límites del servidor. Antes de dividir, se comprueba que el máximo sea positivo.

### Función auxiliar ReadValue completa

```vb
# Función auxiliar ReadValue completa
#
# Lee la salud máxima del modelo local.
#
# Integer — valor del campo HitsMax, no un porcentaje ni un Boolean. Cero puede ser un valor
# real o datos ausentes. Nunca divida entre un máximo de cero. Los valores de otros mobile
# pueden ser desconocidos. HP/HitsMax pueden contener una escala relativa del servidor en lugar
# de puntos exactos. HP=0 no demuestra la muerte; utilice Dead/IsDead.

SUB Main()
    # Este nombre no tiene una forma con ID. ReadValue sin parámetros lee self; WAIT(1000) separa
    # dos llamadas. La comparación de instantáneas puede omitir cambios intermedios.

    VAR before = ReadValue()
    WAIT(1000)
    VAR after = ReadValue()
    UO.Print('Before: ' + CStr(before) + '; after: ' + CStr(after))
END SUB

SUB ReadValue()
    RETURN UO.MaxHP()
END SUB
```

**Explicación de los parámetros y la ejecución:**

- Este nombre no tiene una forma con ID. ReadValue sin parámetros lee self; WAIT(1000) separa dos llamadas. La comparación de instantáneas puede omitir cambios intermedios.
