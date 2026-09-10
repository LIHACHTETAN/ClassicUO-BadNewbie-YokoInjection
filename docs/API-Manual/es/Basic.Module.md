# Module / End Module

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Module agrupa funciones, procedimientos, VAR/DIM y CONST bajo un nombre. Desde fuera se usan Tools.Sum o Counter.count; dentro del módulo actual se admiten nombres cortos.

## Sintaxis exacta

```text
Module moduleName
    members
End Module
moduleName.member(arguments)
moduleName.field
```

## Parámetros

- `moduleName` — moduleName: identificador simple sin distinguir mayúsculas, por ejemplo Tools. UO está reservado. Se rechazan nombres de módulo duplicados y módulos anidados.
- `members` — members: SUB/FUNCTION, VAR/DIM escalares, CONST, Include y una directiva Option Explicit válida. Un campo puede contener un array u objeto. DIM[...] directamente en el módulo no está disponible; cree el array con una función y guárdelo en VAR.
- `member / arguments` — member / arguments: nombre del miembro y argumentos de función. Tools.Sum(2, 3) pasa left=2 y right=3. El campo Counter.count se consulta sin paréntesis.

## Devuelve

Module no devuelve valor ni se llama como Module(...). Tools.Sum(...) devuelve el RETURN de esa función; un campo devuelve su valor almacenado. Las comparaciones devuelven Integer 1/0, correspondientes a TRUE/FALSE en condiciones y comparaciones. Un número, ID o cantidad cualquiera no es automáticamente un resultado booleano.

## Comportamiento

- Declare Module al nivel del archivo y termine con End Module. Include puede cargar un módulo o sus miembros; los errores conservan archivo y línea originales. Option Explicit pertenece al archivo físico.
- La preparación recopila nombres completos, vincula referencias cortas al módulo actual y comprueba el acceso antes de ejecutar. Un parámetro, VAR, CONST o DIM local explícito oculta un campo del mismo nombre. En otro caso se busca primero el campo del módulo y después la variable global tradicional.
- Los campos se inicializan en orden de declaración al comenzar cada ejecución independiente. Las llamadas anidadas de esa ejecución comparten cambios. Una ejecución nueva empieza de nuevo; los scripts concurrentes no comparten el estado del módulo. No se guarda en disco.
- Las funciones/procedimientos son Public por defecto; los campos/constantes son Private. Private requiere Module. Consulte Public / Private.
- El IDE muestra nombres completos. Las funciones públicas sin argumentos obligatorios se pueden iniciar desde la lista; los auxiliares privados siguen siendo internos. Sugerencias, navegación e inspección respetan el módulo actual.

## Ejemplos

### 1. Mismo nombre en módulos distintos

```vb
# Tools.Sum suma left=2 y right=3 y devuelve 5. Other.Sum los multiplica y devuelve 6. Los nombres completos distinguen las funciones; Main devuelve Integer 11.
Option Explicit On
Module Tools
    Public Function Sum(ByVal left, ByVal right)
        Return left + right
    End Function
End Module
Module Other
    Public Function Sum(ByVal left, ByVal right)
        Return left * right
    End Function
End Module
Sub Main()
    Return Tools.Sum(2, 3) + Other.Sum(2, 3)
End Sub
```

**Explicación de los parámetros y la ejecución:**

Tools.Sum suma left=2 y right=3 y devuelve 5. Other.Sum los multiplica y devuelve 6. Los nombres completos distinguen las funciones; Main devuelve Integer 11.

### 2. Campo compartido en una ejecución

```vb
# count comienza en 0. Cada Increment suma 1 al mismo campo; dos llamadas dejan before=2. Read observa Counter.count=5. Main devuelve 2*10+5, Integer 25. Una nueva ejecución vuelve a empezar en 0.
Option Explicit On
Module Counter
    Public Var count As Integer = 0
    Public Sub Increment()
        count += 1
    End Sub
    Public Function Read()
        Return count
    End Function
End Module
Sub Main()
    Counter.Increment()
    Counter.Increment()
    Var before = Counter.Read()
    Counter.count = 5
    Return before * 10 + Counter.Read()
End Sub
```

**Explicación de los parámetros y la ejecución:**

count comienza en 0. Cada Increment suma 1 al mismo campo; dos llamadas dejan before=2. Read observa Counter.count=5. Main devuelve 2*10+5, Integer 25. Una nueva ejecución vuelve a empezar en 0.

### 3. Resultado booleano

```vb
# maximum=4 es accesible dentro de Limits. Allowed(3) devuelve Integer 1 y Allowed(7) Integer 0. accepted=TRUE y rejected=FALSE comprueban esos valores. Main devuelve Integer 10 al cumplirse ambos.
Option Explicit On
Module Limits
    Private Const maximum = 4
    Public Function Allowed(ByVal amount)
        Return amount <= maximum
    End Function
End Module
Sub Main()
    Var accepted = Limits.Allowed(3)
    Var rejected = Limits.Allowed(7)
    If accepted = TRUE AndAlso rejected = FALSE Then
        Return 10
    End If
    Return 0
End Sub
```

**Explicación de los parámetros y la ejecución:**

maximum=4 es accesible dentro de Limits. Allowed(3) devuelve Integer 1 y Allowed(7) Integer 0. accepted=TRUE y rejected=FALSE comprueban esos valores. Main devuelve Integer 10 al cumplirse ambos.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: moduleDeclaration / moduleSection
Runtime/DeclarationScope.cs: Qualify / IsPrivate
Runtime/ScriptBindings.cs: Builder.Variable / CallName
Runtime/SemanticScope.cs: Scope / DefineGlobalVariables
Runtime/Interpreter.cs: EvaluateBoundExpression / CallSubrutine
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/module-statement
-->
