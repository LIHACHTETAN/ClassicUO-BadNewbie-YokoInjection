# Include

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Include carga otro archivo fuente antes del análisis y la ejecución. Sus funciones y variables quedan disponibles sin iniciar automáticamente procedimientos ni hilos.

## Sintaxis exacta

```text
Include "fileName"
```

## Parámetros

- `fileName` — fileName: nombre no vacío entre comillas simples o dobles. Ruta relativa o absoluta literal, no variable ni expresión. Extensión libre; el contenido debe ser código admitido por el motor.

## Devuelve

Sin valor devuelto: directiva de preparación. No asignar Include(...) ni esperar ID, TRUE/FALSE o 1/0. Las funciones incluidas devuelven sus valores mediante RETURN.

## Comportamiento

- Escribir Include en una línea propia fuera de SUB/FUNCTION. Buscar junto al archivo que incluye, después en su subcarpeta Include. Rutas anidadas relativas a la biblioteca actual. Guardar el archivo principal antes de usar rutas relativas.
- Cada ruta completa se incluye una vez. Un ciclo A → B → A genera SC016. Errores de ruta, acceso y sintaxis impiden iniciar antes de inicializar globales. Diagnóstico y depurador conservan archivo y línea originales.
- Cerrar cadenas y SUB/FUNCTION en el mismo archivo. Volver a declarar una variable global o constante genera SC017 antes de ejecutar.
- El siguiente inicio lee bibliotecas modificadas; un script preparado o activo conserva su código. No copia perfiles ni inicia otros scripts.
- Cada archivo puede definir Option Explicit antes de sus declaraciones; si falta, hereda el principal. Las declaraciones comparten espacio de nombres, sin crear módulos automáticamente.
- UTF-8 con reconocimiento de BOM. Límites: 128 archivos incluido el principal, 32 niveles, 16.777.216 caracteres fuente. Include en comentarios o cadenas no carga archivos.
- Cada ejemplo tiene su carpeta. Guardar Main.bas y todos los archivos mostrados con nombres y subcarpetas exactos. Conjuntos listos: API Manual/Examples/Basic.Include/1, /2, /3. Ejecutar Main.bas sin concatenar archivos.

## Ejemplos

### 1. Función compartida

```vb
# Main.bas incluye Common.bas y llama Add(4, 7). left y right se pasan por valor; Add devuelve la suma y Main Integer 11. Common.bas no se inicia solo.
Option Explicit On
Include "Common.bas"
SUB Main()
    RETURN Add(4, 7)
END SUB
```

**Explicación de los parámetros y la ejecución:**

Main.bas incluye Common.bas y llama Add(4, 7). left y right se pasan por valor; Add devuelve la suma y Main Integer 11. Common.bas no se inicia solo.

**Common.bas**

```vbnet
Option Explicit On
FUNCTION Add(ByVal left, ByVal right)
    RETURN left + right
END FUNCTION
```

### 2. Biblioteca anidada

```vb
# Main.bas incluye lib/Route.bas, que incluye Math.bas de su carpeta lib. Distance(-3, 5) pasa dx=-3, dy=5 a Manhattan; Abs quita los signos y la suma es Integer 8. No mueve al personaje.
Option Explicit On
Include "lib/Route.bas"
SUB Main()
    RETURN Distance(-3, 5)
END SUB
```

**Explicación de los parámetros y la ejecución:**

Main.bas incluye lib/Route.bas, que incluye Math.bas de su carpeta lib. Distance(-3, 5) pasa dx=-3, dy=5 a Manhattan; Abs quita los signos y la suma es Integer 8. No mueve al personaje.

**lib/Route.bas**

```vbnet
Option Explicit On
Include "Math.bas"
FUNCTION Distance(ByVal dx, ByVal dy)
    RETURN Manhattan(dx, dy)
END FUNCTION
```

**lib/Math.bas**

```vbnet
Option Explicit On
FUNCTION Manhattan(ByVal dx, ByVal dy)
    RETURN Abs(dx) + Abs(dy)
END FUNCTION
```

### 3. Inclusión repetida

```vb
# Common.bas y ./Common.bas son el mismo archivo: CONST y función se declaran una vez. SharedValue=7; GetShared() devuelve 7, Main multiplica por 2 y devuelve Integer 14. Ambos usan Option Explicit On.
Option Explicit On
Include "Common.bas"
Include "./Common.bas"
SUB Main()
    RETURN GetShared() * 2
END SUB
```

**Explicación de los parámetros y la ejecución:**

Common.bas y ./Common.bas son el mismo archivo: CONST y función se declaran una vez. SharedValue=7; GetShared() devuelve 7, Main multiplica por 2 y devuelve Integer 14. Ambos usan Option Explicit On.

**Common.bas**

```vbnet
Option Explicit On
CONST SharedValue = 7
FUNCTION GetShared()
    RETURN SharedValue
END FUNCTION
```

<!-- implementation references (not callable script procedures):
Parsing/ScriptSourceGraph.cs: Load / Builder.AddInclude / ResolveLine
Runtime/InjectionRuntime.cs: Prepare / Load
Runtime/Interpreter.cs: Location / EvaluateInitializer / CallObserved
Analysis/SanityAnalyzer.cs: Analyze
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: PrepareScriptForExecution
InjectionScript.Lsp/Workspace.cs: UpdateDiagnostic
-->
