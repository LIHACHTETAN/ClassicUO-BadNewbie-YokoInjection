# UO.LastTarget

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee el serial del último objetivo de objeto guardado.

## Sintaxis exacta

```text
UO.LastTarget() -> Integer
```

## Parámetros

Sin parámetros.

## Devuelve

Integer — serial/ID, no type ni Boolean. 0: sin objetivo de objeto; terreno/estáticos también tienen serial 0 aunque guarden coordenadas. Conserva los 32 bits. Comprobar <> 0, no > 0 ni = TRUE.

## Comportamiento

- Sin parámetros, cursor, selección, ataque ni paquetes. LastTarget difiere de LastAttack y LastStatus. Seleccionar self normalmente no lo sustituye; ClientMarkChar puede cambiarlo explícitamente.
- SetEntity guarda Entity.X/Y conocidos, quizás coordenadas internas de contenedor. SetLand/SetStatic guardan casillas del mundo. Movimiento/eliminación posterior no los cambia. GetX/GetY(serial) dan la posición actual.
- Clear y World.Clear reinician incluso conservando scripts. Un serial desconocido asignado explícitamente recibe X/Y=0, nunca las coordenadas anteriores. No garantiza existencia en el servidor.
- Lecturas separadas no son atómicas. LastTile conserva X/Y de protocolo 65535 para objetos; para terreno/estáticos LastTile(1)/(2) leen X/Y. lasttarget sin paréntesis es dinámico salvo que una variable lo oculte.
- World.Clear llama a ClearWorldState: borra cursor/callback activo, objetivo y paquete de repetición. Reset normal conserva el historial. TargetLast nativo solo envía un paquete guardado con cursor servidor activo; sin historial o con callback local mantiene el cursor sin enviar nada. El callback cliente activo recibe null una vez como cancelación: ClientTargetResponsePresent pasa a 1 con respuesta vacía. Una selección completada no recibe otro resultado.

### Funciones internas: de la llamada al resultado

Estas son las etapas internas reales de C#. ReadTargetValue es una función auxiliar completamente definida en el ejemplo, no un comando integrado oculto.

#### 1. SetEntity

SetEntity guarda serial y X/Y mediante World.Get. Entity ausente/destruida produce X/Y=0; mantiene los centinelas del protocolo.

SetEntity guarda Entity.X/Y conocidos, quizás coordenadas internas de contenedor. SetLand/SetStatic guardan casillas del mundo. Movimiento/eliminación posterior no los cambia. GetX/GetY(serial) dan la posición actual.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; función `SetEntity`.

#### 2. SetLand

SetLand/SetStatic guardan X/Y/Z con serial 0. SavedX/SavedY se separan de los campos transmitidos.

Integer — serial/ID, no type ni Boolean. 0: sin objetivo de objeto; terreno/estáticos también tienen serial 0 aunque guarden coordenadas. Conserva los 32 bits. Comprobar <> 0, no > 0 ni = TRUE.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; función `SetLand`.

#### 3. SetStatic

SetLand/SetStatic guardan X/Y/Z con serial 0. SavedX/SavedY se separan de los campos transmitidos.

Integer — serial/ID, no type ni Boolean. 0: sin objetivo de objeto; terreno/estáticos también tienen serial 0 aunque guarden coordenadas. Conserva los 32 bits. Comprobar <> 0, no > 0 ni = TRUE.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; función `SetStatic`.

#### 4. ExecuteStealthCompatibility

LastTargetX/LastTargetY leen ITargetSnapshotBridge; un bridge externo antiguo mantiene GetX/GetY. Invoke lee en el hilo del juego con cancelación.

Integer — serial/ID, no type ni Boolean. 0: sin objetivo de objeto; terreno/estáticos también tienen serial 0 aunque guarden coordenadas. Conserva los 32 bits. Comprobar <> 0, no > 0 ni = TRUE.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `ExecuteStealthCompatibility`.

#### 5. Invoke

LastTargetX/LastTargetY leen ITargetSnapshotBridge; un bridge externo antiguo mantiene GetX/GetY. Invoke lee en el hilo del juego con cancelación.

Sin parámetros, cursor, selección, ataque ni paquetes. LastTarget difiere de LastAttack y LastStatus. Seleccionar self normalmente no lo sustituye; ClientMarkChar puede cambiarlo explícitamente.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 6. Clear

Clear borra serial y coordenadas guardadas; World.Clear lo llama al limpiar.

Clear y World.Clear reinician incluso conservando scripts. Un serial desconocido asignado explícitamente recibe X/Y=0, nunca las coordenadas anteriores. No garantiza existencia en el servidor.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; función `Clear`.

#### 7. ClearWorldState

