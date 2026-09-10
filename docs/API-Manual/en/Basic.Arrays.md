# DIM / REDIM / PRESERVE

ClassicUO • Basic

<!-- yoko-manual: 1 -->
<!-- yoko-language-guide: 1 -->
<!-- yoko-locale: en -->

DIM creates a dynamic array; REDIM replaces its storage. Add PRESERVE to copy values at overlapping indices. Dimensions specify inclusive upper bounds, not item counts. Initialize elements before reading them.

## Exact syntax

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

## Parameters

- `name` — name: array variable. DIM declares it; REDIM writes an existing binding. Reading and writing elements uses square brackets: items[i], grid[x][y].
- `upper` — upper: expression converted to Integer, evaluated once from left to right. DIM items[2] creates three slots, 0..2. -1 creates an empty dimension; smaller bounds and an overflowing length are errors. Memory still limits practical sizes.
- `PRESERVE` — PRESERVE: optional on REDIM. Copies overlapping indices recursively; shrinking discards values outside the new bounds. Omit it to get uninitialized slots.
- `AS type` — AS type: accepted on DIM array declarations as an annotation; it does not type, initialize or coerce array elements. Arrays may contain different value kinds.

## Returns

DIM and REDIM return no value (Unit). items[i] returns the stored value with its actual kind: Integer, Decimal, String, Array or Object. An uninitialized slot raises an error instead of returning zero or FALSE. GetArrayLength(array) returns the outer length as Integer; non-arrays return 0.

## Behavior

- Parentheses are accepted in declarations: DIM grid(1, 2) means grid[1][2], with 2 rows of 3 slots. Functions in bounds are preserved. Access still uses grid[1][2]; parentheses in an expression mean a function call.
- Normal assignment and ByVal parameter passing copy an array reference, not its elements. Mutating a shared slot is visible through aliases. REDIM binds a new array; aliases retain the old one. PRESERVE copies matching nested array coordinates, not an unrestricted deep clone of objects.
- Only zero-based dimensions are supported. Inline DIM/REDIM initializers such as DIM items[2]=5 are rejected with SC014; assign each slot separately. Invalid indices and reads of missing/uninitialized elements raise catchable errors.
- This is the project’s Basic dialect. Its dynamic element kinds and multidimensional PRESERVE differ from VB.NET typed arrays. A Boolean stored in an element uses 1/0; an arbitrary numeric element or array length is not a Boolean flag.
- RETURN array returns the array reference; its storage survives the creating function. Assigning the result to another variable does not copy elements. A shared helper can therefore create an array for a Module field. Separate script runs create fresh arrays when DIM executes again.

## Examples

### 1. Sum initialized elements

```vb
# Abs(-2) evaluates to upper bound 2, so Main creates 3 slots and writes 2, 4, 6. Sum receives their shared reference ByVal, loops from 0 to GetArrayLength(items)-1 and returns 12. The helper reads elements without changing them; it also handles an empty array.
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

**Parameter and execution notes:**

Abs(-2) evaluates to upper bound 2, so Main creates 3 slots and writes 2, 4, 6. Sum receives their shared reference ByVal, loops from 0 to GetArrayLength(items)-1 and returns 12. The helper reads elements without changing them; it also handles an empty array.

### 2. Grow and keep contents

```vb
# values initially contains 7 and 8. REDIM PRESERVE values(2) creates 3 slots and copies indices 0 and 1. The new slot 2 must be assigned 9. Main returns 7*100+8*10+9=789.
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

**Parameter and execution notes:**

values initially contains 7 and 8. REDIM PRESERVE values(2) creates 3 slots and copies indices 0 and 1. The new slot 2 must be assigned 9. Main returns 7*100+8*10+9=789.

### 3. Observe aliases and new storage

```vb
# grid has two rows of two slots. alias references the same array, so alias[0][1]=9 changes grid too. PRESERVE grows grid to three rows, copies 9 and leaves alias at two rows. Main returns "9:3:2": preserved value, new outer length, old alias length.
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

**Parameter and execution notes:**

grid has two rows of two slots. alias references the same array, so alias[0][1]=9 changes grid too. PRESERVE grows grid to three rows, copies 9 and leaves alias at two rows. Main returns "9:3:2": preserved value, new outer length, old alias length.

<!-- implementation references (not callable script procedures):
Runtime/BasicSyntaxPreprocessor.cs: NormalizeDim / NormalizeArrayDeclarator
Analysis/ArrayDeclarationVisitor.cs: VisitDimDef
Runtime/Interpreter.cs: VisitDimDef / VisitRedim / VisitIndexedSymbol
Runtime/SemanticScope.cs: CreateArray / CopyArray / GetDim / SetDim
https://learn.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/redim-statement
-->
