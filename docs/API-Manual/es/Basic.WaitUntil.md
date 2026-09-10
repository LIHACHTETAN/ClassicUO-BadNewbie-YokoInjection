# Wait Until / Timeout

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Wait Until comprueba una condición hasta que se cumple o vence el plazo. Es una extensión de Basic, no una instrucción VB.NET. Se ejecuta en el script actual sin crear hilos ni iniciar otra rutina.

## Sintaxis exacta

```text
Wait Until condition Timeout milliseconds
```

## Parámetros

- `condition` — condition se evalúa inmediatamente y después entre esperas cortas. Use Boolean o una comparación: el número 0 significa false; los demás valores siguen If. El String "false" no es Boolean false. Puede llamar a UO o a sus funciones; los errores se propagan y los efectos se repiten en cada prueba.
- `Timeout milliseconds` — Timeout es obligatorio. milliseconds se evalúa una vez antes de la primera prueba y debe ser Integer 0..2147483647. Negativos, fracciones y Strings generan un error antes de condition. Cero permite solamente la prueba inmediata. En otros lugares timeout sigue siendo un nombre de variable válido.

## Devuelve

La instrucción no devuelve un valor. El éxito continúa en la siguiente línea; el vencimiento genera un error con archivo y línea, manejable por Try/Catch u On Error. Sin manejador falla la ejecución actual. No devuelve false automáticamente: el ejemplo 2 crea una función con True/1 o False/0.

## Comportamiento

- El intérprete guarda la duración e inicia un Stopwatch monótono. La primera prueba inmediata puede tener éxito incluso con límite cero. Tras false, el ciclo comprueba cancelación y pausa, calcula el tiempo restante y espera hasta 10 ms antes de otra prueba. Evita un bucle ocupado continuo; el planificador puede alargar los intervalos.
- La pausa suspende las pruebas, pero el tiempo real cuenta en el límite. Al reanudar, un plazo vencido produce error antes de otra prueba. Detener interrumpe la espera y omite Catch/Finally del script como otras cancelaciones de emergencia. No puede interrumpir por fuerza una llamada bloqueada en condition: use funciones cortas. Una prueba iniciada termina antes de procesar su resultado o error.
- Un error de condition conserva su identidad y no se convierte en timeout. Errores normales y vencimientos ejecutan los Finally correspondientes. Las variables pertenecen a la llamada actual y cada nueva entrada inicia otro plazo. No hay End Wait ni parámetro adicional de intervalo. Wait(milliseconds) sigue siendo una función de demora independiente.

## Ejemplos

### 1. Consultar una función con presupuesto

```vb
# checks comienza en 0; Ready lo recibe ByRef y aumenta en cada prueba. required=3 es ByVal; budget=5000 permite cinco segundos. Dos pruebas dan false y la tercera true; Main devuelve Integer 3. Es un ejemplo determinista sin simular un servidor; cambie la condición por su consulta real.
Option Explicit On
Function Ready(ByRef checks As Integer, ByVal required As Integer) As Boolean
    checks += 1
    Return checks >= required
End Function

Sub Main()
    Dim checks As Integer = 0
    Const budget = 5000
    Wait Until Ready(checks, 3) Timeout budget
    Return checks
End Sub
```

**Explicación de los parámetros y la ejecución:**

checks comienza en 0; Ready lo recibe ByRef y aumenta en cada prueba. required=3 es ByVal; budget=5000 permite cinco segundos. Dos pruebas dan false y la tercera true; Main devuelve Integer 3. Es un ejemplo determinista sin simular un servidor; cambie la condición por su consulta real.

### 2. Devolver Boolean desde una función propia

```vb
# TryWait recibe ready=False y budget=0. La prueba inmediata falla por timeout. Catch problem devuelve False; Main devuelve 0, comparable con False. ready=True daría 1/True. Esta función captura todos los errores: examine problem para diferenciarlos. ready es un valor Boolean, no una función callback.
Option Explicit On
Function TryWait(ByVal ready As Boolean, ByVal budget As Integer) As Boolean
    Try
        Wait Until ready Timeout budget
        Return True
    Catch problem
        Return False
    End Try
End Function

Sub Main()
    Dim success = TryWait(False, 0)
    Return success
End Sub
```

**Explicación de los parámetros y la ejecución:**

TryWait recibe ready=False y budget=0. La prueba inmediata falla por timeout. Catch problem devuelve False; Main devuelve 0, comparable con False. ready=True daría 1/True. Esta función captura todos los errores: examine problem para diferenciarlos. ready es un valor Boolean, no una función callback.

### 3. Conservar un error y finalizar

```vb
# CheckStatus con state=-1 lanza "disconnected" inmediatamente. El límite de 3000 ms no reemplaza el error. Catch copia problem a message; Finally fija finished=True/1. Main devuelve "disconnected:1". state=1 tendría éxito inmediato; state=0 seguiría false hasta vencer el plazo. No requiere conexión al juego.
Option Explicit On
Function CheckStatus(ByVal state As Integer) As Boolean
    If state < 0 Then
        Throw "disconnected"
    End If
    Return state = 1
End Function

Sub Main()
    Dim message = ""
    Dim finished = False
    Try
        Wait Until CheckStatus(-1) Timeout 3000
    Catch problem
        message = problem
    Finally
        finished = True
    End Try
    Return message & ":" & CStr(finished)
End Sub
```

**Explicación de los parámetros y la ejecución:**

CheckStatus con state=-1 lanza "disconnected" inmediatamente. El límite de 3000 ms no reemplaza el error. Catch copia problem a message; Finally fija finished=True/1. Main devuelve "disconnected:1". state=1 tendría éxito inmediato; state=0 seguiría false hasta vencer el plazo. No requiere conexión al juego.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: waitUntilStatement / WAIT_UNTIL
Analysis/LoopStructureValidator.cs: VisitWaitUntilStatement
Runtime/Interpreter.cs: VisitWaitUntilStatement / Failure
Runtime/InjectionRuntime.cs: executionCheckpoint / retrieveCancellationToken
-->
