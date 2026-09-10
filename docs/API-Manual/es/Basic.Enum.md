# Enum / End Enum

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Enum agrupa constantes Integer con nombre para estados del script. Se declara en el archivo o en Module, fuera de Sub/Function. Es un subconjunto de VB.NET y no crea un objeto .NET Enum.

## Sintaxis exacta

```text
[Public | Private] Enum name [As Integer]
    member [= constantExpression]
    ...
End Enum
Dim state As name = name.member
ModuleName.name.member
```

## Parámetros

- `Public / Private` — Public es el valor predeterminado, también en Module. Private solo se permite en Module y oculta el tipo y sus miembros al resto de módulos y al archivo.
- `name` — Nombre simple sin puntos, como Mode, sin distinguir mayúsculas. UO y los tipos integrados están reservados. El nombre completo no puede duplicar Enum, Module o una variable global.
- `As Integer` — Opcional; solo Integer de 32 bits con signo, -2147483648..2147483647. Otros tipos base se rechazan. As Mode en variable, parámetro o resultado Function usa almacenamiento y conversión Integer; no restringe los valores a los miembros. Sin inicializar vale 0.
- `member` — Un nombre simple por línea, al menos un miembro. Se rechazan duplicados, True y False. Sin expresión, el primero vale 0 y cada siguiente aumenta el anterior en 1. Distintos nombres pueden compartir un valor.
- `constantExpression` — Expresión constante opcional: enteros decimales/0x, paréntesis, menos unario, + - * / Mod, miembros anteriores y Const numéricas ya declaradas. El resultado final debe ser entero dentro del rango; las divisiones intermedias pueden ser fraccionarias. Las Const referidas también deben dar Integer, sin tipo o As Integer/Long/Short/Byte. Sin llamadas, variables, String, comparaciones ni lecturas de arrays. Se rechazan referencias futuras, ciclos y dependencias de más de 128 niveles.
- `name.member` — Leer Mode.Ready o Tools.Mode.Ready desde fuera del módulo. Dentro de Tools basta Mode.Ready; With Mode permite .Ready. Asignar, += y escribir de vuelta por ByRef no pueden cambiar constantes. Enum no se llama como función.

## Devuelve

La declaración no devuelve valores ni necesita paréntesis de llamada. Un miembro devuelve Integer, por ejemplo Mode.Working = 3: es un estado, no éxito automático. La comparación state = Mode.Finished devuelve 1/True o 0/False; ambas formas son válidas. El estado 0 puede significar Idle y no fallo.

## Comportamiento

- EnumCatalog calcula constantes anteriores durante la preparación sin ejecutar script/API, asigna valores automáticos y verifica nombres, acceso y límites. SC026 impide iniciar incluso sin Option Explicit. Los errores sintácticos también bloquean; escribir una declaración incompleta produce diagnósticos.
- DefinitionCollector instala miembros constantes antes de inicializadores globales y valores Optional, que pueden usar Enum declarados más abajo. Dentro de Enum solo se admiten constantes anteriores. El script preparado conserva el catálogo; cargar otro lo sustituye.
- ScriptBindings resuelve nombres de módulo y Private una vez. La ejecución lee constantes, sin recalcular en bucles ni reflexión. As Mode se normaliza a Integer, que puede mostrar el depurador. Include puede aportar la declaración. No hay atributos Flags, métodos System.Enum, importación implícita ni lista automática de miembros.

## Ejemplos

### 1. Nombrar estados

```vb
# Idle=0 y Queued=1 se asignan automáticamente. Working=10 reinicia la secuencia y Finished=11. state As TaskState recibe 10. Main devuelve String "0:1:10:11"; CStr convierte los números. Adapte los nombres a su script; la declaración no inicia procedimientos.
Option Explicit On
Enum TaskState As Integer
    Idle
    Queued
    Working = 10
    Finished
End Enum

Sub Main()
    Dim state As TaskState = TaskState.Working
    Return CStr(TaskState.Idle) & ":" & CStr(TaskState.Queued) & ":" & CStr(state) & ":" & CStr(TaskState.Finished)
End Sub
```

