# Select Case / Case / Exit Select

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Select Case elige una rama comparando un valor guardado con alternativas ordenadas. Sirve para categorías, modos del script e intervalos numéricos. Es una instrucción Basic sin UO.; las llamadas al juego dentro de expresiones conservan UO.

## Sintaxis exacta

```text
Select Case expression
    Case value1, value2
        statements
        Exit Select
    Case from To to
        statements
    Case Is >= value
        statements
    Case Else
        statements
End Select
```

## Parámetros

- `expression` — Expresión obligatoria: variable, literal o llamada a función. Se evalúa exactamente una vez por entrada, incluso en bloques vacíos o solo con Case Else.
- `value / from / to` — Case admite un valor o alternativas separadas por comas, cada una una expresión. from To to incluye ambos extremos; un intervalo invertido no coincide. El extremo superior se evalúa solo si pasa la comparación inferior. Las comas de argumentos de una función no separan alternativas.
- `Is comparison value` — Comparaciones =, <>, <, <=, > o >=. Is es opcional: Case Is >= 5 equivale a Case >= 5. Son comparaciones de valores del motor, no pruebas de tipo de objeto.
- `Case Else` — Rama opcional para cuando ningún Case anterior coincide. Debe ser única y la última. Sin ella, la falta de coincidencia continúa tras End Select.
- `Exit Select` — Sale del Select Case contenedor más cercano, después de su End Select. No termina el bucle exterior ni la rutina. Fuera de Select Case produce un error de carga.

## Devuelve

Select Case, Case, End Select y Exit Select no devuelven valores y no se comparan con TRUE o 1. Las funciones de ejemplo devuelven String o Integer mediante Return. TRUE es numéricamente 1 y FALSE es 0: Case True coincide con 1, no con cualquier número distinto de cero.

## Comportamiento

- La preparación crea SelectInstruction, comprobaciones CaseInstruction ordenadas y saltos resueltos. El valor queda privado de la llamada actual, sin variable local artificial. Recursión y bloques anidados mantienen capturas independientes; una nueva entrada sustituye la anterior.
- CaseMatches comprueba de izquierda a derecha hasta coincidir. La rama elegida se ejecuta una vez y un salto omite las restantes. Los cambios en un Case no releen la selección; los efectos ya producidos permanecen.
- Números y cadenas usan las comparaciones habituales del motor; las cadenas distinguen mayúsculas. Option Compare Text y las conversiones automáticas de VB.NET no están implementados. Convierte explícitamente al comparar números y texto.
- End Select es obligatorio. No se admite código ejecutable antes del primer Case ni un For/Next dividido entre ramas. Los bloques incorrectos impiden la carga. Entra por Select Case, no mediante GoTo al interior.
- Los errores van al manejador actual. On Error Resume Next omite toda la selección si falla su expresión; un Case fallido avanza al siguiente. Resume reintenta la instrucción. Exit Select ejecuta los Finally activos que abandona. Pausa y parada se comprueban entre instrucciones; no se añaden esperas ni tiempos límite.

## Ejemplos

### 1. Clasificar cantidades

```vb
# DescribeAmount recibe amount ByVal. Case 0 devuelve empty; 1 To 4 incluye 1 y 4; Is >= 5 devuelve large. Los negativos llegan a Case Else. Main llama con -1, 0, 4, 5 y concatena negative:empty:small:large. Son resultados definidos por el script.
Option Explicit On
Function DescribeAmount(ByVal amount)
    Select Case amount
        Case 0
            Return "empty"
        Case 1 To 4
            Return "small"
        Case Is >= 5
            Return "large"
        Case Else
            Return "negative"
    End Select
End Function

Sub Main()
    Return DescribeAmount(-1) & ":" & DescribeAmount(0) & ":" & DescribeAmount(4) & ":" & DescribeAmount(5)
End Sub
```

**Explicación de los parámetros y la ejecución:**

DescribeAmount recibe amount ByVal. Case 0 devuelve empty; 1 To 4 incluye 1 y 4; Is >= 5 devuelve large. Los negativos llegan a Case Else. Main llama con -1, 0, 4, 5 y concatena negative:empty:small:large. Son resultados definidos por el script.

### 2. Observar llamadas

```vb
# ReadMode incrementa reads ByRef y devuelve 2 una vez. Candidate incrementa checks y devuelve value. El candidato 1 no coincide, 2 sí y 3 se omite. selected vale 7; Main devuelve 1*100+2*10+7=127 sin acceder al juego.
Option Explicit On
Function ReadMode(ByRef reads)
    reads += 1
    Return 2
End Function

Function Candidate(ByRef checks, ByVal value)
    checks += 1
    Return value
End Function

Sub Main()
    Dim reads = 0
    Dim checks = 0
    Dim selected = 0
    Select Case ReadMode(reads)
        Case Candidate(checks, 1)
            selected = -1
        Case Candidate(checks, 2), Candidate(checks, 3)
            selected = 7
        Case Else
            selected = -9
    End Select
    Return reads * 100 + checks * 10 + selected
End Sub
```

**Explicación de los parámetros y la ejecución:**

ReadMode incrementa reads ByRef y devuelve 2 una vez. Candidate incrementa checks y devuelve value. El candidato 1 no coincide, 2 sí y 3 se omite. selected vale 7; Main devuelve 1*100+2*10+7=127 sin acceder al juego.

### 3. Salir de una selección anidada

```vb
# route contiene harvest y la primera rama pone trace=1. El Case 2 interno ejecuta Exit Select, omite trace=99 y Finally añade 2. La rama exterior añade 3: resultado 123. Su Case Else se omite. Otra cadena en route devuelve -1.
Option Explicit On
Sub Main()
    Dim route = "harvest"
    Dim trace = 0
    Select Case route
        Case "harvest", "loot"
            trace = 1
            Select Case 2
                Case 2
                    Try
                        Exit Select
                        trace = 99
                    Finally
                        trace = trace * 10 + 2
                    End Try
            End Select
            trace = trace * 10 + 3
        Case Else
            trace = -1
    End Select
    Return trace
End Sub
```

**Explicación de los parámetros y la ejecución:**

route contiene harvest y la primera rama pone trace=1. El Case 2 interno ejecuta Exit Select, omite trace=99 y Finally añade 2. La rama exterior añade 3: resultado 123. Su Case Else se omite. Otra cadena en route devuelve -1.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: selectStatement / caseClause / caseTest / exitSelect
Analysis/LoopStructureValidator.cs: VisitSelectStatement / VisitExitSelect / VisitCodeBlock
Runtime/Instructions/Generator.cs: Generate(SelectStatementContext)
Runtime/Instructions/SelectInstruction.cs: SelectInstruction / CaseInstruction
Runtime/Interpreter.cs: CaseMatches / ResumeNextAddress / Transfer
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/select-case-statement
-->
