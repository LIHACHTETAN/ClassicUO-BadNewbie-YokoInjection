# UO.GetStaticArt

ClassicUO • Runtime API • `UO.GetStaticArt.md`

## Точный синтаксис / Registered signatures

```text
UO.GetStaticArt(ObjType:Any, Hue:Any) -> Any
```

Порядок аргументов соответствует строкам выше. `Unit` означает отсутствие возвращаемого значения. `Any` — значение BASIC с преобразованием при вызове. Имена нечувствительны к регистру.

## `UO.GetStaticArt`

### Compatibility description

> Historical Stealth/Pascal reference text. Current Basic signatures and return contracts below are authoritative when behavior differs.

Возвращает объект TBitmap для статик-арта с указанным ObjType и Hue . Если Hue = 0 , арт берётся с оригинальными цветами. Возвращает nil (Pascal) или пустой буфер (Python), если персонаж не подключён или файлы UO Data не загружены. В Python метод называется GetStaticArtBitmap и возвращает содержимое BMP-файла в виде list[int] — BMP используется как единственный формат, гарантированно совместимый с Delphi TBitmap.

### Current Basic signatures / Return

- `UO.GetStaticArt(ObjType:Integer, Hue:Integer) -> Array`
  - **Return type:** `Array`
  - **Return contract:** Byte Array containing a complete 24-bit BMP image; empty array means no decodable art.
  - **Runtime route:** `DISPATCH -> InjectionApiUO.ExecuteStealthCompatibility["GetStaticArt"]` → `BRIDGE CONTRACT -> IApiBridge.GetStaticArt`

**Pascal compatibility signature:** `function GetStaticArt(ObjType: Cardinal; Hue: Word): TBitmap;`

### Parameters

- `ObjType` — Item/mobile/tile type (graphic/body ID). -1/0xFFFF may mean wildcard only for commands that document it.
- `Hue` — Hue/color filter. -1 commonly means any hue where the overload supports wildcard filtering.

### Accepted values / constants

- `ObjType` — Decimal or 0x-prefixed graphic/body/tile ID; -1/0xFFFF is wildcard only where Behavior explicitly allows it.
- `Hue` — Decimal or 0x-prefixed hue; -1 is any/default only where Behavior explicitly allows it.

### Defaults / omitted arguments

No parameters are optional unless the signature/Behavior explicitly states otherwise.

### Behavior

Loads the requested static art from the active ClassicUO asset loaders (MUL/UOP), applies hue/partial-hue rules and encodes a complete 24-bit BMP byte array.

### Notes / limitations

Requires decodable art assets in the active ClassicUO data source. Empty Array means art is unavailable/undecodable.

### Examples

```basic
SUB Main()
    VAR result = UO.GetStaticArt(0x0190, -1)
END SUB
```

---

## Варианты использования

Это отдельные сценарии. Подставьте свои serial, пути и координаты; серверные действия зависят от текущего состояния игры.

### Прямой вызов

```vb
SUB Main()
    VAR result = UO.GetStaticArt(1, -1)
    UO.Print(CStr(result))
END SUB
```

### Явные аргументы и сохранение результата

```vb
SUB Main()
    VAR arg1 = 1 # ObjType
    VAR arg2 = -1 # Hue
    VAR result = UO.GetStaticArt(arg1, arg2)
    UO.Print(CStr(result))
END SUB
```

### Получение результата внутри процедуры

```vb
SUB ReadResult()
    VAR arg1 = 1 # ObjType
    VAR arg2 = -1 # Hue
    VAR result = UO.GetStaticArt(arg1, arg2)
    UO.Print(CStr(result))
END SUB

SUB Main()
    ReadResult()
END SUB
```

## Реализация для проверки поведения

- `InjectionScript.Runtime.InjectionApiUO+<>c__DisplayClass41_0.<RegisterStealthCompatibility>b__0`
