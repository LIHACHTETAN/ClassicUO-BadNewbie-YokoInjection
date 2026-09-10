# UO.GetFoundedText

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee el texto guardado de la entrada del diario seleccionada por este script.

## Sintaxis exacta

```text
UO.GetFoundedText() -> String
```

## Parámetros

Sin parámetros.

## Devuelve

String — texto seleccionado o cadena vacía si no hay selección. Una entrada existente también puede tener texto vacío. No es un serial, un índice ni un indicador booleano de éxito.

## Comportamiento

- InJournal, InJournalBetweenTimes, Journal/GetJournal y LastJournalMessage cambian la selección. Una búsqueda sin resultados, un índice Journal inválido o el borrado mediante este script la restablece. No recibe argumentos ni realiza otra búsqueda.
- Los mensajes nuevos no sustituyen el texto guardado. Si la entrada se elimina o se descarta del búfer, el texto permanece, pero GetFoundedTextIndex/LineIndex devuelve -1. Otro script puede vaciar el diario compartido; las variables guardadas no cambian.

## Ejemplos

### Leer un mensaje encontrado

```vb
# Leer un mensaje encontrado
#
# Lee el texto guardado de la entrada del diario seleccionada por este script.
#
# String — texto seleccionado o cadena vacía si no hay selección. Una entrada existente también
# puede tener texto vacío. No es un serial, un índice ni un indicador booleano de éxito.

SUB Main()
    # needle es una subcadena que distingue mayúsculas y minúsculas. Compruebe InJournal > 0:
    # devuelve la posición más 1, no el número de coincidencias.

    IF UO.InJournal('needle') > 0 THEN
        VAR text = UO.GetFoundedText()
        UO.Print(text)
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- needle es una subcadena que distingue mayúsculas y minúsculas. Compruebe InJournal > 0: devuelve la posición más 1, no el número de coincidencias.

### Leer una línea seleccionada

```vb
# Leer una línea seleccionada
#
# Lee el texto guardado de la entrada del diario seleccionada por este script.
#
# String — texto seleccionado o cadena vacía si no hay selección. Una entrada existente también
# puede tener texto vacío. No es un serial, un índice ni un indicador booleano de éxito.

SUB Main()
    # Journal(0) selecciona la entrada más reciente. Guarde texto e índice antes de Print, que puede
    # añadir un mensaje. Un texto vacío no demuestra que falte la entrada.

    VAR latest = UO.Journal(0)
    VAR index = UO.LineIndex()
    VAR text = UO.GetFoundedText()
    IF index >= 0 THEN
        UO.Print(text)
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- Journal(0) selecciona la entrada más reciente. Guarde texto e índice antes de Print, que puede añadir un mensaje. Un texto vacío no demuestra que falte la entrada.

### Guardar el texto antes de otra búsqueda

```vb
# Guardar el texto antes de otra búsqueda
#
# Lee el texto guardado de la entrada del diario seleccionada por este script.
#
# String — texto seleccionado o cadena vacía si no hay selección. Una entrada existente también
# puede tener texto vacío. No es un serial, un índice ni un indicador booleano de éxito.

SUB Main()
    # saved copia el primer resultado antes de que la segunda búsqueda cambie la selección. Los
    # mensajes y búsquedas posteriores no modifican esa variable.

    IF UO.InJournal('success') > 0 THEN
        VAR saved = UO.GetFoundedText()
        VAR another = UO.InJournal('failed')
        UO.Print(saved)
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- saved copia el primer resultado antes de que la segunda búsqueda cambie la selección. Los mensajes y búsquedas posteriores no modifican esa variable.
