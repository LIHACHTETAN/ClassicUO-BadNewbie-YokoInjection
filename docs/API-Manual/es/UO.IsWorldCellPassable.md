# UO.IsWorldCellPassable

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Comprueba un paso a una celda vecina y devuelve transitabilidad junto con altura.

## Sintaxis exacta

```text
UO.IsWorldCellPassable(CurrX:Any, CurrY:Any, CurrZ:Any, DestX:Any, DestY:Any, DestZ:Any, WorldNum:Any) -> Array
```

## Parámetros

- `CurrX` — Coordenada mundial X obligatoria de la celda inicial: entero 0..65535 dentro del mapa cargado, no una coordenada de gump.
- `CurrY` — Coordenada mundial Y obligatoria de la celda inicial: entero 0..65535 dentro del mapa cargado, no una coordenada de gump.
- `CurrZ` — Altura inicial obligatoria −128..127, no número de piso. Las alturas inválidas se rechazan, no se recortan.
- `DestX` — Coordenada mundial X obligatoria de la celda de destino: entero 0..65535 dentro del mapa cargado, no una coordenada de gump.
- `DestY` — Coordenada mundial Y obligatoria de la celda de destino: entero 0..65535 dentro del mapa cargado, no una coordenada de gump.
- `DestZ` — Z de respaldo de entrada obligatoria, normalmente CurrZ. No es var: la variable no cambia ni fija un piso. Lea la altura calculada de result[1]. Este bridge siempre proporciona su altura; el argumento conserva la forma Pascal.
- `WorldNum` — Número de mapa obligatorio: UO.WorldNum(). Solo comprueba el mapa actual con dimensiones conocidas; no carga otro mapa.

## Devuelve

Array de dos Integer: [0] — transitabilidad, 1 = TRUE, 0 = FALSE; [1] — Z calculada. Solo el primero es lógico; no compare el array con TRUE. Altura cero/negativa es válida; con [0]=0 no demuestra accesibilidad. Argumentos rechazados devuelven [0, CurrZ].

## Comportamiento

- Sin movimiento, apertura de puertas, objetivo ni paquetes. Lee geometría local existente; el servidor puede rechazar un paso posterior. Las consultas son instantáneas separadas.
- Vecina: diferencias X/Y de como máximo 1. Destino lejano, límites de mapa, personaje/mapa ausente o IsDestroyed se rechazan antes de colisiones. Para una ruta completa: GetPathArray o NewMoveXY.
- X/Y iguales y válidas dan [1, CurrZ] sin comprobar colisiones: no hace falta paso. No comprueba si se puede salir de esa celda. Estado del personaje y reglas Pathfinder afectan al paso vecino; sin geometría cargada puede rechazarse.

### Funciones internas: de la llamada al resultado

Estas son las etapas internas reales de C#. IsCellOpen es una función auxiliar completamente definida en el ejemplo, no un comando integrado oculto.

#### 1. ExecuteStealthCompatibility

Lee siete argumentos Integer. DestZ solo se usa si otro bridge no proporciona altura. Devuelve un array sin cambiar argumentos.

Array de dos Integer: [0] — transitabilidad, 1 = TRUE, 0 = FALSE; [1] — Z calculada. Solo el primero es lógico; no compare el array con TRUE. Altura cero/negativa es válida; con [0]=0 no demuestra accesibilidad. Argumentos rechazados devuelven [0, CurrZ].

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `ExecuteStealthCompatibility`.

#### 2. CheckWorldStep

Invoke valida personaje, mapa, dimensiones, coordenadas, altura y vecindad antes de restar; elige dirección. Exige X/Y de destino exactas tras CanWalkForQuery.

Array de dos Integer: [0] — transitabilidad, 1 = TRUE, 0 = FALSE; [1] — Z calculada. Solo el primero es lógico; no compare el array con TRUE. Altura cero/negativa es válida; con [0]=0 no demuestra accesibilidad. Argumentos rechazados devuelven [0, CurrZ].

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `CheckWorldStep`.

#### 3. CanWalkForQuery

Quita temporalmente el predicado de celdas prohibidas de otra ruta, lo restaura en finally y llama CanWalk sin iniciar ruta.

Sin movimiento, apertura de puertas, objetivo ni paquetes. Lee geometría local existente; el servidor puede rechazar un paso posterior. Las consultas son instantáneas separadas.

Código del proyecto: `src/ClassicUO.Client/Game/Pathfinder.cs`; función `CanWalkForQuery`.

#### 4. CanWalk

Comprueba paso principal y lados diagonales. Devuelve bool y modifica coordenadas ref solo para un paso aceptado.

Las funciones de colisión leen geometría cargada y estado del personaje. Una alternativa lateral diagonal no significa alcanzar la celda solicitada.

Código del proyecto: `src/ClassicUO.Client/Game/Pathfinder.cs`; función `CanWalk`.

#### 5. CalculateNewZ

Recibe X/Y de destino, Z inicial por ref y dirección. Elige superficie y espacio libre según el personaje; bool indica transitabilidad, z altura.

