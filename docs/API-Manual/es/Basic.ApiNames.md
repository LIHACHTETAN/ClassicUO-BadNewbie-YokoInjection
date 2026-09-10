# Basic / UO.

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Los comandos del juego usan UO.; Basic y tus funciones usan sus nombres declarados.

## Sintaxis exacta

```text
UO.command(arguments)
BasicFunction(arguments)
UserFunction(arguments)
```

## Parámetros

- `UO.command` — UO.command(arguments): prefijo obligatorio del juego. UO.GetType(id) lee el gráfico/cuerpo, no un tipo Basic o CLR.
- `BasicFunction` — BasicFunction(arguments): por ejemplo Int(value), Str(value), CInt(value), sin UO.
- `arguments` — self, backpack, ground y Rhand conservan su significado como argumentos de objeto, filtro o capa; no son llamadas abreviadas.

## Devuelve

La regla de nombres no devuelve nada. Int devuelve Integer, Str String; los tres Api*Exists devuelven Integer 1/0, utilizables como TRUE/FALSE.

## Comportamiento

- No se distingue entre mayúsculas y minúsculas. InjectionApi registra Basic sin prefijo, InjectionApiUO el juego con UO. Una llamada corta antigua produce SC005 con sugerencia UO.; no se ejecuta una sustitución implícita. Los valores de atributos también requieren UO. ApiNameExists, ApiSignatureExists y ApiParameterExists quitan espacios exteriores y comprueban el nombre registrado exacto sin añadir prefijo. Consultan metadatos, no el servidor. No se implementa el operador de reflexión VB.NET GetType(TypeName).

## Ejemplos

### 1. 1

```vb
# graphic lee el cuerpo o 0 sin datos; whole=2. registered comprueba UO.GetType con un argumento. Main devuelve "2:1" independientemente del gráfico, sin movimiento ni traslado.
Option Explicit On
Sub Main()
    Var graphic = UO.GetType('self')
    Var whole = Int(2.9)
    Var registered = UO.ApiSignatureExists('UO.GetType', 1)
    Return CStr(whole) + ":" + CStr(registered)
End Sub
```

**Explicación de los parámetros y la ejecución:**

graphic lee el cuerpo o 0 sin datos; whole=2. registered comprueba UO.GetType con un argumento. Main devuelve "2:1" independientemente del gráfico, sin movimiento ni traslado.

### 2. 2

```vb
# La Function GetType completa recibe value=6 de CInt(6) y devuelve 7. UO.GetType sigue leyendo el gráfico del juego. Las dos llamadas permanecen separadas.
Option Explicit On
Function GetType(value)
    Return value + 1
End Function
Sub Main()
    Var localResult = GetType(CInt(6))
    Var graphic = UO.GetType('self')
    Return localResult
End Sub
```

**Explicación de los parámetros y la ejecución:**

La Function GetType completa recibe value=6 de CInt(6) y devuelve 7. UO.GetType sigue leyendo el gráfico del juego. Las dos llamadas permanecen separadas.

### 3. 3

```vb
# oldCall=0, gameCall=1 y basicCall=1 comprueban GetType, UO.GetType(id) e Int(value). argumentName=1 confirma backpack como selector. Main devuelve "0:1:1:1". No se buscan procedimientos del usuario.
Option Explicit On
Sub Main()
    Var oldCall = UO.ApiSignatureExists('GetType', 1)
    Var gameCall = UO.ApiSignatureExists('UO.GetType', 1)
    Var basicCall = UO.ApiSignatureExists('Int', 1)
    Var argumentName = UO.ApiParameterExists('backpack')
    Return CStr(oldCall) + ":" + CStr(gameCall) + ":" + CStr(basicCall) + ":" + CStr(argumentName)
End Sub
```

**Explicación de los parámetros y la ejecución:**

oldCall=0, gameCall=1 y basicCall=1 comprueban GetType, UO.GetType(id) e Int(value). argumentName=1 confirma backpack como selector. Main devuelve "0:1:1:1". No se buscan procedimientos del usuario.

<!-- implementation references (not callable script procedures):
Runtime/InjectionApi.cs: Register
Runtime/InjectionApiUO.cs: Register / RegisterCharacterGetterAliases / ApiNameExists / ApiSignatureExists / ApiParameterExists
Analysis/InvalidSymbolVisitor.cs: VisitCall
Runtime/ScriptBindings.cs: Builder.CallName
-->
