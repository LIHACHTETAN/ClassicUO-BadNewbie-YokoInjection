# UO.FindAnyType

ClassicUO • Runtime API • `UO.FindAnyType.md`

Ищет ближайшего загруженного ПЕРСОНАЖА (mobile) по одной или нескольким body/graphic. Предметы, золото и содержимое контейнеров эта реализация не перебирает. Возвращает serial, либо 0 при отсутствии результата. Принимает от 2 до 32 аргументов: distance и до 31 значения type; поддерживается объединённая маска в строке/массиве. Учитываются расстояние и Ignore, результаты сортируются по расстоянию и serial; свой персонаж не исключается автоматически. Это не массив результатов.

## Точный синтаксис / Registered signatures

```text
UO.FindAnyType(distance:Any, type:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any, type20:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any, type20:Any, type21:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any, type20:Any, type21:Any, type22:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any, type20:Any, type21:Any, type22:Any, type23:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any, type20:Any, type21:Any, type22:Any, type23:Any, type24:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any, type20:Any, type21:Any, type22:Any, type23:Any, type24:Any, type25:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any, type20:Any, type21:Any, type22:Any, type23:Any, type24:Any, type25:Any, type26:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any, type20:Any, type21:Any, type22:Any, type23:Any, type24:Any, type25:Any, type26:Any, type27:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any, type20:Any, type21:Any, type22:Any, type23:Any, type24:Any, type25:Any, type26:Any, type27:Any, type28:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any, type20:Any, type21:Any, type22:Any, type23:Any, type24:Any, type25:Any, type26:Any, type27:Any, type28:Any, type29:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any, type20:Any, type21:Any, type22:Any, type23:Any, type24:Any, type25:Any, type26:Any, type27:Any, type28:Any, type29:Any, type30:Any) -> Integer
UO.FindAnyType(distance:Any, type:Any, type2:Any, type3:Any, type4:Any, type5:Any, type6:Any, type7:Any, type8:Any, type9:Any, type10:Any, type11:Any, type12:Any, type13:Any, type14:Any, type15:Any, type16:Any, type17:Any, type18:Any, type19:Any, type20:Any, type21:Any, type22:Any, type23:Any, type24:Any, type25:Any, type26:Any, type27:Any, type28:Any, type29:Any, type30:Any, type31:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Поиск по одному body

```vb
SUB Main()
    VAR found = UO.FindAnyType(5, 0x0190)
    UO.Print(CStr(found))
END SUB
```

### Несколько body отдельными аргументами

```vb
SUB Main()
    VAR found = UO.FindAnyType(10, 0x0190, 0x0191)
    UO.Print(CStr(found))
END SUB
```

### Маска body через массив

```vb
SUB Main()
    DIM bodies(2)
    bodies[0] = 0x0190
    bodies[1] = 0x0191
    VAR found = UO.FindAnyType(5, bodies)
    UO.Print(CStr(found))
END SUB
```

### Расширенная перегрузка: 32 аргументов

```vb
SUB Main()
    VAR arg1 = 5 # distance
    VAR arg2 = 0x0190 # type
    VAR arg3 = 0x0191 # type2
    VAR arg4 = 0x0190 # type3
    VAR arg5 = 0x0191 # type4
    VAR arg6 = 0x0190 # type5
    VAR arg7 = 0x0191 # type6
    VAR arg8 = 0x0190 # type7
    VAR arg9 = 0x0191 # type8
    VAR arg10 = 0x0190 # type9
    VAR arg11 = 0x0191 # type10
    VAR arg12 = 0x0190 # type11
    VAR arg13 = 0x0191 # type12
    VAR arg14 = 0x0190 # type13
    VAR arg15 = 0x0191 # type14
    VAR arg16 = 0x0190 # type15
    VAR arg17 = 0x0191 # type16
    VAR arg18 = 0x0190 # type17
    VAR arg19 = 0x0191 # type18
    VAR arg20 = 0x0190 # type19
    VAR arg21 = 0x0191 # type20
    VAR arg22 = 0x0190 # type21
    VAR arg23 = 0x0191 # type22
    VAR arg24 = 0x0190 # type23
    VAR arg25 = 0x0191 # type24
    VAR arg26 = 0x0190 # type25
    VAR arg27 = 0x0191 # type26
    VAR arg28 = 0x0190 # type27
    VAR arg29 = 0x0191 # type28
    VAR arg30 = 0x0190 # type29
    VAR arg31 = 0x0191 # type30
    VAR arg32 = 0x0190 # type31
    VAR result = UO.FindAnyType(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28, arg29, arg30, arg31, arg32)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 5 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 6 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 7 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 8 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 9 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 10 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 11 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 12 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 13 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 14 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 15 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 16 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 17 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 18 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 19 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 20 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 21 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 22 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 23 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 24 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 25 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 26 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 27 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 28 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 29 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 30 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 31 аргументов

```vb
SUB Main()
    VAR result = UO.FindAnyType(5, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191, 0x0190, 0x0191)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 5 # distance
    VAR arg2 = 0x0190 # type
    VAR result = UO.FindAnyType(arg1, arg2)
    # Пример порога; выберите подходящий смыслу команды.
    IF result > 0 THEN
        UO.Print(CStr(result))
    END IF
END SUB
```

### Результат через собственную функцию

```vb
FUNCTION ReadResult()
    VAR arg1 = 5 # distance
    VAR arg2 = 0x0190 # type
    VAR result = UO.FindAnyType(arg1, arg2)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.<RegisterCompactSearchApi>b__351_8`
