# Do / Loop / While / Until / Repeat

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Do comprueba antes o después del cuerpo. While repite si es verdadero; Until hasta que sea verdadero. Repeat … Until es la forma antigua admitida con comprobación final.

## Sintaxis exacta

```text
Do While condition
    statements
Loop
Do Until condition
    statements
Loop
Do
    statements
Loop While condition
Do
    statements
Loop Until condition
Do
    statements
Loop
Repeat
    statements
Until condition
Continue Do
Exit Do
Break
```

## Parámetros

- `condition / While / Until` — Expresión Boolean numérica 0/False o 1/True. While continúa si es verdadera; Until sale si es verdadera. Se reevalúa en cada comprobación; el texto no se convierte a Boolean.
- `position / Repeat` — Tras Do, la condición puede evitar la primera pasada. Tras Loop o Until de Repeat ocurre al menos una. Solo se permite una posición de condición. Do … Loop sin condición necesita una salida explícita.
- `statements / exit` — Cuerpo. Continue Do llega a la próxima comprobación; Exit Do sale del Do o Repeat más cercano. Break sale del bucle más interno de cualquier tipo. RETURN termina todo el procedimiento/función.

## Devuelve

Do, Loop, Repeat, Until y Exit Do no devuelven valores. Los ejemplos devuelven explícitamente Integer 1,33,83 desde Main: contadores combinados, no resultados Boolean de comandos.

## Comportamiento

- La preparación empareja bloques y valida transferencias. Condiciones al principio y al final del mismo Do producen SC020. El motor comprueba en la posición elegida y repite según While/Until.
- Continue Do comprueba también la condición final cuando existe; con condición inicial vuelve a la cabecera. Los Finally abandonados se ejecutan exactamente una vez antes de transferir.
- Repeat ejecuta primero: comprueba arrays vacíos antes de entrar. Sin plazo implícito. Para esperar al juego usa Wait y un límite temporal; pausa/parada siguen activas.

## Ejemplos

### 1. Antes o después

```vb
# ready=True ya satisface Until. Do Until ready no realiza pasadas: before=0. El segundo ciclo comprueba después de incrementar, así que after=1. Main devuelve before*10+after=1.
Option Explicit On
Sub Main()
    Var ready = True
    Var before = 0
    Var after = 0
    Do Until ready
        before += 1
    Loop
    Do
        after += 1
    Loop Until ready
    Return before * 10 + after
End Sub
```

**Explicación de los parámetros y la ejecución:**

ready=True ya satisface Until. Do Until ready no realiza pasadas: before=0. El segundo ciclo comprueba después de incrementar, así que after=1. Main devuelve before*10+after=1.

### 2. Intentos limitados con limpieza

```vb
# attempts empieza en 0 y aumenta en cada pasada. Los primeros dos Continue Do ejecutan Finally y comprueban attempts<4. En el tercer intento Exit Do también ejecuta Finally. attempts=3, cleanup=3 producen 33. Es una simulación local, no reintentos de red reales.
Option Explicit On
Sub Main()
    Var attempts = 0
    Var cleanup = 0
    Do
        Try
            attempts += 1
            If attempts < 3 Then
                Continue Do
            End If
            Exit Do
        Finally
            cleanup += 1
        End Try
    Loop While attempts < 4
    Return attempts * 10 + cleanup
End Sub
```

**Explicación de los parámetros y la ejecución:**

attempts empieza en 0 y aumenta en cada pasada. Los primeros dos Continue Do ejecutan Finally y comprueban attempts<4. En el tercer intento Exit Do también ejecuta Finally. attempts=3, cleanup=3 producen 33. Es una simulación local, no reintentos de red reales.

### 3. Bucle antiguo con marcador

```vb
# values=[3,5,0] no está vacío. Repeat lee, incrementa index y suma. Until termina en cero o en el límite del array; OrElse omite la segunda comprobación al encontrar cero. total=8 e index=3 producen 83.
Option Explicit On
Sub Main()
    Dim values[2]
    values[0] = 3
    values[1] = 5
    values[2] = 0
    Var index = 0
    Var value = 0
    Var total = 0
    Repeat
        value = values[index]
        index += 1
        total += value
    Until (value = 0) OrElse (index >= GetArrayLength(values))
    Return total * 10 + index
End Sub
```

**Explicación de los parámetros y la ejecución:**

values=[3,5,0] no está vacío. Repeat lee, incrementa index y suma. Until termina en cero o en el límite del array; OrElse omite la segunda comprobación al encontrar cero. total=8 e index=3 producen 83.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(DoLoopContext) / VisitStatement(Repeat/Until)
Runtime/Interpreter.cs: LoopConditionInstruction / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/do-loop-statement
-->
