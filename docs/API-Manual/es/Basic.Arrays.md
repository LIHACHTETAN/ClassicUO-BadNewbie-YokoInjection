# DIM / REDIM / PRESERVE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: es -->

DIM crea una matriz dinámica; REDIM sustituye su almacenamiento. PRESERVE copia valores en índices comunes. Las dimensiones indican límites superiores incluidos, no cantidades. Inicialice las celdas antes de leerlas.

## Sintaxis exacta

```text
DIM name[upper]
DIM name(upper) AS type
DIM grid[xUpper][yUpper]
DIM grid(xUpper, yUpper)
REDIM name[upper]
REDIM PRESERVE name[upper]
name[index] = value
GetArrayLength(name)
```

## Parámetros

- `name` — name: variable de matriz. DIM la declara; REDIM reemplaza el valor de una variable existente. Acceso mediante items[i], grid[x][y].
- `upper` — upper: expresión convertida a Integer, evaluada una vez de izquierda a derecha. DIM items[2] crea tres celdas 0..2. -1 crea una dimensión vacía; límites menores y desbordamientos de longitud son errores. La memoria limita el tamaño práctico.
- `PRESERVE` — PRESERVE: opcional tras REDIM. Copia recursivamente los índices comunes; reducir elimina valores fuera de los límites nuevos. Sin él, las celdas no están inicializadas.
- `AS type` — AS type: anotación DIM admitida que no tipa, inicializa ni convierte elementos. Pueden coexistir valores de tipos distintos.

## Devuelve

DIM y REDIM no devuelven valores (Unit). items[i] devuelve el valor con su tipo real: Integer, Decimal, String, Array u Object. Leer una celda no inicializada produce un error, no 0 ni FALSE. GetArrayLength(array) devuelve la longitud exterior como Integer; para otros valores devuelve 0.

## Comportamiento

- DIM grid(1, 2) equivale a grid[1][2], dos filas de tres celdas. Se conservan las funciones en los límites. Acceda con grid[1][2]; los paréntesis en una expresión indican una llamada.
- La asignación y ByVal copian la referencia, no los elementos. Los alias ven cambios en celdas compartidas. REDIM enlaza una matriz nueva; los alias mantienen la anterior. PRESERVE copia coordenadas comunes de matrices anidadas, sin clonar objetos arbitrarios por completo.
- Los índices empiezan en cero. DIM items[2]=5 y los inicializadores REDIM se rechazan con SC014; asigne cada celda por separado. Índices inválidos y lecturas no inicializadas producen errores capturables.
- Este dialecto difiere de las matrices tipadas de VB.NET por sus tipos dinámicos y PRESERVE multidimensional. Un booleano almacenado usa 1/0; un número cualquiera o una longitud no es un indicador de éxito.
- RETURN array devuelve la referencia al array; sus datos permanecen tras finalizar la función creadora. Asignar el resultado no copia elementos. Una función compartida puede crear un array para un campo Module. Ejecuciones independientes crean arrays nuevos al ejecutar DIM de nuevo.

## Ejemplos

### 1. Sumar elementos

```vb
# Abs(-2) da límite 2: Main crea 3 celdas con 2, 4, 6. Sum recibe la referencia ByVal, recorre 0..GetArrayLength(items)-1 y devuelve 12. La función completa no modifica elementos y acepta matrices vacías.
Option Explicit On
FUNCTION Sum(ByVal items)
    VAR total = 0
    VAR i = 0
    FOR i = 0 TO GetArrayLength(items) - 1
        total += items[i]
    NEXT
    RETURN total
END FUNCTION
SUB Main()
    DIM items(Abs(-2))
    items[0] = 2
    items[1] = 4
    items[2] = 6
    RETURN Sum(items)
END SUB
```

**Explicación de los parámetros y la ejecución:**

Abs(-2) da límite 2: Main crea 3 celdas con 2, 4, 6. Sum recibe la referencia ByVal, recorre 0..GetArrayLength(items)-1 y devuelve 12. La función completa no modifica elementos y acepta matrices vacías.

### 2. Ampliar conservando

```vb
# values contiene 7 y 8. REDIM PRESERVE values(2) crea 3 celdas y copia índices 0 y 1. Inicialice la celda nueva 2 con 9. Main devuelve 7*100+8*10+9=789.
Option Explicit On
SUB Main()
    DIM values[1]
    values[0] = 7
    values[1] = 8
    REDIM PRESERVE values(2)
    values[2] = 9
    RETURN values[0] * 100 + values[1] * 10 + values[2]
END SUB
```

**Explicación de los parámetros y la ejecución:**

values contiene 7 y 8. REDIM PRESERVE values(2) crea 3 celdas y copia índices 0 y 1. Inicialice la celda nueva 2 con 9. Main devuelve 7*100+8*10+9=789.

### 3. Observar alias

```vb
# grid tiene dos filas de dos celdas. alias comparte la matriz: alias[0][1]=9 cambia también grid. PRESERVE amplía grid a tres filas y conserva 9; alias mantiene dos filas. "9:3:2" indica valor, nueva longitud exterior y longitud del alias antiguo.
Option Explicit On
SUB Main()
    DIM grid[1][1]
    grid[0][1] = 4
    VAR alias = grid
    alias[0][1] = 9
    REDIM PRESERVE grid[2][1]
    RETURN CStr(grid[0][1]) + ":" + CStr(GetArrayLength(grid)) + ":" + CStr(GetArrayLength(alias))
END SUB
```

**Explicación de los parámetros y la ejecución:**

grid tiene dos filas de dos celdas. alias comparte la matriz: alias[0][1]=9 cambia también grid. PRESERVE amplía grid a tres filas y conserva 9; alias mantiene dos filas. "9:3:2" indica valor, nueva longitud exterior y longitud del alias antiguo.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim / NormalizeArrayDeclarator
Analysis/ArrayDeclarationVisitor.cs: VisitDimDef
Runtime/Interpreter.cs: VisitDimDef / VisitRedim / VisitIndexedSymbol
Runtime/SemanticScope.cs: CreateArray / CopyArray / GetDim / SetDim
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/redim-statement
-->
