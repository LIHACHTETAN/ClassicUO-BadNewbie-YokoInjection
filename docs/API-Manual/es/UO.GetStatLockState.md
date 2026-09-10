# UO.GetStatLockState

ClassicUO • Runtime API

<!-- yoko-manual: 1 -->
<!-- yoko-locale: es -->

Lee el modo local de avance del atributo.

## Sintaxis exacta

```text
UO.GetStatLockState(statNum:Any) -> Integer
```

## Parámetros

- `statNum` — Número de atributo obligatorio: 0 — STR, 1 — DEX, 2 — INT. No es su valor actual ni un nombre textual.

## Devuelve

Integer: 0 — aumentar, 1 — disminuir, 2 — bloquear. Código de modo, no true/false. Un número fuera de 0..2 devuelve −1. Sin personaje, un número válido devuelve 0 por defecto; no confirma el estado del servidor.

## Comportamiento

- Invoke lee datos existentes en el hilo del juego sin enviar paquetes. No usa ni entrena la habilidad. Dos consultas son instantáneas distintas.
- Número de atributo obligatorio: 0 — STR, 1 — DEX, 2 — INT. No es su valor actual ni un nombre textual.
- ExecuteStealthCompatibility elige la rama. Text lee el selector de habilidad; Arg lee números y modos. Un argumento no convertible puede producir un error de conversión.

### Funciones internas: de la llamada al resultado

Estas son las etapas internas reales de C#. ReadMode es una función auxiliar completamente definida en el ejemplo, no un comando integrado oculto.

#### 1. ExecuteStealthCompatibility

ExecuteStealthCompatibility elige la rama. Text lee el selector de habilidad; Arg lee números y modos. Un argumento no convertible puede producir un error de conversión.

Integer: 0 — aumentar, 1 — disminuir, 2 — bloquear. Código de modo, no true/false. Un número fuera de 0..2 devuelve −1. Sin personaje, un número válido devuelve 0 por defecto; no confirma el estado del servidor.

Código del proyecto: `external/InjectionScript/src/InjectionScript/Runtime/InjectionApiUO.cs`; función `ExecuteStealthCompatibility`.

#### 2. Invoke

Invoke lee en el hilo del juego; un hilo de trabajo espera el procesamiento del gestor. Cancelar el script interrumpe esa espera. No añade demoras ni consultas de red.

Invoke lee datos existentes en el hilo del juego sin enviar paquetes. No usa ni entrena la habilidad. Dos consultas son instantáneas distintas.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `Invoke`.

#### 3. GetStatLockState

GetStatLockState/SetStatLockState eligen StrLock, DexLock o IntLock según 0/1/2. Un número desconocido lee −1; escribir comprueba ambos límites antes del envío.

Integer: 0 — aumentar, 1 — disminuir, 2 — bloquear. Código de modo, no true/false. Un número fuera de 0..2 devuelve −1. Sin personaje, un número válido devuelve 0 por defecto; no confirma el estado del servidor.

Código del proyecto: `src/ClassicUO.Client/Game/Managers/ClassicUOInjectionApiBridge.cs`; función `GetStatLockState`.

Invoke lee datos existentes en el hilo del juego sin enviar paquetes. No usa ni entrena la habilidad. Dos consultas son instantáneas distintas.


## Ejemplos

### Leer y mostrar

```vb
# Leer y mostrar
#
# Lee el modo local de avance del atributo.
#
# Integer: 0 — aumentar, 1 — disminuir, 2 — bloquear. Código de modo, no true/false. Un número
# fuera de 0..2 devuelve −1. Sin personaje, un número válido devuelve 0 por defecto; no confirma
# el estado del servidor.

SUB Main()
    # El ejemplo fija selector y, para escribir, mode. La primera línea elige la habilidad por
    # nombre o el atributo por número. Print solo muestra el resultado.

    VAR selector = 0
    VAR mode = UO.GetStatLockState(selector)
    UO.Print(CStr(mode))
END SUB
```

**Explicación de los parámetros y la ejecución:**

- El ejemplo fija selector y, para escribir, mode. La primera línea elige la habilidad por nombre o el atributo por número. Print solo muestra el resultado.

### Usar en una condición o comparación

```vb
# Usar en una condición o comparación
#
# Lee el modo local de avance del atributo.
#
# Integer: 0 — aumentar, 1 — disminuir, 2 — bloquear. Código de modo, no true/false. Un número
# fuera de 0..2 devuelve −1. Sin personaje, un número válido devuelve 0 por defecto; no confirma
# el estado del servidor.

SUB Main()
    # El umbral 95.1 y los modos 0/1/2 son ajustes de ejemplo. Compruebe −1 antes de cambiar el
    # modo. Leer después de escribir muestra la copia local sin esperar al servidor.

    VAR mode = UO.GetStatLockState(0)
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
# Lee el modo local de avance del atributo.
#
# Integer: 0 — aumentar, 1 — disminuir, 2 — bloquear. Código de modo, no true/false. Un número
# fuera de 0..2 devuelve −1. Sin personaje, un número válido devuelve 0 por defecto; no confirma
# el estado del servidor.

SUB Main()
    # La función completa sigue a Main. selector elige habilidad/atributo; mode indica el modo de
    # escritura. ReadValue/ReadMode devuelven el número original; ApplyMode comprueba argumentos,
    # actúa y no devuelve valor. WAIT(1000) separa dos lecturas.

    VAR before = ReadMode(0)
    WAIT(1000)
    VAR after = ReadMode(0)
    UO.Print(CStr(before) + " -> " + CStr(after))
END SUB

SUB ReadMode(selector)
    RETURN UO.GetStatLockState(selector)
END SUB
```

**Explicación de los parámetros y la ejecución:**

- La función completa sigue a Main. selector elige habilidad/atributo; mode indica el modo de escritura. ReadValue/ReadMode devuelven el número original; ApplyMode comprueba argumentos, actúa y no devuelve valor. WAIT(1000) separa dos lecturas.
