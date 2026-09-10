# UO.GetSkillLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee el modo local de avance de la habilidad.

## Sintaxis exacta

```text
UO.GetSkillLockState(SkillName:Any) -> Integer
```

## Parámetros

- `SkillName` — Habilidad obligatoria: nombre de los datos del cliente, como "Mining" o "Animal Lore", o índice decimal 0..Skills.Length−1 como número o cadena. Ignora mayúsculas, quita espacios exteriores y cambia _ por un espacio. No es un ID de objeto ni un índice desde 1. Las cadenas numéricas siempre indican un índice.

## Devuelve

Integer: 0 — aumentar, 1 — disminuir, 2 — bloquear. Código de modo, no true/false. Una habilidad desconocida o un personaje ausente devuelve −1.

## Comportamiento

- Invoke lee datos existentes en el hilo del juego sin enviar paquetes. No usa ni entrena la habilidad. Dos consultas son instantáneas distintas.
- Habilidad obligatoria: nombre de los datos del cliente, como "Mining" o "Animal Lore", o índice decimal 0..Skills.Length−1 como número o cadena. Ignora mayúsculas, quita espacios exteriores y cambia _ por un espacio. No es un ID de objeto ni un índice desde 1. Las cadenas numéricas siempre indican un índice.
- ExecuteStealthCompatibility elige la rama. Text lee el selector de habilidad; Arg lee números y modos. Un argumento no convertible puede producir un error de conversión.

### Funciones internas: de la llamada al resultado

Estas son las etapas internas reales de C#. ReadMode es una función auxiliar completamente definida en el ejemplo, no un comando integrado oculto.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility elige la rama. Text lee el selector de habilidad; Arg lee números y modos. Un argumento no convertible puede producir un error de conversión.

Integer: 0 — aumentar, 1 — disminuir, 2 — bloquear. Código de modo, no true/false. Una habilidad desconocida o un personaje ausente devuelve −1.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke lee en el hilo del juego; un hilo de trabajo espera el procesamiento del gestor. Cancelar el script interrumpe esa espera. No añade demoras ni consultas de red.

Invoke lee datos existentes en el hilo del juego sin enviar paquetes. No usa ni entrena la habilidad. Dos consultas son instantáneas distintas.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 3. FindSkillUnsafe

FindSkillUnsafe comprueba primero el índice decimal y sus límites; si no es numérico, normaliza el nombre y compara exactamente Skill.Name sin distinguir mayúsculas. Un nombre desconocido produce null; no abre objetivo.

Una habilidad desconocida o un personaje ausente devuelve −1.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `FindSkillUnsafe`.

#### 4. GetSkillLockState

Lee el modo local de avance de la habilidad.

Integer: 0 — aumentar, 1 — disminuir, 2 — bloquear. Código de modo, no true/false. Una habilidad desconocida o un personaje ausente devuelve −1.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `GetSkillLockState`.

Invoke lee datos existentes en el hilo del juego sin enviar paquetes. No usa ni entrena la habilidad. Dos consultas son instantáneas distintas.


## Ejemplos

### Leer y mostrar

```vb
# Leer y mostrar
#
# Lee el modo local de avance de la habilidad.
#
# Integer: 0 — aumentar, 1 — disminuir, 2 — bloquear. Código de modo, no true/false. Una
# habilidad desconocida o un personaje ausente devuelve −1.

SUB Main()
    # El ejemplo fija selector y, para escribir, mode. La primera línea elige la habilidad por
    # nombre o el atributo por número. Print solo muestra el resultado.

    VAR selector = 'Mining'
    VAR mode = UO.GetSkillLockState(selector)
    UO.Print(CStr(mode))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El ejemplo fija selector y, para escribir, mode. La primera línea elige la habilidad por nombre o el atributo por número. Print solo muestra el resultado.

### Usar en una condición o comparación

```vb
# Usar en una condición o comparación
#
# Lee el modo local de avance de la habilidad.
#
# Integer: 0 — aumentar, 1 — disminuir, 2 — bloquear. Código de modo, no true/false. Una
# habilidad desconocida o un personaje ausente devuelve −1.

SUB Main()
    # El umbral 95.1 y los modos 0/1/2 son ajustes de ejemplo. Compruebe −1 antes de cambiar el
    # modo. Leer después de escribir muestra la copia local sin esperar al servidor.

    VAR mode = UO.GetSkillLockState('Mining')
    IF mode = 2 THEN
        UO.Print("Locked")
    ELSE
        IF mode = -1 THEN
            UO.Print("Unknown selector")
        ELSE
            UO.Print("Mode: " + CStr(mode))
        END IF
    END IF
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El umbral 95.1 y los modos 0/1/2 son ajustes de ejemplo. Compruebe −1 antes de cambiar el modo. Leer después de escribir muestra la copia local sin esperar al servidor.

### Función auxiliar completa

```vb
# Función auxiliar completa
#
# Lee el modo local de avance de la habilidad.
#
# Integer: 0 — aumentar, 1 — disminuir, 2 — bloquear. Código de modo, no true/false. Una
# habilidad desconocida o un personaje ausente devuelve −1.

SUB Main()
    # La función completa sigue a Main. selector elige habilidad/atributo; mode indica el modo de
    # escritura. ReadValue/ReadMode devuelven el número original; ApplyMode comprueba argumentos,
    # actúa y no devuelve valor. WAIT(1000) separa dos lecturas.

    VAR before = ReadMode('Mining')
    WAIT(1000)
    VAR after = ReadMode('Mining')
    UO.Print(CStr(before) + " -> " + CStr(after))
END SUB

SUB ReadMode(selector)
    RETURN UO.GetSkillLockState(selector)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- La función completa sigue a Main. selector elige habilidad/atributo; mode indica el modo de escritura. ReadValue/ReadMode devuelven el número original; ApplyMode comprueba argumentos, actúa y no devuelve valor. WAIT(1000) separa dos lecturas.
