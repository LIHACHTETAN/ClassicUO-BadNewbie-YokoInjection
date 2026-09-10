# UO.PredictedDirection

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee el valor previsto de la dirección tras los pasos del jugador ya en cola.

## Sintaxis exacta

```text
UO.PredictedDirection() -> Integer
```

## Parámetros

Sin parámetros.

## Devuelve

Integer dirección 0..7 sin bit de carrera. 0 indica norte o jugador ausente.

## Comportamiento

- Solo la función UO sin argumentos mostrada en Sintaxis. Sin target, serial, type, destino, distancia ni timeout. Número, no Boolean, ID ni registro tile: 1 no significa llegada.
- GetEndPosition lee X/Y/Z/dirección del último Mobile.Step ya en cola. Si está vacía, lee posición/dirección actual. Lectura O(1) sin extraer pasos, mover, enviar paquetes, calcular rutas ni esperar la llegada.
- Direcciones del mundo: 0 norte, 1 nordeste, 2 este, 3 sudeste, 4 sur, 5 sudoeste, 6 oeste, 7 noroeste. Pantalla isométrica. Direction.Mask quita el indicador de carrera; no devuelve velocidad.
- Predicción local, no llegada confirmada. Pasos nuevos/completados/rechazados, vaciado de cola o teletransporte pueden cambiarla. Lecturas separadas no atómicas; X igual no demuestra Y/Z ni aceptación del servidor.
- Invoke lee en el hilo del juego; un hilo de trabajo espera el procesamiento del gestor. Cancelar el script interrumpe esa espera. No añade demoras ni consultas de red.
- Las IApiBridge externas sin IPredictedMovementBridge conservan la posición/dirección actual como alternativa. Classic UO implementa la interfaz que consulta la cola.

### Funciones internas: de la llamada al resultado

Pasos nativos reales. PredictionEquals es una función BASIC de usuario definida completamente, no una orden interna ni un procedimiento de movimiento.

#### 1. ExecuteStealthCompatibility

La función nativa llama a ReadPredictedCoordinate, que elige la propiedad IPredictedMovementBridge. No llama a NewMoveXY ni inicia búsqueda de rutas.

Solo la función UO sin argumentos mostrada en Sintaxis. Sin target, serial, type, destino, distancia ni timeout. Número, no Boolean, ID ni registro tile: 1 no significa llegada.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `ExecuteStealthCompatibility`.

#### 2. ReadPredictedCoordinate

La función nativa llama a ReadPredictedCoordinate, que elige la propiedad IPredictedMovementBridge. No llama a NewMoveXY ni inicia búsqueda de rutas.

Las IApiBridge externas sin IPredictedMovementBridge conservan la posición/dirección actual como alternativa. Classic UO implementa la interfaz que consulta la cola.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `ReadPredictedCoordinate`.

#### 3. Invoke

Invoke lee en el hilo del juego; un hilo de trabajo espera el procesamiento del gestor. Cancelar el script interrumpe esa espera. No añade demoras ni consultas de red.

Integer dirección 0..7 sin bit de carrera. 0 indica norte o jugador ausente.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 4. ReadPredictedPosition

ReadPredictedPosition devuelve 0 si Player falta/está destruido; si existe llama a GetEndPosition y elige un componente.

GetEndPosition lee X/Y/Z/dirección del último Mobile.Step ya en cola. Si está vacía, lee posición/dirección actual. Lectura O(1) sin extraer pasos, mover, enviar paquetes, calcular rutas ni esperar la llegada.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `ReadPredictedPosition`.

#### 5. GetEndPosition

GetEndPosition lee X/Y/Z/dirección del último Mobile.Step ya en cola. Si está vacía, lee posición/dirección actual. Lectura O(1) sin extraer pasos, mover, enviar paquetes, calcular rutas ni esperar la llegada.

Direcciones del mundo: 0 norte, 1 nordeste, 2 este, 3 sudeste, 4 sur, 5 sudoeste, 6 oeste, 7 noroeste. Pantalla isométrica. Direction.Mask quita el indicador de carrera; no devuelve velocidad.

Código del proyecto: `src/ClassicUO.Client/Game/GameObjects/Mobile.cs`; función `GetEndPosition`.

#### 6. InjectionValue

Integer dirección 0..7 sin bit de carrera. 0 indica norte o jugador ausente.

Predicción local, no llegada confirmada. Pasos nuevos/completados/rechazados, vaciado de cola o teletransporte pueden cambiarla. Lecturas separadas no atómicas; X igual no demuestra Y/Z ni aceptación del servidor.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionValue.cs`; función `InjectionValue`.

PredictionEquals(expected) recibe una coordenada/altura/dirección numérica, rechaza jugador ausente y compara un componente previsto. Devuelve Integer Boolean 1=TRUE o 0=FALSE. No espera ni garantiza la llegada.


## Ejemplos

### Leer un componente

```vb
# Leer un componente
#
# Lee el valor previsto de la dirección tras los pasos del jugador ya en cola.
#
# Integer dirección 0..7 sin bit de carrera. 0 indica norte o jugador ausente.

SUB Main()
    # predicted guarda una llamada sin argumentos; CStr formatea el número para el diario.

    VAR predicted = UO.PredictedDirection()
    UO.Print('Predicted: ' + CStr(predicted))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- predicted guarda una llamada sin argumentos; CStr formatea el número para el diario.

### Observar un cambio

```vb
# Observar un cambio
#
# Lee el valor previsto de la dirección tras los pasos del jugador ya en cola.
#
# Integer dirección 0..7 sin bit de carrera. 0 indica norte o jugador ausente.

SUB Main()
    # WAIT(100) pausa este ejemplo 100 ms. before/after pueden coincidir pese a movimientos
    # intermedios; estas lecturas no inician movimiento.

    VAR before = UO.PredictedDirection()
    WAIT(100)
    VAR after = UO.PredictedDirection()
    IF before <> after THEN
        UO.Print('Prediction changed: ' + CStr(before) + ' -> ' + CStr(after))
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- WAIT(100) pausa este ejemplo 100 ms. before/after pueden coincidir pese a movimientos intermedios; estas lecturas no inician movimiento.

### Función de comparación completa

```vb
# Función de comparación completa
#
# Lee el valor previsto de la dirección tras los pasos del jugador ya en cola.
#
# Integer dirección 0..7 sin bit de carrera. 0 indica norte o jugador ausente.

SUB Main()
    # expected es una coordenada/altura/dirección de ejemplo, no un argumento nativo.
    # PredictionEquals comprueba UO.Self(), lee una vez y devuelve 1=TRUE si coincide; si no,
    # 0=FALSE. Código completo debajo de Main. Un componente igual no equivale a llegar.

    IF PredictionEquals(4) = TRUE THEN
        UO.Print('Queued endpoint matches this component')
    ELSE
        UO.Print('Different component or no player')
    END IF
END SUB

SUB PredictionEquals(expected)
    IF UO.Self() = 0 THEN
        RETURN FALSE
    END IF
    VAR predicted = UO.PredictedDirection()
    RETURN predicted = expected
END SUB
```

**Explicación de los parámetros y la ejecución:**

- expected es una coordenada/altura/dirección de ejemplo, no un argumento nativo. PredictionEquals comprueba UO.Self(), lee una vez y devuelve 1=TRUE si coincide; si no, 0=FALSE. Código completo debajo de Main. Un componente igual no equivale a llegar.
