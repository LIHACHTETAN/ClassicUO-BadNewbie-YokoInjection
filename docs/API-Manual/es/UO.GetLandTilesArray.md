# UO.GetLandTilesArray

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Busca baldosas de terreno por graphic/type en un rectángulo.

## Sintaxis exacta

```text
UO.GetLandTilesArray(Xmin:Any, Ymin:Any, Xmax:Any, Ymax:Any, WorldNum:Any, TileType:Any) -> Any
```

## Parámetros

- `Xmin` — Coordenadas mundiales de dos esquinas incluidas, 0..65535. Las esquinas invertidas se normalizan. Máximo 1.000.000 de celdas; límites inválidos producen un error de script antes de leer el mapa.
- `Ymin` — Coordenadas mundiales de dos esquinas incluidas, 0..65535. Las esquinas invertidas se normalizan. Máximo 1.000.000 de celdas; límites inválidos producen un error de script antes de leer el mapa.
- `Xmax` — Coordenadas mundiales de dos esquinas incluidas, 0..65535. Las esquinas invertidas se normalizan. Máximo 1.000.000 de celdas; límites inválidos producen un error de script antes de leer el mapa.
- `Ymax` — Coordenadas mundiales de dos esquinas incluidas, 0..65535. Las esquinas invertidas se normalizan. Máximo 1.000.000 de celdas; límites inválidos producen un error de script antes de leer el mapa.
- `WorldNum` — Número de mapa/faceta 0..255; usa UO.WorldNum(). Otro mapa devuelve un Array vacío. Si cambia el mapa entre bloques de trabajo, se descarta el resultado parcial.
- `TileType` — Un graphic/type de baldosa, normalmente 0..65535, no un serial. 0 busca exactamente graphic 0; -1 no es un comodín. Un tipo sin coincidencias produce un resultado vacío.

## Devuelve

Array de registros [graphic, X, Y, Z], todos Integer. graphic es el tipo de terreno, Z la altura de su base. Sin coincidencias: Array vacío. La cantidad de registros es GetArrayLength(result). Los índices empiezan en 0. No es Boolean, serial ni Pascal record; no existe un séptimo parámetro de salida.

## Comportamiento

- Lee datos locales sin cambiar FindItem/FindCount, mover al personaje, activar target ni enviar órdenes al servidor.
- X ascendente y, dentro de cada X, Y ascendente. Los registros de una celda conservan el orden del bridge, no el de distancia o altura.
- Hasta 32 celdas por bloque de trabajo con un presupuesto flexible de aproximadamente 1 ms. Comprueba cancelación entre bloques. Una celda compleja o una lectura en frío puede tardar más. Divide las áreas grandes; el mundo puede cambiar durante la lectura.

### Funciones internas: de la llamada al resultado

Pasos C# reales, no comandos UO adicionales. Los ejemplos incluyen la definición completa del procedimiento auxiliar.

#### 1. ExecuteStealthCompatibility

Recibe seis argumentos; la forma normal pasa un tipo, Ex convierte un Array o escalar en tipos.

Llama a FindPortableTiles en modo land/static y devuelve directamente el Array de registros.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `ExecuteStealthCompatibility`.

#### 2. FindPortableTiles

Valida coordenadas, mapa y área con aritmética de 64 bits; normaliza las esquinas y crea un HashSet de tipos.

Guarda el cursor X/Y y programa ScanSlice mediante ExecutePathQuerySlice. Wait(0) comprueba cancelación entre bloques; un cambio de mapa produce un Array vacío.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `FindPortableTiles`.

#### 3. ScanSlice

Procesa hasta 32 celdas en el hilo del juego, guardando el cursor después de cada celda.

GetLandscapeTile proporciona graphic/Z/flags; GetStaticTiles proporciona ternas graphic/Z/hue. Añade coincidencias y devuelve el control entre bloques.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `ScanSlice`.

#### 4. GetChunk2

Recibe coordenadas del bloque y opción de carga; valida ambos ejes antes del índice lineal.

Devuelve Chunk o null; Y fuera del mapa no se sustituye por una columna vecina. Reutiliza los bloques cargados y lee otros cuando es necesario.

Código del proyecto: `src/ClassicUO.Client/Game/Map/Map.cs`; función `GetChunk2`.