Las funciones de colisión leen geometría cargada y estado del personaje. Una alternativa lateral diagonal no significa alcanzar la celda solicitada.

Código del proyecto: `src/ClassicUO.Client/Game/Pathfinder.cs`; función `CalculateNewZ`.

#### 6. CalculateMinMaxZ

Recibe nueva celda, Z actual, dirección y modo. Usa CreateItemList para calcular ref minZ/maxZ con la geometría inicial.

Las funciones de colisión leen geometría cargada y estado del personaje. Una alternativa lateral diagonal no significa alcanzar la celda solicitada.

Código del proyecto: `src/ClassicUO.Client/Game/Pathfinder.cs`; función `CalculateMinMaxZ`.

#### 7. CreateItemList

Recibe lista, X/Y y modo. Recopila objetos cargados y reglas de colisión; bool indica geometría disponible. Map.GetTile usa load=false sin leer bloques nuevos.

Las funciones de colisión leen geometría cargada y estado del personaje. Una alternativa lateral diagonal no significa alcanzar la celda solicitada.

Código del proyecto: `src/ClassicUO.Client/Game/Pathfinder.cs`; función `CreateItemList`.

Sin movimiento, apertura de puertas, objetivo ni paquetes. Lee geometría local existente; el servidor puede rechazar un paso posterior. Las consultas son instantáneas separadas.


## Ejemplos

### Comprobar la celda al este

```vb
# Comprobar la celda al este
#
# Comprueba un paso a una celda vecina y devuelve transitabilidad junto con altura.
#
# Array de dos Integer: [0] — transitabilidad, 1 = TRUE, 0 = FALSE; [1] — Z calculada. Solo el
# primero es lógico; no compare el array con TRUE. Altura cero/negativa es válida; con [0]=0 no
# demuestra accesibilidad. Argumentos rechazados devuelven [0, CurrZ].

SUB Main()
    # x/y/z son el origen, x+1/y la vecina; sexto argumento Z de respaldo, último mapa actual.
    # Compruebe result[0] antes de result[1].

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR result = UO.IsWorldCellPassable(x,y,z,x+1,y,z,UO.WorldNum())
    IF result[0] = TRUE THEN
        UO.Print('Passable, Z=' + CStr(result[1]))
    ELSE
        UO.Print('Blocked')
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- x/y/z son el origen, x+1/y la vecina; sexto argumento Z de respaldo, último mapa actual. Compruebe result[0] antes de result[1].

### Leer Z sin cambiar el argumento

```vb
# Leer Z sin cambiar el argumento
#
# Comprueba un paso a una celda vecina y devuelve transitabilidad junto con altura.
#
# Array de dos Integer: [0] — transitabilidad, 1 = TRUE, 0 = FALSE; [1] — Z calculada. Solo el
# primero es lógico; no compare el array con TRUE. Altura cero/negativa es válida; con [0]=0 no
# demuestra accesibilidad. Argumentos rechazados devuelven [0, CurrZ].

SUB Main()
    # proposedZ sigue en 0. targetZ viene de result[1], no del argumento. No se deduce altura si se
    # rechaza.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR z = UO.GetZ()
    VAR proposedZ = 0
    VAR result = UO.IsWorldCellPassable(x,y,z,x,y+1,proposedZ,UO.WorldNum())
    IF result[0] = 1 THEN
        VAR targetZ = result[1]
        UO.Print('Input=' + CStr(proposedZ) + '; result=' + CStr(targetZ))
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- proposedZ sigue en 0. targetZ viene de result[1], no del argumento. No se deduce altura si se rechaza.

### Función IsCellOpen completa

```vb
# Función IsCellOpen completa
#
# Comprueba un paso a una celda vecina y devuelve transitabilidad junto con altura.
#
# Array de dos Integer: [0] — transitabilidad, 1 = TRUE, 0 = FALSE; [1] — Z calculada. Solo el
# primero es lógico; no compare el array con TRUE. Altura cero/negativa es válida; con [0]=0 no
# demuestra accesibilidad. Argumentos rechazados devuelven [0, CurrZ].

SUB Main()
    # La función completa tras Main recibe X/Y/Z iniciales, X/Y finales y mapa. Añade el sexto
    # argumento y devuelve solo Integer 1/0, no un array. IsCellOpen se puede comparar con TRUE. No
    # mueve al personaje.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR openCell = IsCellOpen(x,y,UO.GetZ(),x+1,y+1,UO.WorldNum())
    IF openCell = TRUE THEN
        UO.Print('Diagonal cell is locally passable')
    END IF
END SUB

SUB IsCellOpen(x,y,z,toX,toY,map)
    VAR cellResult = UO.IsWorldCellPassable(x,y,z,toX,toY,z,map)
    IF GetArrayLength(cellResult) <> 2 THEN
        RETURN 0
    END IF
    RETURN cellResult[0]
END SUB
```

**Explicación de los parámetros y la ejecución:**

- La función completa tras Main recibe X/Y/Z iniciales, X/Y finales y mapa. Añade el sexto argumento y devuelve solo Integer 1/0, no un array. IsCellOpen se puede comparar con TRUE. No mueve al personaje.
