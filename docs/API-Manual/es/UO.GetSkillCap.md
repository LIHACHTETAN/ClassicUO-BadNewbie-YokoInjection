# UO.GetSkillCap

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee el límite de habilidad recibido del servidor.

## Sintaxis exacta

```text
UO.GetSkillCap(SkillName:Any) -> Decimal
```

## Parámetros

- `SkillName` — Habilidad obligatoria: nombre de los datos del cliente, como "Mining" o "Animal Lore", o índice decimal 0..Skills.Length−1 como número o cadena. Ignora mayúsculas, quita espacios exteriores y cambia _ por un espacio. No es un ID de objeto ni un índice desde 1. Las cadenas numéricas siempre indican un índice.

## Devuelve

Decimal (Double) — puntos de habilidad en décimas, por ejemplo 95,1 en lugar de 951. El campo CapFixed se divide directamente entre 10 en Double. Cero significa habilidad cero o personaje/habilidad ausente. No es Boolean. Las antiguas SkillVal/BaseVal usan otra escala; no mezcle las familias.

## Comportamiento

- Invoke lee datos existentes en el hilo del juego sin enviar paquetes. No usa ni entrena la habilidad. Dos consultas son instantáneas distintas.
- Habilidad obligatoria: nombre de los datos del cliente, como "Mining" o "Animal Lore", o índice decimal 0..Skills.Length−1 como número o cadena. Ignora mayúsculas, quita espacios exteriores y cambia _ por un espacio. No es un ID de objeto ni un índice desde 1. Las cadenas numéricas siempre indican un índice.
- ExecuteStealthCompatibility elige la rama. Text lee el selector de habilidad; Arg lee números y modos. Un argumento no convertible puede producir un error de conversión.

### Funciones internas: de la llamada al resultado

Estas son las etapas internas reales de C#. ReadValue es una función auxiliar completamente definida en el ejemplo, no un comando integrado oculto.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility elige la rama. Text lee el selector de habilidad; Arg lee números y modos. Un argumento no convertible puede producir un error de conversión.

Decimal (Double) — puntos de habilidad en décimas, por ejemplo 95,1 en lugar de 951. El campo CapFixed se divide directamente entre 10 en Double. Cero significa habilidad cero o personaje/habilidad ausente. No es Boolean. Las antiguas SkillVal/BaseVal usan otra escala; no mezcle las familias.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke lee en el hilo del juego; un hilo de trabajo espera el procesamiento del gestor. Cancelar el script interrumpe esa espera. No añade demoras ni consultas de red.

Invoke lee datos existentes en el hilo del juego sin enviar paquetes. No usa ni entrena la habilidad. Dos consultas son instantáneas distintas.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 3. FindSkillUnsafe

FindSkillUnsafe comprueba primero el índice decimal y sus límites; si no es numérico, normaliza el nombre y compara exactamente Skill.Name sin distinguir mayúsculas. Un nombre desconocido produce null; no abre objetivo.

Una habilidad desconocida o un personaje ausente devuelve −1.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `FindSkillUnsafe`.

#### 4. GetSkillValue

GetSkillValue elige BaseFixed, ValueFixed o CapFixed y divide las décimas enteras entre 10d, sin redondeo intermedio a Single.

Decimal (Double) — puntos de habilidad en décimas, por ejemplo 95,1 en lugar de 951. El campo CapFixed se divide directamente entre 10 en Double. Cero significa habilidad cero o personaje/habilidad ausente. No es Boolean. Las antiguas SkillVal/BaseVal usan otra escala; no mezcle las familias.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `GetSkillValue`.

Invoke lee datos existentes en el hilo del juego sin enviar paquetes. No usa ni entrena la habilidad. Dos consultas son instantáneas distintas.


## Ejemplos

### Leer y mostrar

```vb
# Leer y mostrar
#
# Lee el límite de habilidad recibido del servidor.
#
# Decimal (Double) — puntos de habilidad en décimas, por ejemplo 95,1 en lugar de 951. El campo
# CapFixed se divide directamente entre 10 en Double. Cero significa habilidad cero o
# personaje/habilidad ausente. No es Boolean. Las antiguas SkillVal/BaseVal usan otra escala; no
# mezcle las familias.

SUB Main()
    # El ejemplo fija selector y, para escribir, mode. La primera línea elige la habilidad por
    # nombre o el atributo por número. Print solo muestra el resultado.

    VAR selector = 'Mining'
    VAR value = UO.GetSkillCap(selector)
    UO.Print(CStr(value))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El ejemplo fija selector y, para escribir, mode. La primera línea elige la habilidad por nombre o el atributo por número. Print solo muestra el resultado.

### Usar en una condición o comparación

```vb
# Usar en una condición o comparación
#
# Lee el límite de habilidad recibido del servidor.
#
# Decimal (Double) — puntos de habilidad en décimas, por ejemplo 95,1 en lugar de 951. El campo
# CapFixed se divide directamente entre 10 en Double. Cero significa habilidad cero o
# personaje/habilidad ausente. No es Boolean. Las antiguas SkillVal/BaseVal usan otra escala; no
# mezcle las familias.

SUB Main()
    # El umbral 95.1 y los modos 0/1/2 son ajustes de ejemplo. Compruebe −1 antes de cambiar el
    # modo. Leer después de escribir muestra la copia local sin esperar al servidor.

    IF UO.GetSkillLockState('Mining') >= 0 THEN
        VAR value = UO.GetSkillCap('Mining')
        IF value >= 95.1 THEN
            UO.Print('Value >= 95.1: ' + CStr(value))
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
# Lee el límite de habilidad recibido del servidor.
#
# Decimal (Double) — puntos de habilidad en décimas, por ejemplo 95,1 en lugar de 951. El campo
# CapFixed se divide directamente entre 10 en Double. Cero significa habilidad cero o
# personaje/habilidad ausente. No es Boolean. Las antiguas SkillVal/BaseVal usan otra escala; no
# mezcle las familias.

SUB Main()
    # La función completa sigue a Main. selector elige habilidad/atributo; mode indica el modo de
    # escritura. ReadValue/ReadMode devuelven el número original; ApplyMode comprueba argumentos,
    # actúa y no devuelve valor. WAIT(1000) separa dos lecturas.

    VAR before = ReadValue('Animal_Lore')
    WAIT(1000)
    VAR after = ReadValue('Animal Lore')
    UO.Print(CStr(after - before))
END SUB

SUB ReadValue(selector)
    RETURN UO.GetSkillCap(selector)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- La función completa sigue a Main. selector elige habilidad/atributo; mode indica el modo de escritura. ReadValue/ReadMode devuelven el número original; ApplyMode comprueba argumentos, actúa y no devuelve valor. WAIT(1000) separa dos lecturas.
