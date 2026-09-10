# Continue For / Do / While

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

Continue omite el resto del cuerpo del bucle contenedor más próximo del tipo indicado. Continue For sirve para For y For Each, Continue Do para Do/Loop y Repeat/Until, Continue While para While/Wend.

## Sintaxis exacta

```text
Continue For
Continue Do
Continue While
```

## Parámetros

- `kind` — kind: For, Do o While obligatorio después de Continue, sin paréntesis. El bucle debe contener la instrucción en el mismo procedimiento. Un bucle interno de otro tipo no intercepta el salto.

## Devuelve

Continue no devuelve valores ni se usa en expresiones. No es TRUE/FALSE ni reinicia el procedimiento. La función puede devolver un resultado mediante RETURN; los ejemplos devuelven Integer 10, 3 y 34.

## Comportamiento

- For ejecuta NEXT, aplica STEP y comprueba el siguiente valor frente al límite; For Each obtiene el siguiente elemento. Al agotarse termina. No se repiten la inicialización ni la expresión de colección.
- Do comprueba otra vez su condición al inicio o, si está en Loop, al final. Repeat/Until usa UNTIL. Do/Loop incondicional continúa hasta salir o detenerse. While vuelve a comprobar WHILE. Continue Do no elige While/Wend.
- La preparación resuelve la dirección del bucle solicitado. Si no existe genera SC020 antes de inicializar, incluso sin Option Explicit. También comprueba nombres NEXT y cierres. Se conserva la forma antigua FOR/NEXT que cruza IF.
- Salir de TRY/CATCH ejecuta cada FINALLY atravesado una vez, de dentro hacia fuera. Si todo el bucle está dentro de TRY, ese FINALLY no se ejecuta en cada vuelta. RETURN o un error en FINALLY sustituye el salto pendiente.
- Continue no espera. Actualice la condición o use una espera apropiada al consultar repetidamente, para evitar bucles infinitos. Pausa y parada siguen activas. Se liberan enumeradores nativos abandonados y cada ejecución es independiente. Exit For/Do/While abandona el bucle.

## Ejemplos

### 1. Omitir elementos

```vb
# values contiene -2, 4, 0, 6. item<=0 activa Continue For para -2 y 0 y omite total+=item. Funciona también en For Each. SumPositive y Main devuelven Integer 10, la suma 4+6.
Option Explicit On
Function SumPositive(values)
    Var total = 0
    For Each item In values
        If item <= 0 Then
            Continue For
        End If
        total += item
    Next
    Return total
End Function
Sub Main()
    Dim values[3]
    values[0] = -2
    values[1] = 4
    values[2] = 0
    values[3] = 6
    Return SumPositive(values)
End Sub
```

**Explicación de los parámetros y la ejecución:**

values contiene -2, 4, 0, 6. item<=0 activa Continue For para -2 y 0 y omite total+=item. Funciona también en For Each. SumPositive y Main devuelven Integer 10, la suma 4+6.

### 2. Elegir el bucle exterior

```vb
# AdvanceTo recibe limit=3 y count comienza en 0. En While True, count aumenta y Continue Do salta al Do exterior. Se vuelve a comprobar su condición; count=3 termina y devuelve Integer 3.
Option Explicit On
Function AdvanceTo(limit)
    Var count = 0
    Do While count < limit
        While True
            count += 1
            Continue Do
        Wend
    Loop
    Return count
End Function
Sub Main()
    Return AdvanceTo(3)
End Sub
```

**Explicación de los parámetros y la ejecución:**

AdvanceTo recibe limit=3 y count comienza en 0. En While True, count aumenta y Continue Do salta al Do exterior. Se vuelve a comprobar su condición; count=3 termina y devuelve Integer 3.

### 3. Limpieza de una vuelta omitida

```vb
# Process recibe limit=3 y skip=2. i toma 1, 2, 3. La segunda vuelta omite total+=i, pero Finally aumenta cleanup tres veces. total=4 y cleanup=3; RETURN cleanup*10+total devuelve Integer 34.
Option Explicit On
Function Process(limit, skip)
    Var total = 0
    Var cleanup = 0
    For Var i = 1 To limit
        Try
            If i = skip Then
                Continue For
            End If
            total += i
        Finally
            cleanup += 1
        End Try
    Next i
    Return cleanup * 10 + total
End Function
Sub Main()
    Return Process(3, 2)
End Sub
```

**Explicación de los parámetros y la ejecución:**

Process recibe limit=3 y skip=2. i toma 1, 2, 3. La segunda vuelta omite total+=i, pero Finally aumenta cleanup tres veces. total=4 y cleanup=3; RETURN cleanup*10+total devuelve Integer 34.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4: continueLoop / doLoop
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: AddTransfer / EndBreakScope
Runtime/Interpreter.cs: Transfer / DeferReturn / TryHandleStructuredError
Runtime/ForScope.cs: HasNext / AdvanceEach
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/continue-statement
-->
