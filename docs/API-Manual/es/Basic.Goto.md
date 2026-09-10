# GoTo / label:

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

GoTo transfiere la ejecución a una etiqueta del procedimiento o función actual. Una etiqueta marca una posición, no un procedimiento invocable. Para el control habitual usa If, bucles y Return.

## Sintaxis exacta

```text
GoTo label
label:
```

## Parámetros

- `label` — Identificador declarado como label: en su propia línea del mismo procedimiento. Escribe GoTo label sin comillas, paréntesis ni dos puntos después del destino. Admite saltos hacia delante y atrás sin distinguir mayúsculas. Otro procedimiento puede reutilizar el nombre. Se admiten puntos, pero no convierten la etiqueta en miembro de módulo. No se admiten números, expresiones calculadas ni etiquetas de otro procedimiento como destinos.

## Devuelve

GoTo y label: no devuelven valores, tampoco 1/0 ni TRUE/FALSE. Los ejemplos devuelven explícitamente desde Main los Integer -1, 6 y 123 calculados por el script.

## Comportamiento

- La preparación registra direcciones y resuelve saltos después de leer todo el procedimiento. La ejecución usa la dirección resuelta sin buscar otra vez en el texto. Conserva las variables y no revierte acciones anteriores.
- Destino desconocido: SC009 y ejecución bloqueada por el cliente. Nombre repetido dentro de un procedimiento, incluso cambiando mayúsculas: SC021 antes de inicializar. Include conserva archivo y línea originales. Caracteres sobrantes pueden generar advertencias; usa la sintaxis exacta.
- Salir de Try activos ejecuta sus Finally del interior al exterior antes del destino. Un salto dentro del mismo Try activo lo conserva. Un error en Finally puede impedir alcanzar el destino.
- Entra en bucles y Try/Catch/Finally por su inicio normal. Saltar al medio no recrea inicializaciones ni contextos omitidos; no es una reanudación admitida. Para bucles usa Continue o Exit.
- El salto atrás no añade límite de intentos, plazo ni espera. Cambia expresamente la condición de salida. El flujo normal también atraviesa las etiquetas: salta las secciones no deseadas o usa Return. Los manejadores de errores se instalan con On Error.

## Ejemplos

### 1. Salto hacia delante

```vb
# amount=0 elige NoItems y result=-1, luego Finished devuelve -1. Con amount=4 el camino normal asigna 40 y GoTo Finished omite NoItems. Ambas etiquetas pertenecen a Main y no son llamadas.
Option Explicit On
Sub Main()
    Var amount = 0
    Var result = 0
    If amount <= 0 Then
        GoTo NoItems
    End If
    result = amount * 10
    GoTo Finished
NoItems:
    result = -1
Finished:
    Return result
End Sub
```

**Explicación de los parámetros y la ejecución:**

amount=0 elige NoItems y result=-1, luego Finished devuelve -1. Con amount=4 el camino normal asigna 40 y GoTo Finished omite NoItems. Ambas etiquetas pertenecen a Main y no son llamadas.

### 2. Repetición acotada

```vb
# attempt comienza en 0 y aumenta antes de comprobar. Again y again son la misma etiqueta. Tres pasadas suman 1, 2 y 3; después attempt<3 es falso y Return da 6. total se inicializa antes de la etiqueta y no se reinicia al saltar.
Option Explicit On
Sub Main()
    Var attempt = 0
    Var total = 0
Again:
    attempt += 1
    total += attempt
    If attempt < 3 Then
        GoTo again
    End If
    Return total
End Sub
```

**Explicación de los parámetros y la ejecución:**

attempt comienza en 0 y aumenta antes de comprobar. Again y again son la misma etiqueta. Tres pasadas suman 1, 2 y 3; después attempt<3 es falso y Return da 6. total se inicializa antes de la etiqueta y no se reinicia al saltar.

### 3. Salir de Try anidados

```vb
# trace pasa a 1; GoTo Finished omite trace=99. El Finally interior agrega el dígito 2 y el exterior agrega 3. Después se alcanza Finished y se devuelve 123. Cada Finally se ejecuta una vez para este salto.
Option Explicit On
Sub Main()
    Var trace = 0
    Try
        Try
            trace = trace * 10 + 1
            GoTo Finished
            trace = 99
        Finally
            trace = trace * 10 + 2
        End Try
    Finally
        trace = trace * 10 + 3
    End Try
Finished:
    Return trace
End Sub
```

**Explicación de los parámetros y la ejecución:**

trace pasa a 1; GoTo Finished omite trace=99. El Finally interior agrega el dígito 2 y el exterior agrega 3. Después se alcanza Finished y se devuelve 123. Cada Finally se ejecuta una vez para este salto.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: goto / label / SYMBOL
Analysis/LabelStructureValidator.cs: VisitSubrutine / VisitLabel
Analysis/InvalidSymbolVisitor.cs: VisitGoto / ValidateLabelReference
Runtime/Instructions/Generator.cs: Generate / VisitSubrutine
Runtime/Interpreter.cs: GotoInstruction / Transfer / forScopes disposal
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/goto-statement
-->
