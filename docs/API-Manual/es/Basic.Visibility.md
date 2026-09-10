# Public / Private

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Public expone un miembro del módulo al código externo. Private permite acceso solo desde funciones, procedimientos e inicializadores de su propio módulo. El modificador va antes de la declaración, no de la llamada.

## Sintaxis exacta

```text
Public declaration
Private declaration
```

## Parámetros

- `visibility` — visibility: Public o Private. Sin modificador, SUB/FUNCTION del módulo son públicos y VAR/DIM/CONST privados.
- `declaration` — declaration: SUB/FUNCTION, VAR/DIM escalar o CONST. Public también admite Module y declaraciones de archivo. Private no se admite al nivel del archivo ni dentro del cuerpo de un procedimiento. Declare nombres sin punto.

## Devuelve

Public y Private no devuelven valores ni cambian tipos o resultados. Normalize(12) devuelve Integer 10 mediante RETURN; NextCount() devuelve el nuevo contador, no TRUE/FALSE.

## Comportamiento

- Dentro de Module se admiten nombres cortos y completos de sus miembros. El código externo solo accede a Public mediante ModuleName.Member. Public no crea un nombre global corto.
- El acceso se comprueba antes de ejecutar, incluso con Option Explicit Off. Acceder a un Private ajeno produce SC019; declaraciones incorrectas de módulo/modificador producen SC018 o errores de sintaxis. Los inicializadores no se ejecutan después de estos errores.
- Una función pública puede llamar un auxiliar privado: importa el módulo donde se declara la función llamante. Un auxiliar privado no se inicia por separado desde el IDE, una tecla rápida o la API externa de procedimientos.
- Public Const sigue siendo constante y Public Var mutable. Una variable local explícita oculta un campo del mismo nombre solo dentro de su procedimiento. Private no cifra ni oculta el código a su dueño.
- El depurador resuelve nombres cortos y acceso Private según el marco seleccionado. El campo es accesible dentro del módulo; desde el llamante externo se rechaza ModuleName.privateField.

## Ejemplos

### 1. Interfaz pública y auxiliar privado

```vb
# value=12 pasa a Limits.Normalize y luego Clamp. maximum=10 limita el resultado; ambas funciones devuelven Integer 10. Main solo llama a Normalize. Una llamada externa Limits.Clamp(12) está prohibida.
Option Explicit On
Module Limits
    Private Const maximum = 10
    Private Function Clamp(ByVal value)
        If value > maximum Then
            Return maximum
        End If
        Return value
    End Function
    Public Function Normalize(ByVal value)
        Return Clamp(value)
    End Function
End Module
Sub Main()
    Return Limits.Normalize(12)
End Sub
```

**Explicación de los parámetros y la ejecución:**

value=12 pasa a Limits.Normalize y luego Clamp. maximum=10 limita el resultado; ambas funciones devuelven Integer 10. Main solo llama a Normalize. Una llamada externa Limits.Clamp(12) está prohibida.

### 2. Campo privado y variable local

```vb
# VAR value=7 sin modificador es privada en Store. Read devuelve el campo 7. LocalValue declara su propia value=9 sin cambiar el campo. Main devuelve 7*10+9, Integer 79.
Option Explicit On
Module Store
    Var value = 7
    Public Function Read()
        Return value
    End Function
    Public Function LocalValue()
        Var value = 9
        Return value
    End Function
End Module
Sub Main()
    Return Store.Read() * 10 + Store.LocalValue()
End Sub
```

**Explicación de los parámetros y la ejecución:**

VAR value=7 sin modificador es privada en Store. Read devuelve el campo 7. LocalValue declara su propia value=9 sin cambiar el campo. Main devuelve 7*10+9, Integer 79.

### 3. Constante pública y contador privado

```vb
# Public Const increment=2 se lee como Counter.increment. Private count empieza en 1. NextCount suma increment, guarda y devuelve 3. Main devuelve 3*10+2, Integer 32. Se prohíben el acceso externo a Counter.count y la modificación de increment.
Option Explicit On
Module Counter
    Public Const increment = 2
    Private Var count = 1
    Public Function NextCount()
        count += increment
        Return count
    End Function
End Module
Sub Main()
    Var result = Counter.NextCount()
    Return result * 10 + Counter.increment
End Sub
```

**Explicación de los parámetros y la ejecución:**

Public Const increment=2 se lee como Counter.increment. Private count empieza en 1. NextCount suma increment, guarda y devuelve 3. Main devuelve 3*10+2, Integer 32. Se prohíben el acceso externo a Counter.count y la modificación de increment.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: visibility / globalVar / globalConst / subrutine
Runtime/ScriptBindings.cs: CheckAccess / CheckDeclaration
Runtime/InjectionRuntime.cs: BlockingLanguageError / CallSubrutineValues
ClassicUO.Client/Game/Managers/YokoInjectionManager.cs: DiscoverScopedProcedures / RunProcedure
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/modifiers/private
-->