**Explicación de los parámetros y la ejecución:**

Idle=0 y Queued=1 se asignan automáticamente. Working=10 reinicia la secuencia y Finished=11. state As TaskState recibe 10. Main devuelve String "0:1:10:11"; CStr convierte los números. Adapte los nombres a su script; la declaración no inicia procedimientos.

### 2. Ocultar el estado de un módulo

```vb
# Controller.Mode es interno. NextMode recibe distance ByVal As Integer sin modificar el argumento original. distance<=1 elige Arrived=5; de lo contrario Walking=4. state empieza en 0. Main pasa 3 y 1, recibe 4 y 5 y devuelve Integer 45. No mueve al personaje: distance es un dato de ejemplo. Desde fuera se permite Controller.NextMode, pero no Controller.Mode.Arrived.
Option Explicit On
Module Controller
    Private Enum Mode
        Idle
        Walking = 4
        Arrived
    End Enum

    Public Function NextMode(ByVal distance As Integer) As Integer
        Dim state As Mode
        If distance <= 1 Then
            state = Mode.Arrived
        Else
            state = Mode.Walking
        End If
        Return state
    End Function
End Module

Sub Main()
    Dim farState = Controller.NextMode(3)
    Dim nearState = Controller.NextMode(1)
    Return farState * 10 + nearState
End Sub
```

**Explicación de los parámetros y la ejecución:**

Controller.Mode es interno. NextMode recibe distance ByVal As Integer sin modificar el argumento original. distance<=1 elige Arrived=5; de lo contrario Walking=4. state empieza en 0. Main pasa 3 y 1, recibe 4 y 5 y devuelve Integer 45. No mueve al personaje: distance es un dato de ejemplo. Desde fuera se permite Controller.NextMode, pero no Controller.Mode.Arrived.

### 3. Cambiar estados y devolver Boolean

```vb
# La Const Integer anterior FirstState=2 produce Idle=2, Working=3, Finished=4. Advance recibe state ByRef y modifica la variable de Main; With Mode abrevia nombres y Select Case elige la transición. Dos llamadas dan 2→3→4. IsFinal recibe una copia ByVal y compara Finished: Main devuelve 1/True; tras una sola transición sería 0/False. Otro Advance lanzaría "No next state". Las constantes nunca cambian.
Option Explicit On
Const FirstState As Integer = 2
Enum Mode
    Idle = FirstState
    Working = Idle + 1
    Finished
End Enum

Sub Advance(ByRef state As Mode)
    With Mode
        Select Case state
            Case .Idle
                state = .Working
            Case .Working
                state = .Finished
            Case Else
                Throw "No next state"
        End Select
    End With
End Sub

Function IsFinal(ByVal state As Mode) As Boolean
    Return state = Mode.Finished
End Function

Sub Main()
    Dim state As Mode = Mode.Idle
    Advance(state)
    Advance(state)
    Return IsFinal(state)
End Sub
```

**Explicación de los parámetros y la ejecución:**

La Const Integer anterior FirstState=2 produce Idle=2, Working=3, Finished=4. Advance recibe state ByRef y modifica la variable de Main; With Mode abrevia nombres y Select Case elige la transición. Dos llamadas dan 2→3→4. IsFinal recibe una copia ByVal y compara Finished: Main devuelve 1/True; tras una sola transición sería 0/False. Otro Advance lanzaría "No next state". Las constantes nunca cambian.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: enumDeclaration / enumMember
Runtime/EnumCatalog.cs: Build / Observe / Reference / Evaluate
Runtime/DefinitionCollector.cs: VisitFile / VisitEnumDeclaration
Runtime/ScriptBindings.cs: Variable / VisitTypeClause / VisitWithStatement
Runtime/SemanticScope.cs: DefineGlobalVariables / SetVar
Runtime/Metadata.cs: NormalizeType
-->