Lee datos locales sin cambiar FindItem/FindCount, mover al personaje, activar target ni enviar órdenes al servidor.


## Ejemplos

### Buscar cerca del personaje

```vb
# Buscar cerca del personaje
#
# Busca baldosas de terreno por graphic/type en un rectángulo.
#
# Array de registros [graphic, X, Y, Z], todos Integer. graphic es el tipo de terreno, Z la
# altura de su base. Sin coincidencias: Array vacío. La cantidad de registros es
# GetArrayLength(result). Los índices empiezan en 0. No es Boolean, serial ni Pascal record; no
# existe un séptimo parámetro de salida.

SUB Main()
    # x/y son las coordenadas de self, map es el mapa actual. El área 3×3 incluye los bordes. Ex usa
    # dos tipos de ejemplo y la forma normal uno. Cambia los graphic según tus recursos, no por ID
    # de objetos.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetLandTilesArray(x, y, x + 2, y + 2, map, 0x0003)
    UO.Print("Records: " + CStr(GetArrayLength(rows)))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- x/y son las coordenadas de self, map es el mapa actual. El área 3×3 incluye los bordes. Ex usa dos tipos de ejemplo y la forma normal uno. Cambia los graphic según tus recursos, no por ID de objetos.

### Esquinas invertidas y todos los campos

```vb
# Esquinas invertidas y todos los campos
#
# Busca baldosas de terreno por graphic/type en un rectángulo.
#
# Array de registros [graphic, X, Y, Z], todos Integer. graphic es el tipo de terreno, Z la
# altura de su base. Sin coincidencias: Array vacío. La cantidad de registros es
# GetArrayLength(result). Los índices empiezan en 0. No es Boolean, serial ni Pascal record; no
# existe un séptimo parámetro de salida.

SUB Main()
    # El área 2×2 usa esquinas descendentes que se normalizan. row es un registro. PrintTile está
    # definida por completo y solo imprime números. Para terreno hue=0 es un argumento de relleno;
    # sus registros no tienen campo hue.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR rows = UO.GetLandTilesArray(x + 1, y + 1, x, y, map, 0x0003)
    VAR i = 0
    WHILE i < GetArrayLength(rows)
        VAR row = rows[i]
        PrintTile(row[0], row[1], row[2], row[3], 0)
        i = i + 1
    WEND
END SUB

SUB PrintTile(graphic, x, y, z, hue)
    UO.Print("Type=" + CStr(graphic) + " X=" + CStr(x) + " Y=" + CStr(y))
    UO.Print("Z=" + CStr(z) + " hue=" + CStr(hue))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El área 2×2 usa esquinas descendentes que se normalizan. row es un registro. PrintTile está definida por completo y solo imprime números. Para terreno hue=0 es un argumento de relleno; sus registros no tienen campo hue.

### Repetir con intentos limitados

```vb
# Repetir con intentos limitados
#
# Busca baldosas de terreno por graphic/type en un rectángulo.
#
# Array de registros [graphic, X, Y, Z], todos Integer. graphic es el tipo de terreno, Z la
# altura de su base. Sin coincidencias: Array vacío. La cantidad de registros es
# GetArrayLength(result). Los índices empiezan en 0. No es Boolean, serial ni Pascal record; no
# existe un séptimo parámetro de salida.

SUB Main()
    # Como máximo tres búsquedas de una celda con WAIT(250) entre intentos. Cada llamada crea un
    # resultado nuevo. Longitud cero significa que no hay coincidencias ahora, no ausencia
    # permanente en el servidor.

    VAR x = UO.GetX()
    VAR y = UO.GetY()
    VAR map = UO.WorldNum()
    VAR attempt = 0
    WHILE attempt < 3
        VAR rows = UO.GetLandTilesArray(x, y, x, y, map, 0x0003)
        UO.Print("Records: " + CStr(GetArrayLength(rows)))
        attempt = attempt + 1
        WAIT(250)
    WEND
END SUB
```

**Explicación de los parámetros y la ejecución:**

- Como máximo tres búsquedas de una celda con WAIT(250) entre intentos. Cada llamada crea un resultado nuevo. Longitud cero significa que no hay coincidencias ahora, no ausencia permanente en el servidor.
