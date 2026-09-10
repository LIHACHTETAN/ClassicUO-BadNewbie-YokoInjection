# UO.GetGumpInfo

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee una instantánea coherente de un gump del servidor y sus controles.

## Sintaxis exacta

```text
UO.GetGumpInfo(GumpIndex:Any) -> Array
```

## Parámetros

- `GumpIndex` — Integer obligatorio: índice desde 0 hasta GetGumpsCount()-1, no serial ni GumpID. Un índice negativo o fuera de la lista es inválido. Abrir, cerrar o reordenar ventanas puede cambiar el índice.

## Devuelve

Array de cinco campos: [0] Integer serial; [1] Integer GumpID; [2] Array<String> de textos no vacíos; [3] Array<String> de descripciones de botones normales; [4] Array<String> de todos los controles activos, incluidos los anidados. Un gump inválido, cerrado o ignorado devuelve []. Los ID con el bit alto aparecen como Integer negativos; Hex muestra sus bits.

## Comportamiento

- Todo se copia en una petición al hilo del juego. Los cambios o cierres posteriores no modifican los arrays guardados. Solo incluye gumps activos del servidor; las ventanas locales de mochila, mapa y ajustes quedan fuera.
- Este array BASIC no es el registro Pascal TGumpInfo ni el paquete original de diseño. Las descripciones incluyen tipo, page, ID, X/Y y dimensiones; los botones añaden ButtonID, action, toPage y gráficos; los selectores añaden checked e inactive/active. El texto puede contener espacios y =. Los botones de opción están en [4], no en [3].
- AddGumpIgnoreByID/BySerial suprimen esta lectura en el script actual; ClearGumpsIgnore elimina el filtro. GetGumpsCount no cambia. Un gump existente puede tener arrays de texto vacíos. La longitud de un array se obtiene con GetArrayLength, no Len.

## Ejemplos

### Leer ambos ID

```vb
# Leer ambos ID
#
# Lee una instantánea coherente de un gump del servidor y sus controles.
#
# Array de cinco campos: [0] Integer serial; [1] Integer GumpID; [2] Array<String> de textos no
# vacíos; [3] Array<String> de descripciones de botones normales; [4] Array<String> de todos los
# controles activos, incluidos los anidados. Un gump inválido, cerrado o ignorado devuelve [].
# Los ID con el bit alto aparecen como Integer negativos; Hex muestra sus bits.

SUB Main()
    # 0 selecciona el primer gump del servidor. Comprobar GetArrayLength(info)=5 antes de acceder a
    # los campos. info[0] es serial e info[1] es GumpID de la misma instantánea.

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        UO.Print('Serial=' + Hex(info[0]))
        UO.Print('GumpID=' + Hex(info[1]))
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- 0 selecciona el primer gump del servidor. Comprobar GetArrayLength(info)=5 antes de acceder a los campos. info[0] es serial e info[1] es GumpID de la misma instantánea.

### Enumerar los ButtonID reales

```vb
# Enumerar los ButtonID reales
#
# Lee una instantánea coherente de un gump del servidor y sus controles.
#
# Array de cinco campos: [0] Integer serial; [1] Integer GumpID; [2] Array<String> de textos no
# vacíos; [3] Array<String> de descripciones de botones normales; [4] Array<String> de todos los
# controles activos, incluidos los anidados. Un gump inválido, cerrado o ignorado devuelve [].
# Los ID con el bit alto aparecen como Integer negativos; Hex muestra sus bits.

SUB Main()
    # info[3] contiene descripciones de botones. i es el índice de una línea; el campo ButtonID de
    # la descripción es el ID para responder. Los botones de opción pertenecen a la lista completa.

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR buttons = info[3]
        VAR i = 0
        WHILE i < GetArrayLength(buttons)
            UO.Print(buttons[i])
            i = i + 1
        WEND
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- info[3] contiene descripciones de botones. i es el índice de una línea; el campo ButtonID de la descripción es el ID para responder. Los botones de opción pertenecen a la lista completa.

### Guardar el texto antes de cerrar

```vb
# Guardar el texto antes de cerrar
#
# Lee una instantánea coherente de un gump del servidor y sus controles.
#
# Array de cinco campos: [0] Integer serial; [1] Integer GumpID; [2] Array<String> de textos no
# vacíos; [3] Array<String> de descripciones de botones normales; [4] Array<String> de todos los
# controles activos, incluidos los anidados. Un gump inválido, cerrado o ignorado devuelve [].
# Los ID con el bit alto aparecen como Integer negativos; Hex muestra sus bits.

SUB Main()
    # info[2] es una copia del texto. CloseSimpleGump(0) cierra localmente solo sin NoClose y no
    # devuelve un valor. Los textos guardados permanecen; comprobar la longitud antes de texts[0].

    VAR info = UO.GetGumpInfo(0)
    IF GetArrayLength(info) = 5 THEN
        VAR texts = info[2]
        UO.CloseSimpleGump(0)
        IF GetArrayLength(texts) > 0 THEN
            UO.Print(texts[0])
        END IF
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- info[2] es una copia del texto. CloseSimpleGump(0) cierra localmente solo sin NoClose y no devuelve un valor. Los textos guardados permanecen; comprobar la longitud antes de texts[0].
