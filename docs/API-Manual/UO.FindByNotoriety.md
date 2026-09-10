# UO.FindByNotoriety

ClassicUO • Runtime API • `UO.FindByNotoriety.md`

Ищет загруженного персонажа по расстоянию и маске notoriety. Возвращает serial или 0. Принимает от 2 до 32 аргументов: distance и до 31 значения notoriety. Маска может передаваться также строкой или массивом; применяются общие фильтры поиска.

## Точный синтаксис / Registered signatures

```text
UO.FindByNotoriety(distance:Any, notoriety:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any, notoriety20:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any, notoriety20:Any, notoriety21:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any, notoriety20:Any, notoriety21:Any, notoriety22:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any, notoriety20:Any, notoriety21:Any, notoriety22:Any, notoriety23:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any, notoriety20:Any, notoriety21:Any, notoriety22:Any, notoriety23:Any, notoriety24:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any, notoriety20:Any, notoriety21:Any, notoriety22:Any, notoriety23:Any, notoriety24:Any, notoriety25:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any, notoriety20:Any, notoriety21:Any, notoriety22:Any, notoriety23:Any, notoriety24:Any, notoriety25:Any, notoriety26:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any, notoriety20:Any, notoriety21:Any, notoriety22:Any, notoriety23:Any, notoriety24:Any, notoriety25:Any, notoriety26:Any, notoriety27:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any, notoriety20:Any, notoriety21:Any, notoriety22:Any, notoriety23:Any, notoriety24:Any, notoriety25:Any, notoriety26:Any, notoriety27:Any, notoriety28:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any, notoriety20:Any, notoriety21:Any, notoriety22:Any, notoriety23:Any, notoriety24:Any, notoriety25:Any, notoriety26:Any, notoriety27:Any, notoriety28:Any, notoriety29:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any, notoriety20:Any, notoriety21:Any, notoriety22:Any, notoriety23:Any, notoriety24:Any, notoriety25:Any, notoriety26:Any, notoriety27:Any, notoriety28:Any, notoriety29:Any, notoriety30:Any) -> Integer
UO.FindByNotoriety(distance:Any, notoriety:Any, notoriety2:Any, notoriety3:Any, notoriety4:Any, notoriety5:Any, notoriety6:Any, notoriety7:Any, notoriety8:Any, notoriety9:Any, notoriety10:Any, notoriety11:Any, notoriety12:Any, notoriety13:Any, notoriety14:Any, notoriety15:Any, notoriety16:Any, notoriety17:Any, notoriety18:Any, notoriety19:Any, notoriety20:Any, notoriety21:Any, notoriety22:Any, notoriety23:Any, notoriety24:Any, notoriety25:Any, notoriety26:Any, notoriety27:Any, notoriety28:Any, notoriety29:Any, notoriety30:Any, notoriety31:Any) -> Integer
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Одна репутация

```vb
SUB Main()
    VAR found = UO.FindByNotoriety(10, 6)
    UO.Print(CStr(found))
END SUB
```

### Несколько значений репутации

```vb
SUB Main()
    VAR found = UO.FindByNotoriety(10, 3, 6)
    UO.Print(CStr(found))
END SUB
```

### Проверить отсутствие результата

```vb
SUB Main()
    VAR found = UO.FindByNotoriety(5, 6)
    IF found = 0 THEN
        UO.Print('No matching mobile')
    ELSE
        UO.Info(found)
    END IF
END SUB
```

### Расширенная перегрузка: 32 аргументов

```vb
SUB Main()
    VAR arg1 = 5 # distance
    VAR arg2 = -1 # notoriety
    VAR arg3 = 3 # notoriety2
    VAR arg4 = 4 # notoriety3
    VAR arg5 = 5 # notoriety4
    VAR arg6 = 6 # notoriety5
    VAR arg7 = 7 # notoriety6
    VAR arg8 = 8 # notoriety7
    VAR arg9 = 9 # notoriety8
    VAR arg10 = 10 # notoriety9
    VAR arg11 = 11 # notoriety10
    VAR arg12 = 12 # notoriety11
    VAR arg13 = 13 # notoriety12
    VAR arg14 = 14 # notoriety13
    VAR arg15 = 15 # notoriety14
    VAR arg16 = 16 # notoriety15
    VAR arg17 = 17 # notoriety16
    VAR arg18 = 18 # notoriety17
    VAR arg19 = 19 # notoriety18
    VAR arg20 = 20 # notoriety19
    VAR arg21 = 21 # notoriety20
    VAR arg22 = 22 # notoriety21
    VAR arg23 = 23 # notoriety22
    VAR arg24 = 24 # notoriety23
    VAR arg25 = 25 # notoriety24
    VAR arg26 = 26 # notoriety25
    VAR arg27 = 27 # notoriety26
    VAR arg28 = 28 # notoriety27
    VAR arg29 = 29 # notoriety28
    VAR arg30 = 30 # notoriety29
    VAR arg31 = 31 # notoriety30
    VAR arg32 = 32 # notoriety31
    VAR result = UO.FindByNotoriety(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28, arg29, arg30, arg31, arg32)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 3 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 4 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 5 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 6 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 7 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 8 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 9 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 10 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 11 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 12 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 13 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 14 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 15 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 16 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 17 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 18 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 19 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 20 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 21 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 22 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 23 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 24 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 25 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 26 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 27 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 28 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 29 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 30 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
    UO.Print(CStr(result))
END SUB
```

### Перегрузка: 31 аргументов

```vb
SUB Main()
    VAR result = UO.FindByNotoriety(5, -1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
    UO.Print(CStr(result))
END SUB
```

### Условие по полученному числу

```vb
SUB Main()
    VAR arg1 = 5 # distance
    VAR arg2 = -1 # notoriety
    VAR result = UO.FindByNotoriety(arg1, arg2)
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
    VAR arg2 = -1 # notoriety
    VAR result = UO.FindByNotoriety(arg1, arg2)
    RETURN result
END FUNCTION

SUB Main()
    VAR answer = ReadResult()
    UO.Print(CStr(answer))
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO.<RegisterCompactSearchApi>b__351_6`