World.Clear llama a ClearWorldState: borra cursor/callback activo, objetivo y paquete de repetición. Reset normal conserva el historial. TargetLast nativo solo envía un paquete guardado con cursor servidor activo; sin historial o con callback local mantiene el cursor sin enviar nada. El callback cliente activo recibe null una vez como cancelación: ClientTargetResponsePresent pasa a 1 con respuesta vacía. Una selección completada no recibe otro resultado.

World.Clear llama a ClearWorldState: borra cursor/callback activo, objetivo y paquete de repetición. Reset normal conserva el historial. TargetLast nativo solo envía un paquete guardado con cursor servidor activo; sin historial o con callback local mantiene el cursor sin enviar nada. El callback cliente activo recibe null una vez como cancelación: ClientTargetResponsePresent pasa a 1 con respuesta vacía. Una selección completada no recibe otro resultado.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; función `ClearWorldState`.

#### 8. TargetLast

World.Clear llama a ClearWorldState: borra cursor/callback activo, objetivo y paquete de repetición. Reset normal conserva el historial. TargetLast nativo solo envía un paquete guardado con cursor servidor activo; sin historial o con callback local mantiene el cursor sin enviar nada. El callback cliente activo recibe null una vez como cancelación: ClientTargetResponsePresent pasa a 1 con respuesta vacía. Una selección completada no recibe otro resultado.

World.Clear llama a ClearWorldState: borra cursor/callback activo, objetivo y paquete de repetición. Reset normal conserva el historial. TargetLast nativo solo envía un paquete guardado con cursor servidor activo; sin historial o con callback local mantiene el cursor sin enviar nada. El callback cliente activo recibe null una vez como cancelación: ClientTargetResponsePresent pasa a 1 con respuesta vacía. Una selección completada no recibe otro resultado.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/TargetManager.cs`; función `TargetLast`.

Lecturas separadas no son atómicas. LastTile conserva X/Y de protocolo 65535 para objetos; para terreno/estáticos LastTile(1)/(2) leen X/Y. lasttarget sin paréntesis es dinámico salvo que una variable lo oculte.


## Ejemplos

### Leer el valor guardado

```vb
# Leer el valor guardado
#
# Lee el serial del último objetivo de objeto guardado.
#
# Integer — serial/ID, no type ni Boolean. 0: sin objetivo de objeto; terreno/estáticos también
# tienen serial 0 aunque guarden coordenadas. Conserva los 32 bits. Comprobar <> 0, no > 0 ni =
# TRUE.

SUB Main()
    # value contiene el resultado; HEX muestra el ID, CStr la coordenada. No selecciona nada.

    VAR value = UO.LastTarget()
    UO.Print('Saved value: ' + HEX(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- value contiene el resultado; HEX muestra el ID, CStr la coordenada. No selecciona nada.

### Comparar posición guardada y actual

```vb
# Comparar posición guardada y actual
#
# Lee el serial del último objetivo de objeto guardado.
#
# Integer — serial/ID, no type ni Boolean. 0: sin objetivo de objeto; terreno/estáticos también
# tienen serial 0 aunque guarden coordenadas. Conserva los 32 bits. Comprobar <> 0, no > 0 ni =
# TRUE.

SUB Main()
    # id es el serial guardado. Exists precede a GetX/GetY; las posiciones pueden diferir. Un ID
    # nulo no prueba que se seleccionó un punto.

    VAR id = UO.LastTarget()
    VAR x = UO.LastTargetX()
    VAR y = UO.LastTargetY()
    UO.Print('Saved XY: ' + CStr(x) + ',' + CStr(y))
    IF id <> 0 AND UO.Exists(id) THEN
        UO.Print('Live XY: ' + CStr(UO.GetX(id)) + ',' + CStr(UO.GetY(id)))
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- id es el serial guardado. Exists precede a GetX/GetY; las posiciones pueden diferir. Un ID nulo no prueba que se seleccionó un punto.

### Función completa ReadTargetValue

```vb
# Función completa ReadTargetValue
#
# Lee el serial del último objetivo de objeto guardado.
#
# Integer — serial/ID, no type ni Boolean. 0: sin objetivo de objeto; terreno/estáticos también
# tienen serial 0 aunque guarden coordenadas. Conserva los 32 bits. Comprobar <> 0, no > 0 ni =
# TRUE.

SUB Main()
    # minimum/maximum configuran el filtro auxiliar, no la API. -1 es su propia señal fuera de
    # rango. La variante ID conserva todo serial no nulo y el bit superior.

    VAR value = ReadTargetValue()
    UO.Print('Checked value: ' + CStr(value))
END SUB

SUB ReadTargetValue()
    VAR value = UO.LastTarget()
    IF value = 0 THEN
        RETURN -1
    END IF
    RETURN value
END SUB
```

**Explicación de los parámetros y la ejecución:**

- minimum/maximum configuran el filtro auxiliar, no la API. -1 es su propia señal fuera de rango. La variante ID conserva todo serial no nulo y el bit superior.
