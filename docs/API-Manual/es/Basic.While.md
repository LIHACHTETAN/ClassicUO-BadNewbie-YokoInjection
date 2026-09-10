# While / Wend / Exit While / Break

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

While comprueba antes de cada pasada y repite mientras la condición sea verdadera. Este motor cierra con Wend; End While de VB.NET no está admitido.

## Sintaxis exacta

```text
While condition
    statements
Wend
Continue While
Exit While
Break
```

## Parámetros

- `condition` — Expresión reevaluada en cada comprobación, incluidas primera y última. Usa comparación o Boolean numérico: 0/False termina, 1/True y otros números distintos de cero continúan. El texto no se interpreta como Boolean.
- `statements` — Instrucciones que realizan trabajo y hacen avanzar la condición. Si la primera comprobación es falsa, se omite todo el cuerpo.
- `Wend / exit` — Wend vuelve a comprobar. Continue While repite la comprobación; Exit While sale del While más cercano incluso cruzando un bucle interno de otro tipo. Break sale del bucle más interno de cualquier tipo.

## Devuelve

While, Wend, Exit While y Break no devuelven valores. RETURN en el cuerpo termina todo el procedimiento/función. Los ejemplos devuelven Integer 6,1,406. El resultado de búsqueda 1 es un índice, no una señal Boolean.

## Comportamiento

- Secuencia: comprobar, ejecutar el cuerpo, volver a comprobar. No guarda un límite numérico ni incrementa automáticamente un contador.
- Programa explícitamente el avance. Para consultar el juego periódicamente añade un Wait adecuado y un plazo: While no espera ni caduca por sí solo. Pausa y parada permanecen disponibles.
- Continue y salida ejecutan los Finally de los Try abandonados. Cabecera, instrucciones y Wend van en líneas separadas dentro de un procedimiento o función.

## Ejemplos

### 1. Suma de dígitos

```vb
# DigitSum recibe number=123 ByVal. MOD 10 lee el último dígito y Fix(number/10) lo elimina: 123→12→1→0. total=3+2+1=6. La comprobación final falsa termina; Main recibe 6. Con 0 no habría pasadas y devolvería 0.
Option Explicit On
Function DigitSum(ByVal number)
    Var total = 0
    While number > 0
        total += number MOD 10
        number = Fix(number / 10)
    Wend
    Return total
End Function
Sub Main()
    Return DigitSum(123)
End Sub
```

**Explicación de los parámetros y la ejecución:**

DigitSum recibe number=123 ByVal. MOD 10 lee el último dígito y Fix(number/10) lo elimina: 123→12→1→0. total=3+2+1=6. La comprobación final falsa termina; Main recibe 6. Con 0 no habría pasadas y devolvería 0.

### 2. Primera coincidencia

```vb
# FirstAbove recibe values=[4,7,9], threshold=6. El límite protege values[index]. En index=1, 7>6 guarda found=1 y Exit While termina. Sin coincidencias queda -1. Main devuelve el índice 1 contando desde cero.
Option Explicit On
Function FirstAbove(ByVal values, ByVal threshold)
    Var index = 0
    Var found = -1
    While index < GetArrayLength(values)
        If values[index] > threshold Then
            found = index
            Exit While
        End If
        index += 1
    Wend
    Return found
End Function
Sub Main()
    Dim values[2]
    values[0] = 4
    values[1] = 7
    values[2] = 9
    Return FirstAbove(values, 6)
End Sub
```

**Explicación de los parámetros y la ejecución:**

FirstAbove recibe values=[4,7,9], threshold=6. El límite protege values[index]. En index=1, 7>6 guarda found=1 y Exit While termina. Sin coincidencias queda -1. Main devuelve el índice 1 contando desde cero.

### 3. Contar comprobaciones

```vb
# CanContinue recibe checks ByRef, index y limit=3 ByVal, incrementa checks y devuelve index<limit como 1/0. Se comprueba con index=0,1,2,3: cuatro llamadas para tres pasadas. total=6; Main devuelve 406.
Option Explicit On
Function CanContinue(ByRef checks, ByVal index, ByVal limit)
    checks += 1
    Return index < limit
End Function
Sub Main()
    Var checks = 0
    Var index = 0
    Var total = 0
    While CanContinue(checks, index, 3)
        index += 1
        total += index
    Wend
    Return checks * 100 + total
End Sub
```

**Explicación de los parámetros y la ejecución:**

CanContinue recibe checks ByRef, index y limit=3 ByVal, incrementa checks y devuelve index<limit como 1/0. Se comprueba con index=0,1,2,3: cuatro llamadas para tres pasadas. total=6; Main devuelve 406.

<!-- implementation references (not callable script procedures):
Parsing/injection.g4
Analysis/LoopStructureValidator.cs
Runtime/Instructions/Generator.cs: Generate(WhileContext)
Runtime/Interpreter.cs: WhileInstruction
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/while-end-while-statement
-->
